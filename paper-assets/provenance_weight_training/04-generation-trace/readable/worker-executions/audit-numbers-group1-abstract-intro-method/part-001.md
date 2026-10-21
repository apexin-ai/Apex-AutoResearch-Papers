# audit numbers group1 abstract intro method — Part 1 of 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

[Transcript overview](../audit-numbers-group1-abstract-intro-method.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/02/02c3bcf5ede54ce3a99c.json)

## Before a recorded user message

## Before a recorded user message

22 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "48ae3c72-5809-4534-9d07-df0077689849",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1779756000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "588b199a-9088-4686-882f-14ff29b6ed76",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to audit all numbers in 4 paper sections for accuracy, traceability, and consistency. Let me start by reading all 4 files and the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "45675092-c962-4b7e-ab8b-7f31a2fa4c4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSR8PYykt6JHipgS9kRvzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12530,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12530
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

开始审计。先并行读取 4 个 tex 文件和 registry。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "2db820b6-de8e-476e-bee8-48c73138bf4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSR8PYykt6JHipgS9kRvzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12530,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12530
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

<details open><summary>🔧 Tool call — Read · `toolu_01P6yHHNfoCFX6uEQYMjZpXK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "b640baf8-ba3a-4b2d-912d-81987ad08e59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSR8PYykt6JHipgS9kRvzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12530,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12530
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

_source line 7 · 2026-05-25T19:42:10.531Z_

<details><summary>↩ Tool result · `toolu_01P6yHHNfoCFX6uEQYMjZpXK`</summary>

```text
1	As synthetic text pervades web corpora, detect-and-reweight methods that downweight likely-synthetic samples during training have emerged to prevent model collapse, yet when they actually help remains unclear.
2	We investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.
3	First, detect-and-remove (D\&R) outperforms all reweighting methods in our setting; epoch-matched controls attribute over 95\% of the advantage to multi-epoch exposure on filtered data, identifying the mechanism behind D\&R's effectiveness.
4	Second, the detector must provide both sufficient discrimination \emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.
5	Third, minimum intervention, applying the smallest reweighting exponent that meets a quality floor, outperforms unconstrained weight maximization.
6	As an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\bstar$ that improves over uniform training at contamination ratios $\rho \geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.
7	These findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established\footnote{Code and data are available at \url{https://anonymous.4open.science/r/provenance_weight_training-F72D/}.}.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "60d5b4b5-3ff2-4ed0-b704-6993521f788a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/abstract.tex",
      "content": "As synthetic text pervades web corpora, detect-and-reweight methods that downweight likely-synthetic samples during training have emerged to prevent model collapse, yet when they actually help remains unclear.\nWe investigate this question through controlled continued-pretraining experiments (Qwen3-0.6B, 132M tokens, 5 seeds) and identify three effectiveness conditions.\nFirst, detect-and-remove (D\\&R) outperforms all reweighting methods in our setting; epoch-matched controls attribute over 95\\% of the advantage to multi-epoch exposure on filtered data, identifying the mechanism behind D\\&R's effectiveness.\nSecond, the detector must provide both sufficient discrimination \\emph{and} good calibration; high-AUC detectors with poor calibration degrade performance below uniform training.\nThird, minimum intervention, applying the smallest reweighting exponent that meets a quality floor, outperforms unconstrained weight maximization.\nAs an illustrative application of the minimum-intervention principle, we derive a dual-constrained adaptive exponent $\\bstar$ that improves over uniform training at contamination ratios $\\rho \\geq 0.4$, reaching conventional significance after multiple-comparison correction, while requiring no per-model tuning.\nThese findings apply within our self-contamination setup at 0.6B scale; generalization to cross-model contamination and larger models remains to be established\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/provenance_weight_training-F72D/}.}.\n",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2aWHSUCUtMQgM3fEM5qyc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "aec64319-e1ea-45f9-9f31-6b2d9d8c8bb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSR8PYykt6JHipgS9kRvzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12530,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12530
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

_source line 9 · 2026-05-25T19:42:10.883Z_

<details><summary>↩ Tool result · `toolu_01Y2aWHSUCUtMQgM3fEM5qyc`</summary>

```text
1	The detect-and-reweight paradigm~\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\% of crawled data~\citep{cheng2025contamination}.
2	Training on such data risks model collapse~\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.
3	An alternative, Detect and Remove (D\&R), hard-filters samples above a threshold~\citep{feng2025beyond}.
4	
5	\begin{figure*}[t]
6	\centering
7	\includegraphics[width=\textwidth]{fig1_overview}
8	\caption{Three effectiveness conditions for detect-and-reweight.
9	\textbf{(a)}~D\&R achieves the best raw PPL; epoch-matched controls reveal that multi-epoch exposure on filtered data accounts for the bulk of the advantage (\S\ref{sec:results}).
10	\textbf{(b)}~Only detectors with both high AUC \emph{and} low ECE fall in the effective zone; comparable AUC with poor calibration degrades PPL below uniform.
11	\textbf{(c)}~Adaptive $\bstar{\approx}0.9$ operates near the grid-search optimum, while ESS-only $b{\approx}3.5$ falls in the degradation zone.}
12	\label{fig:overview}
13	\end{figure*}
14	
15	Despite growing adoption, the paradigm's effectiveness conditions are poorly characterized.
16	What mechanism drives D\&R's strong performance, and how does it compare to soft reweighting under controlled conditions?
17	What detector properties are necessary for effective reweighting?
18	How does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?
19	
20	We investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\rho{=}0.4$, 5 seeds), with extensions to $\rho \in \{0.2, 0.6\}$ and 1.7B parameters (\S\ref{sec:limitations} discusses scope).
21	To ground the analysis of exponent selection, we implement a dual-constrained formulation as an illustrative application: find the minimum $b$ such that $\aeff(b) \geq \tau$ (quality floor, motivated by convergence theory~\citep{wang2026survive}), subject to $\mathrm{ESS}(b) \geq \nmin$ (stability ceiling)~\citep{kish1965survey,vehtari2024psis}.
22	
23	Our analysis yields three findings:
24	\begin{itemize}[nosep,leftmargin=*]
25	\item \textbf{D\&R as the strongest strategy.}
26	D\&R outperforms all reweighting methods in our setting (PPL $17.250$ vs.\ $17.674$, 3 seeds); epoch-matched controls attribute ${>}$95\% of the advantage to multi-epoch exposure on filtered data, reducing the gap to $\Delta{=}0.017$ (Table~\ref{tab:epoch_match}).
27	
28	\item \textbf{Detector requirements for effective reweighting.}
29	Both sufficient discrimination (area under the ROC curve; AUC) and good calibration (expected calibration error; ECE) are empirically observed requirements in our self-contamination setting; a high-AUC but poorly calibrated detector degrades performance below uniform (3 detectors, 3 seeds; \S\ref{sec:robustness}).
30	
31	\item \textbf{Minimum intervention outperforms maximization.}
32	An $\aeff$ quality constraint binds in ${\sim}$50\% of batches at ${\approx}5.9{\times}$ lower sharpening exponents than an ESS-only alternative (\S\ref{sec:regime}); at $\rho{=}0.6$, ESS-only collapses toward uniform while the dual constraint maintains its advantage.
33	\end{itemize}
34	To demonstrate the minimum-intervention principle, we derive a dual-constrained adaptive $\bstar$ that eliminates per-model grid search ($\Delta{=}{-}0.023$ at $\rho{=}0.4$, $-$0.032 at $\rho{=}0.6$; Table~\ref{tab:main}), with transferable defaults ($\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$).
35	The method fails at $\rho{=}0.2$; at 1.7B it shows no degradation but the benefit diminishes.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "e2d6747a-58fe-43eb-9a5b-6f474b2354dd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/introduction.tex",
      "content": "The detect-and-reweight paradigm~\\citep{drayson2025detection} has emerged as a response to synthetic contamination in web corpora, now estimated at 20--60\\% of crawled data~\\citep{cheng2025contamination}.\nTraining on such data risks model collapse~\\citep{shumailov2024model,dohmatob2025strong}, motivating methods that downweight likely-synthetic samples via $w(x) = (1 - q(x))^b$, where $q(x)$ is a detector's synthetic probability and $b$ is a sharpening exponent.\nAn alternative, Detect and Remove (D\\&R), hard-filters samples above a threshold~\\citep{feng2025beyond}.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_overview}\n\\caption{Three effectiveness conditions for detect-and-reweight.\n\\textbf{(a)}~D\\&R achieves the best raw PPL; epoch-matched controls reveal that multi-epoch exposure on filtered data accounts for the bulk of the advantage (\\S\\ref{sec:results}).\n\\textbf{(b)}~Only detectors with both high AUC \\emph{and} low ECE fall in the effective zone; comparable AUC with poor calibration degrades PPL below uniform.\n\\textbf{(c)}~Adaptive $\\bstar{\\approx}0.9$ operates near the grid-search optimum, while ESS-only $b{\\approx}3.5$ falls in the degradation zone.}\n\\label{fig:overview}\n\\end{figure*}\n\nDespite growing adoption, the paradigm's effectiveness conditions are poorly characterized.\nWhat mechanism drives D\\&R's strong performance, and how does it compare to soft reweighting under controlled conditions?\nWhat detector properties are necessary for effective reweighting?\nHow does the reweighting mechanism behave across contamination levels, and can $b$ be set without per-model grid search?\n\nWe investigate these questions through controlled experiments on Qwen3-0.6B continued pretraining (132M FineWeb tokens, $\\rho{=}0.4$, 5 seeds), with extensions to $\\rho \\in \\{0.2, 0.6\\}$ and 1.7B parameters (\\S\\ref{sec:limitations} discusses scope).\nTo ground the analysis of exponent selection, we implement a dual-constrained formulation as an illustrative application: find the minimum $b$ such that $\\aeff(b) \\geq \\tau$ (quality floor, motivated by convergence theory~\\citep{wang2026survive}), subject to $\\mathrm{ESS}(b) \\geq \\nmin$ (stability ceiling)~\\citep{kish1965survey,vehtari2024psis}.\n\nOur analysis yields three findings:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{D\\&R as the strongest strategy.}\nD\\&R outperforms all reweighting methods in our setting (PPL $17.250$ vs.\\ $17.674$, 3 seeds); epoch-matched controls attribute ${>}$95\\% of the advantage to multi-epoch exposure on filtered data, reducing the gap to $\\Delta{=}0.017$ (Table~\\ref{tab:epoch_match}).\n\n\\item \\textbf{Detector requirements for effective reweighting.}\nBoth sufficient discrimination (area under the ROC curve; AUC) and good calibration (expected calibration error; ECE) are empirically observed requirements in our self-contamination setting; a high-AUC but poorly calibrated detector degrades performance below uniform (3 detectors, 3 seeds; \\S\\ref{sec:robustness}).\n\n\\item \\textbf{Minimum intervention outperforms maximization.}\nAn $\\aeff$ quality constraint binds in ${\\sim}$50\\% of batches at ${\\approx}5.9{\\times}$ lower sharpening exponents than an ESS-only alternative (\\S\\ref{sec:regime}); at $\\rho{=}0.6$, ESS-only collapses toward uniform while the dual constraint maintains its advantage.\n\\end{itemize}\nTo demonstrate the minimum-intervention principle, we derive a dual-constrained adaptive $\\bstar$ that eliminates per-model grid search ($\\Delta{=}{-}0.023$ at $\\rho{=}0.4$, $-$0.032 at $\\rho{=}0.6$; Table~\\ref{tab:main}), with transferable defaults ($\\tau{=}0.7$, $\\nmin{=}\\lfloor B/2 \\rfloor$).\nThe method fails at $\\rho{=}0.2$; at 1.7B it shows no degradation but the benefit diminishes.\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_019ohtYLjjhAd3WMZ1s3bFaQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "31964b11-81f0-4aa2-97b6-7e8066fdba5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSR8PYykt6JHipgS9kRvzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12530,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12530
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

_source line 11 · 2026-05-25T19:42:11.374Z_

<details><summary>↩ Tool result · `toolu_019ohtYLjjhAd3WMZ1s3bFaQ`</summary>

```text
1	\begin{figure}[t]
2	\centering
3	\includegraphics[width=\columnwidth]{dr_pipeline_concept}
4	\caption{Overview of the detect-and-reweight pipeline. A TF-IDF + LR detector assigns contamination scores $q(x)$; a dual-constrained optimizer selects $b$ to satisfy quality-floor and effective-sample-size constraints; the resulting weights $w(x) = (1{-}q(x))^{b}$ are applied during training.}
5	\label{fig:pipeline}
6	\end{figure}
7	
8	Figure~\ref{fig:pipeline} illustrates the pipeline. Let $\mathcal{D}$ denote a pretraining corpus with unknown synthetic contamination ratio $\rho$~\citep{cheng2025contamination}.
9	A detector assigns each sample $x$ a synthetic probability $q(x) \in [0,1]$; following \citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).
10	Rather than selecting $b$ via grid search, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.
11	
12	Given a batch $\mathcal{B} = \{x_1, \ldots, x_B\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:
13	
14	\paragraph{Quality floor.}
15	The \emph{effective authenticity} $\aeff(b) = \sum_i w_i(b)(1{-}q_i) / \sum_i w_i(b)$ measures the weighted mean detector confidence that samples are real.
16	We require $\aeff(b) \geq \tau$, yielding a lower bound $b_\tau$ on the exponent, motivated by convergence theory under contamination~\citep{wang2026survive}.
17	$\aeff$ correlates with the true batch-level real fraction at Pearson $r \approx 0.79$ (Appendix~\ref{app:alpha_validation}); limitations are discussed in \S\ref{sec:discussion}.
18	
19	\paragraph{Stability ceiling.}
20	Kish's effective sample size $\mathrm{ESS}(b) = (\sum_i w_i)^2 / \sum_i w_i^2$~\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\ref{app:proofs}).
21	We require $\mathrm{ESS}(b) \geq \nmin$, yielding an upper bound $\bess$.
22	
23	\paragraph{Adaptive $\bstar$.}
24	Since $\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\tau, \bess]$.
25	The optimal exponent implements \emph{minimum intervention}:
26	\begin{equation}
27	  b^{*} = \begin{cases}
28	    0        & \text{if } \aeff(0) \geq \tau, \\
29	    b_\tau   & \text{if } b_\tau \leq \bess, \\
30	    \bess & \text{otherwise (stability precedence)},
31	  \end{cases}
32	  \label{eq:bstar}
33	\end{equation}
34	applying the smallest $b$ that achieves the quality floor.
35	Each batch falls into one of three regimes (clean, $\aeff$-binding, or ESS-binding; Figure~\ref{fig:dual_constraint}) whose frequencies we analyze in \S\ref{sec:regime}.
36	The resulting $\bstar$ trajectory (Figure~\ref{fig:bstar_traj}, Appendix) varies substantially across batches, with all three regimes alternating throughout; this per-batch variation indicates adaptation to local composition rather than global dynamics.
37	
38	\begin{figure*}[t]
39	\centering
40	\includegraphics[width=\textwidth]{dual_constraint_illustration}
41	\caption{Dual-constraint $\bstar$ selection for two representative batches ($B{=}4$, $\tau{=}0.7$, $\nmin{=}2$).
42	\textbf{(a)}~Quality constraint binds: $\aeff(b)$ reaches $\tau$ before $\mathrm{ESS}(b)$ drops below $\nmin$, so $\bstar = \btau$.
43	\textbf{(b)}~Stability constraint binds: $\mathrm{ESS}(b)$ hits the floor first, so $\bstar = \bess$.
44	Green: feasible interval; red: over-sharpening.}
45	\label{fig:dual_constraint}
46	\end{figure*}
47	
48	Given $\bstar$, normalized weights $\pi_i = w_i(\bstar) / \sum_j w_j(\bstar)$ define the weighted loss $\mathcal{L} = \sum_i \pi_i \ell_i$; $\bstar$ is found via bisection (Algorithm~\ref{alg:bstar}, Appendix~\ref{app:algorithm}) in $\mathcal{O}(B \log(b_{\max}/\varepsilon))$ operations, negligible beside the forward pass.
49	Defaults: $\tau{=}0.7$, $\nmin{=}\lfloor B/2 \rfloor$; sensitivity in \S\ref{sec:sensitivity}.
50	
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "05453150-e189-4d22-85eb-504f2d81da78",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/method.tex",
      "content": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{dr_pipeline_concept}\n\\caption{Overview of the detect-and-reweight pipeline. A TF-IDF + LR detector assigns contamination scores $q(x)$; a dual-constrained optimizer selects $b$ to satisfy quality-floor and effective-sample-size constraints; the resulting weights $w(x) = (1{-}q(x))^{b}$ are applied during training.}\n\\label{fig:pipeline}\n\\end{figure}\n\nFigure~\\ref{fig:pipeline} illustrates the pipeline. Let $\\mathcal{D}$ denote a pretraining corpus with unknown synthetic contamination ratio $\\rho$~\\citep{cheng2025contamination}.\nA detector assigns each sample $x$ a synthetic probability $q(x) \\in [0,1]$; following \\citet{drayson2025detection}, we weight each sample as $w(x) = (1 - q(x))^{b}$, where $b \\geq 0$ is a sharpening exponent ($b{=}0$ recovers uniform training).\nRather than selecting $b$ via grid search, we derive $b$ per-batch from the batch's $q$-score distribution using two opposing constraints.\n\nGiven a batch $\\mathcal{B} = \\{x_1, \\ldots, x_B\\}$ with scores $q_i = q(x_i)$ and weights $w_i(b) = (1 - q_i)^{b}$:\n\n\\paragraph{Quality floor.}\nThe \\emph{effective authenticity} $\\aeff(b) = \\sum_i w_i(b)(1{-}q_i) / \\sum_i w_i(b)$ measures the weighted mean detector confidence that samples are real.\nWe require $\\aeff(b) \\geq \\tau$, yielding a lower bound $b_\\tau$ on the exponent, motivated by convergence theory under contamination~\\citep{wang2026survive}.\n$\\aeff$ correlates with the true batch-level real fraction at Pearson $r \\approx 0.79$ (Appendix~\\ref{app:alpha_validation}); limitations are discussed in \\S\\ref{sec:discussion}.\n\n\\paragraph{Stability ceiling.}\nKish's effective sample size $\\mathrm{ESS}(b) = (\\sum_i w_i)^2 / \\sum_i w_i^2$~\\citep{kish1965survey} decreases monotonically in $b$ (Appendix~\\ref{app:proofs}).\nWe require $\\mathrm{ESS}(b) \\geq \\nmin$, yielding an upper bound $\\bess$.\n\n\\paragraph{Adaptive $\\bstar$.}\nSince $\\aeff$ is non-decreasing and ESS is decreasing in $b$, the two constraints define an interval $[b_\\tau, \\bess]$.\nThe optimal exponent implements \\emph{minimum intervention}:\n\\begin{equation}\n  b^{*} = \\begin{cases}\n    0        & \\text{if } \\aeff(0) \\geq \\tau, \\\\\n    b_\\tau   & \\text{if } b_\\tau \\leq \\bess, \\\\\n    \\bess & \\text{otherwise (stability precedence)},\n  \\end{cases}\n  \\label{eq:bstar}\n\\end{equation}\napplying the smallest $b$ that achieves the quality floor.\nEach batch falls into one of three regimes (clean, $\\aeff$-binding, or ESS-binding; Figure~\\ref{fig:dual_constraint}) whose frequencies we analyze in \\S\\ref{sec:regime}.\nThe resulting $\\bstar$ trajectory (Figure~\\ref{fig:bstar_traj}, Appendix) varies substantially across batches, with all three regimes alternating throughout; this per-batch variation indicates adaptation to local composition rather than global dynamics.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{dual_constraint_illustration}\n\\caption{Dual-constraint $\\bstar$ selection for two representative batches ($B{=}4$, $\\tau{=}0.7$, $\\nmin{=}2$).\n\\textbf{(a)}~Quality constraint binds: $\\aeff(b)$ reaches $\\tau$ before $\\mathrm{ESS}(b)$ drops below $\\nmin$, so $\\bstar = \\btau$.\n\\textbf{(b)}~Stability constraint binds: $\\mathrm{ESS}(b)$ hits the floor first, so $\\bstar = \\bess$.\nGreen: feasible interval; red: over-sharpening.}\n\\label{fig:dual_constraint}\n\\end{figure*}\n\nGiven $\\bstar$, normalized weights $\\pi_i = w_i(\\bstar) / \\sum_j w_j(\\bstar)$ define the weighted loss $\\mathcal{L} = \\sum_i \\pi_i \\ell_i$; $\\bstar$ is found via bisection (Algorithm~\\ref{alg:bstar}, Appendix~\\ref{app:algorithm}) in $\\mathcal{O}(B \\log(b_{\\max}/\\varepsilon))$ operations, negligible beside the forward pass.\nDefaults: $\\tau{=}0.7$, $\\nmin{=}\\lfloor B/2 \\rfloor$; sensitivity in \\S\\ref{sec:sensitivity}.\n\n",
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01AZHWBF1kFRCZWw2GpTLm3T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "a819381a-4f7b-49ab-be7e-0ce27c94035a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSR8PYykt6JHipgS9kRvzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12530,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12530
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

_source line 13 · 2026-05-25T19:42:12.464Z_

<details><summary>↩ Tool result · `toolu_01AZHWBF1kFRCZWw2GpTLm3T`</summary>

```text
1	\paragraph{Synthetic Contamination and Model Collapse.}
2	Training on recursively generated data leads to irreversible quality degradation (\emph{model collapse})~\citep{shumailov2024model}.
3	\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.
4	More critically, \citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.
5	\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\% of web corpora, though accumulating real data avoids divergence~\citep{kazdan2025collapse} and even minimal curation suffices~\citep{amin2025escaping}.
6	Not all synthetic data is harmful: the Phi series~\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.
7	
8	\paragraph{Detection, Filtering, and Data Reweighting.}
9	Continuous-score detectors---probability curvature~\citep{mitchell2023detectgpt}, cross-perplexity ratios~\citep{hans2024binoculars}, low-probability token statistics~\citep{shi2024minkprob}---enable document-level weighting~\citep{wu2025survey}.
10	Data composition is optimized via perplexity filtering~\citep{wenzek2020ccnet}, domain-level importance sampling~\citep{xie2023doremi,xie2023dsir,grangier2025crisp,ye2025mixing}, instance-level strategies~\citep{bengio2009curriculum,mindermann2022prioritized,sow2025dynamic,engstrom2024dsdm}, and deduplication~\citep{abbas2023semdedup}; see \citet{albalak2024survey}.
11	None targets synthetic provenance; moreover, classifier-based quality scores may capture stylistic similarity rather than intrinsic quality~\citep{naitsaada2025illusion}.
12	Most directly related, \citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight in from-scratch pretraining, where $q_j$ is the detector's synthetic probability. We adopt the same formula but differ fundamentally:
13	\textbf{(i)}~Drayson et al.\ select $b$ via validation-set grid search, with different model scales requiring different values ($b{=}10$ for ${\leq}360$M, $b{=}1$ for 1.7B); our $\bstar$ is derived per-batch from dual constraints ($\aeff \geq \tau$, $\mathrm{ESS} \geq \nmin$) at zero validation cost.
14	\textbf{(ii)}~Their sampling importance resampling (SIR) discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.
15	\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\,=\,0.986) on WikiText-2 (${\sim}$2M tokens); we show that a lightweight TF-IDF + logistic regression detector (AUC\,=\,0.94) suffices on FineWeb-scale data (132M+ tokens), and both calibration and sufficient discrimination appear required for effective reweighting.
16	
17	\paragraph{Theoretical Foundations.}
18	Importance weighting theory underpins our constraints. \citet{cortes2010learning} establish generalization bounds governed by the weight second moment, directly motivating our ESS floor since $\mathrm{ESS} = n/\mathbb{E}[w^2]$.
19	\citet{fang2020rethinking} show that na\"ive importance weighting degrades in deep networks under distribution shift, motivating adaptive, bounded schemes such as ours.
20	For LLM pretraining, \citet{sow2025dynamic} prove convergence guarantees for instance-level reweighting under bounded weight variance---a condition our ESS constraint explicitly enforces---while \citet{ye2025mixing} derive functional laws governing how mixture proportions affect loss, complementing our instance-level approach.
21	\citet{he2025golden} derive the optimal real-data weight under known mixture proportions (the golden-ratio reciprocal ${\approx}0.62$); their result requires the contamination ratio $k$, unavailable in web-scale settings, so we use it as an oracle baseline.
22	\citet{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\alpha$; this motivates our quality threshold $\aeff(b) \geq \tau$.
23	We operationalize this without the known-proportion assumption, estimating $\aeff$ from batch-level statistics online.
24	Score calibration~\citep{guo2017calibration} is relevant because miscalibration systematically biases $\aeff$; for the stability constraint, we build on Kish's effective sample size~\citep{kish1965survey}.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "6ad69c38-d7ab-43b9-9fd0-401f7f878c78",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/related_work.tex",
      "content": "\\paragraph{Synthetic Contamination and Model Collapse.}\nTraining on recursively generated data leads to irreversible quality degradation (\\emph{model collapse})~\\citep{shumailov2024model}.\n\\citet{alemohammad2024mad} formalize this as Model Autophagy Disorder, showing that quality inevitably degrades without fresh real data.\nMore critically, \\citet{dohmatob2025strong} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger collapse, ruling out data scaling as a remedy.\n\\citet{cheng2025contamination} confirm that synthetic content now constitutes an estimated 20--60\\% of web corpora, though accumulating real data avoids divergence~\\citep{kazdan2025collapse} and even minimal curation suffices~\\citep{amin2025escaping}.\nNot all synthetic data is harmful: the Phi series~\\citep{gunasekar2023textbooks,li2023textbooks2} demonstrates that curated synthetic data can improve training efficiency, but this assumes intentional generation with quality control, unlike the uncontrolled web contamination we address.\n\n\\paragraph{Detection, Filtering, and Data Reweighting.}\nContinuous-score detectors---probability curvature~\\citep{mitchell2023detectgpt}, cross-perplexity ratios~\\citep{hans2024binoculars}, low-probability token statistics~\\citep{shi2024minkprob}---enable document-level weighting~\\citep{wu2025survey}.\nData composition is optimized via perplexity filtering~\\citep{wenzek2020ccnet}, domain-level importance sampling~\\citep{xie2023doremi,xie2023dsir,grangier2025crisp,ye2025mixing}, instance-level strategies~\\citep{bengio2009curriculum,mindermann2022prioritized,sow2025dynamic,engstrom2024dsdm}, and deduplication~\\citep{abbas2023semdedup}; see \\citet{albalak2024survey}.\nNone targets synthetic provenance; moreover, classifier-based quality scores may capture stylistic similarity rather than intrinsic quality~\\citep{naitsaada2025illusion}.\nMost directly related, \\citet{drayson2025detection} propose $w_j = (1{-}q_j)^b$ for collapse prevention via detect-and-reweight in from-scratch pretraining, where $q_j$ is the detector's synthetic probability. We adopt the same formula but differ fundamentally:\n\\textbf{(i)}~Drayson et al.\\ select $b$ via validation-set grid search, with different model scales requiring different values ($b{=}10$ for ${\\leq}360$M, $b{=}1$ for 1.7B); our $\\bstar$ is derived per-batch from dual constraints ($\\aeff \\geq \\tau$, $\\mathrm{ESS} \\geq \\nmin$) at zero validation cost.\n\\textbf{(ii)}~Their sampling importance resampling (SIR) discretizes the weight distribution; we apply direct loss reweighting with continuous gradients.\n\\textbf{(iii)}~They employ a ModernBERT-150M detector (AUC\\,=\\,0.986) on WikiText-2 (${\\sim}$2M tokens); we show that a lightweight TF-IDF + logistic regression detector (AUC\\,=\\,0.94) suffices on FineWeb-scale data (132M+ tokens), and both calibration and sufficient discrimination appear required for effective reweighting.\n\n\\paragraph{Theoretical Foundations.}\nImportance weighting theory underpins our constraints. \\citet{cortes2010learning} establish generalization bounds governed by the weight second moment, directly motivating our ESS floor since $\\mathrm{ESS} = n/\\mathbb{E}[w^2]$.\n\\citet{fang2020rethinking} show that na\\\"ive importance weighting degrades in deep networks under distribution shift, motivating adaptive, bounded schemes such as ours.\nFor LLM pretraining, \\citet{sow2025dynamic} prove convergence guarantees for instance-level reweighting under bounded weight variance---a condition our ESS constraint explicitly enforces---while \\citet{ye2025mixing} derive functional laws governing how mixture proportions affect loss, complementing our instance-level approach.\n\\citet{he2025golden} derive the optimal real-data weight under known mixture proportions (the golden-ratio reciprocal ${\\approx}0.62$); their result requires the contamination ratio $k$, unavailable in web-scale settings, so we use it as an oracle baseline.\n\\citet{wang2026survive} prove that contaminated recursive training converges at a rate governed by the effective real-data fraction $\\alpha$; this motivates our quality threshold $\\aeff(b) \\geq \\tau$.\nWe operationalize this without the known-proportion assumption, estimating $\\aeff$ from batch-level statistics online.\nScore calibration~\\citep{guo2017calibration} is relevant because miscalibration systematically biases $\\aeff$; for the stability constraint, we build on Kish's effective sample size~\\citep{kish1965survey}.\n",
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

_source line 14_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ha5KVYuFT8yqNanLRRWX9Q`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "cf02f4e3-38b4-4ab2-9293-dc552ecd28e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSR8PYykt6JHipgS9kRvzj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12530,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12530
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

_source line 15 · 2026-05-25T19:42:12.951Z_

<details><summary>↩ Tool result · `toolu_01Ha5KVYuFT8yqNanLRRWX9Q`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "64eb00c7-4be8-4c47-8160-6d0b292a3c4f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the registry to get all experiment data for cross-referencing numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "4c311cba-c789-4f99-8187-6517ee4dbb99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5ChxhTRcBuM6GnZXeaNZ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5346,
      "cache_read_input_tokens": 24371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5346
      },
      "output_tokens": 19,
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

读取 registry 获取实验数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "cf591662-83d9-45c2-b991-cb041de88817",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5ChxhTRcBuM6GnZXeaNZ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5346,
      "cache_read_input_tokens": 24371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5346
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01FvyXAioaLyFpPXCaXbqCGS`</summary>

```json
{
  "project": "provenance_weight_training",
  "limit": 0,
  "fields": [
    "*"
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
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "3ad214b7-2fa9-496b-9de7-f3fc8b34b4aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5ChxhTRcBuM6GnZXeaNZ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5346,
      "cache_read_input_tokens": 24371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5346
      },
      "output_tokens": 19,
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

_source line 19 · 2026-05-25T19:42:18.916Z_

<details><summary>↩ Tool result · `toolu_01FvyXAioaLyFpPXCaXbqCGS`</summary>

```text
Error: result (485,271 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "222bf66f-5efc-4480-9116-fd42a588ed32",
  "tool_use_result": {
    "content": "Error: result (485,271 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"detect_remove_q07_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:35:47.832Z\", \"updated_at\": \"2026-05-25T09:01:28.560Z\", \"hypothesis\": \"D&R q>0.7 threshold seed=456 replicate. Retains ~50% data (184,908/370k). Cross-seed for error bar with seed42 (r3) and seed123.\", \"parent\": \"detect_remove_q07_seed42_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q07.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --bf16 --save_total_limit 2 --logging_steps 10 --save_steps 500\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data_filtered_q07.jsonl\", \"data_count\": 184908, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed456/final\", \"log_path\": \"/tmp/eval_q07_seed456.log\", \"metrics\": {\"holdout_ppl\": 17.32, \"owt_ppl\": 18.03, \"wiki_ppl\": 15.11}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T09:01:28.560Z\"}, \"detect_remove_q07_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:35:46.625Z\", \"updated_at\": \"2026-05-25T09:01:26.030Z\", \"hypothesis\": \"D&R q>0.7 threshold seed=123 replicate. Retains ~50% data (184,908/370k). Cross-seed for error bar with seed42 (r3) and seed456.\", \"parent\": \"detect_remove_q07_seed42_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q07.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --bf16 --save_total_limit 2 --logging_steps 10 --save_steps 500\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data_filtered_q07.jsonl\", \"data_count\": 184908, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed123/final\", \"log_path\": \"/tmp/eval_q07_seed123.log\", \"metrics\": {\"holdout_ppl\": 17.32, \"owt_ppl\": 18.04, \"wiki_ppl\": 15.1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T09:01:26.030Z\"}, \"detect_remove_q07_seed42_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T04:32:32.606Z\", \"updated_at\": \"2026-05-25T09:01:23.531Z\", \"hypothesis\": \"D&R q>0.7 threshold fresh rerun (r3). Retains ~50% data (184,908/370k). Prior r2 corrupted by optimizer state loss during resume. Fresh training from step 0 with full optimizer state preservation.\", \"parent\": \"detect_remove_q07_seed42_r2\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q07.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed42_r3 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_total_limit 2 --logging_steps 10 --save_steps 500\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data_filtered_q07.jsonl\", \"data_count\": 184908, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"pid\": 12122, \"gpu\": \"cuda:1\", \"log_path\": \"/root/provenance_weight_training/logs/detect_remove_q07_seed42_r3_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed42_r3\", \"checkpoint_source\": \"N/A (fresh training, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed42_r3/final\", \"log_path\": \"/tmp/eval_q07_seed42_r3.log\", \"metrics\": {\"holdout_ppl\": 17.32, \"owt_ppl\": 18.04, \"wiki_ppl\": 15.11}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T09:01:23.531Z\"}, \"detect_remove_q07_seed42_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:12:00.041Z\", \"updated_at\": \"2026-05-25T04:30:47.018Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q07.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_total_limit 2 --save_only_model --logging_steps 10 --eval_steps 500 --save_steps 500\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"987903\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed42/train.log\", \"submitted_at\": \"2026-05-18T12:11:59.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q07.jsonl\", \"data_count\": 184908, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 577078.5, \"gpu_hours\": 160.3}, \"conclusion\": \"killed\", \"hypothesis\": \"Hard filtering at q_score > 0.7 threshold retains ~50% of data (184,908/370k samples), the most conservative D&R strategy keeping only high-confidence clean samples. Expected to outperform more aggressive thresholds (q>0.3, q>0.5) due to higher data quality per sample, completing the D&R threshold sweep.\", \"completed_at\": \"2026-05-25T04:29:58.212Z\", \"notes\": \"Killed: resume from checkpoint had missing optimizer/scheduler state (--save_only_model), AdamW momentum reset corrupted training. Replaced by detect_remove_q07_seed42_r3 (fresh from step 0).\"}, \"detect_remove_q03_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T14:24:48.317Z\", \"updated_at\": \"2026-05-25T04:30:44.316Z\", \"hypothesis\": \"Hard filtering (detect-and-remove) at q_score > 0.3 threshold retains ~70% of data by removing only high-confidence contaminated samples. Expected to outperform q>0.5 filtering (which is more aggressive) but underperform adaptive weighting which uses soft scores instead of binary thresholds.\", \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"completed_at\": \"2026-05-18T16:26:07.870Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"pid\": 8472, \"note\": \"resume from checkpoint-3000, inline eval disabled (--eval_data_path removed)\"}, \"conclusion\": \"killed\", \"notes\": \"Killed: resume from checkpoint had missing optimizer/scheduler state (--save_only_model), AdamW momentum reset corrupted training. q03 already has 3 seeds from prior runs, no rerun needed.\"}, \"detect_remove_q05_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T11:28:28.035Z\", \"updated_at\": \"2026-05-25T04:30:42.171Z\", \"hypothesis\": \"Hard filtering (detect-and-remove) at q_score > 0.5 threshold discards contaminated samples and trains uniformly on remaining clean data. Expected to underperform adaptive weighting because it wastes information from borderline samples and the binary threshold is miscalibrated relative to the soft q_score distribution.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_seed42/checkpoint-5500\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_seed42/train.log\"}, \"notes\": \"ckpt-5500 used as final due to resume optimizer corruption (--save_only_model caused missing optimizer/scheduler state, AdamW momentum reset on resume → PPL degraded to 17.946). ckpt-5500 metrics: holdout=17.291, owt=18.02, wiki=15.06\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T03:50:28.538385+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T04:30:30.091Z\", \"metrics\": {\"holdout_ppl\": 17.291, \"owt_ppl\": 18.02, \"wiki_ppl\": 15.06}}, \"eval_dr_q05_ckpt5500\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T03:28:03.136Z\", \"updated_at\": \"2026-05-25T03:56:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.29, \"holdout_loss\": 2.8502, \"owt_ppl\": 18.02, \"owt_loss\": 2.8916, \"wiki_ppl\": 15.06, \"wiki_loss\": 2.7118}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_seed42/checkpoint-5500\", \"log_path\": \"/tmp/eval_dr_q05_ckpt5500.log\", \"hypothesis\": \"Interim eval of D&R q>0.5 at checkpoint-5500 (70.8% training progress) to provide early data for paper while final training completes\", \"parent\": \"detect_remove_q05_seed42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_perplexity.py --checkpoints .../checkpoint-5500 --data_path {holdout,owt,wiki} --max_docs 5000 --max_length 2048\", \"server\": \"westd-41312\", \"data_path\": \"data/human/eval_holdout.jsonl, data/eval_openwebtext.jsonl, data/eval_wikipedia.jsonl\", \"data_count\": 15000, \"model_name\": \"detect_remove_q05_seed42/checkpoint-5500\", \"seed\": 42, \"checkpoint_source\": \"detect_remove_q05_seed42\", \"eval_data\": \"holdout + openwebtext + wikipedia (5000 docs each)\"}}, \"detect_remove_q07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T07:41:19.509Z\", \"updated_at\": \"2026-05-25T03:50:18.391Z\", \"hypothesis\": \"D&R threshold t=0.7: keep q≤0.7 (184,908 samples, 49.8%), removing moderately suspicious data. Tests intermediate filtering aggressiveness between t=0.5 (41.4%) and t=0.9 (61.6%). Part of threshold sensitivity sweep.\", \"spec\": {\"pid\": 8867, \"note\": \"resume from checkpoint-2500, inline eval disabled (--eval_data_path removed)\"}, \"metrics\": {\"eval_ppl_holdout\": 17.32, \"eval_loss_holdout\": 2.8519, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"note\": \"final checkpoint, replaces partial ckpt-3500 PPL=17.49\"}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q07_seed42/checkpoint-3500\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q07_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:26:21.761Z\"}, \"random_subset_epoch_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T08:45:39.415Z\", \"updated_at\": \"2026-05-24T22:13:15.428Z\", \"hypothesis\": \"Random 31.48% subset with multi-epoch training should produce PPL between uniform full-data baseline and D&R filtered multi-epoch, because data filtering quality matters more than simply repeating data multiple epochs\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/random_subset_seed42.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/random_subset_epoch_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --max_steps 6103 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_total_limit 2 --save_only_model --logging_steps 10 --eval_steps 500 --save_steps 500\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"data_path\": \"data/random_subset_seed42.jsonl\", \"data_count\": 116935, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-24T22:00:13.455Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T22:00:17.241Z\", \"notes\": \"holdout_ppl=17.694, owt_ppl=18.349, wiki_ppl=15.317, Δ≈-0.005 vs uniform (17.699)，无显著差异——random subset multi-epoch ≈ uniform single-epoch，确认 epoch 效应中性。Cron 误判为 failed（M066，第二次），训练实际完成 6103/6103 steps。\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T22:00:22.253102+00:00\"}]}, \"metrics\": {\"holdout_ppl\": 17.694, \"owt_ppl\": 18.349, \"wiki_ppl\": 15.317}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/random_subset_epoch_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/random_subset_epoch_seed42/step_metrics.jsonl\"}, \"contamination_20_tau07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:52:04.527Z\", \"updated_at\": \"2026-05-24T21:15:44.342Z\", \"hypothesis\": \"ρ=0.2 + τ=0.7: previous ρ=0.2 + τ=0.8 was negative (+0.046). Testing whether lower τ=0.7 is more appropriate at low contamination where natural α_eff is high. If still negative, confirms ρ=0.2 is below the method's effective range regardless of τ.\", \"parent\": \"rho02_adaptive_tau08_seed42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u training/pretrain_weighted.py --data_path data/scored_data_rho02.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_20_tau07_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 2 --num_train_tokens 200000000 --contamination_ratio 0.2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 42 --bf16 --save_total_limit 2 --logging_steps 10\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"data_path\": \"data/scored_data_rho02.jsonl\", \"data_count\": 206111, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/contamination_20_tau07_seed42\", \"log_path\": \"~/runs/provenance_weight_training/contamination_20_tau07_seed42.log\", \"hyperparams\": {\"weighting_method\": \"adaptive\", \"tau\": 0.7, \"n_min\": 2, \"contamination_ratio\": 0.2, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": 5e-05}, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment, not eval)\"}, \"conclusion\": \"negative\", \"metrics\": {\"holdout_ppl\": 17.35, \"holdout_loss\": 2.853, \"owt_ppl\": 18.06, \"owt_loss\": 2.893, \"wiki_ppl\": 15.11, \"wiki_loss\": 2.715}, \"notes\": \"ρ=0.2 + τ=0.7: holdout_ppl=17.35 (Δ=+0.014 vs uniform 17.336). 比 τ=0.8 的 Δ=+0.046 好 70%，但仍略差于 uniform。确认 ρ=0.2 接近方法有效范围下限，τ=0.7 减少过度干预但不足以逆转。结果可补入 appendix。\"}, \"permuted_score_control_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T16:02:17.992Z\", \"updated_at\": \"2026-05-24T20:59:36.176Z\", \"hypothesis\": \"Permuted q-scores (random assignment of real scores to samples) should degrade vs uniform, confirming that the detector's provenance signal is load-bearing for adaptive weighting — not merely the non-uniformity of weights.\", \"reproduce\": {\"finished_at\": \"2026-05-24T20:52:47.395Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-24T16:43:05.828Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T16:43:14.298708+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T20:52:56.202366+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u training/pretrain_weighted.py --data_path data/scored_data_random_shuffle.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/permuted_score_control_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 2 --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 42 --bf16 --save_total_limit 2 --logging_steps 10\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data_random_shuffle.jsonl\", \"data_count\": null, \"model_name\": \"models/Qwen/Qwen3-0.6B\", \"seed\": 42, \"pid\": 966241, \"gpu\": \"cuda:3\", \"retry_count\": 2, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/permuted_score_control_seed42\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/permuted_score_control_seed42/train.log\", \"train_loss\": 8.033, \"train_runtime_sec\": 13540, \"train_samples_per_second\": 7.212, \"train_steps_per_second\": 0.451, \"max_steps_reached\": 6103, \"epoch\": 0.2629, \"final_learning_rate\": 2.07e-07}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/permuted_score_control_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/permuted_score_control_seed42/train.log\", \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.919, \"holdout_loss\": 2.886, \"holdout_tokens\": 5004058, \"owt_ppl\": 18.046, \"owt_loss\": 2.893, \"owt_tokens\": 5000859, \"wiki_ppl\": 14.891, \"wiki_loss\": 2.701, \"wiki_tokens\": 5009907}, \"notes\": \"Cron 误判为 failed（无 W&B sentinel），实际训练完成 6103/6103 steps。Reclassified as success: permuted scores holdout_ppl=17.919 vs uniform~17.694 (Δ=+0.225 degradation), confirms detector signal is load-bearing. train_loss=8.033 高但符合预期（随机分配的 scores 导致 weighted loss 不稳定，但 unweighted eval 指标正常）。\"}, \"p0_nmin_5\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T16:01:10.072Z\", \"updated_at\": \"2026-05-24T17:11:14.799Z\", \"hypothesis\": \"n_min sensitivity: n_min=5 (>B/2=2) over-constrains ESS floor, forcing b* toward 0 more often. Expected to degrade toward uniform PPL (~17.694). Completes n_min sensitivity curve: n_min=1 (+0.048), n_min=2 (−0.020, optimal), n_min=4 (recovers uniform), n_min=5 (this experiment).\", \"reproduce\": {\"finished_at\": \"2026-05-24T16:42:23.767Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-24T16:42:22.464Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T16:42:31.288480+00:00\"}], \"previous_failure\": {\"conclusion\": \"negative\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/p0_nmin_5 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 5 --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 42 --bf16 --save_total_limit 2 --logging_steps 10\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": null, \"model_name\": \"models/Qwen/Qwen3-0.6B\", \"seed\": 42, \"pid\": 966103, \"gpu\": \"cuda:1\", \"retry_count\": 2, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/p0_nmin_5\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/p0_nmin_5/train.log\"}, \"conclusion\": \"negative\", \"notes\": \"n_min≥B forces b*=0, degenerates to uniform; killed by disk full at step 80, not worth rerunning. Analytically confirmed: n_min=5 > B=4 makes ESS constraint impossible to satisfy for any b>0, so b*≡0 (uniform weights).\"}, \"p0_batchsize_16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T15:56:36.323Z\", \"updated_at\": \"2026-05-24T16:22:23.171Z\", \"hypothesis\": \"Batch size amplification at B=16: adaptive τ=0.7 with n_min=8 (auto-compute: 16//2=8). Validates n_min coupling rule at B=16 and completes batch-size amplification series (B=4→8→16). Expected Δ≈-0.068 based on monotonic amplification trend from B=4 (Δ=-0.020) and B=8 (Δ=-0.052).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/p0_batchsize_16 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 8 --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 16 --gradient_accumulation_steps 1 --learning_rate 5e-5 --seed 42 --bf16 --save_total_limit 2 --logging_steps 10\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\", \"hyperparams\": {\"weighting_method\": \"adaptive\", \"tau\": 0.7, \"n_min\": 8, \"batch_size\": 16, \"gradient_accumulation_steps\": 1, \"effective_batch_size\": 16, \"lr\": 5e-05, \"contamination_ratio\": 0.4}, \"failure_reason\": \"OOM: 18.55 GiB logits tensor, B=16 grad_accum=1 exceeds GPU memory\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-24T16:22:23.171Z\"}, \"adaptive_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T04:42:39.014Z\", \"updated_at\": \"2026-05-24T09:06:09.955Z\", \"hypothesis\": \"N=5 seed replication (seed=789): adaptive provenance weighting with τ=0.7, n_min=2, B=4 on ρ=0.4 data. Fourth seed to strengthen paired t-test statistical power for B=4 Δ significance.\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_seed789 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 2 --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 789 --bf16 --save_total_limit 2 --logging_steps 10\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 922510, \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed789.log\", \"submitted_at\": \"2026-05-24T04:42:54.988Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 789, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_seed789\", \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.4, \"tau\": 0.7, \"n_min\": 2, \"num_train_tokens\": 200000000, \"max_steps\": 6103, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"save_total_limit\": 2}, \"wall_clock_seconds\": 13925.8, \"gpu_hours\": 3.87}, \"reproduce\": {\"finished_at\": \"2026-05-24T08:31:07.184Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T08:31:13.649238+00:00\"}]}, \"metrics\": {\"holdout_ppl\": 17.668, \"owt_ppl\": 18.365, \"wiki_ppl\": 15.33, \"train_loss\": 9.65, \"train_duration_s\": 13570}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T08:35:00.800Z\"}, \"adaptive_seed234\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T04:42:41.978Z\", \"updated_at\": \"2026-05-24T09:06:08.809Z\", \"hypothesis\": \"N=5 seed replication (seed=234): adaptive provenance weighting with τ=0.7, n_min=2, B=4 on ρ=0.4 data. Fifth seed to complete N=5 paired t-test for B=4 Δ significance.\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_seed234 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 2 --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 234 --bf16 --save_total_limit 2 --logging_steps 10\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": 922738, \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed234.log\", \"submitted_at\": \"2026-05-24T04:43:00.381Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 234, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_seed234\", \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.4, \"tau\": 0.7, \"n_min\": 2, \"num_train_tokens\": 200000000, \"max_steps\": 6103, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"save_total_limit\": 2}, \"wall_clock_seconds\": 13917.9, \"gpu_hours\": 3.87}, \"reproduce\": {\"finished_at\": \"2026-05-24T08:31:23.754Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T08:31:32.096109+00:00\"}]}, \"metrics\": {\"holdout_ppl\": 17.678, \"owt_ppl\": 18.34, \"wiki_ppl\": 15.341, \"train_loss\": 9.695, \"train_duration_s\": 13540}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T08:34:58.273Z\"}, \"uniform_seed234\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T04:42:43.151Z\", \"updated_at\": \"2026-05-24T08:44:03.476Z\", \"hypothesis\": \"N=5 seed replication (seed=234): uniform weighting baseline on ρ=0.4 data. Fifth seed paired with adaptive_seed234 for Δ calculation.\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_seed234 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 234 --bf16 --save_total_limit 2 --logging_steps 10\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"pid\": 923155, \"log_path\": \"~/runs/provenance_weight_training/uniform_seed234.log\", \"submitted_at\": \"2026-05-24T04:43:04.505Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 234, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/uniform_seed234\", \"hyperparams\": {\"weighting_method\": \"uniform\", \"contamination_ratio\": 0.4, \"num_train_tokens\": 200000000, \"max_steps\": 6103, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"save_total_limit\": 2}, \"wall_clock_seconds\": 13533.1, \"gpu_hours\": 3.76}, \"reproduce\": {\"finished_at\": \"2026-05-24T08:19:51.651Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T08:20:05.021154+00:00\"}]}, \"metrics\": {\"holdout_ppl\": 17.708, \"holdout_loss\": 2.874, \"owt_ppl\": 18.355, \"wiki_ppl\": 15.352, \"train_loss\": 8.008, \"train_duration_s\": 12780}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T08:28:37.605Z\"}, \"uniform_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T04:42:40.614Z\", \"updated_at\": \"2026-05-24T08:44:02.005Z\", \"hypothesis\": \"N=5 seed replication (seed=789): uniform weighting baseline on ρ=0.4 data. Fourth seed paired with adaptive_seed789 for Δ calculation.\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_seed789 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 789 --bf16 --save_total_limit 2 --logging_steps 10\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": 922589, \"log_path\": \"~/runs/provenance_weight_training/uniform_seed789.log\", \"submitted_at\": \"2026-05-24T04:42:57.790Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 789, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/uniform_seed789\", \"hyperparams\": {\"weighting_method\": \"uniform\", \"contamination_ratio\": 0.4, \"num_train_tokens\": 200000000, \"max_steps\": 6103, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"save_total_limit\": 2}, \"wall_clock_seconds\": 13535.4, \"gpu_hours\": 3.76}, \"reproduce\": {\"finished_at\": \"2026-05-24T08:19:16.269Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T08:19:22.467092+00:00\"}]}, \"metrics\": {\"holdout_ppl\": 17.695, \"holdout_loss\": 2.8733, \"owt_ppl\": 18.387, \"wiki_ppl\": 15.349, \"train_loss\": 7.959, \"train_duration_s\": 12790}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T08:28:33.161Z\"}, \"aeff_only_nmin1_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:41:16.042Z\", \"updated_at\": \"2026-05-24T01:50:47.441Z\", \"hypothesis\": \"α_eff-only ablation seed456: cross-seed replicate. n_min=1 removes ESS constraint. Third seed for paired t-test vs dual-constrained baseline.\", \"spec\": {\"gpu\": \"cuda:1\", \"server\": \"westd-41312\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/aeff_only_nmin1_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 1 --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 456 --bf16 --save_total_limit 2\\\"\", \"pid\": 893568, \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/aeff_only_nmin1_seed456.log\", \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.4, \"tau\": 0.7, \"n_min\": 1, \"num_train_tokens\": 200000000, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"save_total_limit\": 2}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/aeff_only_nmin1_seed456/final\"}, \"metrics\": {\"holdout_ppl\": 17.744, \"holdout_loss\": 2.8761}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:50:47.441Z\"}, \"bs8_nmin4_adaptive_seed456_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T12:49:48.326Z\", \"updated_at\": \"2026-05-23T23:11:36.489Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 4 --num_train_tokens 200000000 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 2 --gradient_checkpointing\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"pid\": 872464, \"gpu\": \"cuda:0\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed456\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin4_adaptive_seed456_r2.log\", \"note\": \"重启 r2: 原实验 contamination_ratio 配置错误，使用 rho=0.4 数据重跑\"}, \"hypothesis\": \"B=8 第三 seed 补全 3-seed paired comparison。seed42 Δ=−0.044, seed123 Δ=−0.056。预期 Δ∈[−0.040, −0.060]。3-seed 均值将提供 batch-size amplification (B=4→B=8→B=16) 的完整统计支撑。\", \"metrics\": {\"holdout_ppl\": 17.646, \"holdout_loss\": 2.8705, \"owt_ppl\": 18.322, \"wiki_ppl\": 15.299}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T22:42:34.159Z\"}, \"bs8_nmin4_uniform_seed456_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T12:49:50.668Z\", \"updated_at\": \"2026-05-23T23:09:57.578Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 200000000 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 2 --gradient_checkpointing\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"pid\": 872861, \"gpu\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed456\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin4_uniform_seed456_r2.log\", \"note\": \"重启 r2: 原实验 contamination_ratio 配置错误，使用 rho=0.4 数据重跑\"}, \"hypothesis\": \"seed456 uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed456. Completes 3-seed set for batch-size amplification statistical analysis.\", \"metrics\": {\"holdout_ppl\": 17.702, \"holdout_loss\": 2.8737, \"owt_ppl\": 18.393, \"wiki_ppl\": 15.354}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T22:42:36.457Z\"}, \"aeff_only_nmin1_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:41:13.680Z\", \"updated_at\": \"2026-05-23T20:14:39.454Z\", \"hypothesis\": \"α_eff-only ablation seed123: cross-seed replicate of aeff_only_nmin1_seed42. n_min=1 removes ESS constraint, isolating α_eff signal contribution.\", \"spec\": {\"gpu\": \"cuda:3\", \"server\": \"westd-41312\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/aeff_only_nmin1_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 1 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 123 --bf16 --save_total_limit 2\\\"\", \"pid\": 875597, \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.4, \"tau\": 0.7, \"n_min\": 1, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"save_total_limit\": 2}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/aeff_only_nmin1_seed123/checkpoint-6103\", \"log_path\": \"~/runs/provenance_weight_training/aeff_only_nmin1_seed123.log\"}, \"metrics\": {\"holdout_ppl\": 17.733, \"holdout_loss\": 2.8755}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T20:11:18.697Z\"}, \"aeff_only_nmin1_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:41:10.968Z\", \"updated_at\": \"2026-05-23T20:11:10.688Z\", \"hypothesis\": \"α_eff-only ablation: adaptive reweighting with n_min=1 (ESS≥1 always satisfied, only α_eff≤τ active). If PPL worse than dual-constrained (n_min=2, 17.674±0.007), ESS constraint has independent value beyond α_eff signal. Addresses R11-C2 + R12-W1.\", \"spec\": {\"gpu\": \"cuda:1\", \"server\": \"westd-41312\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/aeff_only_nmin1_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 1 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --seed 42 --bf16 --save_total_limit 2\\\"\", \"pid\": 875527, \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.4, \"tau\": 0.7, \"n_min\": 1, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"save_total_limit\": 2}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/aeff_only_nmin1_seed42/checkpoint-6103\", \"log_path\": \"~/runs/provenance_weight_training/aeff_only_nmin1_seed42.log\"}, \"metrics\": {\"holdout_ppl\": 17.75, \"holdout_loss\": 2.8763}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T20:11:10.688Z\"}, \"bs8_nmin4_uniform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T12:40:18.458Z\", \"updated_at\": \"2026-05-23T13:26:34.576Z\", \"hypothesis\": \"seed456 uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed456. Completes 3-seed set for batch-size amplification statistical analysis.\", \"parent\": \"\", \"spec\": {\"gpu\": \"cuda:2\", \"server\": \"westd-41312\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --seed 456 --bf16 --save_total_limit 2\\\"\", \"pid\": 871842, \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"hyperparams\": {\"weighting_method\": \"uniform\", \"contamination_ratio\": 0.4, \"batch_size\": 8, \"gradient_accumulation_steps\": 2, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"save_total_limit\": 2}}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-23T13:26:34.576Z\"}, \"bs8_nmin4_adaptive_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T12:40:14.696Z\", \"updated_at\": \"2026-05-23T13:26:32.270Z\", \"hypothesis\": \"B=8 第三 seed 补全 3-seed paired comparison。seed42 Δ=−0.044, seed123 Δ=−0.056。预期 Δ∈[−0.040, −0.060]。3-seed 均值将提供 batch-size amplification (B=4→B=8→B=16) 的完整统计支撑。\", \"parent\": \"\", \"spec\": {\"gpu\": \"cuda:0\", \"server\": \"westd-41312\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 4 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --seed 456 --bf16 --save_total_limit 2\\\"\", \"pid\": 871448, \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.4, \"tau\": 0.7, \"batch_size\": 8, \"gradient_accumulation_steps\": 2, \"effective_batch_size\": 16, \"n_min\": 4, \"lr\": \"5e-5\", \"save_total_limit\": 2}}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-23T13:26:32.270Z\"}, \"bs8_nmin4_uniform_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:24:23.816Z\", \"updated_at\": \"2026-05-23T08:51:36.835Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir .../bs8_nmin4_uniform_seed123 --model_name Qwen3-0.6B --weighting_method uniform --batch_size 8 --gradient_accumulation_steps 2 --lr 5e-5 --seed 123 --bf16 --save_total_limit 2 --resume_from_checkpoint checkpoint-500\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"pid\": 835333, \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin4_uniform_seed123_r2.log\", \"submitted_at\": \"2026-05-23T03:25:06.274Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"hyperparams\": {\"weighting_method\": \"uniform\", \"contamination_ratio\": 0.4, \"batch_size\": 8, \"gradient_accumulation_steps\": 2, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"scheduler\": \"linear\", \"max_length\": 2048, \"num_train_tokens\": 200000000, \"max_steps\": 6103, \"save_total_limit\": 2, \"resumed_from\": \"checkpoint-500\"}, \"wall_clock_seconds\": 19590.6, \"gpu_hours\": 5.44}, \"hypothesis\": \"Cross-seed replicate (seed=123) uniform baseline at B=8. Retry from checkpoint-500 after disk-full crash. Provides second data point for B=8 batch-size amplification.\", \"metrics\": {\"eval_ppl_holdout\": 17.687, \"eval_ppl_owt\": 18.37, \"eval_ppl_wiki\": 15.385}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:51:36.835Z\"}, \"bs8_nmin4_adaptive_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:24:19.527Z\", \"updated_at\": \"2026-05-23T08:51:34.609Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir .../bs8_nmin4_adaptive_seed123 --model_name Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 4 --batch_size 8 --gradient_accumulation_steps 2 --lr 5e-5 --seed 123 --bf16 --save_total_limit 2 --resume_from_checkpoint checkpoint-500\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": 835240, \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin4_adaptive_seed123_r2.log\", \"submitted_at\": \"2026-05-23T03:25:03.062Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.4, \"tau\": 0.7, \"batch_size\": 8, \"gradient_accumulation_steps\": 2, \"effective_batch_size\": 16, \"n_min\": 4, \"lr\": \"5e-5\", \"scheduler\": \"linear\", \"max_length\": 2048, \"num_train_tokens\": 200000000, \"max_steps\": 6103, \"save_total_limit\": 2, \"resumed_from\": \"checkpoint-500\"}, \"wall_clock_seconds\": 19591.5, \"gpu_hours\": 5.44}, \"hypothesis\": \"Cross-seed replicate (seed=123) of bs8_nmin4_adaptive_seed42 (Δ=−0.044). Retry from checkpoint-500 after disk-full crash. B=8 n_min=4 adaptive should show consistent negative Δ vs uniform.\", \"metrics\": {\"eval_ppl_holdout\": 17.631, \"eval_ppl_owt\": 18.338, \"eval_ppl_wiki\": 15.353}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:51:34.609Z\"}, \"rho03_adaptive_seed456_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:23:15.525Z\", \"updated_at\": \"2026-05-23T08:51:32.331Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir .../rho03_adaptive_seed456_r2 --model_name Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.3 --tau 0.7 --batch_size 4 --gradient_accumulation_steps 4 --lr 5e-5 --seed 456 --bf16 --save_total_limit 2\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 834745, \"log_path\": \"~/runs/provenance_weight_training/rho03_adaptive_seed456_r2.log\", \"submitted_at\": \"2026-05-23T03:23:46.396Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_rho03.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.3, \"tau\": 0.7, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"n_min\": 2, \"lr\": \"5e-5\", \"scheduler\": \"linear\", \"max_length\": 2048, \"num_train_tokens\": 200000000, \"max_steps\": 6103, \"save_total_limit\": 2}, \"wall_clock_seconds\": 19665.9, \"gpu_hours\": 5.46}, \"hypothesis\": \"Third seed (456) for ρ=0.3 boundary check (retry, from scratch after disk-full crash). With seed42 Δ=0.000 and seed123 Δ=+0.002 on holdout, seed456 should confirm ρ=0.3 as neutral transition zone.\", \"metrics\": {\"eval_ppl_holdout\": 17.424, \"eval_ppl_owt\": 18.115, \"eval_ppl_wiki\": 15.161}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/rho03_adaptive_seed456_r2/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:51:32.331Z\"}, \"rho03_uniform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:04:02.959Z\", \"updated_at\": \"2026-05-23T07:04:54.839Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/rho03_uniform_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.3 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/rho03_uniform_seed456/checkpoint-1000\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"833051\", \"log_path\": \"~/runs/provenance_weight_training/rho03_uniform_seed456.log\", \"submitted_at\": \"2026-05-23T03:19:08.210Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13490.1, \"gpu_hours\": 3.75}, \"hypothesis\": \"Third seed (456) uniform baseline at ρ=0.3 for paired comparison with rho03_adaptive_seed456. Completes 3-seed set for paired t-test at the boundary contamination ratio.\", \"reproduce\": {\"finished_at\": \"2026-05-23T06:48:09.472Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T06:48:15.272349+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.419, \"eval_ppl_owt\": 18.109, \"eval_ppl_wiki\": 15.168}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/rho03_uniform_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/rho03_uniform_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T07:03:58.335Z\"}, \"rho03_adaptive_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:04:00.701Z\", \"updated_at\": \"2026-05-23T03:24:17.322Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/rho03_adaptive_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.3 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/rho03_adaptive_seed456/checkpoint-1000\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"832974\", \"log_path\": \"~/runs/provenance_weight_training/rho03_adaptive_seed456.log\", \"submitted_at\": \"2026-05-23T03:19:05.498Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 164.1, \"gpu_hours\": 0.05}, \"hypothesis\": \"Third seed (456) for ρ=0.3 boundary check. With seed42 Δ=0.000 and seed123 Δ=+0.002 on holdout, seed456 should confirm ρ=0.3 as neutral transition zone (Δ ≈ 0), enabling paired t-test (N=3) to formally establish non-significance at the boundary.\", \"reproduce\": {\"finished_at\": \"2026-05-23T03:21:43.508Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T03:21:49.561Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-23T03:21:55.579981+00:00\"}]}, \"notes\": \"失败原因: FileNotFoundError — checkpoint-1000/trainer_state.json 不存在，resume_from_checkpoint 失败 | 类型: infrastructure | fix_worker_id: worker_diagnose_rho03_adaptive_seed456_20260523T032401 | 自动修复中\"}, \"batchsize16_nmin8_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:17:10.215Z\", \"updated_at\": \"2026-05-23T03:23:40.397Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/provenance_weight_training && bash scripts/run_bs16_nmin8_r2.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"48881\", \"log_path\": \"~/runs/provenance_weight_training/batchsize16_nmin8_r2.log\", \"submitted_at\": \"2026-05-17T19:32:48.742Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 324648.2, \"gpu_hours\": 90.18}, \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T11:44:39.058Z\"}, \"eval_uniform_1_7b_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:06:38.917Z\", \"updated_at\": \"2026-05-23T03:23:12.618Z\", \"spec\": {\"command\": \"eval_perplexity.py on uniform_1_7b_seed42_resumed/final\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"241549\", \"log_path\": \"~/runs/provenance_weight_training/eval_uniform_1_7b_v3.log\", \"submitted_at\": \"2026-05-18T19:06:38.561Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"Qwen3-1.7B (uniform)\", \"seed\": 42, \"checkpoint_source\": \"uniform_1_7b_seed42_resumed\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42_resumed/final\", \"wall_clock_seconds\": 11071.3, \"gpu_hours\": 3.08}, \"metrics\": {\"eval_ppl_holdout\": 13.5}, \"conclusion\": \"success\", \"hypothesis\": \"Eval uniform_1_7b_seed42_resumed on holdout: baseline PPL for 1.7B uniform training. Paired with eval_adaptive_1_7b_v2 to measure adaptive vs uniform gap at larger scale.\", \"completed_at\": \"2026-05-18T22:11:09.846Z\"}, \"eval_adaptive_1_7b_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:06:41.217Z\", \"updated_at\": \"2026-05-23T03:23:09.813Z\", \"spec\": {\"command\": \"eval_perplexity.py on adaptive_1_7b_seed42/final\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"241628\", \"log_path\": \"~/runs/provenance_weight_training/eval_adaptive_1_7b_v2.log\", \"submitted_at\": \"2026-05-18T19:06:40.866Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"Qwen3-1.7B (adaptive)\", \"seed\": 42, \"checkpoint_source\": \"adaptive_1_7b_seed42\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/final\", \"wall_clock_seconds\": 11067.4, \"gpu_hours\": 3.07}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 13.27}, \"hypothesis\": \"Eval adaptive_1_7b_seed42 on holdout: if adaptive PPL < uniform PPL at 1.7B scale, the provenance weighting advantage persists with larger models, not just 0.6B.\", \"completed_at\": \"2026-05-18T22:11:08.245Z\"}, \"bs8_nmin4_uniform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:08:21.983Z\", \"updated_at\": \"2026-05-23T03:23:04.956Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed123/checkpoint-1000\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"833558\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin4_uniform_seed123.log\", \"submitted_at\": \"2026-05-23T03:19:17.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 195.3, \"gpu_hours\": 0.05}, \"hypothesis\": \"Cross-seed replicate (seed=123) uniform baseline at B=8 for paired comparison with bs8_nmin4_adaptive_seed123. Provides second data point for B=8 batch-size amplification.\", \"reproduce\": {\"finished_at\": \"2026-05-23T03:22:28.059Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T03:22:32.518Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-23T03:22:44.697596+00:00\"}]}}, \"bs8_nmin4_adaptive_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:08:19.280Z\", \"updated_at\": \"2026-05-23T03:23:03.743Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --n_min 4 --num_train_tokens 200000000 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed123/checkpoint-1000\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"833474\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin4_adaptive_seed123.log\", \"submitted_at\": \"2026-05-23T03:19:14.537Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 179.8, \"gpu_hours\": 0.05}, \"hypothesis\": \"Cross-seed replicate (seed=123) of bs8_nmin4_adaptive_seed42 (Δ=−0.044). B=8 n_min=4 adaptive should show consistent negative Δ vs uniform, strengthening batch-size amplification evidence (B=4 Δ=−0.020, B=8 Δ=−0.044, B=16 Δ=−0.068).\", \"reproduce\": {\"finished_at\": \"2026-05-23T03:22:07.156Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T03:22:14.307Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-23T03:22:20.183110+00:00\"}]}}, \"rho03_uniform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:58:34.743Z\", \"updated_at\": \"2026-05-23T00:24:24.189Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir .../rho03_uniform_seed123 --model_name Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.3 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --seed 123 --bf16 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"pid\": 805963, \"log_path\": \"~/runs/provenance_weight_training/rho03_uniform_seed123.log\", \"submitted_at\": \"2026-05-22T18:59:03.235Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_rho03.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"hyperparams\": {\"weighting_method\": \"uniform\", \"contamination_ratio\": 0.3, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"scheduler\": \"linear\", \"max_length\": 2048, \"num_train_tokens\": 200000000, \"max_steps\": 6103}, \"wall_clock_seconds\": 19521.0, \"gpu_hours\": 5.42}, \"metrics\": {\"eval_ppl_holdout\": 17.433, \"eval_ppl_owt\": 18.126, \"eval_ppl_wiki\": 15.204}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/rho03_uniform_seed123/final\", \"conclusion\": \"success\", \"hypothesis\": \"Cross-seed replicate (seed=123) uniform baseline at ρ=0.3 for paired comparison with rho03_adaptive_seed123. Provides second data point for measuring adaptive Δ at the boundary contamination ratio.\", \"completed_at\": \"2026-05-23T00:24:24.189Z\"}, \"rho03_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:55:51.970Z\", \"updated_at\": \"2026-05-23T00:24:21.897Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir .../rho03_uniform_seed42 --model_name Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.3 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --seed 42 --bf16 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": 805117, \"log_path\": \"~/runs/provenance_weight_training/rho03_uniform_seed42.log\", \"submitted_at\": \"2026-05-22T18:56:37.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_rho03.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"hyperparams\": {\"weighting_method\": \"uniform\", \"contamination_ratio\": 0.3, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"lr\": \"5e-5\", \"scheduler\": \"linear\", \"max_length\": 2048, \"num_train_tokens\": 200000000, \"max_steps\": 6103}, \"wall_clock_seconds\": 19664.4, \"gpu_hours\": 5.46}, \"metrics\": {\"eval_ppl_holdout\": 17.422, \"eval_ppl_owt\": 18.113, \"eval_ppl_wiki\": 15.204}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/rho03_uniform_seed42/final\", \"conclusion\": \"success\", \"hypothesis\": \"Uniform baseline at ρ=0.3 for paired comparison with rho03_adaptive_seed42. Expected PPL between ρ=0.2 uniform (17.336) and ρ=0.4 uniform (17.694), providing the control condition to measure adaptive Δ at the boundary contamination ratio.\", \"completed_at\": \"2026-05-23T00:24:21.897Z\"}, \"rho03_adaptive_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:58:32.055Z\", \"updated_at\": \"2026-05-23T00:24:19.490Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir .../rho03_adaptive_seed123 --model_name Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.3 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --seed 123 --bf16 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": 805886, \"log_path\": \"~/runs/provenance_weight_training/rho03_adaptive_seed123.log\", \"submitted_at\": \"2026-05-22T18:59:00.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_rho03.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.3, \"tau\": 0.7, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"n_min\": 2, \"lr\": \"5e-5\", \"scheduler\": \"linear\", \"max_length\": 2048, \"num_train_tokens\": 200000000, \"max_steps\": 6103}, \"wall_clock_seconds\": 19518.7, \"gpu_hours\": 5.42}, \"metrics\": {\"eval_ppl_holdout\": 17.435, \"eval_ppl_owt\": 18.148, \"eval_ppl_wiki\": 15.165}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/rho03_adaptive_seed123/final\", \"conclusion\": \"success\", \"hypothesis\": \"Cross-seed replicate (seed=123) of rho03_adaptive_seed42. At ρ=0.3 boundary, adaptive τ=0.7 should show consistent Δ vs uniform across seeds, establishing statistical reliability of the boundary effect.\", \"completed_at\": \"2026-05-23T00:24:19.490Z\"}, \"rho03_adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:55:48.966Z\", \"updated_at\": \"2026-05-23T00:24:17.220Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_rho03.jsonl --output_dir .../rho03_adaptive_seed42 --model_name Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.3 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --seed 42 --bf16 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 805034, \"log_path\": \"~/runs/provenance_weight_training/rho03_adaptive_seed42.log\", \"submitted_at\": \"2026-05-22T18:56:35.094Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_rho03.jsonl\", \"data_count\": 235555, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"hyperparams\": {\"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.3, \"tau\": 0.7, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"effective_batch_size\": 16, \"n_min\": 2, \"lr\": \"5e-5\", \"scheduler\": \"linear\", \"max_length\": 2048, \"num_train_tokens\": 200000000, \"max_steps\": 6103}, \"wall_clock_seconds\": 19662.1, \"gpu_hours\": 5.46}, \"metrics\": {\"eval_ppl_holdout\": 17.422, \"eval_ppl_owt\": 18.123, \"eval_ppl_wiki\": 15.172}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/rho03_adaptive_seed42/final\", \"conclusion\": \"success\", \"hypothesis\": \"At ρ=0.3 (boundary between ρ=0.2 fail and ρ=0.4 success), adaptive τ=0.7 weighting should still improve over uniform but with smaller Δ than ρ=0.4 (Δ=−0.068). This tests the contamination threshold where detect-and-reweight becomes effective, establishing the method's sensitivity boundary.\", \"completed_at\": \"2026-05-23T00:24:17.220Z\"}, \"random_reweight_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T17:55:01.850Z\", \"updated_at\": \"2026-05-22T18:58:28.114Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method random --contamination_ratio 0.4 --tau 0.8 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed456/checkpoint-1000\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"136144\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed456.log\", \"submitted_at\": \"2026-05-17T21:30:09.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 317580.3, \"gpu_hours\": 88.22}, \"hypothesis\": \"U(0,2) random weights baseline seed=456: third seed for Claim 1 random degradation evidence. Random weights drawn from U(0,2) should degrade PPL vs uniform and adaptive, consistent with seed42 and seed123 results, confirming detector q-scores provide real data quality signal beyond random noise.\", \"parent\": \"random_reweight_seed123_r5\", \"reproduce\": {\"finished_at\": \"2026-05-17T21:11:42.187Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T21:11:43.582Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T21:11:46.851773+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.777, \"eval_loss_holdout\": 2.8779, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 6.657, \"train_runtime_seconds\": 10739}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed456/final\"}, \"bs8_nmin4_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:29:06.990Z\", \"updated_at\": \"2026-05-22T16:46:39.834Z\", \"hypothesis\": \"Batch-size sensitivity B=8 uniform baseline: uniform weighting with effective batch=16 (bs=8 × grad_accum=2). Paired with bs8_nmin4_adaptive_seed42 to measure Δ(adaptive−uniform) at B=8. Expected: B=4 Δ=−0.020, B=8 Δ should be intermediate, B=16 Δ=−0.068. Monotonic trend confirms batch-size amplification mechanism.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --max_steps 6103 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": 764807, \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin4_uniform_seed42.log\", \"submitted_at\": \"2026-05-22T11:29:28.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 17194.8, \"gpu_hours\": 4.78}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_uniform_seed42/final\", \"metrics\": {\"holdout_ppl\": 17.694185837410274, \"owt_ppl\": 18.363068741825792, \"wiki_ppl\": 15.336710587451519, \"holdout_loss\": 2.8732361018550434, \"owt_loss\": 2.910341514026512, \"wiki_loss\": 2.730249339271619}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:16:03.756Z\"}, \"bs8_nmin4_adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:48:54.953Z\", \"updated_at\": \"2026-05-22T16:46:38.748Z\", \"hypothesis\": \"Batch-size sensitivity B=8: adaptive reweighting with tau=0.7, n_min=4 (⌊B/2⌋), effective batch=16 (bs=8 × grad_accum=2). Tests whether adaptive advantage scales monotonically with batch size: B=4 Δ=−0.020, B=16 Δ=−0.068. B=8 should fall between, confirming batch-size amplification mechanism. Paired with bs8_nmin4_uniform_seed42.\", \"spec\": {\"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"from_scratch\", \"eval_data\": [\"holdout_combined\", \"owt_eval\", \"wiki_eval\"], \"hyperparams\": {\"batch_size\": 8, \"gradient_accumulation_steps\": 2, \"effective_batch\": 16, \"lr\": \"5e-5\", \"lr_scheduler\": \"linear\", \"max_steps\": 6103, \"tau\": 0.7, \"n_min\": 4, \"weighting_method\": \"adaptive\", \"contamination_ratio\": 0.4}, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --n_min 4 --max_steps 6103 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 757990}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs8_nmin4_adaptive_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin4_adaptive_seed42.log\", \"metrics\": {\"holdout_ppl\": 17.650425404986372, \"owt_ppl\": 18.332103963757113, \"wiki_ppl\": 15.318017946105257, \"holdout_loss\": 2.8707598853543677, \"owt_loss\": 2.908653837793633, \"wiki_loss\": 2.729029779056454}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:16:01.573Z\"}, \"detect_remove_q05_v2_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:09:58.143Z\", \"updated_at\": \"2026-05-22T14:29:36.228Z\", \"hypothesis\": \"D&R hard filtering (remove q≤0.5 samples) with seed 456 should produce holdout PPL consistent with seed42 and seed123, confirming the stability of the filtering approach across random seeds.\", \"parent\": \"detect_remove_q05_v2_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=2 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": 742953, \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q05_v2_seed456.log\", \"submitted_at\": \"2026-05-22T09:10:09.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": [\"holdout_combined\", \"owt_eval\", \"wiki_eval\"], \"wall_clock_seconds\": 16469.8, \"gpu_hours\": 4.57}, \"reproduce\": {\"finished_at\": \"2026-05-22T13:20:27.607Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T13:20:37.624112+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.277, \"holdout_loss\": 2.8493, \"owt_ppl\": 18.017, \"owt_loss\": 2.8913, \"wiki_ppl\": 15.04, \"wiki_loss\": 2.7106, \"train_loss\": 11.01, \"total_steps\": 6103, \"training_time_s\": 14920}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q05_v2_seed456.log\", \"completed_at\": \"2026-05-22T13:44:39.347Z\"}, \"random_reweight_v2_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:32:33.573Z\", \"updated_at\": \"2026-05-22T13:43:27.483Z\", \"hypothesis\": \"Random reweight seed456 v2: uses scored_data_random_shuffle.jsonl + adaptive weighting (matching seed42/seed123 config). Third seed for detector signal load-bearing test. Paired with random_reweight_baseline_seed42 (17.958) and random_reweight_seed123 (17.945).\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_random_shuffle.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/random_reweight_v2_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": 699452, \"log_path\": \"~/runs/provenance_weight_training/random_reweight_v2_seed456.log\", \"data_path\": \"data/scored_data_random_shuffle.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": [\"holdout_combined\", \"owt_eval\", \"wiki_eval\"]}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/random_reweight_v2_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_v2_seed456.log\", \"metrics\": {\"holdout_ppl\": 17.951, \"owt_ppl\": 18.602, \"wiki_ppl\": 15.503}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T13:43:27.483Z\"}, \"uniform_epoch_matched_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:42:58.560Z\", \"updated_at\": \"2026-05-22T11:27:52.856Z\", \"hypothesis\": \"Uniform epoch-matched seed456: trains on full data (scored_data.jsonl, 371499 samples) for 2533 steps with independent linear LR schedule (5e-5→0), effective batch=16 (bs=4 × grad_accum=4). Third seed for uniform epoch-matched baseline. Paired with uniform_epoch_matched_indep_lr_seed42 (holdout=18.062) and dr_epoch_matched experiments for epoch confound quantification.\", \"parent\": \"uniform_epoch_matched_indep_lr_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_epoch_matched_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --max_steps 2533 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": 748574, \"log_path\": \"~/runs/provenance_weight_training/uniform_epoch_matched_seed456.log\", \"submitted_at\": \"2026-05-22T09:43:09.347Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": [\"holdout_combined\", \"owt_eval\", \"wiki_eval\"], \"wall_clock_seconds\": 6283.5, \"gpu_hours\": 1.75}, \"reproduce\": {\"finished_at\": \"2026-05-22T11:12:24.109Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:12:29.685867+00:00\"}]}, \"metrics\": {\"holdout_ppl\": 18.068, \"holdout_loss\": 2.8941, \"owt_ppl\": 18.66, \"owt_loss\": 2.9264, \"wiki_ppl\": 15.515, \"wiki_loss\": 2.7418, \"train_loss\": 8.039, \"total_steps\": 2533}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/uniform_epoch_matched_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T11:27:52.856Z\"}, \"dr_epoch_matched_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T08:27:17.771Z\", \"updated_at\": \"2026-05-22T10:45:14.168Z\", \"hypothesis\": \"Epoch-matched D&R seed456: trains on filtered data (q≤0.5, 153725 samples) for exactly 2533 steps with independent linear LR schedule (5e-5→0), effective batch=16 (bs=4 × grad_accum=4). Third seed for epoch confound quantification. Paired with dr_epoch_matched_indep_lr_v2_seed42 (17.651) and dr_epoch_matched_seed123_r2 (17.659).\", \"parent\": \"dr_epoch_matched_indep_lr_v2_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --max_steps 2533 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 725040, \"log_path\": \"~/runs/provenance_weight_training/dr_epoch_matched_seed456.log\", \"submitted_at\": \"2026-05-22T08:27:29.373Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": [\"holdout_combined\", \"owt_eval\", \"wiki_eval\"], \"wall_clock_seconds\": 8264.8, \"gpu_hours\": 2.3}, \"reproduce\": {\"finished_at\": \"2026-05-22T10:24:09.597Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:24:15.210830+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/dr_epoch_matched_seed456.log\", \"metrics\": {\"holdout_ppl\": 17.66, \"owt_ppl\": 18.27, \"wiki_ppl\": 15.16}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:45:14.168Z\"}, \"detect_remove_q05_v2_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:57:35.984Z\", \"updated_at\": \"2026-05-22T09:08:04.733Z\", \"hypothesis\": \"D&R hard filtering seed123 rerun with CORRECT effective batch=16 (batch_size=4 × grad_accum=4). Previous detect_remove_q05_v2_seed123 was invalid (effective batch=4). Full training on filtered data (q≤0.5, 153725 samples) for ~6103 steps with 200M token budget. Paired with detect_remove_q05_v2_seed42 for 2-seed consistency.\", \"parent\": \"detect_remove_q05_v2_seed123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": 682848, \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q05_v2_seed123_r2.log\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"eval_data\": [\"holdout_combined\", \"owt_eval\", \"wiki_eval\"]}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123_r2/final\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q05_v2_seed123_r2.log\", \"metrics\": {\"holdout_loss\": 2.8491, \"holdout_ppl\": 17.272, \"owt_loss\": 2.8908, \"owt_ppl\": 18.008, \"wiki_loss\": 2.7111, \"wiki_ppl\": 15.047, \"eval_holdout_tokens\": 4077068, \"eval_owt_tokens\": 6767242, \"eval_wiki_tokens\": 27000339, \"total_steps\": 6103, \"train_loss\": 11.01}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:08:04.733Z\"}, \"bs16_uniform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:32:02.600Z\", \"updated_at\": \"2026-05-22T08:50:09.265Z\", \"hypothesis\": \"Uniform baseline at batch_size=16, seed456. Third seed for bs16 batch-size sensitivity analysis. Paired with bs16_adaptive_tau07_seed456. If 3-seed Δ(adaptive−uniform) at bs=16 confirms amplification vs bs=4, strengthens the batch-size mechanism claim.\", \"parent\": \"bs16_uniform_seed42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs16_uniform_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 16 --gradient_accumulation_steps 1 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 697578, \"log_path\": \"/root/runs/provenance_weight_training/bs16_uniform_seed456.log\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": [\"holdout_combined\", \"owt_eval\", \"wiki_eval\"]}, \"metrics\": {\"holdout_loss\": 2.8745, \"holdout_ppl\": 17.717, \"owt_loss\": 2.9118, \"owt_ppl\": 18.39, \"wiki_loss\": 2.7319, \"wiki_ppl\": 15.363, \"total_steps\": 6103, \"train_loss\": 1.991}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_uniform_seed456/final\", \"log_path\": \"/root/runs/provenance_weight_training/bs16_uniform_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T08:18:29.641Z\"}, \"bs16_adaptive_tau07_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:32:04.878Z\", \"updated_at\": \"2026-05-22T08:50:07.781Z\", \"hypothesis\": \"Adaptive dual-constraint weighting with bs=16 (n_min=8, tau=0.7), seed456. Third seed for batch-size amplification effect. Paired with bs16_uniform_seed456. If 3-seed mean Δ(adaptive−uniform) at bs=16 >> bs=4's Δ=−0.020, confirms batch size amplifies adaptive advantage.\", \"parent\": \"bs16_adaptive_tau07_seed42\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --num_train_tokens 200000000 --batch_size 16 --gradient_accumulation_steps 1 --n_min 8 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": 698965, \"log_path\": \"~/runs/provenance_weight_training/bs16_adaptive_tau07_seed456.log\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": [\"holdout_combined\", \"owt_eval\", \"wiki_eval\"]}, \"metrics\": {\"holdout_loss\": 2.8704, \"holdout_ppl\": 17.645, \"owt_loss\": 2.9076, \"owt_ppl\": 18.313, \"wiki_loss\": 2.7276, \"wiki_ppl\": 15.296, \"total_steps\": 6103, \"train_loss\": 2.528}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/bs16_adaptive_tau07_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T08:18:31.981Z\"}, \"dr_epoch_matched_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:54:06.369Z\", \"updated_at\": \"2026-05-22T02:22:21.103Z\", \"hypothesis\": \"Epoch-matched D&R seed123 rerun with CORRECT effective batch=16 (batch_size=4 × grad_accum=4). Previous dr_epoch_matched_seed123 was invalid (effective batch=4, missing grad_accum). Trains on filtered data (q≤0.5, 153725 samples) for 2533 steps with independent linear LR schedule (5e-5→0). Paired with detect_remove_q05_v2_seed123 to quantify seed123 epoch confound percentage.\", \"parent\": \"dr_epoch_matched_seed123\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_seed123_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --max_steps 2533 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --lr_scheduler_type linear --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"681583\", \"log_path\": \"~/runs/provenance_weight_training/dr_epoch_matched_seed123_r2.log\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T02:07:51.990Z\"}, \"metrics\": {\"holdout_loss\": 2.8713, \"holdout_ppl\": 17.6591, \"owt_loss\": 2.9069, \"owt_ppl\": 18.2991, \"wiki_loss\": 2.7208, \"wiki_ppl\": 15.1918, \"eval_holdout_tokens\": 4077068, \"eval_owt_tokens\": 6767242, \"eval_wiki_tokens\": 27000339}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_seed123_r2/final\", \"log_path\": \"~/runs/provenance_weight_training/dr_epoch_matched_seed123_r2.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T02:22:21.103Z\"}, \"random_reweight_seed123\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T08:15:03.968Z\", \"updated_at\": \"2026-05-22T01:08:43.003Z\", \"server\": \"westd-30476\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_random_reweight_seed123.sh\\\"\", \"finished_at\": \"2026-05-22T00:52:13.127Z\"}, \"failure_reason\": \"Traceback → , in main trainer = WeightedTrainer( ^^^^^^^^^^^^^^^^ File \\\"/root/provenance_weight_training/training/pretrain_weighted.py\\\", line 101, in __init__ super().__init__(**kwargs) TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'\", \"completed_at\": \"2026-05-17T11:17:19.899Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T11:17:28.307496+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T00:52:18.825002+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"hypothesis\": \"Random reweight seed123 replication: shuffling q_scores before computing adaptive weights destroys the detector's contamination signal while preserving the weight distribution shape. Paired with random_reweight_baseline_seed42 (PPL=17.958) for 2-seed consistency.\", \"parent\": \"random_reweight_baseline_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_random_shuffle.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"653354\", \"data_path\": \"data/scored_data_random_shuffle.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed123.log\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed123\"}, \"metrics\": {\"holdout_loss\": 2.8873, \"holdout_ppl\": 17.945, \"owt_loss\": 2.9243, \"owt_ppl\": 18.622, \"wiki_loss\": 2.7448, \"wiki_ppl\": 15.562, \"total_steps\": 6103, \"train_loss\": 8.042, \"train_runtime_seconds\": 15820, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/random_reweight_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed123.log\", \"conclusion\": \"success\"}, \"bs16_adaptive_tau07_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:56:36.825Z\", \"updated_at\": \"2026-05-22T00:53:30.898Z\", \"hypothesis\": \"Batch size sensitivity replication seed123: adaptive weighting with bs=16 (n_min=8) vs bs=4. If Δ(adaptive−uniform) at bs=16 is comparable to seed42's −0.063, confirms the batch-size amplification effect is not seed-specific. Paired with bs16_uniform_seed123. Restart of bs16_adaptive_tau07_seed123 which crashed at step 500 due to disk full.\", \"parent\": \"bs16_adaptive_tau07_seed123\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --num_train_tokens 200000000 --batch_size 16 --n_min 8 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_total_limit 3 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"645294\", \"log_path\": \"~/runs/provenance_weight_training/bs16_adaptive_tau07_seed123.log\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed123/final\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T23:23:48.322Z\", \"metrics\": {\"holdout_loss\": 2.8688, \"holdout_ppl\": 17.616, \"owt_loss\": 2.9083, \"owt_ppl\": 18.325, \"wiki_loss\": 2.731, \"wiki_ppl\": 15.348}}, \"detect_remove_q05_v2_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:01:59.278Z\", \"updated_at\": \"2026-05-21T23:56:51.369Z\", \"hypothesis\": \"D&R hard filtering seed123 replication with CORRECT filtered data (q≤0.5, 153725 samples, 86.4% real). Paired with detect_remove_q05_v2_seed42 for 2-seed consistency.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 1 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"646037\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q05_v2_seed123.log\", \"submitted_at\": \"2026-05-21T19:02:37.493Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"wall_clock_seconds\": 17290.1, \"gpu_hours\": 4.8}, \"parent\": \"detect_remove_q05_v2_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:19:54.842Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T23:20:00.751774+00:00\"}]}, \"metrics\": {\"holdout_loss\": 2.8545, \"holdout_ppl\": 17.3656, \"owt_loss\": 2.9013, \"owt_ppl\": 18.198, \"wiki_loss\": 2.7234, \"wiki_ppl\": 15.2318, \"total_steps\": 24414, \"train_loss\": 2.76}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q05_v2_seed123.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T23:50:47.575Z\", \"failure_reason\": \"配置错误：缺少 --gradient_accumulation_steps 4，effective batch=4 (应为 16)。Metrics 无效。\"}, \"dr_epoch_matched_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:05:42.275Z\", \"updated_at\": \"2026-05-21T23:53:23.303Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --max_steps 2533 --batch_size 4 --learning_rate 5e-5 --lr_scheduler_type linear --seed 123\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"665830\", \"log_path\": \"~/runs/provenance_weight_training/dr_epoch_matched_seed123.log\", \"submitted_at\": \"2026-05-21T23:05:41.642Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"wall_clock_seconds\": 2638.3, \"gpu_hours\": 0.73}, \"hypothesis\": \"Epoch-matched D&R seed123: trains on filtered data (q≤0.5, 153725 samples) for exactly 2533 steps with independent linear LR schedule (5e-5→0). Paired with detect_remove_q05_v2_seed123 (full 24414 steps) to independently quantify epoch confound percentage. If full/epoch-matched PPL gap at seed123 is comparable to seed42's gap (17.285 vs 17.651 = 0.366), confirms epoch confound accounts for >90% of D&R's apparent advantage.\", \"parent\": \"dr_epoch_matched_indep_lr_v2_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:32:36.344Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T23:32:42.223280+00:00\"}]}, \"metrics\": {\"holdout_loss\": 2.9087, \"holdout_ppl\": 18.332, \"owt_loss\": 2.9099, \"owt_ppl\": 18.354, \"wiki_loss\": 2.705, \"wiki_ppl\": 14.955}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/dr_epoch_matched_seed123.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T23:49:39.988Z\", \"failure_reason\": \"配置错误：缺少 --gradient_accumulation_steps 4，effective batch=4 (应为 16)，训练仅看 0.066 epoch (应为 0.264)。PPL 18.332 无效。\"}, \"bs16_uniform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:28:09.678Z\", \"updated_at\": \"2026-05-21T22:58:47.511Z\", \"hypothesis\": \"Uniform baseline at batch_size=16, seed123. Paired with bs16_adaptive_tau07_seed123. If Δ(adaptive−uniform) at bs=16 seed123 is comparable to seed42's −0.063, the batch-size amplification is robust across seeds.\", \"parent\": \"bs16_uniform_seed42\", \"spec\": {\"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs16_uniform_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 16 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"643185\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T22:37:56.489Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T22:38:04.855478+00:00\"}]}, \"metrics\": {\"holdout_loss\": 2.8728, \"holdout_ppl\": 17.686, \"owt_loss\": 2.9107, \"owt_ppl\": 18.369, \"wiki_loss\": 2.7332, \"wiki_ppl\": 15.381, \"train_loss\": 1.997}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_uniform_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/bs16_uniform_seed123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T22:58:47.511Z\"}, \"detect_remove_q05_v2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T16:27:14.144Z\", \"updated_at\": \"2026-05-21T20:46:41.018Z\", \"hypothesis\": \"D&R hard filtering baseline with CORRECT filtered data (q≤0.5, 153725 samples, 86.4% real). Full 6103-step linear schedule. Paired with adaptive reweighting to compare hard filtering vs soft reweighting approaches. If D&R PPL > adaptive, soft reweighting extracts more value from contaminated data than simply removing it.\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --weighting_method uniform --num_train_tokens 200000000 --seed 42\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"629320\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q05_v2_seed42.log\", \"submitted_at\": \"2026-05-21T16:27:24.071Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed42/final\", \"wall_clock_seconds\": 15556.9, \"gpu_hours\": 4.32}, \"reproduce\": {\"finished_at\": \"2026-05-21T20:02:25.837Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T20:02:31.420557+00:00\"}]}, \"metrics\": {\"holdout_loss\": 2.8499, \"holdout_ppl\": 17.2853, \"owt_loss\": 2.8911, \"owt_ppl\": 18.0139, \"wiki_loss\": 2.7116, \"wiki_ppl\": 15.0528, \"train_loss\": 11, \"total_steps\": 6103}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T20:46:41.018Z\"}, \"bs16_adaptive_tau07_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:28:08.369Z\", \"updated_at\": \"2026-05-21T18:56:30.480Z\", \"hypothesis\": \"Batch size sensitivity replication seed123: adaptive weighting with bs=16 (n_min=8) vs bs=4. If Δ(adaptive−uniform) at bs=16 is comparable to seed42's −0.063, confirms the batch-size amplification effect is not seed-specific. Paired with bs16_uniform_seed123.\", \"parent\": \"bs16_adaptive_tau07_seed42\", \"spec\": {\"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --num_train_tokens 200000000 --batch_size 16 --n_min 8 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"643108\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T18:52:13.181Z\"}, \"failure_reason\": \"Traceback → packages/torch/serialization.py\\\", line 977, in save _save( File \\\"/root/miniconda3/lib/python3.12/site-packages/torch/serialization.py\\\", line 1286, in _save zip_file.write_record(name, storage, num_bytes) RuntimeError: basic_ios::clear: iostream error\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T18:52:16.154Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T18:52:23.195151+00:00\"}]}, \"notes\": \"失败原因: 磁盘空间不足 — torch.save(optimizer.state_dict()) 在 step 500 首次 checkpoint 时 IOException (basic_ios::clear: iostream error + enforce fail at inline_container.cc:668, unexpected pos 1513744000 vs 1513743888)。训练本身正常 (loss=2.5, lr=4.834e-05, step 500/6103)。| error_type: resource | 建议: 清理磁盘后重试\"}, \"bs16_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:03:21.016Z\", \"updated_at\": \"2026-05-21T18:24:16.989Z\", \"hypothesis\": \"Uniform baseline at batch_size=16 paired with bs16_adaptive_tau07_seed42. If adaptive Δ (adaptive - uniform) at bs=16 is comparable to bs=4 Δ (−0.020), demonstrates dual-constraint robustness to batch size.\", \"parent\": \"uniform_seed42\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs16_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 16 --gradient_accumulation_steps 1 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"620563\", \"log_path\": \"~/runs/provenance_weight_training/bs16_uniform_seed42.log\", \"submitted_at\": \"2026-05-21T14:03:35.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"models/Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_uniform_seed42\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 15641.3, \"gpu_hours\": 4.34}, \"metrics\": {\"holdout_loss\": 2.8732, \"holdout_ppl\": 17.694, \"owt_loss\": 2.9104, \"owt_ppl\": 18.364, \"wiki_loss\": 2.7302, \"wiki_ppl\": 15.337, \"train_loss\": 1.965}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_uniform_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/bs16_uniform_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T18:24:16.990Z\"}, \"bs16_adaptive_tau07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:39:47.600Z\", \"updated_at\": \"2026-05-21T18:04:39.917Z\", \"hypothesis\": \"Adaptive dual-constraint weighting with bs=16 (n_min=8) produces comparable holdout PPL to the bs=4 (n_min=2) main experiment, demonstrating batch size robustness of the dual-constraint mechanism rather than being an artifact of small-batch dynamics.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --num_train_tokens 200000000 --batch_size 16 --gradient_accumulation_steps 1 --n_min 8 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --gradient_checkpointing\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"613352\", \"log_path\": \"~/runs/provenance_weight_training/bs16_adaptive_tau07_seed42.log\", \"submitted_at\": \"2026-05-21T13:40:49.372Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15333.9, \"gpu_hours\": 4.26}, \"reproduce\": {\"finished_at\": \"2026-05-21T17:52:41.541Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T17:52:46.934970+00:00\"}]}, \"metrics\": {\"holdout_loss\": 2.8697, \"holdout_ppl\": 17.631, \"owt_loss\": 2.9074, \"owt_ppl\": 18.309, \"wiki_loss\": 2.7269, \"wiki_ppl\": 15.286, \"train_loss\": 2.537}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/bs16_adaptive_tau07_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/bs16_adaptive_tau07_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T17:56:23.271Z\"}, \"dr_epoch_matched_indep_lr_v2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:53:05.757Z\", \"updated_at\": \"2026-05-21T17:29:56.453Z\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir .../dr_epoch_matched_indep_lr_v2_seed42 --weighting_method uniform --max_steps 2533 --seed 42\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"623042\", \"log_path\": \"~/runs/provenance_weight_training/dr_epoch_matched_indep_lr_v2_seed42.log\", \"submitted_at\": \"2026-05-21T14:53:05.197Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_indep_lr_v2_seed42/final\", \"wall_clock_seconds\": 9411.3, \"gpu_hours\": 2.61}, \"hypothesis\": \"D&R epoch-matched with CORRECT filtered data (q≤0.5, 153725 samples, 86.4% real) and independent linear LR schedule (total_steps=2533). Rerun of invalidated dr_epoch_matched_indep_lr_seed42 which used inverted filter (q>0.5, 85% synthetic). Paired with uniform_epoch_matched_indep_lr_seed42 to quantify D&R effectiveness under fair LR comparison.\", \"parent\": \"dr_epoch_matched_indep_lr_seed42\", \"metrics\": {\"holdout_ppl\": 17.65053, \"holdout_loss\": 2.87077, \"ood_owt_ppl\": 18.26112, \"ood_owt_loss\": 2.90477, \"ood_wiki_ppl\": 15.19382, \"ood_wiki_loss\": 2.72089, \"train_loss_final\": 11.11, \"total_steps\": 2533}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T17:29:56.453Z\"}, \"uniform_epoch_matched_indep_lr_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:56:06.966Z\", \"updated_at\": \"2026-05-21T17:25:46.073Z\", \"hypothesis\": \"Uniform weighting with epoch-matched training tokens (max_steps=2533) and independent linear LR schedule (5e-5, full decay over 2533 steps) serves as the controlled baseline for LR confound elimination. Paired with dr_epoch_matched_indep_lr_seed42 (PPL=18.78) to quantify pure epoch-matching effect without LR schedule artifacts.\", \"parent\": \"uniform_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_epoch_matched_indep_lr_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --max_steps 2533 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"606291\", \"log_path\": \"~/runs/provenance_weight_training/uniform_epoch_matched_indep_lr_seed42.log\", \"submitted_at\": \"2026-05-21T12:12:09.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/uniform_epoch_matched_indep_lr_seed42/final\", \"wall_clock_seconds\": 18817.0, \"gpu_hours\": 5.23}, \"reproduce\": {\"finished_at\": \"2026-05-21T13:43:41.194Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T13:43:49.821951+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 18.06206, \"holdout_loss\": 2.89381, \"ood_owt_ppl\": 18.64966, \"ood_wiki_ppl\": 15.511, \"train_loss_final\": 8.058, \"total_steps\": 2533}, \"completed_at\": \"2026-05-21T17:25:46.074Z\"}, \"random_reweight_baseline_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:47:32.490Z\", \"updated_at\": \"2026-05-21T16:25:30.339Z\", \"hypothesis\": \"Random reweight baseline: shuffling q_scores before computing adaptive weights destroys the detector's contamination signal while preserving the weight distribution shape. If adaptive (PPL=17.674) outperforms random reweight, the detector signal is load-bearing and not just a regularization artifact.\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_random_shuffle.jsonl --weighting_method adaptive --tau 0.8 --seed 42\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"603550\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_baseline_seed42.log\", \"submitted_at\": \"2026-05-21T11:48:08.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_random_shuffle.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/random_reweight_baseline_seed42/final\", \"wall_clock_seconds\": 16641.8, \"gpu_hours\": 4.62}, \"metrics\": {\"holdout_ppl\": 17.95829, \"holdout_loss\": 2.88805, \"ood_owt_ppl\": 18.60614, \"ood_owt_loss\": 2.92349, \"ood_wiki_ppl\": 15.51906, \"ood_wiki_loss\": 2.74207}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T16:25:30.339Z\"}, \"dr_epoch_matched_indep_lr_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:56:34.309Z\", \"updated_at\": \"2026-05-21T14:50:52.460Z\", \"hypothesis\": \"D&R epoch-matched with independent linear LR schedule (total_steps=2533). Eliminates LR schedule confound: previous epoch-matched used 6103-step schedule but stopped at 2533. Paired with uniform_epoch_matched to quantify LR confound magnitude.\", \"parent\": \"detect_remove_q05_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_indep_lr_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --max_steps 2533 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"605271\", \"log_path\": \"~/runs/provenance_weight_training/dr_epoch_matched_indep_lr_seed42.log\", \"submitted_at\": \"2026-05-21T11:56:42.861Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/dr_epoch_matched_indep_lr_seed42/final\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 217774, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"self_trained\", \"eval_data\": \"holdout_combined + owt_eval + wiki_eval\", \"wall_clock_seconds\": 6047.8, \"gpu_hours\": 1.68}, \"conclusion\": \"failed\", \"metrics\": {\"holdout_ppl\": 18.78174, \"holdout_loss\": 2.93288, \"ood_owt_ppl\": 19.23533, \"ood_owt_loss\": 2.95675, \"ood_wiki_ppl\": 15.95958, \"ood_wiki_loss\": 2.77006, \"train_loss_final\": 5.833, \"total_steps\": 2533}, \"completed_at\": \"2026-05-21T13:37:30.667Z\", \"notes\": \"INVALIDATED: scored_data_filtered_q05.jsonl had inverted filter (kept q>0.5 = 85% synthetic instead of q≤0.5 = real data). PPL=18.782 is meaningless. Need to regenerate data and rerun.\"}, \"grid_b0_1_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:26:46.904Z\", \"updated_at\": \"2026-05-21T13:43:44.066Z\", \"hypothesis\": \"Grid-b sweep b=0.1 on ρ=0.4 data, seed42. Minimal reweighting — expect PPL close to uniform (~17.694). Establishes lower bound of useful b range.\", \"parent\": \"grid_b_seed42_batch\", \"notes\": \"PPL=17.657, between uniform(17.694) and b=0.3(17.640). b=0.1 provides minimal but positive improvement over uniform, consistent with near-uniform weighting at low b.\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-16T05:04:42.502Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_grid_b0_1_seed42.sh\\\"\", \"finished_at\": \"2026-05-16T08:42:41.654Z\", \"training_hours\": 3.63}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_grid_b0_1_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"34704\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_1_seed42.log\", \"submitted_at\": \"2026-05-17T17:20:25.910Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 332598.2, \"gpu_hours\": 92.39}, \"pid\": \"295096\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_1_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:42:43.936500+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.657, \"eval_loss_holdout\": 2.871}, \"checkpoint_path\": \"output/models/grid_b0_1_seed42/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:59:24.343Z\"}, \"rho02_adaptive_tau08_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:14:42.459Z\", \"updated_at\": \"2026-05-21T13:43:39.791Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/provenance_weight_training && bash scripts/run_rho02_adaptive_tau08_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"41387\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau08_seed42.log\", \"submitted_at\": \"2026-05-17T18:14:42.195Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/rho02_scored_data.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"rho\": 0.2, \"checkpoint_path\": \"/root/autodl-tmp/output/models/rho02_adaptive_tau08_seed42/final\", \"wall_clock_seconds\": 17407.7, \"gpu_hours\": 4.84}, \"reproduce\": {\"finished_at\": \"2026-05-17T22:19:39.990Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T22:19:47.496007+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_ppl_holdout\": 17.382, \"eval_loss_holdout\": 2.8555, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_seconds\": 14599, \"vs_rho02_uniform\": \"+0.046 (17.382 vs 17.336)\", \"vs_rho04_uniform\": \"-0.312 (17.382 vs 17.694)\", \"tau\": 0.8, \"rho\": 0.2, \"b_star_pct_zero\": \"40-50%\", \"conclusion_note\": \"worse than same-rho uniform baseline\"}, \"hypothesis\": \"Adaptive weighting with τ=0.8 at ρ=0.2 (low contamination): the dual-constrained algorithm finds meaningful b* even with only 20% contamination, achieving PPL < uniform baseline (17.694), demonstrating proportion-robustness (Claim 3 safe default).\", \"completed_at\": \"2026-05-17T23:04:49.876Z\"}, \"ess_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:51:52.911Z\", \"updated_at\": \"2026-05-21T13:43:15.412Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && bash scripts/run_ess_only_seed123.sh\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"115009\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed123.log\", \"submitted_at\": \"2026-05-17T15:31:00.484Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92291.7, \"gpu_hours\": 25.64}, \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"233872\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed123.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T21:41:11.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:41:12.958200+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.72, \"eval_loss_holdout\": 2.8746, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"eval_note\": \"Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693\", \"train_loss\": 10.2159, \"train_steps\": 6103, \"train_runtime_seconds\": 12959.5, \"b_star_mean\": 3.55, \"b_star_median\": 1.5918, \"b_star_std\": 4.7209, \"b_star_min\": 0.2344, \"b_star_max\": 20, \"b_star_p25\": 0.8398, \"b_star_p75\": 3.8281, \"b_star_p90\": 9.5996, \"b_star_count\": 21971, \"vs_uniform_ppl_delta\": \"+0.034\", \"vs_adaptive_fix_ppl_delta\": \"+0.077\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/ess_only_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:51:53.436Z\", \"hypothesis\": \"ESS-only adaptive baseline (max-intervention) seed=123: b* = max{b : ESS(b) >= n_min} ignores α_eff quality constraint, applying strongest possible downweighting. Multi-seed validation that dual-constraint (min-intervention) consistently outperforms ESS-only.\"}, \"ess_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:04:39.611Z\", \"updated_at\": \"2026-05-21T13:43:13.392Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && bash scripts/run_ess_only_seed456.sh\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"115513\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed456.log\", \"submitted_at\": \"2026-05-17T15:33:24.322Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92146.3, \"gpu_hours\": 25.6}, \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"pid\": \"233952\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T21:41:17.276Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:41:21.343173+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.76, \"eval_loss_holdout\": 2.877, \"eval_holdout_tokens\": 4077068, \"train_loss\": 1.9364, \"note\": \"re-eval on westd-41312 latest run (v2)\"}, \"checkpoint_path\": \"output/models/ess_only_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:51:54.328Z\", \"hypothesis\": \"ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only\"}, \"qwen06b_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:59:14.580Z\", \"updated_at\": \"2026-05-21T13:43:11.396Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/provenance_weight_training && bash scripts/run_uniform_seed42_v2.sh\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"125995\", \"log_path\": \"/root/runs/provenance_weight_training/qwen06b_uniform_seed42.log\", \"submitted_at\": \"2026-05-17T18:17:17.865Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"weighting_method\": \"uniform\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/qwen06b_uniform_seed42_v2/final\", \"wall_clock_seconds\": 14806.2, \"gpu_hours\": 4.11}, \"hypothesis\": \"Uniform baseline retrain (seed42) without inline eval overhead — provides clean PPL baseline for Claim 1/2 comparison and enables lm-eval downstream evaluation on same checkpoint\", \"reproduce\": {\"finished_at\": \"2026-05-17T21:52:18.403Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T21:52:22.072131+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733, \"eval_holdout_tokens\": 4077068, \"train_loss\": 1.9882, \"note\": \"v2 run on westd-41312 (no inline eval)\", \"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4836, \"downstream_piqa_acc_norm\": 0.6877, \"downstream_winogrande_acc\": 0.5856, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.365, \"eval_ppl_wikipedia\": 15.335}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T22:24:04.055Z\", \"eval_ppl_openwebtext\": 18.37, \"eval_ppl_wikipedia\": 15.34}, \"rho06_tau07_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:11:59.729Z\", \"updated_at\": \"2026-05-21T11:51:18.525Z\", \"hypothesis\": \"τ=0.7 at ρ=0.6 seed456: third seed completing ρ=0.6 τ=0.7 3-seed set. Together with seed42 and seed123, enables paired comparison against ρ=0.6 τ=0.8 to confirm τ=0.7 universality across contamination levels.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"killed\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"603064\", \"log_path\": \"~/runs/provenance_weight_training/rho06_tau07_seed456.log\", \"submitted_at\": \"2026-05-21T11:47:34.773Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 223.8, \"gpu_hours\": 0.06}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-21T11:51:18.525Z\"}, \"rho06_tau07_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:11:57.382Z\", \"updated_at\": \"2026-05-21T11:50:47.350Z\", \"hypothesis\": \"τ=0.7 at ρ=0.6 seed123: second seed replicating τ=0.7 advantage over τ=0.8 at higher contamination (ρ=0.6). Together with seed42 and seed456, enables paired comparison to confirm τ=0.7 universality across contamination levels.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/rho06_tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"601860\", \"log_path\": \"~/runs/provenance_weight_training/rho06_tau07_seed123.log\", \"submitted_at\": \"2026-05-21T11:28:57.474Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 1309.9, \"gpu_hours\": 0.36}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-21T11:50:47.350Z\"}, \"ngram_adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:14:23.226Z\", \"updated_at\": \"2026-05-21T10:45:11.511Z\", \"hypothesis\": \"Multi-detector validation: adaptive weighting with n-gram PPL detector (statistical, AUC=0.73) produces lower PPL than uniform, demonstrating method works with fundamentally different detector type (not just neural classifier). Complementary to q_score (Spearman r=-0.36). Part of D079 Line A.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_ngram_qscore.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42 --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_only_model --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"226953\", \"log_path\": \"~/runs/provenance_weight_training/ngram_adaptive_seed42.log\", \"submitted_at\": \"2026-05-18T15:01:02.239Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final\", \"train_loss\": 9.298, \"train_runtime_s\": 14170, \"total_steps\": 6103, \"wall_clock_seconds\": 14810.3, \"gpu_hours\": 4.11}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T19:07:52.563Z\", \"metrics\": {\"holdout_ppl\": 17.820214, \"holdout_loss\": 2.880333}}, \"gpt2_adaptive_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:59:23.805Z\", \"updated_at\": \"2026-05-21T10:28:12.735Z\", \"hypothesis\": \"GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=456. V2: from-scratch rerun after disk crash (original used --save_only_model, no optimizer for resume). No --save_only_model, no inline eval.\", \"parent\": \"gpt2_adaptive_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 456 --data_path data/scored_data_gpt2ppl_qscore.jsonl (from scratch, no --save_only_model)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"pid\": \"569718\", \"log_path\": \"~/runs/provenance_weight_training/gpt2_adaptive_seed456_v2.log\", \"submitted_at\": \"2026-05-21T05:00:04.331Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_gpt2ppl_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A (post-hoc eval)\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed456_v2\", \"detector\": \"GPT-2 PPL (AUC=0.913)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed456_v2/final\", \"wall_clock_seconds\": 18020.3, \"gpu_hours\": 5.01}, \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.79719, \"holdout_loss\": 2.87904}, \"completed_at\": \"2026-05-21T10:00:24.591Z\"}, \"adaptive_tau08_scratch_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:59:19.444Z\", \"updated_at\": \"2026-05-21T10:28:11.715Z\", \"hypothesis\": \"From-scratch adaptive (τ=0.8, ρ=0.4, n_min=2, seed=42, Qwen3-0.6B). V3: resume from v2 checkpoint-500 (has optimizer state). No --save_only_model, no inline eval.\", \"parent\": \"adaptive_tau08_scratch_seed42_v2\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 42 --data_path data/scored_data.jsonl --resume_from_checkpoint v2/checkpoint-500 (has optimizer, no --save_only_model)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": \"569244\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_tau08_scratch_seed42_v3.log\", \"submitted_at\": \"2026-05-21T04:59:56.230Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"resume_from_v2_checkpoint-500_with_optimizer\", \"eval_data\": \"N/A (post-hoc eval)\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_tau08_scratch_seed42_v2\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_tau08_scratch_seed42_v2/final\", \"wall_clock_seconds\": 18022.2, \"gpu_hours\": 5.01}, \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.6885, \"holdout_loss\": 2.87291, \"ood_owt_ppl\": 18.37026, \"ood_owt_loss\": 2.91073, \"ood_wiki_ppl\": 15.34964, \"ood_wiki_loss\": 2.73109, \"ood_eval_source\": \"eval_results/ pipeline\"}, \"completed_at\": \"2026-05-21T10:00:18.388Z\"}, \"ngram_adaptive_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:59:22.350Z\", \"updated_at\": \"2026-05-21T10:27:02.278Z\", \"hypothesis\": \"N-gram PPL detector (AUC=0.73) + adaptive weighting, seed=456. V2: from-scratch rerun after disk crash. No --save_only_model, no inline eval.\", \"parent\": \"ngram_adaptive_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 456 --data_path data/scored_data_ngram_qscore.jsonl (from scratch, no --save_only_model)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": \"569464\", \"log_path\": \"~/runs/provenance_weight_training/ngram_adaptive_seed456_v2.log\", \"submitted_at\": \"2026-05-21T05:00:01.488Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_ngram_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A (post-hoc eval)\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed456_v2\", \"detector\": \"N-gram PPL (AUC=0.73)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed456_v2/final\", \"wall_clock_seconds\": 18021.1, \"gpu_hours\": 5.01}, \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.82607, \"holdout_loss\": 2.88066}, \"completed_at\": \"2026-05-21T10:00:22.602Z\"}, \"gpt2_adaptive_seed123_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:59:21.265Z\", \"updated_at\": \"2026-05-21T10:27:00.177Z\", \"hypothesis\": \"GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=123. V3: resume from v2 checkpoint-500 (has optimizer state). No --save_only_model, no inline eval.\", \"parent\": \"gpt2_adaptive_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 123 --data_path data/scored_data_gpt2ppl_qscore.jsonl --resume_from_checkpoint v2/checkpoint-500 (has optimizer, no --save_only_model)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": \"569321\", \"log_path\": \"~/runs/provenance_weight_training/gpt2_adaptive_seed123_v3.log\", \"submitted_at\": \"2026-05-21T04:59:58.685Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_gpt2ppl_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"resume_from_v2_checkpoint-500_with_optimizer\", \"eval_data\": \"N/A (post-hoc eval)\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed123_v2\", \"detector\": \"GPT-2 PPL (AUC=0.913)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed123_v2/final\", \"wall_clock_seconds\": 18021.8, \"gpu_hours\": 5.01}, \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.78848, \"holdout_loss\": 2.87855}, \"completed_at\": \"2026-05-21T10:00:20.515Z\"}, \"gpt2_adaptive_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:44:29.948Z\", \"updated_at\": \"2026-05-21T04:59:11.372Z\", \"hypothesis\": \"GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=456. Third seed for detector ablation to complete 3-seed set with gpt2_adaptive_seed42 (PPL=17.79) and gpt2_adaptive_seed123. Tests reproducibility of method with medium-quality detector.\", \"parent\": \"gpt2_adaptive_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 456 --data_path data/scored_data_gpt2ppl_qscore.jsonl (no inline eval)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"pid\": \"551638\", \"log_path\": \"~/runs/provenance_weight_training/gpt2_adaptive_seed456.log\", \"data_path\": \"data/scored_data_gpt2ppl_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed456\", \"detector\": \"GPT-2 PPL (AUC=0.913)\", \"eval_data\": \"N/A (training experiment, not eval)\", \"checkpoint_path\": \"N/A (disk full crash, checkpoint-5500 has no optimizer)\"}, \"conclusion\": \"failed\", \"failure_reason\": \"Disk 100% full — training crashed at step 6000/6103, checkpoint-6000 corrupted (36KB), checkpoint-5500 has no optimizer (--save_only_model)\", \"completed_at\": \"2026-05-21T04:59:11.372Z\"}, \"ngram_adaptive_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:13:00.621Z\", \"updated_at\": \"2026-05-21T04:59:09.364Z\", \"hypothesis\": \"N-gram PPL detector (statistical, AUC=0.73) + adaptive weighting, seed=456. Third seed completing 3-seed set for detector ablation. Tests consistency with ngram_adaptive_seed42 (PPL=17.82) and ngram_adaptive_seed123.\", \"parent\": \"ngram_adaptive_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 456 --data_path data/scored_data_ngram_qscore.jsonl (from scratch, no --save_only_model, no inline eval)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": \"566782\", \"log_path\": \"~/runs/provenance_weight_training/ngram_adaptive_seed456.log\", \"submitted_at\": \"2026-05-21T04:13:52.043Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_ngram_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A (training, post-hoc eval via eval_results/ pipeline)\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed456\", \"detector\": \"N-gram PPL (AUC=0.73)\", \"checkpoint_path\": \"N/A (disk full crash, no valid checkpoint)\", \"wall_clock_seconds\": 2717.3, \"gpu_hours\": 0.75}, \"conclusion\": \"failed\", \"failure_reason\": \"Disk 100% full — training crashed at checkpoint write, no valid checkpoint to resume\", \"completed_at\": \"2026-05-21T04:59:09.364Z\"}, \"gpt2_adaptive_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:54:05.914Z\", \"updated_at\": \"2026-05-21T04:59:07.344Z\", \"hypothesis\": \"GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=123. V2: rerun without --save_only_model. Replaces corrupted gpt2_adaptive_seed123 (resume caused optimizer loss). Second seed for detector ablation to confirm gpt2_adaptive_seed42 pattern (PPL=17.79).\", \"parent\": \"gpt2_adaptive_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 123 --data_path data/scored_data_gpt2ppl_qscore.jsonl (from scratch, no --save_only_model, no inline eval)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": \"565346\", \"log_path\": \"~/runs/provenance_weight_training/gpt2_adaptive_seed123_v2.log\", \"submitted_at\": \"2026-05-21T03:55:09.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_gpt2ppl_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A (training, post-hoc eval via eval_results/ pipeline)\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed123_v2\", \"detector\": \"GPT-2 PPL (AUC=0.913)\", \"checkpoint_path\": \"N/A (disk full crash)\", \"wall_clock_seconds\": 3837.4, \"gpu_hours\": 1.07}, \"conclusion\": \"failed\", \"failure_reason\": \"Disk 100% full — training crashed at checkpoint write\", \"completed_at\": \"2026-05-21T04:59:07.344Z\"}, \"adaptive_tau08_scratch_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:54:03.912Z\", \"updated_at\": \"2026-05-21T04:59:05.334Z\", \"hypothesis\": \"From-scratch adaptive (τ=0.8, ρ=0.4, n_min=2, seed=42, Qwen3-0.6B). V2: rerun without --save_only_model to preserve optimizer state. Replaces corrupted adaptive_tau08_scratch_seed42 (resume caused optimizer loss). Completes 3-seed from-scratch set for τ=0.8 OOD comparison.\", \"parent\": \"adaptive_tau08_scratch_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 42 --data_path data/scored_data.jsonl (from scratch, no --save_only_model, no inline eval)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": \"565269\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_tau08_scratch_seed42_v2.log\", \"submitted_at\": \"2026-05-21T03:55:07.498Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A (training, post-hoc eval via eval_results/ pipeline)\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_tau08_scratch_seed42_v2\", \"checkpoint_path\": \"N/A (disk full crash)\", \"wall_clock_seconds\": 3837.8, \"gpu_hours\": 1.07}, \"conclusion\": \"failed\", \"failure_reason\": \"Disk 100% full — training crashed at checkpoint write\", \"completed_at\": \"2026-05-21T04:59:05.334Z\"}, \"gpt2_adaptive_seed123\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-20T18:34:08.013Z\", \"updated_at\": \"2026-05-21T03:54:55.606Z\", \"hypothesis\": \"GPT-2 PPL detector (AUC=0.913) + adaptive weighting, seed=123. Second seed for detector ablation to confirm gpt2_adaptive_seed42 pattern (PPL=17.79, worse than TF-IDF but still meaningful reweighting). If consistent, supports claim that method works across detector quality levels.\", \"parent\": \"gpt2_adaptive_seed42\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T18:34:25.885Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_gpt2ppl_qscore.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --eval_steps 500 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-21T00:35:49.664Z\", \"training_hours\": 6.02}, \"failure_reason\": \"Resume from --save_only_model checkpoint caused optimizer state loss. Adam reinitialized → model degraded. Results invalid.\", \"completed_at\": \"2026-05-21T00:35:54.270Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T00:36:02.306636+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 123 --data_path data/scored_data_gpt2ppl_qscore.jsonl --resume_from_checkpoint checkpoint-2500 (no inline eval)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": \"551137\", \"log_path\": \"~/runs/provenance_weight_training/gpt2_adaptive_seed123.log\", \"data_path\": \"data/scored_data_gpt2ppl_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"resume_from_checkpoint-2500\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed123\", \"detector\": \"GPT-2 PPL (AUC=0.913)\", \"resume_note\": \"Resumed from checkpoint-2500 after timeout (6h). Removed --eval_data_path and --eval_steps to eliminate inline eval overhead (~43min/eval). Remaining ~3603 steps, ~2.3h.\", \"eval_data\": \"N/A (training experiment, not eval)\", \"checkpoint_path\": \"N/A (corrupted by optimizer loss)\"}, \"conclusion\": \"failed\"}, \"adaptive_tau08_scratch_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-20T17:17:50.273Z\", \"updated_at\": \"2026-05-21T03:54:53.604Z\", \"hypothesis\": \"From-scratch adaptive (τ=0.8, ρ=0.4, n_min=2, seed=42, Qwen3-0.6B). Replaces resume-checkpoint adaptive_fix_seed42 to complete 3-seed from-scratch set with adaptive_ood_seed123/456. Enables symmetric 3-seed OOD comparison: τ=0.7 3-seed vs τ=0.8 3-seed.\", \"parent\": \"adaptive_fix_seed42\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T17:18:30.262Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_tau08_scratch_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --eval_steps 500 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-21T01:18:39.252Z\", \"training_hours\": 8.0}, \"failure_reason\": \"Resume from --save_only_model checkpoint caused optimizer state loss. Adam reinitialized → model degraded. Holdout PPL=17.905 (expected ~17.65). Results invalid.\", \"completed_at\": \"2026-05-21T01:18:42.560Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T01:18:47.652176+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 42 --data_path data/scored_data.jsonl --resume_from_checkpoint checkpoint-3500 (no inline eval)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": \"553579\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_tau08_scratch_seed42.log\", \"submitted_at\": \"2026-05-21T01:21:15.351Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"resume_from_checkpoint-3500\", \"eval_data\": \"N/A (training experiment, eval post-training via eval_results/ pipeline)\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_tau08_scratch_seed42\", \"resume_note\": \"Resumed from checkpoint-3500 after timeout (8h). Removed --eval_data_path and --eval_steps to eliminate inline eval overhead. Remaining ~2603 steps, ~1.6h.\", \"checkpoint_path\": \"N/A (corrupted by optimizer loss)\", \"wall_clock_seconds\": 9218.3, \"gpu_hours\": 2.56}, \"conclusion\": \"failed\"}, \"ngram_adaptive_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:16:21.156Z\", \"updated_at\": \"2026-05-21T02:19:10.605Z\", \"hypothesis\": \"N-gram PPL detector (statistical, AUC=0.73) + adaptive weighting, seed=123. Second seed for detector ablation to confirm ngram_adaptive_seed42 pattern (PPL=17.82). Tests consistency of method with weak statistical detector.\", \"parent\": \"ngram_adaptive_seed42\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-20T22:16:55.814Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data_ngram_qscore.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-21T02:12:31.315Z\", \"training_hours\": 3.93}, \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --seed 123 --data_path data/scored_data_ngram_qscore.jsonl\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": \"543911\", \"log_path\": \"~/runs/provenance_weight_training/ngram_adaptive_seed123.log\", \"data_path\": \"data/scored_data_ngram_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"from_scratch\", \"output_dir\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed123\", \"detector\": \"N-gram PPL (AUC=0.73)\"}, \"pid\": \"543911\", \"log_path\": \"~/runs/provenance_weight_training/ngram_adaptive_seed123.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T02:12:36.538125+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.823, \"eval_loss_holdout\": 2.8805, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.289, \"total_steps\": 6103}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed123/final\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T02:19:10.606Z\"}, \"adaptive_1_7b_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:55:35.805Z\", \"updated_at\": \"2026-05-20T22:15:23.125Z\", \"hypothesis\": \"Adaptive (dual-constrained) at 1.7B model scale (seed=456, τ=0.8, ρ=0.4). From-scratch on westd-41312 cuda:3. Replicates adaptive_1_7b_seed42_v5 (PPL=13.27) with different seed for 3-seed error bars. Paired with uniform_1_7b_seed456.\", \"parent\": \"adaptive_1_7b_seed42_v5\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed456 --model_name models/Qwen/Qwen3-1.7B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"pid\": \"494706\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_seed456.log\", \"submitted_at\": \"2026-05-20T16:00:18.071Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-1.7B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"data/scored_data.jsonl (training, holdout eval built-in)\", \"wall_clock_seconds\": 21302.6, \"gpu_hours\": 5.92}, \"reproduce\": {\"finished_at\": \"2026-05-20T21:09:28.993Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T21:09:34.067656+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 13.2668, \"eval_ppl_openwebtext\": 13.292, \"eval_ppl_wikipedia\": 10.947, \"downstream_arc_easy_acc_norm\": 0.7146, \"downstream_arc_challenge_acc_norm\": 0.4352, \"downstream_hellaswag_acc_norm\": 0.6133, \"downstream_piqa_acc_norm\": 0.7443, \"downstream_winogrande_acc\": 0.6219, \"downstream_mean\": 0.6259, \"ood_eval_source\": \"eval_results/ pipeline\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T21:55:20.639Z\"}, \"uniform_1_7b_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:55:34.483Z\", \"updated_at\": \"2026-05-20T21:37:05.685Z\", \"hypothesis\": \"Uniform baseline at 1.7B model scale (seed=456). From-scratch on westd-41312 cuda:2. Replicates uniform_1_7b_seed42_v5 (PPL=13.28) with different seed for 3-seed error bars. Paired with adaptive_1_7b_seed456.\", \"parent\": \"uniform_1_7b_seed42_v5\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed456 --model_name models/Qwen/Qwen3-1.7B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": \"494625\", \"log_path\": \"~/runs/provenance_weight_training/uniform_1_7b_seed456.log\", \"submitted_at\": \"2026-05-20T16:00:15.101Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-1.7B\", \"seed\": 456, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"data/scored_data.jsonl (training, holdout eval built-in)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed456/final\", \"wall_clock_seconds\": 20190.8, \"gpu_hours\": 5.61}, \"reproduce\": {\"finished_at\": \"2026-05-20T20:54:45.983Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T20:54:54.034865+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 13.28, \"eval_loss_holdout\": 2.5863, \"train_loss_final\": 7.537, \"total_steps\": 6103, \"num_eval_tokens\": 4077068, \"eval_ppl_openwebtext\": 13.307, \"eval_ppl_wikipedia\": 10.953, \"downstream_arc_easy_acc_norm\": 0.7113, \"downstream_arc_challenge_acc_norm\": 0.4224, \"downstream_hellaswag_acc_norm\": 0.6132, \"downstream_piqa_acc_norm\": 0.7448, \"downstream_winogrande_acc\": 0.6251, \"downstream_mean\": 0.6234}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T21:36:45.857Z\"}, \"adaptive_ood_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:34:31.061Z\", \"updated_at\": \"2026-05-20T17:56:20.991Z\", \"hypothesis\": \"Retrain adaptive (τ=0.8, n_min=2, seed=456) with checkpoint saving for OOD eval. If in-dist PPL matches original 17.657 (±0.01), the checkpoint is valid for OOD generalization testing across OpenWebText/Wikipedia/FineWeb.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --seed 456\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": 313296, \"log_path\": \"~/runs/provenance_weight_training/adaptive_ood_seed456.log\", \"submitted_at\": \"2026-05-19T14:37:05.986Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 6103, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"wall_clock_seconds\": 14843.0, \"gpu_hours\": 4.12}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:26:26.904Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:26:32.576132+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.683, \"eval_ppl_openwebtext\": 18.366, \"eval_ppl_wikipedia\": 15.345, \"downstream_arc_easy_acc_norm\": 0.6077, \"downstream_arc_challenge_acc_norm\": 0.3541, \"downstream_hellaswag_acc_norm\": 0.48, \"downstream_piqa_acc_norm\": 0.6806, \"downstream_winogrande_acc\": 0.5714, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_ood_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_ood_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:44:28.974Z\"}, \"adaptive_ood_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:34:29.354Z\", \"updated_at\": \"2026-05-20T17:56:19.865Z\", \"hypothesis\": \"Retrain adaptive (τ=0.8, n_min=2, seed=123) with checkpoint saving for OOD eval. If in-dist PPL matches original 17.643 (±0.01), the checkpoint is valid for OOD generalization testing across OpenWebText/Wikipedia/FineWeb.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --seed 123\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 313217, \"log_path\": \"~/runs/provenance_weight_training/adaptive_ood_seed123.log\", \"submitted_at\": \"2026-05-19T14:37:03.655Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 6103, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"wall_clock_seconds\": 14843.5, \"gpu_hours\": 4.12}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:26:12.673Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:26:17.460395+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.677, \"eval_ppl_openwebtext\": 18.373, \"eval_ppl_wikipedia\": 15.37, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4791, \"downstream_piqa_acc_norm\": 0.6844, \"downstream_winogrande_acc\": 0.5706, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_ood_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_ood_seed123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:44:27.165Z\"}, \"uniform_1_7b_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:09:34.029Z\", \"updated_at\": \"2026-05-20T17:56:18.709Z\", \"hypothesis\": \"Uniform baseline at 1.7B model scale (seed=123). From-scratch on westd-41312 cuda:0. Replicates uniform_1_7b_seed42_v5 (PPL=13.28) with different seed for 3-seed error bars. Paired with adaptive_1_7b_seed123 for scaling claim.\", \"spec\": {\"command\": \"train uniform_1_7b_seed123\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"260414\", \"log_path\": \"~/runs/provenance_weight_training/uniform_1_7b_seed123.log\", \"submitted_at\": \"2026-05-18T23:09:43.550Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human\", \"data_count\": 5000, \"model_name\": \"1.7B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed123/final\", \"wall_clock_seconds\": 18333.0, \"gpu_hours\": 5.09}, \"reproduce\": {\"finished_at\": \"2026-05-19T04:03:50.026Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T04:03:54.802765+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 13.2648, \"eval_loss_holdout\": 2.5851, \"train_loss_final\": 7.557, \"total_steps\": 6103, \"num_eval_tokens\": 4077068, \"eval_ppl_openwebtext\": 13.2918, \"eval_ppl_wikipedia\": 10.942, \"downstream_arc_easy_acc_norm\": 0.726, \"downstream_arc_challenge_acc_norm\": 0.4317, \"downstream_hellaswag_acc_norm\": 0.6118, \"downstream_piqa_acc_norm\": 0.7454, \"downstream_winogrande_acc\": 0.6133, \"downstream_mean\": 0.6256}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T04:15:16.584Z\"}, \"adaptive_fix_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:31.779Z\", \"updated_at\": \"2026-05-20T17:16:11.079Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)\", \"parent\": \"adaptive_seed456\", \"notes\": \"最终清理后重提交。从 checkpoint-1000 恢复，无 inline eval。PID=127285\", \"spec\": {\"n_min\": 2, \"tau\": 0.8}, \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"pid\": \"115066\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir output/models/adaptive_fix_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --eval_steps 500 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-14T21:00:17.106Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:47.164099+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:00:18.079813+00:00\"}]}, \"metrics\": {\"b_star_count\": 26396, \"b_star_max\": 20, \"b_star_mean\": 1.416, \"b_star_median\": 0.88, \"b_star_min\": 0, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\", \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_pct_below_0.5\": 20.9, \"b_star_std\": 1.993, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.8711, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.66/4077068\", \"eval_ppl_holdout\": 17.6566, \"eval_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 8.3124, \"train_runtime\": 11436.05, \"train_samples_per_second\": 8.539, \"train_steps_per_second\": 0.534, \"ood_note\": \"OOD eval not available — checkpoint on decommissioned westd-47453; adaptive_ood_seed456 has OOD from from-scratch retrain\"}, \"checkpoint_path\": \"output/models/adaptive_fix_seed456/final\"}, \"adaptive_fix_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:31.409Z\", \"updated_at\": \"2026-05-20T17:16:06.137Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)\", \"parent\": \"adaptive_seed123\", \"notes\": \"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126944\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"spec\": {\"contamination_ratio\": 0.4, \"tau\": 0.8, \"batch_size\": 4}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:41:22.910Z\"}, \"completed_at\": \"\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:38.735034+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:41:26.828424+00:00\"}]}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/adaptive_fix_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed123.log\", \"metrics\": {\"b_star_count\": 25906, \"b_star_max\": 20, \"b_star_mean\": 1.431, \"b_star_median\": 0.88, \"b_star_min\": 0, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\", \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_2_to_5\": 6.3, \"b_star_pct_above_2\": 16.1, \"b_star_pct_above_5\": 1.9, \"b_star_pct_below_0.5\": 20.9, \"b_star_std\": 2.029, \"epoch\": 0.26, \"eval_holdout_tokens\": 4077068, \"eval_loss\": 2.8704, \"eval_loss_holdout\": 2.8704, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.643/4077068\", \"eval_ppl_holdout\": 17.6432, \"eval_tokens\": 4077068, \"total_steps\": 6103, \"train_loss_weighted\": 7.517, \"train_runtime_s\": 10347, \"ood_note\": \"OOD eval not available — checkpoint on decommissioned westd-47453; adaptive_ood_seed123 has OOD from from-scratch retrain\"}}, \"uniform_1_7b_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:51:09.912Z\", \"updated_at\": \"2026-05-20T16:42:48.020Z\", \"hypothesis\": \"Uniform baseline at 1.7B model scale (seed=42). From-scratch on westd-41312 cuda:0. v5 replaces v4 (disk full at step 500). 176GB available after cleanup.\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T08:52:12.203Z\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42_v5 --model_name models/Qwen/Qwen3-1.7B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 453123, \"log_path\": \"~/runs/provenance_weight_training/uniform_1_7b_seed42_v5.log\", \"submitted_at\": \"2026-05-20T08:52:46.196Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"wall_clock_seconds\": 19145.3, \"gpu_hours\": 5.32}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42_v5/final\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.56, \"total_steps\": 6103, \"train_runtime_s\": 17630, \"eval_ppl_holdout\": 13.28, \"eval_ppl_openwebtext\": 13.291, \"eval_ppl_wikipedia\": 10.919, \"downstream_arc_easy_acc_norm\": 0.7235, \"downstream_arc_challenge_acc_norm\": 0.4334, \"downstream_hellaswag_acc_norm\": 0.6107, \"downstream_piqa_acc_norm\": 0.7432, \"downstream_winogrande_acc\": 0.6172, \"downstream_mean\": 0.6256, \"ood_eval_source\": \"eval_results/ pipeline\"}, \"completed_at\": \"2026-05-20T14:11:51.458Z\", \"eval_ppl_openwebtext\": 13.291, \"eval_ppl_wikipedia\": 10.919}, \"adaptive_1_7b_seed42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:51:11.055Z\", \"updated_at\": \"2026-05-20T16:42:46.317Z\", \"hypothesis\": \"Adaptive (dual-constrained) at 1.7B model scale (seed=42, τ=0.8, ρ=0.4). From-scratch on westd-41312 cuda:1. v5 replaces v4 (disk full at step 500). Paired with uniform_1_7b_seed42_v5 for scaling claim.\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T08:52:14.451Z\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42_v5 --model_name models/Qwen/Qwen3-1.7B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": 453200, \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_seed42_v5.log\", \"submitted_at\": \"2026-05-20T08:52:48.288Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"wall_clock_seconds\": 19145.2, \"gpu_hours\": 5.32}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42_v5/final\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 9.139, \"total_steps\": 6103, \"train_runtime_s\": 18540, \"eval_ppl_holdout\": 13.27, \"eval_ppl_openwebtext\": 13.282, \"eval_ppl_wikipedia\": 10.955, \"downstream_arc_easy_acc_norm\": 0.7176, \"downstream_arc_challenge_acc_norm\": 0.4403, \"downstream_hellaswag_acc_norm\": 0.6164, \"downstream_piqa_acc_norm\": 0.7443, \"downstream_winogrande_acc\": 0.6069, \"downstream_mean\": 0.6251, \"ood_eval_source\": \"eval_results/ pipeline\"}, \"completed_at\": \"2026-05-20T14:11:53.445Z\", \"eval_ppl_openwebtext\": 13.282, \"eval_ppl_wikipedia\": 10.955}, \"adaptive_1_7b_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:54:50.927Z\", \"updated_at\": \"2026-05-20T16:41:38.288Z\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-1.7B --data_path data/scored_data.jsonl --output_dir .../adaptive_1_7b_seed123 --weighting_method adaptive --tau 0.8 --n_min 2 --seed 123 --batch_size 4 --gradient_accumulation_steps 4 --num_train_tokens 200000000\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": 248439, \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_seed123.log\", \"submitted_at\": \"2026-05-18T19:54:50.523Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-1.7B\", \"seed\": 123, \"wall_clock_seconds\": 19292.5, \"gpu_hours\": 5.36}, \"hypothesis\": \"Adaptive (dual-constrained) at 1.7B model scale (seed=123, τ=0.8, ρ=0.4). From-scratch on westd-41312 cuda:1. Replicates adaptive_1_7b_seed42_v5 (PPL=13.27) with different seed for 3-seed error bars. Paired with uniform_1_7b_seed123.\", \"reproduce\": {\"finished_at\": \"2026-05-19T01:05:21.708Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T01:05:28.647322+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 13.25, \"eval_loss_holdout\": 2.5843, \"eval_ppl_openwebtext\": 13.2909, \"eval_ppl_wikipedia\": 10.9521, \"downstream_arc_easy_acc_norm\": 0.7138, \"downstream_arc_challenge_acc_norm\": 0.4386, \"downstream_hellaswag_acc_norm\": 0.6147, \"downstream_piqa_acc_norm\": 0.7459, \"downstream_winogrande_acc\": 0.6298, \"downstream_mean\": 0.6286}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed123/final\", \"completed_at\": \"2026-05-19T01:16:22.990Z\"}, \"contamination_60_uniform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:38:07.226Z\", \"updated_at\": \"2026-05-20T16:39:23.889Z\", \"hypothesis\": \"Uniform baseline at ρ=0.6 seed456: pairs with contamination_60_seed456 (adaptive) to form seed456 uniform/adaptive contrast. If adaptive PPL < uniform PPL at ρ=0.6, confirms Claim 3 proportion-robustness across seeds.\", \"parent\": \"contamination_60_uniform_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_uniform_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"158709\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed456.log\", \"submitted_at\": \"2026-05-18T01:44:54.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"contamination_60_uniform_seed42\", \"eval_data\": \"data/scored_data_60.jsonl\", \"wall_clock_seconds\": 13381.1, \"gpu_hours\": 3.72}, \"reproduce\": {\"finished_at\": \"2026-05-18T05:19:32.037Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:19:39.289326+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 7.637, \"train_runtime_seconds\": 12845, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\", \"eval_ppl_openwebtext\": 18.449, \"eval_ppl_wikipedia\": 15.42, \"ood_eval_source\": \"eval_results/ pipeline (consistent with adaptive tau07 evals)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/contamination_60_uniform_seed456/final\", \"completed_at\": \"2026-05-18T05:27:55.537Z\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed456.log\", \"eval_ppl_openwebtext\": 18.449, \"eval_ppl_wikipedia\": 15.42}, \"eval_adaptive_1_7b_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:00:55.026Z\", \"updated_at\": \"2026-05-20T16:00:55.026Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && echo '=== OOD OpenWebText ===' && python eval_perplexity.py --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed123/final --data_path data/eval_openwebtext.jsonl --max_docs 5000 --max_length 2048 --output_path /root/autodl-tmp/provenance_weight_training/output/eval/adaptive_1_7b_seed123_openwebtext.json && echo '=== OOD Wikipedia ===' && python eval_perplexity.py --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed123/final --data_path data/eval_wikipedia.jsonl --max_docs 5000 --max_length 2048 --output_path /root/autodl-tmp/provenance_weight_training/output/eval/adaptive_1_7b_seed123_wikipedia.json && echo '=== Downstream ===' && lm_eval --model hf --model_args pretrained=/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed123/final,dtype=float16 --tasks arc_easy,arc_challenge,hellaswag,piqa,winogrande --batch_size auto --num_fewshot 0 --output_path /root/autodl-tmp/provenance_weight_training/output/eval/adaptive_1_7b_seed123_downstream && echo '=== ALL DONE ==='\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"495970\", \"log_path\": \"~/runs/provenance_weight_training/eval_adaptive_1_7b_seed123.log\", \"submitted_at\": \"2026-05-20T16:00:54.254Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_uniform_1_7b_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T16:00:50.758Z\", \"updated_at\": \"2026-05-20T16:00:50.758Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && echo '=== OOD OpenWebText ===' && python eval_perplexity.py --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed123/final --data_path data/eval_openwebtext.jsonl --max_docs 5000 --max_length 2048 --output_path /root/autodl-tmp/provenance_weight_training/output/eval/uniform_1_7b_seed123_openwebtext.json && echo '=== OOD Wikipedia ===' && python eval_perplexity.py --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed123/final --data_path data/eval_wikipedia.jsonl --max_docs 5000 --max_length 2048 --output_path /root/autodl-tmp/provenance_weight_training/output/eval/uniform_1_7b_seed123_wikipedia.json && echo '=== Downstream ===' && lm_eval --model hf --model_args pretrained=/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed123/final,dtype=float16 --tasks arc_easy,arc_challenge,hellaswag,piqa,winogrande --batch_size auto --num_fewshot 0 --output_path /root/autodl-tmp/provenance_weight_training/output/eval/uniform_1_7b_seed123_downstream && echo '=== ALL DONE ==='\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"495407\", \"log_path\": \"~/runs/provenance_weight_training/eval_uniform_1_7b_seed123.log\", \"submitted_at\": \"2026-05-20T16:00:49.082Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"detect_remove_q05_epoch_matched\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:48:49.887Z\", \"updated_at\": \"2026-05-20T14:56:11.593Z\", \"conclusion\": \"killed\"}, \"contamination_60_adaptive_seed123_tau08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:38:08.373Z\", \"updated_at\": \"2026-05-20T14:40:42.968Z\", \"hypothesis\": \"Retrain adaptive (ρ=0.6, τ=0.8, seed=123) from scratch on Qwen3-0.6B to obtain checkpoint for OOD+downstream eval. Original contamination_60_seed123 (PPL=17.732) confirmed holdout performance but checkpoint was cleaned up. Paired with seed42/456 for 3-seed τ=0.8 comparison against τ=0.7.\", \"parent\": \"contamination_60_seed123\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_adaptive_seed123_tau08 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"459396\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_adaptive_seed123_tau08.log\", \"submitted_at\": \"2026-05-20T09:40:23.876Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 16294.4, \"gpu_hours\": 4.53}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/contamination_60_adaptive_seed123_tau08/final\", \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.73, \"eval_ppl_openwebtext\": 18.4, \"eval_ppl_wikipedia\": 15.34, \"downstream_arc_easy_acc_norm\": 0.6014, \"downstream_arc_challenge_acc_norm\": 0.3447, \"downstream_hellaswag_acc_norm\": 0.4804, \"downstream_piqa_acc_norm\": 0.6877, \"downstream_winogrande_acc\": 0.5699, \"downstream_mean\": 0.5368}, \"completed_at\": \"2026-05-20T14:11:58.236Z\"}, \"contamination_60_adaptive_seed42_tau08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:38:07.151Z\", \"updated_at\": \"2026-05-20T14:40:41.593Z\", \"hypothesis\": \"Retrain adaptive (ρ=0.6, τ=0.8, seed=42) from scratch on Qwen3-0.6B to obtain checkpoint for OOD+downstream eval. Original contamination_60_seed42_r2 (PPL=17.74) confirmed holdout performance but checkpoint was cleaned up. Paired with seed123/456 for 3-seed τ=0.8 comparison against τ=0.7 (17.735/17.727/17.732).\", \"parent\": \"contamination_60_seed42_r2\", \"spec\": {\"command\": \"python -u training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_adaptive_seed42_tau08 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"459319\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_adaptive_seed42_tau08.log\", \"submitted_at\": \"2026-05-20T09:40:21.580Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 16294.7, \"gpu_hours\": 4.53}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/contamination_60_adaptive_seed42_tau08/final\", \"conclusion\": \"success\", \"metrics\": {\"holdout_ppl\": 17.74, \"eval_ppl_openwebtext\": 18.42, \"eval_ppl_wikipedia\": 15.37, \"downstream_arc_easy_acc_norm\": 0.612, \"downstream_arc_challenge_acc_norm\": 0.3439, \"downstream_hellaswag_acc_norm\": 0.4802, \"downstream_piqa_acc_norm\": 0.685, \"downstream_winogrande_acc\": 0.5777, \"downstream_mean\": 0.5398}, \"completed_at\": \"2026-05-20T14:11:56.312Z\"}, \"adaptive_fix_seed42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T13:32:30.463Z\", \"updated_at\": \"2026-05-20T08:58:53.948Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\", \"parent\": \"adaptive_seed42\", \"notes\": \"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801\", \"failure_reason\": \"\", \"completed_at\": \"\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"D012 代码验证通过（n_min=max(2,batch_size//2), 无EMA, import OK）。等 GPU 释放后提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:26.312269+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:39:45.953045+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_adaptive_fix_seed42.sh\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"109927\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed42.log\", \"submitted_at\": \"2026-05-17T15:01:06.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:39:44.942Z\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.6527, \"downstream_arc_easy_acc_norm\": 0.6157, \"downstream_arc_challenge_acc_norm\": 0.343, \"downstream_hellaswag_acc_norm\": 0.4785, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5777, \"downstream_mean\": 0.5403, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16\", \"eval_ppl_openwebtext\": 18.424, \"eval_ppl_wikipedia\": 15.473}, \"checkpoint_path\": \"output/models/adaptive_fix_seed42/final\", \"eval_ppl_openwebtext\": 18.42, \"eval_ppl_wikipedia\": 15.47}, \"adaptive_rho06_tau07_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:22:15.719Z\", \"updated_at\": \"2026-05-20T08:58:52.243Z\", \"hypothesis\": \"Pure adaptive training at ρ=0.6, τ=0.7, seed=123. Second seed for clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Validates τ=0.7 as universal default across contamination levels.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"383947\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed123.log\", \"submitted_at\": \"2026-05-20T03:31:35.365Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed123/final\", \"train_loss\": 9.352, \"train_runtime_hours\": 3.74, \"wall_clock_seconds\": 16928.5, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:43.870Z\", \"metrics\": {\"holdout_ppl\": 17.727, \"eval_ppl_openwebtext\": 18.385, \"eval_ppl_wikipedia\": 15.329, \"downstream_arc_easy_acc_norm\": 0.5951, \"downstream_arc_challenge_acc_norm\": 0.3422, \"downstream_hellaswag_acc_norm\": 0.4811, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5754, \"downstream_mean\": 0.5361}}, \"adaptive_rho06_tau07_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:22:16.979Z\", \"updated_at\": \"2026-05-20T08:58:50.338Z\", \"hypothesis\": \"Pure adaptive training at ρ=0.6, τ=0.7, seed=456. Third seed completing clean ρ=0.6 τ=0.7 3-seed set. From-scratch Qwen3-0.6B, no checkpoint reuse. Together with seed42/123, enables paired comparison against ρ=0.6 τ=0.8.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"384114\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed456.log\", \"submitted_at\": \"2026-05-20T03:31:37.645Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed456/final\", \"train_loss\": 9.342, \"train_runtime_hours\": 3.72, \"wall_clock_seconds\": 16928.3, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:45.922Z\", \"metrics\": {\"holdout_ppl\": 17.732, \"eval_ppl_openwebtext\": 18.411, \"eval_ppl_wikipedia\": 15.424, \"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3456, \"downstream_hellaswag_acc_norm\": 0.4806, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.562, \"downstream_mean\": 0.5375}}, \"adaptive_rho06_tau07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:19:02.608Z\", \"updated_at\": \"2026-05-20T08:58:48.541Z\", \"hypothesis\": \"Pure adaptive retraining at ρ=0.6, τ=0.7, seed=42. Replaces rho06_tau07_seed42 which was contaminated by hybrid checkpoint. From-scratch training with base Qwen3-0.6B to clean output dir. If PPL < 17.73 (ρ=0.6 τ=0.8 baseline), validates τ=0.7 as universal default across contamination levels.\", \"parent\": \"rho06_tau07_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"383864\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_rho06_tau07_seed42.log\", \"submitted_at\": \"2026-05-20T03:31:32.965Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data_rho06.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_rho06_tau07_seed42/final\", \"train_loss\": 9.358, \"train_runtime_hours\": 3.74, \"wall_clock_seconds\": 16929.0, \"gpu_hours\": 4.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T08:13:41.995Z\", \"metrics\": {\"holdout_ppl\": 17.735, \"eval_ppl_openwebtext\": 18.408, \"eval_ppl_wikipedia\": 15.355, \"downstream_arc_easy_acc_norm\": 0.6132, \"downstream_arc_challenge_acc_norm\": 0.3422, \"downstream_hellaswag_acc_norm\": 0.4807, \"downstream_piqa_acc_norm\": 0.6861, \"downstream_winogrande_acc\": 0.5793, \"downstream_mean\": 0.5403}}, \"adaptive_1_7b_seed42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:51:02.045Z\", \"updated_at\": \"2026-05-20T08:47:34.649Z\", \"hypothesis\": \"Adaptive (dual-constrained) at 1.7B model scale (seed=42, τ=0.8, ρ=0.4). From-scratch on westd-41312. Tests if adaptive advantage holds at larger model scale. v4 replaces v3. Already approved.\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T05:52:27.750Z\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42_v4 --model_name models/Qwen/Qwen3-1.7B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.8 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:1\", \"pid\": 437225, \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_seed42_v4.log\", \"submitted_at\": \"2026-05-20T08:14:12.537Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"N/A (disk full at step 500)\", \"fail_reason\": \"No space left on device (os error 28) at step 500 checkpoint save. /root/autodl-tmp/ 250GB 100% full.\", \"wall_clock_seconds\": 2002.1, \"gpu_hours\": 0.56}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T08:47:34.649Z\"}, \"uniform_1_7b_seed42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T05:50:59.956Z\", \"updated_at\": \"2026-05-20T08:47:26.437Z\", \"hypothesis\": \"Uniform baseline at 1.7B model scale (seed=42). From-scratch training on westd-41312. Provides 1.7B uniform PPL baseline for model scaling comparison. v4 replaces v3 (killed when westd-30476 decommissioned). Already approved.\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T05:52:26.116Z\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && PYTHONUNBUFFERED=1 WANDB_MODE=disabled python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42_v4 --model_name models/Qwen/Qwen3-1.7B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 437143, \"log_path\": \"~/runs/provenance_weight_training/uniform_1_7b_seed42_v4.log\", \"submitted_at\": \"2026-05-20T08:14:10.069Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-1.7B\", \"seed\": 42, \"checkpoint_source\": \"N/A (from-scratch training)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"N/A (disk full at step 500)\", \"fail_reason\": \"No space left on device (os error 28) at step 500 checkpoint save. /root/autodl-tmp/ 250GB 100% full.\", \"wall_clock_seconds\": 1996.4, \"gpu_hours\": 0.55}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T08:47:26.437Z\"}, \"detect_remove_q04_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:57:02.595Z\", \"updated_at\": \"2026-05-20T07:14:37.043Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q04_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q04_seed42.log\", \"data_count\": 136957}, \"hypothesis\": \"D&R threshold t=0.4: keep q≤0.4 samples. Densification point between q03 (31.5%) and q05 (41.4%, PPL=17.28). Helps pinpoint the PPL sweet spot and quantify sensitivity. Part of expanded 9-point D&R threshold curve.\", \"reproduce\": {\"finished_at\": \"2026-05-18T21:34:03.227Z\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.26, \"eval_loss_holdout\": 2.8485, \"downstream_arc_easy_acc_norm\": 0.6107, \"downstream_arc_challenge_acc_norm\": 0.3567, \"downstream_hellaswag_acc_norm\": 0.4819, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5659, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.001, \"eval_ppl_wikipedia\": 15.038}, \"completed_at\": \"2026-05-18T22:01:52.526Z\", \"eval_ppl_openwebtext\": 18, \"eval_ppl_wikipedia\": 15.04}, \"detect_remove_q03_seed42_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:59.443Z\", \"updated_at\": \"2026-05-20T07:14:34.819Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q03.jsonl --output_dir /root/autodl-tmp/output/models/detect_remove_q03_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_total_limit 3 --logging_steps 10 --save_steps 500'\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"59986\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q03_seed42_r2.log\", \"submitted_at\": \"2026-05-18T17:56:58.742Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q03.jsonl\", \"data_count\": 116935, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q03_seed42_r2/checkpoint-6103\", \"wall_clock_seconds\": 14691.7, \"gpu_hours\": 4.08}, \"hypothesis\": \"D&R threshold t=0.3: keep q≤0.3 (116,935 samples, 31.5%). Second most aggressive filtering level. Part of 9-point D&R sensitivity curve (q01-q09). Previous attempt failed (python: command not found). Rerun on westd-30476.\", \"reproduce\": {\"finished_at\": \"2026-05-18T21:31:12.021Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:31:16.535916+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.25, \"eval_loss_holdout\": 2.848, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3549, \"downstream_hellaswag_acc_norm\": 0.4851, \"downstream_piqa_acc_norm\": 0.6872, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.004, \"eval_ppl_wikipedia\": 15.037}, \"completed_at\": \"2026-05-18T22:01:50.398Z\", \"eval_ppl_openwebtext\": 18, \"eval_ppl_wikipedia\": 15.04}, \"detect_remove_q08_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:53:26.593Z\", \"updated_at\": \"2026-05-20T07:14:32.824Z\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_filtered_q08.jsonl --output_dir .../detect_remove_q08_seed42 --weighting_method uniform --seed 42\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"pid\": 248002, \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q08_seed42.log\", \"submitted_at\": \"2026-05-18T19:53:26.126Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q08.jsonl\", \"data_count\": 202455, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 14855.4, \"gpu_hours\": 4.13}, \"hypothesis\": \"D&R threshold t=0.8: keep q≤0.8 samples (~210K). Lenient filtering near q09 (228K). Part of 9-point D&R sensitivity curve. Expected PPL between q07 (17.32) and q09 (17.42) confirming right side of U-shape.\", \"reproduce\": {\"finished_at\": \"2026-05-18T23:28:13.145Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T23:28:18.092622+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.3442, \"eval_loss_holdout\": 2.8533, \"downstream_arc_easy_acc_norm\": 0.6086, \"downstream_arc_challenge_acc_norm\": 0.3592, \"downstream_hellaswag_acc_norm\": 0.4855, \"downstream_piqa_acc_norm\": 0.6937, \"downstream_winogrande_acc\": 0.5817, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_ppl_openwebtext\": 18.039, \"eval_ppl_wikipedia\": 15.066}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q08_seed42/final\", \"completed_at\": \"2026-05-19T00:01:01.571Z\", \"downstream_arc_easy\": 0.6086, \"downstream_arc_challenge\": 0.3592, \"downstream_hellaswag\": 0.4855, \"downstream_piqa\": 0.6937, \"downstream_winogrande\": 0.5817, \"downstream_mean\": 0.5457, \"eval_ppl_openwebtext\": 18.04, \"eval_ppl_wikipedia\": 15.07}, \"adaptive_1_7b_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-20T04:49:58.165Z\", \"updated_at\": \"2026-05-20T05:50:47.354Z\", \"hypothesis\": \"Adaptive (dual-constrained) at 1.7B model scale (seed=42, τ=0.8, ρ=0.4). Paired with uniform_1_7b_seed42_v3 to test if adaptive advantage holds at larger model scale. Key for model scaling claim in paper.\", \"server\": \"westd-30476\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-30476\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T04:50:57.591Z\"}, \"completed_at\": \"2026-05-20T05:38:50.468Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"conclusion\": \"killed\", \"spec\": {\"kill_reason\": \"westd-30476 已注销，checkpoint 丢失\"}}, \"uniform_1_7b_seed42_v3\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-20T04:49:30.213Z\", \"updated_at\": \"2026-05-20T05:50:45.424Z\", \"hypothesis\": \"Uniform baseline at 1.7B model scale (seed=42). Provides 1.7B uniform PPL baseline for model scaling comparison. Previous uniform_1_7b_seed42 failed; this is a clean re-run on westd-30476 with verified model weights.\", \"server\": \"westd-30476\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-30476\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T04:50:55.085Z\"}, \"completed_at\": \"2026-05-20T05:38:48.621Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"conclusion\": \"killed\", \"spec\": {\"kill_reason\": \"westd-30476 已注销，checkpoint 丢失\"}}, \"detect_remove_q01_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T06:48:51.429Z\", \"updated_at\": \"2026-05-20T05:04:46.527Z\", \"hypothesis\": \"D&R extreme threshold q>0.1: removes all samples with q_score>0.1, keeping only the most confidently clean data. Tests D&R sensitivity to threshold — if PPL degrades severely, filtering is too aggressive and most data is discarded. Paired with q>0.3/0.5/0.7/0.9 to map the full threshold-PPL curve, showing adaptive avoids this calibration problem entirely.\", \"reproduce\": {\"finished_at\": \"2026-05-18T14:54:29.368Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"completed_at\": \"2026-05-18T14:54:33.151Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:54:38.690732+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q01.jsonl --weighting_method uniform --num_train_tokens 200000000 --seed 42\", \"server\": \"westd-30476\", \"data_path\": \"data/scored_data_filtered_q01.jsonl\", \"data_count\": 55799, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"gpu\": \"cuda:3\", \"note\": \"Cron 误报 failed (M025)，实际仍在训练 ~48%\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q01_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q01_seed42.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.4, \"eval_ppl_openwebtext\": 18.22, \"eval_ppl_wikitext\": 28.22}, \"conclusion\": \"success\"}, \"detect_remove_q03_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:04:05.454Z\", \"updated_at\": \"2026-05-20T05:04:45.643Z\", \"spec\": {\"command\": \"D&R q03 seed456 on 30476\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:1\"], \"pid\": \"76791\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q03_seed456.log\", \"submitted_at\": \"2026-05-18T22:04:04.680Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q03.jsonl\", \"data_count\": 116935, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"wall_clock_seconds\": 13846.2, \"gpu_hours\": 3.85}, \"hypothesis\": \"D&R threshold t=0.3 seed456: cross-seed replication of q03 sweet spot (PPL=17.25 at seed42). Third seed for 3-seed mean and variance estimate at the D&R optimal threshold.\", \"reproduce\": {\"finished_at\": \"2026-05-19T01:38:41.994Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T01:38:47.039510+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.2509, \"eval_loss_holdout\": 2.8479, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"train_loss\": 11.255, \"total_steps\": 6103, \"eval_ppl_openwebtext\": 18.03, \"eval_ppl_wikitext\": 27.61}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q03_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:54:50.846Z\"}, \"detect_remove_q03_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:04:03.208Z\", \"updated_at\": \"2026-05-20T05:04:43.723Z\", \"spec\": {\"command\": \"D&R q03 seed123 on 30476\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"76714\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q03_seed123.log\", \"submitted_at\": \"2026-05-18T22:04:02.773Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q03.jsonl\", \"data_count\": 116935, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q03_seed123/final\", \"wall_clock_seconds\": 13059, \"gpu_hours\": 3.63}, \"hypothesis\": \"Cross-seed replication of D&R q03 sweet spot: if seed123 reproduces seed42's PPL=17.25 (the U-curve optimum), q03 is a robust threshold, not a seed42 artifact. Two seeds converging validates the U-shape minimum at q03-q04.\", \"reproduce\": {\"finished_at\": \"2026-05-19T01:43:26.091Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T01:43:31.103456+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.25, \"eval_loss_holdout\": 2.8479, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 6103, \"train_loss_final\": 11.2441, \"train_runtime_s\": 13059, \"epoch\": 0.84, \"eval_ppl_openwebtext\": 18.03, \"eval_ppl_wikitext\": 27.53}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T01:49:44.145Z\"}, \"detect_remove_q05_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:46:10.870Z\", \"updated_at\": \"2026-05-20T05:04:41.870Z\", \"hypothesis\": \"Detect-and-remove baseline with q>0.5 threshold and seed=456 will produce similar PPL to seed42 (17.29), confirming reproducibility of the filtering approach across seeds.\", \"parent\": \"\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/output/models/detect_remove_q05_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/output/models/detect_remove_q05_seed456/checkpoint-500\", \"server\": \"westd-30476\", \"gpu\": 1, \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"models/Qwen/Qwen3-0.6B\", \"seed\": 456, \"weighting_method\": \"uniform\", \"threshold\": 0.5, \"max_steps\": 6103, \"pid\": 26855, \"output_dir\": \"/root/autodl-tmp/output/models/detect_remove_q05_seed456\", \"tmux_session\": \"detect_remove_q05_seed456\", \"total_steps\": 6103, \"estimated_time\": \"3.5h\", \"note\": \"Resumed from checkpoint-500 after killing PID 25514 (from-scratch run without --resume_from_checkpoint) and PID 13654 (had extra --eval_data_path causing slowdown)\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q05_seed456\", \"log_path\": \"/root/autodl-tmp/output/models/detect_remove_q05_seed456/training.log\", \"resumed_from\": \"checkpoint-500\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T12:59:17.900Z\", \"metrics\": {\"eval_ppl_holdout\": 17.28, \"eval_loss_holdout\": 2.8493, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_ppl_openwebtext\": 18.01, \"eval_ppl_wikitext\": 27.68}}, \"detect_remove_q05_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:46:09.441Z\", \"updated_at\": \"2026-05-20T05:04:40.013Z\", \"hypothesis\": \"Uniform weighting on q05-filtered data (contamination removed) with seed 123 will show different convergence behavior compared to provenance-weighted training, serving as a detection baseline for measuring the effect of removing contaminated data.\", \"parent\": \"\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/output/models/detect_remove_q05_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-30476\", \"gpu\": \"0\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 200000000, \"model_name\": \"models/Qwen/Qwen3-0.6B\", \"seed\": 123, \"pid\": 22336, \"output_dir\": \"/root/autodl-tmp/output/models/detect_remove_q05_seed123\", \"log_path\": \"/root/autodl-tmp/output/models/detect_remove_q05_seed123.log\", \"weighting_method\": \"uniform\", \"num_train_tokens\": 200000000, \"learning_rate\": 5e-05, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q05_seed123\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T12:59:14.465Z\", \"metrics\": {\"eval_ppl_holdout\": 17.27, \"eval_loss_holdout\": 2.8491, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_ppl_openwebtext\": 18.01, \"eval_ppl_wikitext\": 27.75}}, \"detect_remove_q02_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:47:54.392Z\", \"updated_at\": \"2026-05-20T05:04:38.545Z\", \"spec\": {\"command\": \"detect_remove_q02_seed42 training\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"65827\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q02_seed42.log\", \"submitted_at\": \"2026-05-18T19:47:54.017Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q02_seed42/final\", \"data_count\": 91654, \"data_path\": \"data/scored_data_filtered_q02.jsonl\", \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 13347.2, \"gpu_hours\": 3.71}, \"reproduce\": {\"finished_at\": \"2026-05-18T23:22:37.551Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T23:22:43.918775+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.27, \"eval_loss_holdout\": 2.8491, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 (final checkpoint)\", \"train_loss\": 11.348, \"train_steps\": 6103, \"data_count\": 91654, \"eval_ppl_openwebtext\": 18.06, \"eval_ppl_wikitext\": 27.64}, \"conclusion\": \"success\", \"hypothesis\": \"D&R q>0.2 threshold retains ~23% of data (q_score<=0.2). Maps the left side of the U-curve between q01(17.40) and q03(17.25). If PPL closer to q03 than q01, the steep rise only occurs at extreme filtering (q01). If closer to q01, the left branch rises steeply from q03 onward.\", \"completed_at\": \"2026-05-18T23:30:21.249Z\"}, \"epoch_matched_dr_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:14:29.174Z\", \"updated_at\": \"2026-05-20T05:04:36.608Z\", \"hypothesis\": \"Cross-seed confirmation of D080: epoch-matched D&R (1 content epoch, ~83M tokens) will produce PPL similar to adaptive (~17.65), proving D&R's apparent 0.36 PPL advantage over adaptive is entirely from multi-epoch training, not data quality filtering. Seed 456 for 3-seed significance.\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/output/models/epoch_matched_dr_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 83000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --bf16 --save_only_model --save_total_limit 3\", \"server\": \"westd-30476\", \"gpu\": 1, \"pid\": \"unknown\", \"log_path\": \"~/runs/provenance_weight_training/epoch_matched_dr_seed456.log\", \"submitted_at\": \"2026-05-18T14:15:10.126Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"output_dir\": \"/root/autodl-tmp/output/models/epoch_matched_dr_seed456\", \"num_train_tokens\": 83000000, \"weighting_method\": \"uniform\", \"wall_clock_seconds\": 2350.3, \"gpu_hours\": 0.65}, \"reproduce\": {\"finished_at\": \"2026-05-18T14:54:03.288Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:54:20.380Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:54:25.712372+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8712, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\", \"eval_ppl_openwebtext\": 18.27, \"eval_ppl_wikitext\": 28.14}}, \"epoch_matched_dr_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:14:28.033Z\", \"updated_at\": \"2026-05-20T05:04:34.758Z\", \"hypothesis\": \"Cross-seed confirmation of D080: epoch-matched D&R (1 content epoch, ~83M tokens) will produce PPL similar to adaptive (~17.65), proving D&R's apparent 0.36 PPL advantage over adaptive is entirely from multi-epoch training, not data quality filtering. Seed 123 for 3-seed significance.\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/output/models/epoch_matched_dr_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 83000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --bf16 --save_only_model --save_total_limit 3\", \"server\": \"westd-30476\", \"gpu\": 0, \"pid\": \"unknown\", \"log_path\": \"~/runs/provenance_weight_training/epoch_matched_dr_seed123.log\", \"submitted_at\": \"2026-05-18T14:15:07.644Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"output_dir\": \"/root/autodl-tmp/output/models/epoch_matched_dr_seed123\", \"num_train_tokens\": 83000000, \"weighting_method\": \"uniform\", \"wall_clock_seconds\": 2321.3, \"gpu_hours\": 0.64}, \"reproduce\": {\"finished_at\": \"2026-05-18T14:53:34.631Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T14:53:48.912Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T14:53:58.046964+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=127 (command not found)，训练在 step ~201/2532 后中断。wall_clock=2321s 但日志仅记录到 ~7min。已派 Worker worker_diagnose_epoch_matched_dr_seed123_20260518T145604 深查。\", \"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8713, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\", \"eval_ppl_openwebtext\": 18.3, \"eval_ppl_wikitext\": 27.9}}, \"eval_q04\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:49:30.129Z\", \"updated_at\": \"2026-05-20T04:49:10.488Z\", \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints /root/autodl-tmp/output/models/detect_remove_q04_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:1\"], \"pid\": \"75261\", \"log_path\": \"~/runs/provenance_weight_training/eval_q04.log\", \"submitted_at\": \"2026-05-18T21:49:29.738Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"detect_remove_q04_seed42\", \"seed\": 42, \"checkpoint_source\": \"detect_remove_q04_seed42\", \"eval_data\": \"human/eval_holdout.jsonl\", \"wall_clock_seconds\": 109387.9, \"gpu_hours\": 30.39}, \"metrics\": {\"loss\": 2.8485, \"perplexity\": 17.2626, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.8, \"downstream_arc_easy_acc_norm\": 0.6107, \"downstream_arc_challenge_acc_norm\": 0.3567, \"downstream_hellaswag_acc_norm\": 0.4819, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5659, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q04_seed42/final\", \"log_path\": \"/tmp/eval_q04.log\", \"hypothesis\": \"Detect-remove at q=0.4 threshold should show lower PPL than epoch-matched baseline, with slightly higher PPL than q=0.3 due to retaining more borderline-quality documents.\", \"completed_at\": \"2026-05-20T04:12:37.643Z\"}, \"eval_q03_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:49:14.814Z\", \"updated_at\": \"2026-05-20T04:47:07.748Z\", \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints /root/autodl-tmp/output/models/detect_remove_q03_seed42_r2/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"75089\", \"log_path\": \"~/runs/provenance_weight_training/eval_q03_r2.log\", \"submitted_at\": \"2026-05-18T21:49:14.346Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"detect_remove_q03_seed42_r2\", \"seed\": 42, \"checkpoint_source\": \"detect_remove_q03_seed42_r2\", \"eval_data\": \"human/eval_holdout.jsonl\", \"wall_clock_seconds\": 109401.5, \"gpu_hours\": 30.39}, \"metrics\": {\"loss\": 2.848, \"perplexity\": 17.2538, \"num_tokens\": 4077068, \"elapsed_seconds\": 111, \"downstream_arc_easy_acc_norm\": 0.6301, \"downstream_arc_challenge_acc_norm\": 0.3549, \"downstream_hellaswag_acc_norm\": 0.4851, \"downstream_piqa_acc_norm\": 0.6872, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q03_seed42_r2/final\", \"log_path\": \"/tmp/eval_q03_r2.log\", \"hypothesis\": \"Detect-remove at q=0.3 threshold (r2 rerun) should show lower PPL than epoch-matched baseline because aggressive filtering removes more low-quality synthetic data while retaining high-provenance human content.\", \"completed_at\": \"2026-05-20T04:12:35.816Z\"}, \"eval_rho06_batch_v7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:09:06.933Z\", \"updated_at\": \"2026-05-20T04:14:19.316Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 python eval_perplexity.py --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_ess_only_seed123/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_ess_only_seed456/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_random_seed123/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_random_seed456/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048 2>&1 | tee /tmp/eval_rho06_batch.log\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"213243\", \"log_path\": \"~/runs/provenance_weight_training/eval_rho06_batch_v7.log\", \"submitted_at\": \"2026-05-18T12:09:06.600Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 144312.7, \"gpu_hours\": 40.09}, \"metrics\": {\"contamination_60_ess_only_seed123\": {\"loss\": 2.8771, \"perplexity\": 17.76, \"tokens\": 4077068}, \"contamination_60_ess_only_seed456\": {\"loss\": 2.8771, \"perplexity\": 17.76, \"tokens\": 4077068}, \"contamination_60_random_seed123\": {\"loss\": 2.8832, \"perplexity\": 17.87, \"tokens\": 4077068}, \"contamination_60_random_seed456\": {\"loss\": 2.8837, \"perplexity\": 17.88, \"tokens\": 4077068}, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048}, \"hypothesis\": \"Contamination-aware weighting (rho=0.6) with ESS-only vs random selection should show different perplexity on held-out human text, with ESS-only selection better capturing human-like text distribution.\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/contamination_60_*/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T04:14:19.316Z\"}, \"eval_q01_final_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:18:30.245Z\", \"updated_at\": \"2026-05-20T04:12:43.210Z\", \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints /root/autodl-tmp/output/models/detect_remove_q01_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"64426\", \"log_path\": \"~/runs/provenance_weight_training/eval_q01_final_v2.log\", \"submitted_at\": \"2026-05-18T19:18:29.874Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"detect_remove_q01_seed42\", \"seed\": 42, \"checkpoint_source\": \"detect_remove_q01_seed42\", \"eval_data\": \"human/eval_holdout.jsonl\", \"wall_clock_seconds\": 118453.3, \"gpu_hours\": 32.9}, \"metrics\": {\"loss\": 2.8563, \"perplexity\": 17.3965, \"num_tokens\": 4077068, \"elapsed_seconds\": 105.1}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q01_seed42/final\", \"log_path\": \"/tmp/eval_q01.log\", \"hypothesis\": \"Detect-remove at q=0.1 (most aggressive filtering) should show the lowest PPL among all thresholds if data quality dominates, or degraded PPL if the severe data reduction causes underfitting.\", \"completed_at\": \"2026-05-20T04:12:43.210Z\"}, \"eval_q07_final\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:33:23.528Z\", \"updated_at\": \"2026-05-20T04:12:41.391Z\", \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints /root/autodl-tmp/output/models/detect_remove_q07_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"59032\", \"log_path\": \"~/runs/provenance_weight_training/eval_q07_final.log\", \"submitted_at\": \"2026-05-18T17:33:23.135Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"detect_remove_q07_seed42\", \"seed\": 42, \"checkpoint_source\": \"detect_remove_q07_seed42\", \"eval_data\": \"human/eval_holdout.jsonl\", \"wall_clock_seconds\": 124758.3, \"gpu_hours\": 34.66}, \"metrics\": {\"loss\": 2.8519, \"perplexity\": 17.3201, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.8}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q07_seed42/final\", \"log_path\": \"/tmp/eval_q07.log\", \"hypothesis\": \"Detect-remove at q=0.7 threshold should show lower PPL than epoch-matched baseline, with the PPL gap narrowing as higher thresholds retain more data including lower-provenance documents.\", \"completed_at\": \"2026-05-20T04:12:41.391Z\"}, \"eval_q06\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:49:17.026Z\", \"updated_at\": \"2026-05-20T04:12:39.559Z\", \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints /root/autodl-tmp/output/models/detect_remove_q06_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"75168\", \"log_path\": \"~/runs/provenance_weight_training/eval_q06.log\", \"submitted_at\": \"2026-05-18T21:49:16.263Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"detect_remove_q06_seed42\", \"seed\": 42, \"checkpoint_source\": \"detect_remove_q06_seed42\", \"eval_data\": \"human/eval_holdout.jsonl\", \"wall_clock_seconds\": 109403.3, \"gpu_hours\": 30.39}, \"metrics\": {\"loss\": 2.8507, \"perplexity\": 17.2993, \"num_tokens\": 4077068, \"elapsed_seconds\": 106.9}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q06_seed42/final\", \"log_path\": \"/tmp/eval_q06.log\", \"hypothesis\": \"Detect-remove at q=0.6 threshold should show lower PPL than epoch-matched baseline but higher than q=0.3/0.4 as the less aggressive filtering retains more synthetic-origin content.\", \"completed_at\": \"2026-05-20T04:12:39.559Z\"}, \"eval_epoch_matched_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:33:21.793Z\", \"updated_at\": \"2026-05-20T04:12:33.833Z\", \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints /root/autodl-tmp/output/models/epoch_matched_dr_seed456/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:1\"], \"pid\": \"58952\", \"log_path\": \"~/runs/provenance_weight_training/eval_epoch_matched_seed456.log\", \"submitted_at\": \"2026-05-18T17:33:21.443Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"epoch_matched_dr_seed456\", \"seed\": 456, \"checkpoint_source\": \"epoch_matched_dr_seed456\", \"eval_data\": \"human/eval_holdout.jsonl\", \"wall_clock_seconds\": 124752.4, \"gpu_hours\": 34.65}, \"metrics\": {\"loss\": 2.8712, \"perplexity\": 17.6574, \"num_tokens\": 4077068, \"elapsed_seconds\": 103.6}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/epoch_matched_dr_seed456/final\", \"log_path\": \"/tmp/eval_epoch_seed456.log\", \"hypothesis\": \"Epoch-matched detect-remove baseline (seed456) should achieve similar held-out PPL as seed123, confirming reproducibility of the epoch-matched baseline across random seeds.\", \"completed_at\": \"2026-05-20T04:12:33.833Z\"}, \"eval_epoch_matched_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:33:20.074Z\", \"updated_at\": \"2026-05-20T04:12:31.028Z\", \"spec\": {\"command\": \"python eval_perplexity.py --checkpoints /root/autodl-tmp/output/models/epoch_matched_dr_seed123/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"58873\", \"log_path\": \"~/runs/provenance_weight_training/eval_epoch_matched_seed123.log\", \"submitted_at\": \"2026-05-18T17:33:19.707Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"epoch_matched_dr_seed123\", \"seed\": 123, \"checkpoint_source\": \"epoch_matched_dr_seed123\", \"eval_data\": \"human/eval_holdout.jsonl\", \"wall_clock_seconds\": 124751.3, \"gpu_hours\": 34.65}, \"metrics\": {\"loss\": 2.8713, \"perplexity\": 17.6599, \"num_tokens\": 4077068, \"elapsed_seconds\": 104.3}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/epoch_matched_dr_seed123/final\", \"log_path\": \"/tmp/eval_epoch_seed123.log\", \"hypothesis\": \"Epoch-matched detect-remove baseline (seed123) should achieve similar held-out PPL as uniform training, confirming that matched training budget controls for compute rather than data filtering effects.\", \"completed_at\": \"2026-05-20T04:12:31.028Z\"}, \"eval_ngram_uniform\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:52.785Z\", \"updated_at\": \"2026-05-20T04:04:40.459Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && python eval_perplexity.py --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"243502\", \"log_path\": \"~/runs/provenance_weight_training/eval_ngram_uniform.log\", \"submitted_at\": \"2026-05-18T19:15:52.408Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 118128.1, \"gpu_hours\": 32.81}, \"metrics\": {\"loss\": 2.8733, \"perplexity\": 17.69, \"tokens\": 4077068, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048, \"checkpoint\": \"ngram_uniform_seed42/final\"}, \"hypothesis\": \"Uniform n-gram weighting treats all documents equally regardless of n-gram rarity, serving as a baseline to compare against adaptive weighting for held-out human text perplexity.\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T04:04:40.459Z\"}, \"eval_ngram_adaptive\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:51.010Z\", \"updated_at\": \"2026-05-20T04:02:52.006Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && python eval_perplexity.py --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"243422\", \"log_path\": \"~/runs/provenance_weight_training/eval_ngram_adaptive.log\", \"submitted_at\": \"2026-05-18T19:15:50.620Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 118021.4, \"gpu_hours\": 32.78}, \"metrics\": {\"loss\": 2.8803, \"perplexity\": 17.82, \"tokens\": 4077068, \"eval_data\": \"data/human/eval_holdout.jsonl\", \"max_docs\": 5000, \"max_length\": 2048, \"checkpoint\": \"ngram_adaptive_seed42/final\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final\", \"hypothesis\": \"N-gram adaptive weighting assigns higher weights to documents with rare n-gram patterns, which should yield lower perplexity on held-out human text compared to uniform weighting by better capturing the distribution of natural language.\", \"completed_at\": \"2026-05-20T04:02:52.006Z\"}, \"uniform_seed42_downstream\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T03:31:40.139Z\", \"updated_at\": \"2026-05-20T03:56:46.798Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python -m lm_eval --model hf --model_args pretrained=/root/autodl-tmp/provenance_weight_training/output/models/qwen06b_uniform_seed42_v2/final,dtype=float16 --tasks arc_easy,arc_challenge,hellaswag,piqa,winogrande --batch_size auto --num_fewshot 0 --output_path /root/autodl-tmp/provenance_weight_training/output/eval_results/uniform_seed42_downstream\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"384367\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed42_downstream.log\", \"submitted_at\": \"2026-05-20T03:31:39.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"qwen06b_uniform_seed42\", \"eval_data\": \"arc_easy,arc_challenge,hellaswag,piqa,winogrande (0-shot)\", \"data_path\": \"lm_eval built-in benchmarks\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen3-0.6B (uniform baseline)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/qwen06b_uniform_seed42_v2/final\", \"wall_clock_seconds\": 1504.9, \"gpu_hours\": 0.42}, \"hypothesis\": \"Downstream benchmark eval (ARC-Easy/Challenge, HellaSwag, PIQA, WinoGrande) for uniform_seed42 baseline. Completes 3-seed uniform downstream comparison needed for Table in paper.\", \"parent\": \"qwen06b_uniform_seed42\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T03:56:44.553Z\", \"metrics\": {\"downstream_arc_easy_acc_norm\": 0.6128, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4836, \"downstream_piqa_acc_norm\": 0.6877, \"downstream_winogrande_acc\": 0.5856, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}}, \"adaptive_fromscratch_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T18:50:48.052Z\", \"updated_at\": \"2026-05-20T03:32:28.070Z\", \"hypothesis\": \"From-scratch adaptive (no resume artifact) at seed42 to complete 3-seed consistent dataset. If in-dist PPL matches seed123/456 range (~17.677-17.683) and OOD shows no reversal, distribution matching was a resume artifact.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --seed 42 (from-scratch, no resume)\", \"server\": \"westd-41312\", \"gpu\": \"cuda:0\", \"pid\": 337777, \"log_path\": \"~/runs/provenance_weight_training/adaptive_fromscratch_seed42.log\", \"submitted_at\": \"2026-05-19T18:52:11.626Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 6103, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (from-scratch training, not eval)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fromscratch_seed42/final\", \"wall_clock_seconds\": 31216.4, \"gpu_hours\": 8.67}, \"reproduce\": {\"finished_at\": \"2026-05-19T22:42:07.612Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T22:42:12.912658+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fromscratch_seed42/final\", \"metrics\": {\"train_loss\": 9.976, \"eval_ppl_holdout\": 17.689, \"eval_ppl_openwebtext\": 18.37, \"eval_ppl_wikipedia\": 15.349, \"downstream_arc_easy_acc_norm\": 0.6178, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4806, \"downstream_piqa_acc_norm\": 0.6844, \"downstream_winogrande_acc\": 0.5801, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"training_time_s\": 13660}, \"conclusion\": \"success\", \"log_path\": \"/tmp/eval_fromscratch_seed42.log\", \"completed_at\": \"2026-05-20T03:32:28.071Z\"}, \"hybrid_rho06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:24:56.795Z\", \"updated_at\": \"2026-05-20T03:22:56.658Z\", \"spec\": {\"hypothesis\": \"Hybrid filter+reweight at ρ=0.6: remove q>0.95, then adaptive reweight. Tests if hybrid approach scales to higher contamination.\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.6, \"data_count\": 244502, \"command\": \"bash scripts/run_hybrid_rho06_seed42.sh\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data_hybrid_rho06.jsonl\", \"gpu\": \"cuda:3\", \"pid\": 3727, \"tau\": 0.7, \"n_min\": 2, \"weighting_method\": \"adaptive\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T00:17:27.859Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T00:17:28.940Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T00:17:34.914461+00:00\"}]}, \"metrics\": {\"eval_loss_holdout\": 2.8637, \"eval_ppl_holdout\": 17.526, \"eval_ppl_openwebtext\": 18.208, \"eval_ppl_wikipedia\": 15.267, \"downstream_arc_easy_acc_norm\": 0.6208, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4801, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5785, \"eval_source\": \"rho06_tau07_seed42 eval worker - evaluated hybrid checkpoint by mistake\"}, \"hypothesis\": \"Hybrid filter+reweight on ρ=0.6: remove q>0.95 samples (extreme outliers) then apply adaptive reweighting to remainder. At higher contamination, extreme outliers distort ESS more severely, so pre-filtering should yield larger relative improvement over pure-adaptive than at ρ=0.4.\", \"parent\": \"hybrid_rho04_seed42\"}, \"rho06_tau07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:19:11.044Z\", \"updated_at\": \"2026-05-20T03:20:40.603Z\", \"hypothesis\": \"Adaptive at ρ=0.6 with τ=0.7 (seed=42). results.tex L97 claims τ=0.7 optimal at ρ=0.6 but lacks complete eval. If PPL < current ρ=0.6 τ=0.8 result (17.73 batch_adaptive or hybrid 17.53), validates τ=0.7 as universal default across contamination levels.\", \"spec\": {\"command\": \"python train.py --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --seed 42 --max_steps 6103 --batch_size 4 --learning_rate 5e-05 --model_name Qwen/Qwen3-0.6B\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/hybrid_rho06_seed42/step_metrics.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/hybrid_rho06_seed42/final\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:16:49.813Z\", \"metrics\": {\"eval_ppl_holdout\": 17.526, \"eval_ppl_openwebtext\": 18.208, \"eval_ppl_wikipedia\": 15.267, \"downstream_arc_easy_acc_norm\": 0.6208, \"downstream_arc_challenge_acc_norm\": 0.3524, \"downstream_hellaswag_acc_norm\": 0.4801, \"downstream_piqa_acc_norm\": 0.6931, \"downstream_winogrande_acc\": 0.5785}}, \"tau07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:48:42.641Z\", \"updated_at\": \"2026-05-20T03:03:58.338Z\", \"hypothesis\": \"τ=0.7 sensitivity test (seed=42, ρ=0.4). Third seed for τ=0.7, completing 3-seed set (42/123/456) to match τ=0.8's 3 seeds. Enables paired 3-seed comparison for R3-N2 τ sensitivity response.\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --seed 42\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"tau\": 0.7, \"n_min\": null, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"weighting_method\": \"adaptive\", \"log_path\": \"~/runs/provenance_weight_training/tau07_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/tau07_seed42/final\"}, \"metrics\": {\"eval_ppl_holdout\": 17.68, \"eval_ppl_openwebtext\": 18.348, \"eval_ppl_wikipedia\": 15.331, \"downstream_arc_easy_acc_norm\": 0.6166, \"downstream_arc_challenge_acc_norm\": 0.3473, \"downstream_hellaswag_acc_norm\": 0.4795, \"downstream_piqa_acc_norm\": 0.6861, \"downstream_winogrande_acc\": 0.5817, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/tau07_seed42/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T03:03:58.338Z\"}, \"tau07_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:44:04.805Z\", \"updated_at\": \"2026-05-20T03:03:31.130Z\", \"hypothesis\": \"τ=0.7 sensitivity test (seed=456, ρ=0.4). R3-N2 requires multi-seed τ sensitivity data. Paired with tau07_seed123 for 2-seed mean±std at τ=0.7. Direct comparison against adaptive_ood_seed456 (τ=0.8, same seed) isolates τ effect.\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data.jsonl --output_dir output/models/tau07_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"344534\", \"log_path\": \"~/runs/provenance_weight_training/tau07_seed456.log\", \"submitted_at\": \"2026-05-19T20:46:27.554Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"tau\": 0.7, \"n_min\": 2, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"weighting_method\": \"adaptive\", \"wall_clock_seconds\": 22623.6, \"gpu_hours\": 6.28}, \"metrics\": {\"eval_ppl_holdout\": 17.677, \"eval_ppl_openwebtext\": 18.344, \"eval_ppl_wikipedia\": 15.315, \"downstream_arc_easy_acc_norm\": 0.6111, \"downstream_arc_challenge_acc_norm\": 0.3515, \"downstream_hellaswag_acc_norm\": 0.4811, \"downstream_piqa_acc_norm\": 0.6834, \"downstream_winogrande_acc\": 0.5722, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/tau07_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T03:03:31.130Z\"}, \"tau07_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T20:44:02.827Z\", \"updated_at\": \"2026-05-20T03:03:29.289Z\", \"hypothesis\": \"τ=0.7 sensitivity test (seed=123, ρ=0.4). R3-N2 requires multi-seed τ sensitivity data. Currently have τ=0.8 × 3 seeds. Adding τ=0.7 × 2 seeds enables direct paired comparison: if τ=0.7 degrades PPL vs τ=0.8 at same seed, confirms τ=0.8 is near-optimal. If equivalent, suggests robustness to τ choice.\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data.jsonl --output_dir output/models/tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"344455\", \"log_path\": \"~/runs/provenance_weight_training/tau07_seed123.log\", \"submitted_at\": \"2026-05-19T20:46:25.278Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"tau\": 0.7, \"n_min\": 2, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"weighting_method\": \"adaptive\", \"wall_clock_seconds\": 22624.0, \"gpu_hours\": 6.28}, \"metrics\": {\"eval_ppl_holdout\": 17.666, \"eval_ppl_openwebtext\": 18.348, \"eval_ppl_wikipedia\": 15.345, \"downstream_arc_easy_acc_norm\": 0.6309, \"downstream_arc_challenge_acc_norm\": 0.3481, \"downstream_hellaswag_acc_norm\": 0.4775, \"downstream_piqa_acc_norm\": 0.6866, \"downstream_winogrande_acc\": 0.5675, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\", \"eval_method\": \"eval_ppl_ood.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/tau07_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T03:03:29.289Z\"}, \"tau07_downstream_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:19:08.294Z\", \"updated_at\": \"2026-05-20T03:02:14.151Z\", \"hypothesis\": \"Downstream eval for τ=0.7 (3 seeds). Paper switched main results to τ=0.7; must confirm downstream benchmarks match or exceed τ=0.8 and uniform. Reviewer will ask for downstream under recommended setting.\", \"spec\": {\"command\": \"lm_eval --model hf --tasks arc_easy,arc_challenge,hellaswag,piqa,winogrande on tau07_seed{42,123,456}\", \"server\": \"westd-41312\", \"data_path\": \"tau07_seed{42,123,456}/final\", \"data_count\": 5, \"model_name\": \"Qwen/Qwen3-0.6B (τ=0.7)\", \"seed\": 0, \"checkpoint_source\": \"tau07_seed42/123/456\", \"eval_data\": \"arc_easy,arc_challenge,hellaswag,piqa,winogrande\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T03:02:14.151Z\"}, \"uniform_ood_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:34:32.747Z\", \"updated_at\": \"2026-05-19T20:08:50.226Z\", \"hypothesis\": \"Retrain uniform (b=0, seed=123) with checkpoint saving for OOD eval. If in-dist PPL matches original 17.686 (±0.01), the checkpoint is valid for OOD generalization testing across OpenWebText/Wikipedia/FineWeb.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method uniform --seed 123\", \"server\": \"westd-41312\", \"gpu\": \"cuda:2\", \"pid\": 313437, \"log_path\": \"~/runs/provenance_weight_training/uniform_ood_seed123.log\", \"submitted_at\": \"2026-05-19T14:37:08.809Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 6103, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"wall_clock_seconds\": 14841.9, \"gpu_hours\": 4.12}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:09:16.577Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:09:21.547740+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.6861, \"eval_ppl_openwebtext\": 18.3678, \"eval_ppl_wikipedia\": 15.3768, \"downstream_arc_easy_acc_norm\": 0.6229, \"downstream_arc_challenge_acc_norm\": 0.3507, \"downstream_hellaswag_acc_norm\": 0.4797, \"downstream_piqa_acc_norm\": 0.685, \"downstream_winogrande_acc\": 0.5762, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_ood_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:44:30.750Z\"}, \"uniform_ood_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T14:34:34.440Z\", \"updated_at\": \"2026-05-19T20:08:44.104Z\", \"hypothesis\": \"Retrain uniform (b=0, seed=456) with checkpoint saving for OOD eval. If in-dist PPL matches original 17.702 (±0.01), the checkpoint is valid for OOD generalization testing across OpenWebText/Wikipedia/FineWeb.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method uniform --seed 456\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"pid\": 313688, \"log_path\": \"~/runs/provenance_weight_training/uniform_ood_seed456.log\", \"submitted_at\": \"2026-05-19T14:37:11.107Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 6103, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"wall_clock_seconds\": 14841.4, \"gpu_hours\": 4.12}, \"reproduce\": {\"finished_at\": \"2026-05-19T18:09:49.204Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T18:09:57.258996+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.7015, \"eval_ppl_openwebtext\": 18.3865, \"eval_ppl_wikipedia\": 15.3594, \"downstream_arc_easy_acc_norm\": 0.6166, \"downstream_arc_challenge_acc_norm\": 0.3439, \"downstream_hellaswag_acc_norm\": 0.4826, \"downstream_piqa_acc_norm\": 0.6795, \"downstream_winogrande_acc\": 0.5667, \"downstream_eval_method\": \"lm_eval 0.4.11, 0-shot, float16, batch_size=auto\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_ood_seed456/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T18:44:32.478Z\"}, \"w2_distribution_matching_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:51:37.385Z\", \"updated_at\": \"2026-05-19T07:52:31.452Z\", \"hypothesis\": \"If adaptive weighting's FineWeb PPL improvement is genuine quality gain (not tautological distribution matching), then adaptive should also show lower PPL on non-FineWeb eval sets (C4/OpenWebText, Wikipedia). If the improvement is purely distribution matching, adaptive will only win on FineWeb-derived evals.\", \"spec\": {\"command\": \"eval_perplexity.py --checkpoints adaptive/uniform --data_path fineweb/openwebtext/wikipedia --max_docs 5000 --max_length 2048\", \"server\": \"westd-41312\", \"data_path\": \"data/human/eval_holdout.jsonl, data/eval_openwebtext.jsonl, data/eval_wikipedia.jsonl\", \"data_count\": \"5000 docs x 3 eval sets x 2 models = 6 runs\", \"model_name\": \"qwen06b adaptive_fix_seed42 vs qwen06b_uniform_seed42_v2\", \"seed\": 42, \"checkpoint_source\": \"adaptive_fix_seed42/final, qwen06b_uniform_seed42_v2/final\", \"eval_data\": \"FineWeb holdout (4.1M tokens), OpenWebText (6.8M tokens), Wikipedia (27M tokens)\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/final\", \"log_path\": \"/tmp/eval_all.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T07:52:31.452Z\"}, \"detect_remove_q07_epoch_matched_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T23:59:28.901Z\", \"updated_at\": \"2026-05-19T03:07:24.735Z\", \"hypothesis\": \"Epoch-matched D&R q07: 1 epoch through q07 filtered data (184,908 samples, ~100M tokens, 3047 steps). Part of 5-point epoch-matched curve (q01/q03/q05/q07/q09). If PPL converges to ~17.65-17.74 range like q03(17.74) and q05(17.65), confirms U-shape sweet spot is entirely multi-epoch artifact across the full threshold range.\", \"reproduce\": {\"finished_at\": \"2026-05-19T03:02:01.393Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-19T01:10:23.679Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T01:10:31.706284+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:02:06.510586+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q07.jsonl --output_dir /root/autodl-tmp/output/models/detect_remove_q07_epoch_matched_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --max_steps 3047 --seed 42\", \"server\": \"westd-30476\", \"data_path\": \"data/scored_data_filtered_q07.jsonl\", \"data_count\": 184908, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42}, \"notes\": \"首次运行 EXIT_CODE=1 失败(~70min)，自动重试后训练完成(3047 steps, 6425s, EXIT_CODE=0)。Model saved to /root/autodl-tmp/output/models/detect_remove_q07_epoch_matched_seed42/final。等待 eval holdout PPL。\", \"metrics\": {\"eval_ppl_holdout\": 17.62, \"eval_loss_holdout\": 2.8689, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 3047}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q07_epoch_matched_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q07_epoch_matched_seed42.log\"}, \"detect_remove_q09_epoch_matched_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:28:26.693Z\", \"updated_at\": \"2026-05-19T02:49:02.649Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=3 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q09.jsonl --output_dir /root/autodl-tmp/output/models/detect_remove_q09_epoch_matched_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --max_steps 3770 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"89871\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q09_epoch_matched_seed42.log\", \"submitted_at\": \"2026-05-19T00:28:58.885Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q09.jsonl\", \"data_count\": 228743, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 8403.8, \"gpu_hours\": 2.33}, \"hypothesis\": \"Epoch-matched D&R q09: 1 epoch through q09 filtered data (228,743 samples, ~124M tokens, 3770 steps). Most lenient filter in the curve (61.6% retained, only 1.6x epochs in multi-epoch). Part of 5-point epoch-matched curve. If PPL converges to ~17.65-17.74 range, confirms U-shape is entirely multi-epoch artifact even at the least-filtered end.\", \"reproduce\": {\"finished_at\": \"2026-05-19T02:42:50.661Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T02:42:55.919377+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.628, \"eval_loss_holdout\": 2.8695, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 3770, \"train_loss_final\": 9.9127}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q09_epoch_matched_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q09_epoch_matched_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T02:49:02.649Z\"}, \"detect_remove_q01_epoch_matched_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:27:06.364Z\", \"updated_at\": \"2026-05-19T00:33:17.339Z\", \"hypothesis\": \"Epoch-matched D&R q01: 1 epoch through q01 filtered data (55,799 samples, ~30M tokens, 919 steps). Most extreme filter (15% retained, 4.8x epochs in multi-epoch). If PPL ≈ 17.65 (same as epoch-matched q05 and q03), confirms ALL multi-epoch D&R advantages come from extra epochs regardless of threshold. Three epoch-matched points (q01, q03, q05) spanning the full threshold range converging to same PPL = clean confound isolation.\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q01.jsonl --output_dir .../detect_remove_q01_epoch_matched_seed42 --model_name Qwen3-0.6B --weighting_method uniform --max_steps 919 --seed 42\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"86112\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q01_epoch_matched_seed42.log\", \"submitted_at\": \"2026-05-18T23:51:39.940Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q01.jsonl\", \"data_count\": 55799, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 2497.4, \"gpu_hours\": 0.69}, \"reproduce\": {\"finished_at\": \"2026-05-19T00:24:24.218Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T00:24:30.596234+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 18.0436, \"eval_loss_holdout\": 2.8928, \"eval_holdout_tokens\": 4077068}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q01_epoch_matched_seed42/final\", \"completed_at\": \"2026-05-19T00:33:17.339Z\"}, \"ngram_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:14:25.095Z\", \"updated_at\": \"2026-05-19T00:08:24.320Z\", \"hypothesis\": \"Uniform baseline for n-gram detector comparison. Control condition: uniform weighting on ngram-scored data. Expected to perform worse than ngram_adaptive, confirming adaptive advantage generalizes across detectors.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_ngram_qscore.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42 --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_only_model --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"227105\", \"log_path\": \"~/runs/provenance_weight_training/ngram_uniform_seed42.log\", \"submitted_at\": \"2026-05-18T15:01:05.106Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final\", \"train_loss\": 7.99, \"train_runtime_s\": 12800, \"total_steps\": 6103, \"wall_clock_seconds\": 14808.9, \"gpu_hours\": 4.11}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T19:07:54.054Z\", \"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733}}, \"detect_remove_q03_epoch_matched_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:18:10.019Z\", \"updated_at\": \"2026-05-18T23:35:57.701Z\", \"hypothesis\": \"Epoch-matched D&R q03: 1 epoch through q03 filtered data (116,935 samples, ~63M tokens, 1927 steps). If PPL ≈ 17.65 (same as epoch-matched q05), q03 vs q05 multi-epoch gap (17.25 vs 17.28) comes entirely from extra epochs (3.2x vs 2.4x), not data quality. If PPL significantly below 17.65, q03's stricter filtering genuinely yields higher quality data even at matched training budget.\", \"parent\": \"detect_remove_q03_seed42_r2\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q03.jsonl --output_dir .../detect_remove_q03_epoch_matched_seed42 --model_name Qwen3-0.6B --weighting_method uniform --max_steps 1927 --seed 42\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"78529\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q03_epoch_matched_seed42.log\", \"submitted_at\": \"2026-05-18T22:18:34.216Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q03.jsonl\", \"data_count\": 116935, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q03_epoch_matched_seed42/final\", \"wall_clock_seconds\": 4643.5, \"gpu_hours\": 1.29}, \"reproduce\": {\"finished_at\": \"2026-05-18T23:28:29.606Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T23:28:34.763822+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.876, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16_5000docs\", \"total_steps\": 1927, \"train_loss_final\": 11.3917, \"interpretation\": \"PPL 17.74 vs epoch-matched q05 (17.65): q03 stricter filtering yields HIGHER PPL (+0.09) under matched training budget, not lower. This contradicts the hypothesis that stricter filtering improves data quality per-token. Meanwhile multi-epoch q03 (17.25) is much lower, confirming that the PPL advantage of q03 in multi-epoch setting comes from more training epochs on filtered data, not from higher per-token quality. Conclusion: under fixed training budget, stricter filtering (q03) actually hurts slightly compared to moderate filtering (q05), likely because removing too many borderline samples reduces diversity without sufficient quality gain.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:35:57.701Z\"}, \"gpt2_adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:27:04.666Z\", \"updated_at\": \"2026-05-18T23:32:50.660Z\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_gpt2ppl_qscore.jsonl --output_dir .../gpt2_adaptive_seed42 --weighting_method adaptive --tau 0.8 --n_min 2 --seed 42\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"245417\", \"log_path\": \"~/runs/provenance_weight_training/gpt2_adaptive_seed42.log\", \"submitted_at\": \"2026-05-18T19:27:04.198Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_gpt2ppl_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed42/final\", \"wall_clock_seconds\": 14464.1, \"gpu_hours\": 4.02}, \"hypothesis\": \"GPT-2 PPL detector (AUC=0.913) + adaptive weighting: tests whether a weaker but practical detector still enables effective adaptive training. If adaptive PPL < uniform with GPT-2 scores, method generalizes beyond high-AUC TF-IDF detector.\", \"reproduce\": {\"finished_at\": \"2026-05-18T23:25:26.511Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T23:25:31.727843+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed42/final\", \"metrics\": {\"eval_ppl_holdout\": 17.79, \"eval_loss_holdout\": 2.879, \"train_loss\": 10.58, \"train_steps\": 6103, \"train_runtime_hours\": 3.92}, \"completed_at\": \"2026-05-18T23:28:08.287Z\"}, \"gpt2_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:27:06.537Z\", \"updated_at\": \"2026-05-18T23:08:25.414Z\", \"spec\": {\"command\": \"WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-0.6B --data_path data/scored_data_gpt2ppl_qscore.jsonl --output_dir .../gpt2_uniform_seed42 --weighting_method uniform --seed 42\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"245496\", \"log_path\": \"~/runs/provenance_weight_training/gpt2_uniform_seed42.log\", \"submitted_at\": \"2026-05-18T19:27:06.149Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_gpt2ppl_qscore.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/gpt2_uniform_seed42/final\", \"wall_clock_seconds\": 13279.3, \"gpu_hours\": 3.69}, \"hypothesis\": \"GPT-2 PPL-scored data with uniform weighting (no provenance reweighting) serves as a baseline; without adaptive weighting, the model cannot distinguish high-quality from low-quality training data, resulting in higher holdout perplexity compared to adaptive methods.\", \"reproduce\": {\"finished_at\": \"2026-05-18T23:02:03.184Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T23:02:07.864942+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.69, \"eval_loss_holdout\": 2.8733, \"train_loss\": 7.989, \"train_steps\": 6103, \"train_runtime_hours\": 3.54}, \"completed_at\": \"2026-05-18T23:08:25.414Z\"}, \"detect_remove_q06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:57:05.891Z\", \"updated_at\": \"2026-05-18T22:01:54.629Z\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=2 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q06.jsonl --output_dir /root/autodl-tmp/output/models/detect_remove_q06_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --bf16 --save_total_limit 3 --logging_steps 10 --save_steps 500'\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"60238\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_q06_seed42.log\", \"submitted_at\": \"2026-05-18T17:57:05.534Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_filtered_q06.jsonl\", \"data_count\": 170000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q06_seed42/checkpoint-6103\", \"wall_clock_seconds\": 14689.1, \"gpu_hours\": 4.08}, \"hypothesis\": \"D&R threshold t=0.6: keep q≤0.6 samples. Densification point between q05 (PPL=17.28) and q07 (PPL=17.32). Shows degradation slope as more contaminated data is included. Part of expanded 9-point D&R threshold curve.\", \"reproduce\": {\"finished_at\": \"2026-05-18T21:31:47.836Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T21:31:53.610706+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.3, \"eval_loss_holdout\": 2.8507}, \"completed_at\": \"2026-05-18T22:01:54.629Z\"}, \"adaptive_1_7b_planb_control\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:27:09.816Z\", \"updated_at\": \"2026-05-18T19:27:09.816Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/checkpoint-2500 --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_planb_control --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 100000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"245637\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_planb_control.log\", \"submitted_at\": \"2026-05-18T19:27:09.389Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_q01_final\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:16:20.167Z\", \"updated_at\": \"2026-05-18T19:16:20.167Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && python eval_perplexity.py --checkpoints /root/autodl-tmp/output/models/detect_remove_q01_seed42/final --data_path data/eval_holdout.jsonl --max_docs 5000 --max_length 2048\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"64266\", \"log_path\": \"~/runs/provenance_weight_training/eval_q01_final.log\", \"submitted_at\": \"2026-05-18T19:16:19.810Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"adaptive_1_7b_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:47:25.251Z\", \"updated_at\": \"2026-05-18T19:07:03.284Z\", \"hypothesis\": \"Scale validation: adaptive provenance weighting on Qwen3-1.7B (2.8x larger than 0.6B). If adaptive still outperforms uniform at 1.7B scale, demonstrates method generality beyond small models. Key for Main conference upgrade (D079 Line B). Expected: adaptive < uniform by ≥0.03 PPL (consistent with 0.6B gap).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-1.7B --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42 --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/checkpoint-2500\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"226766\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_seed42.log\", \"submitted_at\": \"2026-05-18T15:00:59.483Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/final\", \"train_loss\": 5.36, \"train_runtime_s\": 10990, \"total_steps\": 6103, \"wall_clock_seconds\": 14763.8, \"gpu_hours\": 4.1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T19:07:03.284Z\"}, \"status_check_41312\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:32:36.750Z\", \"updated_at\": \"2026-05-18T18:32:36.750Z\", \"spec\": {\"command\": \"bash -c \\\"sleep 120 && echo '=== eval_uniform_1_7b_v2 log ===' && cat /root/runs/provenance_weight_training/eval_uniform_1_7b_v2.log && echo '=== nvidia-smi ===' && nvidia-smi && echo '=== adaptive_1_7b progress ===' && ls -la /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42/ && tail -5 /root/runs/provenance_weight_training/adaptive_1_7b_seed42.log && echo '=== ngram progress ===' && ls /root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/ && ls /root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"240306\", \"log_path\": \"~/runs/provenance_weight_training/status_check_41312.log\", \"submitted_at\": \"2026-05-18T18:32:36.404Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_adaptive_1_7b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:32:07.436Z\", \"updated_at\": \"2026-05-18T18:32:07.436Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/provenance_weight_training && echo '=== Checking adaptive_1_7b final ===' && ls -la output/models/adaptive_1_7b_seed42/final/ 2>/dev/null && echo '=== Starting adaptive_1_7b eval ===' && python eval_perplexity.py --checkpoints output/models/adaptive_1_7b_seed42/final --data_path data/human/eval_holdout.jsonl || echo 'EVAL FAILED - final directory may not exist yet'\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/provenance_weight_training/eval_adaptive_1_7b.log\", \"submitted_at\": \"2026-05-18T18:32:07.080Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_uniform_1_7b_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:32:05.664Z\", \"updated_at\": \"2026-05-18T18:32:05.664Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/provenance_weight_training && nvidia-smi && echo '=== Starting uniform_1_7b eval ===' && python eval_perplexity.py --checkpoints output/models/uniform_1_7b_seed42_resumed/final --data_path data/human/eval_holdout.jsonl\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"240255\", \"log_path\": \"~/runs/provenance_weight_training/eval_uniform_1_7b_v2.log\", \"submitted_at\": \"2026-05-18T18:32:05.316Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_uniform_1_7b_resumed\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:59:51.854Z\", \"updated_at\": \"2026-05-18T17:59:51.854Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/provenance_weight_training && python eval_perplexity.py --checkpoints output/models/uniform_1_7b_seed42_resumed/final --data_path data/human/eval_holdout.jsonl\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/provenance_weight_training/eval_uniform_1_7b_resumed.log\", \"submitted_at\": \"2026-05-18T17:59:51.470Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"uniform_1_7b_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:47:26.566Z\", \"updated_at\": \"2026-05-18T15:45:29.875Z\", \"hypothesis\": \"Uniform weighting baseline on Qwen3-1.7B for scale validation. Control condition for comparing adaptive provenance weighting at larger model scale. Part of D079 Line B.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --model_name models/Qwen/Qwen3-1.7B --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42 --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42/checkpoint-3000\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"226623\", \"log_path\": \"~/runs/provenance_weight_training/uniform_1_7b_seed42.log\", \"submitted_at\": \"2026-05-18T15:00:55.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2489.8, \"gpu_hours\": 0.69}, \"reproduce\": {\"finished_at\": \"2026-05-18T15:42:18.572Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T15:42:25.542Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T15:42:32.973826+00:00\"}]}, \"notes\": \"失败原因: FileNotFoundError — checkpoint-3000/trainer_state.json 缺失，resume 崩溃 | 已有成果: checkpoint-3000 存在但不完整 | 建议: 找有效 checkpoint 重 resume 或从头训练\"}, \"detect_remove_q09_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T07:41:18.054Z\", \"updated_at\": \"2026-05-18T14:09:50.472Z\", \"hypothesis\": \"D&R threshold t=0.9 (most lenient): keep q≤0.9 (228,743 samples, 61.6%), only removing the most confidently synthetic data. Expected PPL close to uniform baseline since minimal data is removed. Part of threshold sensitivity sweep (t=0.1/0.3/0.5/0.7/0.9) showing D&R requires careful calibration while adaptive does not.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q09.jsonl --output_dir /root/autodl-tmp/output/models/detect_remove_q09_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-30476\", \"gpu\": 3, \"data_path\": \"data/scored_data_filtered_q09.jsonl\", \"data_count\": 228743, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"pid\": 27362, \"tmux_session\": \"detect_remove_q09_seed42\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/detect_remove_q09_seed42\", \"log_path\": \"/root/autodl-tmp/output/models/detect_remove_q09_seed42.log\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T12:59:21.395Z\", \"metrics\": {\"eval_ppl_holdout\": 17.42, \"eval_loss_holdout\": 2.8577, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048 --stride 1024 --fp16\"}}, \"contamination_60_ess_only_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:18:41.546Z\", \"updated_at\": \"2026-05-18T12:55:23.532Z\", \"hypothesis\": \"Cross-seed replication (seed456) of ESS-only at ρ=0.6. D075 found ESS-only(17.770) ≈ uniform(17.766) at ρ=0.6, suggesting max-intervention collapses at high contamination. 3-seed data tests if this collapse is robust or seed-specific, strengthening Claim 1 four-tier hierarchy cross-ρ evidence.\", \"parent\": \"contamination_60_ess_only_seed42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_ess_only_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"N/A (training experiment, not eval)\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.762, \"eval_loss_holdout\": 2.8771, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/contamination_60_ess_only_seed456/\", \"log_path\": \"/root/provenance_weight_training/logs/contamination_60_ess_only_seed456.log\", \"completed_at\": \"2026-05-18T12:31:20.928Z\"}, \"contamination_60_ess_only_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:18:40.225Z\", \"updated_at\": \"2026-05-18T12:55:22.289Z\", \"hypothesis\": \"Cross-seed replication (seed123) of ESS-only at ρ=0.6. D075 found ESS-only(17.770) ≈ uniform(17.766) at ρ=0.6, suggesting max-intervention collapses at high contamination. 3-seed data tests if this collapse is robust or seed-specific, strengthening Claim 1 four-tier hierarchy cross-ρ evidence.\", \"parent\": \"contamination_60_ess_only_seed42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_ess_only_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.763, \"eval_loss_holdout\": 2.8771, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --checkpoints --max_docs 5000 --max_length 2048\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/contamination_60_ess_only_seed123/\", \"log_path\": \"/root/provenance_weight_training/logs/contamination_60_ess_only_seed123.log\", \"completed_at\": \"2026-05-18T12:31:22.387Z\"}, \"ess_only_seed456_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:25:26.810Z\", \"updated_at\": \"2026-05-18T12:35:23.819Z\", \"hypothesis\": \"ESS-only (max-intervention) seed456 re-run on westd-41312: b* = max{b : ESS(b) >= n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only across seeds\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --n_min 2 --tau 0.8 --max_steps 6103 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --warmup_ratio 0.05 --weight_decay 0.01 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed456/checkpoint-2500\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:1\"], \"pid\": \"133521\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed456_r2.log\", \"submitted_at\": \"2026-05-17T21:00:43.303Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 219.9, \"gpu_hours\": 0.06}, \"reproduce\": {\"finished_at\": \"2026-05-17T21:04:21.425Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T21:04:23.229Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T21:04:28.148336+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.762, \"eval_loss_holdout\": 2.877, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 5.998, \"train_runtime_seconds\": 7611}}, \"ess_only_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:25:27.652Z\", \"updated_at\": \"2026-05-18T12:35:22.330Z\", \"hypothesis\": \"ESS-only (max-intervention) seed123 re-run on westd-41312: b* = max{b : ESS(b) >= n_min} — proves dual-constraint adaptive (min-intervention) superior to ESS-only across seeds\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.4 --n_min 2 --tau 0.8 --max_steps 6103 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --warmup_ratio 0.05 --weight_decay 0.01 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint /root/autodl-tmp/provenance_weight_training/output/models/ess_only_seed123/checkpoint-2000\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"133444\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed123_r2.log\", \"submitted_at\": \"2026-05-17T21:00:40.838Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 234.0, \"gpu_hours\": 0.06}, \"reproduce\": {\"finished_at\": \"2026-05-17T21:04:32.320Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T21:04:34.797Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T21:04:40.672713+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.721, \"eval_loss_holdout\": 2.8747, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 6.86, \"train_runtime_seconds\": 8674}}, \"detect_remove_q05_epoch_matched_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T07:20:02.608Z\", \"updated_at\": \"2026-05-18T12:31:37.482Z\", \"hypothesis\": \"Epoch-matched control: training with uniform weighting on filtered data (q>0.5 removed) for exactly 2533 steps (matching content-level 1 epoch of the contaminated data). If PPL is comparable to the full 6103-step D&R run, the D&R benefit comes from data quality not extra training; if PPL is worse, the extra training contributes meaningfully.\", \"notes\": \"Content-level 1 epoch: 153K samples × ~540 avg tokens = ~83M tokens → max_steps=2533. NOT Trainer epoch (9607 steps/315M tokens).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_filtered_q05.jsonl --output_dir /root/autodl-tmp/output/models/detect_remove_q05_epoch_matched_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.4 --max_steps 2533 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-30476\", \"gpu\": 2, \"data_path\": \"data/scored_data_filtered_q05.jsonl\", \"data_count\": 153725, \"model_name\": \"models/Qwen/Qwen3-0.6B\", \"seed\": 42, \"pid\": 20387, \"output_dir\": \"/root/autodl-tmp/output/models/detect_remove_q05_epoch_matched_seed42\", \"log_path\": \"/root/autodl-tmp/output/logs/detect_remove_q05_epoch_matched_seed42.log\", \"tmux_session\": \"detect_remove_q05_epoch_matched_seed42\", \"weighting_method\": \"uniform\", \"max_steps\": 2533}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.65, \"eval_loss_holdout\": 2.8707, \"eval_holdout_tokens\": 4077068, \"train_loss_final\": 3.184, \"total_steps\": 2533, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"vs_full_dr_q05\": \"+0.360 (17.650 vs 17.290, epoch-matched worse)\", \"vs_adaptive\": \"-0.001 (17.650 vs 17.651, nearly identical to adaptive)\", \"interpretation\": \"D&R 0.36 PPL advantage over epoch-matched is entirely from multi-epoch training on clean data, not from data quality filtering\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/detect_remove_q05_epoch_matched_seed42/\", \"completed_at\": \"2026-05-18T12:31:37.482Z\"}, \"contamination_60_random_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:18:42.911Z\", \"updated_at\": \"2026-05-18T12:31:19.522Z\", \"hypothesis\": \"Cross-seed replication (seed123) of random reweighting at ρ=0.6. Random weights ignore detector scores entirely. If PPL > ESS-only and > uniform (consistent with seed42), completes four-tier ablation hierarchy (adaptive < uniform < ESS-only < random) at ρ=0.6 with 3-seed evidence, confirming Claim 1 holds cross-ρ.\", \"parent\": \"contamination_60_random_seed42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_random_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method random --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-41312\", \"gpu\": 2, \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"N/A (training experiment, not eval)\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.87, \"eval_loss_holdout\": 2.8832, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"/root/provenance_weight_training/output/contamination_60_random_seed123/\", \"log_path\": \"/root/provenance_weight_training/logs/contamination_60_random_seed123.log\", \"completed_at\": \"2026-05-18T12:31:19.522Z\"}, \"contamination_60_random_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:18:44.245Z\", \"updated_at\": \"2026-05-18T12:31:18.086Z\", \"hypothesis\": \"Cross-seed replication (seed456) of random reweighting at ρ=0.6. Random weights ignore detector scores entirely. If PPL > ESS-only and > uniform (consistent with seed42), completes four-tier ablation hierarchy (adaptive < uniform < ESS-only < random) at ρ=0.6 with 3-seed evidence, confirming Claim 1 holds cross-ρ.\", \"parent\": \"contamination_60_random_seed42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_random_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method random --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\", \"server\": \"westd-41312\", \"gpu\": 3, \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"N/A (training experiment, not eval)\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.88, \"eval_loss_holdout\": 2.8837, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"/root/provenance_weight_training/output/contamination_60_random_seed456/\", \"log_path\": \"/root/provenance_weight_training/logs/contamination_60_random_seed456.log\", \"completed_at\": \"2026-05-18T12:31:18.086Z\"}, \"uniform_1_7b_seed42_r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:08:26.207Z\", \"updated_at\": \"2026-05-18T12:08:26.207Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=3 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42 --model_name /root/autodl-tmp/provenance_weight_training/models/Qwen/Qwen3-1.7B --weighting_method uniform --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"212584\", \"log_path\": \"~/runs/provenance_weight_training/uniform_1_7b_seed42_r2.log\", \"submitted_at\": \"2026-05-18T12:08:25.866Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"adaptive_1_7b_seed42_r2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:08:21.071Z\", \"updated_at\": \"2026-05-18T12:08:21.071Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=2 WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_1_7b_seed42 --model_name /root/autodl-tmp/provenance_weight_training/models/Qwen/Qwen3-1.7B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"212439\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_1_7b_seed42_r2.log\", \"submitted_at\": \"2026-05-18T12:08:20.748Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_rho06_batch_v6\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:08:16.687Z\", \"updated_at\": \"2026-05-18T12:08:16.687Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 python eval_perplexity.py --checkpoint_paths /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_ess_only_seed123/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_ess_only_seed456/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_random_seed123/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_random_seed456/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048 --stride 1024 --fp16 2>&1 | tee /tmp/eval_rho06_batch.log\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"212283\", \"log_path\": \"~/runs/provenance_weight_training/eval_rho06_batch_v6.log\", \"submitted_at\": \"2026-05-18T12:08:16.111Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"env_probe_41312_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:07:47.283Z\", \"updated_at\": \"2026-05-18T12:07:47.283Z\", \"spec\": {\"command\": \"bash -c \\\"find /root -maxdepth 4 -name 'python*' -type f 2>/dev/null | head -20 && echo '---' && find /usr -maxdepth 4 -name 'python*' -type f 2>/dev/null | head -10 && echo '---' && ls /root/.venv/bin/python* 2>/dev/null && ls /root/venv/bin/python* 2>/dev/null && cat /root/.profile 2>/dev/null | head -20\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/provenance_weight_training/env_probe_41312_v2.log\", \"submitted_at\": \"2026-05-18T12:07:46.950Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"env_probe_41312\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:07:29.821Z\", \"updated_at\": \"2026-05-18T12:07:29.821Z\", \"spec\": {\"command\": \"bash -c \\\"echo PATH=$PATH && which python3 2>/dev/null && which python 2>/dev/null && ls /root/miniconda3/bin/python 2>/dev/null && ls /root/anaconda3/bin/python 2>/dev/null && ls /opt/conda/bin/python 2>/dev/null && cat /root/.bashrc 2>/dev/null | grep -i 'conda\\\\|python\\\\|PATH' || echo 'no matches'\\\"\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/provenance_weight_training/env_probe_41312.log\", \"submitted_at\": \"2026-05-18T12:07:29.499Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_rho06_batch_v5\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:47:24.659Z\", \"updated_at\": \"2026-05-18T12:06:30.452Z\", \"spec\": {\"command\": \"cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 python eval_perplexity.py --checkpoint_paths /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_ess_only_seed123/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_ess_only_seed456/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_random_seed123/final /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_random_seed456/final --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048 --stride 1024 --fp16 2>&1 | tee /tmp/eval_rho06_batch.log\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/provenance_weight_training/eval_rho06_batch_v5.log\", \"submitted_at\": \"2026-05-18T12:06:30.114Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"contamination_60_grid_b0_3_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T04:04:45.048Z\", \"updated_at\": \"2026-05-18T09:24:10.985Z\", \"hypothesis\": \"Grid b=0.3 at ρ=0.6: tests whether grid-best remains near b=0.3 at higher contamination. If PPL ≈ contamination_60_seed42_r2 (adaptive, 17.74), confirms adaptive ≈ grid-best holds cross-ρ, strengthening Claim 2 generality.\", \"parent\": \"contamination_60_seed42_r2\", \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 30476 on 36.103.198.204\", \"completed_at\": \"2026-05-18T05:20:42.781Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:20:47.849092+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --contamination_ratio 0.6 --resume_from_checkpoint checkpoint-1500\", \"server\": \"westd-30476\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 200000000, \"model_name\": \"models/Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"contamination_60_grid_b0_3_seed42/checkpoint-1500\", \"eval_data\": \"data/scored_data_60.jsonl\"}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/contamination_60_grid_b0_3_seed42/final\", \"log_path\": \"/root/autodl-tmp/output/models/contamination_60_grid_b0_3_seed42/train_resume.log\", \"metrics\": {\"eval_ppl_holdout\": 17.634, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"checkpoint_1500_ppl\": 18.583, \"total_steps\": 6103, \"note\": \"resume from checkpoint-1500 with ~30% LR offset; final PPL improved over checkpoint-1500, no degradation\"}, \"conclusion\": \"success\"}, \"contamination_60_random_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T04:27:24.364Z\", \"updated_at\": \"2026-05-18T09:23:46.870Z\", \"hypothesis\": \"Random reweighting baseline at ρ=0.6: random weights ignore detector scores entirely. If PPL > ESS-only (17.77) and > uniform (17.766), completes four-tier ablation hierarchy (adaptive < uniform < ESS-only < random) at ρ=0.6, confirming Claim 1 structural argument holds cross-ρ.\", \"parent\": \"\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/output/models/contamination_60_random_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method random --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\", \"server\": \"westd-30476\", \"gpu\": \"cuda:3\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-18T08:36:52.838Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T08:36:54.608Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T08:37:00.026076+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.832, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"total_steps\": 6103, \"note\": \"resume from checkpoint-1000; cron falsely marked failed due to log path mismatch\"}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/contamination_60_random_seed42/final\", \"log_path\": \"/root/autodl-tmp/output/models/contamination_60_random_seed42/train_resume.log\"}, \"grid_b0_2_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T01:38:11.212Z\", \"updated_at\": \"2026-05-18T06:13:39.221Z\", \"hypothesis\": \"Cross-seed replication (seed456) of grid b=0.2: 3rd seed for b=0.2 plateau confirmation, completing Claim 2 cross-seed grid curve at the optimal region.\", \"parent\": \"grid_b0_2_seed42\", \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 30476 on 36.103.198.204\", \"completed_at\": \"2026-05-18T05:20:07.918Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python training/pretrain_weighted.py --resume_from_checkpoint checkpoint-5500 --weighting_method grid --grid_b_value 0.2 --seed 456\", \"server\": \"westd-30476\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"grid_b0_2_seed456/checkpoint-5500\", \"eval_data\": \"N/A (training, not eval)\"}, \"metrics\": {\"eval_ppl_holdout\": 17.645, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_checkpoint\": \"checkpoint-5500\", \"note\": \"eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume\"}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/grid_b0_2_seed456/checkpoint-5500\", \"log_path\": \"/root/autodl-tmp/output/models/grid_b0_2_seed456/step_metrics.jsonl\", \"conclusion\": \"success\"}, \"grid_b0_2_seed123\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T01:38:09.495Z\", \"updated_at\": \"2026-05-18T06:13:37.877Z\", \"hypothesis\": \"Cross-seed replication (seed123) of grid b=0.2: if PPL ≈ grid_b0_2_seed42 (17.64) and within plateau [0.2,0.3], confirms grid-best region is not seed-specific, strengthening Claim 2.\", \"parent\": \"grid_b0_2_seed42\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-18T05:20:30.898Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:20:39.515822+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:59:17.253325+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python training/pretrain_weighted.py --resume_from_checkpoint checkpoint-5500 --weighting_method grid --grid_b_value 0.2 --seed 123\", \"server\": \"westd-30476\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"grid_b0_2_seed123/checkpoint-5500\", \"eval_data\": \"N/A (training, not eval)\"}, \"metrics\": {\"eval_ppl_holdout\": 17.637, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --stride 1024 --fp16\", \"eval_checkpoint\": \"checkpoint-5500\", \"note\": \"eval at checkpoint-5500; final checkpoint degraded due to --save_only_model LR reset on resume\"}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/grid_b0_2_seed123/checkpoint-5500\", \"log_path\": \"/root/autodl-tmp/output/models/grid_b0_2_seed123/step_metrics.jsonl\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-18T05:59:08.599Z\"}}, \"contamination_60_adaptive_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:38:05.737Z\", \"updated_at\": \"2026-05-18T05:56:46.834Z\", \"hypothesis\": \"Cross-seed replication (seed456) of adaptive weighting at ρ=0.6: pairs with contamination_60_uniform_seed456 for 3rd seed contrast. If adaptive PPL < uniform PPL at ρ=0.6, completes Claim 3 proportion-robustness 3-seed evidence.\", \"parent\": \"contamination_60_seed42_r2\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/contamination_60_adaptive_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.8 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:0\"], \"pid\": \"158632\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_adaptive_seed456.log\", \"submitted_at\": \"2026-05-18T01:44:51.691Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"contamination_60_seed42_r2\", \"eval_data\": \"data/scored_data_60.jsonl\", \"wall_clock_seconds\": 14209.4, \"gpu_hours\": 3.95}, \"reproduce\": {\"finished_at\": \"2026-05-18T05:36:41.822Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:36:46.155880+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.735, \"eval_loss_holdout\": 2.8755, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --stride 1024 --fp16\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/contamination_60_adaptive_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_adaptive_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T05:41:41.076Z\"}, \"grid_b0_1_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:41:20.961Z\", \"updated_at\": \"2026-05-18T05:28:09.690Z\", \"hypothesis\": \"Grid-b sweep b=0.1 on ρ=0.4 data, seed123. Minimal reweighting to establish lower bound of useful b range. Expect PPL close to uniform (~17.694) and consistent with seed42 result (17.657).\", \"parent\": \"grid_b0_1_seed42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/grid_b0_1_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.1 --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"pid\": \"158918\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_1_seed123.log\", \"submitted_at\": \"2026-05-18T01:45:00.689Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 247666, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"grid_b0_1_seed42\", \"eval_data\": \"data/scored_data.jsonl\", \"wall_clock_seconds\": 13365.6, \"gpu_hours\": 3.71}, \"reproduce\": {\"finished_at\": \"2026-05-18T05:19:43.419Z\"}, \"metrics\": {\"eval_ppl_holdout\": 17.646, \"eval_loss_holdout\": 2.8705, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16\"}, \"checkpoint_path\": \"output/models/grid_b0_1_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_1_seed123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T05:27:46.319Z\"}, \"grid_b0_1_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:41:21.496Z\", \"updated_at\": \"2026-05-18T05:28:09.099Z\", \"hypothesis\": \"Grid-b sweep b=0.1 on ρ=0.4 data, seed456. Minimal reweighting to establish lower bound of useful b range. Expect PPL close to uniform (~17.694) and consistent with seed42 result (17.657).\", \"parent\": \"grid_b0_1_seed42\", \"spec\": {\"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"159304\", \"data_path\": \"data/scored_data.jsonl\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/grid_b0_1_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.1 --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\", \"data_count\": 247666, \"checkpoint_source\": \"grid_b0_1_seed42\", \"eval_data\": \"data/scored_data.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T05:19:52.891Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T05:20:03.157900+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.663, \"eval_loss_holdout\": 2.8715, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048 --fp16\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_1_seed456/final\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_1_seed456.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T05:27:34.520Z\"}, \"contamination_60_ess_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:29:38.654Z\", \"updated_at\": \"2026-05-18T04:48:21.069Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"265012\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log\", \"submitted_at\": \"2026-05-15T23:29:46.475Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 14168.4, \"gpu_hours\": 3.94}, \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T23:29:46.475Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_ess_only_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method ess_only --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-16T03:10:18.007Z\", \"training_hours\": 3.68}, \"pid\": \"265012\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_ess_only_seed42.log\", \"hypothesis\": \"ESS-only (max-intervention) on ρ=0.6 data: b* = max{b : ESS(b) ≥ n_min}. Tests if dual-constraint advantage over ESS-only holds at higher contamination (ρ=0.4→0.6). Paired with adaptive and grid_b0.5 for Claim 1+3 cross-validation.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:10:20.449362+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.77, \"eval_loss_holdout\": 2.8775, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.842, \"total_steps\": 6103, \"train_runtime_seconds\": 13152}, \"checkpoint_path\": \"output/models/contamination_60_ess_only_seed42/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:25:54.836Z\", \"notes\": \"ρ=0.6 ESS-only PPL=17.77 ≈ uniform (17.766), max-intervention 在高 contamination 下完全失效。vs ρ=0.4 ESS-only avg 17.723 → ρ增加0.2导致+0.047退化。关键对比: dual(17.74) < ESS-only(17.77), Claim 1 在 ρ=0.6 下仍成立(gap=0.03, 小于 ρ=0.4 的 gap=0.07)。ESS-only 崩溃而 dual 仍有效 → 强化 \\\"dual-constraint 在高 contamination 下更重要\\\" 叙事。⚠️ 服务器 westd-47453 已下线，checkpoint 不可用。eval 结果已记录在 registry metrics 中。\"}, \"contamination_60_uniform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T00:12:01.324Z\", \"updated_at\": \"2026-05-18T03:30:01.455Z\", \"hypothesis\": \"Uniform baseline at ρ=0.6 seed123: pairs with contamination_60_seed123 (adaptive) to form seed123 uniform/adaptive contrast. If adaptive PPL < uniform PPL at ρ=0.6, confirms Claim 3 proportion-robustness holds cross-seed at higher contamination.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/output/models/contamination_60_uniform_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"66327\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/contamination_60_uniform_seed123/final\", \"metrics\": {\"eval_ppl_holdout\": 17.754, \"eval_loss_holdout\": 2.8766, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/output/models/contamination_60_uniform_seed123/eval_output.log\", \"completed_at\": \"2026-05-18T03:30:01.455Z\"}, \"contamination_60_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:04:52.646Z\", \"updated_at\": \"2026-05-18T03:02:27.875Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir /root/autodl-tmp/output/models/contamination_60_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.8 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --bf16 --save_total_limit 3 --save_only_model --dataloader_num_workers 0\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"63153\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed123.log\", \"submitted_at\": \"2026-05-17T23:06:06.738Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"wall_clock_seconds\": 14181.1, \"gpu_hours\": 3.94}, \"hypothesis\": \"Cross-seed replication (seed123) of adaptive weighting at ρ=0.6: confirms contamination_60_seed42_r2 result is not seed-specific, strengthening Claim 3 proportion-robustness across contamination levels.\", \"reproduce\": {\"finished_at\": \"2026-05-18T02:55:06.709Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:55:10.838537+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.732, \"eval_loss_holdout\": 2.8754, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.6302, \"train_runtime_seconds\": 13638.6, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py --max_docs 5000 --max_length 2048\"}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/contamination_60_seed123/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T03:02:27.875Z\"}, \"grid_b0_3_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:18:02.595Z\", \"updated_at\": \"2026-05-18T01:54:20.680Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export WANDB_MODE=disabled && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/output/models/grid_b0_3_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.3 --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint /root/autodl-tmp/output/models/grid_b0_3_seed123/checkpoint-1000\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:1\"], \"pid\": \"53821\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_3_seed123_r2.log\", \"submitted_at\": \"2026-05-17T21:00:46.891Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"b=0.3 is grid-optimal cross-seed (confirmed at seed42 PPL=17.640). Retry on westd-30476 after previous failure. If seed123 b=0.3 PPL < b=0.5 seed123 (17.638), confirms grid-best is not seed-specific.\", \"parent\": \"grid_b0_5_seed123\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:56:39.769Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T20:56:41.721Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:56:45.078984+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.5792, \"eval_loss_holdout\": 2.8667, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"re_eval_date\": \"2026-05-18\", \"eval_results_path\": \"/root/autodl-tmp/output/models/grid_b0_3_seed123/eval_results.json\", \"re_eval_note\": \"re-eval confirms original PPL=17.58; JSON artifact now saved\"}}, \"grid_b0_3_seed456_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T18:31:21.951Z\", \"updated_at\": \"2026-05-18T01:17:18.486Z\", \"hypothesis\": \"Cross-seed replication (seed456) of grid b=0.3: if PPL ≈ grid_b0_3_seed42 (17.640) and < b=0.5 seed456 (17.65), confirms grid-best=0.3 is not seed-specific, strengthening Claim 2 (adaptive ≈ grid-best).\", \"parent\": \"grid_b0_3_seed456\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 456 --num_train_tokens 200000000\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"54779\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_3_seed456_r2.log\", \"submitted_at\": \"2026-05-17T21:01:36.455Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_source\": \"N/A (fresh training, not eval)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/grid_b0_3_seed456_r2/final\", \"wall_clock_seconds\": 15342.0, \"gpu_hours\": 4.26}, \"server\": \"westd-30476\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-30476\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-17T20:52:01.783Z\", \"finished_at\": \"2026-05-18T00:38:02.877Z\", \"training_hours\": 3.77}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:38:07.191932+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.87, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 9.085, \"vs_uniform\": \"-0.054 (17.64 vs 17.694)\", \"vs_grid_b03_seed42\": \"0.000 (17.64 vs 17.640)\", \"vs_grid_b05_seed456\": \"-0.01 (17.64 vs 17.65)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:17:18.486Z\"}, \"batchsize16_nmin8_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T20:27:38.588Z\", \"updated_at\": \"2026-05-17T23:50:52.194Z\", \"hypothesis\": \"Coupling rule validation at bs=16: n_min=max(2,16//2)=8 with per_device_train_batch_size=16 (not 4×4 grad_accum). If PPL comparable to bs=4 adaptive, confirms coupling rule generalizes across batch sizes. Critical: micro-batch must exceed n_min for ESS constraint to be satisfiable.\", \"parent\": \"batchsize16_nmin8_r2\", \"spec\": {\"command\": \"bash scripts/run_bs16_nmin8_r2.sh\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"48891\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"weighting_method\": \"adaptive\", \"per_device_train_batch_size\": 16, \"gradient_accumulation_steps\": 1, \"n_min\": 8, \"tau\": 0.8, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2/final\", \"log_path\": \"~/runs/provenance_weight_training/batchsize16_nmin8_r3.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.65, \"eval_loss_holdout\": 2.871, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_loss\": 2.6308, \"train_runtime_seconds\": 15057, \"vs_adaptive_bs4\": \"-0.003 (17.65 vs 17.6527)\", \"vs_bs8_nmin4\": \"-0.01 (17.65 vs 17.66)\", \"batch_size\": 16, \"n_min\": 8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T23:50:52.194Z\"}, \"grid_b0_3_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:28:37.148Z\", \"updated_at\": \"2026-05-17T18:14:49.813Z\", \"hypothesis\": \"b=0.3 is grid-optimal cross-seed (confirmed at seed42 PPL=17.640 < b=0.5 seed42 17.651). If seed456 also shows b=0.3 as best, confirms grid-best is not seed-specific and strengthens Claim 2 (adaptive ≈ grid-best).\", \"parent\": \"grid_b0_5_seed456\", \"server\": \"westd-41312\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T05:35:41.476Z\"}, \"gpu_id\": [\"cuda:3\"], \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_3_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.3 --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"88491\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_3_seed456.log\", \"submitted_at\": \"2026-05-17T12:53:05.146Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"contamination_ratio\": 0.4, \"b_value\": 0.3, \"checkpoint_source\": \"none\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"wall_clock_seconds\": 19304.7, \"gpu_hours\": 5.36}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-17T18:14:49.813Z\"}, \"batch_adaptive_tau_rho06_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:42:41.503Z\", \"updated_at\": \"2026-05-17T18:11:09.279Z\", \"spec\": {\"command\": \"bash scripts/run_batch_adaptive_tau_rho06_seed42.sh\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"22904\", \"log_path\": \"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_r5.log\", \"submitted_at\": \"2026-05-17T13:42:41.242Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 371499, \"data_path\": \"data/scored_data_rho06.jsonl\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/batch_adaptive_tau_rho06_seed42/final\", \"wall_clock_seconds\": 16108.0, \"gpu_hours\": 4.47}, \"hypothesis\": \"Batch-adaptive τ on ρ=0.6 data: per-batch τ_batch = clamp(α_eff_natural + 0.3, 0.5, 0.95) adapts threshold to local contamination density. At higher contamination, adaptive τ should outperform fixed τ=0.8 more clearly than at ρ=0.4 (which was negative).\", \"parent\": \"batch_adaptive_tau_rho04_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-17T17:34:39.613Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:34:45.570181+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8754, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.267, \"train_runtime_seconds\": 13903, \"total_steps\": 6103, \"vs_uniform_rho06\": \"-0.036\", \"vs_adaptive_fixed_tau08_rho06\": \"-0.010\", \"vs_grid_best_rho06\": \"+0.026\", \"vs_hybrid_rho06\": \"+0.200\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T18:11:09.279Z\"}, \"random_reweight_seed123_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:59:58.565Z\", \"updated_at\": \"2026-05-17T18:11:08.071Z\", \"spec\": {\"command\": \"bash scripts/run_random_reweight_seed123.sh\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"20073\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed123_r5.log\", \"submitted_at\": \"2026-05-17T12:59:58.325Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 371499, \"data_path\": \"data/scored_data.jsonl\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/random_reweight_seed123/final\", \"wall_clock_seconds\": 18669.7, \"gpu_hours\": 5.19}, \"hypothesis\": \"Cross-seed replication (seed123) of random reweighting baseline: U(0,2) random weights replacing detector q-scores. If PPL > uniform (17.688), confirms detector signal is load-bearing across seeds, strengthening Claim 1.\", \"parent\": \"random_reweight_v2_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-17T16:41:41.672Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T16:41:47.517255+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.8, \"eval_loss_holdout\": 2.8793, \"eval_holdout_tokens\": 4077068, \"train_loss\": 8.0176, \"train_runtime_seconds\": 13267, \"total_steps\": 6103, \"vs_uniform_seed123\": \"+0.114\", \"vs_adaptive_fix_seed123\": \"+0.157\", \"vs_random_reweight_v2_seed42\": \"consistent (+0.136 seed42 vs +0.114 seed123)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T18:11:08.071Z\"}, \"rho02_adaptive_tau09_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:42:23.804Z\", \"updated_at\": \"2026-05-17T18:02:05.662Z\", \"spec\": {\"command\": \"bash scripts/run_rho02_adaptive_tau09_seed42.sh\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"22095\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_r5.log\", \"submitted_at\": \"2026-05-17T13:42:23.566Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 371499, \"data_path\": \"data/scored_data_rho02.jsonl\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/final\", \"wall_clock_seconds\": 15582.1, \"gpu_hours\": 4.33}, \"hypothesis\": \"Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating proportion-robustness (Claim 3).\", \"parent\": \"adaptive_fix_seed42\", \"reproduce\": {\"finished_at\": \"2026-05-17T17:54:21.963Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:54:27.825996+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.45, \"eval_loss_holdout\": 2.8593, \"eval_holdout_tokens\": 4077068, \"train_loss\": 11.864, \"epoch\": 0.47, \"b_star_mean\": 4.3493, \"b_star_median\": 2.9609, \"b_star_std\": 4.3982, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_zero\": 2.65, \"alpha_eff_mean\": 0.8277, \"alpha_eff_median\": 0.8826, \"alpha_eff_pct_at_max\": 42.95, \"ess_mean\": 2.3784, \"ess_median\": 2.0121}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T18:02:05.662Z\"}, \"bs8_auto_nmin_r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:42:31.839Z\", \"updated_at\": \"2026-05-17T17:47:01.475Z\", \"spec\": {\"command\": \"bash scripts/run_bs8_auto_nmin_seed42.sh\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:1\"], \"pid\": \"22466\", \"log_path\": \"~/runs/provenance_weight_training/bs8_auto_nmin_r5.log\", \"submitted_at\": \"2026-05-17T13:42:31.602Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 371499, \"data_path\": \"data/scored_data.jsonl\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/autodl-tmp/output/models/bs8_auto_nmin_seed42/final\", \"wall_clock_seconds\": 14669.9, \"gpu_hours\": 4.07}, \"hypothesis\": \"bs=8 with auto n_min=4 (max(2,bs//2)). Previous bs8_nmin2 failed (PPL=17.73) because explicit n_min=2 was too loose for bs=8. Auto n_min=4 should recover performance, validating the coupling rule.\", \"parent\": \"bs8_nmin2_seed42_r2\", \"reproduce\": {\"finished_at\": \"2026-05-17T17:37:20.718Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T17:37:27.586541+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.66, \"eval_loss_holdout\": 2.8716, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.163, \"total_steps\": 6103, \"train_runtime_seconds\": 14064, \"epoch\": 0.26, \"b_star_mean\": 1.0957, \"b_star_median\": 0.9, \"b_star_std\": 0.7563, \"b_star_pct_zero\": 0.11, \"b_star_pct_below_0.5\": 10.43, \"ess_mean\": 4.4925, \"ess_median\": 4.0446, \"alpha_eff_mean\": 0.7023, \"alpha_eff_median\": 0.7572, \"alpha_eff_pct_at_max\": 38.88}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T17:47:01.475Z\"}, \"llama3b_adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:24:54.473Z\", \"updated_at\": \"2026-05-17T14:21:50.544Z\", \"spec\": {\"hypothesis\": \"Llama-3.2-3B adaptive τ=0.8 at ρ=0.4. Paired with llama3b_uniform to test cross-model generalization of adaptive reweighting.\", \"model_name\": \"unsloth/Llama-3.2-3B\", \"seed\": 42, \"contamination_ratio\": 0.4, \"data_count\": 371499, \"command\": \"bash scripts/run_llama3b_adaptive_seed42.sh\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data.jsonl\", \"gpu\": \"cuda:1\", \"pid\": 4005}, \"hypothesis\": \"Adaptive b* generalizes across model architectures: Llama-3.2-3B with provenance-weighted training should show PPL improvement over uniform baseline proportional to Qwen3-0.6B results, confirming the method is not architecture-specific and dual-constraint b* transfers.\", \"parent\": \"adaptive_fix_seed42\", \"conclusion\": \"negative\", \"reproduce\": {\"finished_at\": \"2026-05-17T13:58:27.135Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-17T13:58:28.583Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:58:31.913203+00:00\"}]}, \"metrics\": {\"ppl\": 10.58, \"eval_loss\": 2.359, \"eval_tokens\": 4017316}, \"notes\": \"诊断中: cron 报 process dead 5× + no W&B，但 memory.md 有 PPL=10.58 结论。疑似训练完成但监控缺失。Worker worker_diagnose_llama3b_adaptive_seed42_20260517T140045 正在 SSH 确认。日志文件 /root/runs/provenance_weight_training/llama3b_adaptive_seed42.log 不存在。\"}, \"batchsize16_nmin8_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T03:04:54.440Z\", \"updated_at\": \"2026-05-17T14:13:30.199Z\", \"notes\": \"westd-47453 permanently down (2026-05-17). Experiment was queued on 47453 (launcher PID 375555) waiting for GPU, never actually ran. Data lost. Needs migration to westd-30476.\", \"hypothesis\": \"batch_size=16 with auto n_min=8 (max(2,bs//2)): larger batch provides more stable ESS estimates and the coupling rule n_min=bs//2 maintains the same ESS dynamic range ratio as bs=4/n_min=2, so PPL should match or improve vs bs=4 baseline.\", \"completed_at\": \"\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"westd-47453 permanently down (2026-05-17). Experiment was queued on 47453 (launcher PID 375555) waiting for GPU, never actually ran. Data lost. Needs migration to westd-30476.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:13:32.124104+00:00\"}]}, \"spec\": {\"server\": \"westd-41312\", \"gpu\": [\"cuda:2\"], \"account\": \"root\", \"command\": \"bash scripts/run_batchsize16_nmin8_seed42.sh\", \"pid\": \"50284\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"batch_size\": 16, \"n_min\": 8, \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499}, \"reproduce\": {\"finished_at\": \"2026-05-17T14:13:27.986Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\"}, \"llama3b_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:24:52.580Z\", \"updated_at\": \"2026-05-17T13:42:46.955Z\", \"spec\": {\"hypothesis\": \"Llama-3.2-3B uniform baseline at ρ=0.4. Cross-model generalization test — if adaptive improves over uniform on 3B model (not just 0.6B), strengthens paper claims.\", \"model_name\": \"unsloth/Llama-3.2-3B\", \"seed\": 42, \"contamination_ratio\": 0.4, \"data_count\": 371499, \"command\": \"bash scripts/run_llama3b_uniform_seed42.sh\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data.jsonl\", \"gpu\": \"cuda:0\", \"pid\": 3112}, \"hypothesis\": \"Uniform weighting baseline on Llama-3.2-3B establishes reference PPL for cross-model generalization experiment, enabling fair comparison with adaptive weighting on the same architecture and data.\", \"parent\": \"uniform_seed42\", \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/llama3b_uniform_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/logs/llama3b_uniform_seed42.log\", \"metrics\": {\"ppl\": 10.38, \"eval_loss\": 2.3397, \"eval_tokens\": 1526195, \"train_loss\": 7.2987, \"train_steps\": 6103, \"train_runtime_seconds\": 94309}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T13:42:46.955Z\"}, \"random_reweight_seed123_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:57:05.055Z\", \"updated_at\": \"2026-05-17T13:18:38.368Z\", \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_random_reweight_seed123.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"18979\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed123_r4.log\", \"submitted_at\": \"2026-05-17T12:57:04.815Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1293.6, \"gpu_hours\": 0.36}, \"hypothesis\": \"Cross-seed replication (seed123) of random reweighting baseline: U(0,2) random weights replacing detector q-scores. If PPL > uniform (17.688), confirms detector signal is load-bearing across seeds, strengthening Claim 1.\", \"parent\": \"random_reweight_v2_seed42\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T13:18:38.368Z\"}, \"rho02_adaptive_tau09_r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:49:18.411Z\", \"updated_at\": \"2026-05-17T12:53:29.865Z\", \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_rho02_adaptive_tau09_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"18281\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_r4.log\", \"submitted_at\": \"2026-05-17T12:49:18.183Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 246.5, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T12:53:24.682Z\", \"failure_reason\": \"Script crash: pretrain_weighted.py: error: unrecognized arguments: --dataloader_num_workers 0. Tmux session killed during cleanup.\"}, \"random_reweight_seed123_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:49:16.975Z\", \"updated_at\": \"2026-05-17T12:53:23.551Z\", \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_random_reweight_seed123.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"18188\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed123_r3.log\", \"submitted_at\": \"2026-05-17T12:49:16.724Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 246.8, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T12:53:23.551Z\"}, \"grid_b0_2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:26:47.719Z\", \"updated_at\": \"2026-05-17T12:52:35.008Z\", \"hypothesis\": \"Grid-b sweep b=0.2 on ρ=0.4 data, seed42. Interpolation between b=0.1 and b=0.3 to characterize PPL curve shape in low-b region.\", \"parent\": \"grid_b_seed42_batch\", \"conclusion\": \"success\", \"notes\": \"Director 预算修正砍掉：b=0.1 和 b=0.3 两点足够推断趋势，b=0.2 不再需要。→ D042 修正：grid_b0_2 重新加入，排在 grid_b0_1/b0_3 之后的下一个空 GPU。\", \"spec\": {\"command\": \"bash /root/provenance_weight_training/scripts/run_grid_b0_2_seed42.sh\", \"server\": \"westd-41312\", \"gpu\": [\"cuda:3\"], \"pid\": \"45224\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.4, \"b_value\": 0.2, \"checkpoint_source\": \"none\", \"eval_data\": \"n/a\"}, \"checkpoint_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_2_seed42/final/\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_2_seed42/step_metrics.jsonl\", \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\"}, \"completed_at\": \"2026-05-17T12:52:35.008Z\"}, \"rho02_adaptive_tau09_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:24:41.471Z\", \"updated_at\": \"2026-05-17T11:44:37.903Z\", \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_rho02_adaptive_tau09_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"10727\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_r3.log\", \"submitted_at\": \"2026-05-17T11:26:28.291Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1089.6, \"gpu_hours\": 0.3}, \"server\": \"westd-30476\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"hypothesis\": \"Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating proportion-robustness (Claim 3).\", \"parent\": \"adaptive_fix_seed42\", \"pid\": \"10727\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_r3.log\", \"reproduce\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_rho02_adaptive_tau09_seed42.sh\\\"\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:44:37.903Z\"}, \"batch_adaptive_tau_rho06_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:24:40.398Z\", \"updated_at\": \"2026-05-17T11:44:36.509Z\", \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_batch_adaptive_tau_rho06_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"10209\", \"log_path\": \"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_r3.log\", \"submitted_at\": \"2026-05-17T11:26:23.874Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1092.6, \"gpu_hours\": 0.3}, \"server\": \"westd-30476\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"hypothesis\": \"Batch-adaptive τ on ρ=0.6 data: per-batch τ_batch = clamp(α_eff_natural + 0.3, 0.5, 0.95) adapts threshold to local contamination density. At higher contamination, adaptive τ should outperform fixed τ=0.8 more clearly than at ρ=0.4 (which was negative).\", \"parent\": \"batch_adaptive_tau_rho04_seed42\", \"pid\": \"10209\", \"log_path\": \"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_r3.log\", \"reproduce\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_batch_adaptive_tau_rho06_seed42.sh\\\"\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:44:36.509Z\"}, \"bs8_auto_nmin_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:24:39.323Z\", \"updated_at\": \"2026-05-17T11:44:35.233Z\", \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_bs8_auto_nmin_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:1\"], \"pid\": \"10119\", \"log_path\": \"~/runs/provenance_weight_training/bs8_auto_nmin_r3.log\", \"submitted_at\": \"2026-05-17T11:26:19.279Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1096.0, \"gpu_hours\": 0.3}, \"server\": \"westd-30476\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"hypothesis\": \"bs=8 with auto n_min=4 (max(2,bs//2)). Previous bs8_nmin2 failed (PPL=17.73) because explicit n_min=2 was too loose for bs=8. Auto n_min=4 should recover performance, validating the coupling rule.\", \"parent\": \"bs8_nmin2_seed42_r2\", \"pid\": \"10119\", \"log_path\": \"~/runs/provenance_weight_training/bs8_auto_nmin_r3.log\", \"reproduce\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_bs8_auto_nmin_seed42.sh\\\"\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:44:35.233Z\"}, \"random_reweight_seed123_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T11:24:38.169Z\", \"updated_at\": \"2026-05-17T11:44:33.731Z\", \"spec\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_random_reweight_seed123.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:0\"], \"pid\": \"10035\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed123_r2.log\", \"submitted_at\": \"2026-05-17T11:26:15.828Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1097.9, \"gpu_hours\": 0.3}, \"server\": \"westd-30476\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"hypothesis\": \"Cross-seed replication (seed123) of random reweighting baseline: U(0,2) random weights replacing detector q-scores. If PPL > uniform (17.688), confirms detector signal is load-bearing across seeds, strengthening Claim 1.\", \"parent\": \"random_reweight_v2_seed42\", \"pid\": \"10035\", \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed123_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_random_reweight_seed123.sh\\\"\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:44:33.731Z\"}, \"rho02_adaptive_tau09_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:25:34.927Z\", \"updated_at\": \"2026-05-17T11:19:34.469Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_rho02_adaptive_tau09_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:3\"], \"pid\": \"7951\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_r2.log\", \"submitted_at\": \"2026-05-17T11:15:37.586Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 142.8, \"gpu_hours\": 0.04}, \"server\": \"westd-30476\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"pid\": \"7951\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_rho02_adaptive_tau09_seed42.sh\\\"\", \"finished_at\": \"2026-05-17T11:16:27.699Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T11:16:40.596896+00:00\"}]}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:18:00.344Z\", \"failure_reason\": \"TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer' — same as bs8_auto_nmin_r2 and batch_adaptive_tau_rho06_r2, transformers version incompatibility on westd-30476\", \"metrics\": {\"error\": \"TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'\", \"error_stage\": \"initialization\", \"training_completed\": false, \"note\": \"Crashed before any training. Same bug as rho02_adaptive_tau09_seed42. Fix: replace tokenizer= with processing_class= in pretrain_weighted.py line ~101.\"}}, \"batch_adaptive_tau_rho06_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:25:31.543Z\", \"updated_at\": \"2026-05-17T11:16:18.424Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_batch_adaptive_tau_rho06_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:2\"], \"pid\": \"7746\", \"log_path\": \"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_r2.log\", \"submitted_at\": \"2026-05-17T11:15:32.058Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 46.4, \"gpu_hours\": 0.01}, \"server\": \"westd-30476\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"pid\": \"7746\", \"log_path\": \"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_batch_adaptive_tau_rho06_seed42.sh\\\"\", \"finished_at\": \"2026-05-17T11:16:15.950Z\"}, \"failure_reason\": \"Traceback → , in main trainer = WeightedTrainer( ^^^^^^^^^^^^^^^^ File \\\"/root/provenance_weight_training/training/pretrain_weighted.py\\\", line 101, in __init__ super().__init__(**kwargs) TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:16:18.424Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T11:16:24.981007+00:00\"}]}}, \"bs8_auto_nmin_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:25:26.255Z\", \"updated_at\": \"2026-05-17T11:16:07.184Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_bs8_auto_nmin_seed42.sh\\\"\", \"server\": \"westd-30476\", \"gpu\": [\"cuda:1\"], \"pid\": \"7543\", \"log_path\": \"~/runs/provenance_weight_training/bs8_auto_nmin_r2.log\", \"submitted_at\": \"2026-05-17T11:15:23.530Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 43.7, \"gpu_hours\": 0.01}, \"server\": \"westd-30476\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"7543\", \"log_path\": \"~/runs/provenance_weight_training/bs8_auto_nmin_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_bs8_auto_nmin_seed42.sh\\\"\", \"finished_at\": \"2026-05-17T11:16:04.481Z\"}, \"failure_reason\": \"Traceback → , in main trainer = WeightedTrainer( ^^^^^^^^^^^^^^^^ File \\\"/root/provenance_weight_training/training/pretrain_weighted.py\\\", line 101, in __init__ super().__init__(**kwargs) TypeError: Trainer.__init__() got an unexpected keyword argument 'tokenizer'\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T11:16:07.184Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T11:16:11.345912+00:00\"}]}}, \"rho02_adaptive_tau09_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:02:16.962Z\", \"updated_at\": \"2026-05-17T10:50:00.000Z\", \"spec\": {\"command\": \"bash scripts/run_rho02_adaptive_tau09_seed42.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"367604\", \"data_path\": \"data/scored_data_rho02.jsonl\", \"data_count\": 206111, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.2, \"tau\": 0.9, \"n_min\": 2, \"weighting_method\": \"adaptive\", \"log_path\": \"~/runs/provenance_weight_training/rho02_adaptive_tau09_seed42.log\"}, \"notes\": \"Retry: first attempt failed due to CUDA_VISIBLE_DEVICES=-1 in script overriding submit_training_job env. Fixed by removing export line from script. PID 367604.\", \"hypothesis\": \"Adaptive weighting with τ=0.9 on ρ=0.2 (low contamination): even at 20% contamination, stricter α_eff threshold should find non-trivial b* and outperform uniform, demonstrating the method works across contamination levels (Claim 3 proportion-robustness).\", \"parent\": \"adaptive_fix_seed42\", \"conclusion\": \"failed\", \"failure_reason\": \"westd-47453 server down, data lost\", \"completed_at\": \"2026-05-17T10:50:00.000Z\"}, \"batch_adaptive_tau_rho06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:16:35.042Z\", \"updated_at\": \"2026-05-17T10:50:00.000Z\", \"spec\": {\"command\": \"bash /root/provenance_weight_training/scripts/run_batch_adaptive_tau_rho06_seed42.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"372142\", \"log_path\": \"~/runs/provenance_weight_training/batch_adaptive_tau_rho06_seed42.log\", \"submitted_at\": \"2026-05-16T23:46:46.802Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_rho06.jsonl\", \"data_count\": 244502, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.6, \"weighting_method\": \"batch_adaptive_tau\", \"tau\": 0.7, \"n_min\": 2}, \"hypothesis\": \"Batch-adaptive τ on ρ=0.6 data: per-batch τ_batch = clamp(α_eff_natural + 0.3, 0.5, 0.95) adapts threshold to local contamination density. At higher contamination, more batches have high α_eff_natural, so adaptive τ should outperform fixed τ=0.8 more clearly than at ρ=0.4.\", \"parent\": \"batch_adaptive_tau_rho04_seed42\", \"conclusion\": \"failed\", \"failure_reason\": \"westd-47453 server down, data lost\", \"completed_at\": \"2026-05-17T10:50:00.000Z\"}, \"bs8_auto_nmin_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:16:38.352Z\", \"updated_at\": \"2026-05-17T10:50:00.000Z\", \"spec\": {\"command\": \"bash /root/provenance_weight_training/scripts/run_bs8_auto_nmin_seed42.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"370013\", \"log_path\": \"~/runs/provenance_weight_training/bs8_auto_nmin_seed42.log\", \"submitted_at\": \"2026-05-16T23:26:39.790Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.4, \"batch_size\": 8, \"n_min\": \"auto (max(2, bs//2) = 4)\", \"weighting_method\": \"adaptive\", \"tau\": 0.8}, \"hypothesis\": \"bs=8 with auto n_min=4 (max(2,bs//2)). Previous bs8_nmin2 failed (PPL=17.73) because explicit n_min=2 was too loose for bs=8. Auto n_min=4 should recover performance.\", \"parent\": \"bs8_nmin2_seed42_r2\", \"conclusion\": \"failed\", \"failure_reason\": \"westd-47453 server down, data lost\", \"completed_at\": \"2026-05-17T10:50:00.000Z\"}, \"grid_b0_3_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T03:08:31.061Z\", \"updated_at\": \"2026-05-17T10:50:00.000Z\", \"hypothesis\": \"b=0.3 is grid-optimal cross-seed (confirmed at seed42 PPL=17.640 < b=0.5 seed42 17.651). If seed123 also shows b=0.3 as best, confirms grid-best is not seed-specific and strengthens Claim 2 (adaptive ≈ grid-best).\", \"parent\": \"grid_b0_5_seed123\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_grid_b0_3_seed123.sh\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"396682\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_3_seed123.log\", \"submitted_at\": \"2026-05-17T07:32:54.221Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"failed\", \"failure_reason\": \"westd-47453 server down, data lost\", \"completed_at\": \"2026-05-17T10:50:00.000Z\"}, \"random_reweight_v2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:42:44.958Z\", \"updated_at\": \"2026-05-17T07:33:09.061Z\", \"spec\": {\"command\": \"bash scripts/run_random_reweight_v2_seed42.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"354002\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"weighting_method\": \"random\", \"log_path\": \"/root/autodl-tmp/output/models/random_reweight_v2_seed42/train.log\"}, \"hypothesis\": \"Random reweighting baseline v2: U(0,2) random weights (mean=1) replacing detector q-scores. Tests if detector signal is load-bearing — if random weights ≈ adaptive, detector is not contributing. Expected: adaptive > random → provenance signal matters.\", \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.83, \"eval_loss_holdout\": 2.8809}, \"checkpoint_path\": \"/root/autodl-tmp/output/models/random_reweight_v2_seed42\", \"completed_at\": \"2026-05-17T07:33:09.061Z\"}, \"tau_095_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:32.419Z\", \"updated_at\": \"2026-05-17T03:00:52.678Z\", \"hypothesis\": \"τ=0.95 forces α_eff > 0.95 before allowing downweighting, which should collapse b* toward near-max values (overfit to quality constraint) and degrade PPL toward ESS-only levels (~17.72), confirming the method requires τ ≤ 0.8 to balance quality and stability.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_095_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/tau_095_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T18:21:58.713Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:22:00.219145+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.723, \"eval_loss\": 2.8749, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 10.198, \"total_steps\": 6103, \"train_runtime_s\": 13699, \"train_samples_per_second\": 7.128, \"b_star_count\": 24412, \"b_star_mean\": 3.0775, \"b_star_median\": 1.52, \"b_star_std\": 3.9923, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.8, \"b_star_p75\": 3.46, \"b_star_pct_zero\": 0, \"b_star_pct_below_0.5\": 8.5, \"b_star_pct_0.5_to_1\": 24.7, \"b_star_pct_1_to_2\": 26.4, \"b_star_pct_above_2\": 40.3}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T18:29:07.389Z\"}, \"batch_adaptive_tau_rho04_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:16:32.221Z\", \"updated_at\": \"2026-05-17T03:00:22.336Z\", \"spec\": {\"hypothesis\": \"Batch-adaptive τ: τ_batch = clamp(α_eff_natural + 0.3, 0.5, τ). Reduces over-intervention on clean batches. Expected PPL ≤ fixed-τ adaptive (17.653).\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.4, \"command\": \"bash scripts/run_batch_adaptive_tau_rho04_seed42.sh\", \"server\": \"westd-47453\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"gpu\": \"cuda:2\", \"pid\": 326274}, \"conclusion\": \"negative\", \"metrics\": {\"eval_loss_holdout\": 2.8725, \"eval_ppl_holdout\": 17.681, \"train_loss\": 9.8206, \"train_runtime_sec\": 45402.86}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/batch_adaptive_tau_rho04_seed42/checkpoint-6103\", \"log_path\": \"/root/provenance_weight_training/output/logs/batch_adaptive_tau_rho04_seed42.log\", \"hypothesis\": \"Batch-adaptive τ (τ_batch = clamp(α_eff_natural + 0.3, 0.5, τ)) reduces over-intervention on clean batches by lowering τ when the batch already has low contamination, yielding lower holdout PPL than fixed τ=0.8.\", \"completed_at\": \"2026-05-16T23:44:28.133Z\", \"parent\": \"adaptive_fix_seed42\"}, \"p0_contamination_60_datagen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:37:10.827Z\", \"updated_at\": \"2026-05-17T03:00:18.545Z\", \"spec\": {\"command\": \"python scripts/prepare_rho06_data.py\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B (TF-IDF scoring)\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"log_path\": \"/root/provenance_weight_training/scripts/prepare_rho06_data.py\"}, \"conclusion\": \"success\", \"metrics\": {\"total_lines\": 371499, \"synthetic_count\": 222900, \"human_count\": 148599, \"actual_contamination_ratio\": 0.6, \"q_score_mean\": 0.6243, \"q_score_std\": 0.3703, \"q_score_median\": 0.7753, \"file_size_mb\": 907}, \"completed_at\": \"2026-05-15T20:08:12.383Z\", \"hypothesis\": \"TF-IDF scoring on ρ=0.6 contamination data produces well-calibrated bimodal q-scores that separate human/synthetic, enabling downstream adaptive reweighting experiments at higher contamination levels.\"}, \"datagen_synthetic_4gpu\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:12:11.474Z\", \"updated_at\": \"2026-05-17T03:00:16.173Z\", \"spec\": {\"command\": \"4x parallel generate_synthetic.py --depth 1 --num_tokens 33000000 --batch_size 128\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"data_count\": \"target 132M tokens across 4 shards\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": \"42/1042/2042/3042\", \"hypothesis\": \"4-GPU parallel generation produces 132M synthetic tokens in ~2.5h\", \"gpu\": \"cuda:0,1,2,3\", \"checkpoint_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"log_path\": \"/root/provenance_weight_training/data/synthetic/gen_gpu{0,1,2,3}.log\", \"total_docs\": 340992, \"total_tokens\": 132033764}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T21:50:46.682Z\", \"hypothesis\": \"4-GPU parallel synthetic data generation (Qwen3-0.6B, depth=1, 33M tokens/shard) produces sufficient scale and diversity for provenance contamination experiments while maintaining consistent stylistic distribution for detector calibration.\"}, \"grid_b5_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T02:52:56.873Z\", \"updated_at\": \"2026-05-17T03:00:06.065Z\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T11:22:30Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-14T15:09:25.359Z\", \"training_hours\": 3.78}, \"completed_at\": \"2026-05-14T11:20:36.319Z\", \"notes\": \"PID 94717 已确认存活（SSH 验证 2026-05-14T11:39）。旧 PID 92798 已 kill，cron 重新注册。\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"前次提交 (PID 92793) 未实际启动训练，标记 killed。等 eval PID 92274 完成后重新提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:36:18.619551+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:09:26.285900+00:00\"}]}, \"failure_reason\": \"\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"94717\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed123.log\"}, \"metrics\": {\"train_loss\": 10.8468, \"total_steps\": 6103, \"train_runtime_s\": 14434, \"gpu_hours\": 4.01, \"eval_ppl_holdout\": 17.8039, \"eval_loss\": 2.8794, \"eval_holdout_tokens\": 4077068}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b5_0_seed123/final/\", \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed123.log\", \"hypothesis\": \"Grid-b sweep b=5.0 seed=123: extreme downweighting (near-zero weight for synthetic). Establishes ceiling of degradation from over-aggressive fixed reweighting, proving that wrong b choice can be worse than no reweighting at all.\"}, \"grid_b3_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:56.285Z\", \"updated_at\": \"2026-05-17T03:00:04.124Z\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\", \"log_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:23:51.699Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:23:52.658692+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.7422, \"total_steps\": 6103, \"train_runtime_s\": 12955.83, \"gpu_hours\": 3.6, \"eval_ppl_holdout\": 17.76, \"eval_loss\": 2.877, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\", \"completed_at\": \"2026-05-14T14:24:22.860Z\", \"log_path\": \"~/runs/provenance_weight_training/grid_b3_0_seed123.log\", \"notes\": \"训练完成，eval 未执行（should_evaluate=false，缺少 --eval_data_path 和 --eval_steps）。Checkpoint: /root/provenance_weight_training/output/models/grid_b3_0_seed123/final/ (model.safetensors 1.19GB)。需补跑 eval。\", \"hypothesis\": \"Grid-b sweep b=3.0 seed=123: very aggressive downweighting well past optimal. Multi-seed confirmation that high-b regime consistently degrades PPL, strengthening the case that grid search sensitivity motivates adaptive b*.\"}, \"grid_b2_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:55.329Z\", \"updated_at\": \"2026-05-17T03:00:02.264Z\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed123 --weighting_method grid --grid_b_value 2.0 --contamination_ratio 0.4 --seed 123\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"88022\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.61, \"total_steps\": 6103, \"train_runtime_s\": 13058.8, \"gpu_hours\": 3.63, \"train_samples_per_second\": 7.478, \"train_steps_per_second\": 0.467, \"eval_ppl_holdout\": 17.725, \"eval_loss\": 2.875, \"eval_holdout_tokens\": 4077068}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:14:05.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:14:06.752002+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b2_0_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed123.log\", \"completed_at\": \"2026-05-14T14:14:33.471Z\", \"hypothesis\": \"Grid-b sweep b=2.0 seed=123: strong downweighting regime past optimal. PPL should degrade further, establishing that aggressive fixed-b over-suppresses synthetic data and motivates adaptive per-batch b* selection.\"}, \"grid_b1_5_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:43.491Z\", \"updated_at\": \"2026-05-17T03:00:00.380Z\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\", \"wall_clock_seconds\": 15053.1, \"gpu_hours\": 4.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:06:15.864Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:06:16.350913+00:00\"}]}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\", \"metrics\": {\"train_loss\": 10.4776, \"total_steps\": 6103, \"train_runtime_s\": 15053.1, \"gpu_hours\": 4.18, \"eval_ppl_holdout\": 17.701, \"eval_loss\": 2.8736}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:18:32.771Z\", \"hypothesis\": \"Grid-b sweep b=1.5 seed=123: testing diminishing returns region. PPL should be higher than b=1.0 as stronger downweighting begins to over-suppress useful synthetic samples, confirming U-shaped PPL-vs-b curve.\"}, \"grid_b1_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:42.784Z\", \"updated_at\": \"2026-05-17T02:59:58.125Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed123 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"68306\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_0_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:47.084Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_0_seed123/final/\", \"wall_clock_seconds\": 13950, \"gpu_hours\": 3.88}, \"reproduce\": {\"finished_at\": \"2026-05-14T10:46:17.839Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:46:18.691130+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.674, \"eval_loss\": 2.8721, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.218, \"total_steps\": 6103, \"train_runtime_s\": 13878, \"gpu_hours\": 3.88}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:53:00Z\", \"hypothesis\": \"Grid-b sweep b=1.0 seed=123: moderate exponential downweighting. Multi-seed data point establishing that b>0.5 yields diminishing returns, supporting the grid-b PPL curve monotonically increasing past optimal.\"}, \"grid_b0_5_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:42.314Z\", \"updated_at\": \"2026-05-17T02:59:55.641Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed123 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"68163\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:43.648Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_5_seed123/final/\", \"wall_clock_seconds\": 13678.0, \"gpu_hours\": 3.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T10:33:23.511Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:33:24.806181+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.638, \"eval_loss\": 2.87, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.601, \"total_steps\": 6103, \"train_runtime_s\": 13104, \"gpu_hours\": 3.8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:41:41.614Z\", \"hypothesis\": \"Grid-b sweep b=0.5 seed=123: multi-seed validation that b=0.5 is near-optimal in grid search. Establishes grid-best baseline PPL for comparison with adaptive b* (which should match without requiring grid search).\"}, \"hybrid_rho04_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:16:41.634Z\", \"updated_at\": \"2026-05-17T00:22:29.508Z\", \"spec\": {\"hypothesis\": \"Hybrid filter+reweight: remove q>0.95, then adaptive reweight remainder. Combines detect_remove's elimination of worst samples with adaptive's soft reweighting. Data: 253,584 rows (from 371,499).\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.4, \"command\": \"bash scripts/run_hybrid_rho04_seed42.sh\", \"server\": \"westd-41312\", \"data_path\": \"data/scored_data_hybrid.jsonl\", \"data_count\": 253584, \"gpu\": \"cuda:2\", \"pid\": 3656, \"tau\": 0.8, \"n_min\": 2, \"weighting_method\": \"adaptive\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/hybrid_rho04_seed42/final\", \"log_path\": \"/root/autodl-tmp/provenance_weight_training/output/logs/hybrid_rho04_seed42.log\", \"hypothesis\": \"Hybrid filter+reweight (remove q>0.95 then adaptive reweight remainder with rho=0.4) will achieve lower holdout PPL than pure adaptive reweighting by eliminating the most contaminated samples before soft reweighting, combining the strengths of detect_remove and adaptive methods.\", \"completed_at\": \"2026-05-17T00:22:23.173Z\", \"metrics\": {\"eval_loss_holdout\": 2.863, \"eval_ppl_holdout\": 17.514}}, \"threshold_q03_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T05:34:34.545Z\", \"updated_at\": \"2026-05-16T23:25:26.414Z\", \"hypothesis\": \"Hard-filter threshold sensitivity: remove q>0.3 samples, train uniformly on remaining. Paired with detect_remove (q>0.5) and threshold_q07 (q>0.7) to test if filtering requires precise threshold calibration while adaptive does not.\", \"reproduce\": {\"finished_at\": \"2026-05-16T10:30:31.843Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-16T10:30:32.935Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:30:35.110226+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash scripts/run_threshold_q03_seed42.sh (restart)\", \"server\": \"westd-47453\", \"data_path\": \"data/scored_data_filtered_q03.jsonl\", \"data_count\": 116935, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"gpu\": \"cuda:3\", \"pid\": 325196, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/threshold_q03_seed42/final\", \"log_path\": \"/root/autodl-tmp/threshold_q03_restart.log\"}, \"conclusion\": \"success\", \"notes\": \"Training completed successfully. 6103/6103 steps, train_loss=11.24, runtime=45076s (~12.5h). Model saved to output/models/threshold_q03_seed42/final (1.19GB safetensors). WANDB_MODE=disabled, offline run available at wandb/offline-run-20260516_184629-s7vw5rw5.\", \"metrics\": {\"eval_loss_holdout\": 2.848, \"eval_ppl_holdout\": 17.253}}, \"rho02_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:02:18.437Z\", \"updated_at\": \"2026-05-16T21:36:26.041Z\", \"spec\": {\"checkpoint_path\": \"output/models/rho02_uniform_seed42/final\", \"log_path\": \"output/logs/rho02_uniform_seed42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl_holdout\": 17.336, \"eval_loss_holdout\": 2.853, \"eval_holdout_tokens\": 4077068}, \"hypothesis\": \"Uniform weighting at ρ=0.2 contamination provides the baseline loss level; adaptive reweighting methods should achieve lower loss on clean validation data by downweighting contaminated samples.\", \"completed_at\": \"2026-05-16T21:32:06.395Z\"}, \"threshold_q07_seed42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-16T05:34:35.477Z\", \"updated_at\": \"2026-05-16T21:07:12.412Z\", \"hypothesis\": \"Hard-filter threshold sensitivity: remove q>0.7 samples (least aggressive, keeps most data+contamination), train uniformly. If PPL varies >0.1 across q=0.3/0.5/0.7 thresholds, proves filtering needs precise calibration while adaptive is threshold-free.\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-16T06:00:07.874Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_threshold_q07_seed42.sh\\\"\"}, \"completed_at\": \"2026-05-16T10:22:01.172Z\", \"notes\": \"Resume r2 failed: ValueError \\\"Your setup doesn't support bf16/gpu\\\" — all 4x GPUs were occupied by other processes when resume script launched. Training stuck at step 5999, checkpoint-5500 intact. Needs retry when GPU is free.\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"Resume r2 from checkpoint-5500 (stuck at step 5999 due to disk full + wandb error loop). wandb/ deleted, WANDB_MODE=disabled. 604 steps remaining.\"}}, \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_threshold_q07_resume_r2.sh'\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"355121\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_filtered_q07.jsonl\", \"data_count\": 184908, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"resume_from\": \"checkpoint-5500\"}, \"conclusion\": \"failed\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\"}, \"random_reweight_seed42\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-16T07:16:33.821Z\", \"updated_at\": \"2026-05-16T13:33:42.598Z\", \"hypothesis\": \"Random reweighting baseline: U(0,2) random weights (mean=1) replacing detector q-scores. Tests if detector signal is load-bearing — if random weights ≈ adaptive, detector is not contributing. Expected: adaptive > random → provenance signal matters.\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-16T07:16:51.087Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && bash scripts/run_random_reweight_seed42.sh\\\"\", \"finished_at\": \"2026-05-16T10:22:28.062Z\", \"training_hours\": 3.09}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-16T07:17:18.186Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:17:20.059724+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T09:30:52.354459+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:22:31.379909+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: wandb.errors.UsageError: No API key configured — 脚本未继承 WANDB_API_KEY 环境变量 | fix_worker_id: worker_diagnose_random_reweight_seed42_20260516T072019 | 修复后将重提交到 cuda:2\"}}, \"notes\": \"根因诊断：实际只跑~500步(8%)，\\\"6092/8477\\\"是eval进度条非training。WANDB_MODE=offline写~150MB到30GB根分区→磁盘满→OOM killer在eval期间杀进程→save从未执行→零checkpoint。修复：WANDB_MODE=disabled + output_dir改数据盘。v2脚本已dry-run验证通过。\", \"spec\": {\"command\": \"bash scripts/run_random_reweight_seed42.sh\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"weighting_method\": \"random\", \"contamination_ratio\": 0.4, \"gpu\": \"cuda:2\", \"pid\": 318752, \"log_path\": \"~/runs/provenance_weight_training/random_reweight_seed42.log\", \"checkpoint_path\": \"output/models/random_reweight_seed42\", \"num_train_tokens\": 200000000, \"max_steps\": 6103}, \"conclusion\": \"failed\"}, \"contamination_60_tau06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:04:51.670Z\", \"updated_at\": \"2026-05-16T07:15:22.736Z\", \"spec\": {\"hypothesis\": \"ρ=0.6 τ=0.6 diagnostic: second data point for ρ=0.6 τ-PPL curve. Tests deeper τ downshift for higher contamination.\", \"parent\": \"contamination_60_seed42_r2\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_tau06_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.6 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"287971\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"log_path\": \"~/runs/provenance_weight_training/contamination_60_tau06_seed42.log\", \"account\": \"root\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\"}, \"hypothesis\": \"ρ=0.6 τ=0.6 diagnostic: second data point for ρ=0.6 τ-PPL curve. Tests deeper τ downshift for higher contamination.\", \"parent\": \"contamination_60_seed42_r2\", \"notes\": \"D045 第二数据点。GPU 队列: cuda:2 (ess_only 完成后)。脚本: scripts/run_contamination_60_tau06.sh。优先级最高。\", \"checkpoint_path\": \"output/models/contamination_60_tau06_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_tau06_seed42.log\", \"metrics\": {\"eval_ppl_holdout\": 17.7359, \"eval_loss_holdout\": 2.8756, \"eval_holdout_tokens\": 4077068, \"train_loss\": 8.9804, \"train_runtime_seconds\": 13367.3, \"train_samples_per_second\": 7.305, \"total_steps\": 6103, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:15:22.736Z\"}, \"contamination_60_tau07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:04:49.597Z\", \"updated_at\": \"2026-05-16T06:10:38.506Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_tau07_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --tau 0.7 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"282223\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_tau07_seed42.log\", \"submitted_at\": \"2026-05-16T02:09:01.658Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 14272.7, \"gpu_hours\": 3.96}, \"hypothesis\": \"ρ=0.6 τ=0.7 diagnostic: Reviewer-suggested formula τ=1-ρ×0.5=0.7. Tests if τ downshift recovers adaptive to grid-best level (PPL≤17.71 target).\", \"parent\": \"contamination_60_seed42_r2\", \"notes\": \"D045 最高优先级。cuda:0, PID=282223, ρ=0.6 τ=0.7 (formula τ=1-ρ×0.5)。参数确认: tau=0.7, n_min=2, ρ=0.6, data=scored_data_60.jsonl (371499 samples)。\\n\\n**结果分析**: PPL=17.73。vs τ=0.8(17.74): -0.01 改善，formula 方向正确。vs grid-best(17.704): +0.026 未达标。vs uniform(17.766): -0.036 显著优于。vs ESS-only(17.77): -0.04。\\n\\n**Claim 3 解读**: formula τ=1-ρ×0.5 给出正确方向但非必需——default τ=0.8 已足够好（τ sensitivity 低）。支持 \\\"proportion-agnostic\\\" framing：无需知道 ρ 即可有效工作。\", \"reproduce\": {\"finished_at\": \"2026-05-16T05:58:17.061Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:58:19.203891+00:00\"}]}, \"checkpoint_path\": \"output/models/contamination_60_tau07_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_tau07_seed42.log\", \"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.875, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.358, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:06:54.366Z\"}, \"detect_remove_baseline_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:26:48.402Z\", \"updated_at\": \"2026-05-16T05:25:32.239Z\", \"hypothesis\": \"Detect-and-remove baseline: hard-filter q&gt;0.5 samples then train uniformly on remaining data. Answers reviewer question \\\"why not just filter instead of reweight?\\\" Expected to underperform adaptive weighting due to information loss from discarded samples.\", \"parent\": \"uniform_seed42\", \"notes\": \"完成时 conclusion 指引: b=0 throughout; adaptive degenerates to uniform post-filtering. detect-and-remove alone sufficient — adaptive adds no value on already-clean data. 写论文时注意: filtered subset (~153K) 训练 200M tokens 重复 ~2.4x，而 adaptive 用全部 ~371K 只过 1 遍，effective epoch 不同需在 experiment section 说明。\", \"spec\": {\"checkpoint_path\": \"output/models/detect_remove_baseline_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/detect_remove_baseline_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T05:19:15.608Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T05:19:17.956961+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.29, \"eval_loss_holdout\": 2.8499, \"eval_holdout_tokens\": 4077068, \"train_loss\": 11.003, \"train_runtime_seconds\": 13248, \"total_steps\": 6103, \"train_samples_per_second\": 7.371}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:25:32.239Z\"}, \"grid_b0_3_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:26:45.815Z\", \"updated_at\": \"2026-05-16T05:03:15.767Z\", \"hypothesis\": \"Grid-b sweep b=0.3 on ρ=0.4 data, seed42. Near suspected optimal region (grid-best b=0.5). Tests if b<0.5 improves PPL. Part of b* curve characterization for Claim 2.\", \"parent\": \"grid_b_seed42_batch\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --weighting_method grid --grid_b_value 0.3 --seed 42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"pid\": 274304, \"log_path\": \"/root/runs/provenance_weight_training/grid_b0_3_seed42.log\", \"submitted_at\": \"2026-05-16T01:13:08.506Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_3_seed42/final\", \"wall_clock_seconds\": 13807.3, \"gpu_hours\": 3.84}, \"reproduce\": {\"finished_at\": \"2026-05-16T04:57:12.423Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:57:14.788065+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.64, \"eval_loss_holdout\": 2.8702, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"train_loss\": 9.1154, \"train_runtime_seconds\": 13365.79, \"train_samples_per_second\": 7.306, \"total_steps\": 6103, \"b_fixed\": 0.3, \"alpha_eff_typical_range\": \"0.07-0.88\", \"ess_typical_range\": \"2.3-4.0\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T05:03:15.767Z\"}, \"tau_095_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:22:54.457Z\", \"updated_at\": \"2026-05-16T03:05:15.616Z\", \"hypothesis\": \"τ=0.95 rerun with correct n_min=2 (original tau_095_seed42 used n_min=3 confound). Most strict α_eff threshold, may over-constrain b*.\", \"parent\": \"tau_095_seed42\", \"completed_at\": \"2026-05-16T02:45:16.182Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"notes\": \"D048: 原始 tau_095_seed42 已确认 n_min=2，数据干净。二次 killed，不重跑。\", \"conclusion\": \"killed\"}, \"tau_09_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T01:22:52.989Z\", \"updated_at\": \"2026-05-16T03:05:14.824Z\", \"hypothesis\": \"τ=0.9 rerun with correct n_min=2 (original tau_09_seed42 used n_min=3 confound). Tests if τ>0.8 still degrades with corrected n_min.\", \"parent\": \"tau_09_seed42\", \"completed_at\": \"2026-05-16T02:45:15.433Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"killed\"}}, \"notes\": \"D048: 原始 tau_09_seed42 已确认 n_min=2，数据干净。二次 killed，不重跑。\", \"conclusion\": \"killed\"}, \"nmin5_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:52:01.911Z\", \"updated_at\": \"2026-05-16T03:03:02.805Z\", \"spec\": {\"hypothesis\": \"n_min=5 > batch_size=4, code clamps to n_min=4, ESS(b=0)=4 is only feasible point → b*=0 always → degenerate uniform case. Validates theoretical prediction.\", \"parent\": \"adaptive_fix_seed42\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T03:03:02.017Z\", \"notes\": \"D047 砍掉，GPU 预算不够。\"}, \"grid_b5_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:39.050Z\", \"updated_at\": \"2026-05-16T03:01:26.368Z\", \"hypothesis\": \"Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T00:52:41.923Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:31:34.604Z\", \"training_hours\": 8.65}, \"failure_reason\": \"\", \"notes\": \"checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。\", \"completed_at\": \"2026-05-15T07:46:15.281Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:46:16.570901+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:35.946616+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"方案 A 重跑：无 inline eval，从 checkpoint-3000 恢复（~3100 步剩余）。PID=183240, cuda:2, timeout=5h。训练完后 post-hoc eval。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b5_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"183240\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.993, \"eval_loss\": 2.89, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.488, \"total_steps\": 6103, \"train_runtime_s\": 6601, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b5_0_seed456/final\", \"conclusion\": \"success\"}, \"grid_b3_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:38.011Z\", \"updated_at\": \"2026-05-16T03:01:25.067Z\", \"hypothesis\": \"Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T00:52:41.254Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:31:37.181Z\", \"training_hours\": 8.65}, \"failure_reason\": \"\", \"notes\": \"checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。\", \"completed_at\": \"2026-05-15T07:46:09.092Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:46:12.926805+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:39.113223+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"方案 A 重跑：无 inline eval，从 checkpoint-3000 恢复（~3100 步剩余）。PID=183446, cuda:3, timeout=5h。训练完后 post-hoc eval。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b3_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"183446\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b3_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.921, \"eval_loss\": 2.886, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.435, \"total_steps\": 6103, \"train_runtime_s\": 6602, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b3_0_seed456/final\", \"conclusion\": \"success\"}, \"grid_b2_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:37.073Z\", \"updated_at\": \"2026-05-16T03:01:24.083Z\", \"hypothesis\": \"Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T22:22:43.944Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:15:04.029Z\", \"training_hours\": 10.87}, \"failure_reason\": \"eval overhead timeout at 65.5% (checkpoint-3500 available). Eval dataset 8477 samples × every 500 steps caused ~40min per eval round, exceeding original timeout.\", \"completed_at\": \"2026-05-15T07:31:09.178Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:31:10.598336+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:15:05.368569+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"恢复自 checkpoint-3500（原超时于 65.5%）。timeout 增至 6h（原因：eval 8477 条 × 每 500 步 ≈ 40min/轮）。PID=182488, cuda:0。\"}}, \"notes\": \"checkpoint_artifact: true. D026 决策：seed456 b≥2.0 的 PPL 异常高（checkpoint 问题），论文只报 2-seed 数据。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b2_0_seed456/checkpoint-3500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"183161\", \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed456.log\", \"submitted_at\": \"2026-05-15T07:40:59.398Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6408.6, \"gpu_hours\": 1.78}, \"metrics\": {\"eval_ppl_holdout\": 17.989, \"eval_loss\": 2.8898, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.625, \"total_steps\": 6103, \"train_runtime_s\": 12969, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.53, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b2_0_seed456/final\", \"conclusion\": \"success\"}, \"ess_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:20:13.656Z\", \"updated_at\": \"2026-05-16T03:01:02.547Z\", \"hypothesis\": \"ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T09:13:26.412Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed42 --weighting_method ess_only --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T12:50:22.690Z\", \"training_hours\": 3.62}, \"spec\": {\"n_min\": 2, \"weighting_method\": \"ess_only\"}, \"pid\": \"189240\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:50:24.148259+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl\": 17.73, \"eval_loss\": 2.875, \"b_star_median\": 1.58, \"b_star_mean\": 3.51, \"vs_uniform_ppl_delta\": \"+0.038\", \"vs_adaptive_ppl_delta\": \"+0.08\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/ess_only_seed42\", \"completed_at\": \"2026-05-15T13:29:03.148Z\"}, \"adaptive_v2_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:19.549Z\", \"updated_at\": \"2026-05-16T02:50:32.828Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed456 performance (baseline adaptive PPL=17.64)\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\", \"completed_at\": \"2026-05-16T02:50:32.054Z\"}, \"adaptive_v2_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:19.157Z\", \"updated_at\": \"2026-05-16T02:50:31.386Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed123 performance (baseline adaptive PPL=17.63)\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\", \"completed_at\": \"2026-05-16T02:50:30.507Z\"}, \"adaptive_v2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:18.265Z\", \"updated_at\": \"2026-05-16T02:50:29.963Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) fixes ESS clamping issue, achieves meaningful improvement over uniform baseline for seed=42\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\", \"completed_at\": \"2026-05-16T02:50:29.147Z\"}, \"tau_07_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:22:51.146Z\", \"updated_at\": \"2026-05-16T02:45:14.675Z\", \"spec\": {\"hypothesis\": \"τ=0.7 rerun with correct n_min=2 (original tau_07_seed42 used n_min=3 confound). Slightly below optimal τ=0.8.\", \"parent\": \"tau_07_seed42\"}, \"hypothesis\": \"τ=0.7 rerun with correct n_min=2 (original tau_07_seed42 used n_min=3 confound). Slightly below optimal τ=0.8.\", \"parent\": \"tau_07_seed42\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:45:14.675Z\"}, \"tau_06_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:22:49.217Z\", \"updated_at\": \"2026-05-16T02:45:13.922Z\", \"spec\": {\"hypothesis\": \"τ=0.6 rerun with correct n_min=2 (original tau_06_seed42 used n_min=3 confound). Tests lower τ region with proper ESS constraint.\", \"parent\": \"tau_06_seed42\"}, \"hypothesis\": \"τ=0.6 rerun with correct n_min=2 (original tau_06_seed42 used n_min=3 confound). Tests lower τ region with proper ESS constraint.\", \"parent\": \"tau_06_seed42\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:45:13.922Z\"}, \"tau_05_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:22:47.367Z\", \"updated_at\": \"2026-05-16T02:45:13.057Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_05_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.5 --n_min 2 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"281298\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_nmin2_seed42.log\", \"submitted_at\": \"2026-05-16T01:58:41.186Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2791.9, \"gpu_hours\": 0.78}, \"hypothesis\": \"τ=0.5 rerun with correct n_min=2 (original tau_05_seed42 used n_min=3 confound). Most permissive α_eff threshold, expect b*≈0 for many batches.\", \"parent\": \"tau_05_seed42\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:45:13.057Z\"}, \"contamination_60_seed42_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:53:48.975Z\", \"updated_at\": \"2026-05-16T01:57:12.472Z\", \"hypothesis\": \"Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on higher contamination data. Tests graceful degradation as ρ increases from 0.4→0.6.\", \"parent\": \"contamination_60_seed42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"257977\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed42_r2.log\", \"submitted_at\": \"2026-05-15T21:54:22.934Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14569.5, \"gpu_hours\": 4.05}, \"pid\": \"257977\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed42_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42_r2 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-16T01:51:18.700Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:51:20.683620+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.74, \"eval_loss_holdout\": 2.8759, \"eval_tokens\": 4077068, \"eval_method\": \"sliding_window_2048_stride1024\", \"train_loss\": 9.6349, \"train_runtime_seconds\": 14092.25}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/contamination_60_seed42_r2/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:57:12.472Z\"}, \"contamination_60_grid_b0_5_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:25.407Z\", \"updated_at\": \"2026-05-16T01:47:52.701Z\", \"hypothesis\": \"ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to higher contamination, or if adaptive b* adapts better.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_grid_b0_5_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method grid --grid_b_value 0.5 --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"255781\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log\", \"submitted_at\": \"2026-05-15T21:49:22.242Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 13153.5, \"gpu_hours\": 3.65}, \"parent\": \"grid_b0_5_seed456\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"reproduce\": {\"finished_at\": \"2026-05-16T01:28:34.213Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:28:35.712Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:28:37.428483+00:00\"}]}, \"notes\": \"训练完成 6103/6103 steps。EXIT_CODE=129 (SIGHUP) 发生在训练完成后（与 contamination_60_uniform_seed42 同一模式）。WANDB_MODE=disabled 导致 cron 误判为 failed。实际 success，等 eval PPL。\", \"metrics\": {\"eval_ppl\": 17.704, \"eval_loss\": 2.8738, \"eval_tokens\": 4077068, \"eval_docs\": 5000}, \"checkpoint_path\": \"output/models/contamination_60_grid_b0_5_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_grid_b0_5_seed42.log\"}, \"contamination_60_uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:24.785Z\", \"updated_at\": \"2026-05-16T01:12:50.897Z\", \"hypothesis\": \"ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher contamination for comparison with adaptive and grid methods.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"250074\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\", \"submitted_at\": \"2026-05-15T21:26:23.538Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12988.3, \"gpu_hours\": 3.61, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/contamination_60_uniform_seed42/final\"}, \"parent\": \"uniform_seed42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T21:19:46.484Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_uniform_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --contamination_ratio 0.6 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-16T01:02:50.356Z\", \"training_hours\": 3.72}, \"pid\": \"250074\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_uniform_seed42.log\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:02:51.880Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:02:54.397978+00:00\"}]}, \"notes\": \"训练实际已完成 (6103/6103 steps, 3:35:04)。模型已保存到 output/models/contamination_60_uniform_seed42/final。EXIT_CODE=129 (SIGHUP) 发生在训练完成后。WANDB_MODE=disabled 导致 cron 误判为 failed。train_loss=7.649 (avg), train_runtime=12904s。需要 eval 获取 PPL。\", \"metrics\": {\"eval_ppl_holdout\": 17.766, \"eval_loss_holdout\": 2.8773, \"eval_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl\", \"train_loss\": 7.649, \"train_runtime_seconds\": 12904}, \"checkpoint_path\": \"output/models/contamination_60_uniform_seed42/final\"}, \"bs8_nmin2_seed42_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:48:45.682Z\", \"updated_at\": \"2026-05-16T00:26:45.368Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"238714\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin2_seed42_r2.log\", \"submitted_at\": \"2026-05-15T18:48:45.530Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training resubmit, not eval)\", \"eval_data\": \"N/A (training resubmit, not eval)\", \"wall_clock_seconds\": 14753.4, \"gpu_hours\": 4.1}, \"hypothesis\": \"batch_size=8 with n_min=2 (correct coupling: n_min=max(2,bs//2)=4→override to 2 for wider ESS dynamic range [2,8]). Resubmit after zombie cleanup on cuda:2. Parent: bs8_nmin2_seed42 (OOM due to zombie).\", \"parent\": \"bs8_nmin2_seed42\", \"plan_id\": \"p0_batchsize_8\", \"notes\": \"训练完成 6103/6103 steps, train_loss=5.4065. EXIT_CODE=129 (SIGHUP) 发生在训练完成后 W&B finalization 阶段，不影响结果。Checkpoint 验证通过。Eval PPL=17.73 > uniform avg 17.694 (+0.036), 与 ESS-only 水平相当(~17.72)。**NEGATIVE but informative**: B=8, n_min=2 (n_min/B=0.25) 导致 ESS range [2,8] 过宽，b* 无法有效约束。与 B=4,n_min=2 (n_min/B=0.5, works) 和 B=4,n_min=4 (n_min/B=1.0, degenerates to uniform) 共同支持 coupling rule n_min=⌊B/2⌋ 的必要性。Director 决策：写入 experiments n_min analysis，不放 limitation section。\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:54:37.472Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-15T22:54:38.917Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:54:40.392745+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.73, \"eval_loss_holdout\": 2.8752, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16\", \"train_loss\": 5.4065, \"train_steps\": 6103, \"train_runtime_seconds\": 14621.6}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/bs8_nmin2_seed42/final\"}, \"grid_b_low_serial_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:56:07.484Z\", \"updated_at\": \"2026-05-15T23:43:07.407Z\", \"hypothesis\": \"Grid-b low sweep (b=0.1, 0.2, 0.3 serial, hardcoded) on ρ=0.4 data, seed42. No shell variables — each b value hardcoded to avoid quoting issues. R3 of grid_b_low_seed42.\", \"parent\": \"grid_b_seed42_batch\", \"spec\": {\"command\": \"bash /root/provenance_weight_training/run_grid_b_low_serial.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"265606\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_serial_seed42.log\", \"submitted_at\": \"2026-05-15T23:33:20.929Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 351.2, \"gpu_hours\": 0.1}, \"conclusion\": \"killed\", \"notes\": \"R4 killed: cuda:2 GPU冲突，与contamination_60_ess_only_seed42双进程占满显存(93042/97887 MiB)，仅完成48/6103步。第3次因GPU冲突失败(R3=cuda:0撞contamination_60, R4=cuda:2撞ess_only)。PID 265617已确认死亡，cuda:2显存恢复至~46.5GB，ess_only速度从~4.5s/it恢复至2.12s/it。需在空卡上R5重启——cuda:1预计~1h21m后释放（contamination_60_uniform完成）。\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T23:33:18.725Z\", \"command\": \"bash /root/provenance_weight_training/run_grid_b_low_serial.sh\"}, \"pid\": \"265606\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_serial_seed42.log\", \"completed_at\": \"2026-05-15T23:39:12.167Z\"}, \"grid_b_low_seed42_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:53:08.449Z\", \"updated_at\": \"2026-05-15T21:57:46.419Z\", \"hypothesis\": \"Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. R3: uses standalone shell script to avoid quoting issues. Confirms behavior in b<0.5 region.\", \"parent\": \"grid_b_low_seed42_r2\", \"spec\": {\"command\": \"bash /root/provenance_weight_training/scripts/run_grid_b_low_seed42.sh\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\"}, \"conclusion\": \"failed\", \"notes\": \"Worker 提交时未指定 GPU，导致与 cuda:0 上的 contamination_60_seed42_r2 冲突。PID 258500 在启动后秒级崩溃。grid_b_low 需在 GPU 释放后单独提交（每个 b 值独立实验或硬编码脚本 + 显式 CUDA_VISIBLE_DEVICES）。\", \"completed_at\": \"2026-05-15T21:57:46.419Z\"}, \"grid_b_low_seed42_r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:19:36.129Z\", \"updated_at\": \"2026-05-15T21:55:52.896Z\", \"hypothesis\": \"Low-b grid sweep (b=0.1, 0.2, 0.3) on ρ=0.4 data, seed42. Confirms behavior in b<0.5 region — expect minimal reweighting effect and PPL close to uniform. Establishes that b=0.5 is already near the lower useful bound.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && for b in 0.1 0.2 0.3; do echo '=== Training grid b='$b' ===' && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b_low_b${b}_seed42 --weighting_method grid --grid_b_value $b --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 || exit 1; done\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"256582\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_seed42_r2.log\", \"submitted_at\": \"2026-05-15T21:50:10.451Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 24.1, \"gpu_hours\": 0.01}, \"parent\": \"grid_b_seed42_batch\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"reproduce\": {\"finished_at\": \"2026-05-15T21:50:31.477Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T21:50:34.583Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:50:36.985471+00:00\"}]}, \"notes\": \"失败根因：bash -c \\\"...\\\" 双引号内的 $b 被外层 shell 提前展开为空字符串，导致 --grid_b_value 收到空参数，argparse 报错 \\\"expected one argument\\\" 立即退出。日志首行 \\\"Training grid b= ===\\\" 确认 $b 为空。修复方法：将 $b 转义为 \\\\$b（如 \\\\$b 和 \\\\${b}），或改用 bash -c '...'（需处理内部单引号），或拆成三条独立命令分别指定 b=0.1/0.2/0.3。\"}, \"baseline_qwen3_0.6b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:53:53.450Z\", \"updated_at\": \"2026-05-15T21:54:29.041Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints models/Qwen/Qwen3-0.6B --data_path data/human/eval_holdout.jsonl --max_docs 5000\", \"server\": \"westd-47453\", \"data_path\": \"data/human/eval_holdout.jsonl\", \"data_count\": 5000, \"model_name\": \"Qwen3-0.6B\", \"seed\": 0, \"checkpoint_source\": \"models/Qwen/Qwen3-0.6B\", \"eval_data\": \"data/human/eval_holdout.jsonl\", \"checkpoint_path\": \"models/Qwen/Qwen3-0.6B\", \"log_path\": \"/root/runs/provenance_weight_training/qwen3_0.6b_baseline_eval.log\"}, \"checkpoint_path\": \"models/Qwen/Qwen3-0.6B\", \"log_path\": \"/root/runs/provenance_weight_training/qwen3_baseline_eval.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:54:15.419Z\", \"hypothesis\": \"Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute improvement from training.\", \"metrics\": {\"eval_ppl_holdout\": 22.97, \"eval_loss\": 3.134, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"sliding_window_stride1024_maxlen2048_fp16\"}, \"notes\": \"Baseline PPL=22.9654 (loss=3.1340), tokens=4,077,068, time=249s. Weight SHA256=f47f71177f32bcd101b7573ec9171e6a57f4f4d31148d38e382306f42996874b. Pretrained weights confirmed (std ~0.02-0.03, layernorm varies across layers). Compared to ess_only_seed456 PPL=17.72: continued pretraining reduces PPL by 22.8%.\"}, \"contamination_60_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:12:18.751Z\", \"updated_at\": \"2026-05-15T21:26:20.768Z\", \"spec\": {\"data_path\": \"data/scored_data_60.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"contamination_ratio\": 0.6, \"hyperparams\": {\"n_min\": 2, \"tau\": 0.8, \"batch_size\": 4, \"gradient_accumulation_steps\": 4, \"learning_rate\": 5e-05, \"max_length\": 2048}}, \"hypothesis\": \"ρ=0.6 contamination robustness test: adaptive weighting (τ=0.8, n_min=2) on higher contamination ratio data. Baseline adaptive_fix_seed42 (ρ=0.4) PPL=17.6527. Tests if adaptive method degrades gracefully as contamination increases from 0.4→0.6.\", \"parent\": \"adaptive_fix_seed42\", \"notes\": \"数据验证通过: scored_data_60.jsonl 371,499行/907MB, synthetic=222900/human=148599, actual ρ=0.6。q_score: mean=0.6243, std=0.3703, median=0.7753。字段: text/depth/source_model/prompt_tokens/generated_tokens/decoding/q_score。符号链接 scored_data_rho06.jsonl → scored_data_60.jsonl。配置基于 adaptive_fix_seed42，改 data_path + contamination_ratio=0.6。\\n\\n**失败诊断**: GPU 分配冲突——实验被分配到 cuda:2，但 bs8_nmin2_seed42_r2 (pid=238714) 已在 cuda:2 运行，占用 79.78 GiB 显存。启动 24 秒即 OOM。非代码问题，需在空闲 GPU 上重试。\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T21:23:32.567Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data_60.jsonl --output_dir output/models/contamination_60_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.6 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T21:23:56.641Z\", \"training_hours\": 0.01}, \"pid\": \"249588\", \"log_path\": \"~/runs/provenance_weight_training/contamination_60_seed42.log\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 48.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 34.81 MiB is free. Process 238719 has 79.78 GiB memory in use. Including non-PyTorch memory, this process has 15.14 GiB memory in use. Of the allocated \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T21:23:57.827Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:23:59.292519+00:00\"}]}}, \"nmin4_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:36:45.229Z\", \"updated_at\": \"2026-05-15T21:22:25.975Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"225265\", \"log_path\": \"~/runs/provenance_weight_training/nmin4_seed42.log\", \"submitted_at\": \"2026-05-15T16:44:47.426Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 16658.5, \"gpu_hours\": 4.63}, \"hypothesis\": \"n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T16:43:55.347Z\", \"finished_at\": \"2026-05-15T21:16:33.618Z\", \"training_hours\": 4.54}, \"notes\": \"Mid-training check @step 2036/6103: b=0.0, ess=4.0 (=n_min), weighted_loss==unweighted_loss — confirms b*=0 degenerates to uniform weighting as theoretically predicted. Eval commands prepared for post-training.\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:16:35.372420+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.6947, \"eval_loss\": 2.8733, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"train_loss\": 7.989, \"total_steps\": 6103, \"train_runtime_s\": 16231, \"train_samples_per_second\": 6.016, \"b_star_count\": 24412, \"b_star_mean\": 0, \"b_star_median\": 0, \"b_star_std\": 0, \"b_star_min\": 0, \"b_star_max\": 0, \"b_star_pct_zero\": 100, \"ess_mean\": 4, \"ess_min\": 4, \"ess_max\": 4}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/nmin4_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/nmin4_seed42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:22:25.975Z\"}, \"bs8_nmin2_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:48.783Z\", \"updated_at\": \"2026-05-15T18:48:29.014Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"237410\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin2_seed42.log\", \"submitted_at\": \"2026-05-15T18:39:14.671Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 37.4, \"gpu_hours\": 0.01}, \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"pid\": \"237410\", \"log_path\": \"~/runs/provenance_weight_training/bs8_nmin2_seed42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T18:39:50.935Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 128.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 116.81 MiB is free. Process 236702 has 79.78 GiB memory in use. Including non-PyTorch memory, this process has 15.06 GiB memory in use. Of the allocate\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T18:39:52.061Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:39:53.502042+00:00\"}]}, \"notes\": \"OOM failed: GPU 2 was occupied by zombie PID 236702 (old bs8_seed42). Superseded by bs8_nmin2_seed42_r2. Config: n_min=2, bs=8, grad_accum=2, tau=0.8, adaptive, seed=42.\"}, \"bs8_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:04:41.935Z\", \"updated_at\": \"2026-05-15T18:43:36.187Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 4 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"236697\", \"log_path\": \"~/runs/provenance_weight_training/bs8_seed42.log\", \"submitted_at\": \"2026-05-15T18:31:59.603Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 695.9, \"gpu_hours\": 0.19}, \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"pid\": \"236697\", \"log_path\": \"~/runs/provenance_weight_training/bs8_seed42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 4 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 3 --save_only_model --bf16\\\"\", \"finished_at\": \"2026-05-15T18:43:32.689Z\"}, \"conclusion\": \"failed\", \"notes\": \"Killed at 1% (71/6103 steps). Wrong config: n_min=4 matches same ESS/bs ratio as n_min=2/bs=4. Director instructed restart with n_min=2 + bs=8 for wider ESS dynamic range [2,8]. Replaced by bs8_nmin2_seed42.\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-15T18:43:35.489Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:43:39.292154+00:00\"}]}}, \"tau_09_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:28.658Z\", \"updated_at\": \"2026-05-15T18:07:01.223Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.9_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/tau_09_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:48:21.169Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:48:25.502664+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_ppl_holdout\": 17.712, \"eval_loss\": 2.8742, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 2.36, \"b_star_median\": 1.32, \"b_star_std\": 3.04, \"b_star_pct_above_2\": 33.7}, \"completed_at\": \"2026-05-15T18:07:01.223Z\"}, \"tau_07_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:27.838Z\", \"updated_at\": \"2026-05-15T17:57:12.394Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"209824\", \"log_path\": \"~/runs/provenance_weight_training/tau_07_seed42.log\", \"submitted_at\": \"2026-05-15T13:35:52.041Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\", \"wall_clock_seconds\": 15680.4, \"gpu_hours\": 4.36}, \"reproduce\": {\"finished_at\": \"2026-05-15T17:48:03.537Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T17:48:04.960427+00:00\"}]}, \"metrics\": {\"train_loss\": 9.6707, \"total_steps\": 6103, \"train_runtime_s\": 15065, \"train_samples_per_second\": 6.482, \"eval_ppl_holdout\": 17.6793, \"eval_loss\": 2.8724, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.8943, \"b_star_median\": 0.58, \"b_star_std\": 1.4007, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.3306, \"b_star_p75\": 0.9712, \"b_star_pct_zero\": 5.8, \"b_star_pct_below_0.5\": 36, \"b_star_pct_0.5_to_1\": 34.2, \"b_star_pct_1_to_2\": 16.2, \"b_star_pct_above_2\": 7.7}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.7_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/tau_07_seed42.log\", \"completed_at\": \"2026-05-15T17:57:12.394Z\"}, \"tau_06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:01:37.442Z\", \"updated_at\": \"2026-05-15T17:09:55.541Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\", \"parent\": \"adaptive_fix_seed42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T10:01:53.614Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\"\", \"finished_at\": \"2026-05-15T13:47:39.608Z\", \"training_hours\": 3.76}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"195746\", \"log_path\": \"~/runs/provenance_weight_training/tau_06_seed42.log\", \"submitted_at\": \"2026-05-15T10:01:55.290Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13972.6, \"gpu_hours\": 3.88, \"tau\": 0.6, \"seed\": 42, \"rho\": 0.4, \"model\": \"Qwen3-0.6B\", \"tokens\": \"200M\", \"method\": \"adaptive\", \"parent\": \"adaptive_fix_seed42\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\", \"eval_results_path\": \"/root/provenance_weight_training/output/eval/posthoc_eval_tau_06_seed42.json\"}, \"pid\": \"195746\", \"log_path\": \"~/runs/provenance_weight_training/tau_06_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:47:40.932954+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.6805, \"eval_loss\": 2.8725, \"train_loss\": 9.275, \"total_steps\": 6103, \"train_runtime_s\": 13436.64, \"train_samples_per_second\": 7.267, \"b_star_mean\": 0.5899, \"b_star_median\": 0.3746, \"b_star_std\": 1.0693, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.1195, \"b_star_p75\": 0.66, \"b_star_zero_frac\": 0.156, \"b_star_nonzero_mean\": 0.699, \"b_star_nonzero_median\": 0.4473}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\", \"completed_at\": \"2026-05-15T13:54:47.892Z\", \"notes\": \"PPL=17.681 劣于 τ=0.8 baseline (17.650)，conclusion=negative。概念修正：τ 越低 → α_eff 下界越松 → b* 更小 → 降权力度更弱（非更激进）。正确因果链：τ 越高 → α_eff 下界越严 → min-intervention 需要更大 b* 才能满足约束 → 降权力度更强。\"}, \"tau_05_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:27.263Z\", \"updated_at\": \"2026-05-15T17:06:51.535Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.5_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.5 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"205652\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_seed42.log\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\"}, \"gpu\": \"cuda:1\", \"server\": \"westd-47453\", \"reproduce\": {\"finished_at\": \"2026-05-15T16:40:01.070Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:40:02.552045+00:00\"}]}, \"metrics\": {\"train_loss\": 8.849, \"total_steps\": 6103, \"epoch\": 0.26, \"train_runtime_s\": 13431.4, \"train_samples_per_second\": 7.27, \"eval_ppl_holdout\": 17.688, \"eval_loss\": 2.8729, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15\", \"b_star_count\": 24412, \"b_star_mean\": 0.3923, \"b_star_median\": 0.1707, \"b_star_std\": 0.8821, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0, \"b_star_p75\": 0.4366, \"b_star_pct_zero\": 29.1, \"b_star_pct_below_0.5\": 78.4, \"b_star_pct_0.5_to_1\": 12.9, \"b_star_pct_1_to_2\": 5.7, \"b_star_pct_above_2\": 2.9}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T16:44:08.996Z\", \"checkpoint_path\": \"output/models/tau_0.5_seed42/final\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_seed42.log\"}, \"adaptive_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:03.137Z\", \"updated_at\": \"2026-05-15T16:43:10.982Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"59058\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed456.log\", \"submitted_at\": \"2026-05-14T02:46:25.330Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"output/models/adaptive_seed456/final\", \"wall_clock_seconds\": 15161.8, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2354, \"train_runtime_s\": 13130.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.437, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.09-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6419, \"eval_loss_holdout\": 2.8703, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.64/4080000 from inline eval\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:07.123Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"adaptive_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:02.771Z\", \"updated_at\": \"2026-05-15T16:43:08.120Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"58978\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed123.log\", \"submitted_at\": \"2026-05-14T02:46:24.381Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"output/models/adaptive_seed123/final\", \"wall_clock_seconds\": 15162.4, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13197.18, \"total_steps\": 6103, \"train_samples_per_second\": 7.399, \"train_steps_per_second\": 0.462, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.04-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.6308, \"eval_loss_holdout\": 2.8696, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.63/4080000 from inline eval\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:06.757Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:01.824Z\", \"updated_at\": \"2026-05-15T16:43:05.333Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"58888\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed42.log\", \"submitted_at\": \"2026-05-14T02:46:23.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"output/models/adaptive_seed42/final\", \"wall_clock_seconds\": 15162.9, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13115.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.445, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.03-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.644, \"eval_loss_holdout\": 2.8704, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:05.861Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"uniform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:55.165Z\", \"updated_at\": \"2026-05-15T16:42:59.635Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"47890\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed456.log\", \"submitted_at\": \"2026-05-13T23:23:58.435Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed456/final/\", \"wall_clock_seconds\": 12349.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.2895, \"total_steps\": 6103, \"train_duration_s\": 11974, \"eval_ppl_holdout\": 17.7015, \"eval_loss_holdout\": 2.8737, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.70/4080000 from inline eval\"}, \"completed_at\": \"2026-05-14T02:49:47.621Z\"}, \"uniform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:53.217Z\", \"updated_at\": \"2026-05-15T16:42:57.800Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"47749\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed123.log\", \"submitted_at\": \"2026-05-13T23:23:55.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed123/final/\", \"wall_clock_seconds\": 12350.8, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3121, \"total_steps\": 6103, \"train_duration_s\": 11994, \"eval_ppl_holdout\": 17.6861, \"eval_loss_holdout\": 2.8728, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}, \"completed_at\": \"2026-05-14T02:49:46.681Z\"}, \"uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:51.722Z\", \"updated_at\": \"2026-05-15T16:42:55.867Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"47603\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed42.log\", \"submitted_at\": \"2026-05-13T23:23:53.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed42/final/\", \"wall_clock_seconds\": 12352.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3104, \"total_steps\": 6103, \"train_duration_s\": 11946, \"eval_ppl_holdout\": 17.6939, \"eval_loss_holdout\": 2.8732, \"eval_holdout_tokens\": 4077068, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\", \"eval_note\": \"unified post-hoc eval 2026-05-15; was 17.69/4080000 from inline eval\"}, \"completed_at\": \"2026-05-14T02:49:45.269Z\"}, \"detector_modernbert\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:40:06.106Z\", \"updated_at\": \"2026-05-15T15:51:50.219Z\", \"conclusion\": \"killed\", \"hypothesis\": \"ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human text with AUC>=0.95 and ECE<=0.05\", \"notes\": \"Superseded by TF-IDF detector (detector_tfidf_lr). Never ran — cancelled at QUEUED stage.\", \"completed_at\": \"2026-05-15T15:51:50.219Z\"}, \"nmin1_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:48:31.298Z\", \"updated_at\": \"2026-05-15T14:36:49.692Z\", \"hypothesis\": \"n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T09:34:56.077Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T14:27:21.174Z\", \"training_hours\": 4.87}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"194005\", \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:06.479Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18033.6, \"gpu_hours\": 5.01}, \"pid\": \"194005\", \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:27:22.547409+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.789, \"eval_loss\": 2.8786, \"eval_holdout_tokens\": 4077068, \"b_star_mean\": 7.197, \"b_star_median\": 1.746, \"b_star_std\": 8.374, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.803, \"b_star_p75\": 20, \"b_star_zero_frac\": 0.019, \"b_star_pct_below_0.5\": 13.1, \"b_star_pct_0.5_to_1\": 19.1, \"b_star_pct_1_to_2\": 21.1, \"b_star_pct_above_2\": 46.7, \"b_star_count\": 24412, \"alpha_eff_mean\": 0.714, \"alpha_eff_median\": 0.8}, \"notes\": \"训练完成(EXIT_CODE=0, 4h50m)。PPL=17.789，比 adaptive_fix(n_min=2, 17.650) 差 +0.139，比 uniform(17.690) 差 +0.099。n_min=1 导致极端 b* 分布：46.7% batch b*≥2，p75=20.0(上限)，mean=7.197。ESS 约束几乎失效，over-downweighting 明显。confirms n_min=2 是更优选择。\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/nmin1_seed42\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:36:40.056Z\"}, \"golden_ratio_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:20:12.943Z\", \"updated_at\": \"2026-05-15T13:33:31.162Z\", \"hypothesis\": \"Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T09:34:55.278Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T13:21:54.212Z\", \"training_hours\": 3.78}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"193921\", \"log_path\": \"~/runs/provenance_weight_training/golden_ratio_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:04.200Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14247.0, \"gpu_hours\": 3.96}, \"pid\": \"193921\", \"log_path\": \"/root/provenance_weight_training/output/models/golden_ratio_seed42/step_metrics.jsonl\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:21:55.558374+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.654, \"eval_loss\": 2.871, \"train_loss\": 2.1145, \"train_loss_last500\": 2.109, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_s\": 13442, \"gpu_hours\": 3.73}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/golden_ratio_seed42/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:33:31.162Z\"}, \"tau_0.6_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:58:48.894Z\", \"updated_at\": \"2026-05-15T12:39:47.541Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\", \"parent\": \"adaptive_fix_seed42\", \"conclusion\": \"killed\", \"notes\": \"废弃: exp_id 含点号不合法，已用 tau_06_seed42 替代\", \"completed_at\": \"2026-05-15T12:39:47.541Z\"}, \"grid_b_low_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T01:18:54.793Z\", \"updated_at\": \"2026-05-15T09:33:21.503Z\", \"hypothesis\": \"Grid-b extension to b<0.5 (b=0.1/0.2/0.3 serial), seed42, confirming whether grid-best lies at b=0.5 or below\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-15T05:23:13.303Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:02:07.651872+00:00\"}]}, \"spec\": {\"command\": \"bash run_grid_b_low_seed42.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"163662\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_seed42.log\", \"submitted_at\": \"2026-05-15T09:20:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 774.2, \"gpu_hours\": 0.22}, \"notes\": \"cron框架误杀(infrastructure bug)。根因: WANDB_MODE=disabled + tmux wrapper PID 不匹配，reconcile_crons 判定进程死亡并发送 SIGTERM。训练实际曾完成 3 个 b 值(8477/8477×3)，但第二次重启后在 step 431 被杀，所有 checkpoint 目录丢失(grid_b0_1/0_2/0_3_seed42 不存在)。需在 cuda:2/3 释放后完全重跑。\", \"reproduce\": {\"finished_at\": \"2026-05-15T09:02:05.942Z\"}, \"conclusion\": \"failed\"}, \"grid_b1_5_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:59:35.658Z\", \"updated_at\": \"2026-05-15T01:03:24.328Z\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T21:10:45.479Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_5_seed456 --weighting_method grid --grid_b_value 1.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:50:58.269Z\", \"training_hours\": 3.67}, \"pid\": \"142985\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_5_seed456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:51:00.583331+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b1_5_seed456/final\", \"metrics\": {\"train_loss\": 10.435, \"total_steps\": 6103, \"train_runtime_s\": 12950.16, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.54, \"eval_loss\": 2.8741, \"eval_ppl_holdout\": 17.71, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.875, \"eval_tokens\": 5004058}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:56:27.189Z\"}, \"grid_b1_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:59:34.733Z\", \"updated_at\": \"2026-05-15T01:03:23.307Z\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T21:10:44.681Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed456 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:50:55.540Z\", \"training_hours\": 3.67}, \"pid\": \"142902\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_0_seed456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:50:56.660568+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b1_0_seed456/final\", \"metrics\": {\"train_loss\": 10.178, \"total_steps\": 6103, \"train_runtime_s\": 12963.87, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.532, \"eval_loss\": 2.8725, \"eval_ppl_holdout\": 17.68, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.8734, \"eval_tokens\": 5004058}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:56:26.614Z\"}, \"grid_b0_5_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:58:17.956Z\", \"updated_at\": \"2026-05-15T01:03:04.640Z\", \"hypothesis\": \"Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T21:10:43.728Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:57:32.591Z\", \"training_hours\": 3.78}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T21:13:26.329Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:13:27.262433+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:57:33.835977+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA OOM at step 0 — GPU 0 被 3 个进程挤爆（PID 138525: 68.61GiB + PID 139132: 19.21GiB + 本进程 7.08GiB > 94.97GiB）。实验分配 cuda:1 但进程实际跑在 GPU 0 上，疑 CUDA_VISIBLE_DEVICES 未正确注入或有残留进程干扰。已有成果: 无（0% 进度）。建议: 清理 GPU 0 残留进程后在 cuda:1 上重新提交，补充 --eval_data_path 和 --eval_steps 参数。\"}}, \"notes\": \"重提交成功（retry_count=1）。原 OOM 因 cuda:1 残留 eval 进程。已清理 exit marker，日志重定向正常。step 56/6103, ETA ~3.5h。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"144400\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed456.log\", \"submitted_at\": \"2026-05-14T21:20:21.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"wall_clock_seconds\": 13363.5, \"gpu_hours\": 3.71}, \"pid\": 145062, \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed456.log\", \"metrics\": {\"train_loss\": 9.5622, \"total_steps\": 6103, \"train_runtime_s\": 12953.96, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.538, \"eval_loss\": 2.8705, \"eval_ppl_holdout\": 17.65, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"output/models/grid_b0_5_seed456/final\", \"conclusion\": \"success\"}, \"grid_b_seed42_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:50:09.001Z\", \"updated_at\": \"2026-05-14T22:21:47.253Z\", \"spec\": {\"command\": \"bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"50134\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_seed42_batch.log\", \"submitted_at\": \"2026-05-13T23:50:08.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 81098.3, \"gpu_hours\": 22.53}, \"hypothesis\": \"Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*\", \"metrics\": {\"b_values\": [0.5, 1, 1.5, 2, 3, 5], \"b0_5_train_loss\": 9.598, \"b0_5_completed\": true, \"b1_0_completed\": true, \"b1_5_completed\": true, \"b2_0_current_step\": 5149, \"b2_0_total_steps\": 6103, \"completed_b_values\": [0.5, 1, 1.5, 2, 3], \"current_b\": 5, \"total_steps\": 6103, \"current_step\": 3422, \"b5_0_progress_pct\": 56, \"eta_minutes\": 95, \"b2_0_completed\": true, \"b2_0_train_loss\": 10.621, \"b2_0_train_runtime_s\": 13034, \"b3_0_completed\": true, \"b3_0_train_loss\": 10.754, \"b3_0_train_runtime_s\": 13036, \"all_completed\": true, \"b1_0_train_loss\": 10.223, \"b1_5_train_loss\": 10.485, \"b5_0_train_loss\": 10.858, \"b0_5_runtime_s\": 13036, \"b1_0_runtime_s\": 12968, \"b1_5_runtime_s\": 14789, \"b2_0_runtime_s\": 13034, \"b3_0_runtime_s\": 13036, \"b5_0_runtime_s\": 13115, \"note\": \"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\", \"b0_5_eval_ppl\": 17.651, \"b1_0_eval_ppl\": 17.692, \"b1_5_eval_ppl\": 17.718, \"b2_0_eval_ppl\": 17.741, \"b3_0_eval_ppl\": 17.774, \"b5_0_eval_ppl\": 17.818, \"eval_holdout_tokens\": 4077068, \"best_b\": 0.5, \"best_eval_ppl\": 17.651}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:05:39.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:05:40.772794+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/models/grid_b{0.5,1.0,1.5,2.0,3.0,5.0}_seed42/final/\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_seed42_batch.log\", \"completed_at\": \"2026-05-14T22:21:47.253Z\"}, \"diagnostic_contamination100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:14:09.555Z\", \"updated_at\": \"2026-05-14T08:48:08.828Z\", \"hypothesis\": \"Diagnostic: does 100% synthetic contamination significantly degrade held-out PPL vs 40%? If PPL ≈ 17.7, contamination sensitivity is too low for this scale.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/synthetic_only.jsonl --output_dir output/models/diagnostic_contamination100_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 20000000 --seed 42\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"77187\", \"data_path\": \"data/synthetic_only.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:48:07.663Z\", \"notes\": \"Director 指令 kill：GPU 2/3 显存打满影响 grid-b seed123 训练速度。诊断实验等 grid-b round 1 完成后重跑。\"}, \"detector_tfidf_lr\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:08.894Z\", \"updated_at\": \"2026-05-13T23:28:28.425Z\", \"spec\": {\"command\": \"python train_tfidf_detector.py (combo_degrade: unigrams, max_features=10000, C=0.01, truncate 100 words)\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/detector.jsonl\", \"data_count\": 67960, \"model_name\": \"TF-IDF + LogisticRegression\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/detector_tfidf/\", \"log_path\": \"/root/provenance_weight_training/output/detector_tfidf/calibration_results.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replacing over-accurate ModernBERT (D007)\", \"metrics\": {\"auc\": 0.939, \"accuracy\": 0.858, \"ece_raw\": 0.24, \"ece_calibrated\": 0.048, \"temperature_T\": 0.204, \"q_score_mean\": 0.6, \"q_score_std\": 0.374, \"q_score_median\": 0.707, \"mid_range_ratio\": 0.463}, \"completed_at\": \"2026-05-13T23:28:28.425Z\"}}, \"count\": 269, \"total\": 269, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3498}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 20_

Registry 太大，用 subagent 进行数字交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "35e5f795-9a01-495d-bc07-ad7e590280bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9Y7Y7UWXMNeNzW69f5Cym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 29717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 650
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

_source line 21_

<details open><summary>🔧 Tool call — Agent · `toolu_019aZNmieHiQcRF1tuv1dBPQ`</summary>

```json
{
  "description": "Audit numbers against registry",
  "prompt": "You are auditing numbers in a research paper against an experiment registry. The registry data is saved at:\n`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt`\n\nIt is JSON with schema `{result: string}` — the `result` field is itself a string that contains the actual registry content (likely JSON or YAML). Probe with jq first to understand structure, then extract data.\n\nI need you to find and verify the following specific numbers that appear in the paper. For each number, tell me:\n1. Whether it exists in the registry\n2. The exact registry experiment ID and metric field it comes from\n3. Whether the paper value matches the registry value exactly\n\n**Numbers to verify:**\n\n### Experimental results (PPL values)\n- Adaptive τ=0.7 5-seed mean holdout PPL: 17.674 (paper says this in introduction)\n- Uniform baseline 5-seed mean: 17.694\n- D&R q>0.7 3-seed PPL: 17.250 (introduction says \"PPL 17.250 vs. 17.674, 3 seeds\")\n- Δ = -0.023 at ρ=0.4 (introduction: \"$\\Delta{=}{-}0.023$ at $\\rho{=}0.4$\")\n- Δ = -0.032 at ρ=0.6 (introduction: \"$-$0.032 at $\\rho{=}0.6$\")\n- Epoch-matched gap Δ=0.017 (introduction: \"reducing the gap to $\\Delta{=}0.017$\")\n- \">95%\" of advantage from multi-epoch (introduction and abstract)\n\n### Detector metrics\n- AUC = 0.94 (related work: \"AUC\\,=\\,0.94\")\n- ECE = 0.048 (from reference numbers)\n\n### Data/model specs\n- 132M tokens\n- 371,499 samples\n- ρ = 0.4\n- Qwen3-0.6B\n\n### Method section\n- Pearson r ≈ 0.79 for α_eff correlation (method section)\n- ~50% of batches where quality constraint binds (introduction: \"${\\sim}$50\\% of batches\")\n- ~5.9× lower sharpening exponents (introduction)\n\n### Related work external numbers\n- \"20-60% of web corpora\" synthetic content\n- Drayson et al. b=10 for ≤360M, b=1 for 1.7B\n- ModernBERT-150M detector AUC=0.986\n- WikiText-2 ~2M tokens\n- Golden ratio reciprocal ≈0.62\n\nAlso check: are there any numbers related to p-values? The reference says:\n- p_BH = 0.011 for adaptive τ=0.7\n- p_BH = 0.064 for ρ=0.6 adaptive\n- SD = 0.006 for adaptive τ=0.7\n\nSearch for these in the registry too.\n\n**Output format**: For each number, report:\n- Paper value\n- Registry value (if found), with experiment ID\n- Match? Yes/No/Not in registry\n- Any discrepancies\n\nBe thorough — probe the registry structure first, then search systematically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "fbca0745-85a0-4a14-adff-dc912e3ca68e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9Y7Y7UWXMNeNzW69f5Cym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 29717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 650
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


### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Audit numbers against registry",
  "task_type": "local_agent",
  "prompt": "You are auditing numbers in a research paper against an experiment registry. The registry data is saved at:\n`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt`\n\nIt is JSON with schema `{result: string}` — the `result` field is itself a string that contains the actual registry content (likely JSON or YAML). Probe with jq first to understand structure, then extract data.\n\nI need you to find and verify the following specific numbers that appear in the paper. For each number, tell me:\n1. Whether it exists in the registry\n2. The exact registry experiment ID and metric field it comes from\n3. Whether the paper value matches the registry value exactly\n\n**Numbers to verify:**\n\n### Experimental results (PPL values)\n- Adaptive τ=0.7 5-seed mean holdout PPL: 17.674 (paper says this in introduction)\n- Uniform baseline 5-seed mean: 17.694\n- D&R q>0.7 3-seed PPL: 17.250 (introduction says \"PPL 17.250 vs. 17.674, 3 seeds\")\n- Δ = -0.023 at ρ=0.4 (introduction: \"$\\Delta{=}{-}0.023$ at $\\rho{=}0.4$\")\n- Δ = -0.032 at ρ=0.6 (introduction: \"$-$0.032 at $\\rho{=}0.6$\")\n- Epoch-matched gap Δ=0.017 (introduction: \"reducing the gap to $\\Delta{=}0.017$\")\n- \">95%\" of advantage from multi-epoch (introduction and abstract)\n\n### Detector metrics\n- AUC = 0.94 (related work: \"AUC\\,=\\,0.94\")\n- ECE = 0.048 (from reference numbers)\n\n### Data/model specs\n- 132M tokens\n- 371,499 samples\n- ρ = 0.4\n- Qwen3-0.6B\n\n### Method section\n- Pearson r ≈ 0.79 for α_eff correlation (method section)\n- ~50% of batches where quality constraint binds (introduction: \"${\\sim}$50\\% of batches\")\n- ~5.9× lower sharpening exponents (introduction)\n\n### Related work external numbers\n- \"20-60% of web corpora\" synthetic content\n- Drayson et al. b=10 for ≤360M, b=1 for 1.7B\n- ModernBERT-150M detector AUC=0.986\n- WikiText-2 ~2M tokens\n- Golden ratio reciprocal ≈0.62\n\nAlso check: are there any numbers related to p-values? The reference says:\n- p_BH = 0.011 for adaptive τ=0.7\n- p_BH = 0.064 for ρ=0.6 adaptive\n- SD = 0.006 for adaptive τ=0.7\n\nSearch for these in the registry too.\n\n**Output format**: For each number, report:\n- Paper value\n- Registry value (if found), with experiment ID\n- Match? Yes/No/Not in registry\n- Any discrepancies\n\nBe thorough — probe the registry structure first, then search systematically.",
  "uuid": "1f673aea-9374-45d7-be81-f15c4d55fcf9",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


## Round 1

## Round 1

122 recorded events


### User

_source line 23 · 2026-05-25T19:42:45.621Z_

You are auditing numbers in a research paper against an experiment registry. The registry data is saved at:
`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt`

It is JSON with schema `{result: string}` — the `result` field is itself a string that contains the actual registry content (likely JSON or YAML). Probe with jq first to understand structure, then extract data.

I need you to find and verify the following specific numbers that appear in the paper. For each number, tell me:
1. Whether it exists in the registry
2. The exact registry experiment ID and metric field it comes from
3. Whether the paper value matches the registry value exactly

**Numbers to verify:**

### Experimental results (PPL values)
- Adaptive τ=0.7 5-seed mean holdout PPL: 17.674 (paper says this in introduction)
- Uniform baseline 5-seed mean: 17.694
- D&R q>0.7 3-seed PPL: 17.250 (introduction says "PPL 17.250 vs. 17.674, 3 seeds")
- Δ = -0.023 at ρ=0.4 (introduction: "$\Delta{=}{-}0.023$ at $\rho{=}0.4$")
- Δ = -0.032 at ρ=0.6 (introduction: "$-$0.032 at $\rho{=}0.6$")
- Epoch-matched gap Δ=0.017 (introduction: "reducing the gap to $\Delta{=}0.017$")
- ">95%" of advantage from multi-epoch (introduction and abstract)

### Detector metrics
- AUC = 0.94 (related work: "AUC\,=\,0.94")
- ECE = 0.048 (from reference numbers)

### Data/model specs
- 132M tokens
- 371,499 samples
- ρ = 0.4
- Qwen3-0.6B

### Method section
- Pearson r ≈ 0.79 for α_eff correlation (method section)
- ~50% of batches where quality constraint binds (introduction: "${\sim}$50\% of batches")
- ~5.9× lower sharpening exponents (introduction)

### Related work external numbers
- "20-60% of web corpora" synthetic content
- Drayson et al. b=10 for ≤360M, b=1 for 1.7B
- ModernBERT-150M detector AUC=0.986
- WikiText-2 ~2M tokens
- Golden ratio reciprocal ≈0.62

Also check: are there any numbers related to p-values? The reference says:
- p_BH = 0.011 for adaptive τ=0.7
- p_BH = 0.064 for ρ=0.6 adaptive
- SD = 0.006 for adaptive τ=0.7

Search for these in the registry too.

**Output format**: For each number, report:
- Paper value
- Registry value (if found), with experiment ID
- Match? Yes/No/Not in registry
- Any discrepancies

Be thorough — probe the registry structure first, then search systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "e55ceddf-aae4-45f2-9a5d-a8efc8a031eb"
}
```

</details>

---


### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Reading ~/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt",
  "usage": {
    "total_tokens": 15778,
    "tool_uses": 1,
    "duration_ms": 3038
  },
  "last_tool_name": "Read",
  "uuid": "ac0c4a32-d073-4b32-9ae9-f3d91c0a09f8",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01FAgSAPxhqRGc9kQBmpW8To`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "92f63a31-7ed6-4290-aed9-b10fbbf1d337",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHusvpv4JzFPWWj7dqhGWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15763,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15763,
        "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-25T19:42:49.191Z_

<details><summary>↩ Tool result · reported error · `toolu_01FAgSAPxhqRGc9kQBmpW8To`</summary>

```text
File content (194926 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "ae53cb11-a6af-4044-a413-f6268590fece",
  "tool_use_result": "Error: File content (194926 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Probe registry JSON structure",
  "usage": {
    "total_tokens": 16854,
    "tool_uses": 2,
    "duration_ms": 8177
  },
  "last_tool_name": "Bash",
  "uuid": "de72f23e-efe6-48b7-9b77-b24ec878d3e5",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mx1eqXURddbeKDAoTiBn1J`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\n# Check top-level keys\nprint('Top-level keys:', list(data.keys()))\nprint('Type of result:', type(data.get('result')))\nresult_str = data['result']\nprint('First 500 chars of result:', result_str[:500])\n\"",
  "description": "Probe registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "85f3b2f6-c92d-4e7b-a374-1bafdb688e30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CCb1AXcmJ6VLUcDEZBhVbp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 15763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
        "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-25T19:42:53.978Z_

<details><summary>↩ Tool result · `toolu_01Mx1eqXURddbeKDAoTiBn1J`</summary>

```text
Top-level keys: ['result']
Type of result: &lt;class 'str'>
First 500 chars of result: {"success": true, "data": {"experiments": {"detect_remove_q07_seed456": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-25T04:35:47.832Z", "updated_at": "2026-05-25T09:01:28.560Z", "hypothesis": "D&R q>0.7 threshold seed=456 replicate. Retains ~50% data (184,908/370k). Cross-seed for error bar with seed42 (r3) and seed123.", "parent": "detect_remove_q07_seed42_r3", "spec": {"command": "CUDA_VISIBLE_DEVICES=3 python -u training/pretrain_weighted.py --data_path data/scored_data_filtere
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "8e74445e-f8d6-4f3e-b9a7-732aa9e13b76"
}
```

</details>

---


### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running List all experiment IDs",
  "usage": {
    "total_tokens": 17432,
    "tool_uses": 3,
    "duration_ms": 12855
  },
  "last_tool_name": "Bash",
  "uuid": "c0044ea4-b74d-4111-832c-62c108347bdd",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_014jKDSxxfRhPzG1crTifqqH`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nprint('Result keys:', list(result.keys()))\nprint('Data keys:', list(result['data'].keys()))\nexps = result['data']['experiments']\nprint('Number of experiments:', len(exps))\nprint('Experiment IDs:', list(exps.keys()))\n\"",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "8c5fad53-a513-4699-a436-3015146c9bcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6h1jjeiwNGEJw1d8mHzWH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 16839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 505,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 32 · 2026-05-25T19:42:58.575Z_

<details><summary>↩ Tool result · `toolu_014jKDSxxfRhPzG1crTifqqH`</summary>

```text
Result keys: ['success', 'data', 'error', 'metadata']
Data keys: ['experiments', 'count', 'total', 'baseline']
Number of experiments: 269
Experiment IDs: ['detect_remove_q07_seed456', 'detect_remove_q07_seed123', 'detect_remove_q07_seed42_r3', 'detect_remove_q07_seed42_r2', 'detect_remove_q03_seed42', 'detect_remove_q05_seed42', 'eval_dr_q05_ckpt5500', 'detect_remove_q07_seed42', 'random_subset_epoch_seed42', 'contamination_20_tau07_seed42', 'permuted_score_control_seed42', 'p0_nmin_5', 'p0_batchsize_16', 'adaptive_seed789', 'adaptive_seed234', 'uniform_seed234', 'uniform_seed789', 'aeff_only_nmin1_seed456', 'bs8_nmin4_adaptive_seed456_r2', 'bs8_nmin4_uniform_seed456_r2', 'aeff_only_nmin1_seed123', 'aeff_only_nmin1_seed42', 'bs8_nmin4_uniform_seed456', 'bs8_nmin4_adaptive_seed456', 'bs8_nmin4_uniform_seed123_r2', 'bs8_nmin4_adaptive_seed123_r2', 'rho03_adaptive_seed456_r2', 'rho03_uniform_seed456', 'rho03_adaptive_seed456', 'batchsize16_nmin8_r2', 'eval_uniform_1_7b_v3', 'eval_adaptive_1_7b_v2', 'bs8_nmin4_uniform_seed123', 'bs8_nmin4_adaptive_seed123', 'rho03_uniform_seed123', 'rho03_uniform_seed42', 'rho03_adaptive_seed123', 'rho03_adaptive_seed42', 'random_reweight_seed456', 'bs8_nmin4_uniform_seed42', 'bs8_nmin4_adaptive_seed42', 'detect_remove_q05_v2_seed456', 'random_reweight_v2_seed456', 'uniform_epoch_matched_seed456', 'dr_epoch_matched_seed456', 'detect_remove_q05_v2_seed123_r2', 'bs16_uniform_seed456', 'bs16_adaptive_tau07_seed456', 'dr_epoch_matched_seed123_r2', 'random_reweight_seed123', 'bs16_adaptive_tau07_seed123_r2', 'detect_remove_q05_v2_seed123', 'dr_epoch_matched_seed123', 'bs16_uniform_seed123', 'detect_remove_q05_v2_seed42', 'bs16_adaptive_tau07_seed123', 'bs16_uniform_seed42', 'bs16_adaptive_tau07_seed42', 'dr_epoch_matched_indep_lr_v2_seed42', 'uniform_epoch_matched_indep_lr_seed42', 'random_reweight_baseline_seed42', 'dr_epoch_matched_indep_lr_seed42', 'grid_b0_1_seed42', 'rho02_adaptive_tau08_seed42', 'ess_only_seed123', 'ess_only_seed456', 'qwen06b_uniform_seed42', 'rho06_tau07_seed456', 'rho06_tau07_seed123', 'ngram_adaptive_seed42', 'gpt2_adaptive_seed456_v2', 'adaptive_tau08_scratch_seed42_v3', 'ngram_adaptive_seed456_v2', 'gpt2_adaptive_seed123_v3', 'gpt2_adaptive_seed456', 'ngram_adaptive_seed456', 'gpt2_adaptive_seed123_v2', 'adaptive_tau08_scratch_seed42_v2', 'gpt2_adaptive_seed123', 'adaptive_tau08_scratch_seed42', 'ngram_adaptive_seed123', 'adaptive_1_7b_seed456', 'uniform_1_7b_seed456', 'adaptive_ood_seed456', 'adaptive_ood_seed123', 'uniform_1_7b_seed123', 'adaptive_fix_seed456', 'adaptive_fix_seed123', 'uniform_1_7b_seed42_v5', 'adaptive_1_7b_seed42_v5', 'adaptive_1_7b_seed123', 'contamination_60_uniform_seed456', 'eval_adaptive_1_7b_seed123', 'eval_uniform_1_7b_seed123', 'detect_remove_q05_epoch_matched', 'contamination_60_adaptive_seed123_tau08', 'contamination_60_adaptive_seed42_tau08', 'adaptive_fix_seed42', 'adaptive_rho06_tau07_seed123', 'adaptive_rho06_tau07_seed456', 'adaptive_rho06_tau07_seed42', 'adaptive_1_7b_seed42_v4', 'uniform_1_7b_seed42_v4', 'detect_remove_q04_seed42', 'detect_remove_q03_seed42_r2', 'detect_remove_q08_seed42', 'adaptive_1_7b_seed42_v3', 'uniform_1_7b_seed42_v3', 'detect_remove_q01_seed42', 'detect_remove_q03_seed456', 'detect_remove_q03_seed123', 'detect_remove_q05_seed456', 'detect_remove_q05_seed123', 'detect_remove_q02_seed42', 'epoch_matched_dr_seed456', 'epoch_matched_dr_seed123', 'eval_q04', 'eval_q03_r2', 'eval_rho06_batch_v7', 'eval_q01_final_v2', 'eval_q07_final', 'eval_q06', 'eval_epoch_matched_seed456', 'eval_epoch_matched_seed123', 'eval_ngram_uniform', 'eval_ngram_adaptive', 'uniform_seed42_downstream', 'adaptive_fromscratch_seed42', 'hybrid_rho06_seed42', 'rho06_tau07_seed42', 'tau07_seed42', 'tau07_seed456', 'tau07_seed123', 'tau07_downstream_eval', 'uniform_ood_seed123', 'uniform_ood_seed456', 'w2_distribution_matching_eval', 'detect_remove_q07_epoch_matched_seed42', 'detect_remove_q09_epoch_matched_seed42', 'detect_remove_q01_epoch_matched_seed42', 'ngram_uniform_seed42', 'detect_remove_q03_epoch_matched_seed42', 'gpt2_adaptive_seed42', 'gpt2_uniform_seed42', 'detect_remove_q06_seed42', 'adaptive_1_7b_planb_control', 'eval_q01_final', 'adaptive_1_7b_seed42', 'status_check_41312', 'eval_adaptive_1_7b', 'eval_uniform_1_7b_v2', 'eval_uniform_1_7b_resumed', 'uniform_1_7b_seed42', 'detect_remove_q09_seed42', 'contamination_60_ess_only_seed456', 'contamination_60_ess_only_seed123', 'ess_only_seed456_r2', 'ess_only_seed123_r2', 'detect_remove_q05_epoch_matched_seed42', 'contamination_60_random_seed123', 'contamination_60_random_seed456', 'uniform_1_7b_seed42_r2', 'adaptive_1_7b_seed42_r2', 'eval_rho06_batch_v6', 'env_probe_41312_v2', 'env_probe_41312', 'eval_rho06_batch_v5', 'contamination_60_grid_b0_3_seed42', 'contamination_60_random_seed42', 'grid_b0_2_seed456', 'grid_b0_2_seed123', 'contamination_60_adaptive_seed456', 'grid_b0_1_seed123', 'grid_b0_1_seed456', 'contamination_60_ess_only_seed42', 'contamination_60_uniform_seed123', 'contamination_60_seed123', 'grid_b0_3_seed123_r2', 'grid_b0_3_seed456_r2', 'batchsize16_nmin8_r3', 'grid_b0_3_seed456', 'batch_adaptive_tau_rho06_r5', 'random_reweight_seed123_r5', 'rho02_adaptive_tau09_r5', 'bs8_auto_nmin_r5', 'llama3b_adaptive_seed42', 'batchsize16_nmin8_seed42', 'llama3b_uniform_seed42', 'random_reweight_seed123_r4', 'rho02_adaptive_tau09_r4', 'random_reweight_seed123_r3', 'grid_b0_2_seed42', 'rho02_adaptive_tau09_r3', 'batch_adaptive_tau_rho06_r3', 'bs8_auto_nmin_r3', 'random_reweight_seed123_r2', 'rho02_adaptive_tau09_r2', 'batch_adaptive_tau_rho06_r2', 'bs8_auto_nmin_r2', 'rho02_adaptive_tau09_seed42', 'batch_adaptive_tau_rho06_seed42', 'bs8_auto_nmin_seed42', 'grid_b0_3_seed123', 'random_reweight_v2_seed42', 'tau_095_seed42', 'batch_adaptive_tau_rho04_seed42', 'p0_contamination_60_datagen', 'datagen_synthetic_4gpu', 'grid_b5_0_seed123', 'grid_b3_0_seed123', 'grid_b2_0_seed123', 'grid_b1_5_seed123', 'grid_b1_0_seed123', 'grid_b0_5_seed123', 'hybrid_rho04_seed42', 'threshold_q03_seed42', 'rho02_uniform_seed42', 'threshold_q07_seed42', 'random_reweight_seed42', 'contamination_60_tau06_seed42', 'contamination_60_tau07_seed42', 'detect_remove_baseline_seed42', 'grid_b0_3_seed42', 'tau_095_nmin2_seed42', 'tau_09_nmin2_seed42', 'nmin5_seed42', 'grid_b5_0_seed456', 'grid_b3_0_seed456', 'grid_b2_0_seed456', 'ess_only_seed42', 'adaptive_v2_seed456', 'adaptive_v2_seed123', 'adaptive_v2_seed42', 'tau_07_nmin2_seed42', 'tau_06_nmin2_seed42', 'tau_05_nmin2_seed42', 'contamination_60_seed42_r2', 'contamination_60_grid_b0_5_seed42', 'contamination_60_uniform_seed42', 'bs8_nmin2_seed42_r2', 'grid_b_low_serial_seed42', 'grid_b_low_seed42_r3', 'grid_b_low_seed42_r2', 'baseline_qwen3_0.6b', 'contamination_60_seed42', 'nmin4_seed42', 'bs8_nmin2_seed42', 'bs8_seed42', 'tau_09_seed42', 'tau_07_seed42', 'tau_06_seed42', 'tau_05_seed42', 'adaptive_seed456', 'adaptive_seed123', 'adaptive_seed42', 'uniform_seed456', 'uniform_seed123', 'uniform_seed42', 'detector_modernbert', 'nmin1_seed42', 'golden_ratio_seed42', 'tau_0.6_seed42', 'grid_b_low_seed42', 'grid_b1_5_seed456', 'grid_b1_0_seed456', 'grid_b0_5_seed456', 'grid_b_seed42_batch', 'diagnostic_contamination100', 'detector_tfidf_lr']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "8a8e7165-51f9-4a0a-ae49-25f67e3b5909"
}
```

</details>

---


### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Examine baseline and experiment structure",
  "usage": {
    "total_tokens": 21059,
    "tool_uses": 4,
    "duration_ms": 24532
  },
  "last_tool_name": "Bash",
  "uuid": "92340f11-1ab0-4bb2-af67-922e47f69a4d",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01BTMQdruh48Vio1MADyzc27`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\n# Check baseline\nprint('Baseline:', json.dumps(result['data'].get('baseline'), indent=2)[:2000])\n# Check one experiment structure\nexps = result['data']['experiments']\nexp = exps['adaptive_seed42']\nprint('\\n--- adaptive_seed42 structure ---')\nprint(json.dumps(exp, indent=2)[:3000])\n\"",
  "description": "Examine baseline and experiment structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "c0cc32dc-3d26-47d2-9934-9035a349bf8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153gpWvLAAWvSAF3DsvxVGx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3589,
      "cache_read_input_tokens": 17344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3589,
        "ephemeral_1h_input_tokens": 0
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

_source line 35 · 2026-05-25T19:43:10.259Z_

<details><summary>↩ Tool result · `toolu_01BTMQdruh48Vio1MADyzc27`</summary>

```text
Baseline: null

--- adaptive_seed42 structure ---
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T02:25:01.824Z",
  "updated_at": "2026-05-15T16:43:05.333Z",
  "hypothesis": "Adaptive b* (from \u03b1_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42",
  "spec": {
    "command": "python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4",
    "server": "westd-47453",
    "gpu": [
      "cuda:1"
    ],
    "pid": "58888",
    "log_path": "~/runs/provenance_weight_training/adaptive_seed42.log",
    "submitted_at": "2026-05-14T02:46:23.000Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 42,
    "checkpoint_path": "output/models/adaptive_seed42/final",
    "wall_clock_seconds": 15162.9,
    "gpu_hours": 4.21
  },
  "metrics": {
    "train_loss": 9.2665,
    "train_runtime_s": 13115.09,
    "total_steps": 6103,
    "train_samples_per_second": 7.445,
    "train_steps_per_second": 0.465,
    "epoch": 0.26,
    "weighting_method": "adaptive",
    "tau": 0.8,
    "n_min": 3,
    "contamination_ratio": 0.4,
    "b_star": "per-batch adaptive (0.0-3.8)",
    "alpha_eff_range": "0.03-0.80 (capped at tau)",
    "eval_ppl_holdout": 17.644,
    "eval_loss_holdout": 2.8704,
    "eval_holdout_tokens": 4077068,
    "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)",
    "eval_note": "unified post-hoc eval 2026-05-15; confirmed unchanged from prior post-hoc (was 17.644/4077068)"
  },
  "conclusion": "success",
  "completed_at": "2026-05-14T06:59:05.861Z",
  "notes": "\u26a0\ufe0f success \u4ec5\u6307\u8bad\u7ec3\u5b8c\u6210\u65e0\u62a5\u9519\u3002MVP \u5047\u8bbe\u9a8c\u8bc1\u5f85 held-out eval perplexity \u7ed3\u679c\u3002"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "c149d36c-3330-4f4c-9e6c-0b72a01cc7cd"
}
```

</details>

---


### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Extract tau0.7 adaptive, uniform, and D&R q>0.7 experiments",
  "usage": {
    "total_tokens": 22327,
    "tool_uses": 5,
    "duration_ms": 39968
  },
  "last_tool_name": "Bash",
  "uuid": "3906fe54-1b98-4ed7-9c32-d98a7cb723f5",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01G4nDrYRXRBUhGu6zM2HJbR`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# 1. Find all tau07 adaptive experiments (5 seeds)\nprint(\"=== TAU 0.7 ADAPTIVE EXPERIMENTS ===\")\nfor eid, exp in sorted(exps.items()):\n    m = exp.get('metrics', {})\n    if 'tau07' in eid or 'tau_07' in eid or ('tau' in str(m) and m.get('tau') == 0.7):\n        ppl = m.get('eval_ppl_holdout')\n        tau = m.get('tau')\n        method = m.get('weighting_method')\n        seed = exp.get('spec', {}).get('seed') or m.get('seed')\n        print(f\"  {eid}: ppl={ppl}, tau={tau}, method={method}, seed={seed}, status={exp.get('status')}\")\n\nprint(\"\\n=== UNIFORM EXPERIMENTS ===\")\nfor eid, exp in sorted(exps.items()):\n    m = exp.get('metrics', {})\n    method = m.get('weighting_method')\n    if method == 'uniform' and 'contamination' not in eid and '1_7b' not in eid and 'epoch_matched' not in eid and 'ngram' not in eid:\n        ppl = m.get('eval_ppl_holdout')\n        seed = exp.get('spec', {}).get('seed') or m.get('seed')\n        rho = m.get('contamination_ratio')\n        print(f\"  {eid}: ppl={ppl}, method={method}, seed={seed}, rho={rho}, status={exp.get('status')}\")\n\nprint(\"\\n=== D&R q>0.7 EXPERIMENTS ===\")\nfor eid, exp in sorted(exps.items()):\n    if 'detect_remove_q07' in eid:\n        m = exp.get('metrics', {})\n        ppl = m.get('eval_ppl_holdout')\n        seed = exp.get('spec', {}).get('seed') or m.get('seed')\n        print(f\"  {eid}: ppl={ppl}, seed={seed}, status={exp.get('status')}\")\nPYEOF",
  "description": "Extract tau0.7 adaptive, uniform, and D&R q>0.7 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "114d9d8d-e972-424f-b85e-db4ad46065a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhpVsZpXQEnQQ6KpFPd9am",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 20933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1260,
        "ephemeral_1h_input_tokens": 0
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

_source line 38 · 2026-05-25T19:43:25.694Z_

<details><summary>↩ Tool result · `toolu_01G4nDrYRXRBUhGu6zM2HJbR`</summary>

```text
=== TAU 0.7 ADAPTIVE EXPERIMENTS ===
  adaptive_rho06_tau07_seed123: ppl=None, tau=None, method=None, seed=123, status=DONE
  adaptive_rho06_tau07_seed42: ppl=None, tau=None, method=None, seed=42, status=DONE
  adaptive_rho06_tau07_seed456: ppl=None, tau=None, method=None, seed=456, status=DONE
  bs16_adaptive_tau07_seed123: ppl=None, tau=None, method=None, seed=123, status=DONE
  bs16_adaptive_tau07_seed123_r2: ppl=None, tau=None, method=None, seed=123, status=DONE
  bs16_adaptive_tau07_seed42: ppl=None, tau=None, method=None, seed=None, status=DONE
  bs16_adaptive_tau07_seed456: ppl=None, tau=None, method=None, seed=456, status=DONE
  contamination_20_tau07_seed42: ppl=None, tau=None, method=None, seed=42, status=DONE
  contamination_60_tau07_seed42: ppl=17.73, tau=None, method=None, seed=42, status=DONE
  rho06_tau07_seed123: ppl=None, tau=None, method=None, seed=123, status=DONE
  rho06_tau07_seed42: ppl=17.526, tau=None, method=None, seed=42, status=DONE
  rho06_tau07_seed456: ppl=None, tau=None, method=None, seed=456, status=DONE
  tau07_downstream_eval: ppl=None, tau=None, method=None, seed=None, status=DONE
  tau07_seed123: ppl=17.666, tau=None, method=None, seed=123, status=DONE
  tau07_seed42: ppl=17.68, tau=None, method=None, seed=42, status=DONE
  tau07_seed456: ppl=17.677, tau=None, method=None, seed=456, status=DONE
  tau_07_nmin2_seed42: ppl=None, tau=None, method=None, seed=None, status=DONE
  tau_07_seed42: ppl=17.6793, tau=None, method=None, seed=42, status=DONE

=== UNIFORM EXPERIMENTS ===

=== D&R q>0.7 EXPERIMENTS ===
  detect_remove_q07_epoch_matched_seed42: ppl=17.62, seed=42, status=DONE
  detect_remove_q07_seed123: ppl=None, seed=123, status=DONE
  detect_remove_q07_seed42: ppl=17.32, seed=None, status=DONE
  detect_remove_q07_seed42_r2: ppl=None, seed=42, status=DONE
  detect_remove_q07_seed42_r3: ppl=None, seed=42, status=DONE
  detect_remove_q07_seed456: ppl=None, seed=456, status=DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "04e4fc35-1909-4a61-a6de-21ede6d07e03"
}
```

</details>

---


### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running List all uniform experiments",
  "usage": {
    "total_tokens": 23980,
    "tool_uses": 6,
    "duration_ms": 50709
  },
  "last_tool_name": "Bash",
  "uuid": "7da55cb0-beb5-4e60-a01c-80ad914c8cde",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01BYpEGkELKZkRvYkRLUMNFR`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get all uniform experiments\nprint(\"=== ALL UNIFORM EXPERIMENTS (by name) ===\")\nfor eid, exp in sorted(exps.items()):\n    if 'uniform' in eid.lower():\n        m = exp.get('metrics', {})\n        ppl = m.get('eval_ppl_holdout')\n        seed = exp.get('spec', {}).get('seed') or m.get('seed')\n        method = m.get('weighting_method')\n        rho = m.get('contamination_ratio')\n        print(f\"  {eid}: ppl={ppl}, method={method}, seed={seed}, rho={rho}, status={exp.get('status')}\")\nPYEOF",
  "description": "List all uniform experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "ef344b5e-b303-449a-a56a-67e737de53dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Es8Mr4k1pwTjP93SrBuzm6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1615,
      "cache_read_input_tokens": 22193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1615,
        "ephemeral_1h_input_tokens": 0
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

_source line 41 · 2026-05-25T19:43:36.424Z_

<details><summary>↩ Tool result · `toolu_01BYpEGkELKZkRvYkRLUMNFR`</summary>

```text
=== ALL UNIFORM EXPERIMENTS (by name) ===
  bs16_uniform_seed123: ppl=None, method=None, seed=123, rho=None, status=DONE
  bs16_uniform_seed42: ppl=None, method=None, seed=42, rho=None, status=DONE
  bs16_uniform_seed456: ppl=None, method=None, seed=456, rho=None, status=DONE
  bs8_nmin4_uniform_seed123: ppl=None, method=None, seed=None, rho=None, status=DONE
  bs8_nmin4_uniform_seed123_r2: ppl=17.687, method=None, seed=123, rho=None, status=DONE
  bs8_nmin4_uniform_seed42: ppl=None, method=None, seed=42, rho=None, status=DONE
  bs8_nmin4_uniform_seed456: ppl=None, method=None, seed=456, rho=None, status=DONE
  bs8_nmin4_uniform_seed456_r2: ppl=None, method=None, seed=456, rho=None, status=DONE
  contamination_60_uniform_seed123: ppl=17.754, method=None, seed=123, rho=None, status=DONE
  contamination_60_uniform_seed42: ppl=17.766, method=None, seed=None, rho=None, status=DONE
  contamination_60_uniform_seed456: ppl=17.77, method=None, seed=456, rho=None, status=DONE
  eval_ngram_uniform: ppl=None, method=None, seed=None, rho=None, status=DONE
  eval_uniform_1_7b_resumed: ppl=None, method=None, seed=None, rho=None, status=PREPARING
  eval_uniform_1_7b_seed123: ppl=None, method=None, seed=None, rho=None, status=PREPARING
  eval_uniform_1_7b_v2: ppl=None, method=None, seed=None, rho=None, status=PREPARING
  eval_uniform_1_7b_v3: ppl=13.5, method=None, seed=42, rho=None, status=DONE
  gpt2_uniform_seed42: ppl=17.69, method=None, seed=42, rho=None, status=DONE
  llama3b_uniform_seed42: ppl=None, method=None, seed=42, rho=None, status=DONE
  ngram_uniform_seed42: ppl=17.69, method=None, seed=None, rho=None, status=DONE
  qwen06b_uniform_seed42: ppl=17.69, method=None, seed=42, rho=None, status=DONE
  rho02_uniform_seed42: ppl=17.336, method=None, seed=None, rho=None, status=DONE
  rho03_uniform_seed123: ppl=17.433, method=None, seed=123, rho=None, status=DONE
  rho03_uniform_seed42: ppl=17.422, method=None, seed=42, rho=None, status=DONE
  rho03_uniform_seed456: ppl=17.419, method=None, seed=None, rho=None, status=DONE
  uniform_1_7b_seed123: ppl=13.2648, method=None, seed=123, rho=None, status=DONE
  uniform_1_7b_seed42: ppl=None, method=None, seed=None, rho=None, status=DONE
  uniform_1_7b_seed42_r2: ppl=None, method=None, seed=None, rho=None, status=PREPARING
  uniform_1_7b_seed42_v3: ppl=None, method=None, seed=None, rho=None, status=DONE
  uniform_1_7b_seed42_v4: ppl=None, method=None, seed=42, rho=None, status=DONE
  uniform_1_7b_seed42_v5: ppl=13.28, method=None, seed=42, rho=None, status=DONE
  uniform_1_7b_seed456: ppl=13.28, method=None, seed=456, rho=None, status=DONE
  uniform_epoch_matched_indep_lr_seed42: ppl=None, method=None, seed=None, rho=None, status=DONE
  uniform_epoch_matched_seed456: ppl=None, method=None, seed=456, rho=None, status=DONE
  uniform_ood_seed123: ppl=17.6861, method=None, seed=123, rho=None, status=DONE
  uniform_ood_seed456: ppl=17.7015, method=None, seed=456, rho=None, status=DONE
  uniform_seed123: ppl=17.6861, method=None, seed=123, rho=None, status=DONE
  uniform_seed234: ppl=None, method=None, seed=234, rho=None, status=DONE
  uniform_seed42: ppl=17.6939, method=None, seed=42, rho=None, status=DONE
  uniform_seed42_downstream: ppl=None, method=None, seed=42, rho=None, status=DONE
  uniform_seed456: ppl=17.7015, method=None, seed=456, rho=None, status=DONE
  uniform_seed789: ppl=None, method=None, seed=789, rho=None, status=DONE
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "50d9eb12-7164-4122-8812-83824fffbfef"
}
```

</details>

---


### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Extract adaptive tau0.7 and uniform seed experiments for mean calculation",
  "usage": {
    "total_tokens": 25857,
    "tool_uses": 7,
    "duration_ms": 65922
  },
  "last_tool_name": "Bash",
  "uuid": "2a41375e-4b2f-4d7a-87bc-fce15d291701",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01UG8xzzmtDbryJFCtc28Reu`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Get all adaptive experiments at rho=0.4 (default) with their PPLs\nprint(\"=== ADAPTIVE (default rho=0.4) EXPERIMENTS ===\")\nfor eid in ['adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456', 'adaptive_seed234', 'adaptive_seed789']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    print(f\"  {eid}: ppl={m.get('eval_ppl_holdout')}, tau={m.get('tau')}, rho={m.get('contamination_ratio')}, seed={exp.get('spec',{}).get('seed')}\")\n\nprint(\"\\n=== TAU 0.7 at rho=0.4 ===\")\nfor eid in ['tau07_seed42', 'tau07_seed123', 'tau07_seed456', 'tau_07_seed42']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    print(f\"  {eid}: ppl={m.get('eval_ppl_holdout')}, tau={m.get('tau')}, method={m.get('weighting_method')}\")\n\n# Uniform main 5 seeds\nprint(\"\\n=== UNIFORM MAIN 5 SEEDS ===\")\nfor eid in ['uniform_seed42', 'uniform_seed123', 'uniform_seed456', 'uniform_seed234', 'uniform_seed789']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    print(f\"  {eid}: ppl={m.get('eval_ppl_holdout')}, method={m.get('weighting_method')}\")\n\n# Check for aggregated/summary data\nprint(\"\\n=== LOOKING FOR SUMMARY/AGGREGATED RESULTS ===\")\nfor eid, exp in exps.items():\n    m = exp.get('metrics', {})\n    for k, v in m.items():\n        if 'mean' in str(k).lower() or 'std' in str(k).lower() or 'p_bh' in str(k).lower() or 'p_value' in str(k).lower():\n            print(f\"  {eid}.{k} = {v}\")\nPYEOF",
  "description": "Extract adaptive tau0.7 and uniform seed experiments for mean calculation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "0e50ee11-3903-4e89-b151-1e9498653091",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gi1Lhj42zpNjVzdxixC1RC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1839,
      "cache_read_input_tokens": 23808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1839,
        "ephemeral_1h_input_tokens": 0
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

_source line 44 · 2026-05-25T19:43:51.643Z_

<details><summary>↩ Tool result · `toolu_01UG8xzzmtDbryJFCtc28Reu`</summary>

```text
=== ADAPTIVE (default rho=0.4) EXPERIMENTS ===
  adaptive_seed42: ppl=17.644, tau=0.8, rho=0.4, seed=42
  adaptive_seed123: ppl=17.6308, tau=0.8, rho=0.4, seed=123
  adaptive_seed456: ppl=17.6419, tau=0.8, rho=0.4, seed=456
  adaptive_seed234: ppl=None, tau=None, rho=None, seed=234
  adaptive_seed789: ppl=None, tau=None, rho=None, seed=789

=== TAU 0.7 at rho=0.4 ===
  tau07_seed42: ppl=17.68, tau=None, method=None
  tau07_seed123: ppl=17.666, tau=None, method=None
  tau07_seed456: ppl=17.677, tau=None, method=None
  tau_07_seed42: ppl=17.6793, tau=None, method=None

=== UNIFORM MAIN 5 SEEDS ===
  uniform_seed42: ppl=17.6939, method=None
  uniform_seed123: ppl=17.6861, method=None
  uniform_seed456: ppl=17.7015, method=None
  uniform_seed234: ppl=None, method=None
  uniform_seed789: ppl=None, method=None

=== LOOKING FOR SUMMARY/AGGREGATED RESULTS ===
  ess_only_seed123.b_star_mean = 3.55
  ess_only_seed123.b_star_std = 4.7209
  adaptive_1_7b_seed456.downstream_mean = 0.6259
  uniform_1_7b_seed456.downstream_mean = 0.6234
  uniform_1_7b_seed123.downstream_mean = 0.6256
  adaptive_fix_seed456.b_star_mean = 1.416
  adaptive_fix_seed456.b_star_std = 1.993
  adaptive_fix_seed123.b_star_mean = 1.431
  adaptive_fix_seed123.b_star_std = 2.029
  uniform_1_7b_seed42_v5.downstream_mean = 0.6256
  adaptive_1_7b_seed42_v5.downstream_mean = 0.6251
  adaptive_1_7b_seed123.downstream_mean = 0.6286
  contamination_60_adaptive_seed123_tau08.downstream_mean = 0.5368
  contamination_60_adaptive_seed42_tau08.downstream_mean = 0.5398
  adaptive_fix_seed42.downstream_mean = 0.5403
  adaptive_rho06_tau07_seed123.downstream_mean = 0.5361
  adaptive_rho06_tau07_seed456.downstream_mean = 0.5375
  adaptive_rho06_tau07_seed42.downstream_mean = 0.5403
  rho02_adaptive_tau09_r5.b_star_mean = 4.3493
  rho02_adaptive_tau09_r5.b_star_std = 4.3982
  rho02_adaptive_tau09_r5.alpha_eff_mean = 0.8277
  rho02_adaptive_tau09_r5.ess_mean = 2.3784
  bs8_auto_nmin_r5.b_star_mean = 1.0957
  bs8_auto_nmin_r5.b_star_std = 0.7563
  bs8_auto_nmin_r5.ess_mean = 4.4925
  bs8_auto_nmin_r5.alpha_eff_mean = 0.7023
  tau_095_seed42.b_star_mean = 3.0775
  tau_095_seed42.b_star_std = 3.9923
  p0_contamination_60_datagen.q_score_mean = 0.6243
  p0_contamination_60_datagen.q_score_std = 0.3703
  ess_only_seed42.b_star_mean = 3.51
  nmin4_seed42.b_star_mean = 0
  nmin4_seed42.b_star_std = 0
  nmin4_seed42.ess_mean = 4
  tau_09_seed42.b_star_mean = 2.36
  tau_09_seed42.b_star_std = 3.04
  tau_07_seed42.b_star_mean = 0.8943
  tau_07_seed42.b_star_std = 1.4007
  tau_06_seed42.b_star_mean = 0.5899
  tau_06_seed42.b_star_std = 1.0693
  tau_06_seed42.b_star_nonzero_mean = 0.699
  tau_05_seed42.b_star_mean = 0.3923
  tau_05_seed42.b_star_std = 0.8821
  nmin1_seed42.b_star_mean = 7.197
  nmin1_seed42.b_star_std = 8.374
  nmin1_seed42.alpha_eff_mean = 0.714
  detector_tfidf_lr.q_score_mean = 0.6
  detector_tfidf_lr.q_score_std = 0.374
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "fdc352d3-c3a5-4695-8f7c-be24e39efe2d"
}
```

</details>

---


### System

_source line 45_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check seed234/789 and bs16_tau07 experiments",
  "usage": {
    "total_tokens": 28207,
    "tool_uses": 8,
    "duration_ms": 78332
  },
  "last_tool_name": "Bash",
  "uuid": "39cdfaa8-b4e0-4291-b5ab-5bd278a16d98",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01F3C3ncahNyDDDxM8FqfKhS`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Need to find the 5-seed tau=0.7 runs. Let me check uniform_seed234 and uniform_seed789 more carefully\nprint(\"=== uniform_seed234 full metrics ===\")\nprint(json.dumps(exps['uniform_seed234'].get('metrics', {}), indent=2))\nprint(\"\\n=== uniform_seed789 full metrics ===\")\nprint(json.dumps(exps['uniform_seed789'].get('metrics', {}), indent=2))\nprint(\"\\n=== adaptive_seed234 full metrics ===\")\nprint(json.dumps(exps['adaptive_seed234'].get('metrics', {}), indent=2))\nprint(\"\\n=== adaptive_seed789 full metrics ===\")\nprint(json.dumps(exps['adaptive_seed789'].get('metrics', {}), indent=2))\n\n# Check the bs16 tau07 experiments since they might be the actual tau=0.7 runs\nprint(\"\\n=== bs16_adaptive_tau07_seed42 full ===\")\nprint(json.dumps(exps['bs16_adaptive_tau07_seed42'].get('metrics', {}), indent=2))\nprint(\"\\n=== bs16_adaptive_tau07_seed123 full ===\")\nprint(json.dumps(exps['bs16_adaptive_tau07_seed123'].get('metrics', {}), indent=2))\nprint(\"\\n=== bs16_adaptive_tau07_seed123_r2 full ===\")\nprint(json.dumps(exps['bs16_adaptive_tau07_seed123_r2'].get('metrics', {}), indent=2))\nprint(\"\\n=== bs16_adaptive_tau07_seed456 full ===\")\nprint(json.dumps(exps['bs16_adaptive_tau07_seed456'].get('metrics', {}), indent=2))\nPYEOF",
  "description": "Check seed234/789 and bs16_tau07 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "ba76874f-a082-4901-925d-81dc8c28633e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYEZnRFkm2Erji3uNvjc87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2312,
      "cache_read_input_tokens": 25647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2312,
        "ephemeral_1h_input_tokens": 0
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

_source line 47 · 2026-05-25T19:44:04.054Z_

<details><summary>↩ Tool result · `toolu_01F3C3ncahNyDDDxM8FqfKhS`</summary>

```text
=== uniform_seed234 full metrics ===
{
  "holdout_ppl": 17.708,
  "holdout_loss": 2.874,
  "owt_ppl": 18.355,
  "wiki_ppl": 15.352,
  "train_loss": 8.008,
  "train_duration_s": 12780
}

=== uniform_seed789 full metrics ===
{
  "holdout_ppl": 17.695,
  "holdout_loss": 2.8733,
  "owt_ppl": 18.387,
  "wiki_ppl": 15.349,
  "train_loss": 7.959,
  "train_duration_s": 12790
}

=== adaptive_seed234 full metrics ===
{
  "holdout_ppl": 17.678,
  "owt_ppl": 18.34,
  "wiki_ppl": 15.341,
  "train_loss": 9.695,
  "train_duration_s": 13540
}

=== adaptive_seed789 full metrics ===
{
  "holdout_ppl": 17.668,
  "owt_ppl": 18.365,
  "wiki_ppl": 15.33,
  "train_loss": 9.65,
  "train_duration_s": 13570
}

=== bs16_adaptive_tau07_seed42 full ===
{
  "holdout_loss": 2.8697,
  "holdout_ppl": 17.631,
  "owt_loss": 2.9074,
  "owt_ppl": 18.309,
  "wiki_loss": 2.7269,
  "wiki_ppl": 15.286,
  "train_loss": 2.537
}

=== bs16_adaptive_tau07_seed123 full ===
{}

=== bs16_adaptive_tau07_seed123_r2 full ===
{
  "holdout_loss": 2.8688,
  "holdout_ppl": 17.616,
  "owt_loss": 2.9083,
  "owt_ppl": 18.325,
  "wiki_loss": 2.731,
  "wiki_ppl": 15.348
}

=== bs16_adaptive_tau07_seed456 full ===
{
  "holdout_loss": 2.8704,
  "holdout_ppl": 17.645,
  "owt_loss": 2.9076,
  "owt_ppl": 18.313,
  "wiki_loss": 2.7276,
  "wiki_ppl": 15.296,
  "total_steps": 6103,
  "train_loss": 2.528
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "800c1bbc-c027-4334-9410-c82a5b2b58b7"
}
```

</details>

---


### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check experiment specs and full details",
  "usage": {
    "total_tokens": 29627,
    "tool_uses": 9,
    "duration_ms": 93615
  },
  "last_tool_name": "Bash",
  "uuid": "603dfb5e-8eaf-47f8-bb41-e1bfb78b0b3b",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_015bbGnnDdhqUDfKiLuCscDK`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Paper says \"Adaptive tau=0.7 5-seed mean holdout PPL: 17.674\"\n# Let me figure out which 5 experiments. The tau07 experiments:\n# tau07_seed42 = 17.68, tau07_seed123 = 17.666, tau07_seed456 = 17.677\n# But those are only 3. Let me check bs16 variants:\n# bs16_adaptive_tau07_seed42 = 17.631, bs16_adaptive_tau07_seed123_r2 = 17.616, bs16_adaptive_tau07_seed456 = 17.645\n# Those are also 3. \n\n# Maybe the 5 seed tau=0.7 uses adaptive_seed* (which are tau=0.8) PLUS tau07_seed*?\n# Or maybe adaptive_seed234 and adaptive_seed789 are tau=0.7?\n\n# Check adaptive_seed234 and adaptive_seed789 specs\nprint(\"=== adaptive_seed234 spec ===\")\nspec = exps['adaptive_seed234'].get('spec', {})\ncmd = spec.get('command', '')\nprint(f\"  command: {cmd[:300]}\")\n\nprint(\"\\n=== adaptive_seed789 spec ===\")\nspec = exps['adaptive_seed789'].get('spec', {})\ncmd = spec.get('command', '')\nprint(f\"  command: {cmd[:300]}\")\n\nprint(\"\\n=== tau07_seed42 spec ===\")\nspec = exps['tau07_seed42'].get('spec', {})\ncmd = spec.get('command', '')\nprint(f\"  command: {cmd[:300]}\")\n\nprint(\"\\n=== tau07_seed123 full ===\")\nprint(json.dumps(exps['tau07_seed123'], indent=2)[:1500])\n\n# Calculate means\nprint(\"\\n=== CALCULATIONS ===\")\n\n# 5-seed tau=0.7: tau07_seed42, tau07_seed123, tau07_seed456 + adaptive_seed234 + adaptive_seed789\n# Wait, those adaptive seeds are tau=0.8 not 0.7. Let me check tau_07_seed42\nprint(\"\\n=== tau_07_seed42 full ===\")\nprint(json.dumps(exps['tau_07_seed42'], indent=2)[:1500])\nPYEOF",
  "description": "Check experiment specs and full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "224521bc-32f6-4234-b53e-5de70dc1c98f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TiYsnx4TqEHzFQsbaCd9MX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1382,
      "cache_read_input_tokens": 27959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1382,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-25T19:44:19.335Z_

<details><summary>↩ Tool result · `toolu_015bbGnnDdhqUDfKiLuCscDK`</summary>

```text
=== adaptive_seed234 spec ===
  command: python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_seed234 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 2 --num_train_tokens 200000000 --contamination_ratio 0.

=== adaptive_seed789 spec ===
  command: python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/adaptive_seed789 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --tau 0.7 --n_min 2 --num_train_tokens 200000000 --contamination_ratio 0.

=== tau07_seed42 spec ===
  command: WANDB_MODE=disabled python training/pretrain_weighted.py --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --seed 42

=== tau07_seed123 full ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T20:44:02.827Z",
  "updated_at": "2026-05-20T03:03:29.289Z",
  "hypothesis": "\u03c4=0.7 sensitivity test (seed=123, \u03c1=0.4). R3-N2 requires multi-seed \u03c4 sensitivity data. Currently have \u03c4=0.8 \u00d7 3 seeds. Adding \u03c4=0.7 \u00d7 2 seeds enables direct paired comparison: if \u03c4=0.7 degrades PPL vs \u03c4=0.8 at same seed, confirms \u03c4=0.8 is near-optimal. If equivalent, suggests robustness to \u03c4 choice.",
  "spec": {
    "command": "WANDB_MODE=disabled python training/pretrain_weighted.py --data_path /root/autodl-tmp/provenance_weight_training/data/scored_data.jsonl --output_dir output/models/tau07_seed123 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --tau 0.7 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 123 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --save_steps 6103",
    "server": "westd-41312",
    "gpu": [
      "cuda:1"
    ],
    "pid": "344455",
    "log_path": "~/runs/provenance_weight_training/tau07_seed123.log",
    "submitted_at": "2026-05-19T20:46:25.278Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 123,
    "tau": 0.7,
    "n_min": 2,
    "batch_size": 4,
    "gra

=== CALCULATIONS ===

=== tau_07_seed42 full ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T10:03:27.838Z",
  "updated_at": "2026-05-15T17:57:12.394Z",
  "hypothesis": "\u03c4 sensitivity sweep: \u03c4=0.7 (slightly below baseline), testing if moderate \u03c4 reduction improves or degrades PPL. Baseline \u03c4=0.8 PPL=17.65.",
  "parent": "adaptive_fix_seed42",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:0"
    ],
    "pid": "209824",
    "log_path": "~/runs/provenance_weight_training/tau_07_seed42.log",
    "submitted_at": "2026-05-15T13:35:52.041Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data.jsonl",
    "data_count": 200000000,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 42,
    "checkpoint_source": "N/A - training from scratch",
    "eval_data": "N/A - training experiment",
    "wall_clock_seconds": 15680.4,
    "gp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "bc9205c5-2fdb-46b1-9228-64537e367cff"
}
```

</details>

---


### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Calculate 5-seed means and check D&R experiments",
  "usage": {
    "total_tokens": 32036,
    "tool_uses": 10,
    "duration_ms": 112532
  },
  "last_tool_name": "Bash",
  "uuid": "4da28434-a871-42c6-b7f3-49c5c7771665",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01EtMqmT36AJPcQdMbPjCCAD`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# So adaptive_seed234 and adaptive_seed789 ARE tau=0.7 experiments (despite the name)\n# Let me find the 5 seeds for tau=0.7 adaptive at rho=0.4\n\n# Candidates: tau07_seed42 (17.68), tau07_seed123 (17.666), tau07_seed456 (17.677)\n# adaptive_seed234 (17.678, tau=0.7), adaptive_seed789 (17.668, tau=0.7)\n# tau_07_seed42 (17.6793) - might be same as tau07_seed42 or different run\n\n# Let's compute the 5-seed mean\nppls_tau07 = [17.68, 17.666, 17.677, 17.678, 17.668]\nmean_tau07 = sum(ppls_tau07) / len(ppls_tau07)\nprint(f\"tau=0.7 5-seed PPLs: {ppls_tau07}\")\nprint(f\"tau=0.7 5-seed mean: {mean_tau07:.3f}\")\n\n# Now uniform 5-seed\n# uniform_seed42=17.6939, uniform_seed123=17.6861, uniform_seed456=17.7015\n# uniform_seed234=17.708 (holdout_ppl), uniform_seed789=17.695 (holdout_ppl)\nppls_uniform = [17.6939, 17.6861, 17.7015, 17.708, 17.695]\nmean_uniform = sum(ppls_uniform) / len(ppls_uniform)\nprint(f\"\\nUniform 5-seed PPLs: {ppls_uniform}\")\nprint(f\"Uniform 5-seed mean: {mean_uniform:.3f}\")\n\n# Paper says adaptive tau=0.7 mean = 17.674, uniform mean = 17.694\n# Delta\ndelta = mean_tau07 - mean_uniform\nprint(f\"\\nDelta (adaptive - uniform): {delta:.3f}\")\nprint(f\"Paper says delta = -0.023 at rho=0.4\")\n\n# D&R q>0.7 3-seed mean\nprint(\"\\n=== D&R q>0.7 seeds ===\")\nfor eid in ['detect_remove_q07_seed42', 'detect_remove_q07_seed42_r2', 'detect_remove_q07_seed42_r3', \n            'detect_remove_q07_seed123', 'detect_remove_q07_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    print(f\"  {eid}: ppl={ppl}\")\nPYEOF",
  "description": "Calculate 5-seed means and check D&R experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "60a5bfd2-19d5-4594-ae57-b872e222757f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRtVcDGybzNLW29WdtZEkM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2373,
      "cache_read_input_tokens": 29341,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2373,
        "ephemeral_1h_input_tokens": 0
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

_source line 53 · 2026-05-25T19:44:38.242Z_

<details><summary>↩ Tool result · `toolu_01EtMqmT36AJPcQdMbPjCCAD`</summary>

```text
tau=0.7 5-seed PPLs: [17.68, 17.666, 17.677, 17.678, 17.668]
tau=0.7 5-seed mean: 17.674

Uniform 5-seed PPLs: [17.6939, 17.6861, 17.7015, 17.708, 17.695]
Uniform 5-seed mean: 17.697

Delta (adaptive - uniform): -0.023
Paper says delta = -0.023 at rho=0.4

=== D&R q>0.7 seeds ===
  detect_remove_q07_seed42: ppl=17.32
  detect_remove_q07_seed42_r2: ppl=None
  detect_remove_q07_seed42_r3: ppl=17.32
  detect_remove_q07_seed123: ppl=17.32
  detect_remove_q07_seed456: ppl=17.32
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "ad92c058-d152-4fc9-a454-7e81dd2218af"
}
```

</details>

---


### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check D&R detailed metrics and rho=0.6 experiments",
  "usage": {
    "total_tokens": 33251,
    "tool_uses": 11,
    "duration_ms": 127513
  },
  "last_tool_name": "Bash",
  "uuid": "10576bcb-932c-4c30-afc7-95e9e9fb337a",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Bash · `toolu_01MR7XtFGtgRBdZxs5Jq6ndt`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# D&R q>0.7 - check all metrics fields more carefully\nprint(\"=== D&R q>0.7 DETAILED ===\")\nfor eid in ['detect_remove_q07_seed42', 'detect_remove_q07_seed42_r2', 'detect_remove_q07_seed42_r3', \n            'detect_remove_q07_seed123', 'detect_remove_q07_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    print(f\"\\n  {eid}:\")\n    for k, v in m.items():\n        if 'ppl' in k.lower() or 'holdout' in k.lower():\n            print(f\"    {k} = {v}\")\n\n# Now check rho=0.6 experiments\nprint(\"\\n\\n=== RHO=0.6 EXPERIMENTS ===\")\nfor eid in ['rho06_tau07_seed42', 'rho06_tau07_seed123', 'rho06_tau07_seed456',\n            'adaptive_rho06_tau07_seed42', 'adaptive_rho06_tau07_seed123', 'adaptive_rho06_tau07_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    print(f\"  {eid}: ppl={ppl}\")\n\n# Check contamination_60 experiments for rho=0.6\nprint(\"\\n=== CONTAMINATION_60 EXPERIMENTS ===\")\nfor eid in sorted(exps.keys()):\n    if 'contamination_60' in eid:\n        exp = exps[eid]\n        m = exp.get('metrics', {})\n        ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n        method_hint = ''\n        cmd = exp.get('spec', {}).get('command', '')\n        if 'adaptive' in eid or 'adaptive' in cmd:\n            method_hint = '[adaptive]'\n        elif 'uniform' in eid or 'uniform' in cmd:\n            method_hint = '[uniform]'\n        print(f\"  {eid}: ppl={ppl} {method_hint}\")\nPYEOF",
  "description": "Check D&R detailed metrics and rho=0.6 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "0974c19c-e85e-41ec-b86c-49024a2298fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TUeWQ4SZm1YguwomXsGgi4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 31714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1177,
        "ephemeral_1h_input_tokens": 0
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

_source line 56 · 2026-05-25T19:44:53.256Z_

<details><summary>↩ Tool result · `toolu_01MR7XtFGtgRBdZxs5Jq6ndt`</summary>

```text
=== D&R q>0.7 DETAILED ===

  detect_remove_q07_seed42:
    eval_ppl_holdout = 17.32
    eval_loss_holdout = 2.8519
    eval_holdout_tokens = 4077068

  detect_remove_q07_seed42_r2:

  detect_remove_q07_seed42_r3:
    holdout_ppl = 17.32
    owt_ppl = 18.04
    wiki_ppl = 15.11

  detect_remove_q07_seed123:
    holdout_ppl = 17.32
    owt_ppl = 18.04
    wiki_ppl = 15.1

  detect_remove_q07_seed456:
    holdout_ppl = 17.32
    owt_ppl = 18.03
    wiki_ppl = 15.11


=== RHO=0.6 EXPERIMENTS ===
  rho06_tau07_seed42: ppl=17.526
  rho06_tau07_seed123: ppl=None
  rho06_tau07_seed456: ppl=None
  adaptive_rho06_tau07_seed42: ppl=17.735
  adaptive_rho06_tau07_seed123: ppl=17.727
  adaptive_rho06_tau07_seed456: ppl=17.732

=== CONTAMINATION_60 EXPERIMENTS ===
  contamination_60_adaptive_seed123_tau08: ppl=17.73 [adaptive]
  contamination_60_adaptive_seed42_tau08: ppl=17.74 [adaptive]
  contamination_60_adaptive_seed456: ppl=17.735 [adaptive]
  contamination_60_ess_only_seed123: ppl=17.763 
  contamination_60_ess_only_seed42: ppl=17.77 
  contamination_60_ess_only_seed456: ppl=17.762 
  contamination_60_grid_b0_3_seed42: ppl=17.634 
  contamination_60_grid_b0_5_seed42: ppl=None 
  contamination_60_random_seed123: ppl=17.87 
  contamination_60_random_seed42: ppl=17.832 
  contamination_60_random_seed456: ppl=17.88 
  contamination_60_seed123: ppl=17.732 [adaptive]
  contamination_60_seed42: ppl=None 
  contamination_60_seed42_r2: ppl=17.74 [adaptive]
  contamination_60_tau06_seed42: ppl=17.7359 [adaptive]
  contamination_60_tau07_seed42: ppl=17.73 [adaptive]
  contamination_60_uniform_seed123: ppl=17.754 [uniform]
  contamination_60_uniform_seed42: ppl=17.766 [uniform]
  contamination_60_uniform_seed456: ppl=17.77 [uniform]
  p0_contamination_60_datagen: ppl=None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "d7d61993-9f62-45ab-b7d8-7ad3df75124e"
}
```

</details>

---


### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Calculate rho=0.6 delta and check epoch-matched experiments",
  "usage": {
    "total_tokens": 34916,
    "tool_uses": 12,
    "duration_ms": 140440
  },
  "last_tool_name": "Bash",
  "uuid": "23cbd729-bd04-4976-a679-6d629b1d5f21",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01Hc86sU6DucYbkmhbpBuy2c`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# rho=0.6 adaptive: adaptive_rho06_tau07_seed42/123/456 = 17.735, 17.727, 17.732\n# rho=0.6 uniform: contamination_60_uniform_seed42/123/456 = 17.766, 17.754, 17.77\n\nrho06_adap = [17.735, 17.727, 17.732]\nrho06_unif = [17.766, 17.754, 17.770]\nmean_rho06_adap = sum(rho06_adap) / 3\nmean_rho06_unif = sum(rho06_unif) / 3\ndelta_rho06 = mean_rho06_adap - mean_rho06_unif\nprint(f\"rho=0.6 adaptive mean: {mean_rho06_adap:.3f}\")\nprint(f\"rho=0.6 uniform mean: {mean_rho06_unif:.3f}\")\nprint(f\"rho=0.6 delta: {delta_rho06:.3f}\")\nprint(f\"Paper says delta = -0.032 at rho=0.6\")\n\n# D&R q>0.7 3-seed mean\ndr_ppls = [17.32, 17.32, 17.32]\ndr_mean = sum(dr_ppls) / 3\nprint(f\"\\nD&R q>0.7 3-seed PPLs: {dr_ppls}\")\nprint(f\"D&R q>0.7 3-seed mean: {dr_mean:.3f}\")\n\n# Check epoch-matched experiments\nprint(\"\\n=== EPOCH-MATCHED EXPERIMENTS ===\")\nfor eid in sorted(exps.keys()):\n    if 'epoch_matched' in eid:\n        exp = exps[eid]\n        m = exp.get('metrics', {})\n        ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n        print(f\"  {eid}: ppl={ppl}\")\nPYEOF",
  "description": "Calculate rho=0.6 delta and check epoch-matched experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "fb3fbeb5-0803-4116-ab75-e76851e620a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9JFz5NJFMD4YQQMMiVxkF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1627,
      "cache_read_input_tokens": 32891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1627,
        "ephemeral_1h_input_tokens": 0
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

_source line 59 · 2026-05-25T19:45:06.163Z_

<details><summary>↩ Tool result · `toolu_01Hc86sU6DucYbkmhbpBuy2c`</summary>

```text
rho=0.6 adaptive mean: 17.731
rho=0.6 uniform mean: 17.763
rho=0.6 delta: -0.032
Paper says delta = -0.032 at rho=0.6

D&R q>0.7 3-seed PPLs: [17.32, 17.32, 17.32]
D&R q>0.7 3-seed mean: 17.320

=== EPOCH-MATCHED EXPERIMENTS ===
  detect_remove_q01_epoch_matched_seed42: ppl=18.0436
  detect_remove_q03_epoch_matched_seed42: ppl=17.74
  detect_remove_q05_epoch_matched: ppl=None
  detect_remove_q05_epoch_matched_seed42: ppl=17.65
  detect_remove_q07_epoch_matched_seed42: ppl=17.62
  detect_remove_q09_epoch_matched_seed42: ppl=17.628
  dr_epoch_matched_indep_lr_seed42: ppl=18.78174
  dr_epoch_matched_indep_lr_v2_seed42: ppl=17.65053
  dr_epoch_matched_seed123: ppl=18.332
  dr_epoch_matched_seed123_r2: ppl=17.6591
  dr_epoch_matched_seed456: ppl=17.66
  epoch_matched_dr_seed123: ppl=17.66
  epoch_matched_dr_seed456: ppl=17.66
  eval_epoch_matched_seed123: ppl=None
  eval_epoch_matched_seed456: ppl=None
  uniform_epoch_matched_indep_lr_seed42: ppl=18.06206
  uniform_epoch_matched_seed456: ppl=18.068
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "439f7cd7-fbdf-462b-9e3f-a36985b4f887"
}
```

</details>

---


### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Search for PPL values near 17.250 and check D&R variants",
  "usage": {
    "total_tokens": 36173,
    "tool_uses": 13,
    "duration_ms": 159748
  },
  "last_tool_name": "Bash",
  "uuid": "054e3847-3459-4c63-900d-9b32cc3729d8",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Bash · `toolu_01Uutc5kk3nmGpTvnW7oZ2MF`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Paper says \"D&R PPL 17.250 vs. 17.674, 3 seeds\" but registry shows 17.32\n# Let me check if there's a different D&R run\n# Wait - D&R q>0.7 shows 17.32 everywhere. Paper says 17.250. Let me check the D&R q>0.5 variants too\nprint(\"=== D&R q>0.5 v2 ===\")\nfor eid in ['detect_remove_q05_v2_seed42', 'detect_remove_q05_v2_seed123', 'detect_remove_q05_v2_seed456',\n            'detect_remove_q05_v2_seed123_r2']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    print(f\"  {eid}: ppl={ppl}\")\n\nprint(\"\\n=== ALL detect_remove experiments ===\")\nfor eid in sorted(exps.keys()):\n    if eid.startswith('detect_remove'):\n        exp = exps[eid]\n        m = exp.get('metrics', {})\n        ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n        if ppl and not 'epoch_matched' in eid:\n            print(f\"  {eid}: ppl={ppl}\")\n\n# Check epoch-matched gap\n# D&R q>0.7 epoch-matched: detect_remove_q07_epoch_matched_seed42 = 17.62\n# Adaptive tau=0.7: let me find the right comparison\n# epoch_matched_dr_seed123 = 17.66, epoch_matched_dr_seed456 = 17.66\n# dr_epoch_matched_seed123_r2 = 17.6591\n\n# For the epoch-matched gap: paper says Delta=0.017\n# Probably: D&R epoch-matched PPL - adaptive PPL = gap\n# detect_remove_q07_epoch_matched_seed42 = 17.62, adaptive tau=0.7 = 17.674\n# But 17.62 < 17.674, so gap would be negative...\n# Maybe it's the other way: adaptive tau=0.7 vs D&R epoch-matched\n# Or maybe comparing different sets\n\n# Let me look for the specific epoch-matched gap calculation\n# Paper says \"reducing the gap to Δ=0.017\"\n# Original gap: D&R 17.250 vs adaptive 17.674 = gap of 0.424\n# Epoch-matched reduces to 0.017\n\n# Check all D&R experiments for PPL near 17.25\nprint(\"\\n=== Looking for PPL near 17.25 ===\")\nfor eid, exp in sorted(exps.items()):\n    m = exp.get('metrics', {})\n    for k, v in m.items():\n        if isinstance(v, (int, float)) and 17.2 <= v <= 17.3 and 'ppl' in k.lower():\n            print(f\"  {eid}.{k} = {v}\")\nPYEOF",
  "description": "Search for PPL values near 17.250 and check D&R variants"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "4928f81d-b11d-424c-bc93-54e656c58a12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BcZhCeYc29cLpsBgMxD8E5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 34518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1218,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 62 · 2026-05-25T19:45:25.463Z_

<details><summary>↩ Tool result · `toolu_01Uutc5kk3nmGpTvnW7oZ2MF`</summary>

```text
=== D&R q>0.5 v2 ===
  detect_remove_q05_v2_seed42: ppl=17.2853
  detect_remove_q05_v2_seed123: ppl=17.3656
  detect_remove_q05_v2_seed456: ppl=17.277
  detect_remove_q05_v2_seed123_r2: ppl=17.272

=== ALL detect_remove experiments ===
  detect_remove_baseline_seed42: ppl=17.29
  detect_remove_q01_seed42: ppl=17.4
  detect_remove_q02_seed42: ppl=17.27
  detect_remove_q03_seed123: ppl=17.25
  detect_remove_q03_seed42_r2: ppl=17.25
  detect_remove_q03_seed456: ppl=17.2509
  detect_remove_q04_seed42: ppl=17.26
  detect_remove_q05_seed123: ppl=17.27
  detect_remove_q05_seed42: ppl=17.291
  detect_remove_q05_seed456: ppl=17.28
  detect_remove_q05_v2_seed123: ppl=17.3656
  detect_remove_q05_v2_seed123_r2: ppl=17.272
  detect_remove_q05_v2_seed42: ppl=17.2853
  detect_remove_q05_v2_seed456: ppl=17.277
  detect_remove_q06_seed42: ppl=17.3
  detect_remove_q07_seed123: ppl=17.32
  detect_remove_q07_seed42: ppl=17.32
  detect_remove_q07_seed42_r3: ppl=17.32
  detect_remove_q07_seed456: ppl=17.32
  detect_remove_q08_seed42: ppl=17.3442
  detect_remove_q09_seed42: ppl=17.42

=== Looking for PPL near 17.25 ===
  detect_remove_baseline_seed42.eval_ppl_holdout = 17.29
  detect_remove_q02_seed42.eval_ppl_holdout = 17.27
  detect_remove_q03_seed123.eval_ppl_holdout = 17.25
  detect_remove_q03_seed42_r2.eval_ppl_holdout = 17.25
  detect_remove_q03_seed456.eval_ppl_holdout = 17.2509
  detect_remove_q04_seed42.eval_ppl_holdout = 17.26
  detect_remove_q05_seed123.eval_ppl_holdout = 17.27
  detect_remove_q05_seed42.holdout_ppl = 17.291
  detect_remove_q05_seed456.eval_ppl_holdout = 17.28
  detect_remove_q05_v2_seed123_r2.holdout_ppl = 17.272
  detect_remove_q05_v2_seed42.holdout_ppl = 17.2853
  detect_remove_q05_v2_seed456.holdout_ppl = 17.277
  detect_remove_q06_seed42.eval_ppl_holdout = 17.3
  eval_dr_q05_ckpt5500.holdout_ppl = 17.29
  threshold_q03_seed42.eval_ppl_holdout = 17.253
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "e3bf6983-176b-4129-a353-a3e326d80a86"
}
```

</details>

---


### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check D&R q>0.3 vs q>0.7, detector experiments",
  "usage": {
    "total_tokens": 38147,
    "tool_uses": 14,
    "duration_ms": 179068
  },
  "last_tool_name": "Bash",
  "uuid": "9ca9dff7-dd48-474f-a1c7-e0ea85acbe57",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_014KtC7NrKciWmd2gf3L6eKS`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Paper says \"D&R q>0.7 PPL 17.250\" but registry shows D&R q>0.7 = 17.32 (3 seeds)\n# The PPL of 17.250 matches D&R q>0.3 (17.25, 17.25, 17.2509) \n# This seems like a MISMATCH - paper might have wrong threshold or wrong PPL\n\n# Let me check D&R q>0.3 3-seed mean\ndr_q03 = [17.25, 17.25, 17.2509]\nprint(f\"D&R q>0.3 3-seed mean: {sum(dr_q03)/3:.3f}\")\n\n# D&R q>0.7 3-seed mean\ndr_q07 = [17.32, 17.32, 17.32]\nprint(f\"D&R q>0.7 3-seed mean: {sum(dr_q07)/3:.3f}\")\n\n# Actually, paper says \"D&R q>0.7\" with PPL 17.250\n# But registry D&R q>0.7 = 17.32. The 17.250 matches q>0.3.\n# This is a discrepancy!\n\n# Let me also verify: the detect_remove_q03_seed42_r2 is seed42 variant\nprint(\"\\n=== D&R q>0.3 details ===\")\nfor eid in ['detect_remove_q03_seed42', 'detect_remove_q03_seed42_r2', 'detect_remove_q03_seed123', 'detect_remove_q03_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    data_retained = m.get('data_retained') or m.get('samples_retained') or m.get('data_count')\n    print(f\"  {eid}: ppl={ppl}, data_info={data_retained}\")\n    # Also check hypothesis for q threshold info\n    hyp = exp.get('hypothesis', '')\n    print(f\"    hypothesis: {hyp[:200]}\")\n\n# Check detector experiment\nprint(\"\\n=== DETECTOR EXPERIMENTS ===\")\nfor eid in ['detector_modernbert', 'detector_tfidf_lr']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    print(f\"\\n  {eid} metrics:\")\n    for k, v in m.items():\n        print(f\"    {k} = {v}\")\nPYEOF",
  "description": "Check D&R q>0.3 vs q>0.7, detector experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "0148ee33-8a36-45d4-8e03-a71dc80c3a25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbuGj5KuC1noMtfcJTY3HY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1936,
      "cache_read_input_tokens": 35736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1936,
        "ephemeral_1h_input_tokens": 0
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

_source line 65 · 2026-05-25T19:45:44.811Z_

<details><summary>↩ Tool result · `toolu_014KtC7NrKciWmd2gf3L6eKS`</summary>

```text
D&R q>0.3 3-seed mean: 17.250
D&R q>0.7 3-seed mean: 17.320

=== D&R q>0.3 details ===
  detect_remove_q03_seed42: ppl=None, data_info=None
    hypothesis: Hard filtering (detect-and-remove) at q_score > 0.3 threshold retains ~70% of data by removing only high-confidence contaminated samples. Expected to outperform q>0.5 filtering (which is more aggressi
  detect_remove_q03_seed42_r2: ppl=17.25, data_info=None
    hypothesis: D&R threshold t=0.3: keep q≤0.3 (116,935 samples, 31.5%). Second most aggressive filtering level. Part of 9-point D&R sensitivity curve (q01-q09). Previous attempt failed (python: command not found). 
  detect_remove_q03_seed123: ppl=17.25, data_info=None
    hypothesis: Cross-seed replication of D&R q03 sweet spot: if seed123 reproduces seed42's PPL=17.25 (the U-curve optimum), q03 is a robust threshold, not a seed42 artifact. Two seeds converging validates the U-sha
  detect_remove_q03_seed456: ppl=17.2509, data_info=None
    hypothesis: D&R threshold t=0.3 seed456: cross-seed replication of q03 sweet spot (PPL=17.25 at seed42). Third seed for 3-seed mean and variance estimate at the D&R optimal threshold.

=== DETECTOR EXPERIMENTS ===

  detector_modernbert metrics:

  detector_tfidf_lr metrics:
    auc = 0.939
    accuracy = 0.858
    ece_raw = 0.24
    ece_calibrated = 0.048
    temperature_T = 0.204
    q_score_mean = 0.6
    q_score_std = 0.374
    q_score_median = 0.707
    mid_range_ratio = 0.463
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "efe1dad6-16b9-497b-9370-d1acfc3125af"
}
```

</details>

---


### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check detector_modernbert, data counts, pearson correlation, alpha_eff, p-values",
  "usage": {
    "total_tokens": 39619,
    "tool_uses": 15,
    "duration_ms": 194256
  },
  "last_tool_name": "Bash",
  "uuid": "0b843ac3-cd1a-4f17-b6bd-b27eee5cdacc",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01SANYZgjsY3HveZUvvvu1N7`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# detector_modernbert has no metrics in the main metrics field. Let me check its full structure\nprint(\"=== detector_modernbert full ===\")\nprint(json.dumps(exps['detector_modernbert'], indent=2)[:3000])\n\n# Check spec.data_count for 371,499\nprint(\"\\n\\n=== DATA COUNTS ===\")\nfor eid in ['uniform_seed42', 'adaptive_seed42', 'tau07_seed42']:\n    exp = exps.get(eid, {})\n    dc = exp.get('spec', {}).get('data_count')\n    print(f\"  {eid}: data_count={dc}\")\n\n# Check for Pearson r ~ 0.79\nprint(\"\\n=== SEARCH FOR PEARSON CORRELATION ===\")\nfor eid, exp in exps.items():\n    m = exp.get('metrics', {})\n    for k, v in m.items():\n        if 'pearson' in str(k).lower() or 'correlation' in str(k).lower() or 'r_value' in str(k).lower():\n            print(f\"  {eid}.{k} = {v}\")\n\n# Search for alpha_eff\nprint(\"\\n=== ALPHA_EFF RELATED ===\")\nfor eid, exp in exps.items():\n    m = exp.get('metrics', {})\n    for k, v in m.items():\n        if 'alpha_eff' in str(k).lower():\n            print(f\"  {eid}.{k} = {v}\")\n\n# Search for p-values\nprint(\"\\n=== P-VALUES ===\")\nfor eid, exp in exps.items():\n    m = exp.get('metrics', {})\n    notes = exp.get('notes', '')\n    conclusion = exp.get('conclusion', '')\n    for k, v in m.items():\n        if 'p_' in str(k).lower() or 'pvalue' in str(k).lower() or 'p_bh' in str(k).lower():\n            print(f\"  {eid}.{k} = {v}\")\n    # Also search notes/conclusion for p-values\n    if 'p_bh' in str(notes).lower() or 'p_bh' in str(conclusion).lower() or 'p=' in str(notes).lower():\n        print(f\"  {eid} notes contains p-value: {notes[:300]}\")\nPYEOF",
  "description": "Check detector_modernbert, data counts, pearson correlation, alpha_eff, p-values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "f1f74aaa-0e5e-49f3-8694-92fd03a5ce17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrCQTmPaBVbVLFHtZjrKeA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 37672,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1434,
        "ephemeral_1h_input_tokens": 0
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

_source line 68 · 2026-05-25T19:45:59.970Z_

<details><summary>↩ Tool result · `toolu_01SANYZgjsY3HveZUvvvu1N7`</summary>

```text
=== detector_modernbert full ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T22:40:06.106Z",
  "updated_at": "2026-05-15T15:51:50.219Z",
  "conclusion": "killed",
  "hypothesis": "ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human text with AUC>=0.95 and ECE<=0.05",
  "notes": "Superseded by TF-IDF detector (detector_tfidf_lr). Never ran \u2014 cancelled at QUEUED stage.",
  "completed_at": "2026-05-15T15:51:50.219Z"
}


=== DATA COUNTS ===
  uniform_seed42: data_count=371499
  adaptive_seed42: data_count=371499
  tau07_seed42: data_count=371499

=== SEARCH FOR PEARSON CORRELATION ===

=== ALPHA_EFF RELATED ===
  rho02_adaptive_tau09_r5.alpha_eff_mean = 0.8277
  rho02_adaptive_tau09_r5.alpha_eff_median = 0.8826
  rho02_adaptive_tau09_r5.alpha_eff_pct_at_max = 42.95
  bs8_auto_nmin_r5.alpha_eff_mean = 0.7023
  bs8_auto_nmin_r5.alpha_eff_median = 0.7572
  bs8_auto_nmin_r5.alpha_eff_pct_at_max = 38.88
  grid_b0_3_seed42.alpha_eff_typical_range = 0.07-0.88
  adaptive_seed456.alpha_eff_range = 0.09-0.80 (capped at tau)
  adaptive_seed123.alpha_eff_range = 0.04-0.80 (capped at tau)
  adaptive_seed42.alpha_eff_range = 0.03-0.80 (capped at tau)
  nmin1_seed42.alpha_eff_mean = 0.714
  nmin1_seed42.alpha_eff_median = 0.8

=== P-VALUES ===
  contamination_60_ess_only_seed42 notes contains p-value: ρ=0.6 ESS-only PPL=17.77 ≈ uniform (17.766), max-intervention 在高 contamination 下完全失效。vs ρ=0.4 ESS-only avg 17.723 → ρ增加0.2导致+0.047退化。关键对比: dual(17.74) < ESS-only(17.77), Claim 1 在 ρ=0.6 下仍成立(gap=0.03, 小于 ρ=0.4 的 gap=0.07)。ESS-only 崩溃而 dual 仍有效 → 强化 "dual-constraint 在高 contamination 下更重要" 叙事。⚠️ 服务器 w
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "2b032056-fa8d-49b0-aa2d-23e0c23ba95f"
}
```

</details>

---


### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Search all experiment fields for specific values",
  "usage": {
    "total_tokens": 41318,
    "tool_uses": 16,
    "duration_ms": 206577
  },
  "last_tool_name": "Bash",
  "uuid": "1b0a208f-7a91-4ecf-b228-2c9d786f3381",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_013vtNehw73FLn1FQC3DQuPS`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Search ALL fields of ALL experiments for p_bh, p_value, SD, pearson, 0.79, 0.011, 0.064\nimport re\n\ntargets = ['p_bh', 'p_value', 'pearson', '0.79', '0.011', '0.064', '0.006', 'sd ', 'standard_dev', \n           'constraint_bind', '50%', '5.9', 'sharpening', '132M', '132000000', 'golden_ratio', '0.62']\n\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp).lower()\n    for target in targets:\n        if target.lower() in full_str:\n            # Find context\n            idx = full_str.lower().find(target.lower())\n            context = full_str[max(0, idx-50):idx+50]\n            print(f\"  [{eid}] found '{target}': ...{context}...\")\nPYEOF",
  "description": "Search all experiment fields for specific values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "0cc027b3-fc65-4b87-bb73-6cd9e134bdf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHefBJq7bKrJLhLkCKtb1A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1661,
      "cache_read_input_tokens": 39106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1661,
        "ephemeral_1h_input_tokens": 0
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

_source line 71 · 2026-05-25T19:46:12.299Z_

<details><summary>↩ Tool result · `toolu_013vtNehw73FLn1FQC3DQuPS`</summary>

```text
  [detect_remove_q07_seed456] found '50%': ..."d&r q>0.7 threshold seed=456 replicate. retains ~50% data (184,908/370k). cross-seed for error bar ...
  [detect_remove_q07_seed123] found '50%': ..."d&r q>0.7 threshold seed=123 replicate. retains ~50% data (184,908/370k). cross-seed for error bar ...
  [detect_remove_q07_seed42_r3] found '50%': ...: "d&r q>0.7 threshold fresh rerun (r3). retains ~50% data (184,908/370k). prior r2 corrupted by opt...
  [detect_remove_q07_seed42_r2] found '50%': ...ard filtering at q_score > 0.7 threshold retains ~50% of data (184,908/370k samples), the most conse...
  [rho03_adaptive_seed456_r2] found '5.9': ..."save_total_limit": 2}, "wall_clock_seconds": 19665.9, "gpu_hours": 5.46}, "hypothesis": "third seed...
  [detect_remove_q05_v2_seed123_r2] found '5.9': ...retry_count": 0, "created_at": "2026-05-21t23:57:35.984z", "updated_at": "2026-05-22t09:08:04.733z",...
  [dr_epoch_matched_indep_lr_seed42] found '5.9': ....23533, "ood_owt_loss": 2.95675, "ood_wiki_ppl": 15.95958, "ood_wiki_loss": 2.77006, "train_loss_fin...
  [grid_b0_1_seed42] found '5.9': ...1_seed42.log", "submitted_at": "2026-05-17t17:20:25.910z", "submitted_via": "submit_training_job", "...
  [rho02_adaptive_tau08_seed42] found '50%': ...", "tau": 0.8, "rho": 0.2, "b_star_pct_zero": "40-50%", "conclusion_note": "worse than same-rho unif...
  [ngram_adaptive_seed456] found '0.62': ...retry_count": 0, "created_at": "2026-05-21t04:13:00.621z", "updated_at": "2026-05-21t04:59:09.364z",...
  [gpt2_adaptive_seed123_v2] found '5.9': ...retry_count": 0, "created_at": "2026-05-21t03:54:05.914z", "updated_at": "2026-05-21t04:59:07.344z",...
  [adaptive_1_7b_seed456] found '5.9': ...in)", "wall_clock_seconds": 21302.6, "gpu_hours": 5.92}, "reproduce": {"finished_at": "2026-05-20t21...
  [adaptive_1_7b_seed456] found '0.62': ...a_acc_norm": 0.7443, "downstream_winogrande_acc": 0.6219, "downstream_mean": 0.6259, "ood_eval_sourc...
  [uniform_1_7b_seed456] found '5.9': ..., "reproduce": {"finished_at": "2026-05-20t20:54:45.983z"}, "extra": {"hook_events": [{"event": "on_...
  [uniform_1_7b_seed456] found '0.62': ...a_acc_norm": 0.7448, "downstream_winogrande_acc": 0.6251, "downstream_mean": 0.6234}, "conclusion": ...
  [adaptive_ood_seed456] found '5.9': ..._seed456.log", "submitted_at": "2026-05-19t14:37:05.986z", "submitted_via": "submit_training_job", "...
  [uniform_1_7b_seed123] found '0.62': ...tream_winogrande_acc": 0.6133, "downstream_mean": 0.6256}, "conclusion": "success", "completed_at": ...
  [uniform_1_7b_seed42_v5] found '0.62': ...tream_winogrande_acc": 0.6172, "downstream_mean": 0.6256, "ood_eval_source": "eval_results/ pipeline...
  [adaptive_1_7b_seed42_v5] found '0.62': ...tream_winogrande_acc": 0.6069, "downstream_mean": 0.6251, "ood_eval_source": "eval_results/ pipeline...
  [adaptive_1_7b_seed123] found '0.62': ...a_acc_norm": 0.7459, "downstream_winogrande_acc": 0.6298, "downstream_mean": 0.6286}, "conclusion": ...
  [adaptive_fix_seed42] found '5.9': ...ete", "action": "agent", "ts": "2026-05-14t20:39:45.953045+00:00"}]}, "spec": {"command": "bash -c \...
  [adaptive_rho06_tau07_seed456] found '5.9': ...n": "success", "completed_at": "2026-05-20t08:13:45.922z", "metrics": {"holdout_ppl": 17.732, "eval_...
  [eval_ngram_adaptive] found '0.62': ...adaptive.log", "submitted_at": "2026-05-18t19:15:50.620z", "submitted_via": "submit_training_job", "...
  [hybrid_rho06_seed42] found '0.62': ...kipedia": 15.267, "downstream_arc_easy_acc_norm": 0.6208, "downstream_arc_challenge_acc_norm": 0.352...
  [rho06_tau07_seed42] found '0.62': ...kipedia": 15.267, "downstream_arc_easy_acc_norm": 0.6208, "downstream_arc_challenge_acc_norm": 0.352...
  [uniform_ood_seed123] found '0.62': ...ipedia": 15.3768, "downstream_arc_easy_acc_norm": 0.6229, "downstream_arc_challenge_acc_norm": 0.350...
  [detect_remove_q09_epoch_matched_seed42] found '5.9': ...ete", "action": "agent", "ts": "2026-05-19t02:42:55.919377+00:00"}]}, "metrics": {"eval_ppl_holdout"...
  [ess_only_seed456_r2] found '5.9': ...ens": 4077068, "total_steps": 6103, "train_loss": 5.998, "train_runtime_seconds": 7611}}...
  [batch_adaptive_tau_rho06_r2] found '5.9': ...6_seed42.sh\"", "finished_at": "2026-05-17t11:16:15.950z"}, "failure_reason": "traceback \u2192 , in...
  [p0_contamination_60_datagen] found '0.62': ...actual_contamination_ratio": 0.6, "q_score_mean": 0.6243, "q_score_std": 0.3703, "q_score_median": 0...
  [datagen_synthetic_4gpu] found '132M': ...ynthetic/shard_{0,1,2,3}/", "data_count": "target 132m tokens across 4 shards", "model_name": "qwen/...
  [grid_b5_0_seed456] found '5.9': ...ete", "action": "agent", "ts": "2026-05-15t09:31:35.946616+00:00"}], "previous_failure": {"conclusio...
  [grid_b2_0_seed456] found '0.62': ...8, "eval_holdout_tokens": 4077068, "train_loss": 10.625, "total_steps": 6103, "train_runtime_s": 129...
  [contamination_60_seed42] found '0.62': ...uman=148599, actual \u03c1=0.6\u3002q_score: mean=0.6243, std=0.3703, median=0.7753\u3002\u5b57\u6bb...
  [nmin4_seed42] found '5.9': ...t14:36:45.229z", "updated_at": "2026-05-15t21:22:25.975z", "spec": {"command": "bash -c \"source /ro...
  [bs8_seed42] found '5.9': ...tmux", "account": "root", "wall_clock_seconds": 695.9, "gpu_hours": 0.19}, "server": "westd-47453", ...
  [uniform_seed123] found '5.9': ..._seed123.log", "submitted_at": "2026-05-13t23:23:55.904z", "submitted_via": "submit_training_job", "...
  [golden_ratio_seed42] found 'golden_ratio': ...data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_rati...
  [grid_b_low_seed42] found '5.9': ..., "reproduce": {"finished_at": "2026-05-15t09:02:05.942z"}, "conclusion": "failed"}...
  [grid_b_seed42_batch] found '0.62': ...: 95, "b2_0_completed": true, "b2_0_train_loss": 10.621, "b2_0_train_runtime_s": 13034, "b3_0_comple...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "768caf32-6f0c-4046-aab6-b157cdd9d1a2"
}
```

</details>

---


### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check datagen, golden ratio, detector AUC details",
  "usage": {
    "total_tokens": 44388,
    "tool_uses": 17,
    "duration_ms": 219392
  },
  "last_tool_name": "Bash",
  "uuid": "c177927a-87fa-486e-ba22-ed535d9570cc",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_017QWsD6YweSZvxeFsTdkPj2`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Check datagen_synthetic_4gpu for 132M tokens\nprint(\"=== datagen_synthetic_4gpu full ===\")\nprint(json.dumps(exps['datagen_synthetic_4gpu'], indent=2)[:3000])\n\n# Check golden_ratio_seed42 for 0.62\nprint(\"\\n=== golden_ratio_seed42 full ===\")\nprint(json.dumps(exps['golden_ratio_seed42'], indent=2)[:2000])\n\n# Check detector AUC more precisely - paper says 0.94\n# Registry: detector_tfidf_lr.auc = 0.939\nprint(\"\\n=== detector_tfidf_lr AUC detail ===\")\nm = exps['detector_tfidf_lr']['metrics']\nprint(f\"  auc = {m['auc']}\")\nprint(f\"  ece_calibrated = {m['ece_calibrated']}\")\nprint(f\"  ece_raw = {m['ece_raw']}\")\n\n# Now check detector_modernbert for AUC = 0.986\nprint(\"\\n=== All detector experiments ===\")\nfor eid, exp in exps.items():\n    if 'detector' in eid.lower():\n        m = exp.get('metrics', {})\n        print(f\"  {eid}: {json.dumps(m)[:500]}\")\nPYEOF",
  "description": "Check datagen, golden ratio, detector AUC details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "9cba7c9c-d70e-493e-b4e9-c54afec3a25e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPLvj8S5htEZdLDkZeaF1R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3032,
      "cache_read_input_tokens": 40767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3032,
        "ephemeral_1h_input_tokens": 0
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

_source line 74 · 2026-05-25T19:46:25.108Z_

<details><summary>↩ Tool result · `toolu_017QWsD6YweSZvxeFsTdkPj2`</summary>

```text
=== datagen_synthetic_4gpu full ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T19:12:11.474Z",
  "updated_at": "2026-05-17T03:00:16.173Z",
  "spec": {
    "command": "4x parallel generate_synthetic.py --depth 1 --num_tokens 33000000 --batch_size 128",
    "server": "westd-47453",
    "data_path": "/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/",
    "data_count": "target 132M tokens across 4 shards",
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": "42/1042/2042/3042",
    "hypothesis": "4-GPU parallel generation produces 132M synthetic tokens in ~2.5h",
    "gpu": "cuda:0,1,2,3",
    "checkpoint_path": "/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/",
    "log_path": "/root/provenance_weight_training/data/synthetic/gen_gpu{0,1,2,3}.log",
    "total_docs": 340992,
    "total_tokens": 132033764
  },
  "conclusion": "success",
  "completed_at": "2026-05-13T21:50:46.682Z",
  "hypothesis": "4-GPU parallel synthetic data generation (Qwen3-0.6B, depth=1, 33M tokens/shard) produces sufficient scale and diversity for provenance contamination experiments while maintaining consistent stylistic distribution for detector calibration."
}

=== golden_ratio_seed42 full ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T07:20:12.943Z",
  "updated_at": "2026-05-15T13:33:31.162Z",
  "hypothesis": "Golden Ratio oracle baseline: w=1/\u03c6\u22480.618 for synthetic (q>0.5), w=1.0 for real \u2014 requires known proportion, serves as oracle upper bound for adaptive method",
  "server": "westd-47453",
  "gpu": "cuda:0",
  "account": "root",
  "reproduce": {
    "server": "westd-47453",
    "gpu": "cuda:0",
    "started_at": "2026-05-15T09:34:55.278Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\"",
    "finished_at": "2026-05-15T13:21:54.212Z",
    "training_hours": 3.78
  },
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:0"
    ],
    "pid": "193921",
    "log_path": "~/runs/provenance_weight_training/golden_ratio_seed42.log",
    "submitted_at": "2026-05-15T09:36:04.200Z",
    "submitte

=== detector_tfidf_lr AUC detail ===
  auc = 0.939
  ece_calibrated = 0.048
  ece_raw = 0.24

=== All detector experiments ===
  detector_modernbert: {}
  detector_tfidf_lr: {"auc": 0.939, "accuracy": 0.858, "ece_raw": 0.24, "ece_calibrated": 0.048, "temperature_T": 0.204, "q_score_mean": 0.6, "q_score_std": 0.374, "q_score_median": 0.707, "mid_range_ratio": 0.463}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "d6efd63b-b80a-48d8-b7a3-617bce67e60b"
}
```

</details>

---


### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Calculate epoch-matched gap",
  "usage": {
    "total_tokens": 46513,
    "tool_uses": 18,
    "duration_ms": 238639
  },
  "last_tool_name": "Bash",
  "uuid": "71cdbb1e-830c-4841-9918-f579cb827ec7",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_01PifotjDjCGqNJgUWVLbYp1`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Epoch-matched gap: paper says \"reducing the gap to Δ=0.017\"\n# D&R q>0.7 epoch-matched: detect_remove_q07_epoch_matched_seed42 = 17.62\n# What's the comparison? Probably D&R epoch-matched vs. adaptive epoch-matched or adaptive standard\n\n# D&R q>0.7 standard: 17.32 (3-seed mean)\n# D&R q>0.7 epoch-matched seed42: 17.62\n# Adaptive tau=0.7 seed42: tau07_seed42 = 17.68\n\n# gap = 17.62 - 17.674 = -0.054? No...\n# Maybe dr_epoch_matched_seed123_r2 = 17.6591, dr_epoch_matched_seed456 = 17.66\n# epoch_matched_dr_seed123 = 17.66, epoch_matched_dr_seed456 = 17.66\n\n# Let me check what epoch_matched_dr experiments are\nprint(\"=== epoch_matched_dr_seed123 ===\")\nexp = exps['epoch_matched_dr_seed123']\nprint(json.dumps({k: exp[k] for k in ['hypothesis', 'metrics', 'status']}, indent=2)[:1500])\n\nprint(\"\\n=== epoch_matched_dr_seed456 ===\")\nexp = exps['epoch_matched_dr_seed456']\nprint(json.dumps({k: exp[k] for k in ['hypothesis', 'metrics', 'status']}, indent=2)[:1500])\n\nprint(\"\\n=== detect_remove_q07_epoch_matched_seed42 ===\")\nexp = exps['detect_remove_q07_epoch_matched_seed42']\nprint(json.dumps({k: exp[k] for k in ['hypothesis', 'metrics', 'status']}, indent=2)[:1500])\n\n# D&R epoch-matched: 3 seeds would be needed for gap calculation\n# q07 epoch-matched seed42=17.62, dr_epoch_matched_seed123_r2=17.6591, epoch_matched_dr_seed456=17.66\n# mean = (17.62 + 17.6591 + 17.66) / 3\n\ndr_em_ppls = [17.62, 17.6591, 17.66]\ndr_em_mean = sum(dr_em_ppls) / 3\nprint(f\"\\nD&R epoch-matched 3-seed PPLs: {dr_em_ppls}\")\nprint(f\"D&R epoch-matched 3-seed mean: {dr_em_mean:.3f}\")\nprint(f\"Adaptive tau=0.7 5-seed mean: 17.674\")\nprint(f\"Gap (adaptive - DR_em): {17.674 - dr_em_mean:.3f}\")\n\n# Or maybe the gap is DR_em - adaptive\nprint(f\"Gap (DR_em - adaptive): {dr_em_mean - 17.674:.3f}\")\nPYEOF",
  "description": "Calculate epoch-matched gap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "cce2132c-c285-4747-9789-524ba429c41f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHbzV5kdpN9n3vvvEGXgTc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2087,
      "cache_read_input_tokens": 43799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2087,
        "ephemeral_1h_input_tokens": 0
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

_source line 77 · 2026-05-25T19:46:44.368Z_

<details><summary>↩ Tool result · `toolu_01PifotjDjCGqNJgUWVLbYp1`</summary>

```text
=== epoch_matched_dr_seed123 ===
{
  "hypothesis": "Cross-seed confirmation of D080: epoch-matched D&R (1 content epoch, ~83M tokens) will produce PPL similar to adaptive (~17.65), proving D&R's apparent 0.36 PPL advantage over adaptive is entirely from multi-epoch training, not data quality filtering. Seed 123 for 3-seed significance.",
  "metrics": {
    "eval_ppl_holdout": 17.66,
    "eval_loss_holdout": 2.8713,
    "eval_holdout_tokens": 4077068,
    "eval_method": "eval_perplexity.py --max_docs 5000 --max_length 2048",
    "eval_ppl_openwebtext": 18.3,
    "eval_ppl_wikitext": 27.9
  },
  "status": "DONE"
}

=== epoch_matched_dr_seed456 ===
{
  "hypothesis": "Cross-seed confirmation of D080: epoch-matched D&R (1 content epoch, ~83M tokens) will produce PPL similar to adaptive (~17.65), proving D&R's apparent 0.36 PPL advantage over adaptive is entirely from multi-epoch training, not data quality filtering. Seed 456 for 3-seed significance.",
  "metrics": {
    "eval_ppl_holdout": 17.66,
    "eval_loss_holdout": 2.8712,
    "eval_holdout_tokens": 4077068,
    "eval_method": "eval_perplexity.py --max_docs 5000 --max_length 2048",
    "eval_ppl_openwebtext": 18.27,
    "eval_ppl_wikitext": 28.14
  },
  "status": "DONE"
}

=== detect_remove_q07_epoch_matched_seed42 ===
{
  "hypothesis": "Epoch-matched D&R q07: 1 epoch through q07 filtered data (184,908 samples, ~100M tokens, 3047 steps). Part of 5-point epoch-matched curve (q01/q03/q05/q07/q09). If PPL converges to ~17.65-17.74 range like q03(17.74) and q05(17.65), confirms U-shape sweet spot is entirely multi-epoch artifact across the full threshold range.",
  "metrics": {
    "eval_ppl_holdout": 17.62,
    "eval_loss_holdout": 2.8689,
    "eval_holdout_tokens": 4077068,
    "eval_method": "sliding_window_stride1024_maxlen2048_fp16_5000docs",
    "total_steps": 3047
  },
  "status": "DONE"
}

D&R epoch-matched 3-seed PPLs: [17.62, 17.6591, 17.66]
D&R epoch-matched 3-seed mean: 17.646
Adaptive tau=0.7 5-seed mean: 17.674
Gap (adaptive - DR_em): 0.028
Gap (DR_em - adaptive): -0.028
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "13aab071-a6a4-4b7f-a617-356ed66c752b"
}
```

</details>

---


### System

_source line 78_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Search for 0.017 and 95% in registry",
  "usage": {
    "total_tokens": 48325,
    "tool_uses": 19,
    "duration_ms": 258690
  },
  "last_tool_name": "Bash",
  "uuid": "6106fbad-b4b9-4a7d-b43c-6be2b98e2a9a",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Bash · `toolu_01T1yn9nY8bzPxSSEhJPBEpS`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# The gap calculation doesn't match 0.017. Let me check other interpretations.\n# Maybe the gap is between D&R epoch-matched and uniform?\n# D&R epoch-matched mean: 17.646\n# Uniform 5-seed mean: 17.697\n# gap = 17.697 - 17.646 = 0.051? No\n\n# Maybe between D&R standard and D&R epoch-matched? \n# D&R standard: 17.320\n# D&R epoch-matched: 17.646\n# This shows multi-epoch effect = 0.326 PPL improvement\n\n# Maybe the paper means the gap between adaptive and D&R epoch-matched = 0.017?\n# adaptive mean = 17.674, D&R epoch-matched = 17.646... gap = 0.028\n\n# Let me check dr_epoch_matched_seed123_r2 more carefully - maybe different seeds used\nprint(\"=== dr_epoch_matched_seed123_r2 ===\")\nexp = exps['dr_epoch_matched_seed123_r2']\nprint(json.dumps({k: exp[k] for k in ['hypothesis', 'metrics', 'status'] if k in exp}, indent=2)[:1500])\n\n# Maybe the epoch-matched experiments used are detect_remove_q07_epoch_matched_seed42 + different ones\n# Let me check what seeds are in these experiments\nprint(\"\\n=== All DR epoch matched candidates ===\")\nfor eid in ['detect_remove_q07_epoch_matched_seed42', 'dr_epoch_matched_seed123_r2', 'dr_epoch_matched_seed456',\n            'epoch_matched_dr_seed123', 'epoch_matched_dr_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    cmd = exp.get('spec', {}).get('command', '')\n    # Check if it mentions q07\n    has_q07 = 'q07' in eid or 'q_07' in cmd or 'q>0.7' in exp.get('hypothesis', '')\n    print(f\"  {eid}: ppl={ppl}, is_q07={has_q07}\")\n    \n# Maybe the gap is between detect_remove_q07_epoch_matched and adaptive_tau07\n# seed42 only: 17.62 vs 17.68 = gap 0.06\n\n# Perhaps the gap is something else. Let me search notes for \"0.017\"\nprint(\"\\n=== SEARCH for 0.017 ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp)\n    if '0.017' in full_str:\n        idx = full_str.find('0.017')\n        print(f\"  {eid}: ...{full_str[max(0,idx-80):idx+80]}...\")\n\n# Search for \">95%\" or \"95\"\nprint(\"\\n=== SEARCH for 95% ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp)\n    if '95%' in full_str or '>95' in full_str:\n        idx = full_str.find('95')\n        print(f\"  {eid}: ...{full_str[max(0,idx-80):idx+80]}...\")\nPYEOF",
  "description": "Search for 0.017 and 95% in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "99f4e82f-fc0a-4d26-9930-c00c1e20cafc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wj39ZY3ztXpGj2dGzF6iah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1774,
      "cache_read_input_tokens": 45886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1774,
        "ephemeral_1h_input_tokens": 0
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

_source line 80 · 2026-05-25T19:47:04.415Z_

<details><summary>↩ Tool result · `toolu_01T1yn9nY8bzPxSSEhJPBEpS`</summary>

```text
=== dr_epoch_matched_seed123_r2 ===
{
  "hypothesis": "Epoch-matched D&R seed123 rerun with CORRECT effective batch=16 (batch_size=4 \u00d7 grad_accum=4). Previous dr_epoch_matched_seed123 was invalid (effective batch=4, missing grad_accum). Trains on filtered data (q\u22640.5, 153725 samples) for 2533 steps with independent linear LR schedule (5e-5\u21920). Paired with detect_remove_q05_v2_seed123 to quantify seed123 epoch confound percentage.",
  "metrics": {
    "holdout_loss": 2.8713,
    "holdout_ppl": 17.6591,
    "owt_loss": 2.9069,
    "owt_ppl": 18.2991,
    "wiki_loss": 2.7208,
    "wiki_ppl": 15.1918,
    "eval_holdout_tokens": 4077068,
    "eval_owt_tokens": 6767242,
    "eval_wiki_tokens": 27000339
  },
  "status": "DONE"
}

=== All DR epoch matched candidates ===
  detect_remove_q07_epoch_matched_seed42: ppl=17.62, is_q07=True
  dr_epoch_matched_seed123_r2: ppl=17.6591, is_q07=False
  dr_epoch_matched_seed456: ppl=17.66, is_q07=False
  epoch_matched_dr_seed123: ppl=17.66, is_q07=False
  epoch_matched_dr_seed456: ppl=17.66, is_q07=False

=== SEARCH for 0.017 ===

=== SEARCH for 95% ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "29a79c85-d2c1-4815-abe7-1e5d39882a6b"
}
```

</details>

---


### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check dr_epoch_matched_seed456 details and bs16 uniforms",
  "usage": {
    "total_tokens": 49911,
    "tool_uses": 20,
    "duration_ms": 286967
  },
  "last_tool_name": "Bash",
  "uuid": "cc486915-f921-4034-ae9a-262616be6aee",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Bash · `toolu_016QqwCNfnEiG4P23torfaw3`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# The 0.017 and 95% are not in the registry - they might be derived calculations\n# Let me verify:\n# D&R q>0.7 standard: 17.320 (3-seed)\n# D&R q>0.7 epoch-matched: 17.62 (seed42 only with q07)\n# But epoch-matched dr_seed123_r2 and dr_seed456 are q<=0.5, not q>0.7\n\n# Original gap: adaptive - D&R_standard = 17.674 - 17.320 = 0.354\n# Epoch-matched: adaptive - D&R_epoch_matched = ?\n\n# Actually the paper likely discusses:\n# D&R advantage = D&R_standard PPL - adaptive PPL = 17.320 - 17.674 = -0.354 (D&R is better by 0.354)\n# But this advantage mostly comes from multi-epoch training\n# When epoch-matched: D&R_epoch_matched - adaptive = 17.62 - 17.674 = -0.054 or similar\n# \"reducing the gap to 0.017\" might be:\n# Epoch-matched D&R advantage = adaptive - D&R_em = 17.674 - 17.66 = 0.014...\n\n# Or with dr_epoch_matched seed42 (q07): 17.62\n# Gap = 17.674 - 17.62 = 0.054\n\n# With dr q05 epoch-matched: detect_remove_q05_epoch_matched_seed42 = 17.65\n# Gap = 17.674 - 17.65 = 0.024\n\n# None of these give exactly 0.017. Let me look at what combination might.\n\n# Maybe using 3-seed DR epoch-matched mean vs 5-seed adaptive mean\n# dr_epoch_matched candidates for q>0.7:\n# Only detect_remove_q07_epoch_matched_seed42 = 17.62 exists for q>0.7\n# dr_epoch_matched_seed123_r2 = 17.6591 (q<=0.5)\n# epoch_matched_dr_seed456 = 17.66\n\n# Maybe the 3-seed epoch-matched mean for the best D&R threshold:\n# 17.6591, 17.66, 17.66 => mean = 17.6597\n# Gap = 17.674 - 17.6597 = 0.0143... close-ish to 0.017 but not exact\n\n# Let me check dr_epoch_matched_seed456 more carefully\nprint(\"=== dr_epoch_matched_seed456 ===\")\nexp = exps['dr_epoch_matched_seed456']\nprint(json.dumps({k: exp[k] for k in ['hypothesis', 'metrics', 'status'] if k in exp}, indent=2)[:1500])\n\n# Also check bs16 experiments for tau=0.7 which might be the actual main-table runs\nprint(\"\\n=== bs16 uniform experiments ===\")\nfor eid in ['bs16_uniform_seed42', 'bs16_uniform_seed123', 'bs16_uniform_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    print(f\"  {eid}: {json.dumps(m)[:300]}\")\nPYEOF",
  "description": "Check dr_epoch_matched_seed456 details and bs16 uniforms"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "0d873092-9c34-4cda-8280-a81ec464af89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtEQpusgTGQz1LpU1njib7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 47660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1548,
        "ephemeral_1h_input_tokens": 0
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

_source line 83 · 2026-05-25T19:47:32.682Z_

<details><summary>↩ Tool result · `toolu_016QqwCNfnEiG4P23torfaw3`</summary>

```text
=== dr_epoch_matched_seed456 ===
{
  "hypothesis": "Epoch-matched D&R seed456: trains on filtered data (q\u22640.5, 153725 samples) for exactly 2533 steps with independent linear LR schedule (5e-5\u21920), effective batch=16 (bs=4 \u00d7 grad_accum=4). Third seed for epoch confound quantification. Paired with dr_epoch_matched_indep_lr_v2_seed42 (17.651) and dr_epoch_matched_seed123_r2 (17.659).",
  "metrics": {
    "holdout_ppl": 17.66,
    "owt_ppl": 18.27,
    "wiki_ppl": 15.16
  },
  "status": "DONE"
}

=== bs16 uniform experiments ===
  bs16_uniform_seed42: {"holdout_loss": 2.8732, "holdout_ppl": 17.694, "owt_loss": 2.9104, "owt_ppl": 18.364, "wiki_loss": 2.7302, "wiki_ppl": 15.337, "train_loss": 1.965}
  bs16_uniform_seed123: {"holdout_loss": 2.8728, "holdout_ppl": 17.686, "owt_loss": 2.9107, "owt_ppl": 18.369, "wiki_loss": 2.7332, "wiki_ppl": 15.381, "train_loss": 1.997}
  bs16_uniform_seed456: {"holdout_loss": 2.8745, "holdout_ppl": 17.717, "owt_loss": 2.9118, "owt_ppl": 18.39, "wiki_loss": 2.7319, "wiki_ppl": 15.363, "total_steps": 6103, "train_loss": 1.991}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "41f3e996-ee77-4cd3-bf7b-b512288a33bc"
}
```

</details>

---


### System

_source line 84_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Verify uniform 5-seed mean calculation and check alternative experiment sets",
  "usage": {
    "total_tokens": 51510,
    "tool_uses": 21,
    "duration_ms": 311996
  },
  "last_tool_name": "Bash",
  "uuid": "86c58801-1c07-455c-90a3-db0eb80e60f6",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Bash · `toolu_01WQjsd4ELG7aomkt2AhPP64`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# The bs16 experiments seem to be the main table runs\n# bs16_adaptive_tau07 = {seed42: 17.631, seed123_r2: 17.616, seed456: 17.645}\n# bs16_uniform = {seed42: 17.694, seed123: 17.686, seed456: 17.717}\n\n# 3-seed means\nbs16_adap = [17.631, 17.616, 17.645]\nbs16_unif = [17.694, 17.686, 17.717]\nprint(f\"bs16 adaptive tau07 3-seed: {bs16_adap}\")\nprint(f\"bs16 adaptive tau07 mean: {sum(bs16_adap)/3:.3f}\")\nprint(f\"bs16 uniform 3-seed: {bs16_unif}\")\nprint(f\"bs16 uniform mean: {sum(bs16_unif)/3:.3f}\")\n\n# Hmm, paper says 5-seed for adaptive tau=0.7\n# Let me check if the paper actually uses bs16 or the smaller runs\n\n# Let me check what other tau07 experiments exist with all seeds\n# Paper adaptive tau=0.7 5-seed: \n# tau07_seed42=17.68, tau07_seed123=17.666, tau07_seed456=17.677\n# adaptive_seed234=17.678 (tau=0.7), adaptive_seed789=17.668 (tau=0.7)\n# Mean = 17.674 (matches paper!)\n\n# Paper uniform 5-seed:\n# uniform_seed42=17.6939, uniform_seed123=17.6861, uniform_seed456=17.7015\n# uniform_seed234=17.708, uniform_seed789=17.695\n# Mean = 17.697 (paper says 17.694)\n\n# Let me recompute more carefully\nu_ppls = [17.6939, 17.6861, 17.7015, 17.708, 17.695]\nu_mean = sum(u_ppls) / len(u_ppls)\nprint(f\"\\nUniform 5-seed mean (exact): {u_mean}\")\nprint(f\"Uniform 5-seed mean (3 decimal): {u_mean:.3f}\")\n\n# Hmm, 17.697 but paper says 17.694. Let me check if the paper might be using \n# different uniform values. Maybe uniform_ood_seed123 and uniform_ood_seed456\n# are the same as uniform_seed123/456?\nprint(\"\\n=== uniform_ood vs uniform ===\")\nfor eid in ['uniform_seed123', 'uniform_ood_seed123', 'uniform_seed456', 'uniform_ood_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    print(f\"  {eid}: ppl={ppl}\")\n\n# Check if uniform_seed234/789 have additional fields  \nprint(\"\\n=== uniform_seed234 full spec command ===\")\ncmd = exps['uniform_seed234'].get('spec', {}).get('command', '')\nprint(f\"  {cmd[:300]}\")\nprint(f\"\\n=== uniform_seed789 full spec command ===\")\ncmd = exps['uniform_seed789'].get('spec', {}).get('command', '')\nprint(f\"  {cmd[:300]}\")\n\n# Look for bs8_nmin4_uniform to check if those are the 5-seed uniform runs\n# bs8_nmin4_uniform: seed42, seed123, seed456, seed123_r2, seed456_r2\nprint(\"\\n=== bs8_nmin4_uniform PPLs ===\")\nfor eid in ['bs8_nmin4_uniform_seed42', 'bs8_nmin4_uniform_seed123', 'bs8_nmin4_uniform_seed123_r2', \n            'bs8_nmin4_uniform_seed456', 'bs8_nmin4_uniform_seed456_r2']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    print(f\"  {eid}: ppl={ppl}\")\nPYEOF",
  "description": "Verify uniform 5-seed mean calculation and check alternative experiment sets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "1b72d00c-89c4-4b53-b4fb-b2afba8f9fd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sczn9T3Vtnug5fJyTczFX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1561,
      "cache_read_input_tokens": 49208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1561,
        "ephemeral_1h_input_tokens": 0
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

_source line 86 · 2026-05-25T19:47:57.708Z_

<details><summary>↩ Tool result · `toolu_01WQjsd4ELG7aomkt2AhPP64`</summary>

```text
bs16 adaptive tau07 3-seed: [17.631, 17.616, 17.645]
bs16 adaptive tau07 mean: 17.631
bs16 uniform 3-seed: [17.694, 17.686, 17.717]
bs16 uniform mean: 17.699

Uniform 5-seed mean (exact): 17.6969
Uniform 5-seed mean (3 decimal): 17.697

=== uniform_ood vs uniform ===
  uniform_seed123: ppl=17.6861
  uniform_ood_seed123: ppl=17.6861
  uniform_seed456: ppl=17.7015
  uniform_ood_seed456: ppl=17.7015

=== uniform_seed234 full spec command ===
  python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_seed234 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gra

=== uniform_seed789 full spec command ===
  python -u training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_seed789 --model_name models/Qwen/Qwen3-0.6B --weighting_method uniform --num_train_tokens 200000000 --contamination_ratio 0.4 --batch_size 4 --gra

=== bs8_nmin4_uniform PPLs ===
  bs8_nmin4_uniform_seed42: ppl=17.694185837410274
  bs8_nmin4_uniform_seed123: ppl=None
  bs8_nmin4_uniform_seed123_r2: ppl=17.687
  bs8_nmin4_uniform_seed456: ppl=None
  bs8_nmin4_uniform_seed456_r2: ppl=17.702
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "6e1ec631-6f81-4890-baed-8a93e9e48bfa"
}
```

</details>

---


### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Resolve uniform mean discrepancy",
  "usage": {
    "total_tokens": 53431,
    "tool_uses": 22,
    "duration_ms": 331716
  },
  "last_tool_name": "Bash",
  "uuid": "cdbd5249-4547-4fd2-8f92-4b833da5fb00",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Bash · `toolu_018iGtF7o3WH48ijHWKYZLnP`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Hmm, the paper says uniform mean = 17.694, but I calculate 17.697 from the 5 individual values\n# Let me see if perhaps the paper uses bs8_nmin4_uniform instead:\n# bs8_nmin4_uniform_seed42 = 17.694185837410274\n# bs8_nmin4_uniform_seed123_r2 = 17.687\n# bs8_nmin4_uniform_seed456_r2 = 17.702\n# But that's only 3 seeds\n\n# Or maybe the paper rounds differently. Let me try:\n# uniform_seed42 = 17.6939\n# If paper rounds to 17.694, then uniform mean:\n# [17.694, 17.686, 17.702, 17.708, 17.695] = 17.697... still 17.697\n\n# Check: maybe the paper uses 3 seeds, not 5, for uniform:\nu3 = [17.6939, 17.6861, 17.7015]\nprint(f\"Uniform 3-seed mean (seed42/123/456): {sum(u3)/3:.3f}\")\n\n# Or bs8 uniform 3-seed:\nu3_bs8 = [17.694185837410274, 17.687, 17.702]\nprint(f\"bs8 uniform 3-seed mean: {sum(u3_bs8)/3:.3f}\")\n\n# Let me also try exact computation with more decimals for 5-seed\nu5 = [17.6939, 17.6861, 17.7015, 17.708, 17.695]\nprint(f\"\\nUniform 5-seed values: {u5}\")\nprint(f\"Sum: {sum(u5)}\")\nprint(f\"Mean: {sum(u5)/5}\")\n\n# For the paper to get 17.694 for uniform, it could be:\n# 5*17.694 = 88.470\n# What values sum to 88.470?\n# Currently: 17.6939 + 17.6861 + 17.7015 + 17.708 + 17.695 = 88.4845\n# Paper implies sum = 88.470\n# Difference = 0.0145\n\n# Maybe the paper values are slightly different. Let me check if there's a \n# \"holdout_ppl\" field instead of \"eval_ppl_holdout\" for some\nfor eid in ['uniform_seed42', 'uniform_seed123', 'uniform_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    print(f\"\\n  {eid} all ppl fields:\")\n    for k, v in m.items():\n        if 'ppl' in k.lower() or 'holdout' in k.lower():\n            print(f\"    {k} = {v}\")\n\n# Maybe the paper says 17.694 based on 3-seed, not 5-seed\n# 3-seed mean = 17.694 (exact match!)\nprint(f\"\\nUniform 3-seed mean = {sum(u3)/3:.3f}\")\n# Yes! The 3-seed mean is 17.694!\nPYEOF",
  "description": "Resolve uniform mean discrepancy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "b4456627-ce70-4ac0-9b90-781f1bf50d4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uqQoYkZs1hLPXp9LMLPp3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 50769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1883,
        "ephemeral_1h_input_tokens": 0
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

_source line 89 · 2026-05-25T19:48:17.440Z_

<details><summary>↩ Tool result · `toolu_018iGtF7o3WH48ijHWKYZLnP`</summary>

```text
Uniform 3-seed mean (seed42/123/456): 17.694
bs8 uniform 3-seed mean: 17.694

Uniform 5-seed values: [17.6939, 17.6861, 17.7015, 17.708, 17.695]
Sum: 88.4845
Mean: 17.6969

  uniform_seed42 all ppl fields:
    eval_ppl_holdout = 17.6939
    eval_loss_holdout = 2.8732
    eval_holdout_tokens = 4077068

  uniform_seed123 all ppl fields:
    eval_ppl_holdout = 17.6861
    eval_loss_holdout = 2.8728
    eval_holdout_tokens = 4077068

  uniform_seed456 all ppl fields:
    eval_ppl_holdout = 17.7015
    eval_loss_holdout = 2.8737
    eval_holdout_tokens = 4077068

Uniform 3-seed mean = 17.694
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "914af14b-1f01-4bfc-a776-de585e3353dc"
}
```

</details>

---


### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Verify delta calculations and identify inconsistencies",
  "usage": {
    "total_tokens": 54753,
    "tool_uses": 23,
    "duration_ms": 354536
  },
  "last_tool_name": "Bash",
  "uuid": "3b889e5e-bfb1-45d2-a5e5-f3819ca27dbd",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_01SPHevmCcvq1waLVqFicavU`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# So the paper says \"5-seed mean\" but uniform 3-seed mean = 17.694, 5-seed = 17.697\n# Let me check if paper really says 5-seed for uniform. The user says:\n# \"Uniform baseline 5-seed mean: 17.694\"\n# Registry 3-seed (42,123,456) = 17.694 ← matches\n# Registry 5-seed (42,123,456,234,789) = 17.697 ← doesn't match\n\n# The claim in the paper is \"5-seed\" but the number matches 3-seed computation.\n# This is a potential discrepancy.\n\n# Now let me verify the adaptive tau=0.7 more carefully:\n# tau07_seed42 = 17.68, tau07_seed123 = 17.666, tau07_seed456 = 17.677\n# adaptive_seed234 (tau=0.7) = 17.678, adaptive_seed789 (tau=0.7) = 17.668\n# 5-seed mean = 17.6738 ≈ 17.674 (matches to 3 d.p.)\n\na5 = [17.68, 17.666, 17.677, 17.678, 17.668]\nprint(f\"Adaptive tau=0.7 5-seed: {a5}\")\nprint(f\"Sum: {sum(a5)}\")\nprint(f\"Mean: {sum(a5)/5}\")\nprint(f\"Mean (3 d.p.): {sum(a5)/5:.3f}\")\n\n# 3-seed adaptive tau=0.7:\na3 = [17.68, 17.666, 17.677]\nprint(f\"\\nAdaptive tau=0.7 3-seed: {a3}\")\nprint(f\"Mean: {sum(a3)/3:.3f}\")\n\n# So adaptive 5-seed mean = 17.674 and 3-seed mean = 17.674 too\n# Paper says 17.674 - checks out\n\n# Delta at rho=0.4:\n# adaptive 5-seed: 17.674, uniform 5-seed: 17.697 => delta = -0.023 ← matches paper\n# adaptive 5-seed: 17.674, uniform 3-seed: 17.694 => delta = -0.020 ← doesn't match\n# adaptive 3-seed: 17.674, uniform 3-seed: 17.694 => delta = -0.020\n\n# Hmm wait, let me recheck:\nprint(f\"\\n5-seed delta: {sum(a5)/5 - 17.6969:.3f}\")\nprint(f\"adaptive_5_seed - uniform_5_seed: {sum(a5)/5 - sum([17.6939, 17.6861, 17.7015, 17.708, 17.695])/5:.3f}\")\n\n# Paper says delta = -0.023 at rho=0.4\n# My calculation: 17.674 - 17.697 = -0.023 (using 5-seed adaptive, 5-seed uniform) ← matches!\n# But paper says uniform is 17.694 (which is 3-seed), while delta -0.023 corresponds to 5-seed uniform 17.697\n# So either the paper uses different seed counts for different claims, or I'm misreading\n\n# Check: 17.674 - 17.694 = -0.020, not -0.023\nprint(f\"\\n17.674 - 17.694 = {17.674 - 17.694:.3f}\")\nprint(f\"17.674 - 17.697 = {17.674 - 17.697:.3f}\")\n\n# So the delta -0.023 is consistent with 5-seed uniform (17.697)\n# But paper says uniform 5-seed mean = 17.694 which gives delta = -0.020\n# This is an internal inconsistency in the paper!\nPYEOF",
  "description": "Verify delta calculations and identify inconsistencies"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "ff3be607-1d89-42bc-aaf4-968002e9cdda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrXC98atA7uEHVaZJ3x4Lg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 52652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1284,
        "ephemeral_1h_input_tokens": 0
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

_source line 92 · 2026-05-25T19:48:40.267Z_

<details><summary>↩ Tool result · `toolu_01SPHevmCcvq1waLVqFicavU`</summary>

```text
Adaptive tau=0.7 5-seed: [17.68, 17.666, 17.677, 17.678, 17.668]
Sum: 88.369
Mean: 17.6738
Mean (3 d.p.): 17.674

Adaptive tau=0.7 3-seed: [17.68, 17.666, 17.677]
Mean: 17.674

5-seed delta: -0.023
adaptive_5_seed - uniform_5_seed: -0.023

17.674 - 17.694 = -0.020
17.674 - 17.697 = -0.023
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "4e6fada6-461e-467b-8db1-a259b6de30b8"
}
```

</details>

---


### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Calculate epoch-matched gap and multi-epoch percentage",
  "usage": {
    "total_tokens": 56163,
    "tool_uses": 24,
    "duration_ms": 381173
  },
  "last_tool_name": "Bash",
  "uuid": "bd5f31fa-158d-4aa9-8fec-937d56a47871",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Bash · `toolu_011gwM1geZaTVbyeqkMtesgF`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Now let me check the epoch-matched gap more carefully\n# The D&R q>0.7 data (non-epoch-matched): seed42_r3=17.32, seed123=17.32, seed456=17.32\n# D&R q>0.7 epoch-matched: only seed42 = 17.62\n# But maybe there are q>0.5 epoch-matched experiments used too\n\n# Let me check the detect_remove_q05_epoch_matched\nprint(\"=== detect_remove_q05_epoch_matched_seed42 ===\")\nexp = exps['detect_remove_q05_epoch_matched_seed42']\nm = exp.get('metrics', {})\nppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\nprint(f\"  ppl={ppl}\")\nprint(json.dumps({k: exp[k] for k in ['hypothesis'] if k in exp}, indent=2)[:500])\n\n# For the epoch-matched gap Δ=0.017:\n# D&R q>0.7 epoch-matched seed42: 17.62\n# D&R q>0.5 epoch-matched seed42: 17.65\n# Adaptive tau=0.7 (some seed): 17.674\n\n# 17.674 - 17.62 = 0.054 (q>0.7 gap)\n# 17.674 - 17.65 = 0.024 (q>0.5 gap)\n\n# What about the epoch confound calculation?\n# D&R standard PPL - D&R epoch-matched PPL = multi-epoch benefit\n# For q>0.7: 17.32 - 17.62 = -0.30 (D&R gets 0.30 PPL from multi-epoch)\n# Adaptive - uniform gap = -0.023\n# \"reducing the gap\" from (D&R_standard - adaptive = 17.32 - 17.674 = -0.354)\n# to (D&R_epoch_matched - adaptive = 17.62 - 17.674 = -0.054)\n\n# Or the gap between D&R epoch-matched and adaptive:\n# adaptive tau=0.7 = 17.674\n# D&R epoch-matched (q>0.5, 3-seed mean): \ndr_q05_em = [17.65053, 17.6591, 17.66]  # dr_epoch_matched_indep_lr_v2_seed42, dr_epoch_matched_seed123_r2, dr_epoch_matched_seed456\ndr_q05_em_mean = sum(dr_q05_em) / 3\nprint(f\"\\nD&R q>0.5 epoch-matched 3-seed mean: {dr_q05_em_mean:.3f}\")\nprint(f\"Gap (adaptive - DR_em): {17.674 - dr_q05_em_mean:.3f}\")\n\n# 17.674 - 17.657 = 0.017 ← MATCHES!\n# So the epoch-matched gap Δ=0.017 is: adaptive_tau07_mean - DR_epoch_matched_mean\n# Using dr_epoch_matched_indep_lr_v2_seed42 (17.65053), dr_epoch_matched_seed123_r2 (17.6591), \n# dr_epoch_matched_seed456 (17.66) for the D&R epoch-matched experiments\n\nprint(f\"\\nExact: {17.674 - dr_q05_em_mean}\")\n\n# Now for \">95% of advantage from multi-epoch\":\n# Original D&R advantage over adaptive: 17.674 - 17.32 = 0.354 PPL gap (D&R better)\n# Epoch-matched residual: 17.674 - 17.657 = 0.017\n# So multi-epoch explains: (0.354 - 0.017) / 0.354 = 0.337 / 0.354 = 95.2%\npct = (0.354 - 0.017) / 0.354 * 100\nprint(f\"\\n% explained by multi-epoch: {pct:.1f}%\")\n# So \">95%\" is derived from 95.2%\nPYEOF",
  "description": "Calculate epoch-matched gap and multi-epoch percentage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "6efd6c67-1719-492c-9eb8-2dfb0b3b8eac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kzAEzRV5ohmfiYTizWff2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1372,
      "cache_read_input_tokens": 53936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1372,
        "ephemeral_1h_input_tokens": 0
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

_source line 95 · 2026-05-25T19:49:06.897Z_

<details><summary>↩ Tool result · `toolu_011gwM1geZaTVbyeqkMtesgF`</summary>

```text
=== detect_remove_q05_epoch_matched_seed42 ===
  ppl=17.65
{
  "hypothesis": "Epoch-matched control: training with uniform weighting on filtered data (q>0.5 removed) for exactly 2533 steps (matching content-level 1 epoch of the contaminated data). If PPL is comparable to the full 6103-step D&R run, the D&R benefit comes from data quality not extra training; if PPL is worse, the extra training contributes meaningfully."
}

D&R q>0.5 epoch-matched 3-seed mean: 17.657
Gap (adaptive - DR_em): 0.017

Exact: 0.017456666666667786

% explained by multi-epoch: 95.2%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "e874d696-fdff-431e-bdc3-1f39d0421bdb"
}
```

</details>

---


### System

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Calculate SD and p-values for adaptive tau=0.7",
  "usage": {
    "total_tokens": 57675,
    "tool_uses": 25,
    "duration_ms": 400801
  },
  "last_tool_name": "Bash",
  "uuid": "fc25b153-68a6-497b-9ccf-0c1c77d08a40",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_01GP9VSSx7cPE3qy2gsU28Di`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Now let me compute SD for adaptive tau=0.7\nimport statistics\n\na5 = [17.68, 17.666, 17.677, 17.678, 17.668]\nsd_a5 = statistics.stdev(a5)\nprint(f\"Adaptive tau=0.7 5-seed SD: {sd_a5:.4f}\")\nprint(f\"Paper says SD = 0.006\")\n\n# SD = 0.006 matches!\n# (Actually 0.0060 to 4 d.p.)\n\n# p-values are derived, not in registry. Let me verify:\n# p_BH = 0.011 for adaptive tau=0.7\n# p_BH = 0.064 for rho=0.6 adaptive\n# These are from a Benjamini-Hochberg corrected test, likely a paired t-test or similar\n\n# Let me compute a t-test for adaptive vs uniform at rho=0.4\n# Paired: tau07_seed42 vs uniform_seed42, etc.\n# But the 5-seed adaptive and uniform have different seeds (234, 789)\n# Actually they do match: adaptive_seed234 = tau=0.7, uniform_seed234\n\n# Paired differences:\ndiffs_5seed = []\nadaptive_seeds = {'42': 17.68, '123': 17.666, '456': 17.677, '234': 17.678, '789': 17.668}\nuniform_seeds = {'42': 17.6939, '123': 17.6861, '456': 17.7015, '234': 17.708, '789': 17.695}\n\nfor s in ['42', '123', '456', '234', '789']:\n    d = adaptive_seeds[s] - uniform_seeds[s]\n    diffs_5seed.append(d)\n    print(f\"  seed {s}: adaptive={adaptive_seeds[s]}, uniform={uniform_seeds[s]}, diff={d:.4f}\")\n\nfrom scipy import stats\nt_stat, p_value = stats.ttest_1samp(diffs_5seed, 0)\nprint(f\"\\nPaired t-test: t={t_stat:.4f}, p={p_value:.4f}\")\nprint(f\"Paper says p_BH = 0.011\")\n\n# Rho=0.6\nrho06_a = [17.735, 17.727, 17.732]\nrho06_u = [17.766, 17.754, 17.770]\ndiffs_rho06 = [a - u for a, u in zip(rho06_a, rho06_u)]\nt_stat6, p_value6 = stats.ttest_1samp(diffs_rho06, 0)\nprint(f\"\\nRho=0.6 paired t-test: t={t_stat6:.4f}, p={p_value6:.4f}\")\nprint(f\"Paper says p_BH = 0.064\")\nPYEOF",
  "description": "Calculate SD and p-values for adaptive tau=0.7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "377ccebe-9eb3-49de-a773-6c16a67a58fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJrDJUpE1pJh8ScGhVse96",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1476,
      "cache_read_input_tokens": 55308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1476,
        "ephemeral_1h_input_tokens": 0
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

_source line 98 · 2026-05-25T19:49:27.385Z_

<details><summary>↩ Tool result · `toolu_01GP9VSSx7cPE3qy2gsU28Di`</summary>

```text
Adaptive tau=0.7 5-seed SD: 0.0063
Paper says SD = 0.006
  seed 42: adaptive=17.68, uniform=17.6939, diff=-0.0139
  seed 123: adaptive=17.666, uniform=17.6861, diff=-0.0201
  seed 456: adaptive=17.677, uniform=17.7015, diff=-0.0245
  seed 234: adaptive=17.678, uniform=17.708, diff=-0.0300
  seed 789: adaptive=17.668, uniform=17.695, diff=-0.0270

Paired t-test: t=-8.2077, p=0.0012
Paper says p_BH = 0.011

Rho=0.6 paired t-test: t=-9.9547, p=0.0099
Paper says p_BH = 0.064
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "69952e54-fe88-40a7-ae56-7c4258b94394"
}
```

</details>

---


### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Search for constraint binding, sharpening exponents, Pearson correlation",
  "usage": {
    "total_tokens": 58907,
    "tool_uses": 26,
    "duration_ms": 427333
  },
  "last_tool_name": "Bash",
  "uuid": "8cec12dc-708e-42f4-a971-4efc9233b944",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_01ChaLVCmJFmx1DwkxKgAc9f`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# p-values:\n# Raw p=0.0012 for rho=0.4 → with BH correction across multiple tests, becomes 0.011\n# Raw p=0.0099 for rho=0.6 → with BH correction, becomes 0.064\n# These are BH-corrected p-values, so the raw values in the registry computation align with\n# the paper's BH-corrected values. The specific BH correction depends on how many tests total.\n\n# Let me compute: if we have k tests and want BH correction:\n# p_BH = p_raw * k / rank\n# For rho=0.4: p_BH = 0.011, p_raw = 0.0012\n# 0.011 = 0.0012 * k / rank\n# If rank=1 (smallest p): k = 0.011 / 0.0012 = 9.17 → ~9 tests?\n\n# For rho=0.6: p_BH = 0.064, p_raw = 0.0099\n# If rank=2: 0.064 = 0.0099 * k / 2, k = 0.064*2/0.0099 = 12.9 → ~13 tests?\n# These don't perfectly align, suggesting the raw p-values from the registry might differ\n# from what I computed (the registry experiments might use different seed pairings)\n\n# These p-values are derived, not directly stored in registry\n# The raw t-test gives plausible input values that would produce these BH-corrected p-values\n\n# Now let me check constraint binding and sharpening exponents\n# \"~50% of batches where quality constraint binds\"\n# \"~5.9× lower sharpening exponents\"\n\n# Search for constraint_binds or bind_rate\nprint(\"=== SEARCH for constraint/bind ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp).lower()\n    if 'bind' in full_str or 'constraint_active' in full_str or 'quality_constraint' in full_str:\n        # Find relevant metrics\n        m = exp.get('metrics', {})\n        for k, v in m.items():\n            if 'bind' in k.lower() or 'constraint' in k.lower() or 'active' in k.lower():\n                print(f\"  {eid}.{k} = {v}\")\n\n# Search for sharpening exponent\nprint(\"\\n=== SEARCH for sharpening/exponent ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp).lower()\n    if 'sharpen' in full_str or 'exponent' in full_str:\n        m = exp.get('metrics', {})\n        for k, v in m.items():\n            if 'sharpen' in k.lower() or 'exponent' in k.lower() or 'b_star' in k.lower():\n                print(f\"  {eid}.{k} = {v}\")\n\n# Check b_star values for comparison (5.9× lower)\n# tau=0.8 adaptive b_star_mean vs tau=0.7\nprint(\"\\n=== b_star values for tau comparison ===\")\nfor eid in ['tau_07_seed42', 'tau_09_seed42', 'tau_06_seed42', 'tau_05_seed42', 'tau_095_seed42']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    bm = m.get('b_star_mean')\n    print(f\"  {eid}: b_star_mean={bm}\")\n\n# Pearson r ≈ 0.79 for alpha_eff correlation\nprint(\"\\n=== SEARCH for r=0.79 or correlation ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp)\n    if '0.79' in full_str:\n        idx = full_str.find('0.79')\n        print(f\"  {eid}: ...{full_str[max(0,idx-60):idx+60]}...\")\nPYEOF",
  "description": "Search for constraint binding, sharpening exponents, Pearson correlation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "12bc40d5-5407-4e39-856b-34c81396f62d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TC5PrTqHcRuSYUejb4tfGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1194,
      "cache_read_input_tokens": 56784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1194,
        "ephemeral_1h_input_tokens": 0
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

_source line 101 · 2026-05-25T19:49:53.071Z_

<details><summary>↩ Tool result · `toolu_01ChaLVCmJFmx1DwkxKgAc9f`</summary>

```text
=== SEARCH for constraint/bind ===

=== SEARCH for sharpening/exponent ===

=== b_star values for tau comparison ===
  tau_07_seed42: b_star_mean=0.8943
  tau_09_seed42: b_star_mean=2.36
  tau_06_seed42: b_star_mean=0.5899
  tau_05_seed42: b_star_mean=0.3923
  tau_095_seed42: b_star_mean=3.0775

=== SEARCH for r=0.79 or correlation ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "38946945-08af-4610-b7e7-aefd4d7f4362"
}
```

</details>

---


### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check sharpening exponent ratios and ESS-only experiments",
  "usage": {
    "total_tokens": 60359,
    "tool_uses": 27,
    "duration_ms": 448786
  },
  "last_tool_name": "Bash",
  "uuid": "69de206f-7ec2-4f2f-ba89-bbbf00954bb8",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Bash · `toolu_015zup5japfEDsHu4hGHCeGR`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# 5.9× lower sharpening exponents: not directly in registry\n# But we can check: adaptive_seed42 says b_star range 0.0-3.8, tau=0.8\n# tau_07_seed42: b_star_mean=0.8943\n# Compare to what? Maybe vs ESS-only or fixed-b approaches?\n\n# Check ess_only b_star\nfor eid in ['ess_only_seed42', 'ess_only_seed123', 'ess_only_seed456',\n            'ess_only_seed123_r2', 'ess_only_seed456_r2']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    bm = m.get('b_star_mean')\n    print(f\"  {eid}: b_star_mean={bm}\")\n\n# ess_only_seed42 b_star_mean=3.51, ess_only_seed123 b_star_mean=3.55\n# tau=0.7: 0.8943\n# ratio: 3.51/0.8943 ≈ 3.93... not 5.9\n\n# Check nmin1\nfor eid in ['nmin1_seed42']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    bm = m.get('b_star_mean')\n    print(f\"  {eid}: b_star_mean={bm}\")\n\n# nmin1: b_star_mean=7.197\n# vs adaptive (tau=0.7) b_star_mean=0.8943\n# 7.197 / 0.8943 ≈ 8.05... not 5.9\n\n# Let me check the adaptive_fix experiments\nfor eid in ['adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    bm = m.get('b_star_mean')\n    bs = m.get('b_star_std')\n    print(f\"  {eid}: b_star_mean={bm}, b_star_std={bs}\")\n\n# Check aeff_only experiments\nfor eid in ['aeff_only_nmin1_seed42', 'aeff_only_nmin1_seed123', 'aeff_only_nmin1_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    bm = m.get('b_star_mean')\n    print(f\"  {eid}: b_star_mean={bm}\")\n\n# The 5.9× factor might be derived from specific comparison not in registry\n# Or from comparing adaptive (tau=0.7, dual constraint) vs ESS-only\n# ESS-only mean ≈ (3.51+3.55)/2 = 3.53\n# Adaptive tau=0.7 ≈ 0.8943\n# Ratio = 3.53/0.8943 ≈ 3.95\n# Not 5.9. This number might come from a more detailed analysis not in the registry.\n\n# Check for rho02 experiments\nfor eid in ['rho02_adaptive_tau09_r5', 'rho02_adaptive_tau08_seed42', 'rho02_uniform_seed42']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    bm = m.get('b_star_mean')\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    print(f\"  {eid}: b_star_mean={bm}, ppl={ppl}\")\nPYEOF",
  "description": "Check sharpening exponent ratios and ESS-only experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "8a08e1af-09c0-402c-a490-1bdd6d2e6dd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4Hi3Q3QGqWc61vXPV7uq2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 57978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1414,
        "ephemeral_1h_input_tokens": 0
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

_source line 104 · 2026-05-25T19:50:14.498Z_

<details><summary>↩ Tool result · `toolu_015zup5japfEDsHu4hGHCeGR`</summary>

```text
  ess_only_seed42: b_star_mean=3.51
  ess_only_seed123: b_star_mean=3.55
  ess_only_seed456: b_star_mean=None
  ess_only_seed123_r2: b_star_mean=None
  ess_only_seed456_r2: b_star_mean=None
  nmin1_seed42: b_star_mean=7.197
  adaptive_fix_seed42: b_star_mean=None, b_star_std=None
  adaptive_fix_seed123: b_star_mean=1.431, b_star_std=2.029
  adaptive_fix_seed456: b_star_mean=1.416, b_star_std=1.993
  aeff_only_nmin1_seed42: b_star_mean=None
  aeff_only_nmin1_seed123: b_star_mean=None
  aeff_only_nmin1_seed456: b_star_mean=None
  rho02_adaptive_tau09_r5: b_star_mean=4.3493, ppl=17.45
  rho02_adaptive_tau08_seed42: b_star_mean=None, ppl=17.382
  rho02_uniform_seed42: b_star_mean=None, ppl=17.336
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "699a833b-6671-4480-b631-be7b980fdadd"
}
```

</details>

---


### System

_source line 105_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Verify D&R threshold PPLs and identify discrepancy",
  "usage": {
    "total_tokens": 62031,
    "tool_uses": 28,
    "duration_ms": 478861
  },
  "last_tool_name": "Bash",
  "uuid": "742abe56-915b-4aeb-89c5-7f7b242b84fc",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 106_

<details open><summary>🔧 Tool call — Bash · `toolu_0133gYr4C5UMLjQENQ7mgrAy`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Let me check the Qwen3-0.6B and data count values in spec\nexp = exps['adaptive_seed42']\nprint(f\"model_name in spec: {exp['spec'].get('model_name')}\")\nprint(f\"data_count in spec: {exp['spec'].get('data_count')}\")\n\n# 132M tokens\nprint(f\"\\ndatagen total_tokens: {exps['datagen_synthetic_4gpu']['spec'].get('total_tokens')}\")\n\n# Check for \"132\" in num_train_tokens\ncmd = exp['spec'].get('command', '')\nprint(f\"\\nnum_train_tokens in command: 200000000 (from command)\")\n\n# The 132M is for synthetic data generation, not training tokens\n# Training uses 200M tokens total\n\n# Now check contamination_ratio = 0.4 means 40% synthetic\n# 371499 total samples, 0.4 contamination = 148,600 synthetic + 222,899 real\n\n# Let me also check the D&R q>0.7 PPL = 17.250 claim more carefully\n# Paper says \"D&R q>0.7 PPL 17.250\" but registry shows D&R q>0.7 = 17.32\n# The 17.250 matches D&R q>0.3 (seed42_r2=17.25, seed123=17.25, seed456=17.2509)\n# D&R q>0.3 retains only 31.5% of data\n\n# So there are two possible issues:\n# 1. Paper might mean \"D&R best threshold\" not specifically \"q>0.7\"\n# 2. Or the paper's number is wrong\n\n# Let me check: paper says \"PPL 17.250 vs. 17.674, 3 seeds\" in introduction\n# \"D&R q>0.7\" might not be the specific claim - maybe just \"D&R\"\n# The user said: \"D&R q>0.7 3-seed PPL: 17.250\"\n\n# D&R q>0.7 3-seed mean from registry = 17.32\n# D&R q>0.3 3-seed mean from registry = 17.250\n\n# Let me also look for the \"D&R best\" threshold\n# q>0.3: 17.25 (best)\n# q>0.2: 17.27\n# q>0.4: 17.26\n# q>0.5: 17.29\n# q>0.7: 17.32\n\n# Actually let me re-read: the user says \"D&R q>0.7 3-seed PPL: 17.250\"\n# This says the PAPER claims D&R q>0.7 gives 17.250\n# But registry shows D&R q>0.7 = 17.32\n# THIS IS A DISCREPANCY - either the paper has the wrong threshold label or wrong PPL\n\n# Confirm the D&R q>0.7 3-seed values\nfor eid in ['detect_remove_q07_seed42_r3', 'detect_remove_q07_seed123', 'detect_remove_q07_seed456']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n    print(f\"  {eid}: ppl={ppl}\")\n\n# All are 17.32\n# The 17.250 value belongs to D&R q>0.3 (best threshold)\n# So either paper says \"q>0.7\" but means something else, or the number is wrong\n\n# Check if maybe D&R best (across thresholds) 3-seed mean is 17.250\nprint(\"\\n=== D&R 3-seed means by threshold ===\")\nthresholds = {\n    'q01': ['detect_remove_q01_seed42'],\n    'q02': ['detect_remove_q02_seed42'],\n    'q03': ['detect_remove_q03_seed42_r2', 'detect_remove_q03_seed123', 'detect_remove_q03_seed456'],\n    'q04': ['detect_remove_q04_seed42'],\n    'q05': ['detect_remove_q05_seed42', 'detect_remove_q05_seed123', 'detect_remove_q05_seed456'],\n    'q06': ['detect_remove_q06_seed42'],\n    'q07': ['detect_remove_q07_seed42_r3', 'detect_remove_q07_seed123', 'detect_remove_q07_seed456'],\n    'q08': ['detect_remove_q08_seed42'],\n    'q09': ['detect_remove_q09_seed42'],\n}\nfor thresh, eids in thresholds.items():\n    ppls = []\n    for eid in eids:\n        exp = exps.get(eid, {})\n        m = exp.get('metrics', {})\n        ppl = m.get('eval_ppl_holdout') or m.get('holdout_ppl')\n        if ppl:\n            ppls.append(ppl)\n    if ppls:\n        mean = sum(ppls) / len(ppls)\n        print(f\"  {thresh}: {len(ppls)}-seed mean={mean:.3f}, values={ppls}\")\nPYEOF",
  "description": "Verify D&R threshold PPLs and identify discrepancy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "6e90409a-9851-4d3c-b7f6-5e527e8ee32e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ep7Yjq3AQHa2m38HUdRPit",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 59392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1634,
        "ephemeral_1h_input_tokens": 0
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

_source line 107 · 2026-05-25T19:50:44.584Z_

<details><summary>↩ Tool result · `toolu_0133gYr4C5UMLjQENQ7mgrAy`</summary>

```text
model_name in spec: Qwen/Qwen3-0.6B
data_count in spec: 371499

datagen total_tokens: 132033764

num_train_tokens in command: 200000000 (from command)
  detect_remove_q07_seed42_r3: ppl=17.32
  detect_remove_q07_seed123: ppl=17.32
  detect_remove_q07_seed456: ppl=17.32

=== D&R 3-seed means by threshold ===
  q01: 1-seed mean=17.400, values=[17.4]
  q02: 1-seed mean=17.270, values=[17.27]
  q03: 3-seed mean=17.250, values=[17.25, 17.25, 17.2509]
  q04: 1-seed mean=17.260, values=[17.26]
  q05: 3-seed mean=17.280, values=[17.291, 17.27, 17.28]
  q06: 1-seed mean=17.300, values=[17.3]
  q07: 3-seed mean=17.320, values=[17.32, 17.32, 17.32]
  q08: 1-seed mean=17.344, values=[17.3442]
  q09: 1-seed mean=17.420, values=[17.42]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "74bdde1d-e708-466a-bb82-15fe86e7ef01"
}
```

</details>

---


### System

_source line 108_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check remaining numbers - wiki tokens, external references",
  "usage": {
    "total_tokens": 63991,
    "tool_uses": 29,
    "duration_ms": 502429
  },
  "last_tool_name": "Bash",
  "uuid": "28c3517e-60af-4f26-9947-a70499c7d6c3",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Bash · `toolu_01LJakf19Yg5LSuat1ap6YUt`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# D&R best threshold is q>0.3 with PPL 17.250 (3-seed)\n# Paper says \"D&R q>0.7 PPL 17.250\" - if paper indeed says q>0.7, this is wrong\n# q>0.7 gives 17.32, while 17.250 belongs to q>0.3\n\n# Let me now check the remaining numbers\n\n# Qwen3-0.6B: confirmed in spec\n# 371,499 samples: confirmed (data_count = 371499)\n# rho = 0.4: confirmed (contamination_ratio = 0.4 in command/metrics)\n# 132M tokens: confirmed (total_tokens = 132033764 in datagen_synthetic_4gpu)\n\n# AUC = 0.94 vs registry 0.939\n# Paper says AUC = 0.94, registry = 0.939\n# 0.939 rounds to 0.94 ← consistent\n\n# ECE = 0.048: matches registry ece_calibrated = 0.048 exactly\n\n# Let me now look for ModernBERT-150M detector AUC=0.986\n# detector_modernbert never ran (killed/cancelled). No metrics.\n# So AUC=0.986 is NOT in registry. This is likely from a cited paper.\n\n# WikiText-2 ~2M tokens - this is a dataset fact, not experimental\n# Let me check if any experiment mentions WikiText tokens\n\nprint(\"=== Wiki tokens in experiments ===\")\nfor eid, exp in exps.items():\n    m = exp.get('metrics', {})\n    for k, v in m.items():\n        if 'wiki' in k.lower() and 'token' in k.lower():\n            print(f\"  {eid}.{k} = {v}\")\n\n# Golden ratio reciprocal ≈0.62\n# golden_ratio_seed42 uses w=1/φ≈0.618 for synthetic\n# 0.62 is approximately 1/φ = 0.618... paper says ≈0.62\n# This is just rounding 0.618 to 0.62\n\n# \"20-60% of web corpora\" synthetic content - external claim, not in registry\n# Drayson et al. b=10 for ≤360M, b=1 for 1.7B - external, not in registry\n\n# Check for any reference to \"Drayson\" or \"b=10\" or \"360M\" in registry\nprint(\"\\n=== Search for external references ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp).lower()\n    for target in ['drayson', '360m', 'modernbert', '150m', 'b=10', '986']:\n        if target in full_str:\n            idx = full_str.find(target)\n            print(f\"  [{eid}] '{target}': ...{full_str[max(0,idx-50):idx+50]}...\")\nPYEOF",
  "description": "Check remaining numbers - wiki tokens, external references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "64db41f5-a385-44a5-9528-bd19d2d7cf96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WZjt4dirgDMMaJDuEHKRPk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 61026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1922,
        "ephemeral_1h_input_tokens": 0
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

_source line 110 · 2026-05-25T19:51:08.164Z_

<details><summary>↩ Tool result · `toolu_01LJakf19Yg5LSuat1ap6YUt`</summary>

```text
=== Wiki tokens in experiments ===
  permuted_score_control_seed42.wiki_tokens = 5009907
  detect_remove_q05_v2_seed123_r2.eval_wiki_tokens = 27000339
  dr_epoch_matched_seed123_r2.eval_wiki_tokens = 27000339

=== Search for external references ===
  [bs8_nmin4_adaptive_seed42] '986': ...ed42.log", "metrics": {"holdout_ppl": 17.650425404986372, "owt_ppl": 18.332103963757113, "wiki_ppl":...
  [adaptive_ood_seed456] '986': ...eed456.log", "submitted_at": "2026-05-19t14:37:05.986z", "submitted_via": "submit_training_job", "ba...
  [detect_remove_q03_seed42_r2] '986': ...ver": "westd-30476", "gpu": ["cuda:0"], "pid": "59986", "log_path": "~/runs/provenance_weight_traini...
  [batchsize16_nmin8_seed42] '986': ..."reproduce": {"finished_at": "2026-05-17t14:13:27.986z"}, "failure_reason": "process dead 5\u00d7 wi...
  [random_reweight_seed42] '150m': ...u6761\u975etraining\u3002wandb_mode=offline\u5199~150mb\u523030gb\u6839\u5206\u533a\u2192\u78c1\u76d...
  [detector_modernbert] 'modernbert': ...:50.219z", "conclusion": "killed", "hypothesis": "modernbert-base can distinguish qwen3-0.6b synthet...
  [detector_tfidf_lr] 'modernbert': ...for provenance weighting, replacing over-accurate modernbert (d007)", "metrics": {"auc": 0.939, "acc...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "98f521da-c153-449c-b096-94d2187797d8"
}
```

</details>

---


### System

_source line 111_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Search for Pearson 0.79, constraint binding, 5.9x in all experiment text",
  "usage": {
    "total_tokens": 65501,
    "tool_uses": 30,
    "duration_ms": 518117
  },
  "last_tool_name": "Bash",
  "uuid": "d021a0a3-1614-472d-a6bf-eb1864279a43",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Bash · `toolu_01DRXKQo2LnhyhGyE5btGiXv`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Let me now verify Pearson r ≈ 0.79 and ~50% constraint binding and ~5.9× sharpening\n# These might be in experiment notes or conclusions, not structured metrics\n\n# Search full text for 0.79\nprint(\"=== SEARCH for 0.79 in all text ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp)\n    if '0.79' in full_str:\n        idx = full_str.find('0.79')\n        print(f\"  [{eid}]: ...{full_str[max(0,idx-100):idx+100]}...\")\n\n# Search for \"5.9\"\nprint(\"\\n=== SEARCH for '5.9x' or 'fold' ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp).lower()\n    if '5.9' in full_str and ('fold' in full_str or 'lower' in full_str or 'times' in full_str):\n        print(f\"  [{eid}]: found\")\n\n# Search for constraint binding percentage\nprint(\"\\n=== SEARCH for constraint binding ===\")\nfor eid, exp in exps.items():\n    full_str = json.dumps(exp).lower()\n    if 'bind' in full_str or 'binding' in full_str or 'quality constraint' in full_str:\n        idx = -1\n        for term in ['bind', 'binding', 'quality constraint']:\n            if term in full_str:\n                idx = full_str.find(term)\n                break\n        if idx >= 0:\n            print(f\"  [{eid}]: ...{full_str[max(0,idx-80):idx+80]}...\")\n\n# Check alpha_eff_pct_at_max for ~50% constraint binding\nprint(\"\\n=== alpha_eff_pct_at_max ===\")\nfor eid, exp in exps.items():\n    m = exp.get('metrics', {})\n    pct = m.get('alpha_eff_pct_at_max')\n    if pct:\n        print(f\"  {eid}: alpha_eff_pct_at_max={pct}\")\nPYEOF",
  "description": "Search for Pearson 0.79, constraint binding, 5.9x in all experiment text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "deb38569-ab99-4c5e-b1b5-7f73901712a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjNe7vprFa21VZx5e5g1QW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1472,
      "cache_read_input_tokens": 62948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1472,
        "ephemeral_1h_input_tokens": 0
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

_source line 113 · 2026-05-25T19:51:23.919Z_

<details><summary>↩ Tool result · `toolu_01DRXKQo2LnhyhGyE5btGiXv`</summary>

```text
=== SEARCH for 0.79 in all text ===

=== SEARCH for '5.9x' or 'fold' ===
  [grid_b0_1_seed42]: found

=== SEARCH for constraint binding ===
  [ess_only_seed123]: ...e (max-intervention) seed=123: b* = max{b : ess(b) >= n_min} ignores \u03b1_eff quality constraint, applying strongest possible downweighting. multi-seed valida...
  [tau_095_seed42]: ...wing downweighting, which should collapse b* toward near-max values (overfit to quality constraint) and degrade ppl toward ess-only levels (~17.72), confirming ...

=== alpha_eff_pct_at_max ===
  rho02_adaptive_tau09_r5: alpha_eff_pct_at_max=42.95
  bs8_auto_nmin_r5: alpha_eff_pct_at_max=38.88
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "39f6e0b5-e059-4422-946e-fc0c31f78048"
}
```

</details>

---


### System

_source line 114_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check tau_07_seed42 and grid_b0_1 for detailed metrics",
  "usage": {
    "total_tokens": 66610,
    "tool_uses": 31,
    "duration_ms": 528992
  },
  "last_tool_name": "Bash",
  "uuid": "c6dc3018-332e-48a0-8450-aa31bd826c13",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — Bash · `toolu_015BUQk5Aahw8EBkLtjLaEhq`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# The alpha_eff_pct_at_max values are 42.95% and 38.88%, but those are for rho=0.2 and bs8 configs\n# Not the main tau=0.7 rho=0.4 configuration\n\n# Paper says \"~50% of batches where quality constraint binds\"\n# The registry doesn't have this exact metric for the main config\n# But ~50% is plausible given the range (39-43% found for other configs)\n\n# Let me check if there are any experiments that have pct_at_max for tau=0.7 rho=0.4\n# or check the tau_07_seed42 experiment for any constraint data\nprint(\"=== tau_07_seed42 full metrics ===\")\nm = exps['tau_07_seed42'].get('metrics', {})\nprint(json.dumps(m, indent=2))\n\nprint(\"\\n=== bs8_nmin4_adaptive_seed42 full metrics ===\")\nm = exps['bs8_nmin4_adaptive_seed42'].get('metrics', {})\nprint(json.dumps(m, indent=2)[:1000])\n\n# Also check grid_b0_1_seed42 for the 5.9x reference\nprint(\"\\n=== grid_b0_1_seed42 notes/hypothesis ===\")\nexp = exps['grid_b0_1_seed42']\nprint(f\"hypothesis: {exp.get('hypothesis', '')[:500]}\")\nprint(f\"notes: {exp.get('notes', '')[:500]}\")\nPYEOF",
  "description": "Check tau_07_seed42 and grid_b0_1 for detailed metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "916e10aa-9f99-42fd-ad70-ae071db5b3ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144dDnNvYLbikQTCKEQQ3Fu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 64420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
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

_source line 116 · 2026-05-25T19:51:34.718Z_

<details><summary>↩ Tool result · `toolu_015BUQk5Aahw8EBkLtjLaEhq`</summary>

```text
=== tau_07_seed42 full metrics ===
{
  "train_loss": 9.6707,
  "total_steps": 6103,
  "train_runtime_s": 15065,
  "train_samples_per_second": 6.482,
  "eval_ppl_holdout": 17.6793,
  "eval_loss": 2.8724,
  "eval_holdout_tokens": 4077068,
  "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)",
  "eval_note": "unified post-hoc eval 2026-05-15",
  "b_star_count": 24412,
  "b_star_mean": 0.8943,
  "b_star_median": 0.58,
  "b_star_std": 1.4007,
  "b_star_min": 0,
  "b_star_max": 20,
  "b_star_p25": 0.3306,
  "b_star_p75": 0.9712,
  "b_star_pct_zero": 5.8,
  "b_star_pct_below_0.5": 36,
  "b_star_pct_0.5_to_1": 34.2,
  "b_star_pct_1_to_2": 16.2,
  "b_star_pct_above_2": 7.7
}

=== bs8_nmin4_adaptive_seed42 full metrics ===
{
  "holdout_ppl": 17.650425404986372,
  "owt_ppl": 18.332103963757113,
  "wiki_ppl": 15.318017946105257,
  "holdout_loss": 2.8707598853543677,
  "owt_loss": 2.908653837793633,
  "wiki_loss": 2.729029779056454
}

=== grid_b0_1_seed42 notes/hypothesis ===
hypothesis: Grid-b sweep b=0.1 on ρ=0.4 data, seed42. Minimal reweighting — expect PPL close to uniform (~17.694). Establishes lower bound of useful b range.
notes: PPL=17.657, between uniform(17.694) and b=0.3(17.640). b=0.1 provides minimal but positive improvement over uniform, consistent with near-uniform weighting at low b.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "f676281a-dd49-43b4-b856-eb59f9268ed8"
}
```

</details>

---


### System

_source line 117_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check ESS-only b_star details for 5.9x ratio",
  "usage": {
    "total_tokens": 67899,
    "tool_uses": 32,
    "duration_ms": 551172
  },
  "last_tool_name": "Bash",
  "uuid": "98f5d38b-a405-4d35-ae2c-a3f712606640",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 118_

<details open><summary>🔧 Tool call — Bash · `toolu_01XH6YeKWT7o9kFohDdRu8N6`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Pearson r ≈ 0.79 for alpha_eff correlation - not found in registry\n# This is likely computed from analysis code, not stored in experiments\n\n# ~50% constraint binding - alpha_eff_pct_at_max closest values are ~39-43%\n# But tau_07_seed42 doesn't have this metric directly\n# The paper says ~50%, which is not directly verifiable from registry\n\n# ~5.9× lower sharpening exponents\n# ESS-only b_star_mean ≈ 3.53\n# tau_07 b_star_mean = 0.8943\n# ratio = 3.53 / 0.8943 ≈ 3.95 (not 5.9)\n# \n# Or nmin1 b_star_mean = 7.197, vs tau=0.7 = 0.8943 → 7.197/0.8943 = 8.05 (not 5.9)\n# \n# Let me check what the comparison might be. Maybe ESS-only median vs adaptive median?\n# Or maybe tau=0.8 vs tau=0.7?\n\n# Actually, let me check ess_only more carefully\nprint(\"=== ess_only_seed42 full metrics ===\")\nm = exps['ess_only_seed42'].get('metrics', {})\nprint(json.dumps(m, indent=2))\n\nprint(\"\\n=== ess_only_seed123 full metrics ===\")\nm = exps['ess_only_seed123'].get('metrics', {})\nprint(json.dumps(m, indent=2))\n\n# Maybe the 5.9x is comparing ess_only b_star_mean vs adaptive b_star for rho=0.6?\n# Or the ratio of b_star at rho=0.2?\n# rho02_adaptive_tau09_r5: b_star_mean=4.3493\n# vs tau_07 b_star_mean=0.8943\n# 4.3493/0.8943 = 4.86 (not 5.9)\n\n# Or maybe nmin1 b_star_mean=7.197 vs adaptive_fix b_star_mean=1.42\n# 7.197/1.42 = 5.07 (close but not 5.9)\n\n# Let me try ESS-only b_star_mean (3.53) vs adaptive tau=0.8 b_star\n# adaptive_seed42 says b_star range 0.0-3.8 but no mean\n# adaptive_fix b_star_mean ≈ 1.42\n# 3.53/0.6 = 5.88 ≈ 5.9 (if comparing ESS-only mean to some adaptive median)\n\n# tau_07 b_star_median = 0.58\n# ess_only mean/median?\nprint(\"\\n=== ess_only_seed42 b_star details ===\")\nfor k, v in m.items():\n    if 'b_star' in k:\n        print(f\"  {k} = {v}\")\n\n# Let me compute: ess_only b_star_mean / tau_07 b_star_median\n# 3.51 / 0.58 = 6.05 ≈ 5.9? Close but we don't have ESS-only median\nPYEOF",
  "description": "Check ESS-only b_star details for 5.9x ratio"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "d7d33634-0297-406d-af0d-37b9674ed19c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wkz7eETvpjzYZ7DGnortij",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1251,
      "cache_read_input_tokens": 65463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1251,
        "ephemeral_1h_input_tokens": 0
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

_source line 119 · 2026-05-25T19:51:56.888Z_

<details><summary>↩ Tool result · `toolu_01XH6YeKWT7o9kFohDdRu8N6`</summary>

```text
=== ess_only_seed42 full metrics ===
{
  "eval_ppl": 17.73,
  "eval_loss": 2.875,
  "b_star_median": 1.58,
  "b_star_mean": 3.51,
  "vs_uniform_ppl_delta": "+0.038",
  "vs_adaptive_ppl_delta": "+0.08"
}

=== ess_only_seed123 full metrics ===
{
  "eval_ppl_holdout": 17.72,
  "eval_loss_holdout": 2.8746,
  "eval_holdout_tokens": 4077068,
  "eval_method": "eval_perplexity.py on data/human/eval_holdout.jsonl, max_docs=5000, stride=1024, fp16",
  "eval_note": "Also ran on scored_data.jsonl (train data): ppl=9.66, loss=2.2677, tokens=3029693",
  "train_loss": 10.2159,
  "train_steps": 6103,
  "train_runtime_seconds": 12959.5,
  "b_star_mean": 3.55,
  "b_star_median": 1.5918,
  "b_star_std": 4.7209,
  "b_star_min": 0.2344,
  "b_star_max": 20,
  "b_star_p25": 0.8398,
  "b_star_p75": 3.8281,
  "b_star_p90": 9.5996,
  "b_star_count": 21971,
  "vs_uniform_ppl_delta": "+0.034",
  "vs_adaptive_fix_ppl_delta": "+0.077"
}

=== ess_only_seed42 b_star details ===
  b_star_mean = 3.55
  b_star_median = 1.5918
  b_star_std = 4.7209
  b_star_min = 0.2344
  b_star_max = 20
  b_star_p25 = 0.8398
  b_star_p75 = 3.8281
  b_star_p90 = 9.5996
  b_star_count = 21971
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "ebd258a8-2ae8-4a5b-a0ef-ca01a411bf01"
}
```

</details>

---


### System

_source line 120_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check rho=0.6 b_star values and contamination_60 metrics",
  "usage": {
    "total_tokens": 69600,
    "tool_uses": 33,
    "duration_ms": 572785
  },
  "last_tool_name": "Bash",
  "uuid": "82daba38-49a6-4232-8029-7a3d25d5083b",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Bash · `toolu_018ACyjCc3M4iD3idEsJNqaE`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# 5.9x calculation:\n# ESS-only b_star_mean ≈ 3.53 (avg of 3.51, 3.55)\n# tau=0.7 b_star_mean = 0.8943\n# ratio: 3.53 / 0.8943 = 3.95 (not 5.9)\n\n# ESS-only b_star_median ≈ 1.59\n# tau=0.7 b_star_median = 0.58\n# ratio: 1.59 / 0.58 = 2.74 (not 5.9)\n\n# Or maybe comparing vs nmin=1:\n# nmin1 b_star_mean = 7.197\n# tau=0.7 + quality constraint: need to check what comparison\n# 7.197 / adaptive_fix_mean ≈ 7.197/1.42 = 5.07\n\n# Or maybe nmin=1 b_star_mean / tau=0.7 b_star_mean... \n# But b_star of tau=0.7 WITH quality constraint is:\n# tau_07_seed42 b_star_mean = 0.8943 (this HAS quality constraint)\n# nmin1 (no quality constraint effectively): b_star_mean = 7.197 \n# But nmin1 also has quality constraint, just n_min=1\n\n# Actually maybe comparing ESS-only vs dual-constraint:\n# ESS-only: b_star_mean = 3.53\n# Dual constraint tau=0.7: b_star_mean = 0.8943  \n# But 3.53/0.8943 = 3.95\n\n# Or comparing specific percentile? Let me check:\n# ESS-only p90 = 9.5996\n# tau=0.7: doesn't have p90 but max=20\n# That doesn't help\n\n# Let me look at it differently: maybe the paper computes median b* \n# for batches where quality constraint BINDS vs not\n# Or the 5.9x might be explained elsewhere\n\n# Let me check the rho=0.6 experiments for b_star\nprint(\"=== rho=0.6 adaptive b_star ===\")\nfor eid in ['adaptive_rho06_tau07_seed42', 'adaptive_rho06_tau07_seed123', 'adaptive_rho06_tau07_seed456']:\n    m = exps.get(eid, {}).get('metrics', {})\n    for k, v in m.items():\n        if 'b_star' in k or 'b_' in k:\n            print(f\"  {eid}.{k} = {v}\")\n\n# Also check contamination_60 tau07\nprint(\"\\n=== contamination_60_tau07_seed42 full metrics ===\")\nm = exps['contamination_60_tau07_seed42'].get('metrics', {})\nprint(json.dumps(m, indent=2))\n\n# And batch_adaptive_tau_rho06\nfor eid in ['batch_adaptive_tau_rho06_seed42', 'batch_adaptive_tau_rho06_r2', 'batch_adaptive_tau_rho06_r3',\n            'batch_adaptive_tau_rho06_r5']:\n    exp = exps.get(eid, {})\n    m = exp.get('metrics', {})\n    for k, v in m.items():\n        if 'b_star' in k:\n            print(f\"  {eid}.{k} = {v}\")\nPYEOF",
  "description": "Check rho=0.6 b_star values and contamination_60 metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "b4c3bbbe-c293-4e16-8ec7-54d72cc6533c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SvZYe9chZeC1woYbYfbHFX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1663,
      "cache_read_input_tokens": 66714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1663,
        "ephemeral_1h_input_tokens": 0
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

_source line 122 · 2026-05-25T19:52:18.505Z_

<details><summary>↩ Tool result · `toolu_018ACyjCc3M4iD3idEsJNqaE`</summary>

```text
=== rho=0.6 adaptive b_star ===

=== contamination_60_tau07_seed42 full metrics ===
{
  "eval_ppl_holdout": 17.73,
  "eval_loss_holdout": 2.875,
  "eval_holdout_tokens": 4077068,
  "train_loss": 9.358,
  "eval_method": "eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "9f75945d-7010-4242-8016-5d6ff407142d"
}
```

</details>

---


### System

_source line 123_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Final search for 5.9x, 0.79, 50% constraint in notes",
  "usage": {
    "total_tokens": 70885,
    "tool_uses": 34,
    "duration_ms": 591554
  },
  "last_tool_name": "Bash",
  "uuid": "48328e72-0e69-443c-a7d1-7b3ef30601d7",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 124_

<details open><summary>🔧 Tool call — Bash · `toolu_0137GgmAGfDDSAS8zXMN6Uv5`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Let me check the contamination_60 ess_only experiments for b_star \n# to compute the 5.9x at rho=0.6\nprint(\"=== contamination_60_ess_only_seed42 full metrics ===\")\nm = exps['contamination_60_ess_only_seed42'].get('metrics', {})\nprint(json.dumps(m, indent=2))\n\n# Also check rho02_adaptive_tau09_r5 vs rho02 tau08\nprint(\"\\n=== rho02_adaptive_tau09_r5 full ===\")\nm = exps['rho02_adaptive_tau09_r5'].get('metrics', {})\nprint(json.dumps(m, indent=2))\n\n# The 5.9x and 0.79 and ~50% numbers might be from analysis scripts, not registry\n# These could be computed from training logs rather than stored in experiment metadata\n\n# Let me do a final comprehensive search for these specific values in all notes/conclusions\nprint(\"\\n=== Search for specific derived values in notes/conclusions ===\")\nfor eid, exp in exps.items():\n    notes = str(exp.get('notes', ''))\n    conclusion = str(exp.get('conclusion', ''))\n    hypothesis = str(exp.get('hypothesis', ''))\n    all_text = notes + conclusion + hypothesis\n    \n    if '5.9' in all_text:\n        print(f\"  [{eid}] '5.9' in text: {all_text[:200]}\")\n    if '0.79' in all_text:\n        print(f\"  [{eid}] '0.79' in text: {all_text[:200]}\")\n    if '50%' in all_text and 'constraint' in all_text.lower():\n        print(f\"  [{eid}] '50% constraint' in text: {all_text[:200]}\")\nPYEOF",
  "description": "Final search for 5.9x, 0.79, 50% constraint in notes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "25604cce-9194-4fab-ada2-642317d16e77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wJ7Sr9cXC89rBVtCqmtNK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1247,
      "cache_read_input_tokens": 68377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1247,
        "ephemeral_1h_input_tokens": 0
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

_source line 125 · 2026-05-25T19:52:37.269Z_

<details><summary>↩ Tool result · `toolu_0137GgmAGfDDSAS8zXMN6Uv5`</summary>

```text
=== contamination_60_ess_only_seed42 full metrics ===
{
  "eval_ppl_holdout": 17.77,
  "eval_loss_holdout": 2.8775,
  "eval_holdout_tokens": 4077068,
  "train_loss": 9.842,
  "total_steps": 6103,
  "train_runtime_seconds": 13152
}

=== rho02_adaptive_tau09_r5 full ===
{
  "eval_ppl_holdout": 17.45,
  "eval_loss_holdout": 2.8593,
  "eval_holdout_tokens": 4077068,
  "train_loss": 11.864,
  "epoch": 0.47,
  "b_star_mean": 4.3493,
  "b_star_median": 2.9609,
  "b_star_std": 4.3982,
  "b_star_min": 0,
  "b_star_max": 20,
  "b_star_pct_zero": 2.65,
  "alpha_eff_mean": 0.8277,
  "alpha_eff_median": 0.8826,
  "alpha_eff_pct_at_max": 42.95,
  "ess_mean": 2.3784,
  "ess_median": 2.0121
}

=== Search for specific derived values in notes/conclusions ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "dd223cf8-6431-403d-bc58-a705aef2edb9"
}
```

</details>

---


### System

_source line 126_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check baseline experiment and registry metadata",
  "usage": {
    "total_tokens": 71999,
    "tool_uses": 35,
    "duration_ms": 598415
  },
  "last_tool_name": "Bash",
  "uuid": "8485be74-f0ae-4a62-8e0c-c9d9b0bc0cf0",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 127_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wr9teqskpcCZ7FyDGNCkqe`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Let me now look at qwen06b_uniform_seed42 and baseline_qwen3_0.6b for model info\nprint(\"=== baseline_qwen3_0.6b ===\")\nexp = exps['baseline_qwen3_0.6b']\nprint(json.dumps(exp, indent=2)[:2000])\n\n# Also check the metadata field\nprint(\"\\n=== Registry metadata ===\")\nmeta = result.get('metadata', {})\nprint(json.dumps(meta, indent=2)[:2000])\n\n# Check if there's a 'count' and 'total' field\nprint(f\"\\ncount: {result['data'].get('count')}\")\nprint(f\"total: {result['data'].get('total')}\")\nPYEOF",
  "description": "Check baseline experiment and registry metadata"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "fd95a931-61bb-4ff3-8dea-d7ba2bea12d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQ2Yy9NPoSzVA2rHpYAqLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 69624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
        "ephemeral_1h_input_tokens": 0
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

_source line 128 · 2026-05-25T19:52:44.143Z_

<details><summary>↩ Tool result · `toolu_01Wr9teqskpcCZ7FyDGNCkqe`</summary>

```text
=== baseline_qwen3_0.6b ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T21:53:53.450Z",
  "updated_at": "2026-05-15T21:54:29.041Z",
  "spec": {
    "command": "CUDA_VISIBLE_DEVICES=3 python eval_perplexity.py --checkpoints models/Qwen/Qwen3-0.6B --data_path data/human/eval_holdout.jsonl --max_docs 5000",
    "server": "westd-47453",
    "data_path": "data/human/eval_holdout.jsonl",
    "data_count": 5000,
    "model_name": "Qwen3-0.6B",
    "seed": 0,
    "checkpoint_source": "models/Qwen/Qwen3-0.6B",
    "eval_data": "data/human/eval_holdout.jsonl",
    "checkpoint_path": "models/Qwen/Qwen3-0.6B",
    "log_path": "/root/runs/provenance_weight_training/qwen3_0.6b_baseline_eval.log"
  },
  "checkpoint_path": "models/Qwen/Qwen3-0.6B",
  "log_path": "/root/runs/provenance_weight_training/qwen3_baseline_eval.log",
  "conclusion": "success",
  "completed_at": "2026-05-15T21:54:15.419Z",
  "hypothesis": "Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute improvement from training.",
  "metrics": {
    "eval_ppl_holdout": 22.97,
    "eval_loss": 3.134,
    "eval_holdout_tokens": 4077068,
    "eval_method": "sliding_window_stride1024_maxlen2048_fp16"
  },
  "notes": "Baseline PPL=22.9654 (loss=3.1340), tokens=4,077,068, time=249s. Weight SHA256=f47f71177f32bcd101b7573ec9171e6a57f4f4d31148d38e382306f42996874b. Pretrained weights confirmed (std ~0.02-0.03, layernorm varies across layers). Compared to ess_only_seed456 PPL=17.72: continued pretraining reduces PPL by 22.8%."
}

=== Registry metadata ===
{
  "elapsed_seconds": 1.3498
}

count: 269
total: 269
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "63a00e0e-6662-490f-a0d1-08cfd1b4aef9"
}
```

</details>

---


### System

_source line 129_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Compile final audit summary",
  "usage": {
    "total_tokens": 73145,
    "tool_uses": 36,
    "duration_ms": 635691
  },
  "last_tool_name": "Bash",
  "uuid": "c02f9a1e-4862-4e2c-945e-57369e8f3659",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 130_

<details open><summary>🔧 Tool call — Bash · `toolu_01Dwj3nENdrXmYUaWTFwdAxt`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Summary of verification:\n# Let me now compile the complete audit\n\nprint(\"=\" * 80)\nprint(\"FINAL AUDIT SUMMARY\")\nprint(\"=\" * 80)\n\n# 1. Adaptive tau=0.7 5-seed mean holdout PPL: 17.674\na5 = [17.68, 17.666, 17.677, 17.678, 17.668]\nprint(f\"\\n1. Adaptive tau=0.7 5-seed mean: paper=17.674, computed={sum(a5)/5:.3f}\")\nprint(f\"   Seeds: tau07_seed42=17.68, tau07_seed123=17.666, tau07_seed456=17.677,\")\nprint(f\"          adaptive_seed234=17.678, adaptive_seed789=17.668\")\n\n# 2. Uniform 5-seed mean: 17.694\nu5 = [17.6939, 17.6861, 17.7015, 17.708, 17.695]\nu3 = [17.6939, 17.6861, 17.7015]\nprint(f\"\\n2. Uniform baseline mean: paper=17.694\")\nprint(f\"   3-seed mean (42,123,456) = {sum(u3)/3:.3f} MATCHES\")\nprint(f\"   5-seed mean (all) = {sum(u5)/5:.3f} DOES NOT MATCH\")\nprint(f\"   ISSUE: paper says '5-seed' but 17.694 is the 3-seed value\")\n\n# 3. D&R q>0.7 3-seed PPL: 17.250\nprint(f\"\\n3. D&R PPL 17.250 (paper says 'D&R q>0.7')\")\nprint(f\"   Registry D&R q>0.7 3-seed mean = 17.320 (MISMATCH)\")\nprint(f\"   Registry D&R q>0.3 3-seed mean = 17.250 (MATCHES this threshold)\")\nprint(f\"   ISSUE: 17.250 belongs to q>0.3, NOT q>0.7\")\n\n# 4. Delta = -0.023 at rho=0.4\nprint(f\"\\n4. Delta = -0.023 at rho=0.4\")\nprint(f\"   adaptive_5seed - uniform_5seed = {sum(a5)/5 - sum(u5)/5:.3f} MATCHES\")\nprint(f\"   But note: this uses 5-seed uniform (17.697), contradicting paper's 17.694 for uniform\")\n\n# 5. Delta = -0.032 at rho=0.6\nr6a = [17.735, 17.727, 17.732]\nr6u = [17.766, 17.754, 17.770]\nprint(f\"\\n5. Delta = -0.032 at rho=0.6\")\nprint(f\"   adaptive 3-seed mean = {sum(r6a)/3:.3f}\")\nprint(f\"   uniform 3-seed mean = {sum(r6u)/3:.3f}\")\nprint(f\"   delta = {sum(r6a)/3 - sum(r6u)/3:.3f} MATCHES\")\n\n# 6. Epoch-matched gap = 0.017\ndr_em = [17.65053, 17.6591, 17.66]\nprint(f\"\\n6. Epoch-matched gap = 0.017\")\nprint(f\"   D&R epoch-matched mean (q<=0.5) = {sum(dr_em)/3:.3f}\")\nprint(f\"   adaptive tau=0.7 mean = 17.674\")\nprint(f\"   gap = {17.674 - sum(dr_em)/3:.3f} MATCHES\")\n\n# 7. >95% from multi-epoch\nprint(f\"\\n7. >95% from multi-epoch\")\nprint(f\"   Original D&R advantage: 17.674 - 17.320 = 0.354\")\nprint(f\"   Epoch-matched residual: 0.017\")\nprint(f\"   Multi-epoch explains: {(0.354-0.017)/0.354*100:.1f}% MATCHES (>95%)\")\n\n# 8. Detector AUC = 0.94\nprint(f\"\\n8. AUC = 0.94\")\nprint(f\"   Registry: detector_tfidf_lr.auc = 0.939\")\nprint(f\"   0.939 rounds to 0.94: MATCH (rounding)\")\n\n# 9. ECE = 0.048\nprint(f\"\\n9. ECE = 0.048\")\nprint(f\"   Registry: detector_tfidf_lr.ece_calibrated = 0.048 EXACT MATCH\")\n\n# 10. 132M tokens\nprint(f\"\\n10. 132M tokens\")\nprint(f\"    Registry: datagen_synthetic_4gpu.total_tokens = 132033764 MATCH\")\n\n# 11. 371,499 samples\nprint(f\"\\n11. 371,499 samples\")\nprint(f\"    Registry: adaptive_seed42.spec.data_count = 371499 EXACT MATCH\")\n\n# 12. rho = 0.4\nprint(f\"\\n12. rho = 0.4\")\nprint(f\"    Registry: contamination_ratio = 0.4 in commands MATCH\")\n\n# 13. Qwen3-0.6B\nprint(f\"\\n13. Qwen3-0.6B\")\nprint(f\"    Registry: model_name = Qwen/Qwen3-0.6B MATCH\")\n\n# 14. Pearson r ≈ 0.79\nprint(f\"\\n14. Pearson r ≈ 0.79 for alpha_eff correlation\")\nprint(f\"    NOT IN REGISTRY (derived from analysis scripts)\")\n\n# 15. ~50% constraint binding\nprint(f\"\\n15. ~50% constraint binding\")\nprint(f\"    NOT IN REGISTRY for main config. alpha_eff_pct_at_max=42.95 (rho=0.2 config)\")\n\n# 16. ~5.9x lower sharpening\nprint(f\"\\n16. ~5.9x lower sharpening exponents\")\nprint(f\"    NOT DIRECTLY IN REGISTRY. ESS-only b_star_mean=3.53, tau=0.7 b_star_mean=0.89\")\nprint(f\"    Ratio = {3.53/0.8943:.1f}x (not 5.9x)\")\n\n# 17. p_BH = 0.011\nprint(f\"\\n17. p_BH = 0.011 for adaptive tau=0.7\")\nprint(f\"    NOT IN REGISTRY (derived). Raw paired t-test p=0.0012\")\n\n# 18. p_BH = 0.064\nprint(f\"\\n18. p_BH = 0.064 for rho=0.6 adaptive\")\nprint(f\"    NOT IN REGISTRY (derived). Raw paired t-test p=0.0099\")\n\n# 19. SD = 0.006\nimport statistics\nprint(f\"\\n19. SD = 0.006 for adaptive tau=0.7\")\nprint(f\"    Computed from 5-seed PPLs: SD = {statistics.stdev(a5):.4f}\")\nprint(f\"    Rounds to 0.006: MATCH\")\nPYEOF",
  "description": "Compile final audit summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "6bff4224-1cfb-444a-a69d-9724d5506470",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpYB3d3GxtKHeRgHwJvnT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 70700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
        "ephemeral_1h_input_tokens": 0
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

_source line 131 · 2026-05-25T19:53:21.423Z_

<details><summary>↩ Tool result · `toolu_01Dwj3nENdrXmYUaWTFwdAxt`</summary>

```text
================================================================================
FINAL AUDIT SUMMARY
================================================================================

1. Adaptive tau=0.7 5-seed mean: paper=17.674, computed=17.674
   Seeds: tau07_seed42=17.68, tau07_seed123=17.666, tau07_seed456=17.677,
          adaptive_seed234=17.678, adaptive_seed789=17.668

2. Uniform baseline mean: paper=17.694
   3-seed mean (42,123,456) = 17.694 MATCHES
   5-seed mean (all) = 17.697 DOES NOT MATCH
   ISSUE: paper says '5-seed' but 17.694 is the 3-seed value

3. D&R PPL 17.250 (paper says 'D&R q>0.7')
   Registry D&R q>0.7 3-seed mean = 17.320 (MISMATCH)
   Registry D&R q>0.3 3-seed mean = 17.250 (MATCHES this threshold)
   ISSUE: 17.250 belongs to q>0.3, NOT q>0.7

4. Delta = -0.023 at rho=0.4
   adaptive_5seed - uniform_5seed = -0.023 MATCHES
   But note: this uses 5-seed uniform (17.697), contradicting paper's 17.694 for uniform

5. Delta = -0.032 at rho=0.6
   adaptive 3-seed mean = 17.731
   uniform 3-seed mean = 17.763
   delta = -0.032 MATCHES

6. Epoch-matched gap = 0.017
   D&R epoch-matched mean (q<=0.5) = 17.657
   adaptive tau=0.7 mean = 17.674
   gap = 0.017 MATCHES

7. >95% from multi-epoch
   Original D&R advantage: 17.674 - 17.320 = 0.354
   Epoch-matched residual: 0.017
   Multi-epoch explains: 95.2% MATCHES (>95%)

8. AUC = 0.94
   Registry: detector_tfidf_lr.auc = 0.939
   0.939 rounds to 0.94: MATCH (rounding)

9. ECE = 0.048
   Registry: detector_tfidf_lr.ece_calibrated = 0.048 EXACT MATCH

10. 132M tokens
    Registry: datagen_synthetic_4gpu.total_tokens = 132033764 MATCH

11. 371,499 samples
    Registry: adaptive_seed42.spec.data_count = 371499 EXACT MATCH

12. rho = 0.4
    Registry: contamination_ratio = 0.4 in commands MATCH

13. Qwen3-0.6B
    Registry: model_name = Qwen/Qwen3-0.6B MATCH

14. Pearson r ≈ 0.79 for alpha_eff correlation
    NOT IN REGISTRY (derived from analysis scripts)

15. ~50% constraint binding
    NOT IN REGISTRY for main config. alpha_eff_pct_at_max=42.95 (rho=0.2 config)

16. ~5.9x lower sharpening exponents
    NOT DIRECTLY IN REGISTRY. ESS-only b_star_mean=3.53, tau=0.7 b_star_mean=0.89
    Ratio = 3.9x (not 5.9x)

17. p_BH = 0.011 for adaptive tau=0.7
    NOT IN REGISTRY (derived). Raw paired t-test p=0.0012

18. p_BH = 0.064 for rho=0.6 adaptive
    NOT IN REGISTRY (derived). Raw paired t-test p=0.0099

19. SD = 0.006 for adaptive tau=0.7
    Computed from 5-seed PPLs: SD = 0.0063
    Rounds to 0.006: MATCH
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "32efc8de-e33f-4f00-837d-5b6b105b3fdb"
}
```

</details>

---


### System

_source line 132_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "description": "Running Check remaining external numbers and verify details",
  "usage": {
    "total_tokens": 76254,
    "tool_uses": 37,
    "duration_ms": 658725
  },
  "last_tool_name": "Bash",
  "uuid": "58e7f76d-f392-4f4d-8be7-b9f9921cce9d",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool call

_source line 133_

<details open><summary>🔧 Tool call — Bash · `toolu_018WrTb3QGm3vr8xR2zJzSSR`</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779738138900.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Check for ModernBERT-150M, WikiText-2, Drayson, golden ratio in any experiment\n# These are likely from cited papers, not from the registry\n\n# Golden ratio: check golden_ratio_seed42\nexp = exps['golden_ratio_seed42']\nhyp = exp.get('hypothesis', '')\nprint(f\"Golden ratio hypothesis: {hyp}\")\n# It says w=1/φ≈0.618 - so 0.62 is a rounded form of 0.618\n\n# Check detector_modernbert hypothesis for AUC=0.986\nexp = exps['detector_modernbert']\nprint(f\"\\nModernBERT hypothesis: {exp.get('hypothesis', '')}\")\n# \"ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human text with AUC>=0.95 and ECE<=0.05\"\n# No AUC=0.986 here. This is from a related work citation.\n\n# Let me also double-check the D&R claim. The user said paper says \"D&R q>0.7\"\n# Let me check if maybe the paper actually says \"D&R (best threshold)\" or just \"D&R\"\n# I can't verify without reading the paper itself, but the registry data is clear:\n# q>0.7 PPL = 17.32, q>0.3 PPL = 17.25\n\n# Also verify that the D&R 3-seed value of 17.320 is consistent\n# detect_remove_q07_seed42_r3=17.32, seed123=17.32, seed456=17.32\n# These are all exactly 17.32 (rounded) - very consistent\n\n# Let me also verify the D&R PPL = 17.250 calculation more precisely\ndr_q03 = [17.25, 17.25, 17.2509]\nprint(f\"\\nD&R q>0.3 3-seed mean exact: {sum(dr_q03)/3:.4f}\")\nprint(f\"D&R q>0.3 3-seed mean rounded: {sum(dr_q03)/3:.3f}\")\n\n# Check the inconsistency about uniform 5-seed more carefully\n# Maybe uniform_seed234 and uniform_seed789 have different holdout_ppl values\nprint(\"\\n=== uniform_seed234 all metrics ===\")\nprint(json.dumps(exps['uniform_seed234'].get('metrics', {}), indent=2))\nprint(\"\\n=== uniform_seed789 all metrics ===\")\nprint(json.dumps(exps['uniform_seed789'].get('metrics', {}), indent=2))\n\n# These use holdout_ppl (not eval_ppl_holdout)\n# holdout_ppl=17.708 and 17.695\n# While seeds 42/123/456 use eval_ppl_holdout=17.6939/17.6861/17.7015\nPYEOF",
  "description": "Check remaining external numbers and verify details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "64ce1456-4b10-47db-bd81-4c160a291894",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NCvUjBvZoGyS7hmvX7Y3Jv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3105,
      "cache_read_input_tokens": 71808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3105,
        "ephemeral_1h_input_tokens": 0
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

_source line 134 · 2026-05-25T19:53:44.444Z_

<details><summary>↩ Tool result · `toolu_018WrTb3QGm3vr8xR2zJzSSR`</summary>

```text
Golden ratio hypothesis: Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method

ModernBERT hypothesis: ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human text with AUC>=0.95 and ECE<=0.05

D&R q>0.3 3-seed mean exact: 17.2503
D&R q>0.3 3-seed mean rounded: 17.250

=== uniform_seed234 all metrics ===
{
  "holdout_ppl": 17.708,
  "holdout_loss": 2.874,
  "owt_ppl": 18.355,
  "wiki_ppl": 15.352,
  "train_loss": 8.008,
  "train_duration_s": 12780
}

=== uniform_seed789 all metrics ===
{
  "holdout_ppl": 17.695,
  "holdout_loss": 2.8733,
  "owt_ppl": 18.387,
  "wiki_ppl": 15.349,
  "train_loss": 7.959,
  "train_duration_s": 12790
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "d4c29a51-b31b-4683-8f54-753fb0e8c14d"
}
```

</details>

---


### System

_source line 135_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a9d34ba9d381fdded",
  "tool_use_id": "toolu_019aZNmieHiQcRF1tuv1dBPQ",
  "status": "completed",
  "output_file": "",
  "summary": "Audit numbers against registry",
  "usage": {
    "total_tokens": 77645,
    "tool_uses": 37,
    "duration_ms": 711167
  },
  "uuid": "6b5110e9-2cc3-46f8-b042-7e34306a5fc4",
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da"
}
```

---


### Tool result

_source line 136 · 2026-05-25T19:54:36.793Z_

<details><summary>↩ Tool result · `toolu_019aZNmieHiQcRF1tuv1dBPQ`</summary>

```text
Here is the complete audit report.

---

## Audit Results: Paper Numbers vs. Registry

### Experimental PPL Values

**1. Adaptive tau=0.7 5-seed mean holdout PPL: 17.674**
- Registry experiments: `tau07_seed42` (17.68), `tau07_seed123` (17.666), `tau07_seed456` (17.677), `adaptive_seed234` (17.678, tau=0.7 per spec), `adaptive_seed789` (17.668, tau=0.7 per spec)
- Computed 5-seed mean: 17.674
- **Match: YES (exact)**

**2. Uniform baseline 5-seed mean: 17.694**
- Registry experiments: `uniform_seed42` (17.6939), `uniform_seed123` (17.6861), `uniform_seed456` (17.7015), `uniform_seed234` (17.708), `uniform_seed789` (17.695)
- Computed 5-seed mean: **17.697** (not 17.694)
- Computed 3-seed mean (seeds 42/123/456 only): **17.694** (matches)
- **Match: NO -- paper says "5-seed" but 17.694 is the 3-seed value. The 5-seed value is 17.697.**

**3. D&R q>0.7 3-seed PPL: 17.250**
- Registry D&R q>0.7: `detect_remove_q07_seed42_r3` (17.32), `detect_remove_q07_seed123` (17.32), `detect_remove_q07_seed456` (17.32) -- 3-seed mean = **17.320**
- Registry D&R q>0.3: `detect_remove_q03_seed42_r2` (17.25), `detect_remove_q03_seed123` (17.25), `detect_remove_q03_seed456` (17.2509) -- 3-seed mean = **17.250**
- **Match: NO -- 17.250 belongs to D&R q>0.3 (best threshold), NOT q>0.7. D&R q>0.7 gives 17.320. Either the paper mislabels the threshold or the PPL value.**

**4. Delta = -0.023 at rho=0.4**
- Adaptive 5-seed mean (17.674) minus uniform 5-seed mean (17.697) = -0.023
- **Match: YES (using 5-seed uniform = 17.697)**
- Note: This is internally inconsistent with #2 above. The delta -0.023 requires the 5-seed uniform mean (17.697), but the paper reports the uniform mean as 17.694 (which is the 3-seed value and would give delta = -0.020).

**5. Delta = -0.032 at rho=0.6**
- `adaptive_rho06_tau07_seed42/123/456`: 17.735, 17.727, 17.732 -- mean = 17.731
- `contamination_60_uniform_seed42/123/456`: 17.766, 17.754, 17.770 -- mean = 17.763
- Delta = -0.032
- **Match: YES (exact)**

**6. Epoch-matched gap Delta = 0.017**
- D&R epoch-matched 3-seed mean (q<=0.5): `dr_epoch_matched_indep_lr_v2_seed42` (17.65053), `dr_epoch_matched_seed123_r2` (17.6591), `dr_epoch_matched_seed456` (17.66) -- mean = 17.657
- Adaptive tau=0.7 mean: 17.674
- Gap: 17.674 - 17.657 = 0.017
- **Match: YES (exact)**

**7. ">95%" of advantage from multi-epoch**
- Original D&R advantage: 17.674 - 17.320 = 0.354 PPL gap
- Epoch-matched residual: 0.017
- Multi-epoch explains: (0.354 - 0.017) / 0.354 = 95.2%
- **Match: YES (95.2% > 95%)**

### Detector Metrics

**8. AUC = 0.94**
- Registry: `detector_tfidf_lr.auc` = 0.939
- 0.939 rounds to 0.94
- **Match: YES (rounding from 0.939)**

**9. ECE = 0.048**
- Registry: `detector_tfidf_lr.ece_calibrated` = 0.048
- **Match: YES (exact)**

### Data/Model Specs

**10. 132M tokens**
- Registry: `datagen_synthetic_4gpu.spec.total_tokens` = 132,033,764
- **Match: YES**

**11. 371,499 samples**
- Registry: `adaptive_seed42.spec.data_count` = 371,499
- **Match: YES (exact)**

**12. rho = 0.4**
- Registry: `contamination_ratio = 0.4` in experiment commands/metrics
- **Match: YES**

**13. Qwen3-0.6B**
- Registry: `model_name = Qwen/Qwen3-0.6B`
- **Match: YES**

### Method Section

**14. Pearson r approximately 0.79 for alpha_eff correlation**
- **Not in registry.** No experiment stores this value. Likely computed by analysis scripts from training logs, not stored as an experiment metric.

**15. ~50% of batches where quality constraint binds**
- **Not in registry for main config (tau=0.7, rho=0.4).** The closest available metric is `alpha_eff_pct_at_max` = 42.95% for `rho02_adaptive_tau09_r5` (a different configuration). Cannot verify.

**16. ~5.9x lower sharpening exponents**
- **Not directly verifiable from registry.** Available data:
  - ESS-only `b_star_mean` = 3.53 (average of seed42=3.51, seed123=3.55)
  - Tau=0.7 adaptive `b_star_mean` = 0.894 (from `tau_07_seed42`)
  - Ratio: 3.53 / 0.894 = **3.9x** (not 5.9x)
- The 5.9x value cannot be reproduced from the registry's stored b_star_mean values. It may come from a different comparison (e.g., per-sample rather than per-batch means, or a different ablation pair).

### P-values and SD

**17. p_BH = 0.011 for adaptive tau=0.7**
- **Not in registry** (derived statistic). Raw paired t-test from registry PPLs yields p = 0.0012, which with Benjamini-Hochberg correction across multiple tests could yield 0.011. Plausible but not directly verifiable without knowing the full set of tests corrected for.

**18. p_BH = 0.064 for rho=0.6 adaptive**
- **Not in registry** (derived statistic). Raw paired t-test yields p = 0.0099. With BH correction this could yield 0.064. Same caveat as above.

**19. SD = 0.006 for adaptive tau=0.7**
- Computed from 5-seed PPLs: SD = 0.0063
- Rounds to 0.006
- **Match: YES**

### Related Work External Numbers

**20. "20-60% of web corpora" synthetic content** -- Not in registry (external citation claim)

**21. Drayson et al. b=10 for <=360M, b=1 for 1.7B** -- Not in registry (external citation)

**22. ModernBERT-150M detector AUC=0.986** -- Not in registry. `detector_modernbert` was cancelled before running (status: killed, no metrics). This is from a cited paper.

**23. WikiText-2 ~2M tokens** -- Not in registry (general dataset fact)

**24. Golden ratio reciprocal approximately 0.62** -- Registry: `golden_ratio_seed42` uses w=1/phi approx 0.618. Paper rounds to 0.62. **Consistent.**

---

## Key Discrepancies Found

1. **Uniform mean seed count mismatch**: Paper claims "5-seed mean = 17.694" but registry 5-seed mean = 17.697. The value 17.694 is actually the **3-seed** mean (seeds 42, 123, 456). Either the paper should say "3-seed" or update the number to 17.697.

2. **D&R threshold/PPL mismatch**: If the paper says "D&R q>0.7" gives PPL 17.250, this is wrong. Registry shows D&R q>0.7 = 17.320. The PPL 17.250 belongs to D&R q>0.3 (the best threshold). Either the threshold label or the PPL value needs correction.

3. **Internal inconsistency between uniform mean and delta**: The delta = -0.023 at rho=0.4 is correct when computed from 5-seed uniform (17.697), but the paper simultaneously reports the uniform mean as 17.694 (3-seed value). If uniform were truly 17.694, the delta would be -0.020, not -0.023.

4. **~5.9x sharpening ratio not reproducible**: From registry b_star_mean values, the ESS-only vs. dual-constraint ratio is ~3.9x, not 5.9x. The 5.9x claim may require different computation methodology than what's stored in the registry.

agentId: a9d34ba9d381fdded (use SendMessage with to: 'a9d34ba9d381fdded' to continue this agent)
&lt;usage>total_tokens: 78760
tool_uses: 37
duration_ms: 711170&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "5c6b7607-f9bc-4e20-a8ec-6b3ca7ba008d",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You are auditing numbers in a research paper against an experiment registry. The registry data is saved at:\n`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/3aaca442-e705-47db-9f84-980fe61c25da/tool-results/mcp-agent-ml-research-read_registry-1779738138900.txt`\n\nIt is JSON with schema `{result: string}` — the `result` field is itself a string that contains the actual registry content (likely JSON or YAML). Probe with jq first to understand structure, then extract data.\n\nI need you to find and verify the following specific numbers that appear in the paper. For each number, tell me:\n1. Whether it exists in the registry\n2. The exact registry experiment ID and metric field it comes from\n3. Whether the paper value matches the registry value exactly\n\n**Numbers to verify:**\n\n### Experimental results (PPL values)\n- Adaptive τ=0.7 5-seed mean holdout PPL: 17.674 (paper says this in introduction)\n- Uniform baseline 5-seed mean: 17.694\n- D&R q>0.7 3-seed PPL: 17.250 (introduction says \"PPL 17.250 vs. 17.674, 3 seeds\")\n- Δ = -0.023 at ρ=0.4 (introduction: \"$\\Delta{=}{-}0.023$ at $\\rho{=}0.4$\")\n- Δ = -0.032 at ρ=0.6 (introduction: \"$-$0.032 at $\\rho{=}0.6$\")\n- Epoch-matched gap Δ=0.017 (introduction: \"reducing the gap to $\\Delta{=}0.017$\")\n- \">95%\" of advantage from multi-epoch (introduction and abstract)\n\n### Detector metrics\n- AUC = 0.94 (related work: \"AUC\\,=\\,0.94\")\n- ECE = 0.048 (from reference numbers)\n\n### Data/model specs\n- 132M tokens\n- 371,499 samples\n- ρ = 0.4\n- Qwen3-0.6B\n\n### Method section\n- Pearson r ≈ 0.79 for α_eff correlation (method section)\n- ~50% of batches where quality constraint binds (introduction: \"${\\sim}$50\\% of batches\")\n- ~5.9× lower sharpening exponents (introduction)\n\n### Related work external numbers\n- \"20-60% of web corpora\" synthetic content\n- Drayson et al. b=10 for ≤360M, b=1 for 1.7B\n- ModernBERT-150M detector AUC=0.986\n- WikiText-2 ~2M tokens\n- Golden ratio reciprocal ≈0.62\n\nAlso check: are there any numbers related to p-values? The reference says:\n- p_BH = 0.011 for adaptive τ=0.7\n- p_BH = 0.064 for ρ=0.6 adaptive\n- SD = 0.006 for adaptive τ=0.7\n\nSearch for these in the registry too.\n\n**Output format**: For each number, report:\n- Paper value\n- Registry value (if found), with experiment ID\n- Match? Yes/No/Not in registry\n- Any discrepancies\n\nBe thorough — probe the registry structure first, then search systematically.",
    "agentId": "a9d34ba9d381fdded",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete audit report.\n\n---\n\n## Audit Results: Paper Numbers vs. Registry\n\n### Experimental PPL Values\n\n**1. Adaptive tau=0.7 5-seed mean holdout PPL: 17.674**\n- Registry experiments: `tau07_seed42` (17.68), `tau07_seed123` (17.666), `tau07_seed456` (17.677), `adaptive_seed234` (17.678, tau=0.7 per spec), `adaptive_seed789` (17.668, tau=0.7 per spec)\n- Computed 5-seed mean: 17.674\n- **Match: YES (exact)**\n\n**2. Uniform baseline 5-seed mean: 17.694**\n- Registry experiments: `uniform_seed42` (17.6939), `uniform_seed123` (17.6861), `uniform_seed456` (17.7015), `uniform_seed234` (17.708), `uniform_seed789` (17.695)\n- Computed 5-seed mean: **17.697** (not 17.694)\n- Computed 3-seed mean (seeds 42/123/456 only): **17.694** (matches)\n- **Match: NO -- paper says \"5-seed\" but 17.694 is the 3-seed value. The 5-seed value is 17.697.**\n\n**3. D&R q>0.7 3-seed PPL: 17.250**\n- Registry D&R q>0.7: `detect_remove_q07_seed42_r3` (17.32), `detect_remove_q07_seed123` (17.32), `detect_remove_q07_seed456` (17.32) -- 3-seed mean = **17.320**\n- Registry D&R q>0.3: `detect_remove_q03_seed42_r2` (17.25), `detect_remove_q03_seed123` (17.25), `detect_remove_q03_seed456` (17.2509) -- 3-seed mean = **17.250**\n- **Match: NO -- 17.250 belongs to D&R q>0.3 (best threshold), NOT q>0.7. D&R q>0.7 gives 17.320. Either the paper mislabels the threshold or the PPL value.**\n\n**4. Delta = -0.023 at rho=0.4**\n- Adaptive 5-seed mean (17.674) minus uniform 5-seed mean (17.697) = -0.023\n- **Match: YES (using 5-seed uniform = 17.697)**\n- Note: This is internally inconsistent with #2 above. The delta -0.023 requires the 5-seed uniform mean (17.697), but the paper reports the uniform mean as 17.694 (which is the 3-seed value and would give delta = -0.020).\n\n**5. Delta = -0.032 at rho=0.6**\n- `adaptive_rho06_tau07_seed42/123/456`: 17.735, 17.727, 17.732 -- mean = 17.731\n- `contamination_60_uniform_seed42/123/456`: 17.766, 17.754, 17.770 -- mean = 17.763\n- Delta = -0.032\n- **Match: YES (exact)**\n\n**6. Epoch-matched gap Delta = 0.017**\n- D&R epoch-matched 3-seed mean (q<=0.5): `dr_epoch_matched_indep_lr_v2_seed42` (17.65053), `dr_epoch_matched_seed123_r2` (17.6591), `dr_epoch_matched_seed456` (17.66) -- mean = 17.657\n- Adaptive tau=0.7 mean: 17.674\n- Gap: 17.674 - 17.657 = 0.017\n- **Match: YES (exact)**\n\n**7. \">95%\" of advantage from multi-epoch**\n- Original D&R advantage: 17.674 - 17.320 = 0.354 PPL gap\n- Epoch-matched residual: 0.017\n- Multi-epoch explains: (0.354 - 0.017) / 0.354 = 95.2%\n- **Match: YES (95.2% > 95%)**\n\n### Detector Metrics\n\n**8. AUC = 0.94**\n- Registry: `detector_tfidf_lr.auc` = 0.939\n- 0.939 rounds to 0.94\n- **Match: YES (rounding from 0.939)**\n\n**9. ECE = 0.048**\n- Registry: `detector_tfidf_lr.ece_calibrated` = 0.048\n- **Match: YES (exact)**\n\n### Data/Model Specs\n\n**10. 132M tokens**\n- Registry: `datagen_synthetic_4gpu.spec.total_tokens` = 132,033,764\n- **Match: YES**\n\n**11. 371,499 samples**\n- Registry: `adaptive_seed42.spec.data_count` = 371,499\n- **Match: YES (exact)**\n\n**12. rho = 0.4**\n- Registry: `contamination_ratio = 0.4` in experiment commands/metrics\n- **Match: YES**\n\n**13. Qwen3-0.6B**\n- Registry: `model_name = Qwen/Qwen3-0.6B`\n- **Match: YES**\n\n### Method Section\n\n**14. Pearson r approximately 0.79 for alpha_eff correlation**\n- **Not in registry.** No experiment stores this value. Likely computed by analysis scripts from training logs, not stored as an experiment metric.\n\n**15. ~50% of batches where quality constraint binds**\n- **Not in registry for main config (tau=0.7, rho=0.4).** The closest available metric is `alpha_eff_pct_at_max` = 42.95% for `rho02_adaptive_tau09_r5` (a different configuration). Cannot verify.\n\n**16. ~5.9x lower sharpening exponents**\n- **Not directly verifiable from registry.** Available data:\n  - ESS-only `b_star_mean` = 3.53 (average of seed42=3.51, seed123=3.55)\n  - Tau=0.7 adaptive `b_star_mean` = 0.894 (from `tau_07_seed42`)\n  - Ratio: 3.53 / 0.894 = **3.9x** (not 5.9x)\n- The 5.9x value cannot be reproduced from the registry's stored b_star_mean values. It may come from a different comparison (e.g., per-sample rather than per-batch means, or a different ablation pair).\n\n### P-values and SD\n\n**17. p_BH = 0.011 for adaptive tau=0.7**\n- **Not in registry** (derived statistic). Raw paired t-test from registry PPLs yields p = 0.0012, which with Benjamini-Hochberg correction across multiple tests could yield 0.011. Plausible but not directly verifiable without knowing the full set of tests corrected for.\n\n**18. p_BH = 0.064 for rho=0.6 adaptive**\n- **Not in registry** (derived statistic). Raw paired t-test yields p = 0.0099. With BH correction this could yield 0.064. Same caveat as above.\n\n**19. SD = 0.006 for adaptive tau=0.7**\n- Computed from 5-seed PPLs: SD = 0.0063\n- Rounds to 0.006\n- **Match: YES**\n\n### Related Work External Numbers\n\n**20. \"20-60% of web corpora\" synthetic content** -- Not in registry (external citation claim)\n\n**21. Drayson et al. b=10 for <=360M, b=1 for 1.7B** -- Not in registry (external citation)\n\n**22. ModernBERT-150M detector AUC=0.986** -- Not in registry. `detector_modernbert` was cancelled before running (status: killed, no metrics). This is from a cited paper.\n\n**23. WikiText-2 ~2M tokens** -- Not in registry (general dataset fact)\n\n**24. Golden ratio reciprocal approximately 0.62** -- Registry: `golden_ratio_seed42` uses w=1/phi approx 0.618. Paper rounds to 0.62. **Consistent.**\n\n---\n\n## Key Discrepancies Found\n\n1. **Uniform mean seed count mismatch**: Paper claims \"5-seed mean = 17.694\" but registry 5-seed mean = 17.697. The value 17.694 is actually the **3-seed** mean (seeds 42, 123, 456). Either the paper should say \"3-seed\" or update the number to 17.697.\n\n2. **D&R threshold/PPL mismatch**: If the paper says \"D&R q>0.7\" gives PPL 17.250, this is wrong. Registry shows D&R q>0.7 = 17.320. The PPL 17.250 belongs to D&R q>0.3 (the best threshold). Either the threshold label or the PPL value needs correction.\n\n3. **Internal inconsistency between uniform mean and delta**: The delta = -0.023 at rho=0.4 is correct when computed from 5-seed uniform (17.697), but the paper simultaneously reports the uniform mean as 17.694 (3-seed value). If uniform were truly 17.694, the delta would be -0.020, not -0.023.\n\n4. **~5.9x sharpening ratio not reproducible**: From registry b_star_mean values, the ESS-only vs. dual-constraint ratio is ~3.9x, not 5.9x. The 5.9x claim may require different computation methodology than what's stored in the registry."
      }
    ],
    "totalDurationMs": 711170,
    "totalTokens": 78760,
    "totalToolUseCount": 37,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 74913,
      "output_tokens": 2456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1390
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2456,
          "cache_read_input_tokens": 74913,
          "cache_creation_input_tokens": 1390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1390,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 36,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---


### Assistant

_source line 137_

<details><summary>Logged reasoning block</summary>

```text
The agent has done a thorough audit. Let me now check the specific discrepancies found and also look at the paper text more carefully to understand the context. Let me also check the experiments.tex file for additional cross-referencing.

Key discrepancies found:
1. Uniform mean: paper says 17.694 (5-seed) but registry 5-seed = 17.697; 17.694 is 3-seed
2. D&R PPL 17.250 labeled as "vs. 17.674" in intro - but 17.250 is D&R q>0.3, not q>0.7. D&R q>0.7 = 17.320


3. The delta of -0.023 aligns with the 5-seed uniform value of 17.697, not the reported 17.694, and the ~5.9x ratio doesn't match what I'm getting from the registry data (closer to 3.9x).

Now I need to carefully re-examine the introduction to see exactly what's being claimed, particularly around line 26 where D&R performance is discussed, and cross-check against the experiments.tex file.

The introduction states D&R achieves 17.250 PPL versus 17.674 for adaptive reweighting with 3 seeds, but doesn't specify which D&R threshold this refers to. Looking at the reference numbers, 17.250 corresponds to D&R with q>0.3, which is the best D&R result. The paper just says "D&R" without clarifying the threshold, which might be acceptable if the main results table presents D&R q>0.3 as the primary result. that checks out—the multi-epoch effect explains about 96% of the performance gap between D&R and the adaptive baseline. Now I need to clarify what "epoch-matched" actually means in this context.

The epoch-matched D&R result of 17.657 represents D&R's performance when constrained to the same number of epochs as the adaptive method, which narrows the gap from 0.424 down to just 0.017. But this calculation hinges on which D&R threshold we're using—the paper reports 17.250 for q>0.3, while the agent used 17.320 for q>0.7, which would give a different attribution percentage.

Either way, the multi-epoch effect accounts for over 95% of D&R's advantage, so that claim holds up. Now I need to track down where the uniform 5-seed baseline of 17.697 comes from, since the paper mentions Δ = -0.023 at ρ = 0.4 but I haven't found that value explicitly stated in my data files. So the 5-seed mean actually comes out to 17.697, which matches what the agent found, while 17.694 is the 3-seed mean—that explains the discrepancy in the reference numbers. And checking against the paper's reported Δ of -0.023 with adaptive at 17.674, the uniform baseline should indeed be 17.697, which confirms the actual registry values are correct.

For the D&R result, the intro mentions 17.250 as the comparison point but doesn't specify whether that's from q>0.3 or q>0.7, so I should clarify that it's the q>0.3 variant they're highlighting. The ~5.9x ratio discrepancy is trickier—the agent only found ~3.9x from the stored b_star_mean values, which suggests there might be something missing in how those values were calculated or reported. I'm noticing the Pearson correlation coefficient isn't documented in the registry either, so that's another claim I can't verify. Looking at the abstract, it does align with what the introduction says about multi-epoch exposure accounting for over 95% of the advantage. I can confirm some of the detector metrics match the cited sources—the TF-IDF baseline checks out at 0.94—but there are several specific numerical claims I need to flag as unverifiable from the available data, particularly around the batch percentages and correlation values. Looking at the remaining claims, the AUC value of 0.94 checks out against the registry data, but I can't verify the Pearson correlation coefficient without access to the experiments file. I should focus on what I can actually cross-reference in my assigned files. The figure caption mentions b_star ≈ 0.9, which aligns with the registry value of 0.894, so that's consistent.

The bigger concern is the 5.9x ratio claim—my calculation shows it should be closer to 3.95x based on the ESS-only and baseline b_star values. This is a substantial discrepancy that I can't confidently resolve without understanding which specific metric or seed configuration the paper is using, so I'll need to flag this as uncertain rather than attempt a fix.

For the intro claim about D&R using 3 seeds, I'm verifying whether both the D&R and adaptive τ=0.7 results use the same seed count. The 3-seed mean for adaptive τ=0.7 works out to 17.674, which matches the 5-seed mean, so the comparison holds up regardless of whether it's 3 or 5 seeds—but the phrasing in the introduction suggests both methods are being compared at 3 seeds.

Now I'm noticing a potential inconsistency with the delta value stated later. The paper claims Δ = -0.023 at ρ=0.4, which appears to be comparing adaptive versus uniform. If this delta comes from the 5-seed results (17.674 vs 17.697), it checks out, but if it's from the 3-seed results (17.674 vs 17.694), the delta should be -0.020 instead. This discrepancy suggests the paper might be mixing seed counts across different comparisons.

Let me verify: the delta of -0.023 only makes sense if the uniform baseline is 17.697 from the 5-seed run, not 17.694. Searching through my files, I don't actually see 17.694 referenced anywhere, so my numbers appear internally consistent with this interpretation. The real issue I'm finding is that the 5.9x ratio claim is likely incorrect.

Now I'm checking the abstract and captions against the registry values—the b* ≈ 0.9 matches the registry's 0.894, and the ESS-only b ≈ 3.5 aligns with ~3.53, so those check out. I should also cross-reference the experiments.tex file to see if there are other numbers that need verification.

Let me focus on the assigned files and compile the audit findings. I'm re-examining that 5.9x claim more carefully—the introduction states the quality constraint produces ~5.9x lower sharpening exponents than ESS-only, but if adaptive b* is 0.9 and ESS-only is 3.5, that's only a 3.9x difference, not 5.9x. There's a discrepancy I need to investigate further.

The comparison might be isolating just the batches where the quality constraint actually binds, which could have different b values than the overall mean, or it could involve a specific pair I haven't located yet. Since I can't determine the correct value with certainty from the registry means, I'll flag this inconsistency and note the ~3.9x ratio I'm seeing instead.

Now I need to verify the method section defaults—it specifies τ=0.7 and n_min=⌊B/2⌋, while the abstract mentions contamination ratios ρ≥0.4. Let me check whether the registry confirms the method works at both ρ=0.4 and ρ=0.6.

The introduction states the method fails at ρ=0.2, and the reference data shows adaptive outperforming uniform at ρ=0.6, which aligns with the qualitative claim that the method doesn't help at lower contamination levels.

I should also check the abstract word count since there's a 200-word limit.

Looking at the abstract, I'm seeing the key findings: detect-and-remove beats reweighting methods, the mechanism is multi-epoch exposure on filtered data, detector calibration matters as much as discrimination, and minimum intervention outperforms unconstrained maximization. The dual-constrained adaptive exponent improves over uniform training at ρ ≥ 0.4 with statistical significance, and these results hold within their experimental scope. I'm noticing a discrepancy between the abstract mentioning "5 seeds" and the intro's "3 seeds" for the D&R comparison, but these refer to different experimental setups so that's consistent. I'm also verifying the method section's illustrative figure parameters—B=4 is just a toy example for demonstration purposes, and the derived values check out. Now I need to cross-check any numbers appearing across multiple sections to ensure consistency throughout the paper. I've finished checking the remaining numbers—"AUC=0.94" and "0.62" each appear only once in the related work section, so there's nothing to cross-reference. No inconsistencies across the files. Now I'm compiling the final report and noting which numbers are external citations that fall outside my audit scope. Continuing through the verification checklist, most values match the registry data, though I'm finding a couple of issues—the ~50% batches claim isn't verifiable from what I have, and the ≈5.9× multiplier appears to be wrong based on the actual numbers showing closer to 3.9×. The delta values at different ρ settings check out, and I'm confirming the hyperparameter choices and formulas used.

Moving into the method section, the τ=0.7 default and N_min formula are solid, but that r ≈ 0.79 value isn't something I can verify from the registry. The figure caption parameters are consistent with the formula, and the complexity claim is theoretical. In related work, the percentage range matches the cited source, and the AUC value is in the registry.

Continuing through the external citations and mathematical facts—the token count, golden ratio reciprocal, and ESS formula all check out. I've found about 39 total claims to verify, with a couple of potential issues and one unverifiable value. Now I need to figure out how to handle that 5.9x multiplier.

The tricky part is understanding what exactly is being compared. The paper says the quality constraint binds in roughly half the batches at 5.9× lower sharpening exponents than ESS-only would use. This isn't necessarily comparing overall mean b values—it's more likely looking at what happens within those specific batches where the constraint activates early. That's a different calculation than just dividing the aggregate means, so I should flag the discrepancy without assuming I know the exact methodology. That settles it—both the 5.9x ratio and the 50% binding frequency are plausible but can't be directly verified from the registry aggregates, so I'll note them as likely derived from per-batch training logs. Now I'll put together the final report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "d3c1553b-34da-4c9b-9fbd-63824ad21547",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNL9BMinJBcDrRhbokxALZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 30367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3600
      },
      "output_tokens": 20,
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

_source line 138_

审计完成。让我也检查 experiments.tex 中是否有可以交叉验证的数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "d7178a55-7874-45b9-8265-60eff139d411",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNL9BMinJBcDrRhbokxALZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 30367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3600
      },
      "output_tokens": 20,
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

_source line 139_

<details open><summary>🔧 Tool call — Glob · `toolu_01HeT7WZpTz8eyXVQ9KEScyA`</summary>

```json
{
  "pattern": "**/experiments.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "54cc41b0-2dc3-4b86-bfe6-124129eb1848",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNL9BMinJBcDrRhbokxALZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3600,
      "cache_read_input_tokens": 30367,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3600
      },
      "output_tokens": 20,
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

_source line 140 · 2026-05-25T19:57:06.093Z_

<details><summary>↩ Tool result · `toolu_01HeT7WZpTz8eyXVQ9KEScyA`</summary>

```text
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "60fb7ef5-38f3-4ea1-9559-c9397ed4a616",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/experiments.tex"
    ],
    "durationMs": 16,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 141_

<details open><summary>🔧 Tool call — Read · `toolu_016dvHALgycG9JK1rwrgJ7Kv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3aaca442-e705-47db-9f84-980fe61c25da",
  "uuid": "92b306f4-fe4b-42fe-a972-c1a87d7d9475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mBW28sXtz1F8Uijis4fR6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7085,
      "cache_read_input_tokens": 33967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7085
      },
      "output_tokens": 53,
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
