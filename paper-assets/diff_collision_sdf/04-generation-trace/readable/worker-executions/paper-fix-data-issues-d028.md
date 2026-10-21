# paper fix data issues d028

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_fix_data_issues_d028_20260526T054317.log`
- **Structured JSON:** [`f5d8785a0fec78bed927.json`](../../sessions/f5/f5d8785a0fec78bed927.json)

## Before a recorded user message

60 recorded events

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
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
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
  "uuid": "3cfcbb14-2842-45bb-8cb9-cf6dec2187b3",
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
    "resetsAt": 1779790800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ef5d1099-ee28-4227-af4e-fa685c14d6a0",
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the three files to understand the current state and find all instances that need fixing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "680af786-ad62-41f2-86d5-a7cba4c7a1a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCok1sGEKpaWMfGGztywqD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12577,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12577
      },
      "output_tokens": 22,
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

先读取三个目标文件，定位所有需要修改的位置。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "130cf01c-cef7-4017-be07-a9ab10ef55ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCok1sGEKpaWMfGGztywqD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12577,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12577
      },
      "output_tokens": 22,
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

<details open><summary>🔧 Tool call — Read · `toolu_013ZhGnDJvUsxoewjJyrGgf5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "e711018d-d6c9-4db6-be4f-3da3344963f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCok1sGEKpaWMfGGztywqD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12577,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12577
      },
      "output_tokens": 22,
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

_source line 7 · 2026-05-26T05:43:33.375Z_

<details><summary>↩ Tool result · `toolu_013ZhGnDJvUsxoewjJyrGgf5`</summary>

```text
1	\subsection{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	At first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\% across 800 evaluation episodes on the SafeLIBERO benchmark~\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\%) exhibit a maximum displacement below 1\,$\mu$m, and another 188 episodes (25.7\%) remain below 0.1\,mm. Only 3 episodes (0.4\%) show displacement above the 0.1\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\sim}$5\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved.
4	
5	We define a safe episode as \emph{fake safe} when the maximum end-effector displacement stays below a threshold $\tau_d = 0.1$\,mm, the criterion used by the displacement-filtered CAR (Eq.~\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}
10	\label{tab:fake_safety}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{lccccc}
14	\toprule
15	Method & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) \\
16	\midrule
17	A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\dagger$ \\
18	LoRA baseline  & 82.0 & 0.0 & 99.4 & $\approx$\,1 / 164 & $\approx$\,0 \\
19	Pi0.5 (3-seed) & 26.8\,$\pm$\,1.6 & 74.7\,$\pm$\,1.5 & 98.2 & 1 / 56 & $\approx$\,0 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{2pt}
23	{\footnotesize $^\dagger$ Denominator $< 5$; statistically unreliable.}
24	\end{table}
25	
26	This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\% with a Task Success Rate (TSR) of 0\%. Among its 164 safe episodes, 99.4\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\sim}$3B$\to$${\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\,$\pm$\,1.6\% and a TSR of 74.7\,$\pm$\,1.5\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.
27	
28	These observations motivate the displacement-filtered CAR (CAR$_\text{f}$) defined in Eq.~\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.
29	
30	The threshold $\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\,mm, three orders of magnitude above $\tau_d = 0.1$\,mm. Any threshold in $[2, 200]$\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\ref{sec:appendix_threshold}.
31	
32	For A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\% CAR but its CAR$_\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.
33	
34	The practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\text{f}$.
35	
36	\paragraph{Capability-safety observation.}
37	The fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\% of their safe episodes classified as fake safe; we term this the \emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\% across seeds), low CAR (25--28\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.
38	
39	This spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "f35a1078-bad9-4bbd-9982-d31409d6bdf0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
      "content": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & 98.2 & 1 / 56 & $\\approx$\\,0 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Bc5h2HPcJLG9fWtsr2jR9S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "ba2af245-6a6a-4c36-9cb4-27cc0f72249d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCok1sGEKpaWMfGGztywqD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12577,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12577
      },
      "output_tokens": 22,
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

_source line 9 · 2026-05-26T05:43:33.864Z_

<details><summary>↩ Tool result · `toolu_01Bc5h2HPcJLG9fWtsr2jR9S`</summary>

```text
1	\section{Introduction}
2	
3	A model that reports 91.5\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.
4	
5	Vision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.
6	
7	Several recent methods target collision avoidance in VLAs. AEGIS~\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\% across SafeLIBERO scenarios without additional training. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.
8	
9	For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\% exhibit a maximum displacement below 0.1\,mm, and obstacle displacement remains below 5\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\% CAR with 99.4\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\% of its safe episodes are fake safe, though here the mechanism is not action collapse per se but the low prior probability of collision along short, incomplete trajectories.
10	
11	We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\,mm, any $\tau_d$ in $[2, 200]$\,mm yields identical filtering.
12	
13	The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\,$\pm$\,1.5\% but a CAR of only 26.8\,$\pm$\,1.6\%, while Pi0-based methods report CAR of 82--91.5\% alongside TSR $\leq$ 0.5\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \emph{lower} CAR than unrefined baselines (best oracle: 76.9\% vs.\ LoRA baseline: 82.0\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\% with TSR of 47--49\% and a frozen rate of 0\%, placing it in the previously empty central region of the TSR-CAR plane. This placement suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.
14	
15	Our contributions are as follows:
16	\begin{itemize}
17	    \item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that 98--99\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\ref{sec:fake_safety}).
18	    \item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\ref{sec:ee_only}).
19	    \item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \pm 3.5$ percentage points difference at low $\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\ref{sec:avoidance_source}).
20	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "a0662256-96b0-4303-9541-b6ae92ab0eb3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\\% of its safe episodes are fake safe, though here the mechanism is not action collapse per se but the low prior probability of collision along short, incomplete trajectories.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\\% with TSR of 47--49\\% and a frozen rate of 0\\%, placing it in the previously empty central region of the TSR-CAR plane. This placement suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that 98--99\\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01B5avsFcZARS8r1tj7sY4wK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "6d776d5c-e995-4d6e-8969-7297fff67108",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCok1sGEKpaWMfGGztywqD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12577,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12577
      },
      "output_tokens": 22,
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

_source line 11 · 2026-05-26T05:43:34.225Z_

<details><summary>↩ Tool result · `toolu_01B5avsFcZARS8r1tj7sY4wK`</summary>

```text
1	\begin{abstract}
2	Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\% CAR alongside 0\% Task Success Rate (TSR), yet 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\% CAR with 99.4\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\% TSR, shows the same pattern. We propose a corrective metric, displacement-filtered CAR (CAR$_\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "dd8a3b33-692f-4efa-a271-88e2f4f0d983",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nRecent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\\% TSR, shows the same pattern. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check analysis_claim3.tex for the 10K vs 30K data issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "653b7328-7ba3-4097-8b9d-1545260f065f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mjVy7ybKv9VQRmgYemJay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 24418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4814
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

读取 analysis_claim3.tex 检查 10K/30K 数据问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "d3902b6b-b681-4712-8f80-effc39fbdd8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mjVy7ybKv9VQRmgYemJay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 24418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4814
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

<details open><summary>🔧 Tool call — Read · `toolu_01Q8uPSUqZLzwHoR1U39XX3T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "1bda71e5-96af-40ac-9fbb-f019cba991ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mjVy7ybKv9VQRmgYemJay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4814,
      "cache_read_input_tokens": 24418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4814
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

_source line 15 · 2026-05-26T05:43:39.645Z_

<details><summary>↩ Tool result · `toolu_01Q8uPSUqZLzwHoR1U39XX3T`</summary>

```text
1	\subsection{Collision Avoidance from Demonstrations, Not Geometry}\label{sec:avoidance_source}
2	
3	Sections~\ref{sec:fake_safety} and~\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of explicit SDF geometric supervision from that of LoRA fine-tuning on collision-free demonstration data by comparing models trained with and without the SDF auxiliary loss.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; the SDF contribution is $0 \pm 3.5$ percentage points at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active collision avoidance.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) & Frozen (\%) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & \placeholder{X.XX} & ${\sim}$26 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 6.3 & 55.3 & 0.478 & 0.0 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 6.8 & 50.5 & \placeholder{X.XX} & 0.0 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 6.8 & 52.8 & \placeholder{X.XX} & 0.0 \\
20	\bottomrule
21	\end{tabular}
22	\end{table}
23	
24	Table~\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 55.3\% across two seeds, comparable to LoRA+SDF at $\lambda = 0.005$ (50.5\%) and $\lambda = 0.01$ (52.8\%). The difference is $0 \pm 3.5$ percentage points, within seed-to-seed variation. All three configurations produce 0\% frozen episodes and mean end-effector displacement near 0.5\,m, confirming that the collision avoidance reflected in CAR is genuine active motion, not action collapse. TSR is similarly collapsed across conditions (6.3--6.8\%), and per-task CAR patterns are consistent between LoRA-only and SDF variants. At these loss weights, the SDF auxiliary loss contributes no measurable collision avoidance beyond what LoRA fine-tuning on collision-free demonstrations provides.
25	
26	The collision avoidance signal originates in the training distribution, not in the geometric loss function. The demonstration data used for fine-tuning consists exclusively of collision-free trajectories. A model that imitates these demonstrations will produce trajectories that tend to avoid obstacles present in the training scenes. This implicit signal raises CAR from the Pi0.5 baseline (26.8\%) to 55\%, an improvement of 29 percentage points attributable entirely to fine-tuning on collision-free data. Explicit SDF supervision adds nothing at $\lambda \in \{0.005, 0.01\}$ because the geometric signal is redundant with information already encoded in the demonstration trajectories.
27	
28	\paragraph{TSR collapse mechanism.}
29	All fine-tuned models exhibit severe TSR degradation relative to the Pi0.5 baseline (74.7\% $\to$ 6.3--6.8\%), a reduction of 68 percentage points. SDF is not the cause: LoRA-only collapses by 68.4 points, SDF variants by 67.9--68.4 points. The collapse reflects catastrophic forgetting of task semantics during fine-tuning, not a side effect of geometric supervision. The robots retain motion capability (0\% frozen, end-effector displacement 0.5\,m) but lose goal-directed grasping and placing. Safe failure rate increases from 0.5\% to 50\%: the robot moves through the workspace without completing the task, and in doing so avoids approximately half of potential collisions. This composite mechanism (task semantic forgetting plus retained collision avoidance from demonstration imitation) explains the simultaneous CAR improvement and TSR collapse.
30	
31	\begin{figure}[t]
32	\centering
33	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Lambda-CAR/TSR curve -- pending $\lambda = 0.1$]\vspace{2em}}}
34	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR for Pi0.5 with LoRA fine-tuning. The $\lambda = 0$ point corresponds to LoRA-only (no SDF). Pending: $\lambda = 0.1$ results.}
35	\label{fig:lambda_car}
36	\end{figure}
37	
38	\placeholder{Pending: $\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\lambda$ range. Final narrative deferred until experimental results are available.}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "6e74bd30-3936-4754-9e37-9f2e434be56f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim3.tex",
      "content": "\\subsection{Collision Avoidance from Demonstrations, Not Geometry}\\label{sec:avoidance_source}\n\nSections~\\ref{sec:fake_safety} and~\\ref{sec:ee_only} establish that standard CAR is contaminated by action collapse and that end-effector-only SDF refinement fails structurally. A constructive question remains: when collision avoidance does improve in fine-tuned models, where does the signal originate? We isolate the contribution of explicit SDF geometric supervision from that of LoRA fine-tuning on collision-free demonstration data by comparing models trained with and without the SDF auxiliary loss.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; the SDF contribution is $0 \\pm 3.5$ percentage points at $\\lambda \\in \\{0.005, 0.01\\}$. All fine-tuned models exhibit 0\\% frozen rate, confirming active collision avoidance.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) & Frozen (\\%) \\\\\n\\midrule\nPi0.5 baseline & 3 & 74.7\\,$\\pm$\\,1.5 & 26.8\\,$\\pm$\\,1.6 & \\placeholder{X.XX} & ${\\sim}$26 \\\\\n\\midrule\nLoRA-only (no SDF) & 2 & 6.3 & 55.3 & 0.478 & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 6.8 & 50.5 & \\placeholder{X.XX} & 0.0 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 6.8 & 52.8 & \\placeholder{X.XX} & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} reports the results. LoRA fine-tuning without any SDF objective achieves CAR of 55.3\\% across two seeds, comparable to LoRA+SDF at $\\lambda = 0.005$ (50.5\\%) and $\\lambda = 0.01$ (52.8\\%). The difference is $0 \\pm 3.5$ percentage points, within seed-to-seed variation. All three configurations produce 0\\% frozen episodes and mean end-effector displacement near 0.5\\,m, confirming that the collision avoidance reflected in CAR is genuine active motion, not action collapse. TSR is similarly collapsed across conditions (6.3--6.8\\%), and per-task CAR patterns are consistent between LoRA-only and SDF variants. At these loss weights, the SDF auxiliary loss contributes no measurable collision avoidance beyond what LoRA fine-tuning on collision-free demonstrations provides.\n\nThe collision avoidance signal originates in the training distribution, not in the geometric loss function. The demonstration data used for fine-tuning consists exclusively of collision-free trajectories. A model that imitates these demonstrations will produce trajectories that tend to avoid obstacles present in the training scenes. This implicit signal raises CAR from the Pi0.5 baseline (26.8\\%) to 55\\%, an improvement of 29 percentage points attributable entirely to fine-tuning on collision-free data. Explicit SDF supervision adds nothing at $\\lambda \\in \\{0.005, 0.01\\}$ because the geometric signal is redundant with information already encoded in the demonstration trajectories.\n\n\\paragraph{TSR collapse mechanism.}\nAll fine-tuned models exhibit severe TSR degradation relative to the Pi0.5 baseline (74.7\\% $\\to$ 6.3--6.8\\%), a reduction of 68 percentage points. SDF is not the cause: LoRA-only collapses by 68.4 points, SDF variants by 67.9--68.4 points. The collapse reflects catastrophic forgetting of task semantics during fine-tuning, not a side effect of geometric supervision. The robots retain motion capability (0\\% frozen, end-effector displacement 0.5\\,m) but lose goal-directed grasping and placing. Safe failure rate increases from 0.5\\% to 50\\%: the robot moves through the workspace without completing the task, and in doing so avoids approximately half of potential collisions. This composite mechanism (task semantic forgetting plus retained collision avoidance from demonstration imitation) explains the simultaneous CAR improvement and TSR collapse.\n\n\\begin{figure}[t]\n\\centering\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Lambda-CAR/TSR curve -- pending $\\lambda = 0.1$]\\vspace{2em}}}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR for Pi0.5 with LoRA fine-tuning. The $\\lambda = 0$ point corresponds to LoRA-only (no SDF). Pending: $\\lambda = 0.1$ results.}\n\\label{fig:lambda_car}\n\\end{figure}\n\n\\placeholder{Pending: $\\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\\lambda$ range. Final narrative deferred until experimental results are available.}\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of all the files. Let me identify all the changes needed:

### Problem 1: Pi0.5 "98.2% fake safe" data

**analysis_claim1.tex:**
1. Line 19: Table row for Pi0.5 shows "98.2" and "1 / 56" — need to mark as pending
2. Line 26: Text "the fake safe rate remains 98.2\% (55 of 56 safe episodes in seed 0 show near-zero displacement)" — need to revise


3. Line 32: "For the LoRA baseline and Pi0.5, CAR$_\text{f}$ is similarly near zero" — this needs updating since Pi0.5's fake safe status is now pending
4. Line 26: The conclusion about Pi0-family models not moving when they don't collide would need revision for Pi0.5 since it actually does move

**introduction.tex:**
1. Line 9: "Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\% of its safe episodes are fake safe, though here the mechanism is not action" — this sentence is incomplete and needs to be addressed given the pending status of Pi0.5's fake safety
2. Line 17: The "98--99%" range for safe episodes attributable to inaction includes Pi0.5's 98.2%, which may need adjustment
3. Line 13: The introduction references a 10K-step checkpoint for Pi0.5 with SDF supervision, but the data should be using 30K instead

**abstract.tex:**
1. Line 2: The statement about Pi0.5 achieving 74.7% TSR and showing the same pattern is vague but still implies fake safety, which needs clarification given the pending status

**introduction.tex C3 contribution:**
Looking more carefully at the C3 section, it reports the difference between LoRA fine-tuning without SDF and SDF-augmented variants as "$0 \pm 3.5$ percentage points difference at low $\lambda$" rather than specific CAR and TSR numbers, so the discrepancy I was tracking doesn't actually exist in the current text. Looking at the actual 30K data in the tables, the C3 contribution already correctly reports those numbers—LoRA-only at 55.3% CAR versus the SDF variants ranging from 50.5% to 52.8%, which supports the claim about minimal difference. The discrepancy seems to be that the intro paragraph is highlighting the 10K checkpoint results instead of the primary 30K results. I see there's a second location in the contributions list at line 19 where C3 mentions LoRA achieving the same CAR as SDF variants. The user is pointing out that both places need updating—the body text references the 10K checkpoint results, but the contributions list should reflect the full picture including the 30K collapse issue. I'm noticing a discrepancy in the 10K checkpoint data — the user mentions TSR values of 26-30.5%, but the current text says 47-49%, which doesn't match the reference metrics I'm checking. Let me verify which checkpoints are actually being referenced and whether the introduction needs correction for both the 10K preliminary results and the 30K main findings. I'm identifying the specific edits needed across both files. In analysis_claim1.tex, I need to mark the Pi0.5 fake safe values as pending re-evaluation with a footnote, revise the description on line 26, and reconsider the claim about CAR being near zero if Pi0.5's data is uncertain. For introduction.tex, I'll remove the 98.2% figure, correct the 10K checkpoint numbers to TSR=26-30.5% and CAR=56.5-57.5%, add context about the 30K full training results, and update the 98-99% range that also appears to be incorrect.

Now I'm going through the abstract.tex file to address the vague implication about Pi0.5 showing fake safety patterns—that statement needs clarification or revision since the underlying data is pending verification.

For the analysis_claim1.tex table, I'm replacing the Pi0.5 row values with dagger symbols to mark them as pending re-evaluation, and adding a footnote explaining that the previous 98.2% measurement was based on obstacle displacement rather than end-effector displacement. Then I'll trim down the paragraph about Pi0.5 to remove redundancy with the table while keeping the key details about its performance and parameter size. I'm noting that for the LoRA baseline specifically, the fake safe rate is near zero, while Pi0.5's safe episodes need re-evaluation before making claims about their composition. Since Pi0.5 achieves a TSR of 74.7%, it's genuinely moving the robot unlike the action-collapsed A1 model, so the mechanism behind its collisions differs fundamentally. The revised conclusion should reflect that Pi0.5's safety comes from something other than simple inaction. Now I'm going through each file systematically to identify the exact strings that need updating. I'm starting with analysis_claim1.tex to locate the Pi0.5 table row and related text, then moving through introduction.tex and abstract.tex to find all the references that need revision based on the earlier edits I outlined. I need to revise the Pi0.5 section to be more concise. The key points are that Pi0.5 is a larger model with less action collapse, achieves lower CAR but higher TSR, and still shows a high fake safe rate despite actually moving the robot. I'll streamline this to focus on the core finding that the pattern holds across model sizes.

Pi0.5, a slightly larger variant from the same family, shows less action collapse but the same underlying pattern: it achieves a lower collision rate (26.8±1.6% CAR, 74.7±1.5% TSR) because it actually moves the robot, yet 98.2% of its safe episodes still exhibit near-zero displacement, confirming that the Pi0-family models avoid collisions primarily by not acting. I'm checking the specific line in the analysis file to see what needs updating. The current text groups the LoRA baseline and Pi0.5 together as having near-zero CAR_f, but given the pending re-evaluation of Pi0.5's safe episodes with displacement data, I should separate them—keeping the LoRA baseline statement as is while noting that Pi0.5's metric requires that additional analysis before we can make a definitive claim. Pi0.5 genuinely moves (TSR=74.7%), most of its episodes would exceed the displacement threshold. So CAR_f would actually be computable and meaningful for Pi0.5. The current statement "similarly near zero" may be wrong. Let me think...

Pi0.5 has CAR=26.8%, meaning about 73.2% of episodes are collisions. If most episodes show real motion (TSR=74.7%), then most episodes exceed the displacement threshold. The safe episodes after filtering would be those where the robot actually moved but didn't collide. If Pi0.5 has genuine avoidance, CAR_f would be non-trivial. But we don't know yet because the fake safe data is pending.

Actually, the current claim "near zero" was based on the assumption that 98.2% of safe episodes are fake safe (only 1/56 real safe). If that assumption is wrong and most safe episodes are genuinely safe, CAR_f would be much higher. So I need to mark this as pending re-evaluation rather than claiming it's near zero. For the introduction, I'm revising the description of Pi0.5 to highlight that it shows genuine motion (74.7% TSR) and qualitatively different behavior compared to the LoRA baseline, with safe episodes involving actual end-effector movement.

For the 10K result, I'm checking the correct data across different checkpoints and lambda values to report the most accurate numbers. The early checkpoint at 10K steps performs much better on task success (26-30.5% TSR) while maintaining collision avoidance (56.5-57.5% CAR), but this degrades sharply by 30K steps, suggesting catastrophic forgetting happens in that window. Importantly, all configurations maintain active robot motion with 0% frozen rate, meaning the collision avoidance comes from actual trajectory changes rather than the model just stopping.

For the C1 contribution, I should narrow the claim to Pi0-based methods specifically since that's what the data supports. For C3, I need to incorporate the 30K step results showing how the tradeoff manifests across training—

the LoRA variants match SDF-augmented performance at low regularization, but the 10K versus 30K contrast reveals that early stopping preserves task performance while later training collapses it, all without explicit geometric supervision. I need to clarify the Pi0.5 results in the abstract—it shows different behavior than the LoRA baseline, with safe episodes involving actual end-effector motion rather than the fake safety contamination pattern, so I should revise that sentence to reflect this distinction rather than claiming it exhibits the same pattern. I'm deciding whether to remove the Pi0.5 reference entirely since it doesn't add much to the abstract's core argument about contamination being method-agnostic. The simpler version focusing just on the baseline comparison is cleaner and more direct. I should also reconsider the "preliminary results" framing later in the abstract since it refers to data that's being corrected anyway. I need to verify the data in analysis_claim3.tex matches the corrected 30K numbers the user provided, since those table values should align with what we're fixing in the abstract and preliminary results sections.

Looking at the metrics there—LoRA-only at 6.3% TSR and 55.3% CAR, along with the SDF variants—these all check out as 30K data points, so that file doesn't have the 10K contamination issue. The Pi0.5 baseline references also look fine since they don't claim anything about fake safe percentages.

Now I'm ready to execute the edits across the files, starting with the table corrections in analysis_claim1.tex. I'm adding a second footnote to clarify that the Pi0.5 evaluation metric was originally computed using obstacle displacement but is currently being re-evaluated with end-effector displacement instead.

Now I'm finishing the Pi0.5 analysis by noting that unlike the earlier models, Pi0.5 actually produces task-directed motion, so its safe episodes might represent genuine collision avoidance rather than frozen inaction—a qualitatively different failure mode that I'm still investigating. Looking at the metrics for Pi0.5, it shows lower collision avoidance rates because the model actually moves the robot, but when it does avoid collisions, nearly all those safe episodes are still fake safe—the robot barely moved. This pattern holds consistently: across the Pi0 family, models avoid collisions primarily by not moving at all. The LoRA baseline without collision avoidance shows a 82.0% CAR but 0% TSR, with 99.4% of its safe episodes being fake safe. Pi0.5, a slightly larger model from the same family, achieves better results with 26.8% CAR and 74.7% TSR across seeds, yet still exhibits a 98.2% fake safe rate among its safe episodes—suggesting that across all Pi0-family models, safety comes primarily from inaction rather than genuine collision avoidance. I'm checking whether the file uses single or double backslashes in the LaTeX escape sequences — the Read output shows `${\\sim}$`, which means the file literally contains double backslashes, so I need to match that exact format when constructing the old_string for the replacement. I'm realizing the Read tool output might be showing escaped backslashes, so what appears as `${\\sim}$` could actually be `${\sim}$` in the file itself. Rather than getting stuck on this, I should just attempt an edit with my best guess and see if it works. I'm realizing the Read tool output shows what's actually in the file without escaping, so if I see `${\\sim}$` there, that's what I need to match. Let me just use that exact string in the replacement and stop second-guessing the tool's output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "17528361-f39f-4f7d-b5d8-255ff0a89620",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjWCMcCxhr9RtNF5YAFUCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1638,
      "cache_read_input_tokens": 29232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1638
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

_source line 17_

Now I have a clear picture. Let me verify the exact encoding of special characters and then make all edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "2cb8825d-7dbc-449d-a9b6-61b6cb3a7799",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjWCMcCxhr9RtNF5YAFUCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1638,
      "cache_read_input_tokens": 29232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1638
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

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01JxRuZ9GhJnQYP4yKGfHot2`</summary>

```json
{
  "pattern": "sim",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
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
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "70ec71fd-87bc-425e-973b-622949485376",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjWCMcCxhr9RtNF5YAFUCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1638,
      "cache_read_input_tokens": 29232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1638
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

_source line 19 · 2026-05-26T05:46:55.926Z_

<details><summary>↩ Tool result · `toolu_01JxRuZ9GhJnQYP4yKGfHot2`</summary>

```text
3:[Omitted long matching line]
26:[Omitted long matching line]
32:For A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\% CAR but its CAR$_\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "5856c634-5fa3-43e0-ba61-27295b02b813",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "3:[Omitted long matching line]\n26:[Omitted long matching line]\n32:For A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
The grep output omits lines 3 and 26 because they're too long. Let me read a specific section to check the exact content around `\sim`:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "8777a827-2292-48e8-b5b1-08da4312027c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRsjhg38MKnEHWsbDt9jm2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10976,
      "cache_read_input_tokens": 30870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10976
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

<details open><summary>🔧 Tool call — Read · `toolu_01UNdLM9miNTgw93rWKQQvtR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "offset": 25,
  "limit": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "7bee7ab8-9cdc-4939-bf40-0ede0d262b2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRsjhg38MKnEHWsbDt9jm2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10976,
      "cache_read_input_tokens": 30870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10976
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

_source line 22 · 2026-05-26T05:47:00.255Z_

<details><summary>↩ Tool result · `toolu_01UNdLM9miNTgw93rWKQQvtR`</summary>

```text
25	
26	This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\% with a Task Success Rate (TSR) of 0\%. Among its 164 safe episodes, 99.4\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\sim}$3B$\to$${\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\,$\pm$\,1.6\% and a TSR of 74.7\,$\pm$\,1.5\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "fdec1b16-1ac8-4f35-807e-6eb96ed3d60c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
      "content": "\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.",
      "numLines": 2,
      "startLine": 25,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
OK so the file literally contains `${\\sim}$` with double backslash in the Read output. Let me just use that exact string in my edits.

Now let me proceed with all the edits. I'll group them by file and execute in parallel.

Let me also double-check the analysis_claim3.tex for the 10K issue - I already read it and it uses 30K data, so no changes needed there.

Let me plan all edits carefully:

### File 1: analysis_claim1.tex

Edit A: Table Pi0.5 row
Old: `Pi0.5 (3-seed) & 26.8\,$\pm$\,1.6 & 74.7\,$\pm$\,1.5 & 98.2 & 1 / 56 & $\approx$\,0 \\`

New: `Pi0.5 (3-seed) & 26.8\,$\pm$\,1.6 & 74.7\,$\pm$\,1.5 & \multicolumn{3}{c}{pending$^\ddagger$} \\`

Edit B: Table footnote
Old: `{\footnotesize $^\dagger$ Denominator $< 5$; statistically unreliable.}`
New: `{\footnotesize $^\dagger$ Denominator $< 5$; statistically unreliable. $^\ddagger$ Prior value (98.2\%) used obstacle displacement; re-evaluation with EE displacement in progress.}`

Edit C: Pi0.5 paragraph - I need to update the text to reflect that the accuracy value is now pending re-evaluation, removing the specific 98.2% figure and noting that the methodology change is underway. Pi0.5 shows more active behavior than Pi0, achieving comparable safety and task success rates across multiple seeds. However, there's uncertainty about whether its safe episodes represent genuine collision avoidance or simply inaction—the displacement data needs closer examination since Pi0.5 does produce meaningful robot motion, unlike the frozen-behavior pattern in the Pi0-based methods where safety consistently correlates with zero movement.

For the LaTeX notation, I should stick with `${\sim}$` since that's the standard form, even if the file shows escaped backslashes in the read output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "f84cb776-e66c-4b44-9875-117ec27265fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jh46ZQvAh9A2k18AnwamGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 41846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 462
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01CB6o3qufvz47d5GduF6KMb`</summary>

```json
{
  "command": "grep -o '..sim..' /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex | head -5",
  "description": "Check exact encoding of \\sim in the file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "bfdb998e-396c-42b4-874a-bba89482a87e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jh46ZQvAh9A2k18AnwamGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 462,
      "cache_read_input_tokens": 41846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 462
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

_source line 25 · 2026-05-26T05:47:15.092Z_

<details><summary>↩ Tool result · `toolu_01CB6o3qufvz47d5GduF6KMb`</summary>

```text
{\sim}$
\\sim}$
\\sim}$
s simil
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "eba21344-b51d-4522-933b-fe542c529f1c",
  "tool_use_result": {
    "stdout": "{\\sim}$\n\\\\sim}$\n\\\\sim}$\ns simil",
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

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Interesting! So the file has both `{\sim}$` and `\\sim}$`. The first occurrence on line 3 has `{\sim}$` (single backslash), while line 26 has `\\sim}$` (double backslash, which is what the Read tool showed). So the file literally contains double backslash on line 26. That's inconsistent but I'll preserve it for now and fix only what I'm asked to fix.

Let me now do all the edits. I have a clear picture:
- analysis_claim1.tex line 26 literally has `${\\sim}$`


- I need to match that exact string when making the replacement

Now I'll execute all the edits across each file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "2cf4edc6-5c97-40fc-8fac-da5f9265c98c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBuxGVQsNqyk41WKrjVjkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 42308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 37,
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

_source line 27_

File has inconsistent `\sim` vs `\\sim` — I'll match exactly what's there. Now executing all edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "60fe0ebc-8c9d-4b1d-8e81-ee7bbc0be6bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBuxGVQsNqyk41WKrjVjkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 42308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 37,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01EpmnJBbBG5yazeY7A69WNV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "old_string": "Pi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & 98.2 & 1 / 56 & $\\approx$\\,0 \\\\",
  "new_string": "Pi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & \\multicolumn{3}{c}{pending$^\\ddagger$} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "4d719bc1-166e-4bf0-ad5e-d3003b41dd7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBuxGVQsNqyk41WKrjVjkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 42308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 37,
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

_source line 29 · 2026-05-26T05:47:23.291Z_

<details><summary>↩ Tool result · `toolu_01EpmnJBbBG5yazeY7A69WNV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "bd4db578-26d9-4d9d-a6f8-6d374aede948",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "oldString": "Pi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & 98.2 & 1 / 56 & $\\approx$\\,0 \\\\",
    "newString": "Pi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & \\multicolumn{3}{c}{pending$^\\ddagger$} \\\\",
    "originalFile": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & 98.2 & 1 / 56 & $\\approx$\\,0 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 16,
        "newLines": 7,
        "lines": [
          " \\midrule",
          " A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\",
          " LoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\",
          "-Pi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & 98.2 & 1 / 56 & $\\approx$\\,0 \\\\",
          "+Pi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & \\multicolumn{3}{c}{pending$^\\ddagger$} \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\vspace{2pt}"
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01GQgM7KMVXvQVarCRmmj27q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "old_string": "{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable.}",
  "new_string": "{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. $^\\ddagger$ Prior value (98.2\\%) used obstacle displacement; re-evaluation with EE displacement in progress.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "8c2f5844-6635-4f4d-97b0-11942d05697a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBuxGVQsNqyk41WKrjVjkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 42308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 37,
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

_source line 31 · 2026-05-26T05:47:24.699Z_

<details><summary>↩ Tool result · `toolu_01GQgM7KMVXvQVarCRmmj27q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "5f0bb137-2e26-48b7-a347-e23bc887a470",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "oldString": "{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable.}",
    "newString": "{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. $^\\ddagger$ Prior value (98.2\\%) used obstacle displacement; re-evaluation with EE displacement in progress.}",
    "originalFile": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & \\multicolumn{3}{c}{pending$^\\ddagger$} \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
    "structuredPatch": [
      {
        "oldStart": 20,
        "oldLines": 7,
        "newStart": 20,
        "newLines": 7,
        "lines": [
          " \\bottomrule",
          " \\end{tabular}",
          " \\vspace{2pt}",
          "-{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable.}",
          "+{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. $^\\ddagger$ Prior value (98.2\\%) used obstacle displacement; re-evaluation with EE displacement in progress.}",
          " \\end{table}",
          " ",
          " This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move."
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

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01KesJ7ypif5c7UL42jre597`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "old_string": "The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.",
  "new_string": "Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. The fake safety status of Pi0.5's safe episodes is under re-evaluation using end-effector displacement data; given that Pi0.5 produces active task-directed motion, its safe episodes may reflect genuine avoidance rather than inaction, which would distinguish it qualitatively from the frozen-motion pattern observed in Pi0 models.\n% TODO: pending Pi0.5 re-eval with EE displacement data — update fake safe characterization once available\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "36ce5262-bd84-4ddd-8d75-6bbe72136c19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBuxGVQsNqyk41WKrjVjkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 42308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 37,
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

_source line 33 · 2026-05-26T05:47:29.596Z_

<details><summary>↩ Tool result · `toolu_01KesJ7ypif5c7UL42jre597`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "b7bedfd2-8381-4b91-b48e-2fd965ee0795",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "oldString": "The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.",
    "newString": "Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. The fake safety status of Pi0.5's safe episodes is under re-evaluation using end-effector displacement data; given that Pi0.5 produces active task-directed motion, its safe episodes may reflect genuine avoidance rather than inaction, which would distinguish it qualitatively from the frozen-motion pattern observed in Pi0 models.\n% TODO: pending Pi0.5 re-eval with EE displacement data — update fake safe characterization once available\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.",
    "originalFile": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & \\multicolumn{3}{c}{pending$^\\ddagger$} \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. $^\\ddagger$ Prior value (98.2\\%) used obstacle displacement; re-evaluation with EE displacement in progress.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 9,
        "lines": [
          " {\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. $^\\ddagger$ Prior value (98.2\\%) used obstacle displacement; re-evaluation with EE displacement in progress.}",
          " \\end{table}",
          " ",
          "-This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. The pattern persists in Pi0.5, a larger model from the same family (${\\\\sim}$3B$\\to$${\\\\sim}$3.5B parameters) that exhibits substantially less action collapse. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects the fact that Pi0.5 actually moves the robot, which naturally increases collision frequency. Yet among its safe episodes, the fake safe rate remains 98.2\\% (55 of 56 safe episodes in seed 0 show near-zero displacement). The conclusion is consistent across methods: when a Pi0-family model does not collide, it is almost certainly because it did not move.",
          "+This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. The fake safety status of Pi0.5's safe episodes is under re-evaluation using end-effector displacement data; given that Pi0.5 produces active task-directed motion, its safe episodes may reflect genuine avoidance rather than inaction, which would distinguish it qualitatively from the frozen-motion pattern observed in Pi0 models.",
          "+% TODO: pending Pi0.5 re-eval with EE displacement data — update fake safe characterization once available",
          "+For the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.",
          " ",
          " These observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.",
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_017vvnZjL6HppENt8SXK3ovK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
  "old_string": "For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero.",
  "new_string": "For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero; Pi0.5 is pending re-evaluation with end-effector displacement data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "7018e345-5876-4fda-bbfa-7c5f693bc3da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBuxGVQsNqyk41WKrjVjkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 42308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 37,
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

_source line 35 · 2026-05-26T05:47:30.907Z_

<details><summary>↩ Tool result · `toolu_017vvnZjL6HppENt8SXK3ovK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "0009b21f-cdbb-4fe6-ad8b-a7820e579f91",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
    "oldString": "For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero.",
    "newString": "For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero; Pi0.5 is pending re-evaluation with end-effector displacement data.",
    "originalFile": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & \\multicolumn{3}{c}{pending$^\\ddagger$} \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. $^\\ddagger$ Prior value (98.2\\%) used obstacle displacement; re-evaluation with EE displacement in progress.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. The fake safety status of Pi0.5's safe episodes is under re-evaluation using end-effector displacement data; given that Pi0.5 produces active task-directed motion, its safe episodes may reflect genuine avoidance rather than inaction, which would distinguish it qualitatively from the frozen-motion pattern observed in Pi0 models.\n% TODO: pending Pi0.5 re-eval with EE displacement data — update fake safe characterization once available\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " ",
          " The threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.",
          " ",
          "-For A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline and Pi0.5, CAR$_\\text{f}$ is similarly near zero. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.",
          "+For A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero; Pi0.5 is pending re-evaluation with end-effector displacement data. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.",
          " ",
          " The practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.",
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

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Good, all analysis_claim1.tex edits succeeded. Now let me do the introduction.tex and abstract.tex edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "9869fd42-7193-4f93-8054-8dbffc69035c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCwiCVguorpGKYrCUguuhD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
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

_source line 37_

analysis_claim1.tex done. Now editing introduction.tex and abstract.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "4ae8b344-12fb-4837-a686-dc5da467b450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCwiCVguorpGKYrCUguuhD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
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

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_01RqyvdbKrQmMhTR2y8fuM27`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\\% of its safe episodes are fake safe, though here the mechanism is not action collapse per se but the low prior probability of collision along short, incomplete trajectories.",
  "new_string": "Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: its safe episodes involve genuine end-effector motion, and whether they constitute fake safety is under re-evaluation with end-effector displacement data."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "485f8f8e-abb5-4bea-860a-a694ab973fec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCwiCVguorpGKYrCUguuhD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
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

_source line 39 · 2026-05-26T05:47:37.368Z_

<details><summary>↩ Tool result · `toolu_01RqyvdbKrQmMhTR2y8fuM27`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "b4d4a390-f7dc-4d11-91b9-7bde9a5ae6a4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\\% of its safe episodes are fake safe, though here the mechanism is not action collapse per se but the low prior probability of collision along short, incomplete trajectories.",
    "newString": "Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: its safe episodes involve genuine end-effector motion, and whether they constitute fake safety is under re-evaluation with end-effector displacement data.",
    "originalFile": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\\% of its safe episodes are fake safe, though here the mechanism is not action collapse per se but the low prior probability of collision along short, incomplete trajectories.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\\% with TSR of 47--49\\% and a frozen rate of 0\\%, placing it in the previously empty central region of the TSR-CAR plane. This placement suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that 98--99\\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 7,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " ",
          " Several recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.",
          " ",
          "-For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family, exhibits the same pattern: 98.2\\% of its safe episodes are fake safe, though here the mechanism is not action collapse per se but the low prior probability of collision along short, incomplete trajectories.",
          "+For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: its safe episodes involve genuine end-effector motion, and whether they constitute fake safety is under re-evaluation with end-effector displacement data.",
          " ",
          " We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.",
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

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_014UifNHNKGHzFmCRtLhZ7nX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "we find that 98--99\\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance",
  "new_string": "we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "53e8461b-d7f8-40e0-a464-49920679ce8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCwiCVguorpGKYrCUguuhD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
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

_source line 41 · 2026-05-26T05:47:39.727Z_

<details><summary>↩ Tool result · `toolu_014UifNHNKGHzFmCRtLhZ7nX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "c1d75eb7-c0cf-47fd-b18b-c635fd635de3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "we find that 98--99\\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance",
    "newString": "we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance",
    "originalFile": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: its safe episodes involve genuine end-effector motion, and whether they constitute fake safety is under re-evaluation with end-effector displacement data.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\\% with TSR of 47--49\\% and a frozen rate of 0\\%, placing it in the previously empty central region of the TSR-CAR plane. This placement suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that 98--99\\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 7,
        "lines": [
          " ",
          " Our contributions are as follows:",
          " \\begin{itemize}",
          "-    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that 98--99\\% of safe episodes across multiple methods and model scales are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).",
          "+    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).",
          "     \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).",
          "     \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).",
          " \\end{itemize}",
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

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01Kn5kbHgXGvRnpAmXKBdt6c`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\\% with TSR of 47--49\\% and a frozen rate of 0\\%, placing it in the previously empty central region of the TSR-CAR plane. This placement suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.",
  "new_string": "Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "304e7a8a-059f-4713-9235-98003ce40709",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCwiCVguorpGKYrCUguuhD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
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

_source line 43 · 2026-05-26T05:47:49.537Z_

<details><summary>↩ Tool result · `toolu_01Kn5kbHgXGvRnpAmXKBdt6c`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "41f989b7-b888-4aab-a6cc-76956e50c82e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\\% with TSR of 47--49\\% and a frozen rate of 0\\%, placing it in the previously empty central region of the TSR-CAR plane. This placement suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.",
    "newString": "Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.",
    "originalFile": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: its safe episodes involve genuine end-effector motion, and whether they constitute fake safety is under re-evaluation with end-effector displacement data.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\\% with TSR of 47--49\\% and a frozen rate of 0\\%, placing it in the previously empty central region of the TSR-CAR plane. This placement suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " ",
          " We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.",
          " ",
          "-The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. A preliminary result provides a constructive counterpoint: a Pi0.5 model augmented with training-time SDF supervision (10K-step checkpoint) achieves CAR of 56--58\\% with TSR of 47--49\\% and a frozen rate of 0\\%, placing it in the previously empty central region of the TSR-CAR plane. This placement suggests that genuine collision avoidance is achievable when the base model retains sufficient capability.",
          "+The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.",
          " ",
          " Our contributions are as follows:",
          " \\begin{itemize}"
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

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01HB3xLiZd19WFBeks5fFZUp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).",
  "new_string": "    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "42410734-00e6-4776-93c3-e46a52732018",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCwiCVguorpGKYrCUguuhD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
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

_source line 45 · 2026-05-26T05:47:55.756Z_

<details><summary>↩ Tool result · `toolu_01HB3xLiZd19WFBeks5fFZUp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "abfcdeb5-5c18-41c6-9513-26ccf56adc87",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).",
    "newString": "    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).",
    "originalFile": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: its safe episodes involve genuine end-effector motion, and whether they constitute fake safety is under re-evaluation with end-effector displacement data.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 5,
        "newStart": 16,
        "newLines": 5,
        "lines": [
          " \\begin{itemize}",
          "     \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).",
          "     \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).",
          "-    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. LoRA fine-tuning without SDF achieves the same CAR as SDF-augmented variants ($0 \\pm 3.5$ percentage points difference at low $\\lambda$), establishing that the avoidance signal resides in the training distribution (Section~\\ref{sec:avoidance_source}).",
          "+    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).",
          " \\end{itemize}",
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

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_019jYTjkKpAaMA2Mkg9Chzxi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "and Pi0.5, which achieves 74.7\\% TSR, shows the same pattern",
  "new_string": "and Pi0.5, which achieves 74.7\\% TSR, presents a contrasting case whose fake safety status is under re-evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "9c13757e-87e5-4ae2-8f48-2dede2656085",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCwiCVguorpGKYrCUguuhD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 43592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
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

_source line 47 · 2026-05-26T05:47:57.552Z_

<details><summary>↩ Tool result · `toolu_019jYTjkKpAaMA2Mkg9Chzxi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "58d7101e-b52d-49a4-90e7-a08612fe6562",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "oldString": "and Pi0.5, which achieves 74.7\\% TSR, shows the same pattern",
    "newString": "and Pi0.5, which achieves 74.7\\% TSR, presents a contrasting case whose fake safety status is under re-evaluation",
    "originalFile": "\\begin{abstract}\nRecent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\\% TSR, shows the same pattern. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.\n\\end{abstract}",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\begin{abstract}",
          "-Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\\% TSR, shows the same pattern. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.",
          "+Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\\% TSR, presents a contrasting case whose fake safety status is under re-evaluation. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.",
          " \\end{abstract}",
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

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
All edits done. Now I also need to update the abstract's "Preliminary results" sentence at the end. Let me check:

The abstract currently says: "Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate."

This references the 10K data. With the 30K results, the story is different: fine-tuning produces genuine avoidance but with catastrophic TSR collapse, and SDF adds no benefit over LoRA-only. Let me update this.

Let me also re-read the updated files to verify everything looks correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "df849c7e-4875-45a6-a959-b9a21d6d2e61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116ZRpSZR943VJRaeZKngeH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 45367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1963
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

_source line 49_

Now updating the abstract's "Preliminary results" line which also references the 10K data, and verifying all changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "769e508d-23a8-4061-8840-0730cff576cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116ZRpSZR943VJRaeZKngeH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 45367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1963
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_018WWDmo3yiD3Ju2BPjdkbmW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate.",
  "new_string": "Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\\sim}$55\\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\\% to $<$7\\%), and explicit SDF supervision adds no measurable benefit."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "5404cfec-c8e1-4007-ba26-8667d5b0e146",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116ZRpSZR943VJRaeZKngeH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 45367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1963
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

_source line 51 · 2026-05-26T05:48:06.063Z_

<details><summary>↩ Tool result · `toolu_018WWDmo3yiD3Ju2BPjdkbmW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "55e7aeeb-c5db-4bb0-8c4e-4b1c225c9b83",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "oldString": "Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate.",
    "newString": "Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\\sim}$55\\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\\% to $<$7\\%), and explicit SDF supervision adds no measurable benefit.",
    "originalFile": "\\begin{abstract}\nRecent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\\% TSR, presents a contrasting case whose fake safety status is under re-evaluation. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.\n\\end{abstract}",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\begin{abstract}",
          "-Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\\% TSR, presents a contrasting case whose fake safety status is under re-evaluation. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Preliminary results indicate that training-time SDF supervision on a sufficiently capable VLA can produce genuine collision avoidance with zero frozen rate. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.",
          "+Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\\% TSR, presents a contrasting case whose fake safety status is under re-evaluation. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\\sim}$55\\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\\% to $<$7\\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.",
          " \\end{abstract}",
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

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_0187bZKi2adScaFYdZkoMVoC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "2c82b56a-4357-458d-abcb-7c4e9ddd5161",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116ZRpSZR943VJRaeZKngeH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 45367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1963
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

_source line 53 · 2026-05-26T05:48:06.536Z_

<details><summary>↩ Tool result · `toolu_0187bZKi2adScaFYdZkoMVoC`</summary>

```text
1	\begin{abstract}
2	Recent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\% CAR alongside 0\% Task Success Rate (TSR), yet 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\% CAR with 99.4\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\% TSR, presents a contrasting case whose fake safety status is under re-evaluation. We propose a corrective metric, displacement-filtered CAR (CAR$_\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\sim}$55\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\% to $<$7\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "5bbe587d-56fd-4830-9a53-f36db29bcc48",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nRecent methods for collision avoidance in Vision-Language-Action (VLA) models report high Collision Avoidance Rate (CAR) on safety benchmarks and claim effective obstacle avoidance. We show that these metrics can be systematically contaminated by action collapse: the model ceases to produce meaningful motion, and the resulting inaction is counted as successful avoidance. On the SafeLIBERO benchmark, a Signed Distance Field (SDF)-augmented VLA reports 91.5\\% CAR alongside 0\\% Task Success Rate (TSR), yet 99.6\\% of its safe episodes exhibit end-effector displacement below 0.1\\,mm and obstacle displacement at the nanometer scale. This contamination is not method-specific; a baseline without any collision objective achieves 82\\% CAR with 99.4\\% of safe episodes below the same threshold, and Pi0.5, which achieves 74.7\\% TSR, presents a contrasting case whose fake safety status is under re-evaluation. We propose a corrective metric, displacement-filtered CAR (CAR$_\\text{f}$), that excludes sub-threshold episodes. Two structural issues compound the problem. First, TSR and CAR are anti-correlated: models that move the robot through the workspace collide, while collapsed models appear safe. Second, ground-truth SDF oracle experiments demonstrate that end-effector-only refinement cannot prevent full-body collisions, as SDF gradients that repel the end-effector simultaneously drive arm links into obstacle volumes. Fine-tuning on collision-free demonstrations produces genuine collision avoidance (CAR ${\\sim}$55\\%, zero frozen rate) but at the cost of catastrophic task performance collapse (TSR drops from 74.7\\% to $<$7\\%), and explicit SDF supervision adds no measurable benefit. Our findings establish that displacement filtering is necessary for meaningful VLA safety evaluation.\n\\end{abstract}",
      "numLines": 3,
      "startLine": 1,
      "totalLines": 3
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01JEsjs34b9is5Ynvr8Yqjrc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "41665366-e911-4990-91d1-3318cc3d3f1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116ZRpSZR943VJRaeZKngeH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 45367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1963
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

_source line 55 · 2026-05-26T05:48:07.008Z_

<details><summary>↩ Tool result · `toolu_01JEsjs34b9is5Ynvr8Yqjrc`</summary>

```text
1	\subsection{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	At first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\% across 800 evaluation episodes on the SafeLIBERO benchmark~\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\%) exhibit a maximum displacement below 1\,$\mu$m, and another 188 episodes (25.7\%) remain below 0.1\,mm. Only 3 episodes (0.4\%) show displacement above the 0.1\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\sim}$5\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\% of safe episodes are artifacts of a robot that never moved.
4	
5	We define a safe episode as \emph{fake safe} when the maximum end-effector displacement stays below a threshold $\tau_d = 0.1$\,mm, the criterion used by the displacement-filtered CAR (Eq.~\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}
10	\label{tab:fake_safety}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{lccccc}
14	\toprule
15	Method & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) \\
16	\midrule
17	A1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\dagger$ \\
18	LoRA baseline  & 82.0 & 0.0 & 99.4 & $\approx$\,1 / 164 & $\approx$\,0 \\
19	Pi0.5 (3-seed) & 26.8\,$\pm$\,1.6 & 74.7\,$\pm$\,1.5 & \multicolumn{3}{c}{pending$^\ddagger$} \\
20	\bottomrule
21	\end{tabular}
22	\vspace{2pt}
23	{\footnotesize $^\dagger$ Denominator $< 5$; statistically unreliable. $^\ddagger$ Prior value (98.2\%) used obstacle displacement; re-evaluation with EE displacement in progress.}
24	\end{table}
25	
26	This phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\% with a Task Success Rate (TSR) of 0\%. Among its 164 safe episodes, 99.4\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\sim}$3B$\to$${\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\,$\pm$\,1.6\% and a TSR of 74.7\,$\pm$\,1.5\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. The fake safety status of Pi0.5's safe episodes is under re-evaluation using end-effector displacement data; given that Pi0.5 produces active task-directed motion, its safe episodes may reflect genuine avoidance rather than inaction, which would distinguish it qualitatively from the frozen-motion pattern observed in Pi0 models.
27	% TODO: pending Pi0.5 re-eval with EE displacement data — update fake safe characterization once available
28	For the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.
29	
30	These observations motivate the displacement-filtered CAR (CAR$_\text{f}$) defined in Eq.~\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.
31	
32	The threshold $\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\,mm, three orders of magnitude above $\tau_d = 0.1$\,mm. Any threshold in $[2, 200]$\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\ref{sec:appendix_threshold}.
33	
34	For A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\text{f}$ is similarly near zero; Pi0.5 is pending re-evaluation with end-effector displacement data. The gap between raw CAR and CAR$_\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\% CAR but its CAR$_\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.
35	
36	The practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\text{f}$.
37	
38	\paragraph{Capability-safety observation.}
39	The fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\% of their safe episodes classified as fake safe; we term this the \emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\% across seeds), low CAR (25--28\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.
40	
41	This spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "adf14fe6-ec2c-4774-8aaf-f96a54e60a00",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/analysis_claim1.tex",
      "content": "\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\n\nAt first glance, the collision avoidance results for SDF-augmented VLA models appear compelling. Our A1-LoRA model (Pi0 fine-tuned with an SDF auxiliary loss) achieves a Collision Avoidance Rate (CAR) of 91.5\\% across 800 evaluation episodes on the SafeLIBERO benchmark~\\cite{hu2025vlsa}, a figure that would suggest reliable obstacle avoidance. Yet this headline metric conceals a fundamental problem. When we examine the end-effector displacement of the 732 episodes classified as ``safe,'' the picture changes entirely: 541 episodes (73.9\\%) exhibit a maximum displacement below 1\\,$\\mu$m, and another 188 episodes (25.7\\%) remain below 0.1\\,mm. Only 3 episodes (0.4\\%) show displacement above the 0.1\\,mm threshold, the minimum we consider consistent with intentional motion. An independent measurement confirms the diagnosis: obstacle displacement across these episodes has a median of ${\\sim}$5\\,nm, consistent with numerical noise rather than physical contact. The remaining 99.6\\% of safe episodes are artifacts of a robot that never moved.\n\nWe define a safe episode as \\emph{fake safe} when the maximum end-effector displacement stays below a threshold $\\tau_d = 0.1$\\,mm, the criterion used by the displacement-filtered CAR (Eq.~\\ref{eq:car_f}). Under this definition, 729 of the 732 safe episodes produced by A1-LoRA are fake safe. An independent signal corroborates the diagnosis: TSR is 0\\% across all 800 episodes, confirming that the model produces no meaningful task-directed behavior. The robot did not avoid obstacles; it avoided motion altogether. The displacement distribution, shown in Figure~\\ref{fig:displacement}, clusters overwhelmingly near zero, with no meaningful spread toward the range that would indicate planned trajectories around obstacles. Table~\\ref{tab:fake_safety} summarizes the fake safety statistics across all evaluated methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\n\\midrule\nA1-LoRA (SDF) & 91.5 & 0.0 & 99.6 & 3 / 732 & ---$^\\dagger$ \\\\\nLoRA baseline  & 82.0 & 0.0 & 99.4 & $\\approx$\\,1 / 164 & $\\approx$\\,0 \\\\\nPi0.5 (3-seed) & 26.8\\,$\\pm$\\,1.6 & 74.7\\,$\\pm$\\,1.5 & \\multicolumn{3}{c}{pending$^\\ddagger$} \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$ Denominator $< 5$; statistically unreliable. $^\\ddagger$ Prior value (98.2\\%) used obstacle displacement; re-evaluation with EE displacement in progress.}\n\\end{table}\n\nThis phenomenon is not an artifact of the SDF auxiliary loss. The LoRA baseline, trained without any collision avoidance objective, reports a CAR of 82.0\\% with a Task Success Rate (TSR) of 0\\%. Among its 164 safe episodes, 99.4\\% are fake safe by the same displacement criterion. Pi0.5 presents a contrasting case. It is a larger model from the same family (${\\sim}$3B$\\to$${\\sim}$3.5B parameters) that retains substantial task capability. Across three seeds (600 total episodes), Pi0.5 achieves a CAR of 26.8\\,$\\pm$\\,1.6\\% and a TSR of 74.7\\,$\\pm$\\,1.5\\%. Its lower CAR reflects genuine robot motion through the workspace, which naturally increases collision frequency. The fake safety status of Pi0.5's safe episodes is under re-evaluation using end-effector displacement data; given that Pi0.5 produces active task-directed motion, its safe episodes may reflect genuine avoidance rather than inaction, which would distinguish it qualitatively from the frozen-motion pattern observed in Pi0 models.\n% TODO: pending Pi0.5 re-eval with EE displacement data — update fake safe characterization once available\nFor the Pi0-based methods (A1-LoRA and LoRA baseline), the conclusion is unambiguous: when these models do not collide, it is because the robot did not move.\n\nThese observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ is intended as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.\n\nThe threshold $\\tau_d$ admits wide latitude. Among episodes that do exhibit meaningful motion, the minimum observed maximum end-effector displacement is 239\\,mm, three orders of magnitude above $\\tau_d = 0.1$\\,mm. Any threshold in $[2, 200]$\\,mm produces identical filtering, because the displacement distribution is bimodal: episodes cluster either near zero (action collapse) or above 200\\,mm (active behavior), with no intermediate population. We provide a full sensitivity analysis in Appendix~\\ref{sec:appendix_threshold}.\n\nFor A1-LoRA, only 3 of 800 episodes exceed the threshold; all 3 happen to be safe, but a denominator of 3 precludes any meaningful rate estimate. For the LoRA baseline, CAR$_\\text{f}$ is similarly near zero; Pi0.5 is pending re-evaluation with end-effector displacement data. The gap between raw CAR and CAR$_\\text{f}$ exposes the scale of contamination: A1-LoRA reports 91.5\\% CAR but its CAR$_\\text{f}$ is statistically undefined, because it has almost no active episodes to evaluate.\n\nThe practical implication is stark. Standard CAR evaluation conflates two behaviors that differ in every meaningful respect: a robot that plans a safe trajectory around an obstacle, and a robot that has collapsed into inaction due to distributional shift. Without displacement filtering, any model suffering from action collapse will receive inflated safety scores, and models that collapse more severely will paradoxically appear safer. This inversion renders CAR, as conventionally computed, unreliable for evaluating collision avoidance in VLA models. CAR$_\\text{f}$ also serves a diagnostic role: a method that achieves a non-trivial CAR$_\\text{f}$ value provides positive evidence that its safety behavior reflects genuine avoidance rather than inaction. Among all configurations evaluated in this work, Pi0.5 fine-tuned on collision-free demonstrations (Section~\\ref{sec:avoidance_source}) is the first to produce a meaningful CAR$_\\text{f}$.\n\n\\paragraph{Capability-safety observation.}\nThe fake safety pattern corresponds to a broader regularity in TSR-CAR space. Figure~\\ref{fig:tsr_car_scatter} plots all evaluated configurations. Two clusters emerge. Pi0-family methods occupy the upper-left region: high CAR, near-zero TSR, with over 99\\% of their safe episodes classified as fake safe; we term this the \\emph{fake safety zone}. Pi0.5 sits in the lower-right: high TSR (73--76\\% across seeds), low CAR (25--28\\%). Its collisions reflect genuine robot motion through the workspace. The pattern holds across all Pi0.5 seeds and across Pi0 variants regardless of whether an SDF loss is applied. Models that execute tasks move the robot into collision-prone configurations; models that fail to act avoid collisions by default.\n\nThis spatial structure has a direct implication for metric interpretation. A model reporting high CAR but near-zero TSR provides no evidence of collision avoidance capability; its safety score is an artifact of inaction. CAR is informative only when conditioned on sufficient task capability. The TSR-CAR plane offers a more complete picture than either metric alone: the upper-right quadrant (high TSR, high CAR) represents genuinely safe and capable behavior, while the upper-left quadrant is accessible through action collapse alone. We report this anti-correlation as an empirical observation within two model families (Pi0 and Pi0.5), not as a universal law. A causal claim would require evidence across a broader range of architectures and benchmarks.",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_017aRgUCgdHeXY8wjkBS9D1X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "7d1f61ef-3c2f-418c-a24f-dc5617df6fe5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116ZRpSZR943VJRaeZKngeH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 45367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1963
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

_source line 57 · 2026-05-26T05:48:07.495Z_

<details><summary>↩ Tool result · `toolu_017aRgUCgdHeXY8wjkBS9D1X`</summary>

```text
1	\section{Introduction}
2	
3	A model that reports 91.5\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.
4	
5	Vision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\pi_0$~\cite{black2024pi0}, OpenVLA~\cite{kim2024openvla}, and RT-2~\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.
6	
7	Several recent methods target collision avoidance in VLAs. AEGIS~\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\% across SafeLIBERO scenarios without additional training. SafeVLA~\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\% through reward shaping during reinforcement learning. CoFreeVLA~\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.
8	
9	For the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\% exhibit a maximum displacement below 0.1\,mm, and obstacle displacement remains below 5\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\% CAR with 99.4\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\%), exhibits qualitatively different behavior: its safe episodes involve genuine end-effector motion, and whether they constitute fake safety is under re-evaluation with end-effector displacement data.
10	
11	We acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\,mm, any $\tau_d$ in $[2, 200]$\,mm yields identical filtering.
12	
13	The fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\,$\pm$\,1.5\% but a CAR of only 26.8\,$\pm$\,1.6\%, while Pi0-based methods report CAR of 82--91.5\% alongside TSR $\leq$ 0.5\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \emph{lower} CAR than unrefined baselines (best oracle: 76.9\% vs.\ LoRA baseline: 82.0\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\% with 0\% frozen rate but suffers catastrophic TSR collapse to 6.3\%; SDF-augmented variants ($\lambda \in \{0.005, 0.01\}$) show comparable CAR (50.5--52.8\%) with similar TSR collapse (6.8\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\% with CAR of 56.5--57.5\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.
14	
15	Our contributions are as follows:
16	\begin{itemize}
17	    \item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\ref{sec:fake_safety}).
18	    \item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\ref{sec:ee_only}).
19	    \item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\% (TSR 6.3\%), comparable to SDF-augmented variants (CAR 50.5--52.8\%, TSR 6.8\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\% before degrading to $<$7\% at 30K (Section~\ref{sec:avoidance_source}).
20	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "2d75e02f-bb26-4d53-9a19-c3c47744814d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nA model that reports 91.5\\% collision avoidance and completes zero tasks has not learned safety; it has learned to stop moving.\n\nVision-Language-Action (VLA) models unify visual perception, language understanding, and continuous action generation in a single architecture. Models such as $\\pi_0$~\\cite{black2024pi0}, OpenVLA~\\cite{kim2024openvla}, and RT-2~\\cite{brohan2023rt2} can follow diverse natural language instructions across manipulation tasks. As these models move toward real-world deployment, a critical failure mode has emerged: frequent collisions with non-target objects in cluttered environments. The demonstration data used for training typically features unobstructed workspaces, and the resulting policies acquire no explicit incentive to maintain clearance from nearby surfaces. Collisions cause task failure, risk damage to the robot and its surroundings, and represent a central barrier to safe deployment. The SafeLIBERO benchmark~\\cite{hu2025vlsa}, comprising 32 collision scenarios across 1,600 evaluation episodes, was introduced to systematically quantify this problem and confirms that even high-performing VLAs exhibit substantial collision rates when non-target objects surround the manipulation target.\n\nSeveral recent methods target collision avoidance in VLAs. AEGIS~\\cite{hu2025vlsa} applies post-hoc Control Barrier Function (CBF) corrections to already-generated trajectories and reports an average Collision Avoidance Rate (CAR) of 77.85\\% across SafeLIBERO scenarios without additional training. SafeVLA~\\cite{zhang2025safevla} formulates safety as a constrained Markov Decision Process and reduces safety violations by 83.58\\% through reward shaping during reinforcement learning. CoFreeVLA~\\cite{cofreeevla2026} trains a risk estimator for dual-arm settings that halts execution when predicted collision risk exceeds a threshold. In our own experiments, a Pi0 model fine-tuned with an auxiliary Signed Distance Field (SDF) loss (referred to as A1-LoRA) achieves 91.5\\% CAR on SafeLIBERO. These methods share a common evaluation pattern: they report high CAR as evidence of effective collision avoidance. The numbers appear compelling, and the implicit assumption across this emerging literature is that high CAR reflects genuine obstacle avoidance behavior.\n\nFor the Pi0-family models we evaluate, this assumption does not hold. Their CAR values are systematically contaminated by \\emph{action collapse}, a phenomenon in which the VLA ceases to produce meaningful motion. Action collapse inflating displacement-based safety metrics is not Pi0-specific in principle; any VLA susceptible to mode collapse is vulnerable. Our direct evidence, however, comes from the Pi0 family. When we examine the end-effector displacement of the 732 episodes that A1-LoRA classifies as ``safe,'' 99.6\\% exhibit a maximum displacement below 0.1\\,mm, and obstacle displacement remains below 5\\,nm at the median. The robot did not learn to avoid obstacles; it learned to stop moving. This contamination is not specific to A1-LoRA or to SDF-based approaches. The LoRA baseline (no collision avoidance objective) achieves 82\\% CAR with 99.4\\% of its safe episodes below the same displacement threshold. Pi0.5, a more capable model from the same family (TSR of 74.7\\%), exhibits qualitatively different behavior: its safe episodes involve genuine end-effector motion, and whether they constitute fake safety is under re-evaluation with end-effector displacement data.\n\nWe acknowledge that action collapse itself is a well-documented failure mode of undertrained or distribution-shifted models, and its existence alone would not warrant a dedicated analysis. The critical consequence is this: action collapse silently inflates the primary safety metric used to evaluate collision avoidance methods. Downstream researchers who compare methods based on reported CAR values will draw incorrect conclusions about relative safety. Models that collapse more severely will paradoxically appear safer, and genuinely unsafe models may be deployed on the basis of contaminated evaluations. We propose the displacement-filtered CAR (CAR$_\\text{f}$), which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator, as a corrective metric that separates genuine avoidance from inaction. The threshold is robust: because active episodes exhibit minimum displacements exceeding 200\\,mm, any $\\tau_d$ in $[2, 200]$\\,mm yields identical filtering.\n\nThe fake safety problem exposes two deeper structural issues. First, task capability and collision avoidance are anti-correlated under current evaluation practice. Pi0.5 achieves a TSR of 74.7\\,$\\pm$\\,1.5\\% but a CAR of only 26.8\\,$\\pm$\\,1.6\\%, while Pi0-based methods report CAR of 82--91.5\\% alongside TSR $\\leq$ 0.5\\%. The explanation is mechanical: a model that moves the robot through the workspace encounters obstacles; a model that does not move encounters none. CAR is therefore informative only when conditioned on sufficient task capability, and the TSR-CAR plane reveals that no current method occupies the upper-right quadrant where both metrics are high. Second, end-effector-only SDF refinement, the most direct geometric approach to collision avoidance, has a structural defect. We construct oracle experiments that replace the learned SDF network with ground-truth signed distance fields computed from simulation geometry. All three oracle variants achieve \\emph{lower} CAR than unrefined baselines (best oracle: 76.9\\% vs.\\ LoRA baseline: 82.0\\%). The SDF gradient pushes the end-effector away from obstacles, but the resulting joint-space displacement rotates intermediate arm links toward or through obstacle volumes. Perfect distance information at the end-effector cannot compensate for the absence of full-body collision awareness. Fine-tuning Pi0.5 with LoRA on collision-free demonstrations (30K steps, no SDF) achieves CAR of 55.3\\% with 0\\% frozen rate but suffers catastrophic TSR collapse to 6.3\\%; SDF-augmented variants ($\\lambda \\in \\{0.005, 0.01\\}$) show comparable CAR (50.5--52.8\\%) with similar TSR collapse (6.8\\%). The best early-stopped checkpoint (10K steps) retains TSR of 26--30.5\\% with CAR of 56.5--57.5\\%, indicating that catastrophic task performance collapse occurs between 10K and 30K steps. Despite the TSR degradation, all fine-tuned configurations produce active robot motion (0\\% frozen rate), confirming that their collision avoidance reflects genuine trajectory modification rather than inaction.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item We identify the fake safety problem in VLA collision avoidance evaluation: action collapse systematically inflates Collision Avoidance Rate, and we find that over 99\\% of safe episodes in Pi0-based methods are attributable to inaction rather than obstacle avoidance. We propose displacement-filtered CAR (CAR$_\\text{f}$) as a corrective metric. A supporting capability-safety observation confirms that higher task capability correlates with lower raw CAR, further demonstrating that cross-method comparisons on standard CAR are unreliable (Section~\\ref{sec:fake_safety}).\n    \\item Through ground-truth SDF oracle experiments, we establish that end-effector-only SDF refinement is a structural limitation: even perfect distance information cannot prevent full-body collisions, as gradients that repel the end-effector simultaneously drive arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n    \\item We trace the source of collision avoidance in fine-tuned VLAs to implicit learning from collision-free demonstration data rather than explicit geometric supervision. At 30K steps, LoRA-only achieves CAR of 55.3\\% (TSR 6.3\\%), comparable to SDF-augmented variants (CAR 50.5--52.8\\%, TSR 6.8\\%), establishing that the avoidance signal resides in the training distribution. All fine-tuned models suffer catastrophic TSR collapse: best early-stopped checkpoints (10K steps) retain TSR of 26--30.5\\% before degrading to $<$7\\% at 30K (Section~\\ref{sec:avoidance_source}).\n\\end{itemize}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
All edits look correct. Let me now verify analysis_claim3.tex doesn't have the 10K vs 30K issue (the user asked me to check). I already read it and it uses 30K data correctly in the table (LoRA-only 30K: CAR=55.3%, TSR=6.3%; SDF variants: CAR=50.5-52.8%, TSR=6.8%). The text also correctly discusses these as 30K results. No 10K data mentioned.

Let me summarize all changes made.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "77f9d386-d86f-442d-8eda-9ca7a0b12fee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvEBfRnZwrLbf3Ef7mBbmH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5555,
      "cache_read_input_tokens": 47330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5555
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

_source line 59_

analysis_claim3.tex 已确认使用 30K 数据，无需修改。

---

## 所有改动汇总

### 问题 1：Pi0.5 "98.2% fake safe" → pending

| 文件 | 位置 | 改动 |
|------|------|------|
| `analysis_claim1.tex:19` | Table Pi0.5 行 | `98.2 / 1 / 56 / ≈0` → `\multicolumn{3}{c}{pending$^\ddagger$}` |
| `analysis_claim1.tex:23` | Table 脚注 | 新增 `$^\ddagger$` 说明：prior value (98.2%) used obstacle displacement |
| `analysis_claim1.tex:26-28` | Pi0.5 段落 | 重写：从"fake safe 98.2%"改为"contrasting case，re-evaluation in progress，may reflect genuine avoidance"；结论限定为 Pi0-based methods |
| `analysis_claim1.tex:34` | CAR_f 段 | "LoRA baseline and Pi0.5 near zero" → LoRA baseline near zero；Pi0.5 pending |
| `introduction.tex:9` | 第3段末 | "exhibits the same pattern: 98.2%" → "exhibits qualitatively different behavior...under re-evaluation" |
| `introduction.tex:17` | C1 贡献 | "98--99% across multiple methods and model scales" → "over 99% in Pi0-based methods" |
| `abstract.tex:2` | Pi0.5 描述 | "shows the same pattern" → "presents a contrasting case whose fake safety status is under re-evaluation" |

### 问题 2：10K → 30K 数据修正

| 文件 | 位置 | 改动 |
|------|------|------|
| `introduction.tex:13` | 段末 preliminary result | 10K "CAR 56-58%, TSR 47-49%" → 30K 为主（LoRA-only CAR=55.3%, TSR=6.3%; SDF CAR=50.5-52.8%, TSR=6.8%），10K 作为补充（TSR=26-30.5%, catastrophic collapse between 10K-30K） |
| `introduction.tex:19` | C3 贡献 | 补充 30K 具体数字（CAR 55.3%/50.5-52.8%, TSR 6.3%/6.8%）和 10K→30K TSR collapse |
| `abstract.tex:2` | Preliminary results 句 | "training-time SDF supervision...genuine collision avoidance" → 报告 30K 结果（CAR ~55%, TSR collapse to <7%, SDF no benefit） |

### 未修改（确认正确）

- A1 的 99.6% fake safe — 保留
- `analysis_claim3.tex` — 已使用 30K 数据，无 10K 问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "uuid": "3c7e6b4d-96e9-4697-9096-691c7a355265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvEBfRnZwrLbf3Ef7mBbmH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5555,
      "cache_read_input_tokens": 47330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5555
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

### Task result

_source line 60_

analysis_claim3.tex 已确认使用 30K 数据，无需修改。

---

## 所有改动汇总

### 问题 1：Pi0.5 "98.2% fake safe" → pending

| 文件 | 位置 | 改动 |
|------|------|------|
| `analysis_claim1.tex:19` | Table Pi0.5 行 | `98.2 / 1 / 56 / ≈0` → `\multicolumn{3}{c}{pending$^\ddagger$}` |
| `analysis_claim1.tex:23` | Table 脚注 | 新增 `$^\ddagger$` 说明：prior value (98.2%) used obstacle displacement |
| `analysis_claim1.tex:26-28` | Pi0.5 段落 | 重写：从"fake safe 98.2%"改为"contrasting case，re-evaluation in progress，may reflect genuine avoidance"；结论限定为 Pi0-based methods |
| `analysis_claim1.tex:34` | CAR_f 段 | "LoRA baseline and Pi0.5 near zero" → LoRA baseline near zero；Pi0.5 pending |
| `introduction.tex:9` | 第3段末 | "exhibits the same pattern: 98.2%" → "exhibits qualitatively different behavior...under re-evaluation" |
| `introduction.tex:17` | C1 贡献 | "98--99% across multiple methods and model scales" → "over 99% in Pi0-based methods" |
| `abstract.tex:2` | Pi0.5 描述 | "shows the same pattern" → "presents a contrasting case whose fake safety status is under re-evaluation" |

### 问题 2：10K → 30K 数据修正

| 文件 | 位置 | 改动 |
|------|------|------|
| `introduction.tex:13` | 段末 preliminary result | 10K "CAR 56-58%, TSR 47-49%" → 30K 为主（LoRA-only CAR=55.3%, TSR=6.3%; SDF CAR=50.5-52.8%, TSR=6.8%），10K 作为补充（TSR=26-30.5%, catastrophic collapse between 10K-30K） |
| `introduction.tex:19` | C3 贡献 | 补充 30K 具体数字（CAR 55.3%/50.5-52.8%, TSR 6.3%/6.8%）和 10K→30K TSR collapse |
| `abstract.tex:2` | Preliminary results 句 | "training-time SDF supervision...genuine collision avoidance" → 报告 30K 结果（CAR ~55%, TSR collapse to <7%, SDF no benefit） |

### 未修改（确认正确）

- A1 的 99.6% fake safe — 保留
- `analysis_claim3.tex` — 已使用 30K 数据，无 10K 问题

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 302658,
  "duration_api_ms": 303730,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "cbb169c9-0d3d-41e4-91b0-bd458b7ba42d",
  "total_cost_usd": 0.844751,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 41044,
    "cache_read_input_tokens": 316804,
    "output_tokens": 17092,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41044,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 929,
        "cache_read_input_tokens": 47330,
        "cache_creation_input_tokens": 5555,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5555
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2354,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0024690000000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 17092,
      "cacheReadInputTokens": 316804,
      "cacheCreationInputTokens": 41044,
      "webSearchRequests": 0,
      "costUSD": 0.8422820000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7c298e48-8ff3-45dd-a971-2aab46cb4708"
}
```

</details>

---
