# paper camera ready polish

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/workers/worker_paper_camera-ready-polish_20260529T174202.log`
- **Structured JSON:** [`83e1910d1d5220473ed4.json`](../../sessions/83/83e1910d1d5220473ed4.json)

## Before a recorded user message

62 recorded events

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "6cfd82ea-a1b9-4d1f-8eda-f54e1a61ce2a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1780087800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "aec93017-dfc5-4eab-935f-c9de0046a3f8",
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5"
}
```

---

### Assistant

_source line 4_

I'll read all the paper files and produce a comprehensive checklist. Let me start by reading all files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "29d400b2-f9d0-4424-af73-a7c522caf922",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

<details open><summary>🔧 Tool call — Read · `toolu_01KyXowShepYEWkFeYN15PjJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "79abb3bf-fb6c-407f-ba10-7829d0fb93e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 6 · 2026-05-29T17:42:12.603Z_

<details><summary>↩ Tool result · `toolu_01KyXowShepYEWkFeYN15PjJ`</summary>

```text
1	\documentclass{article}
2	
3	\PassOptionsToPackage{dvipsnames}{xcolor}
4	\usepackage{corl_2026}
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{wrapfig}
12	\usepackage{threeparttable}
13	\usepackage{enumitem}
14	\graphicspath{{../../artifacts/figures/}}
15	
16	\title{How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation}
17	
18	\author{
19	  Anonymous Authors
20	}
21	
22	\begin{document}
23	
24	\maketitle
25	
26	\input{abstract}
27	
28	\keywords{VLA safety, collision avoidance, action collapse, signed distance fields}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	\input{claim1}
37	
38	\input{claim2}
39	
40	\input{claim3}
41	
42	\input{discussion}
43	
44	\bibliography{references}
45	
46	\clearpage
47	\appendix
48	\input{appendix}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "65f58ecd-da40-4fab-9f71-6960e14b3798",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\PassOptionsToPackage{dvipsnames}{xcolor}\n\\usepackage{corl_2026}\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{subcaption}\n\\usepackage{wrapfig}\n\\usepackage{threeparttable}\n\\usepackage{enumitem}\n\\graphicspath{{../../artifacts/figures/}}\n\n\\title{How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation}\n\n\\author{\n  Anonymous Authors\n}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{abstract}\n\n\\keywords{VLA safety, collision avoidance, action collapse, signed distance fields}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{claim1}\n\n\\input{claim2}\n\n\\input{claim3}\n\n\\input{discussion}\n\n\\bibliography{references}\n\n\\clearpage\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_018vm1v1NkV6bUb9GUrkhV6B`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "0b74987b-6675-4780-93cb-03623480d93e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 8 · 2026-05-29T17:42:13.074Z_

<details><summary>↩ Tool result · `toolu_018vm1v1NkV6bUb9GUrkhV6B`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance. We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, revealing that over 99\% of safe episodes in Pi0-family models are action-collapse artifacts. We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance: ground-truth oracle refinement reduces CAR below unrefined baselines by redistributing collisions to unmonitored arm links, and SDF training supervision shows no statistically significant benefit beyond collision-free demonstrations alone. These findings suggest that collision avoidance primarily arises from demonstration data rather than EE-only geometric supervision.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "0fcda848-3337-415e-a134-abadb926557a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance. We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, revealing that over 99\\% of safe episodes in Pi0-family models are action-collapse artifacts. We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance: ground-truth oracle refinement reduces CAR below unrefined baselines by redistributing collisions to unmonitored arm links, and SDF training supervision shows no statistically significant benefit beyond collision-free demonstrations alone. These findings suggest that collision avoidance primarily arises from demonstration data rather than EE-only geometric supervision.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_0124LmWdNwgMWdJdZpQMMYpM`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "9903c266-7f93-4b71-b839-de22b0504a71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 10 · 2026-05-29T17:42:13.539Z_

<details><summary>↩ Tool result · `toolu_0124LmWdNwgMWdJdZpQMMYpM`</summary>

```text
1	\section{Introduction}\label{sec:intro}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=\textwidth]{fig_overview_pb}
6	\caption{Overview of three findings. \textbf{(a)}~Action-collapsed safety: Pi0+A1 reports 91.5\% CAR, but 99.6\% of safe episodes have displacement ${<}\,0.1$\,mm; dfCAR drops to ${\approx}\,0$\%. \textbf{(b)}~EE-only SDF fails: SDF gradient repels the end-effector (EE) but rotates unmonitored arm links into obstacles; all oracle variants underperform unrefined baselines (73--77\% vs.\ 82--83\%). \textbf{(c)}~Data drives safety: collision-free demonstrations account for $+$26\,pp CAR; SDF supervision adds only $+$2.2\,pp ($p = 0.155$, n.s.).}
7	\label{fig:overview}
8	\end{figure*}
9	
10	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. A single collision can damage hardware, injure humans, or invalidate a task, making reliable safety metrics essential. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization~\cite{zhang2025safevla}, diffusion-process collision costs~\cite{yang2025cape}, and collision risk gating~\cite{cofreeevla2026}. Signed distance fields (SDFs) are a natural candidate: they provide continuous, differentiable proximity information that allows a policy to learn gradient-based obstacle avoidance during training. Our SDF-augmented Pi0~\cite{black2024pi0} (Pi0+A1; Table~\ref{tab:configurations}) reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; Task Success Rate (TSR) is 0\% across all 800 episodes. The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{action-collapsed safety} (colloquially, ``fake safety''): \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.
15	
16	\textbf{Action collapse is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\tau_d$. dfCAR collapses Pi0+A1 from 91.5\% to ${\approx}$\,0\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\,=\,71.5\%, CAR\,=\,28.5\%, with every safe episode above 288\,mm displacement and dfCAR equal to raw CAR (Section~\ref{sec:fake_safety}).
17	
18	\textbf{EE-only SDF refinement is counterproductive under the tested conditions.} Three ground-truth oracle variants applied to action-collapsed baselines all achieve \emph{lower} CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\ref{sec:ee_only}).
19	
20	\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\sim}$26 points with zero action-collapsed episodes. SDF supervision shows no statistically significant additional benefit ($p \geq 0.155$ for SDF loss weight $\lambda \in \{0.01, 0.1\}$; Section~\ref{sec:avoidance_source}).
21	
22	Our contributions are: (1)~We introduce \textbf{dfCAR}, a displacement-filtered CAR metric, and use it to diagnose action collapse across 100+ experiments, revealing that $>$99\% of Pi0 safe episodes are inaction artifacts rather than genuine avoidance. (2)~We show that EE-only oracle SDF refinement \emph{reduces} CAR below unrefined baselines, as unmonitored arm links rotate into obstacles. (3)~We demonstrate that collision-free demonstration data accounts for nearly all CAR gains (${\sim}$26\,pp) with no statistically significant SDF training benefit ($p \geq 0.155$).
23	
24	\begin{figure}[t]
25	\centering
26	\includegraphics[width=\linewidth]{fig1_teaser}
27	\caption{The action-collapsed safety problem in VLA collision avoidance evaluation. Standard CAR classifies an action-collapsed robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau_d$; Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right).}
28	\label{fig:teaser}
29	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "32a175f3-c636-4391-8588-6d29c984535b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:intro}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview_pb}\n\\caption{Overview of three findings. \\textbf{(a)}~Action-collapsed safety: Pi0+A1 reports 91.5\\% CAR, but 99.6\\% of safe episodes have displacement ${<}\\,0.1$\\,mm; dfCAR drops to ${\\approx}\\,0$\\%. \\textbf{(b)}~EE-only SDF fails: SDF gradient repels the end-effector (EE) but rotates unmonitored arm links into obstacles; all oracle variants underperform unrefined baselines (73--77\\% vs.\\ 82--83\\%). \\textbf{(c)}~Data drives safety: collision-free demonstrations account for $+$26\\,pp CAR; SDF supervision adds only $+$2.2\\,pp ($p = 0.155$, n.s.).}\n\\label{fig:overview}\n\\end{figure*}\n\nCollision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. A single collision can damage hardware, injure humans, or invalidate a task, making reliable safety metrics essential. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through constrained optimization~\\cite{zhang2025safevla}, diffusion-process collision costs~\\cite{yang2025cape}, and collision risk gating~\\cite{cofreeevla2026}. Signed distance fields (SDFs) are a natural candidate: they provide continuous, differentiable proximity information that allows a policy to learn gradient-based obstacle avoidance during training. Our SDF-augmented Pi0~\\cite{black2024pi0} (Pi0+A1; Table~\\ref{tab:configurations}) reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.\n\nIt is not (Figure~\\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\\% exhibit displacement below 0.1\\,mm; Task Success Rate (TSR) is 0\\% across all 800 episodes. The robot is action-collapsed, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{action-collapsed safety} (colloquially, ``fake safety''): \\emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\\cite{karwowski2024goodhart}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Action collapse is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\\tau_d$. dfCAR collapses Pi0+A1 from 91.5\\% to ${\\approx}$\\,0\\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\\,=\\,71.5\\%, CAR\\,=\\,28.5\\%, with every safe episode above 288\\,mm displacement and dfCAR equal to raw CAR (Section~\\ref{sec:fake_safety}).\n\n\\textbf{EE-only SDF refinement is counterproductive under the tested conditions.} Three ground-truth oracle variants applied to action-collapsed baselines all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n\n\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero action-collapsed episodes. SDF supervision shows no statistically significant additional benefit ($p \\geq 0.155$ for SDF loss weight $\\lambda \\in \\{0.01, 0.1\\}$; Section~\\ref{sec:avoidance_source}).\n\nOur contributions are: (1)~We introduce \\textbf{dfCAR}, a displacement-filtered CAR metric, and use it to diagnose action collapse across 100+ experiments, revealing that $>$99\\% of Pi0 safe episodes are inaction artifacts rather than genuine avoidance. (2)~We show that EE-only oracle SDF refinement \\emph{reduces} CAR below unrefined baselines, as unmonitored arm links rotate into obstacles. (3)~We demonstrate that collision-free demonstration data accounts for nearly all CAR gains (${\\sim}$26\\,pp) with no statistically significant SDF training benefit ($p \\geq 0.155$).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig1_teaser}\n\\caption{The action-collapsed safety problem in VLA collision avoidance evaluation. Standard CAR classifies an action-collapsed robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\\tau_d$; Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and dfCAR equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01DCKLAT6tkqEQyCnhdYGztA`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "a852ccb6-57c6-46da-8bd5-141971d3b8e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 12 · 2026-05-29T17:42:14.012Z_

<details><summary>↩ Tool result · `toolu_01DCKLAT6tkqEQyCnhdYGztA`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models.}
4	VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but these methods target perception rather than safety, with no collision constraints. Pi0~\cite{black2024pi0} and its successor Pi0.5 use flow matching for action generation, where near-zero actions can arise from training instabilities~\cite{dong2025conditioning}; we test both families to separate architecture effects from safety evaluation artifacts. Whether geometric supervision can teach active obstacle avoidance is the question our work addresses.
5	
6	\paragraph{Safety in Robot Learning.}
7	Safety-aware approaches span training-time constrained RL~\cite{zhang2025safevla} and test-time filters: control barrier functions~\cite{hu2025vlsa}, collision risk gating~\cite{cofreeevla2026}, inverse kinematics QP~\cite{spalter2024ikinqp}, and diffusion-process collision costs~\cite{li2024langguided,yang2025cape}. SafeDiffuser~\cite{xiao2025safediffuser} integrates barrier functions into diffusion denoising but does not learn intrinsic collision awareness. A recent survey~\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed extrinsically, adding inference-time overhead and requiring collision geometry at deployment. This work tests whether auxiliary SDF supervision can instead produce intrinsic collision awareness.
8	
9	\paragraph{Signed Distance Functions in Robotics.}
10	SDFs encode minimum surface distance, with sign indicating free space or penetration. Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\cite{ortiz2022isdf}, planning~\cite{vasilopoulos2023ramp}, and differentiable collision detection~\cite{zhi2021diffco}. CDF~\cite{li2024cdf} and CSSDF-Net~\cite{chen2026cssdfnet} extend SDFs to configuration space for manipulation planning. RDF~\cite{li2024rdf} represents robot geometry as composable per-link SDFs, enabling whole-body collision queries, directly relevant to the full-body gap our work identifies. Neural SDF-based MPC~\cite{jacquet2025neuralnmpc} is effective in classical pipelines, but integration into end-to-end learned policies remains unexplored. All successful SDF applications in robotics operate on full-body or configuration-space representations; restricting supervision to the EE does not transfer these benefits.
11	
12	\paragraph{SDF integration pathways.} SDF-based geometric supervision can enter VLA policies through three mechanisms: (a)~\emph{training-time auxiliary loss} on the EE trajectory (tested here); (b)~\emph{constrained optimization}, where SafeVLA~\citep{zhang2025safevla} embeds safety constraints via Lagrangian optimization; and (c)~\emph{runtime filtering}, where VLSA~\citep{hu2025vlsa} applies control barrier functions at inference. Pathway~(a) provides gradients only at the supervised point, leaving intermediate links unmonitored; (b) and~(c) can query full-body geometry, sidestepping this bottleneck. Our negative finding is specific to~(a).
13	
14	\paragraph{Evaluation Metrics for Safe Manipulation.}
15	SafeLIBERO~\cite{hu2025vlsa} extends LIBERO~\cite{liu2023libero} with obstacle-augmented environments and a CAR metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior, echoing concerns about metric reliability~\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\cite{snyder2026beyond}. Loss collapse in diffusion policies~\cite{dong2025conditioning} can produce near-zero actions; when these occur during safety evaluation, CAR is systematically inflated. Concurrent work such as HazardArena~\cite{chen2026hazardarena} expands the landscape to semantic safety. More broadly, any binary safety metric faces a base-rate problem when most episodes are collision-free through inaction~\cite{gururangan2018annotation}. dfCAR (\S\ref{sec:dfcar}) addresses this by conditioning on active behavior.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "c22120fa-c0e4-43c5-9b75-d2dac1cd1ca5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models.}\nVLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\\cite{brohan2023rt2,black2024pi0,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but these methods target perception rather than safety, with no collision constraints. Pi0~\\cite{black2024pi0} and its successor Pi0.5 use flow matching for action generation, where near-zero actions can arise from training instabilities~\\cite{dong2025conditioning}; we test both families to separate architecture effects from safety evaluation artifacts. Whether geometric supervision can teach active obstacle avoidance is the question our work addresses.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware approaches span training-time constrained RL~\\cite{zhang2025safevla} and test-time filters: control barrier functions~\\cite{hu2025vlsa}, collision risk gating~\\cite{cofreeevla2026}, inverse kinematics QP~\\cite{spalter2024ikinqp}, and diffusion-process collision costs~\\cite{li2024langguided,yang2025cape}. SafeDiffuser~\\cite{xiao2025safediffuser} integrates barrier functions into diffusion denoising but does not learn intrinsic collision awareness. A recent survey~\\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed extrinsically, adding inference-time overhead and requiring collision geometry at deployment. This work tests whether auxiliary SDF supervision can instead produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSDFs encode minimum surface distance, with sign indicating free space or penetration. Neural SDFs~\\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\\cite{ortiz2022isdf}, planning~\\cite{vasilopoulos2023ramp}, and differentiable collision detection~\\cite{zhi2021diffco}. CDF~\\cite{li2024cdf} and CSSDF-Net~\\cite{chen2026cssdfnet} extend SDFs to configuration space for manipulation planning. RDF~\\cite{li2024rdf} represents robot geometry as composable per-link SDFs, enabling whole-body collision queries, directly relevant to the full-body gap our work identifies. Neural SDF-based MPC~\\cite{jacquet2025neuralnmpc} is effective in classical pipelines, but integration into end-to-end learned policies remains unexplored. All successful SDF applications in robotics operate on full-body or configuration-space representations; restricting supervision to the EE does not transfer these benefits.\n\n\\paragraph{SDF integration pathways.} SDF-based geometric supervision can enter VLA policies through three mechanisms: (a)~\\emph{training-time auxiliary loss} on the EE trajectory (tested here); (b)~\\emph{constrained optimization}, where SafeVLA~\\citep{zhang2025safevla} embeds safety constraints via Lagrangian optimization; and (c)~\\emph{runtime filtering}, where VLSA~\\citep{hu2025vlsa} applies control barrier functions at inference. Pathway~(a) provides gradients only at the supervised point, leaving intermediate links unmonitored; (b) and~(c) can query full-body geometry, sidestepping this bottleneck. Our negative finding is specific to~(a).\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nSafeLIBERO~\\cite{hu2025vlsa} extends LIBERO~\\cite{liu2023libero} with obstacle-augmented environments and a CAR metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior, echoing concerns about metric reliability~\\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\\cite{snyder2026beyond}. Loss collapse in diffusion policies~\\cite{dong2025conditioning} can produce near-zero actions; when these occur during safety evaluation, CAR is systematically inflated. Concurrent work such as HazardArena~\\cite{chen2026hazardarena} expands the landscape to semantic safety. More broadly, any binary safety metric faces a base-rate problem when most episodes are collision-free through inaction~\\cite{gururangan2018annotation}. dfCAR (\\S\\ref{sec:dfcar}) addresses this by conditioning on active behavior.\n",
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01Kjmm2m2eZKyRJGnbgkjvnr`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "e5e49bed-e103-44bf-92f5-fdab717fcc64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 14 · 2026-05-29T17:42:14.479Z_

<details><summary>↩ Tool result · `toolu_01Kjmm2m2eZKyRJGnbgkjvnr`</summary>

```text
1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	\subsection{Benchmark and Models}\label{sec:benchmark}
4	
5	We evaluate on SafeLIBERO~\cite{hu2025vlsa}, the \textit{object\_pudding} suite (Level~II): four tabletop pick-and-place tasks with collision hazards and per-timestep collision detection. Two VLA families are tested: \textbf{Pi0} (${\sim}$2.5B)~\cite{black2024pi0} with flow matching~\cite{lipman2023flow}, and \textbf{Pi0.5} with broader pre-training. Table~\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). All metrics are computed using a fixed evaluation seed (seed\,=\,7); the reported $\pm$ values reflect variance across training seeds, not evaluation stochasticity. The four tasks span varied obstacle configurations and gripper approach trajectories, requiring the policy to generalize avoidance across different geometric contexts rather than memorize a single arrangement. We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction of episodes that complete the task~\cite{hu2025vlsa,zhang2025safevla}.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Training configurations. Trainable parameters exclude the frozen backbone. Pi0+A1 LoRA weights were not loaded due to a parameter-name mismatch; only auxiliary heads were trained.}
10	\label{tab:configurations}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{llr}
14	\toprule
15	Configuration & Description & Trainable Params \\
16	\midrule
17	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$2.5B \\
18	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
19	Pi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\sim}$658K \\
20	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
21	Pi0.5 (pre-trained) & No fine-tuning & 0 \\
22	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
23	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
29	
30	Standard CAR conflates genuine avoidance with action collapse. We define an episode as \emph{action-collapsed} when $d_{\max}(e) < \tau_d$ ($\tau_d = 0.1$\,mm) and exclude such episodes:
31	\begin{equation}\label{eq:car_f}
32	\text{dfCAR} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
33	\end{equation}
34	The displacement distribution is sharply bimodal (collapsed episodes below 1\,$\mu$m, active above 200\,mm), making $\tau_d$ robust across $[2, 200]$\,mm (Appendix~\ref{sec:appendix_threshold}). For Pi0 under A1, $d_{\max}$ uses obstacle displacement due to an inconsistent EE reference frame; Pi0.5 uses standard EE displacement.
35	
36	\subsection{SDF Auxiliary Training and Oracle Refinement}\label{sec:sdf_aux}
37	
38	We augment LoRA-adapted~\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\ref{sec:appendix_training}, Table~\ref{tab:hyperparams}). The total loss is:
39	\begin{equation}\label{eq:total_loss}
40	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda \left( \mathcal{L}_\text{SDF} + \mathcal{L}_\text{EE} \right)
41	\end{equation}
42	where $\lambda \in \{0.005, 0.01, 0.1\}$. $\mathcal{L}_\text{SDF}$ trains a 4-layer MLP decoder to predict signed distances, clamped to $[-\delta, \delta]$ ($\delta = 0.05$\,m) with Eikonal regularization (weight 0.1); 64 query points per step are sampled from a precomputed $64^3$ voxel grid. $\mathcal{L}_\text{EE}$ regresses the end-effector position from pooled suffix features via a 2-layer MLP (1024 $\to$ 256 $\to$ 3), providing spatial grounding for the SDF decoder.
43	
44	Training proceeds in two phases: Phase~1 (steps 0--5K) freezes the backbone and LoRA, training only auxiliary heads to convergence; Phase~2 (steps 5K--30K) unfreezes LoRA with a 100-step warmup ramp to avoid destabilizing learned SDF features.
45	
46	In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\,=\,0\%; Table~\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\ref{sec:appendix_oracle}).\label{sec:oracle_setup}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "1ce7aa62-e924-4a95-b6d1-0c1b5f4e62c9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
      "content": "\\section{Experimental Setup and Metrics}\\label{sec:method}\n\n\\subsection{Benchmark and Models}\\label{sec:benchmark}\n\nWe evaluate on SafeLIBERO~\\cite{hu2025vlsa}, the \\textit{object\\_pudding} suite (Level~II): four tabletop pick-and-place tasks with collision hazards and per-timestep collision detection. Two VLA families are tested: \\textbf{Pi0} (${\\sim}$2.5B)~\\cite{black2024pi0} with flow matching~\\cite{lipman2023flow}, and \\textbf{Pi0.5} with broader pre-training. Table~\\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). All metrics are computed using a fixed evaluation seed (seed\\,=\\,7); the reported $\\pm$ values reflect variance across training seeds, not evaluation stochasticity. The four tasks span varied obstacle configurations and gripper approach trajectories, requiring the policy to generalize avoidance across different geometric contexts rather than memorize a single arrangement. We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction of episodes that complete the task~\\cite{hu2025vlsa,zhang2025safevla}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameters exclude the frozen backbone. Pi0+A1 LoRA weights were not loaded due to a parameter-name mismatch; only auxiliary heads were trained.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 (pre-trained) & No fine-tuning & 0 \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\n\nStandard CAR conflates genuine avoidance with action collapse. We define an episode as \\emph{action-collapsed} when $d_{\\max}(e) < \\tau_d$ ($\\tau_d = 0.1$\\,mm) and exclude such episodes:\n\\begin{equation}\\label{eq:car_f}\n\\text{dfCAR} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nThe displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active above 200\\,mm), making $\\tau_d$ robust across $[2, 200]$\\,mm (Appendix~\\ref{sec:appendix_threshold}). For Pi0 under A1, $d_{\\max}$ uses obstacle displacement due to an inconsistent EE reference frame; Pi0.5 uses standard EE displacement.\n\n\\subsection{SDF Auxiliary Training and Oracle Refinement}\\label{sec:sdf_aux}\n\nWe augment LoRA-adapted~\\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\\ref{sec:appendix_training}, Table~\\ref{tab:hyperparams}). The total loss is:\n\\begin{equation}\\label{eq:total_loss}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda \\left( \\mathcal{L}_\\text{SDF} + \\mathcal{L}_\\text{EE} \\right)\n\\end{equation}\nwhere $\\lambda \\in \\{0.005, 0.01, 0.1\\}$. $\\mathcal{L}_\\text{SDF}$ trains a 4-layer MLP decoder to predict signed distances, clamped to $[-\\delta, \\delta]$ ($\\delta = 0.05$\\,m) with Eikonal regularization (weight 0.1); 64 query points per step are sampled from a precomputed $64^3$ voxel grid. $\\mathcal{L}_\\text{EE}$ regresses the end-effector position from pooled suffix features via a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3), providing spatial grounding for the SDF decoder.\n\nTraining proceeds in two phases: Phase~1 (steps 0--5K) freezes the backbone and LoRA, training only auxiliary heads to convergence; Phase~2 (steps 5K--30K) unfreezes LoRA with a 100-step warmup ramp to avoid destabilizing learned SDF features.\n\nIn Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\\,=\\,0\\%; Table~\\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\\ref{sec:appendix_oracle}).\\label{sec:oracle_setup}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_016nHQtLrfQN2t1LVAxvXbZP`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "934682b4-1be9-4d18-98c1-53f08babb763",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 16 · 2026-05-29T17:42:14.949Z_

<details><summary>↩ Tool result · `toolu_016nHQtLrfQN2t1LVAxvXbZP`</summary>

```text
1	\section{The Action-Collapsed Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\% of collision-free episodes are action-collapse artifacts (Table~\ref{tab:fake_safety}). Applying dfCAR collapses all three to ${\approx}$\,0\%. Pi0+A1 achieves the \emph{highest} raw CAR (91.5\%) because more complete action collapse (from a parameter-name mismatch preventing LoRA loading; Table~\ref{tab:configurations}) yields greater CAR inflation. Pi0.5 validates the metric from the opposite direction: every safe episode exceeds 200\,mm displacement, and dfCAR equals raw CAR (28.5\%). The displacement distribution is sharply bimodal (Figure~\ref{fig:displacement}), with a five-order-of-magnitude gap that makes $\tau_d$ robust.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Action-collapse decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \tau_d = 0.1$\,mm. Pi0+A1 dfCAR$\,\approx\,$0: only 3/732 safe episodes exceed the threshold.}
8	\label{tab:fake_safety}
9	\vspace{2pt}
10	\small
11	\begin{tabular*}{\linewidth}{l@{\extracolsep{\fill}}ccccc}
12	\toprule
13	Method & Ep. & CAR (\%) & TSR (\%) & Collapsed (\%) & dfCAR (\%) \\
14	\midrule
15	Pi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\approx$\,0 \\
16	Pi0 LoRA     & 200 & 82.0 & 0.0 & ${\sim}$99 & $\approx$\,0 \\
17	Pi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & $\approx$\,0 \\
18	\midrule
19	Pi0.5  & 200 & 28.5 & 71.5 & 0.0 & 28.5 \\
20	\bottomrule
21	\end{tabular*}
22	\end{table}
23	
24	\begin{figure}[t]
25	\centering
26	\includegraphics[width=\columnwidth]{fig3_scatter_and_oracle}
27	\caption{(Left) CAR inflation from action collapse. Solid dots: reported CAR; hollow dots: dfCAR. The gap (red lines) quantifies illusory safety; Pi0-family models show 82--91\,pp inflation. (Right) CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform despite perfect distance information.}
28	\label{fig:scatter_and_oracle}
29	\end{figure}
30	Figure~\ref{fig:scatter_and_oracle} (left) quantifies CAR inflation from action collapse.\label{sec:anticorrelation} Pi0-family models show 82--91\,pp gaps between reported CAR and dfCAR: virtually all apparent safety is illusory. Pi0.5 and fine-tuned variants show no inflation (dfCAR\,=\,CAR), confirming genuine avoidance. Under dfCAR, the apparent safety--capability tradeoff disappears: high raw CAR was an artifact of action-collapse contamination, not deliberate avoidance.
31	
32	The 0.1\,mm threshold reflects near-total motor inactivity (typical actions produce 1--10\,mm per step). The sharply bimodal distribution (Figure~\ref{fig:displacement}) makes $\tau_d$ robust: any threshold in $[2, 200]$\,mm yields identical dfCAR (Appendix~\ref{sec:appendix_threshold}).
33	
34	\begin{figure}[t]
35	\centering
36	\includegraphics[width=0.85\columnwidth]{fig2_ee_displacement_distribution}
37	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
38	\label{fig:displacement}
39	\end{figure}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "824b6a6f-b737-47d9-a832-a71250f1db9f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex",
      "content": "\\section{The Action-Collapsed Safety Problem}\\label{sec:fake_safety}\n\nStandard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\\% of collision-free episodes are action-collapse artifacts (Table~\\ref{tab:fake_safety}). Applying dfCAR collapses all three to ${\\approx}$\\,0\\%. Pi0+A1 achieves the \\emph{highest} raw CAR (91.5\\%) because more complete action collapse (from a parameter-name mismatch preventing LoRA loading; Table~\\ref{tab:configurations}) yields greater CAR inflation. Pi0.5 validates the metric from the opposite direction: every safe episode exceeds 200\\,mm displacement, and dfCAR equals raw CAR (28.5\\%). The displacement distribution is sharply bimodal (Figure~\\ref{fig:displacement}), with a five-order-of-magnitude gap that makes $\\tau_d$ robust.\n\n\\begin{table}[t]\n\\centering\n\\caption{Action-collapse decomposition on SafeLIBERO. dfCAR excludes episodes with displacement $< \\tau_d = 0.1$\\,mm. Pi0+A1 dfCAR$\\,\\approx\\,$0: only 3/732 safe episodes exceed the threshold.}\n\\label{tab:fake_safety}\n\\vspace{2pt}\n\\small\n\\begin{tabular*}{\\linewidth}{l@{\\extracolsep{\\fill}}ccccc}\n\\toprule\nMethod & Ep. & CAR (\\%) & TSR (\\%) & Collapsed (\\%) & dfCAR (\\%) \\\\\n\\midrule\nPi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\\approx$\\,0 \\\\\nPi0 LoRA     & 200 & 82.0 & 0.0 & ${\\sim}$99 & $\\approx$\\,0 \\\\\nPi0+A1 (SDF) & 800 & 91.5 & 0.0 & 99.6 & $\\approx$\\,0 \\\\\n\\midrule\nPi0.5  & 200 & 28.5 & 71.5 & 0.0 & 28.5 \\\\\n\\bottomrule\n\\end{tabular*}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_scatter_and_oracle}\n\\caption{(Left) CAR inflation from action collapse. Solid dots: reported CAR; hollow dots: dfCAR. The gap (red lines) quantifies illusory safety; Pi0-family models show 82--91\\,pp inflation. (Right) CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform despite perfect distance information.}\n\\label{fig:scatter_and_oracle}\n\\end{figure}\nFigure~\\ref{fig:scatter_and_oracle} (left) quantifies CAR inflation from action collapse.\\label{sec:anticorrelation} Pi0-family models show 82--91\\,pp gaps between reported CAR and dfCAR: virtually all apparent safety is illusory. Pi0.5 and fine-tuned variants show no inflation (dfCAR\\,=\\,CAR), confirming genuine avoidance. Under dfCAR, the apparent safety--capability tradeoff disappears: high raw CAR was an artifact of action-collapse contamination, not deliberate avoidance.\n\nThe 0.1\\,mm threshold reflects near-total motor inactivity (typical actions produce 1--10\\,mm per step). The sharply bimodal distribution (Figure~\\ref{fig:displacement}) makes $\\tau_d$ robust: any threshold in $[2, 200]$\\,mm yields identical dfCAR (Appendix~\\ref{sec:appendix_threshold}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_013dUhdPAXDWmYTxUhBX2Vuy`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "5f3cb87c-021e-426d-a63c-631af1e5e014",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 18 · 2026-05-29T17:42:15.885Z_

<details><summary>↩ Tool result · `toolu_013dUhdPAXDWmYTxUhBX2Vuy`</summary>

```text
1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\S\ref{sec:oracle_setup}). Table~\ref{tab:oracle} and Figure~\ref{fig:scatter_and_oracle} (right) show that all three oracle variants achieve \emph{lower} CAR than unrefined baselines: the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%). Refinement with perfect distance information produces more collisions, not fewer.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}. Oracle variants use 160 episodes (4 tasks $\times$ 40); all other conditions use 200 episodes (4 tasks $\times$ 50).}
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
23	\midrule
24	\multicolumn{4}{l}{\textit{Non-collapsed baseline (Pi0.5 LoRA, 0\% action-collapse)}} \\
25	Pi0.5 LoRA (no refine) & 57.0 & 0.0 & -- \\
26	Pi0.5 Oracle-adaptive & 51.9 & 0.0 & 14.2 \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	The three variants apply the ground-truth SDF gradient differently (distance-adaptive, fixed, or feature-space; Appendix~\ref{sec:appendix_oracle}). Per-task analysis (Appendix~\ref{sec:appendix_pertask_oracle}) reveals the mechanism: on the one task where the EE is the primary collision body, refinement helps (+9\,pp); on the remaining three, the gradient pushes the EE away but rotates intermediate links into obstacles. On \texttt{orange\_juice} (LoRA CAR\,=\,96\%), Oracle-adaptive reduces CAR to 82.5\%. Feature-space application yields no advantage, confirming the failure is geometric. Applying Oracle-adaptive to non-collapsed Pi0.5 LoRA (CAR\,=\,57.0\%) also reduces CAR by 5.1\,pp, confirming the effect is structural. The A3 learned SDF never triggers refinement (0 steps per episode).
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "6bd15d4d-8bad-47e0-8742-8237db763909",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex",
      "content": "\\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\n\nCould a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\\S\\ref{sec:oracle_setup}). Table~\\ref{tab:oracle} and Figure~\\ref{fig:scatter_and_oracle} (right) show that all three oracle variants achieve \\emph{lower} CAR than unrefined baselines: the best oracle (76.9\\%) falls 5.1 points below LoRA (82.0\\%). Refinement with perfect distance information produces more collisions, not fewer.\n\n\\begin{table}[t]\n\\centering\n\\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\\ref{sec:appendix_pertask_oracle}. Oracle variants use 160 episodes (4 tasks $\\times$ 40); all other conditions use 200 episodes (4 tasks $\\times$ 50).}\n\\label{tab:oracle}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & CAR (\\%) & Collapsed (\\%) & Refines/ep \\\\\n\\midrule\nLoRA baseline (no refine) & 82.0 & 99.4 & -- \\\\\nFull-FT baseline (no refine) & 83.0 & -- & -- \\\\\n\\midrule\nOracle-adaptive (GT, dyn.\\ $\\alpha$) & 75.0 & 98.3 & 14.2 \\\\\nOracle-fixed (GT, $\\alpha{=}0.005$) & 73.1 & 98.3 & 14.8 \\\\\nOracle-feature (GT, feat.\\ space) & 76.9 & 96.7 & 241.7 \\\\\n\\midrule\nA3 learned SDF & 77.1 & -- & 0.0 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Non-collapsed baseline (Pi0.5 LoRA, 0\\% action-collapse)}} \\\\\nPi0.5 LoRA (no refine) & 57.0 & 0.0 & -- \\\\\nPi0.5 Oracle-adaptive & 51.9 & 0.0 & 14.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three variants apply the ground-truth SDF gradient differently (distance-adaptive, fixed, or feature-space; Appendix~\\ref{sec:appendix_oracle}). Per-task analysis (Appendix~\\ref{sec:appendix_pertask_oracle}) reveals the mechanism: on the one task where the EE is the primary collision body, refinement helps (+9\\,pp); on the remaining three, the gradient pushes the EE away but rotates intermediate links into obstacles. On \\texttt{orange\\_juice} (LoRA CAR\\,=\\,96\\%), Oracle-adaptive reduces CAR to 82.5\\%. Feature-space application yields no advantage, confirming the failure is geometric. Applying Oracle-adaptive to non-collapsed Pi0.5 LoRA (CAR\\,=\\,57.0\\%) also reduces CAR by 5.1\\,pp, confirming the effect is structural. The A3 learned SDF never triggers refinement (0 steps per episode).\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01XsxsuhGppqpdjeomjnsUoM`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "aebc41b6-a691-4b8f-9979-a357cdc41d4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 20 · 2026-05-29T17:42:16.354Z_

<details><summary>↩ Tool result · `toolu_01XsxsuhGppqpdjeomjnsUoM`</summary>

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
17	LoRA-only (no SDF) & 3 & 49.7\,$\pm$\,3.2 & 54.83\,$\pm$\,2.25 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.83\%) with zero action-collapsed episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.83\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.155$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\% (18K checkpoint, single seed s2), suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions and invariant to $\lambda$ (Figure~\ref{fig:lambda_and_fingerprint}, right), indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.
27	
28	\begin{figure}[t]
29	\centering
30	\includegraphics[width=\columnwidth]{fig5_lambda_and_fingerprint}
31	\caption{(Left) Effect of SDF loss weight $\lambda$ on CAR and TSR ($\lambda = 0$: LoRA-only). All $\lambda$ values remain within the null band ($p > 0.05$). (Right) Per-task CAR fingerprint; the task ordering is preserved across all $\lambda$ values, confirming demonstration-driven avoidance.}
32	\label{fig:lambda_and_fingerprint}
33	\end{figure}
34	
35	\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
36	Fine-tuning degrades TSR by ${\sim}$17--22\,pp (71.5\% $\to$ 49.7--54.0\%) due to distributional shift, not learned paralysis (all models retain $>$\,0.37\,m displacement). The SSR/TSR ratio (SSR\,=\,TSR\,$\cap$\,CAR) increases from 0.39 to 0.51--0.60 (Table~\ref{tab:ssr}): among completing episodes, more avoid collisions after fine-tuning.
37	
38	\begin{table}[t]
39	\centering
40	\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}
41	\label{tab:ssr}
42	\vspace{2pt}
43	\small
44	\begin{tabular}{lcccc}
45	\toprule
46	Condition & TSR (\%) & CAR (\%) & SSR (\%) & SSR/TSR \\
47	\midrule
48	Pi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\
49	LoRA-only (3 seeds) & 49.7 & 54.83 & 27.7 & 0.56 \\
50	SDF $\lambda{=}0.005$ & 54.0 & 54.5 & 27.8 & 0.51 \\
51	SDF $\lambda{=}0.01$ & 53.8 & 56.33 & 30.2 & 0.56 \\
52	SDF $\lambda{=}0.1$ & 50.2 & 57.00 & 30.2 & 0.60 \\
53	\bottomrule
54	\end{tabular}
55	\end{table}
56	
57	
58	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
59	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,57.00\%\,$\pm$\,2.18 (3 seeds: 58.0\%, 58.5\%, 54.5\%), within the null distribution ($p = 0.155$; Figure~\ref{fig:lambda_and_fingerprint}, left). Alternative null constructions yield consistent non-significance (Appendix~\ref{sec:appendix_null}). With $n = 3$ seeds ($\sigma \approx 2.3$\,pp), 80\% power requires effects $\geq 5.6$\,pp; the observed ${\sim}$2.2\,pp falls below this MDE. The binding constraint is not signal magnitude but the structural mismatch between EE monitoring and full-body collision surfaces.
60	
61	\paragraph{Cross-scene validation.}
62	To test whether the null SDF result generalizes beyond the primary scene, we replicate the core comparison on \texttt{spatial\_bowl}, a distinct SafeLIBERO suite with five cluttered obstacles (Table~\ref{tab:spatial_bowl}). The SDF condition ($\lambda = 0.005$) yields CAR of 11.5\% versus 12.0\% for LoRA-only ($\Delta = -0.5$\,pp), consistent with the absence of SDF benefit on the primary scene. The substantially lower CAR (11--12\% vs.\ 54--57\%) reflects greater scene difficulty; both conditions are equally affected.
63	
64	\begin{table}[t]
65	\centering
66	\caption{Cross-scene validation on \texttt{spatial\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\,pp CAR difference is well within noise.}
67	\label{tab:spatial_bowl}
68	\vspace{2pt}
69	\small
70	\begin{tabular}{lcc}
71	\toprule
72	Condition & CAR (\%) & TSR (\%) \\
73	\midrule
74	LoRA-only & 12.0 & 49.0 \\
75	SDF $\lambda{=}0.005$ & 11.5 & 51.5 \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "7b9ccc89-d60d-4700-9ff6-4cf6db550db6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
      "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero action-collapsed episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$). All fine-tuned models exhibit 0\\% action-collapse rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 49.7\\,$\\pm$\\,3.2 & 54.83\\,$\\pm$\\,2.25 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.83\\%) with zero action-collapsed episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.83\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.155$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\% (18K checkpoint, single seed s2), suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions and invariant to $\\lambda$ (Figure~\\ref{fig:lambda_and_fingerprint}, right), indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_lambda_and_fingerprint}\n\\caption{(Left) Effect of SDF loss weight $\\lambda$ on CAR and TSR ($\\lambda = 0$: LoRA-only). All $\\lambda$ values remain within the null band ($p > 0.05$). (Right) Per-task CAR fingerprint; the task ordering is preserved across all $\\lambda$ values, confirming demonstration-driven avoidance.}\n\\label{fig:lambda_and_fingerprint}\n\\end{figure}\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$17--22\\,pp (71.5\\% $\\to$ 49.7--54.0\\%) due to distributional shift, not learned paralysis (all models retain $>$\\,0.37\\,m displacement). The SSR/TSR ratio (SSR\\,=\\,TSR\\,$\\cap$\\,CAR) increases from 0.39 to 0.51--0.60 (Table~\\ref{tab:ssr}): among completing episodes, more avoid collisions after fine-tuning.\n\n\\begin{table}[t]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 49.7 & 54.83 & 27.7 & 0.56 \\\\\nSDF $\\lambda{=}0.005$ & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution ($p = 0.155$; Figure~\\ref{fig:lambda_and_fingerprint}, left). Alternative null constructions yield consistent non-significance (Appendix~\\ref{sec:appendix_null}). With $n = 3$ seeds ($\\sigma \\approx 2.3$\\,pp), 80\\% power requires effects $\\geq 5.6$\\,pp; the observed ${\\sim}$2.2\\,pp falls below this MDE. The binding constraint is not signal magnitude but the structural mismatch between EE monitoring and full-body collision surfaces.\n\n\\paragraph{Cross-scene validation.}\nTo test whether the null SDF result generalizes beyond the primary scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a distinct SafeLIBERO suite with five cluttered obstacles (Table~\\ref{tab:spatial_bowl}). The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 12.0\\% for LoRA-only ($\\Delta = -0.5$\\,pp), consistent with the absence of SDF benefit on the primary scene. The substantially lower CAR (11--12\\% vs.\\ 54--57\\%) reflects greater scene difficulty; both conditions are equally affected.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 12.0 & 49.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01327sCG9asf8hcnTramc7wq`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "a39b7b1e-304c-49d8-beaf-fb851cf08d31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 22 · 2026-05-29T17:42:16.858Z_

<details><summary>↩ Tool result · `toolu_01327sCG9asf8hcnTramc7wq`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We tested whether SDF supervision and collision-aware evaluation deliver reliable geometric safety for VLAs. Action collapse renders reported CAR illusory; dfCAR corrects this using only EE position logging (\S\ref{sec:dfcar}). EE-only oracle SDF refinement is counterproductive, reducing CAR by 5--10\,pp as unmonitored links rotate through obstacles (\S\ref{sec:ee_only}), and collision-free demonstrations account for nearly all avoidance gains with no statistically significant SDF benefit (\S\ref{sec:avoidance_source}). More broadly, dfCAR provides a lightweight diagnostic that any VLA pipeline can adopt to screen for action-collapse contamination, and point-supervision of a single link is insufficient for articulated robots; genuine geometric safety will require full-body collision representations and cross-architecture validation.
4	
5	\section{Limitations}\label{sec:limitations}
6	
7	All experiments use MuJoCo simulation (SafeLIBERO, two VLA families, four tasks); generality to other benchmarks or real hardware is untested. dfCAR requires bimodal displacement separation (Figure~\ref{fig:displacement}) and may need task-specific $\tau_d$ calibration. The EE-only null result applies to auxiliary-loss integration, not constrained optimization or runtime filtering (\S\ref{sec:related}). Oracle refinement uses one seed per variant ($n{=}1$, 160 episodes). The training ablation ($n{=}3$ seeds; MDE ${\approx}$ 5.6\,pp at 80\% power) cannot rule out a small SDF effect (2--5\,pp) without larger samples.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "e3c8e7f3-d776-40c7-a282-49d5916e1a3e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe tested whether SDF supervision and collision-aware evaluation deliver reliable geometric safety for VLAs. Action collapse renders reported CAR illusory; dfCAR corrects this using only EE position logging (\\S\\ref{sec:dfcar}). EE-only oracle SDF refinement is counterproductive, reducing CAR by 5--10\\,pp as unmonitored links rotate through obstacles (\\S\\ref{sec:ee_only}), and collision-free demonstrations account for nearly all avoidance gains with no statistically significant SDF benefit (\\S\\ref{sec:avoidance_source}). More broadly, dfCAR provides a lightweight diagnostic that any VLA pipeline can adopt to screen for action-collapse contamination, and point-supervision of a single link is insufficient for articulated robots; genuine geometric safety will require full-body collision representations and cross-architecture validation.\n\n\\section{Limitations}\\label{sec:limitations}\n\nAll experiments use MuJoCo simulation (SafeLIBERO, two VLA families, four tasks); generality to other benchmarks or real hardware is untested. dfCAR requires bimodal displacement separation (Figure~\\ref{fig:displacement}) and may need task-specific $\\tau_d$ calibration. The EE-only null result applies to auxiliary-loss integration, not constrained optimization or runtime filtering (\\S\\ref{sec:related}). Oracle refinement uses one seed per variant ($n{=}1$, 160 episodes). The training ablation ($n{=}3$ seeds; MDE ${\\approx}$ 5.6\\,pp at 80\\% power) cannot rule out a small SDF effect (2--5\\,pp) without larger samples.\n",
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01VDVAAAMbAwnUmGMsGn565y`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "91c994c8-79a8-4704-ba1b-e2ec755bba34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01NYEcmU6bHyLhaHbH1qzCQa`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "d4dc7b92-c070-4e55-b22a-fd8cdefb94ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186HaSJqAzntvz4KBUB8sZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12575,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12575
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

_source line 25 · 2026-05-29T17:42:17.552Z_

<details><summary>↩ Tool result · `toolu_01NYEcmU6bHyLhaHbH1qzCQa`</summary>

```text
1	% References
2	
3	% ===== VLA Foundation Models =====
4	
5	@article{black2024pi0,
6	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
7	  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},
8	  journal={arXiv preprint arXiv:2410.24164},
9	  year={2024}
10	}
11	
12	@inproceedings{kim2024openvla,
13	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
14	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},
15	  booktitle={Conference on Robot Learning (CoRL)},
16	  year={2024}
17	}
18	
19	@inproceedings{brohan2023rt2,
20	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
21	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
22	  booktitle={Conference on Robot Learning (CoRL)},
23	  year={2023}
24	}
25	
26	% ===== Collision-Aware VLA Methods =====
27	
28	@article{hu2025vlsa,
29	  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
30	  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},
31	  journal={arXiv preprint arXiv:2512.11891},
32	  year={2025}
33	}
34	
35	@inproceedings{zhang2025safevla,
36	  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
37	  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},
38	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
39	  year={2025}
40	}
41	
42	@article{cofreeevla2026,
43	  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},
44	  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},
45	  journal={arXiv preprint arXiv:2601.21712},
46	  year={2026}
47	}
48	
49	@article{spalter2024ikinqp,
50	  title={Towards Online Safety Corrections for Robotic Manipulation Policies},
51	  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},
52	  journal={arXiv preprint arXiv:2409.08233},
53	  year={2024}
54	}
55	
56	@inproceedings{li2024langguided,
57	  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},
58	  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},
59	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
60	  year={2025}
61	}
62	
63	@article{yang2025cape,
64	  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},
65	  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},
66	  journal={arXiv preprint arXiv:2511.22773},
67	  year={2025}
68	}
69	
70	% ===== Safety in Diffusion Planning =====
71	
72	@inproceedings{xiao2025safediffuser,
73	  title={{SafeDiffuser}: Safe Planning with Diffusion Probabilistic Models},
74	  author={Xiao, Wei and Wang, Tsun-Hsuan and Gan, Chuang and Hasani, Ramin and Lechner, Mathias and Rus, Daniela},
75	  booktitle={International Conference on Learning Representations (ICLR)},
76	  year={2025}
77	}
78	
79	% ===== SDF in Robotics =====
80	
81	@inproceedings{park2019deepsdf,
82	  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},
83	  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},
84	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
85	  year={2019}
86	}
87	
88	@inproceedings{ortiz2022isdf,
89	  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},
90	  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\"o}fer, Michael and Mukadam, Mustafa},
91	  booktitle={Robotics: Science and Systems (RSS)},
92	  year={2022}
93	}
94	
95	@article{zhi2021diffco,
96	  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},
97	  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},
98	  journal={IEEE Transactions on Robotics},
99	  volume={38},
100	  number={5},
101	  pages={2668--2685},
102	  year={2022}
103	}
104	
105	% ===== Benchmarks and Training =====
106	
107	@inproceedings{liu2023libero,
108	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
109	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
110	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
111	  year={2023}
112	}
113	
114	@inproceedings{lipman2023flow,
115	  title={Flow Matching for Generative Modeling},
116	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
117	  booktitle={International Conference on Learning Representations (ICLR)},
118	  year={2023}
119	}
120	
121	% ===== Evaluation Reliability =====
122	
123	@inproceedings{gururangan2018annotation,
124	  title={Annotation Artifacts in Natural Language Inference Data},
125	  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},
126	  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
127	  year={2018}
128	}
129	
130	@inproceedings{karwowski2024goodhart,
131	  title={Goodhart's Law in Reinforcement Learning},
132	  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},
133	  booktitle={International Conference on Learning Representations (ICLR)},
134	  year={2024}
135	}
136	
137	% ===== Configuration/Robot-Body SDF =====
138	
139	@inproceedings{li2024cdf,
140	  title={Configuration Space Distance Fields for Manipulation Planning},
141	  author={Li, Yiming and Chi, Xuemin and Razmjoo, Amirreza and Calinon, Sylvain},
142	  booktitle={Robotics: Science and Systems (RSS)},
143	  year={2024}
144	}
145	
146	@inproceedings{li2024rdf,
147	  title={Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation},
148	  author={Li, Yiming and Zhang, Yan and Razmjoo, Amirreza and Calinon, Sylvain},
149	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
150	  year={2024}
151	}
152	
153	% ===== SDF in Robotics (additional) =====
154	
155	@inproceedings{vasilopoulos2023ramp,
156	  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},
157	  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},
158	  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
159	  year={2023}
160	}
161	
162	@article{chen2026cssdfnet,
163	  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},
164	  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},
165	  journal={arXiv preprint arXiv:2603.18669},
166	  year={2026}
167	}
168	
169	@article{jacquet2025neuralnmpc,
170	  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},
171	  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},
172	  journal={The International Journal of Robotics Research},
173	  year={2025}
174	}
175	
176	% ===== 3D-Aware VLA Methods =====
177	
178	@article{depthvla2025,
179	  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},
180	  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},
181	  journal={arXiv preprint arXiv:2510.13375},
182	  year={2025}
183	}
184	
185	@article{li2025qdepth,
186	  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},
187	  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},
188	  journal={arXiv preprint arXiv:2510.14836},
189	  year={2025}
190	}
191	
192	@inproceedings{li2025spatialforcing,
193	  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},
194	  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},
195	  booktitle={International Conference on Learning Representations (ICLR)},
196	  year={2026}
197	}
198	
199	% ===== Parameter-Efficient Fine-Tuning =====
200	
201	@inproceedings{hu2022lora,
202	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
203	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
204	  booktitle = {International Conference on Learning Representations (ICLR)},
205	  year      = {2022},
206	}
207	
208	% ===== VLA Safety Survey =====
209	
210	@article{li2026vlasafety,
211	  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
212	  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},
213	  journal={arXiv preprint arXiv:2604.23775},
214	  year={2026}
215	}
216	
217	% ===== VLA Safety Evaluation Benchmarks =====
218	
219	@article{chen2026hazardarena,
220	  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},
221	  author={Chen, Zixing and Gao, Yifeng and Wang, Li and Zhao, Yunhan and Liu, Yi and Li, Jiayu and Zheng, Xiang and Wu, Zuxuan and Wang, Cong and Ma, Xingjun and Jiang, Yu-Gang},
222	  journal={arXiv preprint arXiv:2604.12447},
223	  year={2026}
224	}
225	
226	% ===== Action Collapse =====
227	
228	@inproceedings{dong2025conditioning,
229	  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},
230	  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},
231	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
232	  year={2025}
233	}
234	
235	% ===== Evaluation Methodology =====
236	
237	@article{snyder2026beyond,
238	  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},
239	  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},
240	  journal={arXiv preprint arXiv:2603.13616},
241	  year={2026}
242	}
243	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "d742c406-445d-4b57-901b-8c1fa02f8aa7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
      "content": "% References\n\n% ===== VLA Foundation Models =====\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Collision-Aware VLA Methods =====\n\n@article{hu2025vlsa,\n  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},\n  journal={arXiv preprint arXiv:2512.11891},\n  year={2025}\n}\n\n@inproceedings{zhang2025safevla,\n  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cofreeevla2026,\n  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},\n  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},\n  journal={arXiv preprint arXiv:2601.21712},\n  year={2026}\n}\n\n@article{spalter2024ikinqp,\n  title={Towards Online Safety Corrections for Robotic Manipulation Policies},\n  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},\n  journal={arXiv preprint arXiv:2409.08233},\n  year={2024}\n}\n\n@inproceedings{li2024langguided,\n  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},\n  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2025}\n}\n\n@article{yang2025cape,\n  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},\n  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},\n  journal={arXiv preprint arXiv:2511.22773},\n  year={2025}\n}\n\n% ===== Safety in Diffusion Planning =====\n\n@inproceedings{xiao2025safediffuser,\n  title={{SafeDiffuser}: Safe Planning with Diffusion Probabilistic Models},\n  author={Xiao, Wei and Wang, Tsun-Hsuan and Gan, Chuang and Hasani, Ramin and Lechner, Mathias and Rus, Daniela},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n% ===== SDF in Robotics =====\n\n@inproceedings{park2019deepsdf,\n  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},\n  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2019}\n}\n\n@inproceedings{ortiz2022isdf,\n  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},\n  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\\\"o}fer, Michael and Mukadam, Mustafa},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2022}\n}\n\n@article{zhi2021diffco,\n  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},\n  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},\n  journal={IEEE Transactions on Robotics},\n  volume={38},\n  number={5},\n  pages={2668--2685},\n  year={2022}\n}\n\n% ===== Benchmarks and Training =====\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ===== Evaluation Reliability =====\n\n@inproceedings{gururangan2018annotation,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year={2018}\n}\n\n@inproceedings{karwowski2024goodhart,\n  title={Goodhart's Law in Reinforcement Learning},\n  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% ===== Configuration/Robot-Body SDF =====\n\n@inproceedings{li2024cdf,\n  title={Configuration Space Distance Fields for Manipulation Planning},\n  author={Li, Yiming and Chi, Xuemin and Razmjoo, Amirreza and Calinon, Sylvain},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{li2024rdf,\n  title={Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation},\n  author={Li, Yiming and Zhang, Yan and Razmjoo, Amirreza and Calinon, Sylvain},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024}\n}\n\n% ===== SDF in Robotics (additional) =====\n\n@inproceedings{vasilopoulos2023ramp,\n  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},\n  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},\n  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},\n  year={2023}\n}\n\n@article{chen2026cssdfnet,\n  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},\n  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},\n  journal={arXiv preprint arXiv:2603.18669},\n  year={2026}\n}\n\n@article{jacquet2025neuralnmpc,\n  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},\n  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},\n  journal={The International Journal of Robotics Research},\n  year={2025}\n}\n\n% ===== 3D-Aware VLA Methods =====\n\n@article{depthvla2025,\n  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},\n  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},\n  journal={arXiv preprint arXiv:2510.13375},\n  year={2025}\n}\n\n@article{li2025qdepth,\n  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},\n  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},\n  journal={arXiv preprint arXiv:2510.14836},\n  year={2025}\n}\n\n@inproceedings{li2025spatialforcing,\n  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},\n  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026}\n}\n\n% ===== Parameter-Efficient Fine-Tuning =====\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n}\n\n% ===== VLA Safety Survey =====\n\n@article{li2026vlasafety,\n  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},\n  journal={arXiv preprint arXiv:2604.23775},\n  year={2026}\n}\n\n% ===== VLA Safety Evaluation Benchmarks =====\n\n@article{chen2026hazardarena,\n  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},\n  author={Chen, Zixing and Gao, Yifeng and Wang, Li and Zhao, Yunhan and Liu, Yi and Li, Jiayu and Zheng, Xiang and Wu, Zuxuan and Wang, Cong and Ma, Xingjun and Jiang, Yu-Gang},\n  journal={arXiv preprint arXiv:2604.12447},\n  year={2026}\n}\n\n% ===== Action Collapse =====\n\n@inproceedings{dong2025conditioning,\n  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},\n  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n% ===== Evaluation Methodology =====\n\n@article{snyder2026beyond,\n  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},\n  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},\n  journal={arXiv preprint arXiv:2603.13616},\n  year={2026}\n}\n",
      "numLines": 243,
      "startLine": 1,
      "totalLines": 243
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T17:42:17.701Z_

<details><summary>↩ Tool result · `toolu_01VDVAAAMbAwnUmGMsGn565y`</summary>

```text
1	\section{Complete Multi-Seed Results}
2	\label{sec:appendix_multiseed}
3	
4	Table~\ref{tab:multiseed_full} reports individual-seed CAR and TSR for all fine-tuned conditions at the 30K checkpoint (200 episodes each, evaluation seed\,=\,7). These per-seed values underlie the means reported in Table~\ref{tab:avoidance_source}.
5	
6	\begin{table}[h]
7	\centering
8	\caption{Per-seed CAR and TSR (\%) at 30K steps, evaluation seed\,=\,7 (200 episodes). All episodes exhibit displacement $>$\,0.37\,m and 0\% action-collapse rate.}
9	\label{tab:multiseed_full}
10	\vspace{2pt}
11	\small
12	\begin{tabular}{llcccc}
13	\toprule
14	Condition & Seed & CAR & TSR & Mean CAR & Mean TSR \\
15	\midrule
16	\multirow{3}{*}{LoRA-only}
17	  & s0 & 57.0 & 46.0 & \multirow{3}{*}{54.83$\pm$2.25} & \multirow{3}{*}{49.7$\pm$3.2} \\
18	  & s1 & 52.5 & 51.5 & & \\
19	  & s2 & 55.0 & 51.5 & & \\
20	\midrule
21	\multirow{3}{*}{SDF $\lambda{=}0.005$}
22	  & s0 & 57.0 & 55.5 & \multirow{3}{*}{54.5$\pm$2.29} & \multirow{3}{*}{54.0$\pm$3.0} \\
23	  & s1 & 54.0 & 50.5 & & \\
24	  & s2 & 52.5 & 56.0 & & \\
25	\midrule
26	\multirow{3}{*}{SDF $\lambda{=}0.01$}
27	  & s0 & 57.0 & 52.5 & \multirow{3}{*}{56.33$\pm$1.61} & \multirow{3}{*}{53.8$\pm$1.5} \\
28	  & s1 & 57.5 & 55.5 & & \\
29	  & s2 & 54.5 & 53.5 & & \\
30	\midrule
31	\multirow{3}{*}{SDF $\lambda{=}0.1$}
32	  & s0 & 58.0 & 47.0 & \multirow{3}{*}{57.00$\pm$2.18} & \multirow{3}{*}{50.2$\pm$3.9} \\
33	  & s1 & 58.5 & 49.0 & & \\
34	  & s2 & 54.5 & 54.5 & & \\
35	\bottomrule
36	\end{tabular}
37	\end{table}
38	
39	\section{Displacement Distribution}
40	\label{sec:appendix_displacement}
41	
42	The displacement distribution is shown in Figure~\ref{fig:displacement} (main text).
43	
44	\section{Displacement Threshold Sensitivity Analysis}
45	\label{sec:appendix_threshold}
46	
47	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% action-collapse rate even at the most conservative setting.
48	
49	\begin{table}[h]
50	\centering
51	\caption{Action-collapse rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
52	\label{tab:threshold_sensitivity}
53	\begin{tabular}{lccc}
54	\toprule
55	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
56	\midrule
57	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
58	0.1 mm  & 99.6 & 0.0 & 0.0 \\
59	1.0 mm  & 100.0 & 0.0 & 0.0 \\
60	10 mm   & 100.0 & 0.0 & 0.0 \\
61	\bottomrule
62	\end{tabular}
63	\end{table}
64	
65	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.
66	
67	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
68	
69	\begin{table}[h]
70	\centering
71	\caption{dfCAR (\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\tau_d \in [2, 200]$\,mm; at $\tau_d = 300$\,mm, at most 2 episodes are excluded.}
72	\label{tab:dfcar_threshold}
73	\vspace{2pt}
74	\footnotesize
75	\begin{tabular}{lcccccccc}
76	\toprule
77	& \multicolumn{8}{c}{$\tau_d$ (mm)} \\
78	\cmidrule(lr){2-9}
79	Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\
80	\midrule
81	LoRA s0            & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
82	LoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\
83	SDF $\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\
84	SDF $\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\
85	SDF $\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\
86	SDF $\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
87	SDF $\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\
88	SDF $\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\
89	\bottomrule
90	\end{tabular}
91	\end{table}
92	
93	
94	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
95	
96	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
97	
98	\begin{table}[h]
99	\centering
100	\caption{Per-task TSR (\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\,=\,71.5\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}
101	\label{tab:per_task_tsr}
102	\vspace{2pt}
103	\small
104	\begin{tabular}{lcccc}
105	\toprule
106	Task & Pi0.5 Base & LoRA-only & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
107	 & (seed\,=\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\
108	\midrule
109	Orange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\
110	Choco.\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\
111	Milk              & 66.0 & 44.7 & 35.3 & 48.7 \\
112	BBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\
113	\midrule
114	Mean              & 71.5 & 51.5 & 54.0 & 53.8 \\
115	\bottomrule
116	\end{tabular}
117	\end{table}
118	
119	\section{Per-Task CAR Breakdown}\label{sec:appendix_pertask_car}
120	
121	Table~\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\S\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.
122	
123	\begin{table}[h]
124	\centering
125	\caption{Per-task CAR (\%) at 30K steps. $\lambda{=}0.005$, $\lambda{=}0.01$, and $\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}
126	\label{tab:per_task_car}
127	\vspace{2pt}
128	\small
129	\begin{tabular}{lccccc}
130	\toprule
131	Condition & OJ & CP & Milk & BBQ & Agg. \\
132	\midrule
133	LoRA s0 & 68 & 74 & 66 & 20 & 57.0 \\
134	LoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\
135	LoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\
136	SDF $\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\
137	SDF $\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\
138	SDF $\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\
139	SDF $\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\
140	SDF $\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\
141	SDF $\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\
142	\bottomrule
143	\end{tabular}
144	\end{table}
145	
146	For the $\lambda = 0.1$ condition, seed~1 records \texttt{avg\_max\_obstacle\_displacement} of 0.0553\,m (per-task: OJ\,=\,0.033, CP\,=\,0.055, Milk\,=\,0.041, BBQ\,=\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.
147	
148	\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
149	
150	See Table~\ref{tab:ssr} (main text) for SSR and SSR/TSR ratio across conditions.
151	
152	\section{Per-Task Oracle Analysis}
153	\label{sec:appendix_pertask}
154	\label{sec:appendix_pertask_oracle}
155	
156	Table~\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\texttt{chocolate\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive improves to 55.0\% and Oracle-feature to 47.5\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\texttt{orange\_juice}) from 96.0\% to 82.5\% and task~2 (\texttt{milk}) from 98.0\% to 77.5\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.
157	
158	The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49), and CAR (76.9\%) shows no advantage despite 17$\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.
159	
160	\begin{table}[h]
161	\centering
162	\caption{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}
163	\label{tab:oracle_pertask}
164	\vspace{2pt}
165	\small
166	\begin{tabular}{lccccc}
167	\toprule
168	Method & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\
169	\midrule
170	LoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\
171	\midrule
172	Oracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\
173	Oracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\
174	Oracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\
175	\bottomrule
176	\end{tabular}
177	\end{table}
178	
179	
180	\paragraph{Oracle on non-collapsed baseline (Pi0.5 LoRA).}
181	Table~\ref{tab:oracle_pertask_pi05} reports the per-task breakdown for Oracle-adaptive applied to Pi0.5 LoRA s0 (0\% action-collapse rate). The aggregate CAR drop ($-$5.1\,pp) masks a heterogeneous pattern: refinement improves CAR on \texttt{chocolate\_pudding} ($+$1.0\,pp) and \texttt{milk} ($+$4.0\,pp) but degrades \texttt{orange\_juice} ($-$18.0\,pp) and \texttt{bbq\_sauce} ($-$7.5\,pp). This mirrors the Pi0 oracle pattern in Table~\ref{tab:oracle_pertask}, where the same task-dependent asymmetry appears. The consistency across both model families confirms that the counterproductive effect is structural: EE-only SDF refinement cannot protect intermediate arm links that pass through unmonitored obstacle volumes.
182	
183	\begin{table}[h]
184	\centering
185	\caption{Per-task CAR (\%) for Oracle-adaptive on Pi0.5 LoRA s0 (40 ep/task) vs.\ unrefined baseline (50 ep/task). EE-only refinement helps on EE-collision tasks but worsens arm-link collisions.}
186	\label{tab:oracle_pertask_pi05}
187	\vspace{2pt}
188	\small
189	\begin{tabular}{lccccc}
190	\toprule
191	Method & OJ & CP & Milk & BBQ & Agg. \\
192	\midrule
193	Pi0.5 LoRA s0 (no refine) & 68.0 & 74.0 & 66.0 & 20.0 & 57.0 \\
194	Pi0.5 Oracle-adaptive & 50.0 & 75.0 & 70.0 & 12.5 & 51.9 \\
195	\midrule
196	$\Delta$ & $-$18.0 & $+$1.0 & $+$4.0 & $-$7.5 & $-$5.1 \\
197	\bottomrule
198	\end{tabular}
199	\end{table}
200	
201	
202	\section{Null Distribution for SDF Loss Weight Analysis}
203	\label{sec:appendix_null}
204	
205	We construct a null distribution by pooling the three LoRA-only seeds and three $\lambda = 0.005$ seeds into six per-seed CAR measurements: 57.0\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 55.0\% (LoRA s2), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.67\% and standard deviation 2.04\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 57.00\% (3 seeds: 58.0\%, 58.5\%, 54.5\%) yields a two-tailed permutation $p = 0.155$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\alpha = 0.05$).
206	
207	The permutation test makes no distributional assumptions. Pooling the six null values $\{57, 52.5, 55, 57, 54, 52.5\}$ and three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$ into nine measurements, we enumerate all $\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 13/84 \approx 0.155$. With the third seed ($s_2 = 54.5\%$) pulling the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.
208	
209	\paragraph{Alternative null construction (Null~A).}
210	If only the three LoRA-only seeds are used as the null pool ($\{57.0, 52.5, 55.0\}$), we obtain $\binom{6}{3} = 20$ permutations for each comparison. For $\lambda = 0.1$ (treatment mean 57.00\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 5/20 = 0.250$. For $\lambda = 0.01$ (treatment mean 56.33\%): one-tailed $p = 6/20 = 0.300$, two-tailed $p = 12/20 = 0.600$. Under the broader Null~B pool, $\lambda = 0.01$ yields one-tailed $p = 13/84 \approx 0.155$, two-tailed $p = 25/84 \approx 0.298$. All tests are non-significant at $\alpha = 0.05$; the narrower Null~A yields \emph{larger} $p$-values because the LoRA-only pool already contains a high seed (57.0\%), making the treatment means less extreme by comparison.
211	
212	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\% at the 18K checkpoint (13K steps of Phase~2 training, single seed s2; full 30K training did not reach the full 30K-step budget). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.
213	
214	\section{Step-wise Checkpoint Analysis for \texorpdfstring{$\lambda = 0.1$}{lambda = 0.1}}
215	\label{sec:appendix_stepwise}
216	
217	Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\%) pulls the three-seed mean to 57.00\%, within the null band ($p = 0.155$).
218	
219	\begin{table}[h]
220	\centering
221	\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\%) remains within the null band ($p = 0.155$, two-tailed permutation).}
222	\label{tab:stepwise_lambda01}
223	\vspace{2pt}
224	\small
225	\begin{tabular}{lcccc}
226	\toprule
227	Checkpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\
228	\midrule
229	16K steps & 55.5 & 56.0 & -- & 55.75 \\
230	20K steps & 55.0 & 56.0 & -- & 55.5 \\
231	22K steps & 60.5 & 56.5 & -- & 58.5 \\
232	24K steps & 52.5 & -- & -- & -- \\
233	26K steps & 53.5 & -- & -- & -- \\
234	28K steps & 54.5 & -- & -- & -- \\
235	30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\
236	\bottomrule
237	\end{tabular}
238	\end{table}
239	
240	Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$3\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). At 30K, the third seed ($s_2 = 54.5\%$) falls well within the null range, pulling the three-seed mean to 57.00\% and rendering the earlier two-seed departure non-significant ($p = 0.155$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
241	
242	
243	\section{Oracle SDF Refinement Details}
244	\label{sec:appendix_oracle}
245	
246	All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\times$ 40).
247	
248	\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.
249	
250	\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.
251	
252	\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space).
253	
254	
255	\section{Cross-Scene Validation: spatial\_bowl}
256	\label{sec:appendix_spatial_bowl}
257	
258	Cross-scene validation results are reported in Table~\ref{tab:spatial_bowl} (main text). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), with a single training seed (seed~0) and evaluation seed (seed~7, 200 episodes). The \texttt{spatial\_bowl} suite uses a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). The substantially lower CAR (11--12\% vs.\ 54--57\%) reflects greater scene difficulty; both conditions are equally affected ($\Delta$CAR\,=\,$-$0.5\,pp).
259	
260	
261	\section{Evaluation Seed Robustness}
262	\label{sec:appendix_eval_seed}
263	
264	To verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate key model configurations under multiple evaluation seeds (200 episodes each). Table~\ref{tab:eval_seed_robustness} reports aggregate CAR and TSR across all tested seeds.
265	
266	\begin{table}[h]
267	\centering
268	\caption{Eval-seed robustness: aggregate CAR and TSR (\%) across evaluation seeds (200 episodes each). Dashes indicate untested seeds. CAR ranges overlap across all three conditions, confirming that SDF redundancy is not an eval-seed artifact.}
269	\label{tab:eval_seed_robustness}
270	\vspace{2pt}
271	\footnotesize
272	\begin{tabular}{llccccccl}
273	\toprule
274	& & \multicolumn{6}{c}{Evaluation seed} & \\
275	\cmidrule(lr){3-8}
276	Condition & & 0 & 7 & 42 & 99 & 123 & 256 & Mean$\pm$Std \\
277	\midrule
278	\multirow{2}{*}{LoRA s0}
279	  & CAR & 53.0 & 57.0 & 56.5 & 57.5 & 53.0 & --- & 55.4$\pm$2.2 \\
280	  & TSR & 55.5 & 46.0 & 46.0 & 52.0 & 50.5 & --- & 50.0$\pm$4.1 \\
281	\midrule
282	\multirow{2}{*}{SDF $\lambda{=}0.01$ s0}
283	  & CAR & 52.5 & 57.0 & --- & 57.0 & --- & 57.0 & 55.9$\pm$2.3 \\
284	  & TSR & 48.5 & 52.5 & --- & 46.5 & --- & 48.0 & 48.9$\pm$2.6 \\
285	\midrule
286	\multirow{2}{*}{SDF $\lambda{=}0.1$ s0}
287	  & CAR & --- & 58.0 & 59.0 & --- & 58.5 & 57.0 & 58.1$\pm$0.9 \\
288	  & TSR & --- & 47.0 & 52.5 & --- & 53.5 & 48.0 & 50.3$\pm$3.2 \\
289	\bottomrule
290	\end{tabular}
291	\end{table}
292	
293	LoRA s0 CAR ranges from 53.0\% to 57.5\% across five evaluation seeds (std\,=\,2.2\,pp), consistent with binomial sampling noise at $n{=}50$ episodes per task. SDF $\lambda{=}0.01$ s0 produces near-identical mean CAR (55.9\% across four eval seeds vs.\ 55.4\% for LoRA), confirming that the null result holds across eval conditions. SDF $\lambda{=}0.1$ s0 shows a slightly higher mean (58.1\%), but the ranges overlap with LoRA-only, and the difference (2.8\,pp, ${<}$1.3$\sigma$) remains non-significant. The per-task CAR ordering (chocolate\_pudding highest, bbq\_sauce lowest) is preserved across all seeds and conditions, reinforcing the demonstration-driven avoidance hypothesis.
294	
295	Table~\ref{tab:eval_seed_car_detail} provides per-task CAR for the five-seed LoRA evaluation, the most complete eval-seed battery.
296	
297	\begin{table}[h]
298	\centering
299	\caption{Per-task CAR (\%) for LoRA s0 across five evaluation seeds. The per-task fingerprint (CP highest, BBQ lowest) is invariant across all seeds.}
300	\label{tab:eval_seed_car_detail}
301	\vspace{2pt}
302	\small
303	\begin{tabular}{lccccc}
304	\toprule
305	Eval seed & OJ & CP & Milk & BBQ & Agg. \\
306	\midrule
307	0   & 46 & 70 & 74 & 22 & 53.0 \\
308	7   & 68 & 74 & 66 & 20 & 57.0 \\
309	42  & 60 & 70 & 68 & 28 & 56.5 \\
310	99  & 58 & 76 & 66 & 30 & 57.5 \\
311	123 & 52 & 74 & 66 & 20 & 53.0 \\
312	\midrule
313	Mean$\pm$Std & 56.8$\pm$8.3 & 72.8$\pm$2.7 & 68.0$\pm$3.5 & 24.0$\pm$4.7 & 55.4$\pm$2.2 \\
314	\bottomrule
315	\end{tabular}
316	\end{table}
317	
318	
319	\section{Training Details}
320	\label{sec:appendix_training}
321	
322	\paragraph{Architecture.}
323	We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
324	
325	\paragraph{Training schedule.}
326	Training proceeds in two phases:
327	\begin{itemize}
328	    \item \textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.
329	    \item \textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.
330	\end{itemize}
331	
332	\paragraph{Hyperparameters.}
333	\begin{table}[h]
334	\centering
335	\caption{Training hyperparameters.}
336	\label{tab:hyperparams}
337	\begin{tabular}{ll}
338	\toprule
339	Parameter & Value \\
340	\midrule
341	Base model & Pi0.5 (OpenPi, $\sim$3.5B parameters) \\
342	Optimizer & AdamW \\
343	Learning rate & $2.5 \times 10^{-5}$ (cosine decay to $\mathrm{lr}/10$) \\
344	Warmup steps & 1000 \\
345	Batch size & 32 \\
346	Total steps & 30000 \\
347	$\lambda_\mathrm{sdf}$ & \{0.005, 0.01, 0.1\} \\
348	$\lambda_\mathrm{ee}$ & 0.01 \\
349	SDF query points per step & 64 \\
350	SDF clamp $\delta$ & 0.05 m \\
351	Eikonal weight & 0.1 \\
352	LoRA rank (vision) & 16 \\
353	LoRA rank (action) & 32 \\
354	Phase 1 duration & 5000 steps \\
355	\bottomrule
356	\end{tabular}
357	\end{table}
358	
359	\paragraph{Evaluation protocol.}
360	Each episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\sim}$5\% to ${\sim}$52\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).
361	
362	\paragraph{Data.}
363	We use the SafeLIBERO object\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.
364	
365	\paragraph{Computational resources.}
366	All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.
367	
368	
369	\section{TSR Collapse Mechanism Analysis}
370	\label{sec:appendix_tsr_collapse}
371	
372	Fine-tuning Pi0.5 with LoRA alone (no SDF supervision) reduces TSR from 71.5\% to 49.7\,$\pm$\,3.2\%, a drop of 21.8\,pp (Table~\ref{tab:multiseed_full}). Adding SDF supervision does not exacerbate this decline: TSR under $\lambda = 0.005$ is 54.0\,$\pm$\,3.0\% ($-$17.5\,pp), under $\lambda = 0.01$ is 53.8\,$\pm$\,1.5\% ($-$17.7\,pp), and under $\lambda = 0.1$ is 50.2\,$\pm$\,3.9\% ($-$21.3\,pp). All SDF conditions are comparable to the LoRA-only baseline, and the largest SDF drop ($\lambda = 0.1$, $-$21.3\,pp) matches the LoRA-only drop ($-$21.8\,pp) to within 0.5\,pp. This confirms that SDF auxiliary loss is not the cause of TSR degradation.
373	
374	The mechanism is catastrophic forgetting of task semantics induced by LoRA fine-tuning on a narrow 4-task subset of the pre-training distribution. Qualitative inspection reveals that fine-tuned models retain full motor capability: 0\% action-collapse rate, end-effector displacement $>$\,0.37\,m, and active obstacle interaction (mean obstacle displacement ${\sim}$0.05\,m), but lose goal-directed grasping and placing behavior. The dominant failure mode shifts from collision (baseline safe failure rate 0.5\%) to task incompletion without collision (${\sim}$50\% of episodes), representing a 100$\times$ increase in safe failures. The robot moves purposefully through the workspace but fails to acquire or deliver the target object, consistent with retained low-level motor skills and degraded high-level task understanding.
375	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "a25720c4-b9f9-4bca-8ff8-1f2b5a3fef8f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "\\section{Complete Multi-Seed Results}\n\\label{sec:appendix_multiseed}\n\nTable~\\ref{tab:multiseed_full} reports individual-seed CAR and TSR for all fine-tuned conditions at the 30K checkpoint (200 episodes each, evaluation seed\\,=\\,7). These per-seed values underlie the means reported in Table~\\ref{tab:avoidance_source}.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR and TSR (\\%) at 30K steps, evaluation seed\\,=\\,7 (200 episodes). All episodes exhibit displacement $>$\\,0.37\\,m and 0\\% action-collapse rate.}\n\\label{tab:multiseed_full}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nCondition & Seed & CAR & TSR & Mean CAR & Mean TSR \\\\\n\\midrule\n\\multirow{3}{*}{LoRA-only}\n  & s0 & 57.0 & 46.0 & \\multirow{3}{*}{54.83$\\pm$2.25} & \\multirow{3}{*}{49.7$\\pm$3.2} \\\\\n  & s1 & 52.5 & 51.5 & & \\\\\n  & s2 & 55.0 & 51.5 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.005$}\n  & s0 & 57.0 & 55.5 & \\multirow{3}{*}{54.5$\\pm$2.29} & \\multirow{3}{*}{54.0$\\pm$3.0} \\\\\n  & s1 & 54.0 & 50.5 & & \\\\\n  & s2 & 52.5 & 56.0 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.01$}\n  & s0 & 57.0 & 52.5 & \\multirow{3}{*}{56.33$\\pm$1.61} & \\multirow{3}{*}{53.8$\\pm$1.5} \\\\\n  & s1 & 57.5 & 55.5 & & \\\\\n  & s2 & 54.5 & 53.5 & & \\\\\n\\midrule\n\\multirow{3}{*}{SDF $\\lambda{=}0.1$}\n  & s0 & 58.0 & 47.0 & \\multirow{3}{*}{57.00$\\pm$2.18} & \\multirow{3}{*}{50.2$\\pm$3.9} \\\\\n  & s1 & 58.5 & 49.0 & & \\\\\n  & s2 & 54.5 & 54.5 & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\nThe displacement distribution is shown in Figure~\\ref{fig:displacement} (main text).\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 68 & 74 & 66 & 20 & 57.0 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nSee Table~\\ref{tab:ssr} (main text) for SSR and SSR/TSR ratio across conditions.\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\paragraph{Oracle on non-collapsed baseline (Pi0.5 LoRA).}\nTable~\\ref{tab:oracle_pertask_pi05} reports the per-task breakdown for Oracle-adaptive applied to Pi0.5 LoRA s0 (0\\% action-collapse rate). The aggregate CAR drop ($-$5.1\\,pp) masks a heterogeneous pattern: refinement improves CAR on \\texttt{chocolate\\_pudding} ($+$1.0\\,pp) and \\texttt{milk} ($+$4.0\\,pp) but degrades \\texttt{orange\\_juice} ($-$18.0\\,pp) and \\texttt{bbq\\_sauce} ($-$7.5\\,pp). This mirrors the Pi0 oracle pattern in Table~\\ref{tab:oracle_pertask}, where the same task-dependent asymmetry appears. The consistency across both model families confirms that the counterproductive effect is structural: EE-only SDF refinement cannot protect intermediate arm links that pass through unmonitored obstacle volumes.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for Oracle-adaptive on Pi0.5 LoRA s0 (40 ep/task) vs.\\ unrefined baseline (50 ep/task). EE-only refinement helps on EE-collision tasks but worsens arm-link collisions.}\n\\label{tab:oracle_pertask_pi05}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nPi0.5 LoRA s0 (no refine) & 68.0 & 74.0 & 66.0 & 20.0 & 57.0 \\\\\nPi0.5 Oracle-adaptive & 50.0 & 75.0 & 70.0 & 12.5 & 51.9 \\\\\n\\midrule\n$\\Delta$ & $-$18.0 & $+$1.0 & $+$4.0 & $-$7.5 & $-$5.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 57.0\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.67\\% and standard deviation 2.04\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.155$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{57, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 13/84 \\approx 0.155$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{57.0, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 5/20 = 0.250$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 6/20 = 0.300$, two-tailed $p = 12/20 = 0.600$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 13/84 \\approx 0.155$, two-tailed $p = 25/84 \\approx 0.298$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (57.0\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed s2; full 30K training did not reach the full 30K-step budget). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.155$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.155$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.155$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nCross-scene validation results are reported in Table~\\ref{tab:spatial_bowl} (main text). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), with a single training seed (seed~0) and evaluation seed (seed~7, 200 episodes). The \\texttt{spatial\\_bowl} suite uses a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). The substantially lower CAR (11--12\\% vs.\\ 54--57\\%) reflects greater scene difficulty; both conditions are equally affected ($\\Delta$CAR\\,=\\,$-$0.5\\,pp).\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate key model configurations under multiple evaluation seeds (200 episodes each). Table~\\ref{tab:eval_seed_robustness} reports aggregate CAR and TSR across all tested seeds.\n\n\\begin{table}[h]\n\\centering\n\\caption{Eval-seed robustness: aggregate CAR and TSR (\\%) across evaluation seeds (200 episodes each). Dashes indicate untested seeds. CAR ranges overlap across all three conditions, confirming that SDF redundancy is not an eval-seed artifact.}\n\\label{tab:eval_seed_robustness}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{llccccccl}\n\\toprule\n& & \\multicolumn{6}{c}{Evaluation seed} & \\\\\n\\cmidrule(lr){3-8}\nCondition & & 0 & 7 & 42 & 99 & 123 & 256 & Mean$\\pm$Std \\\\\n\\midrule\n\\multirow{2}{*}{LoRA s0}\n  & CAR & 53.0 & 57.0 & 56.5 & 57.5 & 53.0 & --- & 55.4$\\pm$2.2 \\\\\n  & TSR & 55.5 & 46.0 & 46.0 & 52.0 & 50.5 & --- & 50.0$\\pm$4.1 \\\\\n\\midrule\n\\multirow{2}{*}{SDF $\\lambda{=}0.01$ s0}\n  & CAR & 52.5 & 57.0 & --- & 57.0 & --- & 57.0 & 55.9$\\pm$2.3 \\\\\n  & TSR & 48.5 & 52.5 & --- & 46.5 & --- & 48.0 & 48.9$\\pm$2.6 \\\\\n\\midrule\n\\multirow{2}{*}{SDF $\\lambda{=}0.1$ s0}\n  & CAR & --- & 58.0 & 59.0 & --- & 58.5 & 57.0 & 58.1$\\pm$0.9 \\\\\n  & TSR & --- & 47.0 & 52.5 & --- & 53.5 & 48.0 & 50.3$\\pm$3.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLoRA s0 CAR ranges from 53.0\\% to 57.5\\% across five evaluation seeds (std\\,=\\,2.2\\,pp), consistent with binomial sampling noise at $n{=}50$ episodes per task. SDF $\\lambda{=}0.01$ s0 produces near-identical mean CAR (55.9\\% across four eval seeds vs.\\ 55.4\\% for LoRA), confirming that the null result holds across eval conditions. SDF $\\lambda{=}0.1$ s0 shows a slightly higher mean (58.1\\%), but the ranges overlap with LoRA-only, and the difference (2.8\\,pp, ${<}$1.3$\\sigma$) remains non-significant. The per-task CAR ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all seeds and conditions, reinforcing the demonstration-driven avoidance hypothesis.\n\nTable~\\ref{tab:eval_seed_car_detail} provides per-task CAR for the five-seed LoRA evaluation, the most complete eval-seed battery.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for LoRA s0 across five evaluation seeds. The per-task fingerprint (CP highest, BBQ lowest) is invariant across all seeds.}\n\\label{tab:eval_seed_car_detail}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nEval seed & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\n0   & 46 & 70 & 74 & 22 & 53.0 \\\\\n7   & 68 & 74 & 66 & 20 & 57.0 \\\\\n42  & 60 & 70 & 68 & 28 & 56.5 \\\\\n99  & 58 & 76 & 66 & 30 & 57.5 \\\\\n123 & 52 & 74 & 66 & 20 & 53.0 \\\\\n\\midrule\nMean$\\pm$Std & 56.8$\\pm$8.3 & 72.8$\\pm$2.7 & 68.0$\\pm$3.5 & 24.0$\\pm$4.7 & 55.4$\\pm$2.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n\n\n\\section{TSR Collapse Mechanism Analysis}\n\\label{sec:appendix_tsr_collapse}\n\nFine-tuning Pi0.5 with LoRA alone (no SDF supervision) reduces TSR from 71.5\\% to 49.7\\,$\\pm$\\,3.2\\%, a drop of 21.8\\,pp (Table~\\ref{tab:multiseed_full}). Adding SDF supervision does not exacerbate this decline: TSR under $\\lambda = 0.005$ is 54.0\\,$\\pm$\\,3.0\\% ($-$17.5\\,pp), under $\\lambda = 0.01$ is 53.8\\,$\\pm$\\,1.5\\% ($-$17.7\\,pp), and under $\\lambda = 0.1$ is 50.2\\,$\\pm$\\,3.9\\% ($-$21.3\\,pp). All SDF conditions are comparable to the LoRA-only baseline, and the largest SDF drop ($\\lambda = 0.1$, $-$21.3\\,pp) matches the LoRA-only drop ($-$21.8\\,pp) to within 0.5\\,pp. This confirms that SDF auxiliary loss is not the cause of TSR degradation.\n\nThe mechanism is catastrophic forgetting of task semantics induced by LoRA fine-tuning on a narrow 4-task subset of the pre-training distribution. Qualitative inspection reveals that fine-tuned models retain full motor capability: 0\\% action-collapse rate, end-effector displacement $>$\\,0.37\\,m, and active obstacle interaction (mean obstacle displacement ${\\sim}$0.05\\,m), but lose goal-directed grasping and placing behavior. The dominant failure mode shifts from collision (baseline safe failure rate 0.5\\%) to task incompletion without collision (${\\sim}$50\\% of episodes), representing a 100$\\times$ increase in safe failures. The robot moves purposefully through the workspace but fails to acquire or deliver the target object, consistent with retained low-level motor skills and degraded high-level task understanding.\n",
      "numLines": 375,
      "startLine": 1,
      "totalLines": 375
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the files. Let me analyze them systematically across all the requested dimensions and produce the checklist. Let me go through each dimension carefully.

### 1. LaTeX 排版

**Orphan/Widow lines**: Can't fully detect without compiling, but I can flag potential issues based on short paragraphs and section transitions.

**Table alignment**: Let me check all tables:
- Table 1 (tab:configurations): `{llr}` - text left, number right ✓
- Table 2 (tab:fake_safety): `{l@{\extracolsep{\fill}}ccccc}` - uses center alignment for numbers, not right. Mixed.


- Tables 3-6 all use center alignment for numeric columns rather than right-aligned, which is technically non-standard but consistent throughout the document and common in ML papers.

**Math spacing**: I need to examine the mathematical notation and spacing conventions next. The placement options for figures and tables are mostly `[t]` or `[h]`, though the appendix tables use `[h]` which might cause positioning problems. I don't see any footnotes in the paper. Now looking at the figure quality—I'm checking the captions across the referenced figures and noticing they all end with periods, though the subtitle formatting varies: some use bold labels like `(a)`, `(b)`, `(c)`, while others use descriptive text like `(Left)` and `(Right)`.

For the writing quality, the abstract is already fairly dense at around 100 words and could be tightened. The voice is mostly active with phrases like "We introduce" and "We show" appearing throughout, though I'm noticing some repetition in these sentence patterns that might be worth addressing. I should also verify that all abbreviations are properly defined on first use. Looking more carefully at where EE gets introduced—it appears in the figure caption first at line 6 of introduction.tex, then used in the body text at line 18. The abstract mentions "end-effector-only" but doesn't explicitly abbreviate it as EE, so the figure caption is technically the first formal definition of the abbreviation.

For TSR, that's clearly defined in the intro. But SSR is problematic—it's used in claim3.tex with the formula "SSR = TSR ∩ CAR" but never actually expanded to what SSR stands for, which needs to be fixed. And I'm checking whether MDE gets properly defined before it's used in the same section.

Looking at the section flow, the transitions feel natural from intro through related work into the methodology, and then each claim builds on the metrics established earlier. Now I need to verify the reference formatting—there's inconsistency in how conference names are abbreviated versus spelled out. I'm verifying the formatting consistency across the bibliography—the conference names follow the "Full Name (Abbreviation)" pattern, years are all four digits, and arXiv entries use the standard preprint format with the correct field structure. The entry types are appropriately split between articles for preprints and inproceedings for published conference papers, which looks right. - has volume, number, pages. Good.
  - `jacquet2025neuralnmpc` - journal article but missing volume/pages. Could be in press.
  - Most conference papers don't have pages - this is common and acceptable.

- Duplicate citations: Let me check... No obvious duplicates.

- `li2024langguided` - listed as ICRA 2025 with `year={2025}` and `@inproceedings`. That's fine for a 2025 publication.

The cite key `zhi2021diffco` has a year mismatch with `year={2022}`, but that's acceptable in BibTeX since the key is arbitrary and the paper may have been submitted in 2021 but published in 2022.

Now checking for unreferenced labels - I need to see if labels like `\label{sec:intro}` and `\label{fig:overview}` are actually cited in the text with `\ref` commands.

Looking through the files, I can see explicit references to `\ref{fig:teaser}`, `\ref{fig:scatter_and_oracle}`, `\ref{fig:displacement}`, and `\ref{fig:lambda_and_fingerprint}`, but `\ref{fig:overview}` never appears - the overview figure is just placed without being referenced in the text. Similarly, `\label{sec:anticorrelation}` doesn't seem to have a corresponding `\ref` anywhere.

Checking further, I notice `\label{sec:tsr_collapse}` and `\label{sec:lambda_high}` in claim3.tex also appear unreferenced. In the appendix, there's a double label situation where `\label{sec:appendix_pertask}\label{sec:appendix_pertask_oracle}` appears on the same line - the second one gets used in claim2.tex but the first one looks orphaned. I'm not finding any `\url` commands either.

Looking at formatting consistency, most tables have `\vspace{2pt}` after captions, though there's slight variation in font sizing between main text tables using `\small` and appendix tables mixing `\small` with `\footnotesize`. The BibTeX entries follow standard convention with "others" in author lists, and the paper uses "100+" notation for large numbers rather than alternative phrasing.

Checking other stylistic elements, percent signs are consistently formatted with `\%`, and dashes follow a pattern where hyphens appear in compound terms like "EE-only" while en-dashes mark ranges like "82--83\%". The $p$ value formatting is mostly consistent across the document, though there's minor variation in how inequality symbols are presented.

I'm noticing a terminology inconsistency between the abstract and introduction—one refers to "Collision Avoidance Rates" (plural) while the other uses "Collision Avoidance Rate" (singular). The abstract's claim about "over 99\%" for Pi0-family models aligns with the actual data points shown, so that's accurate. The "n.s." abbreviation appears in figure captions and is standard statistical notation, so it doesn't need expansion.

Looking at the avoidance source table, I'm seeing inconsistent decimal place formatting in the CAR values—some have two decimal places while others have one, which appears to stem from how the averages were calculated across the three runs. I'm noticing the standard deviation values are consistently formatted with 2 decimal places, but the CAR column is mixing 1 and 2 decimal places—54.5 should be 54.50 to match. I also see the TSR column maintains 1 decimal place throughout, so I need to pick one format and apply it uniformly across the table. Additionally, there's an inconsistency in the LaTeX table environments: Table 2 uses `tabular*` while the others use `tabular`, which I should standardize.

Looking at the discussion, I notice SSR is defined as the intersection of TSR and CAR, but the acronym itself is never expanded—it's presumably "Safe Success Rate" based on the table caption, but that should be spelled out explicitly. I'm also going through the label and reference consistency to make sure all cross-references are properly defined and used throughout the document.

Now I'm compiling the complete list of labels across all sections to verify which ones are actually referenced in the text and which might be orphaned. Now I'm continuing through the remaining appendix sections and checking which labels are actually referenced in the document. I can see more sections covering oracle details, spatial bowl analysis, evaluation seed robustness, training hyperparameters, and TSR collapse behavior. Looking at the references scattered throughout the intro and methods, I'm tracking which of these appendix labels are actually cited versus which ones might be orphaned. I'm continuing to scan through the document for unreferenced labels. Looking at the remaining equations and sections, I notice that `\ref{eq:total_loss}` doesn't appear to be cited anywhere either, and I should finish checking the equation references to get a complete picture of what's missing. I'm continuing through the document to identify all the missing cross-references—there are quite a few sections and tables that are defined but never actually cited anywhere in the paper, like the per-task analysis sections, the stepwise appendix, and various threshold sensitivity tables. Looking more carefully at the cross-references throughout the document, I'm seeing a pattern where the intro, methods, and claims sections do reference various appendices and tables consistently using the `\ref{}` syntax. Some appendix sections like the stepwise lambda and spatial bowl don't have explicit references from the main text, which is typical for appendix-only content, but I should verify whether the key figures and equations in the main narrative are actually being cited.

Scanning through the rest of the document, there's definitely an inconsistency in how I'm formatting section references—sometimes using `Section~\ref{}`, sometimes `\S\ref{}`, and sometimes `Appendix~\ref{}`. The conclusion and discussion sections are mixing these styles, which needs to be standardized across the entire document.

I'm also noticing that the non-breaking space usage is inconsistent. When using `\S\ref`, there's no tilde before the reference in some places, but `\S~\ref` would actually be more proper formatting. And there's a bigger issue: the overview figure at the top of the introduction is never actually referenced in the text, which is a significant oversight for such a prominent figure. I'm noticing the paper mixes `\cite` and `\citep` commands inconsistently—related_work uses `\citep` for SafeVLA and VLSA while everything else uses `\cite`, which could cause formatting issues depending on whether the corl_2026 style uses natbib. I found a couple more citation instances to track, and I'm noticing an inconsistency — there are two uses of `\citep` in the SDF integration pathways section while everything else uses `\cite`. I've checked for `\citet` but didn't find any, so it's just these two citation commands in use. One more thing to verify is whether the `\keywords` command at line 28 is properly defined by the CoRL 2026 package, since it appears right after the abstract input. Let me compile a full checklist of everything I've found.

Now I'm going through the references to count them and check for completeness. There are 25 entries total, and while some conference papers are missing page numbers (which is standard), I'm noticing a few entries like `jacquet2025neuralnmpc` that lack volume and number fields. Most of the references look complete, though I'm seeing some inconsistency in the BibTeX key naming convention — most follow the `authorYYYYkeyword` pattern, but a couple like `cofreeevla2026` and `depthvla2025` skip the author prefix entirely.

The key naming inconsistencies don't really matter since BibTeX keys aren't visible to readers anyway. I'm also double-checking the model size claims across different sections — the paper mentions Pi0 at ~2.5B parameters and Pi0.5 at ~3.5B parameters, and these align consistently between the method section and the hyperparameters table, so there's no actual contradiction there.

I think I've got a solid grasp of the reference quality and internal consistency now, so I'm ready to put together my analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "e930d434-6e99-43f5-adff-6979c589c2f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ihddYqYuR1Xmevhouqd2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4220,
      "cache_creation_input_tokens": 34215,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34215
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

_source line 28_

Now let me search for cross-reference consistency issues more precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "1b6a9b1d-4f3f-4c0f-8b33-e932d359f5e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ihddYqYuR1Xmevhouqd2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4220,
      "cache_creation_input_tokens": 34215,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34215
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

<details open><summary>🔧 Tool call — Grep · `toolu_01BqmZgHgEMd4KKd2BsCDMut`</summary>

```json
{
  "pattern": "\\\\ref\\{fig:overview\\}",
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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "937718a3-a5aa-4fea-a026-76d57c039639",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ihddYqYuR1Xmevhouqd2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4220,
      "cache_creation_input_tokens": 34215,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34215
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

_source line 30 · 2026-05-29T17:45:01.958Z_

<details><summary>↩ Tool result · `toolu_01BqmZgHgEMd4KKd2BsCDMut`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "1293b808-5663-4bd9-9fa5-0a651e2af194",
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

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01NFhrzeqXUSgd7XCWrdp9Ls`</summary>

```json
{
  "pattern": "\\\\citep",
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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "1d7785e1-e5fd-4bd6-bba1-8f7e3430ecb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ihddYqYuR1Xmevhouqd2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4220,
      "cache_creation_input_tokens": 34215,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34215
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

_source line 32 · 2026-05-29T17:45:02.256Z_

<details><summary>↩ Tool result · `toolu_01NFhrzeqXUSgd7XCWrdp9Ls`</summary>

```text
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/appendix.tex:323:We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "bf955c96-0e2f-4f17-ba02-0ca181cde698",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/appendix.tex:323:We use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_0178G17zHhQxK6fHjKU7k24q`</summary>

```json
{
  "pattern": "\\\\(section|Section|\\\\S).*\\\\ref",
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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "9ca62dd2-1e1a-443b-82b4-510bfcebfda0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ihddYqYuR1Xmevhouqd2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4220,
      "cache_creation_input_tokens": 34215,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34215
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

_source line 34 · 2026-05-29T17:45:03.784Z_

<details><summary>↩ Tool result · `toolu_0178G17zHhQxK6fHjKU7k24q`</summary>

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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "764ab99e-6f27-4bc0-937b-2ad1b7c38a42",
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

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_012TdrhUDKjZnHJCJ4i1u2mr`</summary>

```json
{
  "pattern": "\\\\eqref|\\\\ref\\{eq:",
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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "55ad0a8a-e95c-443b-8bdb-d321c4772b08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ihddYqYuR1Xmevhouqd2m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4220,
      "cache_creation_input_tokens": 34215,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 34215
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

_source line 36 · 2026-05-29T17:45:04.317Z_

<details><summary>↩ Tool result · `toolu_012TdrhUDKjZnHJCJ4i1u2mr`</summary>

```text
docs/paper/archive/analysis_claim1.tex:5:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:29:These observations motivate the displacement-filtered CAR (CAR$_\text{f}$) defined in Eq.~\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\text{f}$ serves as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "24ac2217-1fa2-4795-a9f3-aecb2bd3653d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/archive/analysis_claim1.tex:5:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:29:These observations motivate the displacement-filtered CAR (CAR$_\\text{f}$) defined in Eq.~\\ref{eq:car_f}, which excludes episodes with sub-threshold end-effector displacement from both numerator and denominator. CAR$_\\text{f}$ serves as a general-purpose diagnostic for the VLA safety evaluation community, applicable to any model and benchmark where per-episode end-effector trajectories are recorded.",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Grep · `toolu_01RnCY4t1ZSgBd3gFc2oLQXi`</summary>

```json
{
  "pattern": "\\\\S\\\\ref|Section~\\\\ref",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "4619a095-9859-4479-9b09-8f791ab2e379",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHmvAz1DLwH2RFgniZdpo3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13397,
      "cache_read_input_tokens": 45666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13397
      },
      "output_tokens": 36,
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

_source line 38 · 2026-05-29T17:45:07.672Z_

<details><summary>↩ Tool result · `toolu_01RnCY4t1ZSgBd3gFc2oLQXi`</summary>

```text
docs/paper/related_work.tex:15:[Omitted long matching line]
docs/paper/discussion.tex:3:[Omitted long matching line]
docs/paper/discussion.tex:7:[Omitted long matching line]
docs/paper/experimental_framework.tex:41:To test the theoretical upper bound of end-effector-only SDF refinement (analyzed in Section~\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm itself.
docs/paper/method.tex:46:In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\,=\,0\%; Table~\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\ref{sec:appendix_oracle}).\label{sec:oracle_setup}
docs/paper/archive/analysis_claim2.tex:3:[Omitted long matching line]
docs/paper/archive/analysis_claim2.tex:37:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:35:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:7:\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\max} < \tau_d$ (action collapse; Section~\ref{sec:metrics}). Pi0.5+A1 produces 0\% frozen episodes at 10K steps, so CAR$_\text{f}$ equals raw CAR.}
docs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]
docs/paper/archive/analysis_claim4.tex:48:Training-time SDF auxiliary loss yields substantial collision avoidance improvement on Pi0.5, confirming that geometric supervision can address the action-collapse-contaminated safety identified in Sections~\ref{sec:fake_safety}--\ref{sec:tsr_car}. The path to genuine collision avoidance in VLAs runs through the training objective, not through inference-time refinement of a representation that lacks full-body geometric coverage (Section~\ref{sec:ee_only}).
docs/paper/claim2.tex:3:Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\S\ref{sec:oracle_setup}). Table~\ref{tab:oracle} and Figure~\ref{fig:scatter_and_oracle} (right) show that all three oracle variants achieve \emph{lower} CAR than unrefined baselines: the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%). Refinement with perfect distance information produces more collisions, not fewer.
docs/paper/_archive/experiments.tex:20:\paragraph{Training details.} All variants train for 30K steps with batch size 32 on the same dataset. Phase 1 (steps 0--5K) trains only the SDF decoder and EE extractor on detached features; Phase 2 (steps 5K--30K) unfreezes LoRA parameters (${\sim}$33.5M) with linear gradient warmup over 100 steps. The $\pi_0$-LoRA baseline skips Phase 1 and trains for 30K steps with $\mathcal{L}_\mathrm{action}$ only. Hyperparameters follow Section~\ref{sec:training}.
docs/paper/_archive/experiments.tex:66:\paragraph{Optional inference-time correction.} Section~\ref{sec:inference} describes an optional SDF gradient correction at inference. We evaluate its effect on ColliForce by enabling the correction during evaluation. \textbf{[TODO: Report CAR/TSR delta. Expected: minimal change, confirming that ColliForce has already internalized collision avoidance.]}
docs/paper/_archive/method.tex:3:[Omitted long matching line]
docs/paper/_archive/method.tex:34:where $\sigma(\cdot) = \mathrm{Softplus}_{\beta=5}(\cdot)$. The total parameter count is ${\sim}$395K. Spatial gradients $\nabla_{\mathbf{x}} \hat{\Phi}(\mathbf{x})$ are computed via \texttt{torch.autograd.grad} with graph creation enabled during training, which is required for Eikonal regularization and the gradient-guided refinement in Section~\ref{sec:gradient_refinement}.
docs/paper/appendix.tex:96:Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
docs/paper/appendix.tex:121:[Omitted long matching line]
docs/paper/contingency_claim3.tex:19:[Omitted long matching line]
docs/paper/contingency_claim3.tex:28:[Omitted long matching line]
docs/paper/contingency_claim3.tex:37:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/introduction.tex:16:[Omitted long matching line]
docs/paper/introduction.tex:18:\textbf{EE-only SDF refinement is counterproductive under the tested conditions.} Three ground-truth oracle variants applied to action-collapsed baselines all achieve \emph{lower} CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\ref{sec:ee_only}).
docs/paper/introduction.tex:20:\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\sim}$26 points with zero action-collapsed episodes. SDF supervision shows no statistically significant additional benefit ($p \geq 0.155$ for SDF loss weight $\lambda \in \{0.01, 0.1\}$; Section~\ref{sec:avoidance_source}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "75bf66e0-2b42-4807-8424-e65ba2fe18ed",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:15:[Omitted long matching line]\ndocs/paper/discussion.tex:3:[Omitted long matching line]\ndocs/paper/discussion.tex:7:[Omitted long matching line]\ndocs/paper/experimental_framework.tex:41:To test the theoretical upper bound of end-effector-only SDF refinement (analyzed in Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm itself.\ndocs/paper/method.tex:46:In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\\,=\\,0\\%; Table~\\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\\ref{sec:appendix_oracle}).\\label{sec:oracle_setup}\ndocs/paper/archive/analysis_claim2.tex:3:[Omitted long matching line]\ndocs/paper/archive/analysis_claim2.tex:37:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:35:[Omitted long matching line]\ndocs/paper/archive/analysis_claim4.tex:7:\\caption{Results for Pi0.5 with training-time SDF auxiliary loss on SafeLIBERO (200 episodes per configuration). Frozen rate: fraction of episodes with $d_{\\max} < \\tau_d$ (action collapse; Section~\\ref{sec:metrics}). Pi0.5+A1 produces 0\\% frozen episodes at 10K steps, so CAR$_\\text{f}$ equals raw CAR.}\ndocs/paper/archive/analysis_claim4.tex:29:[Omitted long matching line]\ndocs/paper/archive/analysis_claim4.tex:48:Training-time SDF auxiliary loss yields substantial collision avoidance improvement on Pi0.5, confirming that geometric supervision can address the action-collapse-contaminated safety identified in Sections~\\ref{sec:fake_safety}--\\ref{sec:tsr_car}. The path to genuine collision avoidance in VLAs runs through the training objective, not through inference-time refinement of a representation that lacks full-body geometric coverage (Section~\\ref{sec:ee_only}).\ndocs/paper/claim2.tex:3:Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\\S\\ref{sec:oracle_setup}). Table~\\ref{tab:oracle} and Figure~\\ref{fig:scatter_and_oracle} (right) show that all three oracle variants achieve \\emph{lower} CAR than unrefined baselines: the best oracle (76.9\\%) falls 5.1 points below LoRA (82.0\\%). Refinement with perfect distance information produces more collisions, not fewer.\ndocs/paper/_archive/experiments.tex:20:\\paragraph{Training details.} All variants train for 30K steps with batch size 32 on the same dataset. Phase 1 (steps 0--5K) trains only the SDF decoder and EE extractor on detached features; Phase 2 (steps 5K--30K) unfreezes LoRA parameters (${\\sim}$33.5M) with linear gradient warmup over 100 steps. The $\\pi_0$-LoRA baseline skips Phase 1 and trains for 30K steps with $\\mathcal{L}_\\mathrm{action}$ only. Hyperparameters follow Section~\\ref{sec:training}.\ndocs/paper/_archive/experiments.tex:66:\\paragraph{Optional inference-time correction.} Section~\\ref{sec:inference} describes an optional SDF gradient correction at inference. We evaluate its effect on ColliForce by enabling the correction during evaluation. \\textbf{[TODO: Report CAR/TSR delta. Expected: minimal change, confirming that ColliForce has already internalized collision avoidance.]}\ndocs/paper/_archive/method.tex:3:[Omitted long matching line]\ndocs/paper/_archive/method.tex:34:where $\\sigma(\\cdot) = \\mathrm{Softplus}_{\\beta=5}(\\cdot)$. The total parameter count is ${\\sim}$395K. Spatial gradients $\\nabla_{\\mathbf{x}} \\hat{\\Phi}(\\mathbf{x})$ are computed via \\texttt{torch.autograd.grad} with graph creation enabled during training, which is required for Eikonal regularization and the gradient-guided refinement in Section~\\ref{sec:gradient_refinement}.\ndocs/paper/appendix.tex:96:Table~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\ndocs/paper/appendix.tex:121:[Omitted long matching line]\ndocs/paper/contingency_claim3.tex:19:[Omitted long matching line]\ndocs/paper/contingency_claim3.tex:28:[Omitted long matching line]\ndocs/paper/contingency_claim3.tex:37:[Omitted long matching line]\ndocs/paper/introduction.tex:12:[Omitted long matching line]\ndocs/paper/introduction.tex:16:[Omitted long matching line]\ndocs/paper/introduction.tex:18:\\textbf{EE-only SDF refinement is counterproductive under the tested conditions.} Three ground-truth oracle variants applied to action-collapsed baselines all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\ndocs/paper/introduction.tex:20:\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero action-collapsed episodes. SDF supervision shows no statistically significant additional benefit ($p \\geq 0.155$ for SDF loss weight $\\lambda \\in \\{0.01, 0.1\\}$; Section~\\ref{sec:avoidance_source}).",
    "numLines": 25
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Grep · `toolu_01RrwGCnLbE3espkQY38co6n`</summary>

```json
{
  "pattern": "SSR",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "049fdb0a-342c-4a2a-ab10-1e9f858bf2c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHmvAz1DLwH2RFgniZdpo3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13397,
      "cache_read_input_tokens": 45666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13397
      },
      "output_tokens": 36,
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

_source line 40 · 2026-05-29T17:45:09.084Z_

<details><summary>↩ Tool result · `toolu_01RrwGCnLbE3espkQY38co6n`</summary>

```text
docs/paper/claim3.tex:36:Fine-tuning degrades TSR by ${\sim}$17--22\,pp (71.5\% $\to$ 49.7--54.0\%) due to distributional shift, not learned paralysis (all models retain $>$\,0.37\,m displacement). The SSR/TSR ratio (SSR\,=\,TSR\,$\cap$\,CAR) increases from 0.39 to 0.51--0.60 (Table~\ref{tab:ssr}): among completing episodes, more avoid collisions after fine-tuning.
docs/paper/claim3.tex:40:\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}
docs/paper/claim3.tex:46:Condition & TSR (\%) & CAR (\%) & SSR (\%) & SSR/TSR \\
docs/paper/experimental_framework.tex:25:\paragraph{Auxiliary metrics.} We additionally report the \emph{Action-Collapse Rate}, the fraction of episodes with $d_{\max} < \tau_d$, which quantifies the severity of action collapse for each method. The \emph{Simultaneous Success Rate} (SSR $= $ TSR $\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.
docs/paper/archive/analysis_claim4.tex:13:Method & TSR (\%) & CAR (\%) & CAR$_\text{f}$ (\%) & SSR (\%) & Frozen (\%) \\
docs/paper/appendix.tex:150:See Table~\ref{tab:ssr} (main text) for SSR and SSR/TSR ratio across conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "57be4040-7c14-436c-8c84-9bba23b3a6c9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/claim3.tex:36:Fine-tuning degrades TSR by ${\\sim}$17--22\\,pp (71.5\\% $\\to$ 49.7--54.0\\%) due to distributional shift, not learned paralysis (all models retain $>$\\,0.37\\,m displacement). The SSR/TSR ratio (SSR\\,=\\,TSR\\,$\\cap$\\,CAR) increases from 0.39 to 0.51--0.60 (Table~\\ref{tab:ssr}): among completing episodes, more avoid collisions after fine-tuning.\ndocs/paper/claim3.tex:40:\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\ndocs/paper/claim3.tex:46:Condition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\ndocs/paper/experimental_framework.tex:25:\\paragraph{Auxiliary metrics.} We additionally report the \\emph{Action-Collapse Rate}, the fraction of episodes with $d_{\\max} < \\tau_d$, which quantifies the severity of action collapse for each method. The \\emph{Simultaneous Success Rate} (SSR $= $ TSR $\\cap$ CAR) measures the fraction of episodes that achieve both task completion and collision avoidance.\ndocs/paper/archive/analysis_claim4.tex:13:Method & TSR (\\%) & CAR (\\%) & CAR$_\\text{f}$ (\\%) & SSR (\\%) & Frozen (\\%) \\\\\ndocs/paper/appendix.tex:150:See Table~\\ref{tab:ssr} (main text) for SSR and SSR/TSR ratio across conditions.",
    "numLines": 6
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Grep · `toolu_017B2MzMJwBcVte3FwLvAYua`</summary>

```json
{
  "pattern": "MDE",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "c899a3dc-c95c-4164-8c4e-6cbd28b1dd97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHmvAz1DLwH2RFgniZdpo3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13397,
      "cache_read_input_tokens": 45666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13397
      },
      "output_tokens": 36,
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

_source line 42 · 2026-05-29T17:45:09.833Z_

<details><summary>↩ Tool result · `toolu_017B2MzMJwBcVte3FwLvAYua`</summary>

```text
docs/paper/claim3.tex:59:[Omitted long matching line]
docs/paper/discussion.tex:7:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "200abc0e-4af6-4a69-9fa2-4a80aad6343d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/claim3.tex:59:[Omitted long matching line]\ndocs/paper/discussion.tex:7:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the info I need. Let me also check one more thing - the CAR abbreviation in abstract vs intro:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "10ceef70-0234-4229-bc23-d54162033b14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHHqNaGzi33W6isRxsdXRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2603,
      "cache_read_input_tokens": 59063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2603
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

_source line 44_

Now let me check a few more specific issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "b7115707-536f-40a4-9537-c01d68f48bec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHHqNaGzi33W6isRxsdXRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2603,
      "cache_read_input_tokens": 59063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2603
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

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_01DYvGZvJeM3Smm34oPgP4nP`</summary>

```json
{
  "pattern": "Collision Avoidance Rate",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "59296152-a9a5-4c7b-934d-51826688c7b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHHqNaGzi33W6isRxsdXRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2603,
      "cache_read_input_tokens": 59063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2603
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

_source line 46 · 2026-05-29T17:45:14.095Z_

<details><summary>↩ Tool result · `toolu_01DYvGZvJeM3Smm34oPgP4nP`</summary>

```text
docs/paper/experimental_framework.tex:3:This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (dfCAR), which separates genuine avoidance from action collapse.
docs/paper/experimental_framework.tex:15:\paragraph{Standard metrics.} We report two conventional metrics. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.
docs/paper/method.tex:5:[Omitted long matching line]
docs/paper/archive/analysis_claim1.tex:3:[Omitted long matching line]
docs/paper/_archive/experiments.tex:3:We evaluate ColliForce-VLA on the SafeLIBERO benchmark to answer three questions: (1) Does integrating workspace SDF into the VLA forward pass improve collision avoidance? (2) Does the gradient-guided refinement loss contribute beyond auxiliary SDF supervision alone? (3) What is the trade-off between Collision Avoidance Rate (CAR) and Task Success Rate (TSR)?
docs/paper/_archive/experiments.tex:16:\paragraph{Metrics.} We report two metrics: Task Success Rate (TSR, $\uparrow$), the fraction of episodes where the manipulation task is completed, and Collision Avoidance Rate (CAR, $\uparrow$), the fraction of episodes where the end-effector does not contact any non-target obstacle. A collision is registered when the distance between the end-effector and any obstacle mesh falls below \textbf{[TODO: collision\_threshold from code]} meters.
docs/paper/_archive/experiments.tex:28:\caption{Main results on SafeLIBERO collision scenarios. CAR: Collision Avoidance Rate ($\uparrow$), TSR: Task Success Rate ($\uparrow$). \textbf{Bold}: best CAR per scene.}
docs/paper/_archive/conclusion_DEPRECATED.tex:3:[Omitted long matching line]
docs/paper/abstract.tex:2:[Omitted long matching line]
docs/paper/introduction.tex:10:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "73be6ac9-e61d-482a-a342-dab9efc879cf",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/experimental_framework.tex:3:This section defines the evaluation platform, metrics, and model configurations that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. Our primary methodological contribution is the displacement-filtered Collision Avoidance Rate (dfCAR), which separates genuine avoidance from action collapse.\ndocs/paper/experimental_framework.tex:15:\\paragraph{Standard metrics.} We report two conventional metrics. The \\emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion. The \\emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object.\ndocs/paper/method.tex:5:[Omitted long matching line]\ndocs/paper/archive/analysis_claim1.tex:3:[Omitted long matching line]\ndocs/paper/_archive/experiments.tex:3:We evaluate ColliForce-VLA on the SafeLIBERO benchmark to answer three questions: (1) Does integrating workspace SDF into the VLA forward pass improve collision avoidance? (2) Does the gradient-guided refinement loss contribute beyond auxiliary SDF supervision alone? (3) What is the trade-off between Collision Avoidance Rate (CAR) and Task Success Rate (TSR)?\ndocs/paper/_archive/experiments.tex:16:\\paragraph{Metrics.} We report two metrics: Task Success Rate (TSR, $\\uparrow$), the fraction of episodes where the manipulation task is completed, and Collision Avoidance Rate (CAR, $\\uparrow$), the fraction of episodes where the end-effector does not contact any non-target obstacle. A collision is registered when the distance between the end-effector and any obstacle mesh falls below \\textbf{[TODO: collision\\_threshold from code]} meters.\ndocs/paper/_archive/experiments.tex:28:\\caption{Main results on SafeLIBERO collision scenarios. CAR: Collision Avoidance Rate ($\\uparrow$), TSR: Task Success Rate ($\\uparrow$). \\textbf{Bold}: best CAR per scene.}\ndocs/paper/_archive/conclusion_DEPRECATED.tex:3:[Omitted long matching line]\ndocs/paper/abstract.tex:2:[Omitted long matching line]\ndocs/paper/introduction.tex:10:[Omitted long matching line]",
    "numLines": 10
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_01JG1jQaeEVoMm5eUL1CA7zC`</summary>

```json
{
  "pattern": "\\\\label\\{",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "glob": "{main,abstract,introduction,related_work,method,claim1,claim2,claim3,discussion,appendix}.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "0df17607-255e-4c8e-978c-0bf5ae21e8ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHHqNaGzi33W6isRxsdXRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2603,
      "cache_read_input_tokens": 59063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2603
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

_source line 48 · 2026-05-29T17:45:15.634Z_

<details><summary>↩ Tool result · `toolu_01JG1jQaeEVoMm5eUL1CA7zC`</summary>

```text
docs/paper/related_work.tex:1:\section{Related Work}\label{sec:related}
docs/paper/claim3.tex:1:\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
docs/paper/claim3.tex:8:\label{tab:avoidance_source}
docs/paper/claim3.tex:32:\label{fig:lambda_and_fingerprint}
docs/paper/claim3.tex:35:\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
docs/paper/claim3.tex:41:\label{tab:ssr}
docs/paper/claim3.tex:58:\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
docs/paper/claim3.tex:67:\label{tab:spatial_bowl}
docs/paper/discussion.tex:1:\section{Conclusion}\label{sec:conclusion}
docs/paper/discussion.tex:5:\section{Limitations}\label{sec:limitations}
docs/paper/method.tex:1:\section{Experimental Setup and Metrics}\label{sec:method}
docs/paper/method.tex:3:\subsection{Benchmark and Models}\label{sec:benchmark}
docs/paper/method.tex:10:\label{tab:configurations}
docs/paper/method.tex:28:\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
docs/paper/method.tex:31:\begin{equation}\label{eq:car_f}
docs/paper/method.tex:36:\subsection{SDF Auxiliary Training and Oracle Refinement}\label{sec:sdf_aux}
docs/paper/method.tex:39:\begin{equation}\label{eq:total_loss}
docs/paper/method.tex:46:In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\,=\,0\%; Table~\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\ref{sec:appendix_oracle}).\label{sec:oracle_setup}
docs/paper/claim2.tex:1:\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
docs/paper/claim2.tex:8:\label{tab:oracle}
docs/paper/_archive/method.tex:1:\section{Method}\label{sec:method}
docs/paper/_archive/method.tex:5:\subsection{Problem Formulation}\label{sec:problem}
docs/paper/_archive/method.tex:13:\subsection{Differentiable SDF Integration}\label{sec:sdf_integration}
docs/paper/_archive/method.tex:18:\begin{equation}\label{eq:pooling}
docs/paper/_archive/method.tex:24:\begin{equation}\label{eq:sdf_decoder}
docs/paper/_archive/method.tex:29:\mathbf{h}_0 &= \sigma(\mathbf{W}_0 [\bar{\mathbf{z}}; \mathbf{x}] + \mathbf{b}_0), \quad \mathbf{W}_0 \in \mathbb{R}^{256 \times 1027} \label{eq:sdf_layer0} \\
docs/paper/_archive/method.tex:32:\hat{\Phi}(\mathbf{x}) &= \mathbf{W}_3 \mathbf{h}_2 + \mathbf{b}_3, \quad \mathbf{W}_3 \in \mathbb{R}^{1 \times 256} \label{eq:sdf_output}
docs/paper/_archive/method.tex:37:\begin{equation}\label{eq:ee_extractor}
docs/paper/_archive/method.tex:43:\begin{equation}\label{eq:loss_sdf}
docs/paper/_archive/method.tex:47:\begin{equation}\label{eq:loss_ee}
docs/paper/_archive/method.tex:52:\subsection{SDF Gradient-Guided Action Refinement}\label{sec:gradient_refinement}
docs/paper/_archive/method.tex:64:\begin{equation}\label{eq:collision_set}
docs/paper/_archive/method.tex:69:\begin{equation}\label{eq:feature_grad}
docs/paper/_archive/method.tex:75:\begin{equation}\label{eq:gradient_ascent}
docs/paper/_archive/method.tex:81:\begin{equation}\label{eq:projection}
docs/paper/_archive/method.tex:86:\begin{equation}\label{eq:loss_refine}
docs/paper/_archive/method.tex:91:\subsection{Training Protocol}\label{sec:training}
docs/paper/_archive/method.tex:105:\begin{equation}\label{eq:loss_aux}
docs/paper/_archive/method.tex:111:\begin{equation}\label{eq:loss_full}
docs/paper/_archive/method.tex:118:\subsection{Inference}\label{sec:inference}
docs/paper/_archive/method.tex:123:\begin{equation}\label{eq:inference_correction}
docs/paper/appendix.tex:2:\label{sec:appendix_multiseed}
docs/paper/appendix.tex:9:\label{tab:multiseed_full}
docs/paper/appendix.tex:40:\label{sec:appendix_displacement}
docs/paper/appendix.tex:45:\label{sec:appendix_threshold}
docs/paper/appendix.tex:52:\label{tab:threshold_sensitivity}
docs/paper/appendix.tex:72:\label{tab:dfcar_threshold}
docs/paper/appendix.tex:94:\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
docs/paper/appendix.tex:101:\label{tab:per_task_tsr}
docs/paper/appendix.tex:119:\section{Per-Task CAR Breakdown}\label{sec:appendix_pertask_car}
docs/paper/appendix.tex:126:\label{tab:per_task_car}
docs/paper/appendix.tex:148:\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
docs/paper/appendix.tex:153:\label{sec:appendix_pertask}
docs/paper/appendix.tex:154:\label{sec:appendix_pertask_oracle}
docs/paper/appendix.tex:163:\label{tab:oracle_pertask}
docs/paper/appendix.tex:186:\label{tab:oracle_pertask_pi05}
docs/paper/appendix.tex:203:\label{sec:appendix_null}
docs/paper/appendix.tex:215:\label{sec:appendix_stepwise}
docs/paper/appendix.tex:222:\label{tab:stepwise_lambda01}
docs/paper/appendix.tex:244:\label{sec:appendix_oracle}
docs/paper/appendix.tex:256:\label{sec:appendix_spatial_bowl}
docs/paper/appendix.tex:262:\label{sec:appendix_eval_seed}
docs/paper/appendix.tex:269:\label{tab:eval_seed_robustness}
docs/paper/appendix.tex:300:\label{tab:eval_seed_car_detail}
docs/paper/appendix.tex:320:\label{sec:appendix_training}
docs/paper/appendix.tex:336:\label{tab:hyperparams}
docs/paper/appendix.tex:370:\label{sec:appendix_tsr_collapse}
docs/paper/introduction.tex:1:\section{Introduction}\label{sec:intro}
docs/paper/introduction.tex:7:\label{fig:overview}
docs/paper/introduction.tex:28:\label{fig:teaser}
docs/paper/claim1.tex:1:\section{The Action-Collapsed Safety Problem}\label{sec:fake_safety}
docs/paper/claim1.tex:8:\label{tab:fake_safety}
docs/paper/claim1.tex:28:\label{fig:scatter_and_oracle}
docs/paper/claim1.tex:30:Figure~\ref{fig:scatter_and_oracle} (left) quantifies CAR inflation from action collapse.\label{sec:anticorrelation} Pi0-family models show 82--91\,pp gaps between reported CAR and dfCAR: virtually all apparent safety is illusory. Pi0.5 and fine-tuned variants show no inflation (dfCAR\,=\,CAR), confirming genuine avoidance. Under dfCAR, the apparent safety--capability tradeoff disappears: high raw CAR was an artifact of action-collapse contamination, not deliberate avoidance.
docs/paper/claim1.tex:38:\label{fig:displacement}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "fa1a28cd-4761-4aa2-be7d-b54784879140",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:1:\\section{Related Work}\\label{sec:related}\ndocs/paper/claim3.tex:1:\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\ndocs/paper/claim3.tex:8:\\label{tab:avoidance_source}\ndocs/paper/claim3.tex:32:\\label{fig:lambda_and_fingerprint}\ndocs/paper/claim3.tex:35:\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\ndocs/paper/claim3.tex:41:\\label{tab:ssr}\ndocs/paper/claim3.tex:58:\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\ndocs/paper/claim3.tex:67:\\label{tab:spatial_bowl}\ndocs/paper/discussion.tex:1:\\section{Conclusion}\\label{sec:conclusion}\ndocs/paper/discussion.tex:5:\\section{Limitations}\\label{sec:limitations}\ndocs/paper/method.tex:1:\\section{Experimental Setup and Metrics}\\label{sec:method}\ndocs/paper/method.tex:3:\\subsection{Benchmark and Models}\\label{sec:benchmark}\ndocs/paper/method.tex:10:\\label{tab:configurations}\ndocs/paper/method.tex:28:\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\ndocs/paper/method.tex:31:\\begin{equation}\\label{eq:car_f}\ndocs/paper/method.tex:36:\\subsection{SDF Auxiliary Training and Oracle Refinement}\\label{sec:sdf_aux}\ndocs/paper/method.tex:39:\\begin{equation}\\label{eq:total_loss}\ndocs/paper/method.tex:46:In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\\,=\\,0\\%; Table~\\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\\ref{sec:appendix_oracle}).\\label{sec:oracle_setup}\ndocs/paper/claim2.tex:1:\\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\\label{sec:ee_only}\ndocs/paper/claim2.tex:8:\\label{tab:oracle}\ndocs/paper/_archive/method.tex:1:\\section{Method}\\label{sec:method}\ndocs/paper/_archive/method.tex:5:\\subsection{Problem Formulation}\\label{sec:problem}\ndocs/paper/_archive/method.tex:13:\\subsection{Differentiable SDF Integration}\\label{sec:sdf_integration}\ndocs/paper/_archive/method.tex:18:\\begin{equation}\\label{eq:pooling}\ndocs/paper/_archive/method.tex:24:\\begin{equation}\\label{eq:sdf_decoder}\ndocs/paper/_archive/method.tex:29:\\mathbf{h}_0 &= \\sigma(\\mathbf{W}_0 [\\bar{\\mathbf{z}}; \\mathbf{x}] + \\mathbf{b}_0), \\quad \\mathbf{W}_0 \\in \\mathbb{R}^{256 \\times 1027} \\label{eq:sdf_layer0} \\\\\ndocs/paper/_archive/method.tex:32:\\hat{\\Phi}(\\mathbf{x}) &= \\mathbf{W}_3 \\mathbf{h}_2 + \\mathbf{b}_3, \\quad \\mathbf{W}_3 \\in \\mathbb{R}^{1 \\times 256} \\label{eq:sdf_output}\ndocs/paper/_archive/method.tex:37:\\begin{equation}\\label{eq:ee_extractor}\ndocs/paper/_archive/method.tex:43:\\begin{equation}\\label{eq:loss_sdf}\ndocs/paper/_archive/method.tex:47:\\begin{equation}\\label{eq:loss_ee}\ndocs/paper/_archive/method.tex:52:\\subsection{SDF Gradient-Guided Action Refinement}\\label{sec:gradient_refinement}\ndocs/paper/_archive/method.tex:64:\\begin{equation}\\label{eq:collision_set}\ndocs/paper/_archive/method.tex:69:\\begin{equation}\\label{eq:feature_grad}\ndocs/paper/_archive/method.tex:75:\\begin{equation}\\label{eq:gradient_ascent}\ndocs/paper/_archive/method.tex:81:\\begin{equation}\\label{eq:projection}\ndocs/paper/_archive/method.tex:86:\\begin{equation}\\label{eq:loss_refine}\ndocs/paper/_archive/method.tex:91:\\subsection{Training Protocol}\\label{sec:training}\ndocs/paper/_archive/method.tex:105:\\begin{equation}\\label{eq:loss_aux}\ndocs/paper/_archive/method.tex:111:\\begin{equation}\\label{eq:loss_full}\ndocs/paper/_archive/method.tex:118:\\subsection{Inference}\\label{sec:inference}\ndocs/paper/_archive/method.tex:123:\\begin{equation}\\label{eq:inference_correction}\ndocs/paper/appendix.tex:2:\\label{sec:appendix_multiseed}\ndocs/paper/appendix.tex:9:\\label{tab:multiseed_full}\ndocs/paper/appendix.tex:40:\\label{sec:appendix_displacement}\ndocs/paper/appendix.tex:45:\\label{sec:appendix_threshold}\ndocs/paper/appendix.tex:52:\\label{tab:threshold_sensitivity}\ndocs/paper/appendix.tex:72:\\label{tab:dfcar_threshold}\ndocs/paper/appendix.tex:94:\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\ndocs/paper/appendix.tex:101:\\label{tab:per_task_tsr}\ndocs/paper/appendix.tex:119:\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\ndocs/paper/appendix.tex:126:\\label{tab:per_task_car}\ndocs/paper/appendix.tex:148:\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\ndocs/paper/appendix.tex:153:\\label{sec:appendix_pertask}\ndocs/paper/appendix.tex:154:\\label{sec:appendix_pertask_oracle}\ndocs/paper/appendix.tex:163:\\label{tab:oracle_pertask}\ndocs/paper/appendix.tex:186:\\label{tab:oracle_pertask_pi05}\ndocs/paper/appendix.tex:203:\\label{sec:appendix_null}\ndocs/paper/appendix.tex:215:\\label{sec:appendix_stepwise}\ndocs/paper/appendix.tex:222:\\label{tab:stepwise_lambda01}\ndocs/paper/appendix.tex:244:\\label{sec:appendix_oracle}\ndocs/paper/appendix.tex:256:\\label{sec:appendix_spatial_bowl}\ndocs/paper/appendix.tex:262:\\label{sec:appendix_eval_seed}\ndocs/paper/appendix.tex:269:\\label{tab:eval_seed_robustness}\ndocs/paper/appendix.tex:300:\\label{tab:eval_seed_car_detail}\ndocs/paper/appendix.tex:320:\\label{sec:appendix_training}\ndocs/paper/appendix.tex:336:\\label{tab:hyperparams}\ndocs/paper/appendix.tex:370:\\label{sec:appendix_tsr_collapse}\ndocs/paper/introduction.tex:1:\\section{Introduction}\\label{sec:intro}\ndocs/paper/introduction.tex:7:\\label{fig:overview}\ndocs/paper/introduction.tex:28:\\label{fig:teaser}\ndocs/paper/claim1.tex:1:\\section{The Action-Collapsed Safety Problem}\\label{sec:fake_safety}\ndocs/paper/claim1.tex:8:\\label{tab:fake_safety}\ndocs/paper/claim1.tex:28:\\label{fig:scatter_and_oracle}\ndocs/paper/claim1.tex:30:Figure~\\ref{fig:scatter_and_oracle} (left) quantifies CAR inflation from action collapse.\\label{sec:anticorrelation} Pi0-family models show 82--91\\,pp gaps between reported CAR and dfCAR: virtually all apparent safety is illusory. Pi0.5 and fine-tuned variants show no inflation (dfCAR\\,=\\,CAR), confirming genuine avoidance. Under dfCAR, the apparent safety--capability tradeoff disappears: high raw CAR was an artifact of action-collapse contamination, not deliberate avoidance.\ndocs/paper/claim1.tex:38:\\label{fig:displacement}",
    "numLines": 75
  }
}
```

</details>

---

### Assistant

_source line 49_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data. Let me also check the abstract for "Collision Avoidance Rates" (plural) vs. "Collision Avoidance Rate" (singular).

From abstract.tex: "Collision Avoidance Rates (CAR)" - plural
From introduction.tex line 10: "Collision Avoidance Rate (CAR)" - singular
From method.tex line 5: mentions CAR

This is an inconsistency.

Now let me also check if the figures use bitmap vs vector. I can look at the graphicspath and file extensions.

The graphicspath is `../../artifacts/figures/`. All includes use names without extensions (e.g., `fig_overview_pb`, `fig1_teaser`), so LaTeX will search for .pdf, .png, etc. 

Without access to the actual files in that directory, I can't verify the exact format, so I'll move on to compiling the comprehensive checklist.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "54cf66d3-9e5c-492f-b2f2-4118fdd1b7b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hjQYt7e4bVAPBrCVBu6mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3321,
      "cache_read_input_tokens": 61666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3321
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

_source line 50_

Now let me check figure file formats to assess raster vs vector.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "66e2b2f6-aac1-4644-89df-f3dba8c658cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hjQYt7e4bVAPBrCVBu6mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3321,
      "cache_read_input_tokens": 61666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3321
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

_source line 51_

<details open><summary>🔧 Tool call — Glob · `toolu_01WGcqe17cB5SRVVB82T9heo`</summary>

```json
{
  "pattern": "**/artifacts/figures/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "74b032c5-0151-433c-910e-afe839b6ca12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hjQYt7e4bVAPBrCVBu6mw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3321,
      "cache_read_input_tokens": 61666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3321
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

_source line 52 · 2026-05-29T17:45:23.782Z_

<details><summary>↩ Tool result · `toolu_01WGcqe17cB5SRVVB82T9heo`</summary>

```text
artifacts/figures/plot_fig3.py
artifacts/figures/fig3_tsr_car_scatter.pdf
artifacts/figures/fig3_tsr_car_scatter.png
artifacts/figures/plot_threshold_sensitivity.py
artifacts/figures/fig_threshold_sensitivity.pdf
artifacts/figures/fig_threshold_sensitivity.png
artifacts/figures/fig1_teaser.py
artifacts/figures/plot_fig2.py
artifacts/figures/fig1_teaser_v2.py
artifacts/figures/fig2_ee_displacement_distribution.pdf
artifacts/figures/fig2_ee_displacement_distribution.png
artifacts/figures/fig1_teaser_v2.pdf
artifacts/figures/fig1_teaser_v2.png
artifacts/figures/gen_fig_displacement_hist.py
artifacts/figures/fig_displacement_hist.pdf
artifacts/figures/fig2_plan_a.py
artifacts/figures/fig2_plan_a.pdf
artifacts/figures/fig2_plan_a.png
artifacts/figures/fig1_teaser.pdf
artifacts/figures/fig1_teaser.png
artifacts/figures/fig2_plan_b.py
artifacts/figures/fig2_plan_b.pdf
artifacts/figures/fig2_plan_b.png
artifacts/figures/fig_overview.py
artifacts/figures/fig_overview.pdf
artifacts/figures/fig_overview.png
artifacts/figures/fig_overview_pb_v1_backup.png
artifacts/figures/fig_overview_pb_v2.png
artifacts/figures/fig_overview_pb_v4.png
artifacts/figures/fig_overview_pb_v5.png
artifacts/figures/fig_overview_pb_v6.png
artifacts/figures/fig_overview_pb_v7.png
artifacts/figures/fig_overview_pb_v8.png
artifacts/figures/fig_overview_pb_v9.png
artifacts/figures/fig_overview_pb_v10.png
artifacts/figures/fig_overview_pb_v11.png
artifacts/figures/fig_overview_pb_v11b.png
artifacts/figures/fig_overview_pb_v12.png
artifacts/figures/fig_overview_pb_v13.png
artifacts/figures/fig_overview_pb.png
artifacts/figures/fig_overview_pb.pdf
artifacts/figures/threshold_sensitivity_v2.csv
artifacts/figures/plot_fig5.py
artifacts/figures/gen_scatter.py
artifacts/figures/fig5_lambda_curve.pdf
artifacts/figures/fig5_lambda_curve.png
artifacts/figures/fig_pertask_car_fingerprint.pdf
artifacts/figures/fig_pertask_car_fingerprint.png
artifacts/figures/fig_tsr_car_scatter.pdf
artifacts/figures/fig_oracle_bar.pdf
artifacts/figures/plot_fig5_combined.py
artifacts/figures/fig5_lambda_and_fingerprint.pdf
artifacts/figures/fig5_lambda_and_fingerprint.png
artifacts/figures/plot_fig3_combined.py
artifacts/figures/fig3_scatter_and_oracle.pdf
artifacts/figures/fig3_scatter_and_oracle.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "0d938e5f-4cf2-4660-b68b-0bf88d926321",
  "tool_use_result": {
    "filenames": [
      "artifacts/figures/plot_fig3.py",
      "artifacts/figures/fig3_tsr_car_scatter.pdf",
      "artifacts/figures/fig3_tsr_car_scatter.png",
      "artifacts/figures/plot_threshold_sensitivity.py",
      "artifacts/figures/fig_threshold_sensitivity.pdf",
      "artifacts/figures/fig_threshold_sensitivity.png",
      "artifacts/figures/fig1_teaser.py",
      "artifacts/figures/plot_fig2.py",
      "artifacts/figures/fig1_teaser_v2.py",
      "artifacts/figures/fig2_ee_displacement_distribution.pdf",
      "artifacts/figures/fig2_ee_displacement_distribution.png",
      "artifacts/figures/fig1_teaser_v2.pdf",
      "artifacts/figures/fig1_teaser_v2.png",
      "artifacts/figures/gen_fig_displacement_hist.py",
      "artifacts/figures/fig_displacement_hist.pdf",
      "artifacts/figures/fig2_plan_a.py",
      "artifacts/figures/fig2_plan_a.pdf",
      "artifacts/figures/fig2_plan_a.png",
      "artifacts/figures/fig1_teaser.pdf",
      "artifacts/figures/fig1_teaser.png",
      "artifacts/figures/fig2_plan_b.py",
      "artifacts/figures/fig2_plan_b.pdf",
      "artifacts/figures/fig2_plan_b.png",
      "artifacts/figures/fig_overview.py",
      "artifacts/figures/fig_overview.pdf",
      "artifacts/figures/fig_overview.png",
      "artifacts/figures/fig_overview_pb_v1_backup.png",
      "artifacts/figures/fig_overview_pb_v2.png",
      "artifacts/figures/fig_overview_pb_v4.png",
      "artifacts/figures/fig_overview_pb_v5.png",
      "artifacts/figures/fig_overview_pb_v6.png",
      "artifacts/figures/fig_overview_pb_v7.png",
      "artifacts/figures/fig_overview_pb_v8.png",
      "artifacts/figures/fig_overview_pb_v9.png",
      "artifacts/figures/fig_overview_pb_v10.png",
      "artifacts/figures/fig_overview_pb_v11.png",
      "artifacts/figures/fig_overview_pb_v11b.png",
      "artifacts/figures/fig_overview_pb_v12.png",
      "artifacts/figures/fig_overview_pb_v13.png",
      "artifacts/figures/fig_overview_pb.png",
      "artifacts/figures/fig_overview_pb.pdf",
      "artifacts/figures/threshold_sensitivity_v2.csv",
      "artifacts/figures/plot_fig5.py",
      "artifacts/figures/gen_scatter.py",
      "artifacts/figures/fig5_lambda_curve.pdf",
      "artifacts/figures/fig5_lambda_curve.png",
      "artifacts/figures/fig_pertask_car_fingerprint.pdf",
      "artifacts/figures/fig_pertask_car_fingerprint.png",
      "artifacts/figures/fig_tsr_car_scatter.pdf",
      "artifacts/figures/fig_oracle_bar.pdf",
      "artifacts/figures/plot_fig5_combined.py",
      "artifacts/figures/fig5_lambda_and_fingerprint.pdf",
      "artifacts/figures/fig5_lambda_and_fingerprint.png",
      "artifacts/figures/plot_fig3_combined.py",
      "artifacts/figures/fig3_scatter_and_oracle.pdf",
      "artifacts/figures/fig3_scatter_and_oracle.png"
    ],
    "durationMs": 26,
    "numFiles": 56,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
All figures used in the paper have both PDF and PNG versions. LaTeX will prefer PDF (vector), which is good. But the overview figure `fig_overview_pb` — let me check if there's a PDF version. Yes, I see `fig_overview_pb.pdf` and `fig_overview_pb.png`. But there are also many versioned PNG files (v1-v13) that are unused leftovers — could be cleaned up.

The fact that PDFs exist for all main figures is good. But I should note the `fig_overview_pb` has many leftover versions that should be cleaned.


I'm not certain whether `fig_overview_pb.pdf` is a true vector or just a raster wrapped in PDF format. The presence of `fig_overview.py` suggests some figures are matplotlib-generated vectors, but `fig_overview_pb` lacks a generation script and has many version iterations, which points to it being created with a tool like PaperBanana — likely raster-based. Now I'm compiling my findings into a priority checklist.

The main issues I've identified are: the `fig:overview` label is defined but never referenced anywhere in the paper, there's inconsistent singular/plural usage of "Collision Avoidance Rate" between the abstract and the rest of the document, and several abbreviations like SSR and MDE are used without being defined. I'm also seeing inconsistent citation commands where some files use `\citep` while others use `\cite`, and there appear to be equation references that need checking.

Beyond those critical issues, there are cross-reference formatting inconsistencies where some sections use `Section~\ref{}` while others use `\S\ref{}`, and the appendix has duplicate labels on consecutive lines. For lower priority fixes, I'm noticing decimal precision inconsistencies in Table 4 where some values have two decimal places while others have one, and there seem to be some table environment formatting issues as well. uses `tabular*` while all other tables use `tabular`
3. **Table font size inconsistency** — appendix.tex:74 uses `\footnotesize` while other appendix tables use `\small`
4. **Appendix table placement** — all appendix tables use `[h]` which often fails; consider `[ht]` or `[htbp]`
5. **Subcaption style inconsistency** — fig:overview uses `\textbf{(a)}` style, fig:scatter_and_oracle and fig:lambda_and_fingerprint use plain `(Left)`/`(Right)`
6. **"n.s." not expanded** — introduction.tex:6 figure caption uses "(n.s.)" without ever defining the abbreviation
7. **~20 unreferenced labels in appendix** — standard for appendix sections but worth cleaning up

For Priority C issues, there are leftover figure versions cluttering the artifacts directory, some inconsistencies in notation like "100+ experiments" that could use LaTeX formatting, BibTeX key naming that varies across the document, missing PDF metadata setup, and an incomplete citation entry for jacquet2025neuralnmpc.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "17ee2114-dd65-46c4-bda0-52f66334a16d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gfJ4jw8zHVnDF3PFHH2ox",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 64987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1111
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

_source line 54_

I now have all the data needed. Let me load the tools needed to save the artifact and write the checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "15548d27-a2d5-41f7-abe7-9726dd18586a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gfJ4jw8zHVnDF3PFHH2ox",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 64987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1111
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

_source line 55_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Vsoj9uyJBkgtvCWPBRrKP9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "f64e6000-a2a1-472e-85af-17be4f06f1c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gfJ4jw8zHVnDF3PFHH2ox",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 64987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1111
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

_source line 56 · 2026-05-29T17:45:50.752Z_

<details><summary>↩ Tool result · `toolu_01Vsoj9uyJBkgtvCWPBRrKP9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "5a88dc13-7bd7-4df9-b69f-1de1c6f6c8ef",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Write · `toolu_01MccMNtxXbTqZ2PL2fZGLNB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/camera_ready_polish.md",
  "content": "# Camera-Ready Polish Checklist\n\n## Priority A (Should Fix)\n\n- [ ] `fig:overview` never referenced in text — Figure 1 (overview) is defined but no `\\ref{fig:overview}` appears anywhere; add explicit reference in intro paragraph — introduction.tex:7\n- [ ] \"Collision Avoidance Rates\" (plural) in abstract vs \"Collision Avoidance Rate\" (singular) everywhere else; standardize to singular — abstract.tex:2 vs introduction.tex:10, method.tex:5\n- [ ] SSR abbreviation never expanded — first use \"SSR\\,=\\,TSR\\,$\\cap$\\,CAR\" defines the formula but never spells out \"Safe Success Rate\" (or whatever it stands for) — claim3.tex:36\n- [ ] MDE abbreviation never defined — used in claim3.tex:59 (\"MDE ${\\approx}$ 5.6\\,pp\") and discussion.tex:7 without expansion to \"Minimum Detectable Effect\"\n- [ ] `\\citep` vs `\\cite` inconsistency — related_work.tex:12 uses `\\citep{zhang2025safevla}` and `\\citep{hu2025vlsa}`; appendix.tex:323 uses `\\citep{hu2022lora}`; all other citations use `\\cite`. Mixing may produce different bracket styles depending on natbib config\n- [ ] Equations never cross-referenced — `eq:car_f` (method.tex:31) and `eq:total_loss` (method.tex:39) are labeled but never referenced via `\\eqref` or `Eq.~\\ref`; either reference them or remove the labels\n- [ ] Section cross-reference style inconsistent — introduction.tex:16,18,20 use `Section~\\ref{}`; claim2.tex:3 and discussion.tex:3 use `\\S\\ref{}`; related_work.tex:15 uses `\\S\\ref{}`. Pick one convention and apply uniformly\n- [ ] Duplicate `\\label` on same section — appendix.tex:153-154 has both `\\label{sec:appendix_pertask}` and `\\label{sec:appendix_pertask_oracle}` on consecutive lines for the same section; `sec:appendix_pertask` is never referenced and should be removed\n\n## Priority B (Nice to Have)\n\n- [ ] CAR decimal precision inconsistent in Table 4 — claim3.tex:17-20: LoRA-only reports 54.83, SDF λ=0.005 reports 54.5 (should be 54.50), SDF λ=0.1 reports 57.00. Standardize all means to same decimal places\n- [ ] Table environment mismatch — claim1.tex:11 uses `\\begin{tabular*}{\\linewidth}` while all other tables use `\\begin{tabular}`. Standardize\n- [ ] Table font size inconsistency in appendix — appendix.tex:74 (`tab:dfcar_threshold`) uses `\\footnotesize` while all other appendix tables use `\\small`\n- [ ] Appendix table placement specifier — all appendix tables use `[h]` which LaTeX often overrides; consider `[ht]` or `[htbp]` to avoid \"float too large\" warnings\n- [ ] Sub-figure labeling style inconsistent — fig:overview caption (introduction.tex:6) uses `\\textbf{(a)}`, `\\textbf{(b)}`, `\\textbf{(c)}` but fig:scatter_and_oracle (claim1.tex:27) and fig:lambda_and_fingerprint (claim3.tex:31) use plain `(Left)`/`(Right)`. Pick one convention\n- [ ] \"n.s.\" not expanded — introduction.tex:6 (overview figure caption) uses \"n.s.\" without defining it. While standard in statistics, expanding once (\"not significant, n.s.\") aids non-specialist readers\n- [ ] `\\label{sec:oracle_setup}` placed at end of paragraph, not at `\\subsection` — method.tex:46 attaches the label to the end of a paragraph rather than a section/subsection heading, which is fragile for cross-references\n- [ ] `\\label{sec:anticorrelation}` mid-paragraph — claim1.tex:30 defines this label inline mid-sentence; never referenced. Remove or relocate\n- [ ] `\\label{sec:tsr_collapse}` on `\\paragraph` — claim3.tex:35; never referenced from outside. Remove if unused\n- [ ] `\\label{sec:lambda_high}` on `\\paragraph` — claim3.tex:58; never referenced. Remove if unused\n- [ ] `jacquet2025neuralnmpc` missing volume/pages — references.bib:170; journal article with no volume, number, or page range (may be in-press; add \"to appear\" note if so)\n\n## Priority C (Cosmetic)\n\n- [ ] ~15 leftover figure versions in `artifacts/figures/` (fig_overview_pb_v1 through v13, fig1_teaser_v2, fig2_plan_a/b, etc.) — not included in paper; clean up before camera-ready archive submission\n- [ ] \"100+ experiments\" in introduction.tex:14 — consider `$>$100 experiments` for typographic consistency with other numeric comparisons in the paper\n- [ ] BibTeX key naming inconsistent — most keys follow `authorYYYYkeyword` (e.g., `black2024pi0`) but `cofreeevla2026`, `depthvla2025` omit author prefix. Not reader-visible but aids maintainability\n- [ ] No `\\hypersetup` for PDF metadata — main.tex has no `\\hypersetup{pdftitle=..., pdfauthor=...}`; camera-ready PDF should carry correct metadata (update `pdfauthor` when de-anonymizing)\n- [ ] `\\keywords` placement — main.tex:28 places `\\keywords` after `\\input{abstract}`; verify `corl_2026.sty` expects this ordering (some styles require keywords inside the abstract environment)\n- [ ] Unreferenced appendix section labels (not harmful but noisy) — `sec:appendix_multiseed`, `sec:appendix_displacement`, `sec:appendix_tsr_pertask`, `sec:appendix_pertask_car`, `sec:appendix_ssr`, `sec:appendix_stepwise`, `sec:appendix_spatial_bowl`, `sec:appendix_eval_seed`, `sec:appendix_tsr_collapse`, `sec:conclusion`, `sec:limitations`, `sec:intro`, `sec:method`, `sec:benchmark`, `sec:sdf_aux`. Many are structural anchors (standard); consider removing truly orphaned ones\n- [ ] Figures have both PDF and PNG versions — LaTeX will prefer PDF (vector), which is correct; ensure no `\\includegraphics` call accidentally specifies `.png` extension to avoid raster fallback\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "0e14fa36-d95a-49d6-a3bd-0e18bb98dc72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEQYBbgnMyouXTVc55Sfgm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2047,
      "cache_read_input_tokens": 66098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2047
      },
      "output_tokens": 61,
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

_source line 58 · 2026-05-29T17:46:26.774Z_

<details><summary>↩ Tool result · `toolu_01MccMNtxXbTqZ2PL2fZGLNB`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/camera_ready_polish.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "6826076c-a27b-42f9-88f9-beaafab7b89e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/camera_ready_polish.md",
    "content": "# Camera-Ready Polish Checklist\n\n## Priority A (Should Fix)\n\n- [ ] `fig:overview` never referenced in text — Figure 1 (overview) is defined but no `\\ref{fig:overview}` appears anywhere; add explicit reference in intro paragraph — introduction.tex:7\n- [ ] \"Collision Avoidance Rates\" (plural) in abstract vs \"Collision Avoidance Rate\" (singular) everywhere else; standardize to singular — abstract.tex:2 vs introduction.tex:10, method.tex:5\n- [ ] SSR abbreviation never expanded — first use \"SSR\\,=\\,TSR\\,$\\cap$\\,CAR\" defines the formula but never spells out \"Safe Success Rate\" (or whatever it stands for) — claim3.tex:36\n- [ ] MDE abbreviation never defined — used in claim3.tex:59 (\"MDE ${\\approx}$ 5.6\\,pp\") and discussion.tex:7 without expansion to \"Minimum Detectable Effect\"\n- [ ] `\\citep` vs `\\cite` inconsistency — related_work.tex:12 uses `\\citep{zhang2025safevla}` and `\\citep{hu2025vlsa}`; appendix.tex:323 uses `\\citep{hu2022lora}`; all other citations use `\\cite`. Mixing may produce different bracket styles depending on natbib config\n- [ ] Equations never cross-referenced — `eq:car_f` (method.tex:31) and `eq:total_loss` (method.tex:39) are labeled but never referenced via `\\eqref` or `Eq.~\\ref`; either reference them or remove the labels\n- [ ] Section cross-reference style inconsistent — introduction.tex:16,18,20 use `Section~\\ref{}`; claim2.tex:3 and discussion.tex:3 use `\\S\\ref{}`; related_work.tex:15 uses `\\S\\ref{}`. Pick one convention and apply uniformly\n- [ ] Duplicate `\\label` on same section — appendix.tex:153-154 has both `\\label{sec:appendix_pertask}` and `\\label{sec:appendix_pertask_oracle}` on consecutive lines for the same section; `sec:appendix_pertask` is never referenced and should be removed\n\n## Priority B (Nice to Have)\n\n- [ ] CAR decimal precision inconsistent in Table 4 — claim3.tex:17-20: LoRA-only reports 54.83, SDF λ=0.005 reports 54.5 (should be 54.50), SDF λ=0.1 reports 57.00. Standardize all means to same decimal places\n- [ ] Table environment mismatch — claim1.tex:11 uses `\\begin{tabular*}{\\linewidth}` while all other tables use `\\begin{tabular}`. Standardize\n- [ ] Table font size inconsistency in appendix — appendix.tex:74 (`tab:dfcar_threshold`) uses `\\footnotesize` while all other appendix tables use `\\small`\n- [ ] Appendix table placement specifier — all appendix tables use `[h]` which LaTeX often overrides; consider `[ht]` or `[htbp]` to avoid \"float too large\" warnings\n- [ ] Sub-figure labeling style inconsistent — fig:overview caption (introduction.tex:6) uses `\\textbf{(a)}`, `\\textbf{(b)}`, `\\textbf{(c)}` but fig:scatter_and_oracle (claim1.tex:27) and fig:lambda_and_fingerprint (claim3.tex:31) use plain `(Left)`/`(Right)`. Pick one convention\n- [ ] \"n.s.\" not expanded — introduction.tex:6 (overview figure caption) uses \"n.s.\" without defining it. While standard in statistics, expanding once (\"not significant, n.s.\") aids non-specialist readers\n- [ ] `\\label{sec:oracle_setup}` placed at end of paragraph, not at `\\subsection` — method.tex:46 attaches the label to the end of a paragraph rather than a section/subsection heading, which is fragile for cross-references\n- [ ] `\\label{sec:anticorrelation}` mid-paragraph — claim1.tex:30 defines this label inline mid-sentence; never referenced. Remove or relocate\n- [ ] `\\label{sec:tsr_collapse}` on `\\paragraph` — claim3.tex:35; never referenced from outside. Remove if unused\n- [ ] `\\label{sec:lambda_high}` on `\\paragraph` — claim3.tex:58; never referenced. Remove if unused\n- [ ] `jacquet2025neuralnmpc` missing volume/pages — references.bib:170; journal article with no volume, number, or page range (may be in-press; add \"to appear\" note if so)\n\n## Priority C (Cosmetic)\n\n- [ ] ~15 leftover figure versions in `artifacts/figures/` (fig_overview_pb_v1 through v13, fig1_teaser_v2, fig2_plan_a/b, etc.) — not included in paper; clean up before camera-ready archive submission\n- [ ] \"100+ experiments\" in introduction.tex:14 — consider `$>$100 experiments` for typographic consistency with other numeric comparisons in the paper\n- [ ] BibTeX key naming inconsistent — most keys follow `authorYYYYkeyword` (e.g., `black2024pi0`) but `cofreeevla2026`, `depthvla2025` omit author prefix. Not reader-visible but aids maintainability\n- [ ] No `\\hypersetup` for PDF metadata — main.tex has no `\\hypersetup{pdftitle=..., pdfauthor=...}`; camera-ready PDF should carry correct metadata (update `pdfauthor` when de-anonymizing)\n- [ ] `\\keywords` placement — main.tex:28 places `\\keywords` after `\\input{abstract}`; verify `corl_2026.sty` expects this ordering (some styles require keywords inside the abstract environment)\n- [ ] Unreferenced appendix section labels (not harmful but noisy) — `sec:appendix_multiseed`, `sec:appendix_displacement`, `sec:appendix_tsr_pertask`, `sec:appendix_pertask_car`, `sec:appendix_ssr`, `sec:appendix_stepwise`, `sec:appendix_spatial_bowl`, `sec:appendix_eval_seed`, `sec:appendix_tsr_collapse`, `sec:conclusion`, `sec:limitations`, `sec:intro`, `sec:method`, `sec:benchmark`, `sec:sdf_aux`. Many are structural anchors (standard); consider removing truly orphaned ones\n- [ ] Figures have both PDF and PNG versions — LaTeX will prefer PDF (vector), which is correct; ensure no `\\includegraphics` call accidentally specifies `.png` extension to avoid raster fallback\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01UYGhcwtGD537h5pK7HanhG`</summary>

```json
{
  "name": "camera_ready_polish",
  "type": "report",
  "description": "Camera-ready polish checklist: 8 Priority-A issues (unreferenced fig:overview, CAR singular/plural, undefined abbreviations SSR/MDE, citep/cite mixing, unreferenced equations, cross-ref style inconsistency, duplicate label), 11 Priority-B, 7 Priority-C",
  "project": "diff_collision_sdf",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/camera_ready_polish.md",
  "tags": [
    "paper",
    "camera-ready",
    "checklist"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "b0fbc4b4-deb8-4bdb-a6b9-3e3c33695dae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUtGii84WZ4hTndb5kQxMF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1845,
      "cache_read_input_tokens": 68145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1845
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

_source line 60 · 2026-05-29T17:46:31.799Z_

<details><summary>↩ Tool result · `toolu_01UYGhcwtGD537h5pK7HanhG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260529_8d7c1a\", \"name\": \"camera_ready_polish\", \"type\": \"report\", \"description\": \"Camera-ready polish checklist: 8 Priority-A issues (unreferenced fig:overview, CAR singular/plural, undefined abbreviations SSR/MDE, citep/cite mixing, unreferenced equations, cross-ref style inconsistency, duplicate label), 11 Priority-B, 7 Priority-C\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/report/camera_ready_polish.md\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-29T17:46:31.582344+00:00\", \"tags\": [\"paper\", \"camera-ready\", \"checklist\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "28780cf8-0fbc-420d-8d84-68a855a17dc8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260529_8d7c1a\\\", \\\"name\\\": \\\"camera_ready_polish\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Camera-ready polish checklist: 8 Priority-A issues (unreferenced fig:overview, CAR singular/plural, undefined abbreviations SSR/MDE, citep/cite mixing, unreferenced equations, cross-ref style inconsistency, duplicate label), 11 Priority-B, 7 Priority-C\\\", \\\"path\\\": \\\"projects/diff_collision_sdf/artifacts/_project/report/camera_ready_polish.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"diff_collision_sdf\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-29T17:46:31.582344+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"camera-ready\\\", \\\"checklist\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260529_8d7c1a\", \"name\": \"camera_ready_polish\", \"type\": \"report\", \"description\": \"Camera-ready polish checklist: 8 Priority-A issues (unreferenced fig:overview, CAR singular/plural, undefined abbreviations SSR/MDE, citep/cite mixing, unreferenced equations, cross-ref style inconsistency, duplicate label), 11 Priority-B, 7 Priority-C\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/report/camera_ready_polish.md\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-29T17:46:31.582344+00:00\", \"tags\": [\"paper\", \"camera-ready\", \"checklist\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

检查清单已生成并注册：`artifacts/camera_ready_polish.md`

**汇总**：8 项 Priority A（必须修），11 项 Priority B，7 项 Priority C。

最关键的几个：
- `fig:overview`（概览图）全文无 `\ref` 引用
- Abstract 里 "Rates"（复数）与正文 "Rate"（单数）不一致
- SSR、MDE 两个缩写从未展开定义
- `\citep` 和 `\cite` 混用（3 处 `\citep`，其余全是 `\cite`）
- 两个方程（`eq:car_f`、`eq:total_loss`）有 label 但从未被引用
- Section 引用风格混用 `Section~\ref` 和 `\S\ref`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "uuid": "1c1cfbbf-3ccb-43ba-af4a-9601415793f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WumWA3bySdSHGb3Q7yDK7B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 69990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 62_

检查清单已生成并注册：`artifacts/camera_ready_polish.md`

**汇总**：8 项 Priority A（必须修），11 项 Priority B，7 项 Priority C。

最关键的几个：
- `fig:overview`（概览图）全文无 `\ref` 引用
- Abstract 里 "Rates"（复数）与正文 "Rate"（单数）不一致
- SSR、MDE 两个缩写从未展开定义
- `\citep` 和 `\cite` 混用（3 处 `\citep`，其余全是 `\cite`）
- 两个方程（`eq:car_f`、`eq:total_loss`）有 label 但从未被引用
- Section 引用风格混用 `Section~\ref` 和 `\S\ref`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 269395,
  "duration_api_ms": 270746,
  "num_turns": 25,
  "stop_reason": "end_turn",
  "session_id": "6419330c-662b-48f6-bb03-bab9851839a5",
  "total_cost_usd": 1.055257,
  "usage": {
    "input_tokens": 4232,
    "cache_creation_input_tokens": 71706,
    "cache_read_input_tokens": 458517,
    "output_tokens": 14191,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 71706,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 233,
        "cache_read_input_tokens": 69990,
        "cache_creation_input_tokens": 592,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 592
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1821,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001901,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4232,
      "outputTokens": 14191,
      "cacheReadInputTokens": 458517,
      "cacheCreationInputTokens": 71706,
      "webSearchRequests": 0,
      "costUSD": 1.0533559999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "72adffc8-ab64-4fb3-93ee-b9bc9e931675"
}
```

</details>

---
