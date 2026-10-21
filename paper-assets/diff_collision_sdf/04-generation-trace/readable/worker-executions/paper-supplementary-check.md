# paper supplementary check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_paper_supplementary-check_20260529T132039.log`
- **Structured JSON:** [`66829c9a1ba73ef09733.json`](../../sessions/66/66829c9a1ba73ef09733.json)

## Before a recorded user message

44 recorded events

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
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
  "uuid": "e1da8d2f-15c2-4cea-9cb7-82a24ab925c2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1780078200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7ba153ae-2dc4-44eb-aa3d-5b66f79a668a",
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e"
}
```

---

### Assistant

_source line 4_

I'll read all the tex files to check supplementary completeness. Let me start by reading them in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "67f65ed1-472d-40ae-826e-e350ccef6e21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — Read · `toolu_017Mb4MUVQcN1eshnGXspv6q`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "eec54c4d-a0fe-4889-a158-d581ec274631",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-29T13:20:49.160Z_

<details><summary>↩ Tool result · `toolu_017Mb4MUVQcN1eshnGXspv6q`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "974d1fc2-7dfa-4651-8d73-6a0a71c52485",
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

<details open><summary>🔧 Tool call — Read · `toolu_013S1ayNGKXbMSyAMmTG1L64`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "54342ea6-5555-4948-bbf6-5a0a3b6adcc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 8 · 2026-05-29T13:20:49.612Z_

<details><summary>↩ Tool result · `toolu_013S1ayNGKXbMSyAMmTG1L64`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "de98296d-e0dc-4546-9384-82845fcfd015",
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

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01G2E4jU7htqjvG3ZJ2ByWQZ`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "203221f5-2180-4458-bf5d-a42ea5367090",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 10 · 2026-05-29T13:20:50.080Z_

<details><summary>↩ Tool result · `toolu_01G2E4jU7htqjvG3ZJ2ByWQZ`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "cd86aee5-a0c2-49f3-9efd-55b2baeee4a3",
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Nky84XsmZkVGebJPySzDMs`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "a2f1b2f2-a717-43cd-9ffe-04e1d3545d76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 12 · 2026-05-29T13:20:50.552Z_

<details><summary>↩ Tool result · `toolu_01Nky84XsmZkVGebJPySzDMs`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "7ce87a5c-4d57-406a-8055-f5852f51f28d",
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_019MegSakDcz2uqzEm9E1QRH`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "fe790bd0-d972-4eeb-911e-9c246e501cb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 14 · 2026-05-29T13:20:51.022Z_

<details><summary>↩ Tool result · `toolu_019MegSakDcz2uqzEm9E1QRH`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "85a2609a-09fb-492c-9bb6-7e6a94cb7fde",
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01LVDTDu2LP3K13wqoWfAX25`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "8401f321-f039-4103-9b10-9c41f4bc037b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 16 · 2026-05-29T13:20:51.453Z_

<details><summary>↩ Tool result · `toolu_01LVDTDu2LP3K13wqoWfAX25`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "bf63afdb-4a9b-4eaa-97e7-19f96fc9c73e",
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01KtyeQiSNxTaP8pcxvT73ST`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "d39c04ab-f15b-4f2a-9b9d-3436570c0f1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 18 · 2026-05-29T13:20:52.434Z_

<details><summary>↩ Tool result · `toolu_01KtyeQiSNxTaP8pcxvT73ST`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "a3da690e-07f5-4767-a2de-c41fe61697b4",
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01JuEdmkrqiWnrQdaHcSCaMy`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "8df84a82-03cd-4fdf-a812-e92fdfb805a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 20 · 2026-05-29T13:20:52.881Z_

<details><summary>↩ Tool result · `toolu_01JuEdmkrqiWnrQdaHcSCaMy`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We tested whether SDF supervision and collision-aware evaluation deliver reliable geometric safety for VLAs. Action collapse renders reported CAR illusory; dfCAR corrects this using only EE position logging (\S\ref{sec:dfcar}). EE-only oracle SDF refinement is counterproductive, reducing CAR by 5--10\,pp as unmonitored links rotate through obstacles (\S\ref{sec:ee_only}), and collision-free demonstrations account for nearly all avoidance gains with no statistically significant SDF benefit (\S\ref{sec:avoidance_source}). More broadly, dfCAR provides a lightweight diagnostic that any VLA pipeline can adopt to screen for action-collapse contamination, and point-supervision of a single link is insufficient for articulated robots; genuine geometric safety will require full-body collision representations and cross-architecture validation.
4	
5	\section{Limitations}\label{sec:limitations}
6	
7	All experiments use MuJoCo simulation (SafeLIBERO, two VLA families, four pick-and-place tasks); action collapse is structurally general but untested on other benchmarks or real hardware. dfCAR assumes bimodal displacement separation (Figure~\ref{fig:displacement}), which may require task-specific calibration when less pronounced. The EE-only SDF null result is specific to auxiliary loss integration and should not be extrapolated to constrained optimization or runtime filtering (Section~\ref{sec:related}). Oracle refinement uses a single seed per variant ($n{=}1$, 160 episodes). The training ablation ($n{=}3$ seeds; MDE ${\approx}$ 5.6\,pp at 80\% power) cannot rule out a small SDF effect (2--5\,pp) without larger samples.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "881be4cf-3360-4c95-98eb-ed71c98b9794",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe tested whether SDF supervision and collision-aware evaluation deliver reliable geometric safety for VLAs. Action collapse renders reported CAR illusory; dfCAR corrects this using only EE position logging (\\S\\ref{sec:dfcar}). EE-only oracle SDF refinement is counterproductive, reducing CAR by 5--10\\,pp as unmonitored links rotate through obstacles (\\S\\ref{sec:ee_only}), and collision-free demonstrations account for nearly all avoidance gains with no statistically significant SDF benefit (\\S\\ref{sec:avoidance_source}). More broadly, dfCAR provides a lightweight diagnostic that any VLA pipeline can adopt to screen for action-collapse contamination, and point-supervision of a single link is insufficient for articulated robots; genuine geometric safety will require full-body collision representations and cross-architecture validation.\n\n\\section{Limitations}\\label{sec:limitations}\n\nAll experiments use MuJoCo simulation (SafeLIBERO, two VLA families, four pick-and-place tasks); action collapse is structurally general but untested on other benchmarks or real hardware. dfCAR assumes bimodal displacement separation (Figure~\\ref{fig:displacement}), which may require task-specific calibration when less pronounced. The EE-only SDF null result is specific to auxiliary loss integration and should not be extrapolated to constrained optimization or runtime filtering (Section~\\ref{sec:related}). Oracle refinement uses a single seed per variant ($n{=}1$, 160 episodes). The training ablation ($n{=}3$ seeds; MDE ${\\approx}$ 5.6\\,pp at 80\\% power) cannot rule out a small SDF effect (2--5\\,pp) without larger samples.\n",
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01KiM6QLGQKx6Gcy7SgPvZpY`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "215e56b8-9d85-4350-a91d-889b08b8d4b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 22 · 2026-05-29T13:20:53.375Z_

<details><summary>↩ Tool result · `toolu_01KiM6QLGQKx6Gcy7SgPvZpY`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "46273709-6dd9-46cb-a5fe-5d9260c82108",
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01BpfPgqQBprSzCkWr5iwfNQ`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "050a2461-1aea-41d4-acb8-5e67d5a7faf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E14XpGDjGW2kyTazi8qDC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12329,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12329
      },
      "output_tokens": 4,
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

_source line 24 · 2026-05-29T13:20:54.066Z_

<details><summary>↩ Tool result · `toolu_01BpfPgqQBprSzCkWr5iwfNQ`</summary>

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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "24197824-a26d-49a7-af58-68f44aa88208",
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

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the appendix file since it seems to be long.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "4fbe4fe9-27a9-4c7a-ba11-5a82d9e01f62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bofrWeGXtL3kPg3zxBukh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23237,
      "cache_read_input_tokens": 23780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23237
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

_source line 26_

Let me read the rest of the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "4a2bbaaa-e8a0-4e8b-b970-425dc6073ffe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bofrWeGXtL3kPg3zxBukh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23237,
      "cache_read_input_tokens": 23780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23237
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_019Qn18bYd8dzkHawhpNrNBS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "offset": 375
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "84e5cd23-9269-40d1-85ed-1d377922d61d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bofrWeGXtL3kPg3zxBukh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23237,
      "cache_read_input_tokens": 23780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23237
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

_source line 28 · 2026-05-29T13:20:58.662Z_

<details><summary>↩ Tool result · `toolu_019Qn18bYd8dzkHawhpNrNBS`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (375). The file has 375 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "0ea16c70-ae1b-43da-a85a-2f042da64a42",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "",
      "numLines": 1,
      "startLine": 375,
      "totalLines": 375
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Good, I've read all the files. Now let me systematically analyze the cross-references, number consistency, content coverage, and issues.

Let me extract all the cross-references from the main paper to the appendix:

**Main paper references to appendix:**

1. `claim1.tex` line 32: `Appendix~\ref{sec:appendix_threshold}` — threshold sensitivity
2. `claim2.tex` line 7: `Appendix~\ref{sec:appendix_pertask_oracle}` — per-task oracle
3. `claim2.tex` line 30: `Appendix~\ref{sec:appendix_oracle}` — oracle details


4. `claim2.tex` line 30: `Appendix~\ref{sec:appendix_pertask_oracle}` — per-task oracle (again)
5. `claim3.tex` line 26: `Appendix~\ref{sec:appendix_null}` — null distribution
6. `claim3.tex` line 59: `Appendix~\ref{sec:appendix_null}` — null distribution (again)
7. `method.tex` line 34: `Appendix~\ref{sec:appendix_threshold}` — threshold sensitivity
8. `method.tex` line 38: `Appendix~\ref{sec:appendix_training}` and references to hyperparameter tables — training details
9. `method.tex` line 46: `Appendix~\ref{sec:appendix_oracle}` — oracle details
10. `experimental_framework.tex` line 23: `Appendix~\ref{sec:appendix_threshold}` — threshold sensitivity

I should also check the abstract to see if it references any appendices, though it's unlikely. Looking at the appendix labels themselves now to verify what sections are actually defined.

Compiling the full list of appendix labels from appendix.tex: I've got multiseed, displacement, threshold, tsr_pertask, pertask_car, ssr, pertask with its oracle variant, null, stepwise, oracle, spatial_bowl, and eval_seed sections defined across the file. Continuing to verify the remaining table labels and checking which appendix references from the main document are actually defined.

I notice several appendix sections that aren't directly referenced from the main text — like the multiseed results, displacement analysis, per-task TSR breakdown, per-task car details, SSR table, and stepwise analysis. Some of these have inverse references where the appendix points back to the main text, but the main document doesn't explicitly call them out.

Now I'm checking whether the main text actually references these specific tables, and it looks like many of them aren't cited at all — the multiseed full table, threshold sensitivity, per-task metrics, oracle results, and seed robustness tables all appear to be appendix-only content.

Let me shift focus to verifying the numbers themselves. I'm checking the main paper claims against the actual table values — like the 91.5% CAR for Pi0+A1 and the 99.6% safe episodes statistic — to make sure everything matches up correctly. Collapsed = 99.6% ✅
- "dfCAR drops to ≈0%" → Table tab:fake_safety: dfCAR ≈ 0 ✅
- "73--77% vs. 82--83%" for oracle → Table tab:oracle: oracle range 73.1-76.9, baseline 82.0-83.0 ✅
- "+26 pp CAR" → claim3.tex: 28.5 → 54.83, difference = 26.33 ≈ 26 ✅
- "+2.2 pp (p = 0.155, n.s.)" → claim3.tex: 54.83 vs 57.00 = +2.17 ≈ +2.2 ✅
- "3/732 safe episodes survive" → need to find in claim1.tex

Now checking the main claims: the threshold range claim is verified in the appendix table showing consistent dfCAR values across 2-200 mm, and the oracle performance claims check out with the oracle variants underperforming baselines by the stated margins, with per-task breakdowns available in the appendix. I'm verifying the LoRA baseline performance at 54.83% CAR, checking the λ = 0.1 configuration with its p-value, and confirming the Phase 2 ablation results where removing the penalty after step 5K yields 57.5% CAR. I'm also tracking how the SSR/TSR ratio shifts from the baseline 0.39 up to the 0.51–0.60 range across these conditions.

Now I'm cross-referencing the multi-seed results for λ = 0.1, which shows three runs at 58.0%, 58.5%, and 54.5% averaging to 57.0% ± 2.18, and I'm working through the statistical power calculation to confirm that detecting effects of 5.6 percentage points requires the sample size and variance we're working with. Continuing to verify the remaining SDF configurations and double-checking the LoRA-only baseline calculations, including the standard deviation across seeds. Now I'm verifying the per-task collision avoidance results across the appendix tables, checking that the LoRA seed aggregates and SDF lambda variants all match up correctly, then diving into a specific calculation to validate one of the per-task breakdowns. Now I'm verifying the standard deviation calculation by working through the squared deviations and confirming the variance comes to about 4.167, giving a standard deviation of roughly 2.04. The permutation test shows 6 out of 84 possible combinations yield a mean at or above 57.0, resulting in a one-tailed p-value of 0.071, and the two-tailed test captures 13 combinations for a p-value around 0.155—all the numbers align correctly. Moving on to check the ablation study details and threshold specifications. I'm checking which appendix tables and figures are actually referenced from the main text—some are cited directly by table reference while others are only mentioned through section references, so I need to verify the distinction more carefully. appendix_stepwise covers step-wise checkpoint analysis, appendix_spatial_bowl has cross-scene validation data that's already in the main text Table 5, appendix_eval_seed addresses eval seed robustness, and appendix_tsr_collapse analyzes the TSR collapse mechanism. Most of these are supplementary and don't require main text references, though some like the SSR analysis are implicitly connected through table citations. I should verify whether any of these sections genuinely warrant explicit references from the main text—the multiseed appendix providing per-seed details for Table tab:avoidance_source is a borderline case where a reference would be good practice but isn't strictly necessary.

Looking more carefully, there are a few mild gaps: the step-wise progression isn't referenced even though the main text discusses λ=0.1 results, the TSR collapse section isn't cited despite claim3.tex discussing the CAR-TSR trade-off, and the per-task CAR ordering appendix lacks an explicit reference even though the main text mentions this finding. The eval seed robustness check is purely supplementary with no main text mention. The critical appendix sections—threshold details, oracle information, null distribution, and training specifics—are already properly referenced, so these gaps are relatively minor.

I'm also noticing that some appendix sections seem thin or redundant: the displacement section just points back to a main text figure, and the SSR section appears to be cut off mid-sentence, suggesting these might be placeholder sections that could be consolidated or removed. I'm also noticing several more appendix sections that aren't referenced from the main text—stepwise results, evaluation seed analysis, and TSR collapse details. Then there's a mismatch in the TSR values: the main table shows LoRA-only mean at 49.7±3.2, but the per-seed breakdown lists 46.0 for the first seed, which suggests either a calculation error or inconsistent data across conditions.

Let me verify the math on those per-seed values to make sure they actually average to what's reported in the main table, and I should also check whether experimental_framework.tex and method.tex are duplicating content or if they're properly separated. I'm realizing experimental_framework.tex isn't actually included in main.tex — it's an orphaned file, likely an earlier draft of the method section. So those redundant appendix references don't matter since that file never makes it into the compiled paper. Now I need to verify whether method.tex itself has adequate appendix citations.

Looking at method.tex, I can see it properly references the appendix sections for threshold sensitivity, training hyperparameters, and oracle implementation details — all the key methodological components are accounted for.

Now I'm checking the EE displacement values across the tables to see if there's consistency between the main text results and the appendix data. Verifying the per-task Oracle calculations: Oracle-adaptive averages to 75.0%, Oracle-fixed to 73.1%, and Oracle-feature to 76.9% — all matching the reported numbers. Now checking the Pi0.5 LoRA analysis where the CAR reduction of 5.1 percentage points (57.0% minus 51.9%) also checks out. The per-task average checks out at 57.0, confirming the Pi0.5 LoRA s0 numbers are consistent across both tables. Now that I've verified the numerical integrity throughout, I'm ready to compile the full report and document all the cross-references from the main text to the appendix.

All six unique references resolve correctly to their corresponding labels, and the number consistency checks have passed.

Now I'm reviewing the content coverage—the appendix includes all the key ablation studies, seed robustness analysis, and implementation details. But there are several structural issues: the experimental_framework.tex file isn't being compiled into the main document, there are two mostly empty appendix sections that just point back to the main text, and several appendix sections exist but aren't actually referenced anywhere. There's also a duplicate label that's defined but never used, and no figures appear in the appendix despite having content there. Let me draft the report now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "1dd76d8d-247e-4f0b-969f-b9b92f184213",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129bxbubKA9qFk3WsrzTciy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 47017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
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

_source line 30_

Now let me systematically extract all cross-references. Let me search for all `\ref` calls pointing to appendix labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "32c85c22-66d5-42a4-8bb8-9beeb9f22274",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129bxbubKA9qFk3WsrzTciy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 47017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
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

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01Qcybs2vGU9VskaESNfP9pX`</summary>

```json
{
  "pattern": "\\\\ref\\{sec:appendix|\\\\ref\\{tab:hyperparams|\\\\ref\\{tab:multiseed|\\\\ref\\{tab:threshold|\\\\ref\\{tab:dfcar|\\\\ref\\{tab:per_task|\\\\ref\\{tab:oracle_pertask|\\\\ref\\{tab:stepwise|\\\\ref\\{tab:eval_seed",
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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "ba5d6b0e-c4cd-4618-9bb9-467c3ae171f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129bxbubKA9qFk3WsrzTciy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 47017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
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

_source line 32 · 2026-05-29T13:23:17.741Z_

<details><summary>↩ Tool result · `toolu_01Qcybs2vGU9VskaESNfP9pX`</summary>

```text
docs/paper/claim3.tex:26:[Omitted long matching line]
docs/paper/claim3.tex:59:[Omitted long matching line]
docs/paper/experimental_framework.tex:23:where $d_{\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\tau_d = 0.1$\,mm corresponds to sub-actuator-resolution motion. In practice, the displacement distribution is bimodal: collapsed episodes cluster below 1\,$\mu$m and active episodes exceed 200\,mm, with no intermediate population. Consequently, any $\tau_d \in [2, 200]$\,mm produces identical filtering (Appendix~\ref{sec:appendix_threshold}).
docs/paper/method.tex:34:The displacement distribution is sharply bimodal (collapsed episodes below 1\,$\mu$m, active above 200\,mm), making $\tau_d$ robust across $[2, 200]$\,mm (Appendix~\ref{sec:appendix_threshold}). For Pi0 under A1, $d_{\max}$ uses obstacle displacement due to an inconsistent EE reference frame; Pi0.5 uses standard EE displacement.
docs/paper/method.tex:38:We augment LoRA-adapted~\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\ref{sec:appendix_training}, Table~\ref{tab:hyperparams}). The total loss is:
docs/paper/method.tex:46:In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\,=\,0\%; Table~\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\ref{sec:appendix_oracle}).\label{sec:oracle_setup}
docs/paper/archive/analysis_claim1.tex:31:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:31:[Omitted long matching line]
docs/paper/claim2.tex:7:\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}. Oracle variants use 160 episodes (4 tasks $\times$ 40); all other conditions use 200 episodes (4 tasks $\times$ 50).}
docs/paper/claim2.tex:31:[Omitted long matching line]
docs/paper/appendix.tex:4:Table~\ref{tab:multiseed_full} reports individual-seed CAR and TSR for all fine-tuned conditions at the 30K checkpoint (200 episodes each, evaluation seed\,=\,7). These per-seed values underlie the means reported in Table~\ref{tab:avoidance_source}.
docs/paper/appendix.tex:47:To validate the robustness of our displacement threshold $\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% action-collapse rate even at the most conservative setting.
docs/paper/appendix.tex:67:Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
docs/paper/appendix.tex:96:Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
docs/paper/appendix.tex:121:[Omitted long matching line]
docs/paper/appendix.tex:156:[Omitted long matching line]
docs/paper/appendix.tex:181:[Omitted long matching line]
docs/paper/appendix.tex:217:Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\%) pulls the three-seed mean to 57.00\%, within the null band ($p = 0.155$).
docs/paper/appendix.tex:264:To verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate key model configurations under multiple evaluation seeds (200 episodes each). Table~\ref{tab:eval_seed_robustness} reports aggregate CAR and TSR across all tested seeds.
docs/paper/appendix.tex:295:Table~\ref{tab:eval_seed_car_detail} provides per-task CAR for the five-seed LoRA evaluation, the most complete eval-seed battery.
docs/paper/appendix.tex:372:[Omitted long matching line]
docs/paper/claim1.tex:32:The 0.1\,mm threshold reflects near-total motor inactivity (typical actions produce 1--10\,mm per step). The sharply bimodal distribution (Figure~\ref{fig:displacement}) makes $\tau_d$ robust: any threshold in $[2, 200]$\,mm yields identical dfCAR (Appendix~\ref{sec:appendix_threshold}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "d1b6d507-7ab1-4507-9edf-8937269a0ba4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/claim3.tex:26:[Omitted long matching line]\ndocs/paper/claim3.tex:59:[Omitted long matching line]\ndocs/paper/experimental_framework.tex:23:where $d_{\\max}(e)$ denotes the maximum Euclidean displacement of the end-effector across all timesteps in episode $e$. The threshold $\\tau_d = 0.1$\\,mm corresponds to sub-actuator-resolution motion. In practice, the displacement distribution is bimodal: collapsed episodes cluster below 1\\,$\\mu$m and active episodes exceed 200\\,mm, with no intermediate population. Consequently, any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering (Appendix~\\ref{sec:appendix_threshold}).\ndocs/paper/method.tex:34:The displacement distribution is sharply bimodal (collapsed episodes below 1\\,$\\mu$m, active above 200\\,mm), making $\\tau_d$ robust across $[2, 200]$\\,mm (Appendix~\\ref{sec:appendix_threshold}). For Pi0 under A1, $d_{\\max}$ uses obstacle displacement due to an inconsistent EE reference frame; Pi0.5 uses standard EE displacement.\ndocs/paper/method.tex:38:We augment LoRA-adapted~\\cite{hu2022lora} VLAs with an SDF decoder and an EE position extractor (Appendix~\\ref{sec:appendix_training}, Table~\\ref{tab:hyperparams}). The total loss is:\ndocs/paper/method.tex:46:In Pi0+A1, a parameter-name mismatch prevented LoRA loading and caused action collapse (TSR\\,=\\,0\\%; Table~\\ref{tab:configurations}). To test the upper bound of EE-only refinement (Section~\\ref{sec:ee_only}), we also replace the learned SDF with ground-truth distance fields from the simulation geometry in three oracle variants (Appendix~\\ref{sec:appendix_oracle}).\\label{sec:oracle_setup}\ndocs/paper/archive/analysis_claim1.tex:31:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:31:[Omitted long matching line]\ndocs/paper/claim2.tex:7:\\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\\ref{sec:appendix_pertask_oracle}. Oracle variants use 160 episodes (4 tasks $\\times$ 40); all other conditions use 200 episodes (4 tasks $\\times$ 50).}\ndocs/paper/claim2.tex:31:[Omitted long matching line]\ndocs/paper/appendix.tex:4:Table~\\ref{tab:multiseed_full} reports individual-seed CAR and TSR for all fine-tuned conditions at the 30K checkpoint (200 episodes each, evaluation seed\\,=\\,7). These per-seed values underlie the means reported in Table~\\ref{tab:avoidance_source}.\ndocs/paper/appendix.tex:47:To validate the robustness of our displacement threshold $\\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting.\ndocs/paper/appendix.tex:67:Table~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\ndocs/paper/appendix.tex:96:Table~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\ndocs/paper/appendix.tex:121:[Omitted long matching line]\ndocs/paper/appendix.tex:156:[Omitted long matching line]\ndocs/paper/appendix.tex:181:[Omitted long matching line]\ndocs/paper/appendix.tex:217:Table~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.155$).\ndocs/paper/appendix.tex:264:To verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate key model configurations under multiple evaluation seeds (200 episodes each). Table~\\ref{tab:eval_seed_robustness} reports aggregate CAR and TSR across all tested seeds.\ndocs/paper/appendix.tex:295:Table~\\ref{tab:eval_seed_car_detail} provides per-task CAR for the five-seed LoRA evaluation, the most complete eval-seed battery.\ndocs/paper/appendix.tex:372:[Omitted long matching line]\ndocs/paper/claim1.tex:32:The 0.1\\,mm threshold reflects near-total motor inactivity (typical actions produce 1--10\\,mm per step). The sharply bimodal distribution (Figure~\\ref{fig:displacement}) makes $\\tau_d$ robust: any threshold in $[2, 200]$\\,mm yields identical dfCAR (Appendix~\\ref{sec:appendix_threshold}).",
    "numLines": 22
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Grep · `toolu_01XKdLTSZ8uBr6D284epvYZU`</summary>

```json
{
  "pattern": "\\\\label\\{sec:appendix|\\\\label\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "a2dbe6a8-08b2-404e-9dc8-b21cb0bf7a88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0129bxbubKA9qFk3WsrzTciy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 47017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
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

_source line 34 · 2026-05-29T13:23:18.252Z_

<details><summary>↩ Tool result · `toolu_01XKdLTSZ8uBr6D284epvYZU`</summary>

```text
2:\label{sec:appendix_multiseed}
9:\label{tab:multiseed_full}
40:\label{sec:appendix_displacement}
45:\label{sec:appendix_threshold}
52:\label{tab:threshold_sensitivity}
72:\label{tab:dfcar_threshold}
94:\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
101:\label{tab:per_task_tsr}
119:\section{Per-Task CAR Breakdown}\label{sec:appendix_pertask_car}
126:\label{tab:per_task_car}
148:\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
153:\label{sec:appendix_pertask}
154:\label{sec:appendix_pertask_oracle}
163:\label{tab:oracle_pertask}
186:\label{tab:oracle_pertask_pi05}
203:\label{sec:appendix_null}
215:\label{sec:appendix_stepwise}
222:\label{tab:stepwise_lambda01}
244:\label{sec:appendix_oracle}
256:\label{sec:appendix_spatial_bowl}
262:\label{sec:appendix_eval_seed}
269:\label{tab:eval_seed_robustness}
300:\label{tab:eval_seed_car_detail}
320:\label{sec:appendix_training}
336:\label{tab:hyperparams}
370:\label{sec:appendix_tsr_collapse}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "072cef66-b521-4a5d-8375-fc73887232a1",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "2:\\label{sec:appendix_multiseed}\n9:\\label{tab:multiseed_full}\n40:\\label{sec:appendix_displacement}\n45:\\label{sec:appendix_threshold}\n52:\\label{tab:threshold_sensitivity}\n72:\\label{tab:dfcar_threshold}\n94:\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n101:\\label{tab:per_task_tsr}\n119:\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n126:\\label{tab:per_task_car}\n148:\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n153:\\label{sec:appendix_pertask}\n154:\\label{sec:appendix_pertask_oracle}\n163:\\label{tab:oracle_pertask}\n186:\\label{tab:oracle_pertask_pi05}\n203:\\label{sec:appendix_null}\n215:\\label{sec:appendix_stepwise}\n222:\\label{tab:stepwise_lambda01}\n244:\\label{sec:appendix_oracle}\n256:\\label{sec:appendix_spatial_bowl}\n262:\\label{sec:appendix_eval_seed}\n269:\\label{tab:eval_seed_robustness}\n300:\\label{tab:eval_seed_car_detail}\n320:\\label{sec:appendix_training}\n336:\\label{tab:hyperparams}\n370:\\label{sec:appendix_tsr_collapse}",
    "numLines": 26
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also verify that experimental_framework.tex is NOT included in main.tex (I already confirmed this from reading main.tex).

Let me also check: the main text claim1.tex references `Appendix~\ref{sec:appendix_threshold}` at line 32. Let me verify this in the claim1.tex content I already read. Yes: "any threshold in [2, 200] mm yields identical dfCAR (Appendix~\ref{sec:appendix_threshold})".

Now let me construct the complete report and write it.


I'm compiling the cross-reference verification across all included files, checking that each appendix reference in claim1, claim2, claim3, and method files points to valid sections in the appendix.

Now I'm identifying which appendix sections and tables aren't being referenced from the main text—there are quite a few orphaned sections like multiseed, displacement, and tsr_pertask, plus several unreferenced tables that might need to be either removed or integrated into the main narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "8c3e62c3-6421-4276-8728-41c246b53ca3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeSVRsmv3LwyGsxq7BLcBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10403,
      "cache_read_input_tokens": 47206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10403
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

_source line 36_

I have all the data. Now I'll write the completeness check report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "0a358251-ca9e-4e58-9559-009810bf64d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeSVRsmv3LwyGsxq7BLcBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10403,
      "cache_read_input_tokens": 47206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10403
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YJgcqRxcZGqtJzHjPcBj13`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "62c724b5-01ff-44f2-ab84-21a98f0d3eb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeSVRsmv3LwyGsxq7BLcBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10403,
      "cache_read_input_tokens": 47206,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10403
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

_source line 38 · 2026-05-29T13:23:30.595Z_

<details><summary>↩ Tool result · `toolu_01YJgcqRxcZGqtJzHjPcBj13`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "6ebcc6e8-3667-40c2-a172-7e6d45d43c8a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Write · `toolu_01TJjkYKNHk3heRGZ4rhAsfE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_check_report.md",
  "content": "# Supplementary Completeness Check\n\n## Cross-references\n\n### Main → Appendix (all files compiled via main.tex)\n\n| Ref in main | Source file | Label in appendix | Status |\n|---|---|---|---|\n| `\\ref{sec:appendix_threshold}` | claim1.tex:32, method.tex:34 | appendix.tex:45 | ✅ |\n| `\\ref{sec:appendix_pertask_oracle}` | claim2.tex:7, claim2.tex:30 | appendix.tex:154 | ✅ |\n| `\\ref{sec:appendix_oracle}` | claim2.tex:31, method.tex:46 | appendix.tex:244 | ✅ |\n| `\\ref{sec:appendix_null}` | claim3.tex:26, claim3.tex:59 | appendix.tex:203 | ✅ |\n| `\\ref{sec:appendix_training}` | method.tex:38 | appendix.tex:320 | ✅ |\n| `\\ref{tab:hyperparams}` | method.tex:38 | appendix.tex:336 | ✅ |\n\nAll 6 unique main→appendix references resolve correctly.\n\n### Appendix sections NOT referenced from main\n\n| Label | Section title | Severity |\n|---|---|---|\n| `sec:appendix_multiseed` | Complete Multi-Seed Results | Low — underlying data for Table 3, implicitly covered |\n| `sec:appendix_displacement` | Displacement Distribution | None — just redirects to main text Figure 3 |\n| `sec:appendix_tsr_pertask` | Per-Task TSR Breakdown | Low — useful detail, could add reference from §5 |\n| `sec:appendix_pertask_car` | Per-Task CAR Breakdown | Medium — main text claims \"per-task ordering preserved\" but doesn't cite this table |\n| `sec:appendix_ssr` | Safe Success Rate Analysis | None — redirects to main text Table 5 |\n| `sec:appendix_stepwise` | Step-wise Checkpoint Analysis | Low — supplements λ=0.1 discussion |\n| `sec:appendix_spatial_bowl` | Cross-Scene Validation | None — data already in main text Table 6 |\n| `sec:appendix_eval_seed` | Evaluation Seed Robustness | Low — standalone robustness check |\n| `sec:appendix_tsr_collapse` | TSR Collapse Mechanism | Medium — main text discusses TSR drop (claim3.tex:35) without citing this analysis |\n| `sec:appendix_pertask` | (duplicate label on Per-Task Oracle) | Note — unused alias, `sec:appendix_pertask_oracle` is the one referenced |\n\n### Appendix tables not directly `\\ref`'d from main\n\nOnly `tab:hyperparams` is directly referenced. The remaining 10 appendix tables (multiseed_full, threshold_sensitivity, dfcar_threshold, per_task_tsr, per_task_car, oracle_pertask, oracle_pertask_pi05, stepwise_lambda01, eval_seed_robustness, eval_seed_car_detail) are accessible via section-level references. This is acceptable convention.\n\n## Number Consistency\n\n### Claim 1 (Action-Collapsed Safety)\n\n| Assertion in main | Main value | Appendix value | Status |\n|---|---|---|---|\n| Pi0+A1 CAR (Table 1) | 91.5% | — (no appendix duplicate) | ✅ |\n| Pi0+A1 collapsed rate | 99.6% | — | ✅ |\n| Pi0+A1 dfCAR | ≈0% (3/732) | — | ✅ |\n| Threshold robustness [2,200] mm | \"identical dfCAR\" | tab:dfcar_threshold: all 8 configs identical across [2,200] mm | ✅ |\n| Threshold sensitivity A1-LoRA | 99.6% at 0.1mm | tab:threshold_sensitivity: 99.6% at 0.1mm | ✅ |\n\n### Claim 2 (EE-Only SDF)\n\n| Assertion in main | Main value | Appendix value | Status |\n|---|---|---|---|\n| Oracle-adaptive CAR | 75.0% | tab:oracle_pertask: (82.5+55+77.5+85)/4 = 75.0% | ✅ |\n| Oracle-fixed CAR | 73.1% | tab:oracle_pertask: (85+50+77.5+80)/4 = 73.125% | ✅ |\n| Oracle-feature CAR | 76.9% | tab:oracle_pertask: (90+47.5+82.5+87.5)/4 = 76.875% | ✅ |\n| Task 1 (choco_pudding): +9 pp | LoRA 46→Oracle-adaptive 55 | tab:oracle_pertask: 46.0→55.0 | ✅ |\n| orange_juice: LoRA 96%→Oracle 82.5% | -13.5 pp | tab:oracle_pertask: 96.0→82.5 | ✅ |\n| Pi0.5 Oracle Δ = -5.1 pp | 57.0→51.9 | tab:oracle_pertask_pi05: (50+75+70+12.5)/4 = 51.875 ≈ 51.9 | ✅ |\n\n### Claim 3 (Avoidance Source)\n\n| Assertion in main | Main value | Appendix value | Status |\n|---|---|---|---|\n| LoRA-only mean CAR | 54.83±2.25 | tab:multiseed_full: (57+52.5+55)/3 = 54.83, std=2.25 | ✅ |\n| LoRA-only mean TSR | 49.7±3.2 | tab:multiseed_full: (46+51.5+51.5)/3 = 49.67, std=3.18 | ✅ |\n| SDF λ=0.005 mean CAR | 54.5±2.29 | tab:multiseed_full: (57+54+52.5)/3 = 54.5 | ✅ |\n| SDF λ=0.01 mean CAR | 56.33±1.61 | tab:multiseed_full: (57+57.5+54.5)/3 = 56.33 | ✅ |\n| SDF λ=0.1 mean CAR | 57.00±2.18 | tab:multiseed_full: (58+58.5+54.5)/3 = 57.0 | ✅ |\n| SDF λ=0.1 seeds: 58.0, 58.5, 54.5 | claim3.tex:59 | tab:multiseed_full: s0=58.0, s1=58.5, s2=54.5 | ✅ |\n| Permutation p=0.155 (two-tailed) | claim3.tex:59 | sec:appendix_null: 13/84 ≈ 0.155 | ✅ |\n| Permutation p=0.071 (one-tailed) | — | sec:appendix_null: 6/84 ≈ 0.071 | ✅ |\n| Null pool mean=54.67, std=2.04 | — | sec:appendix_null: verified | ✅ |\n| Phase 2 ablation CAR=57.5% (18K, s2) | claim3.tex:26 | sec:appendix_null last para: 57.5% at 18K | ✅ |\n| SSR/TSR 0.39→0.51–0.60 | Table 5 | — (appendix redirects to main) | ✅ |\n| spatial_bowl: 12.0% vs 11.5% | Table 6 | sec:appendix_spatial_bowl: consistent | ✅ |\n\n### Cross-table arithmetic verification\n\n| Check | Result |\n|---|---|\n| Per-task CAR aggregates match per-seed aggregates | ✅ all verified |\n| Eval-seed robustness ranges overlap with training-seed ranges | ✅ |\n| Step-wise λ=0.1 30K values match multiseed table | ✅ s0=58.0, s1=58.5, s2=54.5 |\n\n## Content Coverage\n\n| Required content | Present | Location |\n|---|---|---|\n| Ablation detailed tables | ✅ | threshold (§A.3), per-task CAR (§A.5), per-task TSR (§A.4), step-wise (§A.9), null distribution (§A.8) |\n| Extra seed data | ✅ | per-seed results (§A.1), eval-seed robustness (§A.12) |\n| Implementation details | ✅ | architecture, training schedule, hyperparams table, eval protocol, data, compute (§A.13) |\n| Oracle variant details | ✅ | three variants described (§A.10), per-task breakdown (§A.7) |\n| Cross-scene validation | ✅ | spatial_bowl (§A.11), data also in main text |\n| TSR collapse mechanism | ✅ | §A.14 |\n| SSR analysis | ⚠️ | §A.6 is a stub redirecting to main text Table 5 — no additional analysis |\n| Displacement distribution | ⚠️ | §A.2 is a stub redirecting to main text Figure 3 — no additional analysis |\n\n## Issues Found\n\n### Must-fix\n\nNone. All cross-references resolve, all numbers are consistent.\n\n### Recommended improvements\n\n1. **Add references to unreferenced appendix sections.** Two appendix sections contain substantial analysis that the main text discusses without citing:\n   - claim3.tex \"CAR–TSR trade-off\" paragraph (line 35) should cite `Appendix~\\ref{sec:appendix_tsr_collapse}` for the mechanism analysis.\n   - claim3.tex \"per-task CAR ordering is preserved\" (line 26) should cite `Appendix~\\ref{sec:appendix_pertask_car}` for the detailed table.\n\n2. **Remove or substantiate stub sections.** `sec:appendix_displacement` (§A.2) and `sec:appendix_ssr` (§A.6) contain only one-line redirects to main text. Either add supplementary analysis or remove them to save space.\n\n3. **Remove duplicate label.** `sec:appendix_pertask` (appendix.tex:153) is defined but never referenced; only its sibling `sec:appendix_pertask_oracle` (line 154) is used. Remove the unused label to avoid confusion.\n\n4. **Unused file.** `experimental_framework.tex` is not `\\input`'d in `main.tex` — it appears to be an earlier draft of `method.tex`. Can be archived or deleted.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "7da9f2e2-743d-45ff-9c65-705ec977497d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HxHtYymzorkZXrzzeSyxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1371,
      "cache_read_input_tokens": 57609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1371
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

_source line 40 · 2026-05-29T13:24:24.141Z_

<details><summary>↩ Tool result · `toolu_01TJjkYKNHk3heRGZ4rhAsfE`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_check_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "292455d1-28b5-4a1a-9bf0-45d02e4dce98",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_check_report.md",
    "content": "# Supplementary Completeness Check\n\n## Cross-references\n\n### Main → Appendix (all files compiled via main.tex)\n\n| Ref in main | Source file | Label in appendix | Status |\n|---|---|---|---|\n| `\\ref{sec:appendix_threshold}` | claim1.tex:32, method.tex:34 | appendix.tex:45 | ✅ |\n| `\\ref{sec:appendix_pertask_oracle}` | claim2.tex:7, claim2.tex:30 | appendix.tex:154 | ✅ |\n| `\\ref{sec:appendix_oracle}` | claim2.tex:31, method.tex:46 | appendix.tex:244 | ✅ |\n| `\\ref{sec:appendix_null}` | claim3.tex:26, claim3.tex:59 | appendix.tex:203 | ✅ |\n| `\\ref{sec:appendix_training}` | method.tex:38 | appendix.tex:320 | ✅ |\n| `\\ref{tab:hyperparams}` | method.tex:38 | appendix.tex:336 | ✅ |\n\nAll 6 unique main→appendix references resolve correctly.\n\n### Appendix sections NOT referenced from main\n\n| Label | Section title | Severity |\n|---|---|---|\n| `sec:appendix_multiseed` | Complete Multi-Seed Results | Low — underlying data for Table 3, implicitly covered |\n| `sec:appendix_displacement` | Displacement Distribution | None — just redirects to main text Figure 3 |\n| `sec:appendix_tsr_pertask` | Per-Task TSR Breakdown | Low — useful detail, could add reference from §5 |\n| `sec:appendix_pertask_car` | Per-Task CAR Breakdown | Medium — main text claims \"per-task ordering preserved\" but doesn't cite this table |\n| `sec:appendix_ssr` | Safe Success Rate Analysis | None — redirects to main text Table 5 |\n| `sec:appendix_stepwise` | Step-wise Checkpoint Analysis | Low — supplements λ=0.1 discussion |\n| `sec:appendix_spatial_bowl` | Cross-Scene Validation | None — data already in main text Table 6 |\n| `sec:appendix_eval_seed` | Evaluation Seed Robustness | Low — standalone robustness check |\n| `sec:appendix_tsr_collapse` | TSR Collapse Mechanism | Medium — main text discusses TSR drop (claim3.tex:35) without citing this analysis |\n| `sec:appendix_pertask` | (duplicate label on Per-Task Oracle) | Note — unused alias, `sec:appendix_pertask_oracle` is the one referenced |\n\n### Appendix tables not directly `\\ref`'d from main\n\nOnly `tab:hyperparams` is directly referenced. The remaining 10 appendix tables (multiseed_full, threshold_sensitivity, dfcar_threshold, per_task_tsr, per_task_car, oracle_pertask, oracle_pertask_pi05, stepwise_lambda01, eval_seed_robustness, eval_seed_car_detail) are accessible via section-level references. This is acceptable convention.\n\n## Number Consistency\n\n### Claim 1 (Action-Collapsed Safety)\n\n| Assertion in main | Main value | Appendix value | Status |\n|---|---|---|---|\n| Pi0+A1 CAR (Table 1) | 91.5% | — (no appendix duplicate) | ✅ |\n| Pi0+A1 collapsed rate | 99.6% | — | ✅ |\n| Pi0+A1 dfCAR | ≈0% (3/732) | — | ✅ |\n| Threshold robustness [2,200] mm | \"identical dfCAR\" | tab:dfcar_threshold: all 8 configs identical across [2,200] mm | ✅ |\n| Threshold sensitivity A1-LoRA | 99.6% at 0.1mm | tab:threshold_sensitivity: 99.6% at 0.1mm | ✅ |\n\n### Claim 2 (EE-Only SDF)\n\n| Assertion in main | Main value | Appendix value | Status |\n|---|---|---|---|\n| Oracle-adaptive CAR | 75.0% | tab:oracle_pertask: (82.5+55+77.5+85)/4 = 75.0% | ✅ |\n| Oracle-fixed CAR | 73.1% | tab:oracle_pertask: (85+50+77.5+80)/4 = 73.125% | ✅ |\n| Oracle-feature CAR | 76.9% | tab:oracle_pertask: (90+47.5+82.5+87.5)/4 = 76.875% | ✅ |\n| Task 1 (choco_pudding): +9 pp | LoRA 46→Oracle-adaptive 55 | tab:oracle_pertask: 46.0→55.0 | ✅ |\n| orange_juice: LoRA 96%→Oracle 82.5% | -13.5 pp | tab:oracle_pertask: 96.0→82.5 | ✅ |\n| Pi0.5 Oracle Δ = -5.1 pp | 57.0→51.9 | tab:oracle_pertask_pi05: (50+75+70+12.5)/4 = 51.875 ≈ 51.9 | ✅ |\n\n### Claim 3 (Avoidance Source)\n\n| Assertion in main | Main value | Appendix value | Status |\n|---|---|---|---|\n| LoRA-only mean CAR | 54.83±2.25 | tab:multiseed_full: (57+52.5+55)/3 = 54.83, std=2.25 | ✅ |\n| LoRA-only mean TSR | 49.7±3.2 | tab:multiseed_full: (46+51.5+51.5)/3 = 49.67, std=3.18 | ✅ |\n| SDF λ=0.005 mean CAR | 54.5±2.29 | tab:multiseed_full: (57+54+52.5)/3 = 54.5 | ✅ |\n| SDF λ=0.01 mean CAR | 56.33±1.61 | tab:multiseed_full: (57+57.5+54.5)/3 = 56.33 | ✅ |\n| SDF λ=0.1 mean CAR | 57.00±2.18 | tab:multiseed_full: (58+58.5+54.5)/3 = 57.0 | ✅ |\n| SDF λ=0.1 seeds: 58.0, 58.5, 54.5 | claim3.tex:59 | tab:multiseed_full: s0=58.0, s1=58.5, s2=54.5 | ✅ |\n| Permutation p=0.155 (two-tailed) | claim3.tex:59 | sec:appendix_null: 13/84 ≈ 0.155 | ✅ |\n| Permutation p=0.071 (one-tailed) | — | sec:appendix_null: 6/84 ≈ 0.071 | ✅ |\n| Null pool mean=54.67, std=2.04 | — | sec:appendix_null: verified | ✅ |\n| Phase 2 ablation CAR=57.5% (18K, s2) | claim3.tex:26 | sec:appendix_null last para: 57.5% at 18K | ✅ |\n| SSR/TSR 0.39→0.51–0.60 | Table 5 | — (appendix redirects to main) | ✅ |\n| spatial_bowl: 12.0% vs 11.5% | Table 6 | sec:appendix_spatial_bowl: consistent | ✅ |\n\n### Cross-table arithmetic verification\n\n| Check | Result |\n|---|---|\n| Per-task CAR aggregates match per-seed aggregates | ✅ all verified |\n| Eval-seed robustness ranges overlap with training-seed ranges | ✅ |\n| Step-wise λ=0.1 30K values match multiseed table | ✅ s0=58.0, s1=58.5, s2=54.5 |\n\n## Content Coverage\n\n| Required content | Present | Location |\n|---|---|---|\n| Ablation detailed tables | ✅ | threshold (§A.3), per-task CAR (§A.5), per-task TSR (§A.4), step-wise (§A.9), null distribution (§A.8) |\n| Extra seed data | ✅ | per-seed results (§A.1), eval-seed robustness (§A.12) |\n| Implementation details | ✅ | architecture, training schedule, hyperparams table, eval protocol, data, compute (§A.13) |\n| Oracle variant details | ✅ | three variants described (§A.10), per-task breakdown (§A.7) |\n| Cross-scene validation | ✅ | spatial_bowl (§A.11), data also in main text |\n| TSR collapse mechanism | ✅ | §A.14 |\n| SSR analysis | ⚠️ | §A.6 is a stub redirecting to main text Table 5 — no additional analysis |\n| Displacement distribution | ⚠️ | §A.2 is a stub redirecting to main text Figure 3 — no additional analysis |\n\n## Issues Found\n\n### Must-fix\n\nNone. All cross-references resolve, all numbers are consistent.\n\n### Recommended improvements\n\n1. **Add references to unreferenced appendix sections.** Two appendix sections contain substantial analysis that the main text discusses without citing:\n   - claim3.tex \"CAR–TSR trade-off\" paragraph (line 35) should cite `Appendix~\\ref{sec:appendix_tsr_collapse}` for the mechanism analysis.\n   - claim3.tex \"per-task CAR ordering is preserved\" (line 26) should cite `Appendix~\\ref{sec:appendix_pertask_car}` for the detailed table.\n\n2. **Remove or substantiate stub sections.** `sec:appendix_displacement` (§A.2) and `sec:appendix_ssr` (§A.6) contain only one-line redirects to main text. Either add supplementary analysis or remove them to save space.\n\n3. **Remove duplicate label.** `sec:appendix_pertask` (appendix.tex:153) is defined but never referenced; only its sibling `sec:appendix_pertask_oracle` (line 154) is used. Remove the unused label to avoid confusion.\n\n4. **Unused file.** `experimental_framework.tex` is not `\\input`'d in `main.tex` — it appears to be an earlier draft of `method.tex`. Can be archived or deleted.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01KaN8r7xmWXUfT4XntLQkwc`</summary>

```json
{
  "name": "supplementary_check_report",
  "type": "report",
  "description": "Supplementary completeness check: cross-references, number consistency, content coverage for appendix.tex",
  "project": "diff_collision_sdf",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_check_report.md",
  "tags": [
    "paper",
    "supplementary",
    "quality-check"
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
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "621fa115-5a8c-4a55-bcaf-5a33b87fe4b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQephG2tY5XyqJqPSEdAmS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2941,
      "cache_read_input_tokens": 58980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2941
      },
      "output_tokens": 68,
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

_source line 42 · 2026-05-29T13:24:29.246Z_

<details><summary>↩ Tool result · `toolu_01KaN8r7xmWXUfT4XntLQkwc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260529_9cf7ac\", \"name\": \"supplementary_check_report\", \"type\": \"report\", \"description\": \"Supplementary completeness check: cross-references, number consistency, content coverage for appendix.tex\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/report/supplementary_check_report.md\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-29T13:24:29.036176+00:00\", \"tags\": [\"paper\", \"supplementary\", \"quality-check\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "8b78d800-34dc-4610-93a0-25f0306a9a93",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260529_9cf7ac\\\", \\\"name\\\": \\\"supplementary_check_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Supplementary completeness check: cross-references, number consistency, content coverage for appendix.tex\\\", \\\"path\\\": \\\"projects/diff_collision_sdf/artifacts/_project/report/supplementary_check_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"diff_collision_sdf\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-29T13:24:29.036176+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"supplementary\\\", \\\"quality-check\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260529_9cf7ac\", \"name\": \"supplementary_check_report\", \"type\": \"report\", \"description\": \"Supplementary completeness check: cross-references, number consistency, content coverage for appendix.tex\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/report/supplementary_check_report.md\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-29T13:24:29.036176+00:00\", \"tags\": [\"paper\", \"supplementary\", \"quality-check\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

检查完成。结果总结：

**交叉引用**：主论文 6 个指向附录的 `\ref{}` 全部正确解析，无悬空引用。

**数字一致性**：全部一致。逐项验证了 Claim 1-3 中所有关键数值（CAR/TSR/dfCAR 均值、标准差、per-seed 值、置换检验 p 值、per-task 聚合计算），appendix 表格的算术均与主论文吻合。

**内容覆盖**：ablation 详表、多 seed 数据、实现细节、oracle 变体说明均齐全。两个 stub section（displacement §A.2、SSR §A.6）只有一行重定向到主论文，无额外分析。

**建议改进**（非必须）：
1. claim3.tex 讨论 TSR 下降和 per-task CAR 排序时应分别引用 `sec:appendix_tsr_collapse` 和 `sec:appendix_pertask_car`
2. 去掉或充实两个 stub section
3. 删除未使用的 `sec:appendix_pertask` 重复 label
4. `experimental_framework.tex` 未被 main.tex 引入，可归档

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "uuid": "280dd819-52b7-491a-a863-7ed4606af06c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016oMXLmFMXd96j1eYSq7WSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 61921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 492
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

_source line 44_

检查完成。结果总结：

**交叉引用**：主论文 6 个指向附录的 `\ref{}` 全部正确解析，无悬空引用。

**数字一致性**：全部一致。逐项验证了 Claim 1-3 中所有关键数值（CAR/TSR/dfCAR 均值、标准差、per-seed 值、置换检验 p 值、per-task 聚合计算），appendix 表格的算术均与主论文吻合。

**内容覆盖**：ablation 详表、多 seed 数据、实现细节、oracle 变体说明均齐全。两个 stub section（displacement §A.2、SSR §A.6）只有一行重定向到主论文，无额外分析。

**建议改进**（非必须）：
1. claim3.tex 讨论 TSR 下降和 per-task CAR 排序时应分别引用 `sec:appendix_tsr_collapse` 和 `sec:appendix_pertask_car`
2. 去掉或充实两个 stub section
3. 删除未使用的 `sec:appendix_pertask` 重复 label
4. `experimental_framework.tex` 未被 main.tex 引入，可归档

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 232836,
  "duration_api_ms": 234136,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "50291c29-b889-4939-a4a8-b9be7d43be1e",
  "total_cost_usd": 0.8130445000000001,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 50962,
    "cache_read_input_tokens": 307964,
    "output_tokens": 13554,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 50962,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 362,
        "cache_read_input_tokens": 61921,
        "cache_creation_input_tokens": 492,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 492
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1575,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001645,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 13554,
      "cacheReadInputTokens": 307964,
      "cacheCreationInputTokens": 50962,
      "webSearchRequests": 0,
      "costUSD": 0.8113995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "43eeaac5-d207-46e6-806e-6d83c8a9128e"
}
```

</details>

---
