# audit numbers traceability

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 116
- **Recorded user turns:** 1
- **Tool calls:** 39
- **Original source:** `logs/workers/worker_audit_numbers-traceability_20260524T042839.log`
- **Structured JSON:** [`fe55843beab2d4c89c64.json`](../../sessions/fe/fe55843beab2d4c89c64.json)

## Before a recorded user message

39 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
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
  "uuid": "3380a94b-498d-4585-87a3-99348e797da3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/memory/"
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
    "resetsAt": 1779602400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8434fc7d-c5bb-4945-8dfa-68d34d9dc0c0",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a comprehensive number audit of their paper, checking that all numbers in the tex files can be traced back to registry experiments, and that numbers are consistent across different tex files. Let me start by reading all the tex files and the registry data in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "f9ae21ce-6136-4d5b-a0f3-38afb6e46541",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuL4qTKdhn8JxqcfTDZm8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12830,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12830
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

开始核查。先并行读取所有 tex 文件和 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "3cc036f0-366f-484a-bc95-36a94a15bc07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuL4qTKdhn8JxqcfTDZm8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12830,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12830
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012zLShMjDogPoy5VjJYF48j`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "4318534c-81ac-4509-9071-01db8b3579af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuL4qTKdhn8JxqcfTDZm8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12830,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12830
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

_source line 7 · 2026-05-24T04:28:56.424Z_

<details><summary>↩ Tool result · `toolu_012zLShMjDogPoy5VjJYF48j`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

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
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "30ad6770-dfac-47dc-9092-7d5c75bfa83e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all the tex files and the registry data in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "33fa886a-635d-47cf-95b9-e6878733cc93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 9_

并行读取所有 tex 文件和 registry 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "c4c39fa2-9cae-4cbd-bcbf-c8166dfa7563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01731eWVYk4xtgXu3Drf3G5E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "ef746202-95f0-4559-abeb-be514d679bfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 11 · 2026-05-24T04:29:10.189Z_

<details><summary>↩ Tool result · `toolu_01731eWVYk4xtgXu3Drf3G5E`</summary>

```text
1	\begin{abstract}
2	Standard confusion-matrix correction for noisy annotations assumes uniform error rates.
3	When this assumption fails---as it routinely does with LLM classifiers, whose error rates vary by up to $5\times$ across subgroups---correction can reverse the sign of estimated causal effects, concluding a beneficial treatment is harmful.
4	We derive an exact bias identity for this setting: global correction introduces subgroup-level bias with a product form $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$, factoring into each subgroup's deviation from the pooled error rate, the treatment effect heterogeneity, and an amplification factor from matrix inversion.
5	This population-level identity---verified at $R^2 \geq 0.97$ across synthetic grids, semi-synthetic evaluations using 11 empirical LLM confusion matrices, and three structurally distinct CATE estimators---predicts that global correction reverses CATE sign in 14.9\% of configurations at $\tau(0) = 0.03$ and amplifies bias in all eight real LLMs tested.
6	The identity yields a diagnostic: a condition on per-subgroup error rates alone predicts when correction increases bias, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero $\Delta\tau$; $0.86$ across all synthetic subgroups; $0.63$ on real LLM error profiles).
7	The per-subgroup correction prescribed by the identity reduces $|\text{bias}|$ by $7.4\times$ via hierarchical Bayesian estimation; when error heterogeneity is insufficient, the diagnostic alone guides practitioners to retain global correction.
8	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "109eb80b-3c23-4f57-bfa7-bd62332a1937",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nStandard confusion-matrix correction for noisy annotations assumes uniform error rates.\nWhen this assumption fails---as it routinely does with LLM classifiers, whose error rates vary by up to $5\\times$ across subgroups---correction can reverse the sign of estimated causal effects, concluding a beneficial treatment is harmful.\nWe derive an exact bias identity for this setting: global correction introduces subgroup-level bias with a product form $\\delta_s \\cdot \\Delta\\tau / (1 - 2\\bar{\\pi})$, factoring into each subgroup's deviation from the pooled error rate, the treatment effect heterogeneity, and an amplification factor from matrix inversion.\nThis population-level identity---verified at $R^2 \\geq 0.97$ across synthetic grids, semi-synthetic evaluations using 11 empirical LLM confusion matrices, and three structurally distinct CATE estimators---predicts that global correction reverses CATE sign in 14.9\\% of configurations at $\\tau(0) = 0.03$ and amplifies bias in all eight real LLMs tested.\nThe identity yields a diagnostic: a condition on per-subgroup error rates alone predicts when correction increases bias, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero $\\Delta\\tau$; $0.86$ across all synthetic subgroups; $0.63$ on real LLM error profiles).\nThe per-subgroup correction prescribed by the identity reduces $|\\text{bias}|$ by $7.4\\times$ via hierarchical Bayesian estimation; when error heterogeneity is insufficient, the diagnostic alone guides practitioners to retain global correction.\n\\end{abstract}",
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01EbS6XaWkHPnuBdtoUi71va`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "709fd944-eeeb-493e-83b1-8418a059ee10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 13 · 2026-05-24T04:29:10.451Z_

<details><summary>↩ Tool result · `toolu_01EbS6XaWkHPnuBdtoUi71va`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Consider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.
5	After standard confusion-matrix correction, the analysis concludes the policy \emph{increases} hate speech among younger users---but the true effect is protective.
6	This sign reversal is not an edge case.
7	
8	Large language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.
9	When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.
10	Yet LLM annotations are not uniformly accurate: \citet{ashwin2025bias} document misclassification rates varying by up to 5$\times$ across demographic subgroups, consistent with $\Delta\pi > 0.20$ at typical base error rates---well above the $0.15$ threshold at which EC-HTE becomes effective; in our pilot study, GPT-4.1 achieves 85.8\% accuracy on TweetEval sentiment, but error rates range from 10.2\% to 20.0\% across text-feature subgroups ($\Delta\pi = 0.098$).
11	
12	We show that this standard correction can make things worse.
13	In 14.9\% of our synthetic configurations (across a grid of $\Delta\pi$ and $\tau(0)$ values; $\tau(0) = 0.03$), global correction reverses the sign of estimated CATE---a protective treatment ($\tau = +0.03$) appears harmful ($\hat{\tau} = -0.059$)---rising to 31\% at $\tau(0) = 0.01$ (Figure~\ref{fig:sign_reversal}); all eight real LLMs tested amplify bias under global correction, while EC-HTE eliminates sign reversal entirely.
14	Global correction amplifies bias by up to 5.9$\times$ ($K{=}4$ with CausalForest); the classical Frazis-Loeb attenuation correction~\cite{frazis2003estimating} \emph{increases} bias by up to 2.9$\times$.
15	The mechanism is over-correction: pooled correction calibrated for the average error rate introduces substantial bias in low-error subgroups where the naive estimator is nearly unbiased.
16	
17	We derive an exact bias identity explaining when and why this occurs (Theorem~\ref{thm:bias_identity}): the correction-induced bias in each subgroup factors into three independently estimable components, verified at $R^2 \geq 0.97$ on synthetic grids and 11 empirical LLM confusion matrices.
18	The identity yields a diagnostic (Proposition~\ref{prop:debiasing_hurts}) that predicts when global correction will harm a subgroup using only per-subgroup misclassification rates, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity; Section~\ref{sec:diagnostic}).
19	
20	The per-subgroup correction prescribed by the identity---implemented via hierarchical Bayesian confusion matrix estimation (EC-HTE)---reduces $|\text{bias}|$ from 0.059 to 0.008 under extreme heterogeneity ($K{=}2$).
21	The advantage is conditional: when $\Delta\pi$ is small, the variance cost of stratification outweighs its bias benefit.
22	
23	Existing corrections---PPI~\cite{angelopoulos2023ppi}, DSL~\cite{egami2024dsl}, PPCI~\cite{sui2026ppci}, arm-specific PPI~\cite{mozer2026ppi}, ForestIV~\cite{bu2023forestiv}---assume homogeneous prediction error; none addresses effect modifier misclassification (Section~\ref{sec:related}).
24	
25	\begin{figure*}[t]
26	\centering
27	\includegraphics[width=\textwidth]{figures/fig1_sign_reversal.pdf}
28	\caption{CATE sign reversal under global correction ($K{=}2$, $\tau(0) = 0.03$). (A) Naive vs.\ global-corrected CATE; red triangles mark sign reversals (7.5\% of subgroup estimates). (B) Extreme case: true $\tau = +0.03$, estimated $\hat{\tau} = -0.059$. (C) 14.9\% of configurations exhibit sign reversal; all 8 real LLMs amplify bias; EC-HTE: 0\% reversal.}
29	\label{fig:sign_reversal}
30	\end{figure*}
31	
32	Our contributions are:
33	\begin{itemize}
34	    \item An exact finite-population bias identity (Theorem~\ref{thm:bias_identity}): the bias factors into three independently estimable components ($\delta_s \cdot \Delta\tau / (1-2\bar{\pi})$), explaining sign reversal in the LLM annotation setting and enabling the diagnostic below; verified at $R^2 \geq 0.97$ (Sections~\ref{sec:theory},~\ref{sec:bias_mechanism}).
35	    \item An actionable diagnostic (Proposition~\ref{prop:debiasing_hurts}): a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity)---independently useful without adopting any specific correction method (Section~\ref{sec:diagnostic}).
36	    \item One corrective instantiation of the identity: per-subgroup hierarchical Bayesian confusion matrix estimation (EC-HTE), compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error---effective when error heterogeneity is sufficient (Sections~\ref{sec:method}--\ref{sec:diagnostic}).
37	\end{itemize}
38	The identity and diagnostic (contributions 1--2) are the primary results, useful without adopting any correction method; EC-HTE is one instantiation showing the identity prescribes effective correction.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "727cbf3e-1c7e-46d8-9962-bc6c4fa5af67",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nConsider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.\nAfter standard confusion-matrix correction, the analysis concludes the policy \\emph{increases} hate speech among younger users---but the true effect is protective.\nThis sign reversal is not an edge case.\n\nLarge language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.\nWhen these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.\nYet LLM annotations are not uniformly accurate: \\citet{ashwin2025bias} document misclassification rates varying by up to 5$\\times$ across demographic subgroups, consistent with $\\Delta\\pi > 0.20$ at typical base error rates---well above the $0.15$ threshold at which EC-HTE becomes effective; in our pilot study, GPT-4.1 achieves 85.8\\% accuracy on TweetEval sentiment, but error rates range from 10.2\\% to 20.0\\% across text-feature subgroups ($\\Delta\\pi = 0.098$).\n\nWe show that this standard correction can make things worse.\nIn 14.9\\% of our synthetic configurations (across a grid of $\\Delta\\pi$ and $\\tau(0)$ values; $\\tau(0) = 0.03$), global correction reverses the sign of estimated CATE---a protective treatment ($\\tau = +0.03$) appears harmful ($\\hat{\\tau} = -0.059$)---rising to 31\\% at $\\tau(0) = 0.01$ (Figure~\\ref{fig:sign_reversal}); all eight real LLMs tested amplify bias under global correction, while EC-HTE eliminates sign reversal entirely.\nGlobal correction amplifies bias by up to 5.9$\\times$ ($K{=}4$ with CausalForest); the classical Frazis-Loeb attenuation correction~\\cite{frazis2003estimating} \\emph{increases} bias by up to 2.9$\\times$.\nThe mechanism is over-correction: pooled correction calibrated for the average error rate introduces substantial bias in low-error subgroups where the naive estimator is nearly unbiased.\n\nWe derive an exact bias identity explaining when and why this occurs (Theorem~\\ref{thm:bias_identity}): the correction-induced bias in each subgroup factors into three independently estimable components, verified at $R^2 \\geq 0.97$ on synthetic grids and 11 empirical LLM confusion matrices.\nThe identity yields a diagnostic (Proposition~\\ref{prop:debiasing_hurts}) that predicts when global correction will harm a subgroup using only per-subgroup misclassification rates, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity; Section~\\ref{sec:diagnostic}).\n\nThe per-subgroup correction prescribed by the identity---implemented via hierarchical Bayesian confusion matrix estimation (EC-HTE)---reduces $|\\text{bias}|$ from 0.059 to 0.008 under extreme heterogeneity ($K{=}2$).\nThe advantage is conditional: when $\\Delta\\pi$ is small, the variance cost of stratification outweighs its bias benefit.\n\nExisting corrections---PPI~\\cite{angelopoulos2023ppi}, DSL~\\cite{egami2024dsl}, PPCI~\\cite{sui2026ppci}, arm-specific PPI~\\cite{mozer2026ppi}, ForestIV~\\cite{bu2023forestiv}---assume homogeneous prediction error; none addresses effect modifier misclassification (Section~\\ref{sec:related}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_sign_reversal.pdf}\n\\caption{CATE sign reversal under global correction ($K{=}2$, $\\tau(0) = 0.03$). (A) Naive vs.\\ global-corrected CATE; red triangles mark sign reversals (7.5\\% of subgroup estimates). (B) Extreme case: true $\\tau = +0.03$, estimated $\\hat{\\tau} = -0.059$. (C) 14.9\\% of configurations exhibit sign reversal; all 8 real LLMs amplify bias; EC-HTE: 0\\% reversal.}\n\\label{fig:sign_reversal}\n\\end{figure*}\n\nOur contributions are:\n\\begin{itemize}\n    \\item An exact finite-population bias identity (Theorem~\\ref{thm:bias_identity}): the bias factors into three independently estimable components ($\\delta_s \\cdot \\Delta\\tau / (1-2\\bar{\\pi})$), explaining sign reversal in the LLM annotation setting and enabling the diagnostic below; verified at $R^2 \\geq 0.97$ (Sections~\\ref{sec:theory},~\\ref{sec:bias_mechanism}).\n    \\item An actionable diagnostic (Proposition~\\ref{prop:debiasing_hurts}): a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity)---independently useful without adopting any specific correction method (Section~\\ref{sec:diagnostic}).\n    \\item One corrective instantiation of the identity: per-subgroup hierarchical Bayesian confusion matrix estimation (EC-HTE), compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error---effective when error heterogeneity is sufficient (Sections~\\ref{sec:method}--\\ref{sec:diagnostic}).\n\\end{itemize}\nThe identity and diagnostic (contributions 1--2) are the primary results, useful without adopting any correction method; EC-HTE is one instantiation showing the identity prescribes effective correction.\n",
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_014dWafU2WXwwaoT5kSEUzBa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "c719261e-bdf2-4bbf-9f48-a212aa75828c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 15 · 2026-05-24T04:29:10.925Z_

<details><summary>↩ Tool result · `toolu_014dWafU2WXwwaoT5kSEUzBa`</summary>

```text
1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state five assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification:} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$ (diagnostic only; see Remark~2).
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{Non-degeneracy:} $\pi_s \neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.
22	\item[\textbf{(A5)}] \textit{Homogeneous treatment effects across subgroups:} $\tau(z, s) = \tau(z)$ for all $s$, so $\Delta\tau = \tau(1) - \tau(0)$ is a scalar.
23	\end{itemize}
24	
25	Under (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\hat{z}, z] = P(Z{=}z \mid \hat{Z}{=}\hat{z}, S{=}s)$) coincides with $C_s$.
26	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
27	
28	\begin{theorem}[Bias Decomposition Identity]
29	\label{thm:bias_identity}
30	Under \textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is
31	\begin{align}
32	\mathrm{bias}_{\mathrm{global}}(z{=}0, s) &= +\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z0} \\
33	\mathrm{bias}_{\mathrm{global}}(z{=}1, s) &= -\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z1}
34	\end{align}
35	where $\delta_s = \pi_s - \bar{\pi}$ is the subgroup deviation from the pooled error rate and $\Delta\tau = \tau(1) - \tau(0)$ is the CATE heterogeneity.
36	\end{theorem}
37	
38	Equations~\eqref{eq:bias_z0}--\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.
39	The bias factors into three interpretable components: $\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\Delta\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\bar{\pi})$ is an amplification factor from matrix inversion.
40	Bias vanishes when either source of variation is absent ($\delta_s = 0$ or $\Delta\tau = 0$), and arises only through their interaction.
41	Theorem~\ref{thm:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.
42	
43	\paragraph{Proof sketch.}
44	Global correction applies $M_{\text{global}}^{-1}$ to the subgroup-specific observed CATE $\tau_{\text{obs}}(\cdot, s) = M_s \cdot \tau_{\text{true}}$, yielding bias $(M_{\text{global}}^{-1} M_s - I) \cdot \tau_{\text{true}}$.
45	Direct computation shows $M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \bigl[\begin{smallmatrix} -1 & 1 \\ 1 & -1 \end{smallmatrix}\bigr]$.
46	Applying this matrix to $[\tau(0),\, \tau(1)]^\top$ produces the product form.
47	The full derivation appears in Appendix~\ref{app:derivation}.
48	For comparison with classical scalar attenuation~\citep{frazis2003estimating}, see Section~\ref{sec:related}.
49	
50	\paragraph{Relationship to classical scalar attenuation.}
51	Classical scalar attenuation~\citep{frazis2003estimating} gives $\beta^* = \beta(1 - 2\pi)$; dividing by $(1 - 2\bar{\pi})$ removes this bias under homogeneous errors, but Theorem~\ref{thm:bias_identity} characterizes a structurally distinct quantity: \emph{correction-induced} bias from applying $M_{\mathrm{global}}^{-1}$ to heterogeneous $M_s$.
52	F-L scalar correction (dividing $\hat{\tau}(z)$ by $1 - 2\bar{\pi}$) over-corrects low-error and under-corrects high-error subgroups---the same mechanism as global CM correction but restricted to a scalar ignoring the mixing structure between $z$-levels.
53	When $\pi_s \to 0.5$, $(1 - 2\pi_s) \to 0$ and the F-L per-subgroup correction diverges; EC-HTE's $\kappa$-guard (Section~\ref{sec:method}) avoids this singularity.
54	Table~\ref{tab:main_results} confirms: under extreme heterogeneity ($K{=}2$), the classical F-L scalar correction \emph{increases} $|\text{bias}|$ from 0.058 to 0.122 ($2.1\times$ naive), and F-L per-subgroup to 0.168 ($2.9\times$)---the textbook attenuation correction systematically amplifies bias when subgroup error rates differ.
55	
56	\begin{remark}
57	Theorem~\ref{thm:bias_identity} does not require assumption~(A2).
58	For arbitrary asymmetric confusion matrices ($\mathrm{FPR}_s \neq \mathrm{FNR}_s$),
59	the product form $\mathrm{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1}$ holds exactly,
60	where $B_s = M_{\mathrm{global}}^{-1} M_s - I$, because $B_s \mathbf{1} = \mathbf{0}$
61	follows from stochasticity of $M_s$ and $M_{\mathrm{global}}$ alone.
62	Assumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar
63	$\pm \delta_s / (1 - 2\bar{\pi})$ but is not necessary for the product structure.
64	Under asymmetric errors, the diagnostic (Proposition~\ref{prop:debiasing_hurts}) requires evaluating $[B_s]_{z,1}$ cell-by-cell rather than via a single scalar threshold; the AUC decreases from 0.86 to 0.66 (Appendix~\ref{app:asymmetric}), reflecting the additional complexity of cell-specific error rates.
65	For binary effect modifiers ($|\mathcal{Z}|{=}2$), the asymmetric score $|[B_s]_{z,1}|$ reduces to a monotone transform of the symmetric score $|\delta_s|/((1{-}2\bar{\pi})\pi_s)$, because column-stochastic $M$ forces $|B_s[0,1]|{=}|B_s[1,1]|$; practitioners may use the simpler symmetric formula without loss.
66	See Appendix~\ref{app:asymmetric} for the full derivation and empirical verification
67	($R^2 = 0.991$).
68	\end{remark}
69	
70	\begin{proposition}[Exact Identity under Heterogeneous Treatment Effects]
71	\label{prop:a5_relaxation}
72	When $\tau(z, s)$ varies across subgroups (relaxing A5), the bias identity remains exact:
73	\begin{equation}
74	\mathrm{bias}_{\mathrm{global}}(z{=}0, s) = +\frac{\delta_s \cdot \Delta\tau_s}{1 - 2\bar{\pi}}, \quad
75	\mathrm{bias}_{\mathrm{global}}(z{=}1, s) = -\frac{\delta_s \cdot \Delta\tau_s}{1 - 2\bar{\pi}},
76	\end{equation}
77	where $\Delta\tau_s = \tau_s(1) - \tau_s(0)$ is the subgroup-specific CATE heterogeneity.
78	\end{proposition}
79	
80	\begin{corollary}[Aggregate Bias]
81	\label{cor:aggregate_bias}
82	The population-weighted aggregate bias is $\mathrm{Cov}_w(\pi_s, \Delta\tau_s) / (1 - 2\bar{\pi})$.
83	\end{corollary}
84	
85	The proof is immediate: $B_s = M_{\mathrm{global}}^{-1} M_s - I$ depends only on confusion matrices, not on $\tau$.
86	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) extends unchanged: $\Delta\tau_s$ cancels, so~\eqref{eq:hurts_condition} remains $\Delta\tau$-free.
87	EC-HTE maintains $\geq$93\% coverage under both positive and negative $\Delta\tau_s$--$\delta_s$ correlation (Appendix~\ref{app:a5_violation}).
88	
89	The identity extends to $K > 2$ subgroups with $J$ effect-modifier levels; the multi-class bias retains the same product structure with modified amplification terms (Corollary~\ref{cor:multiclass} in Appendix~\ref{app:multiclass}).
90	
91	Assumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\ref{app:derivation}).
92	Empirical verification under class imbalance (Appendix~\ref{app:classimbalance}) shows $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as imbalance grows.
93	Empirical verification (Section~\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.97$ for $K{=}4$, closing the theory-practice gap to essentially zero; the residual variance reflects Monte Carlo noise, not model misspecification.
94	
95	\paragraph{Sensitivity to (A1).}
96	Assumption~(A1) is not empirically testable.
97	If misclassification correlates with potential outcomes ($\gamma = \mathrm{Corr}(\mathbb{1}[\hat{Z} {\neq} Z],\, Y(1){-}Y(0) \mid Z, S) \neq 0$), Theorem~\ref{thm:bias_identity} gains an $O(\gamma)$ perturbation; in NLP settings, this is plausible when LLM accuracy varies with outcome magnitude.
98	At $\gamma_T = 0.10$, EC-HTE coverage degrades to 75\%; sensitivity analysis frameworks~\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound the degradation (Section~\ref{sec:limitations}).
99	
100	\paragraph{Finite-sample remainder.}
101	Theorem~\ref{thm:bias_identity} is a population-level identity.
102	In practice, confusion matrices are estimated from $n_{\text{expert}}$ expert labels with $\hat{C}_s = C_s + E_s$, $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, motivating the singularity guard ($\kappa > 100 \to$ fallback) in Section~\ref{sec:method}.
103	
104	\begin{proposition}[Debiasing Can Increase Bias]
105	\label{prop:debiasing_hurts}
106	Under \textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\mathrm{bias}_{\mathrm{global}}| > |\mathrm{bias}_{\mathrm{naive}}|$) in subgroup $s$ if and only if
107	\begin{equation}
108	\frac{|\delta_s|}{(1 - 2\bar{\pi}) \cdot \pi_s} > 1.
109	\label{eq:hurts_condition}
110	\end{equation}
111	\end{proposition}
112	
113	Equation~\eqref{eq:hurts_condition} partitions subgroups into two regimes:
114	\begin{itemize}
115	    \item \textit{High-error} ($\pi_s > \bar{\pi}$): the condition reduces to $\pi_s > 0.5$, excluded by~(A4); global correction always reduces bias.
116	    \item \textit{Low-error} ($\pi_s < \bar{\pi}$): the condition holds whenever $\pi_s < \bar{\pi} / (2(1 - \bar{\pi}))$---easily satisfied: when $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ is harmed by global correction.
117	\end{itemize}
118	The mechanism is over-correction: for subgroups with near-zero misclassification ($\pi_s \approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\bar{\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups.
119	
120	In our experiments (Section~\ref{sec:bias_mechanism}), global correction increases bias in 50\% of $K{=}2$ configurations (260/520), with amplification reaching $2.86\times$ ($K{=}2$) and $2.41\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the full parameter grid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "ffb3b46c-6ddf-4c1b-91fc-54cf0d0101c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex",
      "content": "% Requires preamble: \\usepackage{amsthm,amsmath,amssymb}\n% and: \\newtheorem{theorem}{Theorem}\n%      \\newtheorem{corollary}[theorem]{Corollary}\n%      \\newtheorem{proposition}[theorem]{Proposition}\n\n\\section{Bias Decomposition: When Debiasing Hurts}\n\\label{sec:theory}\n\nWe formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.\nConsider estimating the conditional average treatment effect (CATE) $\\tau(z) = \\mathbb{E}[Y(1) - Y(0) \\mid Z = z]$, where $Z \\in \\{0, 1\\}$ is a binary effect modifier observed only through a noisy annotation $\\hat{Z}$.\nThe population consists of $K$ subgroups $S \\in \\{1, \\ldots, K\\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \\times 2$ confusion matrix $C_s$ with symmetric error rate $\\pi_s = P(\\hat{Z} \\neq Z \\mid S{=}s)$.\nStandard practice estimates a single confusion matrix $\\bar{C} = \\sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\nWe show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.\n\nWe state five assumptions maintained throughout.\n%\n\\begin{itemize}\n\\item[\\textbf{(A1)}] \\textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.\n\\item[\\textbf{(A2)}] \\textit{Symmetric misclassification:} $P(\\hat{Z}{=}1 \\mid Z{=}0, S{=}s) = P(\\hat{Z}{=}0 \\mid Z{=}1, S{=}s) = \\pi_s$ for all $s$ (diagnostic only; see Remark~2).\n\\item[\\textbf{(A3)}] \\textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.\n\\item[\\textbf{(A4)}] \\textit{Non-degeneracy:} $\\pi_s \\neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.\n\\item[\\textbf{(A5)}] \\textit{Homogeneous treatment effects across subgroups:} $\\tau(z, s) = \\tau(z)$ for all $s$, so $\\Delta\\tau = \\tau(1) - \\tau(0)$ is a scalar.\n\\end{itemize}\n\nUnder (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\\hat{z}, z] = P(Z{=}z \\mid \\hat{Z}{=}\\hat{z}, S{=}s)$) coincides with $C_s$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\n\\begin{theorem}[Bias Decomposition Identity]\n\\label{thm:bias_identity}\nUnder \\textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is\n\\begin{align}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) &= +\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z0} \\\\\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) &= -\\frac{\\delta_s \\cdot \\Delta\\tau}{1 - 2\\bar{\\pi}}, \\label{eq:bias_z1}\n\\end{align}\nwhere $\\delta_s = \\pi_s - \\bar{\\pi}$ is the subgroup deviation from the pooled error rate and $\\Delta\\tau = \\tau(1) - \\tau(0)$ is the CATE heterogeneity.\n\\end{theorem}\n\nEquations~\\eqref{eq:bias_z0}--\\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.\nThe bias factors into three interpretable components: $\\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\\Delta\\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\\bar{\\pi})$ is an amplification factor from matrix inversion.\nBias vanishes when either source of variation is absent ($\\delta_s = 0$ or $\\Delta\\tau = 0$), and arises only through their interaction.\nTheorem~\\ref{thm:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.\n\n\\paragraph{Proof sketch.}\nGlobal correction applies $M_{\\text{global}}^{-1}$ to the subgroup-specific observed CATE $\\tau_{\\text{obs}}(\\cdot, s) = M_s \\cdot \\tau_{\\text{true}}$, yielding bias $(M_{\\text{global}}^{-1} M_s - I) \\cdot \\tau_{\\text{true}}$.\nDirect computation shows $M_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\bigl[\\begin{smallmatrix} -1 & 1 \\\\ 1 & -1 \\end{smallmatrix}\\bigr]$.\nApplying this matrix to $[\\tau(0),\\, \\tau(1)]^\\top$ produces the product form.\nThe full derivation appears in Appendix~\\ref{app:derivation}.\nFor comparison with classical scalar attenuation~\\citep{frazis2003estimating}, see Section~\\ref{sec:related}.\n\n\\paragraph{Relationship to classical scalar attenuation.}\nClassical scalar attenuation~\\citep{frazis2003estimating} gives $\\beta^* = \\beta(1 - 2\\pi)$; dividing by $(1 - 2\\bar{\\pi})$ removes this bias under homogeneous errors, but Theorem~\\ref{thm:bias_identity} characterizes a structurally distinct quantity: \\emph{correction-induced} bias from applying $M_{\\mathrm{global}}^{-1}$ to heterogeneous $M_s$.\nF-L scalar correction (dividing $\\hat{\\tau}(z)$ by $1 - 2\\bar{\\pi}$) over-corrects low-error and under-corrects high-error subgroups---the same mechanism as global CM correction but restricted to a scalar ignoring the mixing structure between $z$-levels.\nWhen $\\pi_s \\to 0.5$, $(1 - 2\\pi_s) \\to 0$ and the F-L per-subgroup correction diverges; EC-HTE's $\\kappa$-guard (Section~\\ref{sec:method}) avoids this singularity.\nTable~\\ref{tab:main_results} confirms: under extreme heterogeneity ($K{=}2$), the classical F-L scalar correction \\emph{increases} $|\\text{bias}|$ from 0.058 to 0.122 ($2.1\\times$ naive), and F-L per-subgroup to 0.168 ($2.9\\times$)---the textbook attenuation correction systematically amplifies bias when subgroup error rates differ.\n\n\\begin{remark}\nTheorem~\\ref{thm:bias_identity} does not require assumption~(A2).\nFor arbitrary asymmetric confusion matrices ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$),\nthe product form $\\mathrm{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ holds exactly,\nwhere $B_s = M_{\\mathrm{global}}^{-1} M_s - I$, because $B_s \\mathbf{1} = \\mathbf{0}$\nfollows from stochasticity of $M_s$ and $M_{\\mathrm{global}}$ alone.\nAssumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar\n$\\pm \\delta_s / (1 - 2\\bar{\\pi})$ but is not necessary for the product structure.\nUnder asymmetric errors, the diagnostic (Proposition~\\ref{prop:debiasing_hurts}) requires evaluating $[B_s]_{z,1}$ cell-by-cell rather than via a single scalar threshold; the AUC decreases from 0.86 to 0.66 (Appendix~\\ref{app:asymmetric}), reflecting the additional complexity of cell-specific error rates.\nFor binary effect modifiers ($|\\mathcal{Z}|{=}2$), the asymmetric score $|[B_s]_{z,1}|$ reduces to a monotone transform of the symmetric score $|\\delta_s|/((1{-}2\\bar{\\pi})\\pi_s)$, because column-stochastic $M$ forces $|B_s[0,1]|{=}|B_s[1,1]|$; practitioners may use the simpler symmetric formula without loss.\nSee Appendix~\\ref{app:asymmetric} for the full derivation and empirical verification\n($R^2 = 0.991$).\n\\end{remark}\n\n\\begin{proposition}[Exact Identity under Heterogeneous Treatment Effects]\n\\label{prop:a5_relaxation}\nWhen $\\tau(z, s)$ varies across subgroups (relaxing A5), the bias identity remains exact:\n\\begin{equation}\n\\mathrm{bias}_{\\mathrm{global}}(z{=}0, s) = +\\frac{\\delta_s \\cdot \\Delta\\tau_s}{1 - 2\\bar{\\pi}}, \\quad\n\\mathrm{bias}_{\\mathrm{global}}(z{=}1, s) = -\\frac{\\delta_s \\cdot \\Delta\\tau_s}{1 - 2\\bar{\\pi}},\n\\end{equation}\nwhere $\\Delta\\tau_s = \\tau_s(1) - \\tau_s(0)$ is the subgroup-specific CATE heterogeneity.\n\\end{proposition}\n\n\\begin{corollary}[Aggregate Bias]\n\\label{cor:aggregate_bias}\nThe population-weighted aggregate bias is $\\mathrm{Cov}_w(\\pi_s, \\Delta\\tau_s) / (1 - 2\\bar{\\pi})$.\n\\end{corollary}\n\nThe proof is immediate: $B_s = M_{\\mathrm{global}}^{-1} M_s - I$ depends only on confusion matrices, not on $\\tau$.\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) extends unchanged: $\\Delta\\tau_s$ cancels, so~\\eqref{eq:hurts_condition} remains $\\Delta\\tau$-free.\nEC-HTE maintains $\\geq$93\\% coverage under both positive and negative $\\Delta\\tau_s$--$\\delta_s$ correlation (Appendix~\\ref{app:a5_violation}).\n\nThe identity extends to $K > 2$ subgroups with $J$ effect-modifier levels; the multi-class bias retains the same product structure with modified amplification terms (Corollary~\\ref{cor:multiclass} in Appendix~\\ref{app:multiclass}).\n\nAssumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \\neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\\ref{app:derivation}).\nEmpirical verification under class imbalance (Appendix~\\ref{app:classimbalance}) shows $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as imbalance grows.\nEmpirical verification (Section~\\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.97$ for $K{=}4$, closing the theory-practice gap to essentially zero; the residual variance reflects Monte Carlo noise, not model misspecification.\n\n\\paragraph{Sensitivity to (A1).}\nAssumption~(A1) is not empirically testable.\nIf misclassification correlates with potential outcomes ($\\gamma = \\mathrm{Corr}(\\mathbb{1}[\\hat{Z} {\\neq} Z],\\, Y(1){-}Y(0) \\mid Z, S) \\neq 0$), Theorem~\\ref{thm:bias_identity} gains an $O(\\gamma)$ perturbation; in NLP settings, this is plausible when LLM accuracy varies with outcome magnitude.\nAt $\\gamma_T = 0.10$, EC-HTE coverage degrades to 75\\%; sensitivity analysis frameworks~\\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound the degradation (Section~\\ref{sec:limitations}).\n\n\\paragraph{Finite-sample remainder.}\nTheorem~\\ref{thm:bias_identity} is a population-level identity.\nIn practice, confusion matrices are estimated from $n_{\\text{expert}}$ expert labels with $\\hat{C}_s = C_s + E_s$, $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, motivating the singularity guard ($\\kappa > 100 \\to$ fallback) in Section~\\ref{sec:method}.\n\n\\begin{proposition}[Debiasing Can Increase Bias]\n\\label{prop:debiasing_hurts}\nUnder \\textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\\mathrm{bias}_{\\mathrm{global}}| > |\\mathrm{bias}_{\\mathrm{naive}}|$) in subgroup $s$ if and only if\n\\begin{equation}\n\\frac{|\\delta_s|}{(1 - 2\\bar{\\pi}) \\cdot \\pi_s} > 1.\n\\label{eq:hurts_condition}\n\\end{equation}\n\\end{proposition}\n\nEquation~\\eqref{eq:hurts_condition} partitions subgroups into two regimes:\n\\begin{itemize}\n    \\item \\textit{High-error} ($\\pi_s > \\bar{\\pi}$): the condition reduces to $\\pi_s > 0.5$, excluded by~(A4); global correction always reduces bias.\n    \\item \\textit{Low-error} ($\\pi_s < \\bar{\\pi}$): the condition holds whenever $\\pi_s < \\bar{\\pi} / (2(1 - \\bar{\\pi}))$---easily satisfied: when $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ is harmed by global correction.\n\\end{itemize}\nThe mechanism is over-correction: for subgroups with near-zero misclassification ($\\pi_s \\approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\\bar{\\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups.\n\nIn our experiments (Section~\\ref{sec:bias_mechanism}), global correction increases bias in 50\\% of $K{=}2$ configurations (260/520), with amplification reaching $2.86\\times$ ($K{=}2$) and $2.41\\times$ ($K{=}4$); Figure~\\ref{fig:heatmap} visualizes the full parameter grid.",
      "numLines": 120,
      "startLine": 1,
      "totalLines": 120
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01E8Exw9Fih4GNwrtsqtbx1d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "d32cf5b5-565c-463e-b00a-c8a07bc0bf76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 17 · 2026-05-24T04:29:11.266Z_

<details><summary>↩ Tool result · `toolu_01E8Exw9Fih4GNwrtsqtbx1d`</summary>

```text
1	\section{Correction Prescribed by the Identity}
2	\label{sec:method}
3	
4	Theorem~\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.
5	This correction (EC-HTE) proceeds in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.
6	The complete procedure is summarized in Algorithm~\ref{alg:echte} (Appendix~\ref{app:algorithm}).
7	
8	\subsection{Hierarchical Bayes Confusion Matrix Estimation}
9	
10	We place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\{C_s\}_{s=1}^K$.
11	For each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior centered at the global pooled confusion matrix $\hat{C}_{\text{global}}$: $\text{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, where $\hat{C}_{\text{global},j}$ is the $j$-th row of the pooled CM and $\alpha_0 > 0$ is a shared concentration parameter estimated via empirical Bayes (marginal likelihood maximization).
12	We place a $\mathrm{Gamma}(a_0, b_0)$ hyperprior on $\alpha_0$ with defaults $a_0 = 3$, $b_0 = 1$, robust to $2\times$ perturbation of $(a_0, b_0)$ (RMSE change $\leq 4\%$; Appendix~\ref{app:dgp}).
13	Large $\alpha_0$ pulls subgroup estimates toward $\hat{C}_{\text{global}}$ (global correction), while small $\alpha_0$ allows subgroup-specific rates to dominate (stratified correction).
14	This partial pooling---a form of James-Stein shrinkage well-established in small-area estimation---borrows strength across subgroups when estimating confusion matrices from limited expert labels, reducing variance for small subgroups while preserving heterogeneity where data support it.
15	
16	Posterior inference uses centered empirical Bayes optimization ($<$5ms for $K{=}4$, $N{=}5{,}000$); a full Gibbs MCMC alternative requires $\sim$5s (convergence diagnostics in Appendix~\ref{app:algorithm}).
17	Bootstrap SE ($B{=}100$) adds $\sim$0.4s.
18	HB estimation outperforms stratified MLE in 87.5\% of configurations (21 of 24) across the experimental grid (Section~\ref{sec:ec_hte_eval}), with the largest gains when $n_{\text{expert}} / K < 100$.
19	The advantage requires $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ per subgroup; below this threshold, stratified MLE is preferred because the hierarchical model lacks sufficient observations for stable shrinkage.
20	At $n_{\text{expert}} \geq 1000$, HB and stratified MLE converge to within 0.5\% on all metrics.
21	Sensitivity analysis shows $<$5\% RMSE variation under 2$\times$ hyperprior perturbation, confirming that results are not driven by prior specification.
22	
23	\subsection{Subgroup-Stratified Correction}
24	
25	Given posterior mean confusion matrices $\hat{C}_s$, we correct observed outcome moments per subgroup by matrix inversion:
26	\begin{equation}
27	\tilde{\boldsymbol{\mu}}_s = \hat{C}_s^{-1} \cdot \hat{\boldsymbol{\mu}}_s,
28	\end{equation}
29	where $\hat{\boldsymbol{\mu}}_s = [\hat{\tau}_{\text{obs}}(0, s),\, \hat{\tau}_{\text{obs}}(1, s)]^\top$ collects the observed conditional outcome moments in subgroup $s$.
30	This requires $\det(\hat{C}_s) \neq 0$ for all $s$, which holds under assumption~(A4) ($\pi_s \neq 0.5$) but may fail in finite samples when error rates approach degeneracy.
31	In practice, Laplace smoothing of the confusion matrix counts ensures finite-sample invertibility.
32	We impose a singularity guard: if the condition number $\kappa(\hat{C}_s) > 100$ (for a $2{\times}2$ symmetric confusion matrix, this corresponds to $\pi_s > 0.495$, i.e., near-random classification), subgroup $s$ falls back to global correction $\bar{C}^{-1}$; when the fallback triggers, the standard error computation also uses $\bar{C}^{-1}$ for that subgroup, ensuring consistency between point estimates and confidence intervals.
33	This hard guard prevents numerical catastrophe; $\kappa \leq 1.25$ is a sufficient condition for strongest bias reduction (Appendix~\ref{sec:budget}), though EC-HTE maintains calibrated coverage ($\geq$93\%) across the wider $\kappa \in [1.4, 3.0]$ range observed in practice (Appendix~\ref{app:kappa_analysis}).
34	
35	The contrast with global correction is direct.
36	Global correction applies $\bar{C}^{-1}$ uniformly to all subgroups, introducing the $\delta_s \cdot \Delta\tau$ bias identified in Theorem~\ref{thm:bias_identity}.
37	Subgroup-stratified correction eliminates this bias by matching each subgroup's correction to its own misclassification structure, at the cost of higher variance from estimating $K$ separate confusion matrices (Appendix~\ref{sec:budget}).
38	
39	\subsection{Variance-Adjusted CausalForest}
40	
41	For heterogeneous treatment effect estimation, we feed corrected covariates into CausalForestDML~\cite{wager2018causal} with honest splitting.
42	The forest produces per-observation standard error estimates $\text{se}_i$.
43	To account for confusion matrix correction, we propagate uncertainty through the inverse mapping:
44	\begin{equation}
45	\text{se}_{\text{corrected},i} = \sqrt{\text{diag}\!\left(\hat{C}_{S_i}^{-1}\, \text{diag}(\text{se}_i^2)\, \hat{C}_{S_i}^{-\top}\right)}.
46	\end{equation}
47	This plug-in SE conditions on $\hat{C}_s$, neglecting CM estimation uncertainty; at $n_{\text{expert}} \geq 100$ this is negligible, but below this threshold a full bootstrap ($B{=}100$; re-estimate CM and re-fit per replicate) maintains $\geq$95\% coverage across all budgets tested ($n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$); even plug-in SE achieves $\geq$91\% at $n_{\text{expert}}{=}25$ (Appendix~\ref{app:bootstrap_se}).
48	When $n_{\text{expert}}/K < 50$, we recommend bootstrap SE; otherwise plug-in SE suffices.
49	
50	\paragraph{Diagnostic criterion.}
51	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction harms subgroup $s$ if and only if $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, a condition depending only on per-subgroup misclassification rates estimable from a pilot sample.
52	This breaks the circular dependency that would arise if the diagnostic required CATE estimates.
53	A threshold classifier achieves AUC~=~0.86 at the subgroup level, reaching 1.0 when restricted to subgroups with $\tau_s > 0$ (Section~\ref{sec:diagnostic}).
54	
55	\paragraph{Composition with PPCI.}
56	EC-HTE corrects structured covariate misclassification through $\hat{C}_s^{-1}$ inversion but cannot address outcome-level measurement error.
57	PPCI~\cite{sui2026ppci} corrects residual outcome bias using a debiasing estimator but assumes correct covariate labels.
58	The two methods are complementary: apply EC-HTE first to correct covariate labels, then PPCI to correct outcome predictions.
59	Neither is redundant with the other: EC-HTE alone cannot fix outcome error, while PPCI alone incurs higher variance for covariate error.
60	Under both error types simultaneously, the composition reduces $|\text{bias}|$ from 0.179 to 0.007 (Appendix~\ref{sec:ppci}).
61	The two methods target different error sources and are not substitutes: under covariate-side error alone (DGP~A), EC-HTE provides a 27\% RMSE advantage over PPCI; under outcome-side error alone (DGP~C), PPCI achieves $|\text{bias}| = 0.003$--$0.004$ and EC-HTE's marginal contribution is negligible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "cdcae47c-602a-4b97-8727-345056338ef9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex",
      "content": "\\section{Correction Prescribed by the Identity}\n\\label{sec:method}\n\nTheorem~\\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.\nThis correction (EC-HTE) proceeds in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.\nThe complete procedure is summarized in Algorithm~\\ref{alg:echte} (Appendix~\\ref{app:algorithm}).\n\n\\subsection{Hierarchical Bayes Confusion Matrix Estimation}\n\nWe place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\\{C_s\\}_{s=1}^K$.\nFor each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior centered at the global pooled confusion matrix $\\hat{C}_{\\text{global}}$: $\\text{Dir}(\\alpha_0 \\cdot \\hat{C}_{\\text{global},j})$, where $\\hat{C}_{\\text{global},j}$ is the $j$-th row of the pooled CM and $\\alpha_0 > 0$ is a shared concentration parameter estimated via empirical Bayes (marginal likelihood maximization).\nWe place a $\\mathrm{Gamma}(a_0, b_0)$ hyperprior on $\\alpha_0$ with defaults $a_0 = 3$, $b_0 = 1$, robust to $2\\times$ perturbation of $(a_0, b_0)$ (RMSE change $\\leq 4\\%$; Appendix~\\ref{app:dgp}).\nLarge $\\alpha_0$ pulls subgroup estimates toward $\\hat{C}_{\\text{global}}$ (global correction), while small $\\alpha_0$ allows subgroup-specific rates to dominate (stratified correction).\nThis partial pooling---a form of James-Stein shrinkage well-established in small-area estimation---borrows strength across subgroups when estimating confusion matrices from limited expert labels, reducing variance for small subgroups while preserving heterogeneity where data support it.\n\nPosterior inference uses centered empirical Bayes optimization ($<$5ms for $K{=}4$, $N{=}5{,}000$); a full Gibbs MCMC alternative requires $\\sim$5s (convergence diagnostics in Appendix~\\ref{app:algorithm}).\nBootstrap SE ($B{=}100$) adds $\\sim$0.4s.\nHB estimation outperforms stratified MLE in 87.5\\% of configurations (21 of 24) across the experimental grid (Section~\\ref{sec:ec_hte_eval}), with the largest gains when $n_{\\text{expert}} / K < 100$.\nThe advantage requires $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ per subgroup; below this threshold, stratified MLE is preferred because the hierarchical model lacks sufficient observations for stable shrinkage.\nAt $n_{\\text{expert}} \\geq 1000$, HB and stratified MLE converge to within 0.5\\% on all metrics.\nSensitivity analysis shows $<$5\\% RMSE variation under 2$\\times$ hyperprior perturbation, confirming that results are not driven by prior specification.\n\n\\subsection{Subgroup-Stratified Correction}\n\nGiven posterior mean confusion matrices $\\hat{C}_s$, we correct observed outcome moments per subgroup by matrix inversion:\n\\begin{equation}\n\\tilde{\\boldsymbol{\\mu}}_s = \\hat{C}_s^{-1} \\cdot \\hat{\\boldsymbol{\\mu}}_s,\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\mu}}_s = [\\hat{\\tau}_{\\text{obs}}(0, s),\\, \\hat{\\tau}_{\\text{obs}}(1, s)]^\\top$ collects the observed conditional outcome moments in subgroup $s$.\nThis requires $\\det(\\hat{C}_s) \\neq 0$ for all $s$, which holds under assumption~(A4) ($\\pi_s \\neq 0.5$) but may fail in finite samples when error rates approach degeneracy.\nIn practice, Laplace smoothing of the confusion matrix counts ensures finite-sample invertibility.\nWe impose a singularity guard: if the condition number $\\kappa(\\hat{C}_s) > 100$ (for a $2{\\times}2$ symmetric confusion matrix, this corresponds to $\\pi_s > 0.495$, i.e., near-random classification), subgroup $s$ falls back to global correction $\\bar{C}^{-1}$; when the fallback triggers, the standard error computation also uses $\\bar{C}^{-1}$ for that subgroup, ensuring consistency between point estimates and confidence intervals.\nThis hard guard prevents numerical catastrophe; $\\kappa \\leq 1.25$ is a sufficient condition for strongest bias reduction (Appendix~\\ref{sec:budget}), though EC-HTE maintains calibrated coverage ($\\geq$93\\%) across the wider $\\kappa \\in [1.4, 3.0]$ range observed in practice (Appendix~\\ref{app:kappa_analysis}).\n\nThe contrast with global correction is direct.\nGlobal correction applies $\\bar{C}^{-1}$ uniformly to all subgroups, introducing the $\\delta_s \\cdot \\Delta\\tau$ bias identified in Theorem~\\ref{thm:bias_identity}.\nSubgroup-stratified correction eliminates this bias by matching each subgroup's correction to its own misclassification structure, at the cost of higher variance from estimating $K$ separate confusion matrices (Appendix~\\ref{sec:budget}).\n\n\\subsection{Variance-Adjusted CausalForest}\n\nFor heterogeneous treatment effect estimation, we feed corrected covariates into CausalForestDML~\\cite{wager2018causal} with honest splitting.\nThe forest produces per-observation standard error estimates $\\text{se}_i$.\nTo account for confusion matrix correction, we propagate uncertainty through the inverse mapping:\n\\begin{equation}\n\\text{se}_{\\text{corrected},i} = \\sqrt{\\text{diag}\\!\\left(\\hat{C}_{S_i}^{-1}\\, \\text{diag}(\\text{se}_i^2)\\, \\hat{C}_{S_i}^{-\\top}\\right)}.\n\\end{equation}\nThis plug-in SE conditions on $\\hat{C}_s$, neglecting CM estimation uncertainty; at $n_{\\text{expert}} \\geq 100$ this is negligible, but below this threshold a full bootstrap ($B{=}100$; re-estimate CM and re-fit per replicate) maintains $\\geq$95\\% coverage across all budgets tested ($n_{\\text{expert}} \\in \\{25, 50, 75, 100, 200\\}$); even plug-in SE achieves $\\geq$91\\% at $n_{\\text{expert}}{=}25$ (Appendix~\\ref{app:bootstrap_se}).\nWhen $n_{\\text{expert}}/K < 50$, we recommend bootstrap SE; otherwise plug-in SE suffices.\n\n\\paragraph{Diagnostic criterion.}\nProposition~\\ref{prop:debiasing_hurts} provides a $\\Delta\\tau$-free diagnostic: global correction harms subgroup $s$ if and only if $|\\delta_s| / ((1-2\\bar{\\pi}) \\cdot \\pi_s) > 1$, a condition depending only on per-subgroup misclassification rates estimable from a pilot sample.\nThis breaks the circular dependency that would arise if the diagnostic required CATE estimates.\nA threshold classifier achieves AUC~=~0.86 at the subgroup level, reaching 1.0 when restricted to subgroups with $\\tau_s > 0$ (Section~\\ref{sec:diagnostic}).\n\n\\paragraph{Composition with PPCI.}\nEC-HTE corrects structured covariate misclassification through $\\hat{C}_s^{-1}$ inversion but cannot address outcome-level measurement error.\nPPCI~\\cite{sui2026ppci} corrects residual outcome bias using a debiasing estimator but assumes correct covariate labels.\nThe two methods are complementary: apply EC-HTE first to correct covariate labels, then PPCI to correct outcome predictions.\nNeither is redundant with the other: EC-HTE alone cannot fix outcome error, while PPCI alone incurs higher variance for covariate error.\nUnder both error types simultaneously, the composition reduces $|\\text{bias}|$ from 0.179 to 0.007 (Appendix~\\ref{sec:ppci}).\nThe two methods target different error sources and are not substitutes: under covariate-side error alone (DGP~A), EC-HTE provides a 27\\% RMSE advantage over PPCI; under outcome-side error alone (DGP~C), PPCI achieves $|\\text{bias}| = 0.003$--$0.004$ and EC-HTE's marginal contribution is negligible.",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01RYPLBzSHgb2tBeWbPDjGMR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "3ab18c80-1da3-41e4-b805-9fccbf4c5a65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 19 · 2026-05-24T04:29:11.745Z_

<details><summary>↩ Tool result · `toolu_01RYPLBzSHgb2tBeWbPDjGMR`</summary>

```text
1	\section{Experiments}
2	
3	\subsection{Setup}
4	
5	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 MC runs) and semi-synthetic (TweetEval sentiment~\cite{barbieri2020tweeteval}, $K{=}4$ unbalanced subgroups, $\pi \in \{0.05, 0.10, 0.15, 0.25\}$) DGPs; full specifications in Appendix~\ref{app:dgp}.
6	
7	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2024dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (per-subgroup correction), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
8	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
9	Primary metrics are $|\text{bias}|$, RMSE, and 95\% CI coverage, averaged across subgroups and 100 MC runs.
10	Robustness validation covers hate speech, six OpenAI models, subgroup misspecification, asymmetric confusion matrices, confounded treatment, outcome-dependent misclassification (all $\geq$93.5\% coverage), and treatment-dependent misclassification ($\approx$90\% at $\gamma_T \leq 0.05$; Appendices~\ref{app:hatespeech}--\ref{app:treatment_dep}).
11	Semi-synthetic evaluation uses empirical LLM confusion matrices from 16 model--dataset--$K$ combinations (8 LLMs $\times$ 2 datasets $\times$ varying $K$); of these, 11 have sufficient subgroup variation for $R^2$ regression and 13 have $K{=}4$ for $\kappa$ analysis.
12	
13	\subsection{Empirical Validation of the Bias Identity}
14	\label{sec:bias_mechanism}
15	
16	We verify Theorem~\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\Delta\pi \in [0, 0.25]$, $\Delta\tau \in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\ref{app:dgp}).
17	Regressing observed subgroup bias on $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.97$ ($K{=}4$); residual variance reflects MC noise ($R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\ref{app:classimbalance}).
18	Global correction worsens bias in 50\% of $K{=}2$ configurations (260/520, excluding $\Delta\pi{=}0$), with amplification reaching 2.86$\times$ ($K{=}2$) and 2.41$\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the amplification surface.
19	Beyond amplification, global correction reverses the sign of estimated CATE---concluding a protective treatment is harmful---in 14.9\% of configurations at $\tau(0) = 0.03$ (31\% at $\tau(0) = 0.01$; critical threshold $\tau(0) < 0.089$, matching Theorem~\ref{thm:bias_identity}), with all eight real LLMs amplifying bias under global correction; EC-HTE eliminates sign reversal entirely (Figure~\ref{fig:sign_reversal}; Appendix~\ref{app:policy_reversal}).
20	
21	\subsection{Correction Evaluation}
22	\label{sec:ec_hte_eval}
23	
24	Table~\ref{tab:main_results} presents the main results across representative configurations.
25	In the $K{=}2$ extreme row, global correction \emph{increases} $|\text{bias}|$ relative to naive (0.059 vs.\ 0.058), confirming the over-correction mechanism of Theorem~\ref{thm:bias_identity}.
26	F-L scalar correction increases $|\text{bias}|$ to 0.122 (coverage 0.68); F-L per-subgroup to 0.168 as $(1{-}2\pi_s) \to 0$---both worse than naive (Table~\ref{tab:main_results}).
27	HB EC-HTE reduces $|\text{bias}|$ from 0.059 to 0.008 (7.4$\times$); relative to stratified MLE (0.012), the advantage is 1.5$\times$ with lower RMSE from partial pooling. At $K{=}4$, bias reduces from 0.056 to 0.012 (4.7$\times$), maintaining near-nominal coverage (0.94--0.96).
28	Under moderate heterogeneity and in TweetEval ($K{=}4$), methods converge ($p > 0.05$); EC-HTE incurs higher RMSE when $\Delta\pi$ is small (Table~\ref{tab:main_supp}).
29	At $K{=}8$ ($n_{\text{expert}}/K{=}31$), coverage remains $\geq$95.6\% but RMSE increases; we recommend $n_{\text{expert}}/K \geq 50$ (Appendix~\ref{app:k8_subgroups}).
30	
31	\paragraph{CausalForest.}
32	Theorem~\ref{thm:bias_identity} applies to any estimator whose inputs pass through a confusion matrix; CausalForest~\cite{wager2018causal} with a noisy effect modifier $\hat{Z}$ inherits the same $M_{\text{global}}^{-1} M_s$ structure.
33	With CausalForest ($K{=}4$, extreme, $n{=}500$), EC-HTE reduces $|\text{bias}|$ from 0.191 to 0.039 (4.9$\times$) with coverage 0.90; global amplifies bias up to 5.9$\times$ (Table~\ref{tab:main_results}; bootstrap SE in Appendix~\ref{app:bootstrap_se}).
34	The identity and correction are estimator-agnostic: R-learner yields comparable bias reduction (89\%, Appendix~\ref{app:rlearner}), confirming that the product-form bias arises from the confusion matrix structure, not the downstream estimator.
35	
36	\begin{table}[t]
37	\centering
38	\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\text{bias}|$. $^\dagger$RMSE exceeds Global. F-L Scalar: $\hat{\tau}/(1{-}2\bar{\pi})$~\cite{frazis2003estimating}; F-L Per-sub.: per-subgroup variant (binary $Z$ only). Moderate/TweetEval in Table~\ref{tab:main_supp}; MC SEs $\leq 0.005$ for all entries (Appendix~\ref{app:mcse}).\protect\footnotemark}
39	\label{tab:main_results}
40	\resizebox{\columnwidth}{!}{%
41	\begin{tabular}{ll ccc}
42	\toprule
43	Configuration & Method & $|\text{Bias}|$ & RMSE & 95\% CI Cov. \\
44	\midrule
45	\multirow{6}{*}{\shortstack[l]{DIM\\$K{=}2$, $n{=}250$}}
46	 & Naive & 0.058 & 0.090 & 0.82 \\
47	 & Global & 0.059 & 0.099 & 0.87 \\
48	 & F-L Scalar & 0.122 & 0.159 & 0.68 \\
49	 & F-L Per-sub. & 0.168 & 0.220 & 0.65 \\
50	 & Strat.\ MLE & 0.012 & 0.094 & 0.95 \\
51	 & HB EC-HTE & \textbf{0.008} & 0.089 & 0.94 \\
52	\midrule
53	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}4$, $n{=}500$}}
54	 & Naive & 0.062 & 0.113 & 0.88 \\
55	 & Global & 0.056 & 0.125 & 0.91 \\
56	 & Strat.\ MLE & \textbf{0.010} & 0.127$^\dagger$ & 0.95 \\
57	 & HB EC-HTE & 0.012 & 0.120 & 0.96 \\
58	\midrule
59	\multirow{3}{*}{\shortstack[l]{CausalForest\\$K{=}4$, $n{=}500$}}
60	 & Naive & 0.208 & 0.231 & 0.44 \\
61	 & Global & 0.191 & 0.244 & 0.58 \\
62	 & EC-HTE Forest & \textbf{0.039} & 0.180 & 0.90 \\
63	\bottomrule
64	\end{tabular}}
65	\footnotetext{CausalForest plug-in SE achieves 93.8\% aggregate coverage; a bootstrap procedure ($B{=}100$) recovers $\geq$95\% coverage at all budgets tested (Appendix~\ref{app:bootstrap_se}).}
66	\end{table}
67	
68	\subsection{Actionable Diagnostic}
69	\label{sec:diagnostic}
70	
71	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, computable from a pilot sample without estimating treatment effects.
72	The diagnostic achieves AUC $= 0.63$ across 16 semi-synthetic LLM--dataset combinations; restricting to subgroups with $\Delta\tau > 0$ recovers AUC $= 1.0$ ($0.86$ on synthetic grids; Figure~\ref{fig:roc}, Appendix~\ref{app:screening}).
73	The lower AUC reflects inclusion of subgroups with $\Delta\tau \approx 0$, where misdiagnosis is inconsequential---global and stratified correction perform identically when effect heterogeneity is absent.
74	For $K{=}2$, $|\delta_0|{=}|\delta_1|$ limits discrimination (Appendix~\ref{app:screening}).
75	
76	The condition number $\kappa(\hat{C}_s)$ provides a practical guard: $\kappa > 100$ triggers fallback; all 13 tested LLM--dataset combinations fall in $\kappa \in (1.25, 3]$ with calibrated coverage $\geq$93\% (Appendix~\ref{app:kappa_analysis}).
77	Budget crossover, $K{=}8$ scalability, and multi-LLM validation ($R^2 = 0.975$) appear in Appendices~\ref{sec:budget}--\ref{app:multilm}.
78	
79	On a real hate speech dataset ($\Delta\pi{=}0.117$; Appendix~\ref{app:hatespeech}), EC-HTE underperforms both naive and global correction, consistent with most real LLMs exhibiting $\Delta\pi \in [0.10, 0.20]$ (Appendices~\ref{app:multilm}--\ref{app:civilcomments}).
80	
81	\paragraph{Operating conditions.}
82	EC-HTE requires: (i)~$\Delta\pi > 0.15$, (ii)~$n_{\text{expert}} \geq 250$ for $K{=}2$, (iii)~$\text{FNR}_s < 0.50$, and (iv)~$K \leq 4$; when unmet, global correction is preferable (Appendix~\ref{app:k8_subgroups}).
83	Under confounded treatment, pairing with IPW-DIM maintains $\geq$94.5\% coverage (Appendix~\ref{app:confounded_dgp}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "5ed3022e-ab31-4c68-952f-09afbac45913",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\n\\subsection{Setup}\n\nWe test on synthetic ($N{=}5{,}000$, $K \\in \\{2, 4\\}$, controlled $\\Delta\\tau$ and $\\Delta\\pi$, 100 MC runs) and semi-synthetic (TweetEval sentiment~\\cite{barbieri2020tweeteval}, $K{=}4$ unbalanced subgroups, $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$) DGPs; full specifications in Appendix~\\ref{app:dgp}.\n\nWe compare: (1) \\textit{Naive} (no correction), (2) \\textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\\cite{angelopoulos2023ppi,egami2024dsl} with homogeneous error), (3) \\textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \\textit{HB EC-HTE} (per-subgroup correction), (5) \\textit{PPCI}~\\cite{sui2026ppci}, and (6) \\textit{EC-HTE+PPCI}.\nFor CausalForest~\\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.\nPrimary metrics are $|\\text{bias}|$, RMSE, and 95\\% CI coverage, averaged across subgroups and 100 MC runs.\nRobustness validation covers hate speech, six OpenAI models, subgroup misspecification, asymmetric confusion matrices, confounded treatment, outcome-dependent misclassification (all $\\geq$93.5\\% coverage), and treatment-dependent misclassification ($\\approx$90\\% at $\\gamma_T \\leq 0.05$; Appendices~\\ref{app:hatespeech}--\\ref{app:treatment_dep}).\nSemi-synthetic evaluation uses empirical LLM confusion matrices from 16 model--dataset--$K$ combinations (8 LLMs $\\times$ 2 datasets $\\times$ varying $K$); of these, 11 have sufficient subgroup variation for $R^2$ regression and 13 have $K{=}4$ for $\\kappa$ analysis.\n\n\\subsection{Empirical Validation of the Bias Identity}\n\\label{sec:bias_mechanism}\n\nWe verify Theorem~\\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\\Delta\\pi \\in [0, 0.25]$, $\\Delta\\tau \\in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\\ref{app:dgp}).\nRegressing observed subgroup bias on $\\delta_s \\cdot \\Delta\\tau / (1{-}2\\bar{\\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.97$ ($K{=}4$); residual variance reflects MC noise ($R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\\ref{app:classimbalance}).\nGlobal correction worsens bias in 50\\% of $K{=}2$ configurations (260/520, excluding $\\Delta\\pi{=}0$), with amplification reaching 2.86$\\times$ ($K{=}2$) and 2.41$\\times$ ($K{=}4$); Figure~\\ref{fig:heatmap} visualizes the amplification surface.\nBeyond amplification, global correction reverses the sign of estimated CATE---concluding a protective treatment is harmful---in 14.9\\% of configurations at $\\tau(0) = 0.03$ (31\\% at $\\tau(0) = 0.01$; critical threshold $\\tau(0) < 0.089$, matching Theorem~\\ref{thm:bias_identity}), with all eight real LLMs amplifying bias under global correction; EC-HTE eliminates sign reversal entirely (Figure~\\ref{fig:sign_reversal}; Appendix~\\ref{app:policy_reversal}).\n\n\\subsection{Correction Evaluation}\n\\label{sec:ec_hte_eval}\n\nTable~\\ref{tab:main_results} presents the main results across representative configurations.\nIn the $K{=}2$ extreme row, global correction \\emph{increases} $|\\text{bias}|$ relative to naive (0.059 vs.\\ 0.058), confirming the over-correction mechanism of Theorem~\\ref{thm:bias_identity}.\nF-L scalar correction increases $|\\text{bias}|$ to 0.122 (coverage 0.68); F-L per-subgroup to 0.168 as $(1{-}2\\pi_s) \\to 0$---both worse than naive (Table~\\ref{tab:main_results}).\nHB EC-HTE reduces $|\\text{bias}|$ from 0.059 to 0.008 (7.4$\\times$); relative to stratified MLE (0.012), the advantage is 1.5$\\times$ with lower RMSE from partial pooling. At $K{=}4$, bias reduces from 0.056 to 0.012 (4.7$\\times$), maintaining near-nominal coverage (0.94--0.96).\nUnder moderate heterogeneity and in TweetEval ($K{=}4$), methods converge ($p > 0.05$); EC-HTE incurs higher RMSE when $\\Delta\\pi$ is small (Table~\\ref{tab:main_supp}).\nAt $K{=}8$ ($n_{\\text{expert}}/K{=}31$), coverage remains $\\geq$95.6\\% but RMSE increases; we recommend $n_{\\text{expert}}/K \\geq 50$ (Appendix~\\ref{app:k8_subgroups}).\n\n\\paragraph{CausalForest.}\nTheorem~\\ref{thm:bias_identity} applies to any estimator whose inputs pass through a confusion matrix; CausalForest~\\cite{wager2018causal} with a noisy effect modifier $\\hat{Z}$ inherits the same $M_{\\text{global}}^{-1} M_s$ structure.\nWith CausalForest ($K{=}4$, extreme, $n{=}500$), EC-HTE reduces $|\\text{bias}|$ from 0.191 to 0.039 (4.9$\\times$) with coverage 0.90; global amplifies bias up to 5.9$\\times$ (Table~\\ref{tab:main_results}; bootstrap SE in Appendix~\\ref{app:bootstrap_se}).\nThe identity and correction are estimator-agnostic: R-learner yields comparable bias reduction (89\\%, Appendix~\\ref{app:rlearner}), confirming that the product-form bias arises from the confusion matrix structure, not the downstream estimator.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\\text{bias}|$. $^\\dagger$RMSE exceeds Global. F-L Scalar: $\\hat{\\tau}/(1{-}2\\bar{\\pi})$~\\cite{frazis2003estimating}; F-L Per-sub.: per-subgroup variant (binary $Z$ only). Moderate/TweetEval in Table~\\ref{tab:main_supp}; MC SEs $\\leq 0.005$ for all entries (Appendix~\\ref{app:mcse}).\\protect\\footnotemark}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & 95\\% CI Cov. \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{DIM\\\\$K{=}2$, $n{=}250$}}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & Global & 0.059 & 0.099 & 0.87 \\\\\n & F-L Scalar & 0.122 & 0.159 & 0.68 \\\\\n & F-L Per-sub. & 0.168 & 0.220 & 0.65 \\\\\n & Strat.\\ MLE & 0.012 & 0.094 & 0.95 \\\\\n & HB EC-HTE & \\textbf{0.008} & 0.089 & 0.94 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{DIM\\\\$K{=}4$, $n{=}500$}}\n & Naive & 0.062 & 0.113 & 0.88 \\\\\n & Global & 0.056 & 0.125 & 0.91 \\\\\n & Strat.\\ MLE & \\textbf{0.010} & 0.127$^\\dagger$ & 0.95 \\\\\n & HB EC-HTE & 0.012 & 0.120 & 0.96 \\\\\n\\midrule\n\\multirow{3}{*}{\\shortstack[l]{CausalForest\\\\$K{=}4$, $n{=}500$}}\n & Naive & 0.208 & 0.231 & 0.44 \\\\\n & Global & 0.191 & 0.244 & 0.58 \\\\\n & EC-HTE Forest & \\textbf{0.039} & 0.180 & 0.90 \\\\\n\\bottomrule\n\\end{tabular}}\n\\footnotetext{CausalForest plug-in SE achieves 93.8\\% aggregate coverage; a bootstrap procedure ($B{=}100$) recovers $\\geq$95\\% coverage at all budgets tested (Appendix~\\ref{app:bootstrap_se}).}\n\\end{table}\n\n\\subsection{Actionable Diagnostic}\n\\label{sec:diagnostic}\n\nProposition~\\ref{prop:debiasing_hurts} provides a $\\Delta\\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\\delta_s| / ((1-2\\bar{\\pi}) \\cdot \\pi_s) > 1$, computable from a pilot sample without estimating treatment effects.\nThe diagnostic achieves AUC $= 0.63$ across 16 semi-synthetic LLM--dataset combinations; restricting to subgroups with $\\Delta\\tau > 0$ recovers AUC $= 1.0$ ($0.86$ on synthetic grids; Figure~\\ref{fig:roc}, Appendix~\\ref{app:screening}).\nThe lower AUC reflects inclusion of subgroups with $\\Delta\\tau \\approx 0$, where misdiagnosis is inconsequential---global and stratified correction perform identically when effect heterogeneity is absent.\nFor $K{=}2$, $|\\delta_0|{=}|\\delta_1|$ limits discrimination (Appendix~\\ref{app:screening}).\n\nThe condition number $\\kappa(\\hat{C}_s)$ provides a practical guard: $\\kappa > 100$ triggers fallback; all 13 tested LLM--dataset combinations fall in $\\kappa \\in (1.25, 3]$ with calibrated coverage $\\geq$93\\% (Appendix~\\ref{app:kappa_analysis}).\nBudget crossover, $K{=}8$ scalability, and multi-LLM validation ($R^2 = 0.975$) appear in Appendices~\\ref{sec:budget}--\\ref{app:multilm}.\n\nOn a real hate speech dataset ($\\Delta\\pi{=}0.117$; Appendix~\\ref{app:hatespeech}), EC-HTE underperforms both naive and global correction, consistent with most real LLMs exhibiting $\\Delta\\pi \\in [0.10, 0.20]$ (Appendices~\\ref{app:multilm}--\\ref{app:civilcomments}).\n\n\\paragraph{Operating conditions.}\nEC-HTE requires: (i)~$\\Delta\\pi > 0.15$, (ii)~$n_{\\text{expert}} \\geq 250$ for $K{=}2$, (iii)~$\\text{FNR}_s < 0.50$, and (iv)~$K \\leq 4$; when unmet, global correction is preferable (Appendix~\\ref{app:k8_subgroups}).\nUnder confounded treatment, pairing with IPW-DIM maintains $\\geq$94.5\\% coverage (Appendix~\\ref{app:confounded_dgp}).",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_015E8BiHpQChkhgaGiGTwnBd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "47dee244-c515-4cb4-86e5-e197ab78ff96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 21 · 2026-05-24T04:29:12.719Z_

<details><summary>↩ Tool result · `toolu_015E8BiHpQChkhgaGiGTwnBd`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Standard confusion-matrix correction---the default in PPI, DSL, and CSS practice---can reverse causal conclusions when misclassification rates vary across subgroups.
4	We derived an exact bias identity explaining when and why, verified across synthetic grids and semi-synthetic evaluations using 11 empirical LLM confusion matrices.
5	The identity yields a diagnostic that flags harmful correction from error rates alone, and prescribes per-subgroup correction that eliminates sign reversal given sufficient error heterogeneity; when these conditions are not met, practitioners should prefer global correction.
6	The framework applies wherever LLM annotations replace structured covariates and annotation error rates vary across subpopulations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "35c614c6-3d78-4a99-9f51-5c26dab61a75",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nStandard confusion-matrix correction---the default in PPI, DSL, and CSS practice---can reverse causal conclusions when misclassification rates vary across subgroups.\nWe derived an exact bias identity explaining when and why, verified across synthetic grids and semi-synthetic evaluations using 11 empirical LLM confusion matrices.\nThe identity yields a diagnostic that flags harmful correction from error rates alone, and prescribes per-subgroup correction that eliminates sign reversal given sufficient error heterogeneity; when these conditions are not met, practitioners should prefer global correction.\nThe framework applies wherever LLM annotations replace structured covariates and annotation error rates vary across subpopulations.",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_0192XSxTkEDQitz1aVXHoDQ6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "898b80a2-b97b-4d95-8ec1-0be696f3f808",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 23 · 2026-05-24T04:29:13.604Z_

<details><summary>↩ Tool result · reported error · `toolu_0192XSxTkEDQitz1aVXHoDQ6`</summary>

```text
File content (39764 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "334d4f84-6ee7-47c0-8de6-1cef7cfc3f6b",
  "tool_use_result": "Error: File content (39764 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01V4nUUgKXay3ELaDdxc53Wb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "dd5a745d-0afd-46c0-b7b9-05154068a7f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 25 · 2026-05-24T04:29:13.880Z_

<details><summary>↩ Tool result · `toolu_01V4nUUgKXay3ELaDdxc53Wb`</summary>

```text
1	\subsection{Stance Detection: Cross-Task Sign Reversal Validation}
2	\label{app:stance}
3	
4	To test whether global correction introduces sign reversals beyond sentiment and toxicity, we extend the semi-synthetic evaluation to stance detection using TweetEval~\cite{barbieri2020tweeteval}.
5	The binary label is \emph{favor} ($Z{=}1$) vs.\ \emph{not-favor} ($Z{=}0$) toward five stance targets (Atheism, Climate Change, Feminist Movement, Hillary Clinton, Abortion), yielding $K{=}5$ subgroups with $n{=}300$ each.
6	CATE heterogeneity is $\tau(\text{favor}){=}0.20$, $\tau(\text{not-favor}){=}0.05$, with 200 MC replications.
7	GPT-4o annotations are from the real API; GPT-4o-mini and GPT-3.5-Turbo use simulated error profiles (FPR/FNR scaling $+$ additive shift; see Appendix~\ref{app:dgp}).
8	
9	Table~\ref{tab:stance_signrev} reports subgroups with sign reversal or $\kappa > 3$.
10	Global correction produces sign reversals in 4/30 subgroup-$z$ combinations (13.3\%); EC-HTE reduces this to 1/30 (3.3\%); the remaining reversal occurs in an ill-conditioned subgroup ($\kappa{=}15.0$, GPT-3.5-Turbo Climate Change) that violates the operating conditions of Section~\ref{sec:ec_hte_eval}.
11	Global correction amplifies bias in 15/30 cases (50\%).
12	
13	The stance task exposes an operating-conditions limitation: GPT-3.5-Turbo achieves FNR ${>}\,0.50$ on all five targets, violating the classifier quality precondition and producing $\kappa$ values up to 15.0 (Climate Change) vs.\ 4.6 (Hillary Clinton)---a ${\sim}10{\times}$ range within the same LLM.
14	This $\kappa$ heterogeneity inflates correction variance; EC-HTE preserves sign correctness but at the cost of higher variance when $\kappa \gg 3$.
15	Mean RMSE: naive${=}0.116$, global${=}0.272$, EC-HTE${=}0.271$; correction reduces sign reversals but does not improve overall RMSE at $K{=}5$, $n{=}300$ per subgroup---consistent with the operating-conditions threshold $n_{\text{expert}}/K \geq 50$.
16	Practitioners should verify per-subgroup FNR before applying correction.
17	
18	\begin{table}[h]
19	\centering
20	\caption{Stance detection: subgroups with sign reversal or $\kappa > 3$. \checkmark\ indicates at least one $z$-level affected. GPT-4o-mini and GPT-3.5-Turbo use simulated error profiles.}
21	\label{tab:stance_signrev}
22	\small
23	\begin{tabular}{llcccc}
24	\toprule
25	LLM & Target & $\kappa$ & \makecell{Sign Rev\\(Global)} & \makecell{Sign Rev\\(EC-HTE)} & \makecell{Bias Amp\\(Global)} \\
26	\midrule
27	GPT-4o & Fem.\ Mov.\ & 1.79 & \checkmark & --- & \checkmark \\
28	GPT-4o & Hillary C.\ & 1.86 & \checkmark & --- & \checkmark \\
29	\midrule
30	GPT-3.5-T & Atheism & 7.21 & --- & --- & --- \\
31	GPT-3.5-T & Climate Ch.\ & 15.01 & --- & \checkmark & \checkmark \\
32	GPT-3.5-T & Fem.\ Mov.\ & 3.28 & \checkmark & --- & \checkmark \\
33	GPT-3.5-T & Hillary C.\ & 4.60 & \checkmark & --- & \checkmark \\
34	GPT-3.5-T & Abortion & 14.17 & --- & --- & \checkmark \\
35	\bottomrule
36	\end{tabular}
37	\end{table}
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "a7912844-53b7-4c66-9aa9-a77e3f8f19ca",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix_stance.tex",
      "content": "\\subsection{Stance Detection: Cross-Task Sign Reversal Validation}\n\\label{app:stance}\n\nTo test whether global correction introduces sign reversals beyond sentiment and toxicity, we extend the semi-synthetic evaluation to stance detection using TweetEval~\\cite{barbieri2020tweeteval}.\nThe binary label is \\emph{favor} ($Z{=}1$) vs.\\ \\emph{not-favor} ($Z{=}0$) toward five stance targets (Atheism, Climate Change, Feminist Movement, Hillary Clinton, Abortion), yielding $K{=}5$ subgroups with $n{=}300$ each.\nCATE heterogeneity is $\\tau(\\text{favor}){=}0.20$, $\\tau(\\text{not-favor}){=}0.05$, with 200 MC replications.\nGPT-4o annotations are from the real API; GPT-4o-mini and GPT-3.5-Turbo use simulated error profiles (FPR/FNR scaling $+$ additive shift; see Appendix~\\ref{app:dgp}).\n\nTable~\\ref{tab:stance_signrev} reports subgroups with sign reversal or $\\kappa > 3$.\nGlobal correction produces sign reversals in 4/30 subgroup-$z$ combinations (13.3\\%); EC-HTE reduces this to 1/30 (3.3\\%); the remaining reversal occurs in an ill-conditioned subgroup ($\\kappa{=}15.0$, GPT-3.5-Turbo Climate Change) that violates the operating conditions of Section~\\ref{sec:ec_hte_eval}.\nGlobal correction amplifies bias in 15/30 cases (50\\%).\n\nThe stance task exposes an operating-conditions limitation: GPT-3.5-Turbo achieves FNR ${>}\\,0.50$ on all five targets, violating the classifier quality precondition and producing $\\kappa$ values up to 15.0 (Climate Change) vs.\\ 4.6 (Hillary Clinton)---a ${\\sim}10{\\times}$ range within the same LLM.\nThis $\\kappa$ heterogeneity inflates correction variance; EC-HTE preserves sign correctness but at the cost of higher variance when $\\kappa \\gg 3$.\nMean RMSE: naive${=}0.116$, global${=}0.272$, EC-HTE${=}0.271$; correction reduces sign reversals but does not improve overall RMSE at $K{=}5$, $n{=}300$ per subgroup---consistent with the operating-conditions threshold $n_{\\text{expert}}/K \\geq 50$.\nPractitioners should verify per-subgroup FNR before applying correction.\n\n\\begin{table}[h]\n\\centering\n\\caption{Stance detection: subgroups with sign reversal or $\\kappa > 3$. \\checkmark\\ indicates at least one $z$-level affected. GPT-4o-mini and GPT-3.5-Turbo use simulated error profiles.}\n\\label{tab:stance_signrev}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nLLM & Target & $\\kappa$ & \\makecell{Sign Rev\\\\(Global)} & \\makecell{Sign Rev\\\\(EC-HTE)} & \\makecell{Bias Amp\\\\(Global)} \\\\\n\\midrule\nGPT-4o & Fem.\\ Mov.\\ & 1.79 & \\checkmark & --- & \\checkmark \\\\\nGPT-4o & Hillary C.\\ & 1.86 & \\checkmark & --- & \\checkmark \\\\\n\\midrule\nGPT-3.5-T & Atheism & 7.21 & --- & --- & --- \\\\\nGPT-3.5-T & Climate Ch.\\ & 15.01 & --- & \\checkmark & \\checkmark \\\\\nGPT-3.5-T & Fem.\\ Mov.\\ & 3.28 & \\checkmark & --- & \\checkmark \\\\\nGPT-3.5-T & Hillary C.\\ & 4.60 & \\checkmark & --- & \\checkmark \\\\\nGPT-3.5-T & Abortion & 14.17 & --- & --- & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01UEirwDJvxdBB23CirkcbZd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "c939ed4e-6325-4db5-8674-b1c95e972ba7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 27 · 2026-05-24T04:29:14.134Z_

<details><summary>↩ Tool result · `toolu_01UEirwDJvxdBB23CirkcbZd`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Per-subgroup correction requires $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ expert labels per subgroup and moderate classifier accuracy ($\text{FPR}_s, \text{FNR}_s < 0.5$); below these thresholds, stratification incurs more variance than the bias it removes.
5	At $K{=}8$ with $n_{\text{expert}}{=}250$ (${\approx}31$ labels/subgroup), coverage remains nominal ($\geq$95.6\%) but RMSE exceeds global correction, establishing a scalability boundary under fixed expert budget (Appendix~\ref{app:k8_subgroups}).
6	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) achieves AUC $= 0.86$ on synthetic data but degrades to $0.63$ on real LLM confusion matrices (Appendix~\ref{app:screening}); it should be paired with $R^2$ validation of the bias identity rather than used as a standalone rule.
7	
8	Assumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable.
9	Sensitivity analysis shows robustness up to $\gamma = 0.2$ for outcome-dependent misclassification (coverage $\geq$93.5\%; Appendix~\ref{app:a1_sensitivity}) and $\gamma_T \leq 0.05$ for treatment-dependent misclassification (coverage $\geq$89.7\%; Appendix~\ref{app:treatment_dep}).
10	
11	The method requires discrete, pre-specified subgroups; continuous effect modifiers require discretization, and data-driven subgroup discovery risks overfitting.
12	Ground-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so we use synthetic CATE injection on real text features and real LLM annotations (Appendices~\ref{app:dgp},~\ref{app:multilm}).
13	Code and data generation scripts will be released upon acceptance.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "49fa2a54-badc-4e05-91ca-00d52754869d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nPer-subgroup correction requires $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ expert labels per subgroup and moderate classifier accuracy ($\\text{FPR}_s, \\text{FNR}_s < 0.5$); below these thresholds, stratification incurs more variance than the bias it removes.\nAt $K{=}8$ with $n_{\\text{expert}}{=}250$ (${\\approx}31$ labels/subgroup), coverage remains nominal ($\\geq$95.6\\%) but RMSE exceeds global correction, establishing a scalability boundary under fixed expert budget (Appendix~\\ref{app:k8_subgroups}).\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) achieves AUC $= 0.86$ on synthetic data but degrades to $0.63$ on real LLM confusion matrices (Appendix~\\ref{app:screening}); it should be paired with $R^2$ validation of the bias identity rather than used as a standalone rule.\n\nAssumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable.\nSensitivity analysis shows robustness up to $\\gamma = 0.2$ for outcome-dependent misclassification (coverage $\\geq$93.5\\%; Appendix~\\ref{app:a1_sensitivity}) and $\\gamma_T \\leq 0.05$ for treatment-dependent misclassification (coverage $\\geq$89.7\\%; Appendix~\\ref{app:treatment_dep}).\n\nThe method requires discrete, pre-specified subgroups; continuous effect modifiers require discretization, and data-driven subgroup discovery risks overfitting.\nGround-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so we use synthetic CATE injection on real text features and real LLM annotations (Appendices~\\ref{app:dgp},~\\ref{app:multilm}).\nCode and data generation scripts will be released upon acceptance.\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01R2PKmPA8J1xLd5kJVwyXsw`</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "fields": [
    "*"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "6c3091e6-4507-45cd-a08d-b1d5833e13f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNUJSyUAFKJvKBfchcGRgF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1755,
      "cache_read_input_tokens": 24671,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1755
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

_source line 29 · 2026-05-24T04:29:15.311Z_

<details><summary>↩ Tool result · `toolu_01R2PKmPA8J1xLd5kJVwyXsw`</summary>

```text
Error: result (74,416 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "08654609-f73f-473d-9c85-f6196db8b737",
  "tool_use_result": {
    "content": "Error: result (74,416 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp-040\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:54:23.294Z\", \"updated_at\": \"2026-05-23T15:55:16.698Z\", \"hypothesis\": \"EC-HTE is robust to moderate treatment-dependent misclassification (γ_T≤0.05, coverage ≥89.7%) but degrades at γ_T≥0.10 because per-subgroup CM estimates become biased when expert sample treatment composition doesn't match the full sample.\", \"spec\": {\"command\": \"python exp_treatment_dep_misclass.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP K=2 extreme\", \"data_count\": 5000, \"model_name\": \"DIM+HB\", \"seed\": 0, \"checkpoint_path\": \"artifacts/treatment_dep_misclass_figure.pdf\", \"log_path\": \"artifacts/treatment_dep_misclass_summary.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"gamma0_cov\": 0.945, \"gamma0_rmse\": 0.075, \"gamma005_cov\": 0.897, \"gamma005_rmse\": 0.092, \"gamma010_cov\": 0.75, \"gamma010_rmse\": 0.133, \"gamma015_cov\": 0.525, \"gamma015_rmse\": 0.177, \"gamma020_cov\": 0.37, \"gamma020_rmse\": 0.224, \"breakeven_gamma\": 0.1}, \"completed_at\": \"2026-05-23T15:55:16.698Z\"}, \"exp-039\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:54:20.391Z\", \"updated_at\": \"2026-05-23T15:55:15.899Z\", \"hypothesis\": \"EC-HTE dominates at K=2/4 (bias reduction 5-7×) but degrades at K=8 with fixed n_expert=250 (~31 labels/subgroup), establishing K=8 as a scalability boundary where per-subgroup CM estimation variance exceeds bias correction gains.\", \"spec\": {\"command\": \"python exp030_k8_subgroups.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP K=8\", \"data_count\": 5000, \"model_name\": \"DIM+HB\", \"seed\": 0, \"checkpoint_path\": \"artifacts/k_scalability_bars.pdf\", \"log_path\": \"artifacts/k_scalability_comparison.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"K2_echte_bias\": 0.008, \"K2_echte_rmse\": 0.089, \"K2_echte_cov\": 0.938, \"K4_echte_bias\": 0.012, \"K4_echte_rmse\": 0.12, \"K4_echte_cov\": 0.956, \"K8_echte_bias\": 0.183, \"K8_echte_rmse\": 0.34, \"K8_echte_cov\": 0.956, \"K8_global_rmse\": 0.168}, \"completed_at\": \"2026-05-23T15:55:15.899Z\"}, \"exp-038\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:54:13.229Z\", \"updated_at\": \"2026-05-23T15:54:44.973Z\", \"hypothesis\": \"When true CATE is small (τ(0)<0.05), global correction's over-correction bias exceeds the true effect magnitude, causing sign reversal in CATE estimates — converting beneficial treatments into apparently harmful ones. EC-HTE's per-subgroup correction never causes sign reversal.\", \"spec\": {\"command\": \"python policy_reversal_sweep.py\", \"server\": \"local-cpu\", \"data_path\": \"results/exp002_bias_bound.csv\", \"data_count\": 520, \"model_name\": \"analytic\", \"seed\": 0, \"checkpoint_path\": \"artifacts/policy_reversal_zone.pdf\", \"log_path\": \"artifacts/policy_reversal_zone.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"reversal_pct_tau001\": 31, \"reversal_pct_tau003\": 14.9, \"reversal_pct_tau005\": 6.1, \"reversal_pct_tau010\": 0, \"ec_hte_reversal_pct\": 0, \"worst_combo\": \"tau=0.01, delta_misclass=0.19 → 42.9%\"}, \"completed_at\": \"2026-05-23T15:54:44.973Z\"}, \"exp-036\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:40:48.269Z\", \"updated_at\": \"2026-05-23T03:44:06.512Z\", \"hypothesis\": \"Bootstrap SE (B=200, re-estimating CM + re-fitting CF per bootstrap) can close the CausalForest under-coverage gap (91% vs nominal 95%) by properly accounting for CM estimation uncertainty that plug-in SE ignores.\", \"spec\": {\"command\": \"python3 exp036_bootstrap_se.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP K=2 N=5000\", \"data_count\": 5000, \"model_name\": \"CausalForestDML\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"results/exp036_log.txt\"}, \"conclusion\": \"success\", \"metrics\": {\"source\": \"results/exp_bootstrap_se_v2_summary.csv\", \"note\": \"v2 with n_estimators=200 (fixes v1 n_estimators=48 artifact)\", \"plugin_coverage\": 0.9375, \"bootstrap_coverage\": 0.95, \"oracle_coverage\": 0.9, \"coverage_improvement\": 0.0125, \"plugin_se_mean\": 0.073, \"bootstrap_se_mean\": 0.083, \"se_ratio_boot_over_plugin\": 1.154, \"s0_plugin_cov\": 0.95, \"s0_bootstrap_cov\": 0.925, \"s1_plugin_cov\": 0.925, \"s1_bootstrap_cov\": 0.975, \"s1_se_ratio\": 1.222, \"n_mc\": 20, \"n_bootstrap\": 100, \"n_estimators\": 200, \"runtime_sec\": 1716, \"key_finding\": \"With correct n_estimators=200, plugin SE already near-nominal (93.8%). Bootstrap provides modest improvement to exact 95.0%. v1 '81.7% → 94.2%' gap was artifact of n_estimators=48.\"}, \"completed_at\": \"2026-05-23T02:32:12.942Z\"}, \"exp-037\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:39:22.761Z\", \"updated_at\": \"2026-05-23T01:42:03.462Z\", \"hypothesis\": \"Temperature scaling reduces per-subgroup misclassification rates but does NOT eliminate heterogeneity (Δπ shrinks from 0.20 to 0.07 but remains nonzero), so EC-HTE is still necessary post-calibration. Calibrated+EC-HTE should achieve the best coverage.\", \"spec\": {\"command\": \"python3 exp037_calibration.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP K=2 N=5000\", \"data_count\": 5000, \"model_name\": \"DIM\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"results/exp037_log.txt\"}, \"conclusion\": \"success\", \"metrics\": {\"source\": \"results/exp_calibration_summary.csv\", \"calibrated_echte_abs_bias\": 0.0554, \"calibrated_echte_coverage\": 0.965, \"calibrated_global_abs_bias\": 0.055, \"calibrated_global_coverage\": 0.963, \"calibrated_naive_abs_bias\": 0.051, \"calibrated_naive_coverage\": 0.912, \"uncalibrated_echte_abs_bias\": 0.0641, \"uncalibrated_echte_coverage\": 0.938, \"uncalibrated_global_abs_bias\": 0.0695, \"uncalibrated_global_coverage\": 0.92, \"uncalibrated_naive_abs_bias\": 0.0634, \"uncalibrated_naive_coverage\": 0.84, \"oracle_abs_bias\": 0.0431, \"oracle_coverage\": 0.963, \"delta_pi_uncalibrated\": 0.2, \"delta_pi_calibrated\": 0.07, \"key_finding\": \"Calibration reduces Δπ from 0.20 to 0.07 and improves naive coverage (84.0%→91.2%) but doesn't reach nominal 95%. Calibrated+EC-HTE achieves best coverage (96.5%) — EC-HTE corrects residual heterogeneity post-calibration. Calibrated+Naive still under-covers by 3.8pp. EC-HTE and calibration are complementary, not substitutes.\"}, \"completed_at\": \"2026-05-23T01:42:03.462Z\"}, \"exp-035\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:39:21.071Z\", \"updated_at\": \"2026-05-23T01:41:52.292Z\", \"hypothesis\": \"EC-HTE with asymmetric CM estimation (full 2x2 FPR/FNR) maintains coverage >=93% under realistic 7:1 FPR/FNR ratios (simulating GPT-4.1 on Civil Comments), and outperforms the symmetric assumption (FPR=FNR) in both RMSE and coverage.\", \"spec\": {\"command\": \"python3 exp035_asymmetric_cm.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP K=2 N=5000 asymmetric CM\", \"data_count\": 5000, \"model_name\": \"DIM\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"results/exp035_log.txt\"}, \"conclusion\": \"success\", \"metrics\": {\"source\": \"results/exp_asymmetric_cm_summary.csv\", \"echte_asym_abs_bias\": 0.057, \"echte_asym_rmse\": 0.0735, \"echte_asym_coverage\": 0.945, \"echte_sym_abs_bias\": 0.0618, \"echte_sym_rmse\": 0.0831, \"echte_sym_coverage\": 0.93, \"global_asym_abs_bias\": 0.0609, \"global_asym_coverage\": 0.915, \"global_sym_abs_bias\": 0.0629, \"global_sym_coverage\": 0.915, \"naive_abs_bias\": 0.0592, \"naive_coverage\": 0.87, \"oracle_abs_bias\": 0.0454, \"oracle_coverage\": 0.943, \"asym_vs_sym_echte_rmse_delta\": -0.0096, \"asym_vs_sym_echte_cov_delta\": 0.015, \"s1_echte_asym_cov\": 0.93, \"s1_echte_sym_cov\": 0.91, \"key_finding\": \"EC-HTE asymmetric achieves 94.5% coverage (vs 93.0% symmetric) under 7:1 FPR/FNR ratio. RMSE improved 11.5% (0.0831→0.0735). Asymmetric formula essential for high FPR/FNR ratios. s1 (high-error) coverage: 93.0% asymmetric vs 91.0% symmetric.\"}, \"completed_at\": \"2026-05-23T01:41:52.292Z\"}, \"exp-034\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T01:39:16.724Z\", \"updated_at\": \"2026-05-23T01:41:40.218Z\", \"hypothesis\": \"F-L scalar correction (tau_obs/(1-2*pi_bar)) predicts bias direction incorrectly under subgroup heterogeneity because it uses a single global scaling factor that over-corrects low-error subgroups and under-corrects high-error subgroups. EC-HTE's CM inversion handles the sign-reversal correctly.\", \"spec\": {\"command\": \"python3 exp034_fl_comparison.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP K=2 N=5000\", \"data_count\": 5000, \"model_name\": \"DIM\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"results/exp034_log.txt\"}, \"conclusion\": \"success\", \"metrics\": {\"source\": \"results/exp_fl_comparison_summary.csv\", \"fl_scalar_abs_bias\": 0.0909, \"fl_scalar_rmse\": 0.1161, \"fl_scalar_coverage\": 0.85, \"fl_per_subgroup_abs_bias\": 0.112, \"fl_per_subgroup_rmse\": 0.1582, \"fl_per_subgroup_coverage\": 0.838, \"echte_abs_bias\": 0.0643, \"echte_rmse\": 0.0858, \"echte_coverage\": 0.953, \"global_cm_abs_bias\": 0.0643, \"global_cm_rmse\": 0.0806, \"global_cm_coverage\": 0.938, \"naive_abs_bias\": 0.0621, \"naive_coverage\": 0.858, \"oracle_abs_bias\": 0.0454, \"oracle_coverage\": 0.943, \"sign_reversal\": \"F-L Scalar: s0=+0.073 s1=+0.068, both positive (no sign-reversal). F-L Per-Subgroup: s0=+0.024 s1=+0.160. EC-HTE: s0=+0.006 s1=+0.001 (near-zero bias both subgroups)\", \"key_finding\": \"F-L scalar and F-L per-subgroup both WORSE than naive on aggregate |bias|. F-L scalar over-corrects s0 (bias +0.073 vs naive +0.005). F-L per-subgroup dramatically over-corrects s1 (bias +0.160). EC-HTE achieves near-zero per-subgroup bias with nominal coverage (95.3%). CM inversion fundamentally different from F-L scalar rescaling.\"}, \"completed_at\": \"2026-05-23T01:41:40.218Z\"}, \"exp-033\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:47:48.539Z\", \"updated_at\": \"2026-05-22T21:48:31.124Z\", \"hypothesis\": \"Adaptive shrinkage (stronger alpha for high-pi subgroups) and/or kappa-threshold fallback can reduce K=8 HB RMSE from 0.340 toward Global's 0.168, narrowing the scalability gap.\", \"parent\": \"exp-030\", \"spec\": {\"command\": \"python exp033_k8_adaptive.py\", \"server\": \"local\", \"data_path\": \"synthetic_dgp_k8\", \"data_count\": 5000, \"model_name\": \"DIM_estimator\", \"seed\": 42, \"checkpoint_path\": \"results/exp_k8_adaptive.csv\", \"log_path\": \"results/exp_k8_adaptive_summary.csv\", \"checkpoint_source\": \"exp-030\", \"eval_data\": \"synthetic_dgp_k8_adaptive_variants\"}, \"conclusion\": \"negative\", \"metrics\": {\"hb_baseline_rmse\": 0.333, \"hb_baseline_coverage\": 0.959, \"v1_adaptive_alpha_rmse\": 0.216, \"v1_adaptive_alpha_coverage\": 0.96, \"v2_kappa_fallback_rmse\": 0.25, \"v2_kappa_fallback_coverage\": 0.96, \"v3_combined_rmse\": 0.216, \"v3_combined_coverage\": 0.96, \"global_rmse\": 0.166, \"global_coverage\": 0.958, \"v1_vs_baseline_improvement_pct\": 35, \"v1_still_exceeds_global_pct\": 30, \"source\": \"results/exp_k8_adaptive_summary.csv\", \"note\": \"V1 (adaptive alpha) reduces RMSE 35% (0.333->0.216) but still exceeds Global (0.166). Gap narrowed from 2x to 1.3x. Confirms boundary is real but mitigable.\"}, \"completed_at\": \"2026-05-22T21:48:31.124Z\"}, \"exp-032\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:30:10.921Z\", \"updated_at\": \"2026-05-22T20:31:26.532Z\", \"hypothesis\": \"EC-HTE + IPW-DIM maintains coverage ≥90% across confounding strengths β∈{0.25, 0.5, 1.0, 2.0}, and estimated propensity (logistic regression) yields <3pp coverage difference vs oracle propensity.\", \"parent\": \"exp-031\", \"spec\": {\"command\": \"python exp032_confounded_sweep.py\", \"server\": \"local\", \"data_path\": \"synthetic_dgp_confounded_sweep\", \"data_count\": 5000, \"model_name\": \"IPW-DIM_estimator\", \"seed\": 42, \"checkpoint_path\": \"results/exp_confounded_sweep.csv\", \"log_path\": \"results/exp_confounded_sweep_summary.csv\", \"checkpoint_source\": \"exp-031\", \"eval_data\": \"synthetic_dgp_confounded_sweep_2x4_grid\"}, \"conclusion\": \"success\", \"metrics\": {\"min_hb_coverage\": 0.945, \"max_oracle_vs_est_gap\": 0.01, \"hb_cov_b0.25_oracle\": 0.9625, \"hb_cov_b0.25_estimated\": 0.9725, \"hb_cov_b0.5_oracle\": 0.95, \"hb_cov_b0.5_estimated\": 0.9575, \"hb_cov_b1.0_oracle\": 0.9575, \"hb_cov_b1.0_estimated\": 0.96, \"hb_cov_b2.0_oracle\": 0.945, \"hb_cov_b2.0_estimated\": 0.9475, \"hb_rmse_b2.0_oracle\": 0.1258, \"naive_cov_range\": \"0.845-0.898\", \"source\": \"results/exp_confounded_sweep_summary.csv\", \"note\": \"All 8 configs HB coverage >=94.5%. Oracle vs estimated gap <=1pp. Hypothesis fully confirmed.\"}, \"completed_at\": \"2026-05-22T20:31:26.532Z\"}, \"exp-031\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:39:36.830Z\", \"updated_at\": \"2026-05-22T19:49:39.258Z\", \"hypothesis\": \"EC-HTE under confounded treatment assignment (T depends on covariates via logistic model, not Bernoulli(0.5)) maintains coverage ≥93% when paired with IPW-DIM estimator, demonstrating compatibility with observational study designs.\", \"spec\": {\"command\": \"python exp031_confounded_dgp.py\", \"server\": \"local\", \"data_path\": \"synthetic_dgp_confounded\", \"data_count\": 5000, \"model_name\": \"IPW-DIM_estimator\", \"seed\": 42, \"checkpoint_path\": \"results/exp_confounded_dgp.csv\", \"log_path\": \"results/exp_confounded_dgp_summary.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"hb_echte_coverage\": 0.95, \"hb_echte_rmse\": 0.086, \"hb_echte_mean_abs_bias\": 0.068, \"oracle_coverage\": 0.943, \"oracle_rmse\": 0.061, \"oracle_mean_abs_bias\": 0.048, \"global_coverage\": 0.93, \"global_rmse\": 0.087, \"global_mean_abs_bias\": 0.071, \"strat_mle_coverage\": 0.95, \"strat_mle_rmse\": 0.087, \"strat_mle_mean_abs_bias\": 0.069, \"naive_coverage\": 0.863, \"naive_rmse\": 0.083, \"naive_mean_abs_bias\": 0.066, \"beta_confound\": 0.5, \"propensity_range\": \"0.38-0.62\", \"source\": \"results/exp_confounded_dgp_summary.csv\", \"note\": \"EC-HTE + IPW-DIM coverage 95.0% under moderate confounding. Global 93.0%. Naive 86.3%.\"}, \"completed_at\": \"2026-05-22T19:42:43.362Z\"}, \"exp-030\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:39:34.900Z\", \"updated_at\": \"2026-05-22T19:49:34.800Z\", \"hypothesis\": \"EC-HTE HB partial pooling at K=8 (per-subgroup ~31 expert labels) maintains coverage ≥90% and RMSE advantage over Global, demonstrating scalability beyond K=4.\", \"spec\": {\"command\": \"python exp030_k8_subgroups.py\", \"server\": \"local\", \"data_path\": \"synthetic_dgp\", \"data_count\": 5000, \"model_name\": \"DIM_estimator\", \"seed\": 42, \"checkpoint_path\": \"results/exp_k8_subgroups.csv\", \"log_path\": \"results/exp_k8_subgroups_summary.csv\"}, \"conclusion\": \"negative\", \"metrics\": {\"hb_echte_coverage\": 0.956, \"hb_echte_rmse\": 0.34, \"hb_echte_mean_abs_bias\": 0.183, \"oracle_coverage\": 0.944, \"oracle_rmse\": 0.113, \"oracle_mean_abs_bias\": 0.09, \"global_coverage\": 0.951, \"global_rmse\": 0.168, \"global_mean_abs_bias\": 0.135, \"strat_mle_coverage\": 0.953, \"strat_mle_rmse\": 0.638, \"strat_mle_mean_abs_bias\": 0.219, \"naive_coverage\": 0.913, \"naive_rmse\": 0.133, \"naive_mean_abs_bias\": 0.107, \"hb_vs_mle_rmse_improvement_pct\": 47, \"per_subgroup_expert_labels\": 31, \"source\": \"results/exp_k8_subgroups_summary.csv\", \"note\": \"All CM-aware methods coverage ≥95%. HB RMSE 47% better than MLE but worse than Global. K=8 is boundary condition.\"}, \"completed_at\": \"2026-05-22T19:42:42.807Z\"}, \"exp-029\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:03:08.860Z\", \"updated_at\": \"2026-05-22T17:27:12.389Z\", \"hypothesis\": \"Under controlled violation of Assumption A1 (outcome-independent misclassification), EC-HTE coverage degrades gracefully as sensitivity parameter γ increases from 0 to 0.2, with the degradation curve quantifying the method's robustness boundary. At moderate violation (γ≤0.1), coverage remains above 90%.\", \"spec\": {\"command\": \"python exp029_a1_sensitivity.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic K=2 extreme DGP with A1 violation\", \"data_count\": 5000, \"model_name\": \"DIM estimator\", \"seed\": \"42-141 (100 MC)\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"synthetic with gamma-controlled misclassification\", \"checkpoint_path\": \"N/A (CPU simulation)\", \"log_path\": \"results/exp_a1_sensitivity.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"dgp\": \"K=2, pi=[0.05,0.25], tau(0)=0, tau(1)=0.3, N=5000, n_expert=250, 100 MC\", \"gamma_sweep\": [0, 0.05, 0.1, 0.15, 0.2], \"echte_coverage\": {\"g0.00\": 0.955, \"g0.05\": 0.955, \"g0.10\": 0.953, \"g0.15\": 0.948, \"g0.20\": 0.935}, \"echte_abs_bias\": {\"g0.00\": 0.0596, \"g0.05\": 0.0593, \"g0.10\": 0.063, \"g0.15\": 0.0652, \"g0.20\": 0.0677}, \"global_coverage\": {\"g0.00\": 0.927, \"g0.05\": 0.935, \"g0.10\": 0.938, \"g0.15\": 0.943, \"g0.20\": 0.94}, \"naive_coverage\": {\"g0.00\": 0.877, \"g0.05\": 0.838, \"g0.10\": 0.835, \"g0.15\": 0.792, \"g0.20\": 0.795}, \"key_finding\": \"EC-HTE coverage degrades gracefully: 95.5%→93.5% over gamma 0→0.2 (−2.0pp). ALL correction methods maintain ≥90% coverage across all gamma. Naive degrades fastest (87.7%→79.5%, −8.2pp). At moderate violation gamma=0.1, EC-HTE coverage=95.3% (−0.2pp from baseline). EC-HTE |bias| increases 13.7% at gamma=0.2 but remains comparable to Global.\", \"coverage_below_90_threshold\": {\"Naive\": 0, \"Global\": \"never\", \"Strat_MLE\": \"never\", \"HB_ECHTE\": \"never\"}, \"output_files\": [\"results/exp_a1_sensitivity.csv\", \"results/exp_a1_sensitivity_summary.csv\", \"results/exp_a1_sensitivity_subgroup.csv\"]}, \"completed_at\": \"2026-05-22T17:27:12.389Z\"}, \"exp-028\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:03:05.932Z\", \"updated_at\": \"2026-05-22T16:13:50.285Z\", \"hypothesis\": \"The Proposition 3 symmetric diagnostic (|δ_s|/((1-2π̄)·π_s) > 1) fails on real asymmetric LLM CMs (AUC=0.21-0.38) because it assumes FPR=FNR. An asymmetric diagnostic using B_s = M_global⁻¹·M_s - I will recover predictive power (AUC≥0.75) by correctly capturing the directional bias structure of asymmetric confusion matrices.\", \"spec\": {\"command\": \"python exp028_asymmetric_diagnostic_auc.py\", \"server\": \"local-cpu\", \"data_path\": \"real LLM CMs from exp025 COMBOS\", \"data_count\": \"11 LLM×dataset combos, 16 (model,dataset,K) configs\", \"model_name\": \"DIM estimator\", \"seed\": \"0-99 (100 MC)\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"semi-synthetic CATE with real CMs\", \"checkpoint_path\": \"N/A (CPU simulation)\", \"log_path\": \"results/exp_asymmetric_diagnostic_auc.csv\"}, \"conclusion\": \"negative\", \"metrics\": {\"overall_symmetric_auc\": 0.626, \"overall_asymmetric_auc\": 0.611, \"k4_only\": {\"symmetric_auc_range\": \"0.0-1.0\", \"asymmetric_auc_range\": \"0.0-1.0\", \"perfect_auc_combos\": [\"Llama/TweetEval\", \"Qwen/TweetEval\", \"Mistral/TweetEval\", \"gpt-4o/TweetEval\", \"gpt-3.5-turbo/TweetEval(asym only)\", \"gpt-4.1/TweetEval(asym only)\"]}, \"k2_all_auc_zero\": true, \"z0_z1_identical\": true, \"theoretical_insight\": \"For DIM, |B_s[0,1]|=|B_s[1,1]| (column-stochastic M). Asymmetric diagnostic degenerates to symmetric because DIM CATE bias depends on δ_s = (FPR_s+FNR_s)/2 - π̄, not on FPR/FNR individually.\", \"output_files\": [\"results/exp_asymmetric_diagnostic_auc.csv\", \"results/exp_asymmetric_diagnostic_auc_summary.csv\"]}, \"completed_at\": \"2026-05-22T16:13:50.285Z\"}, \"exp-027c\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:21:15.764Z\", \"updated_at\": \"2026-05-22T14:37:04.432Z\", \"hypothesis\": \"Under MF2's exact DGP (K=2, π=[0.05,0.25], τ(0)=0.10, τ(1)=0.40, n_expert=250), Oracle CF coverage will reveal whether the 83% vs 92.5% discrepancy between MF2 and exp-027b is due to the harder CATE specification (τ shift) causing CF SE under-calibration, or due to other implementation differences\", \"parent\": \"exp-027b\", \"spec\": {\"command\": \"python exp027c_cf_oracle_mf2dgp.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic (MF2 DGP)\", \"data_count\": 5000, \"model_name\": \"CausalForest\", \"seed\": \"0-99 (100 MC)\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"synthetic K=2 extreme MF2 DGP\", \"checkpoint_path\": \"N/A (CPU simulation)\", \"log_path\": \"results/exp_cf_oracle_coverage_mf2dgp.csv\"}, \"conclusion\": \"success\", \"metrics\": {\"dgp\": \"MF2 exact DGP: K=2, π=[0.05,0.25], τ(0)=0.10, τ(1)=0.40, N=5000, n_expert=250, 100 MC\", \"oracle_true_Z\": {\"coverage\": 0.96, \"bias\": 0.077, \"rmse\": 0.091, \"mean_se\": 0.09}, \"echte_true_CM\": {\"coverage\": 0.913, \"bias\": 0.103, \"rmse\": 0.112, \"mean_se\": 0.114}, \"echte_estimated_CM\": {\"coverage\": 0.923, \"bias\": 0.1, \"rmse\": 0.111, \"mean_se\": 0.119}, \"global_true_CM\": {\"coverage\": 0.95, \"bias\": 0.107, \"rmse\": 0.114, \"mean_se\": 0.107}, \"global_estimated_CM\": {\"coverage\": 0.943, \"bias\": 0.105, \"rmse\": 0.114, \"mean_se\": 0.109}, \"naive\": {\"coverage\": 0.773, \"bias\": 0.12, \"rmse\": 0.125, \"mean_se\": 0.087}, \"key_finding\": \"DGP difference NOT the source of 83% vs 92.5% gap. Per-subgroup EC-HTE coverage ~92.25% in both 027b and 027c. The 83% in MF2 is an aggregate mixing effect: low-misclass subgroup (π=0.05) has 83% coverage while high-misclass subgroup (π=0.25) has 99%. M⁻¹ creates asymmetric SE amplification across subgroups.\", \"comparison_027b\": {\"oracle\": \"94.0% → 96.0%\", \"echte_est\": \"92.5% → 92.25%\", \"conclusion\": \"Nearly identical per-subgroup coverage despite different τ values\"}, \"output_file\": \"results/exp_cf_oracle_coverage_mf2dgp.csv\"}, \"completed_at\": \"2026-05-22T14:37:04.432Z\"}, \"exp-027b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:13:15.853Z\", \"updated_at\": \"2026-05-22T14:18:26.483Z\", \"hypothesis\": \"Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error\", \"parent\": \"exp-027\", \"conclusion\": \"success\", \"metrics\": {\"dgp\": \"K=2 extreme, π=[0.05,0.25], N=5000, n_expert=250, 100 MC runs\", \"oracle_true_Z\": {\"coverage\": 0.94, \"bias\": 0.0023, \"rmse\": 0.056}, \"echte_true_CM\": {\"coverage\": 0.94, \"bias\": 0.0027, \"rmse\": 0.073}, \"echte_estimated_CM\": {\"coverage\": 0.925, \"bias\": 0.0044, \"rmse\": 0.079}, \"global_true_CM\": {\"coverage\": 0.885, \"bias\": 0.045, \"rmse\": 0.083}, \"global_estimated_CM\": {\"coverage\": 0.883, \"bias\": 0.045, \"rmse\": 0.085}, \"naive\": {\"coverage\": 0.828, \"bias\": 0.046, \"rmse\": 0.077}, \"key_finding\": \"K=2: Oracle 94%, EC-HTE true CM 94%, EC-HTE estimated CM 92.5%. CF SE is well-calibrated. 83-85% coverage in paper comes from Naive (uncorrected misclassification bias), NOT from CF SE under-calibration. EC-HTE restores near-nominal coverage.\", \"output_file\": \"results/exp_cf_oracle_coverage_k2.csv\"}}, \"exp-027\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T14:00:37.085Z\", \"updated_at\": \"2026-05-22T14:08:53.096Z\", \"hypothesis\": \"CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimated Ĉ_s, while the DIM estimator with true C_s achieves ~95% — isolating the source of under-coverage\", \"parent\": \"exp-011\", \"conclusion\": \"success\", \"metrics\": {\"oracle_true_Z\": {\"coverage\": 0.945, \"bias\": 0.0056, \"rmse\": 0.078}, \"echte_true_CM\": {\"coverage\": 0.925, \"bias\": 0.0078, \"rmse\": 0.114}, \"echte_estimated_CM\": {\"coverage\": 0.931, \"bias\": 0.0148, \"rmse\": 0.121}, \"global_true_CM\": {\"coverage\": 0.913, \"bias\": 0.0371, \"rmse\": 0.11}, \"global_estimated_CM\": {\"coverage\": 0.911, \"bias\": 0.0379, \"rmse\": 0.111}, \"naive\": {\"coverage\": 0.883, \"bias\": 0.0447, \"rmse\": 0.095}, \"key_finding\": \"Oracle CF SE well-calibrated (94.5%). EC-HTE true CM (92.5%) ≈ estimated CM (93.1%): CM estimation NOT the coverage gap source. ~2pp drop from Oracle to EC-HTE true CM comes from M^{-1} SE propagation, not CM estimation noise.\", \"dgp\": \"K=4 extreme, N=5000, n_expert=500, 100 MC runs\", \"output_file\": \"results/exp_cf_oracle_coverage.csv\"}}, \"exp-026\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:25:18.911Z\", \"updated_at\": \"2026-05-22T13:41:38.543Z\", \"hypothesis\": \"HB partial pooling provides substantial RMSE and coverage improvement over Stratified MLE at extreme low expert budgets (n_expert=25-75, yielding 6-18 labels per subgroup), with the gap widening as n_expert decreases — demonstrating the practical value of hierarchical shrinkage when per-subgroup data is scarce\", \"parent\": \"exp-006,exp-001\", \"conclusion\": \"success\", \"metrics\": {\"K2_n25\": {\"mle_rmse\": 0.2562, \"hb_rmse\": 0.2689, \"delta_pct\": \"+4.9%\", \"global_rmse\": 0.1013}, \"K2_n50\": {\"mle_rmse\": 0.2748, \"hb_rmse\": 0.2306, \"delta_pct\": \"-16.1%\", \"global_rmse\": 0.0879}, \"K2_n75\": {\"mle_rmse\": 0.0911, \"hb_rmse\": 0.0893, \"delta_pct\": \"-1.9%\"}, \"K4_n25\": {\"mle_rmse\": 0.4011, \"hb_rmse\": 0.6116, \"delta_pct\": \"+52.5%\", \"global_rmse\": 0.1289}, \"K4_n50\": {\"mle_rmse\": 0.3798, \"hb_rmse\": 0.4701, \"delta_pct\": \"+23.8%\", \"global_rmse\": 0.1172}, \"K4_n75\": {\"mle_rmse\": 0.2208, \"hb_rmse\": 0.2111, \"delta_pct\": \"-4.4%\"}, \"K4_n100\": {\"mle_rmse\": 0.2152, \"hb_rmse\": 0.2123, \"delta_pct\": \"-1.3%\"}, \"coverage_all\": \">=0.88, no catastrophic failures\", \"crossover_K2\": \"n_expert=50 (HB -16.1%)\", \"crossover_K4\": \"n_expert=75 (HB -4.4%)\", \"key_finding\": \"HB shrinkage advantage emerges at n≥50 (K=2) and n≥75 (K=4). Below these thresholds, global pooling outperforms both HB and MLE — validates budget threshold claim.\", \"mc_runs\": 100, \"output_file\": \"results/exp_low_budget_hb.csv\"}, \"spec\": {\"command\": \"python exp026_low_budget_hb.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP\", \"data_count\": 1200, \"model_name\": \"N/A\", \"seed\": \"42\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"synthetic K=2/K=4 extreme DGP\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/exp_low_budget_hb.csv\"}, \"completed_at\": \"2026-05-22T13:41:38.543Z\"}, \"exp-025\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:25:15.694Z\", \"updated_at\": \"2026-05-22T13:41:37.612Z\", \"hypothesis\": \"Among 7 LLMs with real per-subgroup CMs, those satisfying diagnostic conditions (κ≤1.25 and max(FPR,FNR)<0.5 for all subgroups) will show EC-HTE (HB) outperforming Global correction in RMSE and coverage, while those violating conditions will show EC-HTE degradation — validating Proposition 3 diagnostic as a practical screening tool\", \"parent\": \"exp-015,exp-016\", \"conclusion\": \"success\", \"metrics\": {\"screening\": \"0/16 combos pass all conditions (κ≤1.25 bottleneck)\", \"oracle_screening\": \"HB wins 41/52 comparisons on aggregate RMSE\", \"hb_vs_mle\": \"HB beats Strat MLE in 52/52 comparisons\", \"best_case\": \"Qwen2.5-7B K=4 n=500 Z=0: ΔRMSE=-0.0075\", \"open_source_llms\": \"All 4 (Llama/Qwen/Mistral/Gemma) HB wins 32/32 on TweetEval\", \"hb_loses\": \"gpt-3.5-turbo/TweetEval (high FPR asymmetry), gpt-4o/CivilComments (low P(Z=1)=0.3)\", \"output_files\": [\"results/exp_screening.csv\", \"results/exp_oracle_screening.csv\", \"results/exp_positive_scenario_summary.md\"]}, \"spec\": {\"command\": \"python exp025_positive_scenario.py\", \"server\": \"local-cpu\", \"data_path\": \"artifacts/c1_multi_llm/\", \"data_count\": 16, \"model_name\": \"N/A\", \"seed\": \"42\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"real LLM CMs + synthetic CATE DGP\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/exp_positive_scenario_summary.md\"}, \"completed_at\": \"2026-05-22T13:41:37.612Z\"}, \"exp-024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T12:25:11.234Z\", \"updated_at\": \"2026-05-22T13:41:36.194Z\", \"hypothesis\": \"Theorem 1 bias decomposition identity (asymmetric version: bias(z,s) = Δτ·[M_global⁻¹ M_s - I]_{z,1}) achieves R²>0.95 when evaluated with real per-subgroup FPR/FNR from 7 LLMs (GPT-3.5-turbo, GPT-4o, GPT-4o-mini, GPT-4-turbo, GPT-4.1, GPT-5.4 on Civil Comments; Llama-3.1-8B, Qwen-2.5-7B, Mistral-7B, Gemma-2-9B on TweetEval), demonstrating the bias mechanism holds under empirically-observed asymmetric confusion matrices\", \"parent\": \"exp-002,exp-014\", \"conclusion\": \"success\", \"metrics\": {\"R2_overall\": 0.975, \"data_sources\": [\"exp023_confusion_matrices.json\", \"c1_multi_llm/*_cm_profile.md\"], \"n_llm_dataset_combos\": 11, \"output_files\": [\"results/exp_realcm_bias_identity.csv\", \"results/exp_realcm_summary.csv\"]}, \"spec\": {\"command\": \"python exp024_realcm_bias_identity.py\", \"server\": \"local-cpu\", \"data_path\": \"results/exp023_confusion_matrices.json\", \"data_count\": 11, \"model_name\": \"N/A\", \"seed\": \"42\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"real LLM CMs from exp-008/exp-023\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/exp_realcm_bias_identity.csv\"}, \"completed_at\": \"2026-05-22T13:41:36.194Z\"}, \"exp-023\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T23:27:31.475Z\", \"updated_at\": \"2026-05-21T23:29:42.293Z\", \"hypothesis\": \"Under heterogeneous-τ DGP (Δτ varies 0.1–0.6 across subgroups), EC-HTE's subgroup-stratified CM correction outperforms Global pooled correction in bias because Global's single correction factor over-corrects low-Δτ subgroups and under-corrects high-Δτ subgroups; EC-HTE should also win RMSE in high-Δτ subgroups where bias dominates variance\", \"parent\": \"exp-008\", \"spec\": {\"command\": \"python run_hetero_tau.py\", \"server\": \"local-cpu\", \"data_path\": \"/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/\", \"data_count\": 5000, \"model_name\": \"Llama-3.1-8B (real CM)\", \"seed\": \"50 MC seeds × 3 budgets\", \"checkpoint_path\": \"/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_results.csv\", \"log_path\": \"/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T23:28:08.362Z\", \"metrics\": {\"dgp\": \"heterogeneous-tau\", \"N\": 5000, \"P_Z1\": 0.652, \"K\": 4, \"subgroups\": [\"False_medium\", \"False_short\", \"True_medium\", \"True_short\"], \"delta_tau\": {\"False_medium\": 0.1, \"False_short\": 0.1, \"True_medium\": 0.3, \"True_short\": 0.6}, \"n_expert_sweep\": [200, 500, 1000], \"mc_seeds\": 50, \"hb_method\": \"MAP-EB Gamma(3,1)\", \"bias_echte_wins\": \"3/3 budgets\", \"bias_reduction_n500\": \"68% vs Global (0.0099 vs 0.0314)\", \"bias_reduction_n200\": \"32% vs Global (0.0248 vs 0.0365)\", \"bias_reduction_n1000\": \"55% vs Global (0.0130 vs 0.0286)\", \"rmse_echte_wins\": \"0/3 aggregate\", \"rmse_true_short_n1000\": {\"global\": 0.1693, \"echte\": 0.1637, \"improvement\": \"-3.3%\"}, \"rmse_true_short_z0_n1000\": {\"global\": 0.2577, \"echte\": 0.2117, \"improvement\": \"-17.8%\"}, \"key_finding\": \"EC-HTE wins bias at all budgets. High-Δτ subgroup (True_short) RMSE wins at n≥500. Aggregate RMSE loss driven by low-Δτ subgroups where stratified variance cost exceeds small bias gain.\"}}, \"exp-022\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:43:54.613Z\", \"updated_at\": \"2026-05-21T19:44:39.795Z\", \"hypothesis\": \"EC-HTE's hierarchical Bayes confusion matrix estimation is insensitive to Gamma hyperprior specification: varying shape∈{1,2,3,5,10} and scale∈{0.5,1,2} produces <10% RMSE variation, confirming the method is not driven by prior choice\", \"parent\": \"exp-001\", \"conclusion\": \"success\", \"metrics\": {\"rmse_range_reasonable\": \"6.0%\", \"rmse_range_all\": \"17.3%\", \"gamma31_rmse\": 0.0841, \"gamma31_rank\": \"8/15\", \"coverage_range\": \"0.925-0.938\", \"hb_beats_mle\": \"9/15\", \"best_config\": \"Gamma(1,0.5)\", \"best_rmse\": 0.0825}, \"spec\": {\"command\": \"python artifacts/gamma_sensitivity/run_gamma_sweep.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP K=2 moderate\", \"data_count\": 5000, \"model_name\": \"MAP-EB with Gamma hyperprior sweep\", \"seed\": \"0-19\", \"checkpoint_path\": \"artifacts/gamma_sensitivity/results.csv\", \"log_path\": \"artifacts/gamma_sensitivity/analysis.md\", \"checkpoint_source\": \"N/A - sensitivity analysis, no model checkpoint\", \"eval_data\": \"synthetic DGP K=2 moderate pi=[0.05,0.15]\"}, \"completed_at\": \"2026-05-21T19:44:39.795Z\"}, \"exp-021\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T17:50:05.855Z\", \"updated_at\": \"2026-05-21T17:50:34.986Z\", \"hypothesis\": \"Table 1 RMSE results are stable under doubling of MC seeds (50→100); median cell change <5% confirms 50-seed results are not artifacts of sampling variance\", \"parent\": \"exp-001\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp021_seeds_supplement.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, 3 configs × 6 n_expert × 50 seeds)\", \"data_count\": \"12800 rows supplement + 25600 combined\", \"model_name\": \"Empirical Bayes (EB) estimator\", \"seed\": \"50-99\", \"checkpoint_path\": \"artifacts/seeds_100/combined_100_seeds.csv\", \"log_path\": \"artifacts/seeds_100/table1_100seeds.md\"}, \"completed_at\": \"2026-05-21T17:50:25.344Z\", \"metrics\": {\"total_cells_compared\": 94, \"median_delta_pct\": 3.2, \"max_delta_pct\": 25.5, \"cells_under_5pct\": \"79/94 (84%)\", \"cells_under_10pct\": \"93/94 (99%)\", \"outlier\": \"K=4/extreme/n=100/HB base (-25.5%, known numerically unstable)\", \"method_note\": \"EB instead of Gibbs (<0.002 CM difference, 10s vs 114min)\"}, \"notes\": \"100-seed stability test for Table 1. 84% cells <5% change, 99% <10%. Only outlier: K=4/extreme/n=100/HB base (-25.5%) — known numerically unstable cell where HB overshoots (RMSE 0.71→0.53, still bad but less bad). Used EB estimator for speed (10s vs 114min Gibbs); EB-Gibbs CM difference <0.002. Non-HB methods identical. Addresses RD2-M4.\"}, \"exp-020\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T16:14:37.738Z\", \"updated_at\": \"2026-05-21T16:15:14.257Z\", \"hypothesis\": \"κ=100 condition number guard provides sufficient safety margin for EC-HTE; empirical sweep will show guard rarely triggers under moderate misclassification and the exact threshold is not critical for well-conditioned problems\", \"parent\": \"exp-001\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp020_kappa_sweep.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, K=2, moderate, symmetric CM)\", \"data_count\": \"350 rows (7 κ × 50 seeds)\", \"model_name\": \"HB Gibbs sampler\", \"seed\": \"0-49\", \"checkpoint_path\": \"artifacts/kappa_sweep/results.csv\", \"log_path\": \"artifacts/kappa_sweep/kappa_sweep_analysis.md\", \"kappa_grid\": [10, 25, 50, 100, 200, 500, 1000], \"K\": 2, \"n_expert\": 200, \"pi_s\": [0.05, 0.15]}, \"completed_at\": \"2026-05-21T16:14:59.935Z\", \"metrics\": {\"max_cond_number\": 1.89, \"mean_cond_number\": 1.446, \"p99_cond_number\": 1.893, \"guard_trigger_rate_all_kappa\": 0, \"rmse_hb\": 0.0759, \"rmse_global\": 0.0765, \"rmse_ratio\": 1.048, \"numerical_instability_rate\": 0, \"safety_margin_at_kappa100\": \"53x\", \"stress_test_near_random_max_cond\": 1125.3, \"stress_test_near_random_triggers_kappa100\": true}, \"notes\": \"κ sweep across {10,25,50,100,200,500,1000}: guard never triggers in moderate regime (max cond=1.89, 53× below κ=100). All κ values produce identical RMSE (HB=0.076, Global=0.077). Zero numerical instability. Stress test: guard only activates with near-random labeling (π_s≈0.4-0.5, n_expert=50, max cond=1125). κ=100 validated as safe default. Adaptive formula κ=10·√(n_expert/K) recovers κ=100 for this regime. Addresses RD2-W4.\"}, \"exp-019\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T15:38:56.994Z\", \"updated_at\": \"2026-05-21T15:39:34.345Z\", \"hypothesis\": \"Theorem 1 bias decomposition R² remains high (>0.95) across P(Z=1) range [0.1, 0.5], and EC-HTE RMSE advantage over global persists but degrades at low P(Z=1) due to insufficient minority-class expert labels\", \"parent\": \"exp-001\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp019_pz1_sweep.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, K=2/4, extreme, symmetric CM)\", \"data_count\": \"30000 rows (100 MC × 5 P(Z=1) × 2 K × variable subgroups × 2 z × 4 methods)\", \"model_name\": \"HB Gibbs sampler (4 chains, 1000 iter, 500 warmup)\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp019_pz1_sweep_results.csv\", \"log_path\": \"results/exp019_pz1_sweep_analysis.md\", \"pz1_grid\": [0.1, 0.2, 0.3, 0.4, 0.5], \"K_grid\": [2, 4], \"n_expert\": 250}, \"completed_at\": \"2026-05-21T15:39:19.738Z\", \"metrics\": {\"theorem1_r2\": {\"K2\": {\"pz0.1\": 0.998, \"pz0.2\": 0.989, \"pz0.3\": 0.994, \"pz0.4\": 0.995, \"pz0.5\": 0.995}, \"K4\": {\"pz0.1\": 0.984, \"pz0.2\": 0.976, \"pz0.3\": 0.985, \"pz0.4\": 0.984, \"pz0.5\": 0.992}}, \"theorem1_r2_range\": \"0.976-0.998 (all >0.95)\", \"rmse_ratio_hb_over_global\": {\"K2\": {\"pz0.1\": 0.92, \"pz0.2\": 0.763, \"pz0.3\": 0.78, \"pz0.4\": 0.874, \"pz0.5\": 0.857}, \"K4\": {\"pz0.1\": 1.542, \"pz0.2\": 1.684, \"pz0.3\": 1.121, \"pz0.4\": 1.082, \"pz0.5\": 1.063}}, \"hb_wins_K2\": \"all 5 P(Z=1) values (ratio 0.76-0.92)\", \"hb_wins_K4\": \"none (ratio 1.06-1.68)\", \"coverage_hb\": \"0.92-0.94 across all settings (near-nominal 0.95)\", \"coverage_naive\": \"0.65-0.79\", \"coverage_global\": \"0.79-0.90\", \"key_finding\": \"Theorem 1 R²>0.976 universally — bias decomposition holds regardless of P(Z=1). EC-HTE RMSE advantage depends on K: K=2 HB wins everywhere, K=4 HB loses at n_expert=250 (insufficient per-subgroup minority data). Coverage: HB 0.92-0.94 near-nominal at all settings.\"}, \"notes\": \"Theorem 1 R²=0.976-0.998 across all P(Z=1)∈[0.1,0.5] × K∈{2,4} — bias decomposition holds universally, not dependent on class balance. EC-HTE RMSE: K=2 HB wins at all P(Z=1) (ratio 0.76-0.92); K=4 HB loses at n_expert=250 (ratio 1.06-1.68) due to 250/4=62.5 experts per subgroup being insufficient when minority class is small. Coverage: HB maintains 0.92-0.94 (near-nominal) while naive 0.65-0.79 and global 0.79-0.90 undercover. Directly addresses M2: A3 (class balance) affects RMSE but NOT Theorem 1 validity.\"}, \"exp-018\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:42:13.498Z\", \"updated_at\": \"2026-05-21T13:54:49.523Z\", \"hypothesis\": \"EC-HTE bias reduction persists under multiplicative CATE DGP (Y(1)=Y(0)*exp(tau(Z))), demonstrating robustness beyond additive treatment effect models\", \"parent\": \"exp-001\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp018_multiplicative_dgp.py --n-mc 50\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, K=2, extreme, multiplicative CATE)\", \"data_count\": \"800 rows (50 MC × 2 subgroups × 2 z × 4 methods)\", \"model_name\": \"HB Gibbs sampler (4 chains, 1000 iter, 500 warmup)\", \"seed\": \"0-49\", \"checkpoint_path\": \"results/exp018_multiplicative_results.csv\", \"log_path\": \"results/exp018_multiplicative_analysis.md\"}, \"completed_at\": \"2026-05-21T13:54:35.822Z\", \"metrics\": {\"n_mc\": 50, \"config\": \"K=2/extreme/n_expert=500/multiplicative\", \"dgp\": \"Y(1) = Y(0) * exp(tau(Z)), tau(Z=0)=0, tau(Z=1)=0.3\", \"results\": {\"oracle\": {\"avg_abs_bias\": 0.031, \"rmse\": 0.038, \"coverage\": 0.96}, \"ec_hte\": {\"avg_abs_bias\": 0.054, \"rmse\": 0.068, \"coverage\": 0.955}, \"global_corrected\": {\"avg_abs_bias\": 0.11, \"rmse\": 0.124, \"coverage\": 0.54}, \"naive\": {\"avg_abs_bias\": 0.135, \"rmse\": 0.142, \"coverage\": 0.435}}, \"ec_hte_rmse_reduction_vs_naive\": \"52%\", \"ec_hte_coverage\": 0.955, \"vs_exp001_additive\": \"EC-HTE RMSE 0.068 (multiplicative) vs 0.091 (additive, same config) — actually better due to larger true CATEs making relative bias smaller\", \"key_finding\": \"EC-HTE robust to non-additive treatment effects. 52% RMSE reduction vs naive, 95.5% coverage (target 95%). Answers Reviewer Q3.\"}, \"notes\": \"EC-HTE robust under multiplicative CATE DGP: RMSE 0.068 (52% reduction vs naive 0.142), coverage 0.955 (nominal 0.95). Global correction inadequate (coverage 0.54). Answers Reviewer Q3 on non-additive DGP robustness.\"}, \"exp-017\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:42:12.809Z\", \"updated_at\": \"2026-05-21T13:53:56.536Z\", \"hypothesis\": \"EC-HTE corrected pseudo-outcomes are compatible with R-learner, achieving similar bias reduction as with CausalForest\", \"parent\": \"exp-011\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp017_rlearner.py --n-mc 50\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, K=2, extreme)\", \"data_count\": \"800 rows (50 MC × 2 subgroups × 2 z × 4 methods)\", \"model_name\": \"R-learner (LassoCV) + HB Gibbs CM correction\", \"seed\": \"0-49\", \"checkpoint_path\": \"results/exp017_rlearner_results.csv\", \"log_path\": \"results/exp017_rlearner_analysis.md\"}, \"completed_at\": \"2026-05-21T13:52:52.889Z\", \"metrics\": {\"n_mc\": 50, \"config\": \"K=2/extreme/n_expert=500\", \"rlearner_results\": {\"naive\": {\"avg_abs_bias\": 0.121, \"rmse\": 0.139, \"coverage\": 0.47}, \"global\": {\"avg_abs_bias\": 0.098, \"rmse\": 0.123, \"coverage\": 0.71}, \"ec_hte\": {\"avg_abs_bias\": 0.013, \"rmse\": 0.08, \"coverage\": 0.92}, \"oracle\": {\"avg_abs_bias\": 0.006, \"rmse\": 0.056, \"coverage\": 0.94}}, \"causal_forest_comparison\": {\"naive\": {\"avg_abs_bias\": 0.125, \"rmse\": 0.143, \"coverage\": 0.46}, \"global\": {\"avg_abs_bias\": 0.104, \"rmse\": 0.129, \"coverage\": 0.65}, \"ec_hte\": {\"avg_abs_bias\": 0.008, \"rmse\": 0.082, \"coverage\": 0.91}}, \"ec_hte_bias_reduction_vs_naive\": \"9.3x (R-learner) vs 15.6x (CausalForest)\", \"pattern_consistent\": true, \"key_finding\": \"EC-HTE correction generalizes across CATE estimators. R-learner ec_hte achieves |bias|=0.013 (vs naive 0.121), 92% coverage — closely matching CausalForest pattern.\"}, \"notes\": \"EC-HTE correction generalizes to R-learner: |Bias| 0.121→0.013 (89% reduction), coverage 0.47→0.92. Consistent with CausalForest results (|Bias|=0.008, coverage 0.91). Validates estimator-agnostic upstream correction.\"}, \"exp-016\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:19:22.463Z\", \"updated_at\": \"2026-05-21T13:42:08.581Z\", \"hypothesis\": \"EC-HTE succeeds under realistic asymmetric CMs when worst-subgroup FNR is well below 0.5 — using gpt-4o (or best-FNR model from exp-008) real per-subgroup FPR/FNR on TweetEval, HB correction outperforms global at n_expert≥250\", \"parent\": \"exp-015\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python3 exp016_semi_real_better_cm.py --n-mc 100\", \"server\": \"local-cpu\", \"data_path\": \"results/exp008_multi_llm_annotations.csv (gpt-3.5-turbo per-subgroup FPR/FNR)\", \"data_count\": \"9600 rows (100 MC × 3 n_expert × 4 subgroups × 2 z × 4 methods)\", \"model_name\": \"HB Gibbs sampler (4 chains, 1000 iter, 500 warmup)\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp016_semi_real_raw.csv\", \"log_path\": \"results/exp016_semi_real_analysis.md\", \"mc_config\": {\"n_seeds\": 100, \"n_expert_grid\": [100, 250, 500], \"N\": 5000, \"K\": 4, \"P_Z1\": 0.18}, \"cm_params\": {\"S0_False_medium\": {\"FPR\": 0.143, \"FNR\": 0.211, \"weight\": 0.38}, \"S1_False_short\": {\"FPR\": 0.18, \"FNR\": 0.15, \"weight\": 0.22}, \"S2_True_short\": {\"FPR\": 0.393, \"FNR\": 0.154, \"weight\": 0.14}, \"S3_True_medium\": {\"FPR\": 0.378, \"FNR\": 0.148, \"weight\": 0.25}}, \"model_selected\": \"gpt-3.5-turbo (lowest worst-subgroup FNR=0.211)\", \"delta_pi_effective\": \"FPR range 0.143-0.393, FNR range 0.148-0.211\"}, \"completed_at\": \"2026-05-21T13:40:37.757Z\", \"metrics\": {\"model_selected\": \"gpt-3.5-turbo\", \"worst_subgroup_fnr\": 0.211, \"worst_subgroup_fpr\": 0.393, \"rmse_n100\": {\"naive\": 0.127, \"global\": 0.265, \"hb\": 0.93}, \"rmse_n250\": {\"naive\": 0.127, \"global\": 0.221, \"hb\": 0.527}, \"rmse_n500\": {\"naive\": 0.127, \"global\": 0.199, \"hb\": 0.322}, \"coverage_n100\": {\"naive\": 0.784, \"global\": 0.893, \"hb\": 0.769}, \"coverage_n250\": {\"naive\": 0.784, \"global\": 0.922, \"hb\": 0.843}, \"coverage_n500\": {\"naive\": 0.784, \"global\": 0.939, \"hb\": 0.894}, \"hb_worse_than_global_all_n\": true, \"vs_exp015\": \"exp-016 HB RMSE even worse than exp-015 despite lower FNR, because high FPR variance (0.14-0.39) makes subgroup CM estimation harder\", \"bright_spot\": \"S0/z=1 at n=500: HB |bias|=0.193 < Global |bias|=0.252 — one case where subgroup-specific correction helps\", \"root_cause\": \"High FPR variance across subgroups (0.143-0.393) + P(Z=1)=0.18 → insufficient Z=1 expert labels per subgroup. Lower FNR alone does not fix the fundamental sample-size constraint.\", \"key_finding\": \"Neither low-FNR (gpt-3.5-turbo) nor low-FPR (GPT-4.1) real CMs enable EC-HTE to beat global. The bottleneck is P(Z=1)=0.18 creating too few positive-class expert labels per subgroup for reliable CM estimation.\"}, \"notes\": \"HB EC-HTE fails under gpt-3.5-turbo real asymmetric CMs despite worst-FNR=0.211 (<0.4). Root cause: FPR≈0.4 + P(Z=1)=0.18 class imbalance → mixing matrix ill-conditioned. Demonstrates that CM condition number alone is insufficient; class-prior-adjusted mixing matrix condition is the true diagnostic.\"}, \"exp-015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T12:49:47.680Z\", \"updated_at\": \"2026-05-21T13:04:54.905Z\", \"hypothesis\": \"EC-HTE maintains bias correction under realistic asymmetric confusion matrices estimated from actual GPT-4.1 annotations on TweetEval (Δπ=0.098, FNR/FPR ratio up to 10×)\", \"parent\": \"exp-003\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python3 exp015_semi_real_cm.py --n-mc 100\", \"server\": \"local-cpu\", \"data_path\": \"results/pilot_gemini_annotations.csv (real GPT-4.1 CMs from exp-012)\", \"data_count\": \"1200 runs (100 MC × 3 n_expert × 4 subgroups)\", \"model_name\": \"HB Gibbs sampler (4 chains, 1000 iter, 500 warmup)\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp015_semi_real_raw.csv\", \"log_path\": \"results/exp015_semi_real_analysis.md\", \"mc_config\": {\"n_seeds\": 100, \"n_expert_grid\": [100, 250, 500], \"N\": 5000, \"K\": 4, \"P_Z1\": 0.18, \"estimator\": \"HB Gibbs (Dirichlet-Multinomial, 4 chains, 1000 iter, 500 warmup)\"}, \"cm_params\": {\"S0_False_medium\": {\"FPR\": 0.054, \"FNR\": 0.526, \"weight\": 0.38}, \"S1_False_short\": {\"FPR\": 0.101, \"FNR\": 0.3, \"weight\": 0.22}, \"S2_True_short\": {\"FPR\": 0.143, \"FNR\": 0.308, \"weight\": 0.14}, \"S3_True_medium\": {\"FPR\": 0.194, \"FNR\": 0.222, \"weight\": 0.25}}, \"delta_pi_effective\": 0.098}, \"completed_at\": \"2026-05-21T13:02:02.880Z\", \"metrics\": {\"n_mc\": 100, \"n_expert_grid\": [100, 250, 500], \"subgroups\": 4, \"real_cm_source\": \"exp-012 GPT-4.1 pilot\", \"cm_params\": {\"S0_False_medium\": {\"FPR\": 0.054, \"FNR\": 0.526, \"weight\": 0.38}, \"S1_False_short\": {\"FPR\": 0.101, \"FNR\": 0.3, \"weight\": 0.22}, \"S2_True_short\": {\"FPR\": 0.143, \"FNR\": 0.308, \"weight\": 0.14}, \"S3_True_medium\": {\"FPR\": 0.194, \"FNR\": 0.222, \"weight\": 0.25}}, \"delta_pi\": 0.098, \"P_Z1\": 0.18, \"rmse_n100\": {\"naive\": 0.123, \"global\": 0.263, \"hb\": 0.784}, \"rmse_n250\": {\"naive\": 0.123, \"global\": 0.232, \"hb\": 0.411}, \"rmse_n500\": {\"naive\": 0.123, \"global\": 0.196, \"hb\": 0.26}, \"coverage_n100\": {\"naive\": 0.868, \"global\": 0.922, \"hb\": 0.744}, \"coverage_n250\": {\"naive\": 0.868, \"global\": 0.908, \"hb\": 0.828}, \"coverage_n500\": {\"naive\": 0.873, \"global\": 0.885, \"hb\": 0.89}, \"hb_worse_than_global_all_n\": true, \"root_cause\": \"S0 FNR=0.526 makes CM row near-uniform [0.526, 0.474], inversion amplifies noise. Combined with P(Z=1)=0.18, too few Z=1 expert labels per subgroup for reliable per-subgroup CM estimation.\", \"key_finding\": \"EC-HTE fails under realistic asymmetric CMs when any subgroup has FNR≈0.5 (near-random for positive class). This is consistent with exp-004 (FNR=53%) and exp-013 (boundary at n_expert/K=12.5). Identifies classifier quality threshold as honest limitation.\"}, \"notes\": \"negative: EC-HTE fails under realistic asymmetric CMs from actual GPT-4.1 annotations. HB RMSE 1.3-3.0× worse than global across all n_expert. Root cause: S0 (38% weight) FNR=0.526 → CM row near-uniform → inversion amplifies noise. Converges with exp-004 (FNR=53%) and exp-013 (n_expert/K boundary). Establishes classifier quality threshold as second applicability condition alongside budget threshold.\"}, \"exp-008\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:06:37.084Z\", \"updated_at\": \"2026-05-21T11:51:10.336Z\", \"hypothesis\": \"Subgroup-specific misclassification heterogeneity (Δπ > 0.05) persists across model generations and scales within the OpenAI family (from GPT-3.5 to GPT-5.4, spanning three model generations), demonstrating the bias mechanism is a structural property of LLM annotation rather than an artifact of a specific model version\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp008_multi_llm.py --phase all + exp008_gpt55_annotate.py\", \"server\": \"local-cpu\", \"data_path\": \"results/pilot_gemini_annotations.csv (500 TweetEval tweets)\", \"data_count\": \"500 tweets × 5-6 models\", \"model_name\": \"gpt-3.5-turbo, gpt-4.1, gpt-4o, gpt-4o-mini, gpt-4-turbo, (gpt-5.5 pending)\", \"seed\": \"N/A (deterministic, temperature=0)\", \"checkpoint_path\": \"results/exp008_multi_llm_annotations.csv\", \"log_path\": \"results/exp008_multi_llm_analysis.md\"}, \"completed_at\": \"2026-05-21T10:13:12.323Z\", \"metrics\": {\"models_completed\": [\"gpt-3.5-turbo\", \"gpt-4.1\", \"gpt-4o\", \"gpt-4o-mini\", \"gpt-4-turbo\", \"gpt-5.4\"], \"total_models\": 6, \"proxy_provider\": \"OpenAI only\", \"gpt5x_model_used\": \"gpt-5.4\", \"gpt55_failed\": \"reasoning tokens consume max_tokens budget, too slow (~1min/call)\", \"filtered_analysis\": {\"excluded_subgroups\": [\"False_long (n=6)\", \"True_long (n=4)\"], \"min_n_threshold\": 10, \"retained_subgroups\": [\"False_medium (n=187)\", \"False_short (n=109)\", \"True_medium (n=125)\", \"True_short (n=69)\"]}, \"effective_delta_pi\": {\"gpt-3.5-turbo\": 0.198, \"gpt-4-turbo\": 0.149, \"gpt-4.1\": 0.098, \"gpt-4o\": 0.08, \"gpt-4o-mini\": 0.136, \"gpt-5.4\": 0.114}, \"all_effective_delta_pi_above_005\": true, \"worst_subgroup_consensus\": \"True_medium (5/6 models)\", \"spearman_significant_pairs\": [\"gpt-4-turbo vs gpt-4o (ρ=1.000)\", \"gpt-4.1 vs gpt-4o-mini (ρ=1.000)\", \"gpt-4.1 vs gpt-5.4 (ρ=1.000)\", \"gpt-4o-mini vs gpt-5.4 (ρ=1.000)\"], \"spearman_note\": \"Only 4 subgroups after filtering, limited statistical power (most p>0.20)\", \"key_finding\": \"All 6 models (GPT-3.5 through GPT-5.4, three generations) show effective Δπ > 0.05 after excluding n<10 subgroups. Heterogeneity is structural, not model-specific.\"}}, \"exp-004\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T08:06:35.407Z\", \"updated_at\": \"2026-05-21T11:02:43.280Z\", \"hypothesis\": \"On real hate speech data (UC Berkeley), LLM annotation of dehumanization level exhibits text-feature-based misclassification heterogeneity (e.g., by target group type, text length, presence of explicit language), and EC-HTE subgroup-stratified correction produces qualitatively different CATE distributions compared to global correction — demonstrating the practical relevance of the bias mechanism with text-feature subgroups consistent with the TweetEval experiment design\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp004_hate_speech.py --phase all\", \"server\": \"local-cpu\", \"data_path\": \"ucberkeley-dlab/measuring-hate-speech (HuggingFace)\", \"data_count\": \"2496 unique comments (sampled from 39565)\", \"model_name\": \"gpt-4.1\", \"seed\": \"42\", \"checkpoint_path\": \"results/exp004_llm_annotations.csv\", \"log_path\": \"results/exp004_hate_speech_analysis.md\"}, \"completed_at\": \"2026-05-21T10:59:47.756Z\", \"metrics\": {\"dataset\": \"UC Berkeley Measuring Hate Speech\", \"n_comments\": 2496, \"valid_annotations\": 2496, \"subgroups\": {\"plat0_long\": 624, \"plat0_short\": 624, \"plat23_long\": 624, \"plat23_short\": 624}, \"subgroup_type\": \"text features (platform_group × text_length)\", \"delta_pi\": 0.117, \"global_FPR\": 0.139, \"global_FNR\": 0.533, \"misclass_rates\": {\"plat0_long\": 0.266, \"plat0_short\": 0.337, \"plat23_long\": 0.303, \"plat23_short\": 0.383}, \"avg_abs_bias\": {\"naive\": 0.21, \"global\": 0.273, \"ec_hte\": 0.313}, \"cate_comparison\": \"EC-HTE does not outperform global on avg |bias| — high FNR (~53%) and wide CIs limit correction effectiveness on this dataset\", \"key_finding\": \"Δπ=0.117 confirms real-world misclassification heterogeneity across text-feature subgroups. High global FNR (53%) indicates LLM severely under-classifies dehumanization. CATE correction comparison inconclusive due to wide bootstrap CIs.\"}, \"notes\": \"Δπ=0.117 confirms subgroup-varying misclassification in real hate speech data. However, EC-HTE correction fails (|bias| 0.313 > Global 0.273 > Naive 0.210) due to extreme baseline FNR=53.3%. This identifies a classifier quality threshold as a boundary condition for EC-HTE: when P(Z_hat=1|Z_true=1) ≈ 0.5 (near-random for positive class), confusion matrix inversion amplifies noise regardless of stratification.\"}, \"exp-010\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T09:57:20.485Z\", \"updated_at\": \"2026-05-21T10:18:33.801Z\", \"hypothesis\": \"EC-HTE with HB partial pooling degrades gracefully under subgroup misspecification: mild noise (10%) causes minimal performance loss due to shrinkage toward global, moderate noise (25%) reduces but preserves advantage over global correction, and severe noise (50%) may eliminate EC-HTE's advantage — demonstrating both the method's robustness range and its honest limitation\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp010_misspecified_subgroups.py --n-mc 100\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (K=2/4, extreme, subgroup noise)\", \"data_count\": \"800 MC runs (2 configs × 4 noise levels × 100 MC)\", \"model_name\": \"N/A (synthetic + EB estimation)\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp010_misspecified_results.csv\", \"log_path\": \"results/exp010_misspecified_analysis.md\"}, \"completed_at\": \"2026-05-21T10:10:42.918Z\", \"metrics\": {\"n_mc\": 100, \"configs\": 2, \"noise_levels\": [0, 0.1, 0.25, 0.5], \"total_runs\": 800, \"runtime_sec\": 15, \"k2_coverage_naive\": [0.875, 0.877, 0.89, 0.897], \"k2_coverage_hb\": [0.958, 0.948, 0.95, 0.945], \"k2_coverage_global\": [0.925, 0.935, 0.932, 0.945], \"k4_coverage_naive\": [0.904, 0.916, 0.909, 0.919], \"k4_coverage_hb\": [0.956, 0.958, 0.96, 0.946], \"k4_coverage_global\": [0.93, 0.953, 0.948, 0.944], \"hb_beats_mle_all_configs\": true, \"hb_improvement_range\": \"+0.1% to +0.9% RMSE\", \"graceful_convergence_at_50pct\": true, \"key_finding\": \"Coverage is the decisive metric: naive 87-92%, EC-HTE 95-96% across all noise levels. No catastrophic failure. HB shrinkage provides automatic safeguard — converges to global at 50% noise.\"}, \"notes\": \"EC-HTE maintains near-nominal CI coverage (≥94.5%) across all subgroup noise levels (0-50%), confirming robustness of inferential validity under misspecified subgroup structure. RMSE advantage is not observed at n_expert=500 (convergence zone per exp-006), but coverage is the decisive metric for statistical inference. At p_flip=0.50, EC-HTE gracefully converges to global correction. HB and MLE perform comparably at n=500 (expected per exp-006).\"}, \"exp-014\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:27:32.305Z\", \"updated_at\": \"2026-05-21T07:45:15.046Z\", \"hypothesis\": \"The bias decomposition product structure (delta_s * delta_tau) persists under asymmetric misclassification (FPR != FNR), and EC-HTE subgroup-stratified correction remains effective — the symmetric assumption A2 is sufficient for the qualitative insight but not necessary for EC-HTE to work\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 exp014_asymmetric_verification.py\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (K=2, asymmetric FPR≠FNR)\", \"data_count\": \"3 configs × 5 Δτ × 100 MC = 1500 runs\", \"model_name\": \"N/A (analytic + MC verification)\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp014_asymmetric_results.csv\", \"log_path\": \"results/exp014_asymmetric_analysis.md\"}, \"completed_at\": \"2026-05-21T07:45:03.268Z\", \"metrics\": {\"configs\": 3, \"asymmetric_configs\": [\"balanced(FPR=0.15,FNR=0.25)\", \"fpr_dominant(FPR=0.30,FNR=0.10)\", \"fnr_dominant(FPR=0.10,FNR=0.30)\"], \"delta_tau_grid\": [0, 0.1, 0.2, 0.3, 0.5], \"n_mc\": 100, \"N\": 5000, \"n_expert\": 250, \"r2_analytic_vs_mc\": 0.992, \"product_structure_cv\": \"~1e-16 (exact)\", \"product_structure_confirmed\": true, \"a2_not_required\": true, \"ec_hte_avg_abs_bias\": 0.006, \"ec_hte_avg_rmse\": 0.033, \"ec_hte_avg_coverage\": 0.9, \"global_avg_abs_bias\": 0.025, \"global_avg_rmse\": 0.04, \"global_avg_coverage\": 0.78, \"naive_avg_abs_bias\": 0.025, \"naive_avg_rmse\": 0.039, \"naive_avg_coverage\": 0.87, \"bias_reduction_vs_global\": \"4.2x\", \"coverage_improvement_vs_global\": \"+12pp\", \"latex_derivation_included\": true, \"key_finding\": \"Product structure bias = Δτ·[B_s]_{z,1} holds exactly under asymmetric misclassification. A2 (symmetric) assumption is NOT required. EC-HTE dominates with 4.2x bias reduction.\"}}, \"exp-013\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:25:13.287Z\", \"updated_at\": \"2026-05-21T07:31:28.668Z\", \"hypothesis\": \"EC-HTE (especially HB) degrades significantly at n_expert=50/K=4 because per-subgroup CM estimation with ~12 expert labels per subgroup is too noisy, causing RMSE to substantially exceed global correction — validating the budget threshold claim in the paper\", \"conclusion\": \"success\", \"metrics\": {\"config\": \"K=4/extreme/n_expert=50\", \"n_expert_per_K\": 12.5, \"hb_method\": \"EB (Empirical Bayes, not Gibbs — conservative estimate for boundary condition)\", \"avg_rmse_naive\": 0.109, \"avg_rmse_global\": 0.14, \"avg_rmse_mle\": 0.28, \"avg_rmse_eb\": 0.292, \"worst_subgroup\": \"A(pi=0.30) EB RMSE=0.62\", \"amplification_max\": \"4.4x (A/EB vs global)\", \"threshold_confirmed\": \"n_expert/K=12.5 < 25\", \"naive_beats_all\": true, \"debiasing_hurts_D\": \"Naive bias=0.001, Global bias=0.110 — extreme over-correction in lowest-error subgroup\"}, \"spec\": {\"command\": \"python3 exp013_boundary_condition.py\", \"server\": \"local\", \"data_path\": \"synthetic DGP (K=4, extreme)\", \"data_count\": \"5000 per run x 100 MC\", \"model_name\": \"N/A (synthetic)\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp013_boundary_condition.csv\", \"log_path\": \"results/exp013_boundary_analysis.md\"}, \"completed_at\": \"2026-05-21T07:29:18.249Z\"}, \"exp-012\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:20:57.458Z\", \"updated_at\": \"2026-05-21T05:24:11.994Z\", \"hypothesis\": \"真实 LLM（GPT-4.1）对 TweetEval sentiment 的标注存在跨子群（has_hashtag × text_length_bin）的误分类率异质性（Δπ > 0.05），为 EC-HTE 的必要性提供 empirical motivation\", \"spec\": {\"command\": \"python3 -u pilot_gemini_annotation.py --n-samples 500\", \"server\": \"local-cpu\", \"data_path\": \"/home/ubuntu/ec_hte_llm_annotation/results/pilot_gemini_annotations.csv\", \"data_count\": 500, \"model_name\": \"gpt-4.1-2025-04-14\", \"seed\": 42}, \"conclusion\": \"success\", \"log_path\": \"results/pilot_gpt41_run.log\", \"checkpoint_path\": \"results/pilot_gemini_annotations.csv\", \"completed_at\": \"2026-05-21T05:21:29.106Z\", \"metrics\": {\"model\": \"gpt-4.1-2025-04-14\", \"n_samples\": 500, \"valid_annotations\": 500, \"failed\": 0, \"accuracy_3class\": 0.672, \"accuracy_binary\": 0.858, \"subgroup_misclass_rates\": {\"hash_long\": 0, \"hash_medium\": 0.2, \"hash_short\": 0.174, \"nohash_long\": 0, \"nohash_medium\": 0.102, \"nohash_short\": 0.138}, \"delta_pi\": 0.2, \"heterogeneity_significant\": true, \"key_finding\": \"Hashtag presence increases binary misclassification rate (~0.17-0.20 vs ~0.10-0.14 for non-hashtag). Delta-pi=0.200 confirms meaningful heterogeneity for EC-HTE correction.\", \"analysis_file\": \"results/pilot_gpt41_analysis.md\"}}, \"exp-006\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:32:19.181Z\", \"updated_at\": \"2026-05-21T05:08:56.048Z\", \"hypothesis\": \"HB partial pooling 的 RMSE 优势在小 n_expert 时最明显，存在一个 crossover point（预计 n_expert ∈ [100, 500]）使得 HB 开始系统性优于 Global correction\", \"spec\": {\"command\": \"python exp006_budget_sensitivity.py 2>&1 | tee results/exp006_run.log\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, K=2/4, symmetric misclass)\", \"data_count\": \"288 aggregated rows (100 MC × 24 configs × 4 methods × K subgroups)\", \"model_name\": \"Gibbs sampler + MLE + Global correction\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp006_budget_sensitivity.csv\", \"log_path\": \"results/exp006_run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"n_mc\": 100, \"total_rows\": 288, \"runtime_min\": 110, \"grid\": \"n_expert=[50,100,250,500,1000,2000] × K=[2,4] × regime=[extreme,moderate]\", \"crossover_hb_beats_global\": {\"K2_extreme\": 250, \"K2_moderate\": \"never\", \"K4_extreme\": 1000, \"K4_moderate\": 2000}, \"hb_vs_mle\": \"HB ≥ MLE in 21/24 configs (87.5%; partial pooling rarely hurts in symmetric DGP)\", \"hb_best_improvement_over_mle\": {\"K4_moderate_n50_sgC\": \"+42.4% RMSE\", \"K4_extreme_n50_sgC\": \"+23.4% RMSE\", \"K4_moderate_n50_sgB\": \"+24.0% RMSE\"}, \"convergence\": \"HB ≈ MLE at n≥1000 (<0.5% difference)\", \"key_finding\": \"Crossover depends strongly on K and regime. K=2: crossover at n=250 (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest improvement over MLE via partial pooling.\"}, \"completed_at\": \"2026-05-21T03:02:24.771Z\"}, \"exp-007b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:53:49.325Z\", \"updated_at\": \"2026-05-21T04:54:59.207Z\", \"hypothesis\": \"exp-007 HB 回填：将 ec_hte 方法从 stratified_mle placeholder 替换为真正的 HB Gibbs sampler（Dirichlet-Multinomial partial pooling），验证在 4-DGP matrix 下 HB 版本的 ec_hte 和 ec_hte_ppci 是否保持或改善原 MLE 版本的结果\", \"parent\": \"exp-007\", \"spec\": {\"command\": \"python3 -u exp007_ppci_dsl.py (tmux session exp007hb, PID 151996)\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, 4 types A/B/C/D)\", \"data_count\": \"8 methods x 4 DGP x 3 sigma x 2 K x 6 n_expert x 100 MC\", \"model_name\": \"HB Gibbs sampler (4 chains, 1000 iter, 500 warmup) + PPCI rectifier\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp007_ppci_dsl_hb.csv\", \"log_path\": \"results/exp007_hb_run.log\", \"checkpoint_source\": \"exp-007 (method upgrade: stratified_mle → HB Gibbs)\", \"eval_data\": \"same synthetic DGP as exp-007\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-21T04:54:53.137Z\", \"metrics\": {\"kill_reason\": \"D012: Director 决定放弃 HB backfill。理由：PPCI 表核心 story 是互补性，HB vs MLE 是边际改进；exp-001 已验证 HB。CSV 已重命名为 .broken\"}}, \"exp-003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:28:35.035Z\", \"updated_at\": \"2026-05-21T04:08:06.566Z\", \"hypothesis\": \"在真实文本子群结构（TweetEval sentiment, 基于hashtag和文本长度的4子群）上，当LLM误分类率跨子群异质时，Global correction在低误分类子群反而加偏（debiasing hurts），而Stratified MLE在大子群表现更优但小子群存在variance penalty——验证EC-HTE partial pooling的必要性\", \"spec\": {\"command\": \"python exp003_tweeteval.py 2>&1 | tee results/exp003_run_v2.log\", \"server\": \"local-cpu\", \"data_path\": \"TweetEval sentiment (cardiffnlp/tweet_eval) + synthetic misclass DGP\", \"data_count\": \"5000 sampled from 59899, 200 MC runs x 4 methods x 3 Z-levels\", \"model_name\": \"Stratified MLE confusion matrix correction\", \"seed\": \"42 (data sample) + 0-199 (MC)\", \"checkpoint_path\": \"results/exp003_phase_a_v2.csv\", \"log_path\": \"results/exp003_phase_a_v2_raw.csv\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T22:29:06.267Z\", \"metrics\": {\"phase\": \"A_semi_synthetic\", \"n_subgroups\": 4, \"misclass_rates\": \"S0=0.05, S1=0.10, S2=0.15, S3=0.25\", \"subgroup_sizes\": \"S0~38%, S1~38%, S2~12%, S3~12%\", \"p_z1_actual\": 0.39, \"debiasing_hurts_confirmed\": true, \"mc_runs\": 100, \"v3_hb_integration_100mc\": {\"methods\": [\"oracle\", \"naive\", \"global_corrected\", \"stratified_mle\", \"hb_ec_hte\"], \"hb_vs_mle_summary\": {\"n50_S3_extreme\": \"-57% RMSE (HB worse, but not catastrophic)\", \"n50_S3_moderate\": \"-54% RMSE z1 (HB worse)\", \"n100_S3_extreme\": \"+60% RMSE z1 (HB dramatically better)\", \"n100_S3_moderate\": \"+24% RMSE z1 (HB better)\", \"n100_S2\": \"+5-8% RMSE (HB better)\", \"n250_S3\": \"+5-17% RMSE (HB better)\", \"n500_all\": \"+0.2-1.6% (converged)\"}, \"key_finding\": \"100 MC confirms: S3 blowup at n=50 is real but moderate (not catastrophic as dry-run suggested). At n>=100, HB is better everywhere, especially S3 (+26-60%). Partial pooling sweet spot is n=100-250.\", \"hypothesis_verdict\": \"validated_with_boundary\", \"boundary_condition\": \"n_expert>=100 recommended; n=50 with extreme heterogeneity in tiny subgroups shows moderate degradation\"}, \"results_file_v3\": \"results/exp003_phase_a_v3.csv\", \"results_file_v3_raw\": \"results/exp003_phase_a_v3_raw.csv\"}}, \"exp-011\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:32:16.664Z\", \"updated_at\": \"2026-05-21T02:32:33.894Z\", \"hypothesis\": \"EC-HTE correction 在 CausalForestDML 上复现与 diff-in-means 一致的改善模式：global correction 在低误分类子群加偏（debiasing hurts），stratified correction 修复偏差同时保持 CATE 估计精度\", \"spec\": {\"command\": \"python exp011_causal_forest.py --n-mc 100 2>&1 | tee results/exp011_run.log\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, K=2/4, symmetric misclass)\", \"data_count\": \"144 aggregated rows (100 MC × 8 configs × 3 methods × 2 subgroups × 2 z_levels)\", \"model_name\": \"CausalForestDML (econml) with EC-HTE correction\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp011_causal_forest.csv\", \"log_path\": \"results/exp011_run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"n_mc\": 100, \"n_configs\": 8, \"total_rows\": 144, \"runtime_min\": 35, \"methods\": [\"naive_forest\", \"global_forest\", \"ec_hte_forest\"], \"mean_abs_bias\": {\"naive_forest\": 0.1558, \"global_forest\": 0.1073, \"ec_hte_forest\": 0.0608}, \"mean_rmse\": {\"naive_forest\": 0.1782, \"global_forest\": 0.1659, \"ec_hte_forest\": 0.2289}, \"debiasing_hurts_cases\": 9, \"debiasing_hurts_max_ratio\": 5.9, \"debiasing_hurts_detail\": \"K=4/extreme/sg0: global 5.9x worse than naive\", \"k2_n500_ec_hte_bias_range\": \"0.004-0.013 (near zero)\", \"k2_n500_global_bias_range\": \"0.033-0.109 (still biased)\", \"pattern_consistent_with_diff_in_means\": true, \"claim2_validated\": true}, \"completed_at\": \"2026-05-21T02:32:33.894Z\"}, \"exp-005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:12:28.105Z\", \"updated_at\": \"2026-05-21T00:12:53.084Z\", \"hypothesis\": \"signed product (π̄−π_s)×Δτ 可作为诊断准则预测 global correction 是否在特定子群中反而加偏（debiasing hurts），子群水平 AUC 应显著高于随机（>0.7）\", \"spec\": {\"command\": \"python exp005_diagnostic_criterion.py\", \"server\": \"local-cpu\", \"data_path\": \"results/exp001_hb_results_v2.csv + results/exp003_phase_a_v2.csv\", \"data_count\": \"exp-001 36 settings + exp-003 4 subgroups\", \"model_name\": \"LOSO cross-validated ROC/AUC\", \"seed\": \"N/A (deterministic)\", \"checkpoint_path\": \"results/exp005_diagnostic.csv\", \"log_path\": \"results/exp005_roc.png\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T00:12:51.199Z\", \"metrics\": {\"subgroup_level_auc\": 0.833, \"subgroup_correlation\": 0.86, \"setting_level_auc\": 0.49, \"low_pi_hurt_pct\": 84.6, \"high_pi_hurt_pct\": 15.4, \"theory_alignment\": \"consistent with exp-002 formula\"}}, \"exp-007\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:28:25.658Z\", \"updated_at\": \"2026-05-21T00:05:11.910Z\", \"hypothesis\": \"在同时存在covariate misclassification和treatment-differential outcome error的DGP下，EC-HTE单独处理covariate error、PPCI单独处理outcome error，二者组合(EC-HTE+PPCI)能同时校正两类错误，实现最低bias和RMSE\", \"spec\": {\"command\": \"python exp007_ppci_dsl.py 2>&1 | tee results/exp007_full_run.log\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP, 4 types (A/B/C/D)\", \"data_count\": \"6912 aggregated rows (100 MC × 4 DGP × 8 methods × multiple configs)\", \"model_name\": \"Stratified MLE + PPI rectifier + combination\", \"seed\": \"0-99\", \"checkpoint_path\": \"results/exp007_ppci_dsl.csv\", \"log_path\": \"results/exp007_full_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T00:05:00.962Z\", \"metrics\": {\"total_rows\": 6912, \"dgps\": [\"A_covariate_only\", \"B_outcome_only\", \"C_both_errors\", \"D_no_error\"], \"methods\": 8, \"mc_runs\": 100, \"double_correction_fix_verified\": true, \"dgp_a_ec_hte_ppci_equals_ec_hte\": true, \"dgp_c_extreme_n250_k2\": {\"ec_hte_ppci_bias_z0\": 0.005, \"ec_hte_ppci_rmse_z0\": 0.225, \"ec_hte_bias_z0\": 0.178, \"ec_hte_rmse_z0\": 0.226, \"ppci_bias_z0\": 0.004, \"ppci_rmse_z0\": 0.261, \"naive_bias_z0\": 0.251, \"naive_rmse_z0\": 0.269}, \"dgp_c_n500_k2\": {\"ec_hte_ppci_bias_z0\": 0.005, \"ec_hte_ppci_rmse_z0\": 0.142, \"ec_hte_bias_z0\": 0.088, \"ec_hte_rmse_z0\": 0.134}, \"key_finding\": \"ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.\"}}, \"exp-001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:44:54.310Z\", \"updated_at\": \"2026-05-20T23:55:59.564Z\", \"hypothesis\": \"Hierarchical Bayesian Dirichlet-prior confusion matrix estimator 通过 partial pooling 在 n_expert 小（50-100）时比 MLE/Laplace 实现更低 RMSE 和更好的 coverage 校准，因为它能跨子群借力减少估计方差\", \"spec\": {\"command\": \"python exp001_hb_synthetic.py 2>&1 | tee results/exp001_run.log\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000, symmetric misclass)\", \"data_count\": \"3600 MC runs (36 cells × 100 MC)\", \"model_name\": \"Gibbs sampler Dirichlet-Multinomial HB\", \"seed\": \"0-99 per cell\", \"checkpoint_path\": \"results/exp001_hb_results.csv\", \"log_path\": \"results/exp001_hb_diagnostics.csv\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T21:32:51.348Z\", \"metrics\": {\"mcmc_rhat_max\": 1.024, \"mcmc_ess_min\": 129, \"mcmc_divergent\": 0, \"runtime_min\": 69, \"total_mc_runs\": 3600, \"hb_vs_mle_rmse_improvement_k2_n50\": \"4-9%\", \"hb_vs_mle_rmse_improvement_k2_n100\": \"1-2%\", \"hb_vs_mle_rmse_improvement_k4_n50_moderate\": \"6-9%\", \"hb_coverage_min\": 0.87, \"hb_coverage_median\": 0.93, \"k4_extreme_n50_blowup\": false, \"k4_extreme_n50_blowup_note\": \"Fixed by singularity guard + 4-chain MCMC\", \"mcmc_fix_4chain\": {\"rhat_max_all_configs\": 1.0034, \"ess_min_all_configs\": 1618, \"ess_improvement\": \"~4x vs 2-chain\", \"k4_extreme_n50_A_rmse_z0\": \"3.14 → 0.99\", \"k4_extreme_n50_B_rmse_z0\": \"509.93 → 0.27\", \"k4_extreme_n100_A_rmse_z0\": \"11.57 → 0.29\", \"singularity_guard_triggers\": \"extreme/n=50 only (2 HB, 3 MLE / 100 runs)\", \"results_file\": \"results/exp001_hb_results_v2.csv\"}, \"hyperprior_sensitivity\": {\"scale_range\": \"0.5-2.0\", \"k2_rmse_variation\": \"<1%\", \"k4_rmse_variation\": \"~4-5%\", \"coverage_invariant\": true, \"conclusion\": \"robust\", \"results_file\": \"results/exp001_hyperprior_sensitivity.csv\"}}}, \"exp-002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:44:56.556Z\", \"updated_at\": \"2026-05-20T21:26:53.094Z\", \"hypothesis\": \"Global correction 的子群内 bias 遵循解析公式 bias ∝ Δ_misclass × Δ_CATE，且存在参数区域使 |bias_global| > |bias_naive|（去偏反而加偏），该区域在 K=4 子群时比 K=2 更大\", \"conclusion\": \"success\", \"metrics\": {\"r2_k2\": 0.9939, \"r2_k4\": 0.9738, \"tightness_ratio_k2_median\": 1.0027, \"tightness_ratio_k4_median\": 1.0234, \"debiasing_hurts_pct\": 50, \"debiasing_hurts_pct_note\": \"260/520 (excluding dc=0 rows where bias=0)\", \"debiasing_hurts_threshold_delta_misclass\": 0.1235, \"max_bias_ratio_k2\": 2.86, \"max_bias_ratio_k4\": 2.41, \"coverage_2se_k2\": 0.951, \"coverage_2se_k4\": 0.94}, \"spec\": {\"command\": \"python exp002_bias_bound.py 2>&1 | tee results/exp002_run.log\", \"server\": \"local-cpu\", \"data_path\": \"synthetic DGP (N=5000)\", \"data_count\": \"1000 MC per grid point\", \"model_name\": \"analytic bias formula + MC simulation\", \"seed\": \"0-999\", \"checkpoint_path\": \"results/exp002_*\", \"log_path\": \"results/exp002_run.log\"}, \"completed_at\": \"2026-05-20T20:52:13.210Z\"}}, \"count\": 42, \"total\": 42, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1459}}"
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
The registry data is too large to read directly. I need to read appendix.tex in parts and also parse the registry data. Let me handle this in parallel:

1. Read appendix.tex in parts
2. Parse registry data using jq in a subagent

Let me first read appendix.tex in parts and then process the registry data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "b035b1f0-c2f0-477d-813c-ce1aa7c2d835",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjQrtrcU6xrQTDd17FDZwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15903,
      "cache_read_input_tokens": 26426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15903
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

appendix.tex 太大，需要分段读取。同时需要解析 registry JSON。并行处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "98838ab0-9b65-42fc-9265-e26bfd824276",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjQrtrcU6xrQTDd17FDZwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15903,
      "cache_read_input_tokens": 26426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15903
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

<details open><summary>🔧 Tool call — Read · `toolu_015sx4TCRnJXndNeorzCaCKQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "4bfaa3db-4c7e-4853-9a93-3de8cae400b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjQrtrcU6xrQTDd17FDZwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15903,
      "cache_read_input_tokens": 26426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15903
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

_source line 33 · 2026-05-24T04:29:27.403Z_

<details><summary>↩ Tool result · `toolu_015sx4TCRnJXndNeorzCaCKQ`</summary>

```text
1	\section{EC-HTE Procedure}
2	\label{app:algorithm}
3	
4	\begin{algorithm}[t]
5	\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
6	\label{alg:echte}
7	\begin{algorithmic}[1]
8	\Require Observations $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S: \mathcal{X} \to \{1,\ldots,K\}$
9	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with variance-adjusted CIs
10	\Statex
11	\State \textbf{Preconditions:} verify $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ and $\max_s(\text{FPR}_s, \text{FNR}_s) < 0.5$; if either fails, use global correction
12	\Statex
13	\State \textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}
14	\For{$s = 1, \ldots, K$}
15	    \State $C_s[j,\cdot] \sim \mathrm{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, \; $\alpha_0$ via empirical Bayes
16	    \State Gibbs sampler (4 chains, 4000 iter) on $\{(\hat{Z}_j, Z_j^*) : S_j = s\}$
17	    \State $\hat{C}_s \gets$ posterior mean; verify $\hat{R} < 1.01$
18	\EndFor
19	\Statex
20	\State \textbf{Step 2: Correct observed outcome moments}
21	\For{$s = 1, \ldots, K$}
22	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{singularity guard}
23	    \EndIf
24	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
25	\EndFor
26	\Statex
27	\State \textbf{Step 3: CausalForestDML with variance-adjusted SEs}
28	\State Train CausalForest (honest splitting) on corrected outcome moments $\tilde{\boldsymbol{\mu}}_s$
29	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
30	\State \Return $\hat{\tau}(z)$ with 95\% CIs from $\mathrm{se}_{\mathrm{adj}}$
31	\end{algorithmic}
32	\end{algorithm}
33	
34	\subsection{Condition Number Guard Ablation}
35	\label{app:kappa_ablation}
36	
37	The singularity guard in Algorithm~\ref{alg:echte} (line~6) falls back to global correction when $\kappa(\hat{C}_s) > 100$.
38	We verify that this threshold is not load-bearing by sweeping $\kappa \in \{10, 25, 50, 100, 200, 500, 1000\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs).
39	Across all configurations, the maximum observed condition number is $\kappa_{\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\times}$ safety margin below the $\kappa{=}100$ threshold.
40	Consequently, the guard never triggers at any tested threshold, and all $\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.
41	In a stress test with near-random labeling ($\pi_s \approx 0.4$--$0.5$, $n_{\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\kappa{=}100$ guard and preventing catastrophic inversion.
42	The adaptive formula $\kappa_{\text{adapt}} = 10 \sqrt{n_{\text{expert}} / K}$ recovers $\kappa{=}100$ for this regime and scales naturally with the estimation precision.
43	
44	\section{Full Proof of Theorem~\ref{thm:bias_identity}}
45	\label{app:derivation}
46	
47	\paragraph{Setup.}
48	Under assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is
49	\begin{equation}
50	\tau_{\text{obs}}(z, s) = \sum_{z'} M_s[z, z'] \cdot \tau(z'),
51	\end{equation}
52	where $M_s[z, z'] = P(Z{=}z' \mid \hat{Z}{=}z, S{=}s)$ is the mixing matrix.
53	Under (A2)--(A3), $M_s = \bigl[\begin{smallmatrix} 1-\pi_s & \pi_s \\ \pi_s & 1-\pi_s \end{smallmatrix}\bigr]$.
54	
55	\paragraph{Global correction.}
56	The pooled mixing matrix is $M_{\text{global}} = \sum_s w_s M_s = \bigl[\begin{smallmatrix} 1-\bar{\pi} & \bar{\pi} \\ \bar{\pi} & 1-\bar{\pi} \end{smallmatrix}\bigr]$, with $\bar{\pi} = \sum_s w_s \pi_s$.
57	
58	Global correction applies $M_{\text{global}}^{-1}$ to $\tau_{\text{obs}}(\cdot, s)$:
59	\begin{equation}
60	\hat{\tau}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} M_s \cdot \boldsymbol{\tau}]_z,
61	\end{equation}
62	where $\boldsymbol{\tau} = [\tau(0), \tau(1)]^\top$.
63	
64	\paragraph{Bias computation.}
65	The bias is $\hat{\tau}_{\text{global}}(z, s) - \tau(z) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z$.
66	
67	Direct computation gives:
68	\begin{equation}
69	M_{\text{global}}^{-1} = \frac{1}{1 - 2\bar{\pi}} \begin{bmatrix} 1-\bar{\pi} & -\bar{\pi} \\ -\bar{\pi} & 1-\bar{\pi} \end{bmatrix}.
70	\end{equation}
71	Multiplying by $M_s$:
72	\begin{equation}
73	\resizebox{.88\columnwidth}{!}{$\displaystyle
74	M_{\text{global}}^{-1} M_s = \frac{1}{1-2\bar{\pi}} \begin{bmatrix} (1{-}\bar{\pi})(1{-}\pi_s) - \bar{\pi}\pi_s & (1{-}\bar{\pi})\pi_s - \bar{\pi}(1{-}\pi_s) \\ -\bar{\pi}(1{-}\pi_s) + (1{-}\bar{\pi})\pi_s & -\bar{\pi}\pi_s + (1{-}\bar{\pi})(1{-}\pi_s) \end{bmatrix}.
75	$}
76	\end{equation}
77	
78	Define $\delta_s = \pi_s - \bar{\pi}$. Substituting $\pi_s = \bar{\pi} + \delta_s$:
79	\begin{equation}
80	M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}.
81	\end{equation}
82	
83	To verify: the $(1,1)$ entry of $M_{\text{global}}^{-1} M_s$ is
84	{\small
85	\begin{align}
86	&\frac{(1{-}\bar{\pi})(1{-}\bar{\pi}{-}\delta_s) - \bar{\pi}(\bar{\pi}{+}\delta_s)}{1-2\bar{\pi}} \nonumber\\
87	&= \frac{(1{-}\bar{\pi})^2 - (1{-}\bar{\pi})\delta_s - \bar{\pi}^2 - \bar{\pi}\delta_s}{1-2\bar{\pi}} \nonumber\\
88	&= \frac{1 - 2\bar{\pi} - \delta_s}{1-2\bar{\pi}} = 1 - \frac{\delta_s}{1-2\bar{\pi}}.
89	\end{align}
90	}
91	
92	Applying $(M_{\text{global}}^{-1} M_s - I)$ to $\boldsymbol{\tau}$:
93	{\small
94	\begin{align}
95	\text{bias}(z{=}0, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(-\tau(0) + \tau(1)) = +\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}}, \\
96	\text{bias}(z{=}1, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(\tau(0) - \tau(1)) = -\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}},
97	\end{align}
98	}
99	where $\Delta\tau = \tau(1) - \tau(0)$. \qed
100	
101	\paragraph{Finite-sample remainder.}
102	When $\hat{C}_s = C_s + E_s$ with $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$ (central limit theorem), the estimated correction $\hat{M}_{\text{global}}^{-1} \hat{M}_s$ deviates from its population counterpart by
103	$\|\hat{M}_{\text{global}}^{-1} \hat{M}_s - M_{\text{global}}^{-1} M_s\| \leq \kappa(M_{\text{global}}) \cdot O_p(n_{\text{expert}}^{-1/2})$,
104	where $\kappa(M) = \|M\| \cdot \|M^{-1}\|$ is the condition number~\citep{stewart1990matrix}.
105	This motivates the $\kappa > 100$ singularity guard in Section~\ref{sec:method}.
106	
107	\section{Multi-class Extension and Proof}
108	\label{app:multiclass}
109	
110	\begin{corollary}[Multi-class Extension]
111	\label{cor:multiclass}
112	For $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to
113	\begin{equation}
114	\mathrm{bias}_{\mathrm{global}}(z, s) = \sum_{j=1}^{J} \bigl(\bar{\pi}_j - \pi_{s,j}\bigr) \cdot \bigl(\tau(j) - \bar{\tau}\bigr) \cdot g(\bar{\pi}),
115	\label{eq:multiclass}
116	\end{equation}
117	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms.\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\bar{\pi}) = 1/(1 - 3\bar{\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\bar{\pi})$. In general, $g(\bar{\pi}) = 1/(1 - J\bar{\pi}/(J-1))$.}
118	The essential structure, $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.
119	\end{corollary}
120	
121	\paragraph{Proof.}
122	For $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \times J$ with entries $M_s[j, j'] = P(Z{=}j' \mid \hat{Z}{=}j, S{=}s)$.
123	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
124	
125	The bias of global correction in subgroup $s$ at level $z$ is:
126	\begin{equation}
127	\text{bias}_{\text{global}}(z, s) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z.
128	\end{equation}
129	
130	Write $M_s = M_{\text{global}} + \Delta_s$ where $\Delta_s = M_s - M_{\text{global}}$ satisfies $\sum_s w_s \Delta_s = 0$.
131	Then $M_{\text{global}}^{-1} M_s = I + M_{\text{global}}^{-1} \Delta_s$, so:
132	\begin{equation}
133	\text{bias}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} \Delta_s \cdot \boldsymbol{\tau}]_z.
134	\end{equation}
135	
136	For symmetric misclassification with per-class error rates $\pi_{s,j}$ and pooled rates $\bar{\pi}_j$, the entries of $\Delta_s$ have the form $\Delta_s[j,j'] = (\bar{\pi}_j - \pi_{s,j}) \cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.
137	Expanding the matrix-vector product and collecting terms yields:
138	\begin{equation}
139	\text{bias}_{\text{global}}(z, s) = \sum_{j=1}^{J} (\bar{\pi}_j - \pi_{s,j}) \cdot (\tau(j) - \bar{\tau}) \cdot g(\bar{\pi}),
140	\end{equation}
141	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms and $\bar{\tau} = \sum_j P(Z{=}j) \tau(j)$.
142	
143	The essential structure $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.
144	For non-uniform off-diagonal entries, the scalar amplification $g(\bar{\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \cdot \Delta\tau$ persists but a closed-form amplification factor does not. \qed
145	
146	\section{Proof of Proposition~\ref{prop:debiasing_hurts}}
147	\label{app:debiasing_hurts}
148	
149	The naive estimator has bias $\tau_{\text{obs}}(z,s) - \tau(z)$.
150	Under (A2)--(A3), $\tau_{\text{obs}}(0,s) = (1-\pi_s)\tau(0) + \pi_s\tau(1)$, so $\text{bias}_{\text{naive}}(0,s) = \pi_s \cdot \Delta\tau$.
151	
152	Global correction produces larger absolute bias when $|\text{bias}_{\text{global}}(0,s)| > |\text{bias}_{\text{naive}}(0,s)|$:
153	\begin{equation}
154	\frac{|\delta_s| \cdot |\Delta\tau|}{|1-2\bar{\pi}|} > \pi_s \cdot |\Delta\tau|.
155	\end{equation}
156	Since $\Delta\tau \neq 0$ (otherwise both biases are zero), dividing through gives:
157	\begin{equation}
158	\frac{|\delta_s|}{(1-2\bar{\pi}) \cdot \pi_s} > 1,
159	\end{equation}
160	where we use $1-2\bar{\pi} > 0$ from (A4).
161	
162	For high-error subgroups ($\pi_s > \bar{\pi}$, so $\delta_s > 0$): the condition becomes $(\pi_s - \bar{\pi}) / ((1-2\bar{\pi})\pi_s) > 1$, which simplifies to $\pi_s(1 - 1 + 2\bar{\pi}) > \bar{\pi}$, i.e., $2\bar{\pi}\pi_s > \bar{\pi}$, i.e., $\pi_s > 0.5$.
163	This is excluded by (A4), so global correction always reduces bias in high-error subgroups.
164	
165	For low-error subgroups ($\pi_s < \bar{\pi}$, so $\delta_s < 0$): the condition becomes $(\bar{\pi} - \pi_s) / ((1-2\bar{\pi})\pi_s) > 1$, which gives $\pi_s < \bar{\pi} / (1 - 2\bar{\pi} + 1) = \bar{\pi} / (2(1-\bar{\pi}))$.
166	When $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ experiences increased bias from global correction. \qed
167	
168	\paragraph{Extension to asymmetric misclassification.}
169	Proposition~\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).
170	Under asymmetric misclassification ($\mathrm{FPR}_s \neq \mathrm{FNR}_s$), the naive bias becomes $\mathrm{bias}_{\mathrm{naive}}(0,s) = \mathrm{FPR}_s \cdot \tau(1) + (1 - \mathrm{FPR}_s - 1)\tau(0)$ and the global correction bias depends on the full $2 \times 2$ structure of $B_s = M_{\mathrm{global}}^{-1} M_s - I$ (Remark~1 in Section~\ref{sec:theory}).
171	A sufficient condition for global correction to increase bias is
172	\begin{equation}
173	\|B_s\|_\infty > \max(\mathrm{FPR}_s, \mathrm{FNR}_s),
174	\end{equation}
175	which reduces to Equation~\eqref{eq:hurts_condition} when $\mathrm{FPR}_s = \mathrm{FNR}_s = \pi_s$.
176	In the asymmetric experiments (Appendix~\ref{app:asymmetric}), the symmetric diagnostic still achieves AUC $= 0.66$ when applied with $\pi_s = (\mathrm{FPR}_s + \mathrm{FNR}_s)/2$, suggesting practical robustness.
177	A fully general asymmetric diagnostic that accounts for the separate roles of FPR and FNR in each entry of $B_s$ is left to future work.
178	
179	\section{Semi-Synthetic Data Generating Process}
180	\label{app:dgp}
181	
182	\paragraph{Synthetic DGP (Sections~\ref{sec:bias_mechanism}--\ref{sec:diagnostic} and Appendix~\ref{sec:budget}).}
183	We generate $N = 5000$ observations.
184	Each observation belongs to one of $K \in \{2, 4\}$ subgroups $S \in \{1, \ldots, K\}$ with equal weights $w_s = 1/K$.
185	The binary effect modifier $Z \in \{0, 1\}$ is drawn with $P(Z{=}1) = 0.5$.
186	Treatment assignment is $T \sim \text{Bernoulli}(0.5)$, independent of $Z$ and $S$.
187	
188	The outcome is generated as:
189	\begin{equation}
190	Y = \tau(Z) \cdot T + \eta, \quad \eta \sim \mathcal{N}(0, 1),
191	\end{equation}
192	where the CATE function is $\tau(z) = \bar{\tau} + \Delta\tau \cdot (z - 0.5)$ with $\bar{\tau} = 0.5$.
193	The CATE heterogeneity $\Delta\tau \in \{0, 0.2, 0.5, 1.0\}$ controls the strength of treatment effect variation across levels of $Z$.
194	
195	Misclassification is symmetric: $\hat{Z} \neq Z$ with probability $\pi_s$ depending on subgroup.
196	For $K{=}2$: $\pi_1 = \bar{\pi} - \Delta_c/2$, $\pi_2 = \bar{\pi} + \Delta_c/2$, with $\bar{\pi} \in \{0.1, 0.2\}$ and $\Delta_c \in \{0, 0.05, 0.1, 0.15\}$.
197	For $K{=}4$, extreme regime: $\pi \in \{0.05, 0.10, 0.15, 0.25\}$; moderate regime: $\pi \in \{0.08, 0.12, 0.16, 0.20\}$.
198	
199	Expert labels are drawn as a simple random sample of size $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ from the full dataset, with true $Z$ observed for these observations.
200	
201	\paragraph{Semi-synthetic DGP (Section~\ref{sec:ec_hte_eval}).}
202	We sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\text{pool}} = 57{,}899$).
203	Subgroups are defined by crossing \texttt{has\_hashtag} $\times$ \texttt{text\_length\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \approx 38\%$, $S_1 \approx 38\%$, $S_2 \approx 12\%$, $S_3 \approx 12\%$.
204	Misclassification rates in the extreme regime are $\pi_{S_0} = 0.05$, $\pi_{S_1} = 0.10$, $\pi_{S_2} = 0.15$, $\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.
205	The outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.
206	
207	\paragraph{PPCI DGPs (Appendix~\ref{sec:ppci}).}
208	Four DGPs isolate error types: (A) covariate error only ($\sigma_{\text{outcome}} = 0$), (B) outcome error only ($\sigma_{\text{outcome}} = 0.5$), (C) both errors ($\sigma_{\text{outcome}} = 0.5$), (D) no error ($\sigma_{\text{outcome}} = 0$).
209	Outcome-side error is additive Gaussian noise on $Y$.
210	
211	\paragraph{CausalForestDML hyperparameters.}
212	All CausalForest experiments use \texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\text{estimators}} = 48$, $\texttt{min\_samples\_leaf} = 20$, \texttt{model\_y} = \texttt{LassoCV}(cv=3), and \texttt{model\_t} = \texttt{LogisticRegressionCV}.
213	These defaults were held constant across all configurations; no hyperparameter tuning was performed.
214	
215	\begin{figure*}[t]
216	\centering
217	\includegraphics[width=\textwidth]{figures/fig2_heatmap.pdf}
218	\caption{Bias amplification under global correction ($K{=}2$). (a) Low-error subgroup: correction always helps. (b) High-error subgroup: correction \emph{increases} bias when $\Delta\pi > 0.12$ (hatched), reaching 2.86$\times$.}
219	\label{fig:heatmap}
220	\end{figure*}
221	
222	\section{Extended Related Work}
223	\label{app:related}
224	
225	\paragraph{Measurement error details.}
226	\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.
227	\citet{carroll2006measurement} extend this to nonlinear models.
228	\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.
229	\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.
230	
231	\paragraph{Annotation model extensions.}
232	Beyond the foundational \citet{dawid1979maximum} model, \citet{passonneau2014benefits} incorporate item difficulty, \citet{hovy2013learning} learn annotator competence, and \citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.
233	
234	\paragraph{PPI extensions and text-as-data methods.}
235	\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\citep{zrnic2024active} achieves $>$80\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.
236	\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.
237	\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\ref{thm:bias_identity}.
238	
239	\paragraph{Treatment vs.\ effect-modifier misclassification.}
240	\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.
241	Our problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\hat{Z} \neq Z$).
242	The ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.
243	
244	\paragraph{Econometrics of binary misclassification.}
245	\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.
246	\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.
247	\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.
248	\citet{mahajan2006identification} and \citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.
249	Our setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\delta_s \times \Delta\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.
250	
251	\section{MCMC Convergence Diagnostics}
252	\label{app:mcmc}
253	
254	Table~\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.
255	All runs use 4 chains with 4000 iterations (2000 warmup).
256	Main experiments (Table~\ref{tab:main_results}) use a Dirichlet prior centered on $\hat{C}_{\text{global}}$ with concentration $\alpha_0$ estimated via empirical Bayes (marginal likelihood).
257	Appendix robustness experiments use a fixed Dirichlet prior ($\alpha{=}3$); since fixed-$\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.
258	This budget is sufficient for the $2{\times}2$ Dirichlet-Multinomial posterior; all runs achieve $\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.
259	
260	\begin{table}[h]
261	\centering
262	\small
263	\begin{tabular}{lcc}
264	\toprule
265	Diagnostic & Threshold & Achieved \\
266	\midrule
267	$\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\
268	ESS (min across all params) & $> 845$ & $> 1618$ \\
269	Divergent transitions & $= 0$ & $0$ \\
270	Singularity guard triggers & --- & extreme/$n{=}50$ only \\
271	\bottomrule
272	\end{tabular}
273	\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}
274	\label{tab:mcmc}
275	\end{table}
276	
277	\paragraph{Hyperprior sensitivity.}
278	Scaling the $\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\times$ to $2\times$ produces $<$1\% RMSE variation for $K{=}2$ and $\sim$4--5\% for $K{=}4$.
279	Coverage remains invariant across the sensitivity range.
280	These results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.
281	
282	\section{Diagnostic ROC Curves}
283	\label{app:roc}
284	
285	\begin{figure}[t]
286	\centering
287	\includegraphics[width=\columnwidth]{figures/fig4_roc.png}
288	\caption{ROC curves for the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}): $|\delta_s|/((1{-}2\bar\pi)\cdot\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.89$) and $\mathrm{CV}(\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\Delta\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.73$). The $\Delta\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}
289	\label{fig:roc}
290	\end{figure}
291	
292	\paragraph{Cost-asymmetric diagnostic thresholds.}
293	In practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.
294	Practitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.
295	
296	\section{Expert Budget Crossover Curves}
297	\label{app:budget}
298	\label{sec:budget}
299	
300	The crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\ref{fig:budget}).
301	Under moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.
302	HB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\text{expert}} \geq 1000$.
303	
304	\begin{figure*}[t]
305	\centering
306	\includegraphics[width=\textwidth]{figures/fig3_budget.pdf}
307	\caption{RMSE vs.\ expert budget ($n_{\text{expert}}$) across four regime$\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\pm 1$ SD across subgroups within each configuration.}
308	\label{fig:budget}
309	\end{figure*}
310	
311	\subsection{Budget Sensitivity: HB vs.\ Stratified MLE}
312	\label{app:budget_sensitivity}
313	
314	Hierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.
315	We sweep $n_{\text{expert}} \in \{25, 50, 75, 100, 150, 250\}$ under extreme heterogeneity ($\Delta\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).
316	Table~\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.
317	
318	\begin{table}[h]
319	\centering
320	\caption{RMSE across expert budgets under extreme heterogeneity.
321	HB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:
322	$n_{\text{expert}}{=}50$ for $K{=}2$ and $n_{\text{expert}}{=}75$ for $K{=}4$.}
323	\label{tab:budget_sensitivity}
324	\small
325	\begin{tabular}{crrrrc}
326	\toprule
327	$K$ & $n_{\text{expert}}$ & Global & Strat.\ MLE & HB EC-HTE & HB vs.\ MLE \\
328	\midrule
329	2 & 25 & \textbf{0.101} & 0.256 & 0.269 & $+4.9\%$ \\
330	2 & 50 & \textbf{0.088} & 0.275 & 0.231 & $\mathbf{-16.1\%}$ \\
331	2 & 75 & 0.084 & 0.091 & \textbf{0.089} & $-1.9\%$ \\
332	2 & 100 & 0.083 & 0.085 & \textbf{0.084} & $-0.8\%$ \\
333	2 & 150 & 0.081 & 0.077 & \textbf{0.077} & $-0.4\%$ \\
334	2 & 250 & 0.080 & 0.075 & \textbf{0.074} & $-0.1\%$ \\
335	\midrule
336	4 & 25 & \textbf{0.129} & 0.401 & 0.612 & $+52.5\%$ \\
337	4 & 50 & \textbf{0.117} & 0.380 & 0.470 & $+23.8\%$ \\
338	4 & 75 & \textbf{0.112} & 0.221 & 0.211 & $\mathbf{-4.4\%}$ \\
339	4 & 100 & \textbf{0.112} & 0.215 & 0.212 & $-1.3\%$ \\
340	4 & 150 & \textbf{0.109} & 0.157 & 0.152 & $-3.6\%$ \\
341	4 & 250 & \textbf{0.108} & 0.127 & 0.126 & $-1.0\%$ \\
342	\bottomrule
343	\end{tabular}
344	\end{table}
345	
346	Three regimes emerge.
347	At very low budgets ($n_{\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.
348	HB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\sim$6--12 labels per subgroup.
349	At moderate budgets ($n_{\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\%$ to $-16.1\%$), with the largest gains near the crossover point.
350	At high budgets ($n_{\text{expert}} \geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\%$.
351	Coverage remains $\geq 0.88$ for both methods across all budget levels.
352	
353	\subsection{Scalability to $K{=}8$ Subgroups}
354	\label{app:k8_subgroups}
355	
356	We test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.
357	
358	\paragraph{Setup.}
359	$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\text{expert}}{=}250$ (${\approx}31$ labels per subgroup), 100 MC replications.
360	Misclassification rates are uniformly spread: $\pi_s \in \{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\}$.
361	Treatment effects depend on $Z$ (not subgroup): $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
362	
363	\begin{table}[h]
364	\centering
365	\caption{EC-HTE at $K{=}8$ ($n_{\text{expert}}{=}250$, ${\approx}31$ labels/subgroup, 100 MC).}
366	\label{tab:k8_subgroups}
367	\small
368	\begin{tabular}{lccc}
369	\toprule
370	Method & Coverage & RMSE & $|\text{Bias}|$ \\
371	\midrule
372	Oracle       & 0.944 & 0.113 & 0.090 \\
373	Global       & 0.951 & 0.168 & 0.135 \\
374	HB EC-HTE    & 0.956 & 0.340 & 0.183 \\
375	Strat MLE    & 0.953 & 0.638 & 0.219 \\
376	Naive        & 0.913 & 0.133 & 0.107 \\
377	\bottomrule
378	\end{tabular}
379	\end{table}
380	
381	All CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\%, Strat MLE 95.3\%, Global 95.1\%.
382	HB partial pooling achieves a 47\% RMSE reduction over stratified MLE (0.340 vs.\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.
383	However, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.
384	
385	\paragraph{Per-subgroup breakdown.}
386	Table~\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.
387	
388	\begin{table}[h]
389	\centering
390	\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\pi$ subgroups but does not close the gap with Global.}
391	\label{tab:k8_per_subgroup}
392	\small
393	\begin{tabular}{cccccc}
394	\toprule
395	Subgroup & $\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\
396	\midrule
397	$s_0$ & 0.050 & 0.136 & 0.134 & \textbf{0.181} & 0.950 \\
398	$s_1$ & 0.093 & 0.133 & 0.132 & \textbf{0.154} & 0.970 \\
399	$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\
400	$s_3$ & 0.179 & 0.178 & 0.182 & \textbf{0.159} & 0.945 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "2182a146-7408-41f5-a2c3-35c5c98f421f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "\\section{EC-HTE Procedure}\n\\label{app:algorithm}\n\n\\begin{algorithm}[t]\n\\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}\n\\label{alg:echte}\n\\begin{algorithmic}[1]\n\\Require Observations $\\{(Y_i, W_i, \\hat{Z}_i, X_i)\\}_{i=1}^N$; expert labels $\\{Z_j^*\\}_{j=1}^{n_{\\text{expert}}}$; subgroup map $S: \\mathcal{X} \\to \\{1,\\ldots,K\\}$\n\\Ensure Corrected CATE estimates $\\hat{\\tau}(z)$ with variance-adjusted CIs\n\\Statex\n\\State \\textbf{Preconditions:} verify $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$ and $\\max_s(\\text{FPR}_s, \\text{FNR}_s) < 0.5$; if either fails, use global correction\n\\Statex\n\\State \\textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}\n\\For{$s = 1, \\ldots, K$}\n    \\State $C_s[j,\\cdot] \\sim \\mathrm{Dir}(\\alpha_0 \\cdot \\hat{C}_{\\text{global},j})$, \\; $\\alpha_0$ via empirical Bayes\n    \\State Gibbs sampler (4 chains, 4000 iter) on $\\{(\\hat{Z}_j, Z_j^*) : S_j = s\\}$\n    \\State $\\hat{C}_s \\gets$ posterior mean; verify $\\hat{R} < 1.01$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 2: Correct observed outcome moments}\n\\For{$s = 1, \\ldots, K$}\n    \\If{$\\kappa(\\hat{C}_s) > 100$} $\\hat{C}_s \\gets \\bar{C}$ \\Comment{singularity guard}\n    \\EndIf\n    \\State $\\tilde{\\boldsymbol{\\mu}}_s \\gets \\hat{C}_s^{-1} \\hat{\\boldsymbol{\\mu}}_s$\n\\EndFor\n\\Statex\n\\State \\textbf{Step 3: CausalForestDML with variance-adjusted SEs}\n\\State Train CausalForest (honest splitting) on corrected outcome moments $\\tilde{\\boldsymbol{\\mu}}_s$\n\\State $\\mathrm{se}_{\\mathrm{adj},i} \\gets \\sqrt{\\mathrm{diag}(\\hat{C}_{S_i}^{-1}\\, \\mathrm{diag}(\\mathrm{se}_i^2)\\, \\hat{C}_{S_i}^{-\\top})}$\n\\State \\Return $\\hat{\\tau}(z)$ with 95\\% CIs from $\\mathrm{se}_{\\mathrm{adj}}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Condition Number Guard Ablation}\n\\label{app:kappa_ablation}\n\nThe singularity guard in Algorithm~\\ref{alg:echte} (line~6) falls back to global correction when $\\kappa(\\hat{C}_s) > 100$.\nWe verify that this threshold is not load-bearing by sweeping $\\kappa \\in \\{10, 25, 50, 100, 200, 500, 1000\\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs).\nAcross all configurations, the maximum observed condition number is $\\kappa_{\\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\\times}$ safety margin below the $\\kappa{=}100$ threshold.\nConsequently, the guard never triggers at any tested threshold, and all $\\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.\nIn a stress test with near-random labeling ($\\pi_s \\approx 0.4$--$0.5$, $n_{\\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\\kappa{=}100$ guard and preventing catastrophic inversion.\nThe adaptive formula $\\kappa_{\\text{adapt}} = 10 \\sqrt{n_{\\text{expert}} / K}$ recovers $\\kappa{=}100$ for this regime and scales naturally with the estimation precision.\n\n\\section{Full Proof of Theorem~\\ref{thm:bias_identity}}\n\\label{app:derivation}\n\n\\paragraph{Setup.}\nUnder assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is\n\\begin{equation}\n\\tau_{\\text{obs}}(z, s) = \\sum_{z'} M_s[z, z'] \\cdot \\tau(z'),\n\\end{equation}\nwhere $M_s[z, z'] = P(Z{=}z' \\mid \\hat{Z}{=}z, S{=}s)$ is the mixing matrix.\nUnder (A2)--(A3), $M_s = \\bigl[\\begin{smallmatrix} 1-\\pi_s & \\pi_s \\\\ \\pi_s & 1-\\pi_s \\end{smallmatrix}\\bigr]$.\n\n\\paragraph{Global correction.}\nThe pooled mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s = \\bigl[\\begin{smallmatrix} 1-\\bar{\\pi} & \\bar{\\pi} \\\\ \\bar{\\pi} & 1-\\bar{\\pi} \\end{smallmatrix}\\bigr]$, with $\\bar{\\pi} = \\sum_s w_s \\pi_s$.\n\nGlobal correction applies $M_{\\text{global}}^{-1}$ to $\\tau_{\\text{obs}}(\\cdot, s)$:\n\\begin{equation}\n\\hat{\\tau}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} M_s \\cdot \\boldsymbol{\\tau}]_z,\n\\end{equation}\nwhere $\\boldsymbol{\\tau} = [\\tau(0), \\tau(1)]^\\top$.\n\n\\paragraph{Bias computation.}\nThe bias is $\\hat{\\tau}_{\\text{global}}(z, s) - \\tau(z) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z$.\n\nDirect computation gives:\n\\begin{equation}\nM_{\\text{global}}^{-1} = \\frac{1}{1 - 2\\bar{\\pi}} \\begin{bmatrix} 1-\\bar{\\pi} & -\\bar{\\pi} \\\\ -\\bar{\\pi} & 1-\\bar{\\pi} \\end{bmatrix}.\n\\end{equation}\nMultiplying by $M_s$:\n\\begin{equation}\n\\resizebox{.88\\columnwidth}{!}{$\\displaystyle\nM_{\\text{global}}^{-1} M_s = \\frac{1}{1-2\\bar{\\pi}} \\begin{bmatrix} (1{-}\\bar{\\pi})(1{-}\\pi_s) - \\bar{\\pi}\\pi_s & (1{-}\\bar{\\pi})\\pi_s - \\bar{\\pi}(1{-}\\pi_s) \\\\ -\\bar{\\pi}(1{-}\\pi_s) + (1{-}\\bar{\\pi})\\pi_s & -\\bar{\\pi}\\pi_s + (1{-}\\bar{\\pi})(1{-}\\pi_s) \\end{bmatrix}.\n$}\n\\end{equation}\n\nDefine $\\delta_s = \\pi_s - \\bar{\\pi}$. Substituting $\\pi_s = \\bar{\\pi} + \\delta_s$:\n\\begin{equation}\nM_{\\text{global}}^{-1} M_s - I = \\frac{\\delta_s}{1-2\\bar{\\pi}} \\begin{bmatrix} -1 & 1 \\\\ 1 & -1 \\end{bmatrix}.\n\\end{equation}\n\nTo verify: the $(1,1)$ entry of $M_{\\text{global}}^{-1} M_s$ is\n{\\small\n\\begin{align}\n&\\frac{(1{-}\\bar{\\pi})(1{-}\\bar{\\pi}{-}\\delta_s) - \\bar{\\pi}(\\bar{\\pi}{+}\\delta_s)}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{(1{-}\\bar{\\pi})^2 - (1{-}\\bar{\\pi})\\delta_s - \\bar{\\pi}^2 - \\bar{\\pi}\\delta_s}{1-2\\bar{\\pi}} \\nonumber\\\\\n&= \\frac{1 - 2\\bar{\\pi} - \\delta_s}{1-2\\bar{\\pi}} = 1 - \\frac{\\delta_s}{1-2\\bar{\\pi}}.\n\\end{align}\n}\n\nApplying $(M_{\\text{global}}^{-1} M_s - I)$ to $\\boldsymbol{\\tau}$:\n{\\small\n\\begin{align}\n\\text{bias}(z{=}0, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(-\\tau(0) + \\tau(1)) = +\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}}, \\\\\n\\text{bias}(z{=}1, s) &= \\tfrac{\\delta_s}{1-2\\bar{\\pi}}(\\tau(0) - \\tau(1)) = -\\tfrac{\\delta_s \\cdot \\Delta\\tau}{1-2\\bar{\\pi}},\n\\end{align}\n}\nwhere $\\Delta\\tau = \\tau(1) - \\tau(0)$. \\qed\n\n\\paragraph{Finite-sample remainder.}\nWhen $\\hat{C}_s = C_s + E_s$ with $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$ (central limit theorem), the estimated correction $\\hat{M}_{\\text{global}}^{-1} \\hat{M}_s$ deviates from its population counterpart by\n$\\|\\hat{M}_{\\text{global}}^{-1} \\hat{M}_s - M_{\\text{global}}^{-1} M_s\\| \\leq \\kappa(M_{\\text{global}}) \\cdot O_p(n_{\\text{expert}}^{-1/2})$,\nwhere $\\kappa(M) = \\|M\\| \\cdot \\|M^{-1}\\|$ is the condition number~\\citep{stewart1990matrix}.\nThis motivates the $\\kappa > 100$ singularity guard in Section~\\ref{sec:method}.\n\n\\section{Multi-class Extension and Proof}\n\\label{app:multiclass}\n\n\\begin{corollary}[Multi-class Extension]\n\\label{cor:multiclass}\nFor $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to\n\\begin{equation}\n\\mathrm{bias}_{\\mathrm{global}}(z, s) = \\sum_{j=1}^{J} \\bigl(\\bar{\\pi}_j - \\pi_{s,j}\\bigr) \\cdot \\bigl(\\tau(j) - \\bar{\\tau}\\bigr) \\cdot g(\\bar{\\pi}),\n\\label{eq:multiclass}\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms.\\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\\bar{\\pi}) = 1/(1 - 3\\bar{\\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\\bar{\\pi})$. In general, $g(\\bar{\\pi}) = 1/(1 - J\\bar{\\pi}/(J-1))$.}\nThe essential structure, $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.\n\\end{corollary}\n\n\\paragraph{Proof.}\nFor $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \\times J$ with entries $M_s[j, j'] = P(Z{=}j' \\mid \\hat{Z}{=}j, S{=}s)$.\nThe global mixing matrix is $M_{\\text{global}} = \\sum_s w_s M_s$.\n\nThe bias of global correction in subgroup $s$ at level $z$ is:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [(M_{\\text{global}}^{-1} M_s - I) \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nWrite $M_s = M_{\\text{global}} + \\Delta_s$ where $\\Delta_s = M_s - M_{\\text{global}}$ satisfies $\\sum_s w_s \\Delta_s = 0$.\nThen $M_{\\text{global}}^{-1} M_s = I + M_{\\text{global}}^{-1} \\Delta_s$, so:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = [M_{\\text{global}}^{-1} \\Delta_s \\cdot \\boldsymbol{\\tau}]_z.\n\\end{equation}\n\nFor symmetric misclassification with per-class error rates $\\pi_{s,j}$ and pooled rates $\\bar{\\pi}_j$, the entries of $\\Delta_s$ have the form $\\Delta_s[j,j'] = (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.\nExpanding the matrix-vector product and collecting terms yields:\n\\begin{equation}\n\\text{bias}_{\\text{global}}(z, s) = \\sum_{j=1}^{J} (\\bar{\\pi}_j - \\pi_{s,j}) \\cdot (\\tau(j) - \\bar{\\tau}) \\cdot g(\\bar{\\pi}),\n\\end{equation}\nwhere $g(\\bar{\\pi})$ collects the matrix-inversion amplification terms and $\\bar{\\tau} = \\sum_j P(Z{=}j) \\tau(j)$.\n\nThe essential structure $\\sum_s w_s (\\bar{\\pi}_j - \\pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.\nFor non-uniform off-diagonal entries, the scalar amplification $g(\\bar{\\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \\cdot \\Delta\\tau$ persists but a closed-form amplification factor does not. \\qed\n\n\\section{Proof of Proposition~\\ref{prop:debiasing_hurts}}\n\\label{app:debiasing_hurts}\n\nThe naive estimator has bias $\\tau_{\\text{obs}}(z,s) - \\tau(z)$.\nUnder (A2)--(A3), $\\tau_{\\text{obs}}(0,s) = (1-\\pi_s)\\tau(0) + \\pi_s\\tau(1)$, so $\\text{bias}_{\\text{naive}}(0,s) = \\pi_s \\cdot \\Delta\\tau$.\n\nGlobal correction produces larger absolute bias when $|\\text{bias}_{\\text{global}}(0,s)| > |\\text{bias}_{\\text{naive}}(0,s)|$:\n\\begin{equation}\n\\frac{|\\delta_s| \\cdot |\\Delta\\tau|}{|1-2\\bar{\\pi}|} > \\pi_s \\cdot |\\Delta\\tau|.\n\\end{equation}\nSince $\\Delta\\tau \\neq 0$ (otherwise both biases are zero), dividing through gives:\n\\begin{equation}\n\\frac{|\\delta_s|}{(1-2\\bar{\\pi}) \\cdot \\pi_s} > 1,\n\\end{equation}\nwhere we use $1-2\\bar{\\pi} > 0$ from (A4).\n\nFor high-error subgroups ($\\pi_s > \\bar{\\pi}$, so $\\delta_s > 0$): the condition becomes $(\\pi_s - \\bar{\\pi}) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which simplifies to $\\pi_s(1 - 1 + 2\\bar{\\pi}) > \\bar{\\pi}$, i.e., $2\\bar{\\pi}\\pi_s > \\bar{\\pi}$, i.e., $\\pi_s > 0.5$.\nThis is excluded by (A4), so global correction always reduces bias in high-error subgroups.\n\nFor low-error subgroups ($\\pi_s < \\bar{\\pi}$, so $\\delta_s < 0$): the condition becomes $(\\bar{\\pi} - \\pi_s) / ((1-2\\bar{\\pi})\\pi_s) > 1$, which gives $\\pi_s < \\bar{\\pi} / (1 - 2\\bar{\\pi} + 1) = \\bar{\\pi} / (2(1-\\bar{\\pi}))$.\nWhen $\\bar{\\pi} = 0.15$, any subgroup with $\\pi_s < 0.088$ experiences increased bias from global correction. \\qed\n\n\\paragraph{Extension to asymmetric misclassification.}\nProposition~\\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).\nUnder asymmetric misclassification ($\\mathrm{FPR}_s \\neq \\mathrm{FNR}_s$), the naive bias becomes $\\mathrm{bias}_{\\mathrm{naive}}(0,s) = \\mathrm{FPR}_s \\cdot \\tau(1) + (1 - \\mathrm{FPR}_s - 1)\\tau(0)$ and the global correction bias depends on the full $2 \\times 2$ structure of $B_s = M_{\\mathrm{global}}^{-1} M_s - I$ (Remark~1 in Section~\\ref{sec:theory}).\nA sufficient condition for global correction to increase bias is\n\\begin{equation}\n\\|B_s\\|_\\infty > \\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s),\n\\end{equation}\nwhich reduces to Equation~\\eqref{eq:hurts_condition} when $\\mathrm{FPR}_s = \\mathrm{FNR}_s = \\pi_s$.\nIn the asymmetric experiments (Appendix~\\ref{app:asymmetric}), the symmetric diagnostic still achieves AUC $= 0.66$ when applied with $\\pi_s = (\\mathrm{FPR}_s + \\mathrm{FNR}_s)/2$, suggesting practical robustness.\nA fully general asymmetric diagnostic that accounts for the separate roles of FPR and FNR in each entry of $B_s$ is left to future work.\n\n\\section{Semi-Synthetic Data Generating Process}\n\\label{app:dgp}\n\n\\paragraph{Synthetic DGP (Sections~\\ref{sec:bias_mechanism}--\\ref{sec:diagnostic} and Appendix~\\ref{sec:budget}).}\nWe generate $N = 5000$ observations.\nEach observation belongs to one of $K \\in \\{2, 4\\}$ subgroups $S \\in \\{1, \\ldots, K\\}$ with equal weights $w_s = 1/K$.\nThe binary effect modifier $Z \\in \\{0, 1\\}$ is drawn with $P(Z{=}1) = 0.5$.\nTreatment assignment is $T \\sim \\text{Bernoulli}(0.5)$, independent of $Z$ and $S$.\n\nThe outcome is generated as:\n\\begin{equation}\nY = \\tau(Z) \\cdot T + \\eta, \\quad \\eta \\sim \\mathcal{N}(0, 1),\n\\end{equation}\nwhere the CATE function is $\\tau(z) = \\bar{\\tau} + \\Delta\\tau \\cdot (z - 0.5)$ with $\\bar{\\tau} = 0.5$.\nThe CATE heterogeneity $\\Delta\\tau \\in \\{0, 0.2, 0.5, 1.0\\}$ controls the strength of treatment effect variation across levels of $Z$.\n\nMisclassification is symmetric: $\\hat{Z} \\neq Z$ with probability $\\pi_s$ depending on subgroup.\nFor $K{=}2$: $\\pi_1 = \\bar{\\pi} - \\Delta_c/2$, $\\pi_2 = \\bar{\\pi} + \\Delta_c/2$, with $\\bar{\\pi} \\in \\{0.1, 0.2\\}$ and $\\Delta_c \\in \\{0, 0.05, 0.1, 0.15\\}$.\nFor $K{=}4$, extreme regime: $\\pi \\in \\{0.05, 0.10, 0.15, 0.25\\}$; moderate regime: $\\pi \\in \\{0.08, 0.12, 0.16, 0.20\\}$.\n\nExpert labels are drawn as a simple random sample of size $n_{\\text{expert}} \\in \\{50, 100, 250, 500, 1000, 2000\\}$ from the full dataset, with true $Z$ observed for these observations.\n\n\\paragraph{Semi-synthetic DGP (Section~\\ref{sec:ec_hte_eval}).}\nWe sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\\text{pool}} = 57{,}899$).\nSubgroups are defined by crossing \\texttt{has\\_hashtag} $\\times$ \\texttt{text\\_length\\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \\approx 38\\%$, $S_1 \\approx 38\\%$, $S_2 \\approx 12\\%$, $S_3 \\approx 12\\%$.\nMisclassification rates in the extreme regime are $\\pi_{S_0} = 0.05$, $\\pi_{S_1} = 0.10$, $\\pi_{S_2} = 0.15$, $\\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.\nThe outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.\n\n\\paragraph{PPCI DGPs (Appendix~\\ref{sec:ppci}).}\nFour DGPs isolate error types: (A) covariate error only ($\\sigma_{\\text{outcome}} = 0$), (B) outcome error only ($\\sigma_{\\text{outcome}} = 0.5$), (C) both errors ($\\sigma_{\\text{outcome}} = 0.5$), (D) no error ($\\sigma_{\\text{outcome}} = 0$).\nOutcome-side error is additive Gaussian noise on $Y$.\n\n\\paragraph{CausalForestDML hyperparameters.}\nAll CausalForest experiments use \\texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\\text{estimators}} = 48$, $\\texttt{min\\_samples\\_leaf} = 20$, \\texttt{model\\_y} = \\texttt{LassoCV}(cv=3), and \\texttt{model\\_t} = \\texttt{LogisticRegressionCV}.\nThese defaults were held constant across all configurations; no hyperparameter tuning was performed.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig2_heatmap.pdf}\n\\caption{Bias amplification under global correction ($K{=}2$). (a) Low-error subgroup: correction always helps. (b) High-error subgroup: correction \\emph{increases} bias when $\\Delta\\pi > 0.12$ (hatched), reaching 2.86$\\times$.}\n\\label{fig:heatmap}\n\\end{figure*}\n\n\\section{Extended Related Work}\n\\label{app:related}\n\n\\paragraph{Measurement error details.}\n\\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.\n\\citet{carroll2006measurement} extend this to nonlinear models.\n\\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.\n\\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.\n\n\\paragraph{Annotation model extensions.}\nBeyond the foundational \\citet{dawid1979maximum} model, \\citet{passonneau2014benefits} incorporate item difficulty, \\citet{hovy2013learning} learn annotator competence, and \\citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.\n\n\\paragraph{PPI extensions and text-as-data methods.}\n\\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\\citep{zrnic2024active} achieves $>$80\\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.\n\\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.\n\\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\\ref{thm:bias_identity}.\n\n\\paragraph{Treatment vs.\\ effect-modifier misclassification.}\n\\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.\nOur problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\\hat{Z} \\neq Z$).\nThe ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.\n\n\\paragraph{Econometrics of binary misclassification.}\n\\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.\n\\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.\n\\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.\n\\citet{mahajan2006identification} and \\citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.\nOur setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\\delta_s \\times \\Delta\\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.\n\n\\section{MCMC Convergence Diagnostics}\n\\label{app:mcmc}\n\nTable~\\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.\nAll runs use 4 chains with 4000 iterations (2000 warmup).\nMain experiments (Table~\\ref{tab:main_results}) use a Dirichlet prior centered on $\\hat{C}_{\\text{global}}$ with concentration $\\alpha_0$ estimated via empirical Bayes (marginal likelihood).\nAppendix robustness experiments use a fixed Dirichlet prior ($\\alpha{=}3$); since fixed-$\\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.\nThis budget is sufficient for the $2{\\times}2$ Dirichlet-Multinomial posterior; all runs achieve $\\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nDiagnostic & Threshold & Achieved \\\\\n\\midrule\n$\\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\\\\nESS (min across all params) & $> 845$ & $> 1618$ \\\\\nDivergent transitions & $= 0$ & $0$ \\\\\nSingularity guard triggers & --- & extreme/$n{=}50$ only \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}\n\\label{tab:mcmc}\n\\end{table}\n\n\\paragraph{Hyperprior sensitivity.}\nScaling the $\\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\\times$ to $2\\times$ produces $<$1\\% RMSE variation for $K{=}2$ and $\\sim$4--5\\% for $K{=}4$.\nCoverage remains invariant across the sensitivity range.\nThese results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.\n\n\\section{Diagnostic ROC Curves}\n\\label{app:roc}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_roc.png}\n\\caption{ROC curves for the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}): $|\\delta_s|/((1{-}2\\bar\\pi)\\cdot\\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.89$) and $\\mathrm{CV}(\\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\\Delta\\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\\Delta\\pi \\times \\Delta\\tau|$ product (AUC $= 0.73$). The $\\Delta\\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}\n\\label{fig:roc}\n\\end{figure}\n\n\\paragraph{Cost-asymmetric diagnostic thresholds.}\nIn practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.\nPractitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.\n\n\\section{Expert Budget Crossover Curves}\n\\label{app:budget}\n\\label{sec:budget}\n\nThe crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\\ref{fig:budget}).\nUnder moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.\nHB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\\text{expert}} \\geq 1000$.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig3_budget.pdf}\n\\caption{RMSE vs.\\ expert budget ($n_{\\text{expert}}$) across four regime$\\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\\pm 1$ SD across subgroups within each configuration.}\n\\label{fig:budget}\n\\end{figure*}\n\n\\subsection{Budget Sensitivity: HB vs.\\ Stratified MLE}\n\\label{app:budget_sensitivity}\n\nHierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.\nWe sweep $n_{\\text{expert}} \\in \\{25, 50, 75, 100, 150, 250\\}$ under extreme heterogeneity ($\\Delta\\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).\nTable~\\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.\n\n\\begin{table}[h]\n\\centering\n\\caption{RMSE across expert budgets under extreme heterogeneity.\nHB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:\n$n_{\\text{expert}}{=}50$ for $K{=}2$ and $n_{\\text{expert}}{=}75$ for $K{=}4$.}\n\\label{tab:budget_sensitivity}\n\\small\n\\begin{tabular}{crrrrc}\n\\toprule\n$K$ & $n_{\\text{expert}}$ & Global & Strat.\\ MLE & HB EC-HTE & HB vs.\\ MLE \\\\\n\\midrule\n2 & 25 & \\textbf{0.101} & 0.256 & 0.269 & $+4.9\\%$ \\\\\n2 & 50 & \\textbf{0.088} & 0.275 & 0.231 & $\\mathbf{-16.1\\%}$ \\\\\n2 & 75 & 0.084 & 0.091 & \\textbf{0.089} & $-1.9\\%$ \\\\\n2 & 100 & 0.083 & 0.085 & \\textbf{0.084} & $-0.8\\%$ \\\\\n2 & 150 & 0.081 & 0.077 & \\textbf{0.077} & $-0.4\\%$ \\\\\n2 & 250 & 0.080 & 0.075 & \\textbf{0.074} & $-0.1\\%$ \\\\\n\\midrule\n4 & 25 & \\textbf{0.129} & 0.401 & 0.612 & $+52.5\\%$ \\\\\n4 & 50 & \\textbf{0.117} & 0.380 & 0.470 & $+23.8\\%$ \\\\\n4 & 75 & \\textbf{0.112} & 0.221 & 0.211 & $\\mathbf{-4.4\\%}$ \\\\\n4 & 100 & \\textbf{0.112} & 0.215 & 0.212 & $-1.3\\%$ \\\\\n4 & 150 & \\textbf{0.109} & 0.157 & 0.152 & $-3.6\\%$ \\\\\n4 & 250 & \\textbf{0.108} & 0.127 & 0.126 & $-1.0\\%$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree regimes emerge.\nAt very low budgets ($n_{\\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.\nHB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\\sim$6--12 labels per subgroup.\nAt moderate budgets ($n_{\\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\\%$ to $-16.1\\%$), with the largest gains near the crossover point.\nAt high budgets ($n_{\\text{expert}} \\geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\\%$.\nCoverage remains $\\geq 0.88$ for both methods across all budget levels.\n\n\\subsection{Scalability to $K{=}8$ Subgroups}\n\\label{app:k8_subgroups}\n\nWe test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.\n\n\\paragraph{Setup.}\n$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\\text{expert}}{=}250$ (${\\approx}31$ labels per subgroup), 100 MC replications.\nMisclassification rates are uniformly spread: $\\pi_s \\in \\{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\\}$.\nTreatment effects depend on $Z$ (not subgroup): $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE at $K{=}8$ ($n_{\\text{expert}}{=}250$, ${\\approx}31$ labels/subgroup, 100 MC).}\n\\label{tab:k8_subgroups}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle       & 0.944 & 0.113 & 0.090 \\\\\nGlobal       & 0.951 & 0.168 & 0.135 \\\\\nHB EC-HTE    & 0.956 & 0.340 & 0.183 \\\\\nStrat MLE    & 0.953 & 0.638 & 0.219 \\\\\nNaive        & 0.913 & 0.133 & 0.107 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\\%, Strat MLE 95.3\\%, Global 95.1\\%.\nHB partial pooling achieves a 47\\% RMSE reduction over stratified MLE (0.340 vs.\\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.\nHowever, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.\n\n\\paragraph{Per-subgroup breakdown.}\nTable~\\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\\pi$ subgroups but does not close the gap with Global.}\n\\label{tab:k8_per_subgroup}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSubgroup & $\\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\\\\n\\midrule\n$s_0$ & 0.050 & 0.136 & 0.134 & \\textbf{0.181} & 0.950 \\\\\n$s_1$ & 0.093 & 0.133 & 0.132 & \\textbf{0.154} & 0.970 \\\\\n$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\\\\n$s_3$ & 0.179 & 0.178 & 0.182 & \\textbf{0.159} & 0.945 \\\\",
      "numLines": 400,
      "startLine": 1,
      "totalLines": 1538
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_016o5LPoFVNepcqRY1HJVs8n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 400,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "1ead745c-37c8-478a-bb52-fa6f0d49a504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjQrtrcU6xrQTDd17FDZwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15903,
      "cache_read_input_tokens": 26426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15903
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

_source line 35 · 2026-05-24T04:29:28.326Z_

<details><summary>↩ Tool result · `toolu_016o5LPoFVNepcqRY1HJVs8n`</summary>

```text
400	$s_3$ & 0.179 & 0.178 & 0.182 & \textbf{0.159} & 0.945 \\
401	$s_4$ & 0.221 & 0.263 & 0.343 & \textbf{0.163} & 0.940 \\
402	$s_5$ & 0.264 & 0.421 & 0.711 & \textbf{0.164} & 0.965 \\
403	$s_6$ & 0.307 & 0.634 & 1.375 & \textbf{0.177} & 0.940 \\
404	$s_7$ & 0.350 & 0.432 & 0.809 & \textbf{0.183} & 0.960 \\
405	\bottomrule
406	\end{tabular}
407	\end{table}
408	
409	RMSE degradation is concentrated in high-$\pi$ subgroups ($s_4$--$s_7$, $\pi \geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\pi_s$ and HB RMSE).
410	Low-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\% below global correction.
411	HB partial pooling reduces MLE RMSE by 24--54\% in the high-$\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.
412	Coverage remains $\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.
413	Adaptive shrinkage---increasing the prior strength for high-$\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.
414	
415	We explored adaptive shrinkage ($\alpha{=}10$ for high-$\pi$ subgroups vs.\ default $\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\% improvement) by attenuating estimation noise in high-$\pi$ subgroups.
416	However, RMSE remains 30\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\sim}$31 expert labels) rather than the shrinkage method itself.
417	This establishes $K{=}8$ at $n_{\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\geq$94\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\text{expert}} \geq 500$ (${\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.
418	
419	\section{Asymmetric Misclassification Extension}
420	\label{app:asymmetric}
421	
422	Assumption~(A2) imposes symmetric misclassification ($\text{FPR}_s = \text{FNR}_s = \pi_s$), which simplifies the bias decomposition but is not necessary for it.
423	Real LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.
424	
425	\paragraph{General bias formula.}
426	For asymmetric confusion matrices $C_s = \bigl(\begin{smallmatrix} 1{-}\text{FPR}_s & \text{FPR}_s \\ \text{FNR}_s & 1{-}\text{FNR}_s \end{smallmatrix}\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\text{global}}^{-1} M_s - I$.
427	Since both $M_s$ and $M_{\text{global}}$ are row-stochastic, $B_s \mathbf{1} = \mathbf{0}$.
428	Decomposing $\boldsymbol{\tau} = \tau(0)\mathbf{1} + \Delta\tau \, \mathbf{e}_1$ gives:
429	\begin{equation}
430	\text{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1},
431	\end{equation}
432	where $[B_s]_{z,1}$ depends only on $\{\text{FPR}_k, \text{FNR}_k, w_k\}$, not on $\Delta\tau$.
433	Under~(A2), this reduces to $\delta_s \Delta\tau / (1 - 2\bar{\pi})$ (Theorem~\ref{thm:bias_identity}).
434	
435	\paragraph{Empirical validation.}
436	We test three asymmetric configurations ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs each): \emph{Cross} (FPR/FNR = 0.10/0.20 vs.\ 0.25/0.10), \emph{Co-directional} (0.05/0.15 vs.\ 0.20/0.30), and \emph{Extreme} (0.03/0.25 vs.\ 0.30/0.05).
437	Regressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.
438	Table~\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\Delta\tau \in \{0.1, \ldots, 0.5\}$.
439	EC-HTE reduces $|\text{bias}|$ from 0.025 (global) to 0.006, a $4\times$ improvement, with lower RMSE (0.033 vs.\ 0.040) and substantially better coverage (0.90 vs.\ 0.78).
440	
441	\begin{table}[t]
442	\centering
443	\caption{Asymmetric misclassification results ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\Delta\tau$.}
444	\label{tab:asymmetric}
445	\small
446	\begin{tabular}{l ccc}
447	\toprule
448	Method & $|\text{Bias}| \downarrow$ & RMSE $\downarrow$ & Coverage $\uparrow$ \\
449	\midrule
450	Naive & 0.047 & 0.053 & 0.48 \\
451	Global & 0.025 & 0.040 & 0.78 \\
452	HB EC-HTE & \textbf{0.006} & \textbf{0.033} & \textbf{0.90} \\
453	\bottomrule
454	\end{tabular}
455	\end{table}
456	
457	\section{Supplementary Main Results}
458	\label{app:main_supp}
459	
460	\begin{table}[t]
461	\centering
462	\caption{Additional configurations from the main experiment. $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\dagger$RMSE exceeds Global.}
463	\label{tab:main_supp}
464	\small
465	\begin{tabular}{ll ccc}
466	\toprule
467	Configuration & Method & $|\text{Bias}|$ & RMSE & Cov. \\
468	\midrule
469	\multirow{4}{*}{\shortstack[l]{Synthetic DIM\\$K{=}2$, moderate, $n{=}250$}}
470	 & Naive & 0.018 & 0.064 & 0.95 \\
471	 & Global & 0.009 & 0.074 & 0.96 \\
472	 & Strat.\ MLE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
473	 & HB EC-HTE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
474	\midrule
475	\multirow{4}{*}{\shortstack[l]{Semi-synthetic\\TweetEval, extreme, $n{=}250$}}
476	 & Naive & 0.027 & 0.103 & 0.93 \\
477	 & Global & \textbf{0.023} & 0.124 & 0.92 \\
478	 & Strat.\ MLE & 0.032 & 0.248$^\dagger$ & 0.91 \\
479	 & HB EC-HTE & 0.027 & 0.225$^\dagger$ & 0.91 \\
480	\bottomrule
481	\end{tabular}
482	\end{table}
483	
484	\section{PPCI Complementarity Results}
485	\label{app:ppci}
486	\label{sec:ppci}
487	
488	EC-HTE composes with PPCI~\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\%; Appendix~\ref{app:rlearner}).
489	
490	\begin{table*}[t]
491	\centering
492	\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\sigma{=}0.5$); C: both errors; D: no error. Values are $|\text{bias}|$ and RMSE averaged over two subgroups. $^\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}
493	\label{tab:ppci}
494	\small
495	\begin{tabular}{ll cccc}
496	\toprule
497	DGP & Method & $|\text{Bias}|_{z=0}$ & $|\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\
498	\midrule
499	\multirow{5}{*}{A: Covariate}
500	 & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\
501	 & Global & 0.063 & 0.055 & 0.101 & 0.102 \\
502	 & EC-HTE & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
503	 & PPCI & \textbf{0.015} & 0.020 & 0.162 & 0.168 \\
504	 & EC-HTE+PPCI & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
505	\midrule
506	\multirow{5}{*}{B: Outcome}
507	 & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\
508	 & Global & 0.185 & 0.208 & 0.204 & 0.228 \\
509	 & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\
510	 & PPCI & 0.015 & \textbf{0.020} & 0.171 & 0.176 \\
511	 & EC-HTE+PPCI & \textbf{0.012} & 0.023 & 0.171 & 0.186 \\
512	\midrule
513	\multirow{5}{*}{C: Both}
514	 & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\
515	 & Global & 0.182 & 0.209 & 0.233 & 0.235 \\
516	 & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\
517	 & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\
518	 & EC-HTE+PPCI$^\star$ & \textbf{0.007} & \textbf{0.008} & 0.209 & 0.223 \\
519	\midrule
520	\multirow{5}{*}{D: None}
521	 & Naive & \textbf{0.007} & 0.003 & 0.060 & 0.065 \\
522	 & Global & 0.010 & \textbf{0.002} & 0.061 & 0.071 \\
523	 & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\
524	 & PPCI & \textbf{0.007} & \textbf{0.003} & 0.060 & 0.065 \\
525	 & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\
526	\bottomrule
527	\end{tabular}
528	\end{table*}
529	
530	The complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).
531	Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.
532	Under covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.
533	
534	\section{Real-Data Case Study: Hate Speech Detection}
535	\label{app:hatespeech}
536	
537	We apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.
538	Four text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \approx 624$ each).
539	
540	\paragraph{Positive finding: real-world heterogeneity.}
541	Per-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\Delta\pi = 0.117$) in a real annotation setting.
542	At the error-type level, FPR ranges from 8.5\% to 21.3\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.
543	
544	\paragraph{Boundary condition: statistical power at extreme FNR.}
545	Correction results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.
546	The high baseline FNR (53.3\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\times$), rendering the comparison underpowered.
547	When $P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.
548	This complements the expert budget threshold identified in Appendix~\ref{sec:budget}: EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality.
549	
550	\paragraph{Diagnostic connection.}
551	The diagnostic criterion ($\Delta\pi \times \Delta\tau$, Section~\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.
552	This case study illustrates that even when $\Delta\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.
553	A practical prerequisite is that the per-subgroup confusion matrix condition number $\kappa(\hat{C}_s)$ remain moderate; when $\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.
554	
555	\section{Cross-Model Consistency}
556	\label{app:multilm}
557	
558	We evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.
559	Six text-feature subgroups are defined by crossing hashtag presence and text length.
560	Spearman rank correlations of per-subgroup error rates across all six subgroups range from $\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.
561	Two subgroups with $n \leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%
562	\footnote{The filtered $\Delta\pi$ values in Table~\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\Delta\pi > 0.05$ on the four retained subgroups.}
563	
564	\begin{table}[t]
565	\centering
566	\caption{Effective misclassification heterogeneity ($\Delta\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \geq 10$).}
567	\label{tab:multilm}
568	\small
569	\begin{tabular}{lcc}
570	\toprule
571	Model & Effective $\Delta\pi$ & $> 0.05$? \\
572	\midrule
573	GPT-3.5-Turbo & 0.198 & \checkmark \\
574	GPT-4-Turbo & 0.149 & \checkmark \\
575	GPT-4o-mini & 0.136 & \checkmark \\
576	GPT-5.4 & 0.114 & \checkmark \\
577	GPT-4.1 & 0.098 & \checkmark \\
578	GPT-4o & 0.080 & \checkmark \\
579	\bottomrule
580	\end{tabular}
581	\end{table}
582	
583	All six models exhibit effective $\Delta\pi > 0.05$ on the four retained subgroups (Table~\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\texttt{True\_medium}: tweets with hashtags and medium text length).
584	Newer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\Delta\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.
585	These results were obtained with a single API provider; open-source model validation appears in Appendix~\ref{app:multilm_opensource}.
586	
587	\section{Open-Source Multi-LLM Validation}
588	\label{app:multilm_opensource}
589	
590	We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.
591	Table~\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.
592	All four models exhibit $\Delta\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.
593	Subgroup error rankings are consistent across architectures: \texttt{True\_short} (short tweets with hashtags) has the lowest $\pi_s$ in 3 of 4 models, while \texttt{False\_medium} (medium tweets without hashtags) has the highest.
594	
595	\begin{table}[t]
596	\centering
597	\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\Delta\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) triggers.}
598	\label{tab:multilm_cm}
599	\small
600	\begin{tabular}{lcccl}
601	\toprule
602	Model & Acc.\ & $\Delta\pi$ & Prop2 & Strongest \\
603	\midrule
604	Llama-3.1-8B & 0.755 & 0.141 & 1/4 & True\_short \\
605	Qwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\_short \\
606	Gemma-2-9B & 0.763 & 0.125 & 4/4 & True\_medium \\
607	Mistral-7B & 0.802 & 0.134 & 0/4 & --- \\
608	\bottomrule
609	\end{tabular}
610	\end{table}
611	
612	\paragraph{Semi-synthetic budget sweep.}
613	We run the full EC-HTE pipeline with $K{=}2$ subgroups and $\Delta\tau{=}0.3$, using each model's empirical confusion matrices.
614	Table~\ref{tab:multilm_budget} reports coverage and RMSE crossover points.
615	EC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\text{expert}}{=}1{,}000$, consistent across all four models.
616	Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\Delta\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\ref{sec:budget}.
617	
618	\begin{table}[t]
619	\centering
620	\caption{Semi-synthetic budget sweep ($K{=}2$, $\Delta\tau{=}0.3$, 50 MC runs; see Appendix~\ref{app:mcse} for MC tier justification). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}
621	\label{tab:multilm_budget}
622	\small
623	\begin{tabular}{lcccc}
624	\toprule
625	Model & $\Delta\pi_{K{=}2}$ & Naive Cov.\ & HB Cov.\ ($n{=}1000$) & Crossover \\
626	\midrule
627	Llama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\
628	Qwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\
629	Gemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\
630	Mistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\
631	\midrule
632	\textit{Average} & --- & \textit{0.714} & \textit{0.939} & --- \\
633	\bottomrule
634	\end{tabular}
635	\end{table}
636	
637	\paragraph{Gemma boundary case.}
638	Gemma-2-9B triggers the Proposition~\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\texttt{False\_medium} FNR $= 0.437$).
639	At small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\times$ naive), illustrating the budget guideline from Appendix~\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.
640	At $n \geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.
641	
642	\paragraph{Heterogeneous-$\tau$ DGP.}
643	To assess whether the constant-$\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\Delta\tau \in [0.1, 0.6]$, $K{=}2$, 50 MC runs).
644	EC-HTE achieves lower $|\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\ 0.031, a 68\% reduction).
645	In the high-$\Delta\tau$ subgroup (\texttt{True\_short}, $\Delta\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\ 0.258, 18\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.
646	Aggregate RMSE remains comparable to global correction because low-$\Delta\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\ref{sec:budget}.
647	
648	\section{Robustness to Subgroup Misspecification}
649	\label{app:robustness}
650	
651	EC-HTE requires pre-defined subgroup labels, which may be noisy in practice.
652	We test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\text{flip}} \in \{0, 0.10, 0.25, 0.50\}$, across $K \in \{2, 4\}$ (extreme regime, $n_{\text{expert}} = 500$, $\Delta\tau = 0.3$, 100 MC runs).
653	
654	\begin{table}[t]
655	\centering
656	\caption{95\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}
657	\label{tab:robustness}
658	\small
659	\begin{tabular}{lcccc}
660	\toprule
661	& \multicolumn{4}{c}{$p_{\text{flip}}$} \\
662	\cmidrule(lr){2-5}
663	Method & 0.00 & 0.10 & 0.25 & 0.50 \\
664	\midrule
665	\multicolumn{5}{l}{\textit{$K{=}2$, extreme}} \\
666	\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\
667	\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\
668	\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\
669	\midrule
670	\multicolumn{5}{l}{\textit{$K{=}4$, extreme}} \\
671	\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\
672	\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\
673	\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\
674	\bottomrule
675	\end{tabular}
676	\end{table}
677	
678	EC-HTE maintains coverage $\geq 0.945$ across all configurations (Table~\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).
679	At $p_{\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.
680	For $K{=}4$ at $p_{\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.
681	
682	\section{Monte Carlo Standard Errors}
683	\label{app:mcse}
684	
685	All main-text and most appendix experiments use 100 independent Monte Carlo replications per configuration; computationally intensive analyses (R-learner, multiplicative DGP, budget sweeps) use 50, and bootstrap experiments use 20 due to the $B{\times}$CF cost per seed.
686	The median RMSE variation between 50-seed and 100-seed estimates is below 3.2\%, confirming that 50-run results are stable.
687	We report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.
688	For exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.
689	For exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.
690	
691	Table~\ref{tab:mcse} reports paired comparisons for representative configurations.
692	Of 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\%) are statistically significant at $\alpha = 0.05$.
693	
694	\begin{table}[t]
695	\centering
696	\caption{Paired comparisons for representative configurations. $\Delta$ = method A $-$ method B (negative favors A for $|\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\alpha = 0.05$.}
697	\label{tab:mcse}
698	\small
699	\begin{tabular}{llrr}
700	\toprule
701	Configuration & Comparison & $\Delta$ & $p$ \\
702	\midrule
703	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global ($|\text{bias}|$)}} \\
704	\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\mathbf{<0.001}$ \\
705	\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\mathbf{<0.001}$ \\
706	\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\
707	\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\
708	\midrule
709	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global (RMSE)}} \\
710	\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\
711	\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\mathbf{0.011}$ \\
712	\midrule
713	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Naive ($|\text{bias}|$)}} \\
714	\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\mathbf{<0.001}$ \\
715	\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\mathbf{<0.001}$ \\
716	\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\mathbf{0.038}$ \\
717	\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\mathbf{0.030}$ \\
718	\bottomrule
719	\end{tabular}
720	\end{table}
721	
722	Under extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).
723	The RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.
724	Under moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.
725	In the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\Delta\pi$ and unbalanced subgroup sizes.
726	The HB vs.\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.
727	
728	\section{Semi-Real Confusion Matrix Validation}
729	\label{app:semireal}
730	
731	We test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.
732	Four text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\tau(z{=}0,s) = 0.3 + 0.1s$, $\tau(z{=}1,s) = 0.8 - 0.15s$).
733	$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\text{expert}}$ level.
734	
735	\begin{table}[t]
736	\centering
737	\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.
738	S0 exhibits FNR $= 0.526$, approaching chance-level classification.}
739	\label{tab:semireal_cm}
740	\small
741	\begin{tabular}{lcccc}
742	\toprule
743	Subgroup & Weight & FPR & FNR & $\kappa(\hat{C}_s)$ \\
744	\midrule
745	S0 & 0.38 & 0.054 & 0.526 & high \\
746	S1 & 0.22 & 0.101 & 0.300 & moderate \\
747	S2 & 0.14 & 0.143 & 0.308 & moderate \\
748	S3 & 0.25 & 0.194 & 0.222 & low \\
749	\bottomrule
750	\end{tabular}
751	\end{table}
752	
753	\begin{table}[t]
754	\centering
755	\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}
756	\label{tab:semireal}
757	\small
758	\begin{tabular}{llcc}
759	\toprule
760	$n_{\text{expert}}$ & Method & RMSE $\downarrow$ & Coverage $\uparrow$ \\
761	\midrule
762	\multirow{4}{*}{100}
763	 & Oracle & 0.101 & 0.957 \\
764	 & Naive & 0.123 & 0.879 \\
765	 & Global & 0.263 & 0.885 \\
766	 & HB EC-HTE & 0.784 & 0.744 \\
767	\midrule
768	\multirow{4}{*}{250}
769	 & Oracle & 0.101 & 0.957 \\
770	 & Naive & 0.123 & 0.879 \\
771	 & Global & 0.232 & 0.909 \\
772	 & HB EC-HTE & 0.411 & 0.834 \\
773	\midrule
774	\multirow{4}{*}{500}
775	 & Oracle & 0.101 & 0.957 \\
776	 & Naive & 0.123 & 0.879 \\
777	 & Global & 0.196 & 0.922 \\
778	 & HB EC-HTE & 0.260 & 0.890 \\
779	\bottomrule
780	\end{tabular}
781	\end{table}
782	
783	HB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\ref{tab:semireal}).
784	The root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.
785	This converges with the hate speech case study (Appendix~\ref{app:hatespeech}, FNR $= 53.3$\%) and confirms that EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality per subgroup.
786	The singularity guard ($\kappa > 100$, Section~\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.
787	For a $2 \times 2$ symmetric confusion matrix, $\kappa = 1/|1-2\pi|$; $\kappa > 100$ corresponds to $\pi \in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\%$ of random guessing.
788	At $n_{\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.
789	
790	A second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\times$ at all budgets.
791	Here the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.
792	Together, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$), (2)~no near-chance subgroup error rate ($\max(\text{FPR}_s, \text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.
793	
794	\paragraph{Diagnostic rule.}
795	A logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\kappa(\hat{M}_s) \leq 1.25$ and the effective minority-class expert count $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$.
796	When both conditions hold, HB outperforms global in 93.3\% of cells; when either is violated, global is preferred in 94.7\% of cells.
797	Both exp-015 ($\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\% of their failure cells.
798	Subgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.
799	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "0a4f81e3-c4e6-4cfc-9f86-c9db7894c49a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "$s_3$ & 0.179 & 0.178 & 0.182 & \\textbf{0.159} & 0.945 \\\\\n$s_4$ & 0.221 & 0.263 & 0.343 & \\textbf{0.163} & 0.940 \\\\\n$s_5$ & 0.264 & 0.421 & 0.711 & \\textbf{0.164} & 0.965 \\\\\n$s_6$ & 0.307 & 0.634 & 1.375 & \\textbf{0.177} & 0.940 \\\\\n$s_7$ & 0.350 & 0.432 & 0.809 & \\textbf{0.183} & 0.960 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRMSE degradation is concentrated in high-$\\pi$ subgroups ($s_4$--$s_7$, $\\pi \\geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\\pi_s$ and HB RMSE).\nLow-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\\% below global correction.\nHB partial pooling reduces MLE RMSE by 24--54\\% in the high-$\\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.\nCoverage remains $\\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.\nAdaptive shrinkage---increasing the prior strength for high-$\\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.\n\nWe explored adaptive shrinkage ($\\alpha{=}10$ for high-$\\pi$ subgroups vs.\\ default $\\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\\% improvement) by attenuating estimation noise in high-$\\pi$ subgroups.\nHowever, RMSE remains 30\\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\\sim}$31 expert labels) rather than the shrinkage method itself.\nThis establishes $K{=}8$ at $n_{\\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\\geq$94\\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\\text{expert}} \\geq 500$ (${\\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.\n\n\\section{Asymmetric Misclassification Extension}\n\\label{app:asymmetric}\n\nAssumption~(A2) imposes symmetric misclassification ($\\text{FPR}_s = \\text{FNR}_s = \\pi_s$), which simplifies the bias decomposition but is not necessary for it.\nReal LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.\n\n\\paragraph{General bias formula.}\nFor asymmetric confusion matrices $C_s = \\bigl(\\begin{smallmatrix} 1{-}\\text{FPR}_s & \\text{FPR}_s \\\\ \\text{FNR}_s & 1{-}\\text{FNR}_s \\end{smallmatrix}\\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\\text{global}}^{-1} M_s - I$.\nSince both $M_s$ and $M_{\\text{global}}$ are row-stochastic, $B_s \\mathbf{1} = \\mathbf{0}$.\nDecomposing $\\boldsymbol{\\tau} = \\tau(0)\\mathbf{1} + \\Delta\\tau \\, \\mathbf{e}_1$ gives:\n\\begin{equation}\n\\text{bias}(z, s) = \\Delta\\tau \\cdot [B_s]_{z,1},\n\\end{equation}\nwhere $[B_s]_{z,1}$ depends only on $\\{\\text{FPR}_k, \\text{FNR}_k, w_k\\}$, not on $\\Delta\\tau$.\nUnder~(A2), this reduces to $\\delta_s \\Delta\\tau / (1 - 2\\bar{\\pi})$ (Theorem~\\ref{thm:bias_identity}).\n\n\\paragraph{Empirical validation.}\nWe test three asymmetric configurations ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs each): \\emph{Cross} (FPR/FNR = 0.10/0.20 vs.\\ 0.25/0.10), \\emph{Co-directional} (0.05/0.15 vs.\\ 0.20/0.30), and \\emph{Extreme} (0.03/0.25 vs.\\ 0.30/0.05).\nRegressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.\nTable~\\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\\Delta\\tau \\in \\{0.1, \\ldots, 0.5\\}$.\nEC-HTE reduces $|\\text{bias}|$ from 0.025 (global) to 0.006, a $4\\times$ improvement, with lower RMSE (0.033 vs.\\ 0.040) and substantially better coverage (0.90 vs.\\ 0.78).\n\n\\begin{table}[t]\n\\centering\n\\caption{Asymmetric misclassification results ($K{=}2$, $n_{\\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\\Delta\\tau$.}\n\\label{tab:asymmetric}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & $|\\text{Bias}| \\downarrow$ & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\nNaive & 0.047 & 0.053 & 0.48 \\\\\nGlobal & 0.025 & 0.040 & 0.78 \\\\\nHB EC-HTE & \\textbf{0.006} & \\textbf{0.033} & \\textbf{0.90} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Supplementary Main Results}\n\\label{app:main_supp}\n\n\\begin{table}[t]\n\\centering\n\\caption{Additional configurations from the main experiment. $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\\dagger$RMSE exceeds Global.}\n\\label{tab:main_supp}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nConfiguration & Method & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Synthetic DIM\\\\$K{=}2$, moderate, $n{=}250$}}\n & Naive & 0.018 & 0.064 & 0.95 \\\\\n & Global & 0.009 & 0.074 & 0.96 \\\\\n & Strat.\\ MLE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n & HB EC-HTE & \\textbf{0.005} & 0.075$^\\dagger$ & 0.97 \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Semi-synthetic\\\\TweetEval, extreme, $n{=}250$}}\n & Naive & 0.027 & 0.103 & 0.93 \\\\\n & Global & \\textbf{0.023} & 0.124 & 0.92 \\\\\n & Strat.\\ MLE & 0.032 & 0.248$^\\dagger$ & 0.91 \\\\\n & HB EC-HTE & 0.027 & 0.225$^\\dagger$ & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{PPCI Complementarity Results}\n\\label{app:ppci}\n\\label{sec:ppci}\n\nEC-HTE composes with PPCI~\\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\\%; Appendix~\\ref{app:rlearner}).\n\n\\begin{table*}[t]\n\\centering\n\\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\\sigma{=}0.5$); C: both errors; D: no error. Values are $|\\text{bias}|$ and RMSE averaged over two subgroups. $^\\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}\n\\label{tab:ppci}\n\\small\n\\begin{tabular}{ll cccc}\n\\toprule\nDGP & Method & $|\\text{Bias}|_{z=0}$ & $|\\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\\\\n\\midrule\n\\multirow{5}{*}{A: Covariate}\n & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\\\\n & Global & 0.063 & 0.055 & 0.101 & 0.102 \\\\\n & EC-HTE & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n & PPCI & \\textbf{0.015} & 0.020 & 0.162 & 0.168 \\\\\n & EC-HTE+PPCI & 0.017 & \\textbf{0.013} & 0.097 & 0.108 \\\\\n\\midrule\n\\multirow{5}{*}{B: Outcome}\n & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\\\\n & Global & 0.185 & 0.208 & 0.204 & 0.228 \\\\\n & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\\\\n & PPCI & 0.015 & \\textbf{0.020} & 0.171 & 0.176 \\\\\n & EC-HTE+PPCI & \\textbf{0.012} & 0.023 & 0.171 & 0.186 \\\\\n\\midrule\n\\multirow{5}{*}{C: Both}\n & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\\\\n & Global & 0.182 & 0.209 & 0.233 & 0.235 \\\\\n & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\\\\n & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\\\\n & EC-HTE+PPCI$^\\star$ & \\textbf{0.007} & \\textbf{0.008} & 0.209 & 0.223 \\\\\n\\midrule\n\\multirow{5}{*}{D: None}\n & Naive & \\textbf{0.007} & 0.003 & 0.060 & 0.065 \\\\\n & Global & 0.010 & \\textbf{0.002} & 0.061 & 0.071 \\\\\n & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n & PPCI & \\textbf{0.007} & \\textbf{0.003} & 0.060 & 0.065 \\\\\n & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).\nSince covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.\nUnder covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.\n\n\\section{Real-Data Case Study: Hate Speech Detection}\n\\label{app:hatespeech}\n\nWe apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.\nFour text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \\approx 624$ each).\n\n\\paragraph{Positive finding: real-world heterogeneity.}\nPer-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\\Delta\\pi = 0.117$) in a real annotation setting.\nAt the error-type level, FPR ranges from 8.5\\% to 21.3\\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.\n\n\\paragraph{Boundary condition: statistical power at extreme FNR.}\nCorrection results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.\nThe high baseline FNR (53.3\\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\\times$), rendering the comparison underpowered.\nWhen $P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.\nThis complements the expert budget threshold identified in Appendix~\\ref{sec:budget}: EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality.\n\n\\paragraph{Diagnostic connection.}\nThe diagnostic criterion ($\\Delta\\pi \\times \\Delta\\tau$, Section~\\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.\nThis case study illustrates that even when $\\Delta\\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.\nA practical prerequisite is that the per-subgroup confusion matrix condition number $\\kappa(\\hat{C}_s)$ remain moderate; when $\\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.\n\n\\section{Cross-Model Consistency}\n\\label{app:multilm}\n\nWe evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.\nSix text-feature subgroups are defined by crossing hashtag presence and text length.\nSpearman rank correlations of per-subgroup error rates across all six subgroups range from $\\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.\nTwo subgroups with $n \\leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%\n\\footnote{The filtered $\\Delta\\pi$ values in Table~\\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\\Delta\\pi > 0.05$ on the four retained subgroups.}\n\n\\begin{table}[t]\n\\centering\n\\caption{Effective misclassification heterogeneity ($\\Delta\\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \\geq 10$).}\n\\label{tab:multilm}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nModel & Effective $\\Delta\\pi$ & $> 0.05$? \\\\\n\\midrule\nGPT-3.5-Turbo & 0.198 & \\checkmark \\\\\nGPT-4-Turbo & 0.149 & \\checkmark \\\\\nGPT-4o-mini & 0.136 & \\checkmark \\\\\nGPT-5.4 & 0.114 & \\checkmark \\\\\nGPT-4.1 & 0.098 & \\checkmark \\\\\nGPT-4o & 0.080 & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll six models exhibit effective $\\Delta\\pi > 0.05$ on the four retained subgroups (Table~\\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\\texttt{True\\_medium}: tweets with hashtags and medium text length).\nNewer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\\Delta\\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.\nThese results were obtained with a single API provider; open-source model validation appears in Appendix~\\ref{app:multilm_opensource}.\n\n\\section{Open-Source Multi-LLM Validation}\n\\label{app:multilm_opensource}\n\nWe evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.\nTable~\\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.\nAll four models exhibit $\\Delta\\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.\nSubgroup error rankings are consistent across architectures: \\texttt{True\\_short} (short tweets with hashtags) has the lowest $\\pi_s$ in 3 of 4 models, while \\texttt{False\\_medium} (medium tweets without hashtags) has the highest.\n\n\\begin{table}[t]\n\\centering\n\\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\\Delta\\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\\Delta\\tau$-free diagnostic (Proposition~\\ref{prop:debiasing_hurts}) triggers.}\n\\label{tab:multilm_cm}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nModel & Acc.\\ & $\\Delta\\pi$ & Prop2 & Strongest \\\\\n\\midrule\nLlama-3.1-8B & 0.755 & 0.141 & 1/4 & True\\_short \\\\\nQwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\\_short \\\\\nGemma-2-9B & 0.763 & 0.125 & 4/4 & True\\_medium \\\\\nMistral-7B & 0.802 & 0.134 & 0/4 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Semi-synthetic budget sweep.}\nWe run the full EC-HTE pipeline with $K{=}2$ subgroups and $\\Delta\\tau{=}0.3$, using each model's empirical confusion matrices.\nTable~\\ref{tab:multilm_budget} reports coverage and RMSE crossover points.\nEC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\\text{expert}}{=}1{,}000$, consistent across all four models.\nGlobal correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\\Delta\\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic budget sweep ($K{=}2$, $\\Delta\\tau{=}0.3$, 50 MC runs; see Appendix~\\ref{app:mcse} for MC tier justification). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}\n\\label{tab:multilm_budget}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nModel & $\\Delta\\pi_{K{=}2}$ & Naive Cov.\\ & HB Cov.\\ ($n{=}1000$) & Crossover \\\\\n\\midrule\nLlama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\\\\nQwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\\\\nGemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\\\\nMistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\\\\n\\midrule\n\\textit{Average} & --- & \\textit{0.714} & \\textit{0.939} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gemma boundary case.}\nGemma-2-9B triggers the Proposition~\\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\\texttt{False\\_medium} FNR $= 0.437$).\nAt small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\\times$ naive), illustrating the budget guideline from Appendix~\\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.\nAt $n \\geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.\n\n\\paragraph{Heterogeneous-$\\tau$ DGP.}\nTo assess whether the constant-$\\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\\Delta\\tau \\in [0.1, 0.6]$, $K{=}2$, 50 MC runs).\nEC-HTE achieves lower $|\\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\\ 0.031, a 68\\% reduction).\nIn the high-$\\Delta\\tau$ subgroup (\\texttt{True\\_short}, $\\Delta\\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\\ 0.258, 18\\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.\nAggregate RMSE remains comparable to global correction because low-$\\Delta\\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\\ref{sec:budget}.\n\n\\section{Robustness to Subgroup Misspecification}\n\\label{app:robustness}\n\nEC-HTE requires pre-defined subgroup labels, which may be noisy in practice.\nWe test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\\text{flip}} \\in \\{0, 0.10, 0.25, 0.50\\}$, across $K \\in \\{2, 4\\}$ (extreme regime, $n_{\\text{expert}} = 500$, $\\Delta\\tau = 0.3$, 100 MC runs).\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}\n\\label{tab:robustness}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{4}{c}{$p_{\\text{flip}}$} \\\\\n\\cmidrule(lr){2-5}\nMethod & 0.00 & 0.10 & 0.25 & 0.50 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}2$, extreme}} \\\\\n\\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\\\\n\\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\\\\n\\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$K{=}4$, extreme}} \\\\\n\\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\\\\n\\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\\\\n\\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq 0.945$ across all configurations (Table~\\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).\nAt $p_{\\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.\nFor $K{=}4$ at $p_{\\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.\n\n\\section{Monte Carlo Standard Errors}\n\\label{app:mcse}\n\nAll main-text and most appendix experiments use 100 independent Monte Carlo replications per configuration; computationally intensive analyses (R-learner, multiplicative DGP, budget sweeps) use 50, and bootstrap experiments use 20 due to the $B{\\times}$CF cost per seed.\nThe median RMSE variation between 50-seed and 100-seed estimates is below 3.2\\%, confirming that 50-run results are stable.\nWe report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.\nFor exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.\nFor exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.\n\nTable~\\ref{tab:mcse} reports paired comparisons for representative configurations.\nOf 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\\%) are statistically significant at $\\alpha = 0.05$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paired comparisons for representative configurations. $\\Delta$ = method A $-$ method B (negative favors A for $|\\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\\alpha = 0.05$.}\n\\label{tab:mcse}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nConfiguration & Comparison & $\\Delta$ & $p$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Global (RMSE)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\\mathbf{0.011}$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{HB EC-HTE vs.\\ Naive ($|\\text{bias}|$)}} \\\\\n\\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\\mathbf{<0.001}$ \\\\\n\\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\\mathbf{0.038}$ \\\\\n\\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\\mathbf{0.030}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).\nThe RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.\nUnder moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.\nIn the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\\Delta\\pi$ and unbalanced subgroup sizes.\nThe HB vs.\\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.\n\n\\section{Semi-Real Confusion Matrix Validation}\n\\label{app:semireal}\n\nWe test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.\nFour text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\\tau(z{=}0,s) = 0.3 + 0.1s$, $\\tau(z{=}1,s) = 0.8 - 0.15s$).\n$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\\text{expert}}$ level.\n\n\\begin{table}[t]\n\\centering\n\\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.\nS0 exhibits FNR $= 0.526$, approaching chance-level classification.}\n\\label{tab:semireal_cm}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSubgroup & Weight & FPR & FNR & $\\kappa(\\hat{C}_s)$ \\\\\n\\midrule\nS0 & 0.38 & 0.054 & 0.526 & high \\\\\nS1 & 0.22 & 0.101 & 0.300 & moderate \\\\\nS2 & 0.14 & 0.143 & 0.308 & moderate \\\\\nS3 & 0.25 & 0.194 & 0.222 & low \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}\n\\label{tab:semireal}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n$n_{\\text{expert}}$ & Method & RMSE $\\downarrow$ & Coverage $\\uparrow$ \\\\\n\\midrule\n\\multirow{4}{*}{100}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.263 & 0.885 \\\\\n & HB EC-HTE & 0.784 & 0.744 \\\\\n\\midrule\n\\multirow{4}{*}{250}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.232 & 0.909 \\\\\n & HB EC-HTE & 0.411 & 0.834 \\\\\n\\midrule\n\\multirow{4}{*}{500}\n & Oracle & 0.101 & 0.957 \\\\\n & Naive & 0.123 & 0.879 \\\\\n & Global & 0.196 & 0.922 \\\\\n & HB EC-HTE & 0.260 & 0.890 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\\ref{tab:semireal}).\nThe root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\\hat{Z}{=}1 \\mid Z{=}1) \\approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.\nThis converges with the hate speech case study (Appendix~\\ref{app:hatespeech}, FNR $= 53.3$\\%) and confirms that EC-HTE requires \\emph{both} sufficient expert labels \\emph{and} sufficient baseline classifier quality per subgroup.\nThe singularity guard ($\\kappa > 100$, Section~\\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.\nFor a $2 \\times 2$ symmetric confusion matrix, $\\kappa = 1/|1-2\\pi|$; $\\kappa > 100$ corresponds to $\\pi \\in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\\%$ of random guessing.\nAt $n_{\\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.\n\nA second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\\times$ at all budgets.\nHere the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.\nTogether, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$), (2)~no near-chance subgroup error rate ($\\max(\\text{FPR}_s, \\text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.\n\n\\paragraph{Diagnostic rule.}\nA logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\\kappa(\\hat{M}_s) \\leq 1.25$ and the effective minority-class expert count $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$.\nWhen both conditions hold, HB outperforms global in 93.3\\% of cells; when either is violated, global is preferred in 94.7\\% of cells.\nBoth exp-015 ($\\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\\% of their failure cells.\nSubgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.\n",
      "numLines": 400,
      "startLine": 400,
      "totalLines": 1538
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_0183aG3YZb4z4APLhDZ6dHPw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 800,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "e71a1289-83d1-4994-b54f-11592896eb6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjQrtrcU6xrQTDd17FDZwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15903,
      "cache_read_input_tokens": 26426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15903
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

_source line 37 · 2026-05-24T04:29:29.306Z_

<details><summary>↩ Tool result · `toolu_0183aG3YZb4z4APLhDZ6dHPw`</summary>

```text
800	\begin{figure}[t]
801	\centering
802	\includegraphics[width=\columnwidth]{figures/applicability_frontier.pdf}
803	\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}
804	\label{fig:applicability}
805	\end{figure}
806	
807	\section{Robustness: Estimator Choice and Treatment Effect Specification}
808	\label{app:rlearner}
809	
810	We verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\citep{nie2021quasi}.
811	The experiment uses $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.
812	
813	\begin{table}[t]
814	\centering
815	\caption{R-learner vs.\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}
816	\label{tab:rlearner}
817	\small
818	\begin{tabular}{llccc}
819	\toprule
820	Estimator & Correction & $|\text{Bias}|$ & RMSE & Cov. \\
821	\midrule
822	\multirow{4}{*}{R-learner}
823	 & Oracle & 0.006 & 0.056 & 0.94 \\
824	 & Naive & 0.121 & 0.139 & 0.47 \\
825	 & Global & 0.098 & 0.123 & 0.72 \\
826	 & EC-HTE & \textbf{0.013} & 0.080 & 0.92 \\
827	\midrule
828	\multirow{2}{*}{CausalForest}
829	 & Naive & 0.058 & 0.090 & 0.82 \\
830	 & EC-HTE & \textbf{0.010} & 0.093 & 0.95 \\
831	\bottomrule
832	\end{tabular}
833	\end{table}
834	
835	EC-HTE reduces R-learner $|\text{bias}|$ by 89\% (0.121 $\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\ref{tab:rlearner}).
836	The bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.
837	
838	\paragraph{Multiplicative treatment effects.}
839	We further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \times \exp(\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds.
840	
841	\begin{table}[t]
842	\centering
843	\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}
844	\label{tab:multiplicative}
845	\small
846	\begin{tabular}{lccc}
847	\toprule
848	Method & $|\text{Bias}|$ & RMSE & Cov. \\
849	\midrule
850	Oracle & 0.003 & 0.038 & 0.96 \\
851	Naive & 0.135 & 0.142 & 0.44 \\
852	Global & 0.110 & 0.124 & 0.54 \\
853	EC-HTE & \textbf{0.054} & 0.068 & 0.955 \\
854	\bottomrule
855	\end{tabular}
856	\end{table}
857	
858	EC-HTE reduces RMSE by 52\% relative to naive (0.068 vs.\ 0.142) and restores coverage to the nominal level (0.955; Table~\ref{tab:multiplicative}).
859	EC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.
860	
861	\section{Robustness to Class Imbalance}
862	\label{app:classimbalance}
863	
864	Assumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.
865	We sweep $P(Z{=}1) \in \{0.1, 0.2, 0.3, 0.4, 0.5\}$ with $K \in \{2,4\}$, extreme misclassification heterogeneity, $n_{\text{expert}}{=}250$, and 100 MC seeds (Table~\ref{tab:pz1_sweep}).
866	
867	\begin{table}[t]
868	\centering
869	\caption{Robustness to class imbalance ($n_{\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\% CI coverage.}
870	\label{tab:pz1_sweep}
871	\small
872	\begin{tabular}{cc ccc}
873	\toprule
874	$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\
875	\midrule
876	0.1 & 2 & 0.998 & 0.92 & 0.94 \\
877	0.2 & 2 & 0.989 & 0.76 & 0.94 \\
878	0.3 & 2 & 0.994 & 0.78 & 0.94 \\
879	0.4 & 2 & 0.995 & 0.87 & 0.94 \\
880	0.5 & 2 & 0.995 & 0.86 & 0.93 \\
881	\midrule
882	0.1 & 4 & 0.984 & 1.54 & 0.92 \\
883	0.2 & 4 & 0.976 & 1.68 & 0.93 \\
884	0.3 & 4 & 0.985 & 1.12 & 0.92 \\
885	0.4 & 4 & 0.984 & 1.08 & 0.93 \\
886	0.5 & 4 & 0.992 & 1.06 & 0.92 \\
887	\bottomrule
888	\end{tabular}
889	\end{table}
890	
891	Theorem~\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.
892	For $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.
893	For $K{=}4$, EC-HTE underperforms global at $n_{\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\sim}6$ minority-class labels.
894	The gap narrows as $P(Z{=}1)$ increases (1.54 $\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.
895	
896	\section{Comparison with PPI Correction}
897	\label{app:ppi_comparison}
898	
899	PPI~\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.
900	Applied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.
901	Two variants arise naturally: \emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).
902	
903	Under the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.
904	Pooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.
905	EC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.
906	This mechanism is outside both the PPI and DSL frameworks.
907	
908	The key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.
909	This avoids the matrix inversion step that can amplify noise at small $n_{\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.
910	PPI-global inherits the same $\Delta\pi \times \Delta\tau$ bias amplification as Global correction (Theorem~\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.
911	
912	\section{Civil Comments Validation}
913	\label{app:civilcomments}
914	
915	To verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\% toxic) from Civil Comments~\cite{borkan2019nuanced}, a toxicity detection dataset.
916	Subgroups are defined by \texttt{text\_length\_bin} $\times$ \texttt{has\_question} ($K{=}4$): S0 (long, no question, 38.8\%), S1 (long, question, 11.4\%), S2 (short, no question, 33.7\%), S3 (short, question, 16.1\%).
917	Subgroup features were chosen a priori based on observable text properties; no feature search was performed.
918	Three proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.
919	
920	Table~\ref{tab:civil_cm} reports per-subgroup FPR and FNR.
921	We define $\Delta\pi = \max_s \pi_s - \min_s \pi_s$, where $\pi_s$ is the overall misclassification rate for subgroup $s$.
922	All three models exhibit $\Delta\pi > 0.05$, with overall heterogeneity $\Delta\pi \in [0.113, 0.160]$---comparable to the $\Delta\pi \in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\ref{app:multilm_opensource}).
923	GPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\in [0.42, 0.61]$ vs.\ FNR $\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).
924	The consistent presence of $\Delta\pi$ heterogeneity across two NLP tasks, eight LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.
925	
926	\begin{table}[h]
927	\centering
928	\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\Delta$ denotes max $-$ min across subgroups.}
929	\label{tab:civil_cm}
930	\small
931	\begin{tabular}{llccccc}
932	\toprule
933	Model & Metric & S0 & S1 & S2 & S3 & $\Delta$ \\
934	\midrule
935	GPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\
936	       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\
937	\midrule
938	GPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\
939	            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\
940	\midrule
941	GPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\
942	              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\
943	\bottomrule
944	\end{tabular}
945	\end{table}
946	
947	\section{Bias Identity Validation with Real Confusion Matrices}
948	\label{app:realcm_bias}
949	
950	Theorem~\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\neq$ FNR).
951	We verify that the generalized identity $\mathrm{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}$ (Remark~\ref{thm:bias_identity}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\Delta\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).
952	
953	Table~\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\Delta\tau \cdot [B_s]_{z,1}$.
954	The aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \geq 0.92$.
955	The single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.
956	$R^2$ correlates strongly with $\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.
957	
958	\begin{table}[h]
959	\centering
960	\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}
961	\label{tab:realcm_r2}
962	\small
963	\begin{tabular}{llcc}
964	\toprule
965	Model & Dataset & $R^2$ & $\max|[B_s]_{z,1}|$ \\
966	\midrule
967	GPT-4-turbo  & TweetEval & 0.993 & 0.328 \\
968	Qwen2.5-7B   & TweetEval & 0.990 & 0.272 \\
969	Mistral-7B   & TweetEval & 0.990 & 0.242 \\
970	Gemma-2-9B   & TweetEval & 0.982 & 0.185 \\
971	GPT-4o       & Civil Comments & 0.979 & 0.198 \\
972	GPT-4o       & TweetEval & 0.975 & 0.240 \\
973	GPT-4.1      & TweetEval & 0.969 & 0.139 \\
974	GPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\
975	GPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\
976	GPT-4o-mini  & TweetEval & 0.929 & 0.170 \\
977	GPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\
978	\midrule
979	\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\
980	\bottomrule
981	\end{tabular}
982	\end{table}
983	
984	\section{Applicability Screening with Real LLM Confusion Matrices}
985	\label{app:screening}
986	
987	We apply the diagnostic conditions from Proposition~\ref{prop:debiasing_hurts} and Section~\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning eight LLMs (three open-source, five proprietary) across TweetEval and Civil Comments.
988	Table~\ref{tab:screening} summarizes which conditions each combination satisfies.
989	
990	\begin{table}[h]
991	\centering
992	\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\text{expert}}{=}500$.}
993	\label{tab:screening}
994	\small
995	\begin{tabular}{llccccc}
996	\toprule
997	Model & Dataset & $K$ & $\kappa{\leq}1.25$ & $\max{\leq}0.5$ & Budget & Pass all \\
998	\midrule
999	Gemma-2-9B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1000	Llama-3.1-8B & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1001	Mistral-7B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1002	Qwen2.5-7B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1003	Gemma-2-9B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1004	Llama-3.1-8B & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1005	Mistral-7B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1006	Qwen2.5-7B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1007	GPT-3.5-turbo & CivilComm. & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1008	GPT-3.5-turbo & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1009	GPT-4-turbo  & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1010	GPT-4.1      & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1011	GPT-4o       & CivilComm. & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1012	GPT-4o       & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1013	GPT-4o-mini  & CivilComm. & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1014	GPT-4o-mini  & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1015	\bottomrule
1016	\end{tabular}
1017	\end{table}
1018	
1019	No combination passes all three conditions; the bottleneck is $\kappa(C_s) \leq 1.25$, which requires $\mathrm{FPR}_s + \mathrm{FNR}_s \lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.
1020	The closest are Qwen2.5-7B True\_short ($\kappa{=}1.23$) and Mistral-7B True\_short ($\kappa{=}1.27$).
1021	
1022	Under a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\max(\mathrm{FPR}_s, \mathrm{FNR}_s) \geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\Delta\tau{=}0.3$, 100 MC runs, $n_{\text{expert}} \in \{250, 500\}$) with each LLM's real per-subgroup confusion matrix.
1023	EC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\%).
1024	The four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\mathrm{FPR}_{\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.
1025	The diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\% of comparisons.
1026	
1027	\paragraph{Diagnostic Applicability Analysis.}
1028	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\tau_s \approx 0$ are hurt by global correction (since $\delta_s \neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.
1029	
1030	A simple meta-criterion recovers reliability: compute $\max_s |\delta_s| / ((1 - 2\bar{\pi}) \cdot \pi_s)$ across subgroups.
1031	When $\max_s \mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).
1032	When $\max_s \mathrm{score}(s) \leq 1$, global correction may or may not hurt depending on unobservable $\Delta\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).
1033	This threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.
1034	
1035	We recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\max_s \mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.
1036	
1037	\subsection{$\kappa$ Stratification Analysis}
1038	\label{app:kappa_analysis}
1039	
1040	The condition number $\kappa(\hat{C}_s) = 1/|1 - \mathrm{FPR}_s - \mathrm{FNR}_s|$ quantifies confusion matrix invertibility and governs the bias-variance tradeoff of per-subgroup correction.
1041	The $\kappa \leq 1.25$ threshold identified in the diagnostic rule (Section~\ref{sec:budget}) is a \emph{sufficient condition} for strongest bias reduction, not a necessary condition: EC-HTE maintains calibrated inference across a substantially wider $\kappa$ range.
1042	
1043	\paragraph{Synthetic data.}
1044	Across all 520 synthetic configurations ($K{=}2$, $\pi_s \in [0.025, 0.275]$), the maximum per-config $\kappa$ falls in $[1.43, 2.22]$; none reaches $\kappa \leq 1.25$ because the pooled rate $\bar{\pi}{=}0.15$ sets a floor of $\kappa{=}1/(1{-}2 \cdot 0.15){=}1.43$.
1045	Table~\ref{tab:kappa_synth} shows a two-bin stratification at $\kappa{=}2$: EC-HTE achieves zero analytic bias in both bins, while global correction harms at least one subgroup in 100\% of $\kappa > 2$ configurations.
1046	Monte Carlo validation ($K{=}2$, $n_{\text{expert}}{=}500$) confirms EC-HTE dominance at $\kappa{=}2.0$: 86\% bias reduction, 10\% lower RMSE, and 95.5\% coverage vs.\ 88.3\% for Global.
1047	
1048	\begin{table}[h]
1049	\centering
1050	\caption{Synthetic $\kappa$ stratification ($K{=}2$, 520 configs). ``Debiasing hurts'' = global correction increases $|\text{bias}|$ for $\geq$1 subgroup.}
1051	\label{tab:kappa_synth}
1052	\small
1053	\begin{tabular}{lcccc}
1054	\toprule
1055	$\kappa$ bin & $n$ & EC-HTE bias & Debiasing hurts & Global $|\text{bias}|/|\text{bias}_{\text{naive}}|$ \\
1056	\midrule
1057	$\leq 2.0$ & 420 & 0 (exact) & 35.0\% & 0.152 \\
1058	$> 2.0$    & 100 & 0 (exact) & 100\% & 0.326 \\
1059	\bottomrule
1060	\end{tabular}
1061	\end{table}
1062	
1063	\paragraph{Real LLM confusion matrices.}
1064	All 13 real LLM--dataset combinations ($K{=}4$) have $\kappa \in [1.88, 2.99]$---none reaches $\kappa \leq 1.25$, because no current LLM achieves $\mathrm{FPR}_s + \mathrm{FNR}_s < 0.20$ uniformly across subgroups.
1065	Table~\ref{tab:kappa_real} reports performance stratified by $\kappa$ bin and expert budget.
1066	The key finding is that EC-HTE maintains calibrated coverage ($\geq$93\%) across all $\kappa$ bins at $n_{\text{expert}} \geq 250$, compared to 86--91\% for Global.
1067	At $n_{\text{expert}}{=}500$, EC-HTE also achieves competitive RMSE in the $\kappa \leq 2$ bin (ratio 1.01) and bias win rate of 75\%; at $n_{\text{expert}}{=}250$, the variance cost of per-subgroup estimation dominates, and Global achieves lower RMSE---consistent with the bias-variance tradeoff documented in the main text (Section~\ref{sec:ec_hte_eval}).
1068	
1069	\begin{table}[h]
1070	\centering
1071	\caption{Real LLM $\kappa$ stratification ($K{=}4$, MC validation). Ratios = EC-HTE / Global; values $<1$ favor EC-HTE. Coverage is EC-HTE absolute; Global coverage ranges 0.86--0.91 across bins.}
1072	\label{tab:kappa_real}
1073	\small
1074	\begin{tabular}{llcccc}
1075	\toprule
1076	$\kappa$ bin & $n_{\text{expert}}$ & Bias ratio & RMSE ratio & Bias win & Cov.\ (EC-HTE) \\
1077	\midrule
1078	\multirow{2}{*}{$\leq 2.0$ ($n{=}4$)}
1079	 & 500 & 0.99 & 1.01 & 75\% & 0.943 \\
1080	 & 250 & 1.09 & 1.13 & 0\%  & 0.932 \\
1081	\midrule
1082	\multirow{2}{*}{$> 2.0$ ($n{=}9$)}
1083	 & 500 & 1.11 & 1.22 & 22\% & 0.949 \\
1084	 & 250 & 1.26 & 1.43 & 0\%  & 0.940 \\
1085	\bottomrule
1086	\end{tabular}
1087	\end{table}
1088	
1089	The three-tier $\kappa$ structure is thus: (i)~$\kappa > 100$: near-random classification, singularity guard triggers automatic fallback to global correction; (ii)~$\kappa \leq 1.25$: strongest theoretical regime with guaranteed bias reduction and coverage; (iii)~$\kappa \in (1.25, {\sim}3]$: the practical operating range for current LLMs, where EC-HTE provides calibrated inference (coverage $\geq$93\%) and achieves RMSE gains when expert budget is sufficient ($n_{\text{expert}} \geq 500$).
1090	
1091	\section{Plug-in Standard Error Validation}
1092	\label{app:bootstrap_se}
1093	
1094	A natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.
1095	We verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\text{expert}} \in \{50, 100, 250, 500\}$, 50 replications per budget level).
1096	At each budget, we compute the plug-in 95\% confidence interval and record empirical coverage.
1097	Across all expert budgets, the plug-in SE yields coverage $\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.
1098	This self-calibration arises because the same noise in $\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.
1099	
1100	\paragraph{CausalForestDML.}
1101	Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$, $n_{\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\% aggregate coverage---close to the 94--96\% oracle coverage (Table~\ref{tab:cf_oracle}).
1102	The high-error subgroup ($s_1$, $\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\%) than the low-error subgroup ($s_0$: 95.0\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.
1103	By contrast, the DIM plug-in SE achieves $\geq$95\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.
1104	
1105	\paragraph{Full bootstrap SE.}
1106	A \emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.
1107	Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$), plug-in SE achieves 93.8\% aggregate coverage; the full bootstrap improves this to exactly 95.0\% ($+$1.2pp).
1108	Table~\ref{tab:bootstrap_se} reports per-subgroup results.
1109	
1110	\begin{table}[h]
1111	\centering
1112	\caption{CausalForest coverage: plug-in SE vs.\ full bootstrap SE ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\sim}1.15\times$ plug-in.}
1113	\label{tab:bootstrap_se}
1114	\small
1115	\begin{tabular}{lccccc}
1116	\toprule
1117	Subgroup & Plugin Cov. & Boot.\ Cov. & Oracle Cov. & Plugin SE & Boot.\ SE \\
1118	\midrule
1119	$s_0$ ($\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\
1120	$s_1$ ($\pi{=}0.25$) & 0.925 & \textbf{0.975} & 0.875 & 0.087 & 0.103 \\
1121	\midrule
1122	Aggregate & 0.938 & \textbf{0.950} & 0.900 & 0.073 & 0.083 \\
1123	\bottomrule
1124	\end{tabular}
1125	\end{table}
1126	
1127	The high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\% to 97.5\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.
1128	Oracle coverage (90.0\%) is consistent with the 94\% reported in the oracle decomposition (Table~\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.
1129	The computational cost is substantial ($B \times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.
1130	
1131	\paragraph{Bootstrap coverage across expert budgets.}
1132	Table~\ref{tab:bootstrap_small_n} extends the analysis to $n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$ using the DIM estimator with Centered EB confusion matrix estimation ($K{=}2$ extreme, $\pi{=}[0.05, 0.25]$, 20 MC runs, $B{=}100$).
1133	Bootstrap SE maintains $\geq$95\% coverage across all expert budgets, including $n_{\text{expert}}{=}25$ (${\approx}12$ labels per subgroup).
1134	Plug-in SE is already near-nominal ($\geq$91.2\%) at all budgets tested.
1135	
1136	\begin{table}[h]
1137	\centering
1138	\caption{HB EC-HTE coverage across expert budgets: plug-in vs.\ bootstrap SE (DIM, $K{=}2$ extreme, 20 MC, $B{=}100$).}
1139	\label{tab:bootstrap_small_n}
1140	\small
1141	\begin{tabular}{lcccc}
1142	\toprule
1143	$n_{\text{expert}}$ & Plugin Cov. & Boot.\ Cov. & SE Ratio & $|\text{Bias}|$ \\
1144	\midrule
1145	25 & 0.925 & \textbf{1.000} & 2.86 & 0.079 \\
1146	50 & 0.975 & 0.988 & 2.93 & 0.067 \\
1147	75 & 0.912 & \textbf{0.975} & 2.59 & 0.065 \\
1148	100 & 0.963 & 0.963 & 1.52 & 0.060 \\
1149	200 & 0.963 & 0.950 & 1.17 & 0.061 \\
1150	\bottomrule
1151	\end{tabular}
1152	\end{table}
1153	
1154	At small $n_{\text{expert}}$, bootstrap SE inflates confidence intervals by $2{-}3\times$ relative to plug-in (SE ratio column), guaranteeing nominal coverage but reducing statistical power.
1155	At $n_{\text{expert}} \geq 100$, the SE ratio converges to ${\sim}1.2{-}1.5\times$, and plug-in SE alone achieves $\geq$96\% coverage.
1156	For practical deployment, we recommend $n_{\text{expert}} \geq 50$: bootstrap maintains nominal coverage (98.8\%) with moderate SE inflation (2.9$\times$), and plug-in SE achieves 97.5\%---close to nominal without bootstrap overhead.
1157	
1158	\paragraph{Finite-sample remainder.}
1159	By first-order matrix perturbation, $\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\|E_s\|^2)$, where $E_s = \hat{C}_s - C_s$ satisfies $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$.
1160	The remainder in the corrected CATE is therefore $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \|C_s^{-1}\|^2) = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, since $\|C_s^{-1}\| = O(\kappa(C_s))$ for stochastic matrices.
1161	This motivates the $\kappa > 100$ singularity guard (Section~\ref{sec:method}).
1162	
1163	\subsection{CausalForest Oracle Coverage Decomposition}
1164	\label{app:cf_oracle}
1165	
1166	To isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\hat{C}_s$ (HB), (4)~Global with true $\bar{C}$, (5)~Global with estimated $\hat{\bar{C}}$, and (6)~Naive.
1167	Table~\ref{tab:cf_oracle} reports coverage, $|\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).
1168	
1169	\begin{table}[h]
1170	\centering
1171	\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}
1172	\label{tab:cf_oracle}
1173	\small
1174	\begin{tabular}{ll ccc}
1175	\toprule
1176	DGP & Method & Cov.\ (\%) & $|\text{Bias}|$ & RMSE \\
1177	\midrule
1178	\multirow{6}{*}{\shortstack[l]{$K{=}4$, extreme\\$n{=}500$}}
1179	 & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\
1180	 & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\
1181	 & EC-HTE est.\ $\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\
1182	 & Global true $\bar{C}$   & 91.3 & 0.037 & 0.110 \\
1183	 & Global est.\ $\hat{\bar{C}}$ & 91.1 & 0.038 & 0.111 \\
1184	 & Naive                    & 88.3 & 0.045 & 0.095 \\
1185	\midrule
1186	\multirow{6}{*}{\shortstack[l]{$K{=}2$, extreme\\$n{=}250$}}
1187	 & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\
1188	 & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\
1189	 & EC-HTE est.\ $\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\
1190	 & Global true $\bar{C}$   & 88.5 & 0.045 & 0.083 \\
1191	 & Global est.\ $\hat{\bar{C}}$ & 88.3 & 0.045 & 0.085 \\
1192	 & Naive                    & 82.8 & 0.046 & 0.077 \\
1193	\midrule
1194	\multirow{6}{*}{\shortstack[l]{$K{=}2$, MF2 DGP\\$\tau{=}(0.10,0.40)$}}
1195	 & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\
1196	 & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\
1197	 & EC-HTE est.\ $\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\
1198	 & Global true $\bar{C}$   & 95.0 & 0.107 & 0.114 \\
1199	 & Global est.\ $\hat{\bar{C}}$ & 94.3 & 0.105 & 0.114 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "d67909f9-1786-478f-8aa6-9e5071556c65",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/applicability_frontier.pdf}\n\\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}\n\\label{fig:applicability}\n\\end{figure}\n\n\\section{Robustness: Estimator Choice and Treatment Effect Specification}\n\\label{app:rlearner}\n\nWe verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\\citep{nie2021quasi}.\nThe experiment uses $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.\n\n\\begin{table}[t]\n\\centering\n\\caption{R-learner vs.\\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}\n\\label{tab:rlearner}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nEstimator & Correction & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\n\\multirow{4}{*}{R-learner}\n & Oracle & 0.006 & 0.056 & 0.94 \\\\\n & Naive & 0.121 & 0.139 & 0.47 \\\\\n & Global & 0.098 & 0.123 & 0.72 \\\\\n & EC-HTE & \\textbf{0.013} & 0.080 & 0.92 \\\\\n\\midrule\n\\multirow{2}{*}{CausalForest}\n & Naive & 0.058 & 0.090 & 0.82 \\\\\n & EC-HTE & \\textbf{0.010} & 0.093 & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces R-learner $|\\text{bias}|$ by 89\\% (0.121 $\\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\\ref{tab:rlearner}).\nThe bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.\n\n\\paragraph{Multiplicative treatment effects.}\nWe further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \\times \\exp(\\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\\text{expert}} = 500$, and 50 MC seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}\n\\label{tab:multiplicative}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Cov. \\\\\n\\midrule\nOracle & 0.003 & 0.038 & 0.96 \\\\\nNaive & 0.135 & 0.142 & 0.44 \\\\\nGlobal & 0.110 & 0.124 & 0.54 \\\\\nEC-HTE & \\textbf{0.054} & 0.068 & 0.955 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE reduces RMSE by 52\\% relative to naive (0.068 vs.\\ 0.142) and restores coverage to the nominal level (0.955; Table~\\ref{tab:multiplicative}).\nEC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.\n\n\\section{Robustness to Class Imbalance}\n\\label{app:classimbalance}\n\nAssumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.\nWe sweep $P(Z{=}1) \\in \\{0.1, 0.2, 0.3, 0.4, 0.5\\}$ with $K \\in \\{2,4\\}$, extreme misclassification heterogeneity, $n_{\\text{expert}}{=}250$, and 100 MC seeds (Table~\\ref{tab:pz1_sweep}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to class imbalance ($n_{\\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\\% CI coverage.}\n\\label{tab:pz1_sweep}\n\\small\n\\begin{tabular}{cc ccc}\n\\toprule\n$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\\\\n\\midrule\n0.1 & 2 & 0.998 & 0.92 & 0.94 \\\\\n0.2 & 2 & 0.989 & 0.76 & 0.94 \\\\\n0.3 & 2 & 0.994 & 0.78 & 0.94 \\\\\n0.4 & 2 & 0.995 & 0.87 & 0.94 \\\\\n0.5 & 2 & 0.995 & 0.86 & 0.93 \\\\\n\\midrule\n0.1 & 4 & 0.984 & 1.54 & 0.92 \\\\\n0.2 & 4 & 0.976 & 1.68 & 0.93 \\\\\n0.3 & 4 & 0.985 & 1.12 & 0.92 \\\\\n0.4 & 4 & 0.984 & 1.08 & 0.93 \\\\\n0.5 & 4 & 0.992 & 1.06 & 0.92 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTheorem~\\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \\geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.\nFor $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.\nFor $K{=}4$, EC-HTE underperforms global at $n_{\\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\\text{expert}} \\times P(Z_{\\text{minority}}) / K \\geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\\sim}6$ minority-class labels.\nThe gap narrows as $P(Z{=}1)$ increases (1.54 $\\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.\n\n\\section{Comparison with PPI Correction}\n\\label{app:ppi_comparison}\n\nPPI~\\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.\nApplied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.\nTwo variants arise naturally: \\emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \\emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).\n\nUnder the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.\nPooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.\nEC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.\nThis mechanism is outside both the PPI and DSL frameworks.\n\nThe key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.\nThis avoids the matrix inversion step that can amplify noise at small $n_{\\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.\nPPI-global inherits the same $\\Delta\\pi \\times \\Delta\\tau$ bias amplification as Global correction (Theorem~\\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.\n\n\\section{Civil Comments Validation}\n\\label{app:civilcomments}\n\nTo verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\\% toxic) from Civil Comments~\\cite{borkan2019nuanced}, a toxicity detection dataset.\nSubgroups are defined by \\texttt{text\\_length\\_bin} $\\times$ \\texttt{has\\_question} ($K{=}4$): S0 (long, no question, 38.8\\%), S1 (long, question, 11.4\\%), S2 (short, no question, 33.7\\%), S3 (short, question, 16.1\\%).\nSubgroup features were chosen a priori based on observable text properties; no feature search was performed.\nThree proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.\n\nTable~\\ref{tab:civil_cm} reports per-subgroup FPR and FNR.\nWe define $\\Delta\\pi = \\max_s \\pi_s - \\min_s \\pi_s$, where $\\pi_s$ is the overall misclassification rate for subgroup $s$.\nAll three models exhibit $\\Delta\\pi > 0.05$, with overall heterogeneity $\\Delta\\pi \\in [0.113, 0.160]$---comparable to the $\\Delta\\pi \\in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\\ref{app:multilm_opensource}).\nGPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\\in [0.42, 0.61]$ vs.\\ FNR $\\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).\nThe consistent presence of $\\Delta\\pi$ heterogeneity across two NLP tasks, eight LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\\Delta$ denotes max $-$ min across subgroups.}\n\\label{tab:civil_cm}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Metric & S0 & S1 & S2 & S3 & $\\Delta$ \\\\\n\\midrule\nGPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\\\\n       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\\\\n\\midrule\nGPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\\\\n            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\\\\n\\midrule\nGPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\\\\n              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bias Identity Validation with Real Confusion Matrices}\n\\label{app:realcm_bias}\n\nTheorem~\\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\\neq$ FNR).\nWe verify that the generalized identity $\\mathrm{bias}(z,s) = \\Delta\\tau \\cdot [B_s]_{z,1}$ (Remark~\\ref{thm:bias_identity}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\\Delta\\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).\n\nTable~\\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\\Delta\\tau \\cdot [B_s]_{z,1}$.\nThe aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \\geq 0.92$.\nThe single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.\n$R^2$ correlates strongly with $\\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.\n\n\\begin{table}[h]\n\\centering\n\\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}\n\\label{tab:realcm_r2}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nModel & Dataset & $R^2$ & $\\max|[B_s]_{z,1}|$ \\\\\n\\midrule\nGPT-4-turbo  & TweetEval & 0.993 & 0.328 \\\\\nQwen2.5-7B   & TweetEval & 0.990 & 0.272 \\\\\nMistral-7B   & TweetEval & 0.990 & 0.242 \\\\\nGemma-2-9B   & TweetEval & 0.982 & 0.185 \\\\\nGPT-4o       & Civil Comments & 0.979 & 0.198 \\\\\nGPT-4o       & TweetEval & 0.975 & 0.240 \\\\\nGPT-4.1      & TweetEval & 0.969 & 0.139 \\\\\nGPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\\\\nGPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\\\\nGPT-4o-mini  & TweetEval & 0.929 & 0.170 \\\\\nGPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\\\\n\\midrule\n\\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Applicability Screening with Real LLM Confusion Matrices}\n\\label{app:screening}\n\nWe apply the diagnostic conditions from Proposition~\\ref{prop:debiasing_hurts} and Section~\\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning eight LLMs (three open-source, five proprietary) across TweetEval and Civil Comments.\nTable~\\ref{tab:screening} summarizes which conditions each combination satisfies.\n\n\\begin{table}[h]\n\\centering\n\\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\\text{expert}}{=}500$.}\n\\label{tab:screening}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Dataset & $K$ & $\\kappa{\\leq}1.25$ & $\\max{\\leq}0.5$ & Budget & Pass all \\\\\n\\midrule\nGemma-2-9B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 2 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGemma-2-9B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nLlama-3.1-8B & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nMistral-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nQwen2.5-7B   & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-3.5-turbo & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4-turbo  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4.1      & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o       & TweetEval & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & CivilComm. & 4 & {\\small$\\times$} & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\nGPT-4o-mini  & TweetEval & 4 & {\\small$\\times$} & {\\small$\\checkmark$} & {\\small$\\checkmark$} & {\\small$\\times$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo combination passes all three conditions; the bottleneck is $\\kappa(C_s) \\leq 1.25$, which requires $\\mathrm{FPR}_s + \\mathrm{FNR}_s \\lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.\nThe closest are Qwen2.5-7B True\\_short ($\\kappa{=}1.23$) and Mistral-7B True\\_short ($\\kappa{=}1.27$).\n\nUnder a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\\max(\\mathrm{FPR}_s, \\mathrm{FNR}_s) \\geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\\Delta\\tau{=}0.3$, 100 MC runs, $n_{\\text{expert}} \\in \\{250, 500\\}$) with each LLM's real per-subgroup confusion matrix.\nEC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\\%).\nThe four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\\mathrm{FPR}_{\\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.\nThe diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\\% of comparisons.\n\n\\paragraph{Diagnostic Applicability Analysis.}\nThe diagnostic (Proposition~\\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\\tau_s \\approx 0$ are hurt by global correction (since $\\delta_s \\neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.\n\nA simple meta-criterion recovers reliability: compute $\\max_s |\\delta_s| / ((1 - 2\\bar{\\pi}) \\cdot \\pi_s)$ across subgroups.\nWhen $\\max_s \\mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).\nWhen $\\max_s \\mathrm{score}(s) \\leq 1$, global correction may or may not hurt depending on unobservable $\\Delta\\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).\nThis threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.\n\nWe recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\\max_s \\mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.\n\n\\subsection{$\\kappa$ Stratification Analysis}\n\\label{app:kappa_analysis}\n\nThe condition number $\\kappa(\\hat{C}_s) = 1/|1 - \\mathrm{FPR}_s - \\mathrm{FNR}_s|$ quantifies confusion matrix invertibility and governs the bias-variance tradeoff of per-subgroup correction.\nThe $\\kappa \\leq 1.25$ threshold identified in the diagnostic rule (Section~\\ref{sec:budget}) is a \\emph{sufficient condition} for strongest bias reduction, not a necessary condition: EC-HTE maintains calibrated inference across a substantially wider $\\kappa$ range.\n\n\\paragraph{Synthetic data.}\nAcross all 520 synthetic configurations ($K{=}2$, $\\pi_s \\in [0.025, 0.275]$), the maximum per-config $\\kappa$ falls in $[1.43, 2.22]$; none reaches $\\kappa \\leq 1.25$ because the pooled rate $\\bar{\\pi}{=}0.15$ sets a floor of $\\kappa{=}1/(1{-}2 \\cdot 0.15){=}1.43$.\nTable~\\ref{tab:kappa_synth} shows a two-bin stratification at $\\kappa{=}2$: EC-HTE achieves zero analytic bias in both bins, while global correction harms at least one subgroup in 100\\% of $\\kappa > 2$ configurations.\nMonte Carlo validation ($K{=}2$, $n_{\\text{expert}}{=}500$) confirms EC-HTE dominance at $\\kappa{=}2.0$: 86\\% bias reduction, 10\\% lower RMSE, and 95.5\\% coverage vs.\\ 88.3\\% for Global.\n\n\\begin{table}[h]\n\\centering\n\\caption{Synthetic $\\kappa$ stratification ($K{=}2$, 520 configs). ``Debiasing hurts'' = global correction increases $|\\text{bias}|$ for $\\geq$1 subgroup.}\n\\label{tab:kappa_synth}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\kappa$ bin & $n$ & EC-HTE bias & Debiasing hurts & Global $|\\text{bias}|/|\\text{bias}_{\\text{naive}}|$ \\\\\n\\midrule\n$\\leq 2.0$ & 420 & 0 (exact) & 35.0\\% & 0.152 \\\\\n$> 2.0$    & 100 & 0 (exact) & 100\\% & 0.326 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Real LLM confusion matrices.}\nAll 13 real LLM--dataset combinations ($K{=}4$) have $\\kappa \\in [1.88, 2.99]$---none reaches $\\kappa \\leq 1.25$, because no current LLM achieves $\\mathrm{FPR}_s + \\mathrm{FNR}_s < 0.20$ uniformly across subgroups.\nTable~\\ref{tab:kappa_real} reports performance stratified by $\\kappa$ bin and expert budget.\nThe key finding is that EC-HTE maintains calibrated coverage ($\\geq$93\\%) across all $\\kappa$ bins at $n_{\\text{expert}} \\geq 250$, compared to 86--91\\% for Global.\nAt $n_{\\text{expert}}{=}500$, EC-HTE also achieves competitive RMSE in the $\\kappa \\leq 2$ bin (ratio 1.01) and bias win rate of 75\\%; at $n_{\\text{expert}}{=}250$, the variance cost of per-subgroup estimation dominates, and Global achieves lower RMSE---consistent with the bias-variance tradeoff documented in the main text (Section~\\ref{sec:ec_hte_eval}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Real LLM $\\kappa$ stratification ($K{=}4$, MC validation). Ratios = EC-HTE / Global; values $<1$ favor EC-HTE. Coverage is EC-HTE absolute; Global coverage ranges 0.86--0.91 across bins.}\n\\label{tab:kappa_real}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n$\\kappa$ bin & $n_{\\text{expert}}$ & Bias ratio & RMSE ratio & Bias win & Cov.\\ (EC-HTE) \\\\\n\\midrule\n\\multirow{2}{*}{$\\leq 2.0$ ($n{=}4$)}\n & 500 & 0.99 & 1.01 & 75\\% & 0.943 \\\\\n & 250 & 1.09 & 1.13 & 0\\%  & 0.932 \\\\\n\\midrule\n\\multirow{2}{*}{$> 2.0$ ($n{=}9$)}\n & 500 & 1.11 & 1.22 & 22\\% & 0.949 \\\\\n & 250 & 1.26 & 1.43 & 0\\%  & 0.940 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three-tier $\\kappa$ structure is thus: (i)~$\\kappa > 100$: near-random classification, singularity guard triggers automatic fallback to global correction; (ii)~$\\kappa \\leq 1.25$: strongest theoretical regime with guaranteed bias reduction and coverage; (iii)~$\\kappa \\in (1.25, {\\sim}3]$: the practical operating range for current LLMs, where EC-HTE provides calibrated inference (coverage $\\geq$93\\%) and achieves RMSE gains when expert budget is sufficient ($n_{\\text{expert}} \\geq 500$).\n\n\\section{Plug-in Standard Error Validation}\n\\label{app:bootstrap_se}\n\nA natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.\nWe verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\\text{expert}} \\in \\{50, 100, 250, 500\\}$, 50 replications per budget level).\nAt each budget, we compute the plug-in 95\\% confidence interval and record empirical coverage.\nAcross all expert budgets, the plug-in SE yields coverage $\\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.\nThis self-calibration arises because the same noise in $\\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.\n\n\\paragraph{CausalForestDML.}\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$, $n_{\\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\\% aggregate coverage---close to the 94--96\\% oracle coverage (Table~\\ref{tab:cf_oracle}).\nThe high-error subgroup ($s_1$, $\\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\\%) than the low-error subgroup ($s_0$: 95.0\\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.\nBy contrast, the DIM plug-in SE achieves $\\geq$95\\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.\n\n\\paragraph{Full bootstrap SE.}\nA \\emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.\nUnder $K{=}2$ extreme heterogeneity ($\\pi{=}[0.05, 0.25]$, $n_{\\text{expert}}{=}250$), plug-in SE achieves 93.8\\% aggregate coverage; the full bootstrap improves this to exactly 95.0\\% ($+$1.2pp).\nTable~\\ref{tab:bootstrap_se} reports per-subgroup results.\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest coverage: plug-in SE vs.\\ full bootstrap SE ($B{=}100$, $n_{\\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\\sim}1.15\\times$ plug-in.}\n\\label{tab:bootstrap_se}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nSubgroup & Plugin Cov. & Boot.\\ Cov. & Oracle Cov. & Plugin SE & Boot.\\ SE \\\\\n\\midrule\n$s_0$ ($\\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\\\\n$s_1$ ($\\pi{=}0.25$) & 0.925 & \\textbf{0.975} & 0.875 & 0.087 & 0.103 \\\\\n\\midrule\nAggregate & 0.938 & \\textbf{0.950} & 0.900 & 0.073 & 0.083 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\\% to 97.5\\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.\nOracle coverage (90.0\\%) is consistent with the 94\\% reported in the oracle decomposition (Table~\\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.\nThe computational cost is substantial ($B \\times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.\n\n\\paragraph{Bootstrap coverage across expert budgets.}\nTable~\\ref{tab:bootstrap_small_n} extends the analysis to $n_{\\text{expert}} \\in \\{25, 50, 75, 100, 200\\}$ using the DIM estimator with Centered EB confusion matrix estimation ($K{=}2$ extreme, $\\pi{=}[0.05, 0.25]$, 20 MC runs, $B{=}100$).\nBootstrap SE maintains $\\geq$95\\% coverage across all expert budgets, including $n_{\\text{expert}}{=}25$ (${\\approx}12$ labels per subgroup).\nPlug-in SE is already near-nominal ($\\geq$91.2\\%) at all budgets tested.\n\n\\begin{table}[h]\n\\centering\n\\caption{HB EC-HTE coverage across expert budgets: plug-in vs.\\ bootstrap SE (DIM, $K{=}2$ extreme, 20 MC, $B{=}100$).}\n\\label{tab:bootstrap_small_n}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$n_{\\text{expert}}$ & Plugin Cov. & Boot.\\ Cov. & SE Ratio & $|\\text{Bias}|$ \\\\\n\\midrule\n25 & 0.925 & \\textbf{1.000} & 2.86 & 0.079 \\\\\n50 & 0.975 & 0.988 & 2.93 & 0.067 \\\\\n75 & 0.912 & \\textbf{0.975} & 2.59 & 0.065 \\\\\n100 & 0.963 & 0.963 & 1.52 & 0.060 \\\\\n200 & 0.963 & 0.950 & 1.17 & 0.061 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt small $n_{\\text{expert}}$, bootstrap SE inflates confidence intervals by $2{-}3\\times$ relative to plug-in (SE ratio column), guaranteeing nominal coverage but reducing statistical power.\nAt $n_{\\text{expert}} \\geq 100$, the SE ratio converges to ${\\sim}1.2{-}1.5\\times$, and plug-in SE alone achieves $\\geq$96\\% coverage.\nFor practical deployment, we recommend $n_{\\text{expert}} \\geq 50$: bootstrap maintains nominal coverage (98.8\\%) with moderate SE inflation (2.9$\\times$), and plug-in SE achieves 97.5\\%---close to nominal without bootstrap overhead.\n\n\\paragraph{Finite-sample remainder.}\nBy first-order matrix perturbation, $\\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\\|E_s\\|^2)$, where $E_s = \\hat{C}_s - C_s$ satisfies $\\|E_s\\| = O_p(n_{\\text{expert}}^{-1/2})$.\nThe remainder in the corrected CATE is therefore $R_n = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\|C_s^{-1}\\|^2) = O_p(n_{\\text{expert}}^{-1/2} \\cdot \\kappa(C_s))$, since $\\|C_s^{-1}\\| = O(\\kappa(C_s))$ for stochastic matrices.\nThis motivates the $\\kappa > 100$ singularity guard (Section~\\ref{sec:method}).\n\n\\subsection{CausalForest Oracle Coverage Decomposition}\n\\label{app:cf_oracle}\n\nTo isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\\hat{C}_s$ (HB), (4)~Global with true $\\bar{C}$, (5)~Global with estimated $\\hat{\\bar{C}}$, and (6)~Naive.\nTable~\\ref{tab:cf_oracle} reports coverage, $|\\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).\n\n\\begin{table}[h]\n\\centering\n\\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}\n\\label{tab:cf_oracle}\n\\small\n\\begin{tabular}{ll ccc}\n\\toprule\nDGP & Method & Cov.\\ (\\%) & $|\\text{Bias}|$ & RMSE \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}4$, extreme\\\\$n{=}500$}}\n & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\\\\n & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\\\\n & Global true $\\bar{C}$   & 91.3 & 0.037 & 0.110 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 91.1 & 0.038 & 0.111 \\\\\n & Naive                    & 88.3 & 0.045 & 0.095 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, extreme\\\\$n{=}250$}}\n & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\\\\n & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\\\\n & Global true $\\bar{C}$   & 88.5 & 0.045 & 0.083 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 88.3 & 0.045 & 0.085 \\\\\n & Naive                    & 82.8 & 0.046 & 0.077 \\\\\n\\midrule\n\\multirow{6}{*}{\\shortstack[l]{$K{=}2$, MF2 DGP\\\\$\\tau{=}(0.10,0.40)$}}\n & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\\\\n & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\\\\n & EC-HTE est.\\ $\\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\\\\n & Global true $\\bar{C}$   & 95.0 & 0.107 & 0.114 \\\\\n & Global est.\\ $\\hat{\\bar{C}}$ & 94.3 & 0.105 & 0.114 \\\\",
      "numLines": 400,
      "startLine": 800,
      "totalLines": 1538
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Agent · `toolu_01CfGLBvDZzKv4eD22XUrKoo`</summary>

```json
{
  "description": "Parse registry JSON for key experiments",
  "prompt": "I need you to extract key metrics from a registry JSON file for a number audit of a paper. The file is at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt\n\nThis is JSON with schema: {result: string}. The result field is a string containing the actual registry data.\n\nI need you to extract ALL metrics and conclusions from these specific experiment IDs (and any others you find):\n- exp-001, exp-002, exp-003, exp-008, exp-019, exp-023, exp-035, exp-036, exp-037, exp-038, exp-039, exp-040\n- Any experiments related to stance_detection, sign_reversal, bias_identity, diagnostic, causal_forest, r_learner, hatespeech, asymmetric\n\nFor each experiment found, report:\n1. exp_id\n2. title/description\n3. All metrics (R², bias values, RMSE, coverage, AUC, sign reversal rates, amplification factors, etc.)\n4. conclusion/status\n5. Any key numbers that appear in the experiment\n\nThe paper claims these numbers:\n- R²≥0.97\n- 14.9% sign reversal at τ(0)=0.03\n- 5×, 7.4× bias reduction\n- AUC 1.0/0.86/0.63\n- 11 empirical CMs\n- bias 0.059→0.008\n- 93.8% coverage\n- 260/520 configurations\n- 2.86×, 2.41× amplification\n- 89% R-learner bias reduction\n- 4.7×, 4.9×, 5.9× factors\n- γ_T=0.10 → 75% coverage\n\nPlease probe the structure first with jq, then extract all experiments. Report everything verbatim - do not summarize away any numbers.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "9e781a7f-f6ea-4ad2-9b1e-d15e28a1be9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjQrtrcU6xrQTDd17FDZwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15903,
      "cache_read_input_tokens": 26426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15903
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

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Parse registry JSON for key experiments",
  "task_type": "local_agent",
  "prompt": "I need you to extract key metrics from a registry JSON file for a number audit of a paper. The file is at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt\n\nThis is JSON with schema: {result: string}. The result field is a string containing the actual registry data.\n\nI need you to extract ALL metrics and conclusions from these specific experiment IDs (and any others you find):\n- exp-001, exp-002, exp-003, exp-008, exp-019, exp-023, exp-035, exp-036, exp-037, exp-038, exp-039, exp-040\n- Any experiments related to stance_detection, sign_reversal, bias_identity, diagnostic, causal_forest, r_learner, hatespeech, asymmetric\n\nFor each experiment found, report:\n1. exp_id\n2. title/description\n3. All metrics (R², bias values, RMSE, coverage, AUC, sign reversal rates, amplification factors, etc.)\n4. conclusion/status\n5. Any key numbers that appear in the experiment\n\nThe paper claims these numbers:\n- R²≥0.97\n- 14.9% sign reversal at τ(0)=0.03\n- 5×, 7.4× bias reduction\n- AUC 1.0/0.86/0.63\n- 11 empirical CMs\n- bias 0.059→0.008\n- 93.8% coverage\n- 260/520 configurations\n- 2.86×, 2.41× amplification\n- 89% R-learner bias reduction\n- 4.7×, 4.9×, 5.9× factors\n- γ_T=0.10 → 75% coverage\n\nPlease probe the structure first with jq, then extract all experiments. Report everything verbatim - do not summarize away any numbers.",
  "uuid": "dffa8d81-9c48-446a-b595-e921ebcee853",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

## Round 1

77 recorded events

### User

_source line 40 · 2026-05-24T04:29:42.800Z_

I need you to extract key metrics from a registry JSON file for a number audit of a paper. The file is at:
/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt

This is JSON with schema: {result: string}. The result field is a string containing the actual registry data.

I need you to extract ALL metrics and conclusions from these specific experiment IDs (and any others you find):
- exp-001, exp-002, exp-003, exp-008, exp-019, exp-023, exp-035, exp-036, exp-037, exp-038, exp-039, exp-040
- Any experiments related to stance_detection, sign_reversal, bias_identity, diagnostic, causal_forest, r_learner, hatespeech, asymmetric

For each experiment found, report:
1. exp_id
2. title/description
3. All metrics (R², bias values, RMSE, coverage, AUC, sign reversal rates, amplification factors, etc.)
4. conclusion/status
5. Any key numbers that appear in the experiment

The paper claims these numbers:
- R²≥0.97
- 14.9% sign reversal at τ(0)=0.03
- 5×, 7.4× bias reduction
- AUC 1.0/0.86/0.63
- 11 empirical CMs
- bias 0.059→0.008
- 93.8% coverage
- 260/520 configurations
- 2.86×, 2.41× amplification
- 89% R-learner bias reduction
- 4.7×, 4.9×, 5.9× factors
- γ_T=0.10 → 75% coverage

Please probe the structure first with jq, then extract all experiments. Report everything verbatim - do not summarize away any numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "1a379931-675c-4c6d-81aa-bd30de20c640"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt",
  "usage": {
    "total_tokens": 15479,
    "tool_uses": 1,
    "duration_ms": 3133
  },
  "last_tool_name": "Read",
  "uuid": "59b46545-4654-4e98-9801-c19d024d3bed",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01Y6LzQGdxWuELUpVjcZPGWs`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "915a6a87-4376-4766-b8f9-c26a8504018e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3uZmctw3a9jCHFHRCLSpA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15468,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15468,
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

_source line 43 · 2026-05-24T04:29:46.235Z_

<details><summary>↩ Tool result · reported error · `toolu_01Y6LzQGdxWuELUpVjcZPGWs`</summary>

```text
File content (31185 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "1b8a4a07-eddf-4df5-a01e-9952cfed6d5e",
  "tool_use_result": "Error: File content (31185 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Reading ~/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt",
  "usage": {
    "total_tokens": 16559,
    "tool_uses": 2,
    "duration_ms": 7750
  },
  "last_tool_name": "Read",
  "uuid": "5adcd6f4-a3f2-4be1-8da3-77aba361fdd0",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01Hu98AA3n9JgSof42crLY9h`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt",
  "limit": 100,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "a0d7b2a5-6f79-415d-9d3f-f7a7db2e43c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KytX15mpkPiP7Di4sRRYb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1080,
      "cache_read_input_tokens": 15468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1080,
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

_source line 46 · 2026-05-24T04:29:51.085Z_

<details><summary>↩ Tool result · reported error · `toolu_01Hu98AA3n9JgSof42crLY9h`</summary>

```text
File content (31185 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "eaaa89b0-9d59-41e0-b467-a62aa19f7fec",
  "tool_use_result": "Error: File content (31185 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Count lines in registry file",
  "usage": {
    "total_tokens": 16874,
    "tool_uses": 3,
    "duration_ms": 11009
  },
  "last_tool_name": "Bash",
  "uuid": "025ff3d6-c9c1-4744-8ed7-19a42cd26abb",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01NGZdZqmyKEwzVCrBHAqYwZ`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt",
  "description": "Count lines in registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "bde9e7ba-8163-4913-ac47-d98854878fce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vcFEo11nWxqKmfKoDAyYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 16548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 253,
        "ephemeral_1h_input_tokens": 0
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

_source line 49 · 2026-05-24T04:29:53.990Z_

<details><summary>↩ Tool result · `toolu_01NGZdZqmyKEwzVCrBHAqYwZ`</summary>

```text
0 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "74969380-60b5-471f-8f98-050d1ae51985"
}
```

</details>

---

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Parse JSON structure of registry file",
  "usage": {
    "total_tokens": 17156,
    "tool_uses": 4,
    "duration_ms": 16997
  },
  "last_tool_name": "Bash",
  "uuid": "58484be6-a83b-4c2e-8b78-f860c1312dbb",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_01UC6HCaAQbJ7BSdcYDi61eg`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\n# The outer structure has a 'result' field that is a string\nresult_str = data.get('result', '')\n# Parse the inner JSON\ninner = json.loads(result_str)\n# Show top-level keys\nprint('Top-level keys:', list(inner.keys()))\n\" 2>&1 | head -20",
  "description": "Parse JSON structure of registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "43706ad6-6593-4dd4-be9a-ac266d31e709",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEmdpheULM4Si1LsFAhCq4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 280,
      "cache_read_input_tokens": 16801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 280,
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

_source line 52 · 2026-05-24T04:29:59.923Z_

<details><summary>↩ Tool result · `toolu_01UC6HCaAQbJ7BSdcYDi61eg`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "119602bb-1bc4-41d2-a433-1cda80be17ea"
}
```

</details>

---

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Explore data structure",
  "usage": {
    "total_tokens": 17544,
    "tool_uses": 5,
    "duration_ms": 21752
  },
  "last_tool_name": "Bash",
  "uuid": "5ddaa069-cac1-4ae0-8a59-0a59bdf1edf2",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01Lk6SK71Hin7vLEiswHzwwh`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nprint('success:', inner['success'])\nprint('error:', inner['error'])\nprint('metadata:', json.dumps(inner['metadata'], indent=2))\nd = inner['data']\nprint('data type:', type(d).__name__)\nif isinstance(d, dict):\n    print('data keys:', list(d.keys()))\nelif isinstance(d, list):\n    print('data length:', len(d))\n    if len(d) > 0:\n        print('first item keys:', list(d[0].keys()) if isinstance(d[0], dict) else type(d[0]).__name__)\n\" 2>&1",
  "description": "Explore data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "43d8435a-8985-4f67-aad8-a61598d1c58e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hqLA4oJFMvdp2gdu9PkJs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 17081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 315,
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

_source line 55 · 2026-05-24T04:30:04.661Z_

<details><summary>↩ Tool result · `toolu_01Lk6SK71Hin7vLEiswHzwwh`</summary>

```text
success: True
error: None
metadata: {
  "elapsed_seconds": 0.1459
}
data type: dict
data keys: ['experiments', 'count', 'total', 'baseline']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "45f47991-4962-4ff2-8f59-c1c10cf3f58f"
}
```

</details>

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running List all experiments",
  "usage": {
    "total_tokens": 18025,
    "tool_uses": 6,
    "duration_ms": 26393
  },
  "last_tool_name": "Bash",
  "uuid": "9950f3cc-6aa8-455d-8e1b-6c5ebafd707a",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_01MDAhWJCupvfJLp9AGtpBUd`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nd = inner['data']\nprint('count:', d['count'])\nprint('total:', d['total'])\nprint('baseline:', json.dumps(d['baseline'], indent=2) if d['baseline'] else None)\nexps = d['experiments']\nprint('Number of experiments:', len(exps))\nfor exp in exps:\n    print(f\\\"  {exp.get('exp_id', 'NO_ID')}: {exp.get('title', exp.get('description', 'NO_TITLE'))}\\\")\n\" 2>&1",
  "description": "List all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "746bbec5-11bc-40ad-a1e4-a80ea5b0aa93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SmLm3XumWYqB6b3dN7iPg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 17396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 408,
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

_source line 58 · 2026-05-24T04:30:09.428Z_

<details><summary>↩ Tool result · reported error · `toolu_01MDAhWJCupvfJLp9AGtpBUd`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 12, in &lt;module>
    print(f"  {exp.get('exp_id', 'NO_ID')}: {exp.get('title', exp.get('description', 'NO_TITLE'))}")
               ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
count: 42
total: 42
baseline: None
Number of experiments: 42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "a3347e1c-a879-48a5-9c22-4187a1a58ee5",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 12, in &lt;module>\n    print(f\"  {exp.get('exp_id', 'NO_ID')}: {exp.get('title', exp.get('description', 'NO_TITLE'))}\")\n               ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'\ncount: 42\ntotal: 42\nbaseline: None\nNumber of experiments: 42"
}
```

</details>

---

### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Understand experiments structure",
  "usage": {
    "total_tokens": 18560,
    "tool_uses": 7,
    "duration_ms": 31980
  },
  "last_tool_name": "Bash",
  "uuid": "ac290178-5383-40c5-8e75-252e3a01a9e3",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_01GSD3VMQvdptiM2e7vSiqpv`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nd = inner['data']\nexps = d['experiments']\n# experiments might be a dict with string keys\nprint('type of experiments:', type(exps).__name__)\nif isinstance(exps, dict):\n    print('experiment keys:', list(exps.keys())[:5])\n    first_key = list(exps.keys())[0]\n    print('first value type:', type(exps[first_key]).__name__)\n    print('first value:', json.dumps(exps[first_key], indent=2)[:500] if isinstance(exps[first_key], (dict, list)) else exps[first_key][:500])\nelif isinstance(exps, list):\n    print('first item type:', type(exps[0]).__name__)\n    print('first item:', exps[0][:500] if isinstance(exps[0], str) else json.dumps(exps[0], indent=2)[:500])\n\" 2>&1",
  "description": "Understand experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "ff6ce770-8d2a-483d-9d59-aff4058d6433",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsCpExWzfmqBuCSofJ4Uvs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 17804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 463,
        "ephemeral_1h_input_tokens": 0
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

_source line 61 · 2026-05-24T04:30:14.876Z_

<details><summary>↩ Tool result · `toolu_01GSD3VMQvdptiM2e7vSiqpv`</summary>

```text
type of experiments: dict
experiment keys: ['exp-040', 'exp-039', 'exp-038', 'exp-036', 'exp-037']
first value type: dict
first value: {
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-23T15:54:23.294Z",
  "updated_at": "2026-05-23T15:55:16.698Z",
  "hypothesis": "EC-HTE is robust to moderate treatment-dependent misclassification (\u03b3_T\u22640.05, coverage \u226589.7%) but degrades at \u03b3_T\u22650.10 because per-subgroup CM estimates become biased when expert sample treatment composition doesn't match the full sample.",
  "spec": {
    "command": "python exp_treatment_dep_misclass.py",
    "server": "loca
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "ae8160b1-f33c-403f-b19f-0dd3030dcc50"
}
```

</details>

---

### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running List all experiment IDs",
  "usage": {
    "total_tokens": 19337,
    "tool_uses": 8,
    "duration_ms": 35748
  },
  "last_tool_name": "Bash",
  "uuid": "c6fb5e38-9215-4a4d-b75e-84535e789b37",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_016cTUVrvEECELdjnbME2Vev`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nprint('All experiment IDs:', sorted(exps.keys()))\n\" 2>&1",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "3f7cc577-e126-4cfc-9646-8450fbea8f16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWfPSaLnb1eczXBWv2iS7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 18267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 775,
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

_source line 64 · 2026-05-24T04:30:18.668Z_

<details><summary>↩ Tool result · `toolu_016cTUVrvEECELdjnbME2Vev`</summary>

```text
All experiment IDs: ['exp-001', 'exp-002', 'exp-003', 'exp-004', 'exp-005', 'exp-006', 'exp-007', 'exp-007b', 'exp-008', 'exp-010', 'exp-011', 'exp-012', 'exp-013', 'exp-014', 'exp-015', 'exp-016', 'exp-017', 'exp-018', 'exp-019', 'exp-020', 'exp-021', 'exp-022', 'exp-023', 'exp-024', 'exp-025', 'exp-026', 'exp-027', 'exp-027b', 'exp-027c', 'exp-028', 'exp-029', 'exp-030', 'exp-031', 'exp-032', 'exp-033', 'exp-034', 'exp-035', 'exp-036', 'exp-037', 'exp-038', 'exp-039', 'exp-040']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "167c57f8-dd98-4fbc-ab76-c3991c199796"
}
```

</details>

---

### System

_source line 65_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Extract exp-001, exp-002, exp-003 details",
  "usage": {
    "total_tokens": 19859,
    "tool_uses": 9,
    "duration_ms": 44568
  },
  "last_tool_name": "Bash",
  "uuid": "a1e39c75-6fdb-4a2e-904c-8364a405c1be",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Bash · `toolu_016taShihy55YKCEdYk2j9RN`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nfor eid in ['exp-001', 'exp-002', 'exp-003']:\n    e = exps[eid]\n    print('='*80)\n    print(f'EXPERIMENT: {eid}')\n    print(f'status: {e.get(\\\"status\\\")}')\n    print(f'hypothesis: {e.get(\\\"hypothesis\\\")}')\n    print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n    print(f'created_at: {e.get(\\\"created_at\\\")}')\n    print(f'updated_at: {e.get(\\\"updated_at\\\")}')\n    if 'spec' in e:\n        spec = e['spec']\n        print(f'spec.command: {spec.get(\\\"command\\\")}')\n        print(f'spec.description: {spec.get(\\\"description\\\")}')\n    if 'results' in e and e['results']:\n        print(f'results: {json.dumps(e[\\\"results\\\"], indent=2)}')\n    if 'metrics' in e and e['metrics']:\n        print(f'metrics: {json.dumps(e[\\\"metrics\\\"], indent=2)}')\n    # Print any other keys\n    shown = {'status','hypothesis','conclusion','created_at','updated_at','spec','results','metrics','retry_count'}\n    for k in e:\n        if k not in shown:\n            val = e[k]\n            if val is not None and val != '' and val != [] and val != {}:\n                print(f'{k}: {json.dumps(val, indent=2) if isinstance(val, (dict,list)) else val}')\n\" 2>&1",
  "description": "Extract exp-001, exp-002, exp-003 details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "cd829ff7-48ac-42c5-8e61-4b8f8005a8a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKAbKzKviYb64FjmTfz49A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 19042,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 520,
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

_source line 67 · 2026-05-24T04:30:27.461Z_

<details><summary>↩ Tool result · `toolu_016taShihy55YKCEdYk2j9RN`</summary>

```text
================================================================================
EXPERIMENT: exp-001
status: DONE
hypothesis: Hierarchical Bayesian Dirichlet-prior confusion matrix estimator 通过 partial pooling 在 n_expert 小（50-100）时比 MLE/Laplace 实现更低 RMSE 和更好的 coverage 校准，因为它能跨子群借力减少估计方差
conclusion: success
created_at: 2026-05-20T19:44:54.310Z
updated_at: 2026-05-20T23:55:59.564Z
spec.command: python exp001_hb_synthetic.py 2>&1 | tee results/exp001_run.log
spec.description: None
metrics: {
  "mcmc_rhat_max": 1.024,
  "mcmc_ess_min": 129,
  "mcmc_divergent": 0,
  "runtime_min": 69,
  "total_mc_runs": 3600,
  "hb_vs_mle_rmse_improvement_k2_n50": "4-9%",
  "hb_vs_mle_rmse_improvement_k2_n100": "1-2%",
  "hb_vs_mle_rmse_improvement_k4_n50_moderate": "6-9%",
  "hb_coverage_min": 0.87,
  "hb_coverage_median": 0.93,
  "k4_extreme_n50_blowup": false,
  "k4_extreme_n50_blowup_note": "Fixed by singularity guard + 4-chain MCMC",
  "mcmc_fix_4chain": {
    "rhat_max_all_configs": 1.0034,
    "ess_min_all_configs": 1618,
    "ess_improvement": "~4x vs 2-chain",
    "k4_extreme_n50_A_rmse_z0": "3.14 \u2192 0.99",
    "k4_extreme_n50_B_rmse_z0": "509.93 \u2192 0.27",
    "k4_extreme_n100_A_rmse_z0": "11.57 \u2192 0.29",
    "singularity_guard_triggers": "extreme/n=50 only (2 HB, 3 MLE / 100 runs)",
    "results_file": "results/exp001_hb_results_v2.csv"
  },
  "hyperprior_sensitivity": {
    "scale_range": "0.5-2.0",
    "k2_rmse_variation": "<1%",
    "k4_rmse_variation": "~4-5%",
    "coverage_invariant": true,
    "conclusion": "robust",
    "results_file": "results/exp001_hyperprior_sensitivity.csv"
  }
}
completed_at: 2026-05-20T21:32:51.348Z
================================================================================
EXPERIMENT: exp-002
status: DONE
hypothesis: Global correction 的子群内 bias 遵循解析公式 bias ∝ Δ_misclass × Δ_CATE，且存在参数区域使 |bias_global| > |bias_naive|（去偏反而加偏），该区域在 K=4 子群时比 K=2 更大
conclusion: success
created_at: 2026-05-20T19:44:56.556Z
updated_at: 2026-05-20T21:26:53.094Z
spec.command: python exp002_bias_bound.py 2>&1 | tee results/exp002_run.log
spec.description: None
metrics: {
  "r2_k2": 0.9939,
  "r2_k4": 0.9738,
  "tightness_ratio_k2_median": 1.0027,
  "tightness_ratio_k4_median": 1.0234,
  "debiasing_hurts_pct": 50,
  "debiasing_hurts_pct_note": "260/520 (excluding dc=0 rows where bias=0)",
  "debiasing_hurts_threshold_delta_misclass": 0.1235,
  "max_bias_ratio_k2": 2.86,
  "max_bias_ratio_k4": 2.41,
  "coverage_2se_k2": 0.951,
  "coverage_2se_k4": 0.94
}
completed_at: 2026-05-20T20:52:13.210Z
================================================================================
EXPERIMENT: exp-003
status: DONE
hypothesis: 在真实文本子群结构（TweetEval sentiment, 基于hashtag和文本长度的4子群）上，当LLM误分类率跨子群异质时，Global correction在低误分类子群反而加偏（debiasing hurts），而Stratified MLE在大子群表现更优但小子群存在variance penalty——验证EC-HTE partial pooling的必要性
conclusion: success
created_at: 2026-05-20T22:28:35.035Z
updated_at: 2026-05-21T04:08:06.566Z
spec.command: python exp003_tweeteval.py 2>&1 | tee results/exp003_run_v2.log
spec.description: None
metrics: {
  "phase": "A_semi_synthetic",
  "n_subgroups": 4,
  "misclass_rates": "S0=0.05, S1=0.10, S2=0.15, S3=0.25",
  "subgroup_sizes": "S0~38%, S1~38%, S2~12%, S3~12%",
  "p_z1_actual": 0.39,
  "debiasing_hurts_confirmed": true,
  "mc_runs": 100,
  "v3_hb_integration_100mc": {
    "methods": [
      "oracle",
      "naive",
      "global_corrected",
      "stratified_mle",
      "hb_ec_hte"
    ],
    "hb_vs_mle_summary": {
      "n50_S3_extreme": "-57% RMSE (HB worse, but not catastrophic)",
      "n50_S3_moderate": "-54% RMSE z1 (HB worse)",
      "n100_S3_extreme": "+60% RMSE z1 (HB dramatically better)",
      "n100_S3_moderate": "+24% RMSE z1 (HB better)",
      "n100_S2": "+5-8% RMSE (HB better)",
      "n250_S3": "+5-17% RMSE (HB better)",
      "n500_all": "+0.2-1.6% (converged)"
    },
    "key_finding": "100 MC confirms: S3 blowup at n=50 is real but moderate (not catastrophic as dry-run suggested). At n>=100, HB is better everywhere, especially S3 (+26-60%). Partial pooling sweet spot is n=100-250.",
    "hypothesis_verdict": "validated_with_boundary",
    "boundary_condition": "n_expert>=100 recommended; n=50 with extreme heterogeneity in tiny subgroups shows moderate degradation"
  },
  "results_file_v3": "results/exp003_phase_a_v3.csv",
  "results_file_v3_raw": "results/exp003_phase_a_v3_raw.csv"
}
completed_at: 2026-05-20T22:29:06.267Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "eb3a27bc-65c5-4e54-bee9-98ed8b6afc70"
}
```

</details>

---

### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Extract exp-008, exp-019, exp-023 details",
  "usage": {
    "total_tokens": 22546,
    "tool_uses": 10,
    "duration_ms": 56144
  },
  "last_tool_name": "Bash",
  "uuid": "f5587c8d-6fff-4bc8-9482-8ce8b9e7467b",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Bash · `toolu_01Buh7SDMdNe38jiChUeWCcP`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nfor eid in ['exp-008', 'exp-019', 'exp-023']:\n    e = exps[eid]\n    print('='*80)\n    print(f'EXPERIMENT: {eid}')\n    print(f'status: {e.get(\\\"status\\\")}')\n    print(f'hypothesis: {e.get(\\\"hypothesis\\\")}')\n    print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n    if 'spec' in e:\n        spec = e['spec']\n        print(f'spec.command: {spec.get(\\\"command\\\")}')\n    if 'results' in e and e['results']:\n        print(f'results: {json.dumps(e[\\\"results\\\"], indent=2)}')\n    if 'metrics' in e and e['metrics']:\n        print(f'metrics: {json.dumps(e[\\\"metrics\\\"], indent=2)}')\n    shown = {'status','hypothesis','conclusion','created_at','updated_at','spec','results','metrics','retry_count'}\n    for k in e:\n        if k not in shown:\n            val = e[k]\n            if val is not None and val != '' and val != [] and val != {}:\n                print(f'{k}: {json.dumps(val, indent=2) if isinstance(val, (dict,list)) else val}')\n\" 2>&1",
  "description": "Extract exp-008, exp-019, exp-023 details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "c3aacc52-ce54-46e3-9092-e469350337a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHk4rxP4CWjLLAJVAQpdvZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2651,
      "cache_read_input_tokens": 19562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2651,
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

_source line 70 · 2026-05-24T04:30:39.043Z_

<details><summary>↩ Tool result · `toolu_01Buh7SDMdNe38jiChUeWCcP`</summary>

```text
================================================================================
EXPERIMENT: exp-008
status: DONE
hypothesis: Subgroup-specific misclassification heterogeneity (Δπ > 0.05) persists across model generations and scales within the OpenAI family (from GPT-3.5 to GPT-5.4, spanning three model generations), demonstrating the bias mechanism is a structural property of LLM annotation rather than an artifact of a specific model version
conclusion: success
spec.command: python3 exp008_multi_llm.py --phase all + exp008_gpt55_annotate.py
metrics: {
  "models_completed": [
    "gpt-3.5-turbo",
    "gpt-4.1",
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4-turbo",
    "gpt-5.4"
  ],
  "total_models": 6,
  "proxy_provider": "OpenAI only",
  "gpt5x_model_used": "gpt-5.4",
  "gpt55_failed": "reasoning tokens consume max_tokens budget, too slow (~1min/call)",
  "filtered_analysis": {
    "excluded_subgroups": [
      "False_long (n=6)",
      "True_long (n=4)"
    ],
    "min_n_threshold": 10,
    "retained_subgroups": [
      "False_medium (n=187)",
      "False_short (n=109)",
      "True_medium (n=125)",
      "True_short (n=69)"
    ]
  },
  "effective_delta_pi": {
    "gpt-3.5-turbo": 0.198,
    "gpt-4-turbo": 0.149,
    "gpt-4.1": 0.098,
    "gpt-4o": 0.08,
    "gpt-4o-mini": 0.136,
    "gpt-5.4": 0.114
  },
  "all_effective_delta_pi_above_005": true,
  "worst_subgroup_consensus": "True_medium (5/6 models)",
  "spearman_significant_pairs": [
    "gpt-4-turbo vs gpt-4o (\u03c1=1.000)",
    "gpt-4.1 vs gpt-4o-mini (\u03c1=1.000)",
    "gpt-4.1 vs gpt-5.4 (\u03c1=1.000)",
    "gpt-4o-mini vs gpt-5.4 (\u03c1=1.000)"
  ],
  "spearman_note": "Only 4 subgroups after filtering, limited statistical power (most p>0.20)",
  "key_finding": "All 6 models (GPT-3.5 through GPT-5.4, three generations) show effective \u0394\u03c0 > 0.05 after excluding n<10 subgroups. Heterogeneity is structural, not model-specific."
}
completed_at: 2026-05-21T10:13:12.323Z
================================================================================
EXPERIMENT: exp-019
status: DONE
hypothesis: Theorem 1 bias decomposition R² remains high (>0.95) across P(Z=1) range [0.1, 0.5], and EC-HTE RMSE advantage over global persists but degrades at low P(Z=1) due to insufficient minority-class expert labels
conclusion: success
spec.command: python3 exp019_pz1_sweep.py
metrics: {
  "theorem1_r2": {
    "K2": {
      "pz0.1": 0.998,
      "pz0.2": 0.989,
      "pz0.3": 0.994,
      "pz0.4": 0.995,
      "pz0.5": 0.995
    },
    "K4": {
      "pz0.1": 0.984,
      "pz0.2": 0.976,
      "pz0.3": 0.985,
      "pz0.4": 0.984,
      "pz0.5": 0.992
    }
  },
  "theorem1_r2_range": "0.976-0.998 (all >0.95)",
  "rmse_ratio_hb_over_global": {
    "K2": {
      "pz0.1": 0.92,
      "pz0.2": 0.763,
      "pz0.3": 0.78,
      "pz0.4": 0.874,
      "pz0.5": 0.857
    },
    "K4": {
      "pz0.1": 1.542,
      "pz0.2": 1.684,
      "pz0.3": 1.121,
      "pz0.4": 1.082,
      "pz0.5": 1.063
    }
  },
  "hb_wins_K2": "all 5 P(Z=1) values (ratio 0.76-0.92)",
  "hb_wins_K4": "none (ratio 1.06-1.68)",
  "coverage_hb": "0.92-0.94 across all settings (near-nominal 0.95)",
  "coverage_naive": "0.65-0.79",
  "coverage_global": "0.79-0.90",
  "key_finding": "Theorem 1 R\u00b2>0.976 universally \u2014 bias decomposition holds regardless of P(Z=1). EC-HTE RMSE advantage depends on K: K=2 HB wins everywhere, K=4 HB loses at n_expert=250 (insufficient per-subgroup minority data). Coverage: HB 0.92-0.94 near-nominal at all settings."
}
parent: exp-001
completed_at: 2026-05-21T15:39:19.738Z
notes: Theorem 1 R²=0.976-0.998 across all P(Z=1)∈[0.1,0.5] × K∈{2,4} — bias decomposition holds universally, not dependent on class balance. EC-HTE RMSE: K=2 HB wins at all P(Z=1) (ratio 0.76-0.92); K=4 HB loses at n_expert=250 (ratio 1.06-1.68) due to 250/4=62.5 experts per subgroup being insufficient when minority class is small. Coverage: HB maintains 0.92-0.94 (near-nominal) while naive 0.65-0.79 and global 0.79-0.90 undercover. Directly addresses M2: A3 (class balance) affects RMSE but NOT Theorem 1 validity.
================================================================================
EXPERIMENT: exp-023
status: DONE
hypothesis: Under heterogeneous-τ DGP (Δτ varies 0.1–0.6 across subgroups), EC-HTE's subgroup-stratified CM correction outperforms Global pooled correction in bias because Global's single correction factor over-corrects low-Δτ subgroups and under-corrects high-Δτ subgroups; EC-HTE should also win RMSE in high-Δτ subgroups where bias dominates variance
conclusion: success
spec.command: python run_hetero_tau.py
metrics: {
  "dgp": "heterogeneous-tau",
  "N": 5000,
  "P_Z1": 0.652,
  "K": 4,
  "subgroups": [
    "False_medium",
    "False_short",
    "True_medium",
    "True_short"
  ],
  "delta_tau": {
    "False_medium": 0.1,
    "False_short": 0.1,
    "True_medium": 0.3,
    "True_short": 0.6
  },
  "n_expert_sweep": [
    200,
    500,
    1000
  ],
  "mc_seeds": 50,
  "hb_method": "MAP-EB Gamma(3,1)",
  "bias_echte_wins": "3/3 budgets",
  "bias_reduction_n500": "68% vs Global (0.0099 vs 0.0314)",
  "bias_reduction_n200": "32% vs Global (0.0248 vs 0.0365)",
  "bias_reduction_n1000": "55% vs Global (0.0130 vs 0.0286)",
  "rmse_echte_wins": "0/3 aggregate",
  "rmse_true_short_n1000": {
    "global": 0.1693,
    "echte": 0.1637,
    "improvement": "-3.3%"
  },
  "rmse_true_short_z0_n1000": {
    "global": 0.2577,
    "echte": 0.2117,
    "improvement": "-17.8%"
  },
  "key_finding": "EC-HTE wins bias at all budgets. High-\u0394\u03c4 subgroup (True_short) RMSE wins at n\u2265500. Aggregate RMSE loss driven by low-\u0394\u03c4 subgroups where stratified variance cost exceeds small bias gain."
}
parent: exp-008
completed_at: 2026-05-21T23:28:08.362Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "0ebecd88-9fad-4e98-a77f-c16429d5deff"
}
```

</details>

---

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Extract exp-035 through exp-040 details",
  "usage": {
    "total_tokens": 25587,
    "tool_uses": 11,
    "duration_ms": 68410
  },
  "last_tool_name": "Bash",
  "uuid": "7f08de84-f4a9-44da-9b3a-547f5b14ee14",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_01U4Sogv1HJBrPwjA9Q6gVk7`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nfor eid in ['exp-035', 'exp-036', 'exp-037', 'exp-038', 'exp-039', 'exp-040']:\n    e = exps[eid]\n    print('='*80)\n    print(f'EXPERIMENT: {eid}')\n    print(f'status: {e.get(\\\"status\\\")}')\n    print(f'hypothesis: {e.get(\\\"hypothesis\\\")}')\n    print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n    if 'spec' in e:\n        spec = e['spec']\n        print(f'spec.command: {spec.get(\\\"command\\\")}')\n    if 'results' in e and e['results']:\n        print(f'results: {json.dumps(e[\\\"results\\\"], indent=2)}')\n    if 'metrics' in e and e['metrics']:\n        print(f'metrics: {json.dumps(e[\\\"metrics\\\"], indent=2)}')\n    shown = {'status','hypothesis','conclusion','created_at','updated_at','spec','results','metrics','retry_count'}\n    for k in e:\n        if k not in shown:\n            val = e[k]\n            if val is not None and val != '' and val != [] and val != {}:\n                print(f'{k}: {json.dumps(val, indent=2) if isinstance(val, (dict,list)) else val}')\n\" 2>&1",
  "description": "Extract exp-035 through exp-040 details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "6768565d-add1-4d45-9614-86b84b03cbda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018j1PifMyPQLtZ4taXCWN9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 22213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3005,
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

_source line 73 · 2026-05-24T04:30:51.375Z_

<details><summary>↩ Tool result · `toolu_01U4Sogv1HJBrPwjA9Q6gVk7`</summary>

```text
================================================================================
EXPERIMENT: exp-035
status: DONE
hypothesis: EC-HTE with asymmetric CM estimation (full 2x2 FPR/FNR) maintains coverage >=93% under realistic 7:1 FPR/FNR ratios (simulating GPT-4.1 on Civil Comments), and outperforms the symmetric assumption (FPR=FNR) in both RMSE and coverage.
conclusion: success
spec.command: python3 exp035_asymmetric_cm.py
metrics: {
  "source": "results/exp_asymmetric_cm_summary.csv",
  "echte_asym_abs_bias": 0.057,
  "echte_asym_rmse": 0.0735,
  "echte_asym_coverage": 0.945,
  "echte_sym_abs_bias": 0.0618,
  "echte_sym_rmse": 0.0831,
  "echte_sym_coverage": 0.93,
  "global_asym_abs_bias": 0.0609,
  "global_asym_coverage": 0.915,
  "global_sym_abs_bias": 0.0629,
  "global_sym_coverage": 0.915,
  "naive_abs_bias": 0.0592,
  "naive_coverage": 0.87,
  "oracle_abs_bias": 0.0454,
  "oracle_coverage": 0.943,
  "asym_vs_sym_echte_rmse_delta": -0.0096,
  "asym_vs_sym_echte_cov_delta": 0.015,
  "s1_echte_asym_cov": 0.93,
  "s1_echte_sym_cov": 0.91,
  "key_finding": "EC-HTE asymmetric achieves 94.5% coverage (vs 93.0% symmetric) under 7:1 FPR/FNR ratio. RMSE improved 11.5% (0.0831\u21920.0735). Asymmetric formula essential for high FPR/FNR ratios. s1 (high-error) coverage: 93.0% asymmetric vs 91.0% symmetric."
}
completed_at: 2026-05-23T01:41:52.292Z
================================================================================
EXPERIMENT: exp-036
status: DONE
hypothesis: Bootstrap SE (B=200, re-estimating CM + re-fitting CF per bootstrap) can close the CausalForest under-coverage gap (91% vs nominal 95%) by properly accounting for CM estimation uncertainty that plug-in SE ignores.
conclusion: success
spec.command: python3 exp036_bootstrap_se.py
metrics: {
  "source": "results/exp_bootstrap_se_v2_summary.csv",
  "note": "v2 with n_estimators=200 (fixes v1 n_estimators=48 artifact)",
  "plugin_coverage": 0.9375,
  "bootstrap_coverage": 0.95,
  "oracle_coverage": 0.9,
  "coverage_improvement": 0.0125,
  "plugin_se_mean": 0.073,
  "bootstrap_se_mean": 0.083,
  "se_ratio_boot_over_plugin": 1.154,
  "s0_plugin_cov": 0.95,
  "s0_bootstrap_cov": 0.925,
  "s1_plugin_cov": 0.925,
  "s1_bootstrap_cov": 0.975,
  "s1_se_ratio": 1.222,
  "n_mc": 20,
  "n_bootstrap": 100,
  "n_estimators": 200,
  "runtime_sec": 1716,
  "key_finding": "With correct n_estimators=200, plugin SE already near-nominal (93.8%). Bootstrap provides modest improvement to exact 95.0%. v1 '81.7% \u2192 94.2%' gap was artifact of n_estimators=48."
}
completed_at: 2026-05-23T02:32:12.942Z
================================================================================
EXPERIMENT: exp-037
status: DONE
hypothesis: Temperature scaling reduces per-subgroup misclassification rates but does NOT eliminate heterogeneity (Δπ shrinks from 0.20 to 0.07 but remains nonzero), so EC-HTE is still necessary post-calibration. Calibrated+EC-HTE should achieve the best coverage.
conclusion: success
spec.command: python3 exp037_calibration.py
metrics: {
  "source": "results/exp_calibration_summary.csv",
  "calibrated_echte_abs_bias": 0.0554,
  "calibrated_echte_coverage": 0.965,
  "calibrated_global_abs_bias": 0.055,
  "calibrated_global_coverage": 0.963,
  "calibrated_naive_abs_bias": 0.051,
  "calibrated_naive_coverage": 0.912,
  "uncalibrated_echte_abs_bias": 0.0641,
  "uncalibrated_echte_coverage": 0.938,
  "uncalibrated_global_abs_bias": 0.0695,
  "uncalibrated_global_coverage": 0.92,
  "uncalibrated_naive_abs_bias": 0.0634,
  "uncalibrated_naive_coverage": 0.84,
  "oracle_abs_bias": 0.0431,
  "oracle_coverage": 0.963,
  "delta_pi_uncalibrated": 0.2,
  "delta_pi_calibrated": 0.07,
  "key_finding": "Calibration reduces \u0394\u03c0 from 0.20 to 0.07 and improves naive coverage (84.0%\u219291.2%) but doesn't reach nominal 95%. Calibrated+EC-HTE achieves best coverage (96.5%) \u2014 EC-HTE corrects residual heterogeneity post-calibration. Calibrated+Naive still under-covers by 3.8pp. EC-HTE and calibration are complementary, not substitutes."
}
completed_at: 2026-05-23T01:42:03.462Z
================================================================================
EXPERIMENT: exp-038
status: DONE
hypothesis: When true CATE is small (τ(0)<0.05), global correction's over-correction bias exceeds the true effect magnitude, causing sign reversal in CATE estimates — converting beneficial treatments into apparently harmful ones. EC-HTE's per-subgroup correction never causes sign reversal.
conclusion: success
spec.command: python policy_reversal_sweep.py
metrics: {
  "reversal_pct_tau001": 31,
  "reversal_pct_tau003": 14.9,
  "reversal_pct_tau005": 6.1,
  "reversal_pct_tau010": 0,
  "ec_hte_reversal_pct": 0,
  "worst_combo": "tau=0.01, delta_misclass=0.19 \u2192 42.9%"
}
completed_at: 2026-05-23T15:54:44.973Z
================================================================================
EXPERIMENT: exp-039
status: DONE
hypothesis: EC-HTE dominates at K=2/4 (bias reduction 5-7×) but degrades at K=8 with fixed n_expert=250 (~31 labels/subgroup), establishing K=8 as a scalability boundary where per-subgroup CM estimation variance exceeds bias correction gains.
conclusion: success
spec.command: python exp030_k8_subgroups.py
metrics: {
  "K2_echte_bias": 0.008,
  "K2_echte_rmse": 0.089,
  "K2_echte_cov": 0.938,
  "K4_echte_bias": 0.012,
  "K4_echte_rmse": 0.12,
  "K4_echte_cov": 0.956,
  "K8_echte_bias": 0.183,
  "K8_echte_rmse": 0.34,
  "K8_echte_cov": 0.956,
  "K8_global_rmse": 0.168
}
completed_at: 2026-05-23T15:55:15.899Z
================================================================================
EXPERIMENT: exp-040
status: DONE
hypothesis: EC-HTE is robust to moderate treatment-dependent misclassification (γ_T≤0.05, coverage ≥89.7%) but degrades at γ_T≥0.10 because per-subgroup CM estimates become biased when expert sample treatment composition doesn't match the full sample.
conclusion: success
spec.command: python exp_treatment_dep_misclass.py
metrics: {
  "gamma0_cov": 0.945,
  "gamma0_rmse": 0.075,
  "gamma005_cov": 0.897,
  "gamma005_rmse": 0.092,
  "gamma010_cov": 0.75,
  "gamma010_rmse": 0.133,
  "gamma015_cov": 0.525,
  "gamma015_rmse": 0.177,
  "gamma020_cov": 0.37,
  "gamma020_rmse": 0.224,
  "breakeven_gamma": 0.1
}
completed_at: 2026-05-23T15:55:16.698Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "1938094a-c018-45e3-9858-205d80104ec6"
}
```

</details>

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Find keyword-matching experiments among the remaining ones",
  "usage": {
    "total_tokens": 28601,
    "tool_uses": 12,
    "duration_ms": 82688
  },
  "last_tool_name": "Bash",
  "uuid": "617ad761-a583-4917-90cb-f5aa289cca25",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_018xVy2jAmBKEocqPdrP8uFw`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nalready_shown = {'exp-001','exp-002','exp-003','exp-008','exp-019','exp-023','exp-035','exp-036','exp-037','exp-038','exp-039','exp-040'}\nfor eid in sorted(exps.keys()):\n    if eid in already_shown:\n        continue\n    e = exps[eid]\n    hyp = e.get('hypothesis','')\n    conc = e.get('conclusion','')\n    status = e.get('status','')\n    metrics = e.get('metrics',{})\n    # Check for keywords\n    text = json.dumps(e).lower()\n    keywords = ['stance', 'sign_reversal', 'sign reversal', 'bias_identity', 'diagnostic', 'causal_forest', 'causal forest', 'r_learner', 'r-learner', 'r learner', 'hatespeech', 'hate_speech', 'hate speech', 'asymmetric', 'amplification']\n    matched = [k for k in keywords if k in text]\n    if matched:\n        print('='*80)\n        print(f'EXPERIMENT: {eid} [MATCHED: {matched}]')\n        print(f'status: {status}')\n        print(f'hypothesis: {hyp}')\n        print(f'conclusion: {conc}')\n        if metrics:\n            print(f'metrics: {json.dumps(metrics, indent=2)}')\n        shown = {'status','hypothesis','conclusion','created_at','updated_at','spec','results','metrics','retry_count'}\n        for k in e:\n            if k not in shown:\n                val = e[k]\n                if val is not None and val != '' and val != [] and val != {}:\n                    print(f'{k}: {json.dumps(val, indent=2) if isinstance(val, (dict,list)) else val}')\n\" 2>&1",
  "description": "Find keyword-matching experiments among the remaining ones"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "9ffe2398-cfc8-4508-8749-ada81c7fe3e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5tU54GibSdRy4gGZcVqf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3012,
      "cache_read_input_tokens": 25218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3012,
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

_source line 76 · 2026-05-24T04:31:05.586Z_

<details><summary>↩ Tool result · `toolu_018xVy2jAmBKEocqPdrP8uFw`</summary>

```text
================================================================================
EXPERIMENT: exp-004 [MATCHED: ['hate_speech', 'hate speech']]
status: DONE
hypothesis: On real hate speech data (UC Berkeley), LLM annotation of dehumanization level exhibits text-feature-based misclassification heterogeneity (e.g., by target group type, text length, presence of explicit language), and EC-HTE subgroup-stratified correction produces qualitatively different CATE distributions compared to global correction — demonstrating the practical relevance of the bias mechanism with text-feature subgroups consistent with the TweetEval experiment design
conclusion: success
metrics: {
  "dataset": "UC Berkeley Measuring Hate Speech",
  "n_comments": 2496,
  "valid_annotations": 2496,
  "subgroups": {
    "plat0_long": 624,
    "plat0_short": 624,
    "plat23_long": 624,
    "plat23_short": 624
  },
  "subgroup_type": "text features (platform_group \u00d7 text_length)",
  "delta_pi": 0.117,
  "global_FPR": 0.139,
  "global_FNR": 0.533,
  "misclass_rates": {
    "plat0_long": 0.266,
    "plat0_short": 0.337,
    "plat23_long": 0.303,
    "plat23_short": 0.383
  },
  "avg_abs_bias": {
    "naive": 0.21,
    "global": 0.273,
    "ec_hte": 0.313
  },
  "cate_comparison": "EC-HTE does not outperform global on avg |bias| \u2014 high FNR (~53%) and wide CIs limit correction effectiveness on this dataset",
  "key_finding": "\u0394\u03c0=0.117 confirms real-world misclassification heterogeneity across text-feature subgroups. High global FNR (53%) indicates LLM severely under-classifies dehumanization. CATE correction comparison inconclusive due to wide bootstrap CIs."
}
completed_at: 2026-05-21T10:59:47.756Z
notes: Δπ=0.117 confirms subgroup-varying misclassification in real hate speech data. However, EC-HTE correction fails (|bias| 0.313 > Global 0.273 > Naive 0.210) due to extreme baseline FNR=53.3%. This identifies a classifier quality threshold as a boundary condition for EC-HTE: when P(Z_hat=1|Z_true=1) ≈ 0.5 (near-random for positive class), confusion matrix inversion amplifies noise regardless of stratification.
================================================================================
EXPERIMENT: exp-005 [MATCHED: ['diagnostic']]
status: DONE
hypothesis: signed product (π̄−π_s)×Δτ 可作为诊断准则预测 global correction 是否在特定子群中反而加偏（debiasing hurts），子群水平 AUC 应显著高于随机（>0.7）
conclusion: success
metrics: {
  "subgroup_level_auc": 0.833,
  "subgroup_correlation": 0.86,
  "setting_level_auc": 0.49,
  "low_pi_hurt_pct": 84.6,
  "high_pi_hurt_pct": 15.4,
  "theory_alignment": "consistent with exp-002 formula"
}
completed_at: 2026-05-21T00:12:51.199Z
================================================================================
EXPERIMENT: exp-011 [MATCHED: ['causal_forest']]
status: DONE
hypothesis: EC-HTE correction 在 CausalForestDML 上复现与 diff-in-means 一致的改善模式：global correction 在低误分类子群加偏（debiasing hurts），stratified correction 修复偏差同时保持 CATE 估计精度
conclusion: success
metrics: {
  "n_mc": 100,
  "n_configs": 8,
  "total_rows": 144,
  "runtime_min": 35,
  "methods": [
    "naive_forest",
    "global_forest",
    "ec_hte_forest"
  ],
  "mean_abs_bias": {
    "naive_forest": 0.1558,
    "global_forest": 0.1073,
    "ec_hte_forest": 0.0608
  },
  "mean_rmse": {
    "naive_forest": 0.1782,
    "global_forest": 0.1659,
    "ec_hte_forest": 0.2289
  },
  "debiasing_hurts_cases": 9,
  "debiasing_hurts_max_ratio": 5.9,
  "debiasing_hurts_detail": "K=4/extreme/sg0: global 5.9x worse than naive",
  "k2_n500_ec_hte_bias_range": "0.004-0.013 (near zero)",
  "k2_n500_global_bias_range": "0.033-0.109 (still biased)",
  "pattern_consistent_with_diff_in_means": true,
  "claim2_validated": true
}
completed_at: 2026-05-21T02:32:33.894Z
================================================================================
EXPERIMENT: exp-013 [MATCHED: ['amplification']]
status: DONE
hypothesis: EC-HTE (especially HB) degrades significantly at n_expert=50/K=4 because per-subgroup CM estimation with ~12 expert labels per subgroup is too noisy, causing RMSE to substantially exceed global correction — validating the budget threshold claim in the paper
conclusion: success
metrics: {
  "config": "K=4/extreme/n_expert=50",
  "n_expert_per_K": 12.5,
  "hb_method": "EB (Empirical Bayes, not Gibbs \u2014 conservative estimate for boundary condition)",
  "avg_rmse_naive": 0.109,
  "avg_rmse_global": 0.14,
  "avg_rmse_mle": 0.28,
  "avg_rmse_eb": 0.292,
  "worst_subgroup": "A(pi=0.30) EB RMSE=0.62",
  "amplification_max": "4.4x (A/EB vs global)",
  "threshold_confirmed": "n_expert/K=12.5 < 25",
  "naive_beats_all": true,
  "debiasing_hurts_D": "Naive bias=0.001, Global bias=0.110 \u2014 extreme over-correction in lowest-error subgroup"
}
completed_at: 2026-05-21T07:29:18.249Z
================================================================================
EXPERIMENT: exp-014 [MATCHED: ['asymmetric']]
status: DONE
hypothesis: The bias decomposition product structure (delta_s * delta_tau) persists under asymmetric misclassification (FPR != FNR), and EC-HTE subgroup-stratified correction remains effective — the symmetric assumption A2 is sufficient for the qualitative insight but not necessary for EC-HTE to work
conclusion: success
metrics: {
  "configs": 3,
  "asymmetric_configs": [
    "balanced(FPR=0.15,FNR=0.25)",
    "fpr_dominant(FPR=0.30,FNR=0.10)",
    "fnr_dominant(FPR=0.10,FNR=0.30)"
  ],
  "delta_tau_grid": [
    0,
    0.1,
    0.2,
    0.3,
    0.5
  ],
  "n_mc": 100,
  "N": 5000,
  "n_expert": 250,
  "r2_analytic_vs_mc": 0.992,
  "product_structure_cv": "~1e-16 (exact)",
  "product_structure_confirmed": true,
  "a2_not_required": true,
  "ec_hte_avg_abs_bias": 0.006,
  "ec_hte_avg_rmse": 0.033,
  "ec_hte_avg_coverage": 0.9,
  "global_avg_abs_bias": 0.025,
  "global_avg_rmse": 0.04,
  "global_avg_coverage": 0.78,
  "naive_avg_abs_bias": 0.025,
  "naive_avg_rmse": 0.039,
  "naive_avg_coverage": 0.87,
  "bias_reduction_vs_global": "4.2x",
  "coverage_improvement_vs_global": "+12pp",
  "latex_derivation_included": true,
  "key_finding": "Product structure bias = \u0394\u03c4\u00b7[B_s]_{z,1} holds exactly under asymmetric misclassification. A2 (symmetric) assumption is NOT required. EC-HTE dominates with 4.2x bias reduction."
}
completed_at: 2026-05-21T07:45:03.268Z
================================================================================
EXPERIMENT: exp-015 [MATCHED: ['asymmetric']]
status: DONE
hypothesis: EC-HTE maintains bias correction under realistic asymmetric confusion matrices estimated from actual GPT-4.1 annotations on TweetEval (Δπ=0.098, FNR/FPR ratio up to 10×)
conclusion: negative
metrics: {
  "n_mc": 100,
  "n_expert_grid": [
    100,
    250,
    500
  ],
  "subgroups": 4,
  "real_cm_source": "exp-012 GPT-4.1 pilot",
  "cm_params": {
    "S0_False_medium": {
      "FPR": 0.054,
      "FNR": 0.526,
      "weight": 0.38
    },
    "S1_False_short": {
      "FPR": 0.101,
      "FNR": 0.3,
      "weight": 0.22
    },
    "S2_True_short": {
      "FPR": 0.143,
      "FNR": 0.308,
      "weight": 0.14
    },
    "S3_True_medium": {
      "FPR": 0.194,
      "FNR": 0.222,
      "weight": 0.25
    }
  },
  "delta_pi": 0.098,
  "P_Z1": 0.18,
  "rmse_n100": {
    "naive": 0.123,
    "global": 0.263,
    "hb": 0.784
  },
  "rmse_n250": {
    "naive": 0.123,
    "global": 0.232,
    "hb": 0.411
  },
  "rmse_n500": {
    "naive": 0.123,
    "global": 0.196,
    "hb": 0.26
  },
  "coverage_n100": {
    "naive": 0.868,
    "global": 0.922,
    "hb": 0.744
  },
  "coverage_n250": {
    "naive": 0.868,
    "global": 0.908,
    "hb": 0.828
  },
  "coverage_n500": {
    "naive": 0.873,
    "global": 0.885,
    "hb": 0.89
  },
  "hb_worse_than_global_all_n": true,
  "root_cause": "S0 FNR=0.526 makes CM row near-uniform [0.526, 0.474], inversion amplifies noise. Combined with P(Z=1)=0.18, too few Z=1 expert labels per subgroup for reliable per-subgroup CM estimation.",
  "key_finding": "EC-HTE fails under realistic asymmetric CMs when any subgroup has FNR\u22480.5 (near-random for positive class). This is consistent with exp-004 (FNR=53%) and exp-013 (boundary at n_expert/K=12.5). Identifies classifier quality threshold as honest limitation."
}
parent: exp-003
completed_at: 2026-05-21T13:02:02.880Z
notes: negative: EC-HTE fails under realistic asymmetric CMs from actual GPT-4.1 annotations. HB RMSE 1.3-3.0× worse than global across all n_expert. Root cause: S0 (38% weight) FNR=0.526 → CM row near-uniform → inversion amplifies noise. Converges with exp-004 (FNR=53%) and exp-013 (n_expert/K boundary). Establishes classifier quality threshold as second applicability condition alongside budget threshold.
================================================================================
EXPERIMENT: exp-016 [MATCHED: ['diagnostic', 'asymmetric']]
status: DONE
hypothesis: EC-HTE succeeds under realistic asymmetric CMs when worst-subgroup FNR is well below 0.5 — using gpt-4o (or best-FNR model from exp-008) real per-subgroup FPR/FNR on TweetEval, HB correction outperforms global at n_expert≥250
conclusion: negative
metrics: {
  "model_selected": "gpt-3.5-turbo",
  "worst_subgroup_fnr": 0.211,
  "worst_subgroup_fpr": 0.393,
  "rmse_n100": {
    "naive": 0.127,
    "global": 0.265,
    "hb": 0.93
  },
  "rmse_n250": {
    "naive": 0.127,
    "global": 0.221,
    "hb": 0.527
  },
  "rmse_n500": {
    "naive": 0.127,
    "global": 0.199,
    "hb": 0.322
  },
  "coverage_n100": {
    "naive": 0.784,
    "global": 0.893,
    "hb": 0.769
  },
  "coverage_n250": {
    "naive": 0.784,
    "global": 0.922,
    "hb": 0.843
  },
  "coverage_n500": {
    "naive": 0.784,
    "global": 0.939,
    "hb": 0.894
  },
  "hb_worse_than_global_all_n": true,
  "vs_exp015": "exp-016 HB RMSE even worse than exp-015 despite lower FNR, because high FPR variance (0.14-0.39) makes subgroup CM estimation harder",
  "bright_spot": "S0/z=1 at n=500: HB |bias|=0.193 < Global |bias|=0.252 \u2014 one case where subgroup-specific correction helps",
  "root_cause": "High FPR variance across subgroups (0.143-0.393) + P(Z=1)=0.18 \u2192 insufficient Z=1 expert labels per subgroup. Lower FNR alone does not fix the fundamental sample-size constraint.",
  "key_finding": "Neither low-FNR (gpt-3.5-turbo) nor low-FPR (GPT-4.1) real CMs enable EC-HTE to beat global. The bottleneck is P(Z=1)=0.18 creating too few positive-class expert labels per subgroup for reliable CM estimation."
}
parent: exp-015
completed_at: 2026-05-21T13:40:37.757Z
notes: HB EC-HTE fails under gpt-3.5-turbo real asymmetric CMs despite worst-FNR=0.211 (<0.4). Root cause: FPR≈0.4 + P(Z=1)=0.18 class imbalance → mixing matrix ill-conditioned. Demonstrates that CM condition number alone is insufficient; class-prior-adjusted mixing matrix condition is the true diagnostic.
================================================================================
EXPERIMENT: exp-017 [MATCHED: ['causal_forest', 'r-learner']]
status: DONE
hypothesis: EC-HTE corrected pseudo-outcomes are compatible with R-learner, achieving similar bias reduction as with CausalForest
conclusion: success
metrics: {
  "n_mc": 50,
  "config": "K=2/extreme/n_expert=500",
  "rlearner_results": {
    "naive": {
      "avg_abs_bias": 0.121,
      "rmse": 0.139,
      "coverage": 0.47
    },
    "global": {
      "avg_abs_bias": 0.098,
      "rmse": 0.123,
      "coverage": 0.71
    },
    "ec_hte": {
      "avg_abs_bias": 0.013,
      "rmse": 0.08,
      "coverage": 0.92
    },
    "oracle": {
      "avg_abs_bias": 0.006,
      "rmse": 0.056,
      "coverage": 0.94
    }
  },
  "causal_forest_comparison": {
    "naive": {
      "avg_abs_bias": 0.125,
      "rmse": 0.143,
      "coverage": 0.46
    },
    "global": {
      "avg_abs_bias": 0.104,
      "rmse": 0.129,
      "coverage": 0.65
    },
    "ec_hte": {
      "avg_abs_bias": 0.008,
      "rmse": 0.082,
      "coverage": 0.91
    }
  },
  "ec_hte_bias_reduction_vs_naive": "9.3x (R-learner) vs 15.6x (CausalForest)",
  "pattern_consistent": true,
  "key_finding": "EC-HTE correction generalizes across CATE estimators. R-learner ec_hte achieves |bias|=0.013 (vs naive 0.121), 92% coverage \u2014 closely matching CausalForest pattern."
}
parent: exp-011
completed_at: 2026-05-21T13:52:52.889Z
notes: EC-HTE correction generalizes to R-learner: |Bias| 0.121→0.013 (89% reduction), coverage 0.47→0.92. Consistent with CausalForest results (|Bias|=0.008, coverage 0.91). Validates estimator-agnostic upstream correction.
================================================================================
EXPERIMENT: exp-024 [MATCHED: ['bias_identity', 'asymmetric']]
status: DONE
hypothesis: Theorem 1 bias decomposition identity (asymmetric version: bias(z,s) = Δτ·[M_global⁻¹ M_s - I]_{z,1}) achieves R²>0.95 when evaluated with real per-subgroup FPR/FNR from 7 LLMs (GPT-3.5-turbo, GPT-4o, GPT-4o-mini, GPT-4-turbo, GPT-4.1, GPT-5.4 on Civil Comments; Llama-3.1-8B, Qwen-2.5-7B, Mistral-7B, Gemma-2-9B on TweetEval), demonstrating the bias mechanism holds under empirically-observed asymmetric confusion matrices
conclusion: success
metrics: {
  "R2_overall": 0.975,
  "data_sources": [
    "exp023_confusion_matrices.json",
    "c1_multi_llm/*_cm_profile.md"
  ],
  "n_llm_dataset_combos": 11,
  "output_files": [
    "results/exp_realcm_bias_identity.csv",
    "results/exp_realcm_summary.csv"
  ]
}
parent: exp-002,exp-014
completed_at: 2026-05-22T13:41:36.194Z
================================================================================
EXPERIMENT: exp-025 [MATCHED: ['diagnostic']]
status: DONE
hypothesis: Among 7 LLMs with real per-subgroup CMs, those satisfying diagnostic conditions (κ≤1.25 and max(FPR,FNR)<0.5 for all subgroups) will show EC-HTE (HB) outperforming Global correction in RMSE and coverage, while those violating conditions will show EC-HTE degradation — validating Proposition 3 diagnostic as a practical screening tool
conclusion: success
metrics: {
  "screening": "0/16 combos pass all conditions (\u03ba\u22641.25 bottleneck)",
  "oracle_screening": "HB wins 41/52 comparisons on aggregate RMSE",
  "hb_vs_mle": "HB beats Strat MLE in 52/52 comparisons",
  "best_case": "Qwen2.5-7B K=4 n=500 Z=0: \u0394RMSE=-0.0075",
  "open_source_llms": "All 4 (Llama/Qwen/Mistral/Gemma) HB wins 32/32 on TweetEval",
  "hb_loses": "gpt-3.5-turbo/TweetEval (high FPR asymmetry), gpt-4o/CivilComments (low P(Z=1)=0.3)",
  "output_files": [
    "results/exp_screening.csv",
    "results/exp_oracle_screening.csv",
    "results/exp_positive_scenario_summary.md"
  ]
}
parent: exp-015,exp-016
completed_at: 2026-05-22T13:41:37.612Z
================================================================================
EXPERIMENT: exp-027b [MATCHED: ['amplification']]
status: PREPARING
hypothesis: Under K=2 extreme (π=[0.05,0.25], n_expert=250) — the exact configuration producing 83-85% coverage in the paper — CausalForest oracle coverage with true C_s will determine whether the gap is from CF inherent SE under-calibration or M⁻¹ amplification of CM estimation error
conclusion: success
metrics: {
  "dgp": "K=2 extreme, \u03c0=[0.05,0.25], N=5000, n_expert=250, 100 MC runs",
  "oracle_true_Z": {
    "coverage": 0.94,
    "bias": 0.0023,
    "rmse": 0.056
  },
  "echte_true_CM": {
    "coverage": 0.94,
    "bias": 0.0027,
    "rmse": 0.073
  },
  "echte_estimated_CM": {
    "coverage": 0.925,
    "bias": 0.0044,
    "rmse": 0.079
  },
  "global_true_CM": {
    "coverage": 0.885,
    "bias": 0.045,
    "rmse": 0.083
  },
  "global_estimated_CM": {
    "coverage": 0.883,
    "bias": 0.045,
    "rmse": 0.085
  },
  "naive": {
    "coverage": 0.828,
    "bias": 0.046,
    "rmse": 0.077
  },
  "key_finding": "K=2: Oracle 94%, EC-HTE true CM 94%, EC-HTE estimated CM 92.5%. CF SE is well-calibrated. 83-85% coverage in paper comes from Naive (uncorrected misclassification bias), NOT from CF SE under-calibration. EC-HTE restores near-nominal coverage.",
  "output_file": "results/exp_cf_oracle_coverage_k2.csv"
}
parent: exp-027
================================================================================
EXPERIMENT: exp-027c [MATCHED: ['asymmetric', 'amplification']]
status: DONE
hypothesis: Under MF2's exact DGP (K=2, π=[0.05,0.25], τ(0)=0.10, τ(1)=0.40, n_expert=250), Oracle CF coverage will reveal whether the 83% vs 92.5% discrepancy between MF2 and exp-027b is due to the harder CATE specification (τ shift) causing CF SE under-calibration, or due to other implementation differences
conclusion: success
metrics: {
  "dgp": "MF2 exact DGP: K=2, \u03c0=[0.05,0.25], \u03c4(0)=0.10, \u03c4(1)=0.40, N=5000, n_expert=250, 100 MC",
  "oracle_true_Z": {
    "coverage": 0.96,
    "bias": 0.077,
    "rmse": 0.091,
    "mean_se": 0.09
  },
  "echte_true_CM": {
    "coverage": 0.913,
    "bias": 0.103,
    "rmse": 0.112,
    "mean_se": 0.114
  },
  "echte_estimated_CM": {
    "coverage": 0.923,
    "bias": 0.1,
    "rmse": 0.111,
    "mean_se": 0.119
  },
  "global_true_CM": {
    "coverage": 0.95,
    "bias": 0.107,
    "rmse": 0.114,
    "mean_se": 0.107
  },
  "global_estimated_CM": {
    "coverage": 0.943,
    "bias": 0.105,
    "rmse": 0.114,
    "mean_se": 0.109
  },
  "naive": {
    "coverage": 0.773,
    "bias": 0.12,
    "rmse": 0.125,
    "mean_se": 0.087
  },
  "key_finding": "DGP difference NOT the source of 83% vs 92.5% gap. Per-subgroup EC-HTE coverage ~92.25% in both 027b and 027c. The 83% in MF2 is an aggregate mixing effect: low-misclass subgroup (\u03c0=0.05) has 83% coverage while high-misclass subgroup (\u03c0=0.25) has 99%. M\u207b\u00b9 creates asymmetric SE amplification across subgroups.",
  "comparison_027b": {
    "oracle": "94.0% \u2192 96.0%",
    "echte_est": "92.5% \u2192 92.25%",
    "conclusion": "Nearly identical per-subgroup coverage despite different \u03c4 values"
  },
  "output_file": "results/exp_cf_oracle_coverage_mf2dgp.csv"
}
parent: exp-027b
completed_at: 2026-05-22T14:37:04.432Z
================================================================================
EXPERIMENT: exp-028 [MATCHED: ['diagnostic', 'asymmetric']]
status: DONE
hypothesis: The Proposition 3 symmetric diagnostic (|δ_s|/((1-2π̄)·π_s) > 1) fails on real asymmetric LLM CMs (AUC=0.21-0.38) because it assumes FPR=FNR. An asymmetric diagnostic using B_s = M_global⁻¹·M_s - I will recover predictive power (AUC≥0.75) by correctly capturing the directional bias structure of asymmetric confusion matrices.
conclusion: negative
metrics: {
  "overall_symmetric_auc": 0.626,
  "overall_asymmetric_auc": 0.611,
  "k4_only": {
    "symmetric_auc_range": "0.0-1.0",
    "asymmetric_auc_range": "0.0-1.0",
    "perfect_auc_combos": [
      "Llama/TweetEval",
      "Qwen/TweetEval",
      "Mistral/TweetEval",
      "gpt-4o/TweetEval",
      "gpt-3.5-turbo/TweetEval(asym only)",
      "gpt-4.1/TweetEval(asym only)"
    ]
  },
  "k2_all_auc_zero": true,
  "z0_z1_identical": true,
  "theoretical_insight": "For DIM, |B_s[0,1]|=|B_s[1,1]| (column-stochastic M). Asymmetric diagnostic degenerates to symmetric because DIM CATE bias depends on \u03b4_s = (FPR_s+FNR_s)/2 - \u03c0\u0304, not on FPR/FNR individually.",
  "output_files": [
    "results/exp_asymmetric_diagnostic_auc.csv",
    "results/exp_asymmetric_diagnostic_auc_summary.csv"
  ]
}
completed_at: 2026-05-22T16:13:50.285Z
================================================================================
EXPERIMENT: exp-034 [MATCHED: ['sign_reversal']]
status: DONE
hypothesis: F-L scalar correction (tau_obs/(1-2*pi_bar)) predicts bias direction incorrectly under subgroup heterogeneity because it uses a single global scaling factor that over-corrects low-error subgroups and under-corrects high-error subgroups. EC-HTE's CM inversion handles the sign-reversal correctly.
conclusion: success
metrics: {
  "source": "results/exp_fl_comparison_summary.csv",
  "fl_scalar_abs_bias": 0.0909,
  "fl_scalar_rmse": 0.1161,
  "fl_scalar_coverage": 0.85,
  "fl_per_subgroup_abs_bias": 0.112,
  "fl_per_subgroup_rmse": 0.1582,
  "fl_per_subgroup_coverage": 0.838,
  "echte_abs_bias": 0.0643,
  "echte_rmse": 0.0858,
  "echte_coverage": 0.953,
  "global_cm_abs_bias": 0.0643,
  "global_cm_rmse": 0.0806,
  "global_cm_coverage": 0.938,
  "naive_abs_bias": 0.0621,
  "naive_coverage": 0.858,
  "oracle_abs_bias": 0.0454,
  "oracle_coverage": 0.943,
  "sign_reversal": "F-L Scalar: s0=+0.073 s1=+0.068, both positive (no sign-reversal). F-L Per-Subgroup: s0=+0.024 s1=+0.160. EC-HTE: s0=+0.006 s1=+0.001 (near-zero bias both subgroups)",
  "key_finding": "F-L scalar and F-L per-subgroup both WORSE than naive on aggregate |bias|. F-L scalar over-corrects s0 (bias +0.073 vs naive +0.005). F-L per-subgroup dramatically over-corrects s1 (bias +0.160). EC-HTE achieves near-zero per-subgroup bias with nominal coverage (95.3%). CM inversion fundamentally different from F-L scalar rescaling."
}
completed_at: 2026-05-23T01:41:40.218Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "8374e0f6-ba4b-4891-b021-3791f8d362da"
}
```

</details>

---

### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Extract all remaining experiments",
  "usage": {
    "total_tokens": 37511,
    "tool_uses": 13,
    "duration_ms": 97505
  },
  "last_tool_name": "Bash",
  "uuid": "86ad356e-a253-4c42-971c-b904fad0c812",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01466UnDNcxbMt6uBPfz25PL`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nalready_shown = {'exp-001','exp-002','exp-003','exp-004','exp-005','exp-008','exp-011','exp-013','exp-014','exp-015','exp-016','exp-017','exp-019','exp-023','exp-024','exp-025','exp-027b','exp-027c','exp-028','exp-034','exp-035','exp-036','exp-037','exp-038','exp-039','exp-040'}\nfor eid in sorted(exps.keys()):\n    if eid in already_shown:\n        continue\n    e = exps[eid]\n    print('='*80)\n    print(f'EXPERIMENT: {eid}')\n    print(f'status: {e.get(\\\"status\\\")}')\n    print(f'hypothesis: {e.get(\\\"hypothesis\\\",\\\"\\\")[:200]}')\n    print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n    if 'metrics' in e and e['metrics']:\n        print(f'metrics: {json.dumps(e[\\\"metrics\\\"], indent=2)}')\n    shown = {'status','hypothesis','conclusion','created_at','updated_at','spec','results','metrics','retry_count'}\n    for k in e:\n        if k not in shown:\n            val = e[k]\n            if val is not None and val != '' and val != [] and val != {}:\n                s = json.dumps(val, indent=2) if isinstance(val, (dict,list)) else str(val)\n                if len(s) > 500:\n                    s = s[:500] + '...'\n                print(f'{k}: {s}')\n\" 2>&1",
  "description": "Extract all remaining experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "2a623985-09b0-4704-bd83-aae097d30bbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G5dcBnsXsVQTJNHsXboyXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8908,
      "cache_read_input_tokens": 28230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8908,
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

_source line 79 · 2026-05-24T04:31:20.428Z_

<details><summary>↩ Tool result · `toolu_01466UnDNcxbMt6uBPfz25PL`</summary>

```text
================================================================================
EXPERIMENT: exp-006
status: DONE
hypothesis: HB partial pooling 的 RMSE 优势在小 n_expert 时最明显，存在一个 crossover point（预计 n_expert ∈ [100, 500]）使得 HB 开始系统性优于 Global correction
conclusion: success
metrics: {
  "n_mc": 100,
  "total_rows": 288,
  "runtime_min": 110,
  "grid": "n_expert=[50,100,250,500,1000,2000] \u00d7 K=[2,4] \u00d7 regime=[extreme,moderate]",
  "crossover_hb_beats_global": {
    "K2_extreme": 250,
    "K2_moderate": "never",
    "K4_extreme": 1000,
    "K4_moderate": 2000
  },
  "hb_vs_mle": "HB \u2265 MLE in 21/24 configs (87.5%; partial pooling rarely hurts in symmetric DGP)",
  "hb_best_improvement_over_mle": {
    "K4_moderate_n50_sgC": "+42.4% RMSE",
    "K4_extreme_n50_sgC": "+23.4% RMSE",
    "K4_moderate_n50_sgB": "+24.0% RMSE"
  },
  "convergence": "HB \u2248 MLE at n\u22651000 (<0.5% difference)",
  "key_finding": "Crossover depends strongly on K and regime. K=2: crossover at n=250 (practical). K=4: crossover at n=1000 (higher). HB provides consistent modest improvement over MLE via partial pooling."
}
completed_at: 2026-05-21T03:02:24.771Z
================================================================================
EXPERIMENT: exp-007
status: DONE
hypothesis: 在同时存在covariate misclassification和treatment-differential outcome error的DGP下，EC-HTE单独处理covariate error、PPCI单独处理outcome error，二者组合(EC-HTE+PPCI)能同时校正两类错误，实现最低bias和RMSE
conclusion: success
metrics: {
  "total_rows": 6912,
  "dgps": [
    "A_covariate_only",
    "B_outcome_only",
    "C_both_errors",
    "D_no_error"
  ],
  "methods": 8,
  "mc_runs": 100,
  "double_correction_fix_verified": true,
  "dgp_a_ec_hte_ppci_equals_ec_hte": true,
  "dgp_c_extreme_n250_k2": {
    "ec_hte_ppci_bias_z0": 0.005,
    "ec_hte_ppci_rmse_z0": 0.225,
    "ec_hte_bias_z0": 0.178,
    "ec_hte_rmse_z0": 0.226,
    "ppci_bias_z0": 0.004,
    "ppci_rmse_z0": 0.261,
    "naive_bias_z0": 0.251,
    "naive_rmse_z0": 0.269
  },
  "dgp_c_n500_k2": {
    "ec_hte_ppci_bias_z0": 0.005,
    "ec_hte_ppci_rmse_z0": 0.142,
    "ec_hte_bias_z0": 0.088,
    "ec_hte_rmse_z0": 0.134
  },
  "key_finding": "ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0."
}
completed_at: 2026-05-21T00:05:00.962Z
================================================================================
EXPERIMENT: exp-007b
status: DONE
hypothesis: exp-007 HB 回填：将 ec_hte 方法从 stratified_mle placeholder 替换为真正的 HB Gibbs sampler（Dirichlet-Multinomial partial pooling），验证在 4-DGP matrix 下 HB 版本的 ec_hte 和 ec_hte_ppci 是否保持或改善原 MLE 版本的结果
conclusion: killed
metrics: {
  "kill_reason": "D012: Director \u51b3\u5b9a\u653e\u5f03 HB backfill\u3002\u7406\u7531\uff1aPPCI \u8868\u6838\u5fc3 story \u662f\u4e92\u8865\u6027\uff0cHB vs MLE \u662f\u8fb9\u9645\u6539\u8fdb\uff1bexp-001 \u5df2\u9a8c\u8bc1 HB\u3002CSV \u5df2\u91cd\u547d\u540d\u4e3a .broken"
}
parent: exp-007
completed_at: 2026-05-21T04:54:53.137Z
================================================================================
EXPERIMENT: exp-010
status: DONE
hypothesis: EC-HTE with HB partial pooling degrades gracefully under subgroup misspecification: mild noise (10%) causes minimal performance loss due to shrinkage toward global, moderate noise (25%) reduces but pr
conclusion: success
metrics: {
  "n_mc": 100,
  "configs": 2,
  "noise_levels": [
    0,
    0.1,
    0.25,
    0.5
  ],
  "total_runs": 800,
  "runtime_sec": 15,
  "k2_coverage_naive": [
    0.875,
    0.877,
    0.89,
    0.897
  ],
  "k2_coverage_hb": [
    0.958,
    0.948,
    0.95,
    0.945
  ],
  "k2_coverage_global": [
    0.925,
    0.935,
    0.932,
    0.945
  ],
  "k4_coverage_naive": [
    0.904,
    0.916,
    0.909,
    0.919
  ],
  "k4_coverage_hb": [
    0.956,
    0.958,
    0.96,
    0.946
  ],
  "k4_coverage_global": [
    0.93,
    0.953,
    0.948,
    0.944
  ],
  "hb_beats_mle_all_configs": true,
  "hb_improvement_range": "+0.1% to +0.9% RMSE",
  "graceful_convergence_at_50pct": true,
  "key_finding": "Coverage is the decisive metric: naive 87-92%, EC-HTE 95-96% across all noise levels. No catastrophic failure. HB shrinkage provides automatic safeguard \u2014 converges to global at 50% noise."
}
completed_at: 2026-05-21T10:10:42.918Z
notes: EC-HTE maintains near-nominal CI coverage (≥94.5%) across all subgroup noise levels (0-50%), confirming robustness of inferential validity under misspecified subgroup structure. RMSE advantage is not observed at n_expert=500 (convergence zone per exp-006), but coverage is the decisive metric for statistical inference. At p_flip=0.50, EC-HTE gracefully converges to global correction. HB and MLE perform comparably at n=500 (expected per exp-006).
================================================================================
EXPERIMENT: exp-012
status: DONE
hypothesis: 真实 LLM（GPT-4.1）对 TweetEval sentiment 的标注存在跨子群（has_hashtag × text_length_bin）的误分类率异质性（Δπ > 0.05），为 EC-HTE 的必要性提供 empirical motivation
conclusion: success
metrics: {
  "model": "gpt-4.1-2025-04-14",
  "n_samples": 500,
  "valid_annotations": 500,
  "failed": 0,
  "accuracy_3class": 0.672,
  "accuracy_binary": 0.858,
  "subgroup_misclass_rates": {
    "hash_long": 0,
    "hash_medium": 0.2,
    "hash_short": 0.174,
    "nohash_long": 0,
    "nohash_medium": 0.102,
    "nohash_short": 0.138
  },
  "delta_pi": 0.2,
  "heterogeneity_significant": true,
  "key_finding": "Hashtag presence increases binary misclassification rate (~0.17-0.20 vs ~0.10-0.14 for non-hashtag). Delta-pi=0.200 confirms meaningful heterogeneity for EC-HTE correction.",
  "analysis_file": "results/pilot_gpt41_analysis.md"
}
log_path: results/pilot_gpt41_run.log
checkpoint_path: results/pilot_gemini_annotations.csv
completed_at: 2026-05-21T05:21:29.106Z
================================================================================
EXPERIMENT: exp-018
status: DONE
hypothesis: EC-HTE bias reduction persists under multiplicative CATE DGP (Y(1)=Y(0)*exp(tau(Z))), demonstrating robustness beyond additive treatment effect models
conclusion: success
metrics: {
  "n_mc": 50,
  "config": "K=2/extreme/n_expert=500/multiplicative",
  "dgp": "Y(1) = Y(0) * exp(tau(Z)), tau(Z=0)=0, tau(Z=1)=0.3",
  "results": {
    "oracle": {
      "avg_abs_bias": 0.031,
      "rmse": 0.038,
      "coverage": 0.96
    },
    "ec_hte": {
      "avg_abs_bias": 0.054,
      "rmse": 0.068,
      "coverage": 0.955
    },
    "global_corrected": {
      "avg_abs_bias": 0.11,
      "rmse": 0.124,
      "coverage": 0.54
    },
    "naive": {
      "avg_abs_bias": 0.135,
      "rmse": 0.142,
      "coverage": 0.435
    }
  },
  "ec_hte_rmse_reduction_vs_naive": "52%",
  "ec_hte_coverage": 0.955,
  "vs_exp001_additive": "EC-HTE RMSE 0.068 (multiplicative) vs 0.091 (additive, same config) \u2014 actually better due to larger true CATEs making relative bias smaller",
  "key_finding": "EC-HTE robust to non-additive treatment effects. 52% RMSE reduction vs naive, 95.5% coverage (target 95%). Answers Reviewer Q3."
}
parent: exp-001
completed_at: 2026-05-21T13:54:35.822Z
notes: EC-HTE robust under multiplicative CATE DGP: RMSE 0.068 (52% reduction vs naive 0.142), coverage 0.955 (nominal 0.95). Global correction inadequate (coverage 0.54). Answers Reviewer Q3 on non-additive DGP robustness.
================================================================================
EXPERIMENT: exp-020
status: DONE
hypothesis: κ=100 condition number guard provides sufficient safety margin for EC-HTE; empirical sweep will show guard rarely triggers under moderate misclassification and the exact threshold is not critical for 
conclusion: success
metrics: {
  "max_cond_number": 1.89,
  "mean_cond_number": 1.446,
  "p99_cond_number": 1.893,
  "guard_trigger_rate_all_kappa": 0,
  "rmse_hb": 0.0759,
  "rmse_global": 0.0765,
  "rmse_ratio": 1.048,
  "numerical_instability_rate": 0,
  "safety_margin_at_kappa100": "53x",
  "stress_test_near_random_max_cond": 1125.3,
  "stress_test_near_random_triggers_kappa100": true
}
parent: exp-001
completed_at: 2026-05-21T16:14:59.935Z
notes: κ sweep across {10,25,50,100,200,500,1000}: guard never triggers in moderate regime (max cond=1.89, 53× below κ=100). All κ values produce identical RMSE (HB=0.076, Global=0.077). Zero numerical instability. Stress test: guard only activates with near-random labeling (π_s≈0.4-0.5, n_expert=50, max cond=1125). κ=100 validated as safe default. Adaptive formula κ=10·√(n_expert/K) recovers κ=100 for this regime. Addresses RD2-W4.
================================================================================
EXPERIMENT: exp-021
status: DONE
hypothesis: Table 1 RMSE results are stable under doubling of MC seeds (50→100); median cell change <5% confirms 50-seed results are not artifacts of sampling variance
conclusion: success
metrics: {
  "total_cells_compared": 94,
  "median_delta_pct": 3.2,
  "max_delta_pct": 25.5,
  "cells_under_5pct": "79/94 (84%)",
  "cells_under_10pct": "93/94 (99%)",
  "outlier": "K=4/extreme/n=100/HB base (-25.5%, known numerically unstable)",
  "method_note": "EB instead of Gibbs (<0.002 CM difference, 10s vs 114min)"
}
parent: exp-001
completed_at: 2026-05-21T17:50:25.344Z
notes: 100-seed stability test for Table 1. 84% cells <5% change, 99% <10%. Only outlier: K=4/extreme/n=100/HB base (-25.5%) — known numerically unstable cell where HB overshoots (RMSE 0.71→0.53, still bad but less bad). Used EB estimator for speed (10s vs 114min Gibbs); EB-Gibbs CM difference <0.002. Non-HB methods identical. Addresses RD2-M4.
================================================================================
EXPERIMENT: exp-022
status: DONE
hypothesis: EC-HTE's hierarchical Bayes confusion matrix estimation is insensitive to Gamma hyperprior specification: varying shape∈{1,2,3,5,10} and scale∈{0.5,1,2} produces <10% RMSE variation, confirming the me
conclusion: success
metrics: {
  "rmse_range_reasonable": "6.0%",
  "rmse_range_all": "17.3%",
  "gamma31_rmse": 0.0841,
  "gamma31_rank": "8/15",
  "coverage_range": "0.925-0.938",
  "hb_beats_mle": "9/15",
  "best_config": "Gamma(1,0.5)",
  "best_rmse": 0.0825
}
parent: exp-001
completed_at: 2026-05-21T19:44:39.795Z
================================================================================
EXPERIMENT: exp-026
status: DONE
hypothesis: HB partial pooling provides substantial RMSE and coverage improvement over Stratified MLE at extreme low expert budgets (n_expert=25-75, yielding 6-18 labels per subgroup), with the gap widening as n_
conclusion: success
metrics: {
  "K2_n25": {
    "mle_rmse": 0.2562,
    "hb_rmse": 0.2689,
    "delta_pct": "+4.9%",
    "global_rmse": 0.1013
  },
  "K2_n50": {
    "mle_rmse": 0.2748,
    "hb_rmse": 0.2306,
    "delta_pct": "-16.1%",
    "global_rmse": 0.0879
  },
  "K2_n75": {
    "mle_rmse": 0.0911,
    "hb_rmse": 0.0893,
    "delta_pct": "-1.9%"
  },
  "K4_n25": {
    "mle_rmse": 0.4011,
    "hb_rmse": 0.6116,
    "delta_pct": "+52.5%",
    "global_rmse": 0.1289
  },
  "K4_n50": {
    "mle_rmse": 0.3798,
    "hb_rmse": 0.4701,
    "delta_pct": "+23.8%",
    "global_rmse": 0.1172
  },
  "K4_n75": {
    "mle_rmse": 0.2208,
    "hb_rmse": 0.2111,
    "delta_pct": "-4.4%"
  },
  "K4_n100": {
    "mle_rmse": 0.2152,
    "hb_rmse": 0.2123,
    "delta_pct": "-1.3%"
  },
  "coverage_all": ">=0.88, no catastrophic failures",
  "crossover_K2": "n_expert=50 (HB -16.1%)",
  "crossover_K4": "n_expert=75 (HB -4.4%)",
  "key_finding": "HB shrinkage advantage emerges at n\u226550 (K=2) and n\u226575 (K=4). Below these thresholds, global pooling outperforms both HB and MLE \u2014 validates budget threshold claim.",
  "mc_runs": 100,
  "output_file": "results/exp_low_budget_hb.csv"
}
parent: exp-006,exp-001
completed_at: 2026-05-22T13:41:38.543Z
================================================================================
EXPERIMENT: exp-027
status: PREPARING
hypothesis: CausalForest coverage gap (83-85% vs nominal 95%) is attributable to CF's inherent SE calibration, not CM estimation error: using true C_s (oracle CM) will produce similar ~83-85% coverage as estimate
conclusion: success
metrics: {
  "oracle_true_Z": {
    "coverage": 0.945,
    "bias": 0.0056,
    "rmse": 0.078
  },
  "echte_true_CM": {
    "coverage": 0.925,
    "bias": 0.0078,
    "rmse": 0.114
  },
  "echte_estimated_CM": {
    "coverage": 0.931,
    "bias": 0.0148,
    "rmse": 0.121
  },
  "global_true_CM": {
    "coverage": 0.913,
    "bias": 0.0371,
    "rmse": 0.11
  },
  "global_estimated_CM": {
    "coverage": 0.911,
    "bias": 0.0379,
    "rmse": 0.111
  },
  "naive": {
    "coverage": 0.883,
    "bias": 0.0447,
    "rmse": 0.095
  },
  "key_finding": "Oracle CF SE well-calibrated (94.5%). EC-HTE true CM (92.5%) \u2248 estimated CM (93.1%): CM estimation NOT the coverage gap source. ~2pp drop from Oracle to EC-HTE true CM comes from M^{-1} SE propagation, not CM estimation noise.",
  "dgp": "K=4 extreme, N=5000, n_expert=500, 100 MC runs",
  "output_file": "results/exp_cf_oracle_coverage.csv"
}
parent: exp-011
================================================================================
EXPERIMENT: exp-029
status: DONE
hypothesis: Under controlled violation of Assumption A1 (outcome-independent misclassification), EC-HTE coverage degrades gracefully as sensitivity parameter γ increases from 0 to 0.2, with the degradation curve 
conclusion: success
metrics: {
  "dgp": "K=2, pi=[0.05,0.25], tau(0)=0, tau(1)=0.3, N=5000, n_expert=250, 100 MC",
  "gamma_sweep": [
    0,
    0.05,
    0.1,
    0.15,
    0.2
  ],
  "echte_coverage": {
    "g0.00": 0.955,
    "g0.05": 0.955,
    "g0.10": 0.953,
    "g0.15": 0.948,
    "g0.20": 0.935
  },
  "echte_abs_bias": {
    "g0.00": 0.0596,
    "g0.05": 0.0593,
    "g0.10": 0.063,
    "g0.15": 0.0652,
    "g0.20": 0.0677
  },
  "global_coverage": {
    "g0.00": 0.927,
    "g0.05": 0.935,
    "g0.10": 0.938,
    "g0.15": 0.943,
    "g0.20": 0.94
  },
  "naive_coverage": {
    "g0.00": 0.877,
    "g0.05": 0.838,
    "g0.10": 0.835,
    "g0.15": 0.792,
    "g0.20": 0.795
  },
  "key_finding": "EC-HTE coverage degrades gracefully: 95.5%\u219293.5% over gamma 0\u21920.2 (\u22122.0pp). ALL correction methods maintain \u226590% coverage across all gamma. Naive degrades fastest (87.7%\u219279.5%, \u22128.2pp). At moderate violation gamma=0.1, EC-HTE coverage=95.3% (\u22120.2pp from baseline). EC-HTE |bias| increases 13.7% at gamma=0.2 but remains comparable to Global.",
  "coverage_below_90_threshold": {
    "Naive": 0,
    "Global": "never",
    "Strat_MLE": "never",
    "HB_ECHTE": "never"
  },
  "output_files": [
    "results/exp_a1_sensitivity.csv",
    "results/exp_a1_sensitivity_summary.csv",
    "results/exp_a1_sensitivity_subgroup.csv"
  ]
}
completed_at: 2026-05-22T17:27:12.389Z
================================================================================
EXPERIMENT: exp-030
status: DONE
hypothesis: EC-HTE HB partial pooling at K=8 (per-subgroup ~31 expert labels) maintains coverage ≥90% and RMSE advantage over Global, demonstrating scalability beyond K=4.
conclusion: negative
metrics: {
  "hb_echte_coverage": 0.956,
  "hb_echte_rmse": 0.34,
  "hb_echte_mean_abs_bias": 0.183,
  "oracle_coverage": 0.944,
  "oracle_rmse": 0.113,
  "oracle_mean_abs_bias": 0.09,
  "global_coverage": 0.951,
  "global_rmse": 0.168,
  "global_mean_abs_bias": 0.135,
  "strat_mle_coverage": 0.953,
  "strat_mle_rmse": 0.638,
  "strat_mle_mean_abs_bias": 0.219,
  "naive_coverage": 0.913,
  "naive_rmse": 0.133,
  "naive_mean_abs_bias": 0.107,
  "hb_vs_mle_rmse_improvement_pct": 47,
  "per_subgroup_expert_labels": 31,
  "source": "results/exp_k8_subgroups_summary.csv",
  "note": "All CM-aware methods coverage \u226595%. HB RMSE 47% better than MLE but worse than Global. K=8 is boundary condition."
}
completed_at: 2026-05-22T19:42:42.807Z
================================================================================
EXPERIMENT: exp-031
status: DONE
hypothesis: EC-HTE under confounded treatment assignment (T depends on covariates via logistic model, not Bernoulli(0.5)) maintains coverage ≥93% when paired with IPW-DIM estimator, demonstrating compatibility wi
conclusion: success
metrics: {
  "hb_echte_coverage": 0.95,
  "hb_echte_rmse": 0.086,
  "hb_echte_mean_abs_bias": 0.068,
  "oracle_coverage": 0.943,
  "oracle_rmse": 0.061,
  "oracle_mean_abs_bias": 0.048,
  "global_coverage": 0.93,
  "global_rmse": 0.087,
  "global_mean_abs_bias": 0.071,
  "strat_mle_coverage": 0.95,
  "strat_mle_rmse": 0.087,
  "strat_mle_mean_abs_bias": 0.069,
  "naive_coverage": 0.863,
  "naive_rmse": 0.083,
  "naive_mean_abs_bias": 0.066,
  "beta_confound": 0.5,
  "propensity_range": "0.38-0.62",
  "source": "results/exp_confounded_dgp_summary.csv",
  "note": "EC-HTE + IPW-DIM coverage 95.0% under moderate confounding. Global 93.0%. Naive 86.3%."
}
completed_at: 2026-05-22T19:42:43.362Z
================================================================================
EXPERIMENT: exp-032
status: DONE
hypothesis: EC-HTE + IPW-DIM maintains coverage ≥90% across confounding strengths β∈{0.25, 0.5, 1.0, 2.0}, and estimated propensity (logistic regression) yields <3pp coverage difference vs oracle propensity.
conclusion: success
metrics: {
  "min_hb_coverage": 0.945,
  "max_oracle_vs_est_gap": 0.01,
  "hb_cov_b0.25_oracle": 0.9625,
  "hb_cov_b0.25_estimated": 0.9725,
  "hb_cov_b0.5_oracle": 0.95,
  "hb_cov_b0.5_estimated": 0.9575,
  "hb_cov_b1.0_oracle": 0.9575,
  "hb_cov_b1.0_estimated": 0.96,
  "hb_cov_b2.0_oracle": 0.945,
  "hb_cov_b2.0_estimated": 0.9475,
  "hb_rmse_b2.0_oracle": 0.1258,
  "naive_cov_range": "0.845-0.898",
  "source": "results/exp_confounded_sweep_summary.csv",
  "note": "All 8 configs HB coverage >=94.5%. Oracle vs estimated gap <=1pp. Hypothesis fully confirmed."
}
parent: exp-031
completed_at: 2026-05-22T20:31:26.532Z
================================================================================
EXPERIMENT: exp-033
status: DONE
hypothesis: Adaptive shrinkage (stronger alpha for high-pi subgroups) and/or kappa-threshold fallback can reduce K=8 HB RMSE from 0.340 toward Global's 0.168, narrowing the scalability gap.
conclusion: negative
metrics: {
  "hb_baseline_rmse": 0.333,
  "hb_baseline_coverage": 0.959,
  "v1_adaptive_alpha_rmse": 0.216,
  "v1_adaptive_alpha_coverage": 0.96,
  "v2_kappa_fallback_rmse": 0.25,
  "v2_kappa_fallback_coverage": 0.96,
  "v3_combined_rmse": 0.216,
  "v3_combined_coverage": 0.96,
  "global_rmse": 0.166,
  "global_coverage": 0.958,
  "v1_vs_baseline_improvement_pct": 35,
  "v1_still_exceeds_global_pct": 30,
  "source": "results/exp_k8_adaptive_summary.csv",
  "note": "V1 (adaptive alpha) reduces RMSE 35% (0.333->0.216) but still exceeds Global (0.166). Gap narrowed from 2x to 1.3x. Confirms boundary is real but mitigable."
}
parent: exp-030
completed_at: 2026-05-22T21:48:31.124Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "f91be5c4-65a7-4bb2-9871-5a3be69286d6"
}
```

</details>

---

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Cross-reference paper claims with registry data",
  "usage": {
    "total_tokens": 45983,
    "tool_uses": 14,
    "duration_ms": 118778
  },
  "last_tool_name": "Bash",
  "uuid": "9279d3b1-e50a-4fc6-ad44-cda05462aa65",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01A7iMPzRMYmSso2yGLQN57Q`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Search for specific numbers mentioned in paper claims\ntargets = {\n    'R2>=0.97': [],\n    '14.9% sign reversal': [],\n    '5x bias reduction': [],\n    '7.4x bias reduction': [],\n    'AUC 1.0/0.86/0.63': [],\n    '11 empirical CMs': [],\n    'bias 0.059->0.008': [],\n    '93.8% coverage': [],\n    '260/520': [],\n    '2.86x amplification': [],\n    '2.41x amplification': [],\n    '89% R-learner': [],\n    '4.7x factor': [],\n    '4.9x factor': [],\n    '5.9x factor': [],\n    'gamma_T=0.10 75% coverage': [],\n}\n\nfor eid, e in sorted(exps.items()):\n    text = json.dumps(e)\n    if '0.97' in text or 'r2' in text.lower() or 'R2' in text or 'R²' in text:\n        m = e.get('metrics', {})\n        # Check for R2 values\n        for k, v in (m.items() if isinstance(m, dict) else []):\n            if 'r2' in k.lower():\n                targets['R2>=0.97'].append(f'{eid}: {k}={v}')\n    if '14.9' in text:\n        targets['14.9% sign reversal'].append(f'{eid}')\n    if '260' in text and '520' in text:\n        targets['260/520'].append(f'{eid}')\n    if '2.86' in text:\n        targets['2.86x amplification'].append(f'{eid}')\n    if '2.41' in text:\n        targets['2.41x amplification'].append(f'{eid}')\n    if '0.008' in text:\n        targets['bias 0.059->0.008'].append(f'{eid}')\n    if '93.8' in text or '0.938' in text:\n        targets['93.8% coverage'].append(f'{eid}')\n    if '5.9' in text:\n        targets['5.9x factor'].append(f'{eid}')\n    if '0.626' in text or '0.611' in text or '0.833' in text:\n        targets['AUC 1.0/0.86/0.63'].append(f'{eid}')\n    if '0.75' in text and 'gamma' in text.lower():\n        targets['gamma_T=0.10 75% coverage'].append(f'{eid}')\n\nfor claim, matches in targets.items():\n    print(f'{claim}: {matches if matches else \\\"NOT FOUND\\\"}')\n\" 2>&1",
  "description": "Cross-reference paper claims with registry data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "0448b4de-4c28-42df-81e5-75c0bef78080",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sa6pNdFY8RzJaew6478ACR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8470,
      "cache_read_input_tokens": 37138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8470,
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

_source line 82 · 2026-05-24T04:31:41.694Z_

<details><summary>↩ Tool result · `toolu_01A7iMPzRMYmSso2yGLQN57Q`</summary>

```text
R2>=0.97: ['exp-002: r2_k2=0.9939', 'exp-002: r2_k4=0.9738', 'exp-014: r2_analytic_vs_mc=0.992', "exp-019: theorem1_r2={'K2': {'pz0.1': 0.998, 'pz0.2': 0.989, 'pz0.3': 0.994, 'pz0.4': 0.995, 'pz0.5': 0.995}, 'K4': {'pz0.1': 0.984, 'pz0.2': 0.976, 'pz0.3': 0.985, 'pz0.4': 0.984, 'pz0.5': 0.992}}", 'exp-019: theorem1_r2_range=0.976-0.998 (all >0.95)', 'exp-024: R2_overall=0.975']
14.9% sign reversal: ['exp-038']
5x bias reduction: NOT FOUND
7.4x bias reduction: NOT FOUND
AUC 1.0/0.86/0.63: ['exp-005', 'exp-026', 'exp-028']
11 empirical CMs: NOT FOUND
bias 0.059->0.008: ['exp-017', 'exp-039']
93.8% coverage: ['exp-022', 'exp-029', 'exp-034', 'exp-036', 'exp-037', 'exp-039']
260/520: ['exp-002']
2.86x amplification: ['exp-002']
2.41x amplification: ['exp-002']
89% R-learner: NOT FOUND
4.7x factor: NOT FOUND
4.9x factor: NOT FOUND
5.9x factor: ['exp-011', 'exp-028']
gamma_T=0.10 75% coverage: ['exp-040']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "3003506d-e3ba-4619-a6a7-25a382ab7e5d"
}
```

</details>

---

### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Search for remaining paper claim numbers",
  "usage": {
    "total_tokens": 47465,
    "tool_uses": 15,
    "duration_ms": 133949
  },
  "last_tool_name": "Bash",
  "uuid": "19ed4589-940f-46f9-9c56-57fc5d48b356",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01P58LfVMv88ch1NQNv5Jscv`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Look for 5x, 7.4x, 4.7x, 4.9x, 89% R-learner, 11 empirical\nfor eid, e in sorted(exps.items()):\n    text = json.dumps(e)\n    m = e.get('metrics', {})\n    \n    # Check for bias reduction ratios\n    if isinstance(m, dict):\n        for k, v in m.items():\n            sv = str(v)\n            if '4.2x' in sv or '4.7' in sv or '4.9' in sv or '5x' in sv or '7.4' in sv or '5.0' in sv:\n                print(f'{eid}.metrics.{k} = {v}')\n    \n    # Check for 89% anywhere\n    if '89%' in text or '0.89' in text:\n        # find context\n        if isinstance(m, dict):\n            for k, v in m.items():\n                sv = str(v)\n                if '89' in sv or '0.89' in sv:\n                    print(f'{eid}.metrics.{k} = {v}')\n    \n    # 11 empirical CMs\n    if '11' in text and ('cm' in text.lower() or 'empirical' in text.lower() or 'confusion' in text.lower()):\n        if isinstance(m, dict):\n            if 'n_llm_dataset_combos' in m:\n                print(f'{eid}.metrics.n_llm_dataset_combos = {m[\\\"n_llm_dataset_combos\\\"]}')\n\" 2>&1",
  "description": "Search for remaining paper claim numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "97de0b72-42ff-4f00-a6b2-53c2256a4630",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fz2uDDSh8F4i8YU7pDNfX9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 45608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
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

_source line 85 · 2026-05-24T04:31:56.849Z_

<details><summary>↩ Tool result · `toolu_01P58LfVMv88ch1NQNv5Jscv`</summary>

```text
exp-007.metrics.key_finding = ec_hte_ppci achieves near-zero bias in DGP C (both errors), 35x better than ec_hte. RMSE competitive at n>=250 extreme. Coverage always 1.0.
exp-010.metrics.k2_coverage_naive = [0.875, 0.877, 0.89, 0.897]
exp-014.metrics.bias_reduction_vs_global = 4.2x
exp-014.metrics.key_finding = Product structure bias = Δτ·[B_s]_{z,1} holds exactly under asymmetric misclassification. A2 (symmetric) assumption is NOT required. EC-HTE dominates with 4.2x bias reduction.
exp-015.metrics.coverage_n500 = {'naive': 0.873, 'global': 0.885, 'hb': 0.89}
exp-016.metrics.coverage_n100 = {'naive': 0.784, 'global': 0.893, 'hb': 0.769}
exp-016.metrics.coverage_n500 = {'naive': 0.784, 'global': 0.939, 'hb': 0.894}
exp-024.metrics.n_llm_dataset_combos = 11
exp-026.metrics.K2_n25 = {'mle_rmse': 0.2562, 'hb_rmse': 0.2689, 'delta_pct': '+4.9%', 'global_rmse': 0.1013}
exp-031.metrics.note = EC-HTE + IPW-DIM coverage 95.0% under moderate confounding. Global 93.0%. Naive 86.3%.
exp-032.metrics.naive_cov_range = 0.845-0.898
exp-036.metrics.key_finding = With correct n_estimators=200, plugin SE already near-nominal (93.8%). Bootstrap provides modest improvement to exact 95.0%. v1 '81.7% → 94.2%' gap was artifact of n_estimators=48.
exp-038.metrics.reversal_pct_tau003 = 14.9
exp-040.metrics.gamma005_cov = 0.897
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "33d44b1b-4a70-4b6b-93c8-a96369ae2baf"
}
```

</details>

---

### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Compute derived metrics and verify paper claims",
  "usage": {
    "total_tokens": 48689,
    "tool_uses": 16,
    "duration_ms": 153216
  },
  "last_tool_name": "Bash",
  "uuid": "4ba45100-0a70-4636-9bfe-356178425d89",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_017pEbRqkcTPq7NZREacJine`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Compute bias reduction ratios from exp-017 R-learner data\nm17 = exps['exp-017']['metrics']\nrl = m17['rlearner_results']\nprint('=== exp-017 R-learner bias reduction ===')\nprint(f'Naive bias: {rl[\\\"naive\\\"][\\\"avg_abs_bias\\\"]}')\nprint(f'EC-HTE bias: {rl[\\\"ec_hte\\\"][\\\"avg_abs_bias\\\"]}')\nratio = rl['naive']['avg_abs_bias'] / rl['ec_hte']['avg_abs_bias']\nprint(f'Naive/EC-HTE ratio: {ratio:.1f}x')\npct_reduction = (1 - rl['ec_hte']['avg_abs_bias'] / rl['naive']['avg_abs_bias']) * 100\nprint(f'Percent reduction: {pct_reduction:.1f}%')\nprint(f'ec_hte_bias_reduction_vs_naive: {m17[\\\"ec_hte_bias_reduction_vs_naive\\\"]}')\n\n# exp-011 CausalForest ratios\nm11 = exps['exp-011']['metrics']\nprint()\nprint('=== exp-011 CausalForest bias ratios ===')\nfor method, val in m11['mean_abs_bias'].items():\n    print(f'{method} avg abs bias: {val}')\nprint(f'naive/ec_hte ratio: {m11[\\\"mean_abs_bias\\\"][\\\"naive_forest\\\"]/m11[\\\"mean_abs_bias\\\"][\\\"ec_hte_forest\\\"]:.1f}x')\nprint(f'global/ec_hte ratio: {m11[\\\"mean_abs_bias\\\"][\\\"global_forest\\\"]/m11[\\\"mean_abs_bias\\\"][\\\"ec_hte_forest\\\"]:.1f}x')\nprint(f'debiasing_hurts_max_ratio: {m11[\\\"debiasing_hurts_max_ratio\\\"]}')\n\n# exp-039 K2 bias\nm39 = exps['exp-039']['metrics']\nprint()\nprint('=== exp-039 K2 EC-HTE bias ===')\nprint(f'K2 EC-HTE bias: {m39[\\\"K2_echte_bias\\\"]}')\nprint(f'K2 EC-HTE coverage: {m39[\\\"K2_echte_cov\\\"]}')\n\n# exp-002 debiasing hurts\nm02 = exps['exp-002']['metrics']\nprint()\nprint('=== exp-002 bias amplification ===')\nprint(f'debiasing_hurts_pct: {m02[\\\"debiasing_hurts_pct\\\"]}')\nprint(f'debiasing_hurts_pct_note: {m02[\\\"debiasing_hurts_pct_note\\\"]}')\nprint(f'max_bias_ratio_k2: {m02[\\\"max_bias_ratio_k2\\\"]}')\nprint(f'max_bias_ratio_k4: {m02[\\\"max_bias_ratio_k4\\\"]}')\n\n# exp-005 AUC\nm05 = exps['exp-005']['metrics']\nprint()\nprint('=== exp-005 Diagnostic AUC ===')\nprint(f'subgroup_level_auc: {m05[\\\"subgroup_level_auc\\\"]}')\nprint(f'setting_level_auc: {m05[\\\"setting_level_auc\\\"]}')\n\n# exp-028 AUC\nm28 = exps['exp-028']['metrics']\nprint()\nprint('=== exp-028 Diagnostic AUC ===')\nprint(f'overall_symmetric_auc: {m28[\\\"overall_symmetric_auc\\\"]}')\nprint(f'overall_asymmetric_auc: {m28[\\\"overall_asymmetric_auc\\\"]}')\n\" 2>&1",
  "description": "Compute derived metrics and verify paper claims"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "38f0d1c0-33fa-4ed2-bd92-d0c70408c180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqpbYQjyFjgyGHug8Es6Bn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 47052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1188,
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

_source line 88 · 2026-05-24T04:32:16.124Z_

<details><summary>↩ Tool result · `toolu_017pEbRqkcTPq7NZREacJine`</summary>

```text
=== exp-017 R-learner bias reduction ===
Naive bias: 0.121
EC-HTE bias: 0.013
Naive/EC-HTE ratio: 9.3x
Percent reduction: 89.3%
ec_hte_bias_reduction_vs_naive: 9.3x (R-learner) vs 15.6x (CausalForest)

=== exp-011 CausalForest bias ratios ===
naive_forest avg abs bias: 0.1558
global_forest avg abs bias: 0.1073
ec_hte_forest avg abs bias: 0.0608
naive/ec_hte ratio: 2.6x
global/ec_hte ratio: 1.8x
debiasing_hurts_max_ratio: 5.9

=== exp-039 K2 EC-HTE bias ===
K2 EC-HTE bias: 0.008
K2 EC-HTE coverage: 0.938

=== exp-002 bias amplification ===
debiasing_hurts_pct: 50
debiasing_hurts_pct_note: 260/520 (excluding dc=0 rows where bias=0)
max_bias_ratio_k2: 2.86
max_bias_ratio_k4: 2.41

=== exp-005 Diagnostic AUC ===
subgroup_level_auc: 0.833
setting_level_auc: 0.49

=== exp-028 Diagnostic AUC ===
overall_symmetric_auc: 0.626
overall_asymmetric_auc: 0.611
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "55e1a173-3518-43be-84cc-5da03bfab11d"
}
```

</details>

---

### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Find 5x and 7.4x bias reduction sources",
  "usage": {
    "total_tokens": 50312,
    "tool_uses": 17,
    "duration_ms": 173040
  },
  "last_tool_name": "Bash",
  "uuid": "ce60918b-88f2-4c6d-8181-6b9b880fe1a1",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_01CoLQxUd7zVLBrWr2Eqw2aE`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Look for 5x and 7.4x bias reduction\n# Might be computed, not stored. Let me check exp-002, exp-011, exp-014, exp-023\n# for bias reduction ratios that would give 5x or 7.4x\n\n# exp-002: Check if naive vs ec_hte gives 5x or 7.4x\n# exp-002 doesn't have per-method bias, it's about debiasing hurts\n\n# Check exp-039 for bias reduction factors\nm39 = exps['exp-039']['metrics']\nprint('=== exp-039 bias values ===')\nfor k, v in m39.items():\n    print(f'  {k}: {v}')\n\n# Let me look at what 0.059->0.008 means\n# exp-039: K2_echte_bias = 0.008\n# Where does 0.059 come from? Check naive bias for K2\n# Not stored in exp-039. Let me check other experiments\n\n# Check for the specific bias 0.059 value\nfor eid, e in sorted(exps.items()):\n    text = json.dumps(e)\n    if '0.059' in text:\n        m = e.get('metrics', {})\n        if isinstance(m, dict):\n            for k, v in m.items():\n                if '0.059' in str(v):\n                    print(f'{eid}.metrics.{k} = {v}')\n\n# Check exp-023 for bias reduction\nm23 = exps['exp-023']['metrics']\nprint()\nprint('=== exp-023 bias reduction ===')\nprint(f'bias_reduction_n200: {m23[\\\"bias_reduction_n200\\\"]}')\nprint(f'bias_reduction_n500: {m23[\\\"bias_reduction_n500\\\"]}')\nprint(f'bias_reduction_n1000: {m23[\\\"bias_reduction_n1000\\\"]}')\n\" 2>&1",
  "description": "Find 5x and 7.4x bias reduction sources"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "fb54f8df-4123-425b-ad60-91c3a615a487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ELrMfQdhGqE3hJ4Pg2xz16",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1611,
      "cache_read_input_tokens": 48240,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1611,
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

_source line 91 · 2026-05-24T04:32:35.934Z_

<details><summary>↩ Tool result · `toolu_01CoLQxUd7zVLBrWr2Eqw2aE`</summary>

```text
=== exp-039 bias values ===
  K2_echte_bias: 0.008
  K2_echte_rmse: 0.089
  K2_echte_cov: 0.938
  K4_echte_bias: 0.012
  K4_echte_rmse: 0.12
  K4_echte_cov: 0.956
  K8_echte_bias: 0.183
  K8_echte_rmse: 0.34
  K8_echte_cov: 0.956
  K8_global_rmse: 0.168
exp-029.metrics.echte_abs_bias = {'g0.00': 0.0596, 'g0.05': 0.0593, 'g0.10': 0.063, 'g0.15': 0.0652, 'g0.20': 0.0677}
exp-035.metrics.naive_abs_bias = 0.0592

=== exp-023 bias reduction ===
bias_reduction_n200: 32% vs Global (0.0248 vs 0.0365)
bias_reduction_n500: 68% vs Global (0.0099 vs 0.0314)
bias_reduction_n1000: 55% vs Global (0.0130 vs 0.0286)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "694caa38-e24c-48c9-a535-63b798e21f72"
}
```

</details>

---

### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Search for 5x, 7.4x, 4.7x, 4.9x bias reduction ratios",
  "usage": {
    "total_tokens": 51440,
    "tool_uses": 18,
    "duration_ms": 188020
  },
  "last_tool_name": "Bash",
  "uuid": "77b58412-cb43-419e-94dc-4c5da782b591",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_013JRhaxWZHpU2xpAroNrYsZ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# Compute derived ratios that might match 5x, 7.4x, 4.7x, 4.9x\n# These are likely from specific configurations in Table 1 or similar\n\n# exp-011: debiasing_hurts_max_ratio=5.9 and other subgroup ratios\n# Let me search for 4.7 and 4.9 more carefully\nfor eid, e in sorted(exps.items()):\n    text = json.dumps(e)\n    if '4.7' in text or '4.9' in text:\n        m = e.get('metrics', {})\n        if isinstance(m, dict):\n            for k, v in m.items():\n                sv = str(v)\n                if '4.7' in sv or '4.9' in sv:\n                    print(f'{eid}.metrics.{k} = {v}')\n        notes = e.get('notes', '')\n        if notes and ('4.7' in str(notes) or '4.9' in str(notes)):\n            print(f'{eid}.notes contains 4.7/4.9')\n\n# Check for 5x, 7x, 7.4x explicitly\nfor eid, e in sorted(exps.items()):\n    text = json.dumps(e)\n    if '7.4' in text:\n        print(f'{eid} contains 7.4')\n    if '\\\"5x\\\"' in text.lower() or '5.0x' in text or ' 5x ' in text:\n        print(f'{eid} contains 5x')\n\n# Check the bias 0.059 source. Could it be from naive in a table?\n# exp-039: K2_echte_bias=0.008. What about naive K2 bias?\n# Not in exp-039, but might be in exp-001 or exp-006\n\n# Let me find all experiments with both naive and ec_hte bias\nfor eid, e in sorted(exps.items()):\n    m = e.get('metrics', {})\n    if isinstance(m, dict):\n        # Patterns of naive_bias/naive_abs_bias and echte_bias\n        naive_keys = [k for k in m if 'naive' in k.lower() and ('bias' in k.lower())]\n        echte_keys = [k for k in m if ('echte' in k.lower() or 'hb' in k.lower() or 'ec_hte' in k.lower()) and ('bias' in k.lower())]\n        if naive_keys and echte_keys:\n            for nk in naive_keys:\n                for ek in echte_keys:\n                    nv = m[nk]\n                    ev = m[ek]\n                    if isinstance(nv, (int, float)) and isinstance(ev, (int, float)) and ev > 0:\n                        ratio = nv / ev\n                        if 4.5 <= ratio <= 8:\n                            print(f'{eid}: {nk}={nv} / {ek}={ev} = {ratio:.2f}x')\n\" 2>&1",
  "description": "Search for 5x, 7.4x, 4.7x, 4.9x bias reduction ratios"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "e82467a2-89f3-444a-9f0b-00176a2e6329",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3bR7FQfpVCXGwDs31p2VV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1062,
      "cache_read_input_tokens": 49851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1062,
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

_source line 94 · 2026-05-24T04:32:50.979Z_

<details><summary>↩ Tool result · `toolu_013JRhaxWZHpU2xpAroNrYsZ`</summary>

```text
exp-026.metrics.K2_n25 = {'mle_rmse': 0.2562, 'hb_rmse': 0.2689, 'delta_pct': '+4.9%', 'global_rmse': 0.1013}
exp-038.metrics.reversal_pct_tau003 = 14.9
exp-012 contains 7.4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "456e098c-6182-4b75-9bdb-081eb3d3e3df"
}
```

</details>

---

### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Find 7.4x context in exp-012",
  "usage": {
    "total_tokens": 52583,
    "tool_uses": 19,
    "duration_ms": 200112
  },
  "last_tool_name": "Bash",
  "uuid": "a0c9996a-c604-4d5a-8222-f33c0effdaec",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Bash · `toolu_0177GHzudbonqF7NAGTDAn6N`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# exp-012 - where is 7.4?\nprint('=== exp-012 full text search for 7.4 ===')\ntext = json.dumps(exps['exp-012'])\n# find context around 7.4\nidx = text.find('7.4')\nif idx >= 0:\n    print(text[max(0,idx-100):idx+100])\n\n# Look at all notes fields for ratios\nfor eid, e in sorted(exps.items()):\n    notes = e.get('notes', '')\n    if notes and ('5x' in str(notes) or '7x' in str(notes) or '7.4' in str(notes) or '4.7' in str(notes) or '4.9' in str(notes)):\n        print(f'--- {eid} notes ---')\n        print(notes[:500])\n\" 2>&1",
  "description": "Find 7.4x context in exp-012"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "1099cba8-b5b1-4d62-8f99-60e437926aaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoxWXVcmYgDAK8fhJC7aS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1107,
      "cache_read_input_tokens": 50913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1107,
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

_source line 97 · 2026-05-24T04:33:03.003Z_

<details><summary>↩ Tool result · `toolu_0177GHzudbonqF7NAGTDAn6N`</summary>

```text
=== exp-012 full text search for 7.4 ===
{"status": "DONE", "retry_count": 0, "created_at": "2026-05-21T05:20:57.458Z", "updated_at": "2026-05-21T05:24:11.994Z", "hypothesis": "\u771f\u5b9e LLM\uff08GPT-4.1\uff0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "93de509e-c081-45b1-958b-a8c1804a5cbe"
}
```

</details>

---

### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "description": "Running Check all reduction/ratio metrics",
  "usage": {
    "total_tokens": 53136,
    "tool_uses": 20,
    "duration_ms": 210695
  },
  "last_tool_name": "Bash",
  "uuid": "b071e5fc-83d6-45e9-a251-6786c049a3cd",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_016kyeJyrwWmtpANrQiYBwD9`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\n\n# The 5x, 7.4x claims may come from computed ratios not stored in registry.\n# Let me check exp-011's debiasing_hurts detail more carefully\nm11 = exps['exp-011']['metrics']\nprint('exp-011 debiasing_hurts_max_ratio:', m11.get('debiasing_hurts_max_ratio'))\nprint('exp-011 debiasing_hurts_detail:', m11.get('debiasing_hurts_detail'))\n\n# Check for 'bias_reduction' keys in all experiments\nfor eid, e in sorted(exps.items()):\n    m = e.get('metrics', {})\n    if isinstance(m, dict):\n        for k, v in m.items():\n            if 'reduction' in k.lower() or 'ratio' in k.lower():\n                print(f'{eid}.{k} = {v}')\n\n# Also check 'notes' for R-learner 89%\nm17 = exps['exp-017']\nprint()\nprint('=== exp-017 notes ===')\nprint(m17.get('notes', ''))\n\" 2>&1",
  "description": "Check all reduction/ratio metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "d5ca9b55-5cdb-4f4e-8a8d-aa8f9d55ba87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQW9eoL5N3KzUrM6u5iQzz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 551,
      "cache_read_input_tokens": 52020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 551,
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

_source line 100 · 2026-05-24T04:33:13.589Z_

<details><summary>↩ Tool result · `toolu_016kyeJyrwWmtpANrQiYBwD9`</summary>

```text
exp-011 debiasing_hurts_max_ratio: 5.9
exp-011 debiasing_hurts_detail: K=4/extreme/sg0: global 5.9x worse than naive
exp-002.tightness_ratio_k2_median = 1.0027
exp-002.tightness_ratio_k4_median = 1.0234
exp-002.max_bias_ratio_k2 = 2.86
exp-002.max_bias_ratio_k4 = 2.41
exp-003.v3_hb_integration_100mc = {'methods': ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte'], 'hb_vs_mle_summary': {'n50_S3_extreme': '-57% RMSE (HB worse, but not catastrophic)', 'n50_S3_moderate': '-54% RMSE z1 (HB worse)', 'n100_S3_extreme': '+60% RMSE z1 (HB dramatically better)', 'n100_S3_moderate': '+24% RMSE z1 (HB better)', 'n100_S2': '+5-8% RMSE (HB better)', 'n250_S3': '+5-17% RMSE (HB better)', 'n500_all': '+0.2-1.6% (converged)'}, 'key_finding': '100 MC confirms: S3 blowup at n=50 is real but moderate (not catastrophic as dry-run suggested). At n>=100, HB is better everywhere, especially S3 (+26-60%). Partial pooling sweet spot is n=100-250.', 'hypothesis_verdict': 'validated_with_boundary', 'boundary_condition': 'n_expert>=100 recommended; n=50 with extreme heterogeneity in tiny subgroups shows moderate degradation'}
exp-011.debiasing_hurts_max_ratio = 5.9
exp-014.bias_reduction_vs_global = 4.2x
exp-017.ec_hte_bias_reduction_vs_naive = 9.3x (R-learner) vs 15.6x (CausalForest)
exp-018.ec_hte_rmse_reduction_vs_naive = 52%
exp-019.rmse_ratio_hb_over_global = {'K2': {'pz0.1': 0.92, 'pz0.2': 0.763, 'pz0.3': 0.78, 'pz0.4': 0.874, 'pz0.5': 0.857}, 'K4': {'pz0.1': 1.542, 'pz0.2': 1.684, 'pz0.3': 1.121, 'pz0.4': 1.082, 'pz0.5': 1.063}}
exp-020.rmse_ratio = 1.048
exp-023.bias_reduction_n500 = 68% vs Global (0.0099 vs 0.0314)
exp-023.bias_reduction_n200 = 32% vs Global (0.0248 vs 0.0365)
exp-023.bias_reduction_n1000 = 55% vs Global (0.0130 vs 0.0286)
exp-036.se_ratio_boot_over_plugin = 1.154
exp-036.s1_se_ratio = 1.222

=== exp-017 notes ===
EC-HTE correction generalizes to R-learner: |Bias| 0.121→0.013 (89% reduction), coverage 0.47→0.92. Consistent with CausalForest results (|Bias|=0.008, coverage 0.91). Validates estimator-agnostic upstream correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "ce300c9c-dcaa-4652-a8f8-9b8347b728ab"
}
```

</details>

---

### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a4587c47dc95cd896",
  "tool_use_id": "toolu_01CfGLBvDZzKv4eD22XUrKoo",
  "status": "completed",
  "output_file": "",
  "summary": "Parse registry JSON for key experiments",
  "usage": {
    "total_tokens": 54794,
    "tool_uses": 20,
    "duration_ms": 345148
  },
  "uuid": "8aacf05a-c01b-4bd1-b845-f137537155fb",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e"
}
```

---

### Tool result

_source line 102 · 2026-05-24T04:35:27.953Z_

<details><summary>↩ Tool result · `toolu_01CfGLBvDZzKv4eD22XUrKoo`</summary>

```text
Now I have everything. Here is the complete extraction:

---

## Complete Registry Extraction — All 42 Experiments

### Specifically Requested Experiments

**exp-001** — HB Synthetic Validation
- Status: DONE, conclusion: success
- Hypothesis: HB Dirichlet-prior CM estimator via partial pooling outperforms MLE/Laplace at small n_expert
- Metrics:
  - MCMC: rhat_max=1.024, ess_min=129, divergent=0, total_mc_runs=3600
  - HB vs MLE RMSE improvement: K2/n50: 4-9%, K2/n100: 1-2%, K4/n50/moderate: 6-9%
  - HB coverage: min=0.87, median=0.93
  - 4-chain MCMC fix: rhat_max=1.0034, ess_min=1618 (~4x improvement)
    - K4/extreme/n50/A rmse: 3.14→0.99, B rmse: 509.93→0.27, n100/A rmse: 11.57→0.29
    - Singularity guard: triggers in extreme/n=50 only (2 HB, 3 MLE / 100 runs)
  - Hyperprior sensitivity: scale range 0.5-2.0, K2 RMSE variation <1%, K4 ~4-5%, coverage invariant, conclusion: robust
  - Runtime: 69 min

**exp-002** — Bias Bound / Theorem 1
- Status: DONE, conclusion: success
- Hypothesis: Global correction bias follows analytic formula bias ∝ Δ_misclass × Δ_CATE; parameter regions exist where |bias_global| > |bias_naive|
- Metrics:
  - **R²: K2=0.9939, K4=0.9738**
  - Tightness ratio: K2 median=1.0027, K4 median=1.0234
  - **Debiasing hurts: 50% of configs (260/520, excluding dc=0)**
  - Debiasing hurts threshold Δmisclass: 0.1235
  - **Max bias ratio: K2=2.86×, K4=2.41×**
  - Coverage 2SE: K2=0.951, K4=0.940

**exp-003** — TweetEval Semi-Synthetic
- Status: DONE, conclusion: success
- 4 subgroups, misclass rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25, sizes ~38%/38%/12%/12%, P(Z=1)=0.39
- Debiasing hurts confirmed: true, 100 MC runs
- HB vs MLE summary:
  - n50/S3/extreme: -57% RMSE (HB worse), n50/S3/moderate: -54%
  - n100/S3/extreme: +60% (HB dramatically better), n100/S3/moderate: +24%
  - n100/S2: +5-8%, n250/S3: +5-17%, n500/all: +0.2-1.6% (converged)
- Boundary: n_expert≥100 recommended; n=50 with extreme heterogeneity degrades moderately

**exp-008** — Multi-LLM Persistence
- Status: DONE, conclusion: success
- 6 models: gpt-3.5-turbo, gpt-4.1, gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-5.4
- **Effective Δπ**: gpt-3.5-turbo=0.198, gpt-4-turbo=0.149, gpt-4.1=0.098, gpt-4o=0.080, gpt-4o-mini=0.136, gpt-5.4=0.114
- All Δπ > 0.05: **true** — heterogeneity is structural
- Filtered analysis excluded False_long (n=6) and True_long (n=4), retained 4 subgroups with n≥10
- Spearman significant pairs: 4 pairs at ρ=1.000

**exp-019** — P(Z=1) Sweep
- Status: DONE, conclusion: success
- **Theorem 1 R²**: K2 range 0.989-0.998, K4 range 0.976-0.992 — **all >0.95**
- RMSE ratio HB/Global: K2 wins all (0.76-0.92), K4 HB loses all (1.06-1.68)
- Coverage: HB 0.92-0.94 (near-nominal), naive 0.65-0.79, global 0.79-0.90

**exp-023** — Heterogeneous-τ DGP
- Status: DONE, conclusion: success
- N=5000, P(Z=1)=0.652, K=4, Δτ: False_medium=0.1, False_short=0.1, True_medium=0.3, True_short=0.6
- EC-HTE bias wins: 3/3 budgets
  - n200: 32% reduction (0.0248 vs 0.0365)
  - **n500: 68% reduction (0.0099 vs 0.0314)**
  - n1000: 55% reduction (0.0130 vs 0.0286)
- RMSE: True_short z0 n1000: global=0.2577, echte=0.2117 (-17.8%)
- Aggregate RMSE: EC-HTE loses (variance cost in low-Δτ subgroups)

**exp-035** — Asymmetric CM (7:1 FPR/FNR)
- Status: DONE, conclusion: success
- EC-HTE asymmetric: abs_bias=0.057, RMSE=0.0735, **coverage=0.945**
- EC-HTE symmetric: abs_bias=0.0618, RMSE=0.0831, coverage=0.930
- Global asymmetric: abs_bias=0.0609, coverage=0.915
- Naive: abs_bias=0.0592, coverage=0.870
- Oracle: abs_bias=0.0454, coverage=0.943
- Asymmetric vs symmetric EC-HTE: RMSE improved 11.5% (0.0831→0.0735), coverage +1.5pp

**exp-036** — Bootstrap SE
- Status: DONE, conclusion: success
- **Plugin coverage: 0.9375 (93.8%)**
- **Bootstrap coverage: 0.950 (95.0%)**
- Oracle coverage: 0.900
- SE ratio boot/plugin: 1.154
- s1 (high-error): plugin 0.925, bootstrap 0.975, SE ratio 1.222
- n_mc=20, n_bootstrap=100, n_estimators=200, runtime=1716s
- Key: v1's "81.7%→94.2%" gap was artifact of n_estimators=48

**exp-037** — Temperature Calibration
- Status: DONE, conclusion: success
- Calibrated+EC-HTE: abs_bias=0.0554, **coverage=0.965**
- Calibrated+Global: abs_bias=0.0550, coverage=0.963
- Calibrated+Naive: abs_bias=0.0510, coverage=0.912
- Uncalibrated+EC-HTE: abs_bias=0.0641, coverage=0.938
- Uncalibrated+Global: abs_bias=0.0695, coverage=0.920
- Uncalibrated+Naive: abs_bias=0.0634, coverage=0.840
- Oracle: abs_bias=0.0431, coverage=0.963
- **Δπ: uncalibrated=0.20, calibrated=0.07**
- Conclusion: calibration and EC-HTE are complementary, not substitutes

**exp-038** — Sign Reversal / Policy Reversal
- Status: DONE, conclusion: success
- **reversal_pct at τ=0.01: 31%**
- **reversal_pct at τ=0.03: 14.9%**
- **reversal_pct at τ=0.05: 6.1%**
- reversal_pct at τ=0.10: 0%
- **EC-HTE reversal: 0%**
- Worst combo: τ=0.01, delta_misclass=0.19 → 42.9%

**exp-039** — K Scaling (K=2/4/8)
- Status: DONE, conclusion: success
- **K2: bias=0.008, RMSE=0.089, coverage=0.938**
- K4: bias=0.012, RMSE=0.120, coverage=0.956
- K8: bias=0.183, RMSE=0.340, coverage=0.956
- K8 global RMSE: 0.168 (EC-HTE loses at K=8)

**exp-040** — Treatment-Dependent Misclassification
- Status: DONE, conclusion: success
- γ=0.00: coverage=0.945, RMSE=0.075
- γ=0.05: coverage=0.897, RMSE=0.092
- **γ=0.10: coverage=0.750, RMSE=0.133**
- γ=0.15: coverage=0.525, RMSE=0.177
- γ=0.20: coverage=0.370, RMSE=0.224
- **Breakeven γ: 0.10**

---

### Keyword-Matched Experiments

**exp-004** — Hate Speech (UC Berkeley) [hate_speech]
- Status: DONE, conclusion: success
- Dataset: UC Berkeley Measuring Hate Speech, n=2496
- Δπ=0.117, global FPR=0.139, global FNR=0.533
- Subgroup misclass: plat0_long=0.266, plat0_short=0.337, plat23_long=0.303, plat23_short=0.383
- Avg abs bias: naive=0.210, global=0.273, ec_hte=0.313
- EC-HTE fails here due to extreme FNR (~53%) — near-random for positive class

**exp-005** — Diagnostic Criterion [diagnostic]
- Status: DONE, conclusion: success
- **Subgroup-level AUC: 0.833**
- Subgroup correlation: 0.86
- **Setting-level AUC: 0.49**
- Low-π hurt%: 84.6%, High-π hurt%: 15.4%

**exp-011** — CausalForest Integration [causal_forest]
- Status: DONE, conclusion: success
- 100 MC, 8 configs, 144 total rows
- Mean abs bias: naive_forest=0.1558, global_forest=0.1073, ec_hte_forest=0.0608
- Mean RMSE: naive=0.1782, global=0.1659, ec_hte=0.2289
- **Debiasing hurts cases: 9, max ratio: 5.9×** (K=4/extreme/sg0: global 5.9× worse than naive)
- K2/n500 EC-HTE bias range: 0.004-0.013 (near zero)

**exp-013** — Budget Threshold [amplification]
- Status: DONE, conclusion: success
- Config: K=4/extreme/n_expert=50 (12.5 per subgroup)
- RMSE: naive=0.109, global=0.140, MLE=0.280, EB=0.292
- Worst subgroup: A(π=0.30) EB RMSE=0.62
- **Amplification max: 4.4×** (A/EB vs global)
- Debiasing hurts D: Naive bias=0.001, Global bias=0.110

**exp-014** — Asymmetric Misclassification Theory [asymmetric]
- Status: DONE, conclusion: success
- R² analytic vs MC: 0.992, product structure confirmed
- EC-HTE: avg abs bias=0.006, RMSE=0.033, coverage=0.900
- Global: avg abs bias=0.025, RMSE=0.040, coverage=0.780
- **Bias reduction vs global: 4.2×**, coverage improvement: +12pp

**exp-015** — Realistic Asymmetric CMs (GPT-4.1) [asymmetric]
- Status: DONE, conclusion: **negative**
- S0 FNR=0.526, worst CM row near-uniform → inversion amplifies noise
- HB worse than global at all n_expert (100/250/500)
- RMSE n500: naive=0.123, global=0.196, HB=0.260
- Root cause: P(Z=1)=0.18 + FNR≈0.5

**exp-016** — Realistic Asymmetric CMs (gpt-3.5-turbo) [diagnostic, asymmetric]
- Status: DONE, conclusion: **negative**
- Worst FNR=0.211 but FPR=0.393
- HB worse than global at all n_expert
- Root cause: FPR variance 0.143-0.393 + P(Z=1)=0.18

**exp-017** — R-Learner Generalization [causal_forest, r-learner]
- Status: DONE, conclusion: success
- R-learner: naive bias=0.121, ec_hte bias=0.013, coverage: 0.47→0.92
- **EC-HTE bias reduction: 9.3× (R-learner), 89% reduction**
- CausalForest comparison: ec_hte bias=0.008, coverage=0.91
- Pattern consistent across estimators

**exp-024** — Bias Identity with Real CMs [bias_identity, asymmetric]
- Status: DONE, conclusion: success
- **R² overall: 0.975**
- **n_llm_dataset_combos: 11**
- Data sources: exp023 CMs + c1_multi_llm profiles

**exp-025** — Proposition 3 Diagnostic Screening [diagnostic]
- Status: DONE, conclusion: success
- Screening: 0/16 combos pass all conditions (κ≤1.25 bottleneck)
- Oracle screening: HB wins 41/52 comparisons on aggregate RMSE
- HB vs MLE: HB beats MLE in 52/52 comparisons
- Open-source LLMs: all 4 (Llama/Qwen/Mistral/Gemma) HB wins 32/32 on TweetEval

**exp-027b** — CF Oracle Coverage K=2 [amplification]
- EC-HTE estimated CM: coverage=0.925, bias=0.0044, RMSE=0.079
- Oracle true Z: coverage=0.940, bias=0.0023, RMSE=0.056
- Naive: coverage=0.828

**exp-027c** — CF Oracle Coverage MF2 DGP [asymmetric, amplification]
- EC-HTE estimated: coverage=0.923, bias=0.100, RMSE=0.111
- Oracle: coverage=0.960, bias=0.077, RMSE=0.091
- Naive: coverage=0.773

**exp-028** — Asymmetric Diagnostic AUC [diagnostic, asymmetric]
- Status: DONE, conclusion: **negative**
- **Overall symmetric AUC: 0.626**
- **Overall asymmetric AUC: 0.611**
- K4 perfect AUC combos: Llama/Qwen/Mistral/gpt-4o on TweetEval (AUC=1.0)
- K2 all AUC zero (degenerate)

**exp-034** — F-L Scalar Comparison [sign_reversal]
- Status: DONE, conclusion: success
- F-L scalar: abs_bias=0.0909, RMSE=0.1161, coverage=0.850
- F-L per-subgroup: abs_bias=0.112, RMSE=0.1582, coverage=0.838
- **EC-HTE: abs_bias=0.0643, RMSE=0.0858, coverage=0.953**
- Global CM: abs_bias=0.0643, RMSE=0.0806, coverage=0.938
- Naive: abs_bias=0.0621, coverage=0.858

---

### Remaining Experiments (not specifically requested but present in registry)

**exp-006** — HB Crossover Point: crossover K2/extreme=250, K4/extreme=1000, K4/moderate=2000. HB≥MLE in 87.5% configs.

**exp-007** — EC-HTE + PPCI Complementarity: DGP_C ec_hte_ppci bias=0.005 (35× better than ec_hte alone). Coverage always 1.0.

**exp-007b** — HB Backfill: killed (Director decision, PPCI story is complementarity, not HB vs MLE)

**exp-010** — Subgroup Misspecification Robustness: HB coverage ≥94.5% across all noise levels 0-50%. Graceful convergence to global at 50% noise.

**exp-012** — GPT-4.1 TweetEval Pilot: accuracy binary=0.858, Δπ=0.200, hash presence increases misclassification.

**exp-018** — Multiplicative DGP: EC-HTE RMSE=0.068 (52% reduction vs naive 0.142), coverage=0.955. Robust to non-additive treatment effects.

**exp-020** — κ Condition Number: max cond=1.89, guard never triggers in moderate regime. κ=100 validated as safe default.

**exp-021** — Table 1 Stability (50→100 MC seeds): 84% cells <5% change, 99% <10%. Only outlier K4/extreme/n100/HB.

**exp-022** — Hyperprior Sensitivity: RMSE range 6.0% across reasonable configs, coverage 0.925-0.938. Gamma(3,1) rank 8/15.

**exp-026** — Low Budget HB: crossover K2 at n=50 (HB -16.1%), K4 at n=75 (HB -4.4%). Below these, global outperforms.

**exp-027** — CF Oracle Coverage K=4: Oracle 94.5%, EC-HTE true CM 92.5%, estimated 93.1%. CF SE well-calibrated, M⁻¹ propagation costs ~2pp.

**exp-029** — A1 Sensitivity (outcome-dependent misclass): EC-HTE coverage 95.5%→93.5% over γ=0→0.2 (-2.0pp). All methods ≥90% across all γ.

**exp-030** — K=8 Full: HB RMSE=0.340 (worse than global 0.168), coverage=0.956. HB 47% better than MLE but K=8 is boundary.

**exp-031** — Confounded Treatment + IPW: EC-HTE+IPW coverage=0.950, global=0.930, naive=0.863. β=0.5 confounding.

**exp-032** — Confounding Sweep: All 8 configs (β=0.25-2.0, oracle/estimated) HB coverage ≥94.5%. Oracle vs estimated gap ≤1pp.

**exp-033** — K=8 Adaptive: Adaptive alpha reduces RMSE 35% (0.333→0.216) but still exceeds global (0.166). Gap narrowed 2×→1.3×.

---

### Paper Claim Verification

| Paper Claim | Registry Source | Registry Value | Match? |
|---|---|---|---|
| R²≥0.97 | exp-002 | K2=0.9939, K4=0.9738 | YES (K4=0.974 rounds to 0.97) |
| R²≥0.97 (across P(Z=1)) | exp-019 | 0.976-0.998 | YES (all ≥0.976) |
| R² overall (11 CMs) | exp-024 | 0.975 | YES |
| 14.9% sign reversal at τ(0)=0.03 | exp-038 | reversal_pct_tau003=14.9 | EXACT MATCH |
| 260/520 configurations | exp-002 | "260/520 (excluding dc=0)" | EXACT MATCH |
| 2.86× amplification (K=2) | exp-002 | max_bias_ratio_k2=2.86 | EXACT MATCH |
| 2.41× amplification (K=4) | exp-002 | max_bias_ratio_k4=2.41 | EXACT MATCH |
| bias 0.059→0.008 | exp-039 | K2_echte_bias=0.008; 0.059 likely from exp-029 echte_abs_bias g0.00=0.0596 or exp-035 naive_abs_bias=0.0592 | PARTIAL (0.008 confirmed, 0.059 context-dependent) |
| 93.8% coverage | exp-036 | plugin_coverage=0.9375 | EXACT MATCH (also exp-039 K2_echte_cov=0.938) |
| AUC 1.0/0.86/0.63 | exp-005 + exp-028 | exp-005 subgroup AUC=0.833 (close to 0.86); exp-028 overall symmetric=0.626 (close to 0.63); AUC=1.0 from exp-028 K4 perfect combos | APPROXIMATE (0.833≈0.86? possibly different subsets) |
| 11 empirical CMs | exp-024 | n_llm_dataset_combos=11 | EXACT MATCH |
| 89% R-learner bias reduction | exp-017 | notes: "89% reduction" (0.121→0.013) | EXACT MATCH |
| 5.9× factor | exp-011 | debiasing_hurts_max_ratio=5.9 | EXACT MATCH |
| 5× bias reduction | Not directly stored | Closest: exp-014 bias_reduction=4.2×, exp-013 amplification=4.4× | NOT FOUND as exact "5×" |
| 7.4× bias reduction | Not found in registry | — | NOT FOUND |
| 4.7×, 4.9× factors | Not found in registry | exp-026 has "+4.9%" (delta_pct, not bias ratio) | NOT FOUND as bias ratios |
| γ_T=0.10 → 75% coverage | exp-040 | gamma010_cov=0.750 | EXACT MATCH |

**Summary of unverifiable claims from registry alone**: The 5×, 7.4×, 4.7×, and 4.9× bias reduction/amplification factors are not stored as metrics in the registry. They are likely computed from detailed per-configuration results in the CSV artifact files (e.g., `results/exp001_hb_results_v2.csv`, Table 1 data) rather than summarized in the registry. The registry stores aggregate or representative metrics, not every cell of every results table.

agentId: a4587c47dc95cd896 (use SendMessage with to: 'a4587c47dc95cd896' to continue this agent)
&lt;usage>total_tokens: 60258
tool_uses: 20
duration_ms: 345151&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "2d439a6d-bbea-4b0e-bfd4-8660b924840d",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to extract key metrics from a registry JSON file for a number audit of a paper. The file is at:\n/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-projects-ec-hte-llm-annotation/c1f80a8b-6c5e-4a54-90d1-41867c4cf47e/tool-results/mcp-agent-ml-research-read_registry-1779596955296.txt\n\nThis is JSON with schema: {result: string}. The result field is a string containing the actual registry data.\n\nI need you to extract ALL metrics and conclusions from these specific experiment IDs (and any others you find):\n- exp-001, exp-002, exp-003, exp-008, exp-019, exp-023, exp-035, exp-036, exp-037, exp-038, exp-039, exp-040\n- Any experiments related to stance_detection, sign_reversal, bias_identity, diagnostic, causal_forest, r_learner, hatespeech, asymmetric\n\nFor each experiment found, report:\n1. exp_id\n2. title/description\n3. All metrics (R², bias values, RMSE, coverage, AUC, sign reversal rates, amplification factors, etc.)\n4. conclusion/status\n5. Any key numbers that appear in the experiment\n\nThe paper claims these numbers:\n- R²≥0.97\n- 14.9% sign reversal at τ(0)=0.03\n- 5×, 7.4× bias reduction\n- AUC 1.0/0.86/0.63\n- 11 empirical CMs\n- bias 0.059→0.008\n- 93.8% coverage\n- 260/520 configurations\n- 2.86×, 2.41× amplification\n- 89% R-learner bias reduction\n- 4.7×, 4.9×, 5.9× factors\n- γ_T=0.10 → 75% coverage\n\nPlease probe the structure first with jq, then extract all experiments. Report everything verbatim - do not summarize away any numbers.",
    "agentId": "a4587c47dc95cd896",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have everything. Here is the complete extraction:\n\n---\n\n## Complete Registry Extraction — All 42 Experiments\n\n### Specifically Requested Experiments\n\n**exp-001** — HB Synthetic Validation\n- Status: DONE, conclusion: success\n- Hypothesis: HB Dirichlet-prior CM estimator via partial pooling outperforms MLE/Laplace at small n_expert\n- Metrics:\n  - MCMC: rhat_max=1.024, ess_min=129, divergent=0, total_mc_runs=3600\n  - HB vs MLE RMSE improvement: K2/n50: 4-9%, K2/n100: 1-2%, K4/n50/moderate: 6-9%\n  - HB coverage: min=0.87, median=0.93\n  - 4-chain MCMC fix: rhat_max=1.0034, ess_min=1618 (~4x improvement)\n    - K4/extreme/n50/A rmse: 3.14→0.99, B rmse: 509.93→0.27, n100/A rmse: 11.57→0.29\n    - Singularity guard: triggers in extreme/n=50 only (2 HB, 3 MLE / 100 runs)\n  - Hyperprior sensitivity: scale range 0.5-2.0, K2 RMSE variation <1%, K4 ~4-5%, coverage invariant, conclusion: robust\n  - Runtime: 69 min\n\n**exp-002** — Bias Bound / Theorem 1\n- Status: DONE, conclusion: success\n- Hypothesis: Global correction bias follows analytic formula bias ∝ Δ_misclass × Δ_CATE; parameter regions exist where |bias_global| > |bias_naive|\n- Metrics:\n  - **R²: K2=0.9939, K4=0.9738**\n  - Tightness ratio: K2 median=1.0027, K4 median=1.0234\n  - **Debiasing hurts: 50% of configs (260/520, excluding dc=0)**\n  - Debiasing hurts threshold Δmisclass: 0.1235\n  - **Max bias ratio: K2=2.86×, K4=2.41×**\n  - Coverage 2SE: K2=0.951, K4=0.940\n\n**exp-003** — TweetEval Semi-Synthetic\n- Status: DONE, conclusion: success\n- 4 subgroups, misclass rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25, sizes ~38%/38%/12%/12%, P(Z=1)=0.39\n- Debiasing hurts confirmed: true, 100 MC runs\n- HB vs MLE summary:\n  - n50/S3/extreme: -57% RMSE (HB worse), n50/S3/moderate: -54%\n  - n100/S3/extreme: +60% (HB dramatically better), n100/S3/moderate: +24%\n  - n100/S2: +5-8%, n250/S3: +5-17%, n500/all: +0.2-1.6% (converged)\n- Boundary: n_expert≥100 recommended; n=50 with extreme heterogeneity degrades moderately\n\n**exp-008** — Multi-LLM Persistence\n- Status: DONE, conclusion: success\n- 6 models: gpt-3.5-turbo, gpt-4.1, gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-5.4\n- **Effective Δπ**: gpt-3.5-turbo=0.198, gpt-4-turbo=0.149, gpt-4.1=0.098, gpt-4o=0.080, gpt-4o-mini=0.136, gpt-5.4=0.114\n- All Δπ > 0.05: **true** — heterogeneity is structural\n- Filtered analysis excluded False_long (n=6) and True_long (n=4), retained 4 subgroups with n≥10\n- Spearman significant pairs: 4 pairs at ρ=1.000\n\n**exp-019** — P(Z=1) Sweep\n- Status: DONE, conclusion: success\n- **Theorem 1 R²**: K2 range 0.989-0.998, K4 range 0.976-0.992 — **all >0.95**\n- RMSE ratio HB/Global: K2 wins all (0.76-0.92), K4 HB loses all (1.06-1.68)\n- Coverage: HB 0.92-0.94 (near-nominal), naive 0.65-0.79, global 0.79-0.90\n\n**exp-023** — Heterogeneous-τ DGP\n- Status: DONE, conclusion: success\n- N=5000, P(Z=1)=0.652, K=4, Δτ: False_medium=0.1, False_short=0.1, True_medium=0.3, True_short=0.6\n- EC-HTE bias wins: 3/3 budgets\n  - n200: 32% reduction (0.0248 vs 0.0365)\n  - **n500: 68% reduction (0.0099 vs 0.0314)**\n  - n1000: 55% reduction (0.0130 vs 0.0286)\n- RMSE: True_short z0 n1000: global=0.2577, echte=0.2117 (-17.8%)\n- Aggregate RMSE: EC-HTE loses (variance cost in low-Δτ subgroups)\n\n**exp-035** — Asymmetric CM (7:1 FPR/FNR)\n- Status: DONE, conclusion: success\n- EC-HTE asymmetric: abs_bias=0.057, RMSE=0.0735, **coverage=0.945**\n- EC-HTE symmetric: abs_bias=0.0618, RMSE=0.0831, coverage=0.930\n- Global asymmetric: abs_bias=0.0609, coverage=0.915\n- Naive: abs_bias=0.0592, coverage=0.870\n- Oracle: abs_bias=0.0454, coverage=0.943\n- Asymmetric vs symmetric EC-HTE: RMSE improved 11.5% (0.0831→0.0735), coverage +1.5pp\n\n**exp-036** — Bootstrap SE\n- Status: DONE, conclusion: success\n- **Plugin coverage: 0.9375 (93.8%)**\n- **Bootstrap coverage: 0.950 (95.0%)**\n- Oracle coverage: 0.900\n- SE ratio boot/plugin: 1.154\n- s1 (high-error): plugin 0.925, bootstrap 0.975, SE ratio 1.222\n- n_mc=20, n_bootstrap=100, n_estimators=200, runtime=1716s\n- Key: v1's \"81.7%→94.2%\" gap was artifact of n_estimators=48\n\n**exp-037** — Temperature Calibration\n- Status: DONE, conclusion: success\n- Calibrated+EC-HTE: abs_bias=0.0554, **coverage=0.965**\n- Calibrated+Global: abs_bias=0.0550, coverage=0.963\n- Calibrated+Naive: abs_bias=0.0510, coverage=0.912\n- Uncalibrated+EC-HTE: abs_bias=0.0641, coverage=0.938\n- Uncalibrated+Global: abs_bias=0.0695, coverage=0.920\n- Uncalibrated+Naive: abs_bias=0.0634, coverage=0.840\n- Oracle: abs_bias=0.0431, coverage=0.963\n- **Δπ: uncalibrated=0.20, calibrated=0.07**\n- Conclusion: calibration and EC-HTE are complementary, not substitutes\n\n**exp-038** — Sign Reversal / Policy Reversal\n- Status: DONE, conclusion: success\n- **reversal_pct at τ=0.01: 31%**\n- **reversal_pct at τ=0.03: 14.9%**\n- **reversal_pct at τ=0.05: 6.1%**\n- reversal_pct at τ=0.10: 0%\n- **EC-HTE reversal: 0%**\n- Worst combo: τ=0.01, delta_misclass=0.19 → 42.9%\n\n**exp-039** — K Scaling (K=2/4/8)\n- Status: DONE, conclusion: success\n- **K2: bias=0.008, RMSE=0.089, coverage=0.938**\n- K4: bias=0.012, RMSE=0.120, coverage=0.956\n- K8: bias=0.183, RMSE=0.340, coverage=0.956\n- K8 global RMSE: 0.168 (EC-HTE loses at K=8)\n\n**exp-040** — Treatment-Dependent Misclassification\n- Status: DONE, conclusion: success\n- γ=0.00: coverage=0.945, RMSE=0.075\n- γ=0.05: coverage=0.897, RMSE=0.092\n- **γ=0.10: coverage=0.750, RMSE=0.133**\n- γ=0.15: coverage=0.525, RMSE=0.177\n- γ=0.20: coverage=0.370, RMSE=0.224\n- **Breakeven γ: 0.10**\n\n---\n\n### Keyword-Matched Experiments\n\n**exp-004** — Hate Speech (UC Berkeley) [hate_speech]\n- Status: DONE, conclusion: success\n- Dataset: UC Berkeley Measuring Hate Speech, n=2496\n- Δπ=0.117, global FPR=0.139, global FNR=0.533\n- Subgroup misclass: plat0_long=0.266, plat0_short=0.337, plat23_long=0.303, plat23_short=0.383\n- Avg abs bias: naive=0.210, global=0.273, ec_hte=0.313\n- EC-HTE fails here due to extreme FNR (~53%) — near-random for positive class\n\n**exp-005** — Diagnostic Criterion [diagnostic]\n- Status: DONE, conclusion: success\n- **Subgroup-level AUC: 0.833**\n- Subgroup correlation: 0.86\n- **Setting-level AUC: 0.49**\n- Low-π hurt%: 84.6%, High-π hurt%: 15.4%\n\n**exp-011** — CausalForest Integration [causal_forest]\n- Status: DONE, conclusion: success\n- 100 MC, 8 configs, 144 total rows\n- Mean abs bias: naive_forest=0.1558, global_forest=0.1073, ec_hte_forest=0.0608\n- Mean RMSE: naive=0.1782, global=0.1659, ec_hte=0.2289\n- **Debiasing hurts cases: 9, max ratio: 5.9×** (K=4/extreme/sg0: global 5.9× worse than naive)\n- K2/n500 EC-HTE bias range: 0.004-0.013 (near zero)\n\n**exp-013** — Budget Threshold [amplification]\n- Status: DONE, conclusion: success\n- Config: K=4/extreme/n_expert=50 (12.5 per subgroup)\n- RMSE: naive=0.109, global=0.140, MLE=0.280, EB=0.292\n- Worst subgroup: A(π=0.30) EB RMSE=0.62\n- **Amplification max: 4.4×** (A/EB vs global)\n- Debiasing hurts D: Naive bias=0.001, Global bias=0.110\n\n**exp-014** — Asymmetric Misclassification Theory [asymmetric]\n- Status: DONE, conclusion: success\n- R² analytic vs MC: 0.992, product structure confirmed\n- EC-HTE: avg abs bias=0.006, RMSE=0.033, coverage=0.900\n- Global: avg abs bias=0.025, RMSE=0.040, coverage=0.780\n- **Bias reduction vs global: 4.2×**, coverage improvement: +12pp\n\n**exp-015** — Realistic Asymmetric CMs (GPT-4.1) [asymmetric]\n- Status: DONE, conclusion: **negative**\n- S0 FNR=0.526, worst CM row near-uniform → inversion amplifies noise\n- HB worse than global at all n_expert (100/250/500)\n- RMSE n500: naive=0.123, global=0.196, HB=0.260\n- Root cause: P(Z=1)=0.18 + FNR≈0.5\n\n**exp-016** — Realistic Asymmetric CMs (gpt-3.5-turbo) [diagnostic, asymmetric]\n- Status: DONE, conclusion: **negative**\n- Worst FNR=0.211 but FPR=0.393\n- HB worse than global at all n_expert\n- Root cause: FPR variance 0.143-0.393 + P(Z=1)=0.18\n\n**exp-017** — R-Learner Generalization [causal_forest, r-learner]\n- Status: DONE, conclusion: success\n- R-learner: naive bias=0.121, ec_hte bias=0.013, coverage: 0.47→0.92\n- **EC-HTE bias reduction: 9.3× (R-learner), 89% reduction**\n- CausalForest comparison: ec_hte bias=0.008, coverage=0.91\n- Pattern consistent across estimators\n\n**exp-024** — Bias Identity with Real CMs [bias_identity, asymmetric]\n- Status: DONE, conclusion: success\n- **R² overall: 0.975**\n- **n_llm_dataset_combos: 11**\n- Data sources: exp023 CMs + c1_multi_llm profiles\n\n**exp-025** — Proposition 3 Diagnostic Screening [diagnostic]\n- Status: DONE, conclusion: success\n- Screening: 0/16 combos pass all conditions (κ≤1.25 bottleneck)\n- Oracle screening: HB wins 41/52 comparisons on aggregate RMSE\n- HB vs MLE: HB beats MLE in 52/52 comparisons\n- Open-source LLMs: all 4 (Llama/Qwen/Mistral/Gemma) HB wins 32/32 on TweetEval\n\n**exp-027b** — CF Oracle Coverage K=2 [amplification]\n- EC-HTE estimated CM: coverage=0.925, bias=0.0044, RMSE=0.079\n- Oracle true Z: coverage=0.940, bias=0.0023, RMSE=0.056\n- Naive: coverage=0.828\n\n**exp-027c** — CF Oracle Coverage MF2 DGP [asymmetric, amplification]\n- EC-HTE estimated: coverage=0.923, bias=0.100, RMSE=0.111\n- Oracle: coverage=0.960, bias=0.077, RMSE=0.091\n- Naive: coverage=0.773\n\n**exp-028** — Asymmetric Diagnostic AUC [diagnostic, asymmetric]\n- Status: DONE, conclusion: **negative**\n- **Overall symmetric AUC: 0.626**\n- **Overall asymmetric AUC: 0.611**\n- K4 perfect AUC combos: Llama/Qwen/Mistral/gpt-4o on TweetEval (AUC=1.0)\n- K2 all AUC zero (degenerate)\n\n**exp-034** — F-L Scalar Comparison [sign_reversal]\n- Status: DONE, conclusion: success\n- F-L scalar: abs_bias=0.0909, RMSE=0.1161, coverage=0.850\n- F-L per-subgroup: abs_bias=0.112, RMSE=0.1582, coverage=0.838\n- **EC-HTE: abs_bias=0.0643, RMSE=0.0858, coverage=0.953**\n- Global CM: abs_bias=0.0643, RMSE=0.0806, coverage=0.938\n- Naive: abs_bias=0.0621, coverage=0.858\n\n---\n\n### Remaining Experiments (not specifically requested but present in registry)\n\n**exp-006** — HB Crossover Point: crossover K2/extreme=250, K4/extreme=1000, K4/moderate=2000. HB≥MLE in 87.5% configs.\n\n**exp-007** — EC-HTE + PPCI Complementarity: DGP_C ec_hte_ppci bias=0.005 (35× better than ec_hte alone). Coverage always 1.0.\n\n**exp-007b** — HB Backfill: killed (Director decision, PPCI story is complementarity, not HB vs MLE)\n\n**exp-010** — Subgroup Misspecification Robustness: HB coverage ≥94.5% across all noise levels 0-50%. Graceful convergence to global at 50% noise.\n\n**exp-012** — GPT-4.1 TweetEval Pilot: accuracy binary=0.858, Δπ=0.200, hash presence increases misclassification.\n\n**exp-018** — Multiplicative DGP: EC-HTE RMSE=0.068 (52% reduction vs naive 0.142), coverage=0.955. Robust to non-additive treatment effects.\n\n**exp-020** — κ Condition Number: max cond=1.89, guard never triggers in moderate regime. κ=100 validated as safe default.\n\n**exp-021** — Table 1 Stability (50→100 MC seeds): 84% cells <5% change, 99% <10%. Only outlier K4/extreme/n100/HB.\n\n**exp-022** — Hyperprior Sensitivity: RMSE range 6.0% across reasonable configs, coverage 0.925-0.938. Gamma(3,1) rank 8/15.\n\n**exp-026** — Low Budget HB: crossover K2 at n=50 (HB -16.1%), K4 at n=75 (HB -4.4%). Below these, global outperforms.\n\n**exp-027** — CF Oracle Coverage K=4: Oracle 94.5%, EC-HTE true CM 92.5%, estimated 93.1%. CF SE well-calibrated, M⁻¹ propagation costs ~2pp.\n\n**exp-029** — A1 Sensitivity (outcome-dependent misclass): EC-HTE coverage 95.5%→93.5% over γ=0→0.2 (-2.0pp). All methods ≥90% across all γ.\n\n**exp-030** — K=8 Full: HB RMSE=0.340 (worse than global 0.168), coverage=0.956. HB 47% better than MLE but K=8 is boundary.\n\n**exp-031** — Confounded Treatment + IPW: EC-HTE+IPW coverage=0.950, global=0.930, naive=0.863. β=0.5 confounding.\n\n**exp-032** — Confounding Sweep: All 8 configs (β=0.25-2.0, oracle/estimated) HB coverage ≥94.5%. Oracle vs estimated gap ≤1pp.\n\n**exp-033** — K=8 Adaptive: Adaptive alpha reduces RMSE 35% (0.333→0.216) but still exceeds global (0.166). Gap narrowed 2×→1.3×.\n\n---\n\n### Paper Claim Verification\n\n| Paper Claim | Registry Source | Registry Value | Match? |\n|---|---|---|---|\n| R²≥0.97 | exp-002 | K2=0.9939, K4=0.9738 | YES (K4=0.974 rounds to 0.97) |\n| R²≥0.97 (across P(Z=1)) | exp-019 | 0.976-0.998 | YES (all ≥0.976) |\n| R² overall (11 CMs) | exp-024 | 0.975 | YES |\n| 14.9% sign reversal at τ(0)=0.03 | exp-038 | reversal_pct_tau003=14.9 | EXACT MATCH |\n| 260/520 configurations | exp-002 | \"260/520 (excluding dc=0)\" | EXACT MATCH |\n| 2.86× amplification (K=2) | exp-002 | max_bias_ratio_k2=2.86 | EXACT MATCH |\n| 2.41× amplification (K=4) | exp-002 | max_bias_ratio_k4=2.41 | EXACT MATCH |\n| bias 0.059→0.008 | exp-039 | K2_echte_bias=0.008; 0.059 likely from exp-029 echte_abs_bias g0.00=0.0596 or exp-035 naive_abs_bias=0.0592 | PARTIAL (0.008 confirmed, 0.059 context-dependent) |\n| 93.8% coverage | exp-036 | plugin_coverage=0.9375 | EXACT MATCH (also exp-039 K2_echte_cov=0.938) |\n| AUC 1.0/0.86/0.63 | exp-005 + exp-028 | exp-005 subgroup AUC=0.833 (close to 0.86); exp-028 overall symmetric=0.626 (close to 0.63); AUC=1.0 from exp-028 K4 perfect combos | APPROXIMATE (0.833≈0.86? possibly different subsets) |\n| 11 empirical CMs | exp-024 | n_llm_dataset_combos=11 | EXACT MATCH |\n| 89% R-learner bias reduction | exp-017 | notes: \"89% reduction\" (0.121→0.013) | EXACT MATCH |\n| 5.9× factor | exp-011 | debiasing_hurts_max_ratio=5.9 | EXACT MATCH |\n| 5× bias reduction | Not directly stored | Closest: exp-014 bias_reduction=4.2×, exp-013 amplification=4.4× | NOT FOUND as exact \"5×\" |\n| 7.4× bias reduction | Not found in registry | — | NOT FOUND |\n| 4.7×, 4.9× factors | Not found in registry | exp-026 has \"+4.9%\" (delta_pct, not bias ratio) | NOT FOUND as bias ratios |\n| γ_T=0.10 → 75% coverage | exp-040 | gamma010_cov=0.750 | EXACT MATCH |\n\n**Summary of unverifiable claims from registry alone**: The 5×, 7.4×, 4.7×, and 4.9× bias reduction/amplification factors are not stored as metrics in the registry. They are likely computed from detailed per-configuration results in the CSV artifact files (e.g., `results/exp001_hb_results_v2.csv`, Table 1 data) rather than summarized in the registry. The registry stores aggregate or representative metrics, not every cell of every results table."
      }
    ],
    "totalDurationMs": 345151,
    "totalTokens": 60258,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 52571,
      "output_tokens": 6030,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1656
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6030,
          "cache_read_input_tokens": 52571,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1656,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 18,
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

_source line 103_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me read the remaining parts of appendix.tex and then compile the audit report. I still need to read parts of appendix.tex that cover additional experiments. Let me also check which numbers I still need to trace.

Let me compile the audit report now based on all the data collected. Let me also check the remaining appendix sections I haven't read yet.

Let me now compile the full audit report. I have:

1. All tex files read (abstract, introduction, theory, method, experiments, conclusion, appendix (lines 1-1199), appendix_stance, limitations)
2. Registry data fully parsed by the subagent


3. Now I'm systematically cross-referencing every number in the paper against the registry data to verify accuracy. Starting with the abstract numbers: the R² values, the 14.9% reversal percentage at τ(0)=0.03, and the 5× improvement claim all need to be traced back to their experimental sources.

4. For the 7.4× bias reduction figure, I'm checking the calculation: the global bias of 0.059 divided by the HB EC-HTE bias of 0.008 gives 7.375, which rounds to 7.4×. These values come from Table 1 in experiments.tex, and the corresponding registry entry is exp-039.

5. Now I'm tracing the AUC values more carefully — the 0.63 appears across 16 semi-synthetic LLM-dataset combinations, the 0.86 is specifically on synthetic grids when restricting to subgroups with Δτ > 0, and the 1.0 is the maximum achieved under that same restriction. I need to match these against the registry entries to verify which experiments correspond to each metric. There's a clear mismatch here — the registry shows subgroup-level AUC of 0.833, but the paper's ROC figure caption reports 0.86 for the Δπ-only condition. I'm also noticing the setting-level values don't align either: the registry has 0.49 while the paper shows 0.89. These could be different diagnostic variants or conditions, but I need to figure out which metrics correspond to which experimental setup. Looking at the ROC figure caption and registry data, I see that exp-005 reports a subgroup-level AUC of 0.833, which is close to but not exactly the 0.86 claimed in the paper for the Δπ-only condition on synthetic subgroups. This could indicate the diagnostic experiment was refined or recalculated after the paper was written. Meanwhile, exp-028 shows an overall symmetric AUC of 0.626, which aligns with the paper's reported 0.63 on real LLM error profiles, suggesting these experiments correspond to different evaluation sets mentioned in the abstract. Now I'm verifying the bias reduction metrics from Table 1 — the global correction shows 0.059, HB EC-HTE brings it down to 0.008 for a 7.4× improvement, and at K=4 the reduction from 0.056 to 0.012 yields the 4.7× factor, all matching the reported values. Continuing to verify the remaining metrics from the paper against the registry data — checking the R-learner coverage claim at 89% and working through the final validation points.

Now I'm cross-referencing Table 1 against the experimental results, starting with the K=2 configurations across all methods to ensure the bias and coverage numbers align with what's recorded. The theory section confirms these numbers—it explicitly states the F-L scalar correction increases bias to 0.122 and per-subgroup to 0.168, which matches Table 1 exactly. These specific values are tied to the extreme configuration (DIM, K=2, n=250) rather than being stored as separate registry metrics. Now looking at the K=4 DIM results, I see the naive, global, and stratified MLE approaches with their respective bias, RMSE, and coverage values.

For the HB EC-HTE method, the registry entry exp-039 shows bias of 0.012, RMSE of 0.120, and coverage of 0.956, which rounds to the 0.96 reported in the table. Checking the CausalForest results, the naive and global approaches show substantially higher bias (0.208 and 0.191) compared to EC-HTE Forest at 0.039, but when I cross-reference with the registry entries, the absolute bias values don't align perfectly—the registry shows 0.1558 for naive forest versus the table's 0.208. The 5.9× amplification is a maximum across all eight configurations tested in exp-011, not specific to this K=4/extreme case. The introduction correctly attributes this to K=4 with CausalForest. Now I'm verifying the theory.tex numbers against the registry — the γ_T=0.10 case shows 75% coverage matching exp-040, and I'm checking the F-L scalar progression from 0.058 to 0.122.

For method.tex, there's a potential discrepancy where the paper claims ≤4% RMSE robustness to perturbations, but the registry shows 6% across reasonable configurations — I need to determine if these are measuring different things or if there's an actual inconsistency. I'm noticing there's a discrepancy between how the paper states the robustness claim—one place says "≤4%" while another says "<5%"—and the registry data shows K4 at 4-5%, which technically satisfies the looser bound but potentially violates the stricter one. This looks like an internal inconsistency I should flag.

Now I'm checking the coverage claims across the document. The paper cites ≥93% coverage in multiple locations, and I'm tracing where this comes from—it appears to be grounded in the kappa analysis appendix, which reports calibrated coverage of at least 93% across different κ bins when the number of experts is sufficiently large. The registry data from the kappa analysis experiments seems to support this threshold.

Moving through the introduction numbers, I'm verifying each claim: the 5× misclassification rate variation is a literature citation from Ashwin et al., the 14.9% figure matches what's in the abstract and registry experiment exp-038, the 31% reversal percentage at τ(0) = 0.01 also traces back to exp-038, and now I'm checking the estimated treatment effect of -0.059.

This value comes from the sign reversal analysis in an extreme case where the true treatment effect is +0.03 but the estimate flips to -0.059. The bias here is -0.089, which represents a specific configuration rather than an average across conditions. Figure 1 caption confirms this is the extreme case scenario being illustrated.

Now I'm cross-checking the other key numbers from the introduction against the registry and supporting materials. The 5.9× multiplier from exp-011 checks out, as does the 2.9× bias increase from the Frazis-Loeb method which matches the theory calculations. The 7.5% sign reversal rate comes from the figure data, and the reduction from 0.059 to 0.008 bias aligns with Table 1. The R² threshold of 0.97 or higher appears consistently across multiple experiments in the registry.

Moving into the appendix tables, I'm verifying the stance analysis numbers: the Global category shows 4 out of 30 sign reversals (13.3%), the EC-HTE subset has just 1 out of 30 (3.3%), and about half of the estimates show bias amplification. The kappa values are also documented there.

Now checking cross-location consistency in Section B — the R² threshold of at least 0.97 appears consistently across the abstract, introduction, and theory sections, with specific values like 0.994 for K=2 and 0.97 for K=4 matching across multiple files. The 14.9% sign reversal rate is also being verified across documents. Now I'm checking the AUC values across all the sections to make sure they're reported consistently—the pattern holds with 1.0 appearing on subgroups with heterogeneity, 0.86 at the subgroup level on synthetic data, and 0.63 degrading to real LLM results.

Wait, I'm noticing the registry experiment exp-005 shows a subgroup AUC of 0.833, which doesn't match the 0.86 reported in the paper—that's a discrepancy I need to flag.

For the 7.4× bias reduction claim, the numbers check out: the abstract states 7.4×, the intro shows the calculation from 0.059 to 0.008 which is 7.375×, and the experiments section confirms this with the same values, so that's consistent when rounded.

The 5× variation across subgroups appears in both the abstract and intro as a literature citation to Ashwin et al., so that's consistent too.

The bias values 0.059 and 0.008 appear consistently across the intro, experiments, and Table 1, though theory.tex mentions different values in a separate context, which is fine since it's discussing a different comparison.

Now I'm checking the F-L values... I'm verifying the 5.9× amplification factor appears consistently across the introduction and experiments sections, and checking that the 260/520 split with its corresponding amplification rates of 2.86× and 2.41× are reported identically in theory and experiments. The CausalForest coverage metric of 93.8% is also confirmed across multiple document sections.

Now I'm cross-referencing the γ_T=0.10 parameter with its 75% coverage degradation result against the experimental registry, and I'm noticing some inconsistency in how RMSE variation is reported—method.tex claims ≤4% while the appendix breaks it down more granularly by K value, with K=4 showing 4-5% variation. but appendix says 4-5% for K4, and method.tex:21 says <5%. The ≤4% claim in line 12 is inconsistent with the 4-5% in the appendix.

The PPCI composition results check out—method.tex and appendix both show the |bias| reduction from 0.179 to 0.007, which matches the table values perfectly.

For the R-learner's 89% bias reduction, I'm verifying this across multiple sources: the experiments file claims 89%, the appendix confirms it, and the math checks out (1 - 0.013/0.121 ≈ 89%).

Now I'm cross-referencing the introduction claim about GPT-4.1's 85.8% accuracy on TweetEval sentiment against the registry data to verify those error rate ranges. I'm noticing the registry might be using a different subgroup structure—possibly K=6 instead of K=4—which would explain why the Δπ values diverge between the pilot study's 0.098 and the registry's 0.200. The math checks out for the pilot study—the 9.8 percentage point difference between the extreme subgroups matches the reported Δπ=0.098—but the registry's Δπ=0.200 suggests it's measuring something different, possibly across a broader set of subgroup comparisons or using a different definition entirely. This discrepancy needs to be flagged as a potential inconsistency between what the intro reports and what's stored in the registry. So exp-008's filtered analysis of GPT-4.1 across the 4 retained subgroups gives Δπ=0.098, which matches what the intro reports. The registry's exp-012 with Δπ=0.200 likely comes from a broader analysis using all K=4 subgroups in the semi-synthetic setup, whereas the intro is citing the more refined filtered result from exp-008.

The specific error rates of 10.2% to 20.0% aren't directly in the registry but are consistent with the Δπ value—the 9.8 percentage point spread matches exactly. And I'm verifying the other claims: exp-038 confirms the 31% reversal rate at τ=0.01, and now I need to check the statement about all eight real LLMs amplifying bias under global correction while EC-HTE eliminates sign reversal.

Wait, there's a discrepancy with the model count. The experiments file lists 8 LLMs, but when I count them out—GPT-3.5-turbo, GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, Llama-3.1-8B, Qwen-2.5-7B, Gemma-2-9B, Mistral-7B—that's actually 9 models, not 8. The 11 CMs refers to the 11 model-dataset-K combinations with sufficient subgroup variation out of the 16 total combinations tested. I'm recounting the models more carefully: the TweetEval experiments use 8 models total (5 proprietary OpenAI models plus 3 open-source ones), while Civil Comments uses only 3 models, giving 11 experimental combinations overall. Llama-3.1-8B appears in other appendix analyses but wasn't part of the main real CM validation, so the core count stays at 8 unique models. I'm noticing a discrepancy in the model counts across different sections — the appendix_multilm table shows 10 total models (6 OpenAI plus 4 open-source), but the real CM validation only uses 8 models, excluding GPT-5.4 and Llama from that core validation set.

Now looking at the experiments.tex claim of "8 LLMs × 2 datasets = 16 combinations," but the appendix shows 8 models tested on TweetEval and only 3 on Civil Comments, which doesn't match that multiplication — the "varying K" parameter must account for the additional combinations mentioned. So the 16 combinations break down across different K values for the same models and datasets, with 8 unique LLMs tested on 2 datasets. The 11 rows in the R² regression table represent the subset with sufficient subgroup variation. Now I'm checking the claim that all eight real LLMs amplify bias under global correction—the experiments and semi-synthetic analysis support this across the sign reversal context, though I'm noticing that EC-HTE actually underperforms in the hate speech appendix, which seems to complicate that claim.

Let me verify the 7.5% subgroup-level estimate reversal rate mentioned in Figure 1, which is distinct from the 14.9% configuration-level rate. And I'm checking the theory section's claim about AUC dropping from 0.86 to 0.66 in the asymmetric appendix.

Now I'm noticing a discrepancy: the theory text cites 0.66 as the asymmetric AUC, but the registry shows 0.611 for overall asymmetric AUC and 0.626 for symmetric. The 0.86 appears to be from synthetic data, so I need to reconcile whether 0.66 is a theoretical bound or if there's a mismatch with the empirical results. I'm noticing the 0.66 comes from synthetic asymmetric data while the 0.611 is from real LLM diagnostics—different experimental setups, so not necessarily contradictory. The registry doesn't seem to have a separate entry for the synthetic asymmetric AUC metric, so I'll mark this as something to verify but not a definitive discrepancy. Now looking at the rounding patterns in Section C, where most bias values stick to three decimal places. I notice the multiplier inconsistency is minor—the two-decimal values are specific data points while the one-decimal ones are derived ratios. Now I'm ready to write the comprehensive audit report, but first I want to clarify something about the notation: the abstract references "5×" from Ashwin et al. as a literature comparison for error rate variation across subgroups, which is distinct from the experimental bias amplification factors like 5.9× and 7.4× mentioned in the introduction.

The abstract's claim about reducing bias by 7.4× checks out—that's 0.059 divided by 0.008. However, I'm noticing a small discrepancy in the R² values: theory.tex reports 0.991 for the asymmetric case while the registry shows 0.992, and there's also a mismatch with the K=2 scenario at P(Z=1)=0.1 where the paper states R² ≥ 0.976 but the registry shows 0.998.

Looking at the imbalance sweep data, the RMSE ratio range of 1.06–1.68 for EC-HTE matches what's claimed in theory.tex, and the minimum R² across all conditions does appear to be 0.976 as stated. I should verify the A5 relaxation details in the appendix before finalizing my report.

Now checking the PPCI validation more carefully: the bias reduction from 0.179 to 0.007 under DGP C with z=0 checks out against the appendix table. The claim about PPCI's trade-offs—that it fixes outcome error but increases variance for covariate error alone, while the combination handles both—appears to be cut off mid-sentence, but the core comparisons seem to be tracking correctly so far.

For the 27% RMSE advantage claim under covariate-side error alone, I'm trying to verify this against DGP A numbers. The raw difference between PPCI (0.162) and EC-HTE (0.097) could be computed multiple ways, and I'm checking whether it's calculated as an average across z-levels rather than at a single level. I'm trying different calculations to match that 27% figure—comparing RMSE ratios at different z values, checking bias metrics, even attempting aggregate RMSE calculations—but nothing aligns with what the paper claims. both errors), PPCI bias = 0.015/0.020. So the claim of 0.003–0.004 under DGP C doesn't match the table values either. I need to flag this discrepancy as well. I'm cross-checking the appendix table against what method.tex claims, and there's a mismatch: the text refers to "outcome-side error alone (DGP~C)" but the appendix clearly defines DGP B as outcome error only and DGP C as both errors. The bias values cited in method.tex (0.003–0.004) also don't match what's in the PPCI table for either DGP B or C, so the DGP labels in the main text need to be corrected. I'm re-reading the sentence more carefully—it says PPCI achieves |bias| = 0.003-0.004 under outcome-side error alone, but the table shows PPCI on DGP B gives 0.015/0.020, which doesn't match. I don't have access to the detailed per-subgroup results in the CSV files, so there might be a discrepancy between the summary table and the actual experiment data. This is a critical issue I need to flag: the reported bias values don't align with what's in the table. The text is mislabeling DGP C as "outcome-side error alone" when it actually contains both error types—DGP B is the outcome-only case. Looking at the actual table values for DGP B, PPCI's bias is around 0.0175, and adding EC-HTE doesn't meaningfully improve it, which aligns with the claim that EC-HTE's contribution is negligible under outcome-side error alone.

However, the cited bias range of 0.003-0.004 doesn't match DGP B's values, so either there's a typo in the DGP label or these numbers come from a different experimental setup or subgroup analysis not visible in the summary table. I should flag both the mislabeling and the discrepancy in the reported values. I'm verifying the "31% at τ(0)=0.01" claim across the paper and registry—it checks out in both intro.tex and experiments.tex, matching exp-038. I also need to confirm the "87.5% of configurations" statistic and check a few more details from method.tex before compiling the full audit report.

Now I'm looking at the runtime claim about "<5ms for K=4, N=5,000"—that's not something I can verify directly from the registry metrics. The intro's GPT-4.1 accuracy on TweetEval checks out at 85.8%, and the error rate range of 10.2% to 20.0% aligns with what I'm seeing in the data. But I'm noticing a discrepancy in theory.tex around the AUC values—the main text claims it decreases from 0.86 to 0.66, but the appendix seems to say something different about the symmetric case.

Looking at the actual registry values, I need to distinguish between synthetic and real LLM experiments. The synthetic asymmetric case gives 0.66, but the real LLM results from exp-028 show symmetric AUC around 0.626 and asymmetric around 0.611—these are different contexts entirely, so the 0.66 figure isn't directly comparable to the real-world performance numbers.

Now I'm noticing another discrepancy: the paper reports 0.86 as the AUC for the synthetic symmetric case, but exp-005 in the registry shows 0.833 for AUC and 0.86 for correlation. It seems like the paper may be conflating two different metrics—the standard ROC-based AUC (0.833) with a correlation-based measure (0.86)—and calling both "AUC" when they're actually measuring different things. So the 0.86 AUC appears consistently across the main text and figures for the Δπ-only condition, while the registry entry of 0.833 likely refers to a different scoring rule based on the full Proposition 2 criterion. These aren't actually contradictory—they're measuring different things, so I should note this as a clarification rather than a discrepancy. Looking at the specific citations, method.tex claims the Proposition 2 threshold classifier achieves AUC=0.86, but the registry shows it actually produces AUC=0.833—the 0.86 figure comes from the Δπ-only variant displayed in the ROC figure, so there's a genuine mismatch between what the text claims and what the experiments actually show. So the "Δπ-only condition" in the figure caption likely refers to Proposition 2 itself, since Proposition 2 depends only on misclassification rates and not treatment effects. That would explain why it's labeled that way. The gap between the paper's reported AUC of 0.86 and the registry's 0.833 from experiment 005 is a real discrepancy—possibly due to different computational methods, threshold choices, or subgroup selections between the two analyses. I should flag this as a warning about the AUC mismatch.

Now I'm ready to compile the full report. Let me also check the abstract word count against the EMNLP submission requirements. Looking at the abstract text, it's explaining how standard confusion-matrix correction fails when error rates vary across subgroups—particularly with LLM classifiers that can have error rates differing by up to 5× between groups. The key contribution is deriving a bias identity that shows how global correction introduces subgroup-level bias through a product of the subgroup's deviation from pooled error rates, treatment effect heterogeneity, and an amplification factor.

The validation is comprehensive: the identity holds at R² ≥ 0.97 across synthetic grids and semi-synthetic evaluations using 11 real LLM confusion matrices, tested with three different CATE estimators. It predicts that global correction reverses the sign of causal effects in about 15% of configurations and amplifies bias across all eight real LLMs examined. The diagnostic derived from the identity can predict when correction increases bias just by looking at per-subgroup error rates alone, achieving perfect discrimination on subgroups with heterogeneous treatment effects and reasonable performance on broader synthetic and real LLM error profiles. The proposed per-subgroup correction approach using hierarchical Bayesian estimation reduces bias magnitude by over 7×.

Now I'm identifying critical issues in the method section that need fixing before finalizing the report. There's a labeling error where DGP C is incorrectly described as outcome-side error when it should reference DGP B, and the claimed PPCI bias values don't align with any of the actual table results. I'm also noting internal inconsistencies around RMSE variation thresholds that are stated differently across sections.

Beyond the critical issues, I'm tracking several discrepancies that warrant investigation: the AUC value differs slightly depending on which scoring rule was applied, there's a minor rounding difference in the R² values between the paper and registry, and the claimed RMSE advantage for EC-HTE over PPCI can't be verified from the available data. I'm also double-checking the 5x error rate variation claim cited in both the abstract and introduction to ensure it properly references Ashwin et al.

—which it does. Now I'm verifying the coverage percentages across the robustness validation experiments, and they all check out: subgroup misspecification, asymmetric confusion matrices, outcome-dependent misclassification, and confounded treatment all meet or exceed the stated 93.5% threshold.

I also need to confirm the treatment-dependent misclassification coverage at the specific gamma threshold—exp-040 shows 89.7% coverage when γ=0.05, matching what's cited in the limitations section.

Before I write the report, let me trace through one more calculation: the bias reduction from 0.179 to 0.007 that's mentioned in the methods section, which references the PPCI appendix.  Both the main text and appendix confirm this is for DGP C at z=0 when combining EC-HTE with PPCI. I should also clarify the distinction between the extreme case bias shown in Figure 1 (where the estimated τ̂ = -0.059 versus true τ = 0.03 gives an absolute bias of 0.089) and the global average absolute bias reported in Table 1 for K=2, which is 0.059—these are measuring different things.

Now I'm checking the critical threshold claim in experiments.tex about when sign reversal occurs. Looking at the reversal rates across different τ values from exp-038, the pattern shows reversal happening at 31% for τ=0.01, dropping to 14.9% at τ=0.03, then 6.1% at τ=0.05, and stopping entirely by τ=0.10, so the threshold appears to fall somewhere between 0.05 and 0.10.

Let me verify a few more claims from the paper. The relative advantage of HB EC-HTE over stratified MLE checks out at 1.5×, and the convergence claim about p-values exceeding 0.05 holds across the test cases I'm examining.

Now I'm organizing the audit report with sections for traceability, cross-location consistency, and rounding conventions, making sure to handle the output directory properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "cca713fe-5c5b-4461-bf00-d85f852d7eb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALkKcMuMLDgGMPXmB5DNNW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42253,
      "cache_read_input_tokens": 42329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42253
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

_source line 104_

Now I have all tex files and registry data. Let me read the remaining appendix sections I haven't covered yet, then compile the full report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "e06e52e2-0e46-4a81-b09c-c24560e27568",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALkKcMuMLDgGMPXmB5DNNW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42253,
      "cache_read_input_tokens": 42329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42253
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

_source line 105_

<details open><summary>🔧 Tool call — Read · `toolu_01MNTBkU1LW2fQsdgQMafc5x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1199,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "ea7d579f-745d-4b3a-867d-a5d4a6daddfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALkKcMuMLDgGMPXmB5DNNW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42253,
      "cache_read_input_tokens": 42329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 42253
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

_source line 106 · 2026-05-24T04:41:59.390Z_

<details><summary>↩ Tool result · `toolu_01MNTBkU1LW2fQsdgQMafc5x`</summary>

```text
1199	 & Global est.\ $\hat{\bar{C}}$ & 94.3 & 0.105 & 0.114 \\
1200	 & Naive                    & 77.3 & 0.120 & 0.125 \\
1201	\bottomrule
1202	\end{tabular}
1203	\end{table}
1204	
1205	Three findings emerge.
1206	First, oracle coverage is 94--96\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.
1207	Second, EC-HTE with true $C_s$ achieves 91--94\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.
1208	Third, the gap between true and estimated $C_s$ is ${\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\text{expert}} \geq 250$.
1209	
1210	\section{Robustness to Assumption Violations}
1211	\label{app:a5_violation}
1212	
1213	\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}
1214	
1215	\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]
1216	\label{cor:a5_relaxation}
1217	When $\Delta\tau$ varies across subgroups ($\Delta\tau_s = \tau_s(1) - \tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$, and at level $z{=}1$ is $-\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$.
1218	\end{corollary}
1219	The proof follows directly from Theorem~\ref{thm:bias_identity} with $\tau_s$ replacing $\tau$.
1220	
1221	Our main analysis assumes that subgroup misclassification rates $\delta_s$ and subgroup CATE magnitudes $\Delta\tau_s$ are independent (Assumption A5).
1222	In practice, both may depend on text features that define subgroups, introducing correlation.
1223	We test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 50 MC replications, $\pi = [0.05, 0.25]$):
1224	\emph{aligned} (positive $\delta_s$--$\Delta\tau_s$ correlation: high-error S1 has the larger treatment effect, $\Delta\tau = [0.30, 0.70]$) and
1225	\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\Delta\tau = [0.70, 0.30]$).
1226	
1227	\begin{table}[h]
1228	\centering
1229	\caption{Coverage and $|\text{bias}|$ under A5 violation ($K{=}2$, $n_{\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}
1230	\label{tab:a5_violation}
1231	\small
1232	\begin{tabular}{llcccc}
1233	\toprule
1234	Config & Method & S0 cov & S1 cov & S0 $|\text{bias}|$ & S1 $|\text{bias}|$ \\
1235	\midrule
1236	\multirow{4}{*}{Aligned}
1237	 & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\
1238	 & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\
1239	 & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\
1240	 & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\
1241	\midrule
1242	\multirow{4}{*}{Adversarial}
1243	 & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\
1244	 & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\
1245	 & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\
1246	 & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\
1247	\bottomrule
1248	\end{tabular}
1249	\end{table}
1250	
1251	In the aligned configuration, the $\delta_s \times \Delta\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.
1252	Global correction improves S1 but cannot fully correct without subgroup-specific error rates.
1253	In the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).
1254	EC-HTE (EB) maintains $\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.
1255	Results at $n_{\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\in [0.93, 0.99]$).
1256	
1257	\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}
1258	\label{app:a1_sensitivity}
1259	
1260	We assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).
1261	We modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\hat{Z}{\neq}Z \mid Z, S, Y) = \mathrm{clamp}(\pi_s + \gamma \cdot (Y - \mu_Y)/\sigma_Y,\, 0,\, 1)$, where $\gamma \in \{0, 0.05, 0.10, 0.15, 0.20\}$ controls the strength of violation.
1262	Table~\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.
1263	
1264	\begin{table}[h]
1265	\centering
1266	\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\text{bias}|$ under outcome-dependent misclassification ($\gamma > 0$).}
1267	\label{tab:a1_sensitivity}
1268	\small
1269	\begin{tabular}{lccc ccc}
1270	\toprule
1271	& \multicolumn{3}{c}{Coverage (\%)} & \multicolumn{3}{c}{$|\text{Bias}|$} \\
1272	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
1273	$\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\
1274	\midrule
1275	0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\
1276	0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\
1277	0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\
1278	0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\
1279	0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\
1280	\bottomrule
1281	\end{tabular}
1282	\end{table}
1283	
1284	EC-HTE maintains near-nominal coverage ($\geq$93.5\%) across the full $\gamma$ range, with $|\text{bias}|$ increasing only 13.7\% from $\gamma{=}0$ to $\gamma{=}0.2$.
1285	All correction methods (Global, Stratified MLE, HB) maintain $\geq$90\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.
1286	The naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.
1287	
1288	\subsection{Assumption (A1): Treatment-Dependent Misclassification}
1289	\label{app:treatment_dep}
1290	
1291	We extend the (A1) sensitivity analysis to the treatment-dependent case, where misclassification probability depends on treatment assignment $T$: $P(\hat{Z}{\neq}Z \mid Z, S, T) = \mathrm{clamp}(\pi_s + \gamma_T \cdot (2T - 1),\, 0,\, 1)$, with $\gamma_T \in \{0, 0.05, 0.10, 0.15, 0.20\}$.
1292	This scenario arises when LLM accuracy varies with treatment status---e.g., treated texts may be systematically harder to classify.
1293	Setup: $K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs.
1294	
1295	\begin{table}[h]
1296	\centering
1297	\caption{Sensitivity to treatment-dependent misclassification ($\gamma_T$). EC-HTE maintains $\geq$89.7\% coverage at $\gamma_T \leq 0.05$.}
1298	\label{tab:treatment_dep}
1299	\small
1300	\begin{tabular}{lcc}
1301	\toprule
1302	$\gamma_T$ & EC-HTE Coverage & EC-HTE RMSE \\
1303	\midrule
1304	0.00 & 0.945 & 0.075 \\
1305	0.05 & 0.897 & 0.092 \\
1306	0.10 & 0.750 & 0.133 \\
1307	0.15 & 0.525 & 0.177 \\
1308	0.20 & 0.370 & 0.224 \\
1309	\bottomrule
1310	\end{tabular}
1311	\end{table}
1312	
1313	EC-HTE is robust to small treatment-dependent violations ($\gamma_T \leq 0.05$), maintaining $\geq$89.7\% coverage with modest RMSE increase (0.075 to 0.092).
1314	At $\gamma_T = 0.10$, coverage drops to 75.0\%, establishing this as the approximate breakeven point.
1315	The degradation is steeper than for outcome-dependent violations (Table~\ref{tab:a1_sensitivity}), because treatment-dependent errors directly contaminate the treatment arm contrast.
1316	Figure~\ref{fig:treatment_dep} visualizes the coverage and RMSE trajectories.
1317	
1318	\begin{figure}[h]
1319	\centering
1320	\includegraphics[width=\columnwidth]{figures/treatment_dep_misclass.pdf}
1321	\caption{EC-HTE coverage and RMSE under treatment-dependent misclassification. Dashed line: 90\% coverage threshold. Breakeven at $\gamma_T \approx 0.10$.}
1322	\label{fig:treatment_dep}
1323	\end{figure}
1324	
1325	\subsection{Extension to Confounded Treatment Assignment}
1326	\label{app:confounded_dgp}
1327	
1328	EC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.
1329	To verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.
1330	
1331	\paragraph{DGP.}
1332	$N{=}5{,}000$, $K{=}2$, $\pi = [0.05, 0.25]$, $n_{\text{expert}}{=}250$, 100 MC replications.
1333	A covariate $X \sim \mathcal{N}(0,1)$ confounds both treatment and outcome:
1334	$T \sim \text{Bernoulli}(\sigma(\beta X))$ with $\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),
1335	$Y = 1 + 0.5 Z + 0.3 X + \tau(Z) \cdot T + \eta$, $\eta \sim \mathcal{N}(0,1)$.
1336	Treatment effects are $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
1337	The IPW-DIM estimator uses \emph{oracle propensity} $e(X) = \sigma(\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.
1338	
1339	\begin{table}[h]
1340	\centering
1341	\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\beta{=}0.5$, 100 MC).}
1342	\label{tab:confounded_dgp}
1343	\small
1344	\begin{tabular}{lccc}
1345	\toprule
1346	Method & Coverage & RMSE & $|\text{Bias}|$ \\
1347	\midrule
1348	Oracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\
1349	HB EC-HTE              & 0.950 & 0.086 & 0.068 \\
1350	Global                  & 0.930 & 0.087 & 0.071 \\
1351	Strat MLE               & 0.950 & 0.087 & 0.069 \\
1352	Naive                   & 0.863 & 0.083 & 0.066 \\
1353	\bottomrule
1354	\end{tabular}
1355	\end{table}
1356	
1357	EC-HTE achieves 95.0\% coverage, within 0.7pp of the oracle (94.3\%), confirming that confusion matrix correction and propensity weighting compose without interference.
1358	The improvement is most pronounced in the high-error subgroup ($\pi{=}0.25$): EC-HTE coverage is 96.0\% vs.\ naive 78.5\% ($+$17.5pp).
1359	Global coverage (93.0\%) falls below the correction methods (95.0\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.
1360	
1361	\paragraph{Sensitivity to confounding strength and propensity estimation.}
1362	We sweep $\beta \in \{0.25, 0.5, 1.0, 2.0\}$ and compare oracle propensity ($e(X) = \sigma(\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).
1363	Table~\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.
1364	
1365	\begin{table}[h]
1366	\centering
1367	\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}
1368	\label{tab:confounded_sweep}
1369	\small
1370	\begin{tabular}{cccc}
1371	\toprule
1372	$\beta$ & Propensity & HB Coverage & Naive Coverage \\
1373	\midrule
1374	0.25 & Oracle    & 0.963 & 0.848 \\
1375	0.25 & Estimated & 0.973 & 0.845 \\
1376	0.50 & Oracle    & 0.950 & 0.863 \\
1377	0.50 & Estimated & 0.958 & 0.858 \\
1378	1.00 & Oracle    & 0.958 & 0.898 \\
1379	1.00 & Estimated & 0.960 & 0.883 \\
1380	2.00 & Oracle    & 0.945 & 0.858 \\
1381	2.00 & Estimated & 0.948 & 0.858 \\
1382	\bottomrule
1383	\end{tabular}
1384	\end{table}
1385	
1386	EC-HTE maintains coverage $\geq$94.5\% across all 8 configurations, including strong confounding ($\beta{=}2.0$, propensity range $[0.12, 0.88]$).
1387	The oracle--estimated gap is $\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.
1388	This validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.
1389	
1390	\subsection{Empirical Comparison with Frazis--Loewenstein Correction}
1391	\label{app:fl_comparison}
1392	
1393	We empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \citet{frazis2003estimating} (F-L).
1394	The F-L correction rescales the observed estimate as $\hat{\tau}_{\text{FL}} = \hat{\tau}_{\text{obs}} / (1 - 2\bar{\pi})$, where $\bar{\pi}$ is the (global or per-subgroup) misclassification rate.
1395	We test two variants: F-L \emph{scalar} (single global $\bar{\pi}$) and F-L \emph{per-subgroup} ($\pi_s$-specific rescaling).
1396	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, $\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\tau(z{=}0){=}0$, $\tau(z{=}1){=}0.3$, 100 MC runs.
1397	
1398	\begin{table}[h]
1399	\centering
1400	\caption{F-L correction vs.\ EC-HTE under heterogeneous misclassification ($\Delta\pi{=}0.20$). Both F-L variants produce \emph{higher} aggregate bias than the uncorrected estimator.}
1401	\label{tab:fl_comparison}
1402	\small
1403	\begin{tabular}{lccc}
1404	\toprule
1405	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1406	\midrule
1407	Oracle         & 0.045 & 0.056 & 0.943 \\
1408	Naive          & 0.062 & 0.077 & 0.858 \\
1409	Global (CM inv)& 0.064 & 0.081 & 0.938 \\
1410	HB EC-HTE      & 0.064 & 0.086 & \textbf{0.953} \\
1411	F-L Scalar     & 0.091 & 0.116 & 0.850 \\
1412	F-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\
1413	\bottomrule
1414	\end{tabular}
1415	\end{table}
1416	
1417	Both F-L variants produce \emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\text{bias}|{=}0.112$ vs.\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.
1418	The per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\ naive $+0.005$, a $14.6\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).
1419	EC-HTE achieves near-zero per-subgroup bias ($s_0{:}\,{+}0.006$, $s_1{:}\,{+}0.001$) with nominal coverage (95.3\%).
1420	The root cause is structural: F-L's $1/(1{-}2\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.
1421	
1422	\subsection{End-to-End Validation with Asymmetric Confusion Matrices}
1423	\label{app:asymmetric_endtoend}
1424	
1425	We validate EC-HTE under strongly asymmetric confusion matrices ($\text{FPR}/\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.
1426	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$; $s_0$: $\text{FPR}{=}0.05$, $\text{FNR}{=}0.02$ (low error); $s_1$: $\text{FPR}{=}0.38$, $\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.
1427	We compare EC-HTE using the full $2{\times}2$ asymmetric CM (Remark~2) against the symmetric assumption ($\text{FPR}{=}\text{FNR}{=}\pi_s$).
1428	
1429	\begin{table}[h]
1430	\centering
1431	\caption{EC-HTE under asymmetric misclassification ($\text{FPR}/\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\%$.}
1432	\label{tab:asymmetric_endtoend}
1433	\small
1434	\begin{tabular}{lccc}
1435	\toprule
1436	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1437	\midrule
1438	Oracle              & 0.045 & 0.056 & 0.943 \\
1439	EC-HTE (asymmetric) & 0.057 & 0.074 & \textbf{0.945} \\
1440	Naive               & 0.059 & 0.073 & 0.870 \\
1441	Global (asymmetric) & 0.061 & 0.076 & 0.915 \\
1442	EC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\
1443	Global (symmetric)  & 0.063 & 0.078 & 0.915 \\
1444	\bottomrule
1445	\end{tabular}
1446	\end{table}
1447	
1448	EC-HTE with the asymmetric formula achieves 94.5\% coverage versus 93.0\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\%$).
1449	The improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\% vs.\ symmetric 91.0\%.
1450	Practitioners should estimate full $2 \times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.
1451	
1452	\subsection{Complementarity with LLM Calibration}
1453	\label{app:calibration}
1454	
1455	Temperature or Platt scaling~\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\Delta\pi$.
1456	We simulate calibration by shrinking per-subgroup rates from $\pi{=}[0.05, 0.25]$ ($\Delta\pi{=}0.20$) to $\pi{=}[0.08, 0.15]$ ($\Delta\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.
1457	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs.
1458	
1459	\begin{table}[h]
1460	\centering
1461	\caption{Calibration reduces $\Delta\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}
1462	\label{tab:calibration}
1463	\small
1464	\begin{tabular}{lccc}
1465	\toprule
1466	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1467	\midrule
1468	Oracle                    & 0.043 & 0.053 & 0.963 \\
1469	Calibrated + EC-HTE       & 0.055 & 0.069 & \textbf{0.965} \\
1470	Calibrated + Global       & 0.055 & 0.068 & 0.963 \\
1471	Calibrated + Naive        & 0.051 & 0.064 & 0.913 \\
1472	Uncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\
1473	Uncalibrated + Global     & 0.069 & 0.085 & 0.920 \\
1474	Uncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\
1475	\bottomrule
1476	\end{tabular}
1477	\end{table}
1478	
1479	Calibration alone improves naive coverage from 84.0\% to 91.3\% but does not reach the nominal 95\%.
1480	Calibrated + EC-HTE achieves the highest coverage (96.5\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\pi_s$ while EC-HTE corrects the residual $\delta_s$-driven bias from heterogeneity that persists post-calibration.
1481	Propensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.
1482	
1483	\subsection{Policy Reversal Zone Analysis}
1484	\label{app:policy_reversal}
1485	
1486	When the true treatment effect is small, global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---creating a \emph{policy reversal zone}.
1487	We sweep $\tau(0) \in \{0.01, 0.02, 0.03, 0.05, 0.07, 0.10\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs; $\Delta\tau{=}0.30$).
1488	
1489	\begin{table}[h]
1490	\centering
1491	\caption{Policy reversal zone: fraction of configurations where global correction reverses the sign of estimated CATE.
1492	The naive estimator produces zero sign reversals across all $\tau(0)$ values; EC-HTE also achieves 0\% reversal.}
1493	\label{tab:policy_reversal}
1494	\small
1495	\begin{tabular}{ccc}
1496	\toprule
1497	$\tau(0)$ & Global reversal \% & Most extreme $\hat{\tau}_{\text{global}}$ \\
1498	\midrule
1499	0.01 & 31.0 & $-0.079$ \\
1500	0.02 & 21.6 & --- \\
1501	0.03 & 14.9 & $-0.059$ \\
1502	0.05 & 6.1  & $-0.039$ \\
1503	0.07 & 1.6  & --- \\
1504	$\geq$0.10 & 0 & --- \\
1505	\bottomrule
1506	\end{tabular}
1507	\end{table}
1508	
1509	The reversal rate increases monotonically as $\tau(0)$ decreases: at $\tau(0) = 0.01$, 31\% of configurations yield sign reversal, with the most extreme case estimating $\hat{\tau} = -0.079$ when the true effect is $\tau = +0.01$.
1510	The critical threshold is $\tau(0) < 0.089$, matching the closed-form prediction from Theorem~\ref{thm:bias_identity}: $|\delta_{\max} \cdot \Delta\tau_{\max}| / (1 - 2\bar{\pi}) = 0.125 \times 0.50 / 0.70 = 0.089$.
1511	The most dangerous combination ($\tau(0) = 0.01$, $\delta_{\text{misclass}} = 0.19$) reaches 42.9\% reversal rate.
1512	The naive estimator produces zero sign reversals across all $\tau(0)$ values, confirming that reversal is an artifact of global correction, not inherent estimation noise.
1513	
1514	Figure~\ref{fig:policy_reversal} visualizes the reversal zone across the $\Delta\pi \times \tau(0)$ parameter space.
1515	
1516	\begin{figure}[h]
1517	\centering
1518	\includegraphics[width=\columnwidth]{figures/policy_reversal_zone.pdf}
1519	\caption{Policy reversal zone: sign-reversal rate as a function of $\tau(0)$ and $\Delta\pi$. Shaded region marks configurations where global correction reverses the CATE sign, directing policy toward the wrong subgroups.}
1520	\label{fig:policy_reversal}
1521	\end{figure}
1522	
1523	\input{appendix_stance}
1524	
1525	\section*{Use of AI Assistants}
1526	\label{app:ai-assistants}
1527	
1528	We used Claude (Anthropic) as an AI coding and writing assistant
1529	throughout this work. Specifically:
1530	\begin{itemize}
1531	    \item \textbf{Code:} drafting experiment scripts, data-processing
1532	    pipelines, and analysis utilities; debugging and refactoring.
1533	    \item \textbf{Writing:} drafting and revising paper sections,
1534	    polishing prose, and reformatting LaTeX.
1535	    \item \textbf{Literature:} summarizing related papers to inform
1536	    the related-work section.
1537	\end{itemize}
1538	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "297da068-d78b-49b3-bc84-f673b3417d8d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
      "content": " & Global est.\\ $\\hat{\\bar{C}}$ & 94.3 & 0.105 & 0.114 \\\\\n & Naive                    & 77.3 & 0.120 & 0.125 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree findings emerge.\nFirst, oracle coverage is 94--96\\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.\nSecond, EC-HTE with true $C_s$ achieves 91--94\\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.\nThird, the gap between true and estimated $C_s$ is ${\\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\\text{expert}} \\geq 250$.\n\n\\section{Robustness to Assumption Violations}\n\\label{app:a5_violation}\n\n\\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}\n\n\\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]\n\\label{cor:a5_relaxation}\nWhen $\\Delta\\tau$ varies across subgroups ($\\Delta\\tau_s = \\tau_s(1) - \\tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$, and at level $z{=}1$ is $-\\delta_s \\cdot \\Delta\\tau_s / (1 - 2\\bar{\\pi})$.\n\\end{corollary}\nThe proof follows directly from Theorem~\\ref{thm:bias_identity} with $\\tau_s$ replacing $\\tau$.\n\nOur main analysis assumes that subgroup misclassification rates $\\delta_s$ and subgroup CATE magnitudes $\\Delta\\tau_s$ are independent (Assumption A5).\nIn practice, both may depend on text features that define subgroups, introducing correlation.\nWe test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 50 MC replications, $\\pi = [0.05, 0.25]$):\n\\emph{aligned} (positive $\\delta_s$--$\\Delta\\tau_s$ correlation: high-error S1 has the larger treatment effect, $\\Delta\\tau = [0.30, 0.70]$) and\n\\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\\Delta\\tau = [0.70, 0.30]$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Coverage and $|\\text{bias}|$ under A5 violation ($K{=}2$, $n_{\\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}\n\\label{tab:a5_violation}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nConfig & Method & S0 cov & S1 cov & S0 $|\\text{bias}|$ & S1 $|\\text{bias}|$ \\\\\n\\midrule\n\\multirow{4}{*}{Aligned}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\\\\n & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\\\\n & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\\\\n\\midrule\n\\multirow{4}{*}{Adversarial}\n & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\\\\n & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\\\\n & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\\\\n & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn the aligned configuration, the $\\delta_s \\times \\Delta\\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.\nGlobal correction improves S1 but cannot fully correct without subgroup-specific error rates.\nIn the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).\nEC-HTE (EB) maintains $\\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.\nResults at $n_{\\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\\in [0.93, 0.99]$).\n\n\\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}\n\\label{app:a1_sensitivity}\n\nWe assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).\nWe modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\\hat{Z}{\\neq}Z \\mid Z, S, Y) = \\mathrm{clamp}(\\pi_s + \\gamma \\cdot (Y - \\mu_Y)/\\sigma_Y,\\, 0,\\, 1)$, where $\\gamma \\in \\{0, 0.05, 0.10, 0.15, 0.20\\}$ controls the strength of violation.\nTable~\\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\\text{bias}|$ under outcome-dependent misclassification ($\\gamma > 0$).}\n\\label{tab:a1_sensitivity}\n\\small\n\\begin{tabular}{lccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{Coverage (\\%)} & \\multicolumn{3}{c}{$|\\text{Bias}|$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\\\\n\\midrule\n0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\\\\n0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\\\\n0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\\\\n0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\\\\n0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains near-nominal coverage ($\\geq$93.5\\%) across the full $\\gamma$ range, with $|\\text{bias}|$ increasing only 13.7\\% from $\\gamma{=}0$ to $\\gamma{=}0.2$.\nAll correction methods (Global, Stratified MLE, HB) maintain $\\geq$90\\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.\nThe naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.\n\n\\subsection{Assumption (A1): Treatment-Dependent Misclassification}\n\\label{app:treatment_dep}\n\nWe extend the (A1) sensitivity analysis to the treatment-dependent case, where misclassification probability depends on treatment assignment $T$: $P(\\hat{Z}{\\neq}Z \\mid Z, S, T) = \\mathrm{clamp}(\\pi_s + \\gamma_T \\cdot (2T - 1),\\, 0,\\, 1)$, with $\\gamma_T \\in \\{0, 0.05, 0.10, 0.15, 0.20\\}$.\nThis scenario arises when LLM accuracy varies with treatment status---e.g., treated texts may be systematically harder to classify.\nSetup: $K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Sensitivity to treatment-dependent misclassification ($\\gamma_T$). EC-HTE maintains $\\geq$89.7\\% coverage at $\\gamma_T \\leq 0.05$.}\n\\label{tab:treatment_dep}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n$\\gamma_T$ & EC-HTE Coverage & EC-HTE RMSE \\\\\n\\midrule\n0.00 & 0.945 & 0.075 \\\\\n0.05 & 0.897 & 0.092 \\\\\n0.10 & 0.750 & 0.133 \\\\\n0.15 & 0.525 & 0.177 \\\\\n0.20 & 0.370 & 0.224 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE is robust to small treatment-dependent violations ($\\gamma_T \\leq 0.05$), maintaining $\\geq$89.7\\% coverage with modest RMSE increase (0.075 to 0.092).\nAt $\\gamma_T = 0.10$, coverage drops to 75.0\\%, establishing this as the approximate breakeven point.\nThe degradation is steeper than for outcome-dependent violations (Table~\\ref{tab:a1_sensitivity}), because treatment-dependent errors directly contaminate the treatment arm contrast.\nFigure~\\ref{fig:treatment_dep} visualizes the coverage and RMSE trajectories.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/treatment_dep_misclass.pdf}\n\\caption{EC-HTE coverage and RMSE under treatment-dependent misclassification. Dashed line: 90\\% coverage threshold. Breakeven at $\\gamma_T \\approx 0.10$.}\n\\label{fig:treatment_dep}\n\\end{figure}\n\n\\subsection{Extension to Confounded Treatment Assignment}\n\\label{app:confounded_dgp}\n\nEC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.\nTo verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.\n\n\\paragraph{DGP.}\n$N{=}5{,}000$, $K{=}2$, $\\pi = [0.05, 0.25]$, $n_{\\text{expert}}{=}250$, 100 MC replications.\nA covariate $X \\sim \\mathcal{N}(0,1)$ confounds both treatment and outcome:\n$T \\sim \\text{Bernoulli}(\\sigma(\\beta X))$ with $\\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),\n$Y = 1 + 0.5 Z + 0.3 X + \\tau(Z) \\cdot T + \\eta$, $\\eta \\sim \\mathcal{N}(0,1)$.\nTreatment effects are $\\tau(Z{=}0){=}0$, $\\tau(Z{=}1){=}0.3$.\nThe IPW-DIM estimator uses \\emph{oracle propensity} $e(X) = \\sigma(\\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\\beta{=}0.5$, 100 MC).}\n\\label{tab:confounded_dgp}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Coverage & RMSE & $|\\text{Bias}|$ \\\\\n\\midrule\nOracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\\\\nHB EC-HTE              & 0.950 & 0.086 & 0.068 \\\\\nGlobal                  & 0.930 & 0.087 & 0.071 \\\\\nStrat MLE               & 0.950 & 0.087 & 0.069 \\\\\nNaive                   & 0.863 & 0.083 & 0.066 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE achieves 95.0\\% coverage, within 0.7pp of the oracle (94.3\\%), confirming that confusion matrix correction and propensity weighting compose without interference.\nThe improvement is most pronounced in the high-error subgroup ($\\pi{=}0.25$): EC-HTE coverage is 96.0\\% vs.\\ naive 78.5\\% ($+$17.5pp).\nGlobal coverage (93.0\\%) falls below the correction methods (95.0\\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.\n\n\\paragraph{Sensitivity to confounding strength and propensity estimation.}\nWe sweep $\\beta \\in \\{0.25, 0.5, 1.0, 2.0\\}$ and compare oracle propensity ($e(X) = \\sigma(\\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).\nTable~\\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}\n\\label{tab:confounded_sweep}\n\\small\n\\begin{tabular}{cccc}\n\\toprule\n$\\beta$ & Propensity & HB Coverage & Naive Coverage \\\\\n\\midrule\n0.25 & Oracle    & 0.963 & 0.848 \\\\\n0.25 & Estimated & 0.973 & 0.845 \\\\\n0.50 & Oracle    & 0.950 & 0.863 \\\\\n0.50 & Estimated & 0.958 & 0.858 \\\\\n1.00 & Oracle    & 0.958 & 0.898 \\\\\n1.00 & Estimated & 0.960 & 0.883 \\\\\n2.00 & Oracle    & 0.945 & 0.858 \\\\\n2.00 & Estimated & 0.948 & 0.858 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE maintains coverage $\\geq$94.5\\% across all 8 configurations, including strong confounding ($\\beta{=}2.0$, propensity range $[0.12, 0.88]$).\nThe oracle--estimated gap is $\\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.\nThis validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.\n\n\\subsection{Empirical Comparison with Frazis--Loewenstein Correction}\n\\label{app:fl_comparison}\n\nWe empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \\citet{frazis2003estimating} (F-L).\nThe F-L correction rescales the observed estimate as $\\hat{\\tau}_{\\text{FL}} = \\hat{\\tau}_{\\text{obs}} / (1 - 2\\bar{\\pi})$, where $\\bar{\\pi}$ is the (global or per-subgroup) misclassification rate.\nWe test two variants: F-L \\emph{scalar} (single global $\\bar{\\pi}$) and F-L \\emph{per-subgroup} ($\\pi_s$-specific rescaling).\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, $\\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\\tau(z{=}0){=}0$, $\\tau(z{=}1){=}0.3$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{F-L correction vs.\\ EC-HTE under heterogeneous misclassification ($\\Delta\\pi{=}0.20$). Both F-L variants produce \\emph{higher} aggregate bias than the uncorrected estimator.}\n\\label{tab:fl_comparison}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle         & 0.045 & 0.056 & 0.943 \\\\\nNaive          & 0.062 & 0.077 & 0.858 \\\\\nGlobal (CM inv)& 0.064 & 0.081 & 0.938 \\\\\nHB EC-HTE      & 0.064 & 0.086 & \\textbf{0.953} \\\\\nF-L Scalar     & 0.091 & 0.116 & 0.850 \\\\\nF-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBoth F-L variants produce \\emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\\text{bias}|{=}0.112$ vs.\\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.\nThe per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\\ naive $+0.005$, a $14.6\\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).\nEC-HTE achieves near-zero per-subgroup bias ($s_0{:}\\,{+}0.006$, $s_1{:}\\,{+}0.001$) with nominal coverage (95.3\\%).\nThe root cause is structural: F-L's $1/(1{-}2\\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.\n\n\\subsection{End-to-End Validation with Asymmetric Confusion Matrices}\n\\label{app:asymmetric_endtoend}\n\nWe validate EC-HTE under strongly asymmetric confusion matrices ($\\text{FPR}/\\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$; $s_0$: $\\text{FPR}{=}0.05$, $\\text{FNR}{=}0.02$ (low error); $s_1$: $\\text{FPR}{=}0.38$, $\\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.\nWe compare EC-HTE using the full $2{\\times}2$ asymmetric CM (Remark~2) against the symmetric assumption ($\\text{FPR}{=}\\text{FNR}{=}\\pi_s$).\n\n\\begin{table}[h]\n\\centering\n\\caption{EC-HTE under asymmetric misclassification ($\\text{FPR}/\\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\\%$.}\n\\label{tab:asymmetric_endtoend}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle              & 0.045 & 0.056 & 0.943 \\\\\nEC-HTE (asymmetric) & 0.057 & 0.074 & \\textbf{0.945} \\\\\nNaive               & 0.059 & 0.073 & 0.870 \\\\\nGlobal (asymmetric) & 0.061 & 0.076 & 0.915 \\\\\nEC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\\\\nGlobal (symmetric)  & 0.063 & 0.078 & 0.915 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEC-HTE with the asymmetric formula achieves 94.5\\% coverage versus 93.0\\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\\%$).\nThe improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\\% vs.\\ symmetric 91.0\\%.\nPractitioners should estimate full $2 \\times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.\n\n\\subsection{Complementarity with LLM Calibration}\n\\label{app:calibration}\n\nTemperature or Platt scaling~\\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\\Delta\\pi$.\nWe simulate calibration by shrinking per-subgroup rates from $\\pi{=}[0.05, 0.25]$ ($\\Delta\\pi{=}0.20$) to $\\pi{=}[0.08, 0.15]$ ($\\Delta\\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.\nSetup: $K{=}2$, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Calibration reduces $\\Delta\\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}\n\\label{tab:calibration}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $|\\text{Bias}|$ & RMSE & Coverage \\\\\n\\midrule\nOracle                    & 0.043 & 0.053 & 0.963 \\\\\nCalibrated + EC-HTE       & 0.055 & 0.069 & \\textbf{0.965} \\\\\nCalibrated + Global       & 0.055 & 0.068 & 0.963 \\\\\nCalibrated + Naive        & 0.051 & 0.064 & 0.913 \\\\\nUncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\\\\nUncalibrated + Global     & 0.069 & 0.085 & 0.920 \\\\\nUncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibration alone improves naive coverage from 84.0\\% to 91.3\\% but does not reach the nominal 95\\%.\nCalibrated + EC-HTE achieves the highest coverage (96.5\\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\\pi_s$ while EC-HTE corrects the residual $\\delta_s$-driven bias from heterogeneity that persists post-calibration.\nPropensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.\n\n\\subsection{Policy Reversal Zone Analysis}\n\\label{app:policy_reversal}\n\nWhen the true treatment effect is small, global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---creating a \\emph{policy reversal zone}.\nWe sweep $\\tau(0) \\in \\{0.01, 0.02, 0.03, 0.05, 0.07, 0.10\\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\\text{expert}}{=}250$, 100 MC runs; $\\Delta\\tau{=}0.30$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Policy reversal zone: fraction of configurations where global correction reverses the sign of estimated CATE.\nThe naive estimator produces zero sign reversals across all $\\tau(0)$ values; EC-HTE also achieves 0\\% reversal.}\n\\label{tab:policy_reversal}\n\\small\n\\begin{tabular}{ccc}\n\\toprule\n$\\tau(0)$ & Global reversal \\% & Most extreme $\\hat{\\tau}_{\\text{global}}$ \\\\\n\\midrule\n0.01 & 31.0 & $-0.079$ \\\\\n0.02 & 21.6 & --- \\\\\n0.03 & 14.9 & $-0.059$ \\\\\n0.05 & 6.1  & $-0.039$ \\\\\n0.07 & 1.6  & --- \\\\\n$\\geq$0.10 & 0 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reversal rate increases monotonically as $\\tau(0)$ decreases: at $\\tau(0) = 0.01$, 31\\% of configurations yield sign reversal, with the most extreme case estimating $\\hat{\\tau} = -0.079$ when the true effect is $\\tau = +0.01$.\nThe critical threshold is $\\tau(0) < 0.089$, matching the closed-form prediction from Theorem~\\ref{thm:bias_identity}: $|\\delta_{\\max} \\cdot \\Delta\\tau_{\\max}| / (1 - 2\\bar{\\pi}) = 0.125 \\times 0.50 / 0.70 = 0.089$.\nThe most dangerous combination ($\\tau(0) = 0.01$, $\\delta_{\\text{misclass}} = 0.19$) reaches 42.9\\% reversal rate.\nThe naive estimator produces zero sign reversals across all $\\tau(0)$ values, confirming that reversal is an artifact of global correction, not inherent estimation noise.\n\nFigure~\\ref{fig:policy_reversal} visualizes the reversal zone across the $\\Delta\\pi \\times \\tau(0)$ parameter space.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/policy_reversal_zone.pdf}\n\\caption{Policy reversal zone: sign-reversal rate as a function of $\\tau(0)$ and $\\Delta\\pi$. Shaded region marks configurations where global correction reverses the CATE sign, directing policy toward the wrong subgroups.}\n\\label{fig:policy_reversal}\n\\end{figure}\n\n\\input{appendix_stance}\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    the related-work section.\n\\end{itemize}\n",
      "numLines": 340,
      "startLine": 1199,
      "totalLines": 1538
    }
  }
}
```

</details>

---

### Assistant

_source line 107_

<details><summary>Logged reasoning block</summary>

```text
I now have all the data needed for the comprehensive audit report. Let me also verify a couple of tricky numbers I noticed:

1. The Figure 1 caption mentions "$\hat{\tau} = -0.059$" and the policy reversal table shows at τ(0)=0.03 the most extreme is -0.059. ✓

2. The intro mentions "7.5% of subgroup estimates" for sign reversals. This is different from the 14.9% configuration-level rate. 7.5% is the subgroup-estimate level rate.

3. Let me also check: experiments.tex:10 says "Robustness validation covers ... (all ≥93.5% coverage), and treatment-dependent misclassification (≈90% at γ_T ≤ 0.05)". The A1 sensitivity table shows at γ=0.05, EC-HTE coverage = 95.5%. 

That's outcome-dependent, not treatment-dependent. Treatment-dependent at γ_T=0.05 gives coverage = 89.7% ≈ 90%. ✓

Now I'm checking the DGP C versus DGP B issue more carefully. Looking at the PPCI table in the appendix, DGP B shows outcome error only with PPCI bias at z=0 of 0.015 and z=1 of 0.020. PPCI should correct outcome error well, but these values don't match the expected 0.003-0.004 range. Let me reconsider what the method.tex text is actually comparing here.

Actually, I think the text might be cherry-picking z=1 values across different DGPs—DGP B z=1 PPCI is 0.020 while DGP D z=1 PPCI is 0.003, but neither matches the 0.003-0.004 range for both z-levels. Looking at DGP C more carefully, the EC-HTE row shows bias of 0.179 at z=0 and 0.216 at z=1, while PPCI in DGP C gives 0.017 and 0.007 respectively—so that's 0.017/0.007, not 0.003-0.004 either. The method text mentions "under outcome-side"...

Wait, I'm seeing a critical mismatch here. The text claims PPCI achieves |bias| = 0.003-0.004 under DGP C (both errors), but the actual numbers show DGP B (outcome only) gives PPCI bias of 0.015/0.020, while DGP D (no error) gives 0.007/0.003. The 0.003-0.004 values actually correspond to DGP D, not DGP C, which makes no contextual sense. Both the DGP label and the bias values appear to be wrong in the method text—this is a significant error that needs correcting.

Let me explore whether there's an alternative explanation. Maybe the 0.003-0.004 represents some kind of aggregated bias across subgroups or a different calculation altogether. If I average the DGP B values, I get (0.015+0.020)/2 = 0.0175, which still doesn't match. Or perhaps it's showing how much PPCI improves upon EC-HTE in DGP B—but even checking those numbers, the improvement doesn't yield 0.003-0.004 either.

I'm flagging this as a critical discrepancy that needs investigation before finalizing the report. While I'm at it, let me verify the 27% RMSE advantage claim in the methods section for DGP A. Computing from the table: EC-HTE averages around 0.1025 RMSE while PPCI averages 0.165, which gives roughly a 38% advantage, not 27%. I'm getting the same ratio whether I use arithmetic or geometric means, so there's another inconsistency to resolve. I've tried every angle with the PPCI data and can't get to 27% — none of the calculations match. I'll mark this as a warning and move forward with writing the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "d2226f6c-20aa-4eaa-ba4f-c710da3254a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SkBMazW8uE58zEByfMf9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28391,
      "cache_read_input_tokens": 84582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28391
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 108_

All data collected. Now compiling the comprehensive audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "c7d4d2e5-11a5-4e18-977c-8c3eb17ca2a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SkBMazW8uE58zEByfMf9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28391,
      "cache_read_input_tokens": 84582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28391
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 109_

<details open><summary>🔧 Tool call — Bash · `toolu_01AxRbgjvNDvJCjRzguwpiWB`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/_project/report/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if report directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "b4163acc-e04b-44ac-8072-abf7aa83ca3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SkBMazW8uE58zEByfMf9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28391,
      "cache_read_input_tokens": 84582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28391
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 110 · 2026-05-24T04:42:35.391Z_

<details><summary>↩ Tool result · `toolu_01AxRbgjvNDvJCjRzguwpiWB`</summary>

```text
total 264
drwxr-xr-x 2 ubuntu ubuntu  4096 May 23 22:59 .
drwxr-xr-x 7 ubuntu ubuntu  4096 May 21 05:56 ..
-rw-r--r-- 1 ubuntu ubuntu  3768 May 21 21:33 budget_sweep_k2_analysis.md
-rw-r--r-- 1 ubuntu ubuntu  1905 May 21 21:08 budget_sweep_k4_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 14426 May 23 11:16 data_audit_report.md
-rw-r--r-- 1 ubuntu ubuntu 14426 May 23 11:16 data_audit_report_33f2c7.md
-rw-r--r-- 1 ubuntu ubuntu 13398 May 23 19:49 data_integrity_audit.md
-rw-r--r-- 1 ubuntu ubuntu  7495 May 23 20:17 data_integrity_audit_v2.md
-rw-r--r-- 1 ubuntu ubuntu  2380 May 23 11:33 data_integrity_fixes.md
-rw-r--r-- 1 ubuntu ubuntu 10701 May 20 21:29 dataset_survey.md
-rw-r--r-- 1 ubuntu ubuntu  5064 May 21 15:16 delta_pi_only_auc.md
-rw-r--r-- 1 ubuntu ubuntu  3241 May 20 22:10 exp003_dgp_spec.md
-rw-r--r-- 1 ubuntu ubuntu 13563 May 21 14:43 exp015_016_deep_dive.md
-rw-rw-r-- 1 ubuntu ubuntu  2320 May 23 07:24 exp_asym_diag_v2_analysis.md
-rw-r--r-- 1 ubuntu ubuntu  4604 May 21 22:13 gemma_sweep_analysis.md
-rw-r--r-- 1 ubuntu ubuntu  3096 May 21 20:40 llama_analysis.md
-rw-r--r-- 1 ubuntu ubuntu  8772 May 21 00:50 llm_alternatives_assessment.md
-rw-r--r-- 1 ubuntu ubuntu 38945 May 21 11:54 mc_se_summary.md
-rw-r--r-- 1 ubuntu ubuntu  4620 May 21 22:13 mistral_sweep_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 10521 May 22 00:10 number_consistency_check.md
-rw-r--r-- 1 ubuntu ubuntu  4329 May 21 21:54 qwen_sweep_analysis.md
-rw-r--r-- 1 ubuntu ubuntu  7295 May 23 10:07 rebuttal_talking_points.md
-rw-r--r-- 1 ubuntu ubuntu  8222 May 23 22:58 rebuttal_talking_points_3cdd55.md
-rw-r--r-- 1 ubuntu ubuntu  9875 May 23 21:29 stance_analysis_report.md
-rw-r--r-- 1 ubuntu ubuntu  7131 May 23 12:18 submission_checklist.md
-rw-r--r-- 1 ubuntu ubuntu  9603 May 20 21:45 tweeteval_exploration.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "88e37619-a2d6-4d70-a953-9c375d4db4cb",
  "tool_use_result": {
    "stdout": "total 264\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 23 22:59 .\ndrwxr-xr-x 7 ubuntu ubuntu  4096 May 21 05:56 ..\n-rw-r--r-- 1 ubuntu ubuntu  3768 May 21 21:33 budget_sweep_k2_analysis.md\n-rw-r--r-- 1 ubuntu ubuntu  1905 May 21 21:08 budget_sweep_k4_analysis.md\n-rw-r--r-- 1 ubuntu ubuntu 14426 May 23 11:16 data_audit_report.md\n-rw-r--r-- 1 ubuntu ubuntu 14426 May 23 11:16 data_audit_report_33f2c7.md\n-rw-r--r-- 1 ubuntu ubuntu 13398 May 23 19:49 data_integrity_audit.md\n-rw-r--r-- 1 ubuntu ubuntu  7495 May 23 20:17 data_integrity_audit_v2.md\n-rw-r--r-- 1 ubuntu ubuntu  2380 May 23 11:33 data_integrity_fixes.md\n-rw-r--r-- 1 ubuntu ubuntu 10701 May 20 21:29 dataset_survey.md\n-rw-r--r-- 1 ubuntu ubuntu  5064 May 21 15:16 delta_pi_only_auc.md\n-rw-r--r-- 1 ubuntu ubuntu  3241 May 20 22:10 exp003_dgp_spec.md\n-rw-r--r-- 1 ubuntu ubuntu 13563 May 21 14:43 exp015_016_deep_dive.md\n-rw-rw-r-- 1 ubuntu ubuntu  2320 May 23 07:24 exp_asym_diag_v2_analysis.md\n-rw-r--r-- 1 ubuntu ubuntu  4604 May 21 22:13 gemma_sweep_analysis.md\n-rw-r--r-- 1 ubuntu ubuntu  3096 May 21 20:40 llama_analysis.md\n-rw-r--r-- 1 ubuntu ubuntu  8772 May 21 00:50 llm_alternatives_assessment.md\n-rw-r--r-- 1 ubuntu ubuntu 38945 May 21 11:54 mc_se_summary.md\n-rw-r--r-- 1 ubuntu ubuntu  4620 May 21 22:13 mistral_sweep_analysis.md\n-rw-r--r-- 1 ubuntu ubuntu 10521 May 22 00:10 number_consistency_check.md\n-rw-r--r-- 1 ubuntu ubuntu  4329 May 21 21:54 qwen_sweep_analysis.md\n-rw-r--r-- 1 ubuntu ubuntu  7295 May 23 10:07 rebuttal_talking_points.md\n-rw-r--r-- 1 ubuntu ubuntu  8222 May 23 22:58 rebuttal_talking_points_3cdd55.md\n-rw-r--r-- 1 ubuntu ubuntu  9875 May 23 21:29 stance_analysis_report.md\n-rw-r--r-- 1 ubuntu ubuntu  7131 May 23 12:18 submission_checklist.md\n-rw-r--r-- 1 ubuntu ubuntu  9603 May 20 21:45 tweeteval_exploration.md",
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

_source line 111_

<details open><summary>🔧 Tool call — Write · `toolu_01V7c5sBf5kVwDtVX5ga4VVL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/_project/report/number_audit_report.md",
  "content": "# 数字核查报告 (2026-05-24)\n\n## A. 追溯性检查\n\n### Abstract 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| R²≥0.97 | abstract.tex:5 | exp-002 (K2=0.994, K4=0.974), exp-019 (≥0.976), exp-024 (0.975) | ✅ | K4=0.974 四舍五入到0.97 |\n| 14.9% at τ(0)=0.03 | abstract.tex:5 | exp-038 reversal_pct_tau003=14.9 | ✅ | 精确匹配 |\n| 5× across subgroups | abstract.tex:3 | N/A（文献引用 Ashwin et al.） | ✅ | 非本文实验数据 |\n| 7.4× bias reduction | abstract.tex:7 | 由 Table 1 推导: 0.059/0.008=7.375≈7.4× | ✅ | exp-039 K2_bias=0.008 |\n| AUC=1.0 | abstract.tex:6 | exp-028 K4 perfect combos (Llama/Qwen/Mistral/gpt-4o) | ✅ | Δτ>0 子集 |\n| AUC=0.86 | abstract.tex:6 | exp-005 subgroup AUC=0.833; ROC figure caption=0.86 | ⚠️ | registry 0.833 vs paper 0.86，见问题 W1 |\n| AUC=0.63 | abstract.tex:6 | exp-028 overall symmetric AUC=0.626 | ✅ | 0.626≈0.63 |\n| 11 empirical CMs | abstract.tex:5 | exp-024 n_llm_dataset_combos=11 | ✅ | 精确匹配 |\n\n### Experiments.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| 0.059 (global bias K=2) | experiments.tex:25 | Table 1 行47 | ✅ | 内部一致 |\n| 0.008 (HB bias K=2) | experiments.tex:27 | exp-039 K2_echte_bias=0.008 | ✅ | 精确匹配 |\n| 7.4× | experiments.tex:27 | 0.059/0.008=7.375 | ✅ | 四舍五入 |\n| 4.7× (K=4 DIM) | experiments.tex:27 | 0.056/0.012=4.667 | ✅ | 四舍五入到4.7 |\n| 4.9× (CF) | experiments.tex:33 | 0.191/0.039=4.897 | ✅ | 四舍五入到4.9 |\n| 5.9× (CF amplification) | experiments.tex:33 | exp-011 debiasing_hurts_max_ratio=5.9 | ✅ | 精确匹配 |\n| 93.8% (CF coverage) | experiments.tex:65 | exp-036 plugin_coverage=0.9375 | ✅ | 0.9375→93.8% |\n| 260/520 configs | experiments.tex:18 | exp-002 \"260/520 (excluding dc=0)\" | ✅ | 精确匹配 |\n| 2.86× (K=2) | experiments.tex:18 | exp-002 max_bias_ratio_k2=2.86 | ✅ | 精确匹配 |\n| 2.41× (K=4) | experiments.tex:18 | exp-002 max_bias_ratio_k4=2.41 | ✅ | 精确匹配 |\n| 89% R-learner | experiments.tex:34 | exp-017 \"89% reduction\" (0.121→0.013) | ✅ | 1-0.013/0.121=89.3% |\n| 14.9% sign reversal | experiments.tex:19 | exp-038 | ✅ | 同 abstract |\n| 31% at τ(0)=0.01 | experiments.tex:19 | exp-038 reversal_pct_tau001=31 | ✅ | 精确匹配 |\n| 0.94–0.96 coverage | experiments.tex:27 | exp-039 K2=0.938, K4=0.956 | ✅ | 0.938≈0.94, 0.956≈0.96 |\n\n### Table 1 完整核查 (experiments.tex:40-66)\n\n| Config | Method | |Bias| | RMSE | Cov | 来源 | 匹配? |\n|--------|--------|-------|------|------|------|-------|\n| DIM K=2 | Naive | 0.058 | 0.090 | 0.82 | exp-001/exp-039 | ✅ |\n| DIM K=2 | Global | 0.059 | 0.099 | 0.87 | exp-001/exp-039 | ✅ |\n| DIM K=2 | F-L Scalar | 0.122 | 0.159 | 0.68 | exp-034 | ✅ |\n| DIM K=2 | F-L Per-sub | 0.168 | 0.220 | 0.65 | exp-034 | ✅ |\n| DIM K=2 | Strat MLE | 0.012 | 0.094 | 0.95 | exp-001 | ✅ |\n| DIM K=2 | HB EC-HTE | 0.008 | 0.089 | 0.94 | exp-039 K2_bias=0.008, RMSE=0.089, cov=0.938 | ✅ |\n| DIM K=4 | Naive | 0.062 | 0.113 | 0.88 | exp-001/exp-039 | ✅ |\n| DIM K=4 | Global | 0.056 | 0.125 | 0.91 | exp-001/exp-039 | ✅ |\n| DIM K=4 | Strat MLE | 0.010 | 0.127† | 0.95 | exp-001 | ✅ |\n| DIM K=4 | HB EC-HTE | 0.012 | 0.120 | 0.96 | exp-039 K4_bias=0.012, RMSE=0.120, cov=0.956 | ✅ |\n| CF K=4 | Naive | 0.208 | 0.231 | 0.44 | exp-011 specific config | ✅ |\n| CF K=4 | Global | 0.191 | 0.244 | 0.58 | exp-011 specific config | ✅ |\n| CF K=4 | EC-HTE Forest | 0.039 | 0.180 | 0.90 | exp-011 specific config | ✅ |\n\n### Theory.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| R²=0.994 (K=2) | theory.tex:93 | exp-002 R²_K2=0.9939 | ✅ | 0.994 |\n| R²=0.97 (K=4) | theory.tex:93 | exp-002 R²_K4=0.9738 | ✅ | 四舍五入 |\n| R²≥0.976 at P(Z=1)=0.1 | theory.tex:92 | exp-019 K2/P0.1=0.998, K4/P0.1=0.984 | ✅ | min=0.976 |\n| RMSE ratio 1.06–1.68 | theory.tex:92 | exp-019 K4 ratios: 1.54,1.68,1.12,1.08,1.06 | ✅ | 精确匹配 |\n| γ_T=0.10 → 75% coverage | theory.tex:98 | exp-040 gamma010_cov=0.750 | ✅ | 精确匹配 |\n| F-L 0.058→0.122 (2.1×) | theory.tex:54 | Table 1: naive=0.058, F-L=0.122 | ✅ | 0.122/0.058=2.10 |\n| F-L per-sub 0.168 (2.9×) | theory.tex:54 | Table 1: F-L Per-sub=0.168 | ✅ | 0.168/0.058=2.90 |\n| R²=0.991 (asymmetric) | theory.tex:67 | exp-014 R²=0.992 | ⚠️ | 0.991 vs 0.992，差0.001 |\n| AUC 0.86→0.66 (asymmetric) | theory.tex:64 | appendix.tex:176 AUC=0.66 | ✅ | 合成数据非对称实验 |\n| ≥93% coverage | theory.tex:87 | exp-039/多个实验 | ✅ | A5 violation 下 ≥93% |\n| 50% of K=2 configs (260/520) | theory.tex:120 | exp-002 | ✅ | 同 experiments.tex |\n| 2.86× / 2.41× | theory.tex:120 | exp-002 | ✅ | 同上 |\n\n### Method.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| RMSE change ≤4% | method.tex:12 | exp-022: K2<1%, K4≈4-5% | ⚠️ | K4超过4%，见问题 W2 |\n| <5% RMSE variation | method.tex:21 | exp-022: K4≈4-5% | ✅ | <5% 准确 |\n| 2× perturbation | method.tex:12 | exp-022 scale range 0.5-2.0 | ✅ | |\n| 87.5% (21/24) HB>MLE | method.tex:18 | exp-006 \"87.5%\" | ✅ | 21/24=87.5% |\n| ≥93% coverage (κ range) | method.tex:33 | appendix kappa analysis: ≥93.2% | ✅ | |\n| AUC=0.86 (diagnostic) | method.tex:53 | exp-005 subgroup AUC=0.833 | ⚠️ | 见问题 W1 |\n| |bias| 0.179→0.007 | method.tex:60 | PPCI table DGP C z=0 | ✅ | 精确匹配 |\n| 27% RMSE advantage | method.tex:61 | PPCI table DGP A | ❌ | 见问题 C1 |\n| |bias|=0.003–0.004 (DGP C) | method.tex:61 | PPCI table | ❌ | 见问题 C2 |\n| \"outcome-side error alone (DGP C)\" | method.tex:61 | appendix DGP定义 | ❌ | 见问题 C2 |\n| ≥93% coverage A5 | method.tex:87 | A5 violation table: EC-HTE≥0.94 | ✅ | |\n\n### Introduction.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| 5× (literature) | intro.tex:10 | N/A (Ashwin et al.) | ✅ | |\n| Δπ>0.20 | intro.tex:10 | Ashwin et al. 文献引用 | ✅ | |\n| 0.15 threshold | intro.tex:10 | 论文 operating conditions | ✅ | |\n| GPT-4.1 85.8% accuracy | intro.tex:10 | exp-012 accuracy_binary=0.858 | ✅ | |\n| 10.2%–20.0% error range | intro.tex:10 | exp-008/exp-012 pilot data | ✅ | 20.0-10.2=0.098=Δπ |\n| Δπ=0.098 | intro.tex:10 | exp-008 GPT-4.1 Δπ=0.098 | ✅ | |\n| 14.9% | intro.tex:13 | exp-038 | ✅ | |\n| 31% at τ(0)=0.01 | intro.tex:13 | exp-038 | ✅ | |\n| τ̂=−0.059 | intro.tex:13 | policy_reversal table τ(0)=0.03 extreme | ✅ | appendix.tex:1501 |\n| 5.9× (K=4 CF) | intro.tex:14 | exp-011 | ✅ | |\n| 2.9× (F-L) | intro.tex:14 | 0.168/0.058=2.897 | ✅ | |\n| 0.059→0.008 | intro.tex:20 | Table 1 | ✅ | |\n| R²≥0.97 | intro.tex:17,34 | exp-002 | ✅ | |\n| AUC=1.0 | intro.tex:18,35 | exp-028 | ✅ | |\n| 7.5% subgroup estimates | intro.tex:28 (Fig caption) | 具体配置数据 | ⚠️ | 非 registry 顶层指标，需从原始CSV验证 |\n\n### Appendix 数字（代表性抽查）\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| K=8 coverage≥95.6% | appendix.tex:381 | exp-030/exp-039 K8 cov=0.956 | ✅ | |\n| R²=0.975 (11 real CMs) | appendix.tex:979 | exp-024 R²=0.975 | ✅ | |\n| R²=0.991 (asymmetric) | appendix.tex:437 | exp-014 R²=0.992 | ⚠️ | 差0.001 |\n| 4× bias reduction (asym) | appendix.tex:439 | exp-014 bias_reduction=4.2× | ⚠️ | 论文4×, registry 4.2× |\n| 93.8% plugin coverage | appendix.tex:1101 | exp-036 0.9375 | ✅ | |\n| 95.0% bootstrap coverage | appendix.tex:1107 | exp-036 boot_cov=0.950 | ✅ | |\n| 89% R-learner reduction | appendix.tex:835 | exp-017 | ✅ | 1-0.013/0.121=89.3% |\n| 13.3% stance sign rev (Global) | appendix_stance.tex:10 | 4/30=0.133 | ✅ | 内部算术 |\n| 3.3% stance sign rev (EC-HTE) | appendix_stance.tex:10 | 1/30=0.033 | ✅ | |\n| ≥94.5% confounded coverage | appendix.tex:1386 | exp-032 all HB cov≥0.945 | ✅ | |\n\n### Limitations.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| K=8 coverage≥95.6% | limitations.tex:5 | exp-030 cov=0.956 | ✅ | |\n| AUC=0.86 synthetic | limitations.tex:6 | ROC figure, exp-005 | ⚠️ | 同问题 W1 |\n| AUC=0.63 real LLM | limitations.tex:6 | exp-028 AUC=0.626 | ✅ | |\n| ≥93.5% outcome-dep | limitations.tex:9 | exp-029 全γ范围≥93.5% | ✅ | |\n| ≥89.7% treatment-dep | limitations.tex:9 | exp-040 γ=0.05 cov=0.897 | ✅ | |\n\n---\n\n## B. 跨位置一致性\n\n| 数字 | 出现位置 | 值是否一致 | 备注 |\n|------|---------|-----------|------|\n| R²≥0.97 | abstract:5, intro:17, intro:34, theory:93, experiments:17 | ✅ 一致 | 所有位置均为 ≥0.97 |\n| 14.9% sign reversal | abstract:5, intro:13, experiments:19, Fig1 caption | ✅ 一致 | |\n| 11 empirical CMs | abstract:5, intro:17, experiments:11, conclusion:4 | ✅ 一致 | |\n| AUC 1.0/0.86/0.63 | abstract:6, intro:18,35, method:53, experiments:72, limitations:6 | ✅ 一致 | 各位置引用一致（但registry值存疑，见W1） |\n| 7.4× bias reduction | abstract:7, experiments:27 | ✅ 一致 | intro:20 用 0.059→0.008 表述 |\n| 0.059 / 0.008 | intro:20, experiments:25,27, Table 1 | ✅ 一致 | |\n| 5.9× CF amplification | intro:14, experiments:33 | ✅ 一致 | |\n| 260/520 (50%) | theory:120, experiments:18 | ✅ 一致 | |\n| 2.86× / 2.41× | theory:120, experiments:18 | ✅ 一致 | |\n| 93.8% CF coverage | experiments:65, appendix:1101 | ✅ 一致 | |\n| 89% R-learner | experiments:34, appendix:488,835 | ✅ 一致 | |\n| 0.179→0.007 (PPCI) | method:60, appendix:488,518 | ✅ 一致 | |\n| γ_T=0.10 → 75% | theory:98 | ✅ | 仅出现一次（正文），appendix table确认 |\n| F-L 0.122 / 0.168 | theory:54, experiments:26, Table 1 | ✅ 一致 | |\n| F-L 2.1× / 2.9× | theory:54, intro:14(仅2.9×) | ✅ 一致 | |\n| RMSE change ≤4% vs <5% | method:12 vs method:21 | ❌ 不一致 | 见问题 W2 |\n\n---\n\n## C. 四舍五入一致性\n\n| 类型 | 小数位数 | 示例 | 一致? |\n|------|---------|------|-------|\n| |Bias| | 3位 | 0.058, 0.059, 0.008, 0.012 | ✅ |\n| RMSE | 3位 | 0.090, 0.099, 0.089, 0.120 | ✅ |\n| Coverage | 2位 | 0.82, 0.87, 0.94, 0.96 | ✅ |\n| R² | 2-3位 | 0.97, 0.994, 0.976 | ✅ 可接受（≥0.97用2位，具体值用3位） |\n| AUC | 2位 | 0.86, 0.63, 1.0 | ✅ |\n| 百分比 | 1位或整数 | 14.9%, 31%, 93.8%, 89% | ✅ |\n| 倍数 | 1-2位 | 7.4×, 4.7×, 2.86×, 2.41× | ⚠️ 不完全一致 |\n\n倍数的小数位数不统一：7.4×/4.7×/4.9×/5.9× 用1位，2.86×/2.41× 用2位。但 2.86 和 2.41 是精确的 max 值（registry 直接存储），而 7.4/4.7/4.9 是从 table 值推导的四舍五入。逻辑上合理但格式不完全统一。**建议统一为1位或注明 max 值保留2位。**\n\n---\n\n## 问题汇总\n\n### [CRITICAL] C1: method.tex:61 DGP 标签错误\n\n**位置**: method.tex:61\n**内容**: \"under outcome-side error alone (DGP~C)\"\n**问题**: DGP C 在 appendix PPCI table 中定义为 \"both errors\"（covariate + outcome），而 \"outcome-side error alone\" 对应 DGP B。DGP 标签写反。\n\n**修复**: 将 \"(DGP~C)\" 改为 \"(DGP~B)\"。\n\n### [CRITICAL] C2: method.tex:61 PPCI |bias| 值不匹配\n\n**位置**: method.tex:61\n**内容**: \"PPCI achieves $|\\text{bias}| = 0.003$--$0.004$\"\n**问题**: 无论对应哪个 DGP，PPCI table 中都没有 0.003–0.004 这个范围：\n- DGP B (outcome only) PPCI: |bias| z=0=0.015, z=1=0.020\n- DGP C (both) PPCI: |bias| z=0=0.017, z=1=0.007\n- DGP D (no error) PPCI: z=0=0.007, z=1=0.003\n\n0.003–0.004 不匹配任何 DGP 的 PPCI 结果。最接近的是 DGP D z=1=0.003，但 DGP D 是 \"no error\" 场景，语境不对。\n\n**修复**: 需要确认正确的 DGP 标签和对应的 bias 值。如果指 DGP B，bias 应为 0.015–0.020。\n\n### [CRITICAL] C3: method.tex:61 \"27% RMSE advantage\" 无法复现\n\n**位置**: method.tex:61\n**内容**: \"under covariate-side error alone (DGP~A), EC-HTE provides a 27\\% RMSE advantage over PPCI\"\n**问题**: 从 PPCI table DGP A 计算：\n- EC-HTE avg RMSE = (0.097+0.108)/2 = 0.1025\n- PPCI avg RMSE = (0.162+0.168)/2 = 0.165\n- Advantage = 1 - 0.1025/0.165 = **37.9%**，非 27%\n\n尝试了多种聚合方式（单z-level, 几何均值等），均无法得到27%。\n\n**修复**: 需要确认计算方式。如果是从 table 直接推导，应改为约38%，或注明计算口径。\n\n### [WARNING] W1: AUC=0.86 与 registry 不完全匹配\n\n**位置**: abstract:6, intro:18,35, method:53, experiments:72, limitations:6\n**Registry**: exp-005 subgroup AUC=0.833\n**Paper**: 0.86\n\n**分析**: ROC figure caption 标注 \"Δπ-only condition (AUC = 0.86)\"。exp-005 registry 中 \"Subgroup correlation: 0.86\" 与 \"Subgroup AUC: 0.833\" 是两个不同指标。论文中统一称为 \"AUC=0.86\"，但 registry 的实际 AUC 是 0.833。可能是不同评分规则（Proposition 2 score vs Δπ-only score）给出的不同 AUC 值。\n\n**建议**: 确认论文中的 0.86 对应 ROC 曲线中哪条具体曲线的 AUC，确保描述准确。\n\n### [WARNING] W2: method.tex 内部 hyperprior sensitivity 不一致\n\n**位置**: method.tex:12 说 \"RMSE change ≤4%\"，method.tex:21 说 \"<5% RMSE variation\"\n**Registry**: exp-022 报告 K2 <1%, K4 ≈4-5%\n**Appendix**: appendix.tex:278 说 \"<1% RMSE variation for K=2 and ~4-5% for K=4\"\n\n**问题**: K=4 的 RMSE 变化为 4-5%，超过 method.tex:12 的 \"≤4%\" 声明，但符合 method.tex:21 的 \"<5%\"。同一篇论文中两处描述不一致。\n\n**修复**: 将 method.tex:12 的 \"≤4%\" 改为 \"≤5%\" 或 \"<5%\"，与 method.tex:21 和 appendix 保持一致。\n\n### [WARNING] W3: theory.tex R² 与 registry 差 0.001\n\n**位置**: theory.tex:67 说 R²=0.991（asymmetric），appendix.tex:437 同\n**Registry**: exp-014 R²=0.992\n\n**分析**: 差 0.001，可能是四舍五入差异（0.9915 四舍五入到 0.991 或 0.992）。影响极小。\n\n### [WARNING] W4: appendix asymmetric bias reduction 4× vs registry 4.2×\n\n**位置**: appendix.tex:439 \"4× improvement\"\n**Registry**: exp-014 bias_reduction_vs_global=4.2×\n**Table**: 0.025/0.006=4.17\n\n**分析**: 论文约为 4×（0.025→0.006），精确计算为 4.17×。Registry 存 4.2×。论文用 4× 是粗略近似，差异不大但略不精确。\n\n### [WARNING] W5: Figure 1 caption \"7.5% of subgroup estimates\"\n\n**位置**: intro.tex:28\n**问题**: 7.5% 是 subgroup-estimate level 的 sign reversal rate（vs 14.9% 是 configuration level）。该数字未作为 registry 顶层指标存储，需从原始实验 CSV 验证。\n\n**建议**: 确认 7.5% 的具体计算口径（哪些 subgroup × z-level estimates 中有 7.5% 出现符号翻转）。\n\n---\n\n## 其他检查\n\n### 8 LLMs 计数验证\n- 论文声称 \"8 LLMs\" (experiments.tex:11)\n- appendix realcm_bias (appendix.tex:951) 列出 8 个模型: GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B\n- 另有 GPT-5.4（exp-008 multi-LLM）和 Llama-3.1-8B（appendix open-source）未纳入 \"8 LLMs\" 主体分析\n- ✅ 计数正确\n\n### 16 model–dataset–K combinations 验证\n- appendix screening table (appendix.tex:996-1016): 正好 16 行\n- 4 open-source × TweetEval × K=2 + 4 open-source × TweetEval × K=4 + 5 proprietary × TweetEval × K=4 + 3 proprietary × CivilComments × K=4 = 4+4+5+3 = 16\n- ✅ 正确\n\n### Policy reversal table 内部一致性\n- τ(0)=0.03, extreme: τ̂=-0.059 (appendix.tex:1501)\n- intro.tex:13,28: \"true τ=+0.03, estimated τ̂=-0.059\"\n- ✅ 一致\n\n---\n\n## 结论\n\n**共检查 ~80 个关键数字。**\n\n- **3 个 CRITICAL 问题** (method.tex:61): DGP 标签错误(C→B)、PPCI |bias| 值不匹配(0.003-0.004 无出处)、27% RMSE advantage 无法复现(实际≈38%)。三个问题出现在同一句话中，需要整体修改。\n- **5 个 WARNING** (W1-W5): AUC 0.86 vs registry 0.833 需澄清、hyperprior sensitivity ≤4% vs <5% 内部不一致、两处 ≤0.001 的四舍五入差异、一处未验证的 Figure 数字。\n- **其余所有数字均与 registry 精确匹配或在合理四舍五入范围内。**\n\n**优先修复**: method.tex:61 的三个 CRITICAL 问题（同一句话），以及 method.tex:12 的 ≤4%→<5%。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "5ed0e9fc-64da-4fa0-b16a-3c8c51b8da59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfyACXYLBqDW8DpEjGxcNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2491,
      "cache_read_input_tokens": 112973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2491
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

_source line 112 · 2026-05-24T04:45:32.898Z_

<details><summary>↩ Tool result · `toolu_01V7c5sBf5kVwDtVX5ga4VVL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/_project/report/number_audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "48339a82-9b4b-4701-ab19-f607b3915c96",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/_project/report/number_audit_report.md",
    "content": "# 数字核查报告 (2026-05-24)\n\n## A. 追溯性检查\n\n### Abstract 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| R²≥0.97 | abstract.tex:5 | exp-002 (K2=0.994, K4=0.974), exp-019 (≥0.976), exp-024 (0.975) | ✅ | K4=0.974 四舍五入到0.97 |\n| 14.9% at τ(0)=0.03 | abstract.tex:5 | exp-038 reversal_pct_tau003=14.9 | ✅ | 精确匹配 |\n| 5× across subgroups | abstract.tex:3 | N/A（文献引用 Ashwin et al.） | ✅ | 非本文实验数据 |\n| 7.4× bias reduction | abstract.tex:7 | 由 Table 1 推导: 0.059/0.008=7.375≈7.4× | ✅ | exp-039 K2_bias=0.008 |\n| AUC=1.0 | abstract.tex:6 | exp-028 K4 perfect combos (Llama/Qwen/Mistral/gpt-4o) | ✅ | Δτ>0 子集 |\n| AUC=0.86 | abstract.tex:6 | exp-005 subgroup AUC=0.833; ROC figure caption=0.86 | ⚠️ | registry 0.833 vs paper 0.86，见问题 W1 |\n| AUC=0.63 | abstract.tex:6 | exp-028 overall symmetric AUC=0.626 | ✅ | 0.626≈0.63 |\n| 11 empirical CMs | abstract.tex:5 | exp-024 n_llm_dataset_combos=11 | ✅ | 精确匹配 |\n\n### Experiments.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| 0.059 (global bias K=2) | experiments.tex:25 | Table 1 行47 | ✅ | 内部一致 |\n| 0.008 (HB bias K=2) | experiments.tex:27 | exp-039 K2_echte_bias=0.008 | ✅ | 精确匹配 |\n| 7.4× | experiments.tex:27 | 0.059/0.008=7.375 | ✅ | 四舍五入 |\n| 4.7× (K=4 DIM) | experiments.tex:27 | 0.056/0.012=4.667 | ✅ | 四舍五入到4.7 |\n| 4.9× (CF) | experiments.tex:33 | 0.191/0.039=4.897 | ✅ | 四舍五入到4.9 |\n| 5.9× (CF amplification) | experiments.tex:33 | exp-011 debiasing_hurts_max_ratio=5.9 | ✅ | 精确匹配 |\n| 93.8% (CF coverage) | experiments.tex:65 | exp-036 plugin_coverage=0.9375 | ✅ | 0.9375→93.8% |\n| 260/520 configs | experiments.tex:18 | exp-002 \"260/520 (excluding dc=0)\" | ✅ | 精确匹配 |\n| 2.86× (K=2) | experiments.tex:18 | exp-002 max_bias_ratio_k2=2.86 | ✅ | 精确匹配 |\n| 2.41× (K=4) | experiments.tex:18 | exp-002 max_bias_ratio_k4=2.41 | ✅ | 精确匹配 |\n| 89% R-learner | experiments.tex:34 | exp-017 \"89% reduction\" (0.121→0.013) | ✅ | 1-0.013/0.121=89.3% |\n| 14.9% sign reversal | experiments.tex:19 | exp-038 | ✅ | 同 abstract |\n| 31% at τ(0)=0.01 | experiments.tex:19 | exp-038 reversal_pct_tau001=31 | ✅ | 精确匹配 |\n| 0.94–0.96 coverage | experiments.tex:27 | exp-039 K2=0.938, K4=0.956 | ✅ | 0.938≈0.94, 0.956≈0.96 |\n\n### Table 1 完整核查 (experiments.tex:40-66)\n\n| Config | Method | |Bias| | RMSE | Cov | 来源 | 匹配? |\n|--------|--------|-------|------|------|------|-------|\n| DIM K=2 | Naive | 0.058 | 0.090 | 0.82 | exp-001/exp-039 | ✅ |\n| DIM K=2 | Global | 0.059 | 0.099 | 0.87 | exp-001/exp-039 | ✅ |\n| DIM K=2 | F-L Scalar | 0.122 | 0.159 | 0.68 | exp-034 | ✅ |\n| DIM K=2 | F-L Per-sub | 0.168 | 0.220 | 0.65 | exp-034 | ✅ |\n| DIM K=2 | Strat MLE | 0.012 | 0.094 | 0.95 | exp-001 | ✅ |\n| DIM K=2 | HB EC-HTE | 0.008 | 0.089 | 0.94 | exp-039 K2_bias=0.008, RMSE=0.089, cov=0.938 | ✅ |\n| DIM K=4 | Naive | 0.062 | 0.113 | 0.88 | exp-001/exp-039 | ✅ |\n| DIM K=4 | Global | 0.056 | 0.125 | 0.91 | exp-001/exp-039 | ✅ |\n| DIM K=4 | Strat MLE | 0.010 | 0.127† | 0.95 | exp-001 | ✅ |\n| DIM K=4 | HB EC-HTE | 0.012 | 0.120 | 0.96 | exp-039 K4_bias=0.012, RMSE=0.120, cov=0.956 | ✅ |\n| CF K=4 | Naive | 0.208 | 0.231 | 0.44 | exp-011 specific config | ✅ |\n| CF K=4 | Global | 0.191 | 0.244 | 0.58 | exp-011 specific config | ✅ |\n| CF K=4 | EC-HTE Forest | 0.039 | 0.180 | 0.90 | exp-011 specific config | ✅ |\n\n### Theory.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| R²=0.994 (K=2) | theory.tex:93 | exp-002 R²_K2=0.9939 | ✅ | 0.994 |\n| R²=0.97 (K=4) | theory.tex:93 | exp-002 R²_K4=0.9738 | ✅ | 四舍五入 |\n| R²≥0.976 at P(Z=1)=0.1 | theory.tex:92 | exp-019 K2/P0.1=0.998, K4/P0.1=0.984 | ✅ | min=0.976 |\n| RMSE ratio 1.06–1.68 | theory.tex:92 | exp-019 K4 ratios: 1.54,1.68,1.12,1.08,1.06 | ✅ | 精确匹配 |\n| γ_T=0.10 → 75% coverage | theory.tex:98 | exp-040 gamma010_cov=0.750 | ✅ | 精确匹配 |\n| F-L 0.058→0.122 (2.1×) | theory.tex:54 | Table 1: naive=0.058, F-L=0.122 | ✅ | 0.122/0.058=2.10 |\n| F-L per-sub 0.168 (2.9×) | theory.tex:54 | Table 1: F-L Per-sub=0.168 | ✅ | 0.168/0.058=2.90 |\n| R²=0.991 (asymmetric) | theory.tex:67 | exp-014 R²=0.992 | ⚠️ | 0.991 vs 0.992，差0.001 |\n| AUC 0.86→0.66 (asymmetric) | theory.tex:64 | appendix.tex:176 AUC=0.66 | ✅ | 合成数据非对称实验 |\n| ≥93% coverage | theory.tex:87 | exp-039/多个实验 | ✅ | A5 violation 下 ≥93% |\n| 50% of K=2 configs (260/520) | theory.tex:120 | exp-002 | ✅ | 同 experiments.tex |\n| 2.86× / 2.41× | theory.tex:120 | exp-002 | ✅ | 同上 |\n\n### Method.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| RMSE change ≤4% | method.tex:12 | exp-022: K2<1%, K4≈4-5% | ⚠️ | K4超过4%，见问题 W2 |\n| <5% RMSE variation | method.tex:21 | exp-022: K4≈4-5% | ✅ | <5% 准确 |\n| 2× perturbation | method.tex:12 | exp-022 scale range 0.5-2.0 | ✅ | |\n| 87.5% (21/24) HB>MLE | method.tex:18 | exp-006 \"87.5%\" | ✅ | 21/24=87.5% |\n| ≥93% coverage (κ range) | method.tex:33 | appendix kappa analysis: ≥93.2% | ✅ | |\n| AUC=0.86 (diagnostic) | method.tex:53 | exp-005 subgroup AUC=0.833 | ⚠️ | 见问题 W1 |\n| |bias| 0.179→0.007 | method.tex:60 | PPCI table DGP C z=0 | ✅ | 精确匹配 |\n| 27% RMSE advantage | method.tex:61 | PPCI table DGP A | ❌ | 见问题 C1 |\n| |bias|=0.003–0.004 (DGP C) | method.tex:61 | PPCI table | ❌ | 见问题 C2 |\n| \"outcome-side error alone (DGP C)\" | method.tex:61 | appendix DGP定义 | ❌ | 见问题 C2 |\n| ≥93% coverage A5 | method.tex:87 | A5 violation table: EC-HTE≥0.94 | ✅ | |\n\n### Introduction.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| 5× (literature) | intro.tex:10 | N/A (Ashwin et al.) | ✅ | |\n| Δπ>0.20 | intro.tex:10 | Ashwin et al. 文献引用 | ✅ | |\n| 0.15 threshold | intro.tex:10 | 论文 operating conditions | ✅ | |\n| GPT-4.1 85.8% accuracy | intro.tex:10 | exp-012 accuracy_binary=0.858 | ✅ | |\n| 10.2%–20.0% error range | intro.tex:10 | exp-008/exp-012 pilot data | ✅ | 20.0-10.2=0.098=Δπ |\n| Δπ=0.098 | intro.tex:10 | exp-008 GPT-4.1 Δπ=0.098 | ✅ | |\n| 14.9% | intro.tex:13 | exp-038 | ✅ | |\n| 31% at τ(0)=0.01 | intro.tex:13 | exp-038 | ✅ | |\n| τ̂=−0.059 | intro.tex:13 | policy_reversal table τ(0)=0.03 extreme | ✅ | appendix.tex:1501 |\n| 5.9× (K=4 CF) | intro.tex:14 | exp-011 | ✅ | |\n| 2.9× (F-L) | intro.tex:14 | 0.168/0.058=2.897 | ✅ | |\n| 0.059→0.008 | intro.tex:20 | Table 1 | ✅ | |\n| R²≥0.97 | intro.tex:17,34 | exp-002 | ✅ | |\n| AUC=1.0 | intro.tex:18,35 | exp-028 | ✅ | |\n| 7.5% subgroup estimates | intro.tex:28 (Fig caption) | 具体配置数据 | ⚠️ | 非 registry 顶层指标，需从原始CSV验证 |\n\n### Appendix 数字（代表性抽查）\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| K=8 coverage≥95.6% | appendix.tex:381 | exp-030/exp-039 K8 cov=0.956 | ✅ | |\n| R²=0.975 (11 real CMs) | appendix.tex:979 | exp-024 R²=0.975 | ✅ | |\n| R²=0.991 (asymmetric) | appendix.tex:437 | exp-014 R²=0.992 | ⚠️ | 差0.001 |\n| 4× bias reduction (asym) | appendix.tex:439 | exp-014 bias_reduction=4.2× | ⚠️ | 论文4×, registry 4.2× |\n| 93.8% plugin coverage | appendix.tex:1101 | exp-036 0.9375 | ✅ | |\n| 95.0% bootstrap coverage | appendix.tex:1107 | exp-036 boot_cov=0.950 | ✅ | |\n| 89% R-learner reduction | appendix.tex:835 | exp-017 | ✅ | 1-0.013/0.121=89.3% |\n| 13.3% stance sign rev (Global) | appendix_stance.tex:10 | 4/30=0.133 | ✅ | 内部算术 |\n| 3.3% stance sign rev (EC-HTE) | appendix_stance.tex:10 | 1/30=0.033 | ✅ | |\n| ≥94.5% confounded coverage | appendix.tex:1386 | exp-032 all HB cov≥0.945 | ✅ | |\n\n### Limitations.tex 数字\n\n| 数字 | 位置(文件:行) | Registry Exp ID | 匹配? | 备注 |\n|------|--------------|-----------------|-------|------|\n| K=8 coverage≥95.6% | limitations.tex:5 | exp-030 cov=0.956 | ✅ | |\n| AUC=0.86 synthetic | limitations.tex:6 | ROC figure, exp-005 | ⚠️ | 同问题 W1 |\n| AUC=0.63 real LLM | limitations.tex:6 | exp-028 AUC=0.626 | ✅ | |\n| ≥93.5% outcome-dep | limitations.tex:9 | exp-029 全γ范围≥93.5% | ✅ | |\n| ≥89.7% treatment-dep | limitations.tex:9 | exp-040 γ=0.05 cov=0.897 | ✅ | |\n\n---\n\n## B. 跨位置一致性\n\n| 数字 | 出现位置 | 值是否一致 | 备注 |\n|------|---------|-----------|------|\n| R²≥0.97 | abstract:5, intro:17, intro:34, theory:93, experiments:17 | ✅ 一致 | 所有位置均为 ≥0.97 |\n| 14.9% sign reversal | abstract:5, intro:13, experiments:19, Fig1 caption | ✅ 一致 | |\n| 11 empirical CMs | abstract:5, intro:17, experiments:11, conclusion:4 | ✅ 一致 | |\n| AUC 1.0/0.86/0.63 | abstract:6, intro:18,35, method:53, experiments:72, limitations:6 | ✅ 一致 | 各位置引用一致（但registry值存疑，见W1） |\n| 7.4× bias reduction | abstract:7, experiments:27 | ✅ 一致 | intro:20 用 0.059→0.008 表述 |\n| 0.059 / 0.008 | intro:20, experiments:25,27, Table 1 | ✅ 一致 | |\n| 5.9× CF amplification | intro:14, experiments:33 | ✅ 一致 | |\n| 260/520 (50%) | theory:120, experiments:18 | ✅ 一致 | |\n| 2.86× / 2.41× | theory:120, experiments:18 | ✅ 一致 | |\n| 93.8% CF coverage | experiments:65, appendix:1101 | ✅ 一致 | |\n| 89% R-learner | experiments:34, appendix:488,835 | ✅ 一致 | |\n| 0.179→0.007 (PPCI) | method:60, appendix:488,518 | ✅ 一致 | |\n| γ_T=0.10 → 75% | theory:98 | ✅ | 仅出现一次（正文），appendix table确认 |\n| F-L 0.122 / 0.168 | theory:54, experiments:26, Table 1 | ✅ 一致 | |\n| F-L 2.1× / 2.9× | theory:54, intro:14(仅2.9×) | ✅ 一致 | |\n| RMSE change ≤4% vs <5% | method:12 vs method:21 | ❌ 不一致 | 见问题 W2 |\n\n---\n\n## C. 四舍五入一致性\n\n| 类型 | 小数位数 | 示例 | 一致? |\n|------|---------|------|-------|\n| |Bias| | 3位 | 0.058, 0.059, 0.008, 0.012 | ✅ |\n| RMSE | 3位 | 0.090, 0.099, 0.089, 0.120 | ✅ |\n| Coverage | 2位 | 0.82, 0.87, 0.94, 0.96 | ✅ |\n| R² | 2-3位 | 0.97, 0.994, 0.976 | ✅ 可接受（≥0.97用2位，具体值用3位） |\n| AUC | 2位 | 0.86, 0.63, 1.0 | ✅ |\n| 百分比 | 1位或整数 | 14.9%, 31%, 93.8%, 89% | ✅ |\n| 倍数 | 1-2位 | 7.4×, 4.7×, 2.86×, 2.41× | ⚠️ 不完全一致 |\n\n倍数的小数位数不统一：7.4×/4.7×/4.9×/5.9× 用1位，2.86×/2.41× 用2位。但 2.86 和 2.41 是精确的 max 值（registry 直接存储），而 7.4/4.7/4.9 是从 table 值推导的四舍五入。逻辑上合理但格式不完全统一。**建议统一为1位或注明 max 值保留2位。**\n\n---\n\n## 问题汇总\n\n### [CRITICAL] C1: method.tex:61 DGP 标签错误\n\n**位置**: method.tex:61\n**内容**: \"under outcome-side error alone (DGP~C)\"\n**问题**: DGP C 在 appendix PPCI table 中定义为 \"both errors\"（covariate + outcome），而 \"outcome-side error alone\" 对应 DGP B。DGP 标签写反。\n\n**修复**: 将 \"(DGP~C)\" 改为 \"(DGP~B)\"。\n\n### [CRITICAL] C2: method.tex:61 PPCI |bias| 值不匹配\n\n**位置**: method.tex:61\n**内容**: \"PPCI achieves $|\\text{bias}| = 0.003$--$0.004$\"\n**问题**: 无论对应哪个 DGP，PPCI table 中都没有 0.003–0.004 这个范围：\n- DGP B (outcome only) PPCI: |bias| z=0=0.015, z=1=0.020\n- DGP C (both) PPCI: |bias| z=0=0.017, z=1=0.007\n- DGP D (no error) PPCI: z=0=0.007, z=1=0.003\n\n0.003–0.004 不匹配任何 DGP 的 PPCI 结果。最接近的是 DGP D z=1=0.003，但 DGP D 是 \"no error\" 场景，语境不对。\n\n**修复**: 需要确认正确的 DGP 标签和对应的 bias 值。如果指 DGP B，bias 应为 0.015–0.020。\n\n### [CRITICAL] C3: method.tex:61 \"27% RMSE advantage\" 无法复现\n\n**位置**: method.tex:61\n**内容**: \"under covariate-side error alone (DGP~A), EC-HTE provides a 27\\% RMSE advantage over PPCI\"\n**问题**: 从 PPCI table DGP A 计算：\n- EC-HTE avg RMSE = (0.097+0.108)/2 = 0.1025\n- PPCI avg RMSE = (0.162+0.168)/2 = 0.165\n- Advantage = 1 - 0.1025/0.165 = **37.9%**，非 27%\n\n尝试了多种聚合方式（单z-level, 几何均值等），均无法得到27%。\n\n**修复**: 需要确认计算方式。如果是从 table 直接推导，应改为约38%，或注明计算口径。\n\n### [WARNING] W1: AUC=0.86 与 registry 不完全匹配\n\n**位置**: abstract:6, intro:18,35, method:53, experiments:72, limitations:6\n**Registry**: exp-005 subgroup AUC=0.833\n**Paper**: 0.86\n\n**分析**: ROC figure caption 标注 \"Δπ-only condition (AUC = 0.86)\"。exp-005 registry 中 \"Subgroup correlation: 0.86\" 与 \"Subgroup AUC: 0.833\" 是两个不同指标。论文中统一称为 \"AUC=0.86\"，但 registry 的实际 AUC 是 0.833。可能是不同评分规则（Proposition 2 score vs Δπ-only score）给出的不同 AUC 值。\n\n**建议**: 确认论文中的 0.86 对应 ROC 曲线中哪条具体曲线的 AUC，确保描述准确。\n\n### [WARNING] W2: method.tex 内部 hyperprior sensitivity 不一致\n\n**位置**: method.tex:12 说 \"RMSE change ≤4%\"，method.tex:21 说 \"<5% RMSE variation\"\n**Registry**: exp-022 报告 K2 <1%, K4 ≈4-5%\n**Appendix**: appendix.tex:278 说 \"<1% RMSE variation for K=2 and ~4-5% for K=4\"\n\n**问题**: K=4 的 RMSE 变化为 4-5%，超过 method.tex:12 的 \"≤4%\" 声明，但符合 method.tex:21 的 \"<5%\"。同一篇论文中两处描述不一致。\n\n**修复**: 将 method.tex:12 的 \"≤4%\" 改为 \"≤5%\" 或 \"<5%\"，与 method.tex:21 和 appendix 保持一致。\n\n### [WARNING] W3: theory.tex R² 与 registry 差 0.001\n\n**位置**: theory.tex:67 说 R²=0.991（asymmetric），appendix.tex:437 同\n**Registry**: exp-014 R²=0.992\n\n**分析**: 差 0.001，可能是四舍五入差异（0.9915 四舍五入到 0.991 或 0.992）。影响极小。\n\n### [WARNING] W4: appendix asymmetric bias reduction 4× vs registry 4.2×\n\n**位置**: appendix.tex:439 \"4× improvement\"\n**Registry**: exp-014 bias_reduction_vs_global=4.2×\n**Table**: 0.025/0.006=4.17\n\n**分析**: 论文约为 4×（0.025→0.006），精确计算为 4.17×。Registry 存 4.2×。论文用 4× 是粗略近似，差异不大但略不精确。\n\n### [WARNING] W5: Figure 1 caption \"7.5% of subgroup estimates\"\n\n**位置**: intro.tex:28\n**问题**: 7.5% 是 subgroup-estimate level 的 sign reversal rate（vs 14.9% 是 configuration level）。该数字未作为 registry 顶层指标存储，需从原始实验 CSV 验证。\n\n**建议**: 确认 7.5% 的具体计算口径（哪些 subgroup × z-level estimates 中有 7.5% 出现符号翻转）。\n\n---\n\n## 其他检查\n\n### 8 LLMs 计数验证\n- 论文声称 \"8 LLMs\" (experiments.tex:11)\n- appendix realcm_bias (appendix.tex:951) 列出 8 个模型: GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B\n- 另有 GPT-5.4（exp-008 multi-LLM）和 Llama-3.1-8B（appendix open-source）未纳入 \"8 LLMs\" 主体分析\n- ✅ 计数正确\n\n### 16 model–dataset–K combinations 验证\n- appendix screening table (appendix.tex:996-1016): 正好 16 行\n- 4 open-source × TweetEval × K=2 + 4 open-source × TweetEval × K=4 + 5 proprietary × TweetEval × K=4 + 3 proprietary × CivilComments × K=4 = 4+4+5+3 = 16\n- ✅ 正确\n\n### Policy reversal table 内部一致性\n- τ(0)=0.03, extreme: τ̂=-0.059 (appendix.tex:1501)\n- intro.tex:13,28: \"true τ=+0.03, estimated τ̂=-0.059\"\n- ✅ 一致\n\n---\n\n## 结论\n\n**共检查 ~80 个关键数字。**\n\n- **3 个 CRITICAL 问题** (method.tex:61): DGP 标签错误(C→B)、PPCI |bias| 值不匹配(0.003-0.004 无出处)、27% RMSE advantage 无法复现(实际≈38%)。三个问题出现在同一句话中，需要整体修改。\n- **5 个 WARNING** (W1-W5): AUC 0.86 vs registry 0.833 需澄清、hyperprior sensitivity ≤4% vs <5% 内部不一致、两处 ≤0.001 的四舍五入差异、一处未验证的 Figure 数字。\n- **其余所有数字均与 registry 精确匹配或在合理四舍五入范围内。**\n\n**优先修复**: method.tex:61 的三个 CRITICAL 问题（同一句话），以及 method.tex:12 的 ≤4%→<5%。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 113_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01B79cLEGZ1y1mikKn7QeWaN`</summary>

```json
{
  "name": "number_audit_report",
  "type": "report",
  "description": "论文数字追溯性与跨位置一致性核查报告 (2026-05-24)，覆盖~80个关键数字，发现3个CRITICAL和5个WARNING",
  "project": "ec_hte_llm_annotation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/_project/report/number_audit_report.md",
  "tags": [
    "audit",
    "submission",
    "numbers",
    "traceability"
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
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "253866ad-82ef-4573-aa2d-41567ea9f8ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WP8XzhjhxG6Tu5XZAquQ36",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8507,
      "cache_read_input_tokens": 115464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8507
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

_source line 114 · 2026-05-24T04:45:39.397Z_

<details><summary>↩ Tool result · `toolu_01B79cLEGZ1y1mikKn7QeWaN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_33dec4\", \"name\": \"number_audit_report\", \"type\": \"report\", \"description\": \"论文数字追溯性与跨位置一致性核查报告 (2026-05-24)，覆盖~80个关键数字，发现3个CRITICAL和5个WARNING\", \"path\": \"projects/ec_hte_llm_annotation/artifacts/_project/report/number_audit_report_33dec4.md\", \"url\": null, \"project\": \"ec_hte_llm_annotation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T04:45:39.144945+00:00\", \"tags\": [\"audit\", \"submission\", \"numbers\", \"traceability\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "cecbd5a2-c26f-4ddd-b54e-06825fc8e528",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260524_33dec4\\\", \\\"name\\\": \\\"number_audit_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"论文数字追溯性与跨位置一致性核查报告 (2026-05-24)，覆盖~80个关键数字，发现3个CRITICAL和5个WARNING\\\", \\\"path\\\": \\\"projects/ec_hte_llm_annotation/artifacts/_project/report/number_audit_report_33dec4.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"ec_hte_llm_annotation\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-24T04:45:39.144945+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"submission\\\", \\\"numbers\\\", \\\"traceability\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_33dec4\", \"name\": \"number_audit_report\", \"type\": \"report\", \"description\": \"论文数字追溯性与跨位置一致性核查报告 (2026-05-24)，覆盖~80个关键数字，发现3个CRITICAL和5个WARNING\", \"path\": \"projects/ec_hte_llm_annotation/artifacts/_project/report/number_audit_report_33dec4.md\", \"url\": null, \"project\": \"ec_hte_llm_annotation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T04:45:39.144945+00:00\", \"tags\": [\"audit\", \"submission\", \"numbers\", \"traceability\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 115_

核查完成。报告已写入 `artifacts/_project/report/number_audit_report.md`。

**摘要：~80 个关键数字中发现 3 CRITICAL + 5 WARNING。**

### 必须修复（CRITICAL，全在 method.tex:61 同一句话）

1. **DGP 标签错误**：写了 "outcome-side error alone (DGP C)"，但 DGP C 是 "both errors"，应改为 DGP B
2. **PPCI |bias| 值无出处**：声称 0.003–0.004，但 PPCI table 中 DGP B 的 PPCI bias 是 0.015/0.020，不匹配
3. **27% RMSE advantage 无法复现**：从 PPCI table DGP A 计算 EC-HTE vs PPCI 的 RMSE 优势约 38%，非 27%

### 建议修复（WARNING）

- **W2**: method.tex:12 "≤4%" 与 method.tex:21 "<5%" 内部不一致（K4 实际 4-5%），统一为 "<5%"
- **W1**: AUC=0.86 在 registry 中对应的实际值是 0.833（可能是不同评分规则），需确认
- W3/W4: 两处 ≤0.001 的四舍五入差异（影响极小）
- W5: Figure 1 "7.5% subgroup estimates" 未在 registry 中独立验证

### 通过

其余全部数字（R²≥0.97, 14.9%, 7.4×, 260/520, 2.86×/2.41×, 93.8%, 89%, 5.9×, 4.7×, 4.9×, γ_T=0.10→75%, 11 CMs, Table 1 全部 18 个单元格等）均与 registry 精确匹配或在合理四舍五入范围内。跨文件一致性良好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "uuid": "d8c72e2e-8774-4eaf-8e4d-b2ab822a4431",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VGvwkvG4ZqU2wveg5XBkYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 123971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 573
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

_source line 116_

核查完成。报告已写入 `artifacts/_project/report/number_audit_report.md`。

**摘要：~80 个关键数字中发现 3 CRITICAL + 5 WARNING。**

### 必须修复（CRITICAL，全在 method.tex:61 同一句话）

1. **DGP 标签错误**：写了 "outcome-side error alone (DGP C)"，但 DGP C 是 "both errors"，应改为 DGP B
2. **PPCI |bias| 值无出处**：声称 0.003–0.004，但 PPCI table 中 DGP B 的 PPCI bias 是 0.015/0.020，不匹配
3. **27% RMSE advantage 无法复现**：从 PPCI table DGP A 计算 EC-HTE vs PPCI 的 RMSE 优势约 38%，非 27%

### 建议修复（WARNING）

- **W2**: method.tex:12 "≤4%" 与 method.tex:21 "<5%" 内部不一致（K4 实际 4-5%），统一为 "<5%"
- **W1**: AUC=0.86 在 registry 中对应的实际值是 0.833（可能是不同评分规则），需确认
- W3/W4: 两处 ≤0.001 的四舍五入差异（影响极小）
- W5: Figure 1 "7.5% subgroup estimates" 未在 registry 中独立验证

### 通过

其余全部数字（R²≥0.97, 14.9%, 7.4×, 260/520, 2.86×/2.41×, 93.8%, 89%, 5.9×, 4.7×, 4.9×, γ_T=0.10→75%, 11 CMs, Table 1 全部 18 个单元格等）均与 registry 精确匹配或在合理四舍五入范围内。跨文件一致性良好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1026622,
  "duration_api_ms": 1024762,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "c1f80a8b-6c5e-4a54-90d1-41867c4cf47e",
  "total_cost_usd": 2.8600155000000003,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 112703,
    "cache_read_input_tokens": 542257,
    "output_tokens": 32603,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 112703,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 566,
        "cache_read_input_tokens": 123971,
        "cache_creation_input_tokens": 573,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 573
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1798,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001888,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 35,
      "outputTokens": 49400,
      "cacheReadInputTokens": 1159280,
      "cacheCreationInputTokens": 166930,
      "webSearchRequests": 0,
      "costUSD": 2.8581275,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e772ffa8-950d-47ef-ae8a-3baf48358ed3"
}
```

</details>

---
