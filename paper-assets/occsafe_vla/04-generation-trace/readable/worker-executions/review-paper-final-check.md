# review paper final check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_review_paper-final-check_20260528T094530.log`
- **Structured JSON:** [`d62dd1912b2fc0d560a5.json`](../../sessions/d6/d62dd1912b2fc0d560a5.json)

## Before a recorded user message

65 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
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
  "uuid": "8794c6b6-7f9f-483f-8358-9fec8b8fc24b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
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
    "resetsAt": 1779976200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b248d5cb-53b3-4dbb-af98-cb247ddfb0ab",
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the paper files and running the compilation check in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "e3e45a8f-4de8-483d-8331-817143191486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

开始论文最终检查。先并行读取所有 tex 文件和运行编译。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "215388de-6fb3-4dfb-bcfa-22739ce9d812",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — Read · `toolu_01HiB2QSuREZM4VV56Md49VW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "0362ae36-eb99-4389-92e1-102bb6b510fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 7 · 2026-05-28T09:45:43.268Z_

<details><summary>↩ Tool result · `toolu_01HiB2QSuREZM4VV56Md49VW`</summary>

```text
1	% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models
2	% Target: CoRL 2026
3	\documentclass{article}
4	
5	\usepackage[dvipsnames]{xcolor}
6	\usepackage{corl_2026}
7	
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{subcaption}
13	\usepackage{placeins}
14	
15	\title{Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\\ An Empirical Investigation}
16	
17	\author{
18	Anonymous Author(s)
19	}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates lagging task completion on safety-critical benchmarks.
26	We present a factorial study of twelve conditions varying five factors (gradient flow, label content, normalization type, spatial reference frame, and temporal extent) to isolate how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.
27	Our central finding is a \textbf{normalization-dependent gradient flow effect}. Under Batch Normalization (BN), gradient flow degrades safety: Full OCC BN achieves a 0.725 Collision Avoidance Rate versus 0.767 for Detach BN (Cohen's $d = -0.93$, large), falling below the no-auxiliary-head Vanilla baseline (0.745). Under Layer Normalization (LN), gradient flow is benign: Full OCC LN reaches 0.773, above Vanilla (Cohen's $d = +1.07$, large). Two main effects drive this pattern: (1)~gradient flow under BN reduces CAR by 4.2\,pp ($d{=}0.93$), with BN + gradient flow as the sole configuration falling below the Vanilla baseline; (2)~LN provides a consistent 3.5--4.8\,pp safety advantage over BN ($d{\approx}1.05$--$1.47$, large to very large), regardless of gradient flow. A $2{\times}2$ ANOVA confirms additive main effects with negligible interaction ($\eta^2{<}0.01$). The BN + gradient flow cell is both the worst-performing and most unstable configuration ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all other cells). Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) shows no detectable effect on safety (observed under v1 codebase); the gradient pathway, not the spatial information, determines the outcome. Normalization choice is equally consequential: LayerNorm consistently provides a safety advantage over BatchNorm regardless of gradient flow configuration.
28	We hypothesize that this normalization dependence arises from BN's running statistics: auxiliary gradients may shift batch-level statistics in the shared encoder, a coupling absent in LN's per-token computation. Practical guidelines: detach auxiliary gradients under BN architectures; gradient flow is safe under LN; avoid combining BN with gradient flow.
29	\end{abstract}
30	
31	\keywords{Vision-Language-Action Models, Robot Safety, Auxiliary Supervision, Collision Avoidance}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{method}
38	
39	\input{results}
40	
41	\input{discussion}
42	
43	\input{conclusion}
44	
45	\FloatBarrier
46	\bibliography{references}
47	
48	\clearpage
49	\appendix
50	\input{appendix}
51	
52	\end{document}
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "327943f8-2f47-459d-9c8a-db622afcd00c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
      "content": "% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models\n% Target: CoRL 2026\n\\documentclass{article}\n\n\\usepackage[dvipsnames]{xcolor}\n\\usepackage{corl_2026}\n\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{placeins}\n\n\\title{Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer?\\\\ An Empirical Investigation}\n\n\\author{\nAnonymous Author(s)\n}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nFine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates lagging task completion on safety-critical benchmarks.\nWe present a factorial study of twelve conditions varying five factors (gradient flow, label content, normalization type, spatial reference frame, and temporal extent) to isolate how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.\nOur central finding is a \\textbf{normalization-dependent gradient flow effect}. Under Batch Normalization (BN), gradient flow degrades safety: Full OCC BN achieves a 0.725 Collision Avoidance Rate versus 0.767 for Detach BN (Cohen's $d = -0.93$, large), falling below the no-auxiliary-head Vanilla baseline (0.745). Under Layer Normalization (LN), gradient flow is benign: Full OCC LN reaches 0.773, above Vanilla (Cohen's $d = +1.07$, large). Two main effects drive this pattern: (1)~gradient flow under BN reduces CAR by 4.2\\,pp ($d{=}0.93$), with BN + gradient flow as the sole configuration falling below the Vanilla baseline; (2)~LN provides a consistent 3.5--4.8\\,pp safety advantage over BN ($d{\\approx}1.05$--$1.47$, large to very large), regardless of gradient flow. A $2{\\times}2$ ANOVA confirms additive main effects with negligible interaction ($\\eta^2{<}0.01$). The BN + gradient flow cell is both the worst-performing and most unstable configuration ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all other cells). Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) shows no detectable effect on safety (observed under v1 codebase); the gradient pathway, not the spatial information, determines the outcome. Normalization choice is equally consequential: LayerNorm consistently provides a safety advantage over BatchNorm regardless of gradient flow configuration.\nWe hypothesize that this normalization dependence arises from BN's running statistics: auxiliary gradients may shift batch-level statistics in the shared encoder, a coupling absent in LN's per-token computation. Practical guidelines: detach auxiliary gradients under BN architectures; gradient flow is safe under LN; avoid combining BN with gradient flow.\n\\end{abstract}\n\n\\keywords{Vision-Language-Action Models, Robot Safety, Auxiliary Supervision, Collision Avoidance}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{results}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\FloatBarrier\n\\bibliography{references}\n\n\\clearpage\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01X6kJvqFgR1KXsgwwj2rrt8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "6b5efc6f-a715-48b7-84d0-38a4d945e9e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 9 · 2026-05-28T09:45:43.748Z_

<details><summary>↩ Tool result · `toolu_01X6kJvqFgR1KXsgwwj2rrt8`</summary>

```text
1	\section{Introduction}
2	
3	Vision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\cite{kim2025oft} reaches a Task Success Rate (TSR) of 87.8\% but a Collision Avoidance Rate (CAR) of only 74.5\%. On the three most constrained tasks, collision rates reach 43--93\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.
4	
5	Two active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety method examines whether spatial representations contribute to or detract from safe behavior. A recent survey~\cite{li2026vlasafety} confirms that the relationship between auxiliary spatial supervision and collision safety remains an open question. Moreover, single-factor ablations (the dominant methodology in prior spatial VLA studies) cannot detect interactions between design choices. If gradient flow and normalization type interact in their effect on collision avoidance, a study that varies only one factor will attribute the joint effect to whichever factor it happens to test.
6	
7	\begin{figure}[!htb]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
10	\caption{\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \textbf{(a)}~Training setup: OpenVLA-7B with dual vision encoders (DINOv2 + SigLIP) and an auxiliary spatial head (BEV occupancy or depth), discarded at inference. \textbf{(b)}~$2{\times}2$ factorial crossing gradient flow (ON/OFF) and normalization (BN/LN), plus 8 additional conditions spanning 5 factors. \textbf{(c)}~Key result: under BatchNorm, gradient flow degrades CAR below the Vanilla baseline (0.725 vs.\ 0.745), while detach recovers it (0.767); under LayerNorm, gradient flow is benign (0.773 $>$ Vanilla) and detach further improves CAR ($0.802{\pm}0.024$, $n{=}3$). Only the BN + gradient flow combination falls below Vanilla. Error bars: cross-seed SD.}
11	\label{fig:overview}
12	\end{figure}
13	
14	Before spatial heads are added to deployed VLAs under the assumption of safety benefits, the validity of this assumption requires careful examination. We ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft} and LoRA~\cite{hu2022lora} adaptation. Twelve experimental conditions vary five factors: gradient flow from the auxiliary head into the vision encoders, spatial label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of supervision (Figure~\ref{fig:overview}). As argued above, single-factor designs cannot detect such interactions. Our $2{\times}2$ factorial subset (gradient flow $\times$ normalization) is the minimal design that can detect and quantify them, and effect sizes suggest combined effects that prior work could not have found.
15	
16	The central finding is a \textbf{normalization-dependent gradient flow effect: under BatchNorm, gradient flow is associated with degraded collision avoidance (Cohen's $d{=}-0.93$, large), while under LayerNorm, gradient flow is benign (Cohen's $d{=}+1.07$ vs.\ Vanilla).} A $2{\times}2$ factorial reveals two large main effects: gradient flow under BN reduces CAR by 4.2\,pp, and LN provides a 3.5--4.8\,pp safety advantage over BN ($d{\approx}1.03$, large). Only the BN + gradient flow combination falls below the Vanilla baseline, a practical threshold that underscores when auxiliary heads become harmful. Spatial label content showed no detectable effect on outcomes (\S\ref{sec:results}).
17	
18	Our contributions are:
19	\begin{enumerate}[nosep,leftmargin=*]
20	    \item \textbf{Normalization-dependent gradient flow effect.} A $2{\times}2$ factorial (gradient flow $\times$ normalization) reveals two large main effects: under BatchNorm, gradient flow degrades collision avoidance (Cell~1 $<$ Vanilla, Cohen's $d{=}-0.93$, large) and increases training variability ($\sigma{=}0.064$); under LayerNorm, gradient flow is benign (Cell~2 $>$ Vanilla, Cohen's $d{=}+1.07$, large). LN provides a consistent 3.5--4.8\,pp safety advantage over BN ($d{\approx}1.03$, large). Only the BN + gradient flow combination falls below the Vanilla baseline and exhibits the highest instability. Spatial label content showed no detectable effect on outcomes under the conditions tested (\S\ref{sec:results}, Table~\ref{tab:main_results}, Figure~\ref{fig:factorial}).
21	
22	    \item \textbf{Factorial methodology for VLA auxiliary heads.} We introduce the first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning. This design can detect combined effects that single-factor ablations would miss (\S\ref{sec:ablation}, Table~\ref{tab:ablation_design}).
23	
24	    \item \textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads with gradient flow under BatchNorm architectures. If an auxiliary head is required by other objectives, use detached gradients with LayerNorm (Detach+LN), which normalizes per-token without running statistics, avoiding the distributional coupling that makes BatchNorm sensitive to gradient flow. Avoid combining BatchNorm with gradient flow. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\S\ref{sec:discussion}).
25	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "c53b69aa-f38f-4235-b485-514eb5bdc74b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\\cite{kim2025oft} reaches a Task Success Rate (TSR) of 87.8\\% but a Collision Avoidance Rate (CAR) of only 74.5\\%. On the three most constrained tasks, collision rates reach 43--93\\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.\n\nTwo active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety method examines whether spatial representations contribute to or detract from safe behavior. A recent survey~\\cite{li2026vlasafety} confirms that the relationship between auxiliary spatial supervision and collision safety remains an open question. Moreover, single-factor ablations (the dominant methodology in prior spatial VLA studies) cannot detect interactions between design choices. If gradient flow and normalization type interact in their effect on collision avoidance, a study that varies only one factor will attribute the joint effect to whichever factor it happens to test.\n\n\\begin{figure}[!htb]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_overview.pdf}\n\\caption{\\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \\textbf{(a)}~Training setup: OpenVLA-7B with dual vision encoders (DINOv2 + SigLIP) and an auxiliary spatial head (BEV occupancy or depth), discarded at inference. \\textbf{(b)}~$2{\\times}2$ factorial crossing gradient flow (ON/OFF) and normalization (BN/LN), plus 8 additional conditions spanning 5 factors. \\textbf{(c)}~Key result: under BatchNorm, gradient flow degrades CAR below the Vanilla baseline (0.725 vs.\\ 0.745), while detach recovers it (0.767); under LayerNorm, gradient flow is benign (0.773 $>$ Vanilla) and detach further improves CAR ($0.802{\\pm}0.024$, $n{=}3$). Only the BN + gradient flow combination falls below Vanilla. Error bars: cross-seed SD.}\n\\label{fig:overview}\n\\end{figure}\n\nBefore spatial heads are added to deployed VLAs under the assumption of safety benefits, the validity of this assumption requires careful examination. We ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with the OFT recipe~\\cite{kim2025oft} and LoRA~\\cite{hu2022lora} adaptation. Twelve experimental conditions vary five factors: gradient flow from the auxiliary head into the vision encoders, spatial label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of supervision (Figure~\\ref{fig:overview}). As argued above, single-factor designs cannot detect such interactions. Our $2{\\times}2$ factorial subset (gradient flow $\\times$ normalization) is the minimal design that can detect and quantify them, and effect sizes suggest combined effects that prior work could not have found.\n\nThe central finding is a \\textbf{normalization-dependent gradient flow effect: under BatchNorm, gradient flow is associated with degraded collision avoidance (Cohen's $d{=}-0.93$, large), while under LayerNorm, gradient flow is benign (Cohen's $d{=}+1.07$ vs.\\ Vanilla).} A $2{\\times}2$ factorial reveals two large main effects: gradient flow under BN reduces CAR by 4.2\\,pp, and LN provides a 3.5--4.8\\,pp safety advantage over BN ($d{\\approx}1.03$, large). Only the BN + gradient flow combination falls below the Vanilla baseline, a practical threshold that underscores when auxiliary heads become harmful. Spatial label content showed no detectable effect on outcomes (\\S\\ref{sec:results}).\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Normalization-dependent gradient flow effect.} A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals two large main effects: under BatchNorm, gradient flow degrades collision avoidance (Cell~1 $<$ Vanilla, Cohen's $d{=}-0.93$, large) and increases training variability ($\\sigma{=}0.064$); under LayerNorm, gradient flow is benign (Cell~2 $>$ Vanilla, Cohen's $d{=}+1.07$, large). LN provides a consistent 3.5--4.8\\,pp safety advantage over BN ($d{\\approx}1.03$, large). Only the BN + gradient flow combination falls below the Vanilla baseline and exhibits the highest instability. Spatial label content showed no detectable effect on outcomes under the conditions tested (\\S\\ref{sec:results}, Table~\\ref{tab:main_results}, Figure~\\ref{fig:factorial}).\n\n    \\item \\textbf{Factorial methodology for VLA auxiliary heads.} We introduce the first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning. This design can detect combined effects that single-factor ablations would miss (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).\n\n    \\item \\textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads with gradient flow under BatchNorm architectures. If an auxiliary head is required by other objectives, use detached gradients with LayerNorm (Detach+LN), which normalizes per-token without running statistics, avoiding the distributional coupling that makes BatchNorm sensitive to gradient flow. Avoid combining BatchNorm with gradient flow. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\\S\\ref{sec:discussion}).\n\\end{enumerate}",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_019tzXTtFRdAe7PZpvRCQtAW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "b5b52b20-8358-4ab1-b8e5-a0b1587a72ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 11 · 2026-05-28T09:45:44.231Z_

<details><summary>↩ Tool result · `toolu_019tzXTtFRdAe7PZpvRCQtAW`</summary>

```text
1	
2	\section{Method}
3	
4	We fine-tune OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft}, which concatenates DINOv2~\cite{oquab2024dinov2} (1024-d) and SigLIP~\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\cite{hu2022lora} (rank 32, $\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:
5	\begin{equation}
6	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda(t) \cdot \mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*),
7	\quad \lambda(t) = 0.01 \cdot \exp(-t / 50000)
8	\end{equation}
9	where $h$ denotes the auxiliary head, $\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.
10	
11	\textbf{BEV occupancy head.} The head (1.2M parameters) maps the 256 patch tokens from the current observation frame to a $64{\times}64$ binary occupancy grid. A linear projection ($2176{\to}256$) is reshaped to $16{\times}16$, followed by two transposed convolutions ($256{\to}128{\to}64$, kernel 4, stride 2) each with BatchNorm2d and GELU, and a final $1{\times}1$ convolution with sigmoid activation. Ground-truth grids are rendered from MuJoCo simulator state replay by projecting object bounding boxes onto the table-plane BEV. Training uses focal loss~\cite{lin2017focal} ($\alpha{=}0.25$, $\gamma{=}2.0$) to handle class imbalance in the sparse occupancy signal. The initial auxiliary weight $\lambda_0{=}0.01$ is set to keep auxiliary gradients below 2\% of the action loss magnitude, avoiding interference with action learning.
12	
13	\textbf{Monocular depth head.} This head shares the same convolutional architecture but replaces the sigmoid with ReLU and uses smooth-L1 loss. Ground-truth egocentric depth maps are rendered at $64{\times}64$ resolution from MuJoCo. The depth head provides an egocentric spatial reference frame, complementing the allocentric BEV occupancy grid.
14	
15	\subsection{Ablation Design}
16	\label{sec:ablation}
17	
18	We evaluate twelve conditions that systematically vary five factors: gradient flow from the auxiliary head into the vision encoders, label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of auxiliary supervision.
19	
20	The $2{\times}2$ factorial core crosses gradient flow (ON/OFF) with normalization (BN/LN): \textbf{Vanilla} (no auxiliary head), \textbf{Full OCC} (BEV occupancy, gradient flow, BatchNorm), \textbf{Detach OCC} (gradients blocked via \texttt{stop\_gradient}), and their LN variants (\textbf{Full OCC+LN}, \textbf{Detach+LN}). Seven supplementary conditions probe label content (\textbf{Random OCC}), reference frame (\textbf{Depth}), and temporal extent (\textbf{Cutoff@\{15K--45K\}}, \textbf{Reverse Cutoff}; details in Appendix~\ref{app:training}). Table~\ref{tab:ablation_design} summarizes all twelve conditions and nine pairwise comparisons.
21	
22	Formally, let $\text{sg}(\cdot)$ denote the stop-gradient operator. Full conditions compute $\mathcal{L}_\text{aux}(h(\phi_v(o_t)), s_t^*)$, so auxiliary gradients flow back through $\phi_v$. Detach conditions compute $\mathcal{L}_\text{aux}(h(\text{sg}(\phi_v(o_t))), s_t^*)$: the head $h$ trains on encoder features, but no gradient reaches $\phi_v$. This distinction separates bidirectional coupling (spatial and action objectives jointly shape encoder representations) from unidirectional readout (the head reads encoder features but does not influence encoder weight updates).
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\setlength{\tabcolsep}{4pt}
28	\caption{Ablation design: each comparison isolates one factor.}
29	\label{tab:ablation_design}
30	\begin{tabular}{@{}ll@{}}
31	\toprule
32	Comparison & Isolated Factor \\
33	\midrule
34	Full OCC vs.\ Vanilla & Auxiliary spatial supervision \\
35	Random vs.\ Full OCC & Spatial content vs.\ gradient flow \\
36	Detach vs.\ Vanilla & Encoder gradient flow (presence/absence) \\
37	Detach+LN vs.\ Detach OCC & Normalization (BN vs.\ LN) without gradient flow \\
38	Full OCC+LN vs.\ Full OCC & Normalization (BN vs.\ LN) with gradient flow \\
39	$2{\times}2$ factorial & Normalization $\times$ gradient flow combined effects \\
40	Depth vs.\ Full OCC & Egocentric vs.\ allocentric frame \\
41	Cutoff@\{15K--45K\} vs.\ Full OCC & Temporal extent of gradient flow \\
42	Reverse Cutoff vs.\ Cutoff@35K & Early vs.\ late gradient flow \\
43	\bottomrule
44	\end{tabular}
45	\end{table}
46	
47	\subsection{Evaluation}
48	
49	We evaluate on SafeLIBERO Level~I~\cite{hu2025vlsa}, which places obstacles in close proximity to manipulation targets across 10 tabletop tasks drawn from LIBERO-Spatial~\cite{liu2023libero}. We report two metrics: \textbf{Task Success Rate (TSR)}, the fraction of episodes in which the task is completed, and \textbf{Collision Avoidance Rate (CAR)}, where a collision is registered when the L1 displacement of any obstacle \texttt{body\_xpos} exceeds $10^{-3}$. The five core factorial conditions (Vanilla, Full OCC, Full OCC+LN, Detach OCC, Detach+LN), along with Random OCC, Depth, and Cutoff@35K, each use 1--4 independent seeds; remaining temporal conditions (Cutoff@\{15K, 25K, 45K\}, Reverse Cutoff) use 1--2 seeds as noted in Table~\ref{tab:main_results}. Each seed runs 50 rollouts per task (500 episodes per seed).
50	
51	The BN factorial cells (Full OCC and Detach OCC) have been fully retrained under a revised codebase (v2, 3--4 seeds each); among the LN cells, Full OCC+LN uses v2 ($n{=}4$) and Detach+LN uses v2 ($n{=}3$). Both codebase versions share identical architectures, hyperparameters, and evaluation protocols. Supplementary conditions use the original codebase (v1). Bootstrap 95\% CIs use 10{,}000 hierarchical resamples (percentile method). Training runs for 50K steps on a single NVIDIA RTX PRO 6000 GPU; full details are in Appendix~\ref{app:training}.
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "e179ad6f-f70e-4e3a-99d6-32f31301692f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/method.tex",
      "content": "\n\\section{Method}\n\nWe fine-tune OpenVLA-7B~\\cite{kim2024openvla} with the OFT recipe~\\cite{kim2025oft}, which concatenates DINOv2~\\cite{oquab2024dinov2} (1024-d) and SigLIP~\\cite{zhai2023siglip} (1152-d) patch features into a 2176-dimensional representation per spatial token. We apply LoRA~\\cite{hu2022lora} (rank 32, $\\alpha{=}16$) and augment the action prediction loss with an auxiliary spatial prediction head:\n\\begin{equation}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda(t) \\cdot \\mathcal{L}_\\text{aux}(h(\\phi_v(o_t)), s_t^*),\n\\quad \\lambda(t) = 0.01 \\cdot \\exp(-t / 50000)\n\\end{equation}\nwhere $h$ denotes the auxiliary head, $\\phi_v$ the frozen-then-LoRA-adapted vision encoders, and $s_t^*$ the ground-truth spatial label at step $t$. The coefficient $\\lambda(t)$ decays exponentially so that spatial gradients shape early representations without dominating late-stage action refinement. The auxiliary head is discarded at inference, incurring zero additional cost.\n\n\\textbf{BEV occupancy head.} The head (1.2M parameters) maps the 256 patch tokens from the current observation frame to a $64{\\times}64$ binary occupancy grid. A linear projection ($2176{\\to}256$) is reshaped to $16{\\times}16$, followed by two transposed convolutions ($256{\\to}128{\\to}64$, kernel 4, stride 2) each with BatchNorm2d and GELU, and a final $1{\\times}1$ convolution with sigmoid activation. Ground-truth grids are rendered from MuJoCo simulator state replay by projecting object bounding boxes onto the table-plane BEV. Training uses focal loss~\\cite{lin2017focal} ($\\alpha{=}0.25$, $\\gamma{=}2.0$) to handle class imbalance in the sparse occupancy signal. The initial auxiliary weight $\\lambda_0{=}0.01$ is set to keep auxiliary gradients below 2\\% of the action loss magnitude, avoiding interference with action learning.\n\n\\textbf{Monocular depth head.} This head shares the same convolutional architecture but replaces the sigmoid with ReLU and uses smooth-L1 loss. Ground-truth egocentric depth maps are rendered at $64{\\times}64$ resolution from MuJoCo. The depth head provides an egocentric spatial reference frame, complementing the allocentric BEV occupancy grid.\n\n\\subsection{Ablation Design}\n\\label{sec:ablation}\n\nWe evaluate twelve conditions that systematically vary five factors: gradient flow from the auxiliary head into the vision encoders, label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of auxiliary supervision.\n\nThe $2{\\times}2$ factorial core crosses gradient flow (ON/OFF) with normalization (BN/LN): \\textbf{Vanilla} (no auxiliary head), \\textbf{Full OCC} (BEV occupancy, gradient flow, BatchNorm), \\textbf{Detach OCC} (gradients blocked via \\texttt{stop\\_gradient}), and their LN variants (\\textbf{Full OCC+LN}, \\textbf{Detach+LN}). Seven supplementary conditions probe label content (\\textbf{Random OCC}), reference frame (\\textbf{Depth}), and temporal extent (\\textbf{Cutoff@\\{15K--45K\\}}, \\textbf{Reverse Cutoff}; details in Appendix~\\ref{app:training}). Table~\\ref{tab:ablation_design} summarizes all twelve conditions and nine pairwise comparisons.\n\nFormally, let $\\text{sg}(\\cdot)$ denote the stop-gradient operator. Full conditions compute $\\mathcal{L}_\\text{aux}(h(\\phi_v(o_t)), s_t^*)$, so auxiliary gradients flow back through $\\phi_v$. Detach conditions compute $\\mathcal{L}_\\text{aux}(h(\\text{sg}(\\phi_v(o_t))), s_t^*)$: the head $h$ trains on encoder features, but no gradient reaches $\\phi_v$. This distinction separates bidirectional coupling (spatial and action objectives jointly shape encoder representations) from unidirectional readout (the head reads encoder features but does not influence encoder weight updates).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\caption{Ablation design: each comparison isolates one factor.}\n\\label{tab:ablation_design}\n\\begin{tabular}{@{}ll@{}}\n\\toprule\nComparison & Isolated Factor \\\\\n\\midrule\nFull OCC vs.\\ Vanilla & Auxiliary spatial supervision \\\\\nRandom vs.\\ Full OCC & Spatial content vs.\\ gradient flow \\\\\nDetach vs.\\ Vanilla & Encoder gradient flow (presence/absence) \\\\\nDetach+LN vs.\\ Detach OCC & Normalization (BN vs.\\ LN) without gradient flow \\\\\nFull OCC+LN vs.\\ Full OCC & Normalization (BN vs.\\ LN) with gradient flow \\\\\n$2{\\times}2$ factorial & Normalization $\\times$ gradient flow combined effects \\\\\nDepth vs.\\ Full OCC & Egocentric vs.\\ allocentric frame \\\\\nCutoff@\\{15K--45K\\} vs.\\ Full OCC & Temporal extent of gradient flow \\\\\nReverse Cutoff vs.\\ Cutoff@35K & Early vs.\\ late gradient flow \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Evaluation}\n\nWe evaluate on SafeLIBERO Level~I~\\cite{hu2025vlsa}, which places obstacles in close proximity to manipulation targets across 10 tabletop tasks drawn from LIBERO-Spatial~\\cite{liu2023libero}. We report two metrics: \\textbf{Task Success Rate (TSR)}, the fraction of episodes in which the task is completed, and \\textbf{Collision Avoidance Rate (CAR)}, where a collision is registered when the L1 displacement of any obstacle \\texttt{body\\_xpos} exceeds $10^{-3}$. The five core factorial conditions (Vanilla, Full OCC, Full OCC+LN, Detach OCC, Detach+LN), along with Random OCC, Depth, and Cutoff@35K, each use 1--4 independent seeds; remaining temporal conditions (Cutoff@\\{15K, 25K, 45K\\}, Reverse Cutoff) use 1--2 seeds as noted in Table~\\ref{tab:main_results}. Each seed runs 50 rollouts per task (500 episodes per seed).\n\nThe BN factorial cells (Full OCC and Detach OCC) have been fully retrained under a revised codebase (v2, 3--4 seeds each); among the LN cells, Full OCC+LN uses v2 ($n{=}4$) and Detach+LN uses v2 ($n{=}3$). Both codebase versions share identical architectures, hyperparameters, and evaluation protocols. Supplementary conditions use the original codebase (v1). Bootstrap 95\\% CIs use 10{,}000 hierarchical resamples (percentile method). Training runs for 50K steps on a single NVIDIA RTX PRO 6000 GPU; full details are in Appendix~\\ref{app:training}.\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01NnaB3J5uNQPYaoSWAYpcxx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "e0248301-38d4-4d46-8f72-f4c377a88302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 13 · 2026-05-28T09:45:44.709Z_

<details><summary>↩ Tool result · `toolu_01NnaB3J5uNQPYaoSWAYpcxx`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	
7	Table~\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\times$ 10 tasks per seed). $\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\star$) uses v1 code but is included above the midrule as a factorial control; its $\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Cohen's $d$ against the Vanilla baseline.
8	
9	\textbf{Gradient flow interacts with normalization type.} The four factorial cells reveal a normalization-dependent pattern. Under BatchNorm, gradient flow degrades safety: Full OCC (BN, gradient ON) is the worst-performing cell (CAR $0.725$, $\Delta{=}-2.0$\,pp vs.\ Vanilla) and the sole configuration falling below baseline, while Detach OCC (gradient OFF) exceeds it ($0.767$, $\Delta{=}+2.2$\,pp). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\Delta{=}+2.8$\,pp) already exceeds Vanilla, and Detach+LN ($0.802 \pm 0.024$, $n{=}3$) yields the highest cell mean ($\Delta{=}+5.7$\,pp). Both LN cells exceed the Vanilla baseline, whereas only the gradient-OFF BN cell does so. The BN + gradient flow cell also exhibits the highest instability ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all other cells). Spatial label content does not detectably affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$, observed under v1 codebase for Random OCC and Depth).
10	
11	\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\sigma{=}0.064$, ${\geq}\,2{\times}$ that of all other cells; $\sigma \leq 0.027$ for all other cells): individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\Delta{=}-9.1$\,pp), spanning $12.2$\,pp. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance, suggesting that BatchNorm's running-statistics mechanism amplifies stochastic sensitivity when auxiliary gradients flow through the shared encoders.
12	
13	
14	\begin{table}[t]
15	\centering
16	\caption{Results on SafeLIBERO Level~I (10 tasks, 50 rollouts/seed). Mean $\pm$ SD across seeds. $\Delta$CAR vs.\ v2 Vanilla ($0.745$) for factorial conditions; vs.\ v1 Vanilla ($0.780$) for supplementary. $^{a}$Highest variance. $^\ddagger$2 seeds. $^\star$v1 code.}
17	\label{tab:main_results}
18	\small
19	\setlength{\tabcolsep}{3pt}
20	\begin{tabular}{llcccl}
21	\toprule
22	Flow & Norm & $n$ & CAR & TSR & $\Delta$CAR \\
23	\midrule
24	\multicolumn{6}{l}{\textit{$2{\times}2$ factorial (v2 code)}} \\
25	ON  & BN & 3 & $0.725 \pm 0.064^{a}$ & $0.854 \pm 0.052$ & $-$2.0 \\
26	OFF & BN & 4 & $0.767 \pm 0.024$ & $0.908 \pm 0.026$ & $+$2.2 \\
27	ON  & LN & 4 & $0.773 \pm 0.027$ & $0.914 \pm 0.049$ & $+$2.8 \\
28	OFF & LN & 3 & $0.802 \pm 0.024$ & $0.911 \pm 0.018$ & $+$5.7 \\
29	\addlinespace
30	---  & Vanilla & 3 & $0.745 \pm 0.024$ & $0.878 \pm 0.032$ & --- \\
31	\midrule
32	\multicolumn{6}{l}{\textit{Controls \& supplementary (v1 code)}} \\
33	ON  & BN (Random)$^\star$ & 3 & $0.789 \pm 0.031$ & $0.869 \pm 0.029$ & --- \\
34	ON  & --- (Depth)$^\star$ & 4 & $0.780 \pm 0.039$ & $0.889 \pm 0.042$ & $0.0$ \\
35	ON  & BN (Cutoff@15K)$^\ddagger$ & 2 & $0.782 \pm 0.031$ & $0.883 \pm 0.041$ & $+$0.2 \\
36	ON  & BN (Cutoff@25K)$^\ddagger$ & 2 & $0.724 \pm 0.051$ & $0.887 \pm 0.061$ & $-$5.6 \\
37	ON  & BN (Cutoff@35K)       & 3 & $0.779 \pm 0.017$ & $0.933 \pm 0.032$ & $-$0.1 \\
38	ON  & BN (Cutoff@45K)       & 1 & $0.764$           & $0.896$           & $-$1.6 \\
39	ON  & BN (Rev.\ Cutoff)$^\ddagger$ & 2 & $0.718 \pm 0.025$ & $0.839 \pm 0.072$ & $-$6.2 \\
40	\bottomrule
41	\end{tabular}
42	\end{table}
43	
44	\subsection{Normalization and Gradient Flow Effects}
45	\label{sec:mechanism}
46	
47	The four factorial cells form a $2{\times}2$ design crossing normalization type (BN/LN) with gradient flow (ON/OFF) (Table~\ref{tab:factorial}, Figure~\ref{fig:factorial}).
48	
49	\textbf{Gradient flow is harmful under BatchNorm but benign under LayerNorm.} The BN row provides the clearest signal: gradient flow reduces CAR by 4.2\,pp (Full OCC $0.725 \pm 0.064$ vs.\ Detach OCC $0.767 \pm 0.024$; Cohen's $d{=}-0.93$, large). Full OCC (BN) is the sole factorial cell falling below Vanilla ($\Delta{=}-2.0$\,pp), whereas Detach OCC recovers above it ($\Delta{=}+2.2$\,pp, $d{=}+0.88$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $\Delta{=}+2.8$\,pp, $d{=}+1.07$, large), and Detach+LN yields the highest cell mean ($0.802 \pm 0.024$, $n{=}3$, $\Delta{=}+5.7$\,pp, $d{=}+2.36$, very large). Two main effects drive the factorial pattern ($2{\times}2$ ANOVA: gradient flow $F(1,10){=}3.20$, $p{=}0.104$, $\eta^2{=}0.18$; normalization $F(1,10){=}4.49$, $p{=}0.060$, $\eta^2{=}0.25$; interaction $F{<}0.1$, $p{=}0.76$; Appendix~\ref{app:stat_power}). First, gradient flow under BN reduces CAR by 4.2\,pp ($d{=}0.93$, large), making BN + gradient flow the sole configuration below the Vanilla baseline. Second, LN provides a consistent safety advantage over BN: $+$4.8\,pp under gradient flow ($d{=}1.05$, large) and $+$3.5\,pp without ($d{=}1.47$, very large). This is a practical threshold crossing (only the BN + gradient flow combination harms safety) rather than a statistical interaction (the factorial interaction is negligible, $\eta^2{=}0.005$).
50	
51	Pairwise Welch $t$-tests with Bonferroni correction yield no significant comparisons at $\alpha{=}0.05$, consistent with small per-cell $n$ ($n{=}3$--$4$); we rely on effect sizes rather than $p$-values for inference (Appendix~\ref{app:stat_power}). The normalization main effect approaches significance ($p{=}0.060$). Both main effects amplify by ${\approx}3{\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\ref{app:per_task_factorial}).
52	
53	\begin{table}[t]
54	\centering
55	\caption{$2{\times}2$ factorial: normalization type $\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $d{=}0.93$ (large); normalization effect $d{=}1.05$--$1.47$ (large to very large). BN + gradient flow is the sole cell below Vanilla. ANOVA interaction $F{<}0.1$, $p{=}0.76$.}
56	\label{tab:factorial}
57	\begin{tabular}{lccc}
58	\toprule
59	 & Gradient ON & Gradient OFF & $\Delta$(ON$-$OFF) \\
60	\midrule
61	BatchNorm    & Full OCC (0.725) & Detach OCC (0.767) & $-$4.2 \\
62	LayerNorm    & Full OCC+LN (0.773) & Detach+LN (0.802) & $-$2.9 \\
63	\midrule
64	$\Delta$(BN$-$LN) & $-$4.8 ($d{=}{-}1.05$) & $-$3.5 ($d{=}{-}1.47$) & --- \\
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
69	\begin{figure}[t]
70	\centering
71	\includegraphics[width=0.65\textwidth]{figures/factorial_2x2.pdf}
72	\caption{$2{\times}2$ factorial comparison: normalization type (BN/LN) $\times$ gradient flow (ON/OFF). BN row: gradient flow reduces CAR by 4.2\,pp ($d{=}0.93$); LN row: 2.9\,pp ($d{=}1.12$). All LN cells exceed Vanilla baseline. Error bars: cross-seed SD ($n{=}3$--$4$ per cell).}
73	\label{fig:factorial}
74	\end{figure}
75	
76	\subsection{Gradient Dynamics}
77	
78	Gradient analysis (Figure~\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).
79	
80	\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\approx}$46\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes in our experiments. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis reported here covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)
81	
82	\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.
83	
84	Additional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\ref{app:additional}.
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "d08e1d48-586c-4851-af37-3a48397a88f1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Cohen's $d$ against the Vanilla baseline.\n\n\\textbf{Gradient flow interacts with normalization type.} The four factorial cells reveal a normalization-dependent pattern. Under BatchNorm, gradient flow degrades safety: Full OCC (BN, gradient ON) is the worst-performing cell (CAR $0.725$, $\\Delta{=}-2.0$\\,pp vs.\\ Vanilla) and the sole configuration falling below baseline, while Detach OCC (gradient OFF) exceeds it ($0.767$, $\\Delta{=}+2.2$\\,pp). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\\Delta{=}+2.8$\\,pp) already exceeds Vanilla, and Detach+LN ($0.802 \\pm 0.024$, $n{=}3$) yields the highest cell mean ($\\Delta{=}+5.7$\\,pp). Both LN cells exceed the Vanilla baseline, whereas only the gradient-OFF BN cell does so. The BN + gradient flow cell also exhibits the highest instability ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all other cells). Spatial label content does not detectably affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance ($p > 0.4$, observed under v1 codebase for Random OCC and Depth).\n\n\\textbf{BN + gradient flow destabilizes training.} Full OCC (BN) exhibits the highest variance of any factorial cell ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ that of all other cells; $\\sigma \\leq 0.027$ for all other cells): individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\\Delta{=}-9.1$\\,pp), spanning $12.2$\\,pp. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance, suggesting that BatchNorm's running-statistics mechanism amplifies stochastic sensitivity when auxiliary gradients flow through the shared encoders.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Results on SafeLIBERO Level~I (10 tasks, 50 rollouts/seed). Mean $\\pm$ SD across seeds. $\\Delta$CAR vs.\\ v2 Vanilla ($0.745$) for factorial conditions; vs.\\ v1 Vanilla ($0.780$) for supplementary. $^{a}$Highest variance. $^\\ddagger$2 seeds. $^\\star$v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\nFlow & Norm & $n$ & CAR & TSR & $\\Delta$CAR \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$2{\\times}2$ factorial (v2 code)}} \\\\\nON  & BN & 3 & $0.725 \\pm 0.064^{a}$ & $0.854 \\pm 0.052$ & $-$2.0 \\\\\nOFF & BN & 4 & $0.767 \\pm 0.024$ & $0.908 \\pm 0.026$ & $+$2.2 \\\\\nON  & LN & 4 & $0.773 \\pm 0.027$ & $0.914 \\pm 0.049$ & $+$2.8 \\\\\nOFF & LN & 3 & $0.802 \\pm 0.024$ & $0.911 \\pm 0.018$ & $+$5.7 \\\\\n\\addlinespace\n---  & Vanilla & 3 & $0.745 \\pm 0.024$ & $0.878 \\pm 0.032$ & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Controls \\& supplementary (v1 code)}} \\\\\nON  & BN (Random)$^\\star$ & 3 & $0.789 \\pm 0.031$ & $0.869 \\pm 0.029$ & --- \\\\\nON  & --- (Depth)$^\\star$ & 4 & $0.780 \\pm 0.039$ & $0.889 \\pm 0.042$ & $0.0$ \\\\\nON  & BN (Cutoff@15K)$^\\ddagger$ & 2 & $0.782 \\pm 0.031$ & $0.883 \\pm 0.041$ & $+$0.2 \\\\\nON  & BN (Cutoff@25K)$^\\ddagger$ & 2 & $0.724 \\pm 0.051$ & $0.887 \\pm 0.061$ & $-$5.6 \\\\\nON  & BN (Cutoff@35K)       & 3 & $0.779 \\pm 0.017$ & $0.933 \\pm 0.032$ & $-$0.1 \\\\\nON  & BN (Cutoff@45K)       & 1 & $0.764$           & $0.896$           & $-$1.6 \\\\\nON  & BN (Rev.\\ Cutoff)$^\\ddagger$ & 2 & $0.718 \\pm 0.025$ & $0.839 \\pm 0.072$ & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Normalization and Gradient Flow Effects}\n\\label{sec:mechanism}\n\nThe four factorial cells form a $2{\\times}2$ design crossing normalization type (BN/LN) with gradient flow (ON/OFF) (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}).\n\n\\textbf{Gradient flow is harmful under BatchNorm but benign under LayerNorm.} The BN row provides the clearest signal: gradient flow reduces CAR by 4.2\\,pp (Full OCC $0.725 \\pm 0.064$ vs.\\ Detach OCC $0.767 \\pm 0.024$; Cohen's $d{=}-0.93$, large). Full OCC (BN) is the sole factorial cell falling below Vanilla ($\\Delta{=}-2.0$\\,pp), whereas Detach OCC recovers above it ($\\Delta{=}+2.2$\\,pp, $d{=}+0.88$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $\\Delta{=}+2.8$\\,pp, $d{=}+1.07$, large), and Detach+LN yields the highest cell mean ($0.802 \\pm 0.024$, $n{=}3$, $\\Delta{=}+5.7$\\,pp, $d{=}+2.36$, very large). Two main effects drive the factorial pattern ($2{\\times}2$ ANOVA: gradient flow $F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.18$; normalization $F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.25$; interaction $F{<}0.1$, $p{=}0.76$; Appendix~\\ref{app:stat_power}). First, gradient flow under BN reduces CAR by 4.2\\,pp ($d{=}0.93$, large), making BN + gradient flow the sole configuration below the Vanilla baseline. Second, LN provides a consistent safety advantage over BN: $+$4.8\\,pp under gradient flow ($d{=}1.05$, large) and $+$3.5\\,pp without ($d{=}1.47$, very large). This is a practical threshold crossing (only the BN + gradient flow combination harms safety) rather than a statistical interaction (the factorial interaction is negligible, $\\eta^2{=}0.005$).\n\nPairwise Welch $t$-tests with Bonferroni correction yield no significant comparisons at $\\alpha{=}0.05$, consistent with small per-cell $n$ ($n{=}3$--$4$); we rely on effect sizes rather than $p$-values for inference (Appendix~\\ref{app:stat_power}). The normalization main effect approaches significance ($p{=}0.060$). Both main effects amplify by ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}).\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $d{=}0.93$ (large); normalization effect $d{=}1.05$--$1.47$ (large to very large). BN + gradient flow is the sole cell below Vanilla. ANOVA interaction $F{<}0.1$, $p{=}0.76$.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (0.767) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.773) & Detach+LN (0.802) & $-$2.9 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$4.8 ($d{=}{-}1.05$) & $-$3.5 ($d{=}{-}1.47$) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n\\caption{$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow reduces CAR by 4.2\\,pp ($d{=}0.93$); LN row: 2.9\\,pp ($d{=}1.12$). All LN cells exceed Vanilla baseline. Error bars: cross-seed SD ($n{=}3$--$4$ per cell).}\n\\label{fig:factorial}\n\\end{figure}\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC, with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions, ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes in our experiments. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis reported here covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)\n\n\\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The detrimental effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. CKA analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP), localizing the safety degradation to optimization dynamics rather than representational corruption.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01LYqTTcscXTwEPWdzWWHyLk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "f62ed5b7-2249-45c2-9510-df3d9ee4fd44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 15 · 2026-05-28T09:45:45.158Z_

<details><summary>↩ Tool result · `toolu_01LYqTTcscXTwEPWdzWWHyLk`</summary>

```text
1	
2	\section{Discussion}
3	\label{sec:discussion}
4	\label{sec:why_gradient}
5	
6	BatchNorm is not inherently harmful: Detach OCC (BN, gradient OFF) matches or slightly exceeds Vanilla (0.767 vs.\ 0.745, $p{=}0.28$). The damage is BN-specific: under BatchNorm, gradient flow drops CAR below the Vanilla baseline (0.725 vs.\ 0.745, $d{=}{-}0.93$), while under LayerNorm, gradient flow is benign (0.773 vs.\ 0.745, $d{=}{+}1.07$). Both normalization rows show within-row deficits from gradient flow ($-$4.2\,pp for BN, $-$2.9\,pp for LN), but only the BN row falls below the no-auxiliary baseline. CKA analysis confirms that encoder representations remain intact under all conditions (CKA $\geq$ 0.95 for both DINOv2 and SigLIP), ruling out representational drift and localizing the effect to optimization dynamics. The BN + gradient flow cell is both the worst-performing and the most unstable configuration ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all other cells). We hypothesize that BatchNorm's running statistics introduce sensitivity to distributional shifts from auxiliary gradients, a coupling absent in LayerNorm's per-token computation. The numerical advantage of Detach OCC ($+$2.2\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.
7	
8	\textbf{Normalization independently affects safety.} LN provides a consistent safety advantage over BN ($+$4.8\,pp under gradient flow, $d{=}1.03$; $+$3.5\,pp without), comparable in magnitude to the gradient flow effect. For practitioners who must retain gradient flow, LayerNorm converts the BN safety deficit into a gain, an architectural advantage, since label content does not detectably affect outcomes.
9	
10	\textbf{Additive protection model.} Cell~1 (BN + gradient flow) is the only factorial cell below Vanilla, confirming that safety degradation requires the joint presence of BatchNorm and gradient flow in this setting; removing either condition suffices to restore safety above baseline. The two protections, switching to LayerNorm and detaching auxiliary gradients, are not redundant but complementary: each independently contributes ${\approx}$4--5\,pp (LN: $+$4.8\,pp, detach: $+$4.2\,pp relative to Cell~1), and the $2{\times}2$ ANOVA interaction term is negligible ($F{=}0.10$, $p{=}0.763$, $\eta^2{=}0.005$; Table~\ref{tab:anova}), consistent with a purely additive model. Cell~4 (Detach+LN), which applies both protections simultaneously, yields CAR $0.802{\pm}0.024$ ($n{=}3$), close to the additive prediction from Cell~1 plus both main effects.
11	
12	Gradient analysis confirms orthogonality between action and auxiliary gradients (cosine $\approx$ 0, conflict rate $\approx$ 46\%), ruling out direct gradient conflict~\cite{yu2020pcgrad, liu2021cagrad}. The detrimental effect operates through indirect channels, likely reshaping the LoRA optimization trajectory under a dual-objective loss landscape~\cite{lippl2024implicit, jiang2023forkmerge}, rather than through gradient interference. This sensitivity extends to implementation details: a codebase revision (v2) that fixed a batch-index resume bug (without changing any model architecture, hyperparameter, or evaluation protocol) shifts absolute CAR by up to 8.6\,pp for the same seed (Vanilla stable, $<$1.5\,pp), and the effect pattern itself changed from an apparent crossover under v1 to the dual main effects reported here (Appendix~\ref{app:codebase}). This level of sensitivity to non-hyperparameter implementation details has not been documented in prior multi-task learning work and constitutes an independent finding.
13	
14	The content irrelevance finding (structured $\approx$ random $\approx$ depth labels) was observed under v1; whether it persists under v2 remains open, but is indirectly supported by the gradient orthogonality analysis (confirmed under v2), which shows identical gradient geometry for structured and random labels.
15	
16	These safety findings do not contradict task success improvements reported by spatial VLA methods~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}; safety and task success can respond differently to auxiliary supervision, making independent safety evaluation essential. Normalization type and gradient flow configuration, rarely specified in current work, should be standard reporting practice. Safety differences concentrate on three physically constrained tasks (Appendix~\ref{app:additional}).
17	
18	\textbf{LoRA-specificity caveat.} All experiments use LoRA adapters; whether full fine-tuning exhibits the same pattern is open. The low-rank constraint may amplify sensitivity to dual-objective landscapes that full-rank updates could absorb.
19	
20	\textbf{Practical guideline.} Do not add auxiliary spatial heads for safety purposes. If required, use detached gradients with LayerNorm; avoid combining BatchNorm with gradient flow. No ground-truth labels are needed; the head is discarded at zero inference cost, complementing runtime methods~\cite{hu2025vlsa, raja2024ogmcbf}. Limitations are in Appendix~\ref{app:limitations}.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "7df72f31-0dd0-4059-98bd-da93c8c9fbeb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
      "content": "\n\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_gradient}\n\nBatchNorm is not inherently harmful: Detach OCC (BN, gradient OFF) matches or slightly exceeds Vanilla (0.767 vs.\\ 0.745, $p{=}0.28$). The damage is BN-specific: under BatchNorm, gradient flow drops CAR below the Vanilla baseline (0.725 vs.\\ 0.745, $d{=}{-}0.93$), while under LayerNorm, gradient flow is benign (0.773 vs.\\ 0.745, $d{=}{+}1.07$). Both normalization rows show within-row deficits from gradient flow ($-$4.2\\,pp for BN, $-$2.9\\,pp for LN), but only the BN row falls below the no-auxiliary baseline. CKA analysis confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP), ruling out representational drift and localizing the effect to optimization dynamics. The BN + gradient flow cell is both the worst-performing and the most unstable configuration ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all other cells). We hypothesize that BatchNorm's running statistics introduce sensitivity to distributional shifts from auxiliary gradients, a coupling absent in LayerNorm's per-token computation. The numerical advantage of Detach OCC ($+$2.2\\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.\n\n\\textbf{Normalization independently affects safety.} LN provides a consistent safety advantage over BN ($+$4.8\\,pp under gradient flow, $d{=}1.03$; $+$3.5\\,pp without), comparable in magnitude to the gradient flow effect. For practitioners who must retain gradient flow, LayerNorm converts the BN safety deficit into a gain, an architectural advantage, since label content does not detectably affect outcomes.\n\n\\textbf{Additive protection model.} Cell~1 (BN + gradient flow) is the only factorial cell below Vanilla, confirming that safety degradation requires the joint presence of BatchNorm and gradient flow in this setting; removing either condition suffices to restore safety above baseline. The two protections, switching to LayerNorm and detaching auxiliary gradients, are not redundant but complementary: each independently contributes ${\\approx}$4--5\\,pp (LN: $+$4.8\\,pp, detach: $+$4.2\\,pp relative to Cell~1), and the $2{\\times}2$ ANOVA interaction term is negligible ($F{=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$; Table~\\ref{tab:anova}), consistent with a purely additive model. Cell~4 (Detach+LN), which applies both protections simultaneously, yields CAR $0.802{\\pm}0.024$ ($n{=}3$), close to the additive prediction from Cell~1 plus both main effects.\n\nGradient analysis confirms orthogonality between action and auxiliary gradients (cosine $\\approx$ 0, conflict rate $\\approx$ 46\\%), ruling out direct gradient conflict~\\cite{yu2020pcgrad, liu2021cagrad}. The detrimental effect operates through indirect channels, likely reshaping the LoRA optimization trajectory under a dual-objective loss landscape~\\cite{lippl2024implicit, jiang2023forkmerge}, rather than through gradient interference. This sensitivity extends to implementation details: a codebase revision (v2) that fixed a batch-index resume bug (without changing any model architecture, hyperparameter, or evaluation protocol) shifts absolute CAR by up to 8.6\\,pp for the same seed (Vanilla stable, $<$1.5\\,pp), and the effect pattern itself changed from an apparent crossover under v1 to the dual main effects reported here (Appendix~\\ref{app:codebase}). This level of sensitivity to non-hyperparameter implementation details has not been documented in prior multi-task learning work and constitutes an independent finding.\n\nThe content irrelevance finding (structured $\\approx$ random $\\approx$ depth labels) was observed under v1; whether it persists under v2 remains open, but is indirectly supported by the gradient orthogonality analysis (confirmed under v2), which shows identical gradient geometry for structured and random labels.\n\nThese safety findings do not contradict task success improvements reported by spatial VLA methods~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}; safety and task success can respond differently to auxiliary supervision, making independent safety evaluation essential. Normalization type and gradient flow configuration, rarely specified in current work, should be standard reporting practice. Safety differences concentrate on three physically constrained tasks (Appendix~\\ref{app:additional}).\n\n\\textbf{LoRA-specificity caveat.} All experiments use LoRA adapters; whether full fine-tuning exhibits the same pattern is open. The low-rank constraint may amplify sensitivity to dual-objective landscapes that full-rank updates could absorb.\n\n\\textbf{Practical guideline.} Do not add auxiliary spatial heads for safety purposes. If required, use detached gradients with LayerNorm; avoid combining BatchNorm with gradient flow. No ground-truth labels are needed; the head is discarded at zero inference cost, complementing runtime methods~\\cite{hu2025vlsa, raja2024ogmcbf}. Limitations are in Appendix~\\ref{app:limitations}.\n",
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_015AQEhph12gQr4tDwpnojPC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "1370d2d3-8e9b-424e-9704-a2ba470d8a83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 17 · 2026-05-28T09:45:46.124Z_

<details><summary>↩ Tool result · `toolu_015AQEhph12gQr4tDwpnojPC`</summary>

```text
1	
2	\section{Conclusion}
3	
4	We presented a systematic factorial study of auxiliary spatial supervision during VLA fine-tuning. A $2{\times}2$ factorial reveals two large main effects: gradient flow under BatchNorm degrades collision avoidance below the Vanilla baseline ($d{=}{-}0.93$) and produces the highest training instability ($\sigma{=}0.064$); LayerNorm provides a consistent 3.5--4.8\,pp safety advantage ($d{\approx}1.03$). Only the BN + gradient flow combination harms safety; spatial label content showed no detectable effect. Practitioners should omit auxiliary spatial heads or, if required, use detached gradients with LayerNorm; avoid combining BatchNorm with gradient flow. CKA analysis localizes the degradation to optimization dynamics rather than representational capacity (CKA $\geq$ 0.95). Training-time collision avoidance may instead require approaches that directly encode safety constraints~\cite{zhang2025safevla}.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "d2201fad-fbdb-4c16-a2fb-b0e5bf8c1227",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/conclusion.tex",
      "content": "\n\\section{Conclusion}\n\nWe presented a systematic factorial study of auxiliary spatial supervision during VLA fine-tuning. A $2{\\times}2$ factorial reveals two large main effects: gradient flow under BatchNorm degrades collision avoidance below the Vanilla baseline ($d{=}{-}0.93$) and produces the highest training instability ($\\sigma{=}0.064$); LayerNorm provides a consistent 3.5--4.8\\,pp safety advantage ($d{\\approx}1.03$). Only the BN + gradient flow combination harms safety; spatial label content showed no detectable effect. Practitioners should omit auxiliary spatial heads or, if required, use detached gradients with LayerNorm; avoid combining BatchNorm with gradient flow. CKA analysis localizes the degradation to optimization dynamics rather than representational capacity (CKA $\\geq$ 0.95). Training-time collision avoidance may instead require approaches that directly encode safety constraints~\\cite{zhang2025safevla}.\n",
      "numLines": 5,
      "startLine": 1,
      "totalLines": 5
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01EaP2FCRaeJFa5H4WgAbXMs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "032f49f5-4064-45e0-aae1-edc87b44d26f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 19 · 2026-05-28T09:45:46.599Z_

<details><summary>↩ Tool result · `toolu_01EaP2FCRaeJFa5H4WgAbXMs`</summary>

```text
1	
2	\section{Extended Per-Task Results}
3	\label{app:per_task}
4	
5	Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
6	
7	\begin{table}[h]
8	\centering
9	\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}
10	\label{tab:per_task}
11	\begin{tabular}{clccccccc}
12	\toprule
13	 & & \multicolumn{7}{c}{Mean CAR by Condition} \\
14	\cmidrule(lr){3-9}
15	Task & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\
16	\midrule
17	T0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\
18	T1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\
19	T2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\
20	T3 & Hard  & 0.38 & 0.37 & 0.31 & \textbf{0.11} & 0.44 & 0.50 & 0.55 \\
21	T4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\
22	T5 & Hard  & 0.07 & 0.17 & 0.23 & \textbf{0.05} & 0.12 & 0.08 & 0.04 \\
23	T6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\
24	T7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\
25	T8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\
26	T9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\
27	\midrule
28	\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.
34	
35	\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.
36	
37	\section{Training Details}
38	\label{app:training}
39	
40	\begin{table}[h]
41	\centering
42	\caption{Training hyperparameters.}
43	\begin{tabular}{ll}
44	\toprule
45	Parameter & Value \\
46	\midrule
47	Base model & OpenVLA-7B~\cite{kim2024openvla} \\
48	Fine-tuning recipe & OFT~\cite{kim2025oft} \\
49	Vision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\
50	Patch token dim. & 2176 (concatenated) \\
51	LoRA rank / $\alpha$ & 32 / 16 \\
52	LoRA trainable params & 110.8M (1.45\% of 7.65B) \\
53	Optimizer & AdamW (weight decay 0.01) \\
54	Batch size & 8 \\
55	Learning rate & $5 \times 10^{-4}$ (constant) \\
56	Training steps & 50{,}000 \\
57	Aux.\ loss weight $\lambda_0$ & 0.01 \\
58	Aux.\ loss decay & $\exp(-t / 50{,}000)$ \\
59	BEV grid resolution & $64 \times 64$ \\
60	Focal loss $\alpha$ / $\gamma$ & 0.25 / 2.0 \\
61	Depth loss & Smooth-L1 \\
62	Aux.\ head parameters & 1.2M \\
63	Hardware & NVIDIA RTX PRO 6000 (96\,GB) \\
64	Wall time per run & $\sim$12.9 hours \\
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
69	\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \texttt{body\_xpos} exceeds $10^{-3}$. Bootstrap 95\% CIs are computed via 10{,}000 resamples (percentile method).
70	
71	\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.
72	\textbf{CKA analysis.} Centered Kernel Alignment~\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.
73	
74	\textbf{Cutoff implementation.} As described in Section~\ref{sec:ablation}, setting $\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).
75	
76	\section{Extended Analysis}
77	
78	\begin{figure}[h]
79	\centering
80	\includegraphics[width=\textwidth]{figures/gradient_analysis_v2_combined.pdf}
81	\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\approx}$46\%). (d)~Gradient norm ratio per layer.}
82	\label{fig:gradient_analysis}
83	\end{figure}
84	
85	The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \texttt{stop\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \pm 0.024$ (Table~\ref{tab:main_results}), the highest factorial cell mean ($\Delta{=}+5.7$\,pp vs.\ Vanilla, $d{=}+2.36$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.
86	
87	\textbf{Per-layer gradient analysis.} Figure~\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\%, Full OCC+LN 45.7\% under v2; Full OCC 44.1\%, Random OCC 43.9\% under v1) fall below the 50\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.
88	
89	\begin{figure}[h]
90	\centering
91	\includegraphics[width=\textwidth]{figures/per_layer_combined.pdf}
92	\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\ref{app:codebase}). \textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\sim$46\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\approx}$46\% in early and middle layers; late SigLIP layers show lower conflict rates (${\approx}$25\%), consistent with weak alignment rather than conflict.}
93	\label{fig:per_layer_combined}
94	\end{figure}
95	
96	\subsection{Temporal Dynamics}
97	\label{app:temporal}
98	\textbf{Dose-response: gradient flow duration vs.\ CAR (v1 data).} Figure~\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.
99	
100	\begin{figure}[h]
101	\centering
102	\includegraphics[width=0.75\textwidth]{figures/dose_response.pdf}
103	\caption{Dose-response: CAR vs.\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\leq$2 seeds (counts annotated as $n$). Diamond ($\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\pm\,$1\,SE. The ``+0.2\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}
104	\label{fig:dose_response}
105	\end{figure}
106	
107	\section{Additional Observations}
108	\label{app:additional}
109	
110	\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.
111	
112	\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.
113	
114	\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\Delta = -$0.1\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\ref{app:temporal}.
115	
116	\textbf{Cross-benchmark Vanilla baseline.} Vanilla baseline on LIBERO-Object achieves CAR \textbf{X.XX} ($n{=}2$), confirming that the safety gap between TSR and CAR is not specific to LIBERO-Spatial.
117	% TODO: fill X.XX with vanilla_object eval data (~08:45 UTC)
118	
119	\section{Codebase Sensitivity (v1 vs.\ v2)}
120	\label{app:codebase}
121	
122	The five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.
123	
124	\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\ref{tab:per_task}); under v2, the same condition yields 0.725 $\pm$ 0.064 (Table~\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\,pp, while Vanilla remains stable across codebases ($<$1.5\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.
125	
126	\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\sim$4\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\sim$44\% (v1) to $\sim$46\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.
127	
128	\textbf{Effect pattern shift.} Under v1, the normalization $\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.
129	
130	\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.
131	
132	\section{Statistical Power Analysis}
133	\label{app:stat_power}
134	
135	The $2{\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.
136	
137	The study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\eta^2{=}0.005$) confirms these effects are additive.
138	
139	\textbf{Formal $2{\times}2$ ANOVA.} Table~\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.
140	
141	\begin{table}[h]
142	\centering
143	\caption{$2{\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}
144	\label{tab:anova}
145	\begin{tabular}{lcccc}
146	\toprule
147	Source & $F$ & df & $p$ & $\eta^2$ \\
148	\midrule
149	Gradient flow (ON vs.\ OFF) & 3.20 & 1,\,10 & 0.104 & 0.180 \\
150	Normalization (BN vs.\ LN) & 4.49 & 1,\,10 & 0.060 & 0.253 \\
151	Interaction & 0.10 & 1,\,10 & 0.763 & 0.005 \\
152	\bottomrule
153	\end{tabular}
154	\end{table}
155	
156	\textbf{Pairwise effect sizes.} Table~\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).
157	
158	\begin{table}[h]
159	\centering
160	\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}
161	\label{tab:pairwise}
162	\small
163	\begin{tabular}{lc}
164	\toprule
165	Comparison & Cohen's $d$ \\
166	\midrule
167	Cell~1 (Full OCC BN) vs.\ Cell~2 (Full OCC+LN) & $-$1.05 \\
168	Cell~1 vs.\ Cell~3 (Detach OCC) & $-$0.93 \\
169	Cell~1 vs.\ Cell~4 (Detach+LN) & $-$1.60 \\
170	Cell~2 vs.\ Cell~3 & $+$0.25 \\
171	Cell~2 vs.\ Cell~4 & $-$1.12 \\
172	Cell~3 vs.\ Cell~4 & $-$1.47 \\
173	\addlinespace
174	Cell~1 vs.\ Vanilla & $-$0.42 \\
175	Cell~2 vs.\ Vanilla & $+$1.07 \\
176	Cell~3 vs.\ Vanilla & $+$0.88 \\
177	Cell~4 vs.\ Vanilla & $+$2.36 \\
178	\bottomrule
179	\end{tabular}
180	\end{table}
181	
182	\section{Per-Task Factorial Analysis}
183	\label{app:per_task_factorial}
184	
185	The three physically constrained tasks (T3: \texttt{cookie\_box}, T5: \texttt{ramekin}, T6: \texttt{next\_to\_cookie\_box}) amplify both main effects by approximately $3{\times}$ relative to the overall means.
186	
187	\textbf{Normalization effect amplification.} The overall normalization effect ($\Delta{=}+3.5$--$4.8$\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.
188	
189	\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.
190	
191	These per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.
192	
193	\section{Limitations}
194	\label{app:limitations}
195	
196	Our study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.
197	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "27900963-697c-4950-85be-4b7231d73e7b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
      "content": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Cohen's $d$ for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics during VLA fine-tuning (v2 codebase; seed 42, 200 batches at 50K checkpoint). Five conditions: Vanilla, Full OCC (BN), Full OCC+LN, Detach OCC (BN), Detach+LN. (a)~Action loss gradient norms per encoder layer: all conditions maintain comparable norms, ruling out gradient amplification. (b)~Auxiliary loss gradient norms in the shared encoder (Detach conditions excluded; no auxiliary gradients by design). (c)~Action--auxiliary gradient cosine similarity per layer (near zero for all gradient-flow conditions, confirming orthogonality; conflict rate ${\\approx}$46\\%). (d)~Gradient norm ratio per layer.}\n\\label{fig:gradient_analysis}\n\\end{figure}\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $d{=}+2.36$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into an actively harmful regime. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\textbf{Cross-benchmark Vanilla baseline.} Vanilla baseline on LIBERO-Object achieves CAR \\textbf{X.XX} ($n{=}2$), confirming that the safety gap between TSR and CAR is not specific to LIBERO-Spatial.\n% TODO: fill X.XX with vanilla_object eval data (~08:45 UTC)\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{<}0.1$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Cohen's $d$ for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Cohen's $d$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.93 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.60 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.25 \\\\\nCell~2 vs.\\ Cell~4 & $-$1.12 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.47 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.42 \\\\\nCell~2 vs.\\ Vanilla & $+$1.07 \\\\\nCell~3 vs.\\ Vanilla & $+$0.88 \\\\\nCell~4 vs.\\ Vanilla & $+$2.36 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $d{=}2.65$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($d{=}+1.25$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n\\section{Limitations}\n\\label{app:limitations}\n\nOur study uses a single architecture (OpenVLA-OFT with LoRA rank 32); full fine-tuning may alter the interaction between auxiliary heads and encoder optimization because all parameters update simultaneously, potentially changing the gradient flow dynamics we observe. All experiments are conducted in MuJoCo simulation on a single task suite (SafeLIBERO Level~I, 10 tasks drawn from LIBERO-Spatial); whether the normalization-dependent gradient flow effect generalizes to other task distributions remains open. LIBERO-Object, which involves different spatial constraints, does not provide ground-truth occupancy labels, preventing factorial comparison on that benchmark; generating synthetic labels is straightforward but was not pursued in the current study. Real-world deployment introduces additional sources of distributional shift that could interact differently with auxiliary head training dynamics. The benchmark contains only static obstacles; dynamic obstacle scenarios may induce time-varying distributions where auxiliary head dynamics behave differently. Our collision metric is binary (L1 displacement threshold $10^{-3}$), which does not capture collision severity or near-miss behavior; a continuous safety metric might reveal finer-grained differences between conditions. CKA measures linear representational similarity, which may miss nonlinear structure relevant to safety behavior. The factorial design uses $n{=}3$--$4$ seeds per cell (14 total observations), which limits statistical power for individual pairwise tests; we report effect sizes as the primary inferential quantity rather than relying on $p$-values. Larger-scale replication would further strengthen conclusions. Cutoff conditions have 1--3 seeds, limiting temporal conclusions to preliminary observations. All auxiliary conditions use a fixed loss weight $\\lambda_0{=}0.01$ with exponential decay; we did not sweep this hyperparameter, so the gradient flow effect may vary under different loss weight schedules.\n",
      "numLines": 197,
      "startLine": 1,
      "totalLines": 197
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01SNVrYzAtUrbbiLHgdjCHGH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "48a40bfa-7a69-418e-b198-1a84fccb343f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 21 · 2026-05-28T09:45:47.080Z_

<details><summary>↩ Tool result · `toolu_01SNVrYzAtUrbbiLHgdjCHGH`</summary>

```text
1	
2	\section{Related Work}
3	
4	\subsection{VLA Safety and Spatial Representations}
5	
6	Vision-language-action models achieve high task success but remain collision-prone~\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure (depth fusion, representation alignment, geometric encoding, or occupancy prediction)~\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}, yet none evaluates collision avoidance. The occupancy branch of this line originated in autonomous driving: BEVFormer~\cite{li2022bevformer} introduced transformer-based bird's-eye-view estimation, and subsequent work formalized dense 3D occupancy as a unified scene representation~\cite{sima2023occnet, tian2023occ3d}. OccVLA~\cite{liu2025occvla} adapted this concept to robotics by supervising a VLA with implicit occupancy targets; our BEV occupancy auxiliary head follows the same principle but serves as a controlled experimental factor to isolate the safety effect of spatial supervision. SpatialVLA~\cite{wu2025spatialvla}, DepthVLA~\cite{yuan2025depthvla}, and OccVLA all report task success improvements from spatial auxiliary supervision but do not include safety metrics. The assumption that spatial awareness should improve safety because the robot ``knows where things are'' remains untested; we address this gap by directly measuring collision avoidance under controlled spatial supervision conditions.
7	
8	\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}
9	
10	Multi-task learning exploits shared representations~\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks risk negative transfer through optimization conflict or generalization failure~\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}. PCGrad~\cite{yu2020pcgrad} projects conflicting task gradients to remove their interfering components, while CAGrad~\cite{liu2021cagrad} seeks a descent direction within a conflict-averse region that minimizes worst-case task loss. Both assume that gradient conflict is the primary failure mode of multi-task optimization; our gradient analysis shows near-zero cosine similarity between action and auxiliary gradients, suggesting that the mechanism in our setting operates through a different channel.
11	
12	Batch normalization~\cite{ioffe2015batchnorm} standardizes activations using mini-batch statistics, coupling each sample's representation to the batch composition. Layer normalization~\cite{ba2016layernorm} removes this dependence by computing statistics per token, making it the default in transformer architectures, while group normalization~\cite{wu2018groupnorm} offers a batch-size-independent alternative by normalizing within channel groups. This design choice becomes consequential when auxiliary tasks alter the training distribution: Li et al.~\cite{li2017adabn} show that recalibrating BN statistics suffices to adapt across domains, and Schneider et al.~\cite{schneider2020bn} demonstrate that BN running statistics degrade robustness under covariate shift. Our factorial design varies the normalization scheme in the auxiliary head between BatchNorm and LayerNorm, directly testing whether these distributional sensitivities propagate to the primary action objective.
13	
14	For VLA fine-tuning with LoRA~\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. LoRA constrains updates to a low-rank subspace, which may limit the model's capacity to accommodate competing objectives that full-rank updates could absorb; how this constraint interacts with multi-task gradient dynamics is an open question in the literature. Our factorial design isolates gradient flow from spatial content and identifies a normalization-dependent gradient flow effect that challenges the assumption that auxiliary spatial supervision should improve safety.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "d4f4b109-1417-4408-87e7-eb8b28cd945e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex",
      "content": "\n\\section{Related Work}\n\n\\subsection{VLA Safety and Spatial Representations}\n\nVision-language-action models achieve high task success but remain collision-prone~\\cite{li2026vlasafety}. Existing safety approaches filter actions via control barrier functions or embed constraints during training~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf, zhang2025safevla}; none examines whether spatial representations contribute to safety. A parallel line enriches VLAs with 3D structure (depth fusion, representation alignment, geometric encoding, or occupancy prediction)~\\cite{yuan2025depthvla, li2025qdepthvla, rao2026augvla3d, bhat20253dcavla, abouzeid2025geoaware, yang2024depthanything, li2026spatialforcing, wu2025spatialvla, li2025pointvla, sun2025geovla, wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2026corridorvla, liu2025occvla, li2022bevformer, sima2023occnet, tian2023occ3d}, yet none evaluates collision avoidance. The occupancy branch of this line originated in autonomous driving: BEVFormer~\\cite{li2022bevformer} introduced transformer-based bird's-eye-view estimation, and subsequent work formalized dense 3D occupancy as a unified scene representation~\\cite{sima2023occnet, tian2023occ3d}. OccVLA~\\cite{liu2025occvla} adapted this concept to robotics by supervising a VLA with implicit occupancy targets; our BEV occupancy auxiliary head follows the same principle but serves as a controlled experimental factor to isolate the safety effect of spatial supervision. SpatialVLA~\\cite{wu2025spatialvla}, DepthVLA~\\cite{yuan2025depthvla}, and OccVLA all report task success improvements from spatial auxiliary supervision but do not include safety metrics. The assumption that spatial awareness should improve safety because the robot ``knows where things are'' remains untested; we address this gap by directly measuring collision avoidance under controlled spatial supervision conditions.\n\n\\subsection{Auxiliary Tasks and Multi-Task Gradient Dynamics}\n\nMulti-task learning exploits shared representations~\\cite{caruana1997multitask, ruder2017overview}, but auxiliary tasks risk negative transfer through optimization conflict or generalization failure~\\cite{chen2018gradnorm, yu2020pcgrad, liu2021cagrad, navon2022nashmtl, jiang2023forkmerge}. PCGrad~\\cite{yu2020pcgrad} projects conflicting task gradients to remove their interfering components, while CAGrad~\\cite{liu2021cagrad} seeks a descent direction within a conflict-averse region that minimizes worst-case task loss. Both assume that gradient conflict is the primary failure mode of multi-task optimization; our gradient analysis shows near-zero cosine similarity between action and auxiliary gradients, suggesting that the mechanism in our setting operates through a different channel.\n\nBatch normalization~\\cite{ioffe2015batchnorm} standardizes activations using mini-batch statistics, coupling each sample's representation to the batch composition. Layer normalization~\\cite{ba2016layernorm} removes this dependence by computing statistics per token, making it the default in transformer architectures, while group normalization~\\cite{wu2018groupnorm} offers a batch-size-independent alternative by normalizing within channel groups. This design choice becomes consequential when auxiliary tasks alter the training distribution: Li et al.~\\cite{li2017adabn} show that recalibrating BN statistics suffices to adapt across domains, and Schneider et al.~\\cite{schneider2020bn} demonstrate that BN running statistics degrade robustness under covariate shift. Our factorial design varies the normalization scheme in the auxiliary head between BatchNorm and LayerNorm, directly testing whether these distributional sensitivities propagate to the primary action objective.\n\nFor VLA fine-tuning with LoRA~\\cite{hu2022lora}, the interaction between auxiliary losses and low-rank adapter updates has not been studied. LoRA constrains updates to a low-rank subspace, which may limit the model's capacity to accommodate competing objectives that full-rank updates could absorb; how this constraint interacts with multi-task gradient dynamics is an open question in the literature. Our factorial design isolates gradient flow from spatial content and identifies a normalization-dependent gradient flow effect that challenges the assumption that auxiliary spatial supervision should improve safety.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 15
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01AUr75HKVV1APEqds4BbjEs`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Warning|Error|Undefined|Missing|Overfull|Underfull|pages\"",
  "description": "Compile LaTeX and check for warnings/errors",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "dbafe76d-01fb-49f8-8790-7646294cb911",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Utk4wU1NTcgwUovQwVyhG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11998,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11998
      },
      "output_tokens": 21,
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

_source line 23 · 2026-05-28T09:45:49.098Z_

<details><summary>↩ Tool result · `toolu_01AUr75HKVV1APEqds4BbjEs`</summary>

```text
Underfull \vbox (badness 5787) has occurred while \output is active [2 <./figur
Underfull \vbox (badness 10000) has occurred while \output is active [6])
Underfull \vbox (badness 4739) has occurred while \output is active [7 <./figur
Underfull \vbox (badness 10000) has occurred while \output is active [8]
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
Underfull \vbox (badness 4454) has occurred while \output is active [13]
LaTeX Warning: `h' float specifier changed to `ht'.
LaTeX Warning: `h' float specifier changed to `ht'.
Output written on main.pdf (19 pages, 459537 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "d5b21048-cc69-4002-a001-62b6b3ea3644",
  "tool_use_result": {
    "stdout": "Underfull \\vbox (badness 5787) has occurred while \\output is active [2 <./figur\nUnderfull \\vbox (badness 10000) has occurred while \\output is active [6])\nUnderfull \\vbox (badness 4739) has occurred while \\output is active [7 <./figur\nUnderfull \\vbox (badness 10000) has occurred while \\output is active [8]\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: `h' float specifier changed to `ht'.\nUnderfull \\vbox (badness 4454) has occurred while \\output is active [13]\nLaTeX Warning: `h' float specifier changed to `ht'.\nLaTeX Warning: `h' float specifier changed to `ht'.\nOutput written on main.pdf (19 pages, 459537 bytes).",
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze all the files I've read and the compilation results. Let me also check for broken references by running a more thorough compilation check.

Let me compile again to check for `??` (broken refs) and count pages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "7e8048a6-9b9c-4049-b825-cb0a94bca37e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGzgknzJLPQrFR1232pjrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19643,
      "cache_read_input_tokens": 23843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19643
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

_source line 25_

需要进一步检查 broken refs 和页数。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "a7362a59-95ef-442d-8f5e-d0bd7538bac6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGzgknzJLPQrFR1232pjrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19643,
      "cache_read_input_tokens": 23843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19643
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01HhiJXHsQuNG2QEykEf3g4p`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Second pass LaTeX compile for refs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "2cf019eb-6512-4ac1-98bb-711a896a937f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGzgknzJLPQrFR1232pjrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19643,
      "cache_read_input_tokens": 23843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19643
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

_source line 27 · 2026-05-28T09:45:56.200Z_

<details><summary>↩ Tool result · `toolu_01HhiJXHsQuNG2QEykEf3g4p`</summary>

```text
/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t
imes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (19 pages, 459537 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "9924a2bc-3914-44c2-bb8e-bfa35194c04b",
  "tool_use_result": {
    "stdout": "/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t\nimes/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (19 pages, 459537 bytes).\nTranscript written on main.log.",
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01P1pqx3FMmCGuRNd7P2cyq9`</summary>

```json
{
  "command": "grep -c '??' main.log 2>/dev/null; grep 'LaTeX Warning.*Reference\\|LaTeX Warning.*Citation\\|undefined' main.log 2>/dev/null | head -20",
  "description": "Check for broken references and undefined citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "91560903-564e-4bf7-8afd-384ef2c9a11b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGzgknzJLPQrFR1232pjrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19643,
      "cache_read_input_tokens": 23843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19643
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

_source line 29 · 2026-05-28T09:45:57.257Z_

<details><summary>↩ Tool result · `toolu_01P1pqx3FMmCGuRNd7P2cyq9`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "c3b689b0-bebf-4f74-b4fc-a9ead7dd0903",
  "tool_use_result": {
    "stdout": "0",
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

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01VfV8vv4kz6LcGsBGpVcs8q`</summary>

```json
{
  "command": "bibtex main 2>&1 | head -30",
  "description": "Run bibtex to resolve citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "25932efd-9477-4f85-a990-6ea110c7d364",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGzgknzJLPQrFR1232pjrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19643,
      "cache_read_input_tokens": 23843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19643
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

_source line 31 · 2026-05-28T09:45:57.974Z_

<details><summary>↩ Tool result · `toolu_01VfV8vv4kz6LcGsBGpVcs8q`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: corlabbrvnat.bst
Database file #1: references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "2d672e2a-bf65-4d71-bb65-08258002324a",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: corlabbrvnat.bst\nDatabase file #1: references.bib",
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

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_016Z5zcS48c2g3JDq8mSdiwB`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Warning.*Ref|Warning.*Cit|Undefined|Missing|Output written\"",
  "description": "Full compile chain with bibtex resolved"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "ce828028-78c9-4312-be88-e58112af18c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VaTXoSUi2gpTzgXdR4VrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 43486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 643
      },
      "output_tokens": 38,
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

_source line 33 · 2026-05-28T09:46:04.867Z_

<details><summary>↩ Tool result · `toolu_016Z5zcS48c2g3JDq8mSdiwB`</summary>

```text
Output written on main.pdf (19 pages, 459537 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "f0971357-7887-47b2-a4d4-68593b79e32d",
  "tool_use_result": {
    "stdout": "Output written on main.pdf (19 pages, 459537 bytes).",
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_012tf3KZAbLEGPmYUTVARKPs`</summary>

```json
{
  "command": "grep -n 'TODO\\|TBD\\|placeholder\\|FIXME\\|XXX\\|X\\.XX' appendix.tex method.tex results.tex discussion.tex introduction.tex conclusion.tex main.tex related_work.tex",
  "description": "Check for TODO/placeholder remnants"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "80d96005-f9ff-465e-910c-5e7cb671aa05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VaTXoSUi2gpTzgXdR4VrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 43486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 643
      },
      "output_tokens": 38,
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

_source line 35 · 2026-05-28T09:46:05.174Z_

<details><summary>↩ Tool result · `toolu_012tf3KZAbLEGPmYUTVARKPs`</summary>

```text
appendix.tex:116:\textbf{Cross-benchmark Vanilla baseline.} Vanilla baseline on LIBERO-Object achieves CAR \textbf{X.XX} ($n{=}2$), confirming that the safety gap between TSR and CAR is not specific to LIBERO-Spatial.
appendix.tex:117:% TODO: fill X.XX with vanilla_object eval data (~08:45 UTC)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "bb4abc52-c61e-4bef-83f8-74f3ff3bba49",
  "tool_use_result": {
    "stdout": "appendix.tex:116:\\textbf{Cross-benchmark Vanilla baseline.} Vanilla baseline on LIBERO-Object achieves CAR \\textbf{X.XX} ($n{=}2$), confirming that the safety gap between TSR and CAR is not specific to LIBERO-Spatial.\nappendix.tex:117:% TODO: fill X.XX with vanilla_object eval data (~08:45 UTC)",
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01RmE2GRrpVjgcLyiaPdGx4m`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -c \"Overfull\\|Underfull\"",
  "description": "Count overfull/underfull warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "6ee4095b-a2f7-4218-b61f-5bb03ff13797",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VaTXoSUi2gpTzgXdR4VrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 43486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 643
      },
      "output_tokens": 38,
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

_source line 37 · 2026-05-28T09:46:07.032Z_

<details><summary>↩ Tool result · `toolu_01RmE2GRrpVjgcLyiaPdGx4m`</summary>

```text
5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "90d7d04d-7220-4d70-b7fe-09683fadaa3a",
  "tool_use_result": {
    "stdout": "5",
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

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information. Let me compile the full analysis.

Let me go through each check item:

## 1. Notation 一致性

Let me check:
- CAR: Collision Avoidance Rate - defined in introduction.tex line 3 ("Collision Avoidance Rate (CAR)") ✓
- TSR: Task Success Rate - defined in introduction.tex line 3 ("Task Success Rate (TSR)") ✓
- VLA: Vision-Language-Action - defined in introduction.tex line 2 ("Vision-language-action (VLA) models") ✓


- OCC: appears in condition names like "Full OCC" and "Detach OCC" but isn't formally defined as an abbreviation, though it's used contextually for "occupancy"
- BN: BatchNorm - properly introduced in the abstract as "Batch Normalization (BN)" ✓
- LN: LayerNorm - properly introduced in the abstract as "Layer Normalization (LN)" ✓
- ANOVA: used throughout without explicit definition, though it's a standard statistical term typically assumed to be known in ML papers
- η² (eta-squared): standard statistical notation for effect size, used in the abstract and throughout
- d (Cohen's d): standard effect size notation appearing in the abstract
- LoRA: cited in method.tex but the acronym itself isn't expanded in the text, though it's a well-established technique with a citation provided
- CKA: appears to be defined in results.tex around line 82 with a citation, though the definition seems to be cut off

. I should check if it's expanded elsewhere—looks like it might be in the appendix as "Centered Kernel Alignment" but not in the main text where it first appears
- BEV: used in method.tex as "BEV occupancy head" but never explicitly expanded to "Bird's Eye View," even though the concept appears in related work discussing bird's-eye-view estimation

. It's a common abbreviation, but the formal definition is missing from where it's first introduced
- Now checking the formatting of mathematical notation like `$n{=}3$` versus `$n=3$` across the document—the abstract and results sections use the spaced version consistently, but the appendix has mixed formatting
- Verifying other notation patterns like percentage points with `\,pp` and the equals sign format in expressions like `$d{=}$` all appear uniform throughout

.

Now checking the figure captions against the data. The overview figure lists five conditions with their corresponding accuracy values, and I'm cross-referencing these against Table 1 to confirm they match—Full OCC BN at 0.725, Vanilla at 0.745, Detach OCC at 0.767, Full OCC+LN at 0.773, and Detach+LN at 0.802±0.024 with n=3, all checking out correctly.

For the factorial figure, I'm verifying the effect sizes mentioned in the caption. The BN row shows a 4.2 percentage point reduction in CAR with d=0.93, which matches the difference between 0.767 and 0.725. The LN row shows 2.9 percentage points with d=1.12, confirmed by the difference between 0.802 and 0.773, and the effect size aligns with the pairwise comparison table. The remaining figures on gradient analysis and per-layer results are consistent with their descriptions in the appendix.

Now I'm checking the dose response figure caption against the data—the Cutoff@15K annotation shows a +0.2 percentage point improvement over vanilla, which matches the table values of 0.782 versus 0.780. All figure references throughout the document are properly linked with no broken citations. Moving into the appendix completeness check, the ANOVA table includes all necessary statistical columns: Source, F-statistic, degrees of freedom, p-value, and effect size. Finishing up the pairwise comparisons with the remaining cell-versus-vanilla contrasts, which completes all ten comparisons. Now I'm noticing a critical issue in the appendix where there's a placeholder value and TODO comment that needs to be fixed. Moving into the related work section, I'm checking coverage of major vision-language action models and realizing Octo isn't cited anywhere despite being mentioned in the introduction—I need to verify whether it should be included in the related work discussion. but not Octo specifically.

Actually, let me reconsider - the task says to check if these areas have "citation coverage", not if specific papers are cited. Octo is not cited but there are plenty of VLA citations. However, Octo is a notable VLA model that probably should be cited.

- Safe RL / constrained RL: zhang2025safevla ✓, hu2025vlsa ✓, zhai2026cofreevla ✓, raja2024ogmcbf ✓. But these are more "safe VLA" than general "safe RL / constrained RL". There's no citation of foundational safe RL work (e.g., CPO, CMDP literature). The related_work.tex doesn't have a "safe RL" subsection - it's integrated into the VLA safety subsection.

- Multi-task learning and auxiliary tasks are well covered with citations spanning foundational work through recent gradient-based optimization methods. Occupancy prediction in robotics also has solid coverage across vision-based approaches. Gradient flow and interference between tasks are addressed through the same optimization papers.

Now checking normalization techniques - batch norm, layer norm, group norm, and adaptive batch norm all have citations. The compilation shows 19 pages total, which exceeds typical workshop constraints of 4-8 pages for the main paper.

The critical issue is a placeholder value in the appendix that needs to be filled in. I also need to verify that CKA and BEV are properly defined on first use in the main text, and confirm whether Octo is cited where needed.

Looking more closely at the effect size values, there's an inconsistency between what the abstract reports and what appears in the introduction. The abstract states d≈1.05–1.47 for the BN-LN comparison, but the introduction cites d≈1.03 in two places. Checking against the pairwise table, the actual values are d=1.05 and d=1.47, so the introduction's approximation of 1.03 doesn't match either the abstract or the table data.

Now I'm noticing another discrepancy in the discussion section—it references d=1.03 when describing the 4.8 percentage point advantage, but the results section clearly states this same comparison has d=1.05. So there's a numerical error where the discussion is citing 1.03 instead of the correct 1.05 value. but 1.03 doesn't match either of those values. It might be coming from a different calculation entirely, like the main effect size from the ANOVA rather than the pairwise comparisons. The abstract and table captions correctly cite d≈1.05–1.47, so the error is isolated to the introduction and discussion sections where 1.03 appears—it should be updated to match the pairwise table values.

Now I'm systematically checking the other effect sizes reported throughout the paper. The Cohen's d = -0.93 for the BN gradient flow effect is consistent across the abstract and results. The d = +1.07 comparison against Vanilla checks out against the pairwise table. The interaction effect η² < 0.01 is correctly reported as <0.01 when the actual value is 0.005. The standard deviation claim that σ = 0.064 is at least twice all other cells also holds up—the other cells range from 0.024 to 0.027, so the inequality is satisfied.

I'm now verifying the specific comparisons the paper makes about BatchNorm's effect on gradient flow. The d = -0.93 value refers to the Full OCC BN versus Detach OCC BN comparison, not versus Vanilla, which is an important distinction for understanding what the paper is actually claiming about the gradient flow degradation. Cohen's $d{=}-0.93$, large)" - this is BN flow ON vs OFF, so Cell 1 vs Cell 3 ✓.

Results line 49: "Full OCC+LN already exceeds Vanilla ($0.773$, $\Delta{=}+2.8$\,pp, $d{=}+1.07$, large)" - Cell 2 vs Vanilla ✓.

Results line 49: "Detach+LN yields the highest cell mean ($0.802 \pm 0.024$, $n{=}3$, $\Delta{=}+5.7$\,pp, $d{=}+2.36$, very large)" - Cell 4 vs Vanilla ✓ (pairwise shows +2.36).

All the effect sizes check out against the pairwise comparisons, so I'm not finding any major numerical inconsistencies in how the results are reported.

Actually, wait—there's one discrepancy I keep running into: the intro and discussion mention $d \approx 1.03$ for the normalization main effect, but the pairwise table and results section consistently show $d = 1.05$ for the Cell 1 vs Cell 2 comparison. This could be a stale value from an earlier version of the analysis, or possibly a different computation altogether like an ANOVA effect size, though the paper reports η² for those. Most likely just a typo that slipped through. Let me put together the full report now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "51fc4a64-4d54-4d30-981e-bde09c6b2ce4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLDaKF6fqeKVUkJxoPbqqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 44129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
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

_source line 39_

Now let me check the page breakdown more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "d2e044be-e1f4-4a32-9394-1c4e1d0fb9d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLDaKF6fqeKVUkJxoPbqqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 44129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01Lz9HheUFmTFFZYnv2fQSa3`</summary>

```json
{
  "command": "grep -n '\\\\\\\\section\\|\\\\\\\\appendix\\|\\\\\\\\clearpage' main.tex appendix.tex introduction.tex method.tex results.tex discussion.tex conclusion.tex related_work.tex 2>/dev/null",
  "description": "Find section boundaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "183ac1d8-39ac-4230-84cc-7f3ab26fe33b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLDaKF6fqeKVUkJxoPbqqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 44129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
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

_source line 41 · 2026-05-28T09:47:47.366Z_

<details><summary>↩ Tool result · `toolu_01Lz9HheUFmTFFZYnv2fQSa3`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "de6699f3-063f-4005-9b01-e1fc47728aa9",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01HvnghPu6jXi1Bkt1bEzwEg`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -oP '\\[\\d+' | tail -1",
  "description": "Get total page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "55601836-4224-4dc8-9698-8991f8e4af61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLDaKF6fqeKVUkJxoPbqqv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 44129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
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

_source line 43 · 2026-05-28T09:47:49.150Z_

<details><summary>↩ Tool result · `toolu_01HvnghPu6jXi1Bkt1bEzwEg`</summary>

```text
[19
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "8af03ecf-5e5a-4a0d-8de0-f1b2a7c1d0a9",
  "tool_use_result": {
    "stdout": "[19",
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_012CJp1GdeBKmZbYzxEnhVaf`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -oP '\\[\\d+' | tr -d '['",
  "description": "List all page numbers emitted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "0ec68817-6981-40fa-b4fb-473dfabd013f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYCaDzopSi621k94R5NdWC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5403,
      "cache_read_input_tokens": 44681,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5403
      },
      "output_tokens": 38,
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

_source line 45 · 2026-05-28T09:47:54.243Z_

<details><summary>↩ Tool result · `toolu_012CJp1GdeBKmZbYzxEnhVaf`</summary>

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "47f1c997-3f4e-4705-b101-9e7e927eb3bf",
  "tool_use_result": {
    "stdout": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19",
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

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01Bk5qqiwWjyNwdwgBGUphmf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "c93815cf-97f9-45e8-a441-5a0c2e05138b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhnTR9tnBdCBedKy5SRYA8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 157,
      "cache_read_input_tokens": 50084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 157
      },
      "output_tokens": 38,
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

_source line 47 · 2026-05-28T09:47:58.078Z_

<details><summary>↩ Tool result · `toolu_01Bk5qqiwWjyNwdwgBGUphmf`</summary>

```text
1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "70e3fd8d-5cb6-45a0-bff3-1e948015ec65",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib",
      "content": "% References for OccSafe-VLA\n% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}\n\n% ============================================================\n% VLA Safety\n% ============================================================\n\n@article{hu2025vlsa,\n  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},\n  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  journal   = {arXiv preprint arXiv:2512.11891},\n  year      = {2025},\n  note      = {arXiv:2512.11891}\n}\n\n@inproceedings{zhang2025safevla,\n  author    = {Borong Zhang and others},\n  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2025},",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 439
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Grep · `toolu_01VHNGmpjPw6hTvuuTj8wKwA`</summary>

```json
{
  "pattern": "octo|team2024octo",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
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
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "5407c4a5-ad1b-41ed-aeb8-e15732f1ff8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017q7rYx8EGqLJ4FiC4RKnJD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 420,
      "cache_read_input_tokens": 50241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 420
      },
      "output_tokens": 35,
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

_source line 49 · 2026-05-28T09:48:01.907Z_

<details><summary>↩ Tool result · `toolu_01VHNGmpjPw6hTvuuTj8wKwA`</summary>

```text
aaai.bst:276:MACRO {oct} {"October"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "febfa971-4eda-4d2c-80bf-1847f5f50d44",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "aaai.bst:276:MACRO {oct} {\"October\"}",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
OK, Octo is not cited anywhere in the paper. Let me now compile the full report.

Let me also double-check the d≈1.03 inconsistency more carefully by searching for it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "da2be392-a711-4547-97cd-65f4548d01e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMJGpviJB8EpSALWxi6VnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 50661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 171
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

<details open><summary>🔧 Tool call — Grep · `toolu_01QDH5FySGoLZovATHbt2KiF`</summary>

```json
{
  "pattern": "1\\.03",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
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
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "95384059-f930-4d04-8077-e3500d3ed732",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WMJGpviJB8EpSALWxi6VnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 171,
      "cache_read_input_tokens": 50661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 171
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

_source line 52 · 2026-05-28T09:48:05.898Z_

<details><summary>↩ Tool result · `toolu_01QDH5FySGoLZovATHbt2KiF`</summary>

```text
introduction.tex:16:[Omitted long matching line]
introduction.tex:20:[Omitted long matching line]
discussion.tex:8:\textbf{Normalization independently affects safety.} LN provides a consistent safety advantage over BN ($+$4.8\,pp under gradient flow, $d{=}1.03$; $+$3.5\,pp without), comparable in magnitude to the gradient flow effect. For practitioners who must retain gradient flow, LayerNorm converts the BN safety deficit into a gain, an architectural advantage, since label content does not detectably affect outcomes.
conclusion.tex:4:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "ad6c6ec5-0109-4033-9365-490549c24627",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "introduction.tex:16:[Omitted long matching line]\nintroduction.tex:20:[Omitted long matching line]\ndiscussion.tex:8:\\textbf{Normalization independently affects safety.} LN provides a consistent safety advantage over BN ($+$4.8\\,pp under gradient flow, $d{=}1.03$; $+$3.5\\,pp without), comparable in magnitude to the gradient flow effect. For practitioners who must retain gradient flow, LayerNorm converts the BN safety deficit into a gain, an architectural advantage, since label content does not detectably affect outcomes.\nconclusion.tex:4:[Omitted long matching line]",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Grep · `toolu_014UdJW4ZBhPCKLBeWZZUHpS`</summary>

```json
{
  "pattern": "1\\.05",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
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
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "7c916cc5-babe-4891-9d6a-daba9c03e2cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVDWCseRV1ur6pNLNbwjM5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 359,
      "cache_read_input_tokens": 50832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 359
      },
      "output_tokens": 64,
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

_source line 54 · 2026-05-28T09:48:08.912Z_

<details><summary>↩ Tool result · `toolu_014UdJW4ZBhPCKLBeWZZUHpS`</summary>

```text
main.tex:27:[Omitted long matching line]
appendix.tex:167:Cell~1 (Full OCC BN) vs.\ Cell~2 (Full OCC+LN) & $-$1.05 \\
results.tex:49:[Omitted long matching line]
results.tex:55:\caption{$2{\times}2$ factorial: normalization type $\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $d{=}0.93$ (large); normalization effect $d{=}1.05$--$1.47$ (large to very large). BN + gradient flow is the sole cell below Vanilla. ANOVA interaction $F{<}0.1$, $p{=}0.76$.}
results.tex:64:$\Delta$(BN$-$LN) & $-$4.8 ($d{=}{-}1.05$) & $-$3.5 ($d{=}{-}1.47$) & --- \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "ed7e95b5-cb46-4fd0-9934-a62ab8a7c536",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "main.tex:27:[Omitted long matching line]\nappendix.tex:167:Cell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$1.05 \\\\\nresults.tex:49:[Omitted long matching line]\nresults.tex:55:\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $d{=}0.93$ (large); normalization effect $d{=}1.05$--$1.47$ (large to very large). BN + gradient flow is the sole cell below Vanilla. ANOVA interaction $F{<}0.1$, $p{=}0.76$.}\nresults.tex:64:$\\Delta$(BN$-$LN) & $-$4.8 ($d{=}{-}1.05$) & $-$3.5 ($d{=}{-}1.47$) & --- \\\\",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_01U9MBCub9hTMWxZb5yRzfNf`</summary>

```json
{
  "pattern": "\\\\\\\\label|\\\\\\\\ref",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "f4fea369-e58a-4517-b615-bde1498f063c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHUGrgRoAkxcrXJPRb1ZJr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 51191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 399
      },
      "output_tokens": 42,
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

_source line 56 · 2026-05-28T09:48:12.332Z_

<details><summary>↩ Tool result · `toolu_01U9MBCub9hTMWxZb5yRzfNf`</summary>

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
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "87c31068-2b05-4f79-a5a3-08370c73c637",
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

_source line 57_

<details open><summary>🔧 Tool call — Grep · `toolu_01Egmq4mbGo5yhbm6UiUWL6c`</summary>

```json
{
  "pattern": "label\\{|\\\\ref\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "df614574-c82d-4593-b80d-a87be9acfbb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5aLYmjbJxtmke7g8tJDXc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 51590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 175
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

_source line 58 · 2026-05-28T09:48:15.714Z_

<details><summary>↩ Tool result · `toolu_01Egmq4mbGo5yhbm6UiUWL6c`</summary>

```text
discussion.tex:3:\label{sec:discussion}
discussion.tex:4:\label{sec:why_gradient}
discussion.tex:10:[Omitted long matching line]
discussion.tex:12:[Omitted long matching line]
discussion.tex:16:[Omitted long matching line]
discussion.tex:20:\textbf{Practical guideline.} Do not add auxiliary spatial heads for safety purposes. If required, use detached gradients with LayerNorm; avoid combining BatchNorm with gradient flow. No ground-truth labels are needed; the head is discarded at zero inference cost, complementing runtime methods~\cite{hu2025vlsa, raja2024ogmcbf}. Limitations are in Appendix~\ref{app:limitations}.
method.tex:16:\label{sec:ablation}
method.tex:20:[Omitted long matching line]
method.tex:29:\label{tab:ablation_design}
method.tex:49:[Omitted long matching line]
method.tex:51:[Omitted long matching line]
appendix.tex:3:\label{app:per_task}
appendix.tex:5:Table~\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.
appendix.tex:9:\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}
appendix.tex:10:\label{tab:per_task}
appendix.tex:38:\label{app:training}
appendix.tex:74:\textbf{Cutoff implementation.} As described in Section~\ref{sec:ablation}, setting $\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).
appendix.tex:82:\label{fig:gradient_analysis}
appendix.tex:85:The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \texttt{stop\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \pm 0.024$ (Table~\ref{tab:main_results}), the highest factorial cell mean ($\Delta{=}+5.7$\,pp vs.\ Vanilla, $d{=}+2.36$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.
appendix.tex:87:[Omitted long matching line]
appendix.tex:92:[Omitted long matching line]
appendix.tex:93:\label{fig:per_layer_combined}
appendix.tex:97:\label{app:temporal}
appendix.tex:98:[Omitted long matching line]
appendix.tex:104:\label{fig:dose_response}
appendix.tex:108:\label{app:additional}
appendix.tex:110:[Omitted long matching line]
appendix.tex:114:[Omitted long matching line]
appendix.tex:120:\label{app:codebase}
appendix.tex:124:[Omitted long matching line]
appendix.tex:133:\label{app:stat_power}
appendix.tex:139:[Omitted long matching line]
appendix.tex:144:\label{tab:anova}
appendix.tex:156:\textbf{Pairwise effect sizes.} Table~\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).
appendix.tex:161:\label{tab:pairwise}
appendix.tex:183:\label{app:per_task_factorial}
appendix.tex:194:\label{app:limitations}
experiments_old.tex:9:[Omitted long matching line]
experiments_old.tex:30:All conditions share the same base model: OpenVLA-OFT 7B~\cite{kim2025oft}, pre-trained on Open X-Embodiment. We fine-tune with LoRA (rank 32, $\alpha{=}16$) for 50K steps using AdamW (weight decay $0.01$), a batch size of 8, a constant learning rate of $5 \times 10^{-4}$, and 2--4 random seeds per condition (see Table~\ref{tab:main_results}). The LoRA adapter adds 110.8M trainable parameters (1.45\% of 7.65B total).
introduction.tex:11:\label{fig:overview}
introduction.tex:14:[Omitted long matching line]
introduction.tex:16:[Omitted long matching line]
introduction.tex:20:[Omitted long matching line]
introduction.tex:22:    \item \textbf{Factorial methodology for VLA auxiliary heads.} We introduce the first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning. This design can detect combined effects that single-factor ablations would miss (\S\ref{sec:ablation}, Table~\ref{tab:ablation_design}).
introduction.tex:24:[Omitted long matching line]
results.tex:3:\label{sec:results}
results.tex:7:[Omitted long matching line]
results.tex:17:\label{tab:main_results}
results.tex:45:\label{sec:mechanism}
results.tex:47:The four factorial cells form a $2{\times}2$ design crossing normalization type (BN/LN) with gradient flow (ON/OFF) (Table~\ref{tab:factorial}, Figure~\ref{fig:factorial}).
results.tex:49:[Omitted long matching line]
results.tex:51:Pairwise Welch $t$-tests with Bonferroni correction yield no significant comparisons at $\alpha{=}0.05$, consistent with small per-cell $n$ ($n{=}3$--$4$); we rely on effect sizes rather than $p$-values for inference (Appendix~\ref{app:stat_power}). The normalization main effect approaches significance ($p{=}0.060$). Both main effects amplify by ${\approx}3{\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\ref{app:per_task_factorial}).
results.tex:56:\label{tab:factorial}
results.tex:73:\label{fig:factorial}
results.tex:78:Gradient analysis (Figure~\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).
results.tex:84:Additional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\ref{app:additional}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "0934a81f-81bb-43eb-b104-67c6ff4f107f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "discussion.tex:3:\\label{sec:discussion}\ndiscussion.tex:4:\\label{sec:why_gradient}\ndiscussion.tex:10:[Omitted long matching line]\ndiscussion.tex:12:[Omitted long matching line]\ndiscussion.tex:16:[Omitted long matching line]\ndiscussion.tex:20:\\textbf{Practical guideline.} Do not add auxiliary spatial heads for safety purposes. If required, use detached gradients with LayerNorm; avoid combining BatchNorm with gradient flow. No ground-truth labels are needed; the head is discarded at zero inference cost, complementing runtime methods~\\cite{hu2025vlsa, raja2024ogmcbf}. Limitations are in Appendix~\\ref{app:limitations}.\nmethod.tex:16:\\label{sec:ablation}\nmethod.tex:20:[Omitted long matching line]\nmethod.tex:29:\\label{tab:ablation_design}\nmethod.tex:49:[Omitted long matching line]\nmethod.tex:51:[Omitted long matching line]\nappendix.tex:3:\\label{app:per_task}\nappendix.tex:5:Table~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\nappendix.tex:9:\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\nappendix.tex:10:\\label{tab:per_task}\nappendix.tex:38:\\label{app:training}\nappendix.tex:74:\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\nappendix.tex:82:\\label{fig:gradient_analysis}\nappendix.tex:85:The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $d{=}+2.36$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\nappendix.tex:87:[Omitted long matching line]\nappendix.tex:92:[Omitted long matching line]\nappendix.tex:93:\\label{fig:per_layer_combined}\nappendix.tex:97:\\label{app:temporal}\nappendix.tex:98:[Omitted long matching line]\nappendix.tex:104:\\label{fig:dose_response}\nappendix.tex:108:\\label{app:additional}\nappendix.tex:110:[Omitted long matching line]\nappendix.tex:114:[Omitted long matching line]\nappendix.tex:120:\\label{app:codebase}\nappendix.tex:124:[Omitted long matching line]\nappendix.tex:133:\\label{app:stat_power}\nappendix.tex:139:[Omitted long matching line]\nappendix.tex:144:\\label{tab:anova}\nappendix.tex:156:\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Cohen's $d$ for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\nappendix.tex:161:\\label{tab:pairwise}\nappendix.tex:183:\\label{app:per_task_factorial}\nappendix.tex:194:\\label{app:limitations}\nexperiments_old.tex:9:[Omitted long matching line]\nexperiments_old.tex:30:All conditions share the same base model: OpenVLA-OFT 7B~\\cite{kim2025oft}, pre-trained on Open X-Embodiment. We fine-tune with LoRA (rank 32, $\\alpha{=}16$) for 50K steps using AdamW (weight decay $0.01$), a batch size of 8, a constant learning rate of $5 \\times 10^{-4}$, and 2--4 random seeds per condition (see Table~\\ref{tab:main_results}). The LoRA adapter adds 110.8M trainable parameters (1.45\\% of 7.65B total).\nintroduction.tex:11:\\label{fig:overview}\nintroduction.tex:14:[Omitted long matching line]\nintroduction.tex:16:[Omitted long matching line]\nintroduction.tex:20:[Omitted long matching line]\nintroduction.tex:22:    \\item \\textbf{Factorial methodology for VLA auxiliary heads.} We introduce the first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning. This design can detect combined effects that single-factor ablations would miss (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).\nintroduction.tex:24:[Omitted long matching line]\nresults.tex:3:\\label{sec:results}\nresults.tex:7:[Omitted long matching line]\nresults.tex:17:\\label{tab:main_results}\nresults.tex:45:\\label{sec:mechanism}\nresults.tex:47:The four factorial cells form a $2{\\times}2$ design crossing normalization type (BN/LN) with gradient flow (ON/OFF) (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial}).\nresults.tex:49:[Omitted long matching line]\nresults.tex:51:Pairwise Welch $t$-tests with Bonferroni correction yield no significant comparisons at $\\alpha{=}0.05$, consistent with small per-cell $n$ ($n{=}3$--$4$); we rely on effect sizes rather than $p$-values for inference (Appendix~\\ref{app:stat_power}). The normalization main effect approaches significance ($p{=}0.060$). Both main effects amplify by ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}).\nresults.tex:56:\\label{tab:factorial}\nresults.tex:73:\\label{fig:factorial}\nresults.tex:78:Gradient analysis (Figure~\\ref{fig:gradient_analysis}, Appendix) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\nresults.tex:84:Additional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.",
    "numLines": 56
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Let me also check if CKA is expanded at first use in the main text. The first main-text occurrence is in results.tex line 82 ("CKA analysis"), then discussion.tex line 6 ("CKA analysis"). The expansion "Centered Kernel Alignment" appears only in appendix.tex line 72. That's an issue - CKA should be expanded on first use in main text.

Also, BEV is used in method.tex without expansion. Related_work.tex says "bird's-eye-view estimation" in the context of BEVFormer, but BEV itself isn't formally defined as "Bird's-Eye View (BEV)".


I'm also noticing that discussion.tex has duplicate labels on lines 3-4 — one for the section itself and another labeled `sec:why_gradient` that doesn't appear to be referenced anywhere in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "30406dcc-6937-448c-ab2f-e6c2bd000381",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbJQdj1My9QutHiZ9Tx5Jd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2029,
      "cache_read_input_tokens": 51765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2029
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

_source line 60_

<details open><summary>🔧 Tool call — Grep · `toolu_01K2ViyTk1P1ch7J38WYXUZM`</summary>

```json
{
  "pattern": "sec:why_gradient",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
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
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "7e6ebbfb-d329-4467-a7a3-79a907ec6200",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbJQdj1My9QutHiZ9Tx5Jd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2029,
      "cache_read_input_tokens": 51765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2029
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

_source line 61 · 2026-05-28T09:48:24.856Z_

<details><summary>↩ Tool result · `toolu_01K2ViyTk1P1ch7J38WYXUZM`</summary>

```text
discussion.tex:4:\label{sec:why_gradient}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "f5d7072c-eb6a-4b76-8fdc-0d8cc04110bb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "discussion.tex:4:\\label{sec:why_gradient}",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Grep · `toolu_01Fu4UL5wt6sykDFrXtjngk3`</summary>

```json
{
  "pattern": "CKA|Centered Kernel",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
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
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "de52c750-97ce-4e4a-b90a-fa69edca38a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Q7oHR6ZRvjzXAiACP1yZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 396,
      "cache_read_input_tokens": 53794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 396
      },
      "output_tokens": 62,
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

_source line 63 · 2026-05-28T09:48:28.041Z_

<details><summary>↩ Tool result · `toolu_01Fu4UL5wt6sykDFrXtjngk3`</summary>

```text
conclusion.tex:4:[Omitted long matching line]
discussion.tex:6:[Omitted long matching line]
appendix.tex:72:\textbf{CKA analysis.} Centered Kernel Alignment~\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.
appendix.tex:196:[Omitted long matching line]
results.tex:82:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "3f542e67-9751-48b7-9377-d04471285590",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "conclusion.tex:4:[Omitted long matching line]\ndiscussion.tex:6:[Omitted long matching line]\nappendix.tex:72:\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\nappendix.tex:196:[Omitted long matching line]\nresults.tex:82:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 64_

全部信息已收集完毕。以下是检查报告：

---

## 1. Notation 一致性

- **[ISSUE]** **d≈1.03 vs d=1.05 不一致**：`introduction.tex:16`, `introduction.tex:20`, `discussion.tex:8`, `conclusion.tex:4` 使用 `d≈1.03`，但 `results.tex:49`, `results.tex:64`, `appendix.tex:167` (pairwise table) 给出的 Cell 1 vs Cell 2 精确值为 `d=1.05`。Abstract 正确使用 `d≈1.05--1.47`。需统一为 `1.05`。

- **[ISSUE]** **CKA 首次使用未展开**：CKA 首次出现在 `results.tex:82`（主文），但 "Centered Kernel Alignment" 仅在 `appendix.tex:72` 展开。应在主文首次出现时写 "Centered Kernel Alignment (CKA)"。

- **[ISSUE]** **BEV 未正式定义**：BEV 在 `method.tex:11` 首次使用（"BEV occupancy head"），但未展开为 "Bird's-Eye View (BEV)"。`related_work.tex` 提到 "bird's-eye-view" 但不是作为 BEV 的正式定义。

- **[OK]** CAR (Collision Avoidance Rate)：`introduction.tex:3` 首次定义 ✓
- **[OK]** TSR (Task Success Rate)：`introduction.tex:3` 首次定义 ✓
- **[OK]** VLA (Vision-Language-Action)：`introduction.tex:2` 首次定义 ✓
- **[OK]** BN/LN：abstract 中定义 ✓
- **[OK]** 数学格式统一：`$n{=}3$`, `$d{=}$`, `$\sigma{=}$`, `\,pp` 全文一致 ✓
- **[OK]** η², Cohen's d 等统计符号一致 ✓

- **[MINOR]** `discussion.tex:4` 有未引用的 `\label{sec:why_gradient}`，可删除。

## 2. Figure Caption

- **[OK]** Fig 1 (`fig:overview`) 数值与 Table 1 一致：0.725, 0.745, 0.767, 0.773, 0.802±0.024 n=3 ✓
- **[OK]** Fig 2 (`fig:factorial`) 4.2pp (d=0.93) 和 2.9pp (d=1.12) 与 Table 数据一致 ✓
- **[OK]** Fig 3 (`fig:gradient_analysis`) 描述与正文一致 ✓
- **[OK]** Fig 4 (`fig:per_layer_combined`) 标注 v1 codebase ✓
- **[OK]** Fig 5 (`fig:dose_response`) "+0.2%" 注释 (0.782-0.780) ✓
- **[OK]** 所有 `\label` / `\ref` 对齐，无 broken ref ✓

## 3. Appendix 完整性

- **[CRITICAL]** `appendix.tex:116`: **X.XX 占位符未填**："Vanilla baseline on LIBERO-Object achieves CAR **X.XX**"，对应 `% TODO: fill X.XX with vanilla_object eval data`。

- **[OK]** ANOVA table (`tab:anova`)：Source/F/df/p/η² 五列完整 ✓
- **[OK]** Pairwise table (`tab:pairwise`)：6 个 cell 间对比 + 4 个 vs Vanilla = 10 对完整 ✓
- **[OK]** 其余无 TODO/TBD/placeholder 残留

## 4. Related Work 引用

- **[OK]** VLA 模型：OpenVLA ✓, RT-2 ✓, OFT ✓, SpatialVLA ✓, DepthVLA ✓, OccVLA ✓, + 15+ 其他 spatial VLA 方法
- **[OK]** 安全机器人/VLA 安全：VLSA ✓, SafeVLA ✓, CoFreeVLA ✓, OGM-CBF ✓
- **[OK]** 多任务学习/梯度干扰：Caruana97 ✓, Ruder17 ✓, GradNorm ✓, PCGrad ✓, CAGrad ✓, Nash-MTL ✓, ForkMerge ✓
- **[OK]** Occupancy prediction：BEVFormer ✓, OccNet ✓, Occ3D ✓
- **[OK]** BN/LN 相关：Ioffe15 ✓, Ba16 ✓, GroupNorm ✓, AdaBN ✓, Schneider20 ✓
- **[MINOR]** Octo 未引用——作为主流 VLA 模型之一，建议在 intro 或 related work 中加入。非必须但推荐。

## 5. 编译质量

- **Errors: 0**
- **Warnings: 5**（3× `h` float specifier → `ht`；5× Underfull vbox — 均为页面布局问题，非致命）
- **Broken refs: 0**
- **Undefined citations: 0**
- **页数: 19**（正文约 8 页 + 附录 11 页）

---

### 需要修复的问题（按优先级）

| # | 严重度 | 位置 | 问题 |
|---|--------|------|------|
| 1 | **CRITICAL** | `appendix.tex:116-117` | **X.XX** 占位符 + TODO 注释，需填入 LIBERO-Object 数据或删除该段 |
| 2 | **HIGH** | intro×2, discussion×1, conclusion×1 | `d≈1.03` 应为 `d≈1.05`（与 pairwise table 一致） |
| 3 | **MEDIUM** | `results.tex:82` | CKA 首次出现需展开为 "Centered Kernel Alignment (CKA)" |
| 4 | **MEDIUM** | `method.tex:11` | BEV 需展开为 "bird's-eye view (BEV)" |
| 5 | **LOW** | `discussion.tex:4` | 未引用 label `sec:why_gradient` 可删 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "uuid": "15718618-b570-48cf-a63b-ebde343caa0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDbxFjomjttP9jRutgPAeS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 54190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 320
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

_source line 65_

全部信息已收集完毕。以下是检查报告：

---

## 1. Notation 一致性

- **[ISSUE]** **d≈1.03 vs d=1.05 不一致**：`introduction.tex:16`, `introduction.tex:20`, `discussion.tex:8`, `conclusion.tex:4` 使用 `d≈1.03`，但 `results.tex:49`, `results.tex:64`, `appendix.tex:167` (pairwise table) 给出的 Cell 1 vs Cell 2 精确值为 `d=1.05`。Abstract 正确使用 `d≈1.05--1.47`。需统一为 `1.05`。

- **[ISSUE]** **CKA 首次使用未展开**：CKA 首次出现在 `results.tex:82`（主文），但 "Centered Kernel Alignment" 仅在 `appendix.tex:72` 展开。应在主文首次出现时写 "Centered Kernel Alignment (CKA)"。

- **[ISSUE]** **BEV 未正式定义**：BEV 在 `method.tex:11` 首次使用（"BEV occupancy head"），但未展开为 "Bird's-Eye View (BEV)"。`related_work.tex` 提到 "bird's-eye-view" 但不是作为 BEV 的正式定义。

- **[OK]** CAR (Collision Avoidance Rate)：`introduction.tex:3` 首次定义 ✓
- **[OK]** TSR (Task Success Rate)：`introduction.tex:3` 首次定义 ✓
- **[OK]** VLA (Vision-Language-Action)：`introduction.tex:2` 首次定义 ✓
- **[OK]** BN/LN：abstract 中定义 ✓
- **[OK]** 数学格式统一：`$n{=}3$`, `$d{=}$`, `$\sigma{=}$`, `\,pp` 全文一致 ✓
- **[OK]** η², Cohen's d 等统计符号一致 ✓

- **[MINOR]** `discussion.tex:4` 有未引用的 `\label{sec:why_gradient}`，可删除。

## 2. Figure Caption

- **[OK]** Fig 1 (`fig:overview`) 数值与 Table 1 一致：0.725, 0.745, 0.767, 0.773, 0.802±0.024 n=3 ✓
- **[OK]** Fig 2 (`fig:factorial`) 4.2pp (d=0.93) 和 2.9pp (d=1.12) 与 Table 数据一致 ✓
- **[OK]** Fig 3 (`fig:gradient_analysis`) 描述与正文一致 ✓
- **[OK]** Fig 4 (`fig:per_layer_combined`) 标注 v1 codebase ✓
- **[OK]** Fig 5 (`fig:dose_response`) "+0.2%" 注释 (0.782-0.780) ✓
- **[OK]** 所有 `\label` / `\ref` 对齐，无 broken ref ✓

## 3. Appendix 完整性

- **[CRITICAL]** `appendix.tex:116`: **X.XX 占位符未填**："Vanilla baseline on LIBERO-Object achieves CAR **X.XX**"，对应 `% TODO: fill X.XX with vanilla_object eval data`。

- **[OK]** ANOVA table (`tab:anova`)：Source/F/df/p/η² 五列完整 ✓
- **[OK]** Pairwise table (`tab:pairwise`)：6 个 cell 间对比 + 4 个 vs Vanilla = 10 对完整 ✓
- **[OK]** 其余无 TODO/TBD/placeholder 残留

## 4. Related Work 引用

- **[OK]** VLA 模型：OpenVLA ✓, RT-2 ✓, OFT ✓, SpatialVLA ✓, DepthVLA ✓, OccVLA ✓, + 15+ 其他 spatial VLA 方法
- **[OK]** 安全机器人/VLA 安全：VLSA ✓, SafeVLA ✓, CoFreeVLA ✓, OGM-CBF ✓
- **[OK]** 多任务学习/梯度干扰：Caruana97 ✓, Ruder17 ✓, GradNorm ✓, PCGrad ✓, CAGrad ✓, Nash-MTL ✓, ForkMerge ✓
- **[OK]** Occupancy prediction：BEVFormer ✓, OccNet ✓, Occ3D ✓
- **[OK]** BN/LN 相关：Ioffe15 ✓, Ba16 ✓, GroupNorm ✓, AdaBN ✓, Schneider20 ✓
- **[MINOR]** Octo 未引用——作为主流 VLA 模型之一，建议在 intro 或 related work 中加入。非必须但推荐。

## 5. 编译质量

- **Errors: 0**
- **Warnings: 5**（3× `h` float specifier → `ht`；5× Underfull vbox — 均为页面布局问题，非致命）
- **Broken refs: 0**
- **Undefined citations: 0**
- **页数: 19**（正文约 8 页 + 附录 11 页）

---

### 需要修复的问题（按优先级）

| # | 严重度 | 位置 | 问题 |
|---|--------|------|------|
| 1 | **CRITICAL** | `appendix.tex:116-117` | **X.XX** 占位符 + TODO 注释，需填入 LIBERO-Object 数据或删除该段 |
| 2 | **HIGH** | intro×2, discussion×1, conclusion×1 | `d≈1.03` 应为 `d≈1.05`（与 pairwise table 一致） |
| 3 | **MEDIUM** | `results.tex:82` | CKA 首次出现需展开为 "Centered Kernel Alignment (CKA)" |
| 4 | **MEDIUM** | `method.tex:11` | BEV 需展开为 "bird's-eye view (BEV)" |
| 5 | **LOW** | `discussion.tex:4` | 未引用 label `sec:why_gradient` 可删 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 206543,
  "duration_api_ms": 204140,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "e413fecc-a408-423f-a37a-a0ffa0824ed0",
  "total_cost_usd": 0.8436892500000002,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 42665,
    "cache_read_input_tokens": 632332,
    "output_tokens": 10357,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42665,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1823,
        "cache_read_input_tokens": 54190,
        "cache_creation_input_tokens": 320,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 320
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1792,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001862,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 10357,
      "cacheReadInputTokens": 632332,
      "cacheCreationInputTokens": 42665,
      "webSearchRequests": 0,
      "costUSD": 0.8418272500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3e590e5d-2da5-4076-8a0e-155b78c8fec9"
}
```

</details>

---
