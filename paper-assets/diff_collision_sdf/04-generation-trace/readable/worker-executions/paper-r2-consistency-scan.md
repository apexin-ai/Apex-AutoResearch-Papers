# paper r2 consistency scan

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 82
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_paper_r2-consistency-scan_20260528T065433.log`
- **Structured JSON:** [`69a74638970d27a56b86.json`](../../sessions/69/69a74638970d27a56b86.json)

## Before a recorded user message

82 recorded events

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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
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
  "uuid": "1778af4b-6890-4c6e-8cba-0c7d7497a638",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779966600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "01827d82-d8ce-4249-ac63-9ed6b7966867",
  "session_id": "bd430238-1092-4029-a111-64714589cc5c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the .tex files in the paper directory to perform the consistency scan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "268ee48a-c3c8-471e-ad55-63157ee41503",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3oQ7yR1VEmLUbxfvXGaas",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12536,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12536
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

_source line 5_

开始全文一致性扫描。先读取所有 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "715901c6-a6b4-4e4e-bb20-ecc53efa59b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3oQ7yR1VEmLUbxfvXGaas",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12536,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12536
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

_source line 6_

<details open><summary>🔧 Tool call — Glob · `toolu_012UhXQ2iiqsfbwNioDmRzYN`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "dffc6efe-7851-446b-94b1-3e71236b1591",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3oQ7yR1VEmLUbxfvXGaas",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12536,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12536
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

_source line 7 · 2026-05-28T06:54:50.291Z_

<details><summary>↩ Tool result · `toolu_012UhXQ2iiqsfbwNioDmRzYN`</summary>

```text
docs/paper/_archive/method.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
docs/paper/archive/analysis_claim4.tex
docs/paper/archive/analysis_claim2.tex
docs/paper/archive/analysis_claim1.tex
docs/paper/archive/analysis_claim3.tex
docs/paper/contingency_claim3.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/claim1.tex
docs/paper/experimental_framework.tex
docs/paper/claim2.tex
docs/paper/method.tex
docs/paper/claim3.tex
docs/paper/abstract.tex
docs/paper/appendix.tex
docs/paper/related_work.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "75e12eac-057d-4603-8477-411679420e82",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_archive/method.tex",
      "docs/paper/_archive/experiments.tex",
      "docs/paper/_archive/conclusion_DEPRECATED.tex",
      "docs/paper/archive/analysis_claim4.tex",
      "docs/paper/archive/analysis_claim2.tex",
      "docs/paper/archive/analysis_claim1.tex",
      "docs/paper/archive/analysis_claim3.tex",
      "docs/paper/contingency_claim3.tex",
      "docs/paper/main.tex",
      "docs/paper/introduction.tex",
      "docs/paper/claim1.tex",
      "docs/paper/experimental_framework.tex",
      "docs/paper/claim2.tex",
      "docs/paper/method.tex",
      "docs/paper/claim3.tex",
      "docs/paper/abstract.tex",
      "docs/paper/appendix.tex",
      "docs/paper/related_work.tex",
      "docs/paper/discussion.tex"
    ],
    "durationMs": 13,
    "numFiles": 19,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_019XgThbsdaWdFvZRFjwPvoJ`</summary>

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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "fb440b71-31c0-4060-bea9-44fffc597535",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 9 · 2026-05-28T06:54:53.122Z_

<details><summary>↩ Tool result · `toolu_019XgThbsdaWdFvZRFjwPvoJ`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\,mm. The robot is action-collapsed, not safe.
4	We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\,mm threshold range.
5	We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for nearly all measured avoidance gains (${\sim}$26 percentage points). SDF supervision shows no statistically significant benefit at the tested scale $\lambda \in \{0.005, 0.01, 0.1\}$ ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$; $\lambda = 0.1$: 57.00\%$\,\pm\,$2.18, 3 seeds).
6	Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision does not significantly improve collision avoidance across the tested loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than EE-only geometric supervision.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "eb1cce61-f2bc-4633-8032-d874023c9b30",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\% CAR while 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm. The robot is action-collapsed, not safe.\nWe introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\,mm threshold range.\nWe further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for nearly all measured avoidance gains (${\\sim}$26 percentage points). SDF supervision shows no statistically significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\nDisplacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision does not significantly improve collision avoidance across the tested loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than EE-only geometric supervision.\n\\end{abstract}\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01TPcsWSFZKdKYREyXgZbjpg`</summary>

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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "214691e4-5e8b-4c3e-8e6a-1a13240a0536",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 11 · 2026-05-28T06:54:53.572Z_

<details><summary>↩ Tool result · `toolu_01TPcsWSFZKdKYREyXgZbjpg`</summary>

```text
1	\section{Introduction}\label{sec:intro}
2	
3	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}. Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\linewidth]{fig1_teaser}
8	\caption{The action-collapsed safety problem in VLA collision avoidance evaluation. Standard CAR classifies an action-collapsed robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau_d$; Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{action-collapsed safety} (colloquially, ``fake safety''): \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.
15	
16	\textbf{Action collapse is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\tau_d$. dfCAR collapses Pi0+A1 from 91.5\% to ${\approx}$\,0\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\,=\,71.5\%, CAR\,=\,28.5\%, with every safe episode above 288\,mm displacement and dfCAR equal to raw CAR (Section~\ref{sec:fake_safety}).
17	
18	\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \emph{lower} CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\ref{sec:ee_only}).
19	
20	\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\sim}$26 points with zero action-collapsed episodes. Adding SDF supervision does not yield statistically significant improvement across the tested range $\lambda \in [0.005, 0.1]$ ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$; $\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance (Section~\ref{sec:avoidance_source}).
21	
22	Our contributions are:
23	\begin{itemize}
24	    \item \textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\tau_d \in [2, 200]$\,mm.
25	    \item \textbf{Action-collapse diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\% of Pi0 safe episodes are action-collapse artifacts.
26	    \item \textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.
27	    \item \textbf{Demonstration sufficiency:} collision-free demonstrations account for nearly all measured CAR gains (${\sim}$26\,pp); SDF supervision shows no statistically significant benefit across the tested range $\lambda \in [0.005, 0.1]$ ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$, 3 seeds).
28	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "49cce943-1990-409c-bd17-8ea9a76fb718",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:intro}\n\nCollision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig1_teaser}\n\\caption{The action-collapsed safety problem in VLA collision avoidance evaluation. Standard CAR classifies an action-collapsed robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\\tau_d$; Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and dfCAR equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not (Figure~\\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\\% exhibit displacement below 0.1\\,mm; TSR is 0\\% across all 800 episodes. The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{action-collapsed safety} (colloquially, ``fake safety''): \\emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\\cite{karwowski2024goodhart}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Action collapse is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\\tau_d$. dfCAR collapses Pi0+A1 from 91.5\\% to ${\\approx}$\\,0\\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\\,=\\,71.5\\%, CAR\\,=\\,28.5\\%, with every safe episode above 288\\,mm displacement and dfCAR equal to raw CAR (Section~\\ref{sec:fake_safety}).\n\n\\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n\n\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero action-collapsed episodes. Adding SDF supervision does not yield statistically significant improvement across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance (Section~\\ref{sec:avoidance_source}).\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\\tau_d \\in [2, 200]$\\,mm.\n    \\item \\textbf{Action-collapse diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\\% of Pi0 safe episodes are action-collapse artifacts.\n    \\item \\textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \\emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.\n    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for nearly all measured CAR gains (${\\sim}$26\\,pp); SDF supervision shows no statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$, 3 seeds).\n\\end{itemize}",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01TbXgkbH1AB7j2fr8t6Hczz`</summary>

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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "64570db2-8c37-40e8-b88a-586d3c1c2de7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-28T06:54:54.036Z_

<details><summary>↩ Tool result · `toolu_01TbXgkbH1AB7j2fr8t6Hczz`</summary>

```text
1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	\subsection{Benchmark and Models}\label{sec:benchmark}
4	
5	We evaluate on SafeLIBERO~\cite{hu2025vlsa}, the \textit{object\_pudding} suite (Level~II): four tabletop pick-and-place tasks with collision hazards and per-timestep collision detection. Two VLA families are tested: \textbf{Pi0} (${\sim}$2.5B)~\cite{black2024pi0} with flow matching~\cite{lipman2023flow}, and \textbf{Pi0.5} with broader pre-training. Table~\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). All metrics are computed using a fixed evaluation seed (seed\,=\,7); the reported $\pm$ values reflect variance across training seeds, not evaluation stochasticity. We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction of episodes that complete the task~\cite{hu2025vlsa,zhang2025safevla}.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Training configurations. Trainable parameters exclude the frozen backbone.}
10	\label{tab:configurations}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{llr}
14	\toprule
15	Configuration & Description & Trainable Params \\
16	\midrule
17	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$2.5B \\
18	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
19	Pi0+A1 (SDF aux)\textsuperscript{$\dagger$} & LoRA + SDF decoder + EE extractor & ${\sim}$658K \\
20	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
21	Pi0.5 (pre-trained) & No fine-tuning & 0 \\
22	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
23	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
24	\bottomrule
25	\end{tabular}
26	\vspace{2pt}
27	\raggedright\footnotesize\textsuperscript{$\dagger$}LoRA weights not loaded due to parameter-name mismatch; only auxiliary heads trained.
28	\end{table}
29	
30	\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
31	
32	Standard CAR conflates genuine avoidance with action collapse. We define an episode as \emph{action-collapsed} when $d_{\max}(e) < \tau_d$ ($\tau_d = 0.1$\,mm) and exclude such episodes:
33	\begin{equation}\label{eq:car_f}
34	\text{dfCAR} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
35	\end{equation}
36	The displacement distribution is sharply bimodal, with collapsed episodes below 1\,$\mu$m and active episodes above 200\,mm; any $\tau_d \in [2, 200]$\,mm yields identical results (Appendix~\ref{sec:appendix_threshold}). For Pi0 under the A1 architecture, $d_{\max}$ is computed from obstacle displacement rather than end-effector displacement, because A1's parameter-loading failure produces an inconsistent EE reference frame; all Pi0.5 configurations use standard EE displacement. The five-order-of-magnitude bimodal gap renders these two displacement measures functionally equivalent for collapse detection: collapsed episodes cluster below 1\,$\mu$m while active episodes exceed 200\,mm, so the exact displacement definition (obstacle vs.\ end-effector) is immaterial for classification. This gap also makes a simple displacement threshold sufficient for filtering; alternative displacement metrics (e.g., action variance, mean velocity) would yield equivalent classification given this bimodal separation; we adopt maximum displacement for interpretability.
37	
38	\subsection{SDF Auxiliary Training and Oracle Refinement}\label{sec:sdf_aux}
39	
40	We augment LoRA-adapted~\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\ref{sec:appendix_training}, Table~\ref{tab:hyperparams}). The total loss is:
41	\begin{equation}\label{eq:total_loss}
42	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda \left( \mathcal{L}_\text{SDF} + \mathcal{L}_\text{EE} \right)
43	\end{equation}
44	where $\lambda \in \{0.005, 0.01, 0.1\}$. In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\,=\,0\%; Table~\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\ref{sec:appendix_oracle}).\label{sec:oracle_setup}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "16c912a3-e354-4910-8763-0999354d83a7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
      "content": "\\section{Experimental Setup and Metrics}\\label{sec:method}\n\n\\subsection{Benchmark and Models}\\label{sec:benchmark}\n\nWe evaluate on SafeLIBERO~\\cite{hu2025vlsa}, the \\textit{object\\_pudding} suite (Level~II): four tabletop pick-and-place tasks with collision hazards and per-timestep collision detection. Two VLA families are tested: \\textbf{Pi0} (${\\sim}$2.5B)~\\cite{black2024pi0} with flow matching~\\cite{lipman2023flow}, and \\textbf{Pi0.5} with broader pre-training. Table~\\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). All metrics are computed using a fixed evaluation seed (seed\\,=\\,7); the reported $\\pm$ values reflect variance across training seeds, not evaluation stochasticity. We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction of episodes that complete the task~\\cite{hu2025vlsa,zhang2025safevla}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameters exclude the frozen backbone.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux)\\textsuperscript{$\\dagger$} & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 (pre-trained) & No fine-tuning & 0 \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\raggedright\\footnotesize\\textsuperscript{$\\dagger$}LoRA weights not loaded due to parameter-name mismatch; only auxiliary heads trained.\n\\end{table}\n\n\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\n\nStandard CAR conflates genuine avoidance with action collapse. We define an episode as \\emph{action-collapsed} when $d_{\\max}(e) < \\tau_d$ ($\\tau_d = 0.1$\\,mm) and exclude such episodes:\n\\begin{equation}\\label{eq:car_f}\n\\text{dfCAR} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nThe displacement distribution is sharply bimodal, with collapsed episodes below 1\\,$\\mu$m and active episodes above 200\\,mm; any $\\tau_d \\in [2, 200]$\\,mm yields identical results (Appendix~\\ref{sec:appendix_threshold}). For Pi0 under the A1 architecture, $d_{\\max}$ is computed from obstacle displacement rather than end-effector displacement, because A1's parameter-loading failure produces an inconsistent EE reference frame; all Pi0.5 configurations use standard EE displacement. The five-order-of-magnitude bimodal gap renders these two displacement measures functionally equivalent for collapse detection: collapsed episodes cluster below 1\\,$\\mu$m while active episodes exceed 200\\,mm, so the exact displacement definition (obstacle vs.\\ end-effector) is immaterial for classification. This gap also makes a simple displacement threshold sufficient for filtering; alternative displacement metrics (e.g., action variance, mean velocity) would yield equivalent classification given this bimodal separation; we adopt maximum displacement for interpretability.\n\n\\subsection{SDF Auxiliary Training and Oracle Refinement}\\label{sec:sdf_aux}\n\nWe augment LoRA-adapted~\\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\\ref{sec:appendix_training}, Table~\\ref{tab:hyperparams}). The total loss is:\n\\begin{equation}\\label{eq:total_loss}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda \\left( \\mathcal{L}_\\text{SDF} + \\mathcal{L}_\\text{EE} \\right)\n\\end{equation}\nwhere $\\lambda \\in \\{0.005, 0.01, 0.1\\}$. In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\\,=\\,0\\%; Table~\\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\\ref{sec:appendix_oracle}).\\label{sec:oracle_setup}\n",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01VD5abxwuVKF4HUmQNSVnUn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "685b4e19-c9b2-477b-b151-e919fda57497",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 15 · 2026-05-28T06:54:54.509Z_

<details><summary>↩ Tool result · `toolu_01VD5abxwuVKF4HUmQNSVnUn`</summary>

```text
1	\section{Experimental Framework}\label{sec:framework}
2	
3	This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (dfCAR), which separates genuine avoidance from action collapse.
4	
5	\subsection{Benchmark and Evaluation Protocol}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.
8	
9	We select the \textit{object\_pudding} Level~I suite, which comprises four tabletop manipulation tasks. In each task, a target object is surrounded by non-target obstacles that the robot must avoid during grasping and transport. The MuJoCo physics engine provides collision detection: any contact between the robot (end-effector or arm links) and a non-target object registers as a collision event.
10	
11	Each method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.
12	
13	\subsection{Evaluation Metrics}\label{sec:metrics}
14	
15	\paragraph{Standard metrics.} We report two conventional metrics. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.
16	
17	\paragraph{Displacement-filtered CAR.} Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We propose the displacement-filtered CAR (dfCAR), which excludes episodes exhibiting action collapse from both numerator and denominator.
18	
19	We define an episode $e$ as \emph{action-collapsed} when its maximum end-effector displacement satisfies $d_{\max}(e) < \tau_d$, where $\tau_d = 0.1$\,mm. The filtered metric is then:
20	\begin{equation}\label{eq:car_f}
21	\text{dfCAR} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
22	\end{equation}
23	where $d_{\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\tau_d = 0.1$\,mm corresponds to sub-actuator-resolution motion. In practice, the displacement distribution is bimodal: collapsed episodes cluster below 1\,$\mu$m and active episodes exceed 200\,mm, with no intermediate population. Consequently, any $\tau_d \in [2, 200]$\,mm produces identical filtering (Appendix~\ref{sec:appendix_threshold}).
24	
25	\paragraph{Auxiliary metrics.} We additionally report the \emph{Action-Collapse Rate}, the fraction of episodes with $d_{\max} < \tau_d$, which quantifies the severity of action collapse for each method. The \emph{Simultaneous Success Rate} (SSR $= $ TSR $\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.
26	
27	\subsection{Models and Training}
28	
29	\paragraph{Base architectures.} We evaluate two VLA models from the Pi0 family~\cite{black2024pi0}. \textbf{Pi0} (${\sim}$3B parameters) uses a PaliGemma vision-language encoder paired with a dedicated action expert that generates continuous actions via flow matching~\cite{lipman2023flow}. \textbf{Pi0.5} extends this architecture to ${\sim}$3.5B parameters with broader pre-training data, and serves as a stronger baseline that exhibits less action collapse.
30	
31	\paragraph{Training configurations.} We evaluate four model variants:
32	\begin{itemize}
33	\item \textit{Full-FT baseline}: Pi0 with all parameters fine-tuned on SafeLIBERO demonstrations using the flow-matching action loss.
34	\item \textit{LoRA baseline}: Pi0 with LoRA adapters (${\sim}$33.5M trainable parameters), same demonstrations and loss.
35	\item \textit{A1-LoRA}: Pi0 + LoRA augmented with two auxiliary heads. An SDF Decoder (4-layer MLP, ${\sim}$395K parameters) predicts the signed distance from the end-effector to the nearest obstacle surface, supervised with a clamped $L_1$ loss and an Eikonal regularizer ($\mathcal{L}_\text{SDF}$). An EE Extractor (2-layer MLP, ${\sim}$263K parameters) predicts end-effector position from action expert features ($\mathcal{L}_\text{EE}$, MSE loss). SDF ground truth is computed from known obstacle meshes in simulation.
36	\item \textit{Pi0.5 + A1}: The A1 architecture applied to the Pi0.5 backbone. Training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization. We evaluate $\lambda_\text{SDF} \in \{0.005, 0.01\}$.
37	\end{itemize}
38	
39	\subsection{Oracle SDF Refinement}
40	
41	To test the theoretical upper bound of end-effector-only SDF refinement (analyzed in Section~\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm itself.
42	
43	We evaluate three oracle variants that differ in how the SDF gradient is applied:
44	\begin{itemize}
45	\item \textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\alpha$ that scales inversely with gradient magnitude.
46	\item \textit{Oracle-fixed}: a constant step size $\alpha = 0.005$.
47	\item \textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than Cartesian action space.
48	\end{itemize}
49	Each variant is evaluated for 160 episodes (4 tasks $\times$ 40 episodes) with a single seed.
50	
51	\subsection{SDF Ground Truth}
52	
53	The workspace signed distance field is computed from the known obstacle meshes available in the LIBERO/MuJoCo simulation environment. SDF values are positive in free space, zero on the obstacle surface, and negative inside the obstacle volume. Ground-truth labels are generated at query points sampled along predicted end-effector trajectories during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "a89d6b32-a924-498d-94f5-8438f77f6f69",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex",
      "content": "\\section{Experimental Framework}\\label{sec:framework}\n\nThis section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (dfCAR), which separates genuine avoidance from action collapse.\n\n\\subsection{Benchmark and Evaluation Protocol}\n\nWe conduct all experiments on SafeLIBERO~\\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.\n\nWe select the \\textit{object\\_pudding} Level~I suite, which comprises four tabletop manipulation tasks. In each task, a target object is surrounded by non-target obstacles that the robot must avoid during grasping and transport. The MuJoCo physics engine provides collision detection: any contact between the robot (end-effector or arm links) and a non-target object registers as a collision event.\n\nEach method is evaluated for 50 episodes per task (200 episodes total). For multi-seed experiments (Pi0.5), we run 3 seeds to produce 600 episodes per configuration. Initial object configurations are fixed across methods to ensure fair comparison.\n\n\\subsection{Evaluation Metrics}\\label{sec:metrics}\n\n\\paragraph{Standard metrics.} We report two conventional metrics. The \\emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \\emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.\n\n\\paragraph{Displacement-filtered CAR.} Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We propose the displacement-filtered CAR (dfCAR), which excludes episodes exhibiting action collapse from both numerator and denominator.\n\nWe define an episode $e$ as \\emph{action-collapsed} when its maximum end-effector displacement satisfies $d_{\\max}(e) < \\tau_d$, where $\\tau_d = 0.1$\\,mm. The filtered metric is then:\n\\begin{equation}\\label{eq:car_f}\n\\text{dfCAR} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nwhere $d_{\\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\\tau_d = 0.1$\\,mm corresponds to sub-actuator-resolution motion. In practice, the displacement distribution is bimodal: collapsed episodes cluster below 1\\,$\\mu$m and active episodes exceed 200\\,mm, with no intermediate population. Consequently, any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering (Appendix~\\ref{sec:appendix_threshold}).\n\n\\paragraph{Auxiliary metrics.} We additionally report the \\emph{Action-Collapse Rate}, the fraction of episodes with $d_{\\max} < \\tau_d$, which quantifies the severity of action collapse for each method. The \\emph{Simultaneous Success Rate} (SSR $= $ TSR $\\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.\n\n\\subsection{Models and Training}\n\n\\paragraph{Base architectures.} We evaluate two VLA models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$3B parameters) uses a PaliGemma vision-language encoder paired with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} extends this architecture to ${\\sim}$3.5B parameters with broader pre-training data, and serves as a stronger baseline that exhibits less action collapse.\n\n\\paragraph{Training configurations.} We evaluate four model variants:\n\\begin{itemize}\n\\item \\textit{Full-FT baseline}: Pi0 with all parameters fine-tuned on SafeLIBERO demonstrations using the flow-matching action loss.\n\\item \\textit{LoRA baseline}: Pi0 with LoRA adapters (${\\sim}$33.5M trainable parameters), same demonstrations and loss.\n\\item \\textit{A1-LoRA}: Pi0 + LoRA augmented with two auxiliary heads. An SDF Decoder (4-layer MLP, ${\\sim}$395K parameters) predicts the signed distance from the end-effector to the nearest obstacle surface, supervised with a clamped $L_1$ loss and an Eikonal regularizer ($\\mathcal{L}_\\text{SDF}$). An EE Extractor (2-layer MLP, ${\\sim}$263K parameters) predicts end-effector position from action expert features ($\\mathcal{L}_\\text{EE}$, MSE loss). SDF ground truth is computed from known obstacle meshes in simulation.\n\\item \\textit{Pi0.5 + A1}: The A1 architecture applied to the Pi0.5 backbone. Training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization. We evaluate $\\lambda_\\text{SDF} \\in \\{0.005, 0.01\\}$.\n\\end{itemize}\n\n\\subsection{Oracle SDF Refinement}\n\nTo test the theoretical upper bound of end-effector-only SDF refinement (analyzed in Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm itself.\n\nWe evaluate three oracle variants that differ in how the SDF gradient is applied:\n\\begin{itemize}\n\\item \\textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\\alpha$ that scales inversely with gradient magnitude.\n\\item \\textit{Oracle-fixed}: a constant step size $\\alpha = 0.005$.\n\\item \\textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than Cartesian action space.\n\\end{itemize}\nEach variant is evaluated for 160 episodes (4 tasks $\\times$ 40 episodes) with a single seed.\n\n\\subsection{SDF Ground Truth}\n\nThe workspace signed distance field is computed from the known obstacle meshes available in the LIBERO/MuJoCo simulation environment. SDF values are positive in free space, zero on the obstacle surface, and negative inside the obstacle volume. Ground-truth labels are generated at query points sampled along predicted end-effector trajectories during training.",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01JUw8RqeB9LcnuvvuKY5QBL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "ce4b8a17-8229-4b25-b76a-f97cf4db6ec4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 17 · 2026-05-28T06:54:54.978Z_

<details><summary>↩ Tool result · `toolu_01JUw8RqeB9LcnuvvuKY5QBL`</summary>

```text
1	\section{The Action-Collapsed Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\% of collision-free episodes are action-collapse artifacts (Table~\ref{tab:fake_safety}).\footnote{Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (\S\ref{sec:dfcar}). Sub-millimeter displacement indicates action collapse in both cases.} Applying dfCAR collapses all three to ${\approx}$\,0\%. Pi0+A1 achieves the \emph{highest} raw CAR (91.5\%) because more complete action collapse (from a parameter-name mismatch preventing LoRA loading; Table~\ref{tab:configurations}) yields greater CAR inflation. Pi0.5 validates the metric from the opposite direction: every safe episode exceeds 200\,mm displacement, and dfCAR equals raw CAR (28.5\%). The displacement distribution is sharply bimodal (Appendix~\ref{sec:appendix_displacement}), with a five-order-of-magnitude gap that makes $\tau_d$ robust.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Action-collapse decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \tau_d = 0.1$\,mm.}
8	\label{tab:fake_safety}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Ep. & CAR (\%) & TSR (\%) & Collapsed (\%) & dfCAR (\%) \\
14	\midrule
15	Pi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\approx$\,0 \\
16	Pi0 LoRA     & 200 & 82.0 & 0.0 & ${\sim}$99 & $\approx$\,0 \\
17	Pi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & $\approx$\,0$^*$ \\
18	\midrule
19	Pi0.5  & 200 & 28.5 & 71.5 & 0.0 & 28.5 \\
20	\bottomrule
21	\end{tabular}
22	\vspace{1pt}
23	{\footnotesize $^*$\,3/732 safe episodes above threshold; denominator too small for reliable rate.}
24	\end{table}
25	
26	Figure~\ref{fig:tsr_car_scatter} reveals spatial structure in the TSR-CAR plane.\label{sec:anticorrelation} Pi0-family models cluster in the upper-left (high CAR, near-zero TSR), Pi0.5 in the lower-right (high TSR, low CAR). The upper-right quadrant (high TSR \emph{and} CAR) represents genuinely safe behavior; the upper-left is accessible through action collapse alone. Under dfCAR, Pi0 configurations drop to the origin: the apparent safety-capability tradeoff was an artifact of action-collapse contamination.
27	
28	\begin{figure}[t]
29	\centering
30	\includegraphics[width=0.85\linewidth]{fig_tsr_car_scatter.pdf}
31	\caption{TSR vs.\ CAR for all configurations. Pi0-family models cluster in the upper-left (high CAR from inaction), Pi0.5 in the lower-right (high TSR with collision exposure), fine-tuned Pi0.5 in the center. The upper-right quadrant (high TSR and CAR) represents genuinely safe behavior. Error bars: $\pm$1 std across seeds.}
32	\label{fig:tsr_car_scatter}
33	\end{figure}
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "a2877266-65c5-461b-b85c-38390ce6367e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
      "content": "\\section{The Action-Collapsed Safety Problem}\\label{sec:fake_safety}\n\nStandard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\\% of collision-free episodes are action-collapse artifacts (Table~\\ref{tab:fake_safety}).\\footnote{Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (\\S\\ref{sec:dfcar}). Sub-millimeter displacement indicates action collapse in both cases.} Applying dfCAR collapses all three to ${\\approx}$\\,0\\%. Pi0+A1 achieves the \\emph{highest} raw CAR (91.5\\%) because more complete action collapse (from a parameter-name mismatch preventing LoRA loading; Table~\\ref{tab:configurations}) yields greater CAR inflation. Pi0.5 validates the metric from the opposite direction: every safe episode exceeds 200\\,mm displacement, and dfCAR equals raw CAR (28.5\\%). The displacement distribution is sharply bimodal (Appendix~\\ref{sec:appendix_displacement}), with a five-order-of-magnitude gap that makes $\\tau_d$ robust.\n\n\\begin{table}[t]\n\\centering\n\\caption{Action-collapse decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \\tau_d = 0.1$\\,mm.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Ep. & CAR (\\%) & TSR (\\%) & Collapsed (\\%) & dfCAR (\\%) \\\\\n\\midrule\nPi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\\approx$\\,0 \\\\\nPi0 LoRA     & 200 & 82.0 & 0.0 & ${\\sim}$99 & $\\approx$\\,0 \\\\\nPi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & $\\approx$\\,0$^*$ \\\\\n\\midrule\nPi0.5  & 200 & 28.5 & 71.5 & 0.0 & 28.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\footnotesize $^*$\\,3/732 safe episodes above threshold; denominator too small for reliable rate.}\n\\end{table}\n\nFigure~\\ref{fig:tsr_car_scatter} reveals spatial structure in the TSR-CAR plane.\\label{sec:anticorrelation} Pi0-family models cluster in the upper-left (high CAR, near-zero TSR), Pi0.5 in the lower-right (high TSR, low CAR). The upper-right quadrant (high TSR \\emph{and} CAR) represents genuinely safe behavior; the upper-left is accessible through action collapse alone. Under dfCAR, Pi0 configurations drop to the origin: the apparent safety-capability tradeoff was an artifact of action-collapse contamination.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig_tsr_car_scatter.pdf}\n\\caption{TSR vs.\\ CAR for all configurations. Pi0-family models cluster in the upper-left (high CAR from inaction), Pi0.5 in the lower-right (high TSR with collision exposure), fine-tuned Pi0.5 in the center. The upper-right quadrant (high TSR and CAR) represents genuinely safe behavior. Error bars: $\\pm$1 std across seeds.}\n\\label{fig:tsr_car_scatter}\n\\end{figure}\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01F57XZ5RAaiGuag8vMhToEk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "5cd9522c-a8fa-4d99-bce8-663aaa3de50c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 19 · 2026-05-28T06:54:55.417Z_

<details><summary>↩ Tool result · `toolu_01F57XZ5RAaiGuag8vMhToEk`</summary>

```text
1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\S\ref{sec:oracle_setup}). Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_bar} show that all three oracle variants achieve \emph{lower} CAR than unrefined baselines: the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%). Refinement with perfect distance information produces more collisions, not fewer.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccc}
12	\toprule
13	Method & CAR (\%) & Collapsed (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 77.1 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{figure}[t]
28	\centering
29	\includegraphics[width=0.85\linewidth]{fig_oracle_bar.pdf}
30	\caption{CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform baselines despite perfect distance information.}
31	\label{fig:oracle_bar}
32	\end{figure}
33	
34	Per-task analysis reveals the mechanism (Appendix~\ref{sec:appendix_pertask_oracle}). On the one task where the EE is the primary collision body, oracle refinement helps (+9 points). On the remaining three, the SDF gradient pushes the EE away from obstacles but rotates intermediate arm links into obstacle volumes; the net effect is one collision traded for another. The A3 learned SDF never triggers refinement (0 steps per episode). EE-only refinement is structurally counterproductive: joint-space coupling between EE displacement and arm-link rotation redistributes collisions to unmonitored links regardless of signal quality. The ecological validity of this finding varies across configurations: the Pi0+A1 baseline (TSR$\,\approx\,$0\%) is already fully action-collapsed, making its oracle test a degenerate case. The LoRA baseline is itself largely action-collapsed (99.4\% collapsed episodes, Table~\ref{tab:oracle}); the structural finding---that EE-only refinement redistributes rather than reduces collisions---should hold regardless of base-policy activity level, but validation on a functional (non-collapsed) policy remains future work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "53563039-f997-42c1-a350-1a5db4b06257",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex",
      "content": "\\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\n\nCould a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\\S\\ref{sec:oracle_setup}). Table~\\ref{tab:oracle} and Figure~\\ref{fig:oracle_bar} show that all three oracle variants achieve \\emph{lower} CAR than unrefined baselines: the best oracle (76.9\\%) falls 5.1 points below LoRA (82.0\\%). Refinement with perfect distance information produces more collisions, not fewer.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\\ref{sec:appendix_pertask_oracle}.}\n\\label{tab:oracle}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & CAR (\\%) & Collapsed (\\%) & Refines/ep \\\\\n\\midrule\nLoRA baseline (no refine) & 82.0 & 99.4 & -- \\\\\nFull-FT baseline (no refine) & 83.0 & -- & -- \\\\\n\\midrule\nOracle-adaptive (GT, dyn.\\ $\\alpha$) & 75.0 & 98.3 & 14.2 \\\\\nOracle-fixed (GT, $\\alpha{=}0.005$) & 73.1 & 98.3 & 14.8 \\\\\nOracle-feature (GT, feat.\\ space) & 76.9 & 96.7 & 241.7 \\\\\n\\midrule\nA3 learned SDF & 77.1 & -- & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig_oracle_bar.pdf}\n\\caption{CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform baselines despite perfect distance information.}\n\\label{fig:oracle_bar}\n\\end{figure}\n\nPer-task analysis reveals the mechanism (Appendix~\\ref{sec:appendix_pertask_oracle}). On the one task where the EE is the primary collision body, oracle refinement helps (+9 points). On the remaining three, the SDF gradient pushes the EE away from obstacles but rotates intermediate arm links into obstacle volumes; the net effect is one collision traded for another. The A3 learned SDF never triggers refinement (0 steps per episode). EE-only refinement is structurally counterproductive: joint-space coupling between EE displacement and arm-link rotation redistributes collisions to unmonitored links regardless of signal quality. The ecological validity of this finding varies across configurations: the Pi0+A1 baseline (TSR$\\,\\approx\\,$0\\%) is already fully action-collapsed, making its oracle test a degenerate case. The LoRA baseline is itself largely action-collapsed (99.4\\% collapsed episodes, Table~\\ref{tab:oracle}); the structural finding---that EE-only refinement redistributes rather than reduces collisions---should hold regardless of base-policy activity level, but validation on a functional (non-collapsed) policy remains future work.",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01C1V85ct72XTM3dc2Wz5oc1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "6fa26ac2-5e85-4706-b059-3b1d03522afa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 21 · 2026-05-28T06:54:56.718Z_

<details><summary>↩ Tool result · `toolu_01C1V85ct72XTM3dc2Wz5oc1`</summary>

```text
1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero action-collapsed episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,58.0\%\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce lowest) and invariant to $\lambda$ across the tested range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.
27	
28	\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
29	Fine-tuning degrades TSR by ${\sim}$18--20\,pp (71.5\% $\to$ 51.5--54.0\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% action-collapsed episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
30	
31	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
32	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,57.00\%\,$\pm$\,2.18 at the 30K checkpoint (3 seeds: 58.0\%, 58.5\%, 54.5\%), within the null distribution (mean 54.58\%, $\sigma = 1.93$; permutation $p = 0.131$\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \emph{decrease} CAR, the result remains non-significant.}). SDF supervision does not produce statistically significant benefit across the tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
33	
34	\paragraph{Robustness to null construction.}
35	The preceding permutation test pools LoRA-only and $\lambda = 0.005$ seeds as a single null (Null~B, $\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\alpha = 0.05$.
36	
37	\paragraph{Statistical power.}
38	With $n = 3$ seeds per group and $\sigma \approx 2.0$\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\alpha = 0.05$ (one-tailed) achieves 80\% power only for effects $\geq 5.0$\,pp. The observed effect of ${\sim}$2.3\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.
39	
40	\paragraph{Evaluation-seed consistency.}
41	Under matched evaluation conditions (Appendix~\ref{sec:appendix_eval_seed}), SDF $\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\,pp), with lower cross-seed variance ($\sigma = 0.9$\,pp vs.\ 2.0\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\sim}$2.3\,pp) falls well below the study's MDE (${\sim}$5\,pp at 80\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.
42	
43	\begin{figure}[t]
44	\centering
45	\includegraphics[width=0.85\linewidth]{fig5_lambda_curve}
46	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. The $\lambda \in \{0.01, 0.1\}$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\times$ loss-weight range.}
47	\label{fig:lambda_car}
48	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "433b879c-8d90-49a6-be30-996c471c6824",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
      "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero action-collapsed episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$). All fine-tuned models exhibit 0\\% action-collapse rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero action-collapsed episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across the tested range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% action-collapsed episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision does not produce statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. The $\\lambda \\in \\{0.01, 0.1\\}$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01UHoQ4ZRDzB1zs8pXDgQcBD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "39cce2e8-1dac-489d-973f-24d5fcf81697",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 23 · 2026-05-28T06:54:56.833Z_

<details><summary>↩ Tool result · `toolu_01UHoQ4ZRDzB1zs8pXDgQcBD`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\S\ref{sec:avoidance_source}).
4	
5	\paragraph{Why EE-only SDF fails.}
6	Two independent causes explain the null result. \textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$ (spanning an order of magnitude above the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \emph{reduces} CAR by 6--10\,pp below unrefined baselines (\S\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.
7	
8	\paragraph{Implications for evaluation.}
9	dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\times$ parameter range (Pi0 Full-FT ${\sim}$2.5B to Pi0+A1 ${\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.
10	
11	\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The finding that EE-only SDF shows no significant benefit (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\ref{sec:related}).
12	
13	\paragraph{Limitations.}
14	All experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\approx}$0\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\sim}$18--20\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.
15	
16	\paragraph{Future work.}
17	Three directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.
18	
19	\paragraph{Broader impact.}
20	The displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "4c3769d1-b694-4652-9794-13bf98ae4bcc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (spanning an order of magnitude above the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The finding that EE-only SDF shows no significant benefit (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_019LHhPLJ1aXRx2RLpp1GcRj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "0321c385-2a7e-49ba-812c-443ca8475bd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 25 · 2026-05-28T06:54:57.348Z_

<details><summary>↩ Tool result · `toolu_019LHhPLJ1aXRx2RLpp1GcRj`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models.}
4	VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.
5	
6	\paragraph{Safety in Robot Learning.}
7	Safety-aware approaches span training-time constrained RL~\cite{zhang2025safevla} and test-time filters: control barrier functions~\cite{hu2025vlsa}, collision risk gating~\cite{cofreeevla2026}, inverse kinematics QP~\cite{spalter2024ikinqp}, and diffusion-process collision costs~\cite{li2024langguided,yang2025cape}. SafeDiffuser~\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.
8	
9	\paragraph{Signed Distance Functions in Robotics.}
10	SDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\cite{ortiz2022isdf}, planning~\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\cite{zhi2021diffco}. CDF~\cite{li2024cdf} extends SDFs to robot configuration space, learning neural distance fields that provide efficient joint-angle queries with analytical gradients for manipulation planning; CSSDF-Net~\cite{chen2026cssdfnet} further develops this direction for safe motion planning. RDF~\cite{li2024rdf} represents robot geometry itself as composable per-link SDFs along the kinematic chain, enabling whole-body collision queries---directly relevant to the full-body awareness gap our work identifies. Neural SDF-based model predictive control~\cite{jacquet2025neuralnmpc} demonstrates effectiveness in classical pipelines, but integration into end-to-end learned policies remains unexplored.
11	
12	\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\emph{Constrained optimization}: SafeVLA~\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, embedding safety constraints into the training objective via Lagrangian optimization rather than adding SDF as an auxiliary loss. (c)~\emph{Runtime filtering}: VLSA~\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant at the tested scale---is specific to pathway~(a) and does not imply limitations for pathways~(b) and~(c), which address collision avoidance through fundamentally different mechanisms: constrained optimization of violation probability and runtime action filtering, respectively.
13	
14	\paragraph{Evaluation Metrics for Safe Manipulation.}
15	SafeLIBERO~\cite{hu2025vlsa} extends LIBERO~\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\cite{snyder2026beyond}. Action collapse in diffusion policies~\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. Concurrent work expands the evaluation landscape: HazardArena~\cite{chen2026hazardarena} evaluates semantic safety through safe/unsafe twin scenarios, and VLA-Risk~\cite{vlariskanon2026} benchmarks physical robustness across object, action, and spatial perturbation dimensions. We propose dfCAR (\S\ref{sec:dfcar}) to detect this contamination.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "42f976ff-7b26-4640-96f9-3e6146b6cf3c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models.}\nVLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware approaches span training-time constrained RL~\\cite{zhang2025safevla} and test-time filters: control barrier functions~\\cite{hu2025vlsa}, collision risk gating~\\cite{cofreeevla2026}, inverse kinematics QP~\\cite{spalter2024ikinqp}, and diffusion-process collision costs~\\cite{li2024langguided,yang2025cape}. SafeDiffuser~\\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\\cite{ortiz2022isdf}, planning~\\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\\cite{zhi2021diffco}. CDF~\\cite{li2024cdf} extends SDFs to robot configuration space, learning neural distance fields that provide efficient joint-angle queries with analytical gradients for manipulation planning; CSSDF-Net~\\cite{chen2026cssdfnet} further develops this direction for safe motion planning. RDF~\\cite{li2024rdf} represents robot geometry itself as composable per-link SDFs along the kinematic chain, enabling whole-body collision queries---directly relevant to the full-body awareness gap our work identifies. Neural SDF-based model predictive control~\\cite{jacquet2025neuralnmpc} demonstrates effectiveness in classical pipelines, but integration into end-to-end learned policies remains unexplored.\n\n\\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constrained optimization}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, embedding safety constraints into the training objective via Lagrangian optimization rather than adding SDF as an auxiliary loss. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant at the tested scale---is specific to pathway~(a) and does not imply limitations for pathways~(b) and~(c), which address collision avoidance through fundamentally different mechanisms: constrained optimization of violation probability and runtime action filtering, respectively.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nSafeLIBERO~\\cite{hu2025vlsa} extends LIBERO~\\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\\cite{snyder2026beyond}. Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. Concurrent work expands the evaluation landscape: HazardArena~\\cite{chen2026hazardarena} evaluates semantic safety through safe/unsafe twin scenarios, and VLA-Risk~\\cite{vlariskanon2026} benchmarks physical robustness across object, action, and spatial perturbation dimensions. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_012DVMiEz11v3uRk8L4q624r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "99fa1c91-4f56-476d-be7e-e153425ec7c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 27 · 2026-05-28T06:54:57.808Z_

<details><summary>↩ Tool result · `toolu_012DVMiEz11v3uRk8L4q624r`</summary>

```text
1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% action-collapse rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Action-collapse rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
35	
36	\begin{table}[h]
37	\centering
38	\caption{dfCAR (\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\tau_d \in [2, 200]$\,mm; at $\tau_d = 300$\,mm, at most 2 episodes are excluded.}
39	\label{tab:dfcar_threshold}
40	\vspace{2pt}
41	\footnotesize
42	\begin{tabular}{lcccccccc}
43	\toprule
44	& \multicolumn{8}{c}{$\tau_d$ (mm)} \\
45	\cmidrule(lr){2-9}
46	Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\
47	\midrule
48	LoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\
49	LoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\
50	SDF $\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\
51	SDF $\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\
52	SDF $\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\
53	SDF $\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
54	SDF $\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\
55	SDF $\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\
56	\bottomrule
57	\end{tabular}
58	\end{table}
59	
60	
61	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
62	
63	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
64	
65	\begin{table}[h]
66	\centering
67	\caption{Per-task TSR (\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\,=\,71.5\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}
68	\label{tab:per_task_tsr}
69	\vspace{2pt}
70	\small
71	\begin{tabular}{lcccc}
72	\toprule
73	Task & Pi0.5 Base & LoRA-only & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
74	 & (seed\,=\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\
75	\midrule
76	Orange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\
77	Choco.\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\
78	Milk              & 66.0 & 44.7 & 35.3 & 48.7 \\
79	BBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\
80	\midrule
81	Mean              & 71.5 & 51.5 & 54.0 & 53.8 \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\section{Per-Task CAR Breakdown}\label{sec:appendix_pertask_car}
87	
88	Table~\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\S\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.
89	
90	\begin{table}[h]
91	\centering
92	\caption{Per-task CAR (\%) at 30K steps. $\lambda{=}0.005$, $\lambda{=}0.01$, and $\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}
93	\label{tab:per_task_car}
94	\vspace{2pt}
95	\small
96	\begin{tabular}{lccccc}
97	\toprule
98	Condition & OJ & CP & Milk & BBQ & Agg. \\
99	\midrule
100	LoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\
101	LoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\
102	LoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\
103	SDF $\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\
104	SDF $\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\
105	SDF $\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\
106	SDF $\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\
107	SDF $\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\
108	SDF $\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\
109	\bottomrule
110	\end{tabular}
111	\end{table}
112	
113	For the $\lambda = 0.1$ condition, seed~1 records \texttt{avg\_max\_obstacle\_displacement} of 0.0553\,m (per-task: OJ\,=\,0.033, CP\,=\,0.055, Milk\,=\,0.041, BBQ\,=\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.
114	
115	\begin{figure}[t]
116	\centering
117	\includegraphics[width=\linewidth]{fig_pertask_car_fingerprint}
118	\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\_pudding highest, bbq\_sauce lowest) is preserved across all $\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}
119	\label{fig:pertask_fingerprint}
120	\end{figure}
121	
122	\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
123	
124	Table~\ref{tab:ssr} reports the Safe Success Rate (SSR\,=\,TSR\,$\cap$\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.
125	
126	\begin{table}[h]
127	\centering
128	\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}
129	\label{tab:ssr}
130	\vspace{2pt}
131	\small
132	\begin{tabular}{lcccc}
133	\toprule
134	Condition & TSR (\%) & CAR (\%) & SSR (\%) & SSR/TSR \\
135	\midrule
136	Pi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\
137	LoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\
138	SDF $\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\
139	SDF $\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\
140	SDF $\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
145	\section{Per-Task Oracle Analysis}
146	\label{sec:appendix_pertask}
147	\label{sec:appendix_pertask_oracle}
148	
149	Table~\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\texttt{chocolate\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive improves to 55.0\% and Oracle-feature to 47.5\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\texttt{orange\_juice}) from 96.0\% to 82.5\% and task~2 (\texttt{milk}) from 98.0\% to 77.5\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.
150	
151	The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49), and CAR (76.9\%) shows no advantage despite 17$\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.
152	
153	\begin{table}[h]
154	\centering
155	\caption{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}
156	\label{tab:oracle_pertask}
157	\vspace{2pt}
158	\small
159	\begin{tabular}{lccccc}
160	\toprule
161	Method & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\
162	\midrule
163	LoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\
164	\midrule
165	Oracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\
166	Oracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\
167	Oracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\
168	\bottomrule
169	\end{tabular}
170	\end{table}
171	
172	
173	\section{Null Distribution for SDF Loss Weight Analysis}
174	\label{sec:appendix_null}
175	
176	We construct a null distribution by pooling the three LoRA-only seeds and three $\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 55.0\% (LoRA s2), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.58\% and standard deviation 1.93\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 57.00\% (3 seeds: 58.0\%, 58.5\%, 54.5\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\alpha = 0.05$).
177	
178	The permutation test makes no distributional assumptions. Pooling the six null values $\{56.5, 52.5, 55, 57, 54, 52.5\}$ and three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$ into nine measurements, we enumerate all $\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \approx 0.131$. With the third seed ($s_2 = 54.5\%$) pulling the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.
179	
180	\paragraph{Alternative null construction (Null~A).}
181	If only the three LoRA-only seeds are used as the null pool ($\{56.5, 52.5, 55.0\}$), we obtain $\binom{6}{3} = 20$ permutations for each comparison. For $\lambda = 0.1$ (treatment mean 57.00\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\lambda = 0.01$ (treatment mean 56.33\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\lambda = 0.01$ yields one-tailed $p = 10/84 \approx 0.119$, two-tailed $p = 22/84 \approx 0.262$. All tests are non-significant at $\alpha = 0.05$; the narrower Null~A yields \emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\%), making the treatment means less extreme by comparison.
182	
183	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.
184	
185	\section{Step-wise Checkpoint Analysis for \texorpdfstring{$\lambda = 0.1$}{lambda = 0.1}}
186	\label{sec:appendix_stepwise}
187	
188	Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\%) pulls the three-seed mean to 57.00\%, within the null band ($p = 0.131$).
189	
190	\begin{table}[h]
191	\centering
192	\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\%) remains within the null band ($p = 0.131$, two-tailed permutation).}
193	\label{tab:stepwise_lambda01}
194	\vspace{2pt}
195	\small
196	\begin{tabular}{lcccc}
197	\toprule
198	Checkpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\
199	\midrule
200	16K steps & 55.5 & 56.0 & -- & 55.75 \\
201	20K steps & 55.0 & 56.0 & -- & 55.5 \\
202	22K steps & 60.5 & 56.5 & -- & 58.5 \\
203	24K steps & 52.5 & -- & -- & -- \\
204	26K steps & 53.5 & -- & -- & -- \\
205	28K steps & 54.5 & -- & -- & -- \\
206	30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\
207	\bottomrule
208	\end{tabular}
209	\end{table}
210	
211	Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$3\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). At 30K, the third seed ($s_2 = 54.5\%$) falls well within the null range, pulling the three-seed mean to 57.00\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
212	
213	
214	\section{Oracle SDF Refinement Details}
215	\label{sec:appendix_oracle}
216	
217	All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\times$ 40).
218	
219	\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.
220	
221	\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.
222	
223	\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space).
224	
225	
226	\section{Cross-Scene Validation: spatial\_bowl}
227	\label{sec:appendix_spatial_bowl}
228	
229	To test whether the absence of EE-only SDF benefit generalizes beyond the primary \texttt{object\_pudding} scene, we replicate the core comparison on \texttt{spatial\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.
230	
231	Table~\ref{tab:spatial_bowl} reports the results. The SDF condition ($\lambda = 0.005$) yields CAR of 11.5\% versus 12.0\% for LoRA-only, a $-$0.5\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\% vs.\ 51.5\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \texttt{object\_pudding} findings.
232	
233	\begin{table}[h]
234	\centering
235	\caption{Cross-scene validation on \texttt{spatial\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\,pp CAR difference is well within noise, consistent with the absence of SDF benefit observed on \texttt{object\_pudding}.}
236	\label{tab:spatial_bowl}
237	\vspace{2pt}
238	\small
239	\begin{tabular}{lcc}
240	\toprule
241	Condition & CAR (\%) & TSR (\%) \\
242	\midrule
243	LoRA-only & 12.0 & 49.0 \\
244	SDF $\lambda{=}0.005$ & 11.5 & 51.5 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	The substantially lower CAR on \texttt{spatial\_bowl} relative to \texttt{object\_pudding} (11--12\% vs.\ 54--57\%) reflects the greater scene difficulty: \texttt{spatial\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\Delta$CAR\,=\,$-$0.5\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.
250	
251	
252	\section{Evaluation Seed Robustness}
253	\label{sec:appendix_eval_seed}
254	
255	To verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\ref{tab:eval_seed_car} reports aggregate CAR and Table~\ref{tab:eval_seed_tsr} reports aggregate TSR.
256	
257	\begin{table}[h]
258	\centering
259	\caption{Aggregate CAR (\%) across evaluation seeds (200 episodes each). The LoRA vs.\ SDF $\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}
260	\label{tab:eval_seed_car}
261	\vspace{2pt}
262	\small
263	\begin{tabular}{lcccccc}
264	\toprule
265	& \multicolumn{4}{c}{Per-task CAR (\%)} & & \\
266	\cmidrule(lr){2-5}
267	Condition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\
268	\midrule
269	LoRA s0 (seed\,=\,7)   & 56 & 74 & 70 & 26 & 56.5 \\
270	LoRA s0 (seed\,=\,42)  & 60 & 70 & 68 & 28 & 56.5 \\
271	LoRA s0 (seed\,=\,123) & 52 & 74 & 66 & 20 & 53.0 \\
272	LoRA s0 mean $\pm$ std & 56.0$\pm$4.0 & 72.7$\pm$2.3 & 68.0$\pm$2.0 & 24.7$\pm$4.2 & 55.3$\pm$2.0 \\
273	\midrule
274	SDF $\lambda{=}0.1$ s0 (seed\,=\,7)   & 60 & 74 & 68 & 30 & 58.0 \\
275	SDF $\lambda{=}0.1$ s0 (seed\,=\,42)  & 64 & 74 & 74 & 24 & 59.0 \\
276	SDF $\lambda{=}0.1$ s0 (seed\,=\,123) & 62 & 76 & 74 & 22 & 58.5 \\
277	SDF $\lambda{=}0.1$ s0 (seed\,=\,256) & 60 & 72 & 66 & 30 & 57.0 \\
278	SDF $\lambda{=}0.1$ s0 mean $\pm$ std & 61.5$\pm$1.9 & 74.0$\pm$1.6 & 70.5$\pm$4.1 & 26.5$\pm$4.1 & 58.1$\pm$0.9 \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	\begin{table}[h]
284	\centering
285	\caption{Aggregate TSR (\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\,=\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}
286	\label{tab:eval_seed_tsr}
287	\vspace{2pt}
288	\small
289	\begin{tabular}{lcccccc}
290	\toprule
291	& \multicolumn{4}{c}{Per-task TSR (\%)} & & \\
292	\cmidrule(lr){2-5}
293	Condition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\
294	\midrule
295	LoRA s0 (seed\,=\,7)   & 32 & 74 & 42 & 58 & 51.5 \\
296	LoRA s0 (seed\,=\,42)  & 22 & 70 & 32 & 60 & 46.0 \\
297	LoRA s0 (seed\,=\,123) & 30 & 70 & 40 & 62 & 50.5 \\
298	LoRA s0 mean $\pm$ std & 28.0$\pm$5.3 & 71.3$\pm$2.3 & 38.0$\pm$5.3 & 60.0$\pm$2.0 & 49.3$\pm$3.0 \\
299	\midrule
300	SDF $\lambda{=}0.1$ s0 (seed\,=\,7)   & 28 & 78 & 44 & 60 & 52.5 \\
301	SDF $\lambda{=}0.1$ s0 (seed\,=\,42)  & 18 & 78 & 42 & 72 & 52.5 \\
302	SDF $\lambda{=}0.1$ s0 (seed\,=\,123) & 26 & 82 & 38 & 68 & 53.5 \\
303	SDF $\lambda{=}0.1$ s0 (seed\,=\,256) & 28 & 74 & 32 & 58 & 48.0 \\
304	SDF $\lambda{=}0.1$ s0 mean $\pm$ std & 25.0$\pm$4.8 & 78.0$\pm$3.3 & 39.0$\pm$5.4 & 64.5$\pm$6.6 & 51.6$\pm$2.4 \\
305	\bottomrule
306	\end{tabular}
307	\end{table}
308	
309	Across three matched evaluation seeds (7, 42, 123), the SDF $\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\Delta$CAR\,=\,+1.5, +2.5, +5.5\,pp). Cross-seed CAR standard deviation is 2.0\,pp for LoRA and 0.9\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.
310	
311	
312	\section{Training Details}
313	\label{sec:appendix_training}
314	
315	\paragraph{Architecture.}
316	We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
317	
318	\paragraph{Training schedule.}
319	Training proceeds in two phases:
320	\begin{itemize}
321	    \item \textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.
322	    \item \textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.
323	\end{itemize}
324	
325	\paragraph{Hyperparameters.}
326	\begin{table}[h]
327	\centering
328	\caption{Training hyperparameters.}
329	\label{tab:hyperparams}
330	\begin{tabular}{ll}
331	\toprule
332	Parameter & Value \\
333	\midrule
334	Base model & Pi0.5 (OpenPi, $\sim$3.5B parameters) \\
335	Optimizer & AdamW \\
336	Learning rate & $2.5 \times 10^{-5}$ (cosine decay to $\mathrm{lr}/10$) \\
337	Warmup steps & 1000 \\
338	Batch size & 32 \\
339	Total steps & 30000 \\
340	$\lambda_\mathrm{sdf}$ & \{0.005, 0.01, 0.1\} \\
341	$\lambda_\mathrm{ee}$ & 0.01 \\
342	SDF query points per step & 64 \\
343	SDF clamp $\delta$ & 0.05 m \\
344	Eikonal weight & 0.1 \\
345	LoRA rank (vision) & 16 \\
346	LoRA rank (action) & 32 \\
347	Phase 1 duration & 5000 steps \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\paragraph{Evaluation protocol.}
353	Each episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\sim}$5\% to ${\sim}$52\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).
354	
355	\paragraph{Data.}
356	We use the SafeLIBERO object\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.
357	
358	\paragraph{Computational resources.}
359	All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.
360	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "27759542-ad75-4d66-93b4-a1ce4a4def7f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.58\\% and standard deviation 1.93\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the absence of EE-only SDF benefit generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 12.0\\% for LoRA-only, a $-$0.5\\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the absence of SDF benefit observed on \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 12.0 & 49.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (11--12\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\\Delta$CAR\\,=\\,$-$0.5\\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\\ref{tab:eval_seed_car} reports aggregate CAR and Table~\\ref{tab:eval_seed_tsr} reports aggregate TSR.\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate CAR (\\%) across evaluation seeds (200 episodes each). The LoRA vs.\\ SDF $\\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}\n\\label{tab:eval_seed_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task CAR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 60 & 70 & 68 & 28 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,123) & 52 & 74 & 66 & 20 & 53.0 \\\\\nLoRA s0 mean $\\pm$ std & 56.0$\\pm$4.0 & 72.7$\\pm$2.3 & 68.0$\\pm$2.0 & 24.7$\\pm$4.2 & 55.3$\\pm$2.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 64 & 74 & 74 & 24 & 59.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 62 & 76 & 74 & 22 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 60 & 72 & 66 & 30 & 57.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 61.5$\\pm$1.9 & 74.0$\\pm$1.6 & 70.5$\\pm$4.1 & 26.5$\\pm$4.1 & 58.1$\\pm$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate TSR (\\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\\,=\\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}\n\\label{tab:eval_seed_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task TSR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 32 & 74 & 42 & 58 & 51.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 22 & 70 & 32 & 60 & 46.0 \\\\\nLoRA s0 (seed\\,=\\,123) & 30 & 70 & 40 & 62 & 50.5 \\\\\nLoRA s0 mean $\\pm$ std & 28.0$\\pm$5.3 & 71.3$\\pm$2.3 & 38.0$\\pm$5.3 & 60.0$\\pm$2.0 & 49.3$\\pm$3.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 28 & 78 & 44 & 60 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 18 & 78 & 42 & 72 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 26 & 82 & 38 & 68 & 53.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 28 & 74 & 32 & 58 & 48.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 25.0$\\pm$4.8 & 78.0$\\pm$3.3 & 39.0$\\pm$5.4 & 64.5$\\pm$6.6 & 51.6$\\pm$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross three matched evaluation seeds (7, 42, 123), the SDF $\\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\\Delta$CAR\\,=\\,+1.5, +2.5, +5.5\\,pp). Cross-seed CAR standard deviation is 2.0\\,pp for LoRA and 0.9\\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
      "numLines": 360,
      "startLine": 1,
      "totalLines": 360
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01Cceety6Pcrid7nqNXpFE41`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "e987a8bc-4b78-4789-b648-cbb3837f0859",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BULySjd88PmrywSsqAU75c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 23987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 66,
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

_source line 29 · 2026-05-28T06:54:58.382Z_

<details><summary>↩ Tool result · `toolu_01Cceety6Pcrid7nqNXpFE41`</summary>

```text
1	% contingency_claim3.tex — Three pre-written §6.3 paragraphs for λ=0.1 results.
2	% NOT \input'd into main.tex. Copy the matching scenario into claim3.tex
3	% when results arrive. Replace {MEAN}, {S0}, {S1} with actual numbers.
4	%
5	% Scenario selection (D033 thresholds):
6	%   B: CAR mean ≤ 57%    → full redundancy confirmed
7	%   C: CAR mean 57–60%   → inconclusive, flag 2/3 seeds
8	%   A: CAR mean > 60%    → dose-response evidence
9	%
10	% Also includes discussion + abstract patch bullets at the end.
11	
12	
13	%% ====================================================================
14	%% SCENARIO B — Full redundancy (CAR ≤ 57%)
15	%% ====================================================================
16	
17	% --- claim3 §6.3 paragraph ---
18	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
19	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%), within the null distribution (mean 54.5\%, $\sigma = 2.15$). SDF supervision is redundant with the demonstration signal across the full tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude (Level~A) but the structural mismatch between end-effector monitoring and full-body collision surfaces (Level~B). Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
20	
21	
22	%% ====================================================================
23	%% SCENARIO C — Inconclusive / gray zone (CAR 57–60%)
24	%% ====================================================================
25	
26	% --- claim3 §6.3 paragraph ---
27	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
28	At $\lambda = 0.1$, CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%), representing a suggestive but inconclusive separation from the null distribution (mean 54.5\%, $\sigma = 2.15$; Figure~\ref{fig:lambda_car}). The observed increase of {MEAN}$-$54.5\,=\,{DELTA}\,pp falls in a range where seed-to-seed variation and a genuine treatment effect are difficult to distinguish with two seeds. A third seed was in progress at submission; updated results will be provided upon completion. If the separation holds, it would indicate a dose-response threshold between $\lambda = 0.01$ and $\lambda = 0.1$, suggesting that Level~A signal masking (Section~\ref{sec:conclusion}) can be partially overcome at higher loss weights while the Level~B structural limitation of EE-only monitoring remains.
29	
30	
31	%% ====================================================================
32	%% SCENARIO A — Dose-response evidence (CAR > 60%)
33	%% ====================================================================
34	
35	% --- claim3 §6.3 paragraph ---
36	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
37	Increasing $\lambda$ to 0.1 raises CAR to {MEAN}\% (seeds: {S0}\%, {S1}\%), a {DELTA}\,pp increase beyond the null distribution mean of 54.5\% (Figure~\ref{fig:lambda_car}). This provides preliminary evidence for a dose-response relationship: SDF supervision becomes effective only when $\lambda$ exceeds a threshold between 0.01 and 0.1, below which the geometric gradient is masked by the action loss. In the two-level failure framework (Section~\ref{sec:conclusion}), this result indicates that Level~A signal masking has a breakpoint, while Level~B structural misalignment persists: oracle experiments with perfect SDF still reduce CAR below unrefined baselines regardless of signal strength, confirming that EE-only monitoring remains the binding constraint for full-body safety. Two of three planned seeds are reported; the third was in progress at submission, and updated results will be provided upon completion.
38	
39	
40	%% ====================================================================
41	%% DISCUSSION + ABSTRACT PATCH BULLETS (per scenario)
42	%% ====================================================================
43	
44	% --- Scenario B discussion patch ---
45	% In "Two-level failure" paragraph, replace the λ=0.1 placeholder with:
46	%   "At $\lambda = 0.1$ (20$\times$ higher dose), CAR remains within
47	%    the null range ({MEAN}\%), confirming that Level~A signal masking
48	%    is not the binding constraint. The failure is architectural:
49	%    EE-only supervision cannot prevent arm-body collisions regardless
50	%    of loss weight."
51	%
52	% In abstract, after "LoRA+SDF at $\lambda \in \{0.005, 0.01\}$":
53	%   Extend to: "$\lambda \in \{0.005, 0.01, 0.1\}$"
54	%   Change "($ p > 0.1$)" scope to cover all three λ values.
55	%
56	% In limitations, remove the λ=0.1 placeholder entirely.
57	
58	% --- Scenario C discussion patch ---
59	% In "Two-level failure" paragraph, replace the λ=0.1 placeholder with:
60	%   "At $\lambda = 0.1$, CAR shows a suggestive increase to {MEAN}\%
61	%    (2 seeds), but definitive assessment of whether Level~A masking
62	%    has a breakpoint awaits the third seed."
63	%
64	% In abstract, after "$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$)":
65	%   Add: "; $\lambda = 0.1$ shows a suggestive but inconclusive
66	%   increase ({MEAN}\%, 2 of 3 seeds)"
67	%
68	% In limitations, replace λ=0.1 placeholder with:
69	%   "The $\lambda = 0.1$ result ({MEAN}\%, 2 seeds) is suggestive
70	%    but underpowered; the third seed was in progress at submission."
71	
72	% --- Scenario A discussion patch ---
73	% In "Two-level failure" paragraph, replace the λ=0.1 placeholder with:
74	%   "At $\lambda = 0.1$, CAR increases to {MEAN}\% (2 seeds),
75	%    indicating that Level~A signal masking has a breakpoint between
76	%    $\lambda = 0.01$ and 0.1. Level~B misalignment remains: oracle
77	%    CAR stays below baselines regardless of signal strength."
78	%
79	% In abstract, after "$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$)":
80	%   Add: "; at $\lambda = 0.1$, CAR rises to {MEAN}\%, suggesting a
81	%   dose-response threshold (2 of 3 seeds; third pending)"
82	%
83	% In abstract, replace LAST SENTENCE with:
84	%   "EE-only geometric supervision is structurally limited by
85	%    representation-collision misalignment; at low loss weights
86	%    training signals are masked by the demonstration distribution,
87	%    but a dose-response threshold exists between $\lambda = 0.01$
88	%    and 0.1."
89	%
90	% In limitations, replace λ=0.1 placeholder with:
91	%   "The dose-response result at $\lambda = 0.1$ is based on 2 of 3
92	%    planned seeds; the third was in progress at submission."
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "88b17e35-7853-49c1-b680-59793d41a59e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex",
      "content": "% contingency_claim3.tex — Three pre-written §6.3 paragraphs for λ=0.1 results.\n% NOT \\input'd into main.tex. Copy the matching scenario into claim3.tex\n% when results arrive. Replace {MEAN}, {S0}, {S1} with actual numbers.\n%\n% Scenario selection (D033 thresholds):\n%   B: CAR mean ≤ 57%    → full redundancy confirmed\n%   C: CAR mean 57–60%   → inconclusive, flag 2/3 seeds\n%   A: CAR mean > 60%    → dose-response evidence\n%\n% Also includes discussion + abstract patch bullets at the end.\n\n\n%% ====================================================================\n%% SCENARIO B — Full redundancy (CAR ≤ 57%)\n%% ====================================================================\n\n% --- claim3 §6.3 paragraph ---\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,{MEAN}\\% (seeds: {S0}\\%, {S1}\\%), within the null distribution (mean 54.5\\%, $\\sigma = 2.15$). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude (Level~A) but the structural mismatch between end-effector monitoring and full-body collision surfaces (Level~B). Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\n%% ====================================================================\n%% SCENARIO C — Inconclusive / gray zone (CAR 57–60%)\n%% ====================================================================\n\n% --- claim3 §6.3 paragraph ---\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nAt $\\lambda = 0.1$, CAR\\,=\\,{MEAN}\\% (seeds: {S0}\\%, {S1}\\%), representing a suggestive but inconclusive separation from the null distribution (mean 54.5\\%, $\\sigma = 2.15$; Figure~\\ref{fig:lambda_car}). The observed increase of {MEAN}$-$54.5\\,=\\,{DELTA}\\,pp falls in a range where seed-to-seed variation and a genuine treatment effect are difficult to distinguish with two seeds. A third seed was in progress at submission; updated results will be provided upon completion. If the separation holds, it would indicate a dose-response threshold between $\\lambda = 0.01$ and $\\lambda = 0.1$, suggesting that Level~A signal masking (Section~\\ref{sec:conclusion}) can be partially overcome at higher loss weights while the Level~B structural limitation of EE-only monitoring remains.\n\n\n%% ====================================================================\n%% SCENARIO A — Dose-response evidence (CAR > 60%)\n%% ====================================================================\n\n% --- claim3 §6.3 paragraph ---\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ to 0.1 raises CAR to {MEAN}\\% (seeds: {S0}\\%, {S1}\\%), a {DELTA}\\,pp increase beyond the null distribution mean of 54.5\\% (Figure~\\ref{fig:lambda_car}). This provides preliminary evidence for a dose-response relationship: SDF supervision becomes effective only when $\\lambda$ exceeds a threshold between 0.01 and 0.1, below which the geometric gradient is masked by the action loss. In the two-level failure framework (Section~\\ref{sec:conclusion}), this result indicates that Level~A signal masking has a breakpoint, while Level~B structural misalignment persists: oracle experiments with perfect SDF still reduce CAR below unrefined baselines regardless of signal strength, confirming that EE-only monitoring remains the binding constraint for full-body safety. Two of three planned seeds are reported; the third was in progress at submission, and updated results will be provided upon completion.\n\n\n%% ====================================================================\n%% DISCUSSION + ABSTRACT PATCH BULLETS (per scenario)\n%% ====================================================================\n\n% --- Scenario B discussion patch ---\n% In \"Two-level failure\" paragraph, replace the λ=0.1 placeholder with:\n%   \"At $\\lambda = 0.1$ (20$\\times$ higher dose), CAR remains within\n%    the null range ({MEAN}\\%), confirming that Level~A signal masking\n%    is not the binding constraint. The failure is architectural:\n%    EE-only supervision cannot prevent arm-body collisions regardless\n%    of loss weight.\"\n%\n% In abstract, after \"LoRA+SDF at $\\lambda \\in \\{0.005, 0.01\\}$\":\n%   Extend to: \"$\\lambda \\in \\{0.005, 0.01, 0.1\\}$\"\n%   Change \"($ p > 0.1$)\" scope to cover all three λ values.\n%\n% In limitations, remove the λ=0.1 placeholder entirely.\n\n% --- Scenario C discussion patch ---\n% In \"Two-level failure\" paragraph, replace the λ=0.1 placeholder with:\n%   \"At $\\lambda = 0.1$, CAR shows a suggestive increase to {MEAN}\\%\n%    (2 seeds), but definitive assessment of whether Level~A masking\n%    has a breakpoint awaits the third seed.\"\n%\n% In abstract, after \"$\\lambda \\in \\{0.005, 0.01\\}$ ($p > 0.1$)\":\n%   Add: \"; $\\lambda = 0.1$ shows a suggestive but inconclusive\n%   increase ({MEAN}\\%, 2 of 3 seeds)\"\n%\n% In limitations, replace λ=0.1 placeholder with:\n%   \"The $\\lambda = 0.1$ result ({MEAN}\\%, 2 seeds) is suggestive\n%    but underpowered; the third seed was in progress at submission.\"\n\n% --- Scenario A discussion patch ---\n% In \"Two-level failure\" paragraph, replace the λ=0.1 placeholder with:\n%   \"At $\\lambda = 0.1$, CAR increases to {MEAN}\\% (2 seeds),\n%    indicating that Level~A signal masking has a breakpoint between\n%    $\\lambda = 0.01$ and 0.1. Level~B misalignment remains: oracle\n%    CAR stays below baselines regardless of signal strength.\"\n%\n% In abstract, after \"$\\lambda \\in \\{0.005, 0.01\\}$ ($p > 0.1$)\":\n%   Add: \"; at $\\lambda = 0.1$, CAR rises to {MEAN}\\%, suggesting a\n%   dose-response threshold (2 of 3 seeds; third pending)\"\n%\n% In abstract, replace LAST SENTENCE with:\n%   \"EE-only geometric supervision is structurally limited by\n%    representation-collision misalignment; at low loss weights\n%    training signals are masked by the demonstration distribution,\n%    but a dose-response threshold exists between $\\lambda = 0.01$\n%    and 0.1.\"\n%\n% In limitations, replace λ=0.1 placeholder with:\n%   \"The dose-response result at $\\lambda = 0.1$ is based on 2 of 3\n%    planned seeds; the third was in progress at submission.\"\n",
      "numLines": 93,
      "startLine": 1,
      "totalLines": 93
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
Now I need to also read the bib file and the main.tex to check references. Let me also search for the specific terms mentioned in the checklist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "8d3d7a8e-ee9f-49ca-becf-beabf5e6da5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

Now let me search for the specific terms and read the bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "d114b17c-3d45-47f7-b5cd-9dd0c90ced2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

<details open><summary>🔧 Tool call — Grep · `toolu_01SLqTndQX8cr4eQ3usSdaE6`</summary>

```json
{
  "pattern": "frozen episode|frozen rate",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "fe961333-8a2b-4b0e-b71c-b0c83ba59a13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

_source line 33 · 2026-05-28T06:55:04.611Z_

<details><summary>↩ Tool result · `toolu_01SLqTndQX8cr4eQ3usSdaE6`</summary>

```text
docs/paper/archive/analysis_claim3.tex:7:\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active collision avoidance.}
docs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:54:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:7:\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\max} < \tau_d$ (action collapse; Section~\ref{sec:metrics}). Pi0.5+A1 produces 0\% frozen episodes at 10K steps, so CAR$_\text{f}$ equals raw CAR.}
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/main.aux:85:\@writefile{lot}{\contentsline {table}{\numberline {4}{\ignorespaces Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}}{7}{table.caption.13}\protected@file@percent }
docs/paper/main.aux:86:\newlabel{tab:avoidance_source}{{4}{7}{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m}{table.caption.13}{}}
docs/paper/main.aux:138:\@writefile{lot}{\contentsline {table}{\numberline {5}{\ignorespaces Frozen rate (\% of episodes with $d_\mathrm  {max} < \tau _d$) across threshold values.}}{11}{table.caption.28}\protected@file@percent }
docs/paper/main.aux:139:\newlabel{tab:threshold_sensitivity}{{5}{11}{Frozen rate (\% of episodes with $d_\mathrm {max} < \tau _d$) across threshold values}{table.caption.28}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "c8ac90c4-2448-4a68-aa06-35c4d6695b68",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/archive/analysis_claim3.tex:7:\\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\\lambda \\in \\{0.005, 0.01\\}$. All fine-tuned models exhibit 0\\% frozen rate, confirming active collision avoidance.}\ndocs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:54:[Omitted long matching line]\ndocs/paper/archive/analysis_claim4.tex:7:\\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\\max} < \\tau_d$ (action collapse; Section~\\ref{sec:metrics}). Pi0.5+A1 produces 0\\% frozen episodes at 10K steps, so CAR$_\\text{f}$ equals raw CAR.}\ndocs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]\ndocs/paper/main.aux:85:\\@writefile{lot}{\\contentsline {table}{\\numberline {4}{\\ignorespaces Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}}{7}{table.caption.13}\\protected@file@percent }\ndocs/paper/main.aux:86:\\newlabel{tab:avoidance_source}{{4}{7}{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m}{table.caption.13}{}}\ndocs/paper/main.aux:138:\\@writefile{lot}{\\contentsline {table}{\\numberline {5}{\\ignorespaces Frozen rate (\\% of episodes with $d_\\mathrm  {max} < \\tau _d$) across threshold values.}}{11}{table.caption.28}\\protected@file@percent }\ndocs/paper/main.aux:139:\\newlabel{tab:threshold_sensitivity}{{5}{11}{Frozen rate (\\% of episodes with $d_\\mathrm {max} < \\tau _d$) across threshold values}{table.caption.28}{}}",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_01CekxBXyMSC9xrRBqDJ18g2`</summary>

```json
{
  "pattern": "fake safe",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "31435f9f-3f67-4d3a-b4fb-0c17eb037f81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

_source line 35 · 2026-05-28T06:55:05.571Z_

<details><summary>↩ Tool result · `toolu_01CekxBXyMSC9xrRBqDJ18g2`</summary>

```text
docs/paper/archive/analysis_claim2.tex:3:[Omitted long matching line]
docs/paper/archive/analysis_claim2.tex:7:\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
docs/paper/archive/analysis_claim2.tex:13:Method & TSR (\%) & CAR (\%) & Fake Safe (\%) & Refines/ep \\
docs/paper/archive/analysis_claim2.tex:27:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:1:\subsection{The Fake Safety Problem}\label{sec:fake_safety}
docs/paper/archive/analysis_claim1.tex:5:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:9:\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\text{f}$ excludes episodes with max displacement $< \tau_d = 0.1$\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}
docs/paper/archive/analysis_claim1.tex:15:Method & CAR (\%) & TSR (\%) & Fake Safe (\%) & Real Safe & CAR$_\text{f}$ (\%) \\
docs/paper/archive/analysis_claim1.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:38:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/references.bib:2:% Analysis paper on fake safety in VLA collision avoidance evaluation
docs/paper/main.aux:18:[Omitted long matching line]
docs/paper/main.aux:20:\newlabel{fig:teaser}{{1}{2}{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau _d$; Pi0+A1's 91.5\% safety score drops to ${\approx }$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right)}{figure.caption.2}{}}
docs/paper/main.aux:68:\@writefile{toc}{\contentsline {section}{\numberline {4}The Fake Safety Problem}{4}{section.4}\protected@file@percent }
docs/paper/main.aux:69:\newlabel{sec:fake_safety}{{4}{4}{The Fake Safety Problem}{section.4}{}}
docs/paper/main.aux:70:\newlabel{sec:anticorrelation}{{4}{4}{The Fake Safety Problem}{table.caption.9}{}}
docs/paper/main.aux:71:\@writefile{lot}{\contentsline {table}{\numberline {2}{\ignorespaces Fake safety decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \tau _d = 0.1$\,mm.}}{5}{table.caption.9}\protected@file@percent }
docs/paper/main.aux:72:\newlabel{tab:fake_safety}{{2}{5}{Fake safety decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \tau _d = 0.1$\,mm}{table.caption.9}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "db2ed122-b3e2-4808-9323-5938c2c91097",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/archive/analysis_claim2.tex:3:[Omitted long matching line]\ndocs/paper/archive/analysis_claim2.tex:7:\\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\\%, Full-FT 83.0\\%), and fake safe rates remain above 96\\%.}\ndocs/paper/archive/analysis_claim2.tex:13:Method & TSR (\\%) & CAR (\\%) & Fake Safe (\\%) & Refines/ep \\\\\ndocs/paper/archive/analysis_claim2.tex:27:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:1:\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}\ndocs/paper/archive/analysis_claim1.tex:5:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:9:\\caption{Fake safety decomposition across methods on SafeLIBERO. CAR$_\\text{f}$ excludes episodes with max displacement $< \\tau_d = 0.1$\\,mm. Fake safe rate is computed over safe (non-collision) episodes only.}\ndocs/paper/archive/analysis_claim1.tex:15:Method & CAR (\\%) & TSR (\\%) & Fake Safe (\\%) & Real Safe & CAR$_\\text{f}$ (\\%) \\\\\ndocs/paper/archive/analysis_claim1.tex:26:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:38:[Omitted long matching line]\ndocs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]\ndocs/paper/introduction.tex:12:[Omitted long matching line]\ndocs/paper/references.bib:2:% Analysis paper on fake safety in VLA collision avoidance evaluation\ndocs/paper/main.aux:18:[Omitted long matching line]\ndocs/paper/main.aux:20:\\newlabel{fig:teaser}{{1}{2}{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\\tau _d$; Pi0+A1's 91.5\\% safety score drops to ${\\approx }$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and dfCAR equals raw CAR (right)}{figure.caption.2}{}}\ndocs/paper/main.aux:68:\\@writefile{toc}{\\contentsline {section}{\\numberline {4}The Fake Safety Problem}{4}{section.4}\\protected@file@percent }\ndocs/paper/main.aux:69:\\newlabel{sec:fake_safety}{{4}{4}{The Fake Safety Problem}{section.4}{}}\ndocs/paper/main.aux:70:\\newlabel{sec:anticorrelation}{{4}{4}{The Fake Safety Problem}{table.caption.9}{}}\ndocs/paper/main.aux:71:\\@writefile{lot}{\\contentsline {table}{\\numberline {2}{\\ignorespaces Fake safety decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \\tau _d = 0.1$\\,mm.}}{5}{table.caption.9}\\protected@file@percent }\ndocs/paper/main.aux:72:\\newlabel{tab:fake_safety}{{2}{5}{Fake safety decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \\tau _d = 0.1$\\,mm}{table.caption.9}{}}",
    "numLines": 20
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Grep · `toolu_01CMsz1uMuMhhuFWmbAvhxRQ`</summary>

```json
{
  "pattern": "constraint-based planning|Constraint-based planning",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "53362b0e-090a-4ad7-82b2-e0aa83288e81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

_source line 37 · 2026-05-28T06:55:06.590Z_

<details><summary>↩ Tool result · `toolu_01CMsz1uMuMhhuFWmbAvhxRQ`</summary>

```text
docs/paper/introduction.tex:3:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "be205c52-ee5f-408c-a4b6-636782ac1524",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/introduction.tex:3:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_01BLHWF1qT36XDTLLkV5XrAY`</summary>

```json
{
  "pattern": "redundant",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "0beaaa24-69b4-4b19-a0e5-c6e99e1f1ea5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

_source line 39 · 2026-05-28T06:55:07.728Z_

<details><summary>↩ Tool result · `toolu_01BLHWF1qT36XDTLLkV5XrAY`</summary>

```text
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/discussion.tex:20:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:28:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:72:\placeholder{Pending: $\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\lambda$ range. Final narrative deferred until experimental results are available.}
docs/paper/contingency_claim3.tex:19:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "156782db-81ce-4365-a750-2e352a0ecefe",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/discussion.tex:20:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:28:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:72:\\placeholder{Pending: $\\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\\lambda$ range. Final narrative deferred until experimental results are available.}\ndocs/paper/contingency_claim3.tex:19:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_017URkfAf8a9n7NXUmjuzWhV`</summary>

```json
{
  "pattern": "20\\\\\\\\times|20\\$\\\\\\\\times|20\\{\\\\\\\\times\\}|20.*\\\\\\\\times|20×",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "260680a9-e6b7-4820-b1b3-ac219053d3ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

_source line 41 · 2026-05-28T06:55:09.060Z_

<details><summary>↩ Tool result · `toolu_017URkfAf8a9n7NXUmjuzWhV`</summary>

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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "e3b03dec-05c4-4d05-bb30-970e24f34ca5",
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

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Grep · `toolu_01NjK7qYzTVc8WjLtEx62wcu`</summary>

```json
{
  "pattern": "HazardArena|VLA-Risk|hazardarena|vlariskanon",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "0a4d7866-151d-4c76-8cf6-65972f835b98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

_source line 43 · 2026-05-28T06:55:11.349Z_

<details><summary>↩ Tool result · `toolu_01NjK7qYzTVc8WjLtEx62wcu`</summary>

```text
docs/paper/related_work.tex:15:[Omitted long matching line]
docs/paper/references.bib:237:@article{chen2026hazardarena,
docs/paper/references.bib:238:  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},
docs/paper/references.bib:244:@inproceedings{vlariskanon2026,
docs/paper/references.bib:245:  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "d32302d6-f4eb-4d48-8b8f-5cfe7696b92f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:15:[Omitted long matching line]\ndocs/paper/references.bib:237:@article{chen2026hazardarena,\ndocs/paper/references.bib:238:  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},\ndocs/paper/references.bib:244:@inproceedings{vlariskanon2026,\ndocs/paper/references.bib:245:  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Glob · `toolu_01FDaVSoziYNnxjuK6zXK3we`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "b2b6818f-3b12-489b-85fa-2bcb75af54d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013t1Kt75taoWFJH14mXMDwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 38488,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 38488
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

_source line 45 · 2026-05-28T06:55:11.590Z_

<details><summary>↩ Tool result · `toolu_01FDaVSoziYNnxjuK6zXK3we`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "64d31b1a-176d-4508-9146-28f3f3ef89fa",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 11,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Let me check the specific items more carefully. I need to:

1. Check "frozen episode", "frozen rate" - found in archive/ and main.aux. The archive files are expected. main.aux is auto-generated. Need to check if the .tex source files (non-archive) have these terms.

2. "fake safe" - found in archive/, introduction.tex:12, references.bib:2, and main.aux. Let me check each carefully.

3. "constraint-based planning" - found in introduction.tex:3. Let me check.


4. "redundant" - found in related_work.tex:12, discussion.tex:20. Need to check with full context.

5. "20×" / "20\times" - no matches found. Let me try searching for "20" combined with "times" to see if there's a different formatting pattern I'm missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "02548c21-44dd-47db-a2b8-9472a6590ab1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 47_

Let me get more detail on some of these findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "ba372bab-17be-4e12-8235-46a9beefe0a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 48_

<details open><summary>🔧 Tool call — Grep · `toolu_01Rthkdc8tNpZrFwBmekP4hQ`</summary>

```json
{
  "pattern": "20.{0,5}\\\\times",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "4731a66c-d25b-4b53-a7b4-3094d5eba066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 49 · 2026-05-28T06:55:20.338Z_

<details><summary>↩ Tool result · `toolu_01Rthkdc8tNpZrFwBmekP4hQ`</summary>

```text
docs/paper/claim3.tex:3:Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero action-collapsed episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
docs/paper/claim3.tex:32:[Omitted long matching line]
docs/paper/claim3.tex:46:\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. The $\lambda \in \{0.01, 0.1\}$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\times$ loss-weight range.}
docs/paper/contingency_claim3.tex:19:[Omitted long matching line]
docs/paper/contingency_claim3.tex:46:%   "At $\lambda = 0.1$ (20$\times$ higher dose), CAR remains within
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "40037bca-508d-4789-b8e6-518b332820d5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/claim3.tex:3:Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero action-collapsed episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\ndocs/paper/claim3.tex:32:[Omitted long matching line]\ndocs/paper/claim3.tex:46:\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. The $\\lambda \\in \\{0.01, 0.1\\}$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\\times$ loss-weight range.}\ndocs/paper/contingency_claim3.tex:19:[Omitted long matching line]\ndocs/paper/contingency_claim3.tex:46:%   \"At $\\lambda = 0.1$ (20$\\times$ higher dose), CAR remains within",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Grep · `toolu_01PEvLZQLQVPKKgpkvSgyh4o`</summary>

```json
{
  "pattern": "frozen rate|frozen episode",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-i": true,
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "88f4ad40-b29b-4ba6-bd57-a3b71df7d460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 51 · 2026-05-28T06:55:21.734Z_

<details><summary>↩ Tool result · `toolu_01PEvLZQLQVPKKgpkvSgyh4o`</summary>

```text
docs/paper/archive/analysis_claim3.tex:7:\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\lambda \in \{0.005, 0.01\}$. All fine-tuned models exhibit 0\% frozen rate, confirming active collision avoidance.}
docs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:54:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:7:\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\max} < \tau_d$ (action collapse; Section~\ref{sec:metrics}). Pi0.5+A1 produces 0\% frozen episodes at 10K steps, so CAR$_\text{f}$ equals raw CAR.}
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "6ccce7a9-6a4d-4325-86e7-477f154bd577",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/archive/analysis_claim3.tex:7:\\caption{Avoidance source attribution on SafeLIBERO (200 episodes per seed). LoRA fine-tuning without SDF produces CAR comparable to SDF-augmented variants; SDF adds no measurable CAR beyond LoRA-only at $\\lambda \\in \\{0.005, 0.01\\}$. All fine-tuned models exhibit 0\\% frozen rate, confirming active collision avoidance.}\ndocs/paper/archive/analysis_claim3.tex:26:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:54:[Omitted long matching line]\ndocs/paper/archive/analysis_claim4.tex:7:\\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\\max} < \\tau_d$ (action collapse; Section~\\ref{sec:metrics}). Pi0.5+A1 produces 0\\% frozen episodes at 10K steps, so CAR$_\\text{f}$ equals raw CAR.}\ndocs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Grep · `toolu_01Hf25ddFzmi9QhcVocNrb15`</summary>

```json
{
  "pattern": "fake safe",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "5bc7045a-144d-4dde-b31d-9fa3db079e69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 53 · 2026-05-28T06:55:22.682Z_

<details><summary>↩ Tool result · `toolu_01Hf25ddFzmi9QhcVocNrb15`</summary>

```text
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/archive/analysis_claim2.tex:3:[Omitted long matching line]
docs/paper/archive/analysis_claim2.tex:7:\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\%, Full-FT 83.0\%), and fake safe rates remain above 96\%.}
docs/paper/archive/analysis_claim2.tex:27:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:5:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:26:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:38:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "ed83295a-ed77-4f67-9789-138e1f80747c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/introduction.tex:12:[Omitted long matching line]\ndocs/paper/archive/analysis_claim2.tex:3:[Omitted long matching line]\ndocs/paper/archive/analysis_claim2.tex:7:\\caption{Oracle SDF refinement with ground-truth distance fields (160 episodes, 4 tasks $\\times$ 40). All three variants achieve lower CAR than unrefined baselines (LoRA 82.0\\%, Full-FT 83.0\\%), and fake safe rates remain above 96\\%.}\ndocs/paper/archive/analysis_claim2.tex:27:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:5:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:26:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:38:[Omitted long matching line]\ndocs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]",
    "numLines": 8
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Grep · `toolu_01PYWSrtdd1gZWZPi7fihafy`</summary>

```json
{
  "pattern": "constraint-based planning",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "e92c7cb3-c787-455d-b070-ea903427d27f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 55 · 2026-05-28T06:55:24.160Z_

<details><summary>↩ Tool result · `toolu_01PYWSrtdd1gZWZPi7fihafy`</summary>

```text
docs/paper/introduction.tex:3:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "30eef344-9b47-46a2-a875-8d8bd66d1fb9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/introduction.tex:3:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_01DR6HnF671oV48YMVupECCT`</summary>

```json
{
  "pattern": "redundant",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "d6c02722-6659-4270-8dcc-1da2c139fc9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 57 · 2026-05-28T06:55:25.190Z_

<details><summary>↩ Tool result · `toolu_01DR6HnF671oV48YMVupECCT`</summary>

```text
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/discussion.tex:20:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:28:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:72:\placeholder{Pending: $\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\lambda$ range. Final narrative deferred until experimental results are available.}
docs/paper/contingency_claim3.tex:19:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "59bc4f8f-57ad-47d1-a6f7-25faf6eae844",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/discussion.tex:20:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:28:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:72:\\placeholder{Pending: $\\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\\lambda$ range. Final narrative deferred until experimental results are available.}\ndocs/paper/contingency_claim3.tex:19:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Grep · `toolu_017qbHvcCDyE6FfwG4hTnLtg`</summary>

```json
{
  "pattern": "CAR-based|as currently practiced",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "32edbd9f-11a0-486e-b477-bc62ebcc1d82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 59 · 2026-05-28T06:55:26.530Z_

<details><summary>↩ Tool result · `toolu_017qbHvcCDyE6FfwG4hTnLtg`</summary>

```text
docs/paper/discussion.tex:3:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "88622ec0-6b83-4d84-a58b-ca5609cacd59",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:3:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Grep · `toolu_016io1P6Zzp8cyuECbzV23hu`</summary>

```json
{
  "pattern": "EE-only geometric supervision",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "bc8ef673-53ad-421f-8e50-5c01860e0e66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 61 · 2026-05-28T06:55:27.569Z_

<details><summary>↩ Tool result · `toolu_016io1P6Zzp8cyuECbzV23hu`</summary>

```text
docs/paper/abstract.tex:6:Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision does not significantly improve collision avoidance across the tested loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than EE-only geometric supervision.
docs/paper/contingency_claim3.tex:84:%   "EE-only geometric supervision is structurally limited by
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "e8070cb0-1610-4350-b688-abb60ca7e9e3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/abstract.tex:6:Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision does not significantly improve collision avoidance across the tested loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than EE-only geometric supervision.\ndocs/paper/contingency_claim3.tex:84:%   \"EE-only geometric supervision is structurally limited by",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Grep · `toolu_017MPKfyb3QukCtetHEeXg7U`</summary>

```json
{
  "pattern": "at the tested scale",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "57f3caed-8adb-4130-8a78-be340112e602",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5HxwYqtyrW1SefzQXR1wV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3041,
      "cache_read_input_tokens": 49939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3041
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

_source line 63 · 2026-05-28T06:55:28.859Z_

<details><summary>↩ Tool result · `toolu_017MPKfyb3QukCtetHEeXg7U`</summary>

```text
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/claim3.tex:7:\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$). All fine-tuned models exhibit 0\% action-collapse rate and displacement $>$\,0.37\,m.}
docs/paper/claim3.tex:26:[Omitted long matching line]
docs/paper/discussion.tex:20:[Omitted long matching line]
docs/paper/abstract.tex:5:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "fe8726cd-582d-45bf-ac99-e9bf1240f134",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/claim3.tex:7:\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$). All fine-tuned models exhibit 0\\% action-collapse rate and displacement $>$\\,0.37\\,m.}\ndocs/paper/claim3.tex:26:[Omitted long matching line]\ndocs/paper/discussion.tex:20:[Omitted long matching line]\ndocs/paper/abstract.tex:5:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

````text
Let me now check the specific issues I've found:

1. **Frozen episodes/frozen rate**: Only in `archive/` files (which are not included) and `main.aux` (auto-generated). The active .tex files are clean. **PASS**

2. **"fake safe"**: Found in `introduction.tex:12` - which is the first introduction of the term (colloquially, "fake safety"). This is the ONE place it should appear as a non-formal synonym. Let me also check if it appears elsewhere in non-archive files. The other occurrences are in `archive/` and `references.bib:2` (a comment). 

The `main.aux` file is auto-generated, so I should ignore it. The section labels like `\label{sec:fake_safety}` and `\ref{sec:fake_safety}` are just identifiers and need to stay. Looking at the active .tex files, the only real occurrence is in `introduction.tex:12` where it's introduced colloquially, which is appropriate, and there's a harmless comment in the bibliography file.

But I'm noticing something odd in the compiled output—the `main.aux` shows the section title as "The Fake Safety Problem," but I need to check what the actual source file `claim1.tex` says to see if there's a mismatch between the label and the section title.

Looking at the source, `claim1.tex` has `\section{The Action-Collapsed Safety Problem}\label{sec:fake_safety}`, which is correct. The `main.aux` file is just stale from a previous compilation, so the source itself is fine.

I'm also noticing the figure caption in `main.aux` references "frozen robot," but the current `introduction.tex` says "action-collapsed robot" instead—again, the `.aux` file is outdated and doesn't reflect the current source.

Checking `claim1.tex` more carefully, the caption correctly uses "action-collapse" terminology and describes how dfCAR filters episodes based on displacement thresholds, which matches what I'm seeing in the source. Everything checks out. I'm noticing another discrepancy where the compiled auxiliary file still shows "frozen rate" while the source file claim3.tex correctly uses "action-collapse rate" in the same table caption—this will get corrected on the next compilation pass.

Now checking the third issue about "constraint-based planning" in the introduction. The citation actually attributes this term to CAPE (yang2025cape), not SafeVLA, so this isn't the mislabeling I was looking for. Let me trace through this more carefully to see if there's an actual violation of the task requirements. Looking at the related_work.tex and discussion.tex sections, both correctly use "Constrained optimization" when describing SafeVLA's approach with Lagrangian optimization. The remaining issue is in introduction.tex where "constraint-based planning" is attributed to CAPE, which is the correct reference, so that citation is actually fine. Looking at the related_work.tex excerpt, CAPE is specifically described as using "diffusion-process collision costs" rather than constraint-based planning, so the introduction.tex reference to "constraint-based planning" for CAPE appears to be a terminology mismatch that should be corrected to align with how it's actually characterized in the related work section. the introduction. SafeVLA is being cited under "SDF-augmented training" when the related work clearly states it uses constrained MDP with Lagrangian optimization instead of SDF as an auxiliary loss. So either the introduction citation is misplaced, or I'm misunderstanding whether SafeVLA actually incorporates SDF in some capacity despite the related work's phrasing suggesting it doesn't. I'm realizing the user's checklist specifically targets "Constraint-based planning" as a mislabeling for SafeVLA, but in the introduction SafeVLA is actually grouped under "SDF-augmented training" instead. The related_work.tex correctly categorizes it as "Constrained optimization." So the specific issue the checklist warns about isn't present—though there is a "constraint-based planning" term used for CAPE in introduction.tex, which may or may not be intentional. Looking at the checklist items, I need to verify that SafeVLA is consistently described as "Constrained optimization" across related_work and discussion sections, and check whether "constraint-based planning" appears elsewhere as a residual term. The introduction mentions this phrase when describing CAPE, so I should flag whether that's acceptable or if it needs to be cleaned up based on what the user is looking for. The introduction incorrectly labels SafeVLA as "SDF-augmented training," but the related work clearly states it uses constrained MDP with Lagrangian optimization instead—explicitly contrasting it with SDF auxiliary loss. I need to fix this mischaracterization by recategorizing SafeVLA in the introduction to match its actual approach. I need to recategorize the related work to be consistent with how the paper distinguishes its own approach. Since the paper uses SDF-augmented training, SafeVLA should be labeled as constrained optimization instead. I'll also align CAPE with diffusion-based collision costs to match the related work section. The corrected sentence should read: "Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization, diffusion-based collision costs, and collision-free demonstrations. Our SDF-augmented Pi0 reaches 91.5% CAR across 800 episodes." I'm realizing the original sentence incorrectly attributes SDF-augmented training to SafeVLA when it actually uses constrained optimization instead. CAPE uses diffusion-process collision costs, not constraint-based planning. I need to fix these attributions, but I'm stuck on how to handle the sentence structure since removing the SDF reference creates a gap before mentioning "Our SDF-augmented Pi0" in the next sentence. I could either list all three corrected approaches or restructure to keep SDF as a general method while fixing the specific citations. I'm refining the citations to be more precise—swapping out the generic labels for the actual methods each paper uses. SafeVLA uses constrained optimization, CAPE employs diffusion-process collision costs, and CoFreeEvla provides collision-free demonstrations. The paper's own SDF-augmented approach gets introduced separately in the next sentence, so this keeps things clean and aligned with the related work section.

Now I'm looking at the "redundant" finding in the related work file to understand its context better. to pathway~(a)
  
This has "at the tested scale" qualifier. ✓

- `discussion.tex:20`: From the earlier read:
  ```
  Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data is an evaluation-methodology insight
  ```
  This has "at the tested scale" qualifier. ✓

Both uses of "redundant" have "at the tested scale" qualifier. **PASS**

5. **"20×" usage**: Found in claim3.tex lines 3, 32, and 46. That's exactly 3 occurrences. Let me verify:
- Line 3: "across a 20$\times$ range of loss weights" - first mention defining the range
- Line 32: "because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance" - key argument
- Line 46: "across a 20$\times$ loss-weight range" - figure caption

Also in contingency_claim3.tex:19 and 46, but that file is not \input'd. **PASS** - exactly 3 occurrences in active files.

6. **HazardArena and VLA-Risk**: Found in related_work.tex:15 and references.bib:237,244. Both systems are mentioned together in the related work section, and both have corresponding bibliography entries. **PASS**

Now I need to verify all citations are properly formatted and check if there are any other constraint violations I might have missed. The TSR value for Pi0+A1 is actually 0%, not 70-80%, which the text honestly acknowledges as a limitation of the collapsed baseline. Now I'm checking numerical consistency across the paper—the threshold values of below 1 μm for collapsed episodes and above 200 mm for active episodes appear consistently across the abstract, methods, claims, and appendix sections, so that checks out.

Moving on to scope limitations, I'm verifying that the paper properly qualifies its claims. The discussion acknowledges that CAR-based VLA evaluation on SafeLIBERO is structurally unreliable, the abstract specifies that findings relate to demonstration data versus geometric supervision, and Claim 3 appropriately restricts its conclusions to the tested scale and range. All the major claims have appropriate scope qualifiers in place.

Now I'm checking the citation references against the bibliography to ensure completeness. I found two inconsistencies in how methods are characterized: SafeVLA is described as "SDF-augmented training" in the introduction but categorized as "constrained optimization" in related work, and CAPE is labeled as "constraint-based planning" when related work identifies it as using "diffusion-process collision costs." Everything else checks out, so I need to verify all citations have corresponding bibliography entries.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "978bdec8-6efe-4e92-aca0-f2e42e15e2bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTVXzopoSs9ZXcEzefSmu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3076,
      "cache_read_input_tokens": 52980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3076
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

_source line 65_

Found some issues. Let me verify citations and check remaining items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "7bf4e2eb-a564-4be2-98a7-a2ff2de0397b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTVXzopoSs9ZXcEzefSmu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3076,
      "cache_read_input_tokens": 52980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3076
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

_source line 66_

<details open><summary>🔧 Tool call — Grep · `toolu_019MToWomZ7gihcDaDZbkdso`</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "e81bd2de-1dad-4356-b61c-d23c72f1a98e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTVXzopoSs9ZXcEzefSmu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3076,
      "cache_read_input_tokens": 52980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3076
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

_source line 67 · 2026-05-28T06:57:31.336Z_

<details><summary>↩ Tool result · `toolu_019MToWomZ7gihcDaDZbkdso`</summary>

```text
docs/paper/related_work.tex:4:[Omitted long matching line]
docs/paper/related_work.tex:7:[Omitted long matching line]
docs/paper/related_work.tex:10:[Omitted long matching line]
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/related_work.tex:15:[Omitted long matching line]
docs/paper/experimental_framework.tex:7:We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.
docs/paper/experimental_framework.tex:29:\paragraph{Base architectures.} We evaluate two VLA models from the Pi0 family~\cite{black2024pi0}. \textbf{Pi0} (${\sim}$3B parameters) uses a PaliGemma vision-language encoder paired with a dedicated action expert that generates continuous actions via flow matching~\cite{lipman2023flow}. \textbf{Pi0.5} extends this architecture to ${\sim}$3.5B parameters with broader pre-training data, and serves as a stronger baseline that exhibits less action collapse.
docs/paper/method.tex:5:[Omitted long matching line]
docs/paper/method.tex:40:We augment LoRA-adapted~\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\ref{sec:appendix_training}, Table~\ref{tab:hyperparams}). The total loss is:
docs/paper/archive/analysis_claim2.tex:31:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:3:[Omitted long matching line]
docs/paper/_archive/experiments.tex:7:[Omitted long matching line]
docs/paper/_archive/method.tex:11:Our base model is $\pi_0$~\cite{black2024pi0}, a 3.5B-parameter flow-matching VLA comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. The action expert produces a sequence of action tokens through an output projection $W_{\mathrm{out}} \in \mathbb{R}^{1024 \times 32}$ that maps from the expert's hidden dimension to the action token space.
docs/paper/appendix.tex:316:We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
docs/paper/introduction.tex:3:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/introduction.tex:14:We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "e5acbc70-de15-4247-ae8f-c70d8c39d47a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:4:[Omitted long matching line]\ndocs/paper/related_work.tex:7:[Omitted long matching line]\ndocs/paper/related_work.tex:10:[Omitted long matching line]\ndocs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/related_work.tex:15:[Omitted long matching line]\ndocs/paper/experimental_framework.tex:7:We conduct all experiments on SafeLIBERO~\\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\\cite{liu2023libero}. SafeLIBERO augments standard manipulation benchmarks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety.\ndocs/paper/experimental_framework.tex:29:\\paragraph{Base architectures.} We evaluate two VLA models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$3B parameters) uses a PaliGemma vision-language encoder paired with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} extends this architecture to ${\\sim}$3.5B parameters with broader pre-training data, and serves as a stronger baseline that exhibits less action collapse.\ndocs/paper/method.tex:5:[Omitted long matching line]\ndocs/paper/method.tex:40:We augment LoRA-adapted~\\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\\ref{sec:appendix_training}, Table~\\ref{tab:hyperparams}). The total loss is:\ndocs/paper/archive/analysis_claim2.tex:31:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:3:[Omitted long matching line]\ndocs/paper/_archive/experiments.tex:7:[Omitted long matching line]\ndocs/paper/_archive/method.tex:11:Our base model is $\\pi_0$~\\cite{black2024pi0}, a 3.5B-parameter flow-matching VLA comprising a PaliGemma vision-language encoder (Gemma 2B) and a Gemma 300M action expert. The action expert produces a sequence of action tokens through an output projection $W_{\\mathrm{out}} \\in \\mathbb{R}^{1024 \\times 32}$ that maps from the expert's hidden dimension to the action token space.\ndocs/paper/appendix.tex:316:We use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\ndocs/paper/introduction.tex:3:[Omitted long matching line]\ndocs/paper/introduction.tex:12:[Omitted long matching line]\ndocs/paper/introduction.tex:14:We present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.",
    "numLines": 17
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01VzyzJMxEGBwtwiTwK68fSK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "f080cd58-fce7-4ee4-908b-5b911fe5896a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTVXzopoSs9ZXcEzefSmu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3076,
      "cache_read_input_tokens": 52980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3076
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

_source line 69 · 2026-05-28T06:57:31.905Z_

<details><summary>↩ Tool result · `toolu_01VzyzJMxEGBwtwiTwK68fSK`</summary>

```text
1	% The Safety Illusion — References
2	% Analysis paper on fake safety in VLA collision avoidance evaluation
3	% Generated: 2026-05-24
4	
5	% ===== VLA Foundation Models =====
6	
7	@article{black2024pi0,
8	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
9	  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},
10	  journal={arXiv preprint arXiv:2410.24164},
11	  year={2024}
12	}
13	
14	@inproceedings{kim2024openvla,
15	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
16	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},
17	  booktitle={Conference on Robot Learning (CoRL)},
18	  year={2024}
19	}
20	
21	@inproceedings{brohan2023rt2,
22	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
23	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
24	  booktitle={Conference on Robot Learning (CoRL)},
25	  year={2023}
26	}
27	
28	% ===== Collision-Aware VLA Methods =====
29	
30	@article{hu2025vlsa,
31	  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
32	  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},
33	  journal={arXiv preprint arXiv:2512.11891},
34	  year={2025}
35	}
36	
37	@inproceedings{zhang2025safevla,
38	  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
39	  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},
40	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
41	  year={2025}
42	}
43	
44	@article{cofreeevla2026,
45	  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},
46	  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},
47	  journal={arXiv preprint arXiv:2601.21712},
48	  year={2026}
49	}
50	
51	@article{spalter2024ikinqp,
52	  title={Towards Online Safety Corrections for Robotic Manipulation Policies},
53	  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},
54	  journal={arXiv preprint arXiv:2409.08233},
55	  year={2024}
56	}
57	
58	@inproceedings{li2024langguided,
59	  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},
60	  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},
61	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
62	  year={2025}
63	}
64	
65	@article{yang2025cape,
66	  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},
67	  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},
68	  journal={arXiv preprint arXiv:2511.22773},
69	  year={2025}
70	}
71	
72	% ===== Safety in Diffusion Planning =====
73	
74	@inproceedings{xiao2025safediffuser,
75	  title={{SafeDiffuser}: Safe Planning with Diffusion Probabilistic Models},
76	  author={Xiao, Wei and Wang, Tsun-Hsuan and Gan, Chuang and Hasani, Ramin and Lechner, Mathias and Rus, Daniela},
77	  booktitle={International Conference on Learning Representations (ICLR)},
78	  year={2025}
79	}
80	
81	% ===== SDF in Robotics =====
82	
83	@inproceedings{park2019deepsdf,
84	  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},
85	  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},
86	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
87	  year={2019}
88	}
89	
90	@inproceedings{ortiz2022isdf,
91	  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},
92	  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\"o}fer, Michael and Mukadam, Mustafa},
93	  booktitle={Robotics: Science and Systems (RSS)},
94	  year={2022}
95	}
96	
97	@article{zhi2021diffco,
98	  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},
99	  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},
100	  journal={IEEE Transactions on Robotics},
101	  volume={38},
102	  number={5},
103	  pages={2668--2685},
104	  year={2022}
105	}
106	
107	@inproceedings{huang2023voxposer,
108	  title={{VoxPoser}: Composable {3D} Value Maps for Robotic Manipulation with Language Models},
109	  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},
110	  booktitle={Conference on Robot Learning (CoRL)},
111	  year={2023}
112	}
113	
114	% ===== Benchmarks and Training =====
115	
116	@inproceedings{liu2023libero,
117	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
118	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
119	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
120	  year={2023}
121	}
122	
123	@inproceedings{lipman2023flow,
124	  title={Flow Matching for Generative Modeling},
125	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
126	  booktitle={International Conference on Learning Representations (ICLR)},
127	  year={2023}
128	}
129	
130	% ===== Evaluation Reliability =====
131	
132	@inproceedings{gururangan2018annotation,
133	  title={Annotation Artifacts in Natural Language Inference Data},
134	  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},
135	  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
136	  year={2018}
137	}
138	
139	@inproceedings{karwowski2024goodhart,
140	  title={Goodhart's Law in Reinforcement Learning},
141	  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},
142	  booktitle={International Conference on Learning Representations (ICLR)},
143	  year={2024}
144	}
145	
146	% ===== Diffusion Policy =====
147	
148	@inproceedings{chi2023diffusionpolicy,
149	  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
150	  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
151	  booktitle={Robotics: Science and Systems (RSS)},
152	  year={2023}
153	}
154	
155	% ===== Configuration/Robot-Body SDF =====
156	
157	@inproceedings{li2024cdf,
158	  title={Configuration Space Distance Fields for Manipulation Planning},
159	  author={Li, Yiming and Chi, Xuemin and Razmjoo, Amirreza and Calinon, Sylvain},
160	  booktitle={Robotics: Science and Systems (RSS)},
161	  year={2024}
162	}
163	
164	@inproceedings{li2024rdf,
165	  title={Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation},
166	  author={Li, Yiming and Zhang, Yan and Razmjoo, Amirreza and Calinon, Sylvain},
167	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
168	  year={2024}
169	}
170	
171	% ===== SDF in Robotics (additional) =====
172	
173	@inproceedings{vasilopoulos2023ramp,
174	  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},
175	  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},
176	  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
177	  year={2023}
178	}
179	
180	@article{chen2026cssdfnet,
181	  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},
182	  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},
183	  journal={arXiv preprint arXiv:2603.18669},
184	  year={2026}
185	}
186	
187	@article{jacquet2025neuralnmpc,
188	  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},
189	  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},
190	  journal={The International Journal of Robotics Research},
191	  year={2025}
192	}
193	
194	% ===== 3D-Aware VLA Methods =====
195	
196	@article{depthvla2025,
197	  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},
198	  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},
199	  journal={arXiv preprint arXiv:2510.13375},
200	  year={2025}
201	}
202	
203	@article{li2025qdepth,
204	  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},
205	  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},
206	  journal={arXiv preprint arXiv:2510.14836},
207	  year={2025}
208	}
209	
210	@article{li2025spatialforcing,
211	  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},
212	  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},
213	  journal={arXiv preprint arXiv:2510.12276},
214	  year={2025}
215	}
216	
217	% ===== Parameter-Efficient Fine-Tuning =====
218	
219	@inproceedings{hu2022lora,
220	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
221	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
222	  booktitle = {International Conference on Learning Representations (ICLR)},
223	  year      = {2022},
224	}
225	
226	% ===== VLA Safety Survey =====
227	
228	@article{li2026vlasafety,
229	  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
230	  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},
231	  journal={arXiv preprint arXiv:2604.23775},
232	  year={2026}
233	}
234	
235	% ===== VLA Safety Evaluation Benchmarks =====
236	
237	@article{chen2026hazardarena,
238	  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},
239	  author={Chen, Zixing and Gao, Yifeng and Wang, Li and Zhao, Yunhan and Liu, Yi and Li, Jiayu and Zheng, Xiang and Wu, Zuxuan and Wang, Cong and Ma, Xingjun and Jiang, Yu-Gang},
240	  journal={arXiv preprint arXiv:2604.12447},
241	  year={2026}
242	}
243	
244	@inproceedings{vlariskanon2026,
245	  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},
246	  author={Anonymous},
247	  booktitle={International Conference on Learning Representations (ICLR)},
248	  year={2026},
249	  note={Under review}
250	}
251	
252	% ===== Action Collapse =====
253	
254	@article{dong2025conditioning,
255	  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},
256	  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},
257	  journal={arXiv preprint arXiv:2505.11123},
258	  year={2025}
259	}
260	
261	% ===== Evaluation Methodology =====
262	
263	@article{snyder2026beyond,
264	  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},
265	  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},
266	  journal={arXiv preprint arXiv:2603.13616},
267	  year={2026}
268	}
269	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "61123181-99cf-4a26-b85d-73098ddda531",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
      "content": "% The Safety Illusion — References\n% Analysis paper on fake safety in VLA collision avoidance evaluation\n% Generated: 2026-05-24\n\n% ===== VLA Foundation Models =====\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Collision-Aware VLA Methods =====\n\n@article{hu2025vlsa,\n  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},\n  journal={arXiv preprint arXiv:2512.11891},\n  year={2025}\n}\n\n@inproceedings{zhang2025safevla,\n  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cofreeevla2026,\n  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},\n  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},\n  journal={arXiv preprint arXiv:2601.21712},\n  year={2026}\n}\n\n@article{spalter2024ikinqp,\n  title={Towards Online Safety Corrections for Robotic Manipulation Policies},\n  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},\n  journal={arXiv preprint arXiv:2409.08233},\n  year={2024}\n}\n\n@inproceedings{li2024langguided,\n  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},\n  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2025}\n}\n\n@article{yang2025cape,\n  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},\n  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},\n  journal={arXiv preprint arXiv:2511.22773},\n  year={2025}\n}\n\n% ===== Safety in Diffusion Planning =====\n\n@inproceedings{xiao2025safediffuser,\n  title={{SafeDiffuser}: Safe Planning with Diffusion Probabilistic Models},\n  author={Xiao, Wei and Wang, Tsun-Hsuan and Gan, Chuang and Hasani, Ramin and Lechner, Mathias and Rus, Daniela},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n% ===== SDF in Robotics =====\n\n@inproceedings{park2019deepsdf,\n  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},\n  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2019}\n}\n\n@inproceedings{ortiz2022isdf,\n  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},\n  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\\\"o}fer, Michael and Mukadam, Mustafa},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2022}\n}\n\n@article{zhi2021diffco,\n  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},\n  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},\n  journal={IEEE Transactions on Robotics},\n  volume={38},\n  number={5},\n  pages={2668--2685},\n  year={2022}\n}\n\n@inproceedings{huang2023voxposer,\n  title={{VoxPoser}: Composable {3D} Value Maps for Robotic Manipulation with Language Models},\n  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Benchmarks and Training =====\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ===== Evaluation Reliability =====\n\n@inproceedings{gururangan2018annotation,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year={2018}\n}\n\n@inproceedings{karwowski2024goodhart,\n  title={Goodhart's Law in Reinforcement Learning},\n  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% ===== Diffusion Policy =====\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n% ===== Configuration/Robot-Body SDF =====\n\n@inproceedings{li2024cdf,\n  title={Configuration Space Distance Fields for Manipulation Planning},\n  author={Li, Yiming and Chi, Xuemin and Razmjoo, Amirreza and Calinon, Sylvain},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{li2024rdf,\n  title={Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation},\n  author={Li, Yiming and Zhang, Yan and Razmjoo, Amirreza and Calinon, Sylvain},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024}\n}\n\n% ===== SDF in Robotics (additional) =====\n\n@inproceedings{vasilopoulos2023ramp,\n  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},\n  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},\n  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},\n  year={2023}\n}\n\n@article{chen2026cssdfnet,\n  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},\n  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},\n  journal={arXiv preprint arXiv:2603.18669},\n  year={2026}\n}\n\n@article{jacquet2025neuralnmpc,\n  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},\n  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},\n  journal={The International Journal of Robotics Research},\n  year={2025}\n}\n\n% ===== 3D-Aware VLA Methods =====\n\n@article{depthvla2025,\n  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},\n  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},\n  journal={arXiv preprint arXiv:2510.13375},\n  year={2025}\n}\n\n@article{li2025qdepth,\n  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},\n  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},\n  journal={arXiv preprint arXiv:2510.14836},\n  year={2025}\n}\n\n@article{li2025spatialforcing,\n  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},\n  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},\n  journal={arXiv preprint arXiv:2510.12276},\n  year={2025}\n}\n\n% ===== Parameter-Efficient Fine-Tuning =====\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n}\n\n% ===== VLA Safety Survey =====\n\n@article{li2026vlasafety,\n  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},\n  journal={arXiv preprint arXiv:2604.23775},\n  year={2026}\n}\n\n% ===== VLA Safety Evaluation Benchmarks =====\n\n@article{chen2026hazardarena,\n  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},\n  author={Chen, Zixing and Gao, Yifeng and Wang, Li and Zhao, Yunhan and Liu, Yi and Li, Jiayu and Zheng, Xiang and Wu, Zuxuan and Wang, Cong and Ma, Xingjun and Jiang, Yu-Gang},\n  journal={arXiv preprint arXiv:2604.12447},\n  year={2026}\n}\n\n@inproceedings{vlariskanon2026,\n  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},\n  author={Anonymous},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  note={Under review}\n}\n\n% ===== Action Collapse =====\n\n@article{dong2025conditioning,\n  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},\n  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},\n  journal={arXiv preprint arXiv:2505.11123},\n  year={2025}\n}\n\n% ===== Evaluation Methodology =====\n\n@article{snyder2026beyond,\n  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},\n  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},\n  journal={arXiv preprint arXiv:2603.13616},\n  year={2026}\n}\n",
      "numLines": 269,
      "startLine": 1,
      "totalLines": 269
    }
  }
}
```

</details>

---

### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
Now let me extract all citation keys from the active .tex files and check them against the bib file.

From the grep results, the citation keys used in active .tex files (excluding archive/) are:

From introduction.tex:
- li2026vlasafety
- hu2025vlsa
- zhang2025safevla
- yang2025cape
- cofreeevla2026
- black2024pi0
- karwowski2024goodhart

From method.tex:
- hu2025vlsa
- black2024pi0
- lipman2023flow
- hu2022lora

From experimental_framework.tex:


- hu2025vlsa
- liu2023libero
- black2024pi0
- lipman2023flow

From related_work.tex, I'm seeing a much larger set of citations including brohan2023rt2, chi2023diffusionpolicy, kim2024openvla, several spatial and depth-related papers, and additional safety and vision-language papers like xiao2025safediffuser and park2019deepsdf.

Now I'm checking the appendix and other sections—there are more citations scattered through appendix.tex, claim files, and discussion.tex, though some sections rely more on \ref commands than direct citations. I'm verifying that all the keys I've found actually exist in the bibliography, checking entries like li2026vlasafety, hu2025vlsa, zhang2025safevla, and others against what's available.

Continuing through the verification list...

now checking the point cloud citations. All those entries are accounted for too. With the bibliography complete, I'm moving on to review the actual content and I've spotted an inconsistency in the introduction—SafeVLA is being described with the wrong methodology label, when it should reflect constrained optimization instead. I'm noticing the related_work section uses "diffusion-process collision costs" for CAPE, while the intro currently says "constraint-based planning." I should align the terminology. "Constrained optimization" works well for SafeVLA since it appears in both places, but for CAPE I need to decide between the technical "diffusion-process collision costs" or something more readable like "collision-cost planning." Let me stick with the related_work phrasing for consistency, though I'm trying to keep the intro sentence clean and accessible while accurately representing what each method does. I'm settling on matching the related work terminology exactly—"constrained optimization" for SafeVLA and "diffusion-process collision costs" for CAPE. This keeps things consistent across sections and avoids the problematic "SDF-augmented training" framing that conflates their method with SafeVLA's approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "0ad8021d-e615-4026-8228-9ec6098830af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKyufX42PgaDuNq2B8f8Yd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12650,
      "cache_read_input_tokens": 56056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12650
      },
      "output_tokens": 18,
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

_source line 71_

Found one issue to fix. In `introduction.tex:3`, SafeVLA is incorrectly labeled as "SDF-augmented training" (should be "constrained optimization"), and CAPE is labeled "constraint-based planning" (should match related_work.tex's "diffusion-process collision costs"). Fixing now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "09f20e00-bda4-4e03-8a44-1061c08b1278",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKyufX42PgaDuNq2B8f8Yd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12650,
      "cache_read_input_tokens": 56056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12650
      },
      "output_tokens": 18,
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

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01UGEFTDGhMEi1Lq8x42Mpr8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}.",
  "new_string": "Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization~\\cite{zhang2025safevla}, diffusion-process collision costs~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "7c394490-204a-474a-ba3a-3ee976598c65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKyufX42PgaDuNq2B8f8Yd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12650,
      "cache_read_input_tokens": 56056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12650
      },
      "output_tokens": 18,
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

_source line 73 · 2026-05-28T06:58:06.893Z_

<details><summary>↩ Tool result · `toolu_01UGEFTDGhMEi1Lq8x42Mpr8`</summary>

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
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "e463d0ed-b30c-45d2-9d38-5a569573a833",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}.",
    "newString": "Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization~\\cite{zhang2025safevla}, diffusion-process collision costs~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}.",
    "originalFile": "\\section{Introduction}\\label{sec:intro}\n\nCollision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig1_teaser}\n\\caption{The action-collapsed safety problem in VLA collision avoidance evaluation. Standard CAR classifies an action-collapsed robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\\tau_d$; Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and dfCAR equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not (Figure~\\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\\% exhibit displacement below 0.1\\,mm; TSR is 0\\% across all 800 episodes. The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{action-collapsed safety} (colloquially, ``fake safety''): \\emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\\cite{karwowski2024goodhart}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Action collapse is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\\tau_d$. dfCAR collapses Pi0+A1 from 91.5\\% to ${\\approx}$\\,0\\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\\,=\\,71.5\\%, CAR\\,=\\,28.5\\%, with every safe episode above 288\\,mm displacement and dfCAR equal to raw CAR (Section~\\ref{sec:fake_safety}).\n\n\\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n\n\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero action-collapsed episodes. Adding SDF supervision does not yield statistically significant improvement across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance (Section~\\ref{sec:avoidance_source}).\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\\tau_d \\in [2, 200]$\\,mm.\n    \\item \\textbf{Action-collapse diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\\% of Pi0 safe episodes are action-collapse artifacts.\n    \\item \\textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \\emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.\n    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for nearly all measured CAR gains (${\\sim}$26\\,pp); SDF supervision shows no statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$, 3 seeds).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\section{Introduction}\\label{sec:intro}",
          " ",
          "-Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.",
          "+Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization~\\cite{zhang2025safevla}, diffusion-process collision costs~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.",
          " ",
          " \\begin{figure}[t]",
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

_source line 74_

Let me verify the fix and do a final sweep for any remaining "Fake Safety Problem" in section titles (the main.aux showed stale compiled output—let me confirm the .tex sources are clean).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "6e1d5aae-2352-4302-bc99-b684d8002787",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2nzrQ4FAX13igSLE4jsgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 68706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2225
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

_source line 75_

<details open><summary>🔧 Tool call — Grep · `toolu_01XYc4zb7FjtyrHsrzpCQ6Gd`</summary>

```json
{
  "pattern": "Fake Safety Problem",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "5ba36a42-5c82-4ead-81ba-7e92e1533c0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2nzrQ4FAX13igSLE4jsgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 68706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2225
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

_source line 76 · 2026-05-28T06:58:12.059Z_

<details><summary>↩ Tool result · `toolu_01XYc4zb7FjtyrHsrzpCQ6Gd`</summary>

```text
docs/paper/archive/analysis_claim1.tex:1:\subsection{The Fake Safety Problem}\label{sec:fake_safety}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "2ea0de18-5f65-48ae-a8cb-19a71f3d7c54",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/archive/analysis_claim1.tex:1:\\subsection{The Fake Safety Problem}\\label{sec:fake_safety}",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Grep · `toolu_016WTXpmq6YgjYzW5QS91PyJ`</summary>

```json
{
  "pattern": "nearly all|\\\\bnearly\\\\b",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "18a90a95-5107-473e-9716-f72ef5c76af2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2nzrQ4FAX13igSLE4jsgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 68706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2225
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

_source line 78 · 2026-05-28T06:58:14.054Z_

<details><summary>↩ Tool result · `toolu_016WTXpmq6YgjYzW5QS91PyJ`</summary>

```text
docs/paper/discussion.tex:3:[Omitted long matching line]
docs/paper/abstract.tex:5:[Omitted long matching line]
docs/paper/introduction.tex:27:    \item \textbf{Demonstration sufficiency:} collision-free demonstrations account for nearly all measured CAR gains (${\sim}$26\,pp); SDF supervision shows no statistically significant benefit across the tested range $\lambda \in [0.005, 0.1]$ ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$, 3 seeds).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "9727b89b-5e88-4307-95b0-dab76354d0a4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:3:[Omitted long matching line]\ndocs/paper/abstract.tex:5:[Omitted long matching line]\ndocs/paper/introduction.tex:27:    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for nearly all measured CAR gains (${\\sim}$26\\,pp); SDF supervision shows no statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$, 3 seeds).",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Read · `toolu_01Q2HxWo2E38xXAMs563n9Zd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "e9731ec8-c1fe-4a00-b3d7-c4c1f0f83eaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2nzrQ4FAX13igSLE4jsgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 68706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2225
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

_source line 80 · 2026-05-28T06:58:14.445Z_

<details><summary>↩ Tool result · `toolu_01Q2HxWo2E38xXAMs563n9Zd`</summary>

```text
1	\section{Introduction}\label{sec:intro}
2	
3	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization~\cite{zhang2025safevla}, diffusion-process collision costs~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}. Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "33762b12-048c-4ec0-80bd-2e567af2cab5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:intro}\n\nCollision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization~\\cite{zhang2025safevla}, diffusion-process collision costs~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.\n\n\\begin{figure}[t]",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Assistant

_source line 81_

Fix verified. Here's the full scan report:

---

### 1. 术语一致性 — **PASS**
- "frozen episodes" / "frozen rate": 仅存在于 `archive/` 目录（不参与编译）和 `main.aux`（上次编译残留）。所有活跃 .tex 文件已统一使用 "action-collapsed episodes" 和 "action-collapse rate"。
- "fake safety": 仅在 `introduction.tex:12` 首次引入时出现一次（`colloquially, ``fake safety''`），其后全文不再出现。`\label{sec:fake_safety}` 标识符保持不变。

### 2. SafeVLA 分类一致性 — **FAIL → FIXED**
- `related_work.tex:12`: "Constrained optimization" ✓
- `discussion.tex:6`: "Constrained-optimization approaches (e.g., SafeVLA)" ✓
- ~~`introduction.tex:3`: SafeVLA 被标记为 "SDF-augmented training"（应为 "constrained optimization"），CAPE 被标记为 "constraint-based planning"~~
- **已修复**: 改为 `constrained optimization~\cite{zhang2025safevla}, diffusion-process collision costs~\cite{yang2025cape}`，与 related_work.tex 一致。

### 3. "redundant" 用词 — **PASS**
- `related_work.tex:12`: "redundant **at the tested scale**" ✓
- `discussion.tex:20`: "redundant **at the tested scale** with demonstration data" ✓
- 两处均有适当限定。

### 4. Scope 限定 — **PASS**
- `discussion.tex:3` 首句: "**CAR-based** VLA safety evaluation, **as currently practiced on SafeLIBERO**" ✓
- `abstract.tex:6` 末句: "**EE-only geometric supervision**" ✓
- Claim 3 多处: "**at the tested scale**" / "**across the tested range**" ✓

### 5. "20×" 使用 — **PASS**
活跃文件中恰好 3 处（均在 `claim3.tex`）：
- L3: 首次定义 "a 20$\times$ range of loss weights"
- L32: 关键论证 "a 20$\times$ increase in SDF loss weight"
- L46: figure caption "a 20$\times$ loss-weight range"

### 6. 引用完整性 — **PASS**
- `related_work.tex:15`: HazardArena (`chen2026hazardarena`) 和 VLA-Risk (`vlariskanon2026`) 均已引用 ✓
- `references.bib`: 两者 bib 条目均存在 ✓
- 所有 33 个 `\cite`/`\citep` 引用键均有对应 bib 条目，无悬空引用。

### 7. Oracle caveat 准确性 — **PASS**
`claim2.tex` 末段诚实承认: "the Pi0+A1 baseline (TSR$\,\approx\,$0%) is already fully action-collapsed" 和 "The LoRA baseline is itself largely action-collapsed (99.4% collapsed episodes)"。无 TSR≈70-80% 的错误声称。

### 8. 数值一致性 — **PASS**
- `abstract.tex:5`: "**nearly all** measured avoidance gains" ✓
- bimodal gap: `method.tex:36`, `experimental_framework.tex:23`, `appendix.tex:7` 均为 "below 1\,$\mu$m ... above 200\,mm" ✓

---

**总结**: 8 项检查中 7 项直接 PASS，1 项 FAIL 已修复（introduction.tex 中 SafeVLA 和 CAPE 的分类描述与 related_work.tex 不一致）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "uuid": "ffd6abca-192a-4287-bb4d-72fb3c9f4dda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011T5njfndaX1cpBE7uRJupx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 70931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 921
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

_source line 82_

Fix verified. Here's the full scan report:

---

### 1. 术语一致性 — **PASS**
- "frozen episodes" / "frozen rate": 仅存在于 `archive/` 目录（不参与编译）和 `main.aux`（上次编译残留）。所有活跃 .tex 文件已统一使用 "action-collapsed episodes" 和 "action-collapse rate"。
- "fake safety": 仅在 `introduction.tex:12` 首次引入时出现一次（`colloquially, ``fake safety''`），其后全文不再出现。`\label{sec:fake_safety}` 标识符保持不变。

### 2. SafeVLA 分类一致性 — **FAIL → FIXED**
- `related_work.tex:12`: "Constrained optimization" ✓
- `discussion.tex:6`: "Constrained-optimization approaches (e.g., SafeVLA)" ✓
- ~~`introduction.tex:3`: SafeVLA 被标记为 "SDF-augmented training"（应为 "constrained optimization"），CAPE 被标记为 "constraint-based planning"~~
- **已修复**: 改为 `constrained optimization~\cite{zhang2025safevla}, diffusion-process collision costs~\cite{yang2025cape}`，与 related_work.tex 一致。

### 3. "redundant" 用词 — **PASS**
- `related_work.tex:12`: "redundant **at the tested scale**" ✓
- `discussion.tex:20`: "redundant **at the tested scale** with demonstration data" ✓
- 两处均有适当限定。

### 4. Scope 限定 — **PASS**
- `discussion.tex:3` 首句: "**CAR-based** VLA safety evaluation, **as currently practiced on SafeLIBERO**" ✓
- `abstract.tex:6` 末句: "**EE-only geometric supervision**" ✓
- Claim 3 多处: "**at the tested scale**" / "**across the tested range**" ✓

### 5. "20×" 使用 — **PASS**
活跃文件中恰好 3 处（均在 `claim3.tex`）：
- L3: 首次定义 "a 20$\times$ range of loss weights"
- L32: 关键论证 "a 20$\times$ increase in SDF loss weight"
- L46: figure caption "a 20$\times$ loss-weight range"

### 6. 引用完整性 — **PASS**
- `related_work.tex:15`: HazardArena (`chen2026hazardarena`) 和 VLA-Risk (`vlariskanon2026`) 均已引用 ✓
- `references.bib`: 两者 bib 条目均存在 ✓
- 所有 33 个 `\cite`/`\citep` 引用键均有对应 bib 条目，无悬空引用。

### 7. Oracle caveat 准确性 — **PASS**
`claim2.tex` 末段诚实承认: "the Pi0+A1 baseline (TSR$\,\approx\,$0%) is already fully action-collapsed" 和 "The LoRA baseline is itself largely action-collapsed (99.4% collapsed episodes)"。无 TSR≈70-80% 的错误声称。

### 8. 数值一致性 — **PASS**
- `abstract.tex:5`: "**nearly all** measured avoidance gains" ✓
- bimodal gap: `method.tex:36`, `experimental_framework.tex:23`, `appendix.tex:7` 均为 "below 1\,$\mu$m ... above 200\,mm" ✓

---

**总结**: 8 项检查中 7 项直接 PASS，1 项 FAIL 已修复（introduction.tex 中 SafeVLA 和 CAPE 的分类描述与 related_work.tex 不一致）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 237553,
  "duration_api_ms": 238742,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "bd430238-1092-4029-a111-64714589cc5c",
  "total_cost_usd": 0.9854035,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 73304,
    "cache_read_input_tokens": 345501,
    "output_tokens": 14098,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 73304,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1069,
        "cache_read_input_tokens": 70931,
        "cache_creation_input_tokens": 921,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 921
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1908,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 14098,
      "cacheReadInputTokens": 345501,
      "cacheCreationInputTokens": 73304,
      "webSearchRequests": 0,
      "costUSD": 0.9834005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "30e407b0-832d-4b4e-900f-1842417f2e77"
}
```

</details>

---
