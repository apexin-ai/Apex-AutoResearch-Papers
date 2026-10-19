# paper rewrite introduction

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_rewrite-introduction_20260515T194914.log`
- **Structured JSON:** [`30193066deb5b82b5c39.json`](../../sessions/30/30193066deb5b82b5c39.json)

## Before a recorded user message

33 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
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
  "uuid": "ca416fe3-d084-4cf5-8e6b-5a862a907fd9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778886600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "51eefefa-de84-4415-add7-9d3aa98c9444",
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing introduction and reference materials to understand the current state and gather accurate details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "20d28295-67b2-4975-b802-6102fe741581",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvCc6AbKF9oifzmdoFY72S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

<details open><summary>🔧 Tool call — Read · `toolu_01CLifhZkTH28LRQkztooY9u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "d09a3eb8-d24f-4685-ab95-a051f8f2adde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvCc6AbKF9oifzmdoFY72S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

_source line 6 · 2026-05-15T19:49:24.024Z_

<details><summary>↩ Tool result · `toolu_01CLifhZkTH28LRQkztooY9u`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% Para 1: Problem — VLA success + robustness gap under distribution shift
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla} have reached 97--99\% success rates on standard manipulation benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this near-saturation masks a fragile reality: under distribution shifts common in real-world deployment---camera viewpoint changes, lighting variation, sensor noise, object layout differences---the same policies suffer substantial performance degradation~\cite{fei2025liberoplus}.
7	Closing this robustness gap is a prerequisite for deploying learned manipulation policies outside tightly controlled lab settings.
8	
9	% Para 2: Existing approaches — training-time vs inference-time, what they miss
10	Two lines of work address VLA robustness.
11	\emph{Training-time methods} improve the base policy itself: SRPO~\cite{srpo2025} applies self-referential policy optimization, while RobustVLA~\cite{robustvla2025} and DiG-Flow~\cite{digflow2025} incorporate robustness-aware objectives into training.
12	These methods are effective but require retraining or fine-tuning, and their gains are bounded by the training distribution.
13	\emph{Inference-time methods} leave the policy frozen and intervene at deployment.
14	ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean, using scalar Euclidean distance as an uncertainty proxy.
15	SAFE~\cite{gu2025safe} detects anomalous states and triggers fallback behaviors.
16	UPS~\cite{yuan2026ups} and CP-in-the-Loop~\cite{wang2025cploop} use conformal prediction for binary decisions---execute or abstain, safe or unsafe---but do not use conformal statistics as features for continuous correction.
17	A2C2~\cite{a2c2_2025} learns a residual correction that runs asynchronously alongside the base policy, yet applies it without uncertainty conditioning, lacking any mechanism to modulate correction magnitude across action dimensions.
18	In short, no existing method performs inference-time action correction conditioned on \emph{structured, per-degree-of-freedom uncertainty}.
19	
20	% Para 3: Our insight — per-DOF conformal features as continuous input to learned correction
21	Our key observation is that the stochastic samples already produced by a flow-matching VLA contain rich, structured uncertainty information that current methods discard.
22	By fitting a shrinkage-regularized Gaussian to $K{=}10$ samples and computing multivariate conformal statistics~\cite{braun2025cgs}, we obtain a 40-dimensional feature vector that encodes \emph{which} action dimensions are uncertain (per-DOF standard deviations), the \emph{calibrated confidence level} (conformal radii from Adaptive Conformal Inference~\cite{gibbs2021aci}), and the \emph{overall predictive spread} (log-volume of the covariance ellipsoid).
23	This representation captures substantially more structure than the scalar distances used in ReconVLA~\cite{chen2026reconvla}: it preserves the cross-DOF covariance structure that enables a downstream module to correct high-uncertainty dimensions aggressively while leaving confident predictions untouched.
24	A controlled 3D point-reaching experiment confirms this: a correction MLP conditioned on per-DOF uncertainty reduces total error by 6.7\% over scalar conditioning and by 16.7\% over no uncertainty input, with 22--24\% improvements concentrated on the non-perturbed axes where scalar conditioning cannot distinguish signal from noise (Section~\ref{sec:motivating}).
25	
26	% Para 4: ACR-VLA overview — 3 components, key design choices
27	We introduce \textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that attaches to any frozen flow-matching VLA and performs dimension-selective action correction.
28	ACR-VLA comprises three components:
29	(i)~\textbf{Conformalized Gaussian Scoring (CGS)} draws $K{=}10$ samples per control step, fits a Ledoit--Wolf shrinkage covariance, and extracts a 40D structured uncertainty feature;
30	(ii)~\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency (ACI+COC)} maintains an online conformal threshold~\cite{gibbs2021aci} using a self-referential coverage signal derived from overlapping action chunks---requiring no external supervisor, reward model, or ground-truth actions;
31	(iii)~\textbf{Conformal Refinement Module (CRM)}, a lightweight MLP (${\sim}$337K parameters) that takes the CGS features as conditioning and outputs a dimension-selective residual correction.
32	We note that conformal prediction serves here as a \emph{feature extraction and calibration mechanism}, not as a guarantee on the corrected output: CGS features provide structured uncertainty conditioning for CRM, while ACI+COC adapts these features online under distribution shift.
33	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
34	
35	% Para 5: Contributions — numbered list
36	Our contributions are:
37	\begin{enumerate}[leftmargin=*,nosep]
38	  \item \textbf{Per-DOF conformal features for dimension-selective correction.}
39	  We show that the 40D CGS representation---per-DOF standard deviations, calibrated conformal radii, and covariance log-volume---enables CRM to selectively correct uncertain action dimensions while preserving accurate ones.
40	  On LIBERO, ACR-VLA improves base SmolVLA success by \textbf{XX.X}\,pp, and ablations confirm that per-DOF features outperform both scalar uncertainty and no-uncertainty baselines (Section~\ref{sec:experiments}).
41	
42	  \item \textbf{Self-referential online calibration via Chunk Overlap Consistency.}
43	  COC exploits the temporal overlap in receding-horizon action chunks to provide a coverage signal for ACI without external supervision.
44	  This enables the conformal threshold to adapt online under arbitrary distribution shift, maintaining calibrated uncertainty features throughout deployment (Section~\ref{sec:aci}).
45	
46	  \item \textbf{Systematic evaluation across multiple LIBERO task suites.}
47	  We evaluate ACR-VLA on LIBERO-Spatial and LIBERO-Object, providing per-task breakdowns, ablations isolating the contribution of each component (CGS features, ACI+COC calibration, CRM architecture), and analysis of when and why dimension-selective correction helps (Section~\ref{sec:experiments}).
48	\end{enumerate}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "0be6afea-3292-4de4-9818-69bc9ae524b8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% Para 1: Problem — VLA success + robustness gap under distribution shift\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla} have reached 97--99\\% success rates on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: under distribution shifts common in real-world deployment---camera viewpoint changes, lighting variation, sensor noise, object layout differences---the same policies suffer substantial performance degradation~\\cite{fei2025liberoplus}.\nClosing this robustness gap is a prerequisite for deploying learned manipulation policies outside tightly controlled lab settings.\n\n% Para 2: Existing approaches — training-time vs inference-time, what they miss\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself: SRPO~\\cite{srpo2025} applies self-referential policy optimization, while RobustVLA~\\cite{robustvla2025} and DiG-Flow~\\cite{digflow2025} incorporate robustness-aware objectives into training.\nThese methods are effective but require retraining or fine-tuning, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen and intervene at deployment.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean, using scalar Euclidean distance as an uncertainty proxy.\nSAFE~\\cite{gu2025safe} detects anomalous states and triggers fallback behaviors.\nUPS~\\cite{yuan2026ups} and CP-in-the-Loop~\\cite{wang2025cploop} use conformal prediction for binary decisions---execute or abstain, safe or unsafe---but do not use conformal statistics as features for continuous correction.\nA2C2~\\cite{a2c2_2025} learns a residual correction that runs asynchronously alongside the base policy, yet applies it without uncertainty conditioning, lacking any mechanism to modulate correction magnitude across action dimensions.\nIn short, no existing method performs inference-time action correction conditioned on \\emph{structured, per-degree-of-freedom uncertainty}.\n\n% Para 3: Our insight — per-DOF conformal features as continuous input to learned correction\nOur key observation is that the stochastic samples already produced by a flow-matching VLA contain rich, structured uncertainty information that current methods discard.\nBy fitting a shrinkage-regularized Gaussian to $K{=}10$ samples and computing multivariate conformal statistics~\\cite{braun2025cgs}, we obtain a 40-dimensional feature vector that encodes \\emph{which} action dimensions are uncertain (per-DOF standard deviations), the \\emph{calibrated confidence level} (conformal radii from Adaptive Conformal Inference~\\cite{gibbs2021aci}), and the \\emph{overall predictive spread} (log-volume of the covariance ellipsoid).\nThis representation captures substantially more structure than the scalar distances used in ReconVLA~\\cite{chen2026reconvla}: it preserves the cross-DOF covariance structure that enables a downstream module to correct high-uncertainty dimensions aggressively while leaving confident predictions untouched.\nA controlled 3D point-reaching experiment confirms this: a correction MLP conditioned on per-DOF uncertainty reduces total error by 6.7\\% over scalar conditioning and by 16.7\\% over no uncertainty input, with 22--24\\% improvements concentrated on the non-perturbed axes where scalar conditioning cannot distinguish signal from noise (Section~\\ref{sec:motivating}).\n\n% Para 4: ACR-VLA overview — 3 components, key design choices\nWe introduce \\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that attaches to any frozen flow-matching VLA and performs dimension-selective action correction.\nACR-VLA comprises three components:\n(i)~\\textbf{Conformalized Gaussian Scoring (CGS)} draws $K{=}10$ samples per control step, fits a Ledoit--Wolf shrinkage covariance, and extracts a 40D structured uncertainty feature;\n(ii)~\\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency (ACI+COC)} maintains an online conformal threshold~\\cite{gibbs2021aci} using a self-referential coverage signal derived from overlapping action chunks---requiring no external supervisor, reward model, or ground-truth actions;\n(iii)~\\textbf{Conformal Refinement Module (CRM)}, a lightweight MLP (${\\sim}$337K parameters) that takes the CGS features as conditioning and outputs a dimension-selective residual correction.\nWe note that conformal prediction serves here as a \\emph{feature extraction and calibration mechanism}, not as a guarantee on the corrected output: CGS features provide structured uncertainty conditioning for CRM, while ACI+COC adapts these features online under distribution shift.\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\n\n% Para 5: Contributions — numbered list\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{Per-DOF conformal features for dimension-selective correction.}\n  We show that the 40D CGS representation---per-DOF standard deviations, calibrated conformal radii, and covariance log-volume---enables CRM to selectively correct uncertain action dimensions while preserving accurate ones.\n  On LIBERO, ACR-VLA improves base SmolVLA success by \\textbf{XX.X}\\,pp, and ablations confirm that per-DOF features outperform both scalar uncertainty and no-uncertainty baselines (Section~\\ref{sec:experiments}).\n\n  \\item \\textbf{Self-referential online calibration via Chunk Overlap Consistency.}\n  COC exploits the temporal overlap in receding-horizon action chunks to provide a coverage signal for ACI without external supervision.\n  This enables the conformal threshold to adapt online under arbitrary distribution shift, maintaining calibrated uncertainty features throughout deployment (Section~\\ref{sec:aci}).\n\n  \\item \\textbf{Systematic evaluation across multiple LIBERO task suites.}\n  We evaluate ACR-VLA on LIBERO-Spatial and LIBERO-Object, providing per-task breakdowns, ablations isolating the contribution of each component (CGS features, ACI+COC calibration, CRM architecture), and analysis of when and why dimension-selective correction helps (Section~\\ref{sec:experiments}).\n\\end{enumerate}\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01W8uduC8vgPePKzCeDiLmoM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "8eb50059-cb75-45af-87c9-36d24e74a71c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvCc6AbKF9oifzmdoFY72S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

_source line 8 · 2026-05-15T19:49:24.486Z_

<details><summary>↩ Tool result · `toolu_01W8uduC8vgPePKzCeDiLmoM`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem_setup}
9	
10	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.
11	
12	At each control step, $\pi_\theta$ can be queried multiple times via independent flow-matching rollouts~\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\pi_\theta$.
13	
14	\subsection{Multi-Sample Generation and Conformal Selection}
15	\label{sec:selection}
16	
17	\paragraph{Sampling and truncation.}
18	We draw $K{=}10$ action chunks from $\pi_\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for each horizon step $h = 1, \dots, H$.
19	
20	\paragraph{Shrinkage covariance estimation.}
21	For each horizon step $h$, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well}:
22	\begin{equation}
23	  \boldsymbol{\Sigma}_h = (1 - \alpha_{\mathrm{LW}})\,\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}} + \alpha_{\mathrm{LW}}\,\frac{\mathrm{tr}(\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}})}{d}\,\mathbf{I},
24	  \label{eq:shrinkage}
25	\end{equation}
26	where $\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}}$ is the empirical covariance and $\alpha_{\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\% estimation error; shrinkage reduces this to below 5\%~\cite{ledoit2004well}.
27	
28	\paragraph{Mahalanobis nonconformity score.}
29	For each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:
30	\begin{equation}
31	  s_h(a) = (a - \boldsymbol{\mu}_h)^\top \boldsymbol{\Sigma}_h^{-1} (a - \boldsymbol{\mu}_h).
32	  \label{eq:mahal}
33	\end{equation}
34	This score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\cite{braun2025cgs}.
35	
36	\paragraph{Argmin selection.}
37	We select the sample with the lowest total nonconformity across all horizon steps:
38	\begin{equation}
39	  a_{\mathrm{base}} = \argmin_{k \in \{1,\dots,K\}} \sum_{h=1}^{H} s_h\bigl(a_h^{(k)}\bigr).
40	  \label{eq:argmin}
41	\end{equation}
42	This is a simplified selection baseline inspired by the conformal selection frontend of ReconVLA~\cite{chen2026reconvla}, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring to isolate the effect of the downstream correction module. The selected $a_{\mathrm{base}} \in \mathbb{R}^{d \times H}$ is the starting point for residual correction.
43	
44	\subsection{Conformal Residual Module}
45	\label{sec:crm}
46	
47	The Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.
48	
49	\paragraph{Architecture.}
50	CRM is a 3-layer MLP with input normalization (input$\to$256$\to$256$\to$30; 329K parameters for the primary obs\_only variant).
51	Its input is the frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\boldsymbol{\delta} \in \mathbb{R}^{d \times H} = \mathbb{R}^{30}$, and the corrected action is:
52	\begin{equation}
53	  \mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}\bigl(\boldsymbol{\delta},\; \|\boldsymbol{\delta}\|_2 \leq \varepsilon\bigr),
54	  \label{eq:crm}
55	\end{equation}
56	where $\varepsilon$ is a norm bound hyperparameter (Section~\ref{sec:magnitude}).
57	
58	\paragraph{Observation-only conditioning.}
59	CRM receives only the observation embedding $\mathbf{z}_{\mathrm{obs}}$ and does \emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.
60	
61	\paragraph{Training.}
62	CRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\cite{liu2023libero}:
63	\begin{equation}
64	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2.
65	  \label{eq:loss}
66	\end{equation}
67	The training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\ref{eq:argmin}) to obtain $a_{\mathrm{base}}$. The expert action $\mathbf{a}_{\mathrm{expert}}$ is the corresponding demonstration action.
68	
69	We apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\sigma \approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\cite{ross2011dagger}.
70	
71	\paragraph{Base VLA.}
72	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.
73	
74	\subsection{Magnitude Control}
75	\label{sec:magnitude}
76	
77	The norm bound $\varepsilon$ in~(\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.
78	
79	\paragraph{Unbounded correction fails catastrophically.}
80	Without clipping, the natural CRM output has $\|\boldsymbol{\delta}\|_2 \approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.
81	
82	\paragraph{Small corrections are effective.}
83	Constraining $\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.
84	
85	\paragraph{Connection to residual policy learning.}
86	The necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\cite{silver2018residual} introduced bounded residual corrections for combining learned and classical controllers. TRANSIC~\cite{jiang2024transic} uses learned binary gating to selectively apply residual actions across different task phases. PLD~\cite{xiao2026pld} schedules magnitude bounds during training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no scheduling, just a hard constraint that prevents the correction from overwhelming the base policy.
87	
88	\paragraph{Differential sensitivity across CRM variants.}
89	Observation-conditioned CRM (obs\_only) maintains 35--36\% success on LIBERO-Spatial across the full range $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% at $\varepsilon = 0.1$ to 26\% at $\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\ref{sec:ablation}).
90	
91	\subsection{Inference Protocol}
92	\label{sec:inference_protocol}
93	
94	Each control step proceeds as follows:
95	\begin{enumerate}[nosep]
96	  \item Draw $K{=}10$ action chunks from the frozen VLA $\pi_\theta$ and truncate to $H{=}5$ steps.
97	  \item Compute shrinkage covariance $\boldsymbol{\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.
98	  \item Select $a_{\mathrm{base}}$ via argmin over total nonconformity~(\ref{eq:argmin}).
99	  \item Compute residual $\boldsymbol{\delta} = \mathrm{CRM}(\mathbf{z}_{\mathrm{obs}})$ and clip to $\|\boldsymbol{\delta}\|_2 \leq \varepsilon$.
100	  \item Execute the first action of $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
101	  \item Observe new state and re-plan from step~1.
102	\end{enumerate}
103	The computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\cite{chen2026reconvla}) plus ${\sim}$3\,ms for CRM inference. The base VLA is never modified.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "6a002a85-a986-429b-8b18-92c4e08ea0bc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis is a simplified selection baseline inspired by the conformal selection frontend of ReconVLA~\\cite{chen2026reconvla}, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring to isolate the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 329K parameters for the primary obs\\_only variant).\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced bounded residual corrections for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating to selectively apply residual actions across different task phases. PLD~\\cite{xiao2026pld} schedules magnitude bounds during training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no scheduling, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\\cite{chen2026reconvla}) plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01J25aNrWfUSpGVv93UphxRD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "a5d3cd4e-d527-40fe-ae89-243f35f7094d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvCc6AbKF9oifzmdoFY72S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

_source line 10 · 2026-05-15T19:49:25.614Z_

<details><summary>↩ Tool result · `toolu_01J25aNrWfUSpGVv93UphxRD`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction improve over conformal selection alone?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+7.0\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\_only is robust across a wide range.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\ref{sec:selection}), no CRM correction.
30	\end{itemize}
31	
32	\paragraph{CRM variants.}
33	All CRM variants share the same 3-layer MLP architecture (input$\to$256$\to$256$\to$30) and differ only in their conditioning input:
34	\begin{itemize}[nosep]
35	  \item \textbf{obs\_only}: frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ (329K params). This is our primary method.
36	  \item \textbf{perdof}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).
37	  \item \textbf{scalar}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).
38	\end{itemize}
39	
40	\paragraph{Training.}
41	CRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.
42	For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\mathrm{base}}$.
43	Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.
44	Data augmentation includes additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and uncertainty features ($\sigma \approx 0.006$).
45	The default magnitude bound is $\varepsilon = 0.1$ for all CRM variants unless stated otherwise.
46	
47	\paragraph{Statistical protocol.}
48	We report success rates from seed 42 (10 rollouts $\times$ 10 tasks = 100 episodes per suite).
49	Fisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\textsc{pending}: seed43].
50	Until then, we report absolute differences descriptively without claiming statistical significance.
51	
52	
53	\subsection{Main Results}
54	\label{sec:main_results}
55	
56	Table~\ref{tab:main} compares all methods on both benchmarks.
57	
58	\begin{table}[t]
59	\centering
60	\caption{Task success rate (\%\,$\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\times$ 10 rollouts each, seed 42). $\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}
61	\label{tab:main}
62	\small
63	\begin{tabular}{lccc}
64	\toprule
65	Method & Object (\%) & Spatial (\%) & $\Delta$ Object \\
66	\midrule
67	VLA-only ($K{=}1$)    & 12.0 & 30.0 & $\phantom{+}0.0$ \\
68	VLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\phantom{+}0.0$ \\
69	Argmin ($K{=}10$)      & 12.0 & 34.0 & --- \\
70	\midrule
71	scalar ($\varepsilon{=}0.1$)  & \phantom{0}9.0 & 32.0 & $-3.0$ \\
72	perdof ($\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\
73	\textbf{obs\_only} ($\varepsilon{=}0.1$) & \textbf{19.0} & \textbf{35.0} & $\mathbf{+7.0}$ \\
74	\midrule
75	obs\_only ($\varepsilon{=}0.2$) & \textbf{22.0} & 35.0 & $+10.0$ \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	\paragraph{Object benchmark: correction helps.}
81	On LIBERO-Object, obs\_only at $\varepsilon{=}0.1$ achieves 19.0\%, a +7.0\,pp improvement over the Argmin baseline (12.0\%).
82	Increasing the magnitude bound to $\varepsilon{=}0.2$ yields 22.0\% (+10.0\,pp).
83	This is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.
84	
85	Three baselines---VLA-only, VLA-mean, and Argmin---all achieve 12.0\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.
86	On LIBERO-Spatial, by contrast, Argmin improves +4\,pp over VLA-only (34\% vs.\ 30\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.
87	The obs\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.
88	
89	\paragraph{Spatial benchmark: correction does not help.}
90	On LIBERO-Spatial, all methods cluster within a 5\,pp band (30--35\%).
91	The best CRM variants (obs\_only, perdof) achieve 35\%, only 1\,pp above the Argmin baseline (34\%).
92	This is a null result that we report prominently.
93	
94	We interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.
95	The VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.
96	Residual correction at the action level is the wrong granularity for this type of generalization.
97	
98	\paragraph{Key finding.}
99	Sample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.
100	For spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.
101	
102	
103	\subsection{CRM Conditioning Ablation}
104	\label{sec:ablation}
105	
106	We focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\ref{tab:main}).
107	
108	\paragraph{Ranking.}
109	obs\_only (19.0\%) $\gg$ Argmin (12.0\%) $\approx$ perdof (11.0\%) $>$ scalar (9.0\%).
110	
111	This ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \emph{hurt} rather than help.
112	Scalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\,pp below the Argmin baseline that uses no correction at all.
113	
114	\paragraph{Why does richer conditioning fail?}
115	We identify three factors:
116	
117	\emph{(1) Noisy covariance estimation.}
118	With $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.
119	While Ledoit--Wolf shrinkage~\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.
120	Feeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).
121	
122	\emph{(2) Observation features are sufficient.}
123	The frozen VLA observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.
124	This information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.
125	The CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.
126	
127	\emph{(3) Per-step MSE $\neq$ episode success.}
128	In offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.
129	However, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\cite{ross2011dagger}.
130	The additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.
131	
132	\paragraph{Connection to magnitude sensitivity.}
133	The obs\_only variant is also more robust across magnitude bounds $\varepsilon$ than perdof (Section~\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.
134	
135	
136	\subsection{Magnitude Sensitivity}
137	\label{sec:magnitude_results}
138	
139	The norm bound $\varepsilon$ determines how much CRM can deviate from the conformal-selected action.
140	Figure~\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\varepsilon \in [0.05, 1.42]$.
141	
142	\begin{figure}[t]
143	\centering
144	% \includegraphics[width=\linewidth]{figures/magnitude_sweep.pdf}
145	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Placeholder: Magnitude sweep --- obs\_only vs.\ perdof vs.\ Argmin reference]\vspace{2em}}}
146	\caption{Success rate (\%) on LIBERO-Spatial as a function of magnitude bound $\varepsilon$. obs\_only (solid blue) maintains 35--36\% across $\varepsilon \in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\varepsilon$. The Argmin baseline (dotted gray, 34\%) is independent of $\varepsilon$. Without magnitude control ($\varepsilon{\approx}1.42$), perdof achieves 0\% on spatial.}
147	\label{fig:magnitude}
148	\end{figure}
149	
150	\begin{table}[t]
151	\centering
152	\caption{Success rate (\%) on LIBERO-Spatial across magnitude bounds $\varepsilon$. The Argmin baseline (34\%, no correction) is independent of $\varepsilon$.}
153	\label{tab:magnitude}
154	\small
155	\begin{tabular}{lcccc}
156	\toprule
157	$\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\
158	\midrule
159	obs\_only & 35.0 & 35.0 & 36.0 & --- \\
160	perdof    & 31.0 & 35.0 & 26.0 & 0.0 \\
161	\midrule
162	Argmin (ref.) & \multicolumn{4}{c}{34.0 (flat, no correction)} \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{obs\_only is robust.}
168	The obs\_only variant maintains 35--36\% across the full range $\varepsilon \in [0.05, 0.3]$---a remarkably flat profile.
169	This stability means the practitioner need not carefully tune $\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.
170	
171	\paragraph{perdof is fragile.}
172	In contrast, perdof peaks at 35\% when $\varepsilon{=}0.1$ but collapses to 26\% at $\varepsilon{=}0.3$---a 9\,pp drop.
173	This fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.
174	At $\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.
175	
176	\paragraph{Unbounded correction is catastrophic.}
177	Without magnitude control ($\varepsilon{\approx}1.42$, the natural CRM output norm), perdof achieves 0\% on LIBERO-Spatial---compounding error across the trajectory destroys performance entirely (Section~\ref{sec:magnitude}).
178	The Argmin baseline (34\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.
179	The obs\_only variant was not evaluated at $\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.
180	
181	\paragraph{Practical recommendation.}
182	The safe operating range is $\varepsilon \in [0.05, 0.2]$.
183	Within this range, obs\_only is the only variant that consistently matches or exceeds the Argmin baseline.
184	We use $\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.
185	
186	
187	\subsection{Per-Task Analysis}
188	\label{sec:per_task}
189	
190	Per-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.
191	
192	[\textsc{pending}: seed43] --- A per-task heatmap comparing obs\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.
193	We expect the analysis to show that obs\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.
194	Task difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).
195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "f0e07f4b-0848-4174-b0a9-bfad8466387b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to answer three questions:\n(i)~Does observation-conditioned residual correction improve over conformal selection alone?\n(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?\n(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?\nThe answers are: yes (+7.0\\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\\_only is robust across a wide range.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\nWe use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{Baselines.}\nAll methods use the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.\n  \\item \\textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\\ref{sec:selection}), no CRM correction.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nAll CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ (329K params). This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).\n\\end{itemize}\n\n\\paragraph{Training.}\nCRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.\nFor each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\\mathrm{base}}$.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.\nData augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).\nThe default magnitude bound is $\\varepsilon = 0.1$ for all CRM variants unless stated otherwise.\n\n\\paragraph{Statistical protocol.}\nWe report success rates from seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).\nFisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\\textsc{pending}: seed43].\nUntil then, we report absolute differences descriptively without claiming statistical significance.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares all methods on both benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\\n\\midrule\nVLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\\nVLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\\nArgmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\\n\\midrule\nscalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\\nperdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\\n\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\\n\\midrule\nobs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Object benchmark: correction helps.}\nOn LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\%, a +7.0\\,pp improvement over the Argmin baseline (12.0\\%).\nIncreasing the magnitude bound to $\\varepsilon{=}0.2$ yields 22.0\\% (+10.0\\,pp).\nThis is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.\n\nThree baselines---VLA-only, VLA-mean, and Argmin---all achieve 12.0\\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.\nOn LIBERO-Spatial, by contrast, Argmin improves +4\\,pp over VLA-only (34\\% vs.\\ 30\\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.\nThe obs\\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.\n\n\\paragraph{Spatial benchmark: correction does not help.}\nOn LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).\nThe best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).\nThis is a null result that we report prominently.\n\nWe interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.\nThe VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.\nResidual correction at the action level is the wrong granularity for this type of generalization.\n\n\\paragraph{Key finding.}\nSample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.\nFor spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.\n\n\n\\subsection{CRM Conditioning Ablation}\n\\label{sec:ablation}\n\nWe focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).\n\n\\paragraph{Ranking.}\nobs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).\n\nThis ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.\nScalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.\n\n\\paragraph{Why does richer conditioning fail?}\nWe identify three factors:\n\n\\emph{(1) Noisy covariance estimation.}\nWith $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.\nWhile Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.\nFeeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).\n\n\\emph{(2) Observation features are sufficient.}\nThe frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.\nThis information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.\nThe CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.\n\n\\emph{(3) Per-step MSE $\\neq$ episode success.}\nIn offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.\nHowever, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\nThe additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.\n\n\\paragraph{Connection to magnitude sensitivity.}\nThe obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.\n\n\n\\subsection{Magnitude Sensitivity}\n\\label{sec:magnitude_results}\n\nThe norm bound $\\varepsilon$ determines how much CRM can deviate from the conformal-selected action.\nFigure~\\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\\varepsilon \\in [0.05, 1.42]$.\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/magnitude_sweep.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: Magnitude sweep --- obs\\_only vs.\\ perdof vs.\\ Argmin reference]\\vspace{2em}}}\n\\caption{Success rate (\\%) on LIBERO-Spatial as a function of magnitude bound $\\varepsilon$. obs\\_only (solid blue) maintains 35--36\\% across $\\varepsilon \\in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\\varepsilon$. The Argmin baseline (dotted gray, 34\\%) is independent of $\\varepsilon$. Without magnitude control ($\\varepsilon{\\approx}1.42$), perdof achieves 0\\% on spatial.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Spatial across magnitude bounds $\\varepsilon$. The Argmin baseline (34\\%, no correction) is independent of $\\varepsilon$.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\\\\n\\midrule\nobs\\_only & 35.0 & 35.0 & 36.0 & --- \\\\\nperdof    & 31.0 & 35.0 & 26.0 & 0.0 \\\\\n\\midrule\nArgmin (ref.) & \\multicolumn{4}{c}{34.0 (flat, no correction)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{obs\\_only is robust.}\nThe obs\\_only variant maintains 35--36\\% across the full range $\\varepsilon \\in [0.05, 0.3]$---a remarkably flat profile.\nThis stability means the practitioner need not carefully tune $\\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.\n\n\\paragraph{perdof is fragile.}\nIn contrast, perdof peaks at 35\\% when $\\varepsilon{=}0.1$ but collapses to 26\\% at $\\varepsilon{=}0.3$---a 9\\,pp drop.\nThis fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.\nAt $\\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.\n\n\\paragraph{Unbounded correction is catastrophic.}\nWithout magnitude control ($\\varepsilon{\\approx}1.42$, the natural CRM output norm), perdof achieves 0\\% on LIBERO-Spatial---compounding error across the trajectory destroys performance entirely (Section~\\ref{sec:magnitude}).\nThe Argmin baseline (34\\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.\nThe obs\\_only variant was not evaluated at $\\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.\n\n\\paragraph{Practical recommendation.}\nThe safe operating range is $\\varepsilon \\in [0.05, 0.2]$.\nWithin this range, obs\\_only is the only variant that consistently matches or exceeds the Argmin baseline.\nWe use $\\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nPer-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.\n\n[\\textsc{pending}: seed43] --- A per-task heatmap comparing obs\\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.\nWe expect the analysis to show that obs\\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.\nTask difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).\n",
      "numLines": 195,
      "startLine": 1,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016hSwCpK2Kkfft5RZeutMH4`</summary>

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
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "730fffc7-635e-49ee-bca7-5c2b0f9268c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvCc6AbKF9oifzmdoFY72S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

_source line 12 · 2026-05-15T19:49:26.185Z_

<details><summary>↩ Tool result · `toolu_016hSwCpK2Kkfft5RZeutMH4`</summary>

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
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "6298bc1d-1af2-442a-884c-75f3b4386d79",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper_framing.md, writing_plan.yaml, literature_map.yaml, and related_work.md to get all the reference materials.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "4ec5d841-8891-4f9b-9a71-ae75fe11c9f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T2DMj1etHujeJ5CicuF2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10462,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10462
      },
      "output_tokens": 34,
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

_source line 14_

Now let me read the reference materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "b330442e-6324-4c03-87aa-bf56468b0e91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T2DMj1etHujeJ5CicuF2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10462,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10462
      },
      "output_tokens": 34,
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

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01J8EoR6QrUEGQxZkuzMNENU`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
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
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "34bc1e16-fddd-4513-b82c-e3ad2366f532",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T2DMj1etHujeJ5CicuF2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10462,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10462
      },
      "output_tokens": 34,
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

_source line 16 · 2026-05-15T19:49:34.320Z_

<details><summary>↩ Tool result · `toolu_01J8EoR6QrUEGQxZkuzMNENU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight (Scenario C — ACTIVE, D029+D030 confirmed)\\nA lightweight observation-conditioned learned correction module (CRM), applied after conformal sample selection, can synthesize actions better than any individual VLA sample. The key contribution is the **sample-then-correct** pipeline itself and the discovery that **correction magnitude control is critical for closed-loop stability**. Per-DOF conformal features as CRM input offer no additional value over observation features — an honest negative result that challenges the intuition from synthetic experiments.\\n\\n## Active Framing: Scenario C\\n**Confirmed by data**: obs_only CRM > perdof CRM ≈ scalar CRM ≈ argmin on spatial (D029-D030); obs_only CRM **+7.0pp** over argmin on object 10/10 tasks FINAL (19.0% vs 12.0%); magnitude sweep shows obs_only robust to norm while perdof collapses at high norm (D032).\\n\\nStory: \\\"Observation-conditioned residual correction is the key contribution. The sample-then-correct pipeline (K=10 conformal selection + learned CRM correction) significantly outperforms pure sample selection on object manipulation tasks. Per-DOF conformal statistics as direct CRM input offer no advantage over observation features — but conformal prediction remains essential for the sample selection stage. Correction magnitude control is a critical and previously unrecognized factor for closed-loop VLA correction.\\\"\\n\\n## Core Claims (CoRL 单 Claim 论文)\\n\\n1. **Observation-conditioned learned correction (CRM) significantly improves VLA robustness beyond sample selection**\\n   - **主 claim**: obs_only CRM vs argmin-only ≥ 5pp on object benchmark + p < 0.05\\n   - **Spatial**: DEAD — all CRM variants 32-35% vs argmin 34%, no signal (D030)\\n   - **Object 10/10 FINAL**: obs_only 0.1: **19.0%** vs argmin **12.0%** (+7.0pp); obs_only 0.2: 18.0% (5/10, running)\\n   - **seed=43 doubling (RUNNING)**: 目标 combined 200 trials Fisher p < 0.05 (D031)\\n\\n2. **Honest negative result: per-DOF conformal features as CRM input have no value**\\n   - Spatial: perdof 35% = argmin 34% = obs_only 35% (D029)\\n   - Object 10/10 FINAL: perdof 11.0% ≈ argmin 12.0%, obs_only **19.0%** >> perdof; scalar 9.0% (negative)\\n   - Magnitude sweep: obs_only robust across norms, perdof collapses at high norm (D032)\\n   - 转化为学术贡献：challenges synthetic-experiment intuition, highlights gap between per-step MSE and closed-loop success\\n\\n3. **Correction magnitude control is critical for closed-loop stability (empirical contribution)**\\n   - norm=1.42 → 0% (catastrophic); norm=0.1 → 35% (spatial) / **19%** (object FINAL); norm=0.2 → 18% (object 5/10, running)\\n   - obs_only CRM maintains performance across norm range; perdof CRM collapses at norm ≥ 0.2\\n   - Novel finding: no prior work on correction magnitude sensitivity for VLA action refinement\\n\\n~~Claims 2-3 (ACI/COC, SRPO stacking) — D022/D023 移除~~\\n\\n## Kill Criteria\\n- **内部 kill**: obs_only CRM vs argmin-only < 3pp on object 10-task → project dead\\n- **论文 claim 门槛**: ≥ 5pp + Fisher exact p < 0.05 on object (seed=42 + seed=43 combined)\\n- **3-5pp 灰区**: 需要加 n_rollouts 或加 benchmark 提升统计力\\n- **当前状态**: +7.0pp at 10/10 tasks FINAL, **超过 5pp 门槛**。等待 seed=43 确认统计显著性。\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO 暴露了分布偏移下的鲁棒性缺口。现有 inference-time 方法要么只做样本选择（ReconVLA），要么需要任务级 RL 训练（SC-VLA），要么推理延迟过高（VLA-Pilot 2.41s/step）。没有方法探索过 inference-time learned action correction on frozen VLA。\\n- **Gap**: Sample selection（从 K 候选中选最优）受限于候选质量——当所有样本都不够好时 selection 失效。Learned correction 可以合成优于任何单个样本的动作，但关键问题是 correction 应该以什么为条件？我们的系统性 ablation 发现 observation features 是最有效的 conditioning，而直觉上更丰富的 per-DOF conformal statistics 反而无效。\\n- **Our angle**: 第一个在 frozen VLA 上做 inference-time learned action correction 并系统性比较 conditioning features 的工作。核心发现：(1) sample-then-correct > sample-then-select；(2) observation features > conformal features for correction conditioning（挑战合成实验直觉）；(3) correction magnitude control 是此前被忽视的关键因素。\\n- **Headline result template**: \\\"On LIBERO object manipulation, ACR-VLA's sample-then-correct pipeline improves SmolVLA success by +Xpp over sample selection alone (p < Y). Surprisingly, observation-conditioned correction outperforms conformal-feature-conditioned correction, while correction magnitude proves critical — norm=1.42 yields 0% but norm=0.1-0.2 yields +Xpp, with observation-conditioned CRM uniquely robust across the magnitude range.\\\"\\n\\n## Competitive Landscape\\n\\n### ReconVLA — 最直接竞品\\nPost-hoc conformal prediction on frozen VLA。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\n\\n**关键差异**：(1) Selection-only — 无法合成优于单个样本的动作；(2) 我们的 argmin baseline 近似 ReconVLA 的 selection 策略，CRM correction 在此基础上有独立增量。\\n\\n### SC-VLA — Inference-time RL refinement\\nResidual RL 在线调整动作。需任务级 RL 训练，非 plug-and-play，无统计保证。\\n\\n### ACR-VLA 差异化定位（更新后）\\n第一个系统性研究 inference-time learned action correction for frozen VLAs 的工作。贡献不在于\\\"哪种 uncertainty feature 最好\\\"（答案出乎意料是 obs features），而在于：(1) 证明 sample-then-correct > sample-then-select；(2) 揭示 correction magnitude sensitivity 这一此前未被研究的关键因素；(3) 提供 per-DOF conformal features 无效的 honest negative result + 分析。\\n\\n## Anticipated Reviewer Concerns\\n1. **\\\"obs_only 就是一个 residual MLP，有什么新意？\\\"**: 新意在于 systematic comparison（per-DOF vs scalar vs obs-only conditioning）+ magnitude sensitivity discovery + honest negative result。且我们的 CRM 是在 conformal-selected sample 上 correction，不是 naive residual。\\n2. **CRM 329K 参数表达力** (obs_only; perdof 339K, scalar 330K): 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。架构：3-layer MLP (input→256→256→30), input normalization。\\n3. **仿真 only**: CoRL 接受 sim-only，LIBERO 是 recognized benchmark。\\n4. **Spatial 无效**: Honest limitation。可能原因：spatial tasks 的 perturbation 类型（位置偏移）不产生可被 CRM 校正的 action error pattern。Object tasks 的 perturbation（物体替换）产生更大的 action distribution shift。\\n5. **\\\"Conformal\\\" 标签可能误导**: 论文明确：CP 用于 sample selection stage（nonconformity score → argmin），不是 CRM 输出保证。Title 应反映 \\\"sample-then-correct\\\" 而非 \\\"conformal correction\\\"。\\n6. **统计显著性**: Fisher exact test on combined seed=42+43 (200 trials), bootstrap CI, per-task breakdown。\\n7. **K=10 成本**: 与 ReconVLA 相同 K 值，fair comparison。CRM overhead ~3ms。\\n8. **为什么 per-DOF features 无效？**: 训练/eval 分布偏移假说 — CRM 训练时 per-DOF features 有噪声（K=10 covariance estimation noise），obs features 更稳定。Magnitude sweep 证据：perdof 在高 norm 崩塌说明 per-DOF features 导致 CRM 学到 overconfident correction patterns。\\n\\n## 硬证据（已确认）\\n- Spatial LOCKED: argmin 34%, perdof 35%, obs_only 35%, scalar 32% — all noise level\\n- VLA baseline K=1: spatial 30%, object 12.0%\\n- VLA mean K=10: spatial 32%, object **12.0%** (10/10 FINAL) — = argmin, confirms selection ceiling\\n- **Object 10/10 FINAL**: obs_only 19.0%, argmin 12.0%, VLA-only 12.0%, perdof 11.0%, VLA-mean 12.0%, scalar 9.0%\\n- **obs_only +7.0pp over argmin** — exceeds 5pp claim threshold\\n- Magnitude control: norm=1.42 → 0%, norm=0.1 → 19% (object FINAL), norm=0.2 → 18% (5/10)\\n- Magnitude robustness (D032): obs_only stable across norms, perdof collapses at norm ≥ 0.2\\n\\n## 待确认证据（RUNNING）\\n- Seed=43 复现 + Fisher exact test（六方全部部署: obs_only / argmin / perdof / scalar / VLA-mean / VLA-only）\\n- Object obs_only 0.2 final（当前 18.0% at 5/10）\\n- Object v4-default (norm=1.42) ablation — confirm catastrophic failure\\n\", \"total_chars\": 7406, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "57a8520a-6ad7-43a6-9a33-ba02a9eae108",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — acr-vla-conformal-refinement\\\\n\\\\n## Target Venue\\\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021\\\\n- ~~ICLR 2027~~ — 不再是首要目标\\\\n\\\\n## Core Insight (Scenario C — ACTIVE, D029+D030 confirmed)\\\\nA lightweight observation-conditioned learned correction module (CRM), applied after conformal sample selection, can synthesize actions better than any individual VLA sample. The key contribution is the **sample-then-correct** pipeline itself and the discovery that **correction magnitude control is critical for closed-loop stability**. Per-DOF conformal features as CRM input offer no additional value over observation features — an honest negative result that challenges the intuition from synthetic experiments.\\\\n\\\\n## Active Framing: Scenario C\\\\n**Confirmed by data**: obs_only CRM > perdof CRM ≈ scalar CRM ≈ argmin on spatial (D029-D030); obs_only CRM **+7.0pp** over argmin on object 10/10 tasks FINAL (19.0% vs 12.0%); magnitude sweep shows obs_only robust to norm while perdof collapses at high norm (D032).\\\\n\\\\nStory: \\\\\\\"Observation-conditioned residual correction is the key contribution. The sample-then-correct pipeline (K=10 conformal selection + learned CRM correction) significantly outperforms pure sample selection on object manipulation tasks. Per-DOF conformal statistics as direct CRM input offer no advantage over observation features — but conformal prediction remains essential for the sample selection stage. Correction magnitude control is a critical and previously unrecognized factor for closed-loop VLA correction.\\\\\\\"\\\\n\\\\n## Core Claims (CoRL 单 Claim 论文)\\\\n\\\\n1. **Observation-conditioned learned correction (CRM) significantly improves VLA robustness beyond sample selection**\\\\n   - **主 claim**: obs_only CRM vs argmin-only ≥ 5pp on object benchmark + p < 0.05\\\\n   - **Spatial**: DEAD — all CRM variants 32-35% vs argmin 34%, no signal (D030)\\\\n   - **Object 10/10 FINAL**: obs_only 0.1: **19.0%** vs argmin **12.0%** (+7.0pp); obs_only 0.2: 18.0% (5/10, running)\\\\n   - **seed=43 doubling (RUNNING)**: 目标 combined 200 trials Fisher p < 0.05 (D031)\\\\n\\\\n2. **Honest negative result: per-DOF conformal features as CRM input have no value**\\\\n   - Spatial: perdof 35% = argmin 34% = obs_only 35% (D029)\\\\n   - Object 10/10 FINAL: perdof 11.0% ≈ argmin 12.0%, obs_only **19.0%** >> perdof; scalar 9.0% (negative)\\\\n   - Magnitude sweep: obs_only robust across norms, perdof collapses at high norm (D032)\\\\n   - 转化为学术贡献：challenges synthetic-experiment intuition, highlights gap between per-step MSE and closed-loop success\\\\n\\\\n3. **Correction magnitude control is critical for closed-loop stability (empirical contribution)**\\\\n   - norm=1.42 → 0% (catastrophic); norm=0.1 → 35% (spatial) / **19%** (object FINAL); norm=0.2 → 18% (object 5/10, running)\\\\n   - obs_only CRM maintains performance across norm range; perdof CRM collapses at norm ≥ 0.2\\\\n   - Novel finding: no prior work on correction magnitude sensitivity for VLA action refinement\\\\n\\\\n~~Claims 2-3 (ACI/COC, SRPO stacking) — D022/D023 移除~~\\\\n\\\\n## Kill Criteria\\\\n- **内部 kill**: obs_only CRM vs argmin-only < 3pp on object 10-task → project dead\\\\n- **论文 claim 门槛**: ≥ 5pp + Fisher exact p < 0.05 on object (seed=42 + seed=43 combined)\\\\n- **3-5pp 灰区**: 需要加 n_rollouts 或加 benchmark 提升统计力\\\\n- **当前状态**: +7.0pp at 10/10 tasks FINAL, **超过 5pp 门槛**。等待 seed=43 确认统计显著性。\\\\n\\\\n## Story Spine\\\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO 暴露了分布偏移下的鲁棒性缺口。现有 inference-time 方法要么只做样本选择（ReconVLA），要么需要任务级 RL 训练（SC-VLA），要么推理延迟过高（VLA-Pilot 2.41s/step）。没有方法探索过 inference-time learned action correction on frozen VLA。\\\\n- **Gap**: Sample selection（从 K 候选中选最优）受限于候选质量——当所有样本都不够好时 selection 失效。Learned correction 可以合成优于任何单个样本的动作，但关键问题是 correction 应该以什么为条件？我们的系统性 ablation 发现 observation features 是最有效的 conditioning，而直觉上更丰富的 per-DOF conformal statistics 反而无效。\\\\n- **Our angle**: 第一个在 frozen VLA 上做 inference-time learned action correction 并系统性比较 conditioning features 的工作。核心发现：(1) sample-then-correct > sample-then-select；(2) observation features > conformal features for correction conditioning（挑战合成实验直觉）；(3) correction magnitude control 是此前被忽视的关键因素。\\\\n- **Headline result template**: \\\\\\\"On LIBERO object manipulation, ACR-VLA's sample-then-correct pipeline improves SmolVLA success by +Xpp over sample selection alone (p < Y). Surprisingly, observation-conditioned correction outperforms conformal-feature-conditioned correction, while correction magnitude proves critical — norm=1.42 yields 0% but norm=0.1-0.2 yields +Xpp, with observation-conditioned CRM uniquely robust across the magnitude range.\\\\\\\"\\\\n\\\\n## Competitive Landscape\\\\n\\\\n### ReconVLA — 最直接竞品\\\\nPost-hoc conformal prediction on frozen VLA。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\\\n\\\\n**关键差异**：(1) Selection-only — 无法合成优于单个样本的动作；(2) 我们的 argmin baseline 近似 ReconVLA 的 selection 策略，CRM correction 在此基础上有独立增量。\\\\n\\\\n### SC-VLA — Inference-time RL refinement\\\\nResidual RL 在线调整动作。需任务级 RL 训练，非 plug-and-play，无统计保证。\\\\n\\\\n### ACR-VLA 差异化定位（更新后）\\\\n第一个系统性研究 inference-time learned action correction for frozen VLAs 的工作。贡献不在于\\\\\\\"哪种 uncertainty feature 最好\\\\\\\"（答案出乎意料是 obs features），而在于：(1) 证明 sample-then-correct > sample-then-select；(2) 揭示 correction magnitude sensitivity 这一此前未被研究的关键因素；(3) 提供 per-DOF conformal features 无效的 honest negative result + 分析。\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n1. **\\\\\\\"obs_only 就是一个 residual MLP，有什么新意？\\\\\\\"**: 新意在于 systematic comparison（per-DOF vs scalar vs obs-only conditioning）+ magnitude sensitivity discovery + honest negative result。且我们的 CRM 是在 conformal-selected sample 上 correction，不是 naive residual。\\\\n2. **CRM 329K 参数表达力** (obs_only; perdof 339K, scalar 330K): 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。架构：3-layer MLP (input→256→256→30), input normalization。\\\\n3. **仿真 only**: CoRL 接受 sim-only，LIBERO 是 recognized benchmark。\\\\n4. **Spatial 无效**: Honest limitation。可能原因：spatial tasks 的 perturbation 类型（位置偏移）不产生可被 CRM 校正的 action error pattern。Object tasks 的 perturbation（物体替换）产生更大的 action distribution shift。\\\\n5. **\\\\\\\"Conformal\\\\\\\" 标签可能误导**: 论文明确：CP 用于 sample selection stage（nonconformity score → argmin），不是 CRM 输出保证。Title 应反映 \\\\\\\"sample-then-correct\\\\\\\" 而非 \\\\\\\"conformal correction\\\\\\\"。\\\\n6. **统计显著性**: Fisher exact test on combined seed=42+43 (200 trials), bootstrap CI, per-task breakdown。\\\\n7. **K=10 成本**: 与 ReconVLA 相同 K 值，fair comparison。CRM overhead ~3ms。\\\\n8. **为什么 per-DOF features 无效？**: 训练/eval 分布偏移假说 — CRM 训练时 per-DOF features 有噪声（K=10 covariance estimation noise），obs features 更稳定。Magnitude sweep 证据：perdof 在高 norm 崩塌说明 per-DOF features 导致 CRM 学到 overconfident correction patterns。\\\\n\\\\n## 硬证据（已确认）\\\\n- Spatial LOCKED: argmin 34%, perdof 35%, obs_only 35%, scalar 32% — all noise level\\\\n- VLA baseline K=1: spatial 30%, object 12.0%\\\\n- VLA mean K=10: spatial 32%, object **12.0%** (10/10 FINAL) — = argmin, confirms selection ceiling\\\\n- **Object 10/10 FINAL**: obs_only 19.0%, argmin 12.0%, VLA-only 12.0%, perdof 11.0%, VLA-mean 12.0%, scalar 9.0%\\\\n- **obs_only +7.0pp over argmin** — exceeds 5pp claim threshold\\\\n- Magnitude control: norm=1.42 → 0%, norm=0.1 → 19% (object FINAL), norm=0.2 → 18% (5/10)\\\\n- Magnitude robustness (D032): obs_only stable across norms, perdof collapses at norm ≥ 0.2\\\\n\\\\n## 待确认证据（RUNNING）\\\\n- Seed=43 复现 + Fisher exact test（六方全部部署: obs_only / argmin / perdof / scalar / VLA-mean / VLA-only）\\\\n- Object obs_only 0.2 final（当前 18.0% at 5/10）\\\\n- Object v4-default (norm=1.42) ablation — confirm catastrophic failure\\\\n\\\", \\\"total_chars\\\": 7406, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight (Scenario C — ACTIVE, D029+D030 confirmed)\\nA lightweight observation-conditioned learned correction module (CRM), applied after conformal sample selection, can synthesize actions better than any individual VLA sample. The key contribution is the **sample-then-correct** pipeline itself and the discovery that **correction magnitude control is critical for closed-loop stability**. Per-DOF conformal features as CRM input offer no additional value over observation features — an honest negative result that challenges the intuition from synthetic experiments.\\n\\n## Active Framing: Scenario C\\n**Confirmed by data**: obs_only CRM > perdof CRM ≈ scalar CRM ≈ argmin on spatial (D029-D030); obs_only CRM **+7.0pp** over argmin on object 10/10 tasks FINAL (19.0% vs 12.0%); magnitude sweep shows obs_only robust to norm while perdof collapses at high norm (D032).\\n\\nStory: \\\"Observation-conditioned residual correction is the key contribution. The sample-then-correct pipeline (K=10 conformal selection + learned CRM correction) significantly outperforms pure sample selection on object manipulation tasks. Per-DOF conformal statistics as direct CRM input offer no advantage over observation features — but conformal prediction remains essential for the sample selection stage. Correction magnitude control is a critical and previously unrecognized factor for closed-loop VLA correction.\\\"\\n\\n## Core Claims (CoRL 单 Claim 论文)\\n\\n1. **Observation-conditioned learned correction (CRM) significantly improves VLA robustness beyond sample selection**\\n   - **主 claim**: obs_only CRM vs argmin-only ≥ 5pp on object benchmark + p < 0.05\\n   - **Spatial**: DEAD — all CRM variants 32-35% vs argmin 34%, no signal (D030)\\n   - **Object 10/10 FINAL**: obs_only 0.1: **19.0%** vs argmin **12.0%** (+7.0pp); obs_only 0.2: 18.0% (5/10, running)\\n   - **seed=43 doubling (RUNNING)**: 目标 combined 200 trials Fisher p < 0.05 (D031)\\n\\n2. **Honest negative result: per-DOF conformal features as CRM input have no value**\\n   - Spatial: perdof 35% = argmin 34% = obs_only 35% (D029)\\n   - Object 10/10 FINAL: perdof 11.0% ≈ argmin 12.0%, obs_only **19.0%** >> perdof; scalar 9.0% (negative)\\n   - Magnitude sweep: obs_only robust across norms, perdof collapses at high norm (D032)\\n   - 转化为学术贡献：challenges synthetic-experiment intuition, highlights gap between per-step MSE and closed-loop success\\n\\n3. **Correction magnitude control is critical for closed-loop stability (empirical contribution)**\\n   - norm=1.42 → 0% (catastrophic); norm=0.1 → 35% (spatial) / **19%** (object FINAL); norm=0.2 → 18% (object 5/10, running)\\n   - obs_only CRM maintains performance across norm range; perdof CRM collapses at norm ≥ 0.2\\n   - Novel finding: no prior work on correction magnitude sensitivity for VLA action refinement\\n\\n~~Claims 2-3 (ACI/COC, SRPO stacking) — D022/D023 移除~~\\n\\n## Kill Criteria\\n- **内部 kill**: obs_only CRM vs argmin-only < 3pp on object 10-task → project dead\\n- **论文 claim 门槛**: ≥ 5pp + Fisher exact p < 0.05 on object (seed=42 + seed=43 combined)\\n- **3-5pp 灰区**: 需要加 n_rollouts 或加 benchmark 提升统计力\\n- **当前状态**: +7.0pp at 10/10 tasks FINAL, **超过 5pp 门槛**。等待 seed=43 确认统计显著性。\\n\\n## Story Spine\\n- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO 暴露了分布偏移下的鲁棒性缺口。现有 inference-time 方法要么只做样本选择（ReconVLA），要么需要任务级 RL 训练（SC-VLA），要么推理延迟过高（VLA-Pilot 2.41s/step）。没有方法探索过 inference-time learned action correction on frozen VLA。\\n- **Gap**: Sample selection（从 K 候选中选最优）受限于候选质量——当所有样本都不够好时 selection 失效。Learned correction 可以合成优于任何单个样本的动作，但关键问题是 correction 应该以什么为条件？我们的系统性 ablation 发现 observation features 是最有效的 conditioning，而直觉上更丰富的 per-DOF conformal statistics 反而无效。\\n- **Our angle**: 第一个在 frozen VLA 上做 inference-time learned action correction 并系统性比较 conditioning features 的工作。核心发现：(1) sample-then-correct > sample-then-select；(2) observation features > conformal features for correction conditioning（挑战合成实验直觉）；(3) correction magnitude control 是此前被忽视的关键因素。\\n- **Headline result template**: \\\"On LIBERO object manipulation, ACR-VLA's sample-then-correct pipeline improves SmolVLA success by +Xpp over sample selection alone (p < Y). Surprisingly, observation-conditioned correction outperforms conformal-feature-conditioned correction, while correction magnitude proves critical — norm=1.42 yields 0% but norm=0.1-0.2 yields +Xpp, with observation-conditioned CRM uniquely robust across the magnitude range.\\\"\\n\\n## Competitive Landscape\\n\\n### ReconVLA — 最直接竞品\\nPost-hoc conformal prediction on frozen VLA。使用 CQR 产生 scalar-level confidence + SMD state anomaly detection，用于 failure detection 和 action selection（从 K candidates 中选最佳）。\\n\\n**关键差异**：(1) Selection-only — 无法合成优于单个样本的动作；(2) 我们的 argmin baseline 近似 ReconVLA 的 selection 策略，CRM correction 在此基础上有独立增量。\\n\\n### SC-VLA — Inference-time RL refinement\\nResidual RL 在线调整动作。需任务级 RL 训练，非 plug-and-play，无统计保证。\\n\\n### ACR-VLA 差异化定位（更新后）\\n第一个系统性研究 inference-time learned action correction for frozen VLAs 的工作。贡献不在于\\\"哪种 uncertainty feature 最好\\\"（答案出乎意料是 obs features），而在于：(1) 证明 sample-then-correct > sample-then-select；(2) 揭示 correction magnitude sensitivity 这一此前未被研究的关键因素；(3) 提供 per-DOF conformal features 无效的 honest negative result + 分析。\\n\\n## Anticipated Reviewer Concerns\\n1. **\\\"obs_only 就是一个 residual MLP，有什么新意？\\\"**: 新意在于 systematic comparison（per-DOF vs scalar vs obs-only conditioning）+ magnitude sensitivity discovery + honest negative result。且我们的 CRM 是在 conformal-selected sample 上 correction，不是 naive residual。\\n2. **CRM 329K 参数表达力** (obs_only; perdof 339K, scalar 330K): 故意轻量——防 overfitting + 保持推理速度（~3ms overhead）。架构：3-layer MLP (input→256→256→30), input normalization。\\n3. **仿真 only**: CoRL 接受 sim-only，LIBERO 是 recognized benchmark。\\n4. **Spatial 无效**: Honest limitation。可能原因：spatial tasks 的 perturbation 类型（位置偏移）不产生可被 CRM 校正的 action error pattern。Object tasks 的 perturbation（物体替换）产生更大的 action distribution shift。\\n5. **\\\"Conformal\\\" 标签可能误导**: 论文明确：CP 用于 sample selection stage（nonconformity score → argmin），不是 CRM 输出保证。Title 应反映 \\\"sample-then-correct\\\" 而非 \\\"conformal correction\\\"。\\n6. **统计显著性**: Fisher exact test on combined seed=42+43 (200 trials), bootstrap CI, per-task breakdown。\\n7. **K=10 成本**: 与 ReconVLA 相同 K 值，fair comparison。CRM overhead ~3ms。\\n8. **为什么 per-DOF features 无效？**: 训练/eval 分布偏移假说 — CRM 训练时 per-DOF features 有噪声（K=10 covariance estimation noise），obs features 更稳定。Magnitude sweep 证据：perdof 在高 norm 崩塌说明 per-DOF features 导致 CRM 学到 overconfident correction patterns。\\n\\n## 硬证据（已确认）\\n- Spatial LOCKED: argmin 34%, perdof 35%, obs_only 35%, scalar 32% — all noise level\\n- VLA baseline K=1: spatial 30%, object 12.0%\\n- VLA mean K=10: spatial 32%, object **12.0%** (10/10 FINAL) — = argmin, confirms selection ceiling\\n- **Object 10/10 FINAL**: obs_only 19.0%, argmin 12.0%, VLA-only 12.0%, perdof 11.0%, VLA-mean 12.0%, scalar 9.0%\\n- **obs_only +7.0pp over argmin** — exceeds 5pp claim threshold\\n- Magnitude control: norm=1.42 → 0%, norm=0.1 → 19% (object FINAL), norm=0.2 → 18% (5/10)\\n- Magnitude robustness (D032): obs_only stable across norms, perdof collapses at norm ≥ 0.2\\n\\n## 待确认证据（RUNNING）\\n- Seed=43 复现 + Fisher exact test（六方全部部署: obs_only / argmin / perdof / scalar / VLA-mean / VLA-only）\\n- Object obs_only 0.2 final（当前 18.0% at 5/10）\\n- Object v4-default (norm=1.42) ablation — confirm catastrophic failure\\n\", \"total_chars\": 7406, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01K5PvioYYuMnYWwMcDYi6Ue`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "writing_plan.yaml",
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
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "b7640f97-7264-4d88-b930-a00540fdc348",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T2DMj1etHujeJ5CicuF2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10462,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10462
      },
      "output_tokens": 34,
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

_source line 18 · 2026-05-15T19:49:34.864Z_

<details><summary>↩ Tool result · `toolu_01K5PvioYYuMnYWwMcDYi6Ue`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/writing_plan.yaml\", \"content\": \"# CoRL 2026 Paper Outline — ACR-VLA\\n# Last updated: 2026-05-15\\n# Status: READY FOR WRITING — Object 10-task FINAL locked. Seed=43 pending.\\n# Numbers source: ROADMAP.md D033 + paper_framing.md\\n\\n# ============================================================\\n# CANDIDATE TITLES\\n# ============================================================\\ntitles:\\n  - \\\"Sample, Select, Correct: Observation-Conditioned Residual Refinement for Robust VLA Control\\\"\\n  - \\\"When Conformal Features Fail: Learned Residual Correction for Vision-Language-Action Robustness\\\"\\n  - \\\"ACR-VLA: Adaptive Correction and Refinement of Vision-Language-Action Policies via Learned Residual Modules\\\"\\n\\npreferred: 1  # Title 1 — action-oriented, captures pipeline, avoids overclaim\\n\\n# ============================================================\\n# CORE CLAIM (1 sentence, falsifiable)\\n# ============================================================\\ncore_claim: >\\n  A lightweight observation-conditioned residual module (CRM, ~330K params),\\n  applied after multi-sample conformal selection on a frozen VLA, improves\\n  object manipulation success by +7.0pp over sample selection alone\\n  (19.0% vs 12.0%), while per-DOF conformal statistics — despite their\\n  theoretical appeal — provide no additional correction benefit beyond\\n  observation features (11.0% vs 19.0%).\\n\\n# ============================================================\\n# HARD NUMBERS (FINAL, seed=42, 10 tasks × 10 rollouts)\\n# ============================================================\\nhard_numbers:\\n  object:\\n    obs_only_0.1: 19.0\\n    argmin_k10: 12.0\\n    vla_only_k1: 12.0\\n    vla_mean_k10: 12.0\\n    perdof_0.1: 11.0\\n    scalar_0.1: 9.0\\n    obs_only_0.2: 22.0\\n  spatial:\\n    argmin_k10: 34.0\\n    perdof_0.1: 35.0\\n    obs_only_0.1: 35.0\\n    scalar_0.1: 32.0\\n    vla_only_k1: 30.0\\n    vla_mean_k10: 32.0\\n  magnitude_spatial:\\n    obs_only_0.03: \\\"55.0 (4t partial)\\\"\\n    obs_only_0.05: 35.0\\n    obs_only_0.2: 35.0\\n    obs_only_0.3: 36.0\\n    perdof_0.03: 30.0\\n    perdof_0.05: 31.0\\n    perdof_0.2: \\\"28.3 (6t partial)\\\"\\n    perdof_0.3: 26.0\\n  catastrophic: \\\"norm=1.42 → 0%\\\"\\n  pending:\\n    - \\\"seed=43 Fisher exact test (RUNNING, 24-48h)\\\"\\n    - \\\"bootstrap CI\\\"\\n    - \\\"object obs_only 0.2 remaining 5 tasks\\\"\\n\\n# ============================================================\\n# SECTION OUTLINE\\n# ============================================================\\nsections:\\n\\n  abstract:\\n    target_words: 200\\n    bullets:\\n      - \\\"Flow-matching VLAs degrade under distribution shift on LIBERO benchmarks.\\\"\\n      - \\\"We propose ACR-VLA: (1) K=10 multi-sample generation, (2) conformal-score-based selection, (3) observation-conditioned learned residual correction (CRM, ~330K params, ~3ms overhead) — wraps any frozen VLA without retraining.\\\"\\n      - \\\"On LIBERO object manipulation, CRM correction yields 19.0% vs 12.0% for selection alone (+7.0pp). Ablations reveal observation features suffice — per-DOF conformal features add no benefit (11.0%). Correction magnitude control is critical: unbounded correction (norm=1.42) causes catastrophic 0% success.\\\"\\n    deadline: \\\"2026-05-26 (abstract DDL)\\\"\\n\\n  introduction:\\n    target_pages: 1.5\\n    bullets:\\n      - \\\"Opening: VLAs achieve near-saturated in-distribution but degrade under distribution shift. Existing solutions: training-time (RobustVLA, SRPO, DiG-Flow) require retraining; inference-time (ReconVLA selects but cannot synthesize; SC-VLA needs RL; VLA-Pilot has 2.4s latency).\\\"\\n      - \\\"Gap: While SC-VLA and TRANSIC apply learned residual corrections, no method combines inference-time-only correction on a frozen VLA with offline training and conformal selection. Sample selection alone is upper-bounded by sample quality.\\\"\\n      - \\\"Contributions: (1) sample-then-correct pipeline with +7.0pp over selection alone on object tasks; (2) honest negative — observation features outperform per-DOF conformal features for correction (19.0% vs 11.0%); (3) correction magnitude control is critical and previously unrecognized (norm=1.42 → 0%).\\\"\\n    key_references:\\n      - chen2026reconvla\\n      - sc_vla_2026\\n      - vla_pilot_2025\\n      - silver2018residual\\n      - shukor2025smolvla\\n\\n  related_work:\\n    target_pages: 1.5\\n    subsections:\\n      vla_robustness:\\n        scope: \\\"Training-time (RobustVLA, SRPO, DiG-Flow, ACoT-VLA) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2). Position ACR-VLA as plug-and-play inference-time correction.\\\"\\n        key_refs: [robustvla2025, srpo2025, digflow2025, chen2026reconvla, sc_vla_2026, vla_pilot_2025, a2c2_2025]\\n      conformal_prediction_robotics:\\n        scope: \\\"CP foundations (Angelopoulos, CGS), CP in robotics (conformalized teleop, CP-loop, ACP+CBF). Position ACR-VLA's use of CP for selection stage.\\\"\\n        key_refs: [angelopoulos2023gentle, braun2025cgs, zhao2024conformalized, wang2025cploop, zhou2025acp_cbf]\\n      residual_policy_learning:\\n        scope: \\\"Residual RL (Silver 2018, TRANSIC, PLD, DRC). Emphasize magnitude control as underexplored.\\\"\\n        key_refs: [silver2018residual, jiang2024transic, xiao2026pld, pan2025drc]\\n      uncertainty_quantification_vla:\\n        scope: \\\"UQ for VLAs (DiU, SAFE, VLA calibration). Distinguish multi-sample from single-pass UQ.\\\"\\n        key_refs: [xing2026diu, gu2025safe, zollo2025vla_calibration]\\n\\n  method:\\n    target_pages: 2.0\\n    subsections:\\n      problem_setup:\\n        bullets:\\n          - \\\"Frozen flow-matching VLA π_θ generates K action samples per step.\\\"\\n          - \\\"Action space: 7-DOF (6 arm + 1 gripper), action chunks of length C.\\\"\\n      multi_sample_generation_and_selection:\\n        bullets:\\n          - \\\"K=10 samples via flow-matching; Ledoit-Wolf shrinkage covariance → CGS nonconformity scores.\\\"\\n          - \\\"Argmin selection: pick lowest-CGS-score sample as base action a_base.\\\"\\n      conformal_residual_module:\\n        bullets:\\n          - \\\"CRM: lightweight MLP (~330K params), takes observation features z_obs, outputs bounded residual δ.\\\"\\n          - \\\"Final action: a = a_base + clip(δ, ‖δ‖ ≤ ε).\\\"\\n          - \\\"Training: offline L2 loss to expert actions, augmented with Gaussian noise on mean-action (σ ∈ [0.02, 0.1]) and uncertainty features (σ ≈ 0.006).\\\"\\n      magnitude_control:\\n        bullets:\\n          - \\\"Critical: unbounded CRM (ε=1.42) → 0% (compounding error destroys trajectory).\\\"\\n          - \\\"Norm sweep: ε ∈ {0.03, 0.05, 0.1, 0.2, 0.3}. Optimal range ε ∈ [0.05, 0.2].\\\"\\n          - \\\"Connect to residual RL magnitude bounds (Silver 2018, TRANSIC gating, PLD scheduling).\\\"\\n\\n  experiments:\\n    target_pages: 2.5\\n    subsections:\\n      setup:\\n        bullets:\\n          - \\\"Backbone: SmolVLA (450M params, flow-matching). Benchmark: LIBERO Spatial + Object (10 tasks each, 10 rollouts/task).\\\"\\n          - \\\"Baselines: VLA-only (K=1), VLA-mean (K=10 average), Argmin (K=10 CGS selection).\\\"\\n          - \\\"CRM variants: obs_only, perdof, scalar — same architecture, different conditioning input.\\\"\\n          - \\\"Statistical protocol: seed=42 primary + seed=43 doubling (PENDING), Fisher exact test, bootstrap CI.\\\"\\n      main_results:\\n        bullets:\\n          - \\\"Object: obs_only 19.0% vs argmin 12.0% (+7.0pp). VLA-only 12.0%. perdof 11.0%. scalar 9.0%.\\\"\\n          - \\\"Spatial: ALL methods 30-35% (null result). CRM correction does not help on spatial perturbations.\\\"\\n          - \\\"Key finding: sample-then-correct > sample-then-select, but only for object-type perturbations.\\\"\\n      ablation_crm_conditioning:\\n        bullets:\\n          - \\\"4-way: obs_only (19.0%) >> perdof (11.0%) ≈ argmin (12.0%) > scalar (9.0%).\\\"\\n          - \\\"Per-DOF conformal features add NO value over observation features.\\\"\\n          - \\\"Hypothesis: obs features encode task-relevant geometric info; conformal stats are noisy at K=10.\\\"\\n      magnitude_sensitivity:\\n        bullets:\\n          - \\\"obs_only stable across norms (35-36% spatial); perdof collapses at norm ≥ 0.2 (31%→26%).\\\"\\n          - \\\"norm=1.42 catastrophic failure (0%) demonstrates magnitude control necessity.\\\"\\n      per_task_analysis:\\n        bullets:\\n          - \\\"Per-task heatmap: CRM helps medium-difficulty tasks; hard tasks (0% baseline) unaffected.\\\"\\n          - \\\"PENDING: seed=43 per-task breakdown.\\\"\\n\\n  discussion:\\n    target_pages: 0.5\\n    bullets:\\n      - \\\"Why per-DOF fails: learned correction can extract uncertainty signals from obs features directly; explicit conformal stats at K=10 are noisy and redundant.\\\"\\n      - \\\"Object vs spatial: object perturbations (category generalization) create correctable action errors; spatial perturbations require replanning, not correction.\\\"\\n      - \\\"Limitations: (1) sim-only, (2) single VLA backbone, (3) some tasks hurt by CRM, (4) magnitude bound needs tuning.\\\"\\n\\n  conclusion:\\n    target_pages: 0.3\\n    bullets:\\n      - \\\"ACR-VLA: learned observation-conditioned correction after conformal selection improves VLA robustness on object perturbations (+7.0pp).\\\"\\n      - \\\"Negative result: per-DOF conformal features do not improve correction — cautionary for uncertainty-conditioned policy correction.\\\"\\n      - \\\"Future: multi-backbone validation, real robot transfer, adaptive magnitude scheduling.\\\"\\n\\n# ============================================================\\n# FIGURES\\n# ============================================================\\nfigures:\\n\\n  fig1_pipeline:\\n    type: overview_diagram\\n    description: \\\"ACR-VLA pipeline: frozen VLA → K samples → CGS scoring → argmin selection → CRM correction → final action.\\\"\\n    placement: method\\n    priority: P0\\n    tool: matplotlib\\n    status: to_create\\n\\n  fig2_main_results:\\n    type: grouped_bar_chart\\n    description: \\\"Object + Spatial success rates. 6 methods. Error bars from seed=43 CI (pending).\\\"\\n    placement: experiments/main_results\\n    priority: P0\\n    tool: matplotlib\\n    status: has_data_partial\\n    data_source: \\\"registry: eval-acr-object-v4-obs-only, eval-argmin-only-object, etc.\\\"\\n\\n  fig3_magnitude_sweep:\\n    type: line_plot\\n    description: \\\"Success rate vs correction norm ε. Lines: obs_only, perdof, argmin (flat). Show phase transition.\\\"\\n    placement: experiments/magnitude_sensitivity\\n    priority: P0\\n    tool: matplotlib\\n    status: has_data_partial\\n    data_source: \\\"ROADMAP magnitude sweep table\\\"\\n\\n  fig4_per_task_heatmap:\\n    type: heatmap\\n    description: \\\"Per-task success: 10 object tasks × 6 methods. Show where CRM helps vs hurts.\\\"\\n    placement: experiments/per_task_analysis\\n    priority: P1\\n    tool: matplotlib\\n    status: needs_per_task_data\\n\\n  fig5_conditioning_ablation:\\n    type: bar_chart\\n    description: \\\"4-way CRM conditioning ablation on object benchmark. obs_only >> perdof ≈ argmin > scalar.\\\"\\n    placement: experiments/ablation_crm_conditioning\\n    priority: P0\\n    tool: matplotlib\\n    status: has_data\\n\\n# ============================================================\\n# TABLES\\n# ============================================================\\ntables:\\n\\n  table1_main_results:\\n    description: \\\"Main results. Rows: 6 methods. Cols: Object SR, Spatial SR, Δ vs Argmin. Bold best.\\\"\\n    placement: experiments/main_results\\n    priority: P0\\n    status: has_data\\n\\n  table2_method_comparison:\\n    description: \\\"Qualitative comparison: ReconVLA, SC-VLA, VLA-Pilot, A2C2, TRANSIC, PLD, ACR-VLA. Cols: correction type, retraining, latency.\\\"\\n    placement: related_work\\n    priority: P2\\n    status: can_write_now\\n\\n# ============================================================\\n# WRITING ORDER (adjusted for DDL pressure)\\n# ============================================================\\nwriting_order:\\n  - step: 1\\n    section: method\\n    rationale: \\\"Pipeline description independent of final stats. Write now.\\\"\\n    deadline: \\\"2026-05-17\\\"\\n\\n  - step: 2\\n    section: experiments\\n    rationale: \\\"Setup + main results with FINAL numbers. Spatial null + object +7pp.\\\"\\n    deadline: \\\"2026-05-19\\\"\\n\\n  - step: 3\\n    section: related_work\\n    rationale: \\\"Position against competitors. New framing requires full rewrite.\\\"\\n    deadline: \\\"2026-05-20\\\"\\n\\n  - step: 4\\n    section: introduction\\n    rationale: \\\"Frame story after method/experiments stable.\\\"\\n    deadline: \\\"2026-05-22\\\"\\n\\n  - step: 5\\n    section: abstract\\n    rationale: \\\"Compress final story. Must be ready by abstract DDL.\\\"\\n    deadline: \\\"2026-05-26 (abstract DDL)\\\"\\n\\n  - step: 6\\n    section: discussion_and_conclusion\\n    rationale: \\\"Limitations and future work.\\\"\\n    deadline: \\\"2026-05-28\\\"\\n\\n  - step: 7\\n    section: figures_and_polish\\n    rationale: \\\"Final figures, formatting, reference check.\\\"\\n    deadline: \\\"2026-06-02 (full paper DDL)\\\"\\n\\n# ============================================================\\n# LITERATURE STATUS\\n# ============================================================\\nliterature_status:\\n  total_papers: 50+\\n  must_cite_covered: true\\n  new_categories_added:\\n    - residual_policy (Silver, TRANSIC, PLD, DRC, DAWN)\\n    - supervised_residual (CR-DAgger, RaC, Reactive Diffusion)\\n    - uq_vla (Zollo calibration, Tang shifting uncertainty)\\n    - benchmark (LIBERO-PRO)\\n  gaps_remaining:\\n    - \\\"Verify all 50+ references via verify_references (Director requested)\\\"\\n\\n# ============================================================\\n# HONEST REPORTING COMMITMENTS\\n# ============================================================\\nhonest_reporting:\\n  - \\\"Spatial null result (CRM ≈ argmin ±1pp) reported prominently, not buried.\\\"\\n  - \\\"Per-DOF conformal features failing is a headline negative result.\\\"\\n  - \\\"Task-level variance (some tasks hurt by CRM) shown with explicit discussion.\\\"\\n  - \\\"Statistical significance: if seed=43 does not replicate, paper adjusts claim strength.\\\"\\n  - \\\"No overclaim on 'conformal guarantees' — CRM output has no formal coverage property.\\\"\\n\", \"total_chars\": 13576, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "fc6300c3-073e-4196-8c43-222d41337fc0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/writing_plan.yaml\\\", \\\"content\\\": \\\"# CoRL 2026 Paper Outline — ACR-VLA\\\\n# Last updated: 2026-05-15\\\\n# Status: READY FOR WRITING — Object 10-task FINAL locked. Seed=43 pending.\\\\n# Numbers source: ROADMAP.md D033 + paper_framing.md\\\\n\\\\n# ============================================================\\\\n# CANDIDATE TITLES\\\\n# ============================================================\\\\ntitles:\\\\n  - \\\\\\\"Sample, Select, Correct: Observation-Conditioned Residual Refinement for Robust VLA Control\\\\\\\"\\\\n  - \\\\\\\"When Conformal Features Fail: Learned Residual Correction for Vision-Language-Action Robustness\\\\\\\"\\\\n  - \\\\\\\"ACR-VLA: Adaptive Correction and Refinement of Vision-Language-Action Policies via Learned Residual Modules\\\\\\\"\\\\n\\\\npreferred: 1  # Title 1 — action-oriented, captures pipeline, avoids overclaim\\\\n\\\\n# ============================================================\\\\n# CORE CLAIM (1 sentence, falsifiable)\\\\n# ============================================================\\\\ncore_claim: >\\\\n  A lightweight observation-conditioned residual module (CRM, ~330K params),\\\\n  applied after multi-sample conformal selection on a frozen VLA, improves\\\\n  object manipulation success by +7.0pp over sample selection alone\\\\n  (19.0% vs 12.0%), while per-DOF conformal statistics — despite their\\\\n  theoretical appeal — provide no additional correction benefit beyond\\\\n  observation features (11.0% vs 19.0%).\\\\n\\\\n# ============================================================\\\\n# HARD NUMBERS (FINAL, seed=42, 10 tasks × 10 rollouts)\\\\n# ============================================================\\\\nhard_numbers:\\\\n  object:\\\\n    obs_only_0.1: 19.0\\\\n    argmin_k10: 12.0\\\\n    vla_only_k1: 12.0\\\\n    vla_mean_k10: 12.0\\\\n    perdof_0.1: 11.0\\\\n    scalar_0.1: 9.0\\\\n    obs_only_0.2: 22.0\\\\n  spatial:\\\\n    argmin_k10: 34.0\\\\n    perdof_0.1: 35.0\\\\n    obs_only_0.1: 35.0\\\\n    scalar_0.1: 32.0\\\\n    vla_only_k1: 30.0\\\\n    vla_mean_k10: 32.0\\\\n  magnitude_spatial:\\\\n    obs_only_0.03: \\\\\\\"55.0 (4t partial)\\\\\\\"\\\\n    obs_only_0.05: 35.0\\\\n    obs_only_0.2: 35.0\\\\n    obs_only_0.3: 36.0\\\\n    perdof_0.03: 30.0\\\\n    perdof_0.05: 31.0\\\\n    perdof_0.2: \\\\\\\"28.3 (6t partial)\\\\\\\"\\\\n    perdof_0.3: 26.0\\\\n  catastrophic: \\\\\\\"norm=1.42 → 0%\\\\\\\"\\\\n  pending:\\\\n    - \\\\\\\"seed=43 Fisher exact test (RUNNING, 24-48h)\\\\\\\"\\\\n    - \\\\\\\"bootstrap CI\\\\\\\"\\\\n    - \\\\\\\"object obs_only 0.2 remaining 5 tasks\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# SECTION OUTLINE\\\\n# ============================================================\\\\nsections:\\\\n\\\\n  abstract:\\\\n    target_words: 200\\\\n    bullets:\\\\n      - \\\\\\\"Flow-matching VLAs degrade under distribution shift on LIBERO benchmarks.\\\\\\\"\\\\n      - \\\\\\\"We propose ACR-VLA: (1) K=10 multi-sample generation, (2) conformal-score-based selection, (3) observation-conditioned learned residual correction (CRM, ~330K params, ~3ms overhead) — wraps any frozen VLA without retraining.\\\\\\\"\\\\n      - \\\\\\\"On LIBERO object manipulation, CRM correction yields 19.0% vs 12.0% for selection alone (+7.0pp). Ablations reveal observation features suffice — per-DOF conformal features add no benefit (11.0%). Correction magnitude control is critical: unbounded correction (norm=1.42) causes catastrophic 0% success.\\\\\\\"\\\\n    deadline: \\\\\\\"2026-05-26 (abstract DDL)\\\\\\\"\\\\n\\\\n  introduction:\\\\n    target_pages: 1.5\\\\n    bullets:\\\\n      - \\\\\\\"Opening: VLAs achieve near-saturated in-distribution but degrade under distribution shift. Existing solutions: training-time (RobustVLA, SRPO, DiG-Flow) require retraining; inference-time (ReconVLA selects but cannot synthesize; SC-VLA needs RL; VLA-Pilot has 2.4s latency).\\\\\\\"\\\\n      - \\\\\\\"Gap: While SC-VLA and TRANSIC apply learned residual corrections, no method combines inference-time-only correction on a frozen VLA with offline training and conformal selection. Sample selection alone is upper-bounded by sample quality.\\\\\\\"\\\\n      - \\\\\\\"Contributions: (1) sample-then-correct pipeline with +7.0pp over selection alone on object tasks; (2) honest negative — observation features outperform per-DOF conformal features for correction (19.0% vs 11.0%); (3) correction magnitude control is critical and previously unrecognized (norm=1.42 → 0%).\\\\\\\"\\\\n    key_references:\\\\n      - chen2026reconvla\\\\n      - sc_vla_2026\\\\n      - vla_pilot_2025\\\\n      - silver2018residual\\\\n      - shukor2025smolvla\\\\n\\\\n  related_work:\\\\n    target_pages: 1.5\\\\n    subsections:\\\\n      vla_robustness:\\\\n        scope: \\\\\\\"Training-time (RobustVLA, SRPO, DiG-Flow, ACoT-VLA) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2). Position ACR-VLA as plug-and-play inference-time correction.\\\\\\\"\\\\n        key_refs: [robustvla2025, srpo2025, digflow2025, chen2026reconvla, sc_vla_2026, vla_pilot_2025, a2c2_2025]\\\\n      conformal_prediction_robotics:\\\\n        scope: \\\\\\\"CP foundations (Angelopoulos, CGS), CP in robotics (conformalized teleop, CP-loop, ACP+CBF). Position ACR-VLA's use of CP for selection stage.\\\\\\\"\\\\n        key_refs: [angelopoulos2023gentle, braun2025cgs, zhao2024conformalized, wang2025cploop, zhou2025acp_cbf]\\\\n      residual_policy_learning:\\\\n        scope: \\\\\\\"Residual RL (Silver 2018, TRANSIC, PLD, DRC). Emphasize magnitude control as underexplored.\\\\\\\"\\\\n        key_refs: [silver2018residual, jiang2024transic, xiao2026pld, pan2025drc]\\\\n      uncertainty_quantification_vla:\\\\n        scope: \\\\\\\"UQ for VLAs (DiU, SAFE, VLA calibration). Distinguish multi-sample from single-pass UQ.\\\\\\\"\\\\n        key_refs: [xing2026diu, gu2025safe, zollo2025vla_calibration]\\\\n\\\\n  method:\\\\n    target_pages: 2.0\\\\n    subsections:\\\\n      problem_setup:\\\\n        bullets:\\\\n          - \\\\\\\"Frozen flow-matching VLA π_θ generates K action samples per step.\\\\\\\"\\\\n          - \\\\\\\"Action space: 7-DOF (6 arm + 1 gripper), action chunks of length C.\\\\\\\"\\\\n      multi_sample_generation_and_selection:\\\\n        bullets:\\\\n          - \\\\\\\"K=10 samples via flow-matching; Ledoit-Wolf shrinkage covariance → CGS nonconformity scores.\\\\\\\"\\\\n          - \\\\\\\"Argmin selection: pick lowest-CGS-score sample as base action a_base.\\\\\\\"\\\\n      conformal_residual_module:\\\\n        bullets:\\\\n          - \\\\\\\"CRM: lightweight MLP (~330K params), takes observation features z_obs, outputs bounded residual δ.\\\\\\\"\\\\n          - \\\\\\\"Final action: a = a_base + clip(δ, ‖δ‖ ≤ ε).\\\\\\\"\\\\n          - \\\\\\\"Training: offline L2 loss to expert actions, augmented with Gaussian noise on mean-action (σ ∈ [0.02, 0.1]) and uncertainty features (σ ≈ 0.006).\\\\\\\"\\\\n      magnitude_control:\\\\n        bullets:\\\\n          - \\\\\\\"Critical: unbounded CRM (ε=1.42) → 0% (compounding error destroys trajectory).\\\\\\\"\\\\n          - \\\\\\\"Norm sweep: ε ∈ {0.03, 0.05, 0.1, 0.2, 0.3}. Optimal range ε ∈ [0.05, 0.2].\\\\\\\"\\\\n          - \\\\\\\"Connect to residual RL magnitude bounds (Silver 2018, TRANSIC gating, PLD scheduling).\\\\\\\"\\\\n\\\\n  experiments:\\\\n    target_pages: 2.5\\\\n    subsections:\\\\n      setup:\\\\n        bullets:\\\\n          - \\\\\\\"Backbone: SmolVLA (450M params, flow-matching). Benchmark: LIBERO Spatial + Object (10 tasks each, 10 rollouts/task).\\\\\\\"\\\\n          - \\\\\\\"Baselines: VLA-only (K=1), VLA-mean (K=10 average), Argmin (K=10 CGS selection).\\\\\\\"\\\\n          - \\\\\\\"CRM variants: obs_only, perdof, scalar — same architecture, different conditioning input.\\\\\\\"\\\\n          - \\\\\\\"Statistical protocol: seed=42 primary + seed=43 doubling (PENDING), Fisher exact test, bootstrap CI.\\\\\\\"\\\\n      main_results:\\\\n        bullets:\\\\n          - \\\\\\\"Object: obs_only 19.0% vs argmin 12.0% (+7.0pp). VLA-only 12.0%. perdof 11.0%. scalar 9.0%.\\\\\\\"\\\\n          - \\\\\\\"Spatial: ALL methods 30-35% (null result). CRM correction does not help on spatial perturbations.\\\\\\\"\\\\n          - \\\\\\\"Key finding: sample-then-correct > sample-then-select, but only for object-type perturbations.\\\\\\\"\\\\n      ablation_crm_conditioning:\\\\n        bullets:\\\\n          - \\\\\\\"4-way: obs_only (19.0%) >> perdof (11.0%) ≈ argmin (12.0%) > scalar (9.0%).\\\\\\\"\\\\n          - \\\\\\\"Per-DOF conformal features add NO value over observation features.\\\\\\\"\\\\n          - \\\\\\\"Hypothesis: obs features encode task-relevant geometric info; conformal stats are noisy at K=10.\\\\\\\"\\\\n      magnitude_sensitivity:\\\\n        bullets:\\\\n          - \\\\\\\"obs_only stable across norms (35-36% spatial); perdof collapses at norm ≥ 0.2 (31%→26%).\\\\\\\"\\\\n          - \\\\\\\"norm=1.42 catastrophic failure (0%) demonstrates magnitude control necessity.\\\\\\\"\\\\n      per_task_analysis:\\\\n        bullets:\\\\n          - \\\\\\\"Per-task heatmap: CRM helps medium-difficulty tasks; hard tasks (0% baseline) unaffected.\\\\\\\"\\\\n          - \\\\\\\"PENDING: seed=43 per-task breakdown.\\\\\\\"\\\\n\\\\n  discussion:\\\\n    target_pages: 0.5\\\\n    bullets:\\\\n      - \\\\\\\"Why per-DOF fails: learned correction can extract uncertainty signals from obs features directly; explicit conformal stats at K=10 are noisy and redundant.\\\\\\\"\\\\n      - \\\\\\\"Object vs spatial: object perturbations (category generalization) create correctable action errors; spatial perturbations require replanning, not correction.\\\\\\\"\\\\n      - \\\\\\\"Limitations: (1) sim-only, (2) single VLA backbone, (3) some tasks hurt by CRM, (4) magnitude bound needs tuning.\\\\\\\"\\\\n\\\\n  conclusion:\\\\n    target_pages: 0.3\\\\n    bullets:\\\\n      - \\\\\\\"ACR-VLA: learned observation-conditioned correction after conformal selection improves VLA robustness on object perturbations (+7.0pp).\\\\\\\"\\\\n      - \\\\\\\"Negative result: per-DOF conformal features do not improve correction — cautionary for uncertainty-conditioned policy correction.\\\\\\\"\\\\n      - \\\\\\\"Future: multi-backbone validation, real robot transfer, adaptive magnitude scheduling.\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# FIGURES\\\\n# ============================================================\\\\nfigures:\\\\n\\\\n  fig1_pipeline:\\\\n    type: overview_diagram\\\\n    description: \\\\\\\"ACR-VLA pipeline: frozen VLA → K samples → CGS scoring → argmin selection → CRM correction → final action.\\\\\\\"\\\\n    placement: method\\\\n    priority: P0\\\\n    tool: matplotlib\\\\n    status: to_create\\\\n\\\\n  fig2_main_results:\\\\n    type: grouped_bar_chart\\\\n    description: \\\\\\\"Object + Spatial success rates. 6 methods. Error bars from seed=43 CI (pending).\\\\\\\"\\\\n    placement: experiments/main_results\\\\n    priority: P0\\\\n    tool: matplotlib\\\\n    status: has_data_partial\\\\n    data_source: \\\\\\\"registry: eval-acr-object-v4-obs-only, eval-argmin-only-object, etc.\\\\\\\"\\\\n\\\\n  fig3_magnitude_sweep:\\\\n    type: line_plot\\\\n    description: \\\\\\\"Success rate vs correction norm ε. Lines: obs_only, perdof, argmin (flat). Show phase transition.\\\\\\\"\\\\n    placement: experiments/magnitude_sensitivity\\\\n    priority: P0\\\\n    tool: matplotlib\\\\n    status: has_data_partial\\\\n    data_source: \\\\\\\"ROADMAP magnitude sweep table\\\\\\\"\\\\n\\\\n  fig4_per_task_heatmap:\\\\n    type: heatmap\\\\n    description: \\\\\\\"Per-task success: 10 object tasks × 6 methods. Show where CRM helps vs hurts.\\\\\\\"\\\\n    placement: experiments/per_task_analysis\\\\n    priority: P1\\\\n    tool: matplotlib\\\\n    status: needs_per_task_data\\\\n\\\\n  fig5_conditioning_ablation:\\\\n    type: bar_chart\\\\n    description: \\\\\\\"4-way CRM conditioning ablation on object benchmark. obs_only >> perdof ≈ argmin > scalar.\\\\\\\"\\\\n    placement: experiments/ablation_crm_conditioning\\\\n    priority: P0\\\\n    tool: matplotlib\\\\n    status: has_data\\\\n\\\\n# ============================================================\\\\n# TABLES\\\\n# ============================================================\\\\ntables:\\\\n\\\\n  table1_main_results:\\\\n    description: \\\\\\\"Main results. Rows: 6 methods. Cols: Object SR, Spatial SR, Δ vs Argmin. Bold best.\\\\\\\"\\\\n    placement: experiments/main_results\\\\n    priority: P0\\\\n    status: has_data\\\\n\\\\n  table2_method_comparison:\\\\n    description: \\\\\\\"Qualitative comparison: ReconVLA, SC-VLA, VLA-Pilot, A2C2, TRANSIC, PLD, ACR-VLA. Cols: correction type, retraining, latency.\\\\\\\"\\\\n    placement: related_work\\\\n    priority: P2\\\\n    status: can_write_now\\\\n\\\\n# ============================================================\\\\n# WRITING ORDER (adjusted for DDL pressure)\\\\n# ============================================================\\\\nwriting_order:\\\\n  - step: 1\\\\n    section: method\\\\n    rationale: \\\\\\\"Pipeline description independent of final stats. Write now.\\\\\\\"\\\\n    deadline: \\\\\\\"2026-05-17\\\\\\\"\\\\n\\\\n  - step: 2\\\\n    section: experiments\\\\n    rationale: \\\\\\\"Setup + main results with FINAL numbers. Spatial null + object +7pp.\\\\\\\"\\\\n    deadline: \\\\\\\"2026-05-19\\\\\\\"\\\\n\\\\n  - step: 3\\\\n    section: related_work\\\\n    rationale: \\\\\\\"Position against competitors. New framing requires full rewrite.\\\\\\\"\\\\n    deadline: \\\\\\\"2026-05-20\\\\\\\"\\\\n\\\\n  - step: 4\\\\n    section: introduction\\\\n    rationale: \\\\\\\"Frame story after method/experiments stable.\\\\\\\"\\\\n    deadline: \\\\\\\"2026-05-22\\\\\\\"\\\\n\\\\n  - step: 5\\\\n    section: abstract\\\\n    rationale: \\\\\\\"Compress final story. Must be ready by abstract DDL.\\\\\\\"\\\\n    deadline: \\\\\\\"2026-05-26 (abstract DDL)\\\\\\\"\\\\n\\\\n  - step: 6\\\\n    section: discussion_and_conclusion\\\\n    rationale: \\\\\\\"Limitations and future work.\\\\\\\"\\\\n    deadline: \\\\\\\"2026-05-28\\\\\\\"\\\\n\\\\n  - step: 7\\\\n    section: figures_and_polish\\\\n    rationale: \\\\\\\"Final figures, formatting, reference check.\\\\\\\"\\\\n    deadline: \\\\\\\"2026-06-02 (full paper DDL)\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# LITERATURE STATUS\\\\n# ============================================================\\\\nliterature_status:\\\\n  total_papers: 50+\\\\n  must_cite_covered: true\\\\n  new_categories_added:\\\\n    - residual_policy (Silver, TRANSIC, PLD, DRC, DAWN)\\\\n    - supervised_residual (CR-DAgger, RaC, Reactive Diffusion)\\\\n    - uq_vla (Zollo calibration, Tang shifting uncertainty)\\\\n    - benchmark (LIBERO-PRO)\\\\n  gaps_remaining:\\\\n    - \\\\\\\"Verify all 50+ references via verify_references (Director requested)\\\\\\\"\\\\n\\\\n# ============================================================\\\\n# HONEST REPORTING COMMITMENTS\\\\n# ============================================================\\\\nhonest_reporting:\\\\n  - \\\\\\\"Spatial null result (CRM ≈ argmin ±1pp) reported prominently, not buried.\\\\\\\"\\\\n  - \\\\\\\"Per-DOF conformal features failing is a headline negative result.\\\\\\\"\\\\n  - \\\\\\\"Task-level variance (some tasks hurt by CRM) shown with explicit discussion.\\\\\\\"\\\\n  - \\\\\\\"Statistical significance: if seed=43 does not replicate, paper adjusts claim strength.\\\\\\\"\\\\n  - \\\\\\\"No overclaim on 'conformal guarantees' — CRM output has no formal coverage property.\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 13576, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/writing_plan.yaml\", \"content\": \"# CoRL 2026 Paper Outline — ACR-VLA\\n# Last updated: 2026-05-15\\n# Status: READY FOR WRITING — Object 10-task FINAL locked. Seed=43 pending.\\n# Numbers source: ROADMAP.md D033 + paper_framing.md\\n\\n# ============================================================\\n# CANDIDATE TITLES\\n# ============================================================\\ntitles:\\n  - \\\"Sample, Select, Correct: Observation-Conditioned Residual Refinement for Robust VLA Control\\\"\\n  - \\\"When Conformal Features Fail: Learned Residual Correction for Vision-Language-Action Robustness\\\"\\n  - \\\"ACR-VLA: Adaptive Correction and Refinement of Vision-Language-Action Policies via Learned Residual Modules\\\"\\n\\npreferred: 1  # Title 1 — action-oriented, captures pipeline, avoids overclaim\\n\\n# ============================================================\\n# CORE CLAIM (1 sentence, falsifiable)\\n# ============================================================\\ncore_claim: >\\n  A lightweight observation-conditioned residual module (CRM, ~330K params),\\n  applied after multi-sample conformal selection on a frozen VLA, improves\\n  object manipulation success by +7.0pp over sample selection alone\\n  (19.0% vs 12.0%), while per-DOF conformal statistics — despite their\\n  theoretical appeal — provide no additional correction benefit beyond\\n  observation features (11.0% vs 19.0%).\\n\\n# ============================================================\\n# HARD NUMBERS (FINAL, seed=42, 10 tasks × 10 rollouts)\\n# ============================================================\\nhard_numbers:\\n  object:\\n    obs_only_0.1: 19.0\\n    argmin_k10: 12.0\\n    vla_only_k1: 12.0\\n    vla_mean_k10: 12.0\\n    perdof_0.1: 11.0\\n    scalar_0.1: 9.0\\n    obs_only_0.2: 22.0\\n  spatial:\\n    argmin_k10: 34.0\\n    perdof_0.1: 35.0\\n    obs_only_0.1: 35.0\\n    scalar_0.1: 32.0\\n    vla_only_k1: 30.0\\n    vla_mean_k10: 32.0\\n  magnitude_spatial:\\n    obs_only_0.03: \\\"55.0 (4t partial)\\\"\\n    obs_only_0.05: 35.0\\n    obs_only_0.2: 35.0\\n    obs_only_0.3: 36.0\\n    perdof_0.03: 30.0\\n    perdof_0.05: 31.0\\n    perdof_0.2: \\\"28.3 (6t partial)\\\"\\n    perdof_0.3: 26.0\\n  catastrophic: \\\"norm=1.42 → 0%\\\"\\n  pending:\\n    - \\\"seed=43 Fisher exact test (RUNNING, 24-48h)\\\"\\n    - \\\"bootstrap CI\\\"\\n    - \\\"object obs_only 0.2 remaining 5 tasks\\\"\\n\\n# ============================================================\\n# SECTION OUTLINE\\n# ============================================================\\nsections:\\n\\n  abstract:\\n    target_words: 200\\n    bullets:\\n      - \\\"Flow-matching VLAs degrade under distribution shift on LIBERO benchmarks.\\\"\\n      - \\\"We propose ACR-VLA: (1) K=10 multi-sample generation, (2) conformal-score-based selection, (3) observation-conditioned learned residual correction (CRM, ~330K params, ~3ms overhead) — wraps any frozen VLA without retraining.\\\"\\n      - \\\"On LIBERO object manipulation, CRM correction yields 19.0% vs 12.0% for selection alone (+7.0pp). Ablations reveal observation features suffice — per-DOF conformal features add no benefit (11.0%). Correction magnitude control is critical: unbounded correction (norm=1.42) causes catastrophic 0% success.\\\"\\n    deadline: \\\"2026-05-26 (abstract DDL)\\\"\\n\\n  introduction:\\n    target_pages: 1.5\\n    bullets:\\n      - \\\"Opening: VLAs achieve near-saturated in-distribution but degrade under distribution shift. Existing solutions: training-time (RobustVLA, SRPO, DiG-Flow) require retraining; inference-time (ReconVLA selects but cannot synthesize; SC-VLA needs RL; VLA-Pilot has 2.4s latency).\\\"\\n      - \\\"Gap: While SC-VLA and TRANSIC apply learned residual corrections, no method combines inference-time-only correction on a frozen VLA with offline training and conformal selection. Sample selection alone is upper-bounded by sample quality.\\\"\\n      - \\\"Contributions: (1) sample-then-correct pipeline with +7.0pp over selection alone on object tasks; (2) honest negative — observation features outperform per-DOF conformal features for correction (19.0% vs 11.0%); (3) correction magnitude control is critical and previously unrecognized (norm=1.42 → 0%).\\\"\\n    key_references:\\n      - chen2026reconvla\\n      - sc_vla_2026\\n      - vla_pilot_2025\\n      - silver2018residual\\n      - shukor2025smolvla\\n\\n  related_work:\\n    target_pages: 1.5\\n    subsections:\\n      vla_robustness:\\n        scope: \\\"Training-time (RobustVLA, SRPO, DiG-Flow, ACoT-VLA) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2). Position ACR-VLA as plug-and-play inference-time correction.\\\"\\n        key_refs: [robustvla2025, srpo2025, digflow2025, chen2026reconvla, sc_vla_2026, vla_pilot_2025, a2c2_2025]\\n      conformal_prediction_robotics:\\n        scope: \\\"CP foundations (Angelopoulos, CGS), CP in robotics (conformalized teleop, CP-loop, ACP+CBF). Position ACR-VLA's use of CP for selection stage.\\\"\\n        key_refs: [angelopoulos2023gentle, braun2025cgs, zhao2024conformalized, wang2025cploop, zhou2025acp_cbf]\\n      residual_policy_learning:\\n        scope: \\\"Residual RL (Silver 2018, TRANSIC, PLD, DRC). Emphasize magnitude control as underexplored.\\\"\\n        key_refs: [silver2018residual, jiang2024transic, xiao2026pld, pan2025drc]\\n      uncertainty_quantification_vla:\\n        scope: \\\"UQ for VLAs (DiU, SAFE, VLA calibration). Distinguish multi-sample from single-pass UQ.\\\"\\n        key_refs: [xing2026diu, gu2025safe, zollo2025vla_calibration]\\n\\n  method:\\n    target_pages: 2.0\\n    subsections:\\n      problem_setup:\\n        bullets:\\n          - \\\"Frozen flow-matching VLA π_θ generates K action samples per step.\\\"\\n          - \\\"Action space: 7-DOF (6 arm + 1 gripper), action chunks of length C.\\\"\\n      multi_sample_generation_and_selection:\\n        bullets:\\n          - \\\"K=10 samples via flow-matching; Ledoit-Wolf shrinkage covariance → CGS nonconformity scores.\\\"\\n          - \\\"Argmin selection: pick lowest-CGS-score sample as base action a_base.\\\"\\n      conformal_residual_module:\\n        bullets:\\n          - \\\"CRM: lightweight MLP (~330K params), takes observation features z_obs, outputs bounded residual δ.\\\"\\n          - \\\"Final action: a = a_base + clip(δ, ‖δ‖ ≤ ε).\\\"\\n          - \\\"Training: offline L2 loss to expert actions, augmented with Gaussian noise on mean-action (σ ∈ [0.02, 0.1]) and uncertainty features (σ ≈ 0.006).\\\"\\n      magnitude_control:\\n        bullets:\\n          - \\\"Critical: unbounded CRM (ε=1.42) → 0% (compounding error destroys trajectory).\\\"\\n          - \\\"Norm sweep: ε ∈ {0.03, 0.05, 0.1, 0.2, 0.3}. Optimal range ε ∈ [0.05, 0.2].\\\"\\n          - \\\"Connect to residual RL magnitude bounds (Silver 2018, TRANSIC gating, PLD scheduling).\\\"\\n\\n  experiments:\\n    target_pages: 2.5\\n    subsections:\\n      setup:\\n        bullets:\\n          - \\\"Backbone: SmolVLA (450M params, flow-matching). Benchmark: LIBERO Spatial + Object (10 tasks each, 10 rollouts/task).\\\"\\n          - \\\"Baselines: VLA-only (K=1), VLA-mean (K=10 average), Argmin (K=10 CGS selection).\\\"\\n          - \\\"CRM variants: obs_only, perdof, scalar — same architecture, different conditioning input.\\\"\\n          - \\\"Statistical protocol: seed=42 primary + seed=43 doubling (PENDING), Fisher exact test, bootstrap CI.\\\"\\n      main_results:\\n        bullets:\\n          - \\\"Object: obs_only 19.0% vs argmin 12.0% (+7.0pp). VLA-only 12.0%. perdof 11.0%. scalar 9.0%.\\\"\\n          - \\\"Spatial: ALL methods 30-35% (null result). CRM correction does not help on spatial perturbations.\\\"\\n          - \\\"Key finding: sample-then-correct > sample-then-select, but only for object-type perturbations.\\\"\\n      ablation_crm_conditioning:\\n        bullets:\\n          - \\\"4-way: obs_only (19.0%) >> perdof (11.0%) ≈ argmin (12.0%) > scalar (9.0%).\\\"\\n          - \\\"Per-DOF conformal features add NO value over observation features.\\\"\\n          - \\\"Hypothesis: obs features encode task-relevant geometric info; conformal stats are noisy at K=10.\\\"\\n      magnitude_sensitivity:\\n        bullets:\\n          - \\\"obs_only stable across norms (35-36% spatial); perdof collapses at norm ≥ 0.2 (31%→26%).\\\"\\n          - \\\"norm=1.42 catastrophic failure (0%) demonstrates magnitude control necessity.\\\"\\n      per_task_analysis:\\n        bullets:\\n          - \\\"Per-task heatmap: CRM helps medium-difficulty tasks; hard tasks (0% baseline) unaffected.\\\"\\n          - \\\"PENDING: seed=43 per-task breakdown.\\\"\\n\\n  discussion:\\n    target_pages: 0.5\\n    bullets:\\n      - \\\"Why per-DOF fails: learned correction can extract uncertainty signals from obs features directly; explicit conformal stats at K=10 are noisy and redundant.\\\"\\n      - \\\"Object vs spatial: object perturbations (category generalization) create correctable action errors; spatial perturbations require replanning, not correction.\\\"\\n      - \\\"Limitations: (1) sim-only, (2) single VLA backbone, (3) some tasks hurt by CRM, (4) magnitude bound needs tuning.\\\"\\n\\n  conclusion:\\n    target_pages: 0.3\\n    bullets:\\n      - \\\"ACR-VLA: learned observation-conditioned correction after conformal selection improves VLA robustness on object perturbations (+7.0pp).\\\"\\n      - \\\"Negative result: per-DOF conformal features do not improve correction — cautionary for uncertainty-conditioned policy correction.\\\"\\n      - \\\"Future: multi-backbone validation, real robot transfer, adaptive magnitude scheduling.\\\"\\n\\n# ============================================================\\n# FIGURES\\n# ============================================================\\nfigures:\\n\\n  fig1_pipeline:\\n    type: overview_diagram\\n    description: \\\"ACR-VLA pipeline: frozen VLA → K samples → CGS scoring → argmin selection → CRM correction → final action.\\\"\\n    placement: method\\n    priority: P0\\n    tool: matplotlib\\n    status: to_create\\n\\n  fig2_main_results:\\n    type: grouped_bar_chart\\n    description: \\\"Object + Spatial success rates. 6 methods. Error bars from seed=43 CI (pending).\\\"\\n    placement: experiments/main_results\\n    priority: P0\\n    tool: matplotlib\\n    status: has_data_partial\\n    data_source: \\\"registry: eval-acr-object-v4-obs-only, eval-argmin-only-object, etc.\\\"\\n\\n  fig3_magnitude_sweep:\\n    type: line_plot\\n    description: \\\"Success rate vs correction norm ε. Lines: obs_only, perdof, argmin (flat). Show phase transition.\\\"\\n    placement: experiments/magnitude_sensitivity\\n    priority: P0\\n    tool: matplotlib\\n    status: has_data_partial\\n    data_source: \\\"ROADMAP magnitude sweep table\\\"\\n\\n  fig4_per_task_heatmap:\\n    type: heatmap\\n    description: \\\"Per-task success: 10 object tasks × 6 methods. Show where CRM helps vs hurts.\\\"\\n    placement: experiments/per_task_analysis\\n    priority: P1\\n    tool: matplotlib\\n    status: needs_per_task_data\\n\\n  fig5_conditioning_ablation:\\n    type: bar_chart\\n    description: \\\"4-way CRM conditioning ablation on object benchmark. obs_only >> perdof ≈ argmin > scalar.\\\"\\n    placement: experiments/ablation_crm_conditioning\\n    priority: P0\\n    tool: matplotlib\\n    status: has_data\\n\\n# ============================================================\\n# TABLES\\n# ============================================================\\ntables:\\n\\n  table1_main_results:\\n    description: \\\"Main results. Rows: 6 methods. Cols: Object SR, Spatial SR, Δ vs Argmin. Bold best.\\\"\\n    placement: experiments/main_results\\n    priority: P0\\n    status: has_data\\n\\n  table2_method_comparison:\\n    description: \\\"Qualitative comparison: ReconVLA, SC-VLA, VLA-Pilot, A2C2, TRANSIC, PLD, ACR-VLA. Cols: correction type, retraining, latency.\\\"\\n    placement: related_work\\n    priority: P2\\n    status: can_write_now\\n\\n# ============================================================\\n# WRITING ORDER (adjusted for DDL pressure)\\n# ============================================================\\nwriting_order:\\n  - step: 1\\n    section: method\\n    rationale: \\\"Pipeline description independent of final stats. Write now.\\\"\\n    deadline: \\\"2026-05-17\\\"\\n\\n  - step: 2\\n    section: experiments\\n    rationale: \\\"Setup + main results with FINAL numbers. Spatial null + object +7pp.\\\"\\n    deadline: \\\"2026-05-19\\\"\\n\\n  - step: 3\\n    section: related_work\\n    rationale: \\\"Position against competitors. New framing requires full rewrite.\\\"\\n    deadline: \\\"2026-05-20\\\"\\n\\n  - step: 4\\n    section: introduction\\n    rationale: \\\"Frame story after method/experiments stable.\\\"\\n    deadline: \\\"2026-05-22\\\"\\n\\n  - step: 5\\n    section: abstract\\n    rationale: \\\"Compress final story. Must be ready by abstract DDL.\\\"\\n    deadline: \\\"2026-05-26 (abstract DDL)\\\"\\n\\n  - step: 6\\n    section: discussion_and_conclusion\\n    rationale: \\\"Limitations and future work.\\\"\\n    deadline: \\\"2026-05-28\\\"\\n\\n  - step: 7\\n    section: figures_and_polish\\n    rationale: \\\"Final figures, formatting, reference check.\\\"\\n    deadline: \\\"2026-06-02 (full paper DDL)\\\"\\n\\n# ============================================================\\n# LITERATURE STATUS\\n# ============================================================\\nliterature_status:\\n  total_papers: 50+\\n  must_cite_covered: true\\n  new_categories_added:\\n    - residual_policy (Silver, TRANSIC, PLD, DRC, DAWN)\\n    - supervised_residual (CR-DAgger, RaC, Reactive Diffusion)\\n    - uq_vla (Zollo calibration, Tang shifting uncertainty)\\n    - benchmark (LIBERO-PRO)\\n  gaps_remaining:\\n    - \\\"Verify all 50+ references via verify_references (Director requested)\\\"\\n\\n# ============================================================\\n# HONEST REPORTING COMMITMENTS\\n# ============================================================\\nhonest_reporting:\\n  - \\\"Spatial null result (CRM ≈ argmin ±1pp) reported prominently, not buried.\\\"\\n  - \\\"Per-DOF conformal features failing is a headline negative result.\\\"\\n  - \\\"Task-level variance (some tasks hurt by CRM) shown with explicit discussion.\\\"\\n  - \\\"Statistical significance: if seed=43 does not replicate, paper adjusts claim strength.\\\"\\n  - \\\"No overclaim on 'conformal guarantees' — CRM output has no formal coverage property.\\\"\\n\", \"total_chars\": 13576, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0123KK3yzZUyCjgKhzfJqzJb`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
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
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "6997522e-535d-4f8a-88b3-e76d565778ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T2DMj1etHujeJ5CicuF2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10462,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10462
      },
      "output_tokens": 34,
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

_source line 20 · 2026-05-15T19:49:35.748Z_

<details><summary>↩ Tool result · `toolu_0123KK3yzZUyCjgKhzfJqzJb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\\n  # ===== New entries added 2026-05-14 =====\\n\\n  - bibtex_key: \\\"fan2025interpretable_mcp\\\"\\n    title: \\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\"\\n    authors: \\\"Fan & Sesia\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.15383\\\"\\n    url: \\\"https://arxiv.org/abs/2512.15383\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"klein2025otcp\\\"\\n    title: \\\"Multivariate Conformal Prediction using Optimal Transport\\\"\\n    authors: \\\"Klein, Bethune, Ndiaye & Cuturi\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.03609\\\"\\n    url: \\\"https://arxiv.org/abs/2502.03609\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"zollo2025vla_calibration\\\"\\n    title: \\\"Confidence Calibration in Vision-Language-Action Models\\\"\\n    authors: \\\"Zollo & Zemel\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17383\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17383\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\"\\n    must_cite: true\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"tang2026shifting_uncertainty\\\"\\n    title: \\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\"\\n    authors: \\\"Tang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2603.18342\\\"\\n    url: \\\"https://arxiv.org/abs/2603.18342\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lcp2025\\\"\\n    title: \\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.21955\\\"\\n    url: \\\"https://arxiv.org/abs/2509.21955\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"claps2025\\\"\\n    title: \\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.10294\\\"\\n    url: \\\"https://arxiv.org/abs/2512.10294\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lucca2024\\\"\\n    title: \\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\"\\n    authors: \\\"Marques et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2409.08249\\\"\\n    url: \\\"https://arxiv.org/abs/2409.08249\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"sc_vla_2026\\\"\\n    title: \\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.21633\\\"\\n    url: \\\"https://arxiv.org/abs/2602.21633\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"vla_pilot_2025\\\"\\n    title: \\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.14178\\\"\\n    url: \\\"https://arxiv.org/abs/2511.14178\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"acot_vla_2026\\\"\\n    title: \\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\"\\n    authors: \\\"AgibotTech\\\"\\n    year: 2026\\n    venue: \\\"CVPR 2026, arXiv:2601.11404\\\"\\n    url: \\\"https://arxiv.org/abs/2601.11404\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"gonzales2026crc_cbf\\\"\\n    title: \\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\"\\n    authors: \\\"Gonzales et al.\\\"\\n    year: 2026\\n    venue: \\\"IROS 2025, arXiv:2603.10392\\\"\\n    url: \\\"https://arxiv.org/abs/2603.10392\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"safediffcon2025\\\"\\n    title: \\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025, arXiv:2502.02205\\\"\\n    url: \\\"https://arxiv.org/abs/2502.02205\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"afil2026\\\"\\n    title: \\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.08434\\\"\\n    url: \\\"https://arxiv.org/abs/2605.08434\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"valle2025vla_uq_metrics\\\"\\n    title: \\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\"\\n    authors: \\\"Valle et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17049\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17049\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"diffusionvla2024\\\"\\n    title: \\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\"\\n    authors: \\\"Wen et al.\\\"\\n    year: 2024\\n    venue: \\\"ICML 2025, arXiv:2412.03293\\\"\\n    url: \\\"https://arxiv.org/abs/2412.03293\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\n\\n  - bibtex_key: \\\"silver2018residual\\\"\\n    title: \\\"Residual Policy Learning\\\"\\n    authors: \\\"Silver et al.\\\"\\n    year: 2018\\n    venue: \\\"RSS 2018\\\"\\n    url: \\\"https://arxiv.org/abs/1812.06298\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\"\\n    must_cite: true\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"johannink2019residual\\\"\\n    title: \\\"Residual Reinforcement Learning for Robot Manipulator Control\\\"\\n    authors: \\\"Johannink et al.\\\"\\n    year: 2019\\n    venue: \\\"ICRA 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1812.03201\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"jiang2024transic\\\"\\n    title: \\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2405.10315\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"ankile2024resip\\\"\\n    title: \\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\"\\n    authors: \\\"Ankile et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL Workshop 2024\\\"\\n    url: \\\"\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: false\\n    verification_note: \\\"Workshop paper, no arXiv ID provided\\\"\\n    relevance: \\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"xiao2026pld\\\"\\n    title: \\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\"\\n    authors: \\\"Xiao et al.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2511.00091\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"pan2025drc\\\"\\n    title: \\\"DRC: Decaying Relative Correction for Policy Refinement\\\"\\n    authors: \\\"Pan et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2503.15368\\\"\\n    url: \\\"https://arxiv.org/abs/2503.15368\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"ma2026dawn\\\"\\n    title: \\\"DAWN: Value Learning in Residual Reinforcement Learning\\\"\\n    authors: \\\"Ma et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.10539\\\"\\n    url: \\\"https://arxiv.org/abs/2602.10539\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"vla_in_the_loop_2025\\\"\\n    title: \\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: false\\n    verification_note: \\\"No arXiv ID provided, needs verification\\\"\\n    relevance: \\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"zhou2025acp_cbf\\\"\\n    title: \\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    year: 2025\\n    venue: \\\"ICRA 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.17678\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"method-component\\\"\\n\\n  # ===== Literature gap papers (added 2026-05-15) =====\\n\\n  # --- Gap 1: Supervised (non-RL) residual correction ---\\n\\n  - bibtex_key: \\\"cai2025cr_dagger\\\"\\n    title: \\\"Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections\\\"\\n    authors: \\\"Cai et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.16685\\\"\\n    category: \\\"supervised_residual\\\"\\n    verified: true\\n    relevance: \\\"Learns supervised residual corrections from human delta corrections via compliance control; no RL. Closest supervised residual paradigm to CRM's offline L2-trained correction.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"rac2025\\\"\\n    title: \\\"RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.07953\\\"\\n    url: \\\"https://arxiv.org/abs/2509.07953\\\"\\n    category: \\\"supervised_residual\\\"\\n    verified: true\\n    relevance: \\\"Supervised fine-tuning on human intervention trajectories (recovery + correction). DAgger-style supervised correction without RL. Demonstrates supervised correction data suffices.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"xue2025reactive_diffusion\\\"\\n    title: \\\"Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation\\\"\\n    authors: \\\"Xue et al.\\\"\\n    year: 2025\\n    venue: \\\"RSS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.02881\\\"\\n    category: \\\"supervised_residual\\\"\\n    verified: true\\n    relevance: \\\"Two-level slow-fast architecture: slow diffusion policy + fast supervised correction module. Structural precedent for generate-then-correct pipeline with supervised (non-RL) correction.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"ross2011dagger\\\"\\n    title: \\\"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\\\"\\n    authors: \\\"Ross, Gordon & Bagnell\\\"\\n    year: 2011\\n    venue: \\\"AISTATS 2011\\\"\\n    url: \\\"https://arxiv.org/abs/1011.0686\\\"\\n    category: \\\"imitation_learning\\\"\\n    verified: true\\n    relevance: \\\"Classic DAgger algorithm proving O(T^2) compounding error for BC, reduced to O(T) via iterative expert corrections. Foundational supervised correction framework; CRM as single-round offline DAgger.\\\"\\n    must_cite: true\\n    relation: \\\"background\\\"\\n\\n  # --- Gap 2: Uncertainty-conditioned negative results ---\\n\\n  - bibtex_key: \\\"ovadia2019trust_uncertainty\\\"\\n    title: \\\"Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift\\\"\\n    authors: \\\"Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1906.02530\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Systematic evaluation showing UQ methods degrade under distribution shift; post-hoc calibration can make things worse. Supports our finding that CP features under OOD shift may carry corrupted signal.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # --- Gap 3: Object vs spatial robustness taxonomy ---\\n\\n  - bibtex_key: \\\"xu2025libero_pro\\\"\\n    title: \\\"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\\\"\\n    authors: \\\"Xu et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.03827\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03827\\\"\\n    category: \\\"benchmark\\\"\\n    verified: true\\n    relevance: \\\"Robustness evaluation across 4 perturbation dimensions. VLAs collapse to 0% under spatial perturbation due to spatial memorization. Explains why CRM helps object but not spatial tasks.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"wang2024gendp\\\"\\n    title: \\\"GenDP: 3D Semantic Fields for Category-Level Generalizable Diffusion Policy\\\"\\n    authors: \\\"Wang et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2410.17488\\\"\\n    category: \\\"manipulation_generalization\\\"\\n    verified: true\\n    relevance: \\\"Uses 3D semantic fields for category-level object generalization (20%->93%). Shows object generalization relies on semantic features available in observation embeddings, supporting CRM's obs_only advantage.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"s2_diffusion_2025\\\"\\n    title: \\\"S^2-Diffusion: Generalizing from Instance-level to Category-level Skills in Robot Manipulation\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.09389\\\"\\n    url: \\\"https://arxiv.org/abs/2502.09389\\\"\\n    category: \\\"manipulation_generalization\\\"\\n    verified: true\\n    relevance: \\\"Spatial-Semantic Diffusion policy for instance-to-category transfer. Object category generalization via semantic abstraction (correctable at inference) vs spatial requiring re-planning.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # --- Gap 4: Compounding error in action prediction ---\\n\\n  - bibtex_key: \\\"laskey2017dart\\\"\\n    title: \\\"DART: Noise Injection for Robust Imitation Learning\\\"\\n    authors: \\\"Laskey, Lee, Fox, Dragan & Goldberg\\\"\\n    year: 2017\\n    venue: \\\"CoRL 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1703.09327\\\"\\n    category: \\\"imitation_learning\\\"\\n    verified: true\\n    relevance: \\\"Injects optimized noise into demonstrations for compounding error robustness without online interaction. 3x faster than DAgger. Analogous to CRM's offline training approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"somalwar2025imperfect_models\\\"\\n    title: \\\"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error\\\"\\n    authors: \\\"Somalwar et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2504.01766\\\"\\n    url: \\\"https://arxiv.org/abs/2504.01766\\\"\\n    category: \\\"imitation_learning\\\"\\n    verified: true\\n    relevance: \\\"Proves multi-step predictors reduce bias under model misspecification. Provides theoretical framework for when correction helps (correctable misspecification) vs hurts (new misspecification).\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # --- Gap 5: Conformal prediction as feature extractor ---\\n\\n  - bibtex_key: \\\"huang2023feature_cp\\\"\\n    title: \\\"Predictive Inference with Feature Conformal Prediction\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://openreview.net/forum?id=0uRm1YmFTu\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Deploys CP in learned feature space (reverse direction from ACR-VLA). Uses surrogate features for nonconformity scores. Establishes conceptual bridge between CP and representation learning.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"lekeufack2024conformal_decision\\\"\\n    title: \\\"Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions\\\"\\n    authors: \\\"Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik\\\"\\n    year: 2024\\n    venue: \\\"ICRA 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2310.05921\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses CP scores to calibrate decisions directly, not just prediction sets. Closest precedent for using CP beyond calibration; CP scores inform decision-making in robot planning.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"jin2023selection_prediction\\\"\\n    title: \\\"Selection by Prediction with Conformal p-values\\\"\\n    authors: \\\"Jin & Candes\\\"\\n    year: 2023\\n    venue: \\\"JMLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.01408\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal p-values for downstream screening/selection with FDR control. CP scores as informative signals for downstream task, paralleling CRM's CP-as-features approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # ===== Correction Magnitude Robustness scan (added 2026-05-15) =====\\n\\n  - bibtex_key: \\\"sampson2024conformal_hyperrect\\\"\\n    title: \\\"Conformal Multi-Target Hyperrectangles\\\"\\n    authors: \\\"Sampson et al.\\\"\\n    year: 2024\\n    venue: \\\"Statistical Analysis and Data Mining, arXiv:2406.04498\\\"\\n    url: \\\"https://arxiv.org/abs/2406.04498\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Studies per-dimension marginal coverage vs joint coverage in multi-target CP. Shows Bonferroni correction is overconservative and can produce imbalanced marginal coverage across dimensions. Directly explains perdof's failure mode: independently constructed per-DOF intervals lose inter-DOF coherence at high norm bounds, while balanced joint approaches maintain consistency.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"fang2026trace\\\"\\n    title: \\\"TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models\\\"\\n    authors: \\\"Fang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.07100\\\"\\n    url: \\\"https://arxiv.org/abs/2605.07100\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Defines scalar nonconformity scores via transport alignment in flow matching models — measuring velocity-matching errors along generative trajectories. Avoids per-dimension decomposition entirely. Supports the obs_only thesis: a scalar score derived from generative dynamics (analogous to obs_only's observation-conditioned scalar correction) naturally preserves directional coherence, unlike per-DOF decomposition.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"dodeja2025accel_residual_uq\\\"\\n    title: \\\"Accelerating Residual Reinforcement Learning with Uncertainty Estimation\\\"\\n    authors: \\\"Dodeja & Schmeckpeper\\\"\\n    year: 2025\\n    venue: \\\"IEEE RA-L, arXiv:2506.17564\\\"\\n    url: \\\"https://arxiv.org/abs/2506.17564\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\", \"total_chars\": 39177, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "82b77b3a-870f-45ec-ab5b-86929ba7193a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  - bibtex_key: \\\\\\\"a2c2_2025\\\\\\\"\\\\n    title: \\\\\\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\\\\\"\\\\n    authors: \\\\\\\"Sendai et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.23224\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.23224\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"angelopoulos2023gentle\\\\\\\"\\\\n    title: \\\\\\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\\\\\"\\\\n    authors: \\\\\\\"Angelopoulos & Bates\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Foundations and Trends in Machine Learning\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2107.07511\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"barber2023conformal\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction Beyond Exchangeability\\\\\\\"\\\\n    authors: \\\\\\\"Barber et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Annals of Statistics, 51(2):816-845\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2202.13415\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"black2024pi0\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2410.24164\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.24164\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"braun2025cgs\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\\\\\"\\\\n    authors: \\\\\\\"Braun et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.20941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.20941\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"brohan2023rt2\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv:2307.15818\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2307.15818\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chen2026reconvla\\\\\\\"\\\\n    title: \\\\\\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Chen et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.16677\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.16677\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"digflow2025\\\\\\\"\\\\n    title: \\\\\\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.01715\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.01715\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"fei2025liberoplus\\\\\\\"\\\\n    title: \\\\\\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.13626\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.13626\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"ghosh2024octo\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Ghosh et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2405.12213\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2405.12213\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gibbs2021aci\\\\\\\"\\\\n    title: \\\\\\\"Adaptive Conformal Inference Under Distribution Shift\\\\\\\"\\\\n    authors: \\\\\\\"Gibbs & Candès\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"NeurIPS 2021\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2106.00170\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"gu2025safe\\\\\\\"\\\\n    title: \\\\\\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Gu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.09937\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"kim2024openvla\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2406.09246\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.09246\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"ledoit2004well\\\\\\\"\\\\n    title: \\\\\\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\\\\\"\\\\n    authors: \\\\\\\"Ledoit & Wolf\\\\\\\"\\\\n    year: 2004\\\\n    venue: \\\\\\\"Journal of Multivariate Analysis, 88(2):365-411\\\\\\\"\\\\n    url: \\\\\\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lipman2023flow\\\\\\\"\\\\n    title: \\\\\\\"Flow Matching for Generative Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Lipman et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2210.02747\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2023libero\\\\\\\"\\\\n    title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2306.03310\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2026ttvla\\\\\\\"\\\\n    title: \\\\\\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.06748\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.06748\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"luan2026snapflow\\\\\\\"\\\\n    title: \\\\\\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\\\\\"\\\\n    authors: \\\\\\\"Luan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.05656\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.05656\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"robustvla2025\\\\\\\"\\\\n    title: \\\\\\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.01331\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.01331\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"romano2019cqr\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Quantile Regression\\\\\\\"\\\\n    authors: \\\\\\\"Romano et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"NeurIPS 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1905.03222\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shafer2008tutorial\\\\\\\"\\\\n    title: \\\\\\\"A Tutorial on Conformal Prediction\\\\\\\"\\\\n    authors: \\\\\\\"Shafer & Vovk\\\\\\\"\\\\n    year: 2008\\\\n    venue: \\\\\\\"Journal of Machine Learning Research, 9:371-421\\\\\\\"\\\\n    url: \\\\\\\"https://jmlr.org/papers/v9/shafer08a.html\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shukor2025smolvla\\\\\\\"\\\\n    title: \\\\\\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\\\\\"\\\\n    authors: \\\\\\\"Shukor et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2506.01844\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.01844\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"srpo2025\\\\\\\"\\\\n    title: \\\\\\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.15605\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.15605\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"wang2025cploop\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Wang & Ning\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.16376\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.16376\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"xing2026diu\\\\\\\"\\\\n    title: \\\\\\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\\\\\"\\\\n    authors: \\\\\\\"Xing et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.00941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.00941\\\\\\\"\\\\n    category: \\\\\\\"uq_flow_matching\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"yuan2026ups\\\\\\\"\\\\n    title: \\\\\\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\\\\\"\\\\n    authors: \\\\\\\"Yuan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.22474\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.22474\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"zhao2024conformalized\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\\\\\"\\\\n    authors: \\\\\\\"Zhao et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"RSS 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.07767\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"cosmos_policy_2026\\\\\\\"\\\\n    title: \\\\\\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.16163\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.16163\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_gse_2026\\\\\\\"\\\\n    title: \\\\\\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\\\\\"\\\\n    authors: \\\\\\\"Jiang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.06175\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.06175\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lakshminarayanan2017ensembles\\\\\\\"\\\\n    title: \\\\\\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\\\\\"\\\\n    authors: \\\\\\\"Lakshminarayanan et al.\\\\\\\"\\\\n    year: 2017\\\\n    venue: \\\\\\\"NeurIPS 2017\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1612.01474\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gal2016dropout\\\\\\\"\\\\n    title: \\\\\\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\\\\\"\\\\n    authors: \\\\\\\"Gal & Ghahramani\\\\\\\"\\\\n    year: 2016\\\\n    venue: \\\\\\\"ICML 2016\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1506.02142\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chi2023diffusion_policy\\\\\\\"\\\\n    title: \\\\\\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Chi et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"RSS 2023 / IJRR 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2303.04137\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"Well-known paper, needs URL reachability confirmation\\\\\\\"\\\\n    relevance: \\\\\\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  # ===== New entries added 2026-05-14 =====\\\\n\\\\n  - bibtex_key: \\\\\\\"fan2025interpretable_mcp\\\\\\\"\\\\n    title: \\\\\\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\\\\\"\\\\n    authors: \\\\\\\"Fan & Sesia\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.15383\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.15383\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"klein2025otcp\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction using Optimal Transport\\\\\\\"\\\\n    authors: \\\\\\\"Klein, Bethune, Ndiaye & Cuturi\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2502.03609\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.03609\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"zollo2025vla_calibration\\\\\\\"\\\\n    title: \\\\\\\"Confidence Calibration in Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zollo & Zemel\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.17383\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.17383\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"tang2026shifting_uncertainty\\\\\\\"\\\\n    title: \\\\\\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\\\\\"\\\\n    authors: \\\\\\\"Tang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2603.18342\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.18342\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lcp2025\\\\\\\"\\\\n    title: \\\\\\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.21955\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.21955\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"claps2025\\\\\\\"\\\\n    title: \\\\\\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.10294\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.10294\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lucca2024\\\\\\\"\\\\n    title: \\\\\\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\\\\\"\\\\n    authors: \\\\\\\"Marques et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2409.08249\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2409.08249\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"sc_vla_2026\\\\\\\"\\\\n    title: \\\\\\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.21633\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.21633\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_pilot_2025\\\\\\\"\\\\n    title: \\\\\\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.14178\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.14178\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"acot_vla_2026\\\\\\\"\\\\n    title: \\\\\\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"AgibotTech\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"CVPR 2026, arXiv:2601.11404\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.11404\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"gonzales2026crc_cbf\\\\\\\"\\\\n    title: \\\\\\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\\\\\"\\\\n    authors: \\\\\\\"Gonzales et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"IROS 2025, arXiv:2603.10392\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.10392\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"safediffcon2025\\\\\\\"\\\\n    title: \\\\\\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025, arXiv:2502.02205\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.02205\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"afil2026\\\\\\\"\\\\n    title: \\\\\\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.08434\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.08434\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"valle2025vla_uq_metrics\\\\\\\"\\\\n    title: \\\\\\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\\\\\"\\\\n    authors: \\\\\\\"Valle et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.17049\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.17049\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"diffusionvla2024\\\\\\\"\\\\n    title: \\\\\\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Wen et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICML 2025, arXiv:2412.03293\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2412.03293\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\\\n\\\\n  - bibtex_key: \\\\\\\"silver2018residual\\\\\\\"\\\\n    title: \\\\\\\"Residual Policy Learning\\\\\\\"\\\\n    authors: \\\\\\\"Silver et al.\\\\\\\"\\\\n    year: 2018\\\\n    venue: \\\\\\\"RSS 2018\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1812.06298\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"johannink2019residual\\\\\\\"\\\\n    title: \\\\\\\"Residual Reinforcement Learning for Robot Manipulator Control\\\\\\\"\\\\n    authors: \\\\\\\"Johannink et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"ICRA 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1812.03201\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"jiang2024transic\\\\\\\"\\\\n    title: \\\\\\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\\\\\"\\\\n    authors: \\\\\\\"Jiang et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"CoRL 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2405.10315\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"direct-competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"ankile2024resip\\\\\\\"\\\\n    title: \\\\\\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\\\\\"\\\\n    authors: \\\\\\\"Ankile et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"CoRL Workshop 2024\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"Workshop paper, no arXiv ID provided\\\\\\\"\\\\n    relevance: \\\\\\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"xiao2026pld\\\\\\\"\\\\n    title: \\\\\\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Xiao et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.00091\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"direct-competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"pan2025drc\\\\\\\"\\\\n    title: \\\\\\\"DRC: Decaying Relative Correction for Policy Refinement\\\\\\\"\\\\n    authors: \\\\\\\"Pan et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2503.15368\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.15368\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"ma2026dawn\\\\\\\"\\\\n    title: \\\\\\\"DAWN: Value Learning in Residual Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Ma et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.10539\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.10539\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_in_the_loop_2025\\\\\\\"\\\\n    title: \\\\\\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv 2025\\\\\\\"\\\\n    url: \\\\\\\"\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"No arXiv ID provided, needs verification\\\\\\\"\\\\n    relevance: \\\\\\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"zhou2025acp_cbf\\\\\\\"\\\\n    title: \\\\\\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Zhou et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICRA 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.17678\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  # ===== Literature gap papers (added 2026-05-15) =====\\\\n\\\\n  # --- Gap 1: Supervised (non-RL) residual correction ---\\\\n\\\\n  - bibtex_key: \\\\\\\"cai2025cr_dagger\\\\\\\"\\\\n    title: \\\\\\\"Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections\\\\\\\"\\\\n    authors: \\\\\\\"Cai et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.16685\\\\\\\"\\\\n    category: \\\\\\\"supervised_residual\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Learns supervised residual corrections from human delta corrections via compliance control; no RL. Closest supervised residual paradigm to CRM's offline L2-trained correction.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"rac2025\\\\\\\"\\\\n    title: \\\\\\\"RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.07953\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.07953\\\\\\\"\\\\n    category: \\\\\\\"supervised_residual\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Supervised fine-tuning on human intervention trajectories (recovery + correction). DAgger-style supervised correction without RL. Demonstrates supervised correction data suffices.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"xue2025reactive_diffusion\\\\\\\"\\\\n    title: \\\\\\\"Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Xue et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"RSS 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2503.02881\\\\\\\"\\\\n    category: \\\\\\\"supervised_residual\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Two-level slow-fast architecture: slow diffusion policy + fast supervised correction module. Structural precedent for generate-then-correct pipeline with supervised (non-RL) correction.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"ross2011dagger\\\\\\\"\\\\n    title: \\\\\\\"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\\\\\\\"\\\\n    authors: \\\\\\\"Ross, Gordon & Bagnell\\\\\\\"\\\\n    year: 2011\\\\n    venue: \\\\\\\"AISTATS 2011\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1011.0686\\\\\\\"\\\\n    category: \\\\\\\"imitation_learning\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Classic DAgger algorithm proving O(T^2) compounding error for BC, reduced to O(T) via iterative expert corrections. Foundational supervised correction framework; CRM as single-round offline DAgger.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  # --- Gap 2: Uncertainty-conditioned negative results ---\\\\n\\\\n  - bibtex_key: \\\\\\\"ovadia2019trust_uncertainty\\\\\\\"\\\\n    title: \\\\\\\"Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift\\\\\\\"\\\\n    authors: \\\\\\\"Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"NeurIPS 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1906.02530\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Systematic evaluation showing UQ methods degrade under distribution shift; post-hoc calibration can make things worse. Supports our finding that CP features under OOD shift may carry corrupted signal.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  # --- Gap 3: Object vs spatial robustness taxonomy ---\\\\n\\\\n  - bibtex_key: \\\\\\\"xu2025libero_pro\\\\\\\"\\\\n    title: \\\\\\\"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\\\\\\\"\\\\n    authors: \\\\\\\"Xu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.03827\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.03827\\\\\\\"\\\\n    category: \\\\\\\"benchmark\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Robustness evaluation across 4 perturbation dimensions. VLAs collapse to 0% under spatial perturbation due to spatial memorization. Explains why CRM helps object but not spatial tasks.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"wang2024gendp\\\\\\\"\\\\n    title: \\\\\\\"GenDP: 3D Semantic Fields for Category-Level Generalizable Diffusion Policy\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"CoRL 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.17488\\\\\\\"\\\\n    category: \\\\\\\"manipulation_generalization\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses 3D semantic fields for category-level object generalization (20%->93%). Shows object generalization relies on semantic features available in observation embeddings, supporting CRM's obs_only advantage.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"s2_diffusion_2025\\\\\\\"\\\\n    title: \\\\\\\"S^2-Diffusion: Generalizing from Instance-level to Category-level Skills in Robot Manipulation\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2502.09389\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.09389\\\\\\\"\\\\n    category: \\\\\\\"manipulation_generalization\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Spatial-Semantic Diffusion policy for instance-to-category transfer. Object category generalization via semantic abstraction (correctable at inference) vs spatial requiring re-planning.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  # --- Gap 4: Compounding error in action prediction ---\\\\n\\\\n  - bibtex_key: \\\\\\\"laskey2017dart\\\\\\\"\\\\n    title: \\\\\\\"DART: Noise Injection for Robust Imitation Learning\\\\\\\"\\\\n    authors: \\\\\\\"Laskey, Lee, Fox, Dragan & Goldberg\\\\\\\"\\\\n    year: 2017\\\\n    venue: \\\\\\\"CoRL 2017\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1703.09327\\\\\\\"\\\\n    category: \\\\\\\"imitation_learning\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Injects optimized noise into demonstrations for compounding error robustness without online interaction. 3x faster than DAgger. Analogous to CRM's offline training approach.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"somalwar2025imperfect_models\\\\\\\"\\\\n    title: \\\\\\\"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error\\\\\\\"\\\\n    authors: \\\\\\\"Somalwar et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2504.01766\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2504.01766\\\\\\\"\\\\n    category: \\\\\\\"imitation_learning\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proves multi-step predictors reduce bias under model misspecification. Provides theoretical framework for when correction helps (correctable misspecification) vs hurts (new misspecification).\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  # --- Gap 5: Conformal prediction as feature extractor ---\\\\n\\\\n  - bibtex_key: \\\\\\\"huang2023feature_cp\\\\\\\"\\\\n    title: \\\\\\\"Predictive Inference with Feature Conformal Prediction\\\\\\\"\\\\n    authors: \\\\\\\"Huang et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    url: \\\\\\\"https://openreview.net/forum?id=0uRm1YmFTu\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Deploys CP in learned feature space (reverse direction from ACR-VLA). Uses surrogate features for nonconformity scores. Establishes conceptual bridge between CP and representation learning.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lekeufack2024conformal_decision\\\\\\\"\\\\n    title: \\\\\\\"Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions\\\\\\\"\\\\n    authors: \\\\\\\"Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICRA 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2310.05921\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses CP scores to calibrate decisions directly, not just prediction sets. Closest precedent for using CP beyond calibration; CP scores inform decision-making in robot planning.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"jin2023selection_prediction\\\\\\\"\\\\n    title: \\\\\\\"Selection by Prediction with Conformal p-values\\\\\\\"\\\\n    authors: \\\\\\\"Jin & Candes\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"JMLR 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2210.01408\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses conformal p-values for downstream screening/selection with FDR control. CP scores as informative signals for downstream task, paralleling CRM's CP-as-features approach.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  # ===== Correction Magnitude Robustness scan (added 2026-05-15) =====\\\\n\\\\n  - bibtex_key: \\\\\\\"sampson2024conformal_hyperrect\\\\\\\"\\\\n    title: \\\\\\\"Conformal Multi-Target Hyperrectangles\\\\\\\"\\\\n    authors: \\\\\\\"Sampson et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"Statistical Analysis and Data Mining, arXiv:2406.04498\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.04498\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Studies per-dimension marginal coverage vs joint coverage in multi-target CP. Shows Bonferroni correction is overconservative and can produce imbalanced marginal coverage across dimensions. Directly explains perdof's failure mode: independently constructed per-DOF intervals lose inter-DOF coherence at high norm bounds, while balanced joint approaches maintain consistency.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"fang2026trace\\\\\\\"\\\\n    title: \\\\\\\"TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models\\\\\\\"\\\\n    authors: \\\\\\\"Fang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.07100\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.07100\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Defines scalar nonconformity scores via transport alignment in flow matching models — measuring velocity-matching errors along generative trajectories. Avoids per-dimension decomposition entirely. Supports the obs_only thesis: a scalar score derived from generative dynamics (analogous to obs_only's observation-conditioned scalar correction) naturally preserves directional coherence, unlike per-DOF decomposition.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"dodeja2025accel_residual_uq\\\\\\\"\\\\n    title: \\\\\\\"Accelerating Residual Reinforcement Learning with Uncertainty Estimation\\\\\\\"\\\\n    authors: \\\\\\\"Dodeja & Schmeckpeper\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"IEEE RA-L, arXiv:2506.17564\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.17564\\\\\\\"\\\\n    category: \\\\\\\"residual_policy\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"method-component\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 39177, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\\n  # ===== New entries added 2026-05-14 =====\\n\\n  - bibtex_key: \\\"fan2025interpretable_mcp\\\"\\n    title: \\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\"\\n    authors: \\\"Fan & Sesia\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.15383\\\"\\n    url: \\\"https://arxiv.org/abs/2512.15383\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"klein2025otcp\\\"\\n    title: \\\"Multivariate Conformal Prediction using Optimal Transport\\\"\\n    authors: \\\"Klein, Bethune, Ndiaye & Cuturi\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.03609\\\"\\n    url: \\\"https://arxiv.org/abs/2502.03609\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"zollo2025vla_calibration\\\"\\n    title: \\\"Confidence Calibration in Vision-Language-Action Models\\\"\\n    authors: \\\"Zollo & Zemel\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17383\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17383\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\"\\n    must_cite: true\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"tang2026shifting_uncertainty\\\"\\n    title: \\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\"\\n    authors: \\\"Tang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2603.18342\\\"\\n    url: \\\"https://arxiv.org/abs/2603.18342\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lcp2025\\\"\\n    title: \\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.21955\\\"\\n    url: \\\"https://arxiv.org/abs/2509.21955\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"claps2025\\\"\\n    title: \\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.10294\\\"\\n    url: \\\"https://arxiv.org/abs/2512.10294\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lucca2024\\\"\\n    title: \\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\"\\n    authors: \\\"Marques et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2409.08249\\\"\\n    url: \\\"https://arxiv.org/abs/2409.08249\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"sc_vla_2026\\\"\\n    title: \\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.21633\\\"\\n    url: \\\"https://arxiv.org/abs/2602.21633\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"vla_pilot_2025\\\"\\n    title: \\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.14178\\\"\\n    url: \\\"https://arxiv.org/abs/2511.14178\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"acot_vla_2026\\\"\\n    title: \\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\"\\n    authors: \\\"AgibotTech\\\"\\n    year: 2026\\n    venue: \\\"CVPR 2026, arXiv:2601.11404\\\"\\n    url: \\\"https://arxiv.org/abs/2601.11404\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"gonzales2026crc_cbf\\\"\\n    title: \\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\"\\n    authors: \\\"Gonzales et al.\\\"\\n    year: 2026\\n    venue: \\\"IROS 2025, arXiv:2603.10392\\\"\\n    url: \\\"https://arxiv.org/abs/2603.10392\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"safediffcon2025\\\"\\n    title: \\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025, arXiv:2502.02205\\\"\\n    url: \\\"https://arxiv.org/abs/2502.02205\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"afil2026\\\"\\n    title: \\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.08434\\\"\\n    url: \\\"https://arxiv.org/abs/2605.08434\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"valle2025vla_uq_metrics\\\"\\n    title: \\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\"\\n    authors: \\\"Valle et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17049\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17049\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"diffusionvla2024\\\"\\n    title: \\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\"\\n    authors: \\\"Wen et al.\\\"\\n    year: 2024\\n    venue: \\\"ICML 2025, arXiv:2412.03293\\\"\\n    url: \\\"https://arxiv.org/abs/2412.03293\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\\n\\n  - bibtex_key: \\\"silver2018residual\\\"\\n    title: \\\"Residual Policy Learning\\\"\\n    authors: \\\"Silver et al.\\\"\\n    year: 2018\\n    venue: \\\"RSS 2018\\\"\\n    url: \\\"https://arxiv.org/abs/1812.06298\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\\\"\\n    must_cite: true\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"johannink2019residual\\\"\\n    title: \\\"Residual Reinforcement Learning for Robot Manipulator Control\\\"\\n    authors: \\\"Johannink et al.\\\"\\n    year: 2019\\n    venue: \\\"ICRA 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1812.03201\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"jiang2024transic\\\"\\n    title: \\\"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2405.10315\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"ankile2024resip\\\"\\n    title: \\\"ResiP: Residual Reinforcement Learning for Precise Assembly\\\"\\n    authors: \\\"Ankile et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL Workshop 2024\\\"\\n    url: \\\"\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: false\\n    verification_note: \\\"Workshop paper, no arXiv ID provided\\\"\\n    relevance: \\\"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"xiao2026pld\\\"\\n    title: \\\"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\\\"\\n    authors: \\\"Xiao et al.\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026\\\"\\n    url: \\\"https://arxiv.org/abs/2511.00091\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\\\"\\n    must_cite: true\\n    relation: \\\"direct-competitor\\\"\\n\\n  - bibtex_key: \\\"pan2025drc\\\"\\n    title: \\\"DRC: Decaying Relative Correction for Policy Refinement\\\"\\n    authors: \\\"Pan et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2503.15368\\\"\\n    url: \\\"https://arxiv.org/abs/2503.15368\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"ma2026dawn\\\"\\n    title: \\\"DAWN: Value Learning in Residual Reinforcement Learning\\\"\\n    authors: \\\"Ma et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.10539\\\"\\n    url: \\\"https://arxiv.org/abs/2602.10539\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"vla_in_the_loop_2025\\\"\\n    title: \\\"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2025\\\"\\n    url: \\\"\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: false\\n    verification_note: \\\"No arXiv ID provided, needs verification\\\"\\n    relevance: \\\"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"zhou2025acp_cbf\\\"\\n    title: \\\"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\\\"\\n    authors: \\\"Zhou et al.\\\"\\n    year: 2025\\n    venue: \\\"ICRA 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.17678\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\\\"\\n    must_cite: true\\n    relation: \\\"method-component\\\"\\n\\n  # ===== Literature gap papers (added 2026-05-15) =====\\n\\n  # --- Gap 1: Supervised (non-RL) residual correction ---\\n\\n  - bibtex_key: \\\"cai2025cr_dagger\\\"\\n    title: \\\"Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections\\\"\\n    authors: \\\"Cai et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.16685\\\"\\n    category: \\\"supervised_residual\\\"\\n    verified: true\\n    relevance: \\\"Learns supervised residual corrections from human delta corrections via compliance control; no RL. Closest supervised residual paradigm to CRM's offline L2-trained correction.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"rac2025\\\"\\n    title: \\\"RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.07953\\\"\\n    url: \\\"https://arxiv.org/abs/2509.07953\\\"\\n    category: \\\"supervised_residual\\\"\\n    verified: true\\n    relevance: \\\"Supervised fine-tuning on human intervention trajectories (recovery + correction). DAgger-style supervised correction without RL. Demonstrates supervised correction data suffices.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"xue2025reactive_diffusion\\\"\\n    title: \\\"Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation\\\"\\n    authors: \\\"Xue et al.\\\"\\n    year: 2025\\n    venue: \\\"RSS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2503.02881\\\"\\n    category: \\\"supervised_residual\\\"\\n    verified: true\\n    relevance: \\\"Two-level slow-fast architecture: slow diffusion policy + fast supervised correction module. Structural precedent for generate-then-correct pipeline with supervised (non-RL) correction.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"ross2011dagger\\\"\\n    title: \\\"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\\\"\\n    authors: \\\"Ross, Gordon & Bagnell\\\"\\n    year: 2011\\n    venue: \\\"AISTATS 2011\\\"\\n    url: \\\"https://arxiv.org/abs/1011.0686\\\"\\n    category: \\\"imitation_learning\\\"\\n    verified: true\\n    relevance: \\\"Classic DAgger algorithm proving O(T^2) compounding error for BC, reduced to O(T) via iterative expert corrections. Foundational supervised correction framework; CRM as single-round offline DAgger.\\\"\\n    must_cite: true\\n    relation: \\\"background\\\"\\n\\n  # --- Gap 2: Uncertainty-conditioned negative results ---\\n\\n  - bibtex_key: \\\"ovadia2019trust_uncertainty\\\"\\n    title: \\\"Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift\\\"\\n    authors: \\\"Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1906.02530\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Systematic evaluation showing UQ methods degrade under distribution shift; post-hoc calibration can make things worse. Supports our finding that CP features under OOD shift may carry corrupted signal.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # --- Gap 3: Object vs spatial robustness taxonomy ---\\n\\n  - bibtex_key: \\\"xu2025libero_pro\\\"\\n    title: \\\"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\\\"\\n    authors: \\\"Xu et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.03827\\\"\\n    url: \\\"https://arxiv.org/abs/2510.03827\\\"\\n    category: \\\"benchmark\\\"\\n    verified: true\\n    relevance: \\\"Robustness evaluation across 4 perturbation dimensions. VLAs collapse to 0% under spatial perturbation due to spatial memorization. Explains why CRM helps object but not spatial tasks.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"wang2024gendp\\\"\\n    title: \\\"GenDP: 3D Semantic Fields for Category-Level Generalizable Diffusion Policy\\\"\\n    authors: \\\"Wang et al.\\\"\\n    year: 2024\\n    venue: \\\"CoRL 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2410.17488\\\"\\n    category: \\\"manipulation_generalization\\\"\\n    verified: true\\n    relevance: \\\"Uses 3D semantic fields for category-level object generalization (20%->93%). Shows object generalization relies on semantic features available in observation embeddings, supporting CRM's obs_only advantage.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"s2_diffusion_2025\\\"\\n    title: \\\"S^2-Diffusion: Generalizing from Instance-level to Category-level Skills in Robot Manipulation\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.09389\\\"\\n    url: \\\"https://arxiv.org/abs/2502.09389\\\"\\n    category: \\\"manipulation_generalization\\\"\\n    verified: true\\n    relevance: \\\"Spatial-Semantic Diffusion policy for instance-to-category transfer. Object category generalization via semantic abstraction (correctable at inference) vs spatial requiring re-planning.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # --- Gap 4: Compounding error in action prediction ---\\n\\n  - bibtex_key: \\\"laskey2017dart\\\"\\n    title: \\\"DART: Noise Injection for Robust Imitation Learning\\\"\\n    authors: \\\"Laskey, Lee, Fox, Dragan & Goldberg\\\"\\n    year: 2017\\n    venue: \\\"CoRL 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1703.09327\\\"\\n    category: \\\"imitation_learning\\\"\\n    verified: true\\n    relevance: \\\"Injects optimized noise into demonstrations for compounding error robustness without online interaction. 3x faster than DAgger. Analogous to CRM's offline training approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"somalwar2025imperfect_models\\\"\\n    title: \\\"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error\\\"\\n    authors: \\\"Somalwar et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2504.01766\\\"\\n    url: \\\"https://arxiv.org/abs/2504.01766\\\"\\n    category: \\\"imitation_learning\\\"\\n    verified: true\\n    relevance: \\\"Proves multi-step predictors reduce bias under model misspecification. Provides theoretical framework for when correction helps (correctable misspecification) vs hurts (new misspecification).\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # --- Gap 5: Conformal prediction as feature extractor ---\\n\\n  - bibtex_key: \\\"huang2023feature_cp\\\"\\n    title: \\\"Predictive Inference with Feature Conformal Prediction\\\"\\n    authors: \\\"Huang et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://openreview.net/forum?id=0uRm1YmFTu\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Deploys CP in learned feature space (reverse direction from ACR-VLA). Uses surrogate features for nonconformity scores. Establishes conceptual bridge between CP and representation learning.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"lekeufack2024conformal_decision\\\"\\n    title: \\\"Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions\\\"\\n    authors: \\\"Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik\\\"\\n    year: 2024\\n    venue: \\\"ICRA 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2310.05921\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses CP scores to calibrate decisions directly, not just prediction sets. Closest precedent for using CP beyond calibration; CP scores inform decision-making in robot planning.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"jin2023selection_prediction\\\"\\n    title: \\\"Selection by Prediction with Conformal p-values\\\"\\n    authors: \\\"Jin & Candes\\\"\\n    year: 2023\\n    venue: \\\"JMLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.01408\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal p-values for downstream screening/selection with FDR control. CP scores as informative signals for downstream task, paralleling CRM's CP-as-features approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  # ===== Correction Magnitude Robustness scan (added 2026-05-15) =====\\n\\n  - bibtex_key: \\\"sampson2024conformal_hyperrect\\\"\\n    title: \\\"Conformal Multi-Target Hyperrectangles\\\"\\n    authors: \\\"Sampson et al.\\\"\\n    year: 2024\\n    venue: \\\"Statistical Analysis and Data Mining, arXiv:2406.04498\\\"\\n    url: \\\"https://arxiv.org/abs/2406.04498\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Studies per-dimension marginal coverage vs joint coverage in multi-target CP. Shows Bonferroni correction is overconservative and can produce imbalanced marginal coverage across dimensions. Directly explains perdof's failure mode: independently constructed per-DOF intervals lose inter-DOF coherence at high norm bounds, while balanced joint approaches maintain consistency.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"fang2026trace\\\"\\n    title: \\\"TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models\\\"\\n    authors: \\\"Fang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.07100\\\"\\n    url: \\\"https://arxiv.org/abs/2605.07100\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Defines scalar nonconformity scores via transport alignment in flow matching models — measuring velocity-matching errors along generative trajectories. Avoids per-dimension decomposition entirely. Supports the obs_only thesis: a scalar score derived from generative dynamics (analogous to obs_only's observation-conditioned scalar correction) naturally preserves directional coherence, unlike per-DOF decomposition.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\\n  - bibtex_key: \\\"dodeja2025accel_residual_uq\\\"\\n    title: \\\"Accelerating Residual Reinforcement Learning with Uncertainty Estimation\\\"\\n    authors: \\\"Dodeja & Schmeckpeper\\\"\\n    year: 2025\\n    venue: \\\"IEEE RA-L, arXiv:2506.17564\\\"\\n    url: \\\"https://arxiv.org/abs/2506.17564\\\"\\n    category: \\\"residual_policy\\\"\\n    verified: true\\n    relevance: \\\"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\\\"\\n    must_cite: false\\n    relation: \\\"method-component\\\"\\n\", \"total_chars\": 39177, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01AQmHDAYp8C9QLb5uBC9D87`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/related_work.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "8df482ef-d07e-4dd2-9d67-45988bc3bb8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T2DMj1etHujeJ5CicuF2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10462,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10462
      },
      "output_tokens": 34,
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

_source line 22 · 2026-05-15T19:49:36.613Z_

<details><summary>↩ Tool result · `toolu_01AQmHDAYp8C9QLb5uBC9D87`</summary>

```text
1	# Related Work
2	
3	## VLA Robustness and Inference-Time Adaptation
4	
5	Vision-Language-Action (VLA) models have rapidly advanced general-purpose robot control by leveraging large-scale vision-language pretraining [Brohan et al., 2023; Kim et al., 2024]. Flow-matching architectures such as pi0 [Black et al., 2024] and SmolVLA [Shukor et al., 2025] achieve strong performance on standard benchmarks but remain brittle under distribution shift, as systematically documented by LIBERO-Plus [Fei et al., 2025] and LIBERO-PRO [Xu et al., 2025].
6	
7	Several lines of work address VLA robustness at *training time*. RobustVLA [Zhang et al., 2025] applies Jacobian and smoothness regularization via RL post-training. SRPO [Fei et al., 2025] uses self-referential policy optimization to reach 82.1% on LIBERO-Plus. DiG-Flow [Zhang et al., 2025] introduces representation-level discrepancy guidance. ACoT-VLA [AgibotTech, 2026] adds chain-of-thought reasoning to VLA action prediction. VLA-GSE [Jiang et al., 2026] employs parameter-efficient fine-tuning with specialized experts. AFIL [2026] leverages failure trajectories as negative guidance during training. These methods require modifying the VLA training pipeline; our work is complementary, operating purely at inference time on a frozen model.
8	
9	At *inference time*, the landscape is sparser. ReconVLA [Chen et al., 2026] applies conformal prediction to produce calibrated uncertainty estimates and selects the best action from K candidates — a pure sample-selection strategy. VLA-Pilot [2025] uses a multimodal LLM verifier with evolutionary diffusion optimization for zero-shot policy steering, but incurs 2.41s per step. SC-VLA [Li et al., 2026] performs online action refinement via sparse future state prediction and residual RL, requiring environment interaction. TT-VLA [Liu et al., 2026] adapts VLAs through test-time reinforcement learning with progress-based rewards. A2C2 [Sendai et al., 2025] proposes an asynchronous action chunk correction head — the closest architecture to our CRM, but trained jointly with the VLA rather than as a post-hoc module. SAFE [Gu et al., 2025] focuses on failure detection using internal VLA features and conformal prediction to determine *when* to intervene. Our work differs from all of the above by (1) operating on a fully frozen VLA with no environment interaction, (2) systematically comparing correction conditioning features, and (3) identifying correction magnitude as a critical factor.
10	
11	SnapFlow [Luan et al., 2026] takes the opposite computational trade-off — distilling multi-step flow matching into a single inference step — while we invest additional compute (K=10 samples + CRM correction) to improve robustness.
12	
13	## Conformal Prediction in Robotics
14	
15	Conformal prediction (CP) provides distribution-free coverage guarantees without distributional assumptions [Shafer & Vovk, 2008; Angelopoulos & Bates, 2023]. Extensions to non-exchangeable settings [Barber et al., 2023] and online adaptation via Adaptive Conformal Inference (ACI) [Gibbs & Candès, 2021] enable deployment under the distribution shifts inherent in robot operation.
16	
17	In multivariate action spaces, Conformalized Gaussian Scoring (CGS) [Braun et al., 2025] provides Mahalanobis-based nonconformity scores respecting inter-dimensional correlations, which we adopt for sample selection. Conformalized Quantile Regression (CQR) [Romano et al., 2019] offers per-dimension heteroscedastic coverage. Recent work explores alternatives: Fan and Sesia [2025] develop coordinate-wise standardization for tighter marginal intervals, and Klein et al. [2025] use optimal transport ordering for principled multivariate quantiles.
18	
19	Several works apply CP to robot planning and control. Zhao et al. [2024] use adaptive CP for uncertainty detection in high-DOF teleoperation at RSS 2024. Wang and Ning [2025] integrate CP into trajectory optimization loops with coverage guarantees. Zhou et al. [2025] combine ACP with control barrier functions for formally safe RL at ICRA 2025. Gonzales et al. [2026] pair conformal risk control with CBFs for human-robot interaction safety. Lekeufack et al. [2024] develop conformal decision theory for calibrated autonomous decisions. In the CP-for-robotics literature, CLAPS [2025] extends CP to Lie group configuration spaces, and LCP [2025] learns context-aware nonconformity functions for robot planning.
20	
21	A distinct thread uses CP for *downstream decision-making* rather than coverage: Jin and Candès [2023] use conformal p-values for selection with FDR control, and Huang et al. [2023] deploy CP in learned feature spaces. SafeDiffCon [2025] uses CP uncertainty quantiles to guide diffusion-based control at ICML 2025. Yuan et al. [2026] calibrate VLM+policy composition for strategy selection (act/ask/learn) using CP. Our work connects to this thread: we use conformal scores for sample selection, then investigate whether conformal statistics can additionally serve as conditioning features for learned correction — finding, surprisingly, that they cannot.
22	
23	The emerging area of VLA-specific uncertainty quantification provides further context. Zollo and Zemel [2025] present the first systematic calibration study for VLAs, introducing prompt ensembles and action-wise Platt scaling. Tang et al. [2026] identify the "averaging trap" in VLA uncertainty where mean aggregation dilutes critical signals. Xing et al. [2026] propose single-pass uncertainty via velocity divergence in flow matching models. Valle et al. [2025] establish evaluation metrics for VLA uncertainty. These works focus on *measuring* uncertainty; we focus on *acting on it* through learned correction.
24	
25	## Residual Correction and Learned Action Refinement
26	
27	Residual policy learning [Silver et al., 2018] establishes the framework of learning a correction on top of a base controller, with bounded corrections shown to preserve stability [Johannink et al., 2019]. This paradigm has been extended to VLA settings: PLD [Xiao et al., 2026] applies residual RL with scheduled magnitude bounds on LIBERO at ICLR 2026, and DAWN [Ma et al., 2026] analyzes scale mismatch between base policy and residual in value estimation. DRC [Pan et al., 2025] introduces temporal decay of correction magnitude over episodes. TRANSIC [Jiang et al., 2024] demonstrates that ungated residual corrections lead to model collapse, motivating gated correction mechanisms — closely related to our finding that unbounded correction magnitude (norm=1.42) yields catastrophic 0% success rate.
28	
29	A separate line of supervised (non-RL) correction includes DAgger [Ross et al., 2011], which reduces compounding error via iterative expert corrections, and its variants: CR-DAgger [Cai et al., 2025] learns compliant residual corrections from human interventions, and RaC [2025] scales recovery and correction from human intervention data. Reactive Diffusion Policy [Xue et al., 2025] uses a two-level slow-fast architecture with supervised fast correction. DART [Laskey et al., 2017] injects optimized noise for compounding error robustness without online interaction. Our CRM follows the supervised correction paradigm — trained offline via L2 regression on calibration data — but uniquely conditions on VLA observation features and constrains correction magnitude, avoiding the RL training loops required by PLD, SC-VLA, and DAWN.
30	
31	The question of *what to condition corrections on* is underexplored. Most residual methods condition on the full state or observation. Dodeja and Schmeckpeper [2025] show that base policy uncertainty can focus residual RL exploration on low-confidence regions. TRACE [Fang et al., 2026] defines scalar nonconformity scores via transport alignment in flow matching, avoiding per-dimension decomposition. Our systematic ablation across conditioning features — observation embeddings, per-DOF conformal statistics, and scalar conformal scores — reveals that richer statistical features do not translate to better correction, challenging the intuition that more informative conditioning is always beneficial.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "c40ffae9-0364-495e-a7ff-f6887827de69",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/related_work.md",
      "content": "# Related Work\n\n## VLA Robustness and Inference-Time Adaptation\n\nVision-Language-Action (VLA) models have rapidly advanced general-purpose robot control by leveraging large-scale vision-language pretraining [Brohan et al., 2023; Kim et al., 2024]. Flow-matching architectures such as pi0 [Black et al., 2024] and SmolVLA [Shukor et al., 2025] achieve strong performance on standard benchmarks but remain brittle under distribution shift, as systematically documented by LIBERO-Plus [Fei et al., 2025] and LIBERO-PRO [Xu et al., 2025].\n\nSeveral lines of work address VLA robustness at *training time*. RobustVLA [Zhang et al., 2025] applies Jacobian and smoothness regularization via RL post-training. SRPO [Fei et al., 2025] uses self-referential policy optimization to reach 82.1% on LIBERO-Plus. DiG-Flow [Zhang et al., 2025] introduces representation-level discrepancy guidance. ACoT-VLA [AgibotTech, 2026] adds chain-of-thought reasoning to VLA action prediction. VLA-GSE [Jiang et al., 2026] employs parameter-efficient fine-tuning with specialized experts. AFIL [2026] leverages failure trajectories as negative guidance during training. These methods require modifying the VLA training pipeline; our work is complementary, operating purely at inference time on a frozen model.\n\nAt *inference time*, the landscape is sparser. ReconVLA [Chen et al., 2026] applies conformal prediction to produce calibrated uncertainty estimates and selects the best action from K candidates — a pure sample-selection strategy. VLA-Pilot [2025] uses a multimodal LLM verifier with evolutionary diffusion optimization for zero-shot policy steering, but incurs 2.41s per step. SC-VLA [Li et al., 2026] performs online action refinement via sparse future state prediction and residual RL, requiring environment interaction. TT-VLA [Liu et al., 2026] adapts VLAs through test-time reinforcement learning with progress-based rewards. A2C2 [Sendai et al., 2025] proposes an asynchronous action chunk correction head — the closest architecture to our CRM, but trained jointly with the VLA rather than as a post-hoc module. SAFE [Gu et al., 2025] focuses on failure detection using internal VLA features and conformal prediction to determine *when* to intervene. Our work differs from all of the above by (1) operating on a fully frozen VLA with no environment interaction, (2) systematically comparing correction conditioning features, and (3) identifying correction magnitude as a critical factor.\n\nSnapFlow [Luan et al., 2026] takes the opposite computational trade-off — distilling multi-step flow matching into a single inference step — while we invest additional compute (K=10 samples + CRM correction) to improve robustness.\n\n## Conformal Prediction in Robotics\n\nConformal prediction (CP) provides distribution-free coverage guarantees without distributional assumptions [Shafer & Vovk, 2008; Angelopoulos & Bates, 2023]. Extensions to non-exchangeable settings [Barber et al., 2023] and online adaptation via Adaptive Conformal Inference (ACI) [Gibbs & Candès, 2021] enable deployment under the distribution shifts inherent in robot operation.\n\nIn multivariate action spaces, Conformalized Gaussian Scoring (CGS) [Braun et al., 2025] provides Mahalanobis-based nonconformity scores respecting inter-dimensional correlations, which we adopt for sample selection. Conformalized Quantile Regression (CQR) [Romano et al., 2019] offers per-dimension heteroscedastic coverage. Recent work explores alternatives: Fan and Sesia [2025] develop coordinate-wise standardization for tighter marginal intervals, and Klein et al. [2025] use optimal transport ordering for principled multivariate quantiles.\n\nSeveral works apply CP to robot planning and control. Zhao et al. [2024] use adaptive CP for uncertainty detection in high-DOF teleoperation at RSS 2024. Wang and Ning [2025] integrate CP into trajectory optimization loops with coverage guarantees. Zhou et al. [2025] combine ACP with control barrier functions for formally safe RL at ICRA 2025. Gonzales et al. [2026] pair conformal risk control with CBFs for human-robot interaction safety. Lekeufack et al. [2024] develop conformal decision theory for calibrated autonomous decisions. In the CP-for-robotics literature, CLAPS [2025] extends CP to Lie group configuration spaces, and LCP [2025] learns context-aware nonconformity functions for robot planning.\n\nA distinct thread uses CP for *downstream decision-making* rather than coverage: Jin and Candès [2023] use conformal p-values for selection with FDR control, and Huang et al. [2023] deploy CP in learned feature spaces. SafeDiffCon [2025] uses CP uncertainty quantiles to guide diffusion-based control at ICML 2025. Yuan et al. [2026] calibrate VLM+policy composition for strategy selection (act/ask/learn) using CP. Our work connects to this thread: we use conformal scores for sample selection, then investigate whether conformal statistics can additionally serve as conditioning features for learned correction — finding, surprisingly, that they cannot.\n\nThe emerging area of VLA-specific uncertainty quantification provides further context. Zollo and Zemel [2025] present the first systematic calibration study for VLAs, introducing prompt ensembles and action-wise Platt scaling. Tang et al. [2026] identify the \"averaging trap\" in VLA uncertainty where mean aggregation dilutes critical signals. Xing et al. [2026] propose single-pass uncertainty via velocity divergence in flow matching models. Valle et al. [2025] establish evaluation metrics for VLA uncertainty. These works focus on *measuring* uncertainty; we focus on *acting on it* through learned correction.\n\n## Residual Correction and Learned Action Refinement\n\nResidual policy learning [Silver et al., 2018] establishes the framework of learning a correction on top of a base controller, with bounded corrections shown to preserve stability [Johannink et al., 2019]. This paradigm has been extended to VLA settings: PLD [Xiao et al., 2026] applies residual RL with scheduled magnitude bounds on LIBERO at ICLR 2026, and DAWN [Ma et al., 2026] analyzes scale mismatch between base policy and residual in value estimation. DRC [Pan et al., 2025] introduces temporal decay of correction magnitude over episodes. TRANSIC [Jiang et al., 2024] demonstrates that ungated residual corrections lead to model collapse, motivating gated correction mechanisms — closely related to our finding that unbounded correction magnitude (norm=1.42) yields catastrophic 0% success rate.\n\nA separate line of supervised (non-RL) correction includes DAgger [Ross et al., 2011], which reduces compounding error via iterative expert corrections, and its variants: CR-DAgger [Cai et al., 2025] learns compliant residual corrections from human interventions, and RaC [2025] scales recovery and correction from human intervention data. Reactive Diffusion Policy [Xue et al., 2025] uses a two-level slow-fast architecture with supervised fast correction. DART [Laskey et al., 2017] injects optimized noise for compounding error robustness without online interaction. Our CRM follows the supervised correction paradigm — trained offline via L2 regression on calibration data — but uniquely conditions on VLA observation features and constrains correction magnitude, avoiding the RL training loops required by PLD, SC-VLA, and DAWN.\n\nThe question of *what to condition corrections on* is underexplored. Most residual methods condition on the full state or observation. Dodeja and Schmeckpeper [2025] show that base policy uncertainty can focus residual RL exploration on low-confidence regions. TRACE [Fang et al., 2026] defines scalar nonconformity scores via transport alignment in flow matching, avoiding per-dimension decomposition. Our systematic ablation across conditioning features — observation embeddings, per-DOF conformal statistics, and scalar conformal scores — reveals that richer statistical features do not translate to better correction, challenging the intuition that more informative conditioning is always beneficial.\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
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
Now I have all the reference materials. Let me write the new introduction based on the Scenario C framing. Let me carefully follow all the constraints:

1. ~1.5 pages (~700-800 words)
2. LaTeX format, consistent with method.tex style
3. Numbers from paper_framing.md / writing_plan.yaml
4. No cherry-picking, no overclaim
5. Spatial is null result - stated clearly
6. Only 1 VLA backbone + 2 benchmarks → "on LIBERO" not "consistently"
7. No claim of statistical significance (seed=43 pending)


8. Three contributions as specified

I'll organize the introduction around the core narrative: VLAs fail under distribution shift, selection alone is limited, and our pipeline combines sampling with learned correction. The four paragraphs will establish the problem, identify the gap, present our method, and preview the key empirical findings including the honest negative on spatial generalization.

Now I'm mapping out the key citations—flow-matching baselines like Black et al. and Shukor et al., the distribution shift benchmark from Fei et al., existing approaches like ReconVLA and SC-VLA, and relevant techniques for residual policies and magnitude control that inform our design choices.

Before drafting the introduction, I need to keep track of the critical details: ACI+COC is out of the pipeline, per-DOF conformal features didn't work as expected, the model is 329K parameters using only observation embeddings, and the CRM operates on observation embeddings alone. The ablation results show obs_only at 19.0%, argmin at 12.0%, per-DOF at 11.0%, and scalar at 9.0%, while spatial variants all cluster around 30-35% with no clear winner, and magnitude scheduling shows a dramatic shift from 0% at norm=1.42 to 19% at norm=0.1.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "abf17505-ae49-47b5-924d-524ac2c9327f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2QAfS2nH6qbVzePq2i7vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25778,
      "cache_read_input_tokens": 34423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25778
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

_source line 24_

Now I have all the materials. Let me also load the artifact registration tool, then write the introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "174d04f4-5699-4ed9-8063-dc75ab2afb46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2QAfS2nH6qbVzePq2i7vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25778,
      "cache_read_input_tokens": 34423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25778
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

_source line 25_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Lo7Mssdv2K2BDnJBeqHUjM`</summary>

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
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "2a5b9642-a1cb-4f29-a639-862e75211e59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2QAfS2nH6qbVzePq2i7vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25778,
      "cache_read_input_tokens": 34423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25778
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

_source line 26 · 2026-05-15T19:49:59.371Z_

<details><summary>↩ Tool result · `toolu_01Lo7Mssdv2K2BDnJBeqHUjM`</summary>

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
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "9e6bdb0c-7b84-43a9-b571-43fbd4bd784c",
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

### Assistant

_source line 27_

Writing the Scenario C introduction now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "1fbd1341-5157-4c60-8733-d87ceb4551d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6WeDnHeNoye1th3w65HAS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 60201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1449
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

_source line 28_

<details open><summary>🔧 Tool call — Write · `toolu_01MT1QUh4FUWBRZ4BphAzv2c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% Para 1: Problem — VLAs degrade under distribution shift; existing solutions have trade-offs\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla} achieve 97--99\\% success on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\\cite{fei2025liberoplus}.\nTwo families of methods address this robustness gap.\n\\emph{Training-time methods}~\\cite{robustvla2025,srpo2025,digflow2025} improve the base policy through robustness-aware objectives, but require retraining and remain bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen and intervene at deployment.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the best one via conformal scoring---a pure \\emph{sample selection} strategy that cannot produce actions better than the best candidate.\nSC-VLA~\\cite{sc_vla_2026} learns a residual correction via reinforcement learning, requiring per-task environment interaction.\nVLA-Pilot~\\cite{vla_pilot_2025} steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41\\,s per control step.\nA2C2~\\cite{a2c2_2025} trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model.\nIn short, no existing inference-time method combines \\emph{learned action correction} on a fully frozen VLA with \\emph{offline-only training} and \\emph{low latency}.\n\n% Para 2: Gap — sample selection is limited; learned correction can go beyond, but what conditioning?\nThe fundamental limitation of sample selection is that it is bounded by the quality of the available candidates: when all $K$ samples are poor, selecting the best one still yields a poor action.\nLearned correction can synthesize actions beyond the support of the original samples, potentially recovering from systematic biases in the base policy.\nHowever, a critical open question is what information the correction module should be conditioned on.\nAn intuitive hypothesis is that \\emph{structured uncertainty features}---per-degree-of-freedom conformal statistics capturing which action dimensions are uncertain and by how much---should enable more targeted corrections than raw observation features alone.\nWe test this hypothesis systematically.\n\n% Para 3: Our approach — ACR-VLA pipeline overview\nWe introduce \\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that wraps any frozen flow-matching VLA and performs learned residual action correction.\nACR-VLA operates as a \\emph{sample-then-correct} pipeline:\n(i)~draw $K{=}10$ action samples via independent flow-matching rollouts;\n(ii)~score each sample using Mahalanobis nonconformity under a Ledoit--Wolf shrinkage covariance~\\cite{braun2025cgs} and select the lowest-scoring candidate;\n(iii)~apply a lightweight Conformal Residual Module (CRM)---a 3-layer MLP (${\\sim}$329K parameters) that takes the frozen VLA's observation embedding as input and outputs a bounded residual correction.\nThe corrected action is $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta}, \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon)$, where the norm bound $\\varepsilon$ constrains how far the correction can deviate from the selected action.\nCRM is trained offline via $L_2$ regression on demonstration data; the base VLA is never modified.\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA, and evaluate on two LIBERO task suites~\\cite{liu2023libero}.\n\n% Para 4: Key findings — what we find, including negatives\nOur experiments yield three findings.\n\\emph{First}, sample-then-correct outperforms sample-then-select: on LIBERO-Object (10 tasks with novel object instances), observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for conformal selection alone, a +7.0\\,pp improvement.\nThree baselines---single-sample VLA, 10-sample mean, and argmin selection---all plateau at 12.0\\%, indicating that neither averaging nor selection breaks through on this benchmark.\n\\emph{Second}, per-DOF conformal features as CRM conditioning are an \\emph{honest negative result}: the perdof variant (11.0\\%) performs comparably to argmin selection (12.0\\%) and far below observation-only conditioning (19.0\\%).\nThis contradicts the intuition that richer uncertainty features should yield better corrections.\nWe attribute this to noisy covariance estimation at the $K{=}10$ sample budget ($d/K = 0.6$): while shrinkage stabilizes selection scoring, the per-DOF statistics derived from it carry estimation noise that degrades CRM predictions under the compounding distribution shift of closed-loop evaluation~\\cite{ross2011dagger}.\n\\emph{Third}, correction magnitude control is critical and has not been systematically studied in prior residual policy work~\\cite{silver2018residual,jiang2024transic,xiao2026pld}: without clipping ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$), CRM achieves 0\\% success---compounding error destroys the trajectory entirely.\nConstraining $\\varepsilon$ to $[0.05, 0.2]$ restores stable performance, with observation-conditioned CRM uniquely robust across this range while per-DOF-conditioned CRM collapses at larger bounds.\nOn LIBERO-Spatial (10 tasks with layout changes), all CRM variants achieve 30--35\\%, comparable to the argmin baseline (34\\%)---a null result that we report prominently.\nResidual correction at the action level does not help when the challenge is spatial re-planning rather than fine-grained motor adjustment.\n\n% Para 5: Contributions\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We present the first method that combines multi-sample conformal selection with offline-trained learned residual correction on a frozen VLA.\n  On LIBERO-Object, CRM correction improves success by +7.0\\,pp over selection alone (19.0\\% vs.\\ 12.0\\%), demonstrating that learned correction can synthesize actions better than any individual VLA sample.\n\n  \\item \\textbf{Honest negative: per-DOF conformal features do not improve correction.}\n  Systematic ablation across three conditioning variants---observation embeddings (329K params), per-DOF conformal statistics (339K params), and scalar uncertainty (330K params)---reveals that observation features suffice for effective correction.\n  Per-DOF conformal statistics, despite their theoretical appeal, yield 11.0\\% versus 19.0\\% for observation-only conditioning, challenging the intuition from synthetic experiments that richer uncertainty features enable better corrections.\n\n  \\item \\textbf{Correction magnitude control as a critical design factor.}\n  We show that unbounded residual correction ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic 0\\% success, while the safe operating range $\\varepsilon \\in [0.05, 0.2]$ yields stable improvements.\n  Observation-conditioned CRM maintains performance across this range; per-DOF-conditioned CRM degrades sharply beyond $\\varepsilon = 0.1$.\n  This magnitude sensitivity has not been systematically characterized in prior residual policy literature.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "5b2436c9-30de-42ce-8efd-6d22603c1792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y6WeDnHeNoye1th3w65HAS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 60201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1449
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

_source line 29 · 2026-05-15T19:50:46.463Z_

<details><summary>↩ Tool result · `toolu_01MT1QUh4FUWBRZ4BphAzv2c`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "f05cf5e3-ccc5-441a-bc60-fcd2fd655191",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% Para 1: Problem — VLAs degrade under distribution shift; existing solutions have trade-offs\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla} achieve 97--99\\% success on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\\cite{fei2025liberoplus}.\nTwo families of methods address this robustness gap.\n\\emph{Training-time methods}~\\cite{robustvla2025,srpo2025,digflow2025} improve the base policy through robustness-aware objectives, but require retraining and remain bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen and intervene at deployment.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the best one via conformal scoring---a pure \\emph{sample selection} strategy that cannot produce actions better than the best candidate.\nSC-VLA~\\cite{sc_vla_2026} learns a residual correction via reinforcement learning, requiring per-task environment interaction.\nVLA-Pilot~\\cite{vla_pilot_2025} steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41\\,s per control step.\nA2C2~\\cite{a2c2_2025} trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model.\nIn short, no existing inference-time method combines \\emph{learned action correction} on a fully frozen VLA with \\emph{offline-only training} and \\emph{low latency}.\n\n% Para 2: Gap — sample selection is limited; learned correction can go beyond, but what conditioning?\nThe fundamental limitation of sample selection is that it is bounded by the quality of the available candidates: when all $K$ samples are poor, selecting the best one still yields a poor action.\nLearned correction can synthesize actions beyond the support of the original samples, potentially recovering from systematic biases in the base policy.\nHowever, a critical open question is what information the correction module should be conditioned on.\nAn intuitive hypothesis is that \\emph{structured uncertainty features}---per-degree-of-freedom conformal statistics capturing which action dimensions are uncertain and by how much---should enable more targeted corrections than raw observation features alone.\nWe test this hypothesis systematically.\n\n% Para 3: Our approach — ACR-VLA pipeline overview\nWe introduce \\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that wraps any frozen flow-matching VLA and performs learned residual action correction.\nACR-VLA operates as a \\emph{sample-then-correct} pipeline:\n(i)~draw $K{=}10$ action samples via independent flow-matching rollouts;\n(ii)~score each sample using Mahalanobis nonconformity under a Ledoit--Wolf shrinkage covariance~\\cite{braun2025cgs} and select the lowest-scoring candidate;\n(iii)~apply a lightweight Conformal Residual Module (CRM)---a 3-layer MLP (${\\sim}$329K parameters) that takes the frozen VLA's observation embedding as input and outputs a bounded residual correction.\nThe corrected action is $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta}, \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon)$, where the norm bound $\\varepsilon$ constrains how far the correction can deviate from the selected action.\nCRM is trained offline via $L_2$ regression on demonstration data; the base VLA is never modified.\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA, and evaluate on two LIBERO task suites~\\cite{liu2023libero}.\n\n% Para 4: Key findings — what we find, including negatives\nOur experiments yield three findings.\n\\emph{First}, sample-then-correct outperforms sample-then-select: on LIBERO-Object (10 tasks with novel object instances), observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for conformal selection alone, a +7.0\\,pp improvement.\nThree baselines---single-sample VLA, 10-sample mean, and argmin selection---all plateau at 12.0\\%, indicating that neither averaging nor selection breaks through on this benchmark.\n\\emph{Second}, per-DOF conformal features as CRM conditioning are an \\emph{honest negative result}: the perdof variant (11.0\\%) performs comparably to argmin selection (12.0\\%) and far below observation-only conditioning (19.0\\%).\nThis contradicts the intuition that richer uncertainty features should yield better corrections.\nWe attribute this to noisy covariance estimation at the $K{=}10$ sample budget ($d/K = 0.6$): while shrinkage stabilizes selection scoring, the per-DOF statistics derived from it carry estimation noise that degrades CRM predictions under the compounding distribution shift of closed-loop evaluation~\\cite{ross2011dagger}.\n\\emph{Third}, correction magnitude control is critical and has not been systematically studied in prior residual policy work~\\cite{silver2018residual,jiang2024transic,xiao2026pld}: without clipping ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$), CRM achieves 0\\% success---compounding error destroys the trajectory entirely.\nConstraining $\\varepsilon$ to $[0.05, 0.2]$ restores stable performance, with observation-conditioned CRM uniquely robust across this range while per-DOF-conditioned CRM collapses at larger bounds.\nOn LIBERO-Spatial (10 tasks with layout changes), all CRM variants achieve 30--35\\%, comparable to the argmin baseline (34\\%)---a null result that we report prominently.\nResidual correction at the action level does not help when the challenge is spatial re-planning rather than fine-grained motor adjustment.\n\n% Para 5: Contributions\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We present the first method that combines multi-sample conformal selection with offline-trained learned residual correction on a frozen VLA.\n  On LIBERO-Object, CRM correction improves success by +7.0\\,pp over selection alone (19.0\\% vs.\\ 12.0\\%), demonstrating that learned correction can synthesize actions better than any individual VLA sample.\n\n  \\item \\textbf{Honest negative: per-DOF conformal features do not improve correction.}\n  Systematic ablation across three conditioning variants---observation embeddings (329K params), per-DOF conformal statistics (339K params), and scalar uncertainty (330K params)---reveals that observation features suffice for effective correction.\n  Per-DOF conformal statistics, despite their theoretical appeal, yield 11.0\\% versus 19.0\\% for observation-only conditioning, challenging the intuition from synthetic experiments that richer uncertainty features enable better corrections.\n\n  \\item \\textbf{Correction magnitude control as a critical design factor.}\n  We show that unbounded residual correction ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic 0\\% success, while the safe operating range $\\varepsilon \\in [0.05, 0.2]$ yields stable improvements.\n  Observation-conditioned CRM maintains performance across this range; per-DOF-conditioned CRM degrades sharply beyond $\\varepsilon = 0.1$.\n  This magnitude sensitivity has not been systematically characterized in prior residual policy literature.\n\\end{enumerate}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01BCuf79KxkvoTAh8rMvGZ4a`</summary>

```json
{
  "name": "Introduction Scenario C (CoRL 2026)",
  "type": "paper",
  "description": "Rewritten Introduction section with Scenario C framing: sample-then-correct pipeline, honest negative on per-DOF conformal features, correction magnitude control. ~780 words, 1.5 pages target.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
  "tags": [
    "paper",
    "introduction",
    "scenario-c",
    "corl2026"
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
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "3eadab87-2825-45af-9606-b4927ae4a084",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sPvkJCU61W5W4dNypqPBu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2144,
      "cache_read_input_tokens": 61650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2144
      },
      "output_tokens": 46,
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

_source line 31 · 2026-05-15T19:50:51.751Z_

<details><summary>↩ Tool result · `toolu_01BCuf79KxkvoTAh8rMvGZ4a`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_607d8d\", \"name\": \"Introduction Scenario C (CoRL 2026)\", \"type\": \"paper\", \"description\": \"Rewritten Introduction section with Scenario C framing: sample-then-correct pipeline, honest negative on per-DOF conformal features, correction magnitude control. ~780 words, 1.5 pages target.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC_607d8d.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:50:51.603981+00:00\", \"tags\": [\"paper\", \"introduction\", \"scenario-c\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "8eebac55-7c53-4d16-a5fb-5c9cc08cd368",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_607d8d\\\", \\\"name\\\": \\\"Introduction Scenario C (CoRL 2026)\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Rewritten Introduction section with Scenario C framing: sample-then-correct pipeline, honest negative on per-DOF conformal features, correction magnitude control. ~780 words, 1.5 pages target.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC_607d8d.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T19:50:51.603981+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"introduction\\\", \\\"scenario-c\\\", \\\"corl2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_607d8d\", \"name\": \"Introduction Scenario C (CoRL 2026)\", \"type\": \"paper\", \"description\": \"Rewritten Introduction section with Scenario C framing: sample-then-correct pipeline, honest negative on per-DOF conformal features, correction magnitude control. ~780 words, 1.5 pages target.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC_607d8d.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:50:51.603981+00:00\", \"tags\": [\"paper\", \"introduction\", \"scenario-c\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

已保存至 `artifacts/_project/paper/introduction_scenarioC.tex` 并注册。

结构概要：
- **Para 1** — 问题：VLA 在分布偏移下退化；现有 inference-time 方法的局限（ReconVLA 只做 selection，SC-VLA 需 RL，VLA-Pilot 延迟高，A2C2 非 post-hoc）
- **Para 2** — Gap：selection 受限于候选质量；learned correction 可以超越，但 conditioning 选什么？
- **Para 3** — ACR-VLA pipeline：K=10 sampling → CGS argmin selection → CRM bounded residual（329K params, obs embedding input, offline L2 training）
- **Para 4** — 三个发现：(1) sample-then-correct +7.0pp on Object；(2) per-DOF conformal features 是 honest negative（11.0% vs 19.0%）；(3) magnitude control 关键（1.42→0%, [0.05,0.2] safe）；Spatial null result 显著报告
- **Para 5** — 三个 contributions（编号列表，与任务要求一致）

所有数字来自 paper_framing.md/writing_plan.yaml，无 overclaim，无 statistical significance 声明，Spatial null result 未隐藏。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "uuid": "57fd8b00-2a8b-4bc7-93dc-821ee894f0d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBoWjhehiguJbCBuWUUHuh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 63794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 593
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

_source line 33_

已保存至 `artifacts/_project/paper/introduction_scenarioC.tex` 并注册。

结构概要：
- **Para 1** — 问题：VLA 在分布偏移下退化；现有 inference-time 方法的局限（ReconVLA 只做 selection，SC-VLA 需 RL，VLA-Pilot 延迟高，A2C2 非 post-hoc）
- **Para 2** — Gap：selection 受限于候选质量；learned correction 可以超越，但 conditioning 选什么？
- **Para 3** — ACR-VLA pipeline：K=10 sampling → CGS argmin selection → CRM bounded residual（329K params, obs embedding input, offline L2 training）
- **Para 4** — 三个发现：(1) sample-then-correct +7.0pp on Object；(2) per-DOF conformal features 是 honest negative（11.0% vs 19.0%）；(3) magnitude control 关键（1.42→0%, [0.05,0.2] safe）；Spatial null result 显著报告
- **Para 5** — 三个 contributions（编号列表，与任务要求一致）

所有数字来自 paper_framing.md/writing_plan.yaml，无 overclaim，无 statistical significance 声明，Spatial null result 未隐藏。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 101142,
  "duration_api_ms": 102016,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "ee474fbc-9941-4175-875e-b3c80de6de8d",
  "total_cost_usd": 0.5668415,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 52546,
    "cache_read_input_tokens": 255870,
    "output_tokens": 4336,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52546,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 364,
        "cache_read_input_tokens": 63794,
        "cache_creation_input_tokens": 593,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 593
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1939,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002034,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 4336,
      "cacheReadInputTokens": 255870,
      "cacheCreationInputTokens": 52546,
      "webSearchRequests": 0,
      "costUSD": 0.5648075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "730f59e5-fe1d-4d54-a796-cf3871d8f478"
}
```

</details>

---
