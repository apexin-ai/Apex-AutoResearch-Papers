# audit body text — Part 1 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

[Transcript overview](../audit-body-text.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/36/36525ae706166678cc35.json)

## Before a recorded user message

## Before a recorded user message

49 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
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
    "mcp__agent-ml-research__compare_wandb_runs",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__fetch_wandb_run_history",
    "mcp__agent-ml-research__get_best_wandb_run",
    "mcp__agent-ml-research__list_wandb_runs",
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
  "uuid": "15a60b94-bd60-4d3f-8cc7-6bb5c1418ebe",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/memory/"
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
    "resetsAt": 1779757800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bbf096bd-4ae2-4061-bcb5-c9b37a8696ce",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to audit every number in the main body of their paper, verifying against registry data, figure scripts, and WandB. Let me start by reading all the paper sections and the registry data in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "a121ca7c-057e-4a9d-9f54-ad780a46cd8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

开始审计论文主体文本中的所有数字。先并行读取所有 tex 文件、registry 数据和图表脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "6b2fb81c-aa37-4d98-8304-2aab6ef74f5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_016CW9gt7yrm9onKNE71nx9B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "e677775a-5241-4498-be7c-204632737d9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 7 · 2026-05-25T20:12:10.343Z_

<details><summary>↩ Tool result · `toolu_016CW9gt7yrm9onKNE71nx9B`</summary>

```text
1	\begin{abstract}
2	As multi-turn conversations grow longer, large language models progressively lose attention to the system-prompt goals that define their task, even when the underlying goal representations remain intact. Existing remedies operate at inference time, leaving a natural but untested alternative: training auxiliary attention losses alongside next-token prediction to directly optimize goal attention. This strategy assumes that attention patterns learned under teacher forcing will transfer to autoregressive generation, an assumption that classical exposure bias research has challenged for sequence models but that has never been examined for auxiliary attention objectives in multi-turn transformers.
3	We show this assumption fails. On a controlled five-way testbed spanning two architectures (Qwen-2.5-7B, Llama-3.1-8B), goal attention optimized to target under teacher forcing collapses by an order of magnitude under autoregressive generation. A causal exclusion chain traces the failure to exposure bias, ruling out gradient conflict, gating mechanism, and parameter capacity as primary causes. Inference-time attention steering confirms that the collapse reflects attention misallocation rather than representation loss. Scheduled sampling, applied here for the first time to auxiliary attention objectives in multi-turn transformers, compresses the training--inference gap to near parity on Qwen and substantially on Llama, with no perplexity cost\footnote{Code and data are available at \url{https://anonymous.4open.science/r/turn_residual_gating-8703/}.}.
4	\end{abstract}
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "19937a3d-6eaa-4dcb-b20c-d83dcce4172e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nAs multi-turn conversations grow longer, large language models progressively lose attention to the system-prompt goals that define their task, even when the underlying goal representations remain intact. Existing remedies operate at inference time, leaving a natural but untested alternative: training auxiliary attention losses alongside next-token prediction to directly optimize goal attention. This strategy assumes that attention patterns learned under teacher forcing will transfer to autoregressive generation, an assumption that classical exposure bias research has challenged for sequence models but that has never been examined for auxiliary attention objectives in multi-turn transformers.\nWe show this assumption fails. On a controlled five-way testbed spanning two architectures (Qwen-2.5-7B, Llama-3.1-8B), goal attention optimized to target under teacher forcing collapses by an order of magnitude under autoregressive generation. A causal exclusion chain traces the failure to exposure bias, ruling out gradient conflict, gating mechanism, and parameter capacity as primary causes. Inference-time attention steering confirms that the collapse reflects attention misallocation rather than representation loss. Scheduled sampling, applied here for the first time to auxiliary attention objectives in multi-turn transformers, compresses the training--inference gap to near parity on Qwen and substantially on Llama, with no perplexity cost\\footnote{Code and data are available at \\url{https://anonymous.4open.science/r/turn_residual_gating-8703/}.}.\n\\end{abstract}\n",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_014SbvFRqHsLNtE1bSBdgUmL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "a0f47003-32ef-417f-8d12-6240f60948fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 9 · 2026-05-25T20:12:10.710Z_

<details><summary>↩ Tool result · `toolu_014SbvFRqHsLNtE1bSBdgUmL`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\,=\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.
4	
5	Existing remedies address this decay at inference time. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.
6	
7	We test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a causal exclusion chain (\S\ref{sec:comparison-design}), where each adjacent pair isolates one candidate failure mechanism. The result is unambiguous: every variant converges to target GAR under teacher forcing, yet goal attention collapses by an order of magnitude once the model generates its own context (Figure~\ref{fig:headline}). The exclusion chain traces this collapse to exposure bias, the training--inference distribution mismatch, ruling out gradient direction conflict (PCGrad removes conflict yet \emph{worsens} AR GAR), gating mechanism (Uniform Gate matches ThreadGate), and parameter capacity (LoRA-only shows the same pattern). Inference-time $\beta$-steering confirms that the collapse reflects attention misallocation rather than representation degradation; scheduled sampling bridges the gap by exposing the model to its own generations during training.
8	
9	\begin{figure*}[!ht]
10	  \centering
11	  \includegraphics[width=\textwidth]{fig1_headline.pdf}
12	  \caption{Exposure bias collapses auxiliary attention losses. \textbf{(a)}~Goal attention decays 85--90\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \textbf{(b)}~Under TF evaluation all variants reach GAR$\approx$0.50, but AR generation collapses GAR by 8--17$\times$ (log scale). \textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.8$\times$ to 1.3$\times$ (Qwen) and ${\sim}$27$\times$ to 2.9$\times$ (Llama).}
13	  \label{fig:headline}
14	\end{figure*}
15	
16	Our contributions are:
17	\begin{enumerate}\raggedright
18	    \item \textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).
19	    \item \textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \emph{modus tollens} argument ruling out gradient direction conflict ($p$\,=\,0.002, effect reverses).
20	    \item \textbf{Attention misallocation diagnosis.} Inference-time $\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.
21	    \item \textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\sim}$1.3$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama with no perplexity degradation, robust across three seeds.
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "6874485c-d274-4efd-9322-8aa80dd41705",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nMulti-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \\citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\\,=\\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.\n\nExisting remedies address this decay at inference time. Split-softmax \\citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \\citep{xiao2024streaming} retains anchor tokens; Gated Attention \\citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \\citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.\n\nWe test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a causal exclusion chain (\\S\\ref{sec:comparison-design}), where each adjacent pair isolates one candidate failure mechanism. The result is unambiguous: every variant converges to target GAR under teacher forcing, yet goal attention collapses by an order of magnitude once the model generates its own context (Figure~\\ref{fig:headline}). The exclusion chain traces this collapse to exposure bias, the training--inference distribution mismatch, ruling out gradient direction conflict (PCGrad removes conflict yet \\emph{worsens} AR GAR), gating mechanism (Uniform Gate matches ThreadGate), and parameter capacity (LoRA-only shows the same pattern). Inference-time $\\beta$-steering confirms that the collapse reflects attention misallocation rather than representation degradation; scheduled sampling bridges the gap by exposing the model to its own generations during training.\n\n\\begin{figure*}[!ht]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig1_headline.pdf}\n  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.8$\\times$ to 1.3$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}\n  \\label{fig:headline}\n\\end{figure*}\n\nOur contributions are:\n\\begin{enumerate}\\raggedright\n    \\item \\textbf{Exposure bias characterization.} To our knowledge, the first empirical demonstration that exposure bias collapses auxiliary attention objectives in multi-turn transformers, with an order-of-magnitude TF--AR gap reproduced across two architectures (Qwen-2.5-7B, Llama-3.1-8B) and model scales (1.5B--8B).\n    \\item \\textbf{Causal exclusion testbed.} A five-way diagnostic design, informed by seven loss-formulation iterations, that isolates the failure mechanism via causal exclusion, including a PCGrad \\emph{modus tollens} argument ruling out gradient direction conflict ($p$\\,=\\,0.002, effect reverses).\n    \\item \\textbf{Attention misallocation diagnosis.} Inference-time $\\beta$-steering recovers goal attention with modest perplexity cost, evidence that the collapse is an attention routing failure, not a representational one.\n    \\item \\textbf{Scheduled sampling as remedy.} The first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, compressing the TF--AR gap to ${\\sim}$1.3$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama with no perplexity degradation, robust across three seeds.\n\\end{enumerate}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_0199fywmGk71kPY5GWKhpBG8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4ae15b85-2413-431c-94d5-d185adda0fdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 11 · 2026-05-25T20:12:11.060Z_

<details><summary>↩ Tool result · `toolu_0199fywmGk71kPY5GWKhpBG8`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation; attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}). Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\S\ref{sec:analysis}). Throughout this work, GAR serves primarily as a \emph{diagnostic probe}: it measures whether auxiliary attention training transfers to autoregressive generation, rather than being an end-to-end optimization objective whose increase directly improves downstream task performance (the correlation with instruction retention is weak; $r$\,=\,0.200, $p$\,=\,0.007; \S\ref{sec:discussion}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	\begin{figure}[t]
22	  \centering
23	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
24	  \caption{Per-turn GAR-ours under AR generation ($N$\,=\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\% decay; $\Delta$\,=\,3.3\,pp between ThreadGate and LoRA-only); Base decays 87.5\%. Gating adds zero incremental effect.}
25	  \label{fig:attention-heatmap}
26	\end{figure}
27	
28	Different transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:
29	\begin{equation}
30	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
31	\end{equation}
32	where $f_l$ denotes the sublayer computation (self-attention or feed-forward network, FFN). Since residual networks can be viewed as ensembles of shallow paths \citep{veit2016residual}, per-layer gating selectively modulates individual paths within this ensemble. This resembles ReZero \citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training, but ThreadGate differs in three ways: (i)~gates are \emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\sigma(1.5) \approx 0.82$) rather than zero, preserving the pretrained model's computation.
33	
34	Concretely, each gate $g_l$ is produced by a two-layer MLP that takes both content and turn features as input:
35	\begin{align}\label{eq:gate}
36	  g_l = \sigma\bigl(W_2\,\text{ReLU}(&W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] \notag\\
37	  &+ b_1) + b_2\bigr),
38	\end{align}
39	where $\text{proj}(\cdot)$ reduces the hidden dimension to 16, and $\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding encoding turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\!=\!28$), this adds ${\sim}$57K parameters ($<$0.001\% of 7B). To isolate the contribution of turn conditioning, the \textbf{Uniform Gate} ablation replaces $\text{emb}(\cdot)$ with a learnable constant, removing turn awareness while retaining content-conditioned gating. To preserve pretrained behavior, gate biases are initialized to 1.5 (${\sim}$82\% pass-through) rather than zero as in ReZero, and gate parameters receive a $10\times$ learning rate multiplier to accelerate adaptation.
40	
41	\subsection{Training Objective}\label{sec:loss}
42	
43	Next-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:
44	\begin{equation}
45	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
46	\end{equation}
47	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. For $\mathcal{L}_\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \emph{bidirectional} pressure, penalizing both under- and over-attention and preventing identity collapse (Appendix~\ref{sec:appendix-loss}):
48	\begin{equation}
49	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR\text{-}ours}, \tau),
50	\end{equation}
51	where $\tau = 0.5$ targets allocating half of the last token's attention to goal tokens. Without diversity pressure, all gates converge near 1.0; the gate diversity loss prevents this:
52	\begin{equation}
53	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
54	\end{equation}
55	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min} = 0.05$ is a minimum standard deviation threshold ($\lambda_\text{GAR} = \lambda_\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.
56	
57	\subsection{Controlled Comparison Design}\label{sec:comparison-design}
58	
59	We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate (TG) vs.\ Uniform Gate (UG)} (turn conditioning), \textbf{TG vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
60	
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "ae3683cb-1b9d-469e-bdb4-2d6019c7bf9d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Preliminaries}\\label{sec:background}\n\n\\paragraph{Goal Accessibility Ratio.}\nStandard metrics such as perplexity and attention entropy capture generation quality but not \\emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \\emph{goal tokens} $\\mathcal{G}$. \\citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\\tau$ as\n\\begin{equation}\\label{eq:gar}\n  \\text{GAR}(\\tau) = \\frac{1}{L \\cdot H \\cdot |\\mathcal{R}_\\tau|} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{i \\in \\mathcal{R}_\\tau} \\sum_{j \\in \\mathcal{G}} A_{i,j}^{(\\ell,h)},\n\\end{equation}\nwhere $\\mathcal{R}_\\tau$ is the set of response tokens at turn $\\tau$ and $A_{i,j}^{(\\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\\ell$, head $h$.\n\n\\paragraph{Two GAR variants.}\n\\textbf{GAR-Dongre} is the original definition (Eq.~\\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation; attention at this position most directly reflects the model's awareness of task specifications. \\textbf{GAR-ours} restricts the measurement accordingly:\n\\begin{equation}\\label{eq:gar-ours}\n  \\text{GAR\\text{-}ours}(\\tau) = \\frac{1}{L \\cdot H} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{j \\in \\mathcal{G}} A_{t_\\tau,\\, j}^{(\\ell,h)},\n\\end{equation}\nwhere $t_\\tau$ is the last token index at turn $\\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\\mathcal{L}_\\text{GAR}$ (\\S\\ref{sec:loss}). Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\\S\\ref{sec:analysis}). Throughout this work, GAR serves primarily as a \\emph{diagnostic probe}: it measures whether auxiliary attention training transfers to autoregressive generation, rather than being an end-to-end optimization objective whose increase directly improves downstream task performance (the correlation with instruction retention is weak; $r$\\,=\\,0.200, $p$\\,=\\,0.007; \\S\\ref{sec:discussion}).\n\n\\subsection{ThreadGate Architecture}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig4_attention_heatmap.pdf}\n  \\caption{Per-turn GAR-ours under AR generation ($N$\\,=\\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\\% decay; $\\Delta$\\,=\\,3.3\\,pp between ThreadGate and LoRA-only); Base decays 87.5\\%. Gating adds zero incremental effect.}\n  \\label{fig:attention-heatmap}\n\\end{figure}\n\nDifferent transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \\citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \\emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:\n\\begin{equation}\n  x_{l+1} = x_l + g_l \\cdot f_l(x_l),\n\\end{equation}\nwhere $f_l$ denotes the sublayer computation (self-attention or feed-forward network, FFN). Since residual networks can be viewed as ensembles of shallow paths \\citep{veit2016residual}, per-layer gating selectively modulates individual paths within this ensemble. This resembles ReZero \\citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training, but ThreadGate differs in three ways: (i)~gates are \\emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \\emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\\sigma(1.5) \\approx 0.82$) rather than zero, preserving the pretrained model's computation.\n\nConcretely, each gate $g_l$ is produced by a two-layer MLP that takes both content and turn features as input:\n\\begin{align}\\label{eq:gate}\n  g_l = \\sigma\\bigl(W_2\\,\\text{ReLU}(&W_1\\,[\\text{proj}(x_l);\\;\\text{emb}(t_d, t_i)] \\notag\\\\\n  &+ b_1) + b_2\\bigr),\n\\end{align}\nwhere $\\text{proj}(\\cdot)$ reduces the hidden dimension to 16, and $\\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding encoding turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\\!=\\!28$), this adds ${\\sim}$57K parameters ($<$0.001\\% of 7B). To isolate the contribution of turn conditioning, the \\textbf{Uniform Gate} ablation replaces $\\text{emb}(\\cdot)$ with a learnable constant, removing turn awareness while retaining content-conditioned gating. To preserve pretrained behavior, gate biases are initialized to 1.5 (${\\sim}$82\\% pass-through) rather than zero as in ReZero, and gate parameters receive a $10\\times$ learning rate multiplier to accelerate adaptation.\n\n\\subsection{Training Objective}\\label{sec:loss}\n\nNext-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_\\text{NTP} + \\lambda_\\text{GAR}\\,\\mathcal{L}_\\text{GAR} + \\lambda_\\text{div}\\,\\mathcal{L}_\\text{div}.\n\\end{equation}\n$\\mathcal{L}_\\text{NTP}$ is the standard next-token prediction loss. For $\\mathcal{L}_\\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \\emph{bidirectional} pressure, penalizing both under- and over-attention and preventing identity collapse (Appendix~\\ref{sec:appendix-loss}):\n\\begin{equation}\n  \\mathcal{L}_\\text{GAR} = \\text{MSE}(\\text{GAR\\text{-}ours}, \\tau),\n\\end{equation}\nwhere $\\tau = 0.5$ targets allocating half of the last token's attention to goal tokens. Without diversity pressure, all gates converge near 1.0; the gate diversity loss prevents this:\n\\begin{equation}\n  \\mathcal{L}_\\text{div} = \\text{ReLU}(\\sigma_\\text{min} - \\text{std}(\\mathbf{g})),\n\\end{equation}\nwhere $\\mathbf{g} = [g_1, \\ldots, g_L]$ and $\\sigma_\\text{min} = 0.05$ is a minimum standard deviation threshold ($\\lambda_\\text{GAR} = \\lambda_\\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.\n\n\\subsection{Controlled Comparison Design}\\label{sec:comparison-design}\n\nWe design a five-way comparison where each adjacent pair isolates one factor: \\textbf{ThreadGate (TG) vs.\\ Uniform Gate (UG)} (turn conditioning), \\textbf{TG vs.\\ LoRA-only} (gating mechanism), \\textbf{ThreadGate vs.\\ +PCGrad} (gradient conflict via gradient surgery \\citep{yu2020pcgrad}), and \\textbf{Fine-tuned vs.\\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\\ref{sec:appendix-hyper}).\n\n",
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01XkBEjGRJrUbqudJfkPhVpf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "00567fc2-b148-4710-8854-cdcd2aef1115",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 13 · 2026-05-25T20:12:11.246Z_

<details><summary>↩ Tool result · `toolu_01XkBEjGRJrUbqudJfkPhVpf`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendices~\ref{sec:appendix-data} and~\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and perplexity (PPL).
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendices~\ref{sec:appendix-stats} and~\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). MMLU 5-shot accuracy remains within 0.8\,pp across all variants (per-category breakdown in Appendix~\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\begin{figure*}[!t]
15	  \centering
16	  \includegraphics[width=\textwidth]{fig5_attention_steering.pdf}
17	  \caption{Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, consistent with attention misallocation as a proximal cause (9\% PPL cost at $\beta$\,=\,3; phase transition at $\beta \in [2, 3]$).}
18	  \label{fig:steering-recovery}
19	\end{figure*}
20	
21	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
22	
23	All training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\beta$ to pre-softmax attention logits for goal-token positions during generation:
24	\begin{equation}
25	  \tilde{A}_{i,j}^{(\ell,h)} = A_{i,j}^{(\ell,h)} + \beta \cdot \mathbf{1}[j \in \mathcal{G}],
26	\end{equation}
27	where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\ref{fig:steering-recovery}; full results in Appendix~\ref{sec:appendix-steering}; per-$\beta$ turn-level trajectories in Appendix~\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does, consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\ref{sec:appendix-examples}). Downstream, steering ($\beta$\,=\,3) raises late-turn instruction compliance by +11.1\,pp, though this effect does not reach conventional significance ($p$\,=\,0.077; content-constrained tasks benefit most, +23.8\,pp; Appendix~\ref{sec:appendix-ir}).
28	
29	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
30	
31	\begin{figure}[t]
32	  \centering
33	  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
34	  \caption{Scheduled sampling compresses the TF-AR gap from 7.8$\times$ to ${\sim}$1.3$\times$, the only variant approaching parity across five training conditions.}
35	  \label{fig:ss-gap}
36	\end{figure}
37	
38	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\pm0.047$, compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ (TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.001$; Figure~\ref{fig:ss-gap}; per-seed details in Appendix~\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\beta$\,=\,5: $0.717\pm0.001$, std 0.047$\to$0.001; Figure~\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
39	
40	
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4bd5e408-484f-435a-b7ea-2fbd9888cafb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\begin{figure*}[!t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, consistent with attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure*}\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}; per-$\\beta$ turn-level trajectories in Appendix~\\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does, consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01CnkrRZ7a3kLRMYGmAY3ySZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "da96d902-961c-4b53-9d02-ade86f8a1eef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 15 · 2026-05-25T20:12:12.276Z_

<details><summary>↩ Tool result · `toolu_01CnkrRZ7a3kLRMYGmAY3ySZ`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	\begin{figure*}[!t]
4	  \centering
5	  \includegraphics[width=\textwidth]{fig3_gate_shift.pdf}
6	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:five-way}) due to smaller sample size.}
7	  \label{fig:gate-shift}
8	\end{figure*}
9	
10	Each subsection kills one alternative hypothesis via causal exclusion: \S\ref{subsec:gate-conditioning}~turn conditioning, \S\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms selectivity; \S\ref{subsec:cross-model} confirms cross-architecture generalization.
11	
12	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
13	
14	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:five-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning; the structure thus arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
15	
16	\subsection{PCGrad Gradient Direction Conflict Exclusion}\label{subsec:pcgrad}
17	
18	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ (full gradient statistics in Appendix~\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
19	
20	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b in Appendix~\ref{sec:appendix-gradient}). By \emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\,=\,+0.005) with 25.7$\times$ NTP magnitude dominance (Table~\ref{tab:gradient-crossmodel}).
21	
22	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
23	
24	The TF-AR GAR gap persists across all variants (Table~\ref{tab:five-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, evidence that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\ref{sec:appendix-eb-scaling}).
25	
26	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
27	
28	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
29	
30	\begin{figure}[t]
31	  \centering
32	  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
33	  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
34	  \label{fig:ss-multiseed}
35	\end{figure}
36	
37	\subsection{Cross-Model Replication}\label{subsec:cross-model}
38	
39	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}; per-turn values in Appendix~\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.
40	
41	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\sim}$1.3$\times$ likely due to fewer training epochs (2 vs.\ 3). The phase transition is architecture-dependent: $\beta$\,=\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\beta$\,=\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\% GAR decay, $\beta$-steering recovery to 0.715; Appendix~\ref{sec:appendix-1.5b}).
42	
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "0c22a1bb-7852-40ec-afc5-4537315a12c0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\\label{sec:analysis}\n\n\\begin{figure*}[!t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:five-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure*}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:five-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning; the structure thus arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:five-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, evidence that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed); exposure bias thus disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717; Appendix~\\ref{sec:appendix-llama-ss}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern (79.8\\% GAR decay, $\\beta$-steering recovery to 0.715; Appendix~\\ref{sec:appendix-1.5b}).\n\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01Rw2QwENc9pRLio9T95bzd2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "2874df77-acfe-496e-ae0e-0695a82369f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 17 · 2026-05-25T20:12:12.308Z_

<details><summary>↩ Tool result · `toolu_01Rw2QwENc9pRLio9T95bzd2`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \citep{he2019exposure}; GAR optimizes a \emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\leq}$1.3$\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\,=\,0.743; Appendix~\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.
4	
5	\looseness=-1 Our exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\S\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\,=\,0.200; Appendix~\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\beta$-steering is likewise a \emph{diagnostic}, distinct from inference-time remedies such as split-softmax \citep{li2024measuring} and Rhea \citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\beta$\,=\,5 the two converge (SS\,=\,0.717 vs.\ TG\,=\,0.727).
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "841f7d47-c99f-4b1c-8487-6d820c7fe430",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\looseness=-1 NTP self-recovers because prediction is the same task at both regimes \\citep{he2019exposure}; GAR optimizes a \\emph{global property} (attention allocation to goal tokens) with no autoregressive counterpart. The collapse is selective: GAR-ours collapses by an order of magnitude while GAR-Dongre shows negligible shift (${\\leq}$1.3$\\times$). Per-head analysis confirms selectivity: heads with higher TF GAR shift most under AR ($r$\\,=\\,0.743; Appendix~\\ref{sec:appendix-kl}). Any auxiliary attention objective targeting distributional properties rather than prediction itself should face the same barrier under teacher forcing.\n\n\\looseness=-1 Our exclusion identifies exposure bias as a primary contributing factor, but cannot fully rule out KV cache drift (\\S\\ref{sec:limitations}). The PCGrad exclusion rules out direction conflict but not magnitude imbalance (7.5--25.7$\\times$ NTP dominance; \\citealp{chen2018gradnorm}). The GAR--compliance correlation is weak ($r$\\,=\\,0.200; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe. Our $\\beta$-steering is likewise a \\emph{diagnostic}, distinct from inference-time remedies such as split-softmax \\citep{li2024measuring} and Rhea \\citep{hong2025rhea}. SS and inference-time fixes are complementary: SS modifies representations without inference cost; inference-time methods cannot recover patterns never learned. At $\\beta$\\,=\\,5 the two converge (SS\\,=\\,0.717 vs.\\ TG\\,=\\,0.727).\n",
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

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_018dCPEvKtupaTYCju32wVFB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "b1a74c74-4782-49b2-a09b-46e150f2f0e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 19 · 2026-05-25T20:12:13.139Z_

<details><summary>↩ Tool result · `toolu_018dCPEvKtupaTYCju32wVFB`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "42be46e6-75ec-4dce-900a-20d4f61cef47",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, consistent with attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds; to our knowledge, the first such transfer to auxiliary attention objectives in multi-turn transformers.\n",
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

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01DvNhq3ZcbLkZkk5NyBxrZY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "daa3a06d-f5dd-4d94-acdd-3fdf1a515837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 21 · 2026-05-25T20:12:13.632Z_

<details><summary>↩ Tool result · `toolu_01DvNhq3ZcbLkZkk5NyBxrZY`</summary>

```text
1	\section*{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other architectures and domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. Our causal exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "08c6525d-ab72-4160-94ee-f4d13b456ba5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex",
      "content": "\\section*{Limitations}\\label{sec:limitations}\n\nOur findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other architectures and domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \\S\\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \\citep{hendrycks2021measuring,lin2022truthfulqa}. We test only one auxiliary loss family (GAR with MSE target $\\tau$\\,=\\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. Our causal exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.",
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

_source line 22_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L6eXriJAuaYZvcZQV9S1Bf`</summary>

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
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "7ec1caff-9ed4-4ef7-8fac-6c82ecd6ff0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 23 · 2026-05-25T20:12:14.561Z_

<details><summary>↩ Tool result · `toolu_01L6eXriJAuaYZvcZQV9S1Bf`</summary>

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
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "5d622452-b5f5-4c00-b0de-bb6525d7f09e",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 30
  }
}
```

</details>

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_01AGxqeWFwmFKf9YenbN4vmP`</summary>

```json
{
  "pattern": "figures/paper/gen_fig*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "59cc1630-c6b7-400b-b328-1728b5dd1794",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KxqsQbdynYQ7f8wg9x8irk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13840,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13840
      },
      "output_tokens": 25,
      "service_tier": "standard",
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

_source line 25 · 2026-05-25T20:12:15.213Z_

<details><summary>↩ Tool result · `toolu_01AGxqeWFwmFKf9YenbN4vmP`</summary>

```text
figures/paper/gen_fig_bootstrap_ci.py
figures/paper/gen_fig1_headline_OLD.py
figures/paper/gen_fig_mmlu_comparison.py
figures/paper/gen_fig_training_dynamics.py
figures/paper/gen_fig1_headline_single.py
figures/paper/gen_fig_gate_distribution.py
figures/paper/gen_fig_gate_profile_heatmap.py
figures/paper/gen_fig_steering_perturn_4panel.py
figures/paper/gen_fig_training_curves_6panel.py
figures/paper/gen_fig_ss_multiseed.py
figures/paper/gen_fig_gradient_conflict_heatmap.py
figures/paper/gen_fig_method_framework.py
figures/paper/gen_fig2.py
figures/paper/gen_fig4.py
figures/paper/gen_fig_ss_gap_compression.py
figures/paper/gen_fig_method_framework_v3.py
figures/paper/gen_fig_perturn_llama_detail.py
figures/paper/gen_fig_eb_scaling.py
figures/paper/gen_fig_ar_gar_perturn.py
figures/paper/gen_fig_gate_profile_crossmodel.py
figures/paper/gen_fig_training_loss_curves.py
figures/paper/gen_fig_steering_standalone.py
figures/paper/gen_fig_gar_robustness_grouped.py
figures/paper/gen_fig_instruction_retention.py
figures/paper/gen_fig_crossmodel.py
figures/paper/gen_fig_kl_ar_gar.py
figures/paper/gen_fig_perturn_qwen_detail.py
figures/paper/gen_fig_ss_training_dynamics.py
figures/paper/gen_fig5.py
figures/paper/gen_fig3_gate_shift.py
figures/paper/gen_fig1_3panel.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "8e322e67-a506-477b-87de-1e7e34fd472b",
  "tool_use_result": {
    "filenames": [
      "figures/paper/gen_fig_bootstrap_ci.py",
      "figures/paper/gen_fig1_headline_OLD.py",
      "figures/paper/gen_fig_mmlu_comparison.py",
      "figures/paper/gen_fig_training_dynamics.py",
      "figures/paper/gen_fig1_headline_single.py",
      "figures/paper/gen_fig_gate_distribution.py",
      "figures/paper/gen_fig_gate_profile_heatmap.py",
      "figures/paper/gen_fig_steering_perturn_4panel.py",
      "figures/paper/gen_fig_training_curves_6panel.py",
      "figures/paper/gen_fig_ss_multiseed.py",
      "figures/paper/gen_fig_gradient_conflict_heatmap.py",
      "figures/paper/gen_fig_method_framework.py",
      "figures/paper/gen_fig2.py",
      "figures/paper/gen_fig4.py",
      "figures/paper/gen_fig_ss_gap_compression.py",
      "figures/paper/gen_fig_method_framework_v3.py",
      "figures/paper/gen_fig_perturn_llama_detail.py",
      "figures/paper/gen_fig_eb_scaling.py",
      "figures/paper/gen_fig_ar_gar_perturn.py",
      "figures/paper/gen_fig_gate_profile_crossmodel.py",
      "figures/paper/gen_fig_training_loss_curves.py",
      "figures/paper/gen_fig_steering_standalone.py",
      "figures/paper/gen_fig_gar_robustness_grouped.py",
      "figures/paper/gen_fig_instruction_retention.py",
      "figures/paper/gen_fig_crossmodel.py",
      "figures/paper/gen_fig_kl_ar_gar.py",
      "figures/paper/gen_fig_perturn_qwen_detail.py",
      "figures/paper/gen_fig_ss_training_dynamics.py",
      "figures/paper/gen_fig5.py",
      "figures/paper/gen_fig3_gate_shift.py",
      "figures/paper/gen_fig1_3panel.py"
    ],
    "durationMs": 44,
    "numFiles": 31,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the registry data and the figure generation scripts to get the source data for verification. Let me fetch the registry and read the key figure scripts in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "c0fbd3b2-507c-4cec-9b5b-19c5cc69880a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 27_

Reading registry and figure scripts for source data verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "71fb8717-6cb4-4631-b3e2-461423437bad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01MQBWXYLTjhaqwXcaoJvZ4S`</summary>

```json
{
  "project": "turn_residual_gating",
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
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "e6eca8b4-4dff-48f0-bc42-fadc7c098590",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 29 · 2026-05-25T20:12:23.935Z_

<details><summary>↩ Tool result · `toolu_01MQBWXYLTjhaqwXcaoJvZ4S`</summary>

```text
Error: result (98,179 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "75bd8bfb-dc80-48c1-9622-9373fd8b2aa2",
  "tool_use_result": {
    "content": "Error: result (98,179 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase1a_multiseed_qwen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:26.051Z\", \"updated_at\": \"2026-05-25T11:20:34.089Z\", \"hypothesis\": \"Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.\", \"spec\": {\"command\": \"python src/train_phase2_v9_pcgrad.py\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"N/A\", \"log_path\": \"runs/d048_pcgrad_s123\"}, \"conclusion\": \"killed\", \"notes\": \"用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。\", \"checkpoint_path\": \"N/A\", \"log_path\": \"runs/d048_pcgrad_s123\", \"completed_at\": \"2026-05-25T11:20:34.089Z\"}, \"p1_ss_lora_only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T08:58:41.419Z\", \"updated_at\": \"2026-05-25T09:42:22.185Z\", \"hypothesis\": \"SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).\", \"spec\": {\"command\": \"bash /root/turn_residual_gating/scripts/d048_ss_lo_s42.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/phase2_train.jsonl\", \"data_count\": 2000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"notes\": \"SS+LoRA-only (gate_type=none, ss_max_ratio=0.3). From-scratch training, not resume. Auto TF+AR eval after training. ~6.5h training + eval.\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T09:42:22.185Z\"}, \"phase2_switching\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T08:58:40.187Z\", \"updated_at\": \"2026-05-25T09:42:21.391Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T09:42:21.391Z\"}, \"phase2_tf_ar_switching\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:36.221Z\", \"updated_at\": \"2026-05-25T06:45:27.338Z\", \"hypothesis\": \"TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\"}, \"phase1a_multiseed_8runs\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:18:08.953Z\", \"updated_at\": \"2026-05-25T06:18:08.953Z\", \"spec\": {\"command\": \"bash -c \\\"bash /root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"5508\", \"log_path\": \"~/runs/turn_residual_gating/phase1a_multiseed_8runs.log\", \"submitted_at\": \"2026-05-25T06:18:08.495Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"phase1b_llama_complement\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:15:34.729Z\", \"updated_at\": \"2026-05-25T06:15:44.322Z\", \"hypothesis\": \"Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict.\"}, \"p1_llama_ss_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T15:53:29.650Z\", \"updated_at\": \"2026-05-24T17:12:44.175Z\", \"hypothesis\": \"Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.\", \"spec\": {\"command\": \"bash scripts/p1_llama_ss_eval.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/eval_50.json\", \"data_count\": 50, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"runs/p1_llama_ss_s42/epoch_1/\", \"log_path\": \"runs/p1_llama_ss_eval.log\", \"pid\": 178624, \"checkpoint_path\": \"results/llama_ss_eval/\"}, \"conclusion\": \"success\", \"metrics\": {\"ss_tf_gar\": 0.477, \"ss_tf_ppl\": 2.82, \"ss_ar_b0_gar\": 0.1662, \"ss_ar_b0_ppl\": 1.37, \"ss_ar_b5_gar\": 0.7905, \"ss_ar_b5_ppl\": 1.81, \"base_ar_gar\": 0.0179, \"base_ar_ppl\": 1.22, \"tf_ar_gap\": 2.87}, \"completed_at\": \"2026-05-24T17:12:44.175Z\"}, \"p1_llama_ss_training\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:37:48.689Z\", \"updated_at\": \"2026-05-24T15:53:21.654Z\", \"hypothesis\": \"SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.\", \"spec\": {\"command\": \"bash scripts/p1_llama_ss_train.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/train_400.json\", \"data_count\": 400, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"runs/llama_ss_s42/\", \"log_path\": \"logs/p1_llama_ss_training.log\", \"pid\": 158507, \"hyperparams\": {\"lr\": \"2e-4\", \"batch_size\": 1, \"grad_accum\": 8, \"epochs\": 3, \"ss_max_ratio\": 0.3, \"lora_rank\": 16}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T15:53:21.654Z\"}, \"mmlu_eval_all\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:45:04.153Z\", \"updated_at\": \"2026-05-24T07:23:08.289Z\", \"hypothesis\": \"ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.\", \"spec\": {\"command\": \"python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5\", \"server\": \"westd-20861\", \"data_path\": \"MMLU benchmark (5-shot)\", \"data_count\": 14042, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"base/lo/ug/tg/pcgrad/ss checkpoints\", \"eval_data\": \"MMLU 5-shot\", \"checkpoint_path\": \"results/mmlu/\", \"log_path\": \"logs/gpu_chain_next.log\"}, \"conclusion\": \"success\", \"metrics\": {\"base_qwen\": 0.7423, \"pcgrad_v9_s42\": 0.7386, \"ss_v8b_s42\": 0.7375, \"lo_s42\": 0.7357, \"tg_v7_s42\": 0.7347, \"ug_s42\": 0.7346}, \"completed_at\": \"2026-05-24T06:53:52.873Z\"}, \"p2_llama_gradient_conflict\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:37:50.492Z\", \"updated_at\": \"2026-05-24T07:20:28.248Z\", \"hypothesis\": \"PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).\", \"spec\": {\"command\": \"bash scripts/p2_llama_gradient_conflict.sh\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/train_400.json\", \"data_count\": 400, \"model_name\": \"meta-llama/Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"results/p2_llama_gradient_conflict/\", \"log_path\": \"logs/p2_llama_gradient_conflict.log\"}, \"conclusion\": \"success\", \"metrics\": {\"cos_sim_mean\": 0.0045, \"cos_sim_std\": 0.07, \"neg_cos_sim_layers_pct\": 53.1, \"mag_ratio_median\": 25.7, \"conclusion_note\": \"cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.\"}, \"completed_at\": \"2026-05-24T07:20:28.248Z\"}, \"p1_tf_ar_kl_divergence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:37:46.355Z\", \"updated_at\": \"2026-05-24T07:18:10.268Z\", \"hypothesis\": \"TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.\", \"metrics\": {\"tg_delta_gar\": 0.0165, \"base_delta_gar\": 0.0122, \"tg_mean_kl\": 0.054, \"base_mean_kl\": 0.043, \"gate_kl_correlation\": 0.11, \"high_kl_layers\": \"L23-L27, L9\", \"gar_robustness_ours_tg_base_ratio\": 21.4, \"gar_robustness_goal_only_ratio\": 63, \"gar_robustness_ours_all_ratio\": 1.7, \"gar_robustness_ours_first_ratio\": 1.8}, \"spec\": {\"command\": \"python scripts/p1_kl_divergence.py\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn_residual_gating/data/eval_200.json\", \"data_count\": 30, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"results/p1_kl_perhead/\", \"log_path\": \"logs/p1_kl_divergence_step2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T07:18:06.521Z\"}, \"qwen15b_phase1_diag\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T06:44:59.895Z\", \"updated_at\": \"2026-05-24T06:53:23.496Z\", \"hypothesis\": \"GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.\", \"spec\": {\"command\": \"python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn-residual-gating/data/train_400.json\", \"data_count\": 400, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"runs/qwen15b_tg_v7_s42/\", \"log_path\": \"logs/qwen15b_phase1_diag.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T06:53:23.496Z\"}, \"d048_eval_ss_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T00:38:41.913Z\", \"updated_at\": \"2026-05-24T01:19:46.692Z\", \"hypothesis\": \"SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.\", \"parent\": \"d048_ss_s456\", \"spec\": {\"command\": \"bash scripts/d048_eval_ss_s456.sh\", \"server\": \"westd-20861\", \"pid\": \"129280\", \"data_path\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\", \"data_count\": 200, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct + SS s456 LoRA\", \"seed\": 456, \"gpu\": 0, \"checkpoint_source\": \"/root/turn-residual-gating/runs/d048_ss_s456/epoch_2\", \"eval_data\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\", \"checkpoint_path\": \"/root/turn-residual-gating/results/d048_final_ar/\", \"log_path\": \"/root/turn-residual-gating/results/d048_final_ar/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T01:19:43.693Z\", \"metrics\": {\"tf_gar_ours_mid\": 0.4964, \"tf_gar_dongre_mid\": 0.3862, \"ar_beta0_gar\": 0.4325, \"ar_beta0_ppl\": 1.4394, \"ar_beta3_gar\": 0.605, \"ar_beta3_ppl\": 1.5868, \"ar_beta5_gar\": 0.7157, \"ar_beta5_ppl\": 1.8045, \"n_convs_ar\": 50}}, \"d048_ss_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:46:14.558Z\", \"updated_at\": \"2026-05-24T00:38:35.393Z\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds\", \"parent\": \"d048_ss_s42\", \"spec\": {\"command\": \"python train_phase2_v8b.py --seed 456 --resume runs/d048_ss_s456/epoch_0 --gate-type threadgate --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3\", \"server\": \"westd-20861\", \"pid\": \"112418\", \"data_path\": \"/root/turn-residual-gating/data/phase2_train.jsonl\", \"data_count\": 2000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 456, \"gpu\": 0, \"checkpoint_source\": \"Qwen/Qwen2.5-7B-Instruct (resume from epoch_0)\", \"eval_data\": \"N/A - training experiment\", \"checkpoint_path\": \"/root/turn-residual-gating/runs/d048_ss_s456/epoch_2\", \"log_path\": \"/root/turn-residual-gating/runs/d048_ss_s456/train.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:38:35.393Z\"}, \"p0_ss_steering_eval\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-23T19:37:39.883Z\", \"updated_at\": \"2026-05-23T19:57:38.851Z\", \"hypothesis\": \"SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.\", \"parent\": \"d048_eval_ss_s42\", \"conclusion\": \"killed\", \"notes\": \"Cancelled: ss_s42_ar_n50.json already contains SS+steering data at β=0,3,5. Results show SS and steering do not stack (β=5: SS 0.717 vs TG-only 0.727). Director decision: skip, use existing data.\"}, \"d048_eval_ss_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T17:29:13.803Z\", \"updated_at\": \"2026-05-23T18:05:41.813Z\", \"hypothesis\": \"SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.\", \"parent\": \"d048_ss_s123\", \"spec\": {\"command\": \"bash scripts/d048_eval_ss_s123.sh\", \"server\": \"westd-20861\", \"pid\": \"110052\", \"data_path\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\", \"data_count\": 200, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct + SS s123 LoRA\", \"seed\": 123, \"gpu\": 0, \"checkpoint_source\": \"/root/turn-residual-gating/runs/d048_ss_s123/epoch_2\", \"eval_data\": \"/root/turn-residual-gating/data/eval_200/eval_200.json\", \"checkpoint_path\": \"/root/turn-residual-gating/results/d048_final_ar/\", \"log_path\": \"/root/turn-residual-gating/results/d048_final_ar/\"}, \"notes\": \"Cron误判修复: 原PID 109385是TF eval子进程,退出后cron 5次检测失败auto-resolved为failed。实际AR eval PID 110052仍在运行。已手动恢复RUNNING。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T18:05:35.103Z\", \"metrics\": {\"tf_gar_ours\": 0.5536, \"tf_gar_dongre\": 0.4106, \"tf_ppl\": 2.6123, \"ar_beta0_gar\": 0.4231, \"ar_beta0_ppl\": 1.4408, \"ar_beta3_gar\": 0.5903, \"ar_beta3_ppl\": 1.607, \"ar_beta5_gar\": 0.7174, \"ar_beta5_ppl\": 1.7852, \"n_convs_tf\": 200, \"n_convs_ar\": 39}}, \"d048_ss_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:54:41.928Z\", \"updated_at\": \"2026-05-23T17:29:06.984Z\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.\", \"parent\": \"d048_ss_s42\", \"spec\": {\"command\": \"python train_phase2_v8b.py --gate-type threadgate --seed 123 --output-dir runs/d048_ss_s123 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3\", \"server\": \"westd-20861\", \"pid\": \"84793\", \"data_path\": \"/root/turn-residual-gating/data/phase2_train.jsonl\", \"data_count\": 2000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 123, \"gpu\": 0, \"checkpoint_source\": \"Qwen/Qwen2.5-7B-Instruct (base, no prior checkpoint)\", \"eval_data\": \"N/A - this is a training experiment\", \"checkpoint_path\": \"/root/turn-residual-gating/runs/d048_ss_s123/epoch_2\", \"log_path\": \"/root/turn-residual-gating/runs/d048_ss_s123/train.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T17:29:06.984Z\"}, \"d048_split_softmax_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:47:05.556Z\", \"updated_at\": \"2026-05-23T08:00:42.748Z\", \"hypothesis\": \"Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.\", \"spec\": {\"command\": \"python src/eval_split_softmax.py\", \"server\": \"westd-20861\", \"data_path\": \"data/eval_200/eval_200.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct + TG v7 LoRA\", \"seed\": 42, \"checkpoint_path\": \"N/A (failed)\", \"log_path\": \"results/split_softmax/\", \"failure_reason\": \"Bug 1: system_prompt_len=0 hardcoded (line 373) — split-softmax has no effect. Bug 2: gen mode NaN for k=0.0/0.3/0.5/0.7. Needs code fix before re-run.\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-23T07:53:10.326Z\", \"notes\": \"2 critical bugs: (1) system_prompt_len=0 hardcoded at L373, (2) gen mode NaN for k≠1.0. Director decision 2026-05-23: not urgent, defer fix past DDL 5/25. Does not affect main paper experiments.\"}, \"d048_final_ar_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T03:46:23.495Z\", \"updated_at\": \"2026-05-23T03:47:01.285Z\", \"hypothesis\": \"Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims\", \"spec\": {\"command\": \"bash scripts/d048_final_ar_eval.sh\", \"server\": \"westd-20861\", \"data_path\": \"data/eval_200/eval_200.json\", \"data_count\": 200, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42\", \"eval_data\": \"eval_200.json N=50\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"runs/d048_final_ar_eval.log\", \"results_path\": \"results/d048_final_ar/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T03:46:57.110Z\", \"metrics\": {\"beta0\": {\"base_gar\": 0.019, \"tg_gar\": 0.064, \"ug_gar\": 0.033, \"lo_gar\": 0.037, \"pcgrad_gar\": 0.03, \"ss_gar\": 0.347}, \"beta3\": {\"base_gar\": 0.531, \"tg_gar\": 0.556, \"ss_gar\": 0.593}, \"beta5\": {\"base_gar\": 0.704, \"tg_gar\": 0.727, \"ss_gar\": 0.717}, \"wilcoxon_beta0\": {\"tg_vs_base_p\": \"<0.001\", \"tg_vs_base_r\": 0.802, \"ss_vs_tg_p\": \"<0.001\", \"ss_vs_tg_r\": 0.869}, \"ppl\": {\"base\": 1.447, \"tg\": 1.432, \"ss\": 1.442}, \"n_convs\": 39}}, \"d048_queue_runner\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T23:42:35.919Z\", \"updated_at\": \"2026-05-22T23:42:39.048Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T23:42:38.157928+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-22T23:42:38.522Z\"}}, \"d048_eval_ss_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T22:52:15.395Z\", \"updated_at\": \"2026-05-22T23:32:26.276Z\", \"spec\": {\"command\": \"bash scripts/d048_eval_ss_s42.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"48241\", \"log_path\": \"/root/turn_residual_gating/runs/d048_ss_s42/eval.log\", \"submitted_at\": \"2026-05-22T22:52:15.275Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/ultrachat_8k + model-gen AR N=50\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct (SS s42)\", \"seed\": 42, \"checkpoint_source\": \"runs/d048_ss_s42/epoch_2\", \"eval_data\": \"ultrachat_eval_heldout 50 + model-gen AR N=50\", \"checkpoint_path\": \"runs/d048_ss_s42/epoch_2\", \"wall_clock_seconds\": 1365.5, \"gpu_hours\": 0.38}, \"hypothesis\": \"D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.\", \"parent\": \"d048_ss_s42\", \"reproduce\": {\"finished_at\": \"2026-05-22T23:12:55.735Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T23:12:58.142628+00:00\"}]}, \"metrics\": {\"tf\": {\"base_gar_ours_mid\": 0.0128, \"base_gar_dongre_mid\": 0.0031, \"base_ppl\": 4.34, \"base_ntp\": 1.4, \"tg_gar_ours_mid\": 0.5025, \"tg_gar_dongre_mid\": 0.389, \"tg_ppl\": 2.78, \"tg_ntp\": 0.98, \"baseline_mid_gar\": 0.0122}, \"ar\": {\"gar_ours_mid\": 0.3887, \"gar_ours_ci_95\": [0.3692, 0.3934], \"ppl\": 1.35}, \"gap_ratio\": 1.29, \"n_conversations_tf\": 50, \"n_conversations_ar\": 5, \"bootstrap_turns\": \"curve[2:] (turns 3-T)\", \"note\": \"AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T23:15:00.734Z\"}, \"d048_ss_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:14:13.365Z\", \"updated_at\": \"2026-05-22T23:11:26.493Z\", \"hypothesis\": \"Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).\", \"spec\": {\"command\": \"bash -c \\\"cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0 2>&1 | tee ~/runs/turn_residual_gating/d048_ss_s42_resume.log\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"32861\", \"log_path\": \"~/runs/turn_residual_gating/d048_ss_s42.log\", \"submitted_at\": \"2026-05-22T15:59:07.519Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T15:51:53.120Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 424.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 218.56 MiB is free. Including non-PyTorch memory, this process has 26.13 GiB memory in use. Process 30899 has 68.62 GiB memory in use. Of the allocated\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T15:51:54.391Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T15:51:56.369724+00:00\"}]}, \"notes\": \"Training complete (resume v3). 23418s (6.5h) for epoch 1+2. Final: Avg Loss=0.9326, NTP=0.9320, GAR=0.0007, DIV=0.0000. Gate: mean=0.9527, std=0.0589, min=0.7383(L4), max=1.000. SS: 4750/16000 (29.7%) used, 0 fallback. Checkpoints: epoch_0, epoch_1, epoch_2, final. Gate profile consistent with prior SS runs (L4 lowest).\", \"metrics\": {\"final_avg_loss\": 0.9326, \"final_ntp_loss\": 0.932, \"final_gar_loss\": 0.0007, \"gate_mean\": 0.9527, \"gate_std\": 0.0589, \"gate_min\": 0.7383, \"gate_min_layer\": \"L4\", \"gate_max\": 1, \"ss_usage\": \"4750/16000 (29.7%)\", \"ss_fallback\": 0, \"epochs_completed\": 3, \"wall_clock_s\": 23418, \"wall_clock_h\": 6.5}}, \"d048_ss_s42_resume\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:57:05.941Z\", \"updated_at\": \"2026-05-22T15:57:05.941Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"32472\", \"log_path\": \"~/runs/turn_residual_gating/d048_ss_s42_resume.log\", \"submitted_at\": \"2026-05-22T15:57:05.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_llama_ar_n20\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:52:04.543Z\", \"updated_at\": \"2026-05-22T08:38:33.680Z\", \"hypothesis\": \"N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.\", \"parent\": \"eval_llama_lora_only_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_ar_n20.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"312592\", \"log_path\": \"~/runs/turn_residual_gating/eval_llama_ar_n20.log\", \"submitted_at\": \"2026-05-22T07:52:13.830Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ultrachat_200k + model-gen AR\", \"data_count\": 20, \"model_name\": \"Llama-3.1-8B-Instruct (Base/TG/LoRA-only)\", \"seed\": 42, \"checkpoint_source\": \"llama_tg_s42 + llama_lora_only_s42\", \"eval_data\": \"AR-generated 20 conversations x 4 turns\", \"wall_clock_seconds\": 1435.6, \"gpu_hours\": 0.4}, \"reproduce\": {\"finished_at\": \"2026-05-22T08:09:48.181Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T08:09:50.100538+00:00\"}]}, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/runs/turn_residual_gating/eval_llama_ar_n20.log\", \"metrics\": {\"base\": {\"gar_ours_mean\": 0.0088, \"gar_ours_std\": 0.0056, \"gar_ours_median_per_conv\": 0.0093, \"gar_ours_median_per_turn_pool\": 0.0071, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0049, \"gar_dongre_std\": 0.0013, \"gar_dongre_median\": 0.0047, \"ngar_ours_mid\": 0.1019, \"ngar_dongre_mid\": 0.1171, \"ppl\": 1.293, \"ppl_std\": 0.07, \"ntp_loss\": 0.2552}, \"tg\": {\"gar_ours_mean\": 0.0434, \"gar_ours_std\": 0.1002, \"gar_ours_median_per_conv\": 0.0179, \"gar_ours_median_per_turn_pool\": 0.0126, \"gar_ours_spike_ratio\": \"5% (2/40 turns GAR>=0.4)\", \"gar_dongre_mean\": 0.0183, \"gar_dongre_std\": 0.0198, \"gar_dongre_median\": 0.0152, \"ngar_ours_mid\": 0.5357, \"ngar_dongre_mid\": 0.4436, \"ppl\": 1.437, \"ppl_std\": 0.077, \"ntp_loss\": 0.3612}, \"lora_only\": {\"gar_ours_mean\": 0.0284, \"gar_ours_std\": 0.0481, \"gar_ours_median_per_conv\": 0.0184, \"gar_ours_median_per_turn_pool\": 0.0133, \"gar_ours_spike_ratio\": \"0%\", \"gar_dongre_mean\": 0.0205, \"gar_dongre_std\": 0.0241, \"gar_dongre_median\": 0.016, \"ngar_ours_mid\": 0.3488, \"ngar_dongre_mid\": 0.4997, \"ppl\": 1.419, \"ppl_std\": 0.075, \"ntp_loss\": 0.3483}, \"n_conversations\": 20, \"n_turns\": 4, \"mid_turns_definition\": \"turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.\", \"stat_pool\": \"median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).\", \"ranking_gar_ours_mean\": \"TG(0.0434) > LO(0.0284) > Base(0.0088)\", \"ranking_gar_ours_median_per_conv\": \"TG(0.0179) ≈ LO(0.0184) > Base(0.0093)\", \"ranking_gar_ours_median_per_turn_pool\": \"TG(0.0126) ≈ LO(0.0133) > Base(0.0071)\", \"ranking_gar_dongre\": \"LO(0.0205) > TG(0.0183) > Base(0.0049)\", \"note\": \"Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).\"}, \"notes\": \"N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries use same definition)**. Two median levels: median_per_conv (paper §5.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 per-conversation mid-turn averages; median_per_turn_pool (TG 0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual turns. Both confirm TG ≈ LO (zero-increment). Mean (TG 0.0434 > LO 0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR≥0.4; LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). Pending paper fix: §5.5 says \\\"turns 2-T\\\" but code excludes turns 1-2; will correct to \\\"excluding the first two turns\\\" in next paper edit batch.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T08:16:09.384Z\"}, \"eval_llama_lora_only_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:40:25.352Z\", \"updated_at\": \"2026-05-22T07:51:32.758Z\", \"hypothesis\": \"LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.\", \"parent\": \"llama_lora_only_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_lora_only_s42.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"309670\", \"log_path\": \"/root/runs/turn_residual_gating/eval_llama_lora_only_s42.log\", \"submitted_at\": \"2026-05-22T07:40:34.437Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"ultrachat_200k + model-gen\", \"data_count\": 55, \"model_name\": \"Llama-3.1-8B-Instruct + LoRA-only checkpoint\", \"seed\": 42, \"checkpoint_source\": \"llama_lora_only_s42\", \"eval_data\": \"IID heldout 50 + model-gen 5\", \"checkpoint_path\": \"runs/phase2_llama_lora_only_s42/epoch_2\", \"wall_clock_seconds\": 650.8, \"gpu_hours\": 0.18}, \"reproduce\": {\"finished_at\": \"2026-05-22T07:45:28.637Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T07:45:30.556207+00:00\"}]}, \"metrics\": {\"tf\": {\"gar_ours\": 0.4807, \"gar_dongre\": 0.0188, \"ngar_ours\": 11.8031, \"ngar_dongre\": 0.8261, \"ppl\": 2.6, \"ntp_loss\": 0.9366, \"n_conversations\": 50, \"n_turns\": 4}, \"ar\": {\"gar_ours\": 0.0617, \"gar_dongre\": 0.0226, \"ngar_ours\": 0.6065, \"ngar_dongre\": 0.2537, \"ppl\": 1.32, \"ntp_loss\": 0.2787, \"n_conversations\": 5, \"n_turns\": 10}, \"gap_ratio_gar_ours\": 7.79}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T07:51:25.244Z\"}, \"llama_lora_only_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:33:03.465Z\", \"updated_at\": \"2026-05-22T07:39:06.888Z\", \"hypothesis\": \"Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。\", \"parent\": \"llama_tg_s42\", \"spec\": {\"command\": \"bash scripts/launch_llama_lora_only_s42.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"271741\", \"log_path\": \"logs/llama_lora_only_s42.log\", \"submitted_at\": \"2026-05-22T00:33:16.591Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch, ablation baseline)\", \"eval_data\": \"N/A (training run, not eval)\", \"checkpoint_path\": \"runs/phase2_llama_lora_only_s42/epoch_2\", \"wall_clock_seconds\": 25550.3, \"gpu_hours\": 7.1}, \"reproduce\": {\"finished_at\": \"2026-05-22T07:35:56.232Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T07:35:58.740298+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_avg_loss\": 0.9288, \"final_avg_ntp\": 0.9279, \"final_avg_gar\": 0.0009, \"gate_fixed\": 1, \"gate_type\": \"none\", \"wall_clock_s\": 25317, \"wall_clock_h\": 7.03, \"epochs_completed\": 3}, \"completed_at\": \"2026-05-22T07:39:06.889Z\"}, \"phase2_tg_s42_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:53:01.911Z\", \"updated_at\": \"2026-05-22T04:37:13.229Z\", \"hypothesis\": \"smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。\", \"parent\": \"phase2_tg_s42_v5\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode smooth_saturation --gar-target 0.5 --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v6 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\\\"\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v6\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v6.log\"}, \"metrics\": {\"dryrun_step0_L_NTP\": 2.0275, \"dryrun_step0_L_GAR\": -0.0161, \"dryrun_step0_total_loss\": 2.0114, \"dryrun_step4_L_NTP\": 1.6544, \"dryrun_step4_L_GAR\": -0.0147, \"dryrun_step4_total_loss\": 1.6397, \"dryrun_gate_grad\": true, \"dryrun_gate_mean_init\": 0.8097, \"dryrun_gate_std_init\": 0.0341, \"dryrun_gate_min_init\": 0.6836, \"dryrun_gate_max_init\": 0.8672, \"dryrun_gate_mean_step5\": 0.8025, \"dryrun_gate_std_step5\": 0.0842, \"dryrun_gate_min_step5\": 0.5547, \"dryrun_gate_max_step5\": 0.9805, \"gs50_gate_mean\": 0.8117, \"gs50_gate_std\": 0.0612, \"gs50_gate_min\": 0.6836, \"gs50_gate_max\": 0.9805, \"gs100_gate_mean\": 0.8737, \"gs100_gate_std\": 0.0367, \"gs100_gate_min\": 0.8164, \"gs100_gate_max\": 0.9766, \"gs100_L_NTP\": 0.8151, \"gs100_L_GAR\": -0.158, \"gs100_total_loss\": 0.6571, \"gs100_profile_bottom3\": \"L12=0.816 L4=0.824 L13=0.824\", \"gs100_profile_top3\": \"L27=0.977 L26=0.961 L23=0.914\", \"gs143_L_GAR\": -0.3876, \"gs143_gate_mean\": 0.9227}, \"conclusion\": \"negative\", \"notes\": \"smooth_saturation 与 maximize 同轨迹，单调 GAR 奖励导致恒等退化。step 100: gate_std=0.037↓ gate_mean=0.874↑，step ~143: L_GAR=-0.39 gate_mean=0.923。boundedness 只减缓退化速度不改变终态。D010 指令 kill 转 v7 MSE 双向 loss。\", \"completed_at\": \"2026-05-18T18:18:07.869Z\"}, \"phase2_tg_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:04:12.759Z\", \"updated_at\": \"2026-05-22T04:36:54.262Z\", \"hypothesis\": \"ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预\", \"parent\": \"phase1_gar_diag\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"11286\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42.log\", \"submitted_at\": \"2026-05-18T07:03:28.476Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15333, \"gpu_hours\": 4.26, \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_s42\"}, \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": \"11286\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048\\\"\", \"finished_at\": \"2026-05-18T11:19:00.888Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T11:19:01.512Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T11:19:02.835359+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=143 (SIGTERM) — 大概率被 Worker code:diagnose_gar_loss_and_fix 主动 kill（时间线：Worker 11:13 启动 → v2 11:13 创建 → v1 11:19 SIGTERM）。v2 hypothesis 指出 GAR loss 实现有 bug（缺少 ε=0.001 稳定项）。诊断 Worker worker_diagnose_phase2_tg_s42_20260518T112048 已派出确认日志详情。| 建议: 等诊断结果确认后推进 v2\", \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_s42/epoch_1\", \"metrics\": {\"final_ntp_loss\": 0.94, \"final_gar_loss\": 0, \"gate_mean\": 0.988, \"gar_loss_zero_pct\": 87.6, \"epochs_completed\": 1.67, \"killed_reason\": \"SIGTERM by diagnose worker (unauthorized)\"}}, \"eval_v7_tg_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T22:53:18.163Z\", \"updated_at\": \"2026-05-22T00:30:49.653Z\", \"spec\": {\"command\": \"bash scripts/eval_v7_tg_s123.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"264869\", \"log_path\": \"/root/turn_residual_gating/logs/v7_tg_s123.log\", \"submitted_at\": \"2026-05-21T22:53:18.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"v7_tg_s123\", \"eval_data\": \"data/ultrachat_8k\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2\", \"wall_clock_seconds\": 5844.5, \"gpu_hours\": 1.62}, \"hypothesis\": \"v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness\", \"parent\": \"v7_tg_s123\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T00:30:42.606Z\", \"metrics\": {\"iid_tf\": {\"gar_ours_mid\": 0.5052, \"gar_dongre_mid\": 0.0119, \"ppl\": 2.7802, \"ntp\": 0.9752}, \"modelgen_ar\": {\"gar_ours_mid\": 0.0165, \"gar_dongre_mid\": 0.0177, \"ppl\": 1.3855, \"ntp\": 0.3223}, \"gap_ratio\": 30.6, \"comparison_s42\": {\"tf_gar_ours_delta\": 0.0017, \"ar_gar_ours_delta\": 0.0008, \"gap_ratio_delta\": -1.4}}}, \"eval_v8b_ss_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:15:52.880Z\", \"updated_at\": \"2026-05-21T22:53:15.356Z\", \"spec\": {\"command\": \"bash scripts/eval_v8b_ss_s123.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": 259767, \"log_path\": \"runs/eval_v8b_ss_s123/\", \"submitted_at\": \"2026-05-21T21:15:52.785Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/ultrachat_eval_heldout.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"gpu_index\": 0, \"checkpoint_source\": \"checkpoints/tg_v8b_ss_s123/epoch_2\", \"eval_data\": \"ultrachat_eval_heldout + model-gen\", \"checkpoint_path\": \"checkpoints/tg_v8b_ss_s123/epoch_2\", \"wall_clock_seconds\": 5835.7, \"gpu_hours\": 1.62}, \"hypothesis\": \"v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach\", \"parent\": \"v7_tg_s123\", \"log_path\": \"~/runs/turn_residual_gating/eval_v8b_ss_s123.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T22:53:08.443Z\", \"metrics\": {\"iid\": {\"gar_ours\": 0.503, \"gar_dongre\": 0.394, \"ppl\": 2.781, \"ntp_loss\": 0.976, \"n_conv\": 50, \"n_turns\": 3}, \"modelgen\": {\"gar_ours\": 0.418, \"gar_dongre\": 0.441, \"ppl\": 1.389, \"ntp_loss\": 0.325, \"n_conv\": 5, \"n_turns\": 10}, \"gap_ratio\": 1.2, \"base_iid_ppl\": 4.338, \"base_modelgen_ppl\": 1.351}}, \"v7_tg_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T15:16:39.923Z\", \"updated_at\": \"2026-05-21T21:17:16.499Z\", \"hypothesis\": \"v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash scripts/launch_v7_tg_s123.sh\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"pid\": 245628, \"gpu_index\": 0, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s123_v7\", \"log_path\": \"/root/turn_residual_gating/logs/v7_tg_s123.log\", \"checkpoint_source\": \"N/A (from scratch)\", \"eval_data\": \"N/A\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"runs/phase2_tg_s123_v7/epoch_2\", \"log_path\": \"logs/v7_tg_s123.log\", \"metrics\": {\"epoch_1\": {\"avg_loss\": 0.9447, \"avg_ntp_loss\": 0.9434, \"avg_gar_loss\": 0.0013, \"avg_div_loss\": 0}, \"epoch_2\": {\"avg_loss\": 0.9315, \"avg_ntp_loss\": 0.9305, \"avg_gar_loss\": 0.001, \"avg_div_loss\": 0}, \"final_gate\": {\"mean\": 0.9467, \"std\": 0.051, \"min\": 0.793, \"max\": 1}, \"final_gate_profile\": {\"L0\": 0.883, \"L1\": 0.793, \"L2\": 0.996, \"L3\": 0.988, \"L4\": 0.984, \"L5\": 0.797, \"L6\": 0.961, \"L7\": 0.918, \"L8\": 0.965, \"L9\": 0.934, \"L10\": 0.969, \"L11\": 0.918, \"L12\": 0.926, \"L13\": 0.941, \"L14\": 0.93, \"L15\": 0.965, \"L16\": 0.941, \"L17\": 0.91, \"L18\": 0.961, \"L19\": 0.965, \"L20\": 0.973, \"L21\": 0.988, \"L22\": 0.969, \"L23\": 0.98, \"L24\": 0.98, \"L25\": 0.984, \"L26\": 0.988, \"L27\": 1}, \"training_time_s\": 21425.2}, \"completed_at\": \"2026-05-21T21:17:16.499Z\"}, \"v8b_ss_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:29:28.197Z\", \"updated_at\": \"2026-05-21T15:15:49.282Z\", \"hypothesis\": \"v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。\", \"parent\": \"phase2_tg_s42_v8b_resume\", \"spec\": {\"command\": \"bash scripts/launch_v8b_ss_s123.sh\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"N/A (from scratch)\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_v8b_ss_s123\", \"log_path\": \"/root/turn_residual_gating/logs/v8b_ss_s123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9316, \"final_ntp_loss\": 0.9307, \"final_gar_loss\": 0.0009, \"final_gate_mean\": 0.9505, \"final_gate_std\": 0.0508, \"final_gate_min\": 0.7383, \"final_gate_max\": 1, \"ss_used_ratio\": 0.371, \"training_time_s\": 38773.4, \"epoch0_loss\": 1.0092, \"epoch1_loss\": 0.9444, \"epoch2_loss\": 0.9316}, \"completed_at\": \"2026-05-21T15:15:49.282Z\"}, \"llama_tg_training\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:37:31.513Z\", \"updated_at\": \"2026-05-21T09:44:18.859Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T03:37:33.309826+00:00\"}]}, \"notes\": \"INVALIDATED: Phantom duplicate of llama_tg_s42 (same PID 199643, same experiment). Created by Worker in global registry, duplicated to project registry. Canonical entry is llama_tg_s42 (DONE/success).\"}, \"llama_ar_matched_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:59:40.918Z\", \"updated_at\": \"2026-05-21T04:36:23.237Z\", \"hypothesis\": \"用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。\", \"parent\": \"llama_eval_s42\", \"spec\": {\"command\": \"bash scripts/eval_llama_ar_matched.sh\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_eval_sample.json\", \"data_count\": 50, \"model_name\": \"Meta-Llama-3.1-8B-Instruct + TG LoRA\", \"seed\": 42, \"checkpoint_source\": \"phase2_llama_tg_s42\", \"eval_data\": \"50 UltraChat convs, T=4, AR generation, 4 conditions (base/TG x ours/Dongre)\", \"checkpoint_path\": \"N/A (eval)\", \"log_path\": \"runs/eval_llama_ar_matched.log\"}, \"log_path\": \"/root/turn_residual_gating/runs/eval_llama_ar_matched.log\", \"conclusion\": \"success\", \"metrics\": {\"ar_base_ours\": {\"mid_gar\": 0.0082, \"ngar\": 0.1, \"ppl\": 1.267}, \"ar_tg_ours\": {\"mid_gar\": 0.0388, \"ngar\": 0.493, \"ppl\": 1.413}, \"ar_base_dongre\": {\"mid_gar\": 0.0051, \"ngar\": 0.12, \"ppl\": 1.267}, \"ar_tg_dongre\": {\"mid_gar\": 0.018, \"ngar\": 0.431, \"ppl\": 1.413}, \"tf_reference\": {\"tf_tg_ours_ngar\": 11.88, \"tf_base_ours_ngar\": 0.388, \"tf_tg_ours_raw\": 0.4836, \"tf_tg_dongre_raw\": 0.018}, \"matched_gap_analysis\": {\"gar_ours_raw_gap\": \"12.5x (TF 0.484 / AR 0.039)\", \"gar_ours_ngar_gap\": \"24.1x (TF 11.88 / AR 0.493)\", \"gar_dongre_raw_gap\": \"1.002x (TF 0.018 / AR 0.018) — zero gap\", \"tg_over_base_ar_ours\": \"4.71x\", \"tg_over_base_ar_dongre\": \"3.54x\", \"conclusion\": \"GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.\"}}, \"completed_at\": \"2026-05-21T04:28:38.504Z\", \"notes\": \"CORRECTION (2026-05-21 04:36): Agent 之前错误地将 AR TG nGAR (0.493) 与 TF TG raw GAR (0.484) 对比，误判为 'nGAR aligns, gap is normalization artifact'。Reviewer 核实：TF TG ours nGAR = 11.88（非 0.48）。nGAR gap = 11.88 / 0.493 = 24.1×，比 raw gap (12.5×) 还大。'Normalization artifact' 分析完全错误——GAR-ours 的 gap 是真实的 exposure bias。论文绝对不能使用 normalization artifact 叙事。\"}, \"instruction_retention_test\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:49:26.068Z\", \"updated_at\": \"2026-05-21T03:59:31.835Z\", \"hypothesis\": \"Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.\", \"spec\": {\"command\": \"python src/eval_instruction_retention.py --checkpoint runs/phase2_tg_s42_v7 --prompts data/instruction_retention_prompts.json --betas 0 3 --seed 42 --output results/instruction_retention.json\", \"server\": \"westd-20861\", \"data_path\": \"data/instruction_retention_prompts.json\", \"data_count\": 18, \"model_name\": \"Qwen2.5-7B-Instruct + v7 TG LoRA\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"18 instruction retention prompts, beta=[0,3], 5 turns each\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (eval)\", \"log_path\": \"/root/turn_residual_gating/results/instruction_retention.log\", \"metrics\": {\"late_turn_rate_beta0\": 0.759, \"late_turn_rate_beta3\": 0.87, \"late_turn_delta\": 0.111, \"mcnemar_chi2\": 3.125, \"mcnemar_p\": 0.0771, \"gar_compliance_r\": 0.2003, \"gar_compliance_p\": 0.007, \"category_content_constraint\": {\"beta0\": 0.619, \"beta3\": 0.857, \"delta\": 0.238}, \"category_count_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_format_constraint\": {\"beta0\": 1, \"beta3\": 1, \"delta\": 0}, \"category_position_constraint\": {\"beta0\": 0.667, \"beta3\": 0.733, \"delta\": 0.067}}, \"completed_at\": \"2026-05-21T03:59:31.835Z\"}, \"llama_eval_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:29:51.255Z\", \"updated_at\": \"2026-05-21T03:46:58.167Z\", \"hypothesis\": \"Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。\", \"parent\": \"llama_tg_s42\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_tg_s42.sh 2>&1 | tee runs/eval_llama_tg_s42.log\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_eval_sample.json\", \"data_count\": 50, \"model_name\": \"Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"runs/phase2_llama_tg_s42/epoch_2\", \"eval_data\": \"ultrachat_eval_sample\"}, \"checkpoint_path\": \"runs/phase2_llama_tg_s42/epoch_2\", \"log_path\": \"runs/eval_llama_tg_s42.log\", \"metrics\": {\"tf_base\": {\"gar_ours\": 0.0166, \"ngar_ours\": 0.3882, \"gar_dongre\": 0.0038, \"ngar_dongre\": 0.163, \"ppl\": 3.45, \"N\": 50, \"T\": 4}, \"tf_tg\": {\"gar_ours\": 0.4836, \"ngar_ours\": 11.8818, \"gar_dongre\": 0.018, \"ngar_dongre\": 0.7922, \"ppl\": 2.57, \"N\": 50, \"T\": 4}, \"ar_base\": {\"gar_ours\": 0.0086, \"ngar_ours\": 0.0798, \"gar_dongre\": 0.0118, \"ngar_dongre\": 0.1265, \"ppl\": 1.24, \"N\": 5, \"T\": 10}, \"ar_tg\": {\"gar_ours\": 0.0304, \"ngar_ours\": 0.2632, \"gar_dongre\": 0.0217, \"ngar_dongre\": 0.2459, \"ppl\": 1.32, \"N\": 5, \"T\": 10}, \"gap_ratio_tg_ours\": 15.9, \"gap_ratio_base_ours\": 1.93, \"gap_ratio_tg_dongre\": 0.83, \"vs_qwen_v7_gap_ratio\": 32.1, \"baseline_mid_gar\": 0.0122}, \"conclusion\": \"success\", \"notes\": \"C5 跨模型泛化确认。Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)，低于 Qwen v7 的 32x 但仍非常显著。Base model gap 仅 1.9x（control 通过）。注意 TF/AR eval 设定不同 (N=50/T=4 vs N=5/T=10)，可能影响绝对值对比。GAR-dongre 无明显 gap (ratio 0.83x, AR ≥ TF)，仅 GAR-ours 展现 exposure bias 效应。Gate dynamic range: L24/L28/L30 diff 最大 (0.23-0.38)，与 Qwen 类似集中在中高层。\", \"completed_at\": \"2026-05-21T03:46:58.167Z\"}, \"llama_tg_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T01:34:36.906Z\", \"updated_at\": \"2026-05-21T03:28:07.022Z\", \"hypothesis\": \"在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。\", \"parent\": \"llama_phase1_gar_diag\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python src/train_phase2.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct --data-dir data/ultrachat_8k --output-dir runs/phase2_llama_tg_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"199643\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_llama_tg_s42\", \"log_path\": \"/root/turn_residual_gating/logs/llama_tg_training.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T03:27:55.963Z\", \"metrics\": {\"epochs_completed\": 3, \"total_steps\": 3000, \"wall_clock_seconds\": 26212, \"wall_clock_hours\": 7.28, \"final_avg_loss\": 0.9233, \"final_avg_ntp\": 0.9224, \"final_avg_gar\": 0.0009, \"final_avg_div\": 0, \"final_gate_mean\": 0.9099, \"final_gate_std\": 0.0701, \"final_gate_min\": 0.7188, \"final_gate_max\": 0.9922, \"gate_profile_step3000\": {\"L0\": 0.957, \"L1\": 0.973, \"L2\": 0.977, \"L3\": 0.965, \"L4\": 0.992, \"L5\": 0.969, \"L6\": 0.957, \"L7\": 0.957, \"L8\": 0.961, \"L9\": 0.949, \"L10\": 0.938, \"L11\": 0.934, \"L12\": 0.969, \"L13\": 0.953, \"L14\": 0.957, \"L15\": 0.965, \"L16\": 0.953, \"L17\": 0.961, \"L18\": 0.922, \"L19\": 0.902, \"L20\": 0.883, \"L21\": 0.863, \"L22\": 0.836, \"L23\": 0.844, \"L24\": 0.809, \"L25\": 0.719, \"L26\": 0.762, \"L27\": 0.805, \"L28\": 0.801, \"L29\": 0.855, \"L30\": 0.898, \"L31\": 0.934}, \"checkpoint_size_gate_mb\": 4.2, \"checkpoint_size_lora_mb\": 26, \"gpu\": \"NVIDIA RTX PRO 6000 Blackwell\", \"vram_gb\": 102, \"mem_used_gb\": 63.4}}, \"attention_steering_gen_n50\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:04:17.455Z\", \"updated_at\": \"2026-05-21T01:59:57.100Z\", \"hypothesis\": \"N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。\", \"parent\": \"attention_steering_v7_tg_gen\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py --checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 --output-dir runs/attention_steering/ --output-name attention_steering_gen_n50\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"data_path\": \"data/eval_200/eval_200.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct + v7 TG LoRA\", \"seed\": \"N/A (eval)\", \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"50 conversations from eval_200.json, gen mode autoregressive\", \"checkpoint_path\": \"N/A (eval experiment)\", \"log_path\": \"/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json\"}, \"metrics\": {\"corrected\": true, \"aggregation\": \"per-conv mid_gar(turns 2-7), >=3 turns only\", \"beta_0.0\": {\"mid_gar\": 0.0641, \"mid_gar_std\": 0.0809, \"ppl\": 1.4324, \"ppl_std\": 0.1029, \"n_valid\": 39}, \"beta_2.0\": {\"mid_gar\": 0.128, \"mid_gar_std\": 0.1101, \"ppl\": 1.4822, \"ppl_std\": 0.1385, \"n_valid\": 39}, \"beta_3.0\": {\"mid_gar\": 0.5558, \"mid_gar_std\": 0.0601, \"ppl\": 1.5605, \"ppl_std\": 0.1719, \"n_valid\": 39}, \"beta_4.0\": {\"mid_gar\": 0.6439, \"mid_gar_std\": 0.0607, \"ppl\": 1.6674, \"ppl_std\": 0.2241, \"n_valid\": 39}, \"beta_5.0\": {\"mid_gar\": 0.7271, \"mid_gar_std\": 0.0605, \"ppl\": 1.7723, \"ppl_std\": 0.2693, \"n_valid\": 38}, \"beta_10.0\": {\"mid_gar\": 0.9612, \"mid_gar_std\": 0.0152, \"ppl\": 3.4517, \"ppl_std\": 1.7813, \"n_valid\": 39}, \"n_convs_total\": 50, \"n_convs_valid\": 39, \"mode\": \"gen\", \"phase_transition_range\": \"[2, 3]\"}, \"conclusion\": \"success\", \"notes\": \"原始聚合有 min_turns 截断 bug（截到 2 turns），修正后用 per-conv mid_gar(turns 2-7)。39/50 对话有 ≥3 turns 参与统计。修正后 baseline β=0 GAR 从 0.101 降到 0.064（median 0.031 与 N=5 的 0.028 一致）。Phase transition 在 β∈[2,3] 重现。β=10 corrected 0.961 ≈ N=5 的 0.959。\", \"completed_at\": \"2026-05-20T19:55:34.383Z\"}, \"phase2_tg_s42_v8b_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:08:29.483Z\", \"updated_at\": \"2026-05-21T01:56:13.289Z\", \"hypothesis\": \"从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"parent\": \"phase2_tg_s42_v8b_ss_fixed\", \"spec\": {\"command\": \"python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5 --resume checkpoints/tg_v8b_ss_fixed_s42/epoch_0\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v8b_ss_fixed/epoch_0\", \"eval_data\": \"N/A (training experiment)\", \"checkpoint_path\": \"checkpoints/tg_v8b_ss_fixed_s42\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v8b_resume.log\"}, \"metrics\": {\"training\": {\"total_steps\": 3000, \"epochs_completed\": 3, \"wall_clock_hours\": 8.1, \"final_loss\": 0.933, \"final_ntp_loss\": 0.9322, \"final_gar_loss\": 0.0008, \"final_gate_mean\": 0.9586, \"final_gate_std\": 0.0582, \"ss_ratio\": 0.5}, \"eval_iid\": {\"gar_ours\": 0.4983, \"gar_dongre\": 0.3855, \"ppl\": 2.78}, \"eval_modelgen\": {\"gar_ours\": 0.3177, \"gar_dongre\": 0.3533, \"ppl\": 1.38}, \"vs_v7\": {\"iid_gar_ours_delta\": -0.005, \"modelgen_gar_ours_delta\": 0.302, \"gap_ratio_v7\": 32, \"gap_ratio_v8b\": 1.57}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T18:57:21.189Z\"}, \"llama_phase1_gar_diag\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:39:25.751Z\", \"updated_at\": \"2026-05-21T01:34:36.417Z\", \"hypothesis\": \"Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。\", \"spec\": {\"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"account\": \"local\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/run_phase1_gar_llama.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ --output-dir /root/turn_residual_gating/runs/phase1_llama_gar_diag --max-new-tokens 256\", \"pid\": \"198817\", \"data_path\": \"built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, debate)\", \"data_count\": 5, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (base model, no fine-tuning)\", \"eval_data\": \"5 built-in conversations x 10 turns each, gen mode\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/turn_residual_gating/logs/llama_phase1_gar_diag.log\"}, \"conclusion\": \"success\", \"metrics\": {\"per_turn_gar\": {\"turn_1\": 0.0263, \"turn_2\": 0.0183, \"turn_3\": 0.0087, \"turn_4\": 0.0055, \"turn_5\": 0.006, \"turn_6\": 0.0035, \"turn_7\": 0.0038, \"turn_8\": 0.0037, \"turn_9\": 0.005, \"turn_10\": 0.0026}, \"t1_t10_decay_pct\": 90.1, \"t1_mid38_drop_pct\": 80.2, \"n_topics\": 5, \"model\": \"Meta-Llama-3.1-8B-Instruct\", \"mode\": \"gen\", \"n_conversations\": 5, \"n_turns\": 10}, \"completed_at\": \"2026-05-21T01:34:36.417Z\"}, \"eval_v8b_ss\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:44:23.366Z\", \"updated_at\": \"2026-05-20T18:45:14.523Z\", \"hypothesis\": \"Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.\", \"parent\": \"phase2_tg_s42_v8b_ss\", \"spec\": {\"command\": \"python src/eval_phase2_gar.py --checkpoint-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate\", \"server\": \"westd-20861\", \"data_path\": \"data/ultrachat_eval_heldout.json + built-in 5conv model-gen\", \"data_count\": \"50 heldout + 5 model-gen\", \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/tg_v8b_ss_fixed_s42\", \"eval_data\": \"ultrachat_eval_heldout.json (IID) + built-in model-gen (5x10 turns)\", \"checkpoint_path\": \"checkpoints/tg_v8b_ss_fixed_s42\", \"log_path\": \"/tmp/eval_v8b_all.log\"}, \"metrics\": {\"iid_gar_ours\": 0.4983, \"iid_gar_dongre\": 0.3855, \"iid_ppl\": 2.78, \"iid_ngar_ours\": 13.5, \"iid_ngar_dongre\": 22.68, \"modelgen_gar_ours\": 0.3177, \"modelgen_gar_dongre\": 0.3533, \"modelgen_ppl\": 1.38, \"modelgen_ngar_ours\": 4.47, \"modelgen_ngar_dongre\": 5.92, \"iid_turn1_gar_ours\": 0.5398, \"modelgen_turn1_gar_ours\": 0.4333}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T18:45:14.523Z\"}, \"attention_steering_eval200_tf\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:58:23.626Z\", \"updated_at\": \"2026-05-20T10:08:24.710Z\", \"hypothesis\": \"N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。\", \"parent\": \"attention_steering_v7_tg_gen\", \"spec\": {\"command\": \"python src/eval_attention_steering.py --mode tf --betas 0 2 3 4 5 10 --output-name eval200_attention_steering.json (data: eval_200/eval_200.json, 200 convs)\", \"server\": \"westd-20861\", \"data_path\": \"data/eval_200/eval_200.json\", \"data_count\": 200, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"data/eval_200/eval_200.json\", \"checkpoint_path\": \"checkpoints/tg_v7_s42/final\", \"log_path\": \"/tmp/eval200_steering.log\"}, \"metrics\": {\"beta_0.0\": {\"mid_gar\": 0.5353, \"ppl\": 2.62}, \"beta_2.0\": {\"mid_gar\": 0.6112, \"ppl\": 2.69}, \"beta_3.0\": {\"mid_gar\": 0.788, \"ppl\": 2.93}, \"beta_4.0\": {\"mid_gar\": 0.8165, \"ppl\": 3.49}, \"beta_5.0\": {\"mid_gar\": 0.8325, \"ppl\": 6.15}, \"beta_10.0\": {\"mid_gar\": 0.977, \"ppl\": 505.21}, \"n_convs\": 200, \"mode\": \"tf\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T10:08:24.710Z\"}, \"trc_baseline_v7_tg\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:18:17.576Z\", \"updated_at\": \"2026-05-20T09:34:40.734Z\", \"hypothesis\": \"如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash scripts/launch_trc_baseline.sh\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"158700\", \"log_path\": \"/root/runs/turn_residual_gating/trc_baseline_v7_tg.log\", \"submitted_at\": \"2026-05-20T07:18:38.202Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/standard_conversations.json\", \"data_count\": 5, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_lora_only_s42 + base\", \"eval_data\": \"5 hardcoded multi-turn conversations x 10 turns\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/trc_baseline/\", \"wall_clock_seconds\": 7767.7, \"gpu_hours\": 2.16}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:28:05.853Z\", \"metrics\": {\"v7_tg\": {\"tf_trc\": 0.3339, \"gen_trc\": 0.3323, \"trc_gap\": 0.0016, \"tf_tbp_ppl\": 1.05, \"gen_tbp_ppl\": 1.05}, \"lora_only\": {\"tf_trc\": 0.349, \"gen_trc\": 0.4106, \"trc_gap\": -0.0617, \"tf_tbp_ppl\": 9.5, \"gen_tbp_ppl\": 12}, \"base\": {\"tf_trc\": 0.1494, \"gen_trc\": 0.1494, \"trc_gap\": 0, \"tf_tbp_ppl\": 2.05, \"gen_tbp_ppl\": 2.05}}, \"notes\": \"Cross-space 验证：exposure bias 是 attention-specific。v7 TG: TRC gap = +0.002 (近零)，hidden state 一致性在 TF/gen 之间无差异。对比 GAR 的 30x gap，TRC 无 gap → exposure bias 只扭曲 attention 分布，不影响 hidden state 层面。LoRA-only: 反转 gap (-0.062)，gen TRC 更高但 TBP PPL 严重恶化 (9.5→12.0)——hidden states \\\"坍缩\\\"趋同但信息量下降。Base: 零 gap（但可能有 eval 脚本 bug，gen 模式复用了 TF hidden states）。\"}, \"attention_steering_v7_tg_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T07:07:20.607Z\", \"updated_at\": \"2026-05-20T09:30:17.530Z\", \"hypothesis\": \"推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash scripts/launch_attention_steering.sh gen\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"157657\", \"log_path\": \"runs/attention_steering/phase2_tg_s42_v7_attention_steering.json\", \"submitted_at\": \"2026-05-20T07:07:27.678Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/ShareGPT_V3_format_5convs.json\", \"data_count\": 5, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"data/ShareGPT_V3_format_5convs.json\", \"checkpoint_path\": \"checkpoints/tg_v7_s42/final\", \"wall_clock_seconds\": 8551.2, \"gpu_hours\": 2.38}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T09:29:58.880Z\", \"metrics\": {\"beta_0.0\": {\"mid_turns_avg_gar\": 0.028, \"avg_ppl\": 1.409}, \"beta_0.5\": {\"mid_turns_avg_gar\": 0.0287, \"avg_ppl\": 1.387}, \"beta_1.0\": {\"mid_turns_avg_gar\": 0.0349, \"avg_ppl\": 1.36}, \"beta_2.0\": {\"mid_turns_avg_gar\": 0.062, \"avg_ppl\": 1.411}, \"beta_5.0\": {\"mid_turns_avg_gar\": 0.6795, \"avg_ppl\": 1.908}, \"beta_10.0\": {\"mid_turns_avg_gar\": 0.959, \"avg_ppl\": 4.22}, \"phase_transition_range\": \"[2, 5]\", \"baseline_gar\": 0.028, \"max_gar_at_acceptable_ppl\": 0.6795, \"max_gar_at_acceptable_ppl_beta\": 5}, \"notes\": \"Attention steering 闭合因果环。β=0→2: GAR 缓升 (0.028→0.062), PPL 不变 (~1.4); β=5: phase transition, GAR 跳至 0.68, PPL 升至 1.91; β=10: GAR 饱和 0.96, PPL 恶化 4.22。成功标准 (GAR>0.1 且 PPL 不严重恶化) 在 β=2 即满足。β∈[2,5] 存在 phase transition。证明：手动修正 attention 指向 goal tokens → 直接恢复 GAR → 确认 exposure bias 通过 attention 偏移导致 GAR 坍塌。\"}, \"phase2_tg_s42_v8b_ss_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T02:28:58.064Z\", \"updated_at\": \"2026-05-20T09:30:04.080Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"133321\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v8b_ss_fixed.log\", \"submitted_at\": \"2026-05-20T02:28:58.001Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_v8b_ss_fixed_s42\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 24818.0, \"gpu_hours\": 6.89}, \"hypothesis\": \"Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。\", \"parent\": \"phase2_tg_s42_v7\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 448.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 247.19 MiB is free. Including non-PyTorch memory, this process has 50.68 GiB memory in use. Process 157667 has 26.76 GiB memory in use. Process 158713 \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T09:22:35.962Z\", \"notes\": \"CUDA OOM at Epoch 1 Step 4300 (loss.backward). 其他进程共享 GPU 导致显存不足: Process 157667 (26.76GB) + Process 158713 (17.28GB) + PyTorch 自身 45.21GB + 4.81GB reserved > 94.97GB 总容量。训练在 OOM 前正常收敛 (SS ratio=0.5, Loss~1.0, Gate~0.94)。有 epoch_0 checkpoint。需要独占 GPU 重跑。\"}, \"phase2_tg_s42_v7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:17:45.739Z\", \"updated_at\": \"2026-05-20T03:04:19.923Z\", \"hypothesis\": \"MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。\", \"parent\": \"phase2_tg_s42_v6\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5035, \"eval_iid_dongre_mid_gar\": 0.0152, \"eval_iid_ppl\": 2.784, \"eval_heldout_ours_mid_gar\": 0.5035, \"eval_heldout_dongre_mid_gar\": 0.0152, \"eval_heldout_ppl\": 2.78, \"eval_modelgen_ours_mid_gar\": 0.0157, \"eval_modelgen_dongre_mid_gar\": 0.0194, \"eval_modelgen_ppl\": 1.36, \"gate_mean_final\": 0.9336, \"gate_std_final\": 0.0492}, \"spec\": {\"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v7 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\\\"\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v7\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v7.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T00:48:47.275Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T00:48:47.463Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T00:48:48.850580+00:00\"}]}, \"notes\": \"训练 3 epoch 完成 (21352s/5.9h)。最终 gate: mean=0.9336, std=0.0492, L3=0.801 L4=0.789 最低。Eval 完成：GAR-ours recovery +0.35pp (mid 0.0157 vs baseline 0.0122), GAR-Dongre recovery +0.72pp (mid 0.0194 vs baseline 0.0122)。Gate dynamic range 最大层: L23 diff=-0.2100, L14 diff=-0.1803。\"}, \"phase2_tg_s42_v9_pcgrad\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-19T16:13:21.907Z\", \"updated_at\": \"2026-05-20T03:04:17.171Z\", \"hypothesis\": \"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v9_pcgrad.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v9_pcgrad_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"83860\", \"log_path\": \"/root/turn_residual_gating/logs/phase2_tg_v9_pcgrad_s42.log\", \"submitted_at\": \"2026-05-19T17:42:10.820Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_v9_pcgrad_s42\", \"wall_clock_seconds\": 30601.5, \"gpu_hours\": 8.5}, \"reproduce\": {\"finished_at\": \"2026-05-20T01:42:12.536Z\"}, \"failure_reason\": null, \"conclusion\": \"success\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T17:35:39.776243+00:00\", \"note\": \"第1次提交 EXIT_CODE=2 残留事件\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T01:42:14.275822+00:00\"}]}, \"completed_at\": null, \"notes\": \"D028 因果排除确认（M017 修正后）。训练: EXIT_CODE=0, 7.98h, 3 epochs。PCGrad cos_sim 从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350 step 高原期后仍坍塌到≈0。IID eval (同 protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, 无改善)。Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50。结论: PCGrad 消除梯度方向冲突后所有 IID 指标均 ≈ v7（GAR、PPL、NTP 无变化），方向冲突因 NTP 幅度主导 (10-40x) 而 inconsequential。Exposure bias 是 30x gap 根因。\", \"metrics\": {\"eval_iid_ours_mid_gar\": 0.5002, \"eval_iid_dongre_mid_gar\": 0.0123, \"eval_iid_ppl\": 2.78, \"eval_iid_ntp\": 0.9752, \"eval_heldout_ours_mid_gar\": 0.5002, \"eval_heldout_dongre_mid_gar\": 0.0123, \"eval_heldout_ppl\": 2.78, \"eval_heldout_ntp\": 0.9752, \"eval_modelgen_ours_mid_gar\": 0.0151, \"eval_modelgen_dongre_mid_gar\": 0.0173, \"eval_modelgen_ppl\": 1.5, \"vs_v7_iid_ppl_diff\": 0.004, \"vs_v7_iid_gar_diff\": -0.0033}}, \"phase2_lora_only_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-18T20:36:32.506Z\", \"updated_at\": \"2026-05-20T02:15:18.992Z\", \"hypothesis\": \"LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。\", \"parent\": \"phase2_tg_s42_v7\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-19T12:44:29.475Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:04:35.644174+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type lora_only --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 0.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_lora_only_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\\\"\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_lora_only_s42\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_lora_only_s42.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:04:33.523Z\"}, \"conclusion\": \"success\", \"metrics\": {\"epochs_completed\": 3, \"global_steps\": 3000, \"training_time_seconds\": 20588.6, \"training_time_hours\": 5.7, \"gate_fixed\": 1, \"gate_type_actual\": \"none\", \"final_lora_size_mb\": 20, \"eval_modelgen_ours_mid_gar\": 0.0245, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.371}, \"checkpoint_path\": \"/root/runs/turn_residual_gating/runs/phase2_lora_only_s42/lora/\", \"log_path\": \"/root/runs/turn_residual_gating/phase2_lora_only_s42.log\", \"notes\": \"诊断确认：EXIT_CODE=1 因 argparse 不认 lora_only 选项（choices 只有 threadgate/uniform/none）。训练实际已用 --gate-type none 完成 3 epoch (3000 steps, 20588.6s/5.7h)。Gate 全程固定 1.0（符合 lora_only 语义）。Checkpoint 可用，无需重跑。修复：dispatch 命令改用 --gate-type none 或在 train_phase2.py 添加 lora_only choice。\"}, \"phase2_ug_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:04:17.643Z\", \"updated_at\": \"2026-05-20T02:15:15.775Z\", \"hypothesis\": \"Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.\", \"parent\": \"phase1_gar_diag\", \"notes\": \"3 epoch 完成 (21994.5s/6.1h)。最终 gate: mean=0.9598, std=0.0518, L3=0.777 L5=0.812 最低。重要发现：uniform gate 模式下各层仍学出 per-layer 分化（L3=0.777 vs L27=1.000），与 ThreadGate v7 的 L3/L4 最低模式一致。这说明 per-layer variation 可能来自 LoRA+GAR loss 而非 gate architecture。\", \"spec\": {\"command\": \"python src/train_phase2.py --gate-type uniform --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_ug_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_ug_s42\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_ug_s42.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T06:53:13.931Z\", \"metrics\": {\"epoch0_avg_loss\": 1.0019, \"epoch0_avg_ntp\": 0.9755, \"epoch0_avg_gar\": 0.0259, \"epoch0_avg_div\": 0.0005, \"epoch1_avg_loss\": 0.9447, \"epoch1_avg_ntp\": 0.9435, \"epoch1_avg_gar\": 0.0013, \"epoch1_avg_div\": 0, \"epoch2_avg_loss\": 0.9319, \"epoch2_avg_ntp\": 0.9309, \"epoch2_avg_gar\": 0.001, \"epoch2_avg_div\": 0, \"final_gate_mean\": 0.9598, \"final_gate_std\": 0.0518, \"final_gate_min\": 0.7773, \"final_gate_max\": 1, \"final_profile_L3\": 0.777, \"final_profile_L5\": 0.812, \"final_profile_L0\": 0.875, \"final_profile_L27\": 1, \"training_time_seconds\": 21994.5, \"training_time_hours\": 6.1, \"global_steps\": 7950, \"unexpected_per_layer_variation\": true, \"eval_modelgen_ours_mid_gar\": 0.0149, \"eval_modelgen_dongre_mid_gar\": 0.0185, \"eval_modelgen_ppl\": 1.396}, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_ug_s42\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_ug_s42.log\"}, \"phase2_tg_s42_v8_schedsampling\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:02:00.223Z\", \"updated_at\": \"2026-05-19T16:33:04.989Z\", \"hypothesis\": \"Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"python src/train_phase2_v8.py --scheduled-sampling --ss-max-ratio 0.5\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": 73838, \"log_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v8_schedsampling/\", \"submitted_at\": \"2026-05-19T15:43:01.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (training from scratch with LoRA)\", \"eval_data\": \"ultrachat_eval_heldout.json (post-training eval)\", \"hyperparams\": {\"lr\": 0.0002, \"epochs\": 3, \"grad_accum\": 8, \"ss_max_ratio\": 0.5, \"ss_gen_max_tokens\": 256, \"ss_gen_temperature\": 0.7}, \"estimated_hours\": \"8-9\", \"checkpoint_path\": \"N/A (crashed at 5.8%)\", \"wall_clock_seconds\": 1611.0, \"gpu_hours\": 0.45}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T16:09:52.423Z\", \"metrics\": {\"killed_at_microstep\": 1950, \"total_microsteps\": 24000, \"completion_pct\": 8.1, \"global_step_approx\": 244, \"total_global_steps\": 3000, \"ss_steps_observed\": 1, \"tf_lgar_mean_step850_1400\": 0.0062, \"tf_lgar_std\": 0.0082, \"tf_lgar_collapse_step\": 800, \"gate_mean_final\": 0.93, \"ss_ratio_at_kill\": 0.081, \"crash_reason\": \"killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad\", \"design_flaw_ss_ramp_too_slow\": true, \"design_flaw_no_ss_tf_separate_logging\": true}, \"notes\": \"Director kill at micro-step ~1950 (8.1%). 原因: SS path code bug (D026) + GAR-ours 无推理 gap (D024)，实验无效。GPU 转入 plan_018 PCGrad。详情：(1) SS ratio 仅 0.081 时 kill，仅 1 条 SS step 被日志捕获，(2) TF L_GAR 在 step 800 坍塌到 ≈0.006（与 v7 一致），(3) GAR-ours 推理时 ≈0.50 ≈ target，SS 用 GAR-ours 训练无法验证 exposure bias mitigation，(4) lambda_gar=2.0 (vs v7 的 1.0) confound 未被充分触发。\"}, \"analysis_attention_heatmap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:03:16.154Z\", \"updated_at\": \"2026-05-19T15:22:24.770Z\", \"hypothesis\": \"四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"attention heatmap analysis script\", \"server\": \"westd-20861\", \"data_path\": \"standard_conversations.json\", \"data_count\": 5, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42\", \"eval_data\": \"standard_conversations.json (5 convs x 10 turns)\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"westd-20861:/root/turn_residual_gating/runs/analysis/\"}, \"conclusion\": \"success\", \"metrics\": {\"base_mean_goal_attn\": 0.0136, \"base_decay\": 0.875, \"tg_mean_goal_attn\": 0.0232, \"tg_decay\": 0.777, \"ug_mean_goal_attn\": 0.0216, \"ug_decay\": 0.803, \"lora_mean_goal_attn\": 0.0216, \"lora_decay\": 0.81, \"gating_incremental_benefit\": \"none\"}, \"completed_at\": \"2026-05-19T15:22:24.770Z\"}, \"analysis_gradient_conflict\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:03:12.230Z\", \"updated_at\": \"2026-05-19T15:22:23.782Z\", \"hypothesis\": \"NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"gradient conflict analysis script\", \"server\": \"westd-20861\", \"data_path\": \"v7 epoch 0/1/2 checkpoints\", \"data_count\": 3, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7\", \"eval_data\": \"v7 3-epoch checkpoints (gradient analysis)\", \"checkpoint_path\": \"N/A (analysis)\", \"log_path\": \"westd-20861:/root/turn_residual_gating/runs/analysis/\"}, \"conclusion\": \"success\", \"metrics\": {\"epoch0_cos_sim\": -0.089, \"epoch1_cos_sim\": -0.054, \"epoch2_cos_sim\": -0.042, \"epoch0_neg_layers_pct\": 78.6, \"epoch1_neg_layers_pct\": 71.4, \"epoch2_neg_layers_pct\": 67.9, \"epoch0_mag_ratio\": 7.5, \"epoch1_mag_ratio\": 13.7, \"epoch2_mag_ratio\": 14.7}, \"completed_at\": \"2026-05-19T15:22:23.782Z\"}, \"phase2_4way_eval_heldout\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:58:59.269Z\", \"updated_at\": \"2026-05-19T14:35:47.201Z\", \"hypothesis\": \"四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。\", \"parent\": \"phase2_4way_eval\", \"spec\": {\"command\": \"bash -c \\\"cd /root/turn_residual_gating && bash scripts/run_4way_eval_heldout.sh\\\"\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": 67204, \"log_path\": \"~/runs/turn_residual_gating/phase2_4way_eval_heldout.log\", \"submitted_at\": \"2026-05-19T14:01:00.965Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_eval_heldout.json\", \"data_count\": 50, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42\", \"eval_data\": \"ultrachat_eval_heldout.json (50 convs, idx 8843-68199, no overlap with training 0-7999)\", \"configs\": \"4 models (Base/TG_v7/UG/LoRA-only) x 2 GAR variants (ours/Dongre) = 8 eval runs\", \"checkpoint_path\": \"N/A (eval-only)\", \"wall_clock_seconds\": 2086.2, \"gpu_hours\": 0.58}, \"reproduce\": {\"finished_at\": \"2026-05-19T14:32:09.481Z\"}, \"metrics\": {\"base_ours_mid_gar\": 0.0128, \"base_ours_recovery_pp\": 0.06, \"base_dongre_mid_gar\": 0.0031, \"base_dongre_recovery_pp\": -0.91, \"base_ppl\": 4.34, \"base_ntp\": 1.4045, \"tg_ours_mid_gar\": 0.5035, \"tg_ours_recovery_pp\": 49.13, \"tg_dongre_mid_gar\": 0.0152, \"tg_dongre_recovery_pp\": 0.3, \"tg_ppl\": 2.78, \"tg_ntp\": 0.9771, \"ug_ours_mid_gar\": 0.5053, \"ug_ours_recovery_pp\": 49.31, \"ug_dongre_mid_gar\": 0.0124, \"ug_dongre_recovery_pp\": 0.02, \"ug_ppl\": 2.78, \"ug_ntp\": 0.9752, \"lora_ours_mid_gar\": 0.4978, \"lora_ours_recovery_pp\": 48.56, \"lora_dongre_mid_gar\": 0.0132, \"lora_dongre_recovery_pp\": 0.1, \"lora_ppl\": 2.78, \"lora_ntp\": 0.9771, \"three_way_convergence_confirmed\": true, \"gar_ours_spread_pp\": 0.75, \"ppl_spread\": 0, \"data_overlap\": false}, \"conclusion\": \"success\", \"notes\": \"Held-out eval 三路趋同完全复现。TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL 均为 2.78。与 overlap 数据相比绝对值略高（GAR +1-2pp, PPL +0.15），属正常泛化偏移，相对比较完全一致。数据完整性 confound 已排除。\", \"completed_at\": \"2026-05-19T14:35:47.202Z\"}, \"phase2_4way_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:07:30.673Z\", \"updated_at\": \"2026-05-19T13:15:39.947Z\", \"hypothesis\": \"Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/run_4way_eval.sh 2>&1 | tee runs/4way_eval.log\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"60024\", \"log_path\": \"/root/turn_residual_gating/runs/4way_eval.log\", \"submitted_at\": \"2026-05-19T13:07:37.380Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42\", \"eval_data\": \"ultrachat_8k eval split\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/4way_eval/\", \"wall_clock_seconds\": 447.0, \"gpu_hours\": 0.12}, \"parent\": \"phase2_tg_s42_v7\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-19T13:15:04.405Z\", \"metrics\": {\"base_ours_mid_gar\": 0.0107, \"base_ours_recovery_pp\": -0.15, \"base_dongre_mid_gar\": 0.003, \"base_dongre_recovery_pp\": -0.92, \"base_ppl\": 4.23, \"base_ntp\": 1.4162, \"tg_ours_mid_gar\": 0.4866, \"tg_ours_recovery_pp\": 47.44, \"tg_dongre_mid_gar\": 0.0157, \"tg_dongre_recovery_pp\": 0.35, \"tg_ppl\": 2.63, \"tg_ntp\": 0.9484, \"ug_ours_mid_gar\": 0.4923, \"ug_ours_recovery_pp\": 48.01, \"ug_dongre_mid_gar\": 0.013, \"ug_dongre_recovery_pp\": 0.08, \"ug_ppl\": 2.62, \"ug_ntp\": 0.9433, \"lora_ours_mid_gar\": 0.486, \"lora_ours_recovery_pp\": 47.39, \"lora_dongre_mid_gar\": 0.0137, \"lora_dongre_recovery_pp\": 0.15, \"lora_ppl\": 2.63, \"lora_ntp\": 0.9482, \"route_b_confirmed\": true, \"gating_incremental_benefit\": \"none\"}, \"notes\": \"四路 eval 完成，Route B 决定性确认。三种训练方法（TG/UG/LoRA-only）在推理端完全趋同：ours GAR recovery ~47-48pp（vs base -0.15pp），dongre GAR recovery 0.08-0.35pp，PPL 2.62-2.63，NTP 0.943-0.948。Gating 机制（无论 turn-conditioned 还是 uniform）相比纯 LoRA 微调零增量。LoRA fine-tuning 是 GAR recovery 的唯一来源。hypothesis 被证伪：TRG 不比 LoRA-only 更好。\"}, \"phase2_tg_s42_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:10:23.229Z\", \"updated_at\": \"2026-05-18T17:52:54.605Z\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"parent\": \"phase2_tg_s42_v4\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v5 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\\\"\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": \"3639\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v5.log\", \"submitted_at\": \"2026-05-18T17:10:30.573Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v5\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"wall_clock_seconds\": 2539.4, \"gpu_hours\": 0.71}, \"metrics\": {\"step2000_gate_std\": 0.0225, \"step2000_gate_mean\": 0.9586, \"step2000_gate_min\": 0.9062, \"step2000_gate_max\": 0.9961, \"step2000_L_GAR\": -0.8977, \"step2000_L_NTP\": 0.7611, \"step2000_total_loss\": -0.1365, \"step2400_gate_std\": 0.0219, \"step2400_gate_mean\": 0.9651, \"step2400_gate_min\": 0.918, \"step2400_gate_max\": 0.9961, \"step2400_profile\": \"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\", \"L_GAR_saturated_at\": -0.91, \"gate_range_compression\": \"0.918-0.996\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T17:52:49.951Z\", \"notes\": \"maximize 模式 gate 分化失败：gate_std=0.022↓ gate_mean=0.965↑，与 v3/v3b 同类结构性问题。L_GAR 饱和在 -0.91，maximize 的无界性驱动 gate 趋向恒等（全通过=最大 GAR），丧失层选择性。D009 指令立即 kill，转 v6 smooth_saturation。\"}, \"phase2_tg_s42_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:58:00.124Z\", \"updated_at\": \"2026-05-18T16:50:36.202Z\", \"hypothesis\": \"重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值\", \"parent\": \"phase2_tg_s42_v3b\", \"spec\": {\"command\": \"python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v4 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"pid\": \"36519\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v4\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v4.log\", \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-18T16:50:33.778Z\", \"notes\": \"进程在模型加载后崩溃，服务器重启导致进程丢失，无 checkpoint。日志仅有模型加载输出，无训练 step。GPU 重启后异常（100% util + 0 MiB + 无进程）。需要 GPU 健康恢复后重跑。\"}, \"phase2_tg_s42_v3b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:38:16.020Z\", \"updated_at\": \"2026-05-18T14:51:42.486Z\", \"hypothesis\": \"λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot\", \"parent\": \"phase2_tg_s42_v3\", \"spec\": {\"command\": \"python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 10.0 --init-bias 0.0 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3b --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-steps 500\", \"server\": \"westd-20861\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"from_scratch\", \"eval_data\": \"N/A\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v3b\", \"log_path\": \"/root/turn_residual_gating/runs/v3b_log.txt\"}, \"conclusion\": \"success\", \"metrics\": {\"gate_std_final\": 0.087, \"gate_mean_final\": 0.9388, \"gate_min_final\": 0.5352, \"gate_max_final\": 0.9922, \"L4_gate\": 0.535, \"L0_gate\": 0.777, \"L_NTP_final\": 0.7787, \"L_GAR_final\": -0.9606, \"elapsed_seconds\": 3565.9, \"optimizer_steps\": 500, \"gate_grad_received\": true}, \"completed_at\": \"2026-05-18T14:51:42.486Z\"}, \"phase2_tg_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:07:54.463Z\", \"updated_at\": \"2026-05-18T13:38:10.723Z\", \"hypothesis\": \"ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛\", \"parent\": \"phase2_tg_s42_v2\", \"spec\": {\"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"data_path\": \"/root/turn_residual_gating/data/ultrachat_8k\", \"data_count\": 8000, \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"seed\": 42, \"command\": \"python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 2.0 --init-bias 2.0 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3 --data-dir /root/turn_residual_gating/data/ultrachat_8k\", \"pid\": \"30973\", \"log_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v3.log\", \"checkpoint_source\": \"N/A (training from scratch with LoRA)\", \"eval_data\": \"N/A (training experiment, not eval)\", \"checkpoint_path\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v3\"}, \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"conclusion\": \"negative\", \"metrics\": {\"gate_mean_step0\": 0.8743, \"gate_mean_step500\": 0.8761, \"gate_delta\": 0.004, \"gate_std\": 0.001, \"final_ntp_loss\": 0.94, \"final_gar_loss\": -0.019, \"gar_contribution_pct\": \"2-4%\", \"diagnosis\": \"gate frozen, GAR indirect gradient too weak\"}, \"completed_at\": \"2026-05-18T13:38:10.723Z\"}, \"phase2_tg_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:13:37.042Z\", \"updated_at\": \"2026-05-18T13:11:26.331Z\", \"hypothesis\": \"ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性\", \"parent\": \"phase2_tg_s42\", \"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-20861\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T11:45:26.657Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"25726\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v2.log\", \"submitted_at\": \"2026-05-18T11:50:47.143Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/turn_residual_gating/checkpoints/tg_s42_v2\", \"wall_clock_seconds\": 4839.2, \"gpu_hours\": 1.34}, \"pid\": \"25726\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v2.log\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T13:11:26.331Z\"}, \"phase1_gar_diag\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T05:24:07.903Z\", \"updated_at\": \"2026-05-18T05:59:25.324Z\", \"hypothesis\": \"Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减\", \"spec\": {\"command\": \"python run_phase1_gar.py --results-dir /root/turn_residual_gating/results\", \"server\": \"westd-20861\", \"model_name\": \"Qwen/Qwen2.5-7B-Instruct\", \"data_path\": \"built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, roleplay_advisor)\", \"data_count\": 5, \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/turn_residual_gating/results/phase1_run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"turn1_avg_gar\": 0.0418, \"mid_turns_avg_gar\": 0.0122, \"relative_drop\": 0.708, \"num_conversations\": 5, \"num_turns\": 10, \"per_turn_avg_gar\": [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]}, \"completed_at\": \"2026-05-18T05:59:25.325Z\"}}, \"count\": 60, \"total\": 60, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1953}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01DyNexVAYHhc3MUD4eVTAGa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig1_3panel.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "89ff00bb-e1ac-4a97-823a-a070a9fc99e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 31 · 2026-05-25T20:12:24.854Z_

<details><summary>↩ Tool result · `toolu_01DyNexVAYHhc3MUD4eVTAGa`</summary>

```text
1	"""Figure 1: 3-panel headline figure — Discovery → Diagnosis → Fix.
2	
3	(a) Per-turn GAR decay under AR generation (both models)
4	(b) TF vs AR GAR gap across 5 training configs
5	(c) SS gap compression (before/after)
6	"""
7	import sys
8	sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
9	from palette import *
10	import matplotlib.patheffects as pe
11	import matplotlib.ticker as ticker
12	import matplotlib.gridspec as gridspec
13	import numpy as np
14	
15	apply_style()
16	
17	fig = plt.figure(figsize=(7.2, 2.5))
18	gs = gridspec.GridSpec(2, 2, figure=fig, width_ratios=[1.0, 1.15],
19	                       height_ratios=[1.0, 0.85], hspace=0.65, wspace=0.40)
20	
21	ax_a = fig.add_subplot(gs[:, 0])
22	ax_b = fig.add_subplot(gs[0, 1])
23	ax_c = fig.add_subplot(gs[1, 1])
24	
25	stroke = [pe.withStroke(linewidth=2.2, foreground='white')]
26	
27	# ══════════════════════════════════════════════════════════════════
28	# Panel (a): Per-turn GAR decay under AR generation
29	# ══════════════════════════════════════════════════════════════════
30	turns = np.arange(1, 11)
31	
32	qwen_base = np.array([0.0418, 0.0241, 0.0224, 0.013, 0.0133,
33	                       0.0086, 0.0078, 0.008, 0.0157, 0.0064])
34	llama_base = np.array([0.0263, 0.0183, 0.0087, 0.0055, 0.006,
35	                        0.0035, 0.0038, 0.0037, 0.005, 0.0026])
36	
37	ax_a.plot(turns, qwen_base * 100, 'o-', color=C_TG, markersize=3.5,
38	          markeredgecolor='white', markeredgewidth=0.4,
39	          label='Qwen-2.5-7B', zorder=3, linewidth=1.2)
40	ax_a.plot(turns, llama_base * 100, 's-', color=C_GREEN, markersize=3.5,
41	          markeredgecolor='white', markeredgewidth=0.4,
42	          label='Llama-3.1-8B', zorder=3, linewidth=1.2)
43	
44	ax_a.fill_between(turns, 0, qwen_base * 100, alpha=0.06, color=C_TG)
45	ax_a.fill_between(turns, 0, llama_base * 100, alpha=0.06, color=C_GREEN)
46	
47	t = ax_a.text(7.5, 3.5, '85–90%\ndecay', fontsize=6, color='#666666',
48	              ha='center', va='center', fontstyle='italic')
49	t.set_path_effects(stroke)
50	
51	ax_a.set_xlabel('Turn index')
52	ax_a.set_ylabel('GAR (%)')
53	ax_a.set_xticks([1, 3, 5, 7, 9])
54	ax_a.set_xlim(0.5, 10.5)
55	ax_a.set_ylim(0, 5.0)
56	ax_a.legend(loc='upper right', fontsize=6, handlelength=1.2,
57	            handletextpad=0.3, borderpad=0.2)
58	ax_a.set_title('(a) GAR decays with turn depth',
59	               fontsize=8, pad=6, loc='left', fontweight='medium')
60	
61	# ══════════════════════════════════════════════════════════════════
62	# Panel (b): TF vs AR GAR gap — 5 configs
63	# ══════════════════════════════════════════════════════════════════
64	configs = ['Base', 'TG', '+PCGrad', 'UG', 'LoRA']
65	config_colors = [C_BASE, C_TG, C_PC, C_UG, C_LO]
66	tf_gar  = [0.01, 0.50, 0.50, 0.49, 0.50]
67	ar_gar  = [0.019, 0.064, 0.030, 0.033, 0.037]
68	gaps    = [None, 7.8, 16.7, 14.8, 13.5]
69	
70	x = np.arange(len(configs))
71	w = 0.28
72	
73	bars_tf = ax_b.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced',
74	                   zorder=2, edgecolor='white', linewidth=0.3)
75	bars_ar = ax_b.bar(x + w/2, ar_gar, w, color=C_SS, label='Autoregressive',
76	                   zorder=2, edgecolor='white', linewidth=0.3)
77	
78	ax_b.set_yscale('log')
79	ax_b.set_ylim(0.004, 1.5)
80	ax_b.set_xlim(-0.55, 4.65)
81	
82	ax_b.axhspan(0.005, 0.05, color='#FFF3E0', alpha=0.12, zorder=0)
83	ax_b.axhspan(0.05, 1.5, color='#E8F5E9', alpha=0.12, zorder=0)
84	
85	for i in range(1, len(configs)):
86	    ax_b.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],
87	              color='#CCCCCC', linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))
88	
89	for i, gap in enumerate(gaps):
90	    if gap is not None:
91	        geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])
92	        t = ax_b.text(x[i] + w/2 + 0.12, geo_mean, f'{gap:.0f}×',
93	                      fontsize=7, fontweight='bold', color=C_AR_DARK,
94	                      ha='left', va='center')
95	        t.set_path_effects(stroke)
96	
97	ax_b.set_xticks(x)
98	ax_b.set_xticklabels(configs, fontsize=7)
99	ax_b.set_ylabel('GAR (log scale)')
100	ax_b.legend(loc='upper center', fontsize=5.5, handlelength=0.8,
101	            handletextpad=0.3, borderpad=0.15, ncol=2,
102	            bbox_to_anchor=(0.42, 1.12), columnspacing=0.8)
103	ax_b.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
104	ax_b.set_title('(b) 8–17× TF/AR gap persists',
105	               fontsize=8, pad=6, loc='left', fontweight='medium')
106	
107	# ══════════════════════════════════════════════════════════════════
108	# Panel (c): SS gap compression — before/after
109	# ══════════════════════════════════════════════════════════════════
110	labels_c = ['Qwen TG', 'Qwen SS', 'Llama TG', 'Llama SS']
111	gaps_c   = [7.8, 1.3, 12.5, 2.9]
112	colors_c = [C_TEAL, C_GOLD, C_TEAL, C_GOLD]
113	alphas_c = [0.55, 1.0, 0.55, 1.0]
114	
115	y = np.arange(len(labels_c))
116	
117	for i, (lbl, gap, col) in enumerate(zip(labels_c, gaps_c, colors_c)):
118	    ax_c.barh(i, gap, height=0.55, color=col, alpha=alphas_c[i],
119	              edgecolor='white', linewidth=0.3, zorder=2)
120	    is_ss = 'SS' in lbl
121	    txt_offset = 0.25
122	    ax_c.text(gap + txt_offset, i, f'{gap:.1f}×', va='center', ha='left',
123	              fontsize=6.5, fontweight='bold' if is_ss else 'normal',
124	              color=col if is_ss else '#777777',
125	              path_effects=stroke if is_ss else [], zorder=5)
126	
127	ax_c.axvline(1.0, color=C_GRAY, linestyle='--', linewidth=0.6, zorder=1, alpha=0.5)
128	
129	ax_c.axhline(1.5, color='#DDDDDD', linewidth=0.4, linestyle='-', zorder=0)
130	
131	# Compression arrows — straight vertical at midpoint of SS bar
132	for pair_start, pair_end in [(0, 1), (2, 3)]:
133	    arrow_x = gaps_c[pair_end] * 0.45
134	    ax_c.annotate('',
135	                  xy=(arrow_x, pair_end + 0.3),
136	                  xytext=(arrow_x, pair_start - 0.3),
137	                  arrowprops=dict(arrowstyle='-|>', color='#888888',
138	                                  lw=1.0, mutation_scale=6,
139	                                  shrinkA=0, shrinkB=0),
140	                  zorder=3)
141	
142	ax_c.set_yticks(y)
143	ax_c.set_yticklabels(labels_c, fontsize=6.5)
144	ax_c.set_xlabel('TF/AR gap ratio')
145	ax_c.set_xlim(0, 14.5)
146	ax_c.invert_yaxis()
147	ax_c.set_title('(c) SS compresses the gap',
148	               fontsize=8, pad=6, loc='left', fontweight='medium')
149	
150	save_fig(fig, 'fig1_headline')
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "08dd5c10-0a9d-4a3d-8a72-f3ad9f921642",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig1_3panel.py",
      "content": "\"\"\"Figure 1: 3-panel headline figure — Discovery → Diagnosis → Fix.\n\n(a) Per-turn GAR decay under AR generation (both models)\n(b) TF vs AR GAR gap across 5 training configs\n(c) SS gap compression (before/after)\n\"\"\"\nimport sys\nsys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')\nfrom palette import *\nimport matplotlib.patheffects as pe\nimport matplotlib.ticker as ticker\nimport matplotlib.gridspec as gridspec\nimport numpy as np\n\napply_style()\n\nfig = plt.figure(figsize=(7.2, 2.5))\ngs = gridspec.GridSpec(2, 2, figure=fig, width_ratios=[1.0, 1.15],\n                       height_ratios=[1.0, 0.85], hspace=0.65, wspace=0.40)\n\nax_a = fig.add_subplot(gs[:, 0])\nax_b = fig.add_subplot(gs[0, 1])\nax_c = fig.add_subplot(gs[1, 1])\n\nstroke = [pe.withStroke(linewidth=2.2, foreground='white')]\n\n# ══════════════════════════════════════════════════════════════════\n# Panel (a): Per-turn GAR decay under AR generation\n# ══════════════════════════════════════════════════════════════════\nturns = np.arange(1, 11)\n\nqwen_base = np.array([0.0418, 0.0241, 0.0224, 0.013, 0.0133,\n                       0.0086, 0.0078, 0.008, 0.0157, 0.0064])\nllama_base = np.array([0.0263, 0.0183, 0.0087, 0.0055, 0.006,\n                        0.0035, 0.0038, 0.0037, 0.005, 0.0026])\n\nax_a.plot(turns, qwen_base * 100, 'o-', color=C_TG, markersize=3.5,\n          markeredgecolor='white', markeredgewidth=0.4,\n          label='Qwen-2.5-7B', zorder=3, linewidth=1.2)\nax_a.plot(turns, llama_base * 100, 's-', color=C_GREEN, markersize=3.5,\n          markeredgecolor='white', markeredgewidth=0.4,\n          label='Llama-3.1-8B', zorder=3, linewidth=1.2)\n\nax_a.fill_between(turns, 0, qwen_base * 100, alpha=0.06, color=C_TG)\nax_a.fill_between(turns, 0, llama_base * 100, alpha=0.06, color=C_GREEN)\n\nt = ax_a.text(7.5, 3.5, '85–90%\\ndecay', fontsize=6, color='#666666',\n              ha='center', va='center', fontstyle='italic')\nt.set_path_effects(stroke)\n\nax_a.set_xlabel('Turn index')\nax_a.set_ylabel('GAR (%)')\nax_a.set_xticks([1, 3, 5, 7, 9])\nax_a.set_xlim(0.5, 10.5)\nax_a.set_ylim(0, 5.0)\nax_a.legend(loc='upper right', fontsize=6, handlelength=1.2,\n            handletextpad=0.3, borderpad=0.2)\nax_a.set_title('(a) GAR decays with turn depth',\n               fontsize=8, pad=6, loc='left', fontweight='medium')\n\n# ══════════════════════════════════════════════════════════════════\n# Panel (b): TF vs AR GAR gap — 5 configs\n# ══════════════════════════════════════════════════════════════════\nconfigs = ['Base', 'TG', '+PCGrad', 'UG', 'LoRA']\nconfig_colors = [C_BASE, C_TG, C_PC, C_UG, C_LO]\ntf_gar  = [0.01, 0.50, 0.50, 0.49, 0.50]\nar_gar  = [0.019, 0.064, 0.030, 0.033, 0.037]\ngaps    = [None, 7.8, 16.7, 14.8, 13.5]\n\nx = np.arange(len(configs))\nw = 0.28\n\nbars_tf = ax_b.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced',\n                   zorder=2, edgecolor='white', linewidth=0.3)\nbars_ar = ax_b.bar(x + w/2, ar_gar, w, color=C_SS, label='Autoregressive',\n                   zorder=2, edgecolor='white', linewidth=0.3)\n\nax_b.set_yscale('log')\nax_b.set_ylim(0.004, 1.5)\nax_b.set_xlim(-0.55, 4.65)\n\nax_b.axhspan(0.005, 0.05, color='#FFF3E0', alpha=0.12, zorder=0)\nax_b.axhspan(0.05, 1.5, color='#E8F5E9', alpha=0.12, zorder=0)\n\nfor i in range(1, len(configs)):\n    ax_b.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],\n              color='#CCCCCC', linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))\n\nfor i, gap in enumerate(gaps):\n    if gap is not None:\n        geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])\n        t = ax_b.text(x[i] + w/2 + 0.12, geo_mean, f'{gap:.0f}×',\n                      fontsize=7, fontweight='bold', color=C_AR_DARK,\n                      ha='left', va='center')\n        t.set_path_effects(stroke)\n\nax_b.set_xticks(x)\nax_b.set_xticklabels(configs, fontsize=7)\nax_b.set_ylabel('GAR (log scale)')\nax_b.legend(loc='upper center', fontsize=5.5, handlelength=0.8,\n            handletextpad=0.3, borderpad=0.15, ncol=2,\n            bbox_to_anchor=(0.42, 1.12), columnspacing=0.8)\nax_b.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))\nax_b.set_title('(b) 8–17× TF/AR gap persists',\n               fontsize=8, pad=6, loc='left', fontweight='medium')\n\n# ══════════════════════════════════════════════════════════════════\n# Panel (c): SS gap compression — before/after\n# ══════════════════════════════════════════════════════════════════\nlabels_c = ['Qwen TG', 'Qwen SS', 'Llama TG', 'Llama SS']\ngaps_c   = [7.8, 1.3, 12.5, 2.9]\ncolors_c = [C_TEAL, C_GOLD, C_TEAL, C_GOLD]\nalphas_c = [0.55, 1.0, 0.55, 1.0]\n\ny = np.arange(len(labels_c))\n\nfor i, (lbl, gap, col) in enumerate(zip(labels_c, gaps_c, colors_c)):\n    ax_c.barh(i, gap, height=0.55, color=col, alpha=alphas_c[i],\n              edgecolor='white', linewidth=0.3, zorder=2)\n    is_ss = 'SS' in lbl\n    txt_offset = 0.25\n    ax_c.text(gap + txt_offset, i, f'{gap:.1f}×', va='center', ha='left',\n              fontsize=6.5, fontweight='bold' if is_ss else 'normal',\n              color=col if is_ss else '#777777',\n              path_effects=stroke if is_ss else [], zorder=5)\n\nax_c.axvline(1.0, color=C_GRAY, linestyle='--', linewidth=0.6, zorder=1, alpha=0.5)\n\nax_c.axhline(1.5, color='#DDDDDD', linewidth=0.4, linestyle='-', zorder=0)\n\n# Compression arrows — straight vertical at midpoint of SS bar\nfor pair_start, pair_end in [(0, 1), (2, 3)]:\n    arrow_x = gaps_c[pair_end] * 0.45\n    ax_c.annotate('',\n                  xy=(arrow_x, pair_end + 0.3),\n                  xytext=(arrow_x, pair_start - 0.3),\n                  arrowprops=dict(arrowstyle='-|>', color='#888888',\n                                  lw=1.0, mutation_scale=6,\n                                  shrinkA=0, shrinkB=0),\n                  zorder=3)\n\nax_c.set_yticks(y)\nax_c.set_yticklabels(labels_c, fontsize=6.5)\nax_c.set_xlabel('TF/AR gap ratio')\nax_c.set_xlim(0, 14.5)\nax_c.invert_yaxis()\nax_c.set_title('(c) SS compresses the gap',\n               fontsize=8, pad=6, loc='left', fontweight='medium')\n\nsave_fig(fig, 'fig1_headline')\n",
      "numLines": 151,
      "startLine": 1,
      "totalLines": 151
    }
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01AYW37swTFw8e4Hn8MesHhe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "846cd286-c24e-42fc-8fb7-af352e57d19d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 33 · 2026-05-25T20:12:25.309Z_

<details><summary>↩ Tool result · `toolu_01AYW37swTFw8e4Hn8MesHhe`</summary>

```text
1	from palette import *
2	import matplotlib.patheffects as pe
3	import numpy as np
4	
5	apply_style()
6	
7	# v7 data (micro-step -> global step)
8	v7_ms = np.array([
9	    0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
10	    600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100,
11	    1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600
12	])
13	v7_gs = v7_ms / 8.0
14	
15	v7_lgar = np.array([
16	    0.2342, 0.2349, 0.2337, 0.2277, 0.2348, 0.2314, 0.2263, 0.2298,
17	    0.2368, 0.2251, 0.2285, 0.2326, 0.2179, 0.2106, 0.1886, 0.1386,
18	    0.1237, 0.0788, 0.0676, 0.0549, 0.0454, 0.0398, 0.0328, 0.0044,
19	    0.0053, 0.0359, 0.0002, 0.0001, 0.0000, 0.0005, 0.0000, 0.0011,
20	    0.0004
21	])
22	v7_gar = 0.5 - np.sqrt(v7_lgar)
23	
24	v7_gs_ext = np.concatenate([v7_gs, np.arange(250, 1250, 50)])
25	v7_lgar_ext = np.concatenate([v7_lgar, np.full(20, 0.0005)])
26	
27	# v9 PCGrad data
28	v9_ms = np.array([
29	    0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
30	    600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100
31	])
32	v9_gs = v9_ms / 8.0
33	v9_lgar = np.array([
34	    0.2342, 0.2349, 0.2337, 0.2270, 0.2339, 0.2280, 0.2205, 0.2196,
35	    0.2090, 0.1675, 0.1760, 0.1673, 0.1244, 0.1102, 0.0939, 0.0737,
36	    0.0832, 0.0491, 0.0410, 0.0304, 0.0343, 0.0239, 0.0367
37	])
38	
39	fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 6.0),
40	                                  gridspec_kw={'hspace': 0.38})
41	
42	# ═══════════════════════════════════════════════════════════════════════
43	# Panel (a): Three-Phase GAR Convergence
44	# ═══════════════════════════════════════════════════════════════════════
45	BAND_A = (0, 75)
46	BAND_B = (75, 144)
47	BAND_C = (144, 260)
48	
49	ax_a.axvspan(*BAND_A, alpha=0.08, color=C_SKYBLUE, zorder=0)
50	ax_a.axvspan(*BAND_B, alpha=0.08, color=C_GOLD, zorder=0)
51	ax_a.axvspan(*BAND_C, alpha=0.08, color=C_GREEN, zorder=0)
52	
53	for bx in [BAND_A[1], BAND_B[1]]:
54	    ax_a.axvline(bx, color='#cccccc', linewidth=0.5, linestyle='-',
55	                 alpha=0.45, zorder=0)
56	
57	ax_a.text(37.5, 0.535, 'A', fontsize=11, color=C_TF_DARK, ha='center',
58	          va='bottom', fontweight='bold')
59	ax_a.text(109.5, 0.535, 'B', fontsize=11, color='#B89A5A', ha='center',
60	          va='bottom', fontweight='bold')
61	ax_a.text(200, 0.535, 'C', fontsize=11, color='#6AB06A', ha='center',
62	          va='bottom', fontweight='bold')
63	
64	ax_a.axhline(0.5, color=C_GRAY, linestyle='--', linewidth=0.9,
65	             alpha=0.6, zorder=1)
66	t_target = ax_a.text(255, 0.508, 'target = 0.5', fontsize=7,
67	                     color=C_GRAY, ha='right', va='bottom')
68	t_target.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
69	
70	ax_a.plot(v7_gs, v7_gar, color=C_TG, linewidth=2, zorder=3,
71	          solid_capstyle='round')
72	
73	ax_a.annotate('phase transition\n(gs 75)', xy=(75, 0.033),
74	              xytext=(30, 0.22), fontsize=7, color='#666666',
75	              ha='center', va='bottom',
76	              arrowprops=dict(arrowstyle='->', color=C_GRAY,
77	                              lw=0.8, connectionstyle='arc3,rad=-0.2'))
78	ax_a.annotate('target reached\n(gs 144)', xy=(144, 0.434),
79	              xytext=(210, 0.28), fontsize=7, color='#666666',
80	              ha='center', va='bottom',
81	              arrowprops=dict(arrowstyle='->', color=C_GRAY,
82	                              lw=0.8, connectionstyle='arc3,rad=0.2'))
83	
84	ax_a.set_xlim(-5, 260)
85	ax_a.set_ylim(-0.03, 0.58)
86	ax_a.set_xlabel('Global Step')
87	ax_a.set_ylabel('Training GAR')
88	ax_a.set_title('(a) Three-phase convergence to target',
89	               fontsize=9, pad=8, loc='left')
90	
91	ax_a.text(0.97, 0.38,
92	          'L$_{NTP}$: 2.03 → 0.93\n(normal convergence)',
93	          transform=ax_a.transAxes, fontsize=7, color='#777777',
94	          ha='right', va='top', fontstyle='italic',
95	          bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85, linewidth=0.6))
96	
97	# ═══════════════════════════════════════════════════════════════════════
98	# Panel (b): PCGrad vs v7 — Causal Exclusion
99	# ═══════════════════════════════════════════════════════════════════════
100	ax_b.plot(v7_gs_ext, v7_lgar_ext, color=C_TG, linewidth=1.8,
101	          label='v7 (baseline)', zorder=3, solid_capstyle='round')
102	ax_b.plot(v9_gs, v9_lgar, color=C_ROSE, linewidth=2.0,
103	          linestyle='--', label='v9 (PCGrad)', zorder=3,
104	          solid_capstyle='round')
105	
106	ax_b.axvline(200, color=C_UG, linestyle=':', linewidth=0.9,
107	             alpha=0.7, zorder=2)
108	t_cos = ax_b.text(193, 0.215, 'cos_sim > 0\n(gs ≈ 200)',
109	                  fontsize=6.5, color=C_UG, va='top', ha='right')
110	t_cos.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
111	
112	last_v9 = len(v9_gs) - 1
113	ax_b.plot(v9_gs[last_v9], v9_lgar[last_v9], 'o', color=C_ROSE,
114	          markersize=4.5, zorder=5, markeredgecolor='white', markeredgewidth=0.6)
115	ax_b.annotate('ongoing',
116	              xy=(v9_gs[last_v9], v9_lgar[last_v9]),
117	              xytext=(v9_gs[last_v9] + 15, v9_lgar[last_v9] + 0.01),
118	              fontsize=6.5, color=C_ROSE, ha='left', va='center',
119	              arrowprops=dict(arrowstyle='->', color=C_ROSE, lw=0.7,
120	                              connectionstyle='arc3,rad=-0.15'))
121	
122	ax_b.text(
123	    0.03, 0.30,
124	    'Conflict resolved,\nL$_{GAR}$ still collapses',
125	    transform=ax_b.transAxes, fontsize=7, color='#555555',
126	    ha='left', va='top', fontstyle='italic',
127	    bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF8E7',
128	              edgecolor=C_ROSE, alpha=0.9, linewidth=0.8)
129	)
130	
131	ax_b.legend(loc='upper right', borderpad=0.4, handlelength=1.8)
132	
133	ax_b.set_xlim(-5, 220)
134	ax_b.set_ylim(-0.008, 0.26)
135	ax_b.set_xlabel('Global Step')
136	ax_b.set_ylabel('L$_{GAR}$ (MSE loss)')
137	ax_b.set_title('(b) PCGrad cannot prevent L$_{GAR}$ collapse',
138	               fontsize=9, pad=8, loc='left')
139	
140	for ax in [ax_a, ax_b]:
141	    ax.grid(axis='y', alpha=0.10, linewidth=0.5, color='#888888')
142	
143	fig.subplots_adjust(hspace=0.38)
144	
145	save_fig(fig, 'fig2_training_pcgrad')
146	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "54e8fae7-4cd9-4af1-83f7-c5526930b05c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig2.py",
      "content": "from palette import *\nimport matplotlib.patheffects as pe\nimport numpy as np\n\napply_style()\n\n# v7 data (micro-step -> global step)\nv7_ms = np.array([\n    0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,\n    600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100,\n    1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600\n])\nv7_gs = v7_ms / 8.0\n\nv7_lgar = np.array([\n    0.2342, 0.2349, 0.2337, 0.2277, 0.2348, 0.2314, 0.2263, 0.2298,\n    0.2368, 0.2251, 0.2285, 0.2326, 0.2179, 0.2106, 0.1886, 0.1386,\n    0.1237, 0.0788, 0.0676, 0.0549, 0.0454, 0.0398, 0.0328, 0.0044,\n    0.0053, 0.0359, 0.0002, 0.0001, 0.0000, 0.0005, 0.0000, 0.0011,\n    0.0004\n])\nv7_gar = 0.5 - np.sqrt(v7_lgar)\n\nv7_gs_ext = np.concatenate([v7_gs, np.arange(250, 1250, 50)])\nv7_lgar_ext = np.concatenate([v7_lgar, np.full(20, 0.0005)])\n\n# v9 PCGrad data\nv9_ms = np.array([\n    0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,\n    600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100\n])\nv9_gs = v9_ms / 8.0\nv9_lgar = np.array([\n    0.2342, 0.2349, 0.2337, 0.2270, 0.2339, 0.2280, 0.2205, 0.2196,\n    0.2090, 0.1675, 0.1760, 0.1673, 0.1244, 0.1102, 0.0939, 0.0737,\n    0.0832, 0.0491, 0.0410, 0.0304, 0.0343, 0.0239, 0.0367\n])\n\nfig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 6.0),\n                                  gridspec_kw={'hspace': 0.38})\n\n# ═══════════════════════════════════════════════════════════════════════\n# Panel (a): Three-Phase GAR Convergence\n# ═══════════════════════════════════════════════════════════════════════\nBAND_A = (0, 75)\nBAND_B = (75, 144)\nBAND_C = (144, 260)\n\nax_a.axvspan(*BAND_A, alpha=0.08, color=C_SKYBLUE, zorder=0)\nax_a.axvspan(*BAND_B, alpha=0.08, color=C_GOLD, zorder=0)\nax_a.axvspan(*BAND_C, alpha=0.08, color=C_GREEN, zorder=0)\n\nfor bx in [BAND_A[1], BAND_B[1]]:\n    ax_a.axvline(bx, color='#cccccc', linewidth=0.5, linestyle='-',\n                 alpha=0.45, zorder=0)\n\nax_a.text(37.5, 0.535, 'A', fontsize=11, color=C_TF_DARK, ha='center',\n          va='bottom', fontweight='bold')\nax_a.text(109.5, 0.535, 'B', fontsize=11, color='#B89A5A', ha='center',\n          va='bottom', fontweight='bold')\nax_a.text(200, 0.535, 'C', fontsize=11, color='#6AB06A', ha='center',\n          va='bottom', fontweight='bold')\n\nax_a.axhline(0.5, color=C_GRAY, linestyle='--', linewidth=0.9,\n             alpha=0.6, zorder=1)\nt_target = ax_a.text(255, 0.508, 'target = 0.5', fontsize=7,\n                     color=C_GRAY, ha='right', va='bottom')\nt_target.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\nax_a.plot(v7_gs, v7_gar, color=C_TG, linewidth=2, zorder=3,\n          solid_capstyle='round')\n\nax_a.annotate('phase transition\\n(gs 75)', xy=(75, 0.033),\n              xytext=(30, 0.22), fontsize=7, color='#666666',\n              ha='center', va='bottom',\n              arrowprops=dict(arrowstyle='->', color=C_GRAY,\n                              lw=0.8, connectionstyle='arc3,rad=-0.2'))\nax_a.annotate('target reached\\n(gs 144)', xy=(144, 0.434),\n              xytext=(210, 0.28), fontsize=7, color='#666666',\n              ha='center', va='bottom',\n              arrowprops=dict(arrowstyle='->', color=C_GRAY,\n                              lw=0.8, connectionstyle='arc3,rad=0.2'))\n\nax_a.set_xlim(-5, 260)\nax_a.set_ylim(-0.03, 0.58)\nax_a.set_xlabel('Global Step')\nax_a.set_ylabel('Training GAR')\nax_a.set_title('(a) Three-phase convergence to target',\n               fontsize=9, pad=8, loc='left')\n\nax_a.text(0.97, 0.38,\n          'L$_{NTP}$: 2.03 → 0.93\\n(normal convergence)',\n          transform=ax_a.transAxes, fontsize=7, color='#777777',\n          ha='right', va='top', fontstyle='italic',\n          bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85, linewidth=0.6))\n\n# ═══════════════════════════════════════════════════════════════════════\n# Panel (b): PCGrad vs v7 — Causal Exclusion\n# ═══════════════════════════════════════════════════════════════════════\nax_b.plot(v7_gs_ext, v7_lgar_ext, color=C_TG, linewidth=1.8,\n          label='v7 (baseline)', zorder=3, solid_capstyle='round')\nax_b.plot(v9_gs, v9_lgar, color=C_ROSE, linewidth=2.0,\n          linestyle='--', label='v9 (PCGrad)', zorder=3,\n          solid_capstyle='round')\n\nax_b.axvline(200, color=C_UG, linestyle=':', linewidth=0.9,\n             alpha=0.7, zorder=2)\nt_cos = ax_b.text(193, 0.215, 'cos_sim > 0\\n(gs ≈ 200)',\n                  fontsize=6.5, color=C_UG, va='top', ha='right')\nt_cos.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\nlast_v9 = len(v9_gs) - 1\nax_b.plot(v9_gs[last_v9], v9_lgar[last_v9], 'o', color=C_ROSE,\n          markersize=4.5, zorder=5, markeredgecolor='white', markeredgewidth=0.6)\nax_b.annotate('ongoing',\n              xy=(v9_gs[last_v9], v9_lgar[last_v9]),\n              xytext=(v9_gs[last_v9] + 15, v9_lgar[last_v9] + 0.01),\n              fontsize=6.5, color=C_ROSE, ha='left', va='center',\n              arrowprops=dict(arrowstyle='->', color=C_ROSE, lw=0.7,\n                              connectionstyle='arc3,rad=-0.15'))\n\nax_b.text(\n    0.03, 0.30,\n    'Conflict resolved,\\nL$_{GAR}$ still collapses',\n    transform=ax_b.transAxes, fontsize=7, color='#555555',\n    ha='left', va='top', fontstyle='italic',\n    bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF8E7',\n              edgecolor=C_ROSE, alpha=0.9, linewidth=0.8)\n)\n\nax_b.legend(loc='upper right', borderpad=0.4, handlelength=1.8)\n\nax_b.set_xlim(-5, 220)\nax_b.set_ylim(-0.008, 0.26)\nax_b.set_xlabel('Global Step')\nax_b.set_ylabel('L$_{GAR}$ (MSE loss)')\nax_b.set_title('(b) PCGrad cannot prevent L$_{GAR}$ collapse',\n               fontsize=9, pad=8, loc='left')\n\nfor ax in [ax_a, ax_b]:\n    ax.grid(axis='y', alpha=0.10, linewidth=0.5, color='#888888')\n\nfig.subplots_adjust(hspace=0.38)\n\nsave_fig(fig, 'fig2_training_pcgrad')\n",
      "numLines": 146,
      "startLine": 1,
      "totalLines": 146
    }
  }
}
```

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01Sm7cMjVATdoYQmfby4yrQE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "091288cf-1703-46e5-99f2-6811335696bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 35 · 2026-05-25T20:12:26.310Z_

<details><summary>↩ Tool result · `toolu_01Sm7cMjVATdoYQmfby4yrQE`</summary>

```text
1	"""Generate Figure 6: Gate Turn Conditioning + Distribution Shift (horizontal 2-panel, double-column)."""
2	from palette import *
3	import matplotlib.patheffects as pe
4	import matplotlib.ticker as ticker
5	import numpy as np
6	
7	apply_style()
8	
9	fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.0, 2.2),
10	                                   gridspec_kw={'width_ratios': [1, 1.15]})
11	
12	# ======================================================================
13	# Panel (a): Gate Turn Conditioning — Cleveland dot plot (top-5 layers)
14	# ======================================================================
15	layers = ['L9', 'L20', 'L12', 'L14', 'L23']
16	turn1  = [0.8578, 0.8228, 0.8200, 0.7473, 0.7693]
17	turn21 = [0.9679, 0.9393, 0.9465, 0.9276, 0.9793]
18	diffs  = [-0.1101, -0.1165, -0.1265, -0.1803, -0.2100]
19	
20	y = np.arange(len(layers))
21	
22	for i in range(len(layers)):
23	    ax_a.plot([turn1[i], turn21[i]], [y[i], y[i]],
24	             color='#DDDDDD', linewidth=2.0, zorder=1, solid_capstyle='round')
25	
26	ax_a.scatter(turn1, y, color=C_PURPLE, s=50, zorder=3,
27	            edgecolors='white', linewidths=0.6, label='Turn 1 (early)')
28	ax_a.scatter(turn21, y, color=C_GREEN, s=50, zorder=3,
29	            edgecolors='white', linewidths=0.6, label='Turn 21 (late)')
30	
31	for i, d in enumerate(diffs):
32	    ax_a.text(1.012, y[i], f'{d:+.2f}', fontsize=6.5, va='center',
33	              color='#666666', family='monospace')
34	
35	ax_a.set_yticks(y)
36	ax_a.set_yticklabels(layers, fontsize=8)
37	ax_a.set_xlim(0.70, 1.02)
38	ax_a.set_xlabel('Gate value', fontsize=8)
39	ax_a.set_title('(a) Gates become passive at late turns',
40	               fontsize=9, fontweight='bold', pad=8, loc='left')
41	ax_a.legend(loc='lower right', fontsize=6.5, frameon=False,
42	           handletextpad=0.3, borderpad=0.35)
43	
44	ax_a.text(0.97, 0.05, 'p = 3.7e-8, r = 0.975',
45	          transform=ax_a.transAxes, fontsize=6, va='bottom', ha='right',
46	          color=C_GRAY, fontstyle='italic')
47	
48	ax_a.grid(axis='x', alpha=0.08, zorder=0)
49	
50	# ======================================================================
51	# Panel (b): Distribution Shift — Grouped bar chart (log scale)
52	# ======================================================================
53	models = ['Base', 'TG', 'PCGrad', 'UG', 'LoRA']
54	iid    = [0.0122, 0.5035, 0.5002, 0.5053, 0.4978]
55	mg     = [0.0122, 0.0157, 0.0151, 0.0149, 0.0245]
56	
57	x = np.arange(len(models))
58	w = 0.30
59	
60	import matplotlib.patches as mpatches
61	variant_colors = [C_BASE, C_TG, C_PC, C_UG, C_LO]
62	bars_iid = ax_b.bar(x - w/2, iid, w, color=variant_colors,
63	                     zorder=2, edgecolor='white', linewidth=0.4)
64	bars_mg = ax_b.bar(x + w/2, mg, w, color=variant_colors,
65	                    zorder=2, edgecolor='white', linewidth=0.4, alpha=0.55)
66	
67	ax_b.set_yscale('log')
68	ax_b.set_ylim(0.005, 1.2)
69	ax_b.set_xticks(x)
70	ax_b.set_xticklabels(models, fontsize=8)
71	ax_b.set_ylabel('GAR (ours)', fontsize=9)
72	ax_b.set_title('(b) 20–33× gap across all variants',
73	               fontsize=9, fontweight='bold', pad=8, loc='left')
74	p_iid = mpatches.Patch(facecolor=C_TG, edgecolor='white', linewidth=0.4, label='IID eval')
75	p_mg  = mpatches.Patch(facecolor=C_TG, edgecolor='white', linewidth=0.4, alpha=0.55, label='Model-gen.')
76	ax_b.legend(handles=[p_iid, p_mg], loc='upper right', fontsize=6.5, frameon=False,
77	           handletextpad=0.3, borderpad=0.35, ncol=1)
78	
79	for i, v in enumerate(iid):
80	    if v > 0.1:
81	        label = f'{v:.2f}'
82	        ax_b.text(i - w/2, v * 1.15, label, ha='center', va='bottom',
83	                 fontsize=5.5, color=C_TF_DARK)
84	
85	for i, v in enumerate(mg):
86	    if i > 0:
87	        ax_b.text(i + w/2, v * 1.25, f'{v:.4f}', ha='center', va='bottom',
88	                 fontsize=5, color=C_AR_DARK)
89	
90	for i in range(1, len(models)):
91	    gap = iid[i] / mg[i]
92	    geo_mean = np.sqrt(iid[i] * mg[i])
93	    t = ax_b.text(i + w/2 + 0.17, geo_mean, f'{gap:.0f}×', fontsize=7,
94	                  fontweight='bold', color=C_AR_DARK, ha='left', va='center')
95	    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])
96	
97	    ax_b.plot([x[i] - w/2, x[i] + w/2], [iid[i], mg[i]],
98	             color='#CCCCCC', linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))
99	
100	ax_b.axhspan(0.005, 0.05, color='#FFF3E0', alpha=0.15, zorder=0)
101	ax_b.axhspan(0.05, 1.2, color='#E8F5E9', alpha=0.15, zorder=0)
102	
103	ax_b.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
104	ax_b.grid(axis='y', which='major', alpha=0.10, zorder=0)
105	
106	plt.tight_layout(w_pad=2.5)
107	
108	save_fig(fig, 'fig3_gate_shift')
109	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "3d734c38-1f18-4f5b-9559-ff7f7d961aa3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
      "content": "\"\"\"Generate Figure 6: Gate Turn Conditioning + Distribution Shift (horizontal 2-panel, double-column).\"\"\"\nfrom palette import *\nimport matplotlib.patheffects as pe\nimport matplotlib.ticker as ticker\nimport numpy as np\n\napply_style()\n\nfig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.0, 2.2),\n                                   gridspec_kw={'width_ratios': [1, 1.15]})\n\n# ======================================================================\n# Panel (a): Gate Turn Conditioning — Cleveland dot plot (top-5 layers)\n# ======================================================================\nlayers = ['L9', 'L20', 'L12', 'L14', 'L23']\nturn1  = [0.8578, 0.8228, 0.8200, 0.7473, 0.7693]\nturn21 = [0.9679, 0.9393, 0.9465, 0.9276, 0.9793]\ndiffs  = [-0.1101, -0.1165, -0.1265, -0.1803, -0.2100]\n\ny = np.arange(len(layers))\n\nfor i in range(len(layers)):\n    ax_a.plot([turn1[i], turn21[i]], [y[i], y[i]],\n             color='#DDDDDD', linewidth=2.0, zorder=1, solid_capstyle='round')\n\nax_a.scatter(turn1, y, color=C_PURPLE, s=50, zorder=3,\n            edgecolors='white', linewidths=0.6, label='Turn 1 (early)')\nax_a.scatter(turn21, y, color=C_GREEN, s=50, zorder=3,\n            edgecolors='white', linewidths=0.6, label='Turn 21 (late)')\n\nfor i, d in enumerate(diffs):\n    ax_a.text(1.012, y[i], f'{d:+.2f}', fontsize=6.5, va='center',\n              color='#666666', family='monospace')\n\nax_a.set_yticks(y)\nax_a.set_yticklabels(layers, fontsize=8)\nax_a.set_xlim(0.70, 1.02)\nax_a.set_xlabel('Gate value', fontsize=8)\nax_a.set_title('(a) Gates become passive at late turns',\n               fontsize=9, fontweight='bold', pad=8, loc='left')\nax_a.legend(loc='lower right', fontsize=6.5, frameon=False,\n           handletextpad=0.3, borderpad=0.35)\n\nax_a.text(0.97, 0.05, 'p = 3.7e-8, r = 0.975',\n          transform=ax_a.transAxes, fontsize=6, va='bottom', ha='right',\n          color=C_GRAY, fontstyle='italic')\n\nax_a.grid(axis='x', alpha=0.08, zorder=0)\n\n# ======================================================================\n# Panel (b): Distribution Shift — Grouped bar chart (log scale)\n# ======================================================================\nmodels = ['Base', 'TG', 'PCGrad', 'UG', 'LoRA']\niid    = [0.0122, 0.5035, 0.5002, 0.5053, 0.4978]\nmg     = [0.0122, 0.0157, 0.0151, 0.0149, 0.0245]\n\nx = np.arange(len(models))\nw = 0.30\n\nimport matplotlib.patches as mpatches\nvariant_colors = [C_BASE, C_TG, C_PC, C_UG, C_LO]\nbars_iid = ax_b.bar(x - w/2, iid, w, color=variant_colors,\n                     zorder=2, edgecolor='white', linewidth=0.4)\nbars_mg = ax_b.bar(x + w/2, mg, w, color=variant_colors,\n                    zorder=2, edgecolor='white', linewidth=0.4, alpha=0.55)\n\nax_b.set_yscale('log')\nax_b.set_ylim(0.005, 1.2)\nax_b.set_xticks(x)\nax_b.set_xticklabels(models, fontsize=8)\nax_b.set_ylabel('GAR (ours)', fontsize=9)\nax_b.set_title('(b) 20–33× gap across all variants',\n               fontsize=9, fontweight='bold', pad=8, loc='left')\np_iid = mpatches.Patch(facecolor=C_TG, edgecolor='white', linewidth=0.4, label='IID eval')\np_mg  = mpatches.Patch(facecolor=C_TG, edgecolor='white', linewidth=0.4, alpha=0.55, label='Model-gen.')\nax_b.legend(handles=[p_iid, p_mg], loc='upper right', fontsize=6.5, frameon=False,\n           handletextpad=0.3, borderpad=0.35, ncol=1)\n\nfor i, v in enumerate(iid):\n    if v > 0.1:\n        label = f'{v:.2f}'\n        ax_b.text(i - w/2, v * 1.15, label, ha='center', va='bottom',\n                 fontsize=5.5, color=C_TF_DARK)\n\nfor i, v in enumerate(mg):\n    if i > 0:\n        ax_b.text(i + w/2, v * 1.25, f'{v:.4f}', ha='center', va='bottom',\n                 fontsize=5, color=C_AR_DARK)\n\nfor i in range(1, len(models)):\n    gap = iid[i] / mg[i]\n    geo_mean = np.sqrt(iid[i] * mg[i])\n    t = ax_b.text(i + w/2 + 0.17, geo_mean, f'{gap:.0f}×', fontsize=7,\n                  fontweight='bold', color=C_AR_DARK, ha='left', va='center')\n    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])\n\n    ax_b.plot([x[i] - w/2, x[i] + w/2], [iid[i], mg[i]],\n             color='#CCCCCC', linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))\n\nax_b.axhspan(0.005, 0.05, color='#FFF3E0', alpha=0.15, zorder=0)\nax_b.axhspan(0.05, 1.2, color='#E8F5E9', alpha=0.15, zorder=0)\n\nax_b.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))\nax_b.grid(axis='y', which='major', alpha=0.10, zorder=0)\n\nplt.tight_layout(w_pad=2.5)\n\nsave_fig(fig, 'fig3_gate_shift')\n",
      "numLines": 109,
      "startLine": 1,
      "totalLines": 109
    }
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01UGArHewkV7wGfiW2Dv7Ewp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig4.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "af347c4e-33d0-49bd-9ec0-da48e967b4f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 37 · 2026-05-25T20:12:26.780Z_

<details><summary>↩ Tool result · `toolu_01UGArHewkV7wGfiW2Dv7Ewp`</summary>

```text
1	"""Generate Figure 4: Goal Attention Decay — Gating adds zero inference overhead."""
2	from palette import *
3	import matplotlib.patheffects as pe
4	import numpy as np
5	
6	apply_style()
7	
8	turns = np.arange(1, 11)
9	
10	base_data = np.array([0.0418, 0.0241, 0.0224, 0.013, 0.0133,
11	                       0.0086, 0.0078, 0.008, 0.0157, 0.0064])
12	
13	
14	def exponential_decay_curve(mean_attn, decay_frac, n=10):
15	    k = -np.log(1 - decay_frac) / (n - 1)
16	    t = np.arange(n)
17	    weights = np.exp(-k * t)
18	    a1 = mean_attn * n / weights.sum()
19	    return a1 * weights
20	
21	
22	tg_curve = exponential_decay_curve(0.0232, 0.777)
23	ug_curve = exponential_decay_curve(0.0216, 0.803)
24	lora_curve = exponential_decay_curve(0.0216, 0.810)
25	
26	fig, ax = plt.subplots(figsize=(3.5, 2.8))
27	
28	ax.plot(turns, base_data, 'o:', color=C_BASE, markersize=3.5,
29	        markeredgecolor='white', markeredgewidth=0.4,
30	        label='Base (87.5%)', zorder=3, linewidth=1.2)
31	
32	ax.plot(turns, tg_curve, 's-', color=C_TG, markersize=3.5,
33	        markeredgecolor='white', markeredgewidth=0.4,
34	        label='ThreadGate (77.7%)', zorder=5, linewidth=1.6)
35	
36	ax.plot(turns, lora_curve, '^--', color=C_LO, markersize=4,
37	        markeredgecolor='white', markeredgewidth=0.4,
38	        label='LoRA-only (81.0%)', zorder=4, linewidth=1.3)
39	
40	ax.plot(turns, ug_curve, 'D-.', color=C_TEAL, markersize=3.5,
41	        markeredgecolor='white', markeredgewidth=0.4,
42	        label='Ungated (80.3%)', zorder=3, linewidth=1.2)
43	
44	ax.fill_between(turns, tg_curve, lora_curve,
45	                alpha=0.06, color=C_LILAC, zorder=1)
46	
47	mid_idx = 4
48	mid_y = (tg_curve[mid_idx] + lora_curve[mid_idx]) / 2
49	ax.annotate('Δ = 3.3 pp',
50	            xy=(turns[mid_idx], mid_y),
51	            xytext=(turns[mid_idx] + 2.2, mid_y + 0.012),
52	            fontsize=6, color='#666666', fontstyle='italic', ha='left',
53	            arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=0.5,
54	                            connectionstyle='arc3,rad=-0.12'))
55	
56	ax.set_xticks(turns)
57	ax.set_xlabel('Turn Index')
58	ax.set_ylabel('GAR-ours')
59	ax.set_xlim(0.5, 10.5)
60	ax.set_ylim(-0.002, 0.058)
61	
62	ax.legend(loc='upper right', borderpad=0.3, handlelength=1.2,
63	          handletextpad=0.3, fontsize=6)
64	
65	ax.grid(axis='y', alpha=0.10, zorder=0)
66	
67	save_fig(fig, 'fig4_attention_heatmap')
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "8c2068b9-1804-4b7c-8ed6-653cb32ed151",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig4.py",
      "content": "\"\"\"Generate Figure 4: Goal Attention Decay — Gating adds zero inference overhead.\"\"\"\nfrom palette import *\nimport matplotlib.patheffects as pe\nimport numpy as np\n\napply_style()\n\nturns = np.arange(1, 11)\n\nbase_data = np.array([0.0418, 0.0241, 0.0224, 0.013, 0.0133,\n                       0.0086, 0.0078, 0.008, 0.0157, 0.0064])\n\n\ndef exponential_decay_curve(mean_attn, decay_frac, n=10):\n    k = -np.log(1 - decay_frac) / (n - 1)\n    t = np.arange(n)\n    weights = np.exp(-k * t)\n    a1 = mean_attn * n / weights.sum()\n    return a1 * weights\n\n\ntg_curve = exponential_decay_curve(0.0232, 0.777)\nug_curve = exponential_decay_curve(0.0216, 0.803)\nlora_curve = exponential_decay_curve(0.0216, 0.810)\n\nfig, ax = plt.subplots(figsize=(3.5, 2.8))\n\nax.plot(turns, base_data, 'o:', color=C_BASE, markersize=3.5,\n        markeredgecolor='white', markeredgewidth=0.4,\n        label='Base (87.5%)', zorder=3, linewidth=1.2)\n\nax.plot(turns, tg_curve, 's-', color=C_TG, markersize=3.5,\n        markeredgecolor='white', markeredgewidth=0.4,\n        label='ThreadGate (77.7%)', zorder=5, linewidth=1.6)\n\nax.plot(turns, lora_curve, '^--', color=C_LO, markersize=4,\n        markeredgecolor='white', markeredgewidth=0.4,\n        label='LoRA-only (81.0%)', zorder=4, linewidth=1.3)\n\nax.plot(turns, ug_curve, 'D-.', color=C_TEAL, markersize=3.5,\n        markeredgecolor='white', markeredgewidth=0.4,\n        label='Ungated (80.3%)', zorder=3, linewidth=1.2)\n\nax.fill_between(turns, tg_curve, lora_curve,\n                alpha=0.06, color=C_LILAC, zorder=1)\n\nmid_idx = 4\nmid_y = (tg_curve[mid_idx] + lora_curve[mid_idx]) / 2\nax.annotate('Δ = 3.3 pp',\n            xy=(turns[mid_idx], mid_y),\n            xytext=(turns[mid_idx] + 2.2, mid_y + 0.012),\n            fontsize=6, color='#666666', fontstyle='italic', ha='left',\n            arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=0.5,\n                            connectionstyle='arc3,rad=-0.12'))\n\nax.set_xticks(turns)\nax.set_xlabel('Turn Index')\nax.set_ylabel('GAR-ours')\nax.set_xlim(0.5, 10.5)\nax.set_ylim(-0.002, 0.058)\n\nax.legend(loc='upper right', borderpad=0.3, handlelength=1.2,\n          handletextpad=0.3, fontsize=6)\n\nax.grid(axis='y', alpha=0.10, zorder=0)\n\nsave_fig(fig, 'fig4_attention_heatmap')\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  }
}
```

</details>

---


### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01HrXwkwKAnP9hPwMJbESXcy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig5.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "01d85fda-e444-46cf-8b6b-409870ff7a9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 39 · 2026-05-25T20:12:27.260Z_

<details><summary>↩ Tool result · `toolu_01HrXwkwKAnP9hPwMJbESXcy`</summary>

```text
1	from palette import *
2	import matplotlib.gridspec as gridspec
3	import numpy as np
4	
5	apply_style()
6	
7	# ── Data (unchanged) ──────────────────────────────────────────────
8	gen_beta =    [0.0,   0.5,   1.0,   2.0,   5.0,   10.0]
9	gen_gar =     [0.028, 0.0287, 0.0349, 0.062, 0.6795, 0.959]
10	gen_gar_std = [0.014, 0.008, 0.007, 0.011, 0.020, 0.003]
11	gen_ppl =     [1.41,  1.39,  1.36,  1.41,  1.91,  4.22]
12	gen_ppl_std = [0.12,  0.11,  0.10,  0.12,  0.36,  0.99]
13	
14	gen50_beta =    [0.0,   2.0,   3.0,   4.0,   5.0,   10.0]
15	gen50_gar =     [0.064, 0.128, 0.556, 0.644, 0.727, 0.961]
16	gen50_gar_std = [0.081, 0.110, 0.060, 0.061, 0.061, 0.015]
17	gen50_ppl =     [1.43,  1.48,  1.56,  1.67,  1.77,  3.45]
18	gen50_ppl_std = [0.10,  0.14,  0.17,  0.22,  0.27,  1.78]
19	
20	# ── Layout: 2×2 grid for double-column figure ─────────────────────
21	fig = plt.figure(figsize=(7.0, 2.8))
22	gs = gridspec.GridSpec(2, 2, hspace=0.55, wspace=0.35,
23	                       height_ratios=[1, 0.85])
24	
25	ax_gar5  = fig.add_subplot(gs[0, 0])
26	ax_ppl5  = fig.add_subplot(gs[1, 0])
27	ax_gar50 = fig.add_subplot(gs[0, 1])
28	ax_ppl50 = fig.add_subplot(gs[1, 1])
29	
30	XLO, XHI = -0.8, 11.3
31	
32	# ── Shared plotting helpers ───────────────────────────────────────
33	def style_ax(ax):
34	    ax.grid(axis='y', alpha=0.08, linewidth=0.5)
35	
36	def plot_gar(ax, beta, gar, gar_std, title):
37	    style_ax(ax)
38	    ax.axvspan(2, 5, alpha=0.07, color=C_SWEET, zorder=0)
39	    ax.axhline(y=0.535, color=C_GRAY, linestyle=':', linewidth=0.7, zorder=1)
40	    ax.errorbar(beta, gar, yerr=gar_std, fmt='-o', color=C_TEAL,
41	                markersize=4.5, markerfacecolor=C_TEAL, markeredgecolor='white',
42	                markeredgewidth=0.5, capsize=2, capthick=0.7, elinewidth=0.7,
43	                zorder=3)
44	    ax.set_ylabel('Mid-GAR', color=C_TEAL, fontsize=9)
45	    ax.set_ylim(-0.02, 1.08)
46	    ax.set_xlim(XLO, XHI)
47	    ax.tick_params(axis='y', colors=C_TEAL)
48	    ax.set_title(title, pad=6, loc='left', fontsize=9.5, fontweight='medium')
49	
50	def plot_ppl(ax, beta, ppl, ppl_std):
51	    style_ax(ax)
52	    ax.axvspan(2, 5, alpha=0.07, color=C_SWEET, zorder=0)
53	    ax.errorbar(beta, ppl, yerr=ppl_std, fmt='--^', color=C_ROSE,
54	                markersize=4, markerfacecolor=C_ROSE, markeredgecolor='white',
55	                markeredgewidth=0.5, capsize=2, capthick=0.7, elinewidth=0.7,
56	                zorder=3, linewidth=1.1)
57	    ax.set_ylabel('PPL', color=C_ROSE, fontsize=9)
58	    ax.set_xlim(XLO, XHI)
59	    ax.tick_params(axis='y', colors=C_ROSE)
60	    ax.set_xlabel(r'$\beta$ (Steering Strength)', fontsize=9)
61	
62	# ── Panel (a): N=5 ────────────────────────────────────────────────
63	plot_gar(ax_gar5, gen_beta, gen_gar, gen_gar_std,
64	         '(a) $N$=5 Generation')
65	ax_gar5.set_xticks([0, 1, 2, 5, 10])
66	ax_gar5.set_xticklabels([])
67	ax_gar5.text(8.5, 0.56, 'TF baseline', fontsize=6.5, color=C_GRAY,
68	             va='bottom', ha='center')
69	ax_gar5.text(3.5, 1.03, 'sweet spot', fontsize=6, color='#B8960F',
70	             ha='center', va='top', fontstyle='italic', alpha=0.65)
71	
72	plot_ppl(ax_ppl5, gen_beta, gen_ppl, gen_ppl_std)
73	ax_ppl5.set_xticks([0, 1, 2, 5, 10])
74	ax_ppl5.set_ylim(0.9, 5.5)
75	
76	# ── Panel (b): N=50 ───────────────────────────────────────────────
77	plot_gar(ax_gar50, gen50_beta, gen50_gar, gen50_gar_std,
78	         '(b) $N$=50 Generation')
79	ax_gar50.set_xticks([0, 2, 3, 4, 5, 10])
80	ax_gar50.set_xticklabels([])
81	ax_gar50.text(9.5, 0.56, 'TF baseline', fontsize=6.5, color=C_GRAY,
82	              va='bottom', ha='center')
83	ax_gar50.text(3.5, 1.03, 'sweet spot', fontsize=6, color='#B8960F',
84	              ha='center', va='top', fontstyle='italic', alpha=0.65)
85	
86	ax_gar50.annotate(r'$\beta$=3 operating pt.',
87	                  xy=(3, 0.556), xytext=(7.0, 0.15),
88	                  fontsize=7, color='#444444', ha='center',
89	                  arrowprops=dict(arrowstyle='->', color=C_GRAY,
90	                                  lw=0.7, connectionstyle='arc3,rad=-0.12'),
91	                  bbox=dict(boxstyle='round,pad=0.25', facecolor='white', alpha=0.9, linewidth=0.5))
92	
93	plot_ppl(ax_ppl50, gen50_beta, gen50_ppl, gen50_ppl_std)
94	ax_ppl50.set_xticks([0, 2, 3, 4, 5, 10])
95	ax_ppl50.set_ylim(0.9, 5.5)
96	
97	save_fig(fig, 'fig5_attention_steering')
98	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "e7a0d923-db42-4053-a7c1-8bb68f7c5d6a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig5.py",
      "content": "from palette import *\nimport matplotlib.gridspec as gridspec\nimport numpy as np\n\napply_style()\n\n# ── Data (unchanged) ──────────────────────────────────────────────\ngen_beta =    [0.0,   0.5,   1.0,   2.0,   5.0,   10.0]\ngen_gar =     [0.028, 0.0287, 0.0349, 0.062, 0.6795, 0.959]\ngen_gar_std = [0.014, 0.008, 0.007, 0.011, 0.020, 0.003]\ngen_ppl =     [1.41,  1.39,  1.36,  1.41,  1.91,  4.22]\ngen_ppl_std = [0.12,  0.11,  0.10,  0.12,  0.36,  0.99]\n\ngen50_beta =    [0.0,   2.0,   3.0,   4.0,   5.0,   10.0]\ngen50_gar =     [0.064, 0.128, 0.556, 0.644, 0.727, 0.961]\ngen50_gar_std = [0.081, 0.110, 0.060, 0.061, 0.061, 0.015]\ngen50_ppl =     [1.43,  1.48,  1.56,  1.67,  1.77,  3.45]\ngen50_ppl_std = [0.10,  0.14,  0.17,  0.22,  0.27,  1.78]\n\n# ── Layout: 2×2 grid for double-column figure ─────────────────────\nfig = plt.figure(figsize=(7.0, 2.8))\ngs = gridspec.GridSpec(2, 2, hspace=0.55, wspace=0.35,\n                       height_ratios=[1, 0.85])\n\nax_gar5  = fig.add_subplot(gs[0, 0])\nax_ppl5  = fig.add_subplot(gs[1, 0])\nax_gar50 = fig.add_subplot(gs[0, 1])\nax_ppl50 = fig.add_subplot(gs[1, 1])\n\nXLO, XHI = -0.8, 11.3\n\n# ── Shared plotting helpers ───────────────────────────────────────\ndef style_ax(ax):\n    ax.grid(axis='y', alpha=0.08, linewidth=0.5)\n\ndef plot_gar(ax, beta, gar, gar_std, title):\n    style_ax(ax)\n    ax.axvspan(2, 5, alpha=0.07, color=C_SWEET, zorder=0)\n    ax.axhline(y=0.535, color=C_GRAY, linestyle=':', linewidth=0.7, zorder=1)\n    ax.errorbar(beta, gar, yerr=gar_std, fmt='-o', color=C_TEAL,\n                markersize=4.5, markerfacecolor=C_TEAL, markeredgecolor='white',\n                markeredgewidth=0.5, capsize=2, capthick=0.7, elinewidth=0.7,\n                zorder=3)\n    ax.set_ylabel('Mid-GAR', color=C_TEAL, fontsize=9)\n    ax.set_ylim(-0.02, 1.08)\n    ax.set_xlim(XLO, XHI)\n    ax.tick_params(axis='y', colors=C_TEAL)\n    ax.set_title(title, pad=6, loc='left', fontsize=9.5, fontweight='medium')\n\ndef plot_ppl(ax, beta, ppl, ppl_std):\n    style_ax(ax)\n    ax.axvspan(2, 5, alpha=0.07, color=C_SWEET, zorder=0)\n    ax.errorbar(beta, ppl, yerr=ppl_std, fmt='--^', color=C_ROSE,\n                markersize=4, markerfacecolor=C_ROSE, markeredgecolor='white',\n                markeredgewidth=0.5, capsize=2, capthick=0.7, elinewidth=0.7,\n                zorder=3, linewidth=1.1)\n    ax.set_ylabel('PPL', color=C_ROSE, fontsize=9)\n    ax.set_xlim(XLO, XHI)\n    ax.tick_params(axis='y', colors=C_ROSE)\n    ax.set_xlabel(r'$\\beta$ (Steering Strength)', fontsize=9)\n\n# ── Panel (a): N=5 ────────────────────────────────────────────────\nplot_gar(ax_gar5, gen_beta, gen_gar, gen_gar_std,\n         '(a) $N$=5 Generation')\nax_gar5.set_xticks([0, 1, 2, 5, 10])\nax_gar5.set_xticklabels([])\nax_gar5.text(8.5, 0.56, 'TF baseline', fontsize=6.5, color=C_GRAY,\n             va='bottom', ha='center')\nax_gar5.text(3.5, 1.03, 'sweet spot', fontsize=6, color='#B8960F',\n             ha='center', va='top', fontstyle='italic', alpha=0.65)\n\nplot_ppl(ax_ppl5, gen_beta, gen_ppl, gen_ppl_std)\nax_ppl5.set_xticks([0, 1, 2, 5, 10])\nax_ppl5.set_ylim(0.9, 5.5)\n\n# ── Panel (b): N=50 ───────────────────────────────────────────────\nplot_gar(ax_gar50, gen50_beta, gen50_gar, gen50_gar_std,\n         '(b) $N$=50 Generation')\nax_gar50.set_xticks([0, 2, 3, 4, 5, 10])\nax_gar50.set_xticklabels([])\nax_gar50.text(9.5, 0.56, 'TF baseline', fontsize=6.5, color=C_GRAY,\n              va='bottom', ha='center')\nax_gar50.text(3.5, 1.03, 'sweet spot', fontsize=6, color='#B8960F',\n              ha='center', va='top', fontstyle='italic', alpha=0.65)\n\nax_gar50.annotate(r'$\\beta$=3 operating pt.',\n                  xy=(3, 0.556), xytext=(7.0, 0.15),\n                  fontsize=7, color='#444444', ha='center',\n                  arrowprops=dict(arrowstyle='->', color=C_GRAY,\n                                  lw=0.7, connectionstyle='arc3,rad=-0.12'),\n                  bbox=dict(boxstyle='round,pad=0.25', facecolor='white', alpha=0.9, linewidth=0.5))\n\nplot_ppl(ax_ppl50, gen50_beta, gen50_ppl, gen50_ppl_std)\nax_ppl50.set_xticks([0, 2, 3, 4, 5, 10])\nax_ppl50.set_ylim(0.9, 5.5)\n\nsave_fig(fig, 'fig5_attention_steering')\n",
      "numLines": 98,
      "startLine": 1,
      "totalLines": 98
    }
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01Sut29Y1ULVs5b1RfnUNkfq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_ss_gap_compression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "d8f1776a-7cb8-4a0d-afc1-d64fb17d8836",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 41 · 2026-05-25T20:12:27.756Z_

<details><summary>↩ Tool result · `toolu_01Sut29Y1ULVs5b1RfnUNkfq`</summary>

```text
1	"""Figure A: SS Gap Compression — TF/AR gap ratio by config (horizontal bars)."""
2	import sys
3	sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
4	from palette import *
5	import numpy as np
6	
7	apply_style()
8	
9	configs =    ['Llama SS', 'Qwen SS', 'ThreadGate', 'LoRA', 'UG', 'PCGrad', 'Llama TG']
10	gap_ratios = [2.9,        1.3,       7.8,          13.5,   14.8, 16.7,     12.5]
11	color_keys = ['SS',       'SS',      'ThreadGate', 'LoRA', 'UG', 'PCGrad', 'ThreadGate']
12	colors = [COLORS.get(c, C_GRAY) for c in color_keys]
13	
14	fig, ax = plt.subplots(figsize=(5.2, 2.8))
15	
16	y = np.arange(len(configs))
17	alphas = [1.0 if 'SS' in c else 0.55 for c in configs]
18	
19	for i, (cfg, gap, col) in enumerate(zip(configs, gap_ratios, colors)):
20	    ax.barh(i, gap, height=0.6, color=col, alpha=alphas[i],
21	            edgecolor='white', linewidth=0.4, zorder=2)
22	    is_ss = 'SS' in cfg
23	    ax.text(gap + 0.4, i, f'{gap:.1f}×', va='center', ha='left',
24	            fontsize=7.5, fontweight='bold' if is_ss else 'normal',
25	            color=col if is_ss else '#666666')
26	
27	ax.axvline(1.0, color=C_GRAY, linestyle='--', linewidth=0.8, zorder=1, alpha=0.6)
28	ax.text(1.0, len(configs) - 0.15, 'parity', fontsize=6, color=C_GRAY,
29	        ha='center', va='bottom')
30	
31	# Separator between Qwen and Llama entries
32	ax.axhline(1.5, color='#DDDDDD', linewidth=0.5, linestyle='-', zorder=0)
33	
34	ax.set_yticks(y)
35	ax.set_yticklabels(configs, fontsize=8)
36	ax.set_xlabel('TF / AR Gap Ratio', fontsize=9)
37	ax.set_xlim(0, 20)
38	ax.invert_yaxis()
39	
40	save_fig(fig, 'fig_ss_gap_compression')
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "f0e0c99a-38b9-411b-a5de-6f5e37a19683",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_ss_gap_compression.py",
      "content": "\"\"\"Figure A: SS Gap Compression — TF/AR gap ratio by config (horizontal bars).\"\"\"\nimport sys\nsys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')\nfrom palette import *\nimport numpy as np\n\napply_style()\n\nconfigs =    ['Llama SS', 'Qwen SS', 'ThreadGate', 'LoRA', 'UG', 'PCGrad', 'Llama TG']\ngap_ratios = [2.9,        1.3,       7.8,          13.5,   14.8, 16.7,     12.5]\ncolor_keys = ['SS',       'SS',      'ThreadGate', 'LoRA', 'UG', 'PCGrad', 'ThreadGate']\ncolors = [COLORS.get(c, C_GRAY) for c in color_keys]\n\nfig, ax = plt.subplots(figsize=(5.2, 2.8))\n\ny = np.arange(len(configs))\nalphas = [1.0 if 'SS' in c else 0.55 for c in configs]\n\nfor i, (cfg, gap, col) in enumerate(zip(configs, gap_ratios, colors)):\n    ax.barh(i, gap, height=0.6, color=col, alpha=alphas[i],\n            edgecolor='white', linewidth=0.4, zorder=2)\n    is_ss = 'SS' in cfg\n    ax.text(gap + 0.4, i, f'{gap:.1f}×', va='center', ha='left',\n            fontsize=7.5, fontweight='bold' if is_ss else 'normal',\n            color=col if is_ss else '#666666')\n\nax.axvline(1.0, color=C_GRAY, linestyle='--', linewidth=0.8, zorder=1, alpha=0.6)\nax.text(1.0, len(configs) - 0.15, 'parity', fontsize=6, color=C_GRAY,\n        ha='center', va='bottom')\n\n# Separator between Qwen and Llama entries\nax.axhline(1.5, color='#DDDDDD', linewidth=0.5, linestyle='-', zorder=0)\n\nax.set_yticks(y)\nax.set_yticklabels(configs, fontsize=8)\nax.set_xlabel('TF / AR Gap Ratio', fontsize=9)\nax.set_xlim(0, 20)\nax.invert_yaxis()\n\nsave_fig(fig, 'fig_ss_gap_compression')\n",
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

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01R8k6wiyfavXHgipcYotWV4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_ss_multiseed.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "bae50648-6949-4d86-a6ad-5517bd5b9760",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 43 · 2026-05-25T20:12:28.686Z_

<details><summary>↩ Tool result · `toolu_01R8k6wiyfavXHgipcYotWV4`</summary>

```text
1	"""Figure B: Multi-seed Confidence — SS AR GAR at β=0 and β=5."""
2	import sys
3	sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
4	from palette import *
5	import numpy as np
6	import matplotlib.patheffects as pe
7	
8	apply_style()
9	
10	betas = [r'$\beta=0$', r'$\beta=5$']
11	seeds_b0 = [0.347, 0.423, 0.433]
12	seeds_b5 = [0.716, 0.717, 0.718]
13	all_seeds = [seeds_b0, seeds_b5]
14	means = [np.mean(s) for s in all_seeds]
15	stds = [np.std(s) for s in all_seeds]
16	
17	C_COLD = '#7BA7C2'
18	C_WARM = C_SS
19	bar_colors = [C_COLD, C_WARM]
20	edge_colors = ['#5A8CA6', '#9E5E3E']
21	
22	fig, ax = plt.subplots(figsize=(3.2, 2.8))
23	
24	x = np.arange(len(betas))
25	bar_width = 0.45
26	
27	for i in range(len(betas)):
28	    ax.bar(x[i], means[i], bar_width,
29	           color=bar_colors[i], edgecolor=edge_colors[i], linewidth=0.6,
30	           zorder=2, alpha=0.85)
31	
32	    ax.errorbar(x[i], means[i], yerr=stds[i], fmt='none', capsize=4,
33	                ecolor='#666666', elinewidth=0.9, capthick=0.7, zorder=3)
34	
35	    jitter = np.linspace(-0.06, 0.06, len(all_seeds[i]))
36	    dc = '#5A8CA6' if i == 0 else '#9E5E3E'
37	    ec = '#4A7A92' if i == 0 else '#8A4E30'
38	    ax.scatter(x[i] + jitter, all_seeds[i], s=22,
39	               color=dc, edgecolor=ec, linewidth=0.6, zorder=4)
40	
41	    txt = ax.text(x[i], means[i] + stds[i] + 0.030,
42	                  f'{means[i]:.3f}±{stds[i]:.3f}',
43	                  ha='center', va='bottom', fontsize=7.5, color='#444444')
44	    txt.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
45	
46	# Subtle horizontal grid
47	ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
48	ax.set_axisbelow(True)
49	ax.grid(axis='y', alpha=0.12, linewidth=0.4, color='#888888')
50	
51	ax.set_xticks(x)
52	ax.set_xticklabels(betas, fontsize=9)
53	ax.set_ylabel('AR GAR', fontsize=9)
54	ax.set_ylim(0, 0.85)
55	ax.set_xlim(-0.5, 1.5)
56	
57	save_fig(fig, 'fig_ss_multiseed')
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "c187ba5e-b23a-493a-8da9-3f6ddc5f5c25",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_ss_multiseed.py",
      "content": "\"\"\"Figure B: Multi-seed Confidence — SS AR GAR at β=0 and β=5.\"\"\"\nimport sys\nsys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')\nfrom palette import *\nimport numpy as np\nimport matplotlib.patheffects as pe\n\napply_style()\n\nbetas = [r'$\\beta=0$', r'$\\beta=5$']\nseeds_b0 = [0.347, 0.423, 0.433]\nseeds_b5 = [0.716, 0.717, 0.718]\nall_seeds = [seeds_b0, seeds_b5]\nmeans = [np.mean(s) for s in all_seeds]\nstds = [np.std(s) for s in all_seeds]\n\nC_COLD = '#7BA7C2'\nC_WARM = C_SS\nbar_colors = [C_COLD, C_WARM]\nedge_colors = ['#5A8CA6', '#9E5E3E']\n\nfig, ax = plt.subplots(figsize=(3.2, 2.8))\n\nx = np.arange(len(betas))\nbar_width = 0.45\n\nfor i in range(len(betas)):\n    ax.bar(x[i], means[i], bar_width,\n           color=bar_colors[i], edgecolor=edge_colors[i], linewidth=0.6,\n           zorder=2, alpha=0.85)\n\n    ax.errorbar(x[i], means[i], yerr=stds[i], fmt='none', capsize=4,\n                ecolor='#666666', elinewidth=0.9, capthick=0.7, zorder=3)\n\n    jitter = np.linspace(-0.06, 0.06, len(all_seeds[i]))\n    dc = '#5A8CA6' if i == 0 else '#9E5E3E'\n    ec = '#4A7A92' if i == 0 else '#8A4E30'\n    ax.scatter(x[i] + jitter, all_seeds[i], s=22,\n               color=dc, edgecolor=ec, linewidth=0.6, zorder=4)\n\n    txt = ax.text(x[i], means[i] + stds[i] + 0.030,\n                  f'{means[i]:.3f}±{stds[i]:.3f}',\n                  ha='center', va='bottom', fontsize=7.5, color='#444444')\n    txt.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n# Subtle horizontal grid\nax.yaxis.set_major_locator(plt.MultipleLocator(0.2))\nax.set_axisbelow(True)\nax.grid(axis='y', alpha=0.12, linewidth=0.4, color='#888888')\n\nax.set_xticks(x)\nax.set_xticklabels(betas, fontsize=9)\nax.set_ylabel('AR GAR', fontsize=9)\nax.set_ylim(0, 0.85)\nax.set_xlim(-0.5, 1.5)\n\nsave_fig(fig, 'fig_ss_multiseed')\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01MT5irGf7FNcRtJjoGo4w83`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_crossmodel.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4cb24991-e04b-4189-8f3a-88cd731a31e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8oZJw5SqRSMaeM3tBUkv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25398
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

_source line 45 · 2026-05-25T20:12:28.860Z_

<details><summary>↩ Tool result · `toolu_01MT5irGf7FNcRtJjoGo4w83`</summary>

```text
1	"""Generate cross-model comparison figure: TF-AR gap + gate profile overlay."""
2	import sys
3	sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
4	from palette import *
5	import matplotlib.patheffects as pe
6	import matplotlib.ticker as ticker
7	import numpy as np
8	
9	apply_style()
10	
11	fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 5.8),
12	                                   gridspec_kw={'height_ratios': [1, 1.1]})
13	
14	# ======================================================================
15	# Panel (a): Qwen vs Llama TF-AR gap (grouped bars, log scale)
16	# ======================================================================
17	models = ['Qwen-2.5-7B', 'Llama-3.1-8B']
18	tf_gar = [0.50, 0.484]
19	ar_gar = [0.064, 0.018]
20	gaps   = [7.8, 27]
21	
22	x = np.arange(len(models))
23	w = 0.28
24	
25	bars_tf = ax_a.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced',
26	                   zorder=2, edgecolor='white', linewidth=0.4)
27	bars_ar = ax_a.bar(x + w/2, ar_gar, w, color=C_AR, label='Autoregressive',
28	                   zorder=2, edgecolor='white', linewidth=0.4)
29	
30	ax_a.set_yscale('log')
31	ax_a.set_ylim(0.008, 1.5)
32	ax_a.set_xlim(-0.55, 2.0)
33	
34	ax_a.axhspan(0.008, 0.08, color='#FFF3E0', alpha=0.15, zorder=0)
35	ax_a.axhspan(0.08, 1.5, color='#E8F5E9', alpha=0.15, zorder=0)
36	
37	for i in range(len(models)):
38	    ax_a.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],
39	             color=C_GRAY, linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))
40	
41	for i, v in enumerate(tf_gar):
42	    ax_a.text(x[i] - w/2, v * 1.15, f'.{round(v*100):02d}', ha='center',
43	              va='bottom', fontsize=6, color=C_TF_DARK, fontweight='bold')
44	
45	for i, v in enumerate(ar_gar):
46	    ax_a.text(x[i] + w/2, v * 1.20, f'.{round(v*1000):03d}', ha='center',
47	              va='bottom', fontsize=5.5, color=C_AR_DARK)
48	
49	for i, gap in enumerate(gaps):
50	    geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])
51	    suffix = '\n(median)' if i == 1 else ''
52	    t = ax_a.text(x[i] + w/2 + 0.14, geo_mean, f'{gap:.0f}×{suffix}',
53	                  fontsize=7.5, fontweight='bold', color=C_AR,
54	                  ha='left', va='center')
55	    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])
56	
57	ax_a.set_xticks(x)
58	ax_a.set_xticklabels(models, fontsize=8)
59	ax_a.set_ylabel('GAR-ours (ThreadGate)')
60	ax_a.set_title('(a) TF-AR gap generalizes across architectures',
61	               fontsize=9, fontweight='bold', pad=8, loc='left')
62	ax_a.legend(loc='upper right',
63	            handletextpad=0.3, borderpad=0.35, fontsize=6.5)
64	
65	ax_a.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
66	ax_a.grid(axis='y', which='major', alpha=0.10, zorder=0)
67	
68	# ======================================================================
69	# Panel (b): Gate profile overlay (normalized depth)
70	# ======================================================================
71	qwen_gates = np.array([
72	    .883, .793, .996, .988, .984, .797, .961, .918,
73	    .965, .934, .969, .918, .926, .941, .930, .965,
74	    .941, .910, .961, .965, .973, .988, .969, .980,
75	    .980, .984, .988, 1.00
76	])
77	llama_gates = np.array([
78	    0.957, 0.973, 0.977, 0.965, 0.992, 0.969, 0.957, 0.957,
79	    0.961, 0.949, 0.938, 0.934, 0.969, 0.953, 0.957, 0.965,
80	    0.953, 0.961, 0.922, 0.902, 0.883, 0.863, 0.836, 0.844,
81	    0.809, 0.719, 0.762, 0.805, 0.801, 0.855, 0.898, 0.934
82	])
83	
84	qwen_depth = np.linspace(0, 1, len(qwen_gates))
85	llama_depth = np.linspace(0, 1, len(llama_gates))
86	
87	ax_b.plot(qwen_depth, qwen_gates, 'o-', color=C_TG, markersize=3.5,
88	          markeredgecolor='white', markeredgewidth=0.4,
89	          label='Qwen-2.5-7B (28L)', zorder=3, linewidth=1.5)
90	ax_b.plot(llama_depth, llama_gates, 's-', color=C_LO, markersize=3.5,
91	          markeredgecolor='white', markeredgewidth=0.4,
92	          label='Llama-3.1-8B (32L)', zorder=3, linewidth=1.5)
93	
94	ax_b.axhline(1.0, color='#DDDDDD', linestyle=':', linewidth=0.6, zorder=1)
95	ax_b.text(0.98, 1.006, 'identity', fontsize=6, color='#BBBBBB',
96	          ha='right', va='bottom')
97	
98	ax_b.annotate('L1=.793', xy=(qwen_depth[1], qwen_gates[1]),
99	              xytext=(qwen_depth[1] + 0.10, 0.755), fontsize=6,
100	              color=C_TG, ha='left',
101	              arrowprops=dict(arrowstyle='->', color=C_TG, lw=0.5))
102	ax_b.annotate('L5=.797', xy=(qwen_depth[5], qwen_gates[5]),
103	              xytext=(qwen_depth[5] + 0.10, 0.76), fontsize=6,
104	              color=C_TG, ha='left',
105	              arrowprops=dict(arrowstyle='->', color=C_TG, lw=0.5))
106	
107	ax_b.annotate('L25=.719', xy=(llama_depth[25], llama_gates[25]),
108	              xytext=(llama_depth[25] - 0.15, 0.695), fontsize=6,
109	              color=C_LO, ha='right',
110	              arrowprops=dict(arrowstyle='->', color=C_LO, lw=0.5))
111	
112	ax_b.set_xlabel('Normalized Depth (layer / L)')
113	ax_b.set_ylabel('Gate Value')
114	ax_b.set_ylim(0.68, 1.03)
115	ax_b.set_xlim(-0.02, 1.02)
116	ax_b.set_title('(b) Architecture-dependent gate patterns',
117	               fontsize=9, fontweight='bold', pad=8, loc='left')
118	ax_b.legend(loc='lower right',
119	            handletextpad=0.3, borderpad=0.35, fontsize=6.5)
120	ax_b.grid(axis='y', alpha=0.10, zorder=0)
121	
122	plt.tight_layout(h_pad=1.8)
123	save_fig(fig, 'fig_crossmodel')
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "644b336d-eb14-4687-9434-616e453067f8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_crossmodel.py",
      "content": "\"\"\"Generate cross-model comparison figure: TF-AR gap + gate profile overlay.\"\"\"\nimport sys\nsys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')\nfrom palette import *\nimport matplotlib.patheffects as pe\nimport matplotlib.ticker as ticker\nimport numpy as np\n\napply_style()\n\nfig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 5.8),\n                                   gridspec_kw={'height_ratios': [1, 1.1]})\n\n# ======================================================================\n# Panel (a): Qwen vs Llama TF-AR gap (grouped bars, log scale)\n# ======================================================================\nmodels = ['Qwen-2.5-7B', 'Llama-3.1-8B']\ntf_gar = [0.50, 0.484]\nar_gar = [0.064, 0.018]\ngaps   = [7.8, 27]\n\nx = np.arange(len(models))\nw = 0.28\n\nbars_tf = ax_a.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced',\n                   zorder=2, edgecolor='white', linewidth=0.4)\nbars_ar = ax_a.bar(x + w/2, ar_gar, w, color=C_AR, label='Autoregressive',\n                   zorder=2, edgecolor='white', linewidth=0.4)\n\nax_a.set_yscale('log')\nax_a.set_ylim(0.008, 1.5)\nax_a.set_xlim(-0.55, 2.0)\n\nax_a.axhspan(0.008, 0.08, color='#FFF3E0', alpha=0.15, zorder=0)\nax_a.axhspan(0.08, 1.5, color='#E8F5E9', alpha=0.15, zorder=0)\n\nfor i in range(len(models)):\n    ax_a.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],\n             color=C_GRAY, linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))\n\nfor i, v in enumerate(tf_gar):\n    ax_a.text(x[i] - w/2, v * 1.15, f'.{round(v*100):02d}', ha='center',\n              va='bottom', fontsize=6, color=C_TF_DARK, fontweight='bold')\n\nfor i, v in enumerate(ar_gar):\n    ax_a.text(x[i] + w/2, v * 1.20, f'.{round(v*1000):03d}', ha='center',\n              va='bottom', fontsize=5.5, color=C_AR_DARK)\n\nfor i, gap in enumerate(gaps):\n    geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])\n    suffix = '\\n(median)' if i == 1 else ''\n    t = ax_a.text(x[i] + w/2 + 0.14, geo_mean, f'{gap:.0f}×{suffix}',\n                  fontsize=7.5, fontweight='bold', color=C_AR,\n                  ha='left', va='center')\n    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])\n\nax_a.set_xticks(x)\nax_a.set_xticklabels(models, fontsize=8)\nax_a.set_ylabel('GAR-ours (ThreadGate)')\nax_a.set_title('(a) TF-AR gap generalizes across architectures',\n               fontsize=9, fontweight='bold', pad=8, loc='left')\nax_a.legend(loc='upper right',\n            handletextpad=0.3, borderpad=0.35, fontsize=6.5)\n\nax_a.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))\nax_a.grid(axis='y', which='major', alpha=0.10, zorder=0)\n\n# ======================================================================\n# Panel (b): Gate profile overlay (normalized depth)\n# ======================================================================\nqwen_gates = np.array([\n    .883, .793, .996, .988, .984, .797, .961, .918,\n    .965, .934, .969, .918, .926, .941, .930, .965,\n    .941, .910, .961, .965, .973, .988, .969, .980,\n    .980, .984, .988, 1.00\n])\nllama_gates = np.array([\n    0.957, 0.973, 0.977, 0.965, 0.992, 0.969, 0.957, 0.957,\n    0.961, 0.949, 0.938, 0.934, 0.969, 0.953, 0.957, 0.965,\n    0.953, 0.961, 0.922, 0.902, 0.883, 0.863, 0.836, 0.844,\n    0.809, 0.719, 0.762, 0.805, 0.801, 0.855, 0.898, 0.934\n])\n\nqwen_depth = np.linspace(0, 1, len(qwen_gates))\nllama_depth = np.linspace(0, 1, len(llama_gates))\n\nax_b.plot(qwen_depth, qwen_gates, 'o-', color=C_TG, markersize=3.5,\n          markeredgecolor='white', markeredgewidth=0.4,\n          label='Qwen-2.5-7B (28L)', zorder=3, linewidth=1.5)\nax_b.plot(llama_depth, llama_gates, 's-', color=C_LO, markersize=3.5,\n          markeredgecolor='white', markeredgewidth=0.4,\n          label='Llama-3.1-8B (32L)', zorder=3, linewidth=1.5)\n\nax_b.axhline(1.0, color='#DDDDDD', linestyle=':', linewidth=0.6, zorder=1)\nax_b.text(0.98, 1.006, 'identity', fontsize=6, color='#BBBBBB',\n          ha='right', va='bottom')\n\nax_b.annotate('L1=.793', xy=(qwen_depth[1], qwen_gates[1]),\n              xytext=(qwen_depth[1] + 0.10, 0.755), fontsize=6,\n              color=C_TG, ha='left',\n              arrowprops=dict(arrowstyle='->', color=C_TG, lw=0.5))\nax_b.annotate('L5=.797', xy=(qwen_depth[5], qwen_gates[5]),\n              xytext=(qwen_depth[5] + 0.10, 0.76), fontsize=6,\n              color=C_TG, ha='left',\n              arrowprops=dict(arrowstyle='->', color=C_TG, lw=0.5))\n\nax_b.annotate('L25=.719', xy=(llama_depth[25], llama_gates[25]),\n              xytext=(llama_depth[25] - 0.15, 0.695), fontsize=6,\n              color=C_LO, ha='right',\n              arrowprops=dict(arrowstyle='->', color=C_LO, lw=0.5))\n\nax_b.set_xlabel('Normalized Depth (layer / L)')\nax_b.set_ylabel('Gate Value')\nax_b.set_ylim(0.68, 1.03)\nax_b.set_xlim(-0.02, 1.02)\nax_b.set_title('(b) Architecture-dependent gate patterns',\n               fontsize=9, fontweight='bold', pad=8, loc='left')\nax_b.legend(loc='lower right',\n            handletextpad=0.3, borderpad=0.35, fontsize=6.5)\nax_b.grid(axis='y', alpha=0.10, zorder=0)\n\nplt.tight_layout(h_pad=1.8)\nsave_fig(fig, 'fig_crossmodel')\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  }
}
```

</details>

---


### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I need to extract the registry data. The registry output was too large and was saved to a file. Let me use a subagent to extract the relevant metrics from the registry, and also read the table data from the experiments section. Let me also look for the main results table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "e88db9d1-7e86-4d2b-ba4d-8d25e24dfeb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uNoZQNSs1PYhUQshc861a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17215,
      "cache_read_input_tokens": 37239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17215
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

Registry too large for direct read. Launching agents to extract registry metrics and check additional data sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "66e5a3ef-43fa-4152-9fbb-fa8515a49f79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uNoZQNSs1PYhUQshc861a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17215,
      "cache_read_input_tokens": 37239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17215
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

<details open><summary>🔧 Tool call — Agent · `toolu_015ssicCAvnA5h5YRztQP8Qm`</summary>

```json
{
  "description": "Extract registry metrics for audit",
  "prompt": "Extract all experiment metrics from the registry JSON file at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt\n\nThis is a JSON file with schema: {result: string}. The `result` field contains the actual registry data as a string (likely JSON itself).\n\nI need you to extract the following for EVERY experiment entry:\n1. Experiment ID/name\n2. Status\n3. All metrics (especially GAR-ours TF, GAR-ours AR, GAR-Dongre TF, GAR-Dongre AR, PPL, TF/AR gap ratios, MMLU scores)\n4. Spec info (model, lr, batch_size, epochs, steps, LoRA rank, dataset size, seed)\n5. Any scheduled sampling related metrics\n6. Any cross-model (Llama) related metrics\n7. Any steering ($\\beta$) related metrics\n8. Any gradient statistics (cosine similarity, magnitude ratios)\n9. Any instruction retention / compliance metrics\n10. Any TRC (Turn-level Residual Coherence) values\n\nUse bash with jq or python to parse. Report ALL numbers verbatim - do not summarize or round. I need exact values for an audit.",
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
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "9c362c08-5722-477b-9d0d-136c3d871a5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uNoZQNSs1PYhUQshc861a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17215,
      "cache_read_input_tokens": 37239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17215
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

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Extract registry metrics for audit",
  "task_type": "local_agent",
  "prompt": "Extract all experiment metrics from the registry JSON file at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt\n\nThis is a JSON file with schema: {result: string}. The `result` field contains the actual registry data as a string (likely JSON itself).\n\nI need you to extract the following for EVERY experiment entry:\n1. Experiment ID/name\n2. Status\n3. All metrics (especially GAR-ours TF, GAR-ours AR, GAR-Dongre TF, GAR-Dongre AR, PPL, TF/AR gap ratios, MMLU scores)\n4. Spec info (model, lr, batch_size, epochs, steps, LoRA rank, dataset size, seed)\n5. Any scheduled sampling related metrics\n6. Any cross-model (Llama) related metrics\n7. Any steering ($\\beta$) related metrics\n8. Any gradient statistics (cosine similarity, magnitude ratios)\n9. Any instruction retention / compliance metrics\n10. Any TRC (Turn-level Residual Coherence) values\n\nUse bash with jq or python to parse. Report ALL numbers verbatim - do not summarize or round. I need exact values for an audit.",
  "uuid": "dda3d2cd-41f7-4532-b2ff-d42d948b401b",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


## Round 1

## Round 1

6 recorded events


### User

_source line 50 · 2026-05-25T20:12:48.825Z_

Extract all experiment metrics from the registry JSON file at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt

This is a JSON file with schema: {result: string}. The `result` field contains the actual registry data as a string (likely JSON itself).

I need you to extract the following for EVERY experiment entry:
1. Experiment ID/name
2. Status
3. All metrics (especially GAR-ours TF, GAR-ours AR, GAR-Dongre TF, GAR-Dongre AR, PPL, TF/AR gap ratios, MMLU scores)
4. Spec info (model, lr, batch_size, epochs, steps, LoRA rank, dataset size, seed)
5. Any scheduled sampling related metrics
6. Any cross-model (Llama) related metrics
7. Any steering ($\beta$) related metrics
8. Any gradient statistics (cosine similarity, magnitude ratios)
9. Any instruction retention / compliance metrics
10. Any TRC (Turn-level Residual Coherence) values

Use bash with jq or python to parse. Report ALL numbers verbatim - do not summarize or round. I need exact values for an audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "ff4beb4a-bfc6-4743-9700-cacfe53e0c6e"
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt",
  "usage": {
    "total_tokens": 16605,
    "tool_uses": 1,
    "duration_ms": 3975
  },
  "last_tool_name": "Read",
  "uuid": "ad2d06f2-4773-402b-906c-a9c15ebdaf70",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01633ThTkqkTj78kCzLzRs5e`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4af11985-9d25-452b-b228-b1858bb27e83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fGgg4W1CSwHoeb8KKWHtX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16598,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16598,
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

_source line 53 · 2026-05-25T20:12:53.179Z_

<details><summary>↩ Tool result · reported error · `toolu_01633ThTkqkTj78kCzLzRs5e`</summary>

```text
File content (45595 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "cca3c309-dd34-4dbf-8720-ed83e17f225a",
  "tool_use_result": "Error: File content (45595 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Agent · `toolu_0126ddH2zuvchsxkYkbVEdSy`</summary>

```json
{
  "description": "Find tables and appendix data",
  "prompt": "Search for all LaTeX table definitions in the paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/\n\n1. Find where Table 1 (tab:five-way) is defined - read the full table data\n2. Find where Table tab:gradient-crossmodel is defined\n3. Find any other tables referenced in the main text\n4. Read any appendix files that contain data referenced from the main text sections (especially appendix-hyper for hyperparameters, appendix-stats for p-values, appendix-ir for instruction retention)\n\nReport all numbers found in these tables verbatim.",
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
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "2c61b9f7-d5b0-49bf-8b0a-41830dc1cbfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014uNoZQNSs1PYhUQshc861a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17215,
      "cache_read_input_tokens": 37239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17215
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

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Find tables and appendix data",
  "task_type": "local_agent",
  "prompt": "Search for all LaTeX table definitions in the paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/\n\n1. Find where Table 1 (tab:five-way) is defined - read the full table data\n2. Find where Table tab:gradient-crossmodel is defined\n3. Find any other tables referenced in the main text\n4. Read any appendix files that contain data referenced from the main text sections (especially appendix-hyper for hyperparameters, appendix-stats for p-values, appendix-ir for instruction retention)\n\nReport all numbers found in these tables verbatim.",
  "uuid": "8b1c7a91-d766-4441-adf3-574539d7e16a",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


## Round 2

## Round 2

120 recorded events


### User

_source line 56 · 2026-05-25T20:12:53.423Z_

Search for all LaTeX table definitions in the paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/

1. Find where Table 1 (tab:five-way) is defined - read the full table data
2. Find where Table tab:gradient-crossmodel is defined
3. Find any other tables referenced in the main text
4. Read any appendix files that contain data referenced from the main text sections (especially appendix-hyper for hyperparameters, appendix-stats for p-values, appendix-ir for instruction retention)

Report all numbers found in these tables verbatim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "8e87cca6-70d3-4673-9fb6-93c54604281d"
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt",
  "usage": {
    "total_tokens": 17695,
    "tool_uses": 2,
    "duration_ms": 8576
  },
  "last_tool_name": "Read",
  "uuid": "b325d950-6e08-4345-9025-e4c344bea6bf",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01MW1mia76wzWPS75Yg7jCwY`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "34c1d83b-9063-4705-89bd-24199e343283",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014XQyb8ANEsjigCMqs5LEYZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 16598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1090,
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


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Finding **/*.tex",
  "usage": {
    "total_tokens": 16416,
    "tool_uses": 1,
    "duration_ms": 4005
  },
  "last_tool_name": "Glob",
  "uuid": "104de458-551b-4f19-b4b8-cdcc63593c34",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Glob · `toolu_01EqoCRNfFZJmyJqvyTBEAwm`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "bcf28126-d7d4-4862-8a9f-696990c0de02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011e9P1k5QGhxArXeUhz57Zx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7069,
      "cache_read_input_tokens": 9326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7069,
        "ephemeral_1h_input_tokens": 0
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

_source line 61 · 2026-05-25T20:12:57.445Z_

<details><summary>↩ Tool result · `toolu_01EqoCRNfFZJmyJqvyTBEAwm`</summary>

```text
docs/paper/background.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/method.tex
docs/paper/introduction.tex
docs/paper/analysis.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex
docs/paper/abstract.tex
docs/paper/sections/abstract.tex
docs/paper/sections/analysis.tex
docs/paper/sections/appendix.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/discussion.tex
docs/paper/sections/experiments.tex
docs/paper/sections/introduction.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "d3b77d4e-0358-4d9a-ab95-18260fa0e18b"
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-25T20:12:57.727Z_

<details><summary>↩ Tool result · reported error · `toolu_01MW1mia76wzWPS75Yg7jCwY`</summary>

```text
File content (45595 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "947dc03a-fe77-4eab-a7e6-4ee00a8b954c",
  "tool_use_result": "Error: File content (45595 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Searching for \\\\begin\\{table",
  "usage": {
    "total_tokens": 16425,
    "tool_uses": 2,
    "duration_ms": 5050
  },
  "last_tool_name": "Grep",
  "uuid": "4b6d95b7-28aa-46e0-b761-86f6c8dcaa00",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Grep · `toolu_01E8oHRege2ChAQ7VPyxiuNZ`</summary>

```json
{
  "pattern": "\\\\begin\\{table",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "f20be360-fb73-4974-bd6c-6d5141f381d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011e9P1k5QGhxArXeUhz57Zx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7069,
      "cache_read_input_tokens": 9326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7069,
        "ephemeral_1h_input_tokens": 0
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

_source line 65 · 2026-05-25T20:12:58.494Z_

<details><summary>↩ Tool result · `toolu_01E8oHRege2ChAQ7VPyxiuNZ`</summary>

```text
Found 4 files
docs/paper/sections/related_work.tex
docs/paper/sections/appendix.tex
docs/paper/analysis.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "f74c5a43-f58e-4c0d-a8d5-0092068b1320"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Searching for \\\\label\\{tab:",
  "usage": {
    "total_tokens": 16434,
    "tool_uses": 3,
    "duration_ms": 5716
  },
  "last_tool_name": "Grep",
  "uuid": "75e36acc-7a37-4171-b099-eb76c0933c6c",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Grep · `toolu_01LzGWpb9NWG3Vo2ZwgBt8GM`</summary>

```json
{
  "pattern": "\\\\label\\{tab:",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "9e7a6036-88cd-49ca-8ff1-dd3c63c8d784",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011e9P1k5QGhxArXeUhz57Zx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7069,
      "cache_read_input_tokens": 9326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7069,
        "ephemeral_1h_input_tokens": 0
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

_source line 68 · 2026-05-25T20:12:59.158Z_

<details><summary>↩ Tool result · `toolu_01LzGWpb9NWG3Vo2ZwgBt8GM`</summary>

```text
docs/paper/analysis.tex:13:\label{tab:grad-conflict}
docs/paper/experiments.tex:24:\label{tab:four-way}
docs/paper/sections/related_work.tex:16:\label{tab:five-way}
docs/paper/sections/appendix.tex:8:\label{tab:hyperparams}
docs/paper/sections/appendix.tex:50:\label{tab:loss-iterations}
docs/paper/sections/appendix.tex:90:\label{tab:ir-results}
docs/paper/sections/appendix.tex:118:\label{tab:n5-ar}
docs/paper/sections/appendix.tex:148:\label{tab:stat-tests}
docs/paper/sections/appendix.tex:182:\label{tab:llama-full}
docs/paper/sections/appendix.tex:222:\label{tab:gradient-crossmodel}
docs/paper/sections/appendix.tex:311:\label{tab:steering-full}
docs/paper/sections/appendix.tex:345:\label{tab:gate-profile}
docs/paper/sections/appendix.tex:390:\label{tab:cost}
docs/paper/sections/appendix.tex:425:\label{tab:examples}
docs/paper/sections/appendix.tex:473:\label{tab:data-stats}
docs/paper/sections/appendix.tex:533:\label{tab:kl-perhead}
docs/paper/sections/appendix.tex:558:\label{tab:gar-robust}
docs/paper/sections/appendix.tex:582:\label{tab:mmlu}
docs/paper/sections/appendix.tex:610:\label{tab:1.5b-steering}
docs/paper/sections/appendix.tex:799:\label{tab:llama-ss-steering}
docs/paper/sections/appendix.tex:821:\label{tab:llama-vs-qwen-ss}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "13188fbc-d0e7-4e18-9707-f94dce501654"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading docs/paper/sections/related_work.tex",
  "usage": {
    "total_tokens": 18399,
    "tool_uses": 4,
    "duration_ms": 10732
  },
  "last_tool_name": "Read",
  "uuid": "7e98b942-9d37-4627-8ab9-a0a5e0992b1c",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01UhVkxHwsqVeTwTyG5TDX1J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "dab6d070-5ccc-49d0-9e4e-5098f5181466",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbGm443x5f2scVH8GiAZAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1959,
      "cache_read_input_tokens": 16395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1959,
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


### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Running Count lines in registry file",
  "usage": {
    "total_tokens": 17989,
    "tool_uses": 3,
    "duration_ms": 15779
  },
  "last_tool_name": "Bash",
  "uuid": "fc3f47dd-456e-4be2-82b0-15c745344177",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Bash · `toolu_01ThjHj3X5Pn3Ti9xNXJfy6j`</summary>

```json
{
  "command": "wc -l \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt\"",
  "description": "Count lines in registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "61f40828-b14e-439d-9f68-147418ec112d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YAoLoNN5YKLsAEzSSEcBMh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 17688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 236,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
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

_source line 73 · 2026-05-25T20:13:04.160Z_

<details><summary>↩ Tool result · `toolu_01UhVkxHwsqVeTwTyG5TDX1J`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn dialogue and attention decay.}
4	Multi-turn coherence has been a persistent challenge from early dialogue systems \citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \citep{xu2022goldfish}, with benchmarks such as MT-Bench \citep{zheng2024judging} and MT-Bench-101 \citep{bai2024mtbench101} continuing to expose quality gaps at later turns \citep{laban2025lost,liu2026intent}. Most relevant to our work, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B. \citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.
5	
6	\paragraph{Gating and attention manipulation.}
7	Residual gating spans highway networks \citep{srivastava2015highway}, ReZero \citep{bachlechner2021rezero}, layer pruning \citep{gromov2024unreasonable,fan2020layerdrop}, and adaptive depth \citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \citep{hendrycks2021measuring} $+$2.03 at 15B scale; ThreadGate differs in conditioning on turn position. On the analysis side, head specialization \citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, positional bias calibration \citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \citealp{zhang2024tell}) address inference behavior; our $\beta$-steering serves a diagnostic role. PCGrad \citep{yu2020pcgrad} and CAGrad \citep{liu2021cagrad} treat gradient conflict as the root cause; we show direction conflict is a symptom, not the primary cause.
8	
9	\paragraph{Exposure bias in sequence models.}
10	Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for neural machine translation (NMT; \citealp{zhang2019bridging}), and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \citet{dou2019attention} proposed attention forcing (supervising cross-attention during NMT), and \citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.
11	
12	\begin{table*}[!t]
13	\centering
14	\small
15	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
16	\label{tab:five-way}
17	\begin{tabular}{l ccc ccc cc c}
18	\toprule
19	& \multicolumn{3}{c}{\textbf{IID (TF)}} & \multicolumn{3}{c}{\textbf{Held-out (TF)}} & \multicolumn{2}{c}{\textbf{AR ($N$\,=\,50)}} & \\
20	\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-9}
21	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
22	\midrule
23	\multicolumn{10}{l}{\emph{Baseline}} \\
24	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\scriptsize[.014,\,.024]} & --- \\
25	\midrule
26	\multicolumn{10}{l}{\emph{Gated variants}} \\
27	ThreadGate        & 0.50 & \textbf{0.02} & 2.78 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
28	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\scriptsize[.023,\,.038]} & --- \\
29	Uniform Gate      & 0.49 & 0.01 & 2.78 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
30	\midrule
31	\multicolumn{10}{l}{\emph{Ungated}} \\
32	LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
33	\bottomrule
34	\end{tabular}
35	\end{table*}
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "951c8e60-4d1e-4a58-8708-f7125c90851b"
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-25T20:13:04.762Z_

<details><summary>↩ Tool result · `toolu_01ThjHj3X5Pn3Ti9xNXJfy6j`</summary>

```text
0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "25bf9655-d485-4e94-842a-a66be49f1951"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading docs/paper/experiments.tex",
  "usage": {
    "total_tokens": 18403,
    "tool_uses": 5,
    "duration_ms": 11359
  },
  "last_tool_name": "Read",
  "uuid": "4361591b-f736-4f38-80bd-ec9e21b965d5",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2g5DZytfxLuJGdYLdZNFn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4c0e61fc-bef5-460c-ba3b-d94e18b5fb2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbGm443x5f2scVH8GiAZAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1959,
      "cache_read_input_tokens": 16395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1959,
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

_source line 77 · 2026-05-25T20:13:04.786Z_

<details><summary>↩ Tool result · `toolu_01Y2g5DZytfxLuJGdYLdZNFn`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 8) are applied to all linear layers. The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~A.
7	
8	To isolate the contribution of gating, we evaluate four configurations: (1)~\textbf{ThreadGate}: LoRA + per-layer learned gates + NTP + GAR loss; (2)~\textbf{Uniform Gate}: LoRA + a single shared gate across all layers + NTP + GAR loss; (3)~\textbf{LoRA-only}: LoRA + NTP + GAR loss, with gates fixed at 1.0 (no learned gating mechanism); (4)~\textbf{Base}: the pretrained model without any fine-tuning. Each configuration is evaluated under two teacher-forced protocols. \emph{IID evaluation} computes metrics on UltraChat text from the same distribution as training. \emph{Held-out evaluation} uses 50 non-overlapping conversations to test within-distribution generalization. We report three metrics: GAR-ours (attention to goal tokens at the last token of each assistant turn, as defined in \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (attention to goal tokens averaged across all response tokens, all layers, and all heads), and perplexity (PPL).
9	
10	\subsection{Main Results}
11	
12	Table~\ref{tab:four-way} presents the four-way ablation. The central finding is that all three fine-tuned variants converge to nearly identical performance across both evaluation settings. On held-out data, GAR-ours spans only 0.75 percentage points (pp) across ThreadGate (0.50), Uniform Gate (0.51), and LoRA-only (0.50), and PPL is identical at 2.78 for all three. This convergence replicates on IID evaluation, where GAR-ours is 0.49 for all three variants and PPL varies by at most 0.01. Neither per-layer gating (ThreadGate) nor shared gating (Uniform Gate) provides any measurable benefit over LoRA-only fine-tuning. These results hold without exception across every metric-split combination in Table~\ref{tab:four-way}.
13	
14	The Base model confirms that LoRA fine-tuning is the operative variable. GAR-ours increases from 0.01 (Base) to approximately 0.49 (all fine-tuned variants) under teacher-forced evaluation, a roughly 45-fold increase. Since all three fine-tuned variants share the same GAR auxiliary loss ($\tau = 0.5$), this convergence near the target is expected; it confirms that the loss functions normally but does not by itself demonstrate benefit from the gating mechanism. PPL improves correspondingly from 4.23 to 2.63 on IID data, which confirms that NTP training functions normally across all configurations. The three-variant convergence holds across both metrics and both evaluation splits; overfitting cannot account for a pattern this consistent.
15	
16	GAR-Dongre remains uniformly low across all conditions (0.00 for Base, 0.01--0.02 for fine-tuned variants). This is consistent with the observation of \citet{dongre2026attention} that the original GAR definition, which averages over all response tokens across all layers and heads, captures a persistently diffuse attention signal. The contrast with GAR-ours reflects measurement granularity: GAR-ours isolates the last token of each assistant turn, where learned attention steering concentrates its effect, while GAR-Dongre dilutes the signal across all positions.
17	
18	The teacher-forced GAR-ours values of 0.49--0.51 stand in sharp contrast to autoregressive generation, where GAR-ours drops to 0.016 for ThreadGate. This 30$\times$ gap between teacher-forced and model-generated evaluation is the central empirical finding of this paper. Under teacher-forcing, the model conditions on UltraChat reference text as the prefix for each response; under autoregressive generation, the prefix consists of the model's own prior outputs. The attention patterns optimized for the former distribution do not transfer to the latter, and the gating mechanism does nothing to bridge this gap. We defer the mechanistic analysis of this distribution shift to \S\ref{sec:analysis}.
19	
20	\begin{table*}[t]
21	\centering
22	\small
23	\caption{Four-way ablation on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All three fine-tuned variants converge to within 0.75\,pp on GAR-ours and 0\,pp on PPL (held-out). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}. No values are bolded because no configuration achieves a meaningful advantage.}
24	\label{tab:four-way}
25	\begin{tabular}{l ccc ccc}
26	\toprule
27	& \multicolumn{3}{c}{\textbf{IID Evaluation}} & \multicolumn{3}{c}{\textbf{Held-out Evaluation}} \\
28	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
29	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL \\
30	\midrule
31	Base          & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 \\
32	ThreadGate    & 0.49 & 0.02 & 2.63 & 0.50 & 0.02 & 2.78 \\
33	Uniform Gate  & 0.49 & 0.01 & 2.62 & 0.51 & 0.01 & 2.78 \\
34	LoRA-only     & 0.49 & 0.01 & 2.63 & 0.50 & 0.01 & 2.78 \\
35	\bottomrule
36	\end{tabular}
37	\end{table*}
38	
39	\subsection{Cross-Model Validation}
40	\label{sec:cross-model}
41	
42	To verify that the convergence pattern and the 30$\times$ training-inference gap are not specific to the Qwen architecture, we are conducting parallel experiments on Llama-3.1-8B-Instruct. Llama-3.1 differs from Qwen-2.5 in several architectural choices, including grouped-query attention with 8 KV heads and a distinct BPE tokenizer. These differences provide a meaningful test of generalization across model families. Results will be reported in the final version of this paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "b0e835bf-bb3e-4e53-be31-3f532dbd1bad"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading docs/paper/analysis.tex",
  "usage": {
    "total_tokens": 18407,
    "tool_uses": 6,
    "duration_ms": 11547
  },
  "last_tool_name": "Read",
  "uuid": "6f778e08-6f57-40e1-a4ef-62508ba680fc",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Read · `toolu_01EvTark1hcAQUxEtbkJEu2z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "8a5eb5a7-db7c-4e1f-b0ec-cddd94c5e3a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbGm443x5f2scVH8GiAZAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1959,
      "cache_read_input_tokens": 16395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1959,
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

_source line 80 · 2026-05-25T20:13:04.975Z_

<details><summary>↩ Tool result · `toolu_01EvTark1hcAQUxEtbkJEu2z`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The four-way ablation in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section investigates why. We first characterize the gradient dynamics between the two training objectives (\S\ref{subsec:gradient-conflict}), then show that the learned gates exhibit behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}). A targeted causal experiment rules out gradient direction conflict as the explanation (\S\ref{subsec:pcgrad}), and a distribution shift analysis identifies the actual failure mode (\S\ref{subsec:dist-shift}).
4	
5	\subsection{Gradient Conflict Observation}\label{subsec:gradient-conflict}
6	
7	To understand how the two loss terms interact during training, we measure the cosine similarity between $\nabla_\theta \mathcal{L}_\text{NTP}$ and $\nabla_\theta \mathcal{L}_\text{GAR}$ at each transformer layer across three training epochs. Table~\ref{tab:grad-conflict} summarizes the results.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Gradient interaction between $\mathcal{L}_\text{NTP}$ and $\mathcal{L}_\text{GAR}$ across training epochs. \textit{cos\_sim}: mean cosine similarity across layers. \textit{neg\%}: percentage of layers with negative cosine similarity. \textit{mag\_ratio}: ratio of NTP to GAR gradient magnitudes.}
13	\label{tab:grad-conflict}
14	\begin{tabular}{lccc}
15	\toprule
16	\textbf{Epoch} & \textbf{cos\_sim} & \textbf{neg\%} & \textbf{mag\_ratio} \\
17	\midrule
18	0 & $-$0.089 & 78.6 & 7.5$\times$ \\
19	1 & $-$0.054 & 71.4 & 13.7$\times$ \\
20	2 & $-$0.042 & 67.9 & 14.7$\times$ \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	Two patterns are apparent. First, the NTP and GAR gradients point in opposing directions across 68--79\% of layers throughout training. The mean cosine similarity is negative at every epoch, though it attenuates slightly from $-$0.089 to $-$0.042 as training progresses. Second, the NTP gradient magnitude dominates the GAR gradient by a factor that grows from 7.5$\times$ at epoch~0 to 14.7$\times$ at epoch~2. Direction conflict decreases while magnitude imbalance worsens. We observe these patterns as descriptive statistics of the training dynamics. This does not establish that gradient conflict causes $\mathcal{L}_\text{GAR}$ to fail; \S\ref{subsec:pcgrad} tests this hypothesis directly.
26	
27	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
28	
29	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
30	
31	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
32	
33	The practical consequence is that the gates provide almost no intervention at inference time. Across all layers, mean gate values during inference range from 0.93 to 0.98, corresponding to residual stream attenuation of only 2--7\%. This attenuation is far below what would be required for meaningful modulation, and it explains the convergence with LoRA-only in Table~\ref{tab:four-way}. Figure~\ref{fig:gate-shift}(a) visualizes the per-layer gate difference between early and late turns.
34	
35	\subsection{PCGrad Causal Exclusion}\label{subsec:pcgrad}
36	
37	The gradient conflict observed in \S\ref{subsec:gradient-conflict} raises a natural hypothesis: perhaps the opposing gradient directions between $\mathcal{L}_\text{NTP}$ and $\mathcal{L}_\text{GAR}$ prevent the GAR objective from converging. If direction conflict is the cause of $\mathcal{L}_\text{GAR}$ collapse, then eliminating direction conflict should prevent the collapse. We test this prediction using PCGrad \citep{yu2020pcgrad}.
38	
39	PCGrad projects the gradient of one task onto the normal plane of the other whenever two task gradients conflict in direction. We apply PCGrad to the gate parameters only, projecting $\nabla_\theta \mathcal{L}_\text{NTP}$ onto the orthogonal complement of $\nabla_\theta \mathcal{L}_\text{GAR}$ whenever their cosine similarity is negative. This eliminates the directional component of the conflict while leaving magnitude differences intact. PCGrad does not address magnitude imbalance (which GradNorm targets; \citealp{chen2018gradnorm}) or Nash equilibrium violations (which Nash-MTL targets; \citealp{navon2022nash}); our claim is scoped to direction conflict alone.
40	
41	The result is unambiguous. Under PCGrad, the cosine similarity between NTP and GAR gradients on gate parameters turns positive by gradient step~200 ($+$0.086), confirming that PCGrad successfully removes direction conflict. Yet $\mathcal{L}_\text{GAR}$ follows a trajectory nearly identical to the baseline (v7) and collapses in the same manner. Figure~\ref{fig:training-pcgrad}(b) overlays the $\mathcal{L}_\text{GAR}$ training curves for both conditions.
42	
43	The causal exclusion follows by \emph{modus tollens}:
44	\begin{enumerate}
45	    \item If direction conflict causes $\mathcal{L}_\text{GAR}$ collapse, then removing direction conflict should prevent the collapse.
46	    \item PCGrad removes direction conflict (cosine similarity turns positive at step~200).
47	    \item $\mathcal{L}_\text{GAR}$ collapses regardless.
48	    \item Therefore, direction conflict is not the cause of $\mathcal{L}_\text{GAR}$ collapse.
49	\end{enumerate}
50	
51	This result recharacterizes the gradient observations in \S\ref{subsec:gradient-conflict}: direction conflict between $\mathcal{L}_\text{NTP}$ and $\mathcal{L}_\text{GAR}$ is a symptom of the multi-objective optimization dynamics, not the mechanism responsible for GAR failure. The magnitude imbalance (7.5--14.7$\times$) and potential Nash equilibrium violations remain as candidate explanations that future work can test with GradNorm \citep{chen2018gradnorm} and Nash-MTL \citep{navon2022nash}.
52	
53	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
54	
55	The preceding subsections explain why the gating mechanism is ineffective during training. This subsection addresses why the learned GAR improvements fail to transfer from training to inference.
56	
57	Recall from \S\ref{sec:experiments} that teacher-forced GAR-ours reaches 0.49 for all fine-tuned variants, while autoregressive GAR-ours drops to 0.016 for ThreadGate, a 30$\times$ gap. We decompose this gap by comparing same-distribution and cross-distribution evaluation. Under same-distribution evaluation (teacher-forced UltraChat text), GAR-ours is approximately 0.49, confirming that the model has learned the intended attention pattern on the training distribution. Under cross-distribution evaluation (model-generated text), GAR-ours drops to 0.016. The training itself is sound; the failure is one of generalization.
58	
59	GAR-Dongre provides a revealing control. Across both evaluation conditions, GAR-Dongre remains uniformly low (0.01--0.02) with no distribution gap. The distribution shift selectively destroys the concentrated attention pattern captured by GAR-ours (last-token, summary-position attention) while leaving the diffuse attention pattern captured by GAR-Dongre (averaged across all positions) unaffected. This selectivity implies that the distribution shift disrupts a specific learned routing behavior rather than attention computation in general.
60	
61	The mechanism connecting training regime to distribution shift is exposure bias \citep{bengio2015scheduled}. During training, the model conditions each token prediction on ground-truth prefixes from UltraChat. At inference, it conditions on its own prior outputs. The attention patterns optimized for the former distribution do not transfer to the latter, because the statistical properties of model-generated text diverge from those of human-written reference text. The 2--7\% gate attenuation documented in \S\ref{subsec:gate-conditioning} is far too weak to compensate for this distributional mismatch.
62	
63	\citet{he2019exposure} showed that language models exhibit token-level self-recovery from exposure bias: accumulated errors in autoregressive generation do not degrade perplexity as severely as worst-case analysis predicts. Our results are consistent with this finding at the token level, as PPL remains normal across all conditions (Table~\ref{tab:four-way}). The critical distinction is between primary and auxiliary objectives. The NTP objective is robust to exposure bias because next-token prediction is the same task at both training and inference time. The GAR auxiliary objective is fragile because it optimizes an attention pattern under teacher-forced context that has no counterpart in autoregressive generation. Primary-task self-recovery does not extend to auxiliary objectives that depend on distributional properties of the input prefix. Figure~\ref{fig:gate-shift}(b) summarizes the four-model GAR comparison across evaluation conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "d80b546a-ec9a-4879-96c8-55f59278de10"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 18411,
    "tool_uses": 7,
    "duration_ms": 12249
  },
  "last_tool_name": "Read",
  "uuid": "05b28ed2-5e09-493f-8929-8bcd2bca0b15",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_019b58okJRQBUGJZUkgQKsG1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4c24d43b-39d9-4e7d-a9ab-a89c1043eeb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbGm443x5f2scVH8GiAZAM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1959,
      "cache_read_input_tokens": 16395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1959,
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

_source line 83 · 2026-05-25T20:13:05.963Z_

<details><summary>↩ Tool result · reported error · `toolu_019b58okJRQBUGJZUkgQKsG1`</summary>

```text
File content (26122 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "9bce7c61-bba3-4662-9e9e-867eb0c7579f",
  "tool_use_result": "Error: File content (26122 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Running Parse outer JSON structure and inspect result field",
  "usage": {
    "total_tokens": 18268,
    "tool_uses": 4,
    "duration_ms": 21437
  },
  "last_tool_name": "Bash",
  "uuid": "8daf8bc2-b97f-446e-92f7-2abf5b764173",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Bash · `toolu_01A8mWowKD2egcsJJEePuLSc`</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt') as f:\n    raw = json.load(f)\n\n# The outer wrapper has a 'result' field containing string\nresult_str = raw.get('result', '')\nprint(f'Type of result: {type(result_str)}')\nprint(f'Length of result string: {len(result_str)}')\nprint(f'First 500 chars: {result_str[:500]}')\n\"\n",
  "description": "Parse outer JSON structure and inspect result field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "93c56f3e-8606-4d99-a9e5-85771d67c49a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KiWy8VJrys5jNy6S9CwmGt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 17924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 277,
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

_source line 86 · 2026-05-25T20:13:10.347Z_

<details><summary>↩ Tool result · `toolu_01A8mWowKD2egcsJJEePuLSc`</summary>

```text
Type of result: &lt;class 'str'>
Length of result string: 91546
First 500 chars: {"success": true, "data": {"experiments": {"phase1a_multiseed_qwen": {"status": "DONE", "retry_count": 0, "created_at": "2026-05-25T06:15:26.051Z", "updated_at": "2026-05-25T11:20:34.089Z", "hypothesis": "Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.", "spec": {"command": "python src/train_phase2_v9_pcgrad
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "f88c30db-1e28-464d-895a-f1e34c957f8f"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 25461,
    "tool_uses": 8,
    "duration_ms": 18251
  },
  "last_tool_name": "Read",
  "uuid": "01591a42-15d0-42e3-8ea7-1d430e213ab5",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_011QAMJz5SQ1CuHi7VKKVrvQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "98be2355-eb3b-4ac6-87af-7d91a9a95e8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLzASVs7V4gRoxjyZSm1Kb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7048,
      "cache_read_input_tokens": 18354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7048,
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

_source line 89 · 2026-05-25T20:13:11.681Z_

<details><summary>↩ Tool result · `toolu_011QAMJz5SQ1CuHi7VKKVrvQ`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[t]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (96\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
69	
70	\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
71	
72	\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
73	
74	\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
75	
76	Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
77	
78	\begin{figure}[t]
79	  \centering
80	  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
81	  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
82	  \label{fig:ir-bar}
83	\end{figure}
84	
85	\FloatBarrier
86	
87	\begin{table}[t]
88	\centering\small
89	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
90	\label{tab:ir-results}
91	\begin{tabular}{lccc}
92	\toprule
93	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
94	\midrule
95	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
96	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
97	Count      & 100\%  & 100\%  & 0 \\
98	Format     & 100\%  & 100\%  & 0 \\
99	\midrule
100	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
101	\bottomrule
102	\end{tabular}
103	\end{table}
104	
105	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
106	
107	The main results (Table~\ref{tab:five-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
108	
109	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
110	
111	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
112	
113	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
114	
115	\begin{table}[t]
116	\centering\small
117	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:five-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
118	\label{tab:n5-ar}
119	\begin{tabular}{lcc}
120	\toprule
121	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:five-way}} \\
122	\midrule
123	Base & 0.012 & $-$0.007 \\
124	\midrule
125	ThreadGate & 0.016 & $-$0.048 \\
126	\;+\,PCGrad & 0.015 & $-$0.015 \\
127	Uniform Gate & 0.015 & $-$0.018 \\
128	LoRA-only & 0.025 & $-$0.012 \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	\section{Statistical Test Details}\label{sec:appendix-stats}
134	
135	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
136	
137	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
138	
139	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:five-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
140	
141	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
142	
143	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
144	
145	\begin{table}[t]
146	\centering\small
147	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
148	\label{tab:stat-tests}
149	\begin{tabular}{llcc}
150	\toprule
151	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
152	\midrule
153	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
154	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
155	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
156	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
157	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
158	\midrule
159	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
160	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
161	\midrule
162	\multicolumn{4}{l}{\emph{Instruction retention}} \\
163	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
164	GAR--compliance & Pearson & 0.007 & 0.200 \\
165	\bottomrule
166	\end{tabular}
167	\end{table}
168	
169	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
170	
171	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
172	
173	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
174	
175	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
176	
177	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
178	
179	\begin{table}[t]
180	\centering\small
181	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
182	\label{tab:llama-full}
183	\resizebox{\columnwidth}{!}{%
184	\begin{tabular}{lcccc}
185	\toprule
186	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
187	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
188	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
189	\midrule
190	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
191	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
192	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
193	\textbf{SS} & 0.477 & 2.82 & \textbf{0.166} & --- \\
194	\bottomrule
195	\end{tabular}}
196	\end{table}
197	
198	\FloatBarrier
199	
200	\begin{figure}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "32401bcd-3eed-46e1-a447-f02d1774bfcc"
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Running Parse inner JSON and list all experiment IDs",
  "usage": {
    "total_tokens": 18852,
    "tool_uses": 5,
    "duration_ms": 26530
  },
  "last_tool_name": "Bash",
  "uuid": "6c4ffffa-688b-4364-a94e-b2dc33c9871b",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_012GSK2oEWa6ch27yjRvSL25`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt') as f:\n    raw = json.load(f)\n\nresult_str = raw['result']\ndata = json.loads(result_str)\n\nexperiments = data['data']['experiments']\nprint(f\"Total experiments: {len(experiments)}\")\nprint(f\"Experiment IDs: {list(experiments.keys())}\")\nPYEOF\n",
  "description": "Parse inner JSON and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "d313dbbc-d36d-4d7d-bdf7-826718b145c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016thsbAtsC7BWPXL5fXVmEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 18201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 525,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 92 · 2026-05-25T20:13:15.436Z_

<details><summary>↩ Tool result · `toolu_012GSK2oEWa6ch27yjRvSL25`</summary>

```text
Total experiments: 60
Experiment IDs: ['phase1a_multiseed_qwen', 'p1_ss_lora_only', 'phase2_switching', 'phase2_tf_ar_switching', 'phase1a_multiseed_8runs', 'phase1b_llama_complement', 'p1_llama_ss_eval', 'p1_llama_ss_training', 'mmlu_eval_all', 'p2_llama_gradient_conflict', 'p1_tf_ar_kl_divergence', 'qwen15b_phase1_diag', 'd048_eval_ss_s456', 'd048_ss_s456', 'p0_ss_steering_eval', 'd048_eval_ss_s123', 'd048_ss_s123', 'd048_split_softmax_eval', 'd048_final_ar_eval', 'd048_queue_runner', 'd048_eval_ss_s42', 'd048_ss_s42', 'd048_ss_s42_resume', 'eval_llama_ar_n20', 'eval_llama_lora_only_s42', 'llama_lora_only_s42', 'phase2_tg_s42_v6', 'phase2_tg_s42', 'eval_v7_tg_s123', 'eval_v8b_ss_s123', 'v7_tg_s123', 'v8b_ss_s123', 'llama_tg_training', 'llama_ar_matched_eval', 'instruction_retention_test', 'llama_eval_s42', 'llama_tg_s42', 'attention_steering_gen_n50', 'phase2_tg_s42_v8b_resume', 'llama_phase1_gar_diag', 'eval_v8b_ss', 'attention_steering_eval200_tf', 'trc_baseline_v7_tg', 'attention_steering_v7_tg_gen', 'phase2_tg_s42_v8b_ss_fixed', 'phase2_tg_s42_v7', 'phase2_tg_s42_v9_pcgrad', 'phase2_lora_only_s42', 'phase2_ug_s42', 'phase2_tg_s42_v8_schedsampling', 'analysis_attention_heatmap', 'analysis_gradient_conflict', 'phase2_4way_eval_heldout', 'phase2_4way_eval', 'phase2_tg_s42_v5', 'phase2_tg_s42_v4', 'phase2_tg_s42_v3b', 'phase2_tg_s42_v3', 'phase2_tg_s42_v2', 'phase1_gar_diag']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "e29395e0-3326-4d57-a74d-0dbfda6368bb"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 31651,
    "tool_uses": 9,
    "duration_ms": 23514
  },
  "last_tool_name": "Read",
  "uuid": "a4f1c3dc-dff1-4bdb-b63e-ecce69bc6b49",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_01NvVgy4YUDZGA1bckNiwyR9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "3017c0e8-3733-41ab-bd19-1824d94c440d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRywgBwv2fYPxxm7L5CUN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6153,
      "cache_read_input_tokens": 25402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6153,
        "ephemeral_1h_input_tokens": 0
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

_source line 95 · 2026-05-25T20:13:16.943Z_

<details><summary>↩ Tool result · `toolu_01NvVgy4YUDZGA1bckNiwyR9`</summary>

```text
200	\begin{figure}[t]
201	  \centering
202	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
203	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
204	  \label{fig:crossmodel}
205	\end{figure}
206	
207	\paragraph{Cross-model summary.} Table~\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\approx$ 0.5, AR GAR $\ll$ 0.1, gap $\geq$ 7.9$\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\times$ by median for TG; mean-based range 11.2--17.2$\times$) compared to Qwen's (7.9--13.5$\times$) may reflect its deeper architecture (32 vs.\ 28 layers), which allows more layers for distributional drift to compound through.
208	
209	\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
210	
211	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
212	
213	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
214	
215	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
216	
217	\paragraph{Cross-model gradient analysis.} Table~\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\approx$\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\times$ on Qwen and 25.7$\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \emph{modus tollens} argument (\S\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.
218	
219	\begin{table}[t]
220	\centering\small
221	\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\times$.}
222	\label{tab:gradient-crossmodel}
223	\begin{tabular}{lcc}
224	\toprule
225	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
226	\midrule
227	Mean cos sim & $-$0.042 & +0.005 \\
228	Neg-layer \% & 67.9\% & 53.1\% \\
229	NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	\section{Additional Visualizations}\label{sec:appendix-viz}
235	
236	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
237	
238	\subsection{Gate Profile Heatmap}
239	
240	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
241	
242	\begin{figure}[H]
243	\centering
244	\includegraphics[width=\columnwidth]{fig_gate_profile_heatmap.pdf}
245	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
246	\label{fig:gate-heatmap}
247	\end{figure}
248	
249	\subsection{Cross-Model Gate Profile Comparison}
250	
251	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
252	
253	\begin{figure}[H]
254	\centering
255	\includegraphics[width=\columnwidth]{fig_gate_profile_crossmodel.pdf}
256	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
257	\label{fig:gate-crossmodel}
258	\end{figure}
259	
260	\subsection{Per-Turn AR GAR Decay}
261	
262	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:five-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
263	
264	\begin{figure}[H]
265	\centering
266	\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
267	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
268	\label{fig:ar-gar-perturn}
269	\end{figure}
270	
271	\subsection{Bootstrap Confidence Intervals}
272	
273	Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:five-way}.
274	
275	\begin{figure}[H]
276	  \centering
277	  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
278	  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
279	  \label{fig:bootstrap-ci}
280	\end{figure}
281	
282	\subsection{Gate Value Distributions}
283	
284	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
285	
286	\begin{figure}[H]
287	\centering
288	\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
289	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
290	\label{fig:gate-distribution}
291	\end{figure}
292	
293	\subsection{Training Loss Curves}
294	
295	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
296	
297	\begin{figure}[H]
298	\centering
299	\includegraphics[width=\columnwidth]{fig_training_loss_curves.pdf}
300	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
301	\label{fig:training-loss}
302	\end{figure}
303	
304	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
305	
306	\begin{table*}[t]
307	\centering\small
308	\caption{Full attention steering results across evaluation settings.
309	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
310	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
311	\label{tab:steering-full}
312	\begin{tabular}{r cc cc cc}
313	\toprule
314	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
315	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
316	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
317	\midrule
318	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
319	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
320	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
321	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
322	\addlinespace[3pt]
323	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
324	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
325	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
326	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
327	\bottomrule
328	\end{tabular}
329	\end{table*}
330	
331	\begin{figure}[t]
332	  \centering
333	  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
334	  \caption{Detailed $\beta$-steering trade-off ($N$\,=\,50). GAR-ours (top) increases monotonically with $\beta$; PPL (bottom) remains stable below $\beta$\,=\,3 (9\% cost), then rises sharply. The $\beta$\,=\,3 operating point (circled) achieves 8.7$\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}
335	  \label{fig:steering-standalone}
336	\end{figure}
337	
338	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
339	
340	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
341	
342	\begin{table}[t]
343	\centering\small
344	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
345	\label{tab:gate-profile}
346	\resizebox{\columnwidth}{!}{%
347	\begin{tabular}{cccccccc}
348	\toprule
349	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
350	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
351	\midrule
352	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
353	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
354	\midrule
355	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
356	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
357	\midrule
358	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
359	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
360	\bottomrule
361	\end{tabular}}
362	\end{table}
363	
364	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
365	
366	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
367	
368	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
369	
370	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
371	
372	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
373	
374	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
375	
376	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.
377	
378	\begin{figure}[t]
379	  \centering
380	  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
381	  \caption{Scheduled sampling training dynamics: sampling ratio $\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}
382	  \label{fig:ss-dynamics}
383	\end{figure}
384	
385	\section{Computational Cost Analysis}\label{sec:appendix-cost}
386	
387	\begin{table}[t]
388	\centering\small
389	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM).}
390	\label{tab:cost}
391	\resizebox{\columnwidth}{!}{%
392	\begin{tabular}{lcccc}
393	\toprule
394	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
395	\midrule
396	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
397	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
398	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
399	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "52c8b3ea-9dbd-49fe-bbfa-41a1aa3a699c"
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Running Dump all experiments with full details",
  "usage": {
    "total_tokens": 19861,
    "tool_uses": 6,
    "duration_ms": 32291
  },
  "last_tool_name": "Bash",
  "uuid": "0738ab7a-f8f2-4055-8e26-2e5deb8f2e4e",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_01DttCStKLVMmf9dyYLsvWNd`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt') as f:\n    raw = json.load(f)\n\nresult_str = raw['result']\ndata = json.loads(result_str)\nexperiments = data['data']['experiments']\n\n# Dump each experiment fully, one at a time\nfor exp_id in sorted(experiments.keys()):\n    exp = experiments[exp_id]\n    print(f\"\\n{'='*80}\")\n    print(f\"EXPERIMENT: {exp_id}\")\n    print(f\"{'='*80}\")\n    print(json.dumps(exp, indent=2, ensure_ascii=False))\n\nPYEOF\n",
  "description": "Dump all experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "677e991f-1e04-49d1-8f18-0954cbcd79bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJyHLPJbEy7mY4AFNwc5uK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 18726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1007,
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

_source line 98 · 2026-05-25T20:13:21.200Z_

<details><summary>↩ Tool result · `toolu_01DttCStKLVMmf9dyYLsvWNd`</summary>

```text
&lt;persisted-output>
Output too large (113.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt

Preview (first 2KB):
================================================================================
EXPERIMENT: analysis_attention_heatmap
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T15:03:16.154Z",
  "updated_at": "2026-05-19T15:22:24.770Z",
  "hypothesis": "四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。",
  "parent": "phase2_tg_s42_v7",
  "spec": {
    "command": "attention heatmap analysis script",
    "server": "westd-20861",
    "data_path": "standard_conversations.json",
    "data_count": 5,
    "model_name": "Qwen2.5-7B-Instruct",
    "seed": 42,
    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
    "eval_data": "standard_conversations.json (5 convs x 10 turns)",
    "checkpoint_path": "N/A (analysis)",
    "log_path": "westd-20861:/root/turn_residual_gating/runs/analysis/"
  },
  "conclusion": "success",
  "metrics": {
    "base_mean_goal_attn": 0.0136,
    "base_decay": 0.875,
    "tg_mean_goal_attn": 0.0232,
    "tg_decay": 0.777,
    "ug_mean_goal_attn": 0.0216,
    "ug_decay": 0.803,
    "lora_mean_goal_attn": 0.0216,
    "lora_decay": 0.81,
    "gating_incremental_benefit": "none"
  },
  "completed_at": "2026-05-19T15:22:24.770Z"
}

================================================================================
EXPERIMENT: analysis_gradient_conflict
================================================================================
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-19T15:03:12.230Z",
  "updated_at": "2026-05-19T15:22:23.782Z",
  "hypothesis": "NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。",
  "parent": "phase2_tg_s42_v7",
  "spec": {
    "command": "gradient conflict analysis script",
    "server": "westd-20861",
    "data_path": "v7 epoch 0/1/2 checkpoints",
    "data_count": 3,
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "dc473b8b-84c4-4d0f-9652-dbd37483309b"
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "usage": {
    "total_tokens": 21265,
    "tool_uses": 7,
    "duration_ms": 35885
  },
  "last_tool_name": "Read",
  "uuid": "2fe2d494-3240-4771-aabc-65019d64dd48",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Read · `toolu_018Ah3YDkx6WjdEDVkKDnu3t`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "627a9441-3ed3-4e5a-9588-2745b62e9689",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EZsHeALPiuuQucsgJthq5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1402,
      "cache_read_input_tokens": 19733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1402,
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

_source line 101 · 2026-05-25T20:13:24.718Z_

<details><summary>↩ Tool result · `toolu_018Ah3YDkx6WjdEDVkKDnu3t`</summary>

```text
1	
2	================================================================================
3	EXPERIMENT: analysis_attention_heatmap
4	================================================================================
5	{
6	  "status": "DONE",
7	  "retry_count": 0,
8	  "created_at": "2026-05-19T15:03:16.154Z",
9	  "updated_at": "2026-05-19T15:22:24.770Z",
10	  "hypothesis": "四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。",
11	  "parent": "phase2_tg_s42_v7",
12	  "spec": {
13	    "command": "attention heatmap analysis script",
14	    "server": "westd-20861",
15	    "data_path": "standard_conversations.json",
16	    "data_count": 5,
17	    "model_name": "Qwen2.5-7B-Instruct",
18	    "seed": 42,
19	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
20	    "eval_data": "standard_conversations.json (5 convs x 10 turns)",
21	    "checkpoint_path": "N/A (analysis)",
22	    "log_path": "westd-20861:/root/turn_residual_gating/runs/analysis/"
23	  },
24	  "conclusion": "success",
25	  "metrics": {
26	    "base_mean_goal_attn": 0.0136,
27	    "base_decay": 0.875,
28	    "tg_mean_goal_attn": 0.0232,
29	    "tg_decay": 0.777,
30	    "ug_mean_goal_attn": 0.0216,
31	    "ug_decay": 0.803,
32	    "lora_mean_goal_attn": 0.0216,
33	    "lora_decay": 0.81,
34	    "gating_incremental_benefit": "none"
35	  },
36	  "completed_at": "2026-05-19T15:22:24.770Z"
37	}
38	
39	================================================================================
40	EXPERIMENT: analysis_gradient_conflict
41	================================================================================
42	{
43	  "status": "DONE",
44	  "retry_count": 0,
45	  "created_at": "2026-05-19T15:03:12.230Z",
46	  "updated_at": "2026-05-19T15:22:23.782Z",
47	  "hypothesis": "NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。",
48	  "parent": "phase2_tg_s42_v7",
49	  "spec": {
50	    "command": "gradient conflict analysis script",
51	    "server": "westd-20861",
52	    "data_path": "v7 epoch 0/1/2 checkpoints",
53	    "data_count": 3,
54	    "model_name": "Qwen2.5-7B-Instruct",
55	    "seed": 42,
56	    "checkpoint_source": "phase2_tg_s42_v7",
57	    "eval_data": "v7 3-epoch checkpoints (gradient analysis)",
58	    "checkpoint_path": "N/A (analysis)",
59	    "log_path": "westd-20861:/root/turn_residual_gating/runs/analysis/"
60	  },
61	  "conclusion": "success",
62	  "metrics": {
63	    "epoch0_cos_sim": -0.089,
64	    "epoch1_cos_sim": -0.054,
65	    "epoch2_cos_sim": -0.042,
66	    "epoch0_neg_layers_pct": 78.6,
67	    "epoch1_neg_layers_pct": 71.4,
68	    "epoch2_neg_layers_pct": 67.9,
69	    "epoch0_mag_ratio": 7.5,
70	    "epoch1_mag_ratio": 13.7,
71	    "epoch2_mag_ratio": 14.7
72	  },
73	  "completed_at": "2026-05-19T15:22:23.782Z"
74	}
75	
76	================================================================================
77	EXPERIMENT: attention_steering_eval200_tf
78	================================================================================
79	{
80	  "status": "DONE",
81	  "retry_count": 0,
82	  "created_at": "2026-05-20T09:58:23.626Z",
83	  "updated_at": "2026-05-20T10:08:24.710Z",
84	  "hypothesis": "N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。",
85	  "parent": "attention_steering_v7_tg_gen",
86	  "spec": {
87	    "command": "python src/eval_attention_steering.py --mode tf --betas 0 2 3 4 5 10 --output-name eval200_attention_steering.json (data: eval_200/eval_200.json, 200 convs)",
88	    "server": "westd-20861",
89	    "data_path": "data/eval_200/eval_200.json",
90	    "data_count": 200,
91	    "model_name": "Qwen2.5-7B-Instruct",
92	    "seed": 42,
93	    "checkpoint_source": "phase2_tg_s42_v7",
94	    "eval_data": "data/eval_200/eval_200.json",
95	    "checkpoint_path": "checkpoints/tg_v7_s42/final",
96	    "log_path": "/tmp/eval200_steering.log"
97	  },
98	  "metrics": {
99	    "beta_0.0": {
100	      "mid_gar": 0.5353,
101	      "ppl": 2.62
102	    },
103	    "beta_2.0": {
104	      "mid_gar": 0.6112,
105	      "ppl": 2.69
106	    },
107	    "beta_3.0": {
108	      "mid_gar": 0.788,
109	      "ppl": 2.93
110	    },
111	    "beta_4.0": {
112	      "mid_gar": 0.8165,
113	      "ppl": 3.49
114	    },
115	    "beta_5.0": {
116	      "mid_gar": 0.8325,
117	      "ppl": 6.15
118	    },
119	    "beta_10.0": {
120	      "mid_gar": 0.977,
121	      "ppl": 505.21
122	    },
123	    "n_convs": 200,
124	    "mode": "tf"
125	  },
126	  "conclusion": "success",
127	  "completed_at": "2026-05-20T10:08:24.710Z"
128	}
129	
130	================================================================================
131	EXPERIMENT: attention_steering_gen_n50
132	================================================================================
133	{
134	  "status": "DONE",
135	  "retry_count": 0,
136	  "created_at": "2026-05-20T19:04:17.455Z",
137	  "updated_at": "2026-05-21T01:59:57.100Z",
138	  "hypothesis": "N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。",
139	  "parent": "attention_steering_v7_tg_gen",
140	  "spec": {
141	    "command": "CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py --checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 --output-dir runs/attention_steering/ --output-name attention_steering_gen_n50",
142	    "server": "westd-20861",
143	    "gpu": [
144	      "cuda:0"
145	    ],
146	    "data_path": "data/eval_200/eval_200.json",
147	    "data_count": 50,
148	    "model_name": "Qwen2.5-7B-Instruct + v7 TG LoRA",
149	    "seed": "N/A (eval)",
150	    "checkpoint_source": "phase2_tg_s42_v7",
151	    "eval_data": "50 conversations from eval_200.json, gen mode autoregressive",
152	    "checkpoint_path": "N/A (eval experiment)",
153	    "log_path": "/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json"
154	  },
155	  "metrics": {
156	    "corrected": true,
157	    "aggregation": "per-conv mid_gar(turns 2-7), >=3 turns only",
158	    "beta_0.0": {
159	      "mid_gar": 0.0641,
160	      "mid_gar_std": 0.0809,
161	      "ppl": 1.4324,
162	      "ppl_std": 0.1029,
163	      "n_valid": 39
164	    },
165	    "beta_2.0": {
166	      "mid_gar": 0.128,
167	      "mid_gar_std": 0.1101,
168	      "ppl": 1.4822,
169	      "ppl_std": 0.1385,
170	      "n_valid": 39
171	    },
172	    "beta_3.0": {
173	      "mid_gar": 0.5558,
174	      "mid_gar_std": 0.0601,
175	      "ppl": 1.5605,
176	      "ppl_std": 0.1719,
177	      "n_valid": 39
178	    },
179	    "beta_4.0": {
180	      "mid_gar": 0.6439,
181	      "mid_gar_std": 0.0607,
182	      "ppl": 1.6674,
183	      "ppl_std": 0.2241,
184	      "n_valid": 39
185	    },
186	    "beta_5.0": {
187	      "mid_gar": 0.7271,
188	      "mid_gar_std": 0.0605,
189	      "ppl": 1.7723,
190	      "ppl_std": 0.2693,
191	      "n_valid": 38
192	    },
193	    "beta_10.0": {
194	      "mid_gar": 0.9612,
195	      "mid_gar_std": 0.0152,
196	      "ppl": 3.4517,
197	      "ppl_std": 1.7813,
198	      "n_valid": 39
199	    },
200	    "n_convs_total": 50,
201	    "n_convs_valid": 39,
202	    "mode": "gen",
203	    "phase_transition_range": "[2, 3]"
204	  },
205	  "conclusion": "success",
206	  "notes": "原始聚合有 min_turns 截断 bug（截到 2 turns），修正后用 per-conv mid_gar(turns 2-7)。39/50 对话有 ≥3 turns 参与统计。修正后 baseline β=0 GAR 从 0.101 降到 0.064（median 0.031 与 N=5 的 0.028 一致）。Phase transition 在 β∈[2,3] 重现。β=10 corrected 0.961 ≈ N=5 的 0.959。",
207	  "completed_at": "2026-05-20T19:55:34.383Z"
208	}
209	
210	================================================================================
211	EXPERIMENT: attention_steering_v7_tg_gen
212	================================================================================
213	{
214	  "status": "DONE",
215	  "retry_count": 0,
216	  "created_at": "2026-05-20T07:07:20.607Z",
217	  "updated_at": "2026-05-20T09:30:17.530Z",
218	  "hypothesis": "推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。",
219	  "parent": "phase2_tg_s42_v7",
220	  "spec": {
221	    "command": "bash scripts/launch_attention_steering.sh gen",
222	    "server": "westd-20861",
223	    "gpu": [
224	      "cuda:0"
225	    ],
226	    "pid": "157657",
227	    "log_path": "runs/attention_steering/phase2_tg_s42_v7_attention_steering.json",
228	    "submitted_at": "2026-05-20T07:07:27.678Z",
229	    "submitted_via": "submit_training_job",
230	    "backend": "tmux",
231	    "account": "root",
232	    "data_path": "data/ShareGPT_V3_format_5convs.json",
233	    "data_count": 5,
234	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
235	    "seed": 42,
236	    "checkpoint_source": "phase2_tg_s42_v7",
237	    "eval_data": "data/ShareGPT_V3_format_5convs.json",
238	    "checkpoint_path": "checkpoints/tg_v7_s42/final",
239	    "wall_clock_seconds": 8551.2,
240	    "gpu_hours": 2.38
241	  },
242	  "conclusion": "success",
243	  "completed_at": "2026-05-20T09:29:58.880Z",
244	  "metrics": {
245	    "beta_0.0": {
246	      "mid_turns_avg_gar": 0.028,
247	      "avg_ppl": 1.409
248	    },
249	    "beta_0.5": {
250	      "mid_turns_avg_gar": 0.0287,
251	      "avg_ppl": 1.387
252	    },
253	    "beta_1.0": {
254	      "mid_turns_avg_gar": 0.0349,
255	      "avg_ppl": 1.36
256	    },
257	    "beta_2.0": {
258	      "mid_turns_avg_gar": 0.062,
259	      "avg_ppl": 1.411
260	    },
261	    "beta_5.0": {
262	      "mid_turns_avg_gar": 0.6795,
263	      "avg_ppl": 1.908
264	    },
265	    "beta_10.0": {
266	      "mid_turns_avg_gar": 0.959,
267	      "avg_ppl": 4.22
268	    },
269	    "phase_transition_range": "[2, 5]",
270	    "baseline_gar": 0.028,
271	    "max_gar_at_acceptable_ppl": 0.6795,
272	    "max_gar_at_acceptable_ppl_beta": 5
273	  },
274	  "notes": "Attention steering 闭合因果环。β=0→2: GAR 缓升 (0.028→0.062), PPL 不变 (~1.4); β=5: phase transition, GAR 跳至 0.68, PPL 升至 1.91; β=10: GAR 饱和 0.96, PPL 恶化 4.22。成功标准 (GAR>0.1 且 PPL 不严重恶化) 在 β=2 即满足。β∈[2,5] 存在 phase transition。证明：手动修正 attention 指向 goal tokens → 直接恢复 GAR → 确认 exposure bias 通过 attention 偏移导致 GAR 坍塌。"
275	}
276	
277	================================================================================
278	EXPERIMENT: d048_eval_ss_s123
279	================================================================================
280	{
281	  "status": "DONE",
282	  "retry_count": 0,
283	  "created_at": "2026-05-23T17:29:13.803Z",
284	  "updated_at": "2026-05-23T18:05:41.813Z",
285	  "hypothesis": "SS s123 eval: TF + AR N=50 + bootstrap CI to establish multi-seed SS metrics. Expect TF GAR ~0.50, AR GAR similar to s42 (0.347), confirming SS effectiveness across seeds.",
286	  "parent": "d048_ss_s123",
287	  "spec": {
288	    "command": "bash scripts/d048_eval_ss_s123.sh",
289	    "server": "westd-20861",
290	    "pid": "110052",
291	    "data_path": "/root/turn-residual-gating/data/eval_200/eval_200.json",
292	    "data_count": 200,
293	    "model_name": "Qwen/Qwen2.5-7B-Instruct + SS s123 LoRA",
294	    "seed": 123,
295	    "gpu": 0,
296	    "checkpoint_source": "/root/turn-residual-gating/runs/d048_ss_s123/epoch_2",
297	    "eval_data": "/root/turn-residual-gating/data/eval_200/eval_200.json",
298	    "checkpoint_path": "/root/turn-residual-gating/results/d048_final_ar/",
299	    "log_path": "/root/turn-residual-gating/results/d048_final_ar/"
300	  },
301	  "notes": "Cron误判修复: 原PID 109385是TF eval子进程,退出后cron 5次检测失败auto-resolved为failed。实际AR eval PID 110052仍在运行。已手动恢复RUNNING。",
302	  "conclusion": "success",
303	  "completed_at": "2026-05-23T18:05:35.103Z",
304	  "metrics": {
305	    "tf_gar_ours": 0.5536,
306	    "tf_gar_dongre": 0.4106,
307	    "tf_ppl": 2.6123,
308	    "ar_beta0_gar": 0.4231,
309	    "ar_beta0_ppl": 1.4408,
310	    "ar_beta3_gar": 0.5903,
311	    "ar_beta3_ppl": 1.607,
312	    "ar_beta5_gar": 0.7174,
313	    "ar_beta5_ppl": 1.7852,
314	    "n_convs_tf": 200,
315	    "n_convs_ar": 39
316	  }
317	}
318	
319	================================================================================
320	EXPERIMENT: d048_eval_ss_s42
321	================================================================================
322	{
323	  "status": "DONE",
324	  "retry_count": 0,
325	  "created_at": "2026-05-22T22:52:15.395Z",
326	  "updated_at": "2026-05-22T23:32:26.276Z",
327	  "spec": {
328	    "command": "bash scripts/d048_eval_ss_s42.sh",
329	    "server": "westd-20861",
330	    "gpu": [
331	      "cuda:0"
332	    ],
333	    "pid": "48241",
334	    "log_path": "/root/turn_residual_gating/runs/d048_ss_s42/eval.log",
335	    "submitted_at": "2026-05-22T22:52:15.275Z",
336	    "submitted_via": "submit_training_job",
337	    "backend": "tmux",
338	    "account": "root",
339	    "data_path": "data/ultrachat_8k + model-gen AR N=50",
340	    "data_count": 50,
341	    "model_name": "Qwen2.5-7B-Instruct (SS s42)",
342	    "seed": 42,
343	    "checkpoint_source": "runs/d048_ss_s42/epoch_2",
344	    "eval_data": "ultrachat_eval_heldout 50 + model-gen AR N=50",
345	    "checkpoint_path": "runs/d048_ss_s42/epoch_2",
346	    "wall_clock_seconds": 1365.5,
347	    "gpu_hours": 0.38
348	  },
349	  "hypothesis": "D048 multi-seed SS s42 eval: TF + AR N=50 + bootstrap CI (curve[2:]) to establish mean±std for scheduled sampling. Expect TF GAR ~0.50, AR GAR gap < 2× (vs base ~31×), PPL stable.",
350	  "parent": "d048_ss_s42",
351	  "reproduce": {
352	    "finished_at": "2026-05-22T23:12:55.735Z"
353	  },
354	  "extra": {
355	    "hook_events": [
356	      {
357	        "event": "on_complete",
358	        "action": "agent",
359	        "ts": "2026-05-22T23:12:58.142628+00:00"
360	      }
361	    ]
362	  },
363	  "metrics": {
364	    "tf": {
365	      "base_gar_ours_mid": 0.0128,
366	      "base_gar_dongre_mid": 0.0031,
367	      "base_ppl": 4.34,
368	      "base_ntp": 1.4,
369	      "tg_gar_ours_mid": 0.5025,
370	      "tg_gar_dongre_mid": 0.389,
371	      "tg_ppl": 2.78,
372	      "tg_ntp": 0.98,
373	      "baseline_mid_gar": 0.0122
374	    },
375	    "ar": {
376	      "gar_ours_mid": 0.3887,
377	      "gar_ours_ci_95": [
378	        0.3692,
379	        0.3934
380	      ],
381	      "ppl": 1.35
382	    },
383	    "gap_ratio": 1.29,
384	    "n_conversations_tf": 50,
385	    "n_conversations_ar": 5,
386	    "bootstrap_turns": "curve[2:] (turns 3-T)",
387	    "note": "AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50."
388	  },
389	  "conclusion": "success",
390	  "completed_at": "2026-05-22T23:15:00.734Z"
391	}
392	
393	================================================================================
394	EXPERIMENT: d048_eval_ss_s456
395	================================================================================
396	{
397	  "status": "DONE",
398	  "retry_count": 0,
399	  "created_at": "2026-05-24T00:38:41.913Z",
400	  "updated_at": "2026-05-24T01:19:46.692Z",
401	  "hypothesis": "SS s456 eval: TF + AR N=50 + bootstrap CI to complete 3-seed SS metrics. Together with s42 and s123, establishes mean±std for C2 reviewer requirement.",
402	  "parent": "d048_ss_s456",
403	  "spec": {
404	    "command": "bash scripts/d048_eval_ss_s456.sh",
405	    "server": "westd-20861",
406	    "pid": "129280",
407	    "data_path": "/root/turn-residual-gating/data/eval_200/eval_200.json",
408	    "data_count": 200,
409	    "model_name": "Qwen/Qwen2.5-7B-Instruct + SS s456 LoRA",
410	    "seed": 456,
411	    "gpu": 0,
412	    "checkpoint_source": "/root/turn-residual-gating/runs/d048_ss_s456/epoch_2",
413	    "eval_data": "/root/turn-residual-gating/data/eval_200/eval_200.json",
414	    "checkpoint_path": "/root/turn-residual-gating/results/d048_final_ar/",
415	    "log_path": "/root/turn-residual-gating/results/d048_final_ar/"
416	  },
417	  "conclusion": "success",
418	  "completed_at": "2026-05-24T01:19:43.693Z",
419	  "metrics": {
420	    "tf_gar_ours_mid": 0.4964,
421	    "tf_gar_dongre_mid": 0.3862,
422	    "ar_beta0_gar": 0.4325,
423	    "ar_beta0_ppl": 1.4394,
424	    "ar_beta3_gar": 0.605,
425	    "ar_beta3_ppl": 1.5868,
426	    "ar_beta5_gar": 0.7157,
427	    "ar_beta5_ppl": 1.8045,
428	    "n_convs_ar": 50
429	  }
430	}
431	
432	================================================================================
433	EXPERIMENT: d048_final_ar_eval
434	================================================================================
435	{
436	  "status": "DONE",
437	  "retry_count": 0,
438	  "created_at": "2026-05-23T03:46:23.495Z",
439	  "updated_at": "2026-05-23T03:47:01.285Z",
440	  "hypothesis": "Unified AR N=50 eval across 6 conditions (Base/TG/UG/LO/PCGrad/SS) with bootstrap CI and Wilcoxon tests to establish statistically rigorous comparisons for all claims",
441	  "spec": {
442	    "command": "bash scripts/d048_final_ar_eval.sh",
443	    "server": "westd-20861",
444	    "data_path": "data/eval_200/eval_200.json",
445	    "data_count": 200,
446	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
447	    "seed": 42,
448	    "checkpoint_source": "phase2_tg_s42_v7 / phase2_ug_s42 / phase2_lora_only_s42 / tg_v9_pcgrad_s42 / d048_ss_s42",
449	    "eval_data": "eval_200.json N=50",
450	    "checkpoint_path": "N/A (eval only)",
451	    "log_path": "runs/d048_final_ar_eval.log",
452	    "results_path": "results/d048_final_ar/"
453	  },
454	  "conclusion": "success",
455	  "completed_at": "2026-05-23T03:46:57.110Z",
456	  "metrics": {
457	    "beta0": {
458	      "base_gar": 0.019,
459	      "tg_gar": 0.064,
460	      "ug_gar": 0.033,
461	      "lo_gar": 0.037,
462	      "pcgrad_gar": 0.03,
463	      "ss_gar": 0.347
464	    },
465	    "beta3": {
466	      "base_gar": 0.531,
467	      "tg_gar": 0.556,
468	      "ss_gar": 0.593
469	    },
470	    "beta5": {
471	      "base_gar": 0.704,
472	      "tg_gar": 0.727,
473	      "ss_gar": 0.717
474	    },
475	    "wilcoxon_beta0": {
476	      "tg_vs_base_p": "<0.001",
477	      "tg_vs_base_r": 0.802,
478	      "ss_vs_tg_p": "<0.001",
479	      "ss_vs_tg_r": 0.869
480	    },
481	    "ppl": {
482	      "base": 1.447,
483	      "tg": 1.432,
484	      "ss": 1.442
485	    },
486	    "n_convs": 39
487	  }
488	}
489	
490	================================================================================
491	EXPERIMENT: d048_queue_runner
492	================================================================================
493	{
494	  "status": "PREPARING",
495	  "retry_count": 0,
496	  "created_at": "2026-05-22T23:42:35.919Z",
497	  "updated_at": "2026-05-22T23:42:39.048Z",
498	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
499	  "conclusion": "failed",
500	  "extra": {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "d9104e62-b739-4b03-8f87-b96cf600b72b"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 37586,
    "tool_uses": 10,
    "duration_ms": 34835
  },
  "last_tool_name": "Read",
  "uuid": "13d1bb62-6bac-4eb8-81c0-4d7f05837ebb",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 103_

<details open><summary>🔧 Tool call — Read · `toolu_01YbkYyqzH6Ly4yWpfsUae6T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": 399,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "84eb8edd-6b2f-4cdc-8cdc-95b14ea3780f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BoXA6uqykjHL6df8XZrPTv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5897,
      "cache_read_input_tokens": 31555,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5897,
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

_source line 104 · 2026-05-25T20:13:28.274Z_

<details><summary>↩ Tool result · `toolu_01YbkYyqzH6Ly4yWpfsUae6T`</summary>

```text
399	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
400	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
401	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
402	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
403	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
404	\midrule
405	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
406	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
407	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}
411	
412	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
413	
414	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
415	
416	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
417	
418	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
419	
420	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
421	
422	\begin{table*}[t]
423	\centering\small
424	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
425	\label{tab:examples}
426	\begin{tabular}{c p{5.5cm} p{5.5cm}}
427	\toprule
428	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
429	\midrule
430	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
431	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
432	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
433	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
434	\bottomrule
435	\end{tabular}
436	\end{table*}
437	
438	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
439	
440	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
441	
442	\begin{figure}[t]
443	  \centering
444	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
445	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient direction conflict is not the primary cause (\S\ref{subsec:pcgrad}).}
446	  \label{fig:training-pcgrad}
447	\end{figure}
448	
449	This section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \S\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.
450	
451	\paragraph{Gradient direction analysis.} Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.
452	
453	\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\rho$\,=\,$-$0.12, $p$\,=\,0.54 between gate value and conflict magnitude).
454	
455	\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\times$ at epoch~0 and 14.7$\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\% of the effective update magnitude, explaining why PCGrad is ineffective.
456	
457	\paragraph{Cross-model consistency.} Table~\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient direction conflict is not the primary cause.
458	
459	\begin{figure*}[t]
460	\centering
461	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
462	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient direction conflict as the primary cause (\S\ref{subsec:pcgrad}).}
463	\label{fig:gradient-heatmap}
464	\end{figure*}
465	
466	\section{Training Data Characteristics}\label{sec:appendix-data}
467	
468	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
469	
470	\begin{table}[t]
471	\centering\small
472	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
473	\label{tab:data-stats}
474	\begin{tabular}{lcc}
475	\toprule
476	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
477	\midrule
478	Conversations & 8,000 & 50 \\
479	Min user turns & 3 & 3 \\
480	Max sequence length & 2,048 & 2,048 \\
481	Source & UltraChat train & UltraChat train \\
482	Overlap & --- & non-overlapping \\
483	\bottomrule
484	\end{tabular}
485	\end{table}
486	
487	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
488	
489	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
490	
491	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.3$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
492	
493	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
494	
495	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\sim}$1.3$\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\ref{sec:appendix-steering-viz}).
496	
497	\begin{figure}[t]
498	\centering
499	\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
500	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
501	\label{fig:eb-scaling}
502	\end{figure}
503	
504	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
505	
506	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
507	
508	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:five-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
509	
510	\begin{figure}[t]
511	\centering
512	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
513	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
514	\label{fig:kl_ar_gar_curves}
515	\end{figure}
516	
517	\begin{figure}[t]
518	\centering
519	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
520	\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}
521	\label{fig:kl_ar_gar_bar}
522	\end{figure}
523	
524	This pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \S\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.
525	
526	\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
527	
528	To test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\text{KL}(p_\text{TF} \| p_\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\Delta\text{GAR} = |\text{GAR}_\text{TF} - \text{GAR}_\text{AR}|$. This head-level analysis provides diagnostic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.
529	
530	\begin{table}[t]
531	\centering\small
532	\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\,=\,0.743).}
533	\label{tab:kl-perhead}
534	\begin{tabular}{lcc}
535	\toprule
536	\textbf{Metric} & \textbf{Base} & \textbf{TG} \\
537	\midrule
538	Mean $\Delta$GAR & 0.012 & 0.016 \\
539	Mean KL & 0.043 & 0.054 \\
540	Corr(TF\_GAR, $\Delta$GAR) & 0.673 & 0.743 \\
541	\bottomrule
542	\end{tabular}
543	\end{table}
544	
545	\paragraph{Selective disruption.} ThreadGate exhibits 35\% larger mean $\Delta$GAR (0.016 vs.\ 0.012) and 26\% larger mean KL (0.054 vs.\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\Delta$GAR is strong for both models ($r$\,=\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.
546	
547	\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\,$>$\,0.077) and L9 (KL\,$\approx$\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.
548	
549	\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\,=\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.
550	
551	\section{GAR Definition Robustness}\label{sec:appendix-gar-robust}
552	
553	To assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\ref{tab:gar-robust}): (1)~\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\emph{all-token}: average attention from all tokens to goal tokens; (3)~\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).
554	
555	\begin{table}[t]
556	\centering\small
557	\caption{Mid-turn GAR under four alternative definitions ($N$\,=\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}
558	\label{tab:gar-robust}
559	\begin{tabular}{lccc}
560	\toprule
561	\textbf{Definition} & \textbf{Base} & \textbf{TG} & \textbf{SS} \\
562	\midrule
563	Ours (last-token) & 0.015 & \textbf{0.325} & \textbf{0.458} \\
564	All-token & 0.015 & 0.025 & \textbf{0.366} \\
565	First-token & 0.022 & 0.039 & \textbf{0.412} \\
566	Goal-only & 0.005 & \textbf{0.310} & \textbf{0.444} \\
567	\bottomrule
568	\end{tabular}
569	\end{table}
570	
571	ThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \to 0.325$; goal-only: $0.005 \to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.
572	
573	Scheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.
574	
575	\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
576	
577	To confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \citep{hendrycks2021measuring} ($N$\,=\,14{,}042 questions).
578	
579	\begin{table}[t]
580	\centering\small
581	\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\,pp of the base LoRA-only checkpoint.}
582	\label{tab:mmlu}
583	\begin{tabular}{lcc}
584	\toprule
585	\textbf{Model} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs Base} \\
586	\midrule
587	Base (LoRA-only) & 74.23 & --- \\
588	PCGrad & 73.86 & $-$0.38 \\
589	SS & 73.75 & $-$0.48 \\
590	LoRA-only & 73.57 & $-$0.66 \\
591	ThreadGate & 73.47 & $-$0.77 \\
592	Uniform Gate & 73.46 & $-$0.78 \\
593	\bottomrule
594	\end{tabular}
595	\end{table}
596	
597	All variants degrade by $<$0.8\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.
598	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "2c16b124-20d5-486e-80de-a6213ad1ecc3"
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "usage": {
    "total_tokens": 29924,
    "tool_uses": 8,
    "duration_ms": 42112
  },
  "last_tool_name": "Read",
  "uuid": "ec817c71-716c-497d-8c81-8ef5f53a2a77",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 106_

<details open><summary>🔧 Tool call — Read · `toolu_01AB3dEjv2HEPWujzarsvQae`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "f6e8a4c2-cc52-414d-b329-403386aa4223",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VABjns72b4vMRJD5JLQJYa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8624,
      "cache_read_input_tokens": 21135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8624,
        "ephemeral_1h_input_tokens": 0
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

_source line 107 · 2026-05-25T20:13:30.953Z_

<details><summary>↩ Tool result · `toolu_01AB3dEjv2HEPWujzarsvQae`</summary>

```text
500	  "extra": {
501	    "hook_events": [
502	      {
503	        "event": "on_failed",
504	        "action": "agent",
505	        "ts": "2026-05-22T23:42:38.157928+00:00"
506	      }
507	    ]
508	  },
509	  "reproduce": {
510	    "finished_at": "2026-05-22T23:42:38.522Z"
511	  }
512	}
513	
514	================================================================================
515	EXPERIMENT: d048_split_softmax_eval
516	================================================================================
517	{
518	  "status": "DONE",
519	  "retry_count": 0,
520	  "created_at": "2026-05-23T07:47:05.556Z",
521	  "updated_at": "2026-05-23T08:00:42.748Z",
522	  "hypothesis": "Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.",
523	  "spec": {
524	    "command": "python src/eval_split_softmax.py",
525	    "server": "westd-20861",
526	    "data_path": "data/eval_200/eval_200.json",
527	    "data_count": 50,
528	    "model_name": "Qwen2.5-7B-Instruct + TG v7 LoRA",
529	    "seed": 42,
530	    "checkpoint_path": "N/A (failed)",
531	    "log_path": "results/split_softmax/",
532	    "failure_reason": "Bug 1: system_prompt_len=0 hardcoded (line 373) — split-softmax has no effect. Bug 2: gen mode NaN for k=0.0/0.3/0.5/0.7. Needs code fix before re-run."
533	  },
534	  "conclusion": "failed",
535	  "completed_at": "2026-05-23T07:53:10.326Z",
536	  "notes": "2 critical bugs: (1) system_prompt_len=0 hardcoded at L373, (2) gen mode NaN for k≠1.0. Director decision 2026-05-23: not urgent, defer fix past DDL 5/25. Does not affect main paper experiments."
537	}
538	
539	================================================================================
540	EXPERIMENT: d048_ss_s123
541	================================================================================
542	{
543	  "status": "DONE",
544	  "retry_count": 0,
545	  "created_at": "2026-05-23T07:54:41.928Z",
546	  "updated_at": "2026-05-23T17:29:06.984Z",
547	  "hypothesis": "Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s123) to establish 3-seed mean±std for C2 reviewer requirement. Corrected hyperparams matching d048_ss_s456.",
548	  "parent": "d048_ss_s42",
549	  "spec": {
550	    "command": "python train_phase2_v8b.py --gate-type threadgate --seed 123 --output-dir runs/d048_ss_s123 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3",
551	    "server": "westd-20861",
552	    "pid": "84793",
553	    "data_path": "/root/turn-residual-gating/data/phase2_train.jsonl",
554	    "data_count": 2000,
555	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
556	    "seed": 123,
557	    "gpu": 0,
558	    "checkpoint_source": "Qwen/Qwen2.5-7B-Instruct (base, no prior checkpoint)",
559	    "eval_data": "N/A - this is a training experiment",
560	    "checkpoint_path": "/root/turn-residual-gating/runs/d048_ss_s123/epoch_2",
561	    "log_path": "/root/turn-residual-gating/runs/d048_ss_s123/train.log"
562	  },
563	  "conclusion": "success",
564	  "completed_at": "2026-05-23T17:29:06.984Z"
565	}
566	
567	================================================================================
568	EXPERIMENT: d048_ss_s42
569	================================================================================
570	{
571	  "status": "DONE",
572	  "retry_count": 0,
573	  "created_at": "2026-05-22T09:14:13.365Z",
574	  "updated_at": "2026-05-22T23:11:26.493Z",
575	  "hypothesis": "Scheduled sampling (ratio=0.3) with ThreadGate reduces the ~30× TF-AR GAR gap by exposing the model to its own generated text during training. Multi-seed run (s42) under D048 unified protocol to establish mean±std for statistical testing. SS is the strongest mitigation candidate (prior single-seed showed gap 31×→1.57×).",
576	  "spec": {
577	    "command": "bash -c \"cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0 2>&1 | tee ~/runs/turn_residual_gating/d048_ss_s42_resume.log\"",
578	    "server": "westd-20861",
579	    "gpu": [
580	      "cuda:0"
581	    ],
582	    "pid": "32861",
583	    "log_path": "~/runs/turn_residual_gating/d048_ss_s42.log",
584	    "submitted_at": "2026-05-22T15:59:07.519Z",
585	    "submitted_via": "submit_training_job",
586	    "backend": "tmux",
587	    "account": "root"
588	  },
589	  "reproduce": {
590	    "finished_at": "2026-05-22T15:51:53.120Z"
591	  },
592	  "failure_reason": "CUDA OOM: CUDA out of memory. Tried to allocate 424.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 218.56 MiB is free. Including non-PyTorch memory, this process has 26.13 GiB memory in use. Process 30899 has 68.62 GiB memory in use. Of the allocated",
593	  "conclusion": "success",
594	  "completed_at": "2026-05-22T15:51:54.391Z",
595	  "extra": {
596	    "hook_events": [
597	      {
598	        "event": "on_failed",
599	        "action": "agent",
600	        "ts": "2026-05-22T15:51:56.369724+00:00"
601	      }
602	    ]
603	  },
604	  "notes": "Training complete (resume v3). 23418s (6.5h) for epoch 1+2. Final: Avg Loss=0.9326, NTP=0.9320, GAR=0.0007, DIV=0.0000. Gate: mean=0.9527, std=0.0589, min=0.7383(L4), max=1.000. SS: 4750/16000 (29.7%) used, 0 fallback. Checkpoints: epoch_0, epoch_1, epoch_2, final. Gate profile consistent with prior SS runs (L4 lowest).",
605	  "metrics": {
606	    "final_avg_loss": 0.9326,
607	    "final_ntp_loss": 0.932,
608	    "final_gar_loss": 0.0007,
609	    "gate_mean": 0.9527,
610	    "gate_std": 0.0589,
611	    "gate_min": 0.7383,
612	    "gate_min_layer": "L4",
613	    "gate_max": 1,
614	    "ss_usage": "4750/16000 (29.7%)",
615	    "ss_fallback": 0,
616	    "epochs_completed": 3,
617	    "wall_clock_s": 23418,
618	    "wall_clock_h": 6.5
619	  }
620	}
621	
622	================================================================================
623	EXPERIMENT: d048_ss_s42_resume
624	================================================================================
625	{
626	  "status": "PREPARING",
627	  "retry_count": 0,
628	  "created_at": "2026-05-22T15:57:05.941Z",
629	  "updated_at": "2026-05-22T15:57:05.941Z",
630	  "spec": {
631	    "command": "bash -c \"cd /root/turn_residual_gating && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --batch-size 1 --grad-accum 8 --max-seq-len 2048 --scheduled-sampling --ss-max-ratio 0.3 --seed 42 --epochs 3 --output-dir runs/d048_ss_s42 --data-dir data/ultrachat_8k --resume runs/d048_ss_s42/epoch_0\"",
632	    "server": "westd-20861",
633	    "gpu": [
634	      "cuda:0"
635	    ],
636	    "pid": "32472",
637	    "log_path": "~/runs/turn_residual_gating/d048_ss_s42_resume.log",
638	    "submitted_at": "2026-05-22T15:57:05.791Z",
639	    "submitted_via": "submit_training_job",
640	    "backend": "tmux",
641	    "account": "root"
642	  }
643	}
644	
645	================================================================================
646	EXPERIMENT: d048_ss_s456
647	================================================================================
648	{
649	  "status": "DONE",
650	  "retry_count": 0,
651	  "created_at": "2026-05-23T03:46:14.558Z",
652	  "updated_at": "2026-05-24T00:38:35.393Z",
653	  "hypothesis": "Scheduled sampling (ratio=0.3) with ThreadGate multi-seed (s456) to establish 3-seed mean±std for C2 reviewer requirement of at least 3 seeds",
654	  "parent": "d048_ss_s42",
655	  "spec": {
656	    "command": "python train_phase2_v8b.py --seed 456 --resume runs/d048_ss_s456/epoch_0 --gate-type threadgate --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --ss-ratio 0.3",
657	    "server": "westd-20861",
658	    "pid": "112418",
659	    "data_path": "/root/turn-residual-gating/data/phase2_train.jsonl",
660	    "data_count": 2000,
661	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
662	    "seed": 456,
663	    "gpu": 0,
664	    "checkpoint_source": "Qwen/Qwen2.5-7B-Instruct (resume from epoch_0)",
665	    "eval_data": "N/A - training experiment",
666	    "checkpoint_path": "/root/turn-residual-gating/runs/d048_ss_s456/epoch_2",
667	    "log_path": "/root/turn-residual-gating/runs/d048_ss_s456/train.log"
668	  },
669	  "conclusion": "success",
670	  "completed_at": "2026-05-24T00:38:35.393Z"
671	}
672	
673	================================================================================
674	EXPERIMENT: eval_llama_ar_n20
675	================================================================================
676	{
677	  "status": "DONE",
678	  "retry_count": 0,
679	  "created_at": "2026-05-22T07:52:04.543Z",
680	  "updated_at": "2026-05-22T08:38:33.680Z",
681	  "hypothesis": "N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) autoregressive GAR estimates. N=5 suffered from outlier influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides robust mean±std.",
682	  "parent": "eval_llama_lora_only_s42",
683	  "spec": {
684	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_ar_n20.sh\"",
685	    "server": "westd-20861",
686	    "gpu": [
687	      "cuda:0"
688	    ],
689	    "pid": "312592",
690	    "log_path": "~/runs/turn_residual_gating/eval_llama_ar_n20.log",
691	    "submitted_at": "2026-05-22T07:52:13.830Z",
692	    "submitted_via": "submit_training_job",
693	    "backend": "tmux",
694	    "account": "root",
695	    "data_path": "ultrachat_200k + model-gen AR",
696	    "data_count": 20,
697	    "model_name": "Llama-3.1-8B-Instruct (Base/TG/LoRA-only)",
698	    "seed": 42,
699	    "checkpoint_source": "llama_tg_s42 + llama_lora_only_s42",
700	    "eval_data": "AR-generated 20 conversations x 4 turns",
701	    "wall_clock_seconds": 1435.6,
702	    "gpu_hours": 0.4
703	  },
704	  "reproduce": {
705	    "finished_at": "2026-05-22T08:09:48.181Z"
706	  },
707	  "extra": {
708	    "hook_events": [
709	      {
710	        "event": "on_complete",
711	        "action": "agent",
712	        "ts": "2026-05-22T08:09:50.100538+00:00"
713	      }
714	    ]
715	  },
716	  "checkpoint_path": "N/A",
717	  "log_path": "/root/runs/turn_residual_gating/eval_llama_ar_n20.log",
718	  "metrics": {
719	    "base": {
720	      "gar_ours_mean": 0.0088,
721	      "gar_ours_std": 0.0056,
722	      "gar_ours_median_per_conv": 0.0093,
723	      "gar_ours_median_per_turn_pool": 0.0071,
724	      "gar_ours_spike_ratio": "0%",
725	      "gar_dongre_mean": 0.0049,
726	      "gar_dongre_std": 0.0013,
727	      "gar_dongre_median": 0.0047,
728	      "ngar_ours_mid": 0.1019,
729	      "ngar_dongre_mid": 0.1171,
730	      "ppl": 1.293,
731	      "ppl_std": 0.07,
732	      "ntp_loss": 0.2552
733	    },
734	    "tg": {
735	      "gar_ours_mean": 0.0434,
736	      "gar_ours_std": 0.1002,
737	      "gar_ours_median_per_conv": 0.0179,
738	      "gar_ours_median_per_turn_pool": 0.0126,
739	      "gar_ours_spike_ratio": "5% (2/40 turns GAR>=0.4)",
740	      "gar_dongre_mean": 0.0183,
741	      "gar_dongre_std": 0.0198,
742	      "gar_dongre_median": 0.0152,
743	      "ngar_ours_mid": 0.5357,
744	      "ngar_dongre_mid": 0.4436,
745	      "ppl": 1.437,
746	      "ppl_std": 0.077,
747	      "ntp_loss": 0.3612
748	    },
749	    "lora_only": {
750	      "gar_ours_mean": 0.0284,
751	      "gar_ours_std": 0.0481,
752	      "gar_ours_median_per_conv": 0.0184,
753	      "gar_ours_median_per_turn_pool": 0.0133,
754	      "gar_ours_spike_ratio": "0%",
755	      "gar_dongre_mean": 0.0205,
756	      "gar_dongre_std": 0.0241,
757	      "gar_dongre_median": 0.016,
758	      "ngar_ours_mid": 0.3488,
759	      "ngar_dongre_mid": 0.4997,
760	      "ppl": 1.419,
761	      "ppl_std": 0.075,
762	      "ntp_loss": 0.3483
763	    },
764	    "n_conversations": 20,
765	    "n_turns": 4,
766	    "mid_turns_definition": "turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.",
767	    "stat_pool": "median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).",
768	    "ranking_gar_ours_mean": "TG(0.0434) > LO(0.0284) > Base(0.0088)",
769	    "ranking_gar_ours_median_per_conv": "TG(0.0179) ≈ LO(0.0184) > Base(0.0093)",
770	    "ranking_gar_ours_median_per_turn_pool": "TG(0.0126) ≈ LO(0.0133) > Base(0.0071)",
771	    "ranking_gar_dongre": "LO(0.0205) > TG(0.0183) > Base(0.0049)",
772	    "note": "Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment)."
773	  },
774	  "notes": "N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries use same definition)**. Two median levels: median_per_conv (paper §5.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 per-conversation mid-turn averages; median_per_turn_pool (TG 0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual turns. Both confirm TG ≈ LO (zero-increment). Mean (TG 0.0434 > LO 0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR≥0.4; LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). Pending paper fix: §5.5 says \"turns 2-T\" but code excludes turns 1-2; will correct to \"excluding the first two turns\" in next paper edit batch.",
775	  "conclusion": "success",
776	  "completed_at": "2026-05-22T08:16:09.384Z"
777	}
778	
779	================================================================================
780	EXPERIMENT: eval_llama_lora_only_s42
781	================================================================================
782	{
783	  "status": "DONE",
784	  "retry_count": 0,
785	  "created_at": "2026-05-22T07:40:25.352Z",
786	  "updated_at": "2026-05-22T07:51:32.758Z",
787	  "hypothesis": "LoRA-only ablation (no gate) on Llama-3.1-8B: if TG's GAR improvement comes from the gate, LoRA-only should show minimal GAR recovery vs base.",
788	  "parent": "llama_lora_only_s42",
789	  "spec": {
790	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_lora_only_s42.sh\"",
791	    "server": "westd-20861",
792	    "gpu": [
793	      "cuda:0"
794	    ],
795	    "pid": "309670",
796	    "log_path": "/root/runs/turn_residual_gating/eval_llama_lora_only_s42.log",
797	    "submitted_at": "2026-05-22T07:40:34.437Z",
798	    "submitted_via": "submit_training_job",
799	    "backend": "tmux",
800	    "account": "root",
801	    "data_path": "ultrachat_200k + model-gen",
802	    "data_count": 55,
803	    "model_name": "Llama-3.1-8B-Instruct + LoRA-only checkpoint",
804	    "seed": 42,
805	    "checkpoint_source": "llama_lora_only_s42",
806	    "eval_data": "IID heldout 50 + model-gen 5",
807	    "checkpoint_path": "runs/phase2_llama_lora_only_s42/epoch_2",
808	    "wall_clock_seconds": 650.8,
809	    "gpu_hours": 0.18
810	  },
811	  "reproduce": {
812	    "finished_at": "2026-05-22T07:45:28.637Z"
813	  },
814	  "extra": {
815	    "hook_events": [
816	      {
817	        "event": "on_complete",
818	        "action": "agent",
819	        "ts": "2026-05-22T07:45:30.556207+00:00"
820	      }
821	    ]
822	  },
823	  "metrics": {
824	    "tf": {
825	      "gar_ours": 0.4807,
826	      "gar_dongre": 0.0188,
827	      "ngar_ours": 11.8031,
828	      "ngar_dongre": 0.8261,
829	      "ppl": 2.6,
830	      "ntp_loss": 0.9366,
831	      "n_conversations": 50,
832	      "n_turns": 4
833	    },
834	    "ar": {
835	      "gar_ours": 0.0617,
836	      "gar_dongre": 0.0226,
837	      "ngar_ours": 0.6065,
838	      "ngar_dongre": 0.2537,
839	      "ppl": 1.32,
840	      "ntp_loss": 0.2787,
841	      "n_conversations": 5,
842	      "n_turns": 10
843	    },
844	    "gap_ratio_gar_ours": 7.79
845	  },
846	  "conclusion": "success",
847	  "completed_at": "2026-05-22T07:51:25.244Z"
848	}
849	
850	================================================================================
851	EXPERIMENT: eval_v7_tg_s123
852	================================================================================
853	{
854	  "status": "DONE",
855	  "retry_count": 0,
856	  "created_at": "2026-05-21T22:53:18.163Z",
857	  "updated_at": "2026-05-22T00:30:49.653Z",
858	  "spec": {
859	    "command": "bash scripts/eval_v7_tg_s123.sh",
860	    "server": "westd-20861",
861	    "gpu": [
862	      "cuda:0"
863	    ],
864	    "pid": "264869",
865	    "log_path": "/root/turn_residual_gating/logs/v7_tg_s123.log",
866	    "submitted_at": "2026-05-21T22:53:18.065Z",
867	    "submitted_via": "submit_training_job",
868	    "backend": "tmux",
869	    "account": "root",
870	    "data_path": "data/ultrachat_8k",
871	    "data_count": 8000,
872	    "model_name": "Qwen2.5-7B-Instruct",
873	    "seed": 123,
874	    "checkpoint_source": "v7_tg_s123",
875	    "eval_data": "data/ultrachat_8k",
876	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2",
877	    "wall_clock_seconds": 5844.5,
878	    "gpu_hours": 1.62
879	  },
880	  "hypothesis": "v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 一致（~32×），确认 multi-seed robustness",
881	  "parent": "v7_tg_s123",
882	  "conclusion": "success",
883	  "completed_at": "2026-05-22T00:30:42.606Z",
884	  "metrics": {
885	    "iid_tf": {
886	      "gar_ours_mid": 0.5052,
887	      "gar_dongre_mid": 0.0119,
888	      "ppl": 2.7802,
889	      "ntp": 0.9752
890	    },
891	    "modelgen_ar": {
892	      "gar_ours_mid": 0.0165,
893	      "gar_dongre_mid": 0.0177,
894	      "ppl": 1.3855,
895	      "ntp": 0.3223
896	    },
897	    "gap_ratio": 30.6,
898	    "comparison_s42": {
899	      "tf_gar_ours_delta": 0.0017,
900	      "ar_gar_ours_delta": 0.0008,
901	      "gap_ratio_delta": -1.4
902	    }
903	  }
904	}
905	
906	================================================================================
907	EXPERIMENT: eval_v8b_ss
908	================================================================================
909	{
910	  "status": "DONE",
911	  "retry_count": 0,
912	  "created_at": "2026-05-20T18:44:23.366Z",
913	  "updated_at": "2026-05-20T18:45:14.523Z",
914	  "hypothesis": "Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and model-gen contexts) closes the 30x training-inference GAR gap by reducing exposure bias, resulting in model-gen GAR significantly above v7 baseline (0.016) while preserving IID GAR and PPL.",
915	  "parent": "phase2_tg_s42_v8b_ss",
916	  "spec": {
917	    "command": "python src/eval_phase2_gar.py --checkpoint-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate",
918	    "server": "westd-20861",
919	    "data_path": "data/ultrachat_eval_heldout.json + built-in 5conv model-gen",
920	    "data_count": "50 heldout + 5 model-gen",
921	    "model_name": "Qwen2.5-7B-Instruct",
922	    "seed": 42,
923	    "checkpoint_source": "checkpoints/tg_v8b_ss_fixed_s42",
924	    "eval_data": "ultrachat_eval_heldout.json (IID) + built-in model-gen (5x10 turns)",
925	    "checkpoint_path": "checkpoints/tg_v8b_ss_fixed_s42",
926	    "log_path": "/tmp/eval_v8b_all.log"
927	  },
928	  "metrics": {
929	    "iid_gar_ours": 0.4983,
930	    "iid_gar_dongre": 0.3855,
931	    "iid_ppl": 2.78,
932	    "iid_ngar_ours": 13.5,
933	    "iid_ngar_dongre": 22.68,
934	    "modelgen_gar_ours": 0.3177,
935	    "modelgen_gar_dongre": 0.3533,
936	    "modelgen_ppl": 1.38,
937	    "modelgen_ngar_ours": 4.47,
938	    "modelgen_ngar_dongre": 5.92,
939	    "iid_turn1_gar_ours": 0.5398,
940	    "modelgen_turn1_gar_ours": 0.4333
941	  },
942	  "conclusion": "success",
943	  "completed_at": "2026-05-20T18:45:14.523Z"
944	}
945	
946	================================================================================
947	EXPERIMENT: eval_v8b_ss_s123
948	================================================================================
949	{
950	  "status": "DONE",
951	  "retry_count": 0,
952	  "created_at": "2026-05-21T21:15:52.880Z",
953	  "updated_at": "2026-05-21T22:53:15.356Z",
954	  "spec": {
955	    "command": "bash scripts/eval_v8b_ss_s123.sh",
956	    "server": "westd-20861",
957	    "gpu": [
958	      "cuda:0"
959	    ],
960	    "pid": 259767,
961	    "log_path": "runs/eval_v8b_ss_s123/",
962	    "submitted_at": "2026-05-21T21:15:52.785Z",
963	    "submitted_via": "submit_training_job",
964	    "backend": "tmux",
965	    "account": "root",
966	    "data_path": "data/ultrachat_eval_heldout.json",
967	    "data_count": 50,
968	    "model_name": "Qwen2.5-7B-Instruct",
969	    "seed": 123,
970	    "gpu_index": 0,
971	    "checkpoint_source": "checkpoints/tg_v8b_ss_s123/epoch_2",
972	    "eval_data": "ultrachat_eval_heldout + model-gen",
973	    "checkpoint_path": "checkpoints/tg_v8b_ss_s123/epoch_2",
974	    "wall_clock_seconds": 5835.7,
975	    "gpu_hours": 1.62
976	  },
977	  "hypothesis": "v8b SS model trained with s123 seed should reproduce s42 GAR metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL degradation, confirming seed robustness of the scheduled sampling approach",
978	  "parent": "v7_tg_s123",
979	  "log_path": "~/runs/turn_residual_gating/eval_v8b_ss_s123.log",
980	  "conclusion": "success",
981	  "completed_at": "2026-05-21T22:53:08.443Z",
982	  "metrics": {
983	    "iid": {
984	      "gar_ours": 0.503,
985	      "gar_dongre": 0.394,
986	      "ppl": 2.781,
987	      "ntp_loss": 0.976,
988	      "n_conv": 50,
989	      "n_turns": 3
990	    },
991	    "modelgen": {
992	      "gar_ours": 0.418,
993	      "gar_dongre": 0.441,
994	      "ppl": 1.389,
995	      "ntp_loss": 0.325,
996	      "n_conv": 5,
997	      "n_turns": 10
998	    },
999	    "gap_ratio": 1.2,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "be8505be-3071-4794-89a0-76a860e57fd7"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 44412,
    "tool_uses": 11,
    "duration_ms": 39876
  },
  "last_tool_name": "Read",
  "uuid": "caff0249-79ed-43bf-9cdf-cd771d9eaa24",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Read · `toolu_01DfqD6XPFVkCG7mE7VQzuwV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": 598,
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "3e413c86-fb09-4fe8-96e5-e9418a3b4dbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtSpLXve6W7UipiDzerpM9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6790,
      "cache_read_input_tokens": 37452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6790,
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

_source line 110 · 2026-05-25T20:13:33.600Z_

<details><summary>↩ Tool result · `toolu_01DfqD6XPFVkCG7mE7VQzuwV`</summary>

```text
598	
599	\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b}
600	
601	We validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\beta$-steering generalize to smaller models.
602	
603	\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\% GAR decline from turn~1 to mid-turns (vs.\ 70.8\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.
604	
605	\paragraph{Steering evaluation.} Table~\ref{tab:1.5b-steering} reports AR evaluation ($N$\,=\,50). We report median PPL because Base $\beta$\,=\,3 contains a catastrophic outlier (conversation~\#11, PPL\,$>$\,$10^8$) that inflates the mean.\footnote{The outlier occurs in a single conversation where $\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}
606	
607	\begin{table}[t]
608	\centering\small
609	\caption{Cross-scale $\beta$-steering on Qwen-2.5-1.5B ($N$\,=\,50, AR). PPL is median due to catastrophic Base outlier at $\beta$\,=\,3. TG eliminates outliers across all $\beta$ values.}
610	\label{tab:1.5b-steering}
611	\begin{tabular}{llcc}
612	\toprule
613	\textbf{Model} & $\beta$ & \textbf{AR GAR} & \textbf{PPL (med)} \\
614	\midrule
615	Base & 0 & 0.017 & 1.909 \\
616	TG & 0 & 0.023 & 1.897 \\
617	\midrule
618	Base & 3 & 0.120 & 2.216 \\
619	TG & 3 & 0.114 & 1.975 \\
620	\midrule
621	Base & 5 & 0.657 & 2.804 \\
622	TG & 5 & 0.715 & 2.624 \\
623	\bottomrule
624	\end{tabular}
625	\end{table}
626	
627	The steering pattern mirrors the 7B results: $\beta$\,=\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\beta$\,=\,0, TG shows a small but significant GAR advantage ($p$\,=\,0.005); at $\beta$\,=\,3, the TG--Base difference is not statistically significant ($p$\,=\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.
628	
629	\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
630	
631	Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
632	
633	\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\pm0.032$ across seeds under the held-out protocol (Table~\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\,=\,200 sample. AR GAR shows meaningful variance (std\,=\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\times$), seed 123 is intermediate (0.423, gap 1.3$\times$), and seed 456 is highest (0.433, gap 1.2$\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\beta$\,=\,5, the cross-seed variance nearly vanishes ($0.717\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.
634	
635	\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.8$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
636	
637	\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\% overhead) vs.\ 6.5 hours for seeds 42 and 456 (8\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.
638	
639	\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}
640	
641	\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}
642	
643	\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
644	
645	Tables~\ref{tab:perturn-qwen} and~\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\ref{tab:five-way}).
646	
647	\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\,=\,0.365 vs.\ 0.066 for ThreadGate), with a much flatter decay profile (15\% decline from turn~1 to turn~5 vs.\ 49\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.
648	
649	\paragraph{Llama per-turn dynamics.} On Llama (Table~\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\% decline in the $N$\,=\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\% decline in the $N$\,=\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.
650	
651	\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.
652	
653	Figures~\ref{fig:perturn-qwen-detail} and~\ref{fig:perturn-llama-detail} visualize these trajectories.
654	
655	\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}
656	
657	\begin{figure}[t]
658	  \centering
659	  \includegraphics[width=\columnwidth]{fig_perturn_qwen_detail.pdf}
660	  \caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}
661	  \label{fig:perturn-qwen-detail}
662	\end{figure}
663	
664	\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}
665	
666	\begin{figure}[t]
667	  \centering
668	  \includegraphics[width=\columnwidth]{fig_perturn_llama_detail.pdf}
669	  \caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\,=\,20, 4 turns). (b)~Extended Base decay profile ($N$\,=\,5, 10 turns), showing 90\% decline.}
670	  \label{fig:perturn-llama-detail}
671	\end{figure}
672	
673	\section{Extended Dataset Statistics}\label{sec:appendix-dataset-ext}
674	
675	Table~\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \texttt{train\_sft} split), we filter for conversations with $\geq$5 assistant turns, yielding 17,302 candidates (8.3\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.
676	
677	\paragraph{Filtering rationale.} The $\geq$5 assistant turns threshold was chosen empirically: conversations with fewer than 3 assistant turns do not exhibit measurable attention decay (turn-1 to turn-3 GAR decline $<$5\%), making them uninformative for studying multi-turn exposure bias. The 5-turn threshold provides sufficient turn depth while retaining a reasonable fraction of the corpus. The average conversation in the filtered set contains 5.6 assistant turns (range: 5--7), with a mean sequence length of 1,247 tokens after tokenization with the Qwen-2.5 tokenizer.
678	
679	\paragraph{Evaluation split design.} We maintain four non-overlapping evaluation sets to avoid contamination: (1)~the primary AR evaluation ($N$\,=\,50) uses the same conversation structure as training but with held-out conversations, enabling direct comparison of TF vs.\ AR behavior; (2)~the IID GAR diagnostic ($N$\,=\,50) uses a separate sample for ablation studies that require independent measurements; (3)~the large instruction retention set ($N$\,=\,200) provides sufficient statistical power for per-category compliance analysis across 18 constraint types; (4)~the long-conversation set ($N$\,=\,5, 10 turns each) tests scaling behavior beyond the training distribution.
680	
681	\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.
682	
683	\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}
684	
685	\section{Extended GAR Robustness Analysis}\label{sec:appendix-gar-ext}
686	
687	Table~\ref{tab:gar_robustness} and Figure~\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \S\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\textit{Goal-only}: attention to goal tokens as defined by \citet{dongre2026attention}, which restricts the target set to system-prompt tokens.
688	
689	\paragraph{Position-specific vs.\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\times$ and 1.07$\times$ respectively. All-token (5.04$\times$) and first-token (8.24$\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\leq$1.83$\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.
690	
691	\paragraph{Turn-1 vs.\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\times$, TG: 8.2$\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.
692	
693	\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}
694	
695	\begin{figure}[t]
696	  \centering
697	  \includegraphics[width=\columnwidth]{fig_gar_robustness_grouped.pdf}
698	  \caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}
699	  \label{fig:gar-robust-grouped}
700	\end{figure}
701	
702	\section{MMLU Category Breakdown}\label{sec:appendix-mmlu-ext}
703	
704	Table~\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.
705	
706	\paragraph{Per-category analysis.} The maximum per-category degradation is 1.2\,pp (ThreadGate on STEM), and no category shows systematic degradation across all variants. Notably, the ordering of variants differs across categories: ThreadGate shows the largest STEM drop but the smallest Humanities drop, while PCGrad shows the smallest overall drop despite having the worst AR GAR. This lack of correlation between GAR performance and MMLU degradation is consistent with GAR and NTP occupying largely orthogonal parameter subspaces---the LoRA adapter capacity (4.2M parameters) is sufficient to accommodate both objectives without interference.
707	
708	\paragraph{Statistical significance.} The per-category differences are small relative to the evaluation noise: with $N$\,=\,14,042 questions total ($\sim$3,500 per category), a 0.8\,pp accuracy difference corresponds to $\sim$28 questions, well within expected stochastic variation for 5-shot in-context learning. A chi-squared test comparing the best (PCGrad, 73.86\%) and worst (Uniform Gate, 73.46\%) variants yields $p$\,=\,0.503, confirming no significant difference. The category-level stability confirms that auxiliary GAR losses and gating do not selectively harm any knowledge domain.
709	
710	Figure~\ref{fig:mmlu-comparison} visualizes the per-category comparison, showing tight clustering across all variants within each category.
711	
712	\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}
713	
714	\begin{figure}[t]
715	  \centering
716	  \includegraphics[width=\columnwidth]{fig_mmlu_comparison.pdf}
717	  \caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.2\,pp of the LoRA-only baseline across all categories.}
718	  \label{fig:mmlu-comparison}
719	\end{figure}
720	
721	\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b-ext}
722	
723	Table~\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.
724	
725	\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.
726	
727	\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\sim}$57K gate parameters). Training completes in 2.1 hours vs.\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.
728	
729	\paragraph{Steering evaluation.} At $\beta$\,=\,5, ThreadGate recovers GAR to 0.715 ($p < 0.001$), closely matching the 7B result (0.727). The recovery is essentially scale-independent at the strong steering regime: the attention bias added by $\beta$-steering overwhelms any capacity differences. At $\beta$\,=\,3, the picture differs: the TG--Base difference is not statistically significant ($p$\,=\,0.815) on 1.5B, unlike the significant difference on 7B ($p$\,=\,0.039). This scale-dependent response at intermediate $\beta$ may reflect the 1.5B model's reduced capacity for fine-grained attention routing: with fewer parameters per layer, the model cannot sustain the subtle attention reweighting that $\beta$\,=\,3 attempts.
730	
731	\paragraph{Catastrophic outliers.} Base 1.5B at $\beta$\,=\,3 produces one catastrophic PPL outlier (conversation \#11, PPL $> 10^8$) caused by a degenerate repetition loop. ThreadGate produces zero such outliers across all $\beta$ values, suggesting the gate provides a stabilizing effect on attention distributions even when aggregate GAR is comparable. We report median PPL to avoid this outlier dominating the central tendency estimate.
732	
733	\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}
734	
735	\section{Extended Statistical Analysis}\label{sec:appendix-stats-ext}
736	
737	Table~\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\ref{sec:appendix-stats}.
738	
739	\paragraph{Test selection rationale.} All primary comparisons use paired Wilcoxon signed-rank tests on $N$\,=\,39 conversations (those with $\geq$3 turns from the 50-conversation held-out set). We use non-parametric tests because per-conversation GAR distributions are heavily right-skewed (skewness $>$ 2.0 for Base and PCGrad at $\beta$\,=\,0), violating normality assumptions required by parametric alternatives. The pairing structure (same conversations evaluated under different training configurations) controls for conversation-level confounds (topic difficulty, conversation length, system-prompt complexity).
740	
741	\paragraph{Effect size interpretation.} Effect sizes are computed as rank-biserial correlations ($r = Z / \sqrt{N}$), following standard practice. The largest effect is SS vs.\ TG ($r$\,=\,0.869, $p < 0.001$), a large effect by conventional thresholds ($r \geq 0.5$), confirming that scheduled sampling produces a qualitatively different outcome. The TG vs.\ Base effect ($r$\,=\,0.802) is also large, while TG vs.\ LoRA-only ($r$\,=\,0.454) is medium, reflecting the modest incremental benefit of gating over LoRA alone.
742	
743	\paragraph{Steering dose-response pattern.} At $\beta$\,=\,0, all four comparisons are significant ($p \leq 0.004$). At $\beta$\,=\,3 (the phase transition), TG vs.\ Base becomes marginally significant ($p$\,=\,0.039) and SS vs.\ TG remains significant ($p$\,=\,0.010), but TG vs.\ LoRA-only and PCGrad vs.\ TG lose significance ($p > 0.7$). At $\beta$\,=\,5, no pairwise comparison reaches significance---steering dominates and equalizes all variants. This dose-response pattern confirms that the training-time variant effects are real but small relative to the inference-time steering effect.
744	
745	\paragraph{Instruction retention.} The instruction retention analysis uses McNemar's test on $N$\,=\,54 paired constraint evaluations (18 constraint types $\times$ 3 conversations). The marginal significance ($p$\,=\,0.077) reflects the small sample size rather than a null effect: the point-biserial correlation ($r$\,=\,0.200, $p$\,=\,0.007) is significant when treating compliance as a continuous variable, and the per-category breakdown (Table~\ref{tab:ir-results}) shows a clear content-constraint improvement (+23.8\,pp).
746	
747	\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\beta$ level.
748	
749	\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}
750	
751	\section{Extended Training Dynamics}\label{sec:appendix-training-ext}
752	
753	Figure~\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.
754	
755	\paragraph{NTP loss convergence.} All fine-tuned variants converge to NTP loss ${\sim}$0.93 by epoch~3, with final-epoch values ranging from 0.929 (LoRA-only) to 0.934 (ThreadGate). PCGrad shows marginally higher variance due to gradient projection, but converges to the same terminal value. The uniformity of NTP convergence across variants---including those with auxiliary losses (ThreadGate, PCGrad) and those without (LoRA-only)---confirms that the GAR auxiliary objective does not interfere with the primary language modeling task during training.
756	
757	\paragraph{GAR loss dynamics.} GAR loss collapses to near-zero within the first epoch under teacher forcing across all variants, consistent with the auxiliary objective being easy to optimize when the model conditions on ground-truth context. This rapid convergence is a double-edged sword: while it confirms that the MSE formulation (v7) achieves stable optimization, the ease of convergence also means the model never learns to maintain attention under distributional drift. The scheduled sampling variant shows distinctive dynamics: higher initial GAR loss variance from stochastic context mixing, with occasional spikes when a particularly challenging model-generated context is sampled, followed by convergence to a similar final value.
758	
759	\paragraph{Training-inference disconnect.} The key observation is that training-time convergence is indistinguishable across variants: an observer with access only to training curves could not predict the 5.4$\times$ AR GAR difference between SS and TG. This disconnect reinforces the diagnosis that the failure occurs at the training-to-inference transition, not during optimization, and explains why architectural modifications (gating, PCGrad) that operate during training cannot address the fundamental distributional mismatch.
760	
761	\begin{figure*}[t]
762	  \centering
763	  \includegraphics[width=0.75\textwidth]{fig_training_curves_6panel.pdf}
764	  \caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}
765	  \label{fig:training-6panel}
766	\end{figure*}
767	
768	\section{Per-$\beta$ Steering Visualization}\label{sec:appendix-steering-viz}
769	
770	Figure~\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\beta$\,=\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\ref{tab:steering-full}.
771	
772	\paragraph{Unsteered baseline ($\beta$\,=\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\%). This trajectory matches the per-turn profiles in Appendix~\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.
773	
774	\paragraph{Phase transition ($\beta$\,=\,3).} Turn-1 GAR jumps to ${\sim}$0.55, but per-turn decay persists (${\sim}$15\% decline from turn~1 to turn~5). This indicates that steering partially compensates for the distributional drift but does not eliminate it: the attention bias adds a constant offset to goal-token logits, while the drift compounds multiplicatively across turns. The residual decay at $\beta$\,=\,3 explains why this operating point shows the strongest training-variant effects in the dose-response analysis (Appendix~\ref{sec:appendix-stats-ext}).
775	
776	\paragraph{Sustained recovery ($\beta$\,=\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\% PPL cost (1.43 $\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.
777	
778	\paragraph{Saturation regime ($\beta$\,=\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.
779	
780	\paragraph{Operating region.} The region $\beta \in [3, 5]$ balances GAR recovery against PPL cost, and the per-turn profiles confirm that steering must counteract an ongoing distributional drift rather than a one-time initialization failure---a key diagnostic that distinguishes exposure bias from alternative hypotheses (e.g., capacity limitations or optimization failures).
781	
782	\begin{figure}[t]
783	  \centering
784	  \includegraphics[width=\columnwidth]{fig_steering_perturn_4panel.pdf}
785	  \caption{Per-turn GAR under four $\beta$-steering strengths. At $\beta$\,=\,0, monotonic decay; at $\beta$\,=\,3, partial recovery with residual decay; at $\beta$\,=\,5, sustained high GAR; at $\beta$\,=\,10, saturation with catastrophic PPL.}
786	  \label{fig:steering-4panel}
787	\end{figure}
788	
789	\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
790	
791	Llama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\S\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\sim}$4$\times$ slower than Qwen on the same hardware (624 steps/h vs.\ ${\sim}$2{,}400 steps/h for Qwen). This is attributable to different vocabulary sizes (Llama 128K vs.\ Qwen 152K tokens) and attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).
792	
793	\paragraph{$\beta$-steering on Llama SS.}
794	Table~\ref{tab:llama-ss-steering} reports $\beta$-steering results on the Llama SS model. Unlike Qwen, $\beta$\,=\,3 does not trigger recovery on Llama (GAR 0.173 vs.\ 0.166 at $\beta$\,=\,0). At $\beta$\,=\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.
795	
796	\begin{table}[t]
797	\centering\small
798	\caption{$\beta$-steering on Llama-3.1-8B SS model ($N$\,=\,50, $T$\,=\,4).}
799	\label{tab:llama-ss-steering}
800	\begin{tabular}{@{}l ccc@{}}
801	\toprule
802	& $\beta$\,=\,0 & $\beta$\,=\,3 & $\beta$\,=\,5 \\
803	\midrule
804	AR GAR & 0.166 & 0.173 & 0.791 \\
805	\bottomrule
806	\end{tabular}
807	\end{table}
808	
809	\paragraph{Cross-model comparison.}
810	Table~\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\times$) is larger than Qwen's (1.2$\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\times$ (from 27$\times$ to 2.9$\times$) while Qwen reduces by 6.5$\times$ (from 7.8$\times$ to 1.2$\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\beta$-steering is more effective on Llama (0.791 vs.\ 0.717 at $\beta$\,=\,5), partially compensating for the weaker training-time compression.
811	
812	\paragraph{Architectural differences.}
813	Several architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.
814	
815	\paragraph{Training dynamics.}
816	The Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\sim}$0.20 at the end of epoch~2 (vs.\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\times$ $\to$ 2.9$\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.
817	
818	\begin{table}[t]
819	\raggedright\small
820	\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\ Llama-3.1-8B.}
821	\label{tab:llama-vs-qwen-ss}
822	\begin{tabular}{@{}l cc@{}}
823	\toprule
824	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
825	\midrule
826	SS epochs & 3 & 2 \\
827	TF GAR & 0.498 & 0.477 \\
828	AR GAR ($\beta$\,=\,0) & 0.401 & 0.166 \\
829	TF/AR gap & 1.2$\times$ & 2.9$\times$ \\
830	Baseline TG gap & 7.8$\times$ & 27$\times$ (median) \\
831	Gap compression & 6.5$\times$ & 9.3$\times$ \\
832	AR GAR ($\beta$\,=\,5) & 0.717 & 0.791 \\
833	TF PPL & 2.78 & 2.82 \\
834	AR PPL & 1.441 & 1.370 \\
835	\bottomrule
836	\end{tabular}
837	\end{table}
838	
839	\section{Use of AI Assistants}\label{sec:appendix-ai}
840	
841	We used Claude (Anthropic) as an AI coding and writing assistant
842	throughout this work. Specifically:
843	\begin{itemize}
844	    \item \textbf{Code:} drafting experiment scripts, data-processing
845	    pipelines, and analysis utilities; debugging and refactoring.
846	    \item \textbf{Writing:} drafting and revising paper sections,
847	    polishing prose, and reformatting LaTeX.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "1cecde4c-a196-4d89-b475-03ee98e60c4e"
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "usage": {
    "total_tokens": 39523,
    "tool_uses": 9,
    "duration_ms": 48340
  },
  "last_tool_name": "Read",
  "uuid": "84312b89-cf22-4282-ace6-428063ec4c52",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Read · `toolu_01Q4FeLTs61BJgfGf3gwRPsZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 1000,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "06b0f814-eee2-4911-aa03-dcdc24e8a067",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014srMJMT8Vos6Pr4dyAnCp5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9564,
      "cache_read_input_tokens": 29759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9564,
        "ephemeral_1h_input_tokens": 0
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

_source line 113 · 2026-05-25T20:13:37.173Z_

<details><summary>↩ Tool result · `toolu_01Q4FeLTs61BJgfGf3gwRPsZ`</summary>

```text
1000	    "base_iid_ppl": 4.338,
1001	    "base_modelgen_ppl": 1.351
1002	  }
1003	}
1004	
1005	================================================================================
1006	EXPERIMENT: instruction_retention_test
1007	================================================================================
1008	{
1009	  "status": "DONE",
1010	  "retry_count": 0,
1011	  "created_at": "2026-05-21T03:49:26.068Z",
1012	  "updated_at": "2026-05-21T03:59:31.835Z",
1013	  "hypothesis": "Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.",
1014	  "spec": {
1015	    "command": "python src/eval_instruction_retention.py --checkpoint runs/phase2_tg_s42_v7 --prompts data/instruction_retention_prompts.json --betas 0 3 --seed 42 --output results/instruction_retention.json",
1016	    "server": "westd-20861",
1017	    "data_path": "data/instruction_retention_prompts.json",
1018	    "data_count": 18,
1019	    "model_name": "Qwen2.5-7B-Instruct + v7 TG LoRA",
1020	    "seed": 42,
1021	    "checkpoint_source": "phase2_tg_s42_v7",
1022	    "eval_data": "18 instruction retention prompts, beta=[0,3], 5 turns each"
1023	  },
1024	  "conclusion": "success",
1025	  "checkpoint_path": "N/A (eval)",
1026	  "log_path": "/root/turn_residual_gating/results/instruction_retention.log",
1027	  "metrics": {
1028	    "late_turn_rate_beta0": 0.759,
1029	    "late_turn_rate_beta3": 0.87,
1030	    "late_turn_delta": 0.111,
1031	    "mcnemar_chi2": 3.125,
1032	    "mcnemar_p": 0.0771,
1033	    "gar_compliance_r": 0.2003,
1034	    "gar_compliance_p": 0.007,
1035	    "category_content_constraint": {
1036	      "beta0": 0.619,
1037	      "beta3": 0.857,
1038	      "delta": 0.238
1039	    },
1040	    "category_count_constraint": {
1041	      "beta0": 1,
1042	      "beta3": 1,
1043	      "delta": 0
1044	    },
1045	    "category_format_constraint": {
1046	      "beta0": 1,
1047	      "beta3": 1,
1048	      "delta": 0
1049	    },
1050	    "category_position_constraint": {
1051	      "beta0": 0.667,
1052	      "beta3": 0.733,
1053	      "delta": 0.067
1054	    }
1055	  },
1056	  "completed_at": "2026-05-21T03:59:31.835Z"
1057	}
1058	
1059	================================================================================
1060	EXPERIMENT: llama_ar_matched_eval
1061	================================================================================
1062	{
1063	  "status": "DONE",
1064	  "retry_count": 0,
1065	  "created_at": "2026-05-21T03:59:40.918Z",
1066	  "updated_at": "2026-05-21T04:36:23.237Z",
1067	  "hypothesis": "用 matched 设置 (N=50/T=4) 重跑 Llama AR eval，消除 TF/AR 设置差异。与 TF 结果对比得到可直接写入论文的 gap ratio，验证 TG 在 AR 模式下仍能提升 GAR。",
1068	  "parent": "llama_eval_s42",
1069	  "spec": {
1070	    "command": "bash scripts/eval_llama_ar_matched.sh",
1071	    "server": "westd-20861",
1072	    "data_path": "data/ultrachat_eval_sample.json",
1073	    "data_count": 50,
1074	    "model_name": "Meta-Llama-3.1-8B-Instruct + TG LoRA",
1075	    "seed": 42,
1076	    "checkpoint_source": "phase2_llama_tg_s42",
1077	    "eval_data": "50 UltraChat convs, T=4, AR generation, 4 conditions (base/TG x ours/Dongre)",
1078	    "checkpoint_path": "N/A (eval)",
1079	    "log_path": "runs/eval_llama_ar_matched.log"
1080	  },
1081	  "log_path": "/root/turn_residual_gating/runs/eval_llama_ar_matched.log",
1082	  "conclusion": "success",
1083	  "metrics": {
1084	    "ar_base_ours": {
1085	      "mid_gar": 0.0082,
1086	      "ngar": 0.1,
1087	      "ppl": 1.267
1088	    },
1089	    "ar_tg_ours": {
1090	      "mid_gar": 0.0388,
1091	      "ngar": 0.493,
1092	      "ppl": 1.413
1093	    },
1094	    "ar_base_dongre": {
1095	      "mid_gar": 0.0051,
1096	      "ngar": 0.12,
1097	      "ppl": 1.267
1098	    },
1099	    "ar_tg_dongre": {
1100	      "mid_gar": 0.018,
1101	      "ngar": 0.431,
1102	      "ppl": 1.413
1103	    },
1104	    "tf_reference": {
1105	      "tf_tg_ours_ngar": 11.88,
1106	      "tf_base_ours_ngar": 0.388,
1107	      "tf_tg_ours_raw": 0.4836,
1108	      "tf_tg_dongre_raw": 0.018
1109	    },
1110	    "matched_gap_analysis": {
1111	      "gar_ours_raw_gap": "12.5x (TF 0.484 / AR 0.039)",
1112	      "gar_ours_ngar_gap": "24.1x (TF 11.88 / AR 0.493)",
1113	      "gar_dongre_raw_gap": "1.002x (TF 0.018 / AR 0.018) — zero gap",
1114	      "tg_over_base_ar_ours": "4.71x",
1115	      "tg_over_base_ar_dongre": "3.54x",
1116	      "conclusion": "GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected."
1117	    }
1118	  },
1119	  "completed_at": "2026-05-21T04:28:38.504Z",
1120	  "notes": "CORRECTION (2026-05-21 04:36): Agent 之前错误地将 AR TG nGAR (0.493) 与 TF TG raw GAR (0.484) 对比，误判为 'nGAR aligns, gap is normalization artifact'。Reviewer 核实：TF TG ours nGAR = 11.88（非 0.48）。nGAR gap = 11.88 / 0.493 = 24.1×，比 raw gap (12.5×) 还大。'Normalization artifact' 分析完全错误——GAR-ours 的 gap 是真实的 exposure bias。论文绝对不能使用 normalization artifact 叙事。"
1121	}
1122	
1123	================================================================================
1124	EXPERIMENT: llama_eval_s42
1125	================================================================================
1126	{
1127	  "status": "DONE",
1128	  "retry_count": 0,
1129	  "created_at": "2026-05-21T03:29:51.255Z",
1130	  "updated_at": "2026-05-21T03:46:58.167Z",
1131	  "hypothesis": "Llama-3.1-8B TG eval: 如果 Llama TG 模型在 TF 模式下 GAR-ours 显著高于 AR 模式（如 Qwen v7 的 20-33x gap），则确认 training-inference GAR gap 跨模型泛化（C5）。同时测量 base model 作为 control。",
1132	  "parent": "llama_tg_s42",
1133	  "spec": {
1134	    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/eval_llama_tg_s42.sh 2>&1 | tee runs/eval_llama_tg_s42.log",
1135	    "server": "westd-20861",
1136	    "data_path": "data/ultrachat_eval_sample.json",
1137	    "data_count": 50,
1138	    "model_name": "Llama-3.1-8B-Instruct",
1139	    "seed": 42,
1140	    "checkpoint_source": "runs/phase2_llama_tg_s42/epoch_2",
1141	    "eval_data": "ultrachat_eval_sample"
1142	  },
1143	  "checkpoint_path": "runs/phase2_llama_tg_s42/epoch_2",
1144	  "log_path": "runs/eval_llama_tg_s42.log",
1145	  "metrics": {
1146	    "tf_base": {
1147	      "gar_ours": 0.0166,
1148	      "ngar_ours": 0.3882,
1149	      "gar_dongre": 0.0038,
1150	      "ngar_dongre": 0.163,
1151	      "ppl": 3.45,
1152	      "N": 50,
1153	      "T": 4
1154	    },
1155	    "tf_tg": {
1156	      "gar_ours": 0.4836,
1157	      "ngar_ours": 11.8818,
1158	      "gar_dongre": 0.018,
1159	      "ngar_dongre": 0.7922,
1160	      "ppl": 2.57,
1161	      "N": 50,
1162	      "T": 4
1163	    },
1164	    "ar_base": {
1165	      "gar_ours": 0.0086,
1166	      "ngar_ours": 0.0798,
1167	      "gar_dongre": 0.0118,
1168	      "ngar_dongre": 0.1265,
1169	      "ppl": 1.24,
1170	      "N": 5,
1171	      "T": 10
1172	    },
1173	    "ar_tg": {
1174	      "gar_ours": 0.0304,
1175	      "ngar_ours": 0.2632,
1176	      "gar_dongre": 0.0217,
1177	      "ngar_dongre": 0.2459,
1178	      "ppl": 1.32,
1179	      "N": 5,
1180	      "T": 10
1181	    },
1182	    "gap_ratio_tg_ours": 15.9,
1183	    "gap_ratio_base_ours": 1.93,
1184	    "gap_ratio_tg_dongre": 0.83,
1185	    "vs_qwen_v7_gap_ratio": 32.1,
1186	    "baseline_mid_gar": 0.0122
1187	  },
1188	  "conclusion": "success",
1189	  "notes": "C5 跨模型泛化确认。Llama TG GAR-ours gap 16x (TF 0.484 vs AR 0.030)，低于 Qwen v7 的 32x 但仍非常显著。Base model gap 仅 1.9x（control 通过）。注意 TF/AR eval 设定不同 (N=50/T=4 vs N=5/T=10)，可能影响绝对值对比。GAR-dongre 无明显 gap (ratio 0.83x, AR ≥ TF)，仅 GAR-ours 展现 exposure bias 效应。Gate dynamic range: L24/L28/L30 diff 最大 (0.23-0.38)，与 Qwen 类似集中在中高层。",
1190	  "completed_at": "2026-05-21T03:46:58.167Z"
1191	}
1192	
1193	================================================================================
1194	EXPERIMENT: llama_lora_only_s42
1195	================================================================================
1196	{
1197	  "status": "DONE",
1198	  "retry_count": 0,
1199	  "created_at": "2026-05-22T00:33:03.465Z",
1200	  "updated_at": "2026-05-22T07:39:06.888Z",
1201	  "hypothesis": "Llama-3.1-8B LoRA-only baseline (gate=none, 无 gating 机制): 与 Llama TG s42 对比，验证 gating 对 Llama 的增量贡献。如果 LoRA-only GAR ≈ TG GAR → gating 零增量与 Qwen 结论一致（C5 跨模型）。",
1202	  "parent": "llama_tg_s42",
1203	  "spec": {
1204	    "command": "bash scripts/launch_llama_lora_only_s42.sh",
1205	    "server": "westd-20861",
1206	    "gpu": [
1207	      "cuda:0"
1208	    ],
1209	    "pid": "271741",
1210	    "log_path": "logs/llama_lora_only_s42.log",
1211	    "submitted_at": "2026-05-22T00:33:16.591Z",
1212	    "submitted_via": "submit_training_job",
1213	    "backend": "tmux",
1214	    "account": "root",
1215	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
1216	    "data_count": 8000,
1217	    "model_name": "Meta-Llama-3.1-8B-Instruct",
1218	    "seed": 42,
1219	    "checkpoint_source": "N/A (training from scratch, ablation baseline)",
1220	    "eval_data": "N/A (training run, not eval)",
1221	    "checkpoint_path": "runs/phase2_llama_lora_only_s42/epoch_2",
1222	    "wall_clock_seconds": 25550.3,
1223	    "gpu_hours": 7.1
1224	  },
1225	  "reproduce": {
1226	    "finished_at": "2026-05-22T07:35:56.232Z"
1227	  },
1228	  "extra": {
1229	    "hook_events": [
1230	      {
1231	        "event": "on_complete",
1232	        "action": "agent",
1233	        "ts": "2026-05-22T07:35:58.740298+00:00"
1234	      }
1235	    ]
1236	  },
1237	  "conclusion": "success",
1238	  "metrics": {
1239	    "final_avg_loss": 0.9288,
1240	    "final_avg_ntp": 0.9279,
1241	    "final_avg_gar": 0.0009,
1242	    "gate_fixed": 1,
1243	    "gate_type": "none",
1244	    "wall_clock_s": 25317,
1245	    "wall_clock_h": 7.03,
1246	    "epochs_completed": 3
1247	  },
1248	  "completed_at": "2026-05-22T07:39:06.889Z"
1249	}
1250	
1251	================================================================================
1252	EXPERIMENT: llama_phase1_gar_diag
1253	================================================================================
1254	{
1255	  "status": "DONE",
1256	  "retry_count": 0,
1257	  "created_at": "2026-05-20T19:39:25.751Z",
1258	  "updated_at": "2026-05-21T01:34:36.417Z",
1259	  "hypothesis": "Llama-3.1-8B-Instruct 在 multi-turn dialogue 中也应出现 goal attention decay（与 Qwen-2.5-7B 类似），确认 attention decay 是 transformer 架构通用现象而非模型特有。Phase 1 诊断：测量 base Llama 的 per-turn GAR profile。",
1260	  "spec": {
1261	    "server": "westd-20861",
1262	    "gpu": [
1263	      "cuda:0"
1264	    ],
1265	    "account": "local",
1266	    "command": "CUDA_VISIBLE_DEVICES=0 python src/run_phase1_gar_llama.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/ --output-dir /root/turn_residual_gating/runs/phase1_llama_gar_diag --max-new-tokens 256",
1267	    "pid": "198817",
1268	    "data_path": "built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, debate)",
1269	    "data_count": 5,
1270	    "model_name": "Meta-Llama-3.1-8B-Instruct",
1271	    "seed": 42,
1272	    "checkpoint_source": "N/A (base model, no fine-tuning)",
1273	    "eval_data": "5 built-in conversations x 10 turns each, gen mode",
1274	    "checkpoint_path": "N/A",
1275	    "log_path": "/root/turn_residual_gating/logs/llama_phase1_gar_diag.log"
1276	  },
1277	  "conclusion": "success",
1278	  "metrics": {
1279	    "per_turn_gar": {
1280	      "turn_1": 0.0263,
1281	      "turn_2": 0.0183,
1282	      "turn_3": 0.0087,
1283	      "turn_4": 0.0055,
1284	      "turn_5": 0.006,
1285	      "turn_6": 0.0035,
1286	      "turn_7": 0.0038,
1287	      "turn_8": 0.0037,
1288	      "turn_9": 0.005,
1289	      "turn_10": 0.0026
1290	    },
1291	    "t1_t10_decay_pct": 90.1,
1292	    "t1_mid38_drop_pct": 80.2,
1293	    "n_topics": 5,
1294	    "model": "Meta-Llama-3.1-8B-Instruct",
1295	    "mode": "gen",
1296	    "n_conversations": 5,
1297	    "n_turns": 10
1298	  },
1299	  "completed_at": "2026-05-21T01:34:36.417Z"
1300	}
1301	
1302	================================================================================
1303	EXPERIMENT: llama_tg_s42
1304	================================================================================
1305	{
1306	  "status": "DONE",
1307	  "retry_count": 0,
1308	  "created_at": "2026-05-21T01:34:36.906Z",
1309	  "updated_at": "2026-05-21T03:28:07.022Z",
1310	  "hypothesis": "在 Llama-3.1-8B-Instruct 上训练 ThreadGate（与 Qwen v7 相同配置），验证 C5：gating mechanism 和 GAR training-inference gap 跨模型泛化。如果 Llama TG 也出现 IID GAR ≈ target 但 model-gen GAR 坍塌 → 确认 exposure bias 的跨模型通用性。",
1311	  "parent": "llama_phase1_gar_diag",
1312	  "spec": {
1313	    "command": "CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python src/train_phase2.py --model /root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct --data-dir data/ultrachat_8k --output-dir runs/phase2_llama_tg_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42",
1314	    "server": "westd-20861",
1315	    "gpu": [
1316	      "cuda:0"
1317	    ],
1318	    "pid": "199643",
1319	    "data_path": "data/ultrachat_8k",
1320	    "data_count": 8000,
1321	    "model_name": "Meta-Llama-3.1-8B-Instruct",
1322	    "seed": 42,
1323	    "checkpoint_source": "N/A (training from scratch)",
1324	    "eval_data": "N/A (training experiment)",
1325	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_llama_tg_s42",
1326	    "log_path": "/root/turn_residual_gating/logs/llama_tg_training.log"
1327	  },
1328	  "conclusion": "success",
1329	  "completed_at": "2026-05-21T03:27:55.963Z",
1330	  "metrics": {
1331	    "epochs_completed": 3,
1332	    "total_steps": 3000,
1333	    "wall_clock_seconds": 26212,
1334	    "wall_clock_hours": 7.28,
1335	    "final_avg_loss": 0.9233,
1336	    "final_avg_ntp": 0.9224,
1337	    "final_avg_gar": 0.0009,
1338	    "final_avg_div": 0,
1339	    "final_gate_mean": 0.9099,
1340	    "final_gate_std": 0.0701,
1341	    "final_gate_min": 0.7188,
1342	    "final_gate_max": 0.9922,
1343	    "gate_profile_step3000": {
1344	      "L0": 0.957,
1345	      "L1": 0.973,
1346	      "L2": 0.977,
1347	      "L3": 0.965,
1348	      "L4": 0.992,
1349	      "L5": 0.969,
1350	      "L6": 0.957,
1351	      "L7": 0.957,
1352	      "L8": 0.961,
1353	      "L9": 0.949,
1354	      "L10": 0.938,
1355	      "L11": 0.934,
1356	      "L12": 0.969,
1357	      "L13": 0.953,
1358	      "L14": 0.957,
1359	      "L15": 0.965,
1360	      "L16": 0.953,
1361	      "L17": 0.961,
1362	      "L18": 0.922,
1363	      "L19": 0.902,
1364	      "L20": 0.883,
1365	      "L21": 0.863,
1366	      "L22": 0.836,
1367	      "L23": 0.844,
1368	      "L24": 0.809,
1369	      "L25": 0.719,
1370	      "L26": 0.762,
1371	      "L27": 0.805,
1372	      "L28": 0.801,
1373	      "L29": 0.855,
1374	      "L30": 0.898,
1375	      "L31": 0.934
1376	    },
1377	    "checkpoint_size_gate_mb": 4.2,
1378	    "checkpoint_size_lora_mb": 26,
1379	    "gpu": "NVIDIA RTX PRO 6000 Blackwell",
1380	    "vram_gb": 102,
1381	    "mem_used_gb": 63.4
1382	  }
1383	}
1384	
1385	================================================================================
1386	EXPERIMENT: llama_tg_training
1387	================================================================================
1388	{
1389	  "status": "PREPARING",
1390	  "retry_count": 0,
1391	  "created_at": "2026-05-21T03:37:31.513Z",
1392	  "updated_at": "2026-05-21T09:44:18.859Z",
1393	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
1394	  "conclusion": "failed",
1395	  "extra": {
1396	    "hook_events": [
1397	      {
1398	        "event": "on_failed",
1399	        "action": "agent",
1400	        "ts": "2026-05-21T03:37:33.309826+00:00"
1401	      }
1402	    ]
1403	  },
1404	  "notes": "INVALIDATED: Phantom duplicate of llama_tg_s42 (same PID 199643, same experiment). Created by Worker in global registry, duplicated to project registry. Canonical entry is llama_tg_s42 (DONE/success)."
1405	}
1406	
1407	================================================================================
1408	EXPERIMENT: mmlu_eval_all
1409	================================================================================
1410	{
1411	  "status": "DONE",
1412	  "retry_count": 0,
1413	  "created_at": "2026-05-23T06:45:04.153Z",
1414	  "updated_at": "2026-05-24T07:23:08.289Z",
1415	  "hypothesis": "ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.",
1416	  "spec": {
1417	    "command": "python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5",
1418	    "server": "westd-20861",
1419	    "data_path": "MMLU benchmark (5-shot)",
1420	    "data_count": 14042,
1421	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1422	    "seed": 42,
1423	    "checkpoint_source": "base/lo/ug/tg/pcgrad/ss checkpoints",
1424	    "eval_data": "MMLU 5-shot",
1425	    "checkpoint_path": "results/mmlu/",
1426	    "log_path": "logs/gpu_chain_next.log"
1427	  },
1428	  "conclusion": "success",
1429	  "metrics": {
1430	    "base_qwen": 0.7423,
1431	    "pcgrad_v9_s42": 0.7386,
1432	    "ss_v8b_s42": 0.7375,
1433	    "lo_s42": 0.7357,
1434	    "tg_v7_s42": 0.7347,
1435	    "ug_s42": 0.7346
1436	  },
1437	  "completed_at": "2026-05-24T06:53:52.873Z"
1438	}
1439	
1440	================================================================================
1441	EXPERIMENT: p0_ss_steering_eval
1442	================================================================================
1443	{
1444	  "status": "PREPARING",
1445	  "retry_count": 0,
1446	  "created_at": "2026-05-23T19:37:39.883Z",
1447	  "updated_at": "2026-05-23T19:57:38.851Z",
1448	  "hypothesis": "SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.",
1449	  "parent": "d048_eval_ss_s42",
1450	  "conclusion": "killed",
1451	  "notes": "Cancelled: ss_s42_ar_n50.json already contains SS+steering data at β=0,3,5. Results show SS and steering do not stack (β=5: SS 0.717 vs TG-only 0.727). Director decision: skip, use existing data."
1452	}
1453	
1454	================================================================================
1455	EXPERIMENT: p1_llama_ss_eval
1456	================================================================================
1457	{
1458	  "status": "DONE",
1459	  "retry_count": 0,
1460	  "created_at": "2026-05-24T15:53:29.650Z",
1461	  "updated_at": "2026-05-24T17:12:44.175Z",
1462	  "hypothesis": "Llama SS (2-epoch) reduces the TF-AR GAR gap on Llama-3.1-8B, confirming SS as model-general mitigation (C4+C5). Eval: TF+AR N=50 β=0/3/5.",
1463	  "spec": {
1464	    "command": "bash scripts/p1_llama_ss_eval.sh",
1465	    "server": "westd-20861",
1466	    "data_path": "/root/turn-residual-gating/data/eval_50.json",
1467	    "data_count": 50,
1468	    "model_name": "meta-llama/Llama-3.1-8B-Instruct",
1469	    "seed": 42,
1470	    "checkpoint_source": "runs/p1_llama_ss_s42/epoch_1/",
1471	    "log_path": "runs/p1_llama_ss_eval.log",
1472	    "pid": 178624,
1473	    "checkpoint_path": "results/llama_ss_eval/"
1474	  },
1475	  "conclusion": "success",
1476	  "metrics": {
1477	    "ss_tf_gar": 0.477,
1478	    "ss_tf_ppl": 2.82,
1479	    "ss_ar_b0_gar": 0.1662,
1480	    "ss_ar_b0_ppl": 1.37,
1481	    "ss_ar_b5_gar": 0.7905,
1482	    "ss_ar_b5_ppl": 1.81,
1483	    "base_ar_gar": 0.0179,
1484	    "base_ar_ppl": 1.22,
1485	    "tf_ar_gap": 2.87
1486	  },
1487	  "completed_at": "2026-05-24T17:12:44.175Z"
1488	}
1489	
1490	================================================================================
1491	EXPERIMENT: p1_llama_ss_training
1492	================================================================================
1493	{
1494	  "status": "DONE",
1495	  "retry_count": 0,
1496	  "created_at": "2026-05-23T19:37:48.689Z",
1497	  "updated_at": "2026-05-24T15:53:21.654Z",
1498	  "hypothesis": "SS is effective on Qwen (gap 8x to 1.4x). If SS also reduces the TF-AR gap on Llama-3.1-8B, it confirms SS as a model-general mitigation, strengthening C4 (mitigation) and C5 (cross-model) claims.",
1499	  "spec": {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "1792948d-c5bd-4879-b4bc-435f309b3e33"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Finding **/*.tex",
  "usage": {
    "total_tokens": 54266,
    "tool_uses": 12,
    "duration_ms": 44566
  },
  "last_tool_name": "Glob",
  "uuid": "aad2527c-2053-4919-ad12-27b05851c057",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — Glob · `toolu_01HEsGgY7Voi94tgiGejiPVE`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "f6bc7fa4-5b56-4f6e-8cdf-431b4566973c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CtE91nK3SZ13aL3cikRhf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9846,
      "cache_read_input_tokens": 44242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9846,
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

_source line 116 · 2026-05-25T20:13:38.001Z_

<details><summary>↩ Tool result · `toolu_01HEsGgY7Voi94tgiGejiPVE`</summary>

```text
artifacts/appendix_expansion/tab_gar_robustness.tex
artifacts/appendix_expansion/tab_statistical_tests.tex
artifacts/appendix_expansion/tab_perseed_ss.tex
artifacts/appendix_expansion/tab_perseed_tg.tex
artifacts/appendix_expansion/tab_perturn_qwen.tex
artifacts/appendix_expansion/tab_mmlu_detail.tex
artifacts/appendix_expansion/tab_qwen15b_results.tex
artifacts/appendix_expansion/tab_crossmodel_detail.tex
artifacts/appendix_expansion/tab_dataset_stats.tex
artifacts/appendix_expansion/tab_perturn_llama.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "2181b971-99ee-4194-bf4b-af45d57108b5"
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
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "usage": {
    "total_tokens": 48969,
    "tool_uses": 10,
    "duration_ms": 55079
  },
  "last_tool_name": "Read",
  "uuid": "8581c9c0-b5aa-420d-989a-5d968800f248",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 118_

<details open><summary>🔧 Tool call — Read · `toolu_01KvEkAMwP9JPNpZa2MxrLKL`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 1500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "06691c56-d065-4bae-9fb4-76470d88ed67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeD7dWYL8DNWhgtcdmTFmN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9410,
      "cache_read_input_tokens": 39323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9410,
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

_source line 119 · 2026-05-25T20:13:43.914Z_

<details><summary>↩ Tool result · `toolu_01KvEkAMwP9JPNpZa2MxrLKL`</summary>

```text
1500	    "command": "bash scripts/p1_llama_ss_train.sh",
1501	    "server": "westd-20861",
1502	    "data_path": "/root/turn-residual-gating/data/train_400.json",
1503	    "data_count": 400,
1504	    "model_name": "meta-llama/Llama-3.1-8B-Instruct",
1505	    "seed": 42,
1506	    "checkpoint_path": "runs/llama_ss_s42/",
1507	    "log_path": "logs/p1_llama_ss_training.log",
1508	    "pid": 158507,
1509	    "hyperparams": {
1510	      "lr": "2e-4",
1511	      "batch_size": 1,
1512	      "grad_accum": 8,
1513	      "epochs": 3,
1514	      "ss_max_ratio": 0.3,
1515	      "lora_rank": 16
1516	    }
1517	  },
1518	  "conclusion": "success",
1519	  "completed_at": "2026-05-24T15:53:21.654Z"
1520	}
1521	
1522	================================================================================
1523	EXPERIMENT: p1_ss_lora_only
1524	================================================================================
1525	{
1526	  "status": "DONE",
1527	  "retry_count": 0,
1528	  "created_at": "2026-05-25T08:58:41.419Z",
1529	  "updated_at": "2026-05-25T09:42:22.185Z",
1530	  "hypothesis": "SS training on LoRA-only checkpoint (no ThreadGate) with same hyperparameters (rho_max=0.3, same schedule) should achieve similar GAR improvement as SS+TG. If confirmed, this proves the SS fix is architecture-agnostic, strengthening the paper's mitigation story (the gap is caused by exposure bias in any auxiliary-loss setup, and SS fixes it regardless of gating mechanism).",
1531	  "spec": {
1532	    "command": "bash /root/turn_residual_gating/scripts/d048_ss_lo_s42.sh",
1533	    "server": "westd-20861",
1534	    "data_path": "/root/turn-residual-gating/data/phase2_train.jsonl",
1535	    "data_count": 2000,
1536	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1537	    "seed": 42,
1538	    "notes": "SS+LoRA-only (gate_type=none, ss_max_ratio=0.3). From-scratch training, not resume. Auto TF+AR eval after training. ~6.5h training + eval."
1539	  },
1540	  "conclusion": "killed",
1541	  "completed_at": "2026-05-25T09:42:22.185Z"
1542	}
1543	
1544	================================================================================
1545	EXPERIMENT: p1_tf_ar_kl_divergence
1546	================================================================================
1547	{
1548	  "status": "DONE",
1549	  "retry_count": 0,
1550	  "created_at": "2026-05-23T19:37:46.355Z",
1551	  "updated_at": "2026-05-24T07:18:10.268Z",
1552	  "hypothesis": "TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.",
1553	  "metrics": {
1554	    "tg_delta_gar": 0.0165,
1555	    "base_delta_gar": 0.0122,
1556	    "tg_mean_kl": 0.054,
1557	    "base_mean_kl": 0.043,
1558	    "gate_kl_correlation": 0.11,
1559	    "high_kl_layers": "L23-L27, L9",
1560	    "gar_robustness_ours_tg_base_ratio": 21.4,
1561	    "gar_robustness_goal_only_ratio": 63,
1562	    "gar_robustness_ours_all_ratio": 1.7,
1563	    "gar_robustness_ours_first_ratio": 1.8
1564	  },
1565	  "spec": {
1566	    "command": "python scripts/p1_kl_divergence.py",
1567	    "server": "westd-20861",
1568	    "data_path": "/root/turn_residual_gating/data/eval_200.json",
1569	    "data_count": 30,
1570	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1571	    "seed": 42,
1572	    "checkpoint_path": "results/p1_kl_perhead/",
1573	    "log_path": "logs/p1_kl_divergence_step2.log"
1574	  },
1575	  "conclusion": "success",
1576	  "completed_at": "2026-05-24T07:18:06.521Z"
1577	}
1578	
1579	================================================================================
1580	EXPERIMENT: p2_llama_gradient_conflict
1581	================================================================================
1582	{
1583	  "status": "DONE",
1584	  "retry_count": 0,
1585	  "created_at": "2026-05-23T19:37:50.492Z",
1586	  "updated_at": "2026-05-24T07:20:28.248Z",
1587	  "hypothesis": "PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).",
1588	  "spec": {
1589	    "command": "bash scripts/p2_llama_gradient_conflict.sh",
1590	    "server": "westd-20861",
1591	    "data_path": "/root/turn-residual-gating/data/train_400.json",
1592	    "data_count": 400,
1593	    "model_name": "meta-llama/Llama-3.1-8B-Instruct",
1594	    "seed": 42,
1595	    "checkpoint_path": "results/p2_llama_gradient_conflict/",
1596	    "log_path": "logs/p2_llama_gradient_conflict.log"
1597	  },
1598	  "conclusion": "success",
1599	  "metrics": {
1600	    "cos_sim_mean": 0.0045,
1601	    "cos_sim_std": 0.07,
1602	    "neg_cos_sim_layers_pct": 53.1,
1603	    "mag_ratio_median": 25.7,
1604	    "conclusion_note": "cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern."
1605	  },
1606	  "completed_at": "2026-05-24T07:20:28.248Z"
1607	}
1608	
1609	================================================================================
1610	EXPERIMENT: phase1_gar_diag
1611	================================================================================
1612	{
1613	  "status": "DONE",
1614	  "retry_count": 0,
1615	  "created_at": "2026-05-18T05:24:07.903Z",
1616	  "updated_at": "2026-05-18T05:59:25.324Z",
1617	  "hypothesis": "Qwen2.5-7B-Instruct 在 10-turn 多轮对话中，中间 turns (3-8) 的 GAR (Goal Accessibility Ratio) 相对 turn-1 下降 ≥15%，表明模型对 system prompt 中目标 token 的注意力随对话进行显著衰减",
1618	  "spec": {
1619	    "command": "python run_phase1_gar.py --results-dir /root/turn_residual_gating/results",
1620	    "server": "westd-20861",
1621	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1622	    "data_path": "built-in 5 conversations (knowledge_qa, coding_help, creative_writing, math_reasoning, roleplay_advisor)",
1623	    "data_count": 5,
1624	    "seed": 0,
1625	    "checkpoint_path": "N/A",
1626	    "log_path": "/root/turn_residual_gating/results/phase1_run.log"
1627	  },
1628	  "conclusion": "success",
1629	  "metrics": {
1630	    "turn1_avg_gar": 0.0418,
1631	    "mid_turns_avg_gar": 0.0122,
1632	    "relative_drop": 0.708,
1633	    "num_conversations": 5,
1634	    "num_turns": 10,
1635	    "per_turn_avg_gar": [
1636	      0.0418,
1637	      0.0241,
1638	      0.0224,
1639	      0.013,
1640	      0.0133,
1641	      0.0086,
1642	      0.0078,
1643	      0.008,
1644	      0.0157,
1645	      0.0064
1646	    ]
1647	  },
1648	  "completed_at": "2026-05-18T05:59:25.325Z"
1649	}
1650	
1651	================================================================================
1652	EXPERIMENT: phase1a_multiseed_8runs
1653	================================================================================
1654	{
1655	  "status": "PREPARING",
1656	  "retry_count": 0,
1657	  "created_at": "2026-05-25T06:18:08.953Z",
1658	  "updated_at": "2026-05-25T06:18:08.953Z",
1659	  "spec": {
1660	    "command": "bash -c \"bash /root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh\"",
1661	    "server": "westd-20861",
1662	    "gpu": [
1663	      "cuda:0"
1664	    ],
1665	    "pid": "5508",
1666	    "log_path": "~/runs/turn_residual_gating/phase1a_multiseed_8runs.log",
1667	    "submitted_at": "2026-05-25T06:18:08.495Z",
1668	    "submitted_via": "submit_training_job",
1669	    "backend": "tmux",
1670	    "account": "root"
1671	  }
1672	}
1673	
1674	================================================================================
1675	EXPERIMENT: phase1a_multiseed_qwen
1676	================================================================================
1677	{
1678	  "status": "DONE",
1679	  "retry_count": 0,
1680	  "created_at": "2026-05-25T06:15:26.051Z",
1681	  "updated_at": "2026-05-25T11:20:34.089Z",
1682	  "hypothesis": "Multi-seed (s123, s456) training across 5 Qwen conditions (PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all claims. 8 training runs + AR eval N≥50 each. Expect TF convergence (GAR~0.50) and consistent AR rankings across seeds.",
1683	  "spec": {
1684	    "command": "python src/train_phase2_v9_pcgrad.py",
1685	    "server": "westd-20861",
1686	    "data_path": "data/ultrachat_8k",
1687	    "data_count": 8000,
1688	    "model_name": "Qwen2.5-7B-Instruct",
1689	    "seed": 123,
1690	    "checkpoint_path": "N/A",
1691	    "log_path": "runs/d048_pcgrad_s123"
1692	  },
1693	  "conclusion": "killed",
1694	  "notes": "用户要求停止：30min 内无法完成。PCGrad s123 在 1800/3000 步时被终止，后续 7 个排队任务全部取消。",
1695	  "checkpoint_path": "N/A",
1696	  "log_path": "runs/d048_pcgrad_s123",
1697	  "completed_at": "2026-05-25T11:20:34.089Z"
1698	}
1699	
1700	================================================================================
1701	EXPERIMENT: phase1b_llama_complement
1702	================================================================================
1703	{
1704	  "status": "PREPARING",
1705	  "retry_count": 0,
1706	  "created_at": "2026-05-25T06:15:34.729Z",
1707	  "updated_at": "2026-05-25T06:15:44.322Z",
1708	  "hypothesis": "Llama PCGrad + UG (s42) to complete cross-model comparison matrix. If Llama PCGrad also fails to improve AR GAR (like Qwen), it strengthens the cross-architecture causal exclusion of gradient conflict."
1709	}
1710	
1711	================================================================================
1712	EXPERIMENT: phase2_4way_eval
1713	================================================================================
1714	{
1715	  "status": "DONE",
1716	  "retry_count": 0,
1717	  "created_at": "2026-05-19T13:07:30.673Z",
1718	  "updated_at": "2026-05-19T13:15:39.947Z",
1719	  "hypothesis": "Turn-residual gating (TRG) improves multi-turn response quality over LoRA-only and base model baselines because it selectively amplifies conversational context signals, which should manifest as higher GAR scores across 4 conditions (base, base+TRG, LoRA, LoRA+TRG).",
1720	  "spec": {
1721	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && bash scripts/run_4way_eval.sh 2>&1 | tee runs/4way_eval.log\"",
1722	    "server": "westd-20861",
1723	    "gpu": [
1724	      "cuda:0"
1725	    ],
1726	    "pid": "60024",
1727	    "log_path": "/root/turn_residual_gating/runs/4way_eval.log",
1728	    "submitted_at": "2026-05-19T13:07:37.380Z",
1729	    "submitted_via": "submit_training_job",
1730	    "backend": "tmux",
1731	    "account": "root",
1732	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
1733	    "data_count": 8000,
1734	    "model_name": "Qwen2.5-7B-Instruct",
1735	    "seed": 42,
1736	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
1737	    "eval_data": "ultrachat_8k eval split",
1738	    "checkpoint_path": "/root/turn_residual_gating/runs/4way_eval/",
1739	    "wall_clock_seconds": 447.0,
1740	    "gpu_hours": 0.12
1741	  },
1742	  "parent": "phase2_tg_s42_v7",
1743	  "conclusion": "negative",
1744	  "completed_at": "2026-05-19T13:15:04.405Z",
1745	  "metrics": {
1746	    "base_ours_mid_gar": 0.0107,
1747	    "base_ours_recovery_pp": -0.15,
1748	    "base_dongre_mid_gar": 0.003,
1749	    "base_dongre_recovery_pp": -0.92,
1750	    "base_ppl": 4.23,
1751	    "base_ntp": 1.4162,
1752	    "tg_ours_mid_gar": 0.4866,
1753	    "tg_ours_recovery_pp": 47.44,
1754	    "tg_dongre_mid_gar": 0.0157,
1755	    "tg_dongre_recovery_pp": 0.35,
1756	    "tg_ppl": 2.63,
1757	    "tg_ntp": 0.9484,
1758	    "ug_ours_mid_gar": 0.4923,
1759	    "ug_ours_recovery_pp": 48.01,
1760	    "ug_dongre_mid_gar": 0.013,
1761	    "ug_dongre_recovery_pp": 0.08,
1762	    "ug_ppl": 2.62,
1763	    "ug_ntp": 0.9433,
1764	    "lora_ours_mid_gar": 0.486,
1765	    "lora_ours_recovery_pp": 47.39,
1766	    "lora_dongre_mid_gar": 0.0137,
1767	    "lora_dongre_recovery_pp": 0.15,
1768	    "lora_ppl": 2.63,
1769	    "lora_ntp": 0.9482,
1770	    "route_b_confirmed": true,
1771	    "gating_incremental_benefit": "none"
1772	  },
1773	  "notes": "四路 eval 完成，Route B 决定性确认。三种训练方法（TG/UG/LoRA-only）在推理端完全趋同：ours GAR recovery ~47-48pp（vs base -0.15pp），dongre GAR recovery 0.08-0.35pp，PPL 2.62-2.63，NTP 0.943-0.948。Gating 机制（无论 turn-conditioned 还是 uniform）相比纯 LoRA 微调零增量。LoRA fine-tuning 是 GAR recovery 的唯一来源。hypothesis 被证伪：TRG 不比 LoRA-only 更好。"
1774	}
1775	
1776	================================================================================
1777	EXPERIMENT: phase2_4way_eval_heldout
1778	================================================================================
1779	{
1780	  "status": "DONE",
1781	  "retry_count": 0,
1782	  "created_at": "2026-05-19T13:58:59.269Z",
1783	  "updated_at": "2026-05-19T14:35:47.201Z",
1784	  "hypothesis": "四路消融的三路趋同结论（TG≈UG≈LoRA-only，gating 零增量）在 held-out eval 数据（idx≥8000，与训练集无重叠）上复现，排除数据重叠 confound。预期：相对比较保持（三路趋同），绝对 GAR 值可能变化。",
1785	  "parent": "phase2_4way_eval",
1786	  "spec": {
1787	    "command": "bash -c \"cd /root/turn_residual_gating && bash scripts/run_4way_eval_heldout.sh\"",
1788	    "server": "westd-20861",
1789	    "gpu": "cuda:0",
1790	    "pid": 67204,
1791	    "log_path": "~/runs/turn_residual_gating/phase2_4way_eval_heldout.log",
1792	    "submitted_at": "2026-05-19T14:01:00.965Z",
1793	    "submitted_via": "submit_training_job",
1794	    "backend": "tmux",
1795	    "account": "root",
1796	    "data_path": "/root/turn_residual_gating/data/ultrachat_eval_heldout.json",
1797	    "data_count": 50,
1798	    "model_name": "Qwen2.5-7B-Instruct",
1799	    "seed": 42,
1800	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42",
1801	    "eval_data": "ultrachat_eval_heldout.json (50 convs, idx 8843-68199, no overlap with training 0-7999)",
1802	    "configs": "4 models (Base/TG_v7/UG/LoRA-only) x 2 GAR variants (ours/Dongre) = 8 eval runs",
1803	    "checkpoint_path": "N/A (eval-only)",
1804	    "wall_clock_seconds": 2086.2,
1805	    "gpu_hours": 0.58
1806	  },
1807	  "reproduce": {
1808	    "finished_at": "2026-05-19T14:32:09.481Z"
1809	  },
1810	  "metrics": {
1811	    "base_ours_mid_gar": 0.0128,
1812	    "base_ours_recovery_pp": 0.06,
1813	    "base_dongre_mid_gar": 0.0031,
1814	    "base_dongre_recovery_pp": -0.91,
1815	    "base_ppl": 4.34,
1816	    "base_ntp": 1.4045,
1817	    "tg_ours_mid_gar": 0.5035,
1818	    "tg_ours_recovery_pp": 49.13,
1819	    "tg_dongre_mid_gar": 0.0152,
1820	    "tg_dongre_recovery_pp": 0.3,
1821	    "tg_ppl": 2.78,
1822	    "tg_ntp": 0.9771,
1823	    "ug_ours_mid_gar": 0.5053,
1824	    "ug_ours_recovery_pp": 49.31,
1825	    "ug_dongre_mid_gar": 0.0124,
1826	    "ug_dongre_recovery_pp": 0.02,
1827	    "ug_ppl": 2.78,
1828	    "ug_ntp": 0.9752,
1829	    "lora_ours_mid_gar": 0.4978,
1830	    "lora_ours_recovery_pp": 48.56,
1831	    "lora_dongre_mid_gar": 0.0132,
1832	    "lora_dongre_recovery_pp": 0.1,
1833	    "lora_ppl": 2.78,
1834	    "lora_ntp": 0.9771,
1835	    "three_way_convergence_confirmed": true,
1836	    "gar_ours_spread_pp": 0.75,
1837	    "ppl_spread": 0,
1838	    "data_overlap": false
1839	  },
1840	  "conclusion": "success",
1841	  "notes": "Held-out eval 三路趋同完全复现。TG/UG/LoRA-only GAR-ours: 0.504/0.505/0.498 (spread 0.75pp), PPL 均为 2.78。与 overlap 数据相比绝对值略高（GAR +1-2pp, PPL +0.15），属正常泛化偏移，相对比较完全一致。数据完整性 confound 已排除。",
1842	  "completed_at": "2026-05-19T14:35:47.202Z"
1843	}
1844	
1845	================================================================================
1846	EXPERIMENT: phase2_lora_only_s42
1847	================================================================================
1848	{
1849	  "status": "DONE",
1850	  "retry_count": 1,
1851	  "created_at": "2026-05-18T20:36:32.506Z",
1852	  "updated_at": "2026-05-20T02:15:18.992Z",
1853	  "hypothesis": "LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。",
1854	  "parent": "phase2_tg_s42_v7",
1855	  "failure_reason": "EXIT_CODE=1 (generic error — check log tail)",
1856	  "completed_at": "2026-05-19T12:44:29.475Z",
1857	  "extra": {
1858	    "previous_failure": {
1859	      "conclusion": "failed"
1860	    },
1861	    "hook_events": [
1862	      {
1863	        "event": "on_failed",
1864	        "action": "agent",
1865	        "ts": "2026-05-19T13:04:35.644174+00:00"
1866	      }
1867	    ]
1868	  },
1869	  "spec": {
1870	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type lora_only --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 0.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_lora_only_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
1871	    "server": "westd-20861",
1872	    "gpu": "cuda:0",
1873	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
1874	    "data_count": 8000,
1875	    "model_name": "Qwen2.5-7B-Instruct",
1876	    "seed": 42,
1877	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_lora_only_s42",
1878	    "log_path": "/root/turn_residual_gating/runs/phase2_lora_only_s42.log",
1879	    "checkpoint_source": "from_scratch",
1880	    "eval_data": "N/A"
1881	  },
1882	  "reproduce": {
1883	    "finished_at": "2026-05-19T13:04:33.523Z"
1884	  },
1885	  "conclusion": "success",
1886	  "metrics": {
1887	    "epochs_completed": 3,
1888	    "global_steps": 3000,
1889	    "training_time_seconds": 20588.6,
1890	    "training_time_hours": 5.7,
1891	    "gate_fixed": 1,
1892	    "gate_type_actual": "none",
1893	    "final_lora_size_mb": 20,
1894	    "eval_modelgen_ours_mid_gar": 0.0245,
1895	    "eval_modelgen_dongre_mid_gar": 0.0185,
1896	    "eval_modelgen_ppl": 1.371
1897	  },
1898	  "checkpoint_path": "/root/runs/turn_residual_gating/runs/phase2_lora_only_s42/lora/",
1899	  "log_path": "/root/runs/turn_residual_gating/phase2_lora_only_s42.log",
1900	  "notes": "诊断确认：EXIT_CODE=1 因 argparse 不认 lora_only 选项（choices 只有 threadgate/uniform/none）。训练实际已用 --gate-type none 完成 3 epoch (3000 steps, 20588.6s/5.7h)。Gate 全程固定 1.0（符合 lora_only 语义）。Checkpoint 可用，无需重跑。修复：dispatch 命令改用 --gate-type none 或在 train_phase2.py 添加 lora_only choice。"
1901	}
1902	
1903	================================================================================
1904	EXPERIMENT: phase2_switching
1905	================================================================================
1906	{
1907	  "status": "DONE",
1908	  "retry_count": 0,
1909	  "created_at": "2026-05-25T08:58:40.187Z",
1910	  "updated_at": "2026-05-25T09:42:21.391Z",
1911	  "hypothesis": "TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual KV cache drift. Staircase = exposure bias dominant; linear slope = KV drift dominant.",
1912	  "conclusion": "killed",
1913	  "completed_at": "2026-05-25T09:42:21.391Z"
1914	}
1915	
1916	================================================================================
1917	EXPERIMENT: phase2_tf_ar_switching
1918	================================================================================
1919	{
1920	  "status": "QUEUED",
1921	  "retry_count": 0,
1922	  "created_at": "2026-05-25T06:15:36.221Z",
1923	  "updated_at": "2026-05-25T06:45:27.338Z",
1924	  "hypothesis": "TF→AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift."
1925	}
1926	
1927	================================================================================
1928	EXPERIMENT: phase2_tg_s42
1929	================================================================================
1930	{
1931	  "status": "DONE",
1932	  "retry_count": 0,
1933	  "created_at": "2026-05-18T06:04:12.759Z",
1934	  "updated_at": "2026-05-22T04:36:54.262Z",
1935	  "hypothesis": "ThreadGate (turn-conditional gating) 在 L_NTP+L_GAR 联合训练后，相比 Uniform Gate，mid-turn GAR recovery 高出 ≥3pp，验证 Cesaro 理论预测：position-conditional 干预优于 uniform 干预",
1936	  "parent": "phase1_gar_diag",
1937	  "spec": {
1938	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048\"",
1939	    "server": "westd-20861",
1940	    "gpu": [
1941	      "cuda:0"
1942	    ],
1943	    "pid": "11286",
1944	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42.log",
1945	    "submitted_at": "2026-05-18T07:03:28.476Z",
1946	    "submitted_via": "submit_training_job",
1947	    "backend": "tmux",
1948	    "account": "root",
1949	    "wall_clock_seconds": 15333,
1950	    "gpu_hours": 4.26,
1951	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
1952	    "data_count": 8000,
1953	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
1954	    "seed": 42,
1955	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_s42"
1956	  },
1957	  "server": "westd-20861",
1958	  "gpu": "cuda:0",
1959	  "pid": "11286",
1960	  "log_path": "~/runs/turn_residual_gating/phase2_tg_s42.log",
1961	  "reproduce": {
1962	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048\"",
1963	    "finished_at": "2026-05-18T11:19:00.888Z"
1964	  },
1965	  "failure_reason": "EXIT_CODE=143 (SIGTERM — graceful kill)",
1966	  "conclusion": "negative",
1967	  "completed_at": "2026-05-18T11:19:01.512Z",
1968	  "extra": {
1969	    "hook_events": [
1970	      {
1971	        "event": "on_failed",
1972	        "action": "agent",
1973	        "ts": "2026-05-18T11:19:02.835359+00:00"
1974	      }
1975	    ]
1976	  },
1977	  "notes": "失败原因: EXIT_CODE=143 (SIGTERM) — 大概率被 Worker code:diagnose_gar_loss_and_fix 主动 kill（时间线：Worker 11:13 启动 → v2 11:13 创建 → v1 11:19 SIGTERM）。v2 hypothesis 指出 GAR loss 实现有 bug（缺少 ε=0.001 稳定项）。诊断 Worker worker_diagnose_phase2_tg_s42_20260518T112048 已派出确认日志详情。| 建议: 等诊断结果确认后推进 v2",
1978	  "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_s42/epoch_1",
1979	  "metrics": {
1980	    "final_ntp_loss": 0.94,
1981	    "final_gar_loss": 0,
1982	    "gate_mean": 0.988,
1983	    "gar_loss_zero_pct": 87.6,
1984	    "epochs_completed": 1.67,
1985	    "killed_reason": "SIGTERM by diagnose worker (unauthorized)"
1986	  }
1987	}
1988	
1989	================================================================================
1990	EXPERIMENT: phase2_tg_s42_v2
1991	================================================================================
1992	{
1993	  "status": "DONE",
1994	  "retry_count": 0,
1995	  "created_at": "2026-05-18T11:13:37.042Z",
1996	  "updated_at": "2026-05-18T13:11:26.331Z",
1997	  "hypothesis": "ThreadGate + 修复后的 cumulative GAR loss (ε=0.001) 在 L_NTP+L_GAR 联合训练后，mid-turn GAR recovery 应显著优于 v1 (NTP-only baseline)，验证 GAR loss 的有效性",
1998	  "parent": "phase2_tg_s42",
1999	  "server": "westd-20861",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "5ec3db9c-119a-40bb-9110-de3750021a9b"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_crossmodel_detail.tex",
  "usage": {
    "total_tokens": 54621,
    "tool_uses": 13,
    "duration_ms": 52308
  },
  "last_tool_name": "Read",
  "uuid": "3bf5dd64-bce0-44e1-ad6f-6c6e5d3df090",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Read · `toolu_01GxkFX2AZn5kkajM4N8Z1vL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "ceba9d17-a510-4972-9cad-c33b6e497fd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 122 · 2026-05-25T20:13:45.736Z_

<details><summary>↩ Tool result · `toolu_01GxkFX2AZn5kkajM4N8Z1vL`</summary>

```text
1	% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct
2	% Conditions shared by both models: Base, ThreadGate, LoRA-only
3	% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0
4	% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4
5	% Llama SS: p1_llama_ss_eval (epoch_1 checkpoint, N=50)
6	\begin{table*}[t]
7	\centering
8	\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.
9	Gap ratio = TF GAR / AR GAR; lower is better (less exposure bias).
10	Qwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$ (SS: $N{=}50$).
11	Llama AR GAR and gaps are mean-based; median-based TG gap is 27$\times$ (\S\ref{subsec:cross-model}).}
12	\label{tab:crossmodel-detail}
13	\small
14	\begin{tabular}{@{}ll ccccc@{}}
15	\toprule
16	\textbf{Model} & \textbf{Condition} & \textbf{TF GAR}$\uparrow$ & \textbf{AR GAR}$\uparrow$ & \textbf{TF PPL}$\downarrow$ & \textbf{AR PPL}$\downarrow$ & \textbf{Gap}$\downarrow$ \\
17	\midrule
18	\multirow{4}{*}{Qwen-7B}
19	  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\times$ \\
20	  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\times$ \\
21	  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\times$ \\
22	  & \textbf{SS} & 0.498 & \textbf{0.401} & 2.78 & 1.441 & \textbf{1.2$\times$} \\
23	\midrule
24	\multirow{4}{*}{Llama-8B}
25	  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\times$ \\
26	  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\times$ \\
27	  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\times$ \\
28	  & \textbf{SS} & 0.477 & \textbf{0.166} & 2.82 & 1.370 & \textbf{2.9$\times$} \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "64ac5d37-bfaa-4228-9a99-8d5561179d62"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_perseed_ss.tex",
  "usage": {
    "total_tokens": 54682,
    "tool_uses": 14,
    "duration_ms": 52794
  },
  "last_tool_name": "Read",
  "uuid": "10940eb1-2b20-443d-b563-cfd27fa7fd4c",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 124_

<details open><summary>🔧 Tool call — Read · `toolu_01GFgWRBcgT5i92xxrq3pGp7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "264a2d2b-5f4f-4dcd-8507-43dd053c7b2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 125 · 2026-05-25T20:13:46.226Z_

<details><summary>↩ Tool result · `toolu_01GFgWRBcgT5i92xxrq3pGp7`</summary>

```text
1	% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456
2	% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)
3	% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\text{valid}} \approx 39$).}
8	\label{tab:perseed-ss}
9	\resizebox{\columnwidth}{!}{
10	\begin{tabular}{@{}l ccc c@{}}
11	\toprule
12	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Seed 456} & \textbf{Mean $\pm$ Std} \\
13	\midrule
14	\multicolumn{5}{@{}l}{\textit{Teacher-Forced (TF)}} \\
15	\quad GAR-ours $\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\pm$ 0.032 \\
16	\quad GAR-Dongre $\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\pm$ 0.014 \\
17	\quad PPL $\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\pm$ 0.097 \\
18	\midrule
19	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
20	\quad GAR-ours $\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\pm$ 0.047 \\
21	\quad PPL $\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\pm$ 0.002 \\
22	\midrule
23	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 3$}} \\
24	\quad GAR-ours $\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\pm$ 0.008 \\
25	\quad PPL $\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\pm$ 0.022 \\
26	\midrule
27	\multicolumn{5}{@{}l}{\textit{Autoregressive (AR), $\beta = 5$}} \\
28	\quad GAR-ours $\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\pm$ 0.001 \\
29	\quad PPL $\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\pm$ 0.013 \\
30	\bottomrule
31	\end{tabular}}
32	\end{table}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "8ecfa08d-d013-45a0-be29-be93509108ee"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_perseed_tg.tex",
  "usage": {
    "total_tokens": 54743,
    "tool_uses": 15,
    "duration_ms": 52873
  },
  "last_tool_name": "Read",
  "uuid": "36e9bb14-e55e-4235-8e51-04a2e6a4ec65",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 127_

<details open><summary>🔧 Tool call — Read · `toolu_01LYhZghXXj89pm64EUoFvDp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "f60b16ef-9fec-4500-9f73-407a2ac4c9c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 128 · 2026-05-25T20:13:46.300Z_

<details><summary>↩ Tool result · `toolu_01LYhZghXXj89pm64EUoFvDp`</summary>

```text
1	% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123
2	% TF eval: N=200 held-out conversations
3	% AR eval: N=5, T=10 model-generated conversations (original eval protocol)
4	\begin{table}[h]
5	\centering
6	\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.
7	TF evaluation uses 200 held-out conversations.
8	AR evaluation uses 5 model-generated conversations with 10 turns each.}
9	\label{tab:perseed-tg}
10	\resizebox{\columnwidth}{!}{
11	\begin{tabular}{@{}l cc c@{}}
12	\toprule
13	\textbf{Metric} & \textbf{Seed 42} & \textbf{Seed 123} & \textbf{Mean $\pm$ Std} \\
14	\midrule
15	\multicolumn{4}{@{}l}{\textit{Teacher-Forced (TF)}} \\
16	\quad GAR-ours $\uparrow$   & 0.504 & 0.505 & 0.504 $\pm$ 0.001 \\
17	\quad GAR-Dongre $\uparrow$ & 0.015 & 0.012 & 0.014 $\pm$ 0.002 \\
18	\quad PPL $\downarrow$       & 2.784 & 2.780 & 2.782 $\pm$ 0.003 \\
19	\midrule
20	\multicolumn{4}{@{}l}{\textit{Autoregressive (AR), $\beta = 0$}} \\
21	\quad GAR-ours $\uparrow$   & 0.016 & 0.017 & 0.016 $\pm$ 0.001 \\
22	\quad GAR-Dongre $\uparrow$ & 0.019 & 0.018 & 0.019 $\pm$ 0.001 \\
23	\quad PPL $\downarrow$       & 1.360 & 1.386 & 1.373 $\pm$ 0.018 \\
24	\midrule
25	\multicolumn{4}{@{}l}{\textit{Derived}} \\
26	\quad Gap ratio (TF/AR GAR-ours) $\downarrow$ & 32.1 & 30.6 & 31.4 $\pm$ 1.1 \\
27	\bottomrule
28	\end{tabular}}
29	\end{table}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "40ebe945-3b1a-4a05-b237-ec09c25f5894"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_perturn_qwen.tex",
  "usage": {
    "total_tokens": 54804,
    "tool_uses": 16,
    "duration_ms": 53514
  },
  "last_tool_name": "Read",
  "uuid": "a30f4c36-9298-4dac-86b0-d92ecbb2525a",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 130_

<details open><summary>🔧 Tool call — Read · `toolu_01DXY7YSEd9csJYTJ1tYMGQJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "3bf3672e-41d6-4025-815f-41ed6dae3c3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 131 · 2026-05-25T20:13:46.941Z_

<details><summary>↩ Tool result · `toolu_01DXY7YSEd9csJYTJ1tYMGQJ`</summary>

```text
1	% Per-turn AR GAR-ours for Qwen2.5-7B-Instruct, 6-way comparison
2	% Source: d048_final_ar, beta=0, N=50 gen-mode, n_valid~39
3	% Only turns 1--5 shown (later turns have survivor bias from variable-length generation)
4	\begin{table}[t]
5	\centering
6	\caption{Per-turn autoregressive GAR-ours ($\beta{=}0$) on Qwen2.5-7B-Instruct across six training configurations. Values represent average GAR over ${\sim}39$ valid conversations in free-form generation mode.}
7	\label{tab:perturn-qwen}
8	\resizebox{\columnwidth}{!}{
9	\begin{tabular}{@{}l ccccc@{}}
10	\toprule
11	\textbf{Configuration} & \textbf{Turn 1} & \textbf{Turn 2} & \textbf{Turn 3} & \textbf{Turn 4} & \textbf{Turn 5} \\
12	\midrule
13	Base         & .085 & .032 & .021 & .013 & .004 \\
14	ThreadGate   & .130 & .073 & .059 & .043 & .066 \\
15	PCGrad       & .090 & .038 & .028 & .029 & .027 \\
16	UG           & .113 & .056 & .033 & .020 & .016 \\
17	LoRA-only    & .107 & .059 & .030 & .049 & .040 \\
18	SS           & \textbf{.458} & \textbf{.381} & \textbf{.344} & \textbf{.370} & \textbf{.365} \\
19	\bottomrule
20	\end{tabular}}
21	\end{table}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "6d117766-05b9-4467-bce9-79a70bdef098"
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
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_perturn_llama.tex",
  "usage": {
    "total_tokens": 54865,
    "tool_uses": 17,
    "duration_ms": 53757
  },
  "last_tool_name": "Read",
  "uuid": "6f4e1603-50d6-4578-8568-03a441e0607d",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 133_

<details open><summary>🔧 Tool call — Read · `toolu_015xMUHGcQGNjunM2rewe4fX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4083a0a9-f084-44a9-9a25-d55aec485980",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 134 · 2026-05-25T20:13:47.195Z_

<details><summary>↩ Tool result · `toolu_015xMUHGcQGNjunM2rewe4fX`</summary>

```text
1	% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct
2	% Panel (a): N=20, T=4 (eval_llama_ar_n20) — reliable estimates
3	% Panel (b): Base only, N=5, T=10 (llama_phase1_gar_diag) — decay profile
4	\begin{table*}[t]
5	\centering
6	\caption{Per-turn autoregressive GAR-ours ($\beta{=}0$) on Llama-3.1-8B-Instruct.
7	(a)~Three-way comparison using $N{=}20$ conversations ($T{=}4$ turns).
8	(b)~Base model decay profile ($N{=}5$, $T{=}10$).}
9	\label{tab:perturn-llama}
10	\small
11	\begin{subtable}[t]{0.48\textwidth}
12	\centering
13	\caption{$N{=}20$, $T{=}4$}
14	\renewcommand{\arraystretch}{1.3}
15	\begin{tabular}{@{}l cccc@{}}
16	\toprule
17	\textbf{Config.} & \textbf{T1} & \textbf{T2} & \textbf{T3} & \textbf{T4} \\
18	\midrule
19	Base      & .028 & .013 & .009 & .008 \\
20	TG        & .041 & .042 & .049 & .038 \\
21	LoRA-only & .033 & .049 & .025 & .031 \\
22	\bottomrule
23	\end{tabular}
24	\end{subtable}
25	\hfill
26	\begin{subtable}[t]{0.38\textwidth}
27	\centering
28	\caption{Base decay ($N{=}5$, $T{=}10$)}
29	\begin{tabular}{@{}cc@{}}
30	\toprule
31	\textbf{Turn} & \textbf{GAR-ours} \\
32	\midrule
33	1  & .026 \\
34	2  & .018 \\
35	3  & .009 \\
36	4  & .006 \\
37	5  & .006 \\
38	6  & .004 \\
39	7  & .004 \\
40	8  & .004 \\
41	9  & .005 \\
42	10 & .003 \\
43	\bottomrule
44	\end{tabular}
45	\end{subtable}
46	\end{table*}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "a9556052-f71b-4bd4-b1e7-eb9cb17dd9d9"
}
```

</details>

---


### System

_source line 135_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_dataset_stats.tex",
  "usage": {
    "total_tokens": 54926,
    "tool_uses": 18,
    "duration_ms": 54109
  },
  "last_tool_name": "Read",
  "uuid": "b0d620a0-1c82-4a28-9bb8-a615626bb3e2",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 136_

<details open><summary>🔧 Tool call — Read · `toolu_01DYividVhgFBvhMTaaiDMhs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_dataset_stats.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "9e9f6a78-088a-490b-9c24-42397aed02be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 137 · 2026-05-25T20:13:47.537Z_

<details><summary>↩ Tool result · `toolu_01DYividVhgFBvhMTaaiDMhs`</summary>

```text
1	% Dataset statistics table
2	\begin{table}[t]
3	\centering
4	\small
5	\caption{Dataset statistics. Training and evaluation data are sampled from UltraChat-200K \texttt{train\_sft} split~\citep{ding2023ultrachat}. All conversations contain $\geq 5$ assistant turns.}
6	\label{tab:dataset_stats}
7	\begin{tabular}{@{}lr@{}}
8	\toprule
9	\textbf{Statistic} & \textbf{Value} \\
10	\midrule
11	\multicolumn{2}{@{}l}{\textit{Source}} \\
12	\quad Total conversations & 207{,}865 \\
13	\quad After $\geq 5$ turn filter & 17{,}302 \\
14	\midrule
15	\multicolumn{2}{@{}l}{\textit{Splits}} \\
16	\quad Training & 8{,}000 \\
17	\quad Held-out AR eval & 50 \\
18	\quad IID GAR diagnostic & 50 \\
19	\quad Instruction retention & 200 \\
20	\midrule
21	\multicolumn{2}{@{}l}{\textit{Conversation structure}} \\
22	\quad Avg.\ assistant turns & 5.6 \\
23	\quad Min / Max turns & 5 / 7 \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "8e3a582f-4c8e-4bce-8fd2-768e10f1c2eb"
}
```

</details>

---


### System

_source line 138_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_gar_robustness.tex",
  "usage": {
    "total_tokens": 54987,
    "tool_uses": 19,
    "duration_ms": 54479
  },
  "last_tool_name": "Read",
  "uuid": "8502607f-6221-4134-928c-f453798316fb",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 139_

<details open><summary>🔧 Tool call — Read · `toolu_01Wd8MSDcRWmrY5BoEwneAuZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_gar_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "7f7031cf-12fe-437f-94f9-528bfd1393b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 140 · 2026-05-25T20:13:47.906Z_

<details><summary>↩ Tool result · `toolu_01Wd8MSDcRWmrY5BoEwneAuZ`</summary>

```text
1	% GAR definition robustness: 4 token selection strategies x 3 conditions
2	\begin{table*}[t]
3	\centering
4	\small
5	\caption{GAR robustness across token selection strategies. We evaluate four ways to select the token position for gradient attribution: \textbf{Last} (final token of each turn), \textbf{All} (mean over all tokens), \textbf{First} (first token), and \textbf{Goal-only} (goal token as in \citet{dongre2026attention}). Turn-1 and Mid-turn GAR are measured under autoregressive generation on 50 held-out conversations. Gap Ratio = Turn-1 / Mid-turn; lower indicates better gradient preservation across turns.}
6	\label{tab:gar_robustness}
7	\begin{tabular}{@{}ll ccc@{}}
8	\toprule
9	\textbf{Token Selection} & \textbf{Condition} & \textbf{Turn-1 GAR} & \textbf{Mid-turn GAR} & \textbf{Gap Ratio} $\downarrow$ \\
10	\midrule
11	\multirow{3}{*}{Last (ours)}
12	  & Base      & 0.0858 & 0.0152 & 5.64$\times$ \\
13	  & TG        & 0.3938 & 0.3254 & 1.21$\times$ \\
14	  & SS        & 0.5274 & 0.4582 & 1.15$\times$ \\
15	\midrule
16	\multirow{3}{*}{All tokens}
17	  & Base      & 0.1152 & 0.0152 & 7.57$\times$ \\
18	  & TG        & 0.1275 & 0.0253 & 5.04$\times$ \\
19	  & SS        & 0.5043 & 0.3658 & 1.38$\times$ \\
20	\midrule
21	\multirow{3}{*}{First token}
22	  & Base      & 0.2987 & 0.0224 & 13.32$\times$ \\
23	  & TG        & 0.3225 & 0.0392 & 8.24$\times$ \\
24	  & SS        & 0.7549 & 0.4118 & 1.83$\times$ \\
25	\midrule
26	\multirow{3}{*}{Goal-only}
27	  & Base      & 0.0110 & 0.0049 & 2.23$\times$ \\
28	  & TG        & 0.3313 & 0.3103 & 1.07$\times$ \\
29	  & SS        & 0.4528 & 0.4435 & 1.02$\times$ \\
30	\bottomrule
31	\end{tabular}
32	\end{table*}
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "8113c253-5e76-4636-9ff5-7299219f02d3"
}
```

</details>

---


### System

_source line 141_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_statistical_tests.tex",
  "usage": {
    "total_tokens": 55048,
    "tool_uses": 20,
    "duration_ms": 54753
  },
  "last_tool_name": "Read",
  "uuid": "27ede438-2e24-43cd-841f-5264b80c040a",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 142_

<details open><summary>🔧 Tool call — Read · `toolu_01LYH6zWd4GcmVdfeWjSvmQv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_statistical_tests.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "35451a91-a5d8-443d-9264-eaf0b165844e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 143 · 2026-05-25T20:13:48.180Z_

<details><summary>↩ Tool result · `toolu_01LYH6zWd4GcmVdfeWjSvmQv`</summary>

```text
1	% Item 9: Statistical tests summary table
2	% Wilcoxon signed-rank tests for per-dialogue GAR + McNemar for instruction retention
3	\begin{table*}[t]
4	\centering
5	\caption{Summary of statistical significance tests.
6	  Wilcoxon signed-rank tests compare per-dialogue GAR across training configurations ($N\!=\!39$);
7	  McNemar's test assesses instruction-following retention under steering ($N\!=\!54$ paired instances).
8	  Bootstrap 95\% CIs from 10{,}000 resamples.
9	  Significance: $^{***}\!p<.001$, $^{**}\!p<.01$, $^{*}\!p<.05$.}
10	\label{tab:statistical_tests}
11	\small
12	\setlength{\tabcolsep}{4pt}
13	\begin{tabular}{@{}llcrrccl@{}}
14	\toprule
15	$\beta$ & Comparison & Test & Stat. & $p$ & $r$ & $\overline{\mathrm{GAR}}$\;[95\% CI] & Sig. \\
16	\midrule
17	\multirow{4}{*}{0.0}
18	 & TG vs Base    & Wilcoxon & $W\!=\!31$  & ${<}.001$ & .802 & .064\,[.041,\,.091]\;vs\;.019\,[.014,\,.024] & $^{***}$ \\
19	 & TG vs LoRA    & Wilcoxon & $W\!=\!187$ & .004      & .454 & .064\,[.041,\,.091]\;vs\;.037\,[.027,\,.050] & $^{**}$  \\
20	 & SS vs TG      & Wilcoxon & $W\!=\!1$   & ${<}.001$ & .869 & .347\,[.327,\,.366]\;vs\;.064\,[.041,\,.091] & $^{***}$ \\
21	 & PCGrad vs TG  & Wilcoxon & $W\!=\!176$ & .002      & .478 & .030\,[.023,\,.038]\;vs\;.064\,[.041,\,.091] & $^{**}$  \\
22	\midrule
23	\multirow{4}{*}{3.0}
24	 & TG vs Base    & Wilcoxon & $W\!=\!242$ & .039 & .331 & .556\,[.538,\,.575]\;vs\;.531\,[.514,\,.550] & $^{*}$  \\
25	 & TG vs LoRA    & Wilcoxon & $W\!=\!376$ & .852 & .031 & .556\,[.538,\,.575]\;vs\;.560\,[.541,\,.581] & n.s.    \\
26	 & SS vs TG      & Wilcoxon & $W\!=\!207$ & .010 & .409 & .593\,[.574,\,.613]\;vs\;.556\,[.538,\,.575] & $^{**}$ \\
27	 & PCGrad vs TG  & Wilcoxon & $W\!=\!368$ & .767 & .049 & .559\,[.543,\,.576]\;vs\;.556\,[.538,\,.575] & n.s.    \\
28	\midrule
29	\multirow{4}{*}{5.0}
30	 & TG vs Base    & Wilcoxon & $W\!=\!251$ & .084 & .281 & .727\,[.708,\,.747]\;vs\;.704\,[.679,\,.730] & n.s. \\
31	 & TG vs LoRA    & Wilcoxon & $W\!=\!277$ & .180 & .220 & .727\,[.708,\,.747]\;vs\;.708\,[.687,\,.729] & n.s. \\
32	 & SS vs TG      & Wilcoxon & $W\!=\!314$ & .421 & .133 & .717\,[.696,\,.738]\;vs\;.727\,[.708,\,.747] & n.s. \\
33	 & PCGrad vs TG  & Wilcoxon & $W\!=\!266$ & .133 & .246 & .708\,[.690,\,.727]\;vs\;.727\,[.708,\,.747] & n.s. \\
34	\midrule
35	\multicolumn{8}{@{}l}{\textit{Instruction-following retention} ($\beta\!=\!0 \to 3$, ThreadGate only)} \\[2pt]
36	 & $\beta\!=\!0$ vs $\beta\!=\!3$ & McNemar & $\chi^2\!=\!3.13$ & .077 & $.200^{\dagger}$ & Rate: .759\;vs\;.870\;($N\!=\!54$) & n.s.$^{\ddagger}$ \\
37	\bottomrule
38	\end{tabular}
39	\\[4pt]
40	{\footnotesize
41	$^{\dagger}$\,Point-biserial $r$; associated $p=.007$ (significant).
42	$^{\ddagger}$\,Marginal by McNemar ($p=.077$); significant by point-biserial correlation.
43	}
44	\end{table*}
45	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "c98e239b-fd30-413b-9871-9681fb9ebab4"
}
```

</details>

---


### System

_source line 144_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_mmlu_detail.tex",
  "usage": {
    "total_tokens": 55109,
    "tool_uses": 21,
    "duration_ms": 55063
  },
  "last_tool_name": "Read",
  "uuid": "72635890-d071-4085-a55e-7ce922acd9e0",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 145_

<details open><summary>🔧 Tool call — Read · `toolu_013iTVLPwxMFDH1mEQpZ8vuV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_mmlu_detail.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "a1dae263-018c-4bad-bb67-23f693b958b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 146 · 2026-05-25T20:13:48.489Z_

<details><summary>↩ Tool result · `toolu_013iTVLPwxMFDH1mEQpZ8vuV`</summary>

```text
1	% MMLU per-category quality preservation table
2	\begin{table}[t]
3	\centering
4	\footnotesize
5	\caption{MMLU accuracy (\%) by category across training conditions. All models are Qwen2.5-7B-Instruct with LoRA adapters evaluated on the full 57-subject MMLU benchmark (14{,}042 questions). $\Delta$ denotes deviation from Base.}
6	\label{tab:mmlu_detail}
7	\resizebox{\columnwidth}{!}{
8	\begin{tabular}{@{}l cccccc@{}}
9	\toprule
10	\textbf{Category} & \textbf{Base} & \textbf{TG} & \textbf{PCGrad} & \textbf{SS} & \textbf{LoRA-only} & \textbf{UG} \\
11	\midrule
12	STEM           & 70.69 & 69.20 & 69.55 & 69.97 & 70.03 & 69.65 \\
13	Social Sciences & 77.28 & 76.92 & 76.79 & 76.83 & 77.08 & 77.02 \\
14	Humanities     & 83.95 & 83.33 & 84.08 & 83.39 & 83.62 & 83.95 \\
15	Other          & 68.25 & 67.59 & 68.12 & 67.95 & 67.06 & 66.80 \\
16	\midrule
17	\textbf{Overall} & \textbf{74.23} & 73.47 & 73.86 & 73.75 & 73.57 & 73.46 \\
18	$\Delta$ & --- & $-$0.76 & $-$0.37 & $-$0.48 & $-$0.66 & $-$0.77 \\
19	\bottomrule
20	\end{tabular}}
21	\end{table}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "be405129-6b5c-47c1-82d9-94a72395c1db"
}
```

</details>

---


### System

_source line 147_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "description": "Reading artifacts/appendix_expansion/tab_qwen15b_results.tex",
  "usage": {
    "total_tokens": 55170,
    "tool_uses": 22,
    "duration_ms": 55301
  },
  "last_tool_name": "Read",
  "uuid": "78345662-7910-4450-ad99-809e7cb717bc",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 148_

<details open><summary>🔧 Tool call — Read · `toolu_01SftH4vCJoa2tzhiU7GQ1TQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_qwen15b_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "575bacdc-7c67-41c8-991a-7703c899432c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wwc2E1y47hDQfQe93Vqo7C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 54088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 294,
        "ephemeral_1h_input_tokens": 0
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

_source line 149 · 2026-05-25T20:13:48.728Z_

<details><summary>↩ Tool result · `toolu_01SftH4vCJoa2tzhiU7GQ1TQ`</summary>

```text
1	% Qwen2.5-1.5B cross-scale results
2	\begin{table}[t]
3	\centering
4	\footnotesize
5	\caption{Cross-scale validation on Qwen2.5-1.5B-Instruct. Phase~1 confirms the GAR decay pattern at smaller scale (79.8\% relative drop). Phase~2 shows TG improves AR at $\beta=0$ (unamplified, $p{=}0.005$) and $\beta=5$ (strong amplification, $p{<}0.001$), confirming the mechanism transfers across model sizes.}
6	\label{tab:qwen15b_results}
7	\resizebox{\columnwidth}{!}{
8	\begin{tabular}{@{}ll cc c@{}}
9	\toprule
10	\textbf{Phase} & \textbf{Metric} & \textbf{Base} & \textbf{TG} & \textbf{$p$-value} \\
11	\midrule
12	\multicolumn{5}{@{}l}{\textit{Phase 1: GAR diagnostic}} \\
13	\quad & Turn-1 GAR & 0.0336 & --- & --- \\
14	\quad & Mid-turn GAR & 0.0068 & --- & --- \\
15	\quad & Relative drop & 79.8\% & --- & --- \\
16	\midrule
17	\multicolumn{5}{@{}l}{\textit{Phase 2: TG training ($\beta$-amplified AR)}} \\
18	\quad & AR @ $\beta{=}0$ & 0.0167 {\scriptsize$\pm$0.005} & \textbf{0.0233} {\scriptsize$\pm$0.006} & 0.005$^{**}$ \\
19	\quad & AR @ $\beta{=}3$ & 0.1202 {\scriptsize$\pm$0.032} & 0.1143 {\scriptsize$\pm$0.019} & 0.815 \\
20	\quad & AR @ $\beta{=}5$ & 0.6571 {\scriptsize$\pm$0.020} & \textbf{0.7150} {\scriptsize$\pm$0.017} & $<$0.001$^{***}$ \\
21	\bottomrule
22	\end{tabular}}
23	\vspace{1mm}
24	\begin{flushleft}
25	\scriptsize
26	$\pm$ values are 95\% CI half-widths. Significance via Wilcoxon signed-rank test ($N{=}39$ paired conversations). Effect sizes: $r{=}0.447$ ($\beta{=}0$), $r{=}0.749$ ($\beta{=}5$).
27	\end{flushleft}
28	\end{table}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "5590931a-0b7c-4748-914f-78ccedba510d"
}
```

</details>

---


### System

_source line 150_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "usage": {
    "total_tokens": 59288,
    "tool_uses": 11,
    "duration_ms": 62006
  },
  "last_tool_name": "Read",
  "uuid": "06b4ef12-5620-414e-90d9-68fbbc175203",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 151_

<details open><summary>🔧 Tool call — Read · `toolu_015b1dJB3wA8EGqRSfDA5E9P`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 2000,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "95ecd301-fa62-4ecd-952e-67aa7c144fb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kTBqLf5RDiqRj9Q8Q5JYg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10281,
      "cache_read_input_tokens": 48733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10281,
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

_source line 152 · 2026-05-25T20:13:50.843Z_

<details><summary>↩ Tool result · `toolu_015b1dJB3wA8EGqRSfDA5E9P`</summary>

```text
2000	  "gpu": "cuda:0",
2001	  "reproduce": {
2002	    "server": "westd-20861",
2003	    "gpu": "cuda:0",
2004	    "started_at": "2026-05-18T11:45:26.657Z",
2005	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0\""
2006	  },
2007	  "spec": {
2008	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating/src && python train_phase2.py --gate-type threadgate --seed 42 --output-dir /root/turn_residual_gating/checkpoints/tg_s42_v2 --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-seq-len 2048 --gar-loss-mode cumulative --gar-epsilon 0.001 --init-bias 2.0 --lambda-gar 5.0\"",
2009	    "server": "westd-20861",
2010	    "gpu": [
2011	      "cuda:0"
2012	    ],
2013	    "pid": "25726",
2014	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v2.log",
2015	    "submitted_at": "2026-05-18T11:50:47.143Z",
2016	    "submitted_via": "submit_training_job",
2017	    "backend": "tmux",
2018	    "account": "root",
2019	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_s42_v2",
2020	    "wall_clock_seconds": 4839.2,
2021	    "gpu_hours": 1.34
2022	  },
2023	  "pid": "25726",
2024	  "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v2.log",
2025	  "conclusion": "killed",
2026	  "completed_at": "2026-05-18T13:11:26.331Z"
2027	}
2028	
2029	================================================================================
2030	EXPERIMENT: phase2_tg_s42_v3
2031	================================================================================
2032	{
2033	  "status": "DONE",
2034	  "retry_count": 0,
2035	  "created_at": "2026-05-18T13:07:54.463Z",
2036	  "updated_at": "2026-05-18T13:38:10.723Z",
2037	  "hypothesis": "ThreadGate + maximize GAR loss (L_GAR=-mean(GAR)) 提供持续非零梯度，避免 hinge loss 的退化平衡点，gate 值应随训练下降（学习到选择性干预），同时 NTP loss 正常收敛",
2038	  "parent": "phase2_tg_s42_v2",
2039	  "spec": {
2040	    "server": "westd-20861",
2041	    "gpu": "cuda:0",
2042	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2043	    "data_count": 8000,
2044	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
2045	    "seed": 42,
2046	    "command": "python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 2.0 --init-bias 2.0 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3 --data-dir /root/turn_residual_gating/data/ultrachat_8k",
2047	    "pid": "30973",
2048	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v3.log",
2049	    "checkpoint_source": "N/A (training from scratch with LoRA)",
2050	    "eval_data": "N/A (training experiment, not eval)",
2051	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v3"
2052	  },
2053	  "server": "westd-20861",
2054	  "gpu": "cuda:0",
2055	  "conclusion": "negative",
2056	  "metrics": {
2057	    "gate_mean_step0": 0.8743,
2058	    "gate_mean_step500": 0.8761,
2059	    "gate_delta": 0.004,
2060	    "gate_std": 0.001,
2061	    "final_ntp_loss": 0.94,
2062	    "final_gar_loss": -0.019,
2063	    "gar_contribution_pct": "2-4%",
2064	    "diagnosis": "gate frozen, GAR indirect gradient too weak"
2065	  },
2066	  "completed_at": "2026-05-18T13:38:10.723Z"
2067	}
2068	
2069	================================================================================
2070	EXPERIMENT: phase2_tg_s42_v3b
2071	================================================================================
2072	{
2073	  "status": "DONE",
2074	  "retry_count": 0,
2075	  "created_at": "2026-05-18T13:38:16.020Z",
2076	  "updated_at": "2026-05-18T14:51:42.486Z",
2077	  "hypothesis": "λ=10 + gate_lr=10x + init_bias=0.0 (sigmoid=0.5) 能否驱动 gate 产生 layer 间分化 (gate_std>0.05)？如果 500 步后 gate_std<0.02 且无选择性 → GAR-driven gating 梯度路径确认失败，需要 pivot",
2078	  "parent": "phase2_tg_s42_v3",
2079	  "spec": {
2080	    "command": "python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 10.0 --init-bias 0.0 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v3b --data-dir /root/turn_residual_gating/data/ultrachat_8k --max-steps 500",
2081	    "server": "westd-20861",
2082	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2083	    "data_count": 8000,
2084	    "model_name": "Qwen2.5-7B-Instruct",
2085	    "seed": 42,
2086	    "checkpoint_source": "from_scratch",
2087	    "eval_data": "N/A",
2088	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v3b",
2089	    "log_path": "/root/turn_residual_gating/runs/v3b_log.txt"
2090	  },
2091	  "conclusion": "success",
2092	  "metrics": {
2093	    "gate_std_final": 0.087,
2094	    "gate_mean_final": 0.9388,
2095	    "gate_min_final": 0.5352,
2096	    "gate_max_final": 0.9922,
2097	    "L4_gate": 0.535,
2098	    "L0_gate": 0.777,
2099	    "L_NTP_final": 0.7787,
2100	    "L_GAR_final": -0.9606,
2101	    "elapsed_seconds": 3565.9,
2102	    "optimizer_steps": 500,
2103	    "gate_grad_received": true
2104	  },
2105	  "completed_at": "2026-05-18T14:51:42.486Z"
2106	}
2107	
2108	================================================================================
2109	EXPERIMENT: phase2_tg_s42_v4
2110	================================================================================
2111	{
2112	  "status": "DONE",
2113	  "retry_count": 0,
2114	  "created_at": "2026-05-18T14:58:00.124Z",
2115	  "updated_at": "2026-05-18T16:50:36.202Z",
2116	  "hypothesis": "重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值",
2117	  "parent": "phase2_tg_s42_v3b",
2118	  "spec": {
2119	    "command": "python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v4 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3",
2120	    "server": "westd-20861",
2121	    "gpu": "cuda:0",
2122	    "pid": "36519",
2123	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2124	    "data_count": 8000,
2125	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
2126	    "seed": 42,
2127	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v4",
2128	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v4.log",
2129	    "checkpoint_source": "from_scratch",
2130	    "eval_data": "N/A"
2131	  },
2132	  "conclusion": "failed",
2133	  "completed_at": "2026-05-18T16:50:33.778Z",
2134	  "notes": "进程在模型加载后崩溃，服务器重启导致进程丢失，无 checkpoint。日志仅有模型加载输出，无训练 step。GPU 重启后异常（100% util + 0 MiB + 无进程）。需要 GPU 健康恢复后重跑。"
2135	}
2136	
2137	================================================================================
2138	EXPERIMENT: phase2_tg_s42_v5
2139	================================================================================
2140	{
2141	  "status": "DONE",
2142	  "retry_count": 0,
2143	  "created_at": "2026-05-18T17:10:23.229Z",
2144	  "updated_at": "2026-05-18T17:52:54.605Z",
2145	  "hypothesis": "重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值",
2146	  "parent": "phase2_tg_s42_v4",
2147	  "spec": {
2148	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v5 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
2149	    "server": "westd-20861",
2150	    "gpu": "cuda:0",
2151	    "pid": "3639",
2152	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v5.log",
2153	    "submitted_at": "2026-05-18T17:10:30.573Z",
2154	    "submitted_via": "submit_training_job",
2155	    "backend": "tmux",
2156	    "account": "root",
2157	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2158	    "data_count": 8000,
2159	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
2160	    "seed": 42,
2161	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v5",
2162	    "checkpoint_source": "from_scratch",
2163	    "eval_data": "N/A",
2164	    "wall_clock_seconds": 2539.4,
2165	    "gpu_hours": 0.71
2166	  },
2167	  "metrics": {
2168	    "step2000_gate_std": 0.0225,
2169	    "step2000_gate_mean": 0.9586,
2170	    "step2000_gate_min": 0.9062,
2171	    "step2000_gate_max": 0.9961,
2172	    "step2000_L_GAR": -0.8977,
2173	    "step2000_L_NTP": 0.7611,
2174	    "step2000_total_loss": -0.1365,
2175	    "step2400_gate_std": 0.0219,
2176	    "step2400_gate_mean": 0.9651,
2177	    "step2400_gate_min": 0.918,
2178	    "step2400_gate_max": 0.9961,
2179	    "step2400_profile": "L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996",
2180	    "L_GAR_saturated_at": -0.91,
2181	    "gate_range_compression": "0.918-0.996"
2182	  },
2183	  "conclusion": "negative",
2184	  "completed_at": "2026-05-18T17:52:49.951Z",
2185	  "notes": "maximize 模式 gate 分化失败：gate_std=0.022↓ gate_mean=0.965↑，与 v3/v3b 同类结构性问题。L_GAR 饱和在 -0.91，maximize 的无界性驱动 gate 趋向恒等（全通过=最大 GAR），丧失层选择性。D009 指令立即 kill，转 v6 smooth_saturation。"
2186	}
2187	
2188	================================================================================
2189	EXPERIMENT: phase2_tg_s42_v6
2190	================================================================================
2191	{
2192	  "status": "DONE",
2193	  "retry_count": 0,
2194	  "created_at": "2026-05-18T17:53:01.911Z",
2195	  "updated_at": "2026-05-22T04:37:13.229Z",
2196	  "hypothesis": "smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。",
2197	  "parent": "phase2_tg_s42_v5",
2198	  "spec": {
2199	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode smooth_saturation --gar-target 0.5 --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v6 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
2200	    "server": "westd-20861",
2201	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2202	    "data_count": 8000,
2203	    "model_name": "Qwen/Qwen2.5-7B-Instruct",
2204	    "seed": 42,
2205	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v6",
2206	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v6.log"
2207	  },
2208	  "metrics": {
2209	    "dryrun_step0_L_NTP": 2.0275,
2210	    "dryrun_step0_L_GAR": -0.0161,
2211	    "dryrun_step0_total_loss": 2.0114,
2212	    "dryrun_step4_L_NTP": 1.6544,
2213	    "dryrun_step4_L_GAR": -0.0147,
2214	    "dryrun_step4_total_loss": 1.6397,
2215	    "dryrun_gate_grad": true,
2216	    "dryrun_gate_mean_init": 0.8097,
2217	    "dryrun_gate_std_init": 0.0341,
2218	    "dryrun_gate_min_init": 0.6836,
2219	    "dryrun_gate_max_init": 0.8672,
2220	    "dryrun_gate_mean_step5": 0.8025,
2221	    "dryrun_gate_std_step5": 0.0842,
2222	    "dryrun_gate_min_step5": 0.5547,
2223	    "dryrun_gate_max_step5": 0.9805,
2224	    "gs50_gate_mean": 0.8117,
2225	    "gs50_gate_std": 0.0612,
2226	    "gs50_gate_min": 0.6836,
2227	    "gs50_gate_max": 0.9805,
2228	    "gs100_gate_mean": 0.8737,
2229	    "gs100_gate_std": 0.0367,
2230	    "gs100_gate_min": 0.8164,
2231	    "gs100_gate_max": 0.9766,
2232	    "gs100_L_NTP": 0.8151,
2233	    "gs100_L_GAR": -0.158,
2234	    "gs100_total_loss": 0.6571,
2235	    "gs100_profile_bottom3": "L12=0.816 L4=0.824 L13=0.824",
2236	    "gs100_profile_top3": "L27=0.977 L26=0.961 L23=0.914",
2237	    "gs143_L_GAR": -0.3876,
2238	    "gs143_gate_mean": 0.9227
2239	  },
2240	  "conclusion": "negative",
2241	  "notes": "smooth_saturation 与 maximize 同轨迹，单调 GAR 奖励导致恒等退化。step 100: gate_std=0.037↓ gate_mean=0.874↑，step ~143: L_GAR=-0.39 gate_mean=0.923。boundedness 只减缓退化速度不改变终态。D010 指令 kill 转 v7 MSE 双向 loss。",
2242	  "completed_at": "2026-05-18T18:18:07.869Z"
2243	}
2244	
2245	================================================================================
2246	EXPERIMENT: phase2_tg_s42_v7
2247	================================================================================
2248	{
2249	  "status": "DONE",
2250	  "retry_count": 0,
2251	  "created_at": "2026-05-18T18:17:45.739Z",
2252	  "updated_at": "2026-05-20T03:04:19.923Z",
2253	  "hypothesis": "MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。",
2254	  "parent": "phase2_tg_s42_v6",
2255	  "metrics": {
2256	    "eval_iid_ours_mid_gar": 0.5035,
2257	    "eval_iid_dongre_mid_gar": 0.0152,
2258	    "eval_iid_ppl": 2.784,
2259	    "eval_heldout_ours_mid_gar": 0.5035,
2260	    "eval_heldout_dongre_mid_gar": 0.0152,
2261	    "eval_heldout_ppl": 2.78,
2262	    "eval_modelgen_ours_mid_gar": 0.0157,
2263	    "eval_modelgen_dongre_mid_gar": 0.0194,
2264	    "eval_modelgen_ppl": 1.36,
2265	    "gate_mean_final": 0.9336,
2266	    "gate_std_final": 0.0492
2267	  },
2268	  "spec": {
2269	    "checkpoint_source": "from_scratch",
2270	    "eval_data": "N/A",
2271	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v7 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3\"",
2272	    "server": "westd-20861",
2273	    "gpu": "cuda:0",
2274	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2275	    "data_count": 8000,
2276	    "model_name": "Qwen2.5-7B-Instruct",
2277	    "seed": 42,
2278	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v7",
2279	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v7.log"
2280	  },
2281	  "reproduce": {
2282	    "finished_at": "2026-05-19T00:48:47.275Z"
2283	  },
2284	  "failure_reason": "process dead 5× with no sentinel/W&B — auto-resolved as failed",
2285	  "conclusion": "success",
2286	  "completed_at": "2026-05-19T00:48:47.463Z",
2287	  "extra": {
2288	    "hook_events": [
2289	      {
2290	        "event": "on_failed",
2291	        "action": "agent",
2292	        "ts": "2026-05-19T00:48:48.850580+00:00"
2293	      }
2294	    ]
2295	  },
2296	  "notes": "训练 3 epoch 完成 (21352s/5.9h)。最终 gate: mean=0.9336, std=0.0492, L3=0.801 L4=0.789 最低。Eval 完成：GAR-ours recovery +0.35pp (mid 0.0157 vs baseline 0.0122), GAR-Dongre recovery +0.72pp (mid 0.0194 vs baseline 0.0122)。Gate dynamic range 最大层: L23 diff=-0.2100, L14 diff=-0.1803。"
2297	}
2298	
2299	================================================================================
2300	EXPERIMENT: phase2_tg_s42_v8_schedsampling
2301	================================================================================
2302	{
2303	  "status": "DONE",
2304	  "retry_count": 0,
2305	  "created_at": "2026-05-19T15:02:00.223Z",
2306	  "updated_at": "2026-05-19T16:33:04.989Z",
2307	  "hypothesis": "Scheduled sampling 应用到 GAR loss（线性从 0→0.5 混合 teacher-forced + model-generated contexts）能缩小 v7 的 30x training-inference GAR gap。机制：在 model-generated context 上计算 GAR loss 迫使 attention pattern 适应推理时分布，直接 address teacher-forcing distribution shift。成功标准：inference GAR 显著高于 v7 的 0.016，PPL 不显著恶化（≤2.78+0.2）。",
2308	  "parent": "phase2_tg_s42_v7",
2309	  "spec": {
2310	    "command": "python src/train_phase2_v8.py --scheduled-sampling --ss-max-ratio 0.5",
2311	    "server": "westd-20861",
2312	    "gpu": "cuda:0",
2313	    "pid": 73838,
2314	    "log_path": "/root/turn_residual_gating/runs/phase2_tg_s42_v8_schedsampling/",
2315	    "submitted_at": "2026-05-19T15:43:01.461Z",
2316	    "submitted_via": "submit_training_job",
2317	    "backend": "tmux",
2318	    "account": "root",
2319	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2320	    "data_count": 8000,
2321	    "model_name": "Qwen2.5-7B-Instruct",
2322	    "seed": 42,
2323	    "checkpoint_source": "N/A (training from scratch with LoRA)",
2324	    "eval_data": "ultrachat_eval_heldout.json (post-training eval)",
2325	    "hyperparams": {
2326	      "lr": 0.0002,
2327	      "epochs": 3,
2328	      "grad_accum": 8,
2329	      "ss_max_ratio": 0.5,
2330	      "ss_gen_max_tokens": 256,
2331	      "ss_gen_temperature": 0.7
2332	    },
2333	    "estimated_hours": "8-9",
2334	    "checkpoint_path": "N/A (crashed at 5.8%)",
2335	    "wall_clock_seconds": 1611.0,
2336	    "gpu_hours": 0.45
2337	  },
2338	  "conclusion": "failed",
2339	  "completed_at": "2026-05-19T16:09:52.423Z",
2340	  "metrics": {
2341	    "killed_at_microstep": 1950,
2342	    "total_microsteps": 24000,
2343	    "completion_pct": 8.1,
2344	    "global_step_approx": 244,
2345	    "total_global_steps": 3000,
2346	    "ss_steps_observed": 1,
2347	    "tf_lgar_mean_step850_1400": 0.0062,
2348	    "tf_lgar_std": 0.0082,
2349	    "tf_lgar_collapse_step": 800,
2350	    "gate_mean_final": 0.93,
2351	    "ss_ratio_at_kill": 0.081,
2352	    "crash_reason": "killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad",
2353	    "design_flaw_ss_ramp_too_slow": true,
2354	    "design_flaw_no_ss_tf_separate_logging": true
2355	  },
2356	  "notes": "Director kill at micro-step ~1950 (8.1%). 原因: SS path code bug (D026) + GAR-ours 无推理 gap (D024)，实验无效。GPU 转入 plan_018 PCGrad。详情：(1) SS ratio 仅 0.081 时 kill，仅 1 条 SS step 被日志捕获，(2) TF L_GAR 在 step 800 坍塌到 ≈0.006（与 v7 一致），(3) GAR-ours 推理时 ≈0.50 ≈ target，SS 用 GAR-ours 训练无法验证 exposure bias mitigation，(4) lambda_gar=2.0 (vs v7 的 1.0) confound 未被充分触发。"
2357	}
2358	
2359	================================================================================
2360	EXPERIMENT: phase2_tg_s42_v8b_resume
2361	================================================================================
2362	{
2363	  "status": "DONE",
2364	  "retry_count": 0,
2365	  "created_at": "2026-05-20T10:08:29.483Z",
2366	  "updated_at": "2026-05-21T01:56:13.289Z",
2367	  "hypothesis": "从 epoch_0 checkpoint resume v8b scheduled sampling 训练。SS 线性混合 0→0.5 teacher-forced + model-generated contexts。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。",
2368	  "parent": "phase2_tg_s42_v8b_ss_fixed",
2369	  "spec": {
2370	    "command": "python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5 --resume checkpoints/tg_v8b_ss_fixed_s42/epoch_0",
2371	    "server": "westd-20861",
2372	    "data_path": "data/ultrachat_8k",
2373	    "data_count": 8000,
2374	    "model_name": "Qwen2.5-7B-Instruct",
2375	    "seed": 42,
2376	    "checkpoint_source": "phase2_tg_s42_v8b_ss_fixed/epoch_0",
2377	    "eval_data": "N/A (training experiment)",
2378	    "checkpoint_path": "checkpoints/tg_v8b_ss_fixed_s42",
2379	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v8b_resume.log"
2380	  },
2381	  "metrics": {
2382	    "training": {
2383	      "total_steps": 3000,
2384	      "epochs_completed": 3,
2385	      "wall_clock_hours": 8.1,
2386	      "final_loss": 0.933,
2387	      "final_ntp_loss": 0.9322,
2388	      "final_gar_loss": 0.0008,
2389	      "final_gate_mean": 0.9586,
2390	      "final_gate_std": 0.0582,
2391	      "ss_ratio": 0.5
2392	    },
2393	    "eval_iid": {
2394	      "gar_ours": 0.4983,
2395	      "gar_dongre": 0.3855,
2396	      "ppl": 2.78
2397	    },
2398	    "eval_modelgen": {
2399	      "gar_ours": 0.3177,
2400	      "gar_dongre": 0.3533,
2401	      "ppl": 1.38
2402	    },
2403	    "vs_v7": {
2404	      "iid_gar_ours_delta": -0.005,
2405	      "modelgen_gar_ours_delta": 0.302,
2406	      "gap_ratio_v7": 32,
2407	      "gap_ratio_v8b": 1.57
2408	    }
2409	  },
2410	  "conclusion": "success",
2411	  "completed_at": "2026-05-20T18:57:21.189Z"
2412	}
2413	
2414	================================================================================
2415	EXPERIMENT: phase2_tg_s42_v8b_ss_fixed
2416	================================================================================
2417	{
2418	  "status": "DONE",
2419	  "retry_count": 0,
2420	  "created_at": "2026-05-20T02:28:58.064Z",
2421	  "updated_at": "2026-05-20T09:30:04.080Z",
2422	  "spec": {
2423	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v8b.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5\"",
2424	    "server": "westd-20861",
2425	    "gpu": [
2426	      "cuda:0"
2427	    ],
2428	    "pid": "133321",
2429	    "log_path": "~/runs/turn_residual_gating/phase2_tg_s42_v8b_ss_fixed.log",
2430	    "submitted_at": "2026-05-20T02:28:58.001Z",
2431	    "submitted_via": "submit_training_job",
2432	    "backend": "tmux",
2433	    "account": "root",
2434	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2435	    "data_count": 8000,
2436	    "model_name": "Qwen2.5-7B-Instruct",
2437	    "seed": 42,
2438	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_v8b_ss_fixed_s42",
2439	    "checkpoint_source": "from_scratch",
2440	    "eval_data": "N/A",
2441	    "wall_clock_seconds": 24818.0,
2442	    "gpu_hours": 6.89
2443	  },
2444	  "hypothesis": "Fixed scheduled sampling (D026 三项 bug 修复后): 线性从 0→0.5 混合 teacher-forced + model-generated contexts 计算 GAR loss。如果 model-gen context 上的 GAR 训练能缩小 30x training-inference gap → exposure bias mitigation 有效，paper 从纯 negative 升级为 diagnosis + initial remedy。超参与 v7 一致 (lambda_gar=1.0, MSE+gate_div)，唯一变量是 SS path。成功标准：inference GAR 显著高于 v7 的 0.016 (至少 +1pp)，PPL 不恶化。",
2445	  "parent": "phase2_tg_s42_v7",
2446	  "failure_reason": "CUDA OOM: CUDA out of memory. Tried to allocate 448.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 247.19 MiB is free. Including non-PyTorch memory, this process has 50.68 GiB memory in use. Process 157667 has 26.76 GiB memory in use. Process 158713 ",
2447	  "conclusion": "failed",
2448	  "completed_at": "2026-05-20T09:22:35.962Z",
2449	  "notes": "CUDA OOM at Epoch 1 Step 4300 (loss.backward). 其他进程共享 GPU 导致显存不足: Process 157667 (26.76GB) + Process 158713 (17.28GB) + PyTorch 自身 45.21GB + 4.81GB reserved > 94.97GB 总容量。训练在 OOM 前正常收敛 (SS ratio=0.5, Loss~1.0, Gate~0.94)。有 epoch_0 checkpoint。需要独占 GPU 重跑。"
2450	}
2451	
2452	================================================================================
2453	EXPERIMENT: phase2_tg_s42_v9_pcgrad
2454	================================================================================
2455	{
2456	  "status": "DONE",
2457	  "retry_count": 2,
2458	  "created_at": "2026-05-19T16:13:21.907Z",
2459	  "updated_at": "2026-05-20T03:04:17.171Z",
2460	  "hypothesis": "PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。",
2461	  "parent": "phase2_tg_s42_v7",
2462	  "spec": {
2463	    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v9_pcgrad.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v9_pcgrad_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42\"",
2464	    "server": "westd-20861",
2465	    "gpu": [
2466	      "cuda:0"
2467	    ],
2468	    "pid": "83860",
2469	    "log_path": "/root/turn_residual_gating/logs/phase2_tg_v9_pcgrad_s42.log",
2470	    "submitted_at": "2026-05-19T17:42:10.820Z",
2471	    "submitted_via": "submit_training_job",
2472	    "backend": "tmux",
2473	    "account": "root",
2474	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_v9_pcgrad_s42",
2475	    "wall_clock_seconds": 30601.5,
2476	    "gpu_hours": 8.5
2477	  },
2478	  "reproduce": {
2479	    "finished_at": "2026-05-20T01:42:12.536Z"
2480	  },
2481	  "failure_reason": null,
2482	  "conclusion": "success",
2483	  "extra": {
2484	    "hook_events": [
2485	      {
2486	        "event": "on_failed",
2487	        "action": "agent",
2488	        "ts": "2026-05-19T17:35:39.776243+00:00",
2489	        "note": "第1次提交 EXIT_CODE=2 残留事件"
2490	      },
2491	      {
2492	        "event": "on_complete",
2493	        "action": "agent",
2494	        "ts": "2026-05-20T01:42:14.275822+00:00"
2495	      }
2496	    ]
2497	  },
2498	  "completed_at": null,
2499	  "notes": "D028 因果排除确认（M017 修正后）。训练: EXIT_CODE=0, 7.98h, 3 epochs。PCGrad cos_sim 从 -0.061→+0.055→-0.035 (围绕 0 振荡), NTP mag_ratio 2.8→28.8 持续增长。L_GAR 有 0-350 step 高原期后仍坍塌到≈0。IID eval (同 protocol 50 heldout convs): GAR-ours=0.5002 (vs v7 0.5035, diff -0.33pp), GAR-Dongre=0.0123 (vs v7 0.0152), PPL=2.780 (vs v7 2.784, diff 0.004, 无改善)。Model-gen eval (5 convs): GAR-ours=0.0151, PPL=1.50。结论: PCGrad 消除梯度方向冲突后所有 IID 指标均 ≈ v7（GAR、PPL、NTP 无变化），方向冲突因 NTP 幅度主导 (10-40x) 而 inconsequential。Exposure bias 是 30x gap 根因。",
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "9c320ddf-a2a1-435b-be62-5da69e5454b3"
}
```

</details>

---


### System

_source line 153_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "usage": {
    "total_tokens": 72120,
    "tool_uses": 12,
    "duration_ms": 76725
  },
  "last_tool_name": "Read",
  "uuid": "d79fb216-f5d9-469f-b1c5-ff1f50831188",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 154_

<details open><summary>🔧 Tool call — Read · `toolu_018GcNStt28Yn5BUNoVs62eD`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/b1ao2hclt.txt",
  "offset": 2500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "edc7d64e-d0f3-4a30-bead-8ed86cf78611",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117FbE3W3xQHumQqM3iBmL7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12796,
      "cache_read_input_tokens": 59014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12796,
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

_source line 155 · 2026-05-25T20:14:05.572Z_

<details><summary>↩ Tool result · `toolu_018GcNStt28Yn5BUNoVs62eD`</summary>

```text
2500	  "metrics": {
2501	    "eval_iid_ours_mid_gar": 0.5002,
2502	    "eval_iid_dongre_mid_gar": 0.0123,
2503	    "eval_iid_ppl": 2.78,
2504	    "eval_iid_ntp": 0.9752,
2505	    "eval_heldout_ours_mid_gar": 0.5002,
2506	    "eval_heldout_dongre_mid_gar": 0.0123,
2507	    "eval_heldout_ppl": 2.78,
2508	    "eval_heldout_ntp": 0.9752,
2509	    "eval_modelgen_ours_mid_gar": 0.0151,
2510	    "eval_modelgen_dongre_mid_gar": 0.0173,
2511	    "eval_modelgen_ppl": 1.5,
2512	    "vs_v7_iid_ppl_diff": 0.004,
2513	    "vs_v7_iid_gar_diff": -0.0033
2514	  }
2515	}
2516	
2517	================================================================================
2518	EXPERIMENT: phase2_ug_s42
2519	================================================================================
2520	{
2521	  "status": "DONE",
2522	  "retry_count": 0,
2523	  "created_at": "2026-05-18T06:04:17.643Z",
2524	  "updated_at": "2026-05-20T02:15:15.775Z",
2525	  "hypothesis": "Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform.",
2526	  "parent": "phase1_gar_diag",
2527	  "notes": "3 epoch 完成 (21994.5s/6.1h)。最终 gate: mean=0.9598, std=0.0518, L3=0.777 L5=0.812 最低。重要发现：uniform gate 模式下各层仍学出 per-layer 分化（L3=0.777 vs L27=1.000），与 ThreadGate v7 的 L3/L4 最低模式一致。这说明 per-layer variation 可能来自 LoRA+GAR loss 而非 gate architecture。",
2528	  "spec": {
2529	    "command": "python src/train_phase2.py --gate-type uniform --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_ug_s42 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3",
2530	    "server": "westd-20861",
2531	    "data_path": "/root/turn_residual_gating/data/ultrachat_8k",
2532	    "data_count": 8000,
2533	    "model_name": "Qwen2.5-7B-Instruct",
2534	    "seed": 42,
2535	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_ug_s42",
2536	    "log_path": "/root/turn_residual_gating/runs/phase2_ug_s42.log",
2537	    "checkpoint_source": "from_scratch",
2538	    "eval_data": "N/A"
2539	  },
2540	  "conclusion": "success",
2541	  "completed_at": "2026-05-19T06:53:13.931Z",
2542	  "metrics": {
2543	    "epoch0_avg_loss": 1.0019,
2544	    "epoch0_avg_ntp": 0.9755,
2545	    "epoch0_avg_gar": 0.0259,
2546	    "epoch0_avg_div": 0.0005,
2547	    "epoch1_avg_loss": 0.9447,
2548	    "epoch1_avg_ntp": 0.9435,
2549	    "epoch1_avg_gar": 0.0013,
2550	    "epoch1_avg_div": 0,
2551	    "epoch2_avg_loss": 0.9319,
2552	    "epoch2_avg_ntp": 0.9309,
2553	    "epoch2_avg_gar": 0.001,
2554	    "epoch2_avg_div": 0,
2555	    "final_gate_mean": 0.9598,
2556	    "final_gate_std": 0.0518,
2557	    "final_gate_min": 0.7773,
2558	    "final_gate_max": 1,
2559	    "final_profile_L3": 0.777,
2560	    "final_profile_L5": 0.812,
2561	    "final_profile_L0": 0.875,
2562	    "final_profile_L27": 1,
2563	    "training_time_seconds": 21994.5,
2564	    "training_time_hours": 6.1,
2565	    "global_steps": 7950,
2566	    "unexpected_per_layer_variation": true,
2567	    "eval_modelgen_ours_mid_gar": 0.0149,
2568	    "eval_modelgen_dongre_mid_gar": 0.0185,
2569	    "eval_modelgen_ppl": 1.396
2570	  },
2571	  "checkpoint_path": "/root/turn_residual_gating/runs/phase2_ug_s42",
2572	  "log_path": "/root/turn_residual_gating/runs/phase2_ug_s42.log"
2573	}
2574	
2575	================================================================================
2576	EXPERIMENT: qwen15b_phase1_diag
2577	================================================================================
2578	{
2579	  "status": "DONE",
2580	  "retry_count": 0,
2581	  "created_at": "2026-05-23T06:44:59.895Z",
2582	  "updated_at": "2026-05-24T06:53:23.496Z",
2583	  "hypothesis": "GAR attention decay toward system-prompt goal tokens is a general phenomenon across model scales, not specific to 7B. Qwen-2.5-1.5B-Instruct should also show progressive GAR decline across conversation turns, confirming the phenomenon is architecture-level rather than scale-dependent.",
2584	  "spec": {
2585	    "command": "python train_phase2.py --model Qwen/Qwen2.5-1.5B-Instruct --config configs/tg_v7.yaml --seed 42 --epochs 3",
2586	    "server": "westd-20861",
2587	    "data_path": "/root/turn-residual-gating/data/train_400.json",
2588	    "data_count": 400,
2589	    "model_name": "Qwen/Qwen2.5-1.5B-Instruct",
2590	    "seed": 42,
2591	    "checkpoint_path": "runs/qwen15b_tg_v7_s42/",
2592	    "log_path": "logs/qwen15b_phase1_diag.log"
2593	  },
2594	  "conclusion": "success",
2595	  "completed_at": "2026-05-24T06:53:23.496Z"
2596	}
2597	
2598	================================================================================
2599	EXPERIMENT: trc_baseline_v7_tg
2600	================================================================================
2601	{
2602	  "status": "DONE",
2603	  "retry_count": 0,
2604	  "created_at": "2026-05-20T07:18:17.576Z",
2605	  "updated_at": "2026-05-20T09:34:40.734Z",
2606	  "hypothesis": "如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。",
2607	  "parent": "phase2_tg_s42_v7",
2608	  "spec": {
2609	    "command": "bash scripts/launch_trc_baseline.sh",
2610	    "server": "westd-20861",
2611	    "gpu": [
2612	      "cuda:0"
2613	    ],
2614	    "pid": "158700",
2615	    "log_path": "/root/runs/turn_residual_gating/trc_baseline_v7_tg.log",
2616	    "submitted_at": "2026-05-20T07:18:38.202Z",
2617	    "submitted_via": "submit_training_job",
2618	    "backend": "tmux",
2619	    "account": "root",
2620	    "data_path": "/root/turn_residual_gating/data/standard_conversations.json",
2621	    "data_count": 5,
2622	    "model_name": "Qwen2.5-7B-Instruct",
2623	    "seed": 42,
2624	    "checkpoint_source": "phase2_tg_s42_v7 + phase2_lora_only_s42 + base",
2625	    "eval_data": "5 hardcoded multi-turn conversations x 10 turns",
2626	    "checkpoint_path": "/root/turn_residual_gating/runs/trc_baseline/",
2627	    "wall_clock_seconds": 7767.7,
2628	    "gpu_hours": 2.16
2629	  },
2630	  "conclusion": "success",
2631	  "completed_at": "2026-05-20T09:28:05.853Z",
2632	  "metrics": {
2633	    "v7_tg": {
2634	      "tf_trc": 0.3339,
2635	      "gen_trc": 0.3323,
2636	      "trc_gap": 0.0016,
2637	      "tf_tbp_ppl": 1.05,
2638	      "gen_tbp_ppl": 1.05
2639	    },
2640	    "lora_only": {
2641	      "tf_trc": 0.349,
2642	      "gen_trc": 0.4106,
2643	      "trc_gap": -0.0617,
2644	      "tf_tbp_ppl": 9.5,
2645	      "gen_tbp_ppl": 12
2646	    },
2647	    "base": {
2648	      "tf_trc": 0.1494,
2649	      "gen_trc": 0.1494,
2650	      "trc_gap": 0,
2651	      "tf_tbp_ppl": 2.05,
2652	      "gen_tbp_ppl": 2.05
2653	    }
2654	  },
2655	  "notes": "Cross-space 验证：exposure bias 是 attention-specific。v7 TG: TRC gap = +0.002 (近零)，hidden state 一致性在 TF/gen 之间无差异。对比 GAR 的 30x gap，TRC 无 gap → exposure bias 只扭曲 attention 分布，不影响 hidden state 层面。LoRA-only: 反转 gap (-0.062)，gen TRC 更高但 TBP PPL 严重恶化 (9.5→12.0)——hidden states \"坍缩\"趋同但信息量下降。Base: 零 gap（但可能有 eval 脚本 bug，gen 模式复用了 TF hidden states）。"
2656	}
2657	
2658	================================================================================
2659	EXPERIMENT: v7_tg_s123
2660	================================================================================
2661	{
2662	  "status": "DONE",
2663	  "retry_count": 0,
2664	  "created_at": "2026-05-21T15:16:39.923Z",
2665	  "updated_at": "2026-05-21T21:17:16.499Z",
2666	  "hypothesis": "v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。",
2667	  "parent": "phase2_tg_s42_v7",
2668	  "spec": {
2669	    "command": "bash scripts/launch_v7_tg_s123.sh",
2670	    "server": "westd-20861",
2671	    "data_path": "data/ultrachat_8k",
2672	    "data_count": 8000,
2673	    "model_name": "Qwen2.5-7B-Instruct",
2674	    "seed": 123,
2675	    "pid": 245628,
2676	    "gpu_index": 0,
2677	    "checkpoint_path": "/root/turn_residual_gating/runs/phase2_tg_s123_v7",
2678	    "log_path": "/root/turn_residual_gating/logs/v7_tg_s123.log",
2679	    "checkpoint_source": "N/A (from scratch)",
2680	    "eval_data": "N/A"
2681	  },
2682	  "conclusion": "success",
2683	  "checkpoint_path": "runs/phase2_tg_s123_v7/epoch_2",
2684	  "log_path": "logs/v7_tg_s123.log",
2685	  "metrics": {
2686	    "epoch_1": {
2687	      "avg_loss": 0.9447,
2688	      "avg_ntp_loss": 0.9434,
2689	      "avg_gar_loss": 0.0013,
2690	      "avg_div_loss": 0
2691	    },
2692	    "epoch_2": {
2693	      "avg_loss": 0.9315,
2694	      "avg_ntp_loss": 0.9305,
2695	      "avg_gar_loss": 0.001,
2696	      "avg_div_loss": 0
2697	    },
2698	    "final_gate": {
2699	      "mean": 0.9467,
2700	      "std": 0.051,
2701	      "min": 0.793,
2702	      "max": 1
2703	    },
2704	    "final_gate_profile": {
2705	      "L0": 0.883,
2706	      "L1": 0.793,
2707	      "L2": 0.996,
2708	      "L3": 0.988,
2709	      "L4": 0.984,
2710	      "L5": 0.797,
2711	      "L6": 0.961,
2712	      "L7": 0.918,
2713	      "L8": 0.965,
2714	      "L9": 0.934,
2715	      "L10": 0.969,
2716	      "L11": 0.918,
2717	      "L12": 0.926,
2718	      "L13": 0.941,
2719	      "L14": 0.93,
2720	      "L15": 0.965,
2721	      "L16": 0.941,
2722	      "L17": 0.91,
2723	      "L18": 0.961,
2724	      "L19": 0.965,
2725	      "L20": 0.973,
2726	      "L21": 0.988,
2727	      "L22": 0.969,
2728	      "L23": 0.98,
2729	      "L24": 0.98,
2730	      "L25": 0.984,
2731	      "L26": 0.988,
2732	      "L27": 1
2733	    },
2734	    "training_time_s": 21425.2
2735	  },
2736	  "completed_at": "2026-05-21T21:17:16.499Z"
2737	}
2738	
2739	================================================================================
2740	EXPERIMENT: v8b_ss_s123
2741	================================================================================
2742	{
2743	  "status": "DONE",
2744	  "retry_count": 0,
2745	  "created_at": "2026-05-21T04:29:28.197Z",
2746	  "updated_at": "2026-05-21T15:15:49.282Z",
2747	  "hypothesis": "v8b SS s42 成功（gap 32×→1.57×），s123 验证结果的 seed robustness。预期 model-gen GAR 同样显著提升，PPL 无恶化。",
2748	  "parent": "phase2_tg_s42_v8b_resume",
2749	  "spec": {
2750	    "command": "bash scripts/launch_v8b_ss_s123.sh",
2751	    "server": "westd-20861",
2752	    "data_path": "data/ultrachat_8k",
2753	    "data_count": 8000,
2754	    "model_name": "Qwen2.5-7B-Instruct",
2755	    "seed": 123,
2756	    "checkpoint_source": "N/A (from scratch)",
2757	    "eval_data": "N/A",
2758	    "checkpoint_path": "/root/turn_residual_gating/checkpoints/tg_v8b_ss_s123",
2759	    "log_path": "/root/turn_residual_gating/logs/v8b_ss_s123.log"
2760	  },
2761	  "conclusion": "success",
2762	  "metrics": {
2763	    "final_loss": 0.9316,
2764	    "final_ntp_loss": 0.9307,
2765	    "final_gar_loss": 0.0009,
2766	    "final_gate_mean": 0.9505,
2767	    "final_gate_std": 0.0508,
2768	    "final_gate_min": 0.7383,
2769	    "final_gate_max": 1,
2770	    "ss_used_ratio": 0.371,
2771	    "training_time_s": 38773.4,
2772	    "epoch0_loss": 1.0092,
2773	    "epoch1_loss": 0.9444,
2774	    "epoch2_loss": 0.9316
2775	  },
2776	  "completed_at": "2026-05-21T15:15:49.282Z"
2777	}
2778	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "9bd99d6a-f22e-4ec2-baa4-74237af81fa4"
}
```

</details>

---


### System

_source line 156_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "description": "Running Count experiments with/without metrics",
  "usage": {
    "total_tokens": 77609,
    "tool_uses": 13,
    "duration_ms": 90165
  },
  "last_tool_name": "Bash",
  "uuid": "e5692b05-259b-45f6-b1b9-b99e70f7c13d",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool call

_source line 157_

<details open><summary>🔧 Tool call — Bash · `toolu_01EFu1Q8kf57dJiegA4un1rQ`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt') as f:\n    raw = json.load(f)\n\nresult_str = raw['result']\ndata = json.loads(result_str)\nexperiments = data['data']['experiments']\n\n# Count experiments with metrics\nwith_metrics = 0\nwithout_metrics = 0\nfor eid, exp in experiments.items():\n    if 'metrics' in exp and exp['metrics']:\n        with_metrics += 1\n    else:\n        without_metrics += 1\n\nprint(f\"Experiments with metrics: {with_metrics}\")\nprint(f\"Experiments without metrics: {without_metrics}\")\n\n# List the ones without metrics\nfor eid, exp in sorted(experiments.items()):\n    if 'metrics' not in exp or not exp['metrics']:\n        print(f\"  NO METRICS: {eid} (status={exp.get('status')}, conclusion={exp.get('conclusion')})\")\nPYEOF\n",
  "description": "Count experiments with/without metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "19cb2861-0593-47ff-ba37-485ff5bb528d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YF1pPcPbe7E5nH8Z4qFy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5485,
      "cache_read_input_tokens": 71810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5485,
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

_source line 158 · 2026-05-25T20:14:19.069Z_

<details><summary>↩ Tool result · `toolu_01EFu1Q8kf57dJiegA4un1rQ`</summary>

```text
Experiments with metrics: 42
Experiments without metrics: 18
  NO METRICS: d048_queue_runner (status=PREPARING, conclusion=failed)
  NO METRICS: d048_split_softmax_eval (status=DONE, conclusion=failed)
  NO METRICS: d048_ss_s123 (status=DONE, conclusion=success)
  NO METRICS: d048_ss_s42_resume (status=PREPARING, conclusion=None)
  NO METRICS: d048_ss_s456 (status=DONE, conclusion=success)
  NO METRICS: llama_tg_training (status=PREPARING, conclusion=failed)
  NO METRICS: p0_ss_steering_eval (status=PREPARING, conclusion=killed)
  NO METRICS: p1_llama_ss_training (status=DONE, conclusion=success)
  NO METRICS: p1_ss_lora_only (status=DONE, conclusion=killed)
  NO METRICS: phase1a_multiseed_8runs (status=PREPARING, conclusion=None)
  NO METRICS: phase1a_multiseed_qwen (status=DONE, conclusion=killed)
  NO METRICS: phase1b_llama_complement (status=PREPARING, conclusion=None)
  NO METRICS: phase2_switching (status=DONE, conclusion=killed)
  NO METRICS: phase2_tf_ar_switching (status=QUEUED, conclusion=None)
  NO METRICS: phase2_tg_s42_v2 (status=DONE, conclusion=killed)
  NO METRICS: phase2_tg_s42_v4 (status=DONE, conclusion=failed)
  NO METRICS: phase2_tg_s42_v8b_ss_fixed (status=DONE, conclusion=failed)
  NO METRICS: qwen15b_phase1_diag (status=DONE, conclusion=success)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "7229ac90-6be9-43e1-b180-48bba20e5bb1"
}
```

</details>

---


### System

_source line 159_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "abd64e66887e6e7f7",
  "tool_use_id": "toolu_0126ddH2zuvchsxkYkbVEdSy",
  "status": "completed",
  "output_file": "",
  "summary": "Find tables and appendix data",
  "usage": {
    "total_tokens": 64138,
    "tool_uses": 22,
    "duration_ms": 190343
  },
  "uuid": "2f77b7d0-9257-434f-83f3-f7499d12888c",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool result

_source line 160 · 2026-05-25T20:16:03.769Z_

<details><summary>↩ Tool result · `toolu_0126ddH2zuvchsxkYkbVEdSy`</summary>

```text
Here is the complete report of all tables and their verbatim numbers.

---

## Main Text Tables

### Table 1: `tab:five-way` (in `sections/related_work.tex`, lines 12-35)
**Five-way comparison on Qwen-2.5-7B-Instruct.**

| Configuration | IID GAR-O | IID GAR-D | IID PPL | Held-out GAR-O | Held-out GAR-D | Held-out PPL | AR GAR-O | AR 95% CI | g_bar +/- sigma_g |
|---|---|---|---|---|---|---|---|---|---|
| Base | 0.01 | 0.00 | 4.23 | 0.01 | 0.00 | 4.34 | 0.019 | [.014, .024] | --- |
| ThreadGate | 0.50 | **0.02** | 2.78 | 0.50 | **0.02** | 2.78 | **0.064** | [.041, .091] | .93 +/- .05 |
| +PCGrad | 0.50 | 0.01 | 2.78 | 0.50 | 0.01 | 2.78 | 0.030 | [.023, .038] | --- |
| Uniform Gate | 0.49 | 0.01 | 2.78 | **0.51** | 0.01 | 2.78 | 0.033 | [.025, .043] | .96 +/- .05 |
| LoRA-only | 0.50 | 0.01 | 2.78 | 0.50 | 0.01 | 2.78 | 0.037 | [.027, .050] | 1.00 |

### Table 2: `tab:four-way` (in `experiments.tex`, lines 20-37)
**Four-way ablation on Qwen-2.5-7B-Instruct.**

| Configuration | IID GAR-O | IID GAR-D | IID PPL | Held-out GAR-O | Held-out GAR-D | Held-out PPL |
|---|---|---|---|---|---|---|
| Base | 0.01 | 0.00 | 4.23 | 0.01 | 0.00 | 4.34 |
| ThreadGate | 0.49 | 0.02 | 2.63 | 0.50 | 0.02 | 2.78 |
| Uniform Gate | 0.49 | 0.01 | 2.62 | 0.51 | 0.01 | 2.78 |
| LoRA-only | 0.49 | 0.01 | 2.63 | 0.50 | 0.01 | 2.78 |

### Table 3: `tab:grad-conflict` (in `analysis.tex`, lines 9-23)
**Gradient interaction between NTP and GAR.**

| Epoch | cos_sim | neg% | mag_ratio |
|---|---|---|---|
| 0 | -0.089 | 78.6 | 7.5x |
| 1 | -0.054 | 71.4 | 13.7x |
| 2 | -0.042 | 67.9 | 14.7x |

---

## Appendix Tables

### `tab:hyperparams` (appendix, lines 5-33)
**Training hyperparameters:**

| Parameter | Value |
|---|---|
| Base model | Qwen-2.5-7B-Instruct |
| LoRA rank / alpha | 16 / 32 |
| LoRA targets | q_proj, v_proj |
| Optimizer | AdamW (beta1=0.9, beta2=0.999) |
| Learning rate | 2e-4 |
| Gate LR mult | 10x |
| Batch / grad accum | 1 / 8 (eff. 8) |
| Epochs | 3 |
| Max seq length | 2048 |
| Training data | 8K UltraChat convs |
| Seed | 42 (+123 for TG, SS) |
| lambda_GAR / lambda_div | 1.0 / 1.0 |
| GAR target tau | 0.5 |
| Gate init bias | 1.5 (sigma ~= 0.82) |
| Gate hidden dim | 64 |
| Turn embed dim | 16 |
| GPU | RTX PRO 6000 (96 GB) |
| Training time | 6-8 h / variant |

### `tab:loss-iterations` (appendix, lines 47-64)
**Loss formulation iterations:**

| Version | Loss Family | Status | GAR | PPL |
|---|---|---|---|---|
| v1 | Cumulative | fail (GAR loss -> 0) | --- | --- |
| v2 | Cumulative + epsilon | fail (same trajectory) | --- | --- |
| v3 | Maximize (lambda=2) | fail (gate frozen) | --- | --- |
| v3b | Maximize (lambda=10) | fail (identity collapse) | --- | --- |
| v5 | Maximize (lambda=1) | fail (identity collapse) | --- | --- |
| v6 | Smooth saturation | fail (identity collapse) | --- | --- |
| v7 | MSE + gate div | **converged** | 0.50 | 2.78 |

### `tab:ir-results` (appendix, lines 87-103)
**Instruction retention by constraint category (beta=3 steering):**

| Category | beta=0 | beta=3 | Delta |
|---|---|---|---|
| Content | 61.9% | 85.7% | +23.8 pp |
| Position | 66.7% | 73.3% | +6.7 pp |
| Count | 100% | 100% | 0 |
| Format | 100% | 100% | 0 |
| **Overall** | 75.9% | 87.0% | +11.1 pp |

### `tab:n5-ar` (appendix, lines 115-131)
**AR GAR-ours on N=5 ten-turn conversations:**

| Configuration | AR GAR-O | Delta vs Table 1 |
|---|---|---|
| Base | 0.012 | -0.007 |
| ThreadGate | 0.016 | -0.048 |
| +PCGrad | 0.015 | -0.015 |
| Uniform Gate | 0.015 | -0.018 |
| LoRA-only | 0.025 | -0.012 |

### `tab:stat-tests` (appendix, lines 145-167)
**Consolidated statistical tests:**

| Comparison | Test | p | r |
|---|---|---|---|
| *AR GAR-ours (beta=0):* | | | |
| TG vs. Base | Wilcoxon | <0.001 | 0.802 |
| TG vs. LoRA-only | Wilcoxon | 0.004 | 0.454 |
| TG vs. +PCGrad | Wilcoxon | 0.002 | --- |
| SS vs. TG | Wilcoxon | <0.001 | 0.869 |
| *Gate conditioning (28 layers):* | | | |
| Turn 1 vs. Turn 21 | Wilcoxon | 3.7e-8 | 0.975 |
| *Instruction retention:* | | | |
| beta=0 vs. beta=3 | McNemar | 0.077 | --- |
| GAR--compliance | Pearson | 0.007 | 0.200 |

### `tab:llama-full` (appendix, lines 179-196)
**Llama-3.1-8B-Instruct complete results:**

| Config | TF GAR-O | TF PPL | AR GAR-O (mean) | AR GAR-O (median) |
|---|---|---|---|---|
| Base | 0.017 | 3.45 | 0.009 | 0.009 |
| ThreadGate | 0.484 | 2.57 | 0.043 | 0.018 |
| LoRA-only | 0.481 | 2.60 | 0.028 | 0.018 |
| **SS** | 0.477 | 2.82 | **0.166** | --- |

### `tab:gradient-crossmodel` (appendix, lines 219-232)
**Cross-model NTP-GAR gradient interaction:**

| Metric | Qwen-7B | Llama-8B |
|---|---|---|
| Mean cos sim | -0.042 | +0.005 |
| Neg-layer % | 67.9% | 53.1% |
| NTP/GAR mag ratio | 14.7x | 25.7x |

### `tab:steering-full` (appendix, lines 306-329)
**Full attention steering results:**

| beta | N=5 Gen GAR | N=5 Gen PPL | N=50 Gen GAR | N=50 Gen PPL | N=200 TF GAR | N=200 TF PPL |
|---|---|---|---|---|---|---|
| 0 | .028 | 1.41 | .064 +/- .081 | 1.43 +/- .10 | .535 | 2.62 |
| 0.5 | .029 | 1.39 | --- | --- | --- | --- |
| 1 | .035 | 1.36 | --- | --- | --- | --- |
| 2 | .062 | 1.41 | .128 +/- .110 | 1.48 +/- .14 | .611 | 2.69 |
| 3 | --- | --- | .556 +/- .060 | 1.56 +/- .17 | .788 | 2.93 |
| 4 | --- | --- | .644 +/- .061 | 1.67 +/- .22 | .817 | 3.49 |
| **5** | **.680** | **1.91** | **.727 +/- .061** | **1.77 +/- .27** | **.833** | **6.15** |
| 10 | .959 | 4.22 | .961 +/- .015 | 3.45 +/- 1.78 | .977 | 505.2 |

### `tab:gate-profile` (appendix, lines 342-362)
**Per-layer gate values for ThreadGate (seed 123), Qwen-2.5-7B:**

| L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|---|---|
| .883 | **.793** | .996 | .988 | .984 | **.797** | .961 | .918 |

| L8 | L9 | L10 | L11 | L12 | L13 | L14 | L15 |
|---|---|---|---|---|---|---|---|
| .965 | .934 | .969 | .918 | .926 | .941 | .930 | .965 |

| L16 | L17 | L18 | L19 | L20 | L21 | L22 | L23 |
|---|---|---|---|---|---|---|---|
| .941 | .910 | .961 | .965 | .973 | .988 | .969 | .980 |

| L24 | L25 | L26 | L27 | Summary |
|---|---|---|---|---|
| .980 | .984 | .988 | 1.00 | g_bar=.947, sigma=.051 |

### `tab:cost` (appendix, lines 387-410)
**Computational cost:**

| Config | Params | Time (h) | VRAM | Overhead |
|---|---|---|---|---|
| *Qwen-2.5-7B:* | | | | |
| LoRA-only | 4.2M | 6.0 | 42 GB | baseline |
| ThreadGate | 4.3M | 6.0 | 43 GB | +57K |
| +PCGrad | 4.3M | 8.0 | 43 GB | +33% |
| Uniform Gate | 4.3M | 6.0 | 43 GB | +57K |
| SS (s42) | 4.3M | 6.5 | 43 GB | +8% |
| SS (s123) | 4.3M | 10.8 | 43 GB | +80% |
| SS (s456) | 4.3M | 6.5 | 43 GB | +8% |
| *Llama-3.1-8B:* | | | | |
| LoRA-only | 4.2M | 7.0 | 45 GB | baseline |
| ThreadGate | 4.3M | 7.3 | 46 GB | +65K |

### `tab:examples` (appendix, lines 422-436)
**Qualitative steering examples (4-turn conversation):**

| Turn | beta=0 (unsteered) | beta=3 (steered) |
|---|---|---|
| 1 | check - Three bullet points, on-topic | check - Three bullet points, on-topic |
| 2 | check - Three bullet points, relevant | check - Three bullet points, relevant |
| 3 | ~ - Four bullet points, partially on-topic | check - Three bullet points, on-topic |
| 4 | X - Free-form paragraph, no bullets | check - Three bullet points, on-topic |

### `tab:data-stats` (appendix, lines 470-485)
**Training and evaluation data characteristics:**

| Property | Train | Eval (primary) |
|---|---|---|
| Conversations | 8,000 | 50 |
| Min user turns | 3 | 3 |
| Max sequence length | 2,048 | 2,048 |

### `tab:kl-perhead` (appendix, lines 530-543)
**Per-head TF-AR divergence statistics:**

| Metric | Base | TG |
|---|---|---|
| Mean Delta-GAR | 0.012 | 0.016 |
| Mean KL | 0.043 | 0.054 |
| Corr(TF_GAR, Delta-GAR) | 0.673 | 0.743 |

### `tab:gar-robust` (appendix, lines 555-569)
**Mid-turn GAR under four alternative definitions (N=50):**

| Definition | Base | TG | SS |
|---|---|---|---|
| Ours (last-token) | 0.015 | **0.325** | **0.458** |
| All-token | 0.015 | 0.025 | **0.366** |
| First-token | 0.022 | 0.039 | **0.412** |
| Goal-only | 0.005 | **0.310** | **0.444** |

### `tab:mmlu` (appendix, lines 579-597)
**MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct:**

| Model | Acc (%) | Delta vs Base |
|---|---|---|
| Base (LoRA-only) | 74.23 | --- |
| PCGrad | 73.86 | -0.38 |
| SS | 73.75 | -0.48 |
| LoRA-only | 73.57 | -0.66 |
| ThreadGate | 73.47 | -0.77 |
| Uniform Gate | 73.46 | -0.78 |

### `tab:1.5b-steering` (appendix, lines 607-625)
**Cross-scale beta-steering on Qwen-2.5-1.5B (N=50, AR):**

| Model | beta | AR GAR | PPL (median) |
|---|---|---|---|
| Base | 0 | 0.017 | 1.909 |
| TG | 0 | 0.023 | 1.897 |
| Base | 3 | 0.120 | 2.216 |
| TG | 3 | 0.114 | 1.975 |
| Base | 5 | 0.657 | 2.804 |
| TG | 5 | 0.715 | 2.624 |

### `tab:llama-ss-steering` (appendix, lines 796-807)
**Beta-steering on Llama-3.1-8B SS model (N=50, T=4):**

| | beta=0 | beta=3 | beta=5 |
|---|---|---|---|
| AR GAR | 0.166 | 0.173 | 0.791 |

### `tab:llama-vs-qwen-ss` (appendix, lines 818-837)
**Scheduled sampling comparison: Qwen-7B vs Llama-8B:**

| Metric | Qwen-7B | Llama-8B |
|---|---|---|
| SS epochs | 3 | 2 |
| TF GAR | 0.498 | 0.477 |
| AR GAR (beta=0) | 0.401 | 0.166 |
| TF/AR gap | 1.2x | 2.9x |
| Baseline TG gap | 7.8x | 27x (median) |
| Gap compression | 6.5x | 9.3x |
| AR GAR (beta=5) | 0.717 | 0.791 |
| TF PPL | 2.78 | 2.82 |
| AR PPL | 1.441 | 1.370 |

---

## Externally-Included Tables (from `artifacts/appendix_expansion/`)

### `tab:crossmodel-detail` (tab_crossmodel_detail.tex)
**Cross-model comparison:**

| Model | Condition | TF GAR | AR GAR | TF PPL | AR PPL | Gap |
|---|---|---|---|---|---|---|
| Qwen-7B | Base | 0.013 | 0.019 | 4.34 | 1.447 | 0.7x |
| Qwen-7B | TG | 0.504 | 0.064 | 2.78 | 1.432 | 7.9x |
| Qwen-7B | LoRA-only | 0.498 | 0.037 | 2.78 | 1.431 | 13.5x |
| Qwen-7B | **SS** | 0.498 | **0.401** | 2.78 | 1.441 | **1.2x** |
| Llama-8B | Base | 0.017 | 0.009 | 3.45 | 1.293 | 1.9x |
| Llama-8B | TG | 0.484 | 0.043 | 2.57 | 1.437 | 11.2x |
| Llama-8B | LoRA-only | 0.481 | 0.028 | 2.60 | 1.419 | 17.2x |
| Llama-8B | **SS** | 0.477 | **0.166** | 2.82 | 1.370 | **2.9x** |

### `tab:perseed-ss` (tab_perseed_ss.tex)
**Per-seed SS results on Qwen-2.5-7B:**

| Metric | Seed 42 | Seed 123 | Seed 456 | Mean +/- Std |
|---|---|---|---|---|
| *TF:* | | | | |
| GAR-ours | 0.502 | 0.554 | 0.496 | 0.517 +/- 0.032 |
| GAR-Dongre | 0.389 | 0.411 | 0.386 | 0.395 +/- 0.014 |
| PPL | 2.780 | 2.612 | 2.611 | 2.668 +/- 0.097 |
| *AR beta=0:* | | | | |
| GAR-ours | 0.347 | 0.423 | 0.433 | 0.401 +/- 0.047 |
| PPL | 1.442 | 1.441 | 1.439 | 1.441 +/- 0.002 |
| *AR beta=3:* | | | | |
| GAR-ours | 0.593 | 0.590 | 0.605 | 0.596 +/- 0.008 |
| PPL | 1.564 | 1.607 | 1.587 | 1.586 +/- 0.022 |
| *AR beta=5:* | | | | |
| GAR-ours | 0.717 | 0.717 | 0.716 | 0.717 +/- 0.001 |
| PPL | 1.779 | 1.785 | 1.804 | 1.789 +/- 0.013 |

### `tab:perseed-tg` (tab_perseed_tg.tex)
**Per-seed ThreadGate results on Qwen-2.5-7B:**

| Metric | Seed 42 | Seed 123 | Mean +/- Std |
|---|---|---|---|
| *TF:* | | | |
| GAR-ours | 0.504 | 0.505 | 0.504 +/- 0.001 |
| GAR-Dongre | 0.015 | 0.012 | 0.014 +/- 0.002 |
| PPL | 2.784 | 2.780 | 2.782 +/- 0.003 |
| *AR beta=0:* | | | |
| GAR-ours | 0.016 | 0.017 | 0.016 +/- 0.001 |
| GAR-Dongre | 0.019 | 0.018 | 0.019 +/- 0.001 |
| PPL | 1.360 | 1.386 | 1.373 +/- 0.018 |
| *Derived:* | | | |
| Gap ratio (TF/AR) | 32.1 | 30.6 | 31.4 +/- 1.1 |

### `tab:perturn-qwen` (tab_perturn_qwen.tex)
**Per-turn AR GAR-ours (beta=0) on Qwen-2.5-7B:**

| Config | Turn 1 | Turn 2 | Turn 3 | Turn 4 | Turn 5 |
|---|---|---|---|---|---|
| Base | .085 | .032 | .021 | .013 | .004 |
| ThreadGate | .130 | .073 | .059 | .043 | .066 |
| PCGrad | .090 | .038 | .028 | .029 | .027 |
| UG | .113 | .056 | .033 | .020 | .016 |
| LoRA-only | .107 | .059 | .030 | .049 | .040 |
| SS | **.458** | **.381** | **.344** | **.370** | **.365** |

### `tab:perturn-llama` (tab_perturn_llama.tex)
**Per-turn AR GAR-ours (beta=0) on Llama-3.1-8B:**

*Panel (a): N=20, T=4:*

| Config | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| Base | .028 | .013 | .009 | .008 |
| TG | .041 | .042 | .049 | .038 |
| LoRA-only | .033 | .049 | .025 | .031 |

*Panel (b): Base decay (N=5, T=10):*

| Turn | GAR-ours |
|---|---|
| 1 | .026 |
| 2 | .018 |
| 3 | .009 |
| 4 | .006 |
| 5 | .006 |
| 6 | .004 |
| 7 | .004 |
| 8 | .004 |
| 9 | .005 |
| 10 | .003 |

### `tab:dataset_stats` (tab_dataset_stats.tex)
**Dataset statistics:**

| Statistic | Value |
|---|---|
| Total conversations | 207,865 |
| After >=5 turn filter | 17,302 |
| Training | 8,000 |
| Held-out AR eval | 50 |
| IID GAR diagnostic | 50 |
| Instruction retention | 200 |
| Avg. assistant turns | 5.6 |
| Min / Max turns | 5 / 7 |

### `tab:gar_robustness` (tab_gar_robustness.tex)
**GAR robustness across token selection strategies (extended version with Turn-1 and Gap Ratio):**

| Token Selection | Condition | Turn-1 GAR | Mid-turn GAR | Gap Ratio |
|---|---|---|---|---|
| Last (ours) | Base | 0.0858 | 0.0152 | 5.64x |
| Last (ours) | TG | 0.3938 | 0.3254 | 1.21x |
| Last (ours) | SS | 0.5274 | 0.4582 | 1.15x |
| All tokens | Base | 0.1152 | 0.0152 | 7.57x |
| All tokens | TG | 0.1275 | 0.0253 | 5.04x |
| All tokens | SS | 0.5043 | 0.3658 | 1.38x |
| First token | Base | 0.2987 | 0.0224 | 13.32x |
| First token | TG | 0.3225 | 0.0392 | 8.24x |
| First token | SS | 0.7549 | 0.4118 | 1.83x |
| Goal-only | Base | 0.0110 | 0.0049 | 2.23x |
| Goal-only | TG | 0.3313 | 0.3103 | 1.07x |
| Goal-only | SS | 0.4528 | 0.4435 | 1.02x |

### `tab:statistical_tests` (tab_statistical_tests.tex)
**Full statistical significance tests (extended version with CIs):**

| beta | Comparison | Test | Stat | p | r | GAR [95% CI] | Sig |
|---|---|---|---|---|---|---|---|
| 0.0 | TG vs Base | Wilcoxon | W=31 | <.001 | .802 | .064[.041,.091] vs .019[.014,.024] | *** |
| 0.0 | TG vs LoRA | Wilcoxon | W=187 | .004 | .454 | .064[.041,.091] vs .037[.027,.050] | ** |
| 0.0 | SS vs TG | Wilcoxon | W=1 | <.001 | .869 | .347[.327,.366] vs .064[.041,.091] | *** |
| 0.0 | PCGrad vs TG | Wilcoxon | W=176 | .002 | .478 | .030[.023,.038] vs .064[.041,.091] | ** |
| 3.0 | TG vs Base | Wilcoxon | W=242 | .039 | .331 | .556[.538,.575] vs .531[.514,.550] | * |
| 3.0 | TG vs LoRA | Wilcoxon | W=376 | .852 | .031 | .556[.538,.575] vs .560[.541,.581] | n.s. |
| 3.0 | SS vs TG | Wilcoxon | W=207 | .010 | .409 | .593[.574,.613] vs .556[.538,.575] | ** |
| 3.0 | PCGrad vs TG | Wilcoxon | W=368 | .767 | .049 | .559[.543,.576] vs .556[.538,.575] | n.s. |
| 5.0 | TG vs Base | Wilcoxon | W=251 | .084 | .281 | .727[.708,.747] vs .704[.679,.730] | n.s. |
| 5.0 | TG vs LoRA | Wilcoxon | W=277 | .180 | .220 | .727[.708,.747] vs .708[.687,.729] | n.s. |
| 5.0 | SS vs TG | Wilcoxon | W=314 | .421 | .133 | .717[.696,.738] vs .727[.708,.747] | n.s. |
| 5.0 | PCGrad vs TG | Wilcoxon | W=266 | .133 | .246 | .708[.690,.727] vs .727[.708,.747] | n.s. |
| --- | beta=0 vs beta=3 | McNemar | chi2=3.13 | .077 | .200 (point-biserial) | Rate: .759 vs .870 (N=54) | n.s. (marginal) |

### `tab:mmlu_detail` (tab_mmlu_detail.tex)
**MMLU accuracy (%) by category:**

| Category | Base | TG | PCGrad | SS | LoRA-only | UG |
|---|---|---|---|---|---|---|
| STEM | 70.69 | 69.20 | 69.55 | 69.97 | 70.03 | 69.65 |
| Social Sciences | 77.28 | 76.92 | 76.79 | 76.83 | 77.08 | 77.02 |
| Humanities | 83.95 | 83.33 | 84.08 | 83.39 | 83.62 | 83.95 |
| Other | 68.25 | 67.59 | 68.12 | 67.95 | 67.06 | 66.80 |
| **Overall** | **74.23** | 73.47 | 73.86 | 73.75 | 73.57 | 73.46 |
| Delta | --- | -0.76 | -0.37 | -0.48 | -0.66 | -0.77 |

### `tab:qwen15b_results` (tab_qwen15b_results.tex)
**Cross-scale validation on Qwen-2.5-1.5B:**

| Phase | Metric | Base | TG | p-value |
|---|---|---|---|---|
| *Phase 1: GAR diagnostic* | | | | |
| | Turn-1 GAR | 0.0336 | --- | --- |
| | Mid-turn GAR | 0.0068 | --- | --- |
| | Relative drop | 79.8% | --- | --- |
| *Phase 2: TG training* | | | | |
| | AR @ beta=0 | 0.0167 +/- 0.005 | **0.0233** +/- 0.006 | 0.005** |
| | AR @ beta=3 | 0.1202 +/- 0.032 | 0.1143 +/- 0.019 | 0.815 |
| | AR @ beta=5 | 0.6571 +/- 0.020 | **0.7150** +/- 0.017 | <0.001*** |

Effect sizes: r=0.447 (beta=0), r=0.749 (beta=5).

---

**Summary of all tables found:**
- **3 main-text tables**: `tab:five-way`, `tab:four-way`, `tab:grad-conflict`
- **18 appendix tables defined inline**: `tab:hyperparams`, `tab:loss-iterations`, `tab:ir-results`, `tab:n5-ar`, `tab:stat-tests`, `tab:llama-full`, `tab:gradient-crossmodel`, `tab:steering-full`, `tab:gate-profile`, `tab:cost`, `tab:examples`, `tab:data-stats`, `tab:kl-perhead`, `tab:gar-robust`, `tab:mmlu`, `tab:1.5b-steering`, `tab:llama-ss-steering`, `tab:llama-vs-qwen-ss`
- **10 externally-included tables** (from `artifacts/appendix_expansion/`): `tab:crossmodel-detail`, `tab:perseed-ss`, `tab:perseed-tg`, `tab:perturn-qwen`, `tab:perturn-llama`, `tab:dataset_stats`, `tab:gar_robustness`, `tab:statistical_tests`, `tab:mmlu_detail`, `tab:qwen15b_results`

agentId: abd64e66887e6e7f7 (use SendMessage with to: 'abd64e66887e6e7f7' to continue this agent)
&lt;usage>total_tokens: 72067
tool_uses: 22
duration_ms: 190345&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4c4fc92d-c0fe-4ad1-9be9-22d968b2ca8e",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for all LaTeX table definitions in the paper at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/\n\n1. Find where Table 1 (tab:five-way) is defined - read the full table data\n2. Find where Table tab:gradient-crossmodel is defined\n3. Find any other tables referenced in the main text\n4. Read any appendix files that contain data referenced from the main text sections (especially appendix-hyper for hyperparameters, appendix-stats for p-values, appendix-ir for instruction retention)\n\nReport all numbers found in these tables verbatim.",
    "agentId": "abd64e66887e6e7f7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete report of all tables and their verbatim numbers.\n\n---\n\n## Main Text Tables\n\n### Table 1: `tab:five-way` (in `sections/related_work.tex`, lines 12-35)\n**Five-way comparison on Qwen-2.5-7B-Instruct.**\n\n| Configuration | IID GAR-O | IID GAR-D | IID PPL | Held-out GAR-O | Held-out GAR-D | Held-out PPL | AR GAR-O | AR 95% CI | g_bar +/- sigma_g |\n|---|---|---|---|---|---|---|---|---|---|\n| Base | 0.01 | 0.00 | 4.23 | 0.01 | 0.00 | 4.34 | 0.019 | [.014, .024] | --- |\n| ThreadGate | 0.50 | **0.02** | 2.78 | 0.50 | **0.02** | 2.78 | **0.064** | [.041, .091] | .93 +/- .05 |\n| +PCGrad | 0.50 | 0.01 | 2.78 | 0.50 | 0.01 | 2.78 | 0.030 | [.023, .038] | --- |\n| Uniform Gate | 0.49 | 0.01 | 2.78 | **0.51** | 0.01 | 2.78 | 0.033 | [.025, .043] | .96 +/- .05 |\n| LoRA-only | 0.50 | 0.01 | 2.78 | 0.50 | 0.01 | 2.78 | 0.037 | [.027, .050] | 1.00 |\n\n### Table 2: `tab:four-way` (in `experiments.tex`, lines 20-37)\n**Four-way ablation on Qwen-2.5-7B-Instruct.**\n\n| Configuration | IID GAR-O | IID GAR-D | IID PPL | Held-out GAR-O | Held-out GAR-D | Held-out PPL |\n|---|---|---|---|---|---|---|\n| Base | 0.01 | 0.00 | 4.23 | 0.01 | 0.00 | 4.34 |\n| ThreadGate | 0.49 | 0.02 | 2.63 | 0.50 | 0.02 | 2.78 |\n| Uniform Gate | 0.49 | 0.01 | 2.62 | 0.51 | 0.01 | 2.78 |\n| LoRA-only | 0.49 | 0.01 | 2.63 | 0.50 | 0.01 | 2.78 |\n\n### Table 3: `tab:grad-conflict` (in `analysis.tex`, lines 9-23)\n**Gradient interaction between NTP and GAR.**\n\n| Epoch | cos_sim | neg% | mag_ratio |\n|---|---|---|---|\n| 0 | -0.089 | 78.6 | 7.5x |\n| 1 | -0.054 | 71.4 | 13.7x |\n| 2 | -0.042 | 67.9 | 14.7x |\n\n---\n\n## Appendix Tables\n\n### `tab:hyperparams` (appendix, lines 5-33)\n**Training hyperparameters:**\n\n| Parameter | Value |\n|---|---|\n| Base model | Qwen-2.5-7B-Instruct |\n| LoRA rank / alpha | 16 / 32 |\n| LoRA targets | q_proj, v_proj |\n| Optimizer | AdamW (beta1=0.9, beta2=0.999) |\n| Learning rate | 2e-4 |\n| Gate LR mult | 10x |\n| Batch / grad accum | 1 / 8 (eff. 8) |\n| Epochs | 3 |\n| Max seq length | 2048 |\n| Training data | 8K UltraChat convs |\n| Seed | 42 (+123 for TG, SS) |\n| lambda_GAR / lambda_div | 1.0 / 1.0 |\n| GAR target tau | 0.5 |\n| Gate init bias | 1.5 (sigma ~= 0.82) |\n| Gate hidden dim | 64 |\n| Turn embed dim | 16 |\n| GPU | RTX PRO 6000 (96 GB) |\n| Training time | 6-8 h / variant |\n\n### `tab:loss-iterations` (appendix, lines 47-64)\n**Loss formulation iterations:**\n\n| Version | Loss Family | Status | GAR | PPL |\n|---|---|---|---|---|\n| v1 | Cumulative | fail (GAR loss -> 0) | --- | --- |\n| v2 | Cumulative + epsilon | fail (same trajectory) | --- | --- |\n| v3 | Maximize (lambda=2) | fail (gate frozen) | --- | --- |\n| v3b | Maximize (lambda=10) | fail (identity collapse) | --- | --- |\n| v5 | Maximize (lambda=1) | fail (identity collapse) | --- | --- |\n| v6 | Smooth saturation | fail (identity collapse) | --- | --- |\n| v7 | MSE + gate div | **converged** | 0.50 | 2.78 |\n\n### `tab:ir-results` (appendix, lines 87-103)\n**Instruction retention by constraint category (beta=3 steering):**\n\n| Category | beta=0 | beta=3 | Delta |\n|---|---|---|---|\n| Content | 61.9% | 85.7% | +23.8 pp |\n| Position | 66.7% | 73.3% | +6.7 pp |\n| Count | 100% | 100% | 0 |\n| Format | 100% | 100% | 0 |\n| **Overall** | 75.9% | 87.0% | +11.1 pp |\n\n### `tab:n5-ar` (appendix, lines 115-131)\n**AR GAR-ours on N=5 ten-turn conversations:**\n\n| Configuration | AR GAR-O | Delta vs Table 1 |\n|---|---|---|\n| Base | 0.012 | -0.007 |\n| ThreadGate | 0.016 | -0.048 |\n| +PCGrad | 0.015 | -0.015 |\n| Uniform Gate | 0.015 | -0.018 |\n| LoRA-only | 0.025 | -0.012 |\n\n### `tab:stat-tests` (appendix, lines 145-167)\n**Consolidated statistical tests:**\n\n| Comparison | Test | p | r |\n|---|---|---|---|\n| *AR GAR-ours (beta=0):* | | | |\n| TG vs. Base | Wilcoxon | <0.001 | 0.802 |\n| TG vs. LoRA-only | Wilcoxon | 0.004 | 0.454 |\n| TG vs. +PCGrad | Wilcoxon | 0.002 | --- |\n| SS vs. TG | Wilcoxon | <0.001 | 0.869 |\n| *Gate conditioning (28 layers):* | | | |\n| Turn 1 vs. Turn 21 | Wilcoxon | 3.7e-8 | 0.975 |\n| *Instruction retention:* | | | |\n| beta=0 vs. beta=3 | McNemar | 0.077 | --- |\n| GAR--compliance | Pearson | 0.007 | 0.200 |\n\n### `tab:llama-full` (appendix, lines 179-196)\n**Llama-3.1-8B-Instruct complete results:**\n\n| Config | TF GAR-O | TF PPL | AR GAR-O (mean) | AR GAR-O (median) |\n|---|---|---|---|---|\n| Base | 0.017 | 3.45 | 0.009 | 0.009 |\n| ThreadGate | 0.484 | 2.57 | 0.043 | 0.018 |\n| LoRA-only | 0.481 | 2.60 | 0.028 | 0.018 |\n| **SS** | 0.477 | 2.82 | **0.166** | --- |\n\n### `tab:gradient-crossmodel` (appendix, lines 219-232)\n**Cross-model NTP-GAR gradient interaction:**\n\n| Metric | Qwen-7B | Llama-8B |\n|---|---|---|\n| Mean cos sim | -0.042 | +0.005 |\n| Neg-layer % | 67.9% | 53.1% |\n| NTP/GAR mag ratio | 14.7x | 25.7x |\n\n### `tab:steering-full` (appendix, lines 306-329)\n**Full attention steering results:**\n\n| beta | N=5 Gen GAR | N=5 Gen PPL | N=50 Gen GAR | N=50 Gen PPL | N=200 TF GAR | N=200 TF PPL |\n|---|---|---|---|---|---|---|\n| 0 | .028 | 1.41 | .064 +/- .081 | 1.43 +/- .10 | .535 | 2.62 |\n| 0.5 | .029 | 1.39 | --- | --- | --- | --- |\n| 1 | .035 | 1.36 | --- | --- | --- | --- |\n| 2 | .062 | 1.41 | .128 +/- .110 | 1.48 +/- .14 | .611 | 2.69 |\n| 3 | --- | --- | .556 +/- .060 | 1.56 +/- .17 | .788 | 2.93 |\n| 4 | --- | --- | .644 +/- .061 | 1.67 +/- .22 | .817 | 3.49 |\n| **5** | **.680** | **1.91** | **.727 +/- .061** | **1.77 +/- .27** | **.833** | **6.15** |\n| 10 | .959 | 4.22 | .961 +/- .015 | 3.45 +/- 1.78 | .977 | 505.2 |\n\n### `tab:gate-profile` (appendix, lines 342-362)\n**Per-layer gate values for ThreadGate (seed 123), Qwen-2.5-7B:**\n\n| L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 |\n|---|---|---|---|---|---|---|---|\n| .883 | **.793** | .996 | .988 | .984 | **.797** | .961 | .918 |\n\n| L8 | L9 | L10 | L11 | L12 | L13 | L14 | L15 |\n|---|---|---|---|---|---|---|---|\n| .965 | .934 | .969 | .918 | .926 | .941 | .930 | .965 |\n\n| L16 | L17 | L18 | L19 | L20 | L21 | L22 | L23 |\n|---|---|---|---|---|---|---|---|\n| .941 | .910 | .961 | .965 | .973 | .988 | .969 | .980 |\n\n| L24 | L25 | L26 | L27 | Summary |\n|---|---|---|---|---|\n| .980 | .984 | .988 | 1.00 | g_bar=.947, sigma=.051 |\n\n### `tab:cost` (appendix, lines 387-410)\n**Computational cost:**\n\n| Config | Params | Time (h) | VRAM | Overhead |\n|---|---|---|---|---|\n| *Qwen-2.5-7B:* | | | | |\n| LoRA-only | 4.2M | 6.0 | 42 GB | baseline |\n| ThreadGate | 4.3M | 6.0 | 43 GB | +57K |\n| +PCGrad | 4.3M | 8.0 | 43 GB | +33% |\n| Uniform Gate | 4.3M | 6.0 | 43 GB | +57K |\n| SS (s42) | 4.3M | 6.5 | 43 GB | +8% |\n| SS (s123) | 4.3M | 10.8 | 43 GB | +80% |\n| SS (s456) | 4.3M | 6.5 | 43 GB | +8% |\n| *Llama-3.1-8B:* | | | | |\n| LoRA-only | 4.2M | 7.0 | 45 GB | baseline |\n| ThreadGate | 4.3M | 7.3 | 46 GB | +65K |\n\n### `tab:examples` (appendix, lines 422-436)\n**Qualitative steering examples (4-turn conversation):**\n\n| Turn | beta=0 (unsteered) | beta=3 (steered) |\n|---|---|---|\n| 1 | check - Three bullet points, on-topic | check - Three bullet points, on-topic |\n| 2 | check - Three bullet points, relevant | check - Three bullet points, relevant |\n| 3 | ~ - Four bullet points, partially on-topic | check - Three bullet points, on-topic |\n| 4 | X - Free-form paragraph, no bullets | check - Three bullet points, on-topic |\n\n### `tab:data-stats` (appendix, lines 470-485)\n**Training and evaluation data characteristics:**\n\n| Property | Train | Eval (primary) |\n|---|---|---|\n| Conversations | 8,000 | 50 |\n| Min user turns | 3 | 3 |\n| Max sequence length | 2,048 | 2,048 |\n\n### `tab:kl-perhead` (appendix, lines 530-543)\n**Per-head TF-AR divergence statistics:**\n\n| Metric | Base | TG |\n|---|---|---|\n| Mean Delta-GAR | 0.012 | 0.016 |\n| Mean KL | 0.043 | 0.054 |\n| Corr(TF_GAR, Delta-GAR) | 0.673 | 0.743 |\n\n### `tab:gar-robust` (appendix, lines 555-569)\n**Mid-turn GAR under four alternative definitions (N=50):**\n\n| Definition | Base | TG | SS |\n|---|---|---|---|\n| Ours (last-token) | 0.015 | **0.325** | **0.458** |\n| All-token | 0.015 | 0.025 | **0.366** |\n| First-token | 0.022 | 0.039 | **0.412** |\n| Goal-only | 0.005 | **0.310** | **0.444** |\n\n### `tab:mmlu` (appendix, lines 579-597)\n**MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct:**\n\n| Model | Acc (%) | Delta vs Base |\n|---|---|---|\n| Base (LoRA-only) | 74.23 | --- |\n| PCGrad | 73.86 | -0.38 |\n| SS | 73.75 | -0.48 |\n| LoRA-only | 73.57 | -0.66 |\n| ThreadGate | 73.47 | -0.77 |\n| Uniform Gate | 73.46 | -0.78 |\n\n### `tab:1.5b-steering` (appendix, lines 607-625)\n**Cross-scale beta-steering on Qwen-2.5-1.5B (N=50, AR):**\n\n| Model | beta | AR GAR | PPL (median) |\n|---|---|---|---|\n| Base | 0 | 0.017 | 1.909 |\n| TG | 0 | 0.023 | 1.897 |\n| Base | 3 | 0.120 | 2.216 |\n| TG | 3 | 0.114 | 1.975 |\n| Base | 5 | 0.657 | 2.804 |\n| TG | 5 | 0.715 | 2.624 |\n\n### `tab:llama-ss-steering` (appendix, lines 796-807)\n**Beta-steering on Llama-3.1-8B SS model (N=50, T=4):**\n\n| | beta=0 | beta=3 | beta=5 |\n|---|---|---|---|\n| AR GAR | 0.166 | 0.173 | 0.791 |\n\n### `tab:llama-vs-qwen-ss` (appendix, lines 818-837)\n**Scheduled sampling comparison: Qwen-7B vs Llama-8B:**\n\n| Metric | Qwen-7B | Llama-8B |\n|---|---|---|\n| SS epochs | 3 | 2 |\n| TF GAR | 0.498 | 0.477 |\n| AR GAR (beta=0) | 0.401 | 0.166 |\n| TF/AR gap | 1.2x | 2.9x |\n| Baseline TG gap | 7.8x | 27x (median) |\n| Gap compression | 6.5x | 9.3x |\n| AR GAR (beta=5) | 0.717 | 0.791 |\n| TF PPL | 2.78 | 2.82 |\n| AR PPL | 1.441 | 1.370 |\n\n---\n\n## Externally-Included Tables (from `artifacts/appendix_expansion/`)\n\n### `tab:crossmodel-detail` (tab_crossmodel_detail.tex)\n**Cross-model comparison:**\n\n| Model | Condition | TF GAR | AR GAR | TF PPL | AR PPL | Gap |\n|---|---|---|---|---|---|---|\n| Qwen-7B | Base | 0.013 | 0.019 | 4.34 | 1.447 | 0.7x |\n| Qwen-7B | TG | 0.504 | 0.064 | 2.78 | 1.432 | 7.9x |\n| Qwen-7B | LoRA-only | 0.498 | 0.037 | 2.78 | 1.431 | 13.5x |\n| Qwen-7B | **SS** | 0.498 | **0.401** | 2.78 | 1.441 | **1.2x** |\n| Llama-8B | Base | 0.017 | 0.009 | 3.45 | 1.293 | 1.9x |\n| Llama-8B | TG | 0.484 | 0.043 | 2.57 | 1.437 | 11.2x |\n| Llama-8B | LoRA-only | 0.481 | 0.028 | 2.60 | 1.419 | 17.2x |\n| Llama-8B | **SS** | 0.477 | **0.166** | 2.82 | 1.370 | **2.9x** |\n\n### `tab:perseed-ss` (tab_perseed_ss.tex)\n**Per-seed SS results on Qwen-2.5-7B:**\n\n| Metric | Seed 42 | Seed 123 | Seed 456 | Mean +/- Std |\n|---|---|---|---|---|\n| *TF:* | | | | |\n| GAR-ours | 0.502 | 0.554 | 0.496 | 0.517 +/- 0.032 |\n| GAR-Dongre | 0.389 | 0.411 | 0.386 | 0.395 +/- 0.014 |\n| PPL | 2.780 | 2.612 | 2.611 | 2.668 +/- 0.097 |\n| *AR beta=0:* | | | | |\n| GAR-ours | 0.347 | 0.423 | 0.433 | 0.401 +/- 0.047 |\n| PPL | 1.442 | 1.441 | 1.439 | 1.441 +/- 0.002 |\n| *AR beta=3:* | | | | |\n| GAR-ours | 0.593 | 0.590 | 0.605 | 0.596 +/- 0.008 |\n| PPL | 1.564 | 1.607 | 1.587 | 1.586 +/- 0.022 |\n| *AR beta=5:* | | | | |\n| GAR-ours | 0.717 | 0.717 | 0.716 | 0.717 +/- 0.001 |\n| PPL | 1.779 | 1.785 | 1.804 | 1.789 +/- 0.013 |\n\n### `tab:perseed-tg` (tab_perseed_tg.tex)\n**Per-seed ThreadGate results on Qwen-2.5-7B:**\n\n| Metric | Seed 42 | Seed 123 | Mean +/- Std |\n|---|---|---|---|\n| *TF:* | | | |\n| GAR-ours | 0.504 | 0.505 | 0.504 +/- 0.001 |\n| GAR-Dongre | 0.015 | 0.012 | 0.014 +/- 0.002 |\n| PPL | 2.784 | 2.780 | 2.782 +/- 0.003 |\n| *AR beta=0:* | | | |\n| GAR-ours | 0.016 | 0.017 | 0.016 +/- 0.001 |\n| GAR-Dongre | 0.019 | 0.018 | 0.019 +/- 0.001 |\n| PPL | 1.360 | 1.386 | 1.373 +/- 0.018 |\n| *Derived:* | | | |\n| Gap ratio (TF/AR) | 32.1 | 30.6 | 31.4 +/- 1.1 |\n\n### `tab:perturn-qwen` (tab_perturn_qwen.tex)\n**Per-turn AR GAR-ours (beta=0) on Qwen-2.5-7B:**\n\n| Config | Turn 1 | Turn 2 | Turn 3 | Turn 4 | Turn 5 |\n|---|---|---|---|---|---|\n| Base | .085 | .032 | .021 | .013 | .004 |\n| ThreadGate | .130 | .073 | .059 | .043 | .066 |\n| PCGrad | .090 | .038 | .028 | .029 | .027 |\n| UG | .113 | .056 | .033 | .020 | .016 |\n| LoRA-only | .107 | .059 | .030 | .049 | .040 |\n| SS | **.458** | **.381** | **.344** | **.370** | **.365** |\n\n### `tab:perturn-llama` (tab_perturn_llama.tex)\n**Per-turn AR GAR-ours (beta=0) on Llama-3.1-8B:**\n\n*Panel (a): N=20, T=4:*\n\n| Config | T1 | T2 | T3 | T4 |\n|---|---|---|---|---|\n| Base | .028 | .013 | .009 | .008 |\n| TG | .041 | .042 | .049 | .038 |\n| LoRA-only | .033 | .049 | .025 | .031 |\n\n*Panel (b): Base decay (N=5, T=10):*\n\n| Turn | GAR-ours |\n|---|---|\n| 1 | .026 |\n| 2 | .018 |\n| 3 | .009 |\n| 4 | .006 |\n| 5 | .006 |\n| 6 | .004 |\n| 7 | .004 |\n| 8 | .004 |\n| 9 | .005 |\n| 10 | .003 |\n\n### `tab:dataset_stats` (tab_dataset_stats.tex)\n**Dataset statistics:**\n\n| Statistic | Value |\n|---|---|\n| Total conversations | 207,865 |\n| After >=5 turn filter | 17,302 |\n| Training | 8,000 |\n| Held-out AR eval | 50 |\n| IID GAR diagnostic | 50 |\n| Instruction retention | 200 |\n| Avg. assistant turns | 5.6 |\n| Min / Max turns | 5 / 7 |\n\n### `tab:gar_robustness` (tab_gar_robustness.tex)\n**GAR robustness across token selection strategies (extended version with Turn-1 and Gap Ratio):**\n\n| Token Selection | Condition | Turn-1 GAR | Mid-turn GAR | Gap Ratio |\n|---|---|---|---|---|\n| Last (ours) | Base | 0.0858 | 0.0152 | 5.64x |\n| Last (ours) | TG | 0.3938 | 0.3254 | 1.21x |\n| Last (ours) | SS | 0.5274 | 0.4582 | 1.15x |\n| All tokens | Base | 0.1152 | 0.0152 | 7.57x |\n| All tokens | TG | 0.1275 | 0.0253 | 5.04x |\n| All tokens | SS | 0.5043 | 0.3658 | 1.38x |\n| First token | Base | 0.2987 | 0.0224 | 13.32x |\n| First token | TG | 0.3225 | 0.0392 | 8.24x |\n| First token | SS | 0.7549 | 0.4118 | 1.83x |\n| Goal-only | Base | 0.0110 | 0.0049 | 2.23x |\n| Goal-only | TG | 0.3313 | 0.3103 | 1.07x |\n| Goal-only | SS | 0.4528 | 0.4435 | 1.02x |\n\n### `tab:statistical_tests` (tab_statistical_tests.tex)\n**Full statistical significance tests (extended version with CIs):**\n\n| beta | Comparison | Test | Stat | p | r | GAR [95% CI] | Sig |\n|---|---|---|---|---|---|---|---|\n| 0.0 | TG vs Base | Wilcoxon | W=31 | <.001 | .802 | .064[.041,.091] vs .019[.014,.024] | *** |\n| 0.0 | TG vs LoRA | Wilcoxon | W=187 | .004 | .454 | .064[.041,.091] vs .037[.027,.050] | ** |\n| 0.0 | SS vs TG | Wilcoxon | W=1 | <.001 | .869 | .347[.327,.366] vs .064[.041,.091] | *** |\n| 0.0 | PCGrad vs TG | Wilcoxon | W=176 | .002 | .478 | .030[.023,.038] vs .064[.041,.091] | ** |\n| 3.0 | TG vs Base | Wilcoxon | W=242 | .039 | .331 | .556[.538,.575] vs .531[.514,.550] | * |\n| 3.0 | TG vs LoRA | Wilcoxon | W=376 | .852 | .031 | .556[.538,.575] vs .560[.541,.581] | n.s. |\n| 3.0 | SS vs TG | Wilcoxon | W=207 | .010 | .409 | .593[.574,.613] vs .556[.538,.575] | ** |\n| 3.0 | PCGrad vs TG | Wilcoxon | W=368 | .767 | .049 | .559[.543,.576] vs .556[.538,.575] | n.s. |\n| 5.0 | TG vs Base | Wilcoxon | W=251 | .084 | .281 | .727[.708,.747] vs .704[.679,.730] | n.s. |\n| 5.0 | TG vs LoRA | Wilcoxon | W=277 | .180 | .220 | .727[.708,.747] vs .708[.687,.729] | n.s. |\n| 5.0 | SS vs TG | Wilcoxon | W=314 | .421 | .133 | .717[.696,.738] vs .727[.708,.747] | n.s. |\n| 5.0 | PCGrad vs TG | Wilcoxon | W=266 | .133 | .246 | .708[.690,.727] vs .727[.708,.747] | n.s. |\n| --- | beta=0 vs beta=3 | McNemar | chi2=3.13 | .077 | .200 (point-biserial) | Rate: .759 vs .870 (N=54) | n.s. (marginal) |\n\n### `tab:mmlu_detail` (tab_mmlu_detail.tex)\n**MMLU accuracy (%) by category:**\n\n| Category | Base | TG | PCGrad | SS | LoRA-only | UG |\n|---|---|---|---|---|---|---|\n| STEM | 70.69 | 69.20 | 69.55 | 69.97 | 70.03 | 69.65 |\n| Social Sciences | 77.28 | 76.92 | 76.79 | 76.83 | 77.08 | 77.02 |\n| Humanities | 83.95 | 83.33 | 84.08 | 83.39 | 83.62 | 83.95 |\n| Other | 68.25 | 67.59 | 68.12 | 67.95 | 67.06 | 66.80 |\n| **Overall** | **74.23** | 73.47 | 73.86 | 73.75 | 73.57 | 73.46 |\n| Delta | --- | -0.76 | -0.37 | -0.48 | -0.66 | -0.77 |\n\n### `tab:qwen15b_results` (tab_qwen15b_results.tex)\n**Cross-scale validation on Qwen-2.5-1.5B:**\n\n| Phase | Metric | Base | TG | p-value |\n|---|---|---|---|---|\n| *Phase 1: GAR diagnostic* | | | | |\n| | Turn-1 GAR | 0.0336 | --- | --- |\n| | Mid-turn GAR | 0.0068 | --- | --- |\n| | Relative drop | 79.8% | --- | --- |\n| *Phase 2: TG training* | | | | |\n| | AR @ beta=0 | 0.0167 +/- 0.005 | **0.0233** +/- 0.006 | 0.005** |\n| | AR @ beta=3 | 0.1202 +/- 0.032 | 0.1143 +/- 0.019 | 0.815 |\n| | AR @ beta=5 | 0.6571 +/- 0.020 | **0.7150** +/- 0.017 | <0.001*** |\n\nEffect sizes: r=0.447 (beta=0), r=0.749 (beta=5).\n\n---\n\n**Summary of all tables found:**\n- **3 main-text tables**: `tab:five-way`, `tab:four-way`, `tab:grad-conflict`\n- **18 appendix tables defined inline**: `tab:hyperparams`, `tab:loss-iterations`, `tab:ir-results`, `tab:n5-ar`, `tab:stat-tests`, `tab:llama-full`, `tab:gradient-crossmodel`, `tab:steering-full`, `tab:gate-profile`, `tab:cost`, `tab:examples`, `tab:data-stats`, `tab:kl-perhead`, `tab:gar-robust`, `tab:mmlu`, `tab:1.5b-steering`, `tab:llama-ss-steering`, `tab:llama-vs-qwen-ss`\n- **10 externally-included tables** (from `artifacts/appendix_expansion/`): `tab:crossmodel-detail`, `tab:perseed-ss`, `tab:perseed-tg`, `tab:perturn-qwen`, `tab:perturn-llama`, `tab:dataset_stats`, `tab:gar_robustness`, `tab:statistical_tests`, `tab:mmlu_detail`, `tab:qwen15b_results`"
      }
    ],
    "totalDurationMs": 190345,
    "totalTokens": 72067,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8967,
      "cache_read_input_tokens": 54382,
      "output_tokens": 8717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8717,
          "cache_read_input_tokens": 54382,
          "cache_creation_input_tokens": 8967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8967,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 18,
      "searchCount": 4,
      "bashCount": 0,
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


### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a24bf7311cd045b90",
  "tool_use_id": "toolu_015ssicCAvnA5h5YRztQP8Qm",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry metrics for audit",
  "usage": {
    "total_tokens": 78508,
    "tool_uses": 13,
    "duration_ms": 296096
  },
  "uuid": "18fe9125-b966-48db-a285-8a107c316271",
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99"
}
```

---


### Tool result

_source line 162 · 2026-05-25T20:17:44.926Z_

<details><summary>↩ Tool result · `toolu_015ssicCAvnA5h5YRztQP8Qm`</summary>

```text
I now have the complete picture. Here is the full audit of all 60 experiments with every metric verbatim.

---

## FULL EXPERIMENT REGISTRY AUDIT (60 experiments)

### 1. analysis_attention_heatmap
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, 5 convs x 10 turns
- **Metrics:**
  - base_mean_goal_attn: 0.0136
  - base_decay: 0.875
  - tg_mean_goal_attn: 0.0232
  - tg_decay: 0.777
  - ug_mean_goal_attn: 0.0216
  - ug_decay: 0.803
  - lora_mean_goal_attn: 0.0216
  - lora_decay: 0.81
  - gating_incremental_benefit: "none"

### 2. analysis_gradient_conflict
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, v7 epoch 0/1/2 checkpoints
- **Metrics:**
  - epoch0_cos_sim: -0.089
  - epoch1_cos_sim: -0.054
  - epoch2_cos_sim: -0.042
  - epoch0_neg_layers_pct: 78.6
  - epoch1_neg_layers_pct: 71.4
  - epoch2_neg_layers_pct: 67.9
  - epoch0_mag_ratio: 7.5
  - epoch1_mag_ratio: 13.7
  - epoch2_mag_ratio: 14.7

### 3. attention_steering_eval200_tf
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, N=200, mode=tf, checkpoint=phase2_tg_s42_v7
- **Metrics:**
  - beta_0.0: mid_gar=0.5353, ppl=2.62
  - beta_2.0: mid_gar=0.6112, ppl=2.69
  - beta_3.0: mid_gar=0.788, ppl=2.93
  - beta_4.0: mid_gar=0.8165, ppl=3.49
  - beta_5.0: mid_gar=0.8325, ppl=6.15
  - beta_10.0: mid_gar=0.977, ppl=505.21
  - n_convs: 200, mode: "tf"

### 4. attention_steering_gen_n50
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct + v7 TG LoRA, N=50, mode=gen, checkpoint=phase2_tg_s42_v7
- **Metrics (corrected, per-conv mid_gar turns 2-7, >=3 turns):**
  - beta_0.0: mid_gar=0.0641, mid_gar_std=0.0809, ppl=1.4324, ppl_std=0.1029, n_valid=39
  - beta_2.0: mid_gar=0.128, mid_gar_std=0.1101, ppl=1.4822, ppl_std=0.1385, n_valid=39
  - beta_3.0: mid_gar=0.5558, mid_gar_std=0.0601, ppl=1.5605, ppl_std=0.1719, n_valid=39
  - beta_4.0: mid_gar=0.6439, mid_gar_std=0.0607, ppl=1.6674, ppl_std=0.2241, n_valid=39
  - beta_5.0: mid_gar=0.7271, mid_gar_std=0.0605, ppl=1.7723, ppl_std=0.2693, n_valid=38
  - beta_10.0: mid_gar=0.9612, mid_gar_std=0.0152, ppl=3.4517, ppl_std=1.7813, n_valid=39
  - n_convs_total: 50, n_convs_valid: 39, phase_transition_range: "[2, 3]"

### 5. attention_steering_v7_tg_gen (N=5, gen mode)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, N=5 convs, mode=gen, checkpoint=phase2_tg_s42_v7
- **Metrics:**
  - beta_0.0: mid_turns_avg_gar=0.028, avg_ppl=1.409
  - beta_0.5: mid_turns_avg_gar=0.0287, avg_ppl=1.387
  - beta_1.0: mid_turns_avg_gar=0.0349, avg_ppl=1.36
  - beta_2.0: mid_turns_avg_gar=0.062, avg_ppl=1.411
  - beta_5.0: mid_turns_avg_gar=0.6795, avg_ppl=1.908
  - beta_10.0: mid_turns_avg_gar=0.959, avg_ppl=4.22
  - phase_transition_range: "[2, 5]"
  - baseline_gar: 0.028
  - max_gar_at_acceptable_ppl: 0.6795
  - max_gar_at_acceptable_ppl_beta: 5

### 6. d048_eval_ss_s123
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct + SS s123 LoRA, seed=123, N_tf=200, N_ar=39
- **Metrics:**
  - tf_gar_ours: 0.5536
  - tf_gar_dongre: 0.4106
  - tf_ppl: 2.6123
  - ar_beta0_gar: 0.4231
  - ar_beta0_ppl: 1.4408
  - ar_beta3_gar: 0.5903
  - ar_beta3_ppl: 1.607
  - ar_beta5_gar: 0.7174
  - ar_beta5_ppl: 1.7852
  - n_convs_tf: 200, n_convs_ar: 39

### 7. d048_eval_ss_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct (SS s42), seed=42
- **Metrics (TF):**
  - base_gar_ours_mid: 0.0128
  - base_gar_dongre_mid: 0.0031
  - base_ppl: 4.34
  - base_ntp: 1.4
  - tg_gar_ours_mid: 0.5025
  - tg_gar_dongre_mid: 0.389
  - tg_ppl: 2.78
  - tg_ntp: 0.98
  - baseline_mid_gar: 0.0122
- **Metrics (AR):**
  - gar_ours_mid: 0.3887
  - gar_ours_ci_95: [0.3692, 0.3934]
  - ppl: 1.35
- gap_ratio: 1.29
- n_conversations_tf: 50, n_conversations_ar: 5

### 8. d048_eval_ss_s456
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct + SS s456 LoRA, seed=456, N_ar=50
- **Metrics:**
  - tf_gar_ours_mid: 0.4964
  - tf_gar_dongre_mid: 0.3862
  - ar_beta0_gar: 0.4325
  - ar_beta0_ppl: 1.4394
  - ar_beta3_gar: 0.605
  - ar_beta3_ppl: 1.5868
  - ar_beta5_gar: 0.7157
  - ar_beta5_ppl: 1.8045
  - n_convs_ar: 50

### 9. d048_final_ar_eval
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, 6 conditions, N=50 AR eval
- **Metrics (beta0):**
  - base_gar: 0.019
  - tg_gar: 0.064
  - ug_gar: 0.033
  - lo_gar: 0.037
  - pcgrad_gar: 0.03
  - ss_gar: 0.347
- **Metrics (beta3):**
  - base_gar: 0.531
  - tg_gar: 0.556
  - ss_gar: 0.593
- **Metrics (beta5):**
  - base_gar: 0.704
  - tg_gar: 0.727
  - ss_gar: 0.717
- **Wilcoxon (beta0):**
  - tg_vs_base_p: "<0.001"
  - tg_vs_base_r: 0.802
  - ss_vs_tg_p: "<0.001"
  - ss_vs_tg_r: 0.869
- **PPL:**
  - base: 1.447, tg: 1.432, ss: 1.442
- n_convs: 39

### 10. d048_queue_runner
- **Status:** PREPARING | **Conclusion:** failed
- **Metrics:** NONE

### 11. d048_split_softmax_eval
- **Status:** DONE | **Conclusion:** failed
- **Metrics:** NONE (bugs: system_prompt_len=0 hardcoded, gen mode NaN)

### 12. d048_ss_s123 (training only)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=2000, lr=2e-4, epochs=3, batch_size=1, grad_accum=8, ss_ratio=0.3
- **Metrics:** NONE (training run, see d048_eval_ss_s123 for eval)

### 13. d048_ss_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.3, epochs=3, lr=2e-4, batch_size=1, grad_accum=8
- **Metrics (training):**
  - final_avg_loss: 0.9326
  - final_ntp_loss: 0.932
  - final_gar_loss: 0.0007
  - gate_mean: 0.9527
  - gate_std: 0.0589
  - gate_min: 0.7383
  - gate_min_layer: "L4"
  - gate_max: 1
  - ss_usage: "4750/16000 (29.7%)"
  - ss_fallback: 0
  - epochs_completed: 3
  - wall_clock_s: 23418, wall_clock_h: 6.5

### 14. d048_ss_s42_resume
- **Status:** PREPARING | **Conclusion:** None
- **Metrics:** NONE

### 15. d048_ss_s456 (training only)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=456, data=2000, epochs=3, ss_ratio=0.3
- **Metrics:** NONE (training run, see d048_eval_ss_s456 for eval)

### 16. eval_llama_ar_n20
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct (Base/TG/LoRA-only), seed=42, N=20, T=4
- **Metrics (base):**
  - gar_ours_mean: 0.0088, gar_ours_std: 0.0056
  - gar_ours_median_per_conv: 0.0093
  - gar_ours_median_per_turn_pool: 0.0071
  - gar_ours_spike_ratio: "0%"
  - gar_dongre_mean: 0.0049, gar_dongre_std: 0.0013, gar_dongre_median: 0.0047
  - ngar_ours_mid: 0.1019, ngar_dongre_mid: 0.1171
  - ppl: 1.293, ppl_std: 0.07, ntp_loss: 0.2552
- **Metrics (tg):**
  - gar_ours_mean: 0.0434, gar_ours_std: 0.1002
  - gar_ours_median_per_conv: 0.0179
  - gar_ours_median_per_turn_pool: 0.0126
  - gar_ours_spike_ratio: "5% (2/40 turns GAR>=0.4)"
  - gar_dongre_mean: 0.0183, gar_dongre_std: 0.0198, gar_dongre_median: 0.0152
  - ngar_ours_mid: 0.5357, ngar_dongre_mid: 0.4436
  - ppl: 1.437, ppl_std: 0.077, ntp_loss: 0.3612
- **Metrics (lora_only):**
  - gar_ours_mean: 0.0284, gar_ours_std: 0.0481
  - gar_ours_median_per_conv: 0.0184
  - gar_ours_median_per_turn_pool: 0.0133
  - gar_ours_spike_ratio: "0%"
  - gar_dongre_mean: 0.0205, gar_dongre_std: 0.0241, gar_dongre_median: 0.016
  - ngar_ours_mid: 0.3488, ngar_dongre_mid: 0.4997
  - ppl: 1.419, ppl_std: 0.075, ntp_loss: 0.3483
- n_conversations: 20, n_turns: 4
- Rankings: TG(0.0434) > LO(0.0284) > Base(0.0088) [mean]; TG(0.0179) ~= LO(0.0184) > Base(0.0093) [median_per_conv]

### 17. eval_llama_lora_only_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct + LoRA-only, seed=42
- **Metrics (TF):**
  - gar_ours: 0.4807, gar_dongre: 0.0188
  - ngar_ours: 11.8031, ngar_dongre: 0.8261
  - ppl: 2.6, ntp_loss: 0.9366
  - N=50, T=4
- **Metrics (AR):**
  - gar_ours: 0.0617, gar_dongre: 0.0226
  - ngar_ours: 0.6065, ngar_dongre: 0.2537
  - ppl: 1.32, ntp_loss: 0.2787
  - N=5, T=10
- gap_ratio_gar_ours: 7.79

### 18. eval_v7_tg_s123
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123
- **Metrics (iid_tf):**
  - gar_ours_mid: 0.5052, gar_dongre_mid: 0.0119
  - ppl: 2.7802, ntp: 0.9752
- **Metrics (modelgen_ar):**
  - gar_ours_mid: 0.0165, gar_dongre_mid: 0.0177
  - ppl: 1.3855, ntp: 0.3223
- gap_ratio: 30.6
- comparison_s42: tf_gar_ours_delta=0.0017, ar_gar_ours_delta=0.0008, gap_ratio_delta=-1.4

### 19. eval_v8b_ss
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, checkpoint=tg_v8b_ss_fixed_s42
- **Metrics:**
  - iid_gar_ours: 0.4983, iid_gar_dongre: 0.3855, iid_ppl: 2.78
  - iid_ngar_ours: 13.5, iid_ngar_dongre: 22.68
  - modelgen_gar_ours: 0.3177, modelgen_gar_dongre: 0.3533, modelgen_ppl: 1.38
  - modelgen_ngar_ours: 4.47, modelgen_ngar_dongre: 5.92
  - iid_turn1_gar_ours: 0.5398
  - modelgen_turn1_gar_ours: 0.4333

### 20. eval_v8b_ss_s123
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123
- **Metrics (iid):**
  - gar_ours: 0.503, gar_dongre: 0.394
  - ppl: 2.781, ntp_loss: 0.976
  - n_conv: 50, n_turns: 3
- **Metrics (modelgen):**
  - gar_ours: 0.418, gar_dongre: 0.441
  - ppl: 1.389, ntp_loss: 0.325
  - n_conv: 5, n_turns: 10
- gap_ratio: 1.2
- base_iid_ppl: 4.338, base_modelgen_ppl: 1.351

### 21. instruction_retention_test
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct + v7 TG LoRA, seed=42, 18 prompts, beta=[0,3], 5 turns each
- **Metrics:**
  - late_turn_rate_beta0: 0.759
  - late_turn_rate_beta3: 0.87
  - late_turn_delta: 0.111
  - mcnemar_chi2: 3.125
  - mcnemar_p: 0.0771
  - gar_compliance_r: 0.2003
  - gar_compliance_p: 0.007
  - category_content_constraint: beta0=0.619, beta3=0.857, delta=0.238
  - category_count_constraint: beta0=1, beta3=1, delta=0
  - category_format_constraint: beta0=1, beta3=1, delta=0
  - category_position_constraint: beta0=0.667, beta3=0.733, delta=0.067

### 22. llama_ar_matched_eval
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct + TG LoRA, seed=42, N=50, T=4
- **Metrics:**
  - ar_base_ours: mid_gar=0.0082, ngar=0.1, ppl=1.267
  - ar_tg_ours: mid_gar=0.0388, ngar=0.493, ppl=1.413
  - ar_base_dongre: mid_gar=0.0051, ngar=0.12, ppl=1.267
  - ar_tg_dongre: mid_gar=0.018, ngar=0.431, ppl=1.413
  - tf_reference: tf_tg_ours_ngar=11.88, tf_base_ours_ngar=0.388, tf_tg_ours_raw=0.4836, tf_tg_dongre_raw=0.018
  - Matched gap: gar_ours_raw_gap="12.5x (TF 0.484 / AR 0.039)", gar_ours_ngar_gap="24.1x", gar_dongre_raw_gap="1.002x (zero gap)"
  - tg_over_base_ar_ours: "4.71x", tg_over_base_ar_dongre: "3.54x"

### 23. llama_eval_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42
- **Metrics (tf_base):** gar_ours=0.0166, ngar_ours=0.3882, gar_dongre=0.0038, ngar_dongre=0.163, ppl=3.45, N=50, T=4
- **Metrics (tf_tg):** gar_ours=0.4836, ngar_ours=11.8818, gar_dongre=0.018, ngar_dongre=0.7922, ppl=2.57, N=50, T=4
- **Metrics (ar_base):** gar_ours=0.0086, ngar_ours=0.0798, gar_dongre=0.0118, ngar_dongre=0.1265, ppl=1.24, N=5, T=10
- **Metrics (ar_tg):** gar_ours=0.0304, ngar_ours=0.2632, gar_dongre=0.0217, ngar_dongre=0.2459, ppl=1.32, N=5, T=10
- gap_ratio_tg_ours: 15.9
- gap_ratio_base_ours: 1.93
- gap_ratio_tg_dongre: 0.83
- vs_qwen_v7_gap_ratio: 32.1
- baseline_mid_gar: 0.0122

### 24. llama_lora_only_s42 (training)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=8000, epochs=3
- **Metrics:**
  - final_avg_loss: 0.9288, final_avg_ntp: 0.9279, final_avg_gar: 0.0009
  - gate_fixed: 1, gate_type: "none"
  - wall_clock_s: 25317, wall_clock_h: 7.03
  - epochs_completed: 3

### 25. llama_phase1_gar_diag
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, 5 convs x 10 turns, gen mode
- **Metrics:**
  - per_turn_gar: turn_1=0.0263, turn_2=0.0183, turn_3=0.0087, turn_4=0.0055, turn_5=0.006, turn_6=0.0035, turn_7=0.0038, turn_8=0.0037, turn_9=0.005, turn_10=0.0026
  - t1_t10_decay_pct: 90.1
  - t1_mid38_drop_pct: 80.2

### 26. llama_tg_s42 (training)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=8000, epochs=3, lr=2e-4, batch_size=1, grad_accum=8
- **Metrics:**
  - epochs_completed: 3, total_steps: 3000
  - wall_clock_seconds: 26212, wall_clock_hours: 7.28
  - final_avg_loss: 0.9233, final_avg_ntp: 0.9224, final_avg_gar: 0.0009, final_avg_div: 0
  - final_gate_mean: 0.9099, final_gate_std: 0.0701
  - final_gate_min: 0.7188, final_gate_max: 0.9922
  - **Gate profile (32 layers):** L0=0.957, L1=0.973, L2=0.977, L3=0.965, L4=0.992, L5=0.969, L6=0.957, L7=0.957, L8=0.961, L9=0.949, L10=0.938, L11=0.934, L12=0.969, L13=0.953, L14=0.957, L15=0.965, L16=0.953, L17=0.961, L18=0.922, L19=0.902, L20=0.883, L21=0.863, L22=0.836, L23=0.844, L24=0.809, L25=0.719, L26=0.762, L27=0.805, L28=0.801, L29=0.855, L30=0.898, L31=0.934
  - checkpoint_size_gate_mb: 4.2, checkpoint_size_lora_mb: 26
  - GPU: NVIDIA RTX PRO 6000 Blackwell, vram_gb: 102, mem_used_gb: 63.4

### 27. llama_tg_training
- **Status:** PREPARING | **Conclusion:** failed
- **Metrics:** NONE (phantom duplicate of llama_tg_s42)

### 28. mmlu_eval_all
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, MMLU 5-shot, 14042 examples
- **Metrics (MMLU scores):**
  - base_qwen: 0.7423
  - pcgrad_v9_s42: 0.7386
  - ss_v8b_s42: 0.7375
  - lo_s42: 0.7357
  - tg_v7_s42: 0.7347
  - ug_s42: 0.7346

### 29. p0_ss_steering_eval
- **Status:** PREPARING | **Conclusion:** killed
- **Metrics:** NONE (cancelled, existing data sufficient)

### 30. p1_llama_ss_eval
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, N=50, checkpoint=p1_llama_ss_s42/epoch_1
- **Metrics:**
  - ss_tf_gar: 0.477
  - ss_tf_ppl: 2.82
  - ss_ar_b0_gar: 0.1662
  - ss_ar_b0_ppl: 1.37
  - ss_ar_b5_gar: 0.7905
  - ss_ar_b5_ppl: 1.81
  - base_ar_gar: 0.0179
  - base_ar_ppl: 1.22
  - tf_ar_gap: 2.87

### 31. p1_llama_ss_training
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=400, lr=2e-4, batch_size=1, grad_accum=8, epochs=3, ss_max_ratio=0.3, lora_rank=16
- **Metrics:** NONE (training only)

### 32. p1_ss_lora_only
- **Status:** DONE | **Conclusion:** killed
- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=2000, ss_max_ratio=0.3, gate_type=none
- **Metrics:** NONE

### 33. p1_tf_ar_kl_divergence
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, 30 convs
- **Metrics:**
  - tg_delta_gar: 0.0165
  - base_delta_gar: 0.0122
  - tg_mean_kl: 0.054
  - base_mean_kl: 0.043
  - gate_kl_correlation: 0.11
  - high_kl_layers: "L23-L27, L9"
  - gar_robustness_ours_tg_base_ratio: 21.4
  - gar_robustness_goal_only_ratio: 63
  - gar_robustness_ours_all_ratio: 1.7
  - gar_robustness_ours_first_ratio: 1.8

### 34. p2_llama_gradient_conflict
- **Status:** DONE | **Conclusion:** success
- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=400
- **Metrics:**
  - cos_sim_mean: 0.0045
  - cos_sim_std: 0.07
  - neg_cos_sim_layers_pct: 53.1
  - mag_ratio_median: 25.7

### 35. phase1_gar_diag
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, 5 convs x 10 turns
- **Metrics:**
  - turn1_avg_gar: 0.0418
  - mid_turns_avg_gar: 0.0122
  - relative_drop: 0.708
  - per_turn_avg_gar: [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]

### 36. phase1a_multiseed_8runs
- **Status:** PREPARING | **Conclusion:** None
- **Metrics:** NONE

### 37. phase1a_multiseed_qwen
- **Status:** DONE | **Conclusion:** killed (30min timeout)
- **Metrics:** NONE

### 38. phase1b_llama_complement
- **Status:** PREPARING | **Conclusion:** None
- **Metrics:** NONE

### 39. phase2_4way_eval
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, training split eval
- **Metrics:**
  - base_ours_mid_gar: 0.0107, base_ours_recovery_pp: -0.15
  - base_dongre_mid_gar: 0.003, base_dongre_recovery_pp: -0.92
  - base_ppl: 4.23, base_ntp: 1.4162
  - tg_ours_mid_gar: 0.4866, tg_ours_recovery_pp: 47.44
  - tg_dongre_mid_gar: 0.0157, tg_dongre_recovery_pp: 0.35
  - tg_ppl: 2.63, tg_ntp: 0.9484
  - ug_ours_mid_gar: 0.4923, ug_ours_recovery_pp: 48.01
  - ug_dongre_mid_gar: 0.013, ug_dongre_recovery_pp: 0.08
  - ug_ppl: 2.62, ug_ntp: 0.9433
  - lora_ours_mid_gar: 0.486, lora_ours_recovery_pp: 47.39
  - lora_dongre_mid_gar: 0.0137, lora_dongre_recovery_pp: 0.15
  - lora_ppl: 2.63, lora_ntp: 0.9482
  - route_b_confirmed: true, gating_incremental_benefit: "none"

### 40. phase2_4way_eval_heldout
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, held-out eval (50 convs, idx 8843-68199)
- **Metrics:**
  - base_ours_mid_gar: 0.0128, base_ours_recovery_pp: 0.06
  - base_dongre_mid_gar: 0.0031, base_dongre_recovery_pp: -0.91
  - base_ppl: 4.34, base_ntp: 1.4045
  - tg_ours_mid_gar: 0.5035, tg_ours_recovery_pp: 49.13
  - tg_dongre_mid_gar: 0.0152, tg_dongre_recovery_pp: 0.3
  - tg_ppl: 2.78, tg_ntp: 0.9771
  - ug_ours_mid_gar: 0.5053, ug_ours_recovery_pp: 49.31
  - ug_dongre_mid_gar: 0.0124, ug_dongre_recovery_pp: 0.02
  - ug_ppl: 2.78, ug_ntp: 0.9752
  - lora_ours_mid_gar: 0.4978, lora_ours_recovery_pp: 48.56
  - lora_dongre_mid_gar: 0.0132, lora_dongre_recovery_pp: 0.1
  - lora_ppl: 2.78, lora_ntp: 0.9771
  - three_way_convergence_confirmed: true
  - gar_ours_spread_pp: 0.75, ppl_spread: 0, data_overlap: false

### 41. phase2_lora_only_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=8000, epochs=3, gate_type=none
- **Metrics:**
  - epochs_completed: 3, global_steps: 3000
  - training_time_seconds: 20588.6, training_time_hours: 5.7
  - gate_fixed: 1, gate_type_actual: "none"
  - final_lora_size_mb: 20
  - eval_modelgen_ours_mid_gar: 0.0245
  - eval_modelgen_dongre_mid_gar: 0.0185
  - eval_modelgen_ppl: 1.371

### 42. phase2_switching
- **Status:** DONE | **Conclusion:** killed
- **Metrics:** NONE

### 43. phase2_tf_ar_switching
- **Status:** QUEUED | **Conclusion:** None
- **Metrics:** NONE

### 44. phase2_tg_s42 (v1)
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=8000
- **Metrics:**
  - final_ntp_loss: 0.94
  - final_gar_loss: 0
  - gate_mean: 0.988
  - gar_loss_zero_pct: 87.6
  - epochs_completed: 1.67
  - killed_reason: "SIGTERM by diagnose worker (unauthorized)"

### 45. phase2_tg_s42_v2
- **Status:** DONE | **Conclusion:** killed
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=cumulative, gar_epsilon=0.001, init_bias=2.0, lambda_gar=5.0
- **Metrics:** NONE

### 46. phase2_tg_s42_v3
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=maximize, lambda_gar=2.0, init_bias=2.0
- **Metrics:**
  - gate_mean_step0: 0.8743, gate_mean_step500: 0.8761
  - gate_delta: 0.004, gate_std: 0.001
  - final_ntp_loss: 0.94, final_gar_loss: -0.019
  - gar_contribution_pct: "2-4%"
  - diagnosis: "gate frozen, GAR indirect gradient too weak"

### 47. phase2_tg_s42_v3b
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, lambda_gar=10.0, init_bias=0.0, gate_lr_multiplier=10, max_steps=500
- **Metrics:**
  - gate_std_final: 0.087
  - gate_mean_final: 0.9388
  - gate_min_final: 0.5352
  - gate_max_final: 0.9922
  - L4_gate: 0.535, L0_gate: 0.777
  - L_NTP_final: 0.7787, L_GAR_final: -0.9606
  - elapsed_seconds: 3565.9, optimizer_steps: 500
  - gate_grad_received: true

### 48. phase2_tg_s42_v4
- **Status:** DONE | **Conclusion:** failed (server crash)
- **Metrics:** NONE

### 49. phase2_tg_s42_v5
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=maximize, lambda_gar=1.0, init_bias=1.5, gate_lr_multiplier=10, epochs=3
- **Metrics:**
  - step2000_gate_std: 0.0225, step2000_gate_mean: 0.9586
  - step2000_gate_min: 0.9062, step2000_gate_max: 0.9961
  - step2000_L_GAR: -0.8977, step2000_L_NTP: 0.7611, step2000_total_loss: -0.1365
  - step2400_gate_std: 0.0219, step2400_gate_mean: 0.9651
  - step2400_gate_min: 0.918, step2400_gate_max: 0.9961
  - step2400_profile: "L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996"
  - L_GAR_saturated_at: -0.91
  - gate_range_compression: "0.918-0.996"

### 50. phase2_tg_s42_v6
- **Status:** DONE | **Conclusion:** negative
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=smooth_saturation, gar_target=0.5, lambda_gar=1.0, init_bias=1.5, gate_lr_multiplier=10, epochs=3
- **Metrics:**
  - dryrun_step0: L_NTP=2.0275, L_GAR=-0.0161, total_loss=2.0114
  - dryrun_step4: L_NTP=1.6544, L_GAR=-0.0147, total_loss=1.6397
  - dryrun_gate_mean_init: 0.8097, dryrun_gate_std_init: 0.0341
  - dryrun_gate_min_init: 0.6836, dryrun_gate_max_init: 0.8672
  - dryrun_gate_mean_step5: 0.8025, dryrun_gate_std_step5: 0.0842
  - dryrun_gate_min_step5: 0.5547, dryrun_gate_max_step5: 0.9805
  - gs50: gate_mean=0.8117, gate_std=0.0612, gate_min=0.6836, gate_max=0.9805
  - gs100: gate_mean=0.8737, gate_std=0.0367, gate_min=0.8164, gate_max=0.9766
  - gs100: L_NTP=0.8151, L_GAR=-0.158, total_loss=0.6571
  - gs100_profile_bottom3: "L12=0.816 L4=0.824 L13=0.824"
  - gs100_profile_top3: "L27=0.977 L26=0.961 L23=0.914"
  - gs143_L_GAR: -0.3876, gs143_gate_mean: 0.9227

### 51. phase2_tg_s42_v7 (canonical)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=mse_target, gar_target=0.5, lambda_gar=1.0, lambda_gate_div=1.0, min_gate_std=0.05, init_bias=1.5, gate_lr_multiplier=10, epochs=3, data=8000
- **Metrics:**
  - eval_iid_ours_mid_gar: 0.5035
  - eval_iid_dongre_mid_gar: 0.0152
  - eval_iid_ppl: 2.784
  - eval_heldout_ours_mid_gar: 0.5035
  - eval_heldout_dongre_mid_gar: 0.0152
  - eval_heldout_ppl: 2.78
  - eval_modelgen_ours_mid_gar: 0.0157
  - eval_modelgen_dongre_mid_gar: 0.0194
  - eval_modelgen_ppl: 1.36
  - gate_mean_final: 0.9336
  - gate_std_final: 0.0492

### 52. phase2_tg_s42_v8_schedsampling
- **Status:** DONE | **Conclusion:** failed
- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.5, lr=2e-4, epochs=3
- **Metrics:**
  - killed_at_microstep: 1950, total_microsteps: 24000, completion_pct: 8.1
  - global_step_approx: 244, total_global_steps: 3000
  - ss_steps_observed: 1
  - tf_lgar_mean_step850_1400: 0.0062, tf_lgar_std: 0.0082, tf_lgar_collapse_step: 800
  - gate_mean_final: 0.93
  - ss_ratio_at_kill: 0.081

### 53. phase2_tg_s42_v8b_resume
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.5, epochs=3
- **Metrics (training):**
  - total_steps: 3000, epochs_completed: 3, wall_clock_hours: 8.1
  - final_loss: 0.933, final_ntp_loss: 0.9322, final_gar_loss: 0.0008
  - final_gate_mean: 0.9586, final_gate_std: 0.0582, ss_ratio: 0.5
- **Metrics (eval_iid):**
  - gar_ours: 0.4983, gar_dongre: 0.3855, ppl: 2.78
- **Metrics (eval_modelgen):**
  - gar_ours: 0.3177, gar_dongre: 0.3533, ppl: 1.38
- **vs_v7:**
  - iid_gar_ours_delta: -0.005
  - modelgen_gar_ours_delta: 0.302
  - gap_ratio_v7: 32, gap_ratio_v8b: 1.57

### 54. phase2_tg_s42_v8b_ss_fixed
- **Status:** DONE | **Conclusion:** failed (CUDA OOM at epoch 1 step 4300)
- **Metrics:** NONE (has epoch_0 checkpoint)

### 55. phase2_tg_s42_v9_pcgrad
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, PCGrad, same hyperparams as v7
- **Metrics:**
  - eval_iid_ours_mid_gar: 0.5002
  - eval_iid_dongre_mid_gar: 0.0123
  - eval_iid_ppl: 2.78
  - eval_iid_ntp: 0.9752
  - eval_heldout_ours_mid_gar: 0.5002
  - eval_heldout_dongre_mid_gar: 0.0123
  - eval_heldout_ppl: 2.78
  - eval_heldout_ntp: 0.9752
  - eval_modelgen_ours_mid_gar: 0.0151
  - eval_modelgen_dongre_mid_gar: 0.0173
  - eval_modelgen_ppl: 1.5
  - vs_v7_iid_ppl_diff: 0.004
  - vs_v7_iid_gar_diff: -0.0033

### 56. phase2_ug_s42
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, gate_type=uniform, data=8000, epochs=3
- **Metrics:**
  - epoch0: avg_loss=1.0019, avg_ntp=0.9755, avg_gar=0.0259, avg_div=0.0005
  - epoch1: avg_loss=0.9447, avg_ntp=0.9435, avg_gar=0.0013, avg_div=0
  - epoch2: avg_loss=0.9319, avg_ntp=0.9309, avg_gar=0.001, avg_div=0
  - final_gate_mean: 0.9598, final_gate_std: 0.0518
  - final_gate_min: 0.7773, final_gate_max: 1
  - final_profile: L3=0.777, L5=0.812, L0=0.875, L27=1
  - training_time_seconds: 21994.5, training_time_hours: 6.1, global_steps: 7950
  - unexpected_per_layer_variation: true
  - eval_modelgen_ours_mid_gar: 0.0149
  - eval_modelgen_dongre_mid_gar: 0.0185
  - eval_modelgen_ppl: 1.396

### 57. qwen15b_phase1_diag
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-1.5B-Instruct, seed=42, data=400, epochs=3
- **Metrics:** NONE (registered without metrics)

### 58. trc_baseline_v7_tg
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=42, 5 convs x 10 turns
- **Metrics (v7_tg):**
  - tf_trc: 0.3339, gen_trc: 0.3323, trc_gap: 0.0016
  - tf_tbp_ppl: 1.05, gen_tbp_ppl: 1.05
- **Metrics (lora_only):**
  - tf_trc: 0.349, gen_trc: 0.4106, trc_gap: -0.0617
  - tf_tbp_ppl: 9.5, gen_tbp_ppl: 12
- **Metrics (base):**
  - tf_trc: 0.1494, gen_trc: 0.1494, trc_gap: 0
  - tf_tbp_ppl: 2.05, gen_tbp_ppl: 2.05

### 59. v7_tg_s123 (training)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=8000
- **Metrics:**
  - epoch_1: avg_loss=0.9447, avg_ntp_loss=0.9434, avg_gar_loss=0.0013, avg_div_loss=0
  - epoch_2: avg_loss=0.9315, avg_ntp_loss=0.9305, avg_gar_loss=0.001, avg_div_loss=0
  - final_gate: mean=0.9467, std=0.051, min=0.793, max=1
  - **Gate profile (28 layers):** L0=0.883, L1=0.793, L2=0.996, L3=0.988, L4=0.984, L5=0.797, L6=0.961, L7=0.918, L8=0.965, L9=0.934, L10=0.969, L11=0.918, L12=0.926, L13=0.941, L14=0.93, L15=0.965, L16=0.941, L17=0.91, L18=0.961, L19=0.965, L20=0.973, L21=0.988, L22=0.969, L23=0.98, L24=0.98, L25=0.984, L26=0.988, L27=1
  - training_time_s: 21425.2

### 60. v8b_ss_s123 (training)
- **Status:** DONE | **Conclusion:** success
- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=8000
- **Metrics:**
  - final_loss: 0.9316, final_ntp_loss: 0.9307, final_gar_loss: 0.0009
  - final_gate_mean: 0.9505, final_gate_std: 0.0508
  - final_gate_min: 0.7383, final_gate_max: 1
  - ss_used_ratio: 0.371
  - training_time_s: 38773.4
  - epoch0_loss: 1.0092, epoch1_loss: 0.9444, epoch2_loss: 0.9316

---

## SUMMARY STATISTICS

- **Total experiments:** 60
- **With metrics:** 42
- **Without metrics:** 18 (7 failed/killed, 5 training-only with evals elsewhere, 4 PREPARING/QUEUED, 2 killed by user)
- **Successful with metrics:** 35
- **Key gap ratios:** v7 TG s42=32x, v7 TG s123=30.6x, v8b SS s42=1.57x, v8b SS s123=1.2x, d048 SS s42=1.29x, Llama TG=15.9x (raw)/12.5x (matched), Llama SS=2.87x, Llama LoRA-only=7.79x
- **MMLU retention:** All within 0.77pp of base (0.7423), confirming no general capability degradation
- **TRC values:** v7_tg tf=0.3339, gen=0.3323 (gap=0.0016); lora_only tf=0.349, gen=0.4106 (gap=-0.0617); base tf/gen=0.1494 (gap=0)

agentId: a24bf7311cd045b90 (use SendMessage with to: 'a24bf7311cd045b90' to continue this agent)
&lt;usage>total_tokens: 92083
tool_uses: 13
duration_ms: 296098&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "3d92dafd-1de0-441d-9a4b-0a57a2d40ccd",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Extract all experiment metrics from the registry JSON file at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99/tool-results/mcp-agent-ml-research-read_registry-1779739943919.txt\n\nThis is a JSON file with schema: {result: string}. The `result` field contains the actual registry data as a string (likely JSON itself).\n\nI need you to extract the following for EVERY experiment entry:\n1. Experiment ID/name\n2. Status\n3. All metrics (especially GAR-ours TF, GAR-ours AR, GAR-Dongre TF, GAR-Dongre AR, PPL, TF/AR gap ratios, MMLU scores)\n4. Spec info (model, lr, batch_size, epochs, steps, LoRA rank, dataset size, seed)\n5. Any scheduled sampling related metrics\n6. Any cross-model (Llama) related metrics\n7. Any steering ($\\beta$) related metrics\n8. Any gradient statistics (cosine similarity, magnitude ratios)\n9. Any instruction retention / compliance metrics\n10. Any TRC (Turn-level Residual Coherence) values\n\nUse bash with jq or python to parse. Report ALL numbers verbatim - do not summarize or round. I need exact values for an audit.",
    "agentId": "a24bf7311cd045b90",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have the complete picture. Here is the full audit of all 60 experiments with every metric verbatim.\n\n---\n\n## FULL EXPERIMENT REGISTRY AUDIT (60 experiments)\n\n### 1. analysis_attention_heatmap\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, 5 convs x 10 turns\n- **Metrics:**\n  - base_mean_goal_attn: 0.0136\n  - base_decay: 0.875\n  - tg_mean_goal_attn: 0.0232\n  - tg_decay: 0.777\n  - ug_mean_goal_attn: 0.0216\n  - ug_decay: 0.803\n  - lora_mean_goal_attn: 0.0216\n  - lora_decay: 0.81\n  - gating_incremental_benefit: \"none\"\n\n### 2. analysis_gradient_conflict\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, v7 epoch 0/1/2 checkpoints\n- **Metrics:**\n  - epoch0_cos_sim: -0.089\n  - epoch1_cos_sim: -0.054\n  - epoch2_cos_sim: -0.042\n  - epoch0_neg_layers_pct: 78.6\n  - epoch1_neg_layers_pct: 71.4\n  - epoch2_neg_layers_pct: 67.9\n  - epoch0_mag_ratio: 7.5\n  - epoch1_mag_ratio: 13.7\n  - epoch2_mag_ratio: 14.7\n\n### 3. attention_steering_eval200_tf\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, N=200, mode=tf, checkpoint=phase2_tg_s42_v7\n- **Metrics:**\n  - beta_0.0: mid_gar=0.5353, ppl=2.62\n  - beta_2.0: mid_gar=0.6112, ppl=2.69\n  - beta_3.0: mid_gar=0.788, ppl=2.93\n  - beta_4.0: mid_gar=0.8165, ppl=3.49\n  - beta_5.0: mid_gar=0.8325, ppl=6.15\n  - beta_10.0: mid_gar=0.977, ppl=505.21\n  - n_convs: 200, mode: \"tf\"\n\n### 4. attention_steering_gen_n50\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct + v7 TG LoRA, N=50, mode=gen, checkpoint=phase2_tg_s42_v7\n- **Metrics (corrected, per-conv mid_gar turns 2-7, >=3 turns):**\n  - beta_0.0: mid_gar=0.0641, mid_gar_std=0.0809, ppl=1.4324, ppl_std=0.1029, n_valid=39\n  - beta_2.0: mid_gar=0.128, mid_gar_std=0.1101, ppl=1.4822, ppl_std=0.1385, n_valid=39\n  - beta_3.0: mid_gar=0.5558, mid_gar_std=0.0601, ppl=1.5605, ppl_std=0.1719, n_valid=39\n  - beta_4.0: mid_gar=0.6439, mid_gar_std=0.0607, ppl=1.6674, ppl_std=0.2241, n_valid=39\n  - beta_5.0: mid_gar=0.7271, mid_gar_std=0.0605, ppl=1.7723, ppl_std=0.2693, n_valid=38\n  - beta_10.0: mid_gar=0.9612, mid_gar_std=0.0152, ppl=3.4517, ppl_std=1.7813, n_valid=39\n  - n_convs_total: 50, n_convs_valid: 39, phase_transition_range: \"[2, 3]\"\n\n### 5. attention_steering_v7_tg_gen (N=5, gen mode)\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, N=5 convs, mode=gen, checkpoint=phase2_tg_s42_v7\n- **Metrics:**\n  - beta_0.0: mid_turns_avg_gar=0.028, avg_ppl=1.409\n  - beta_0.5: mid_turns_avg_gar=0.0287, avg_ppl=1.387\n  - beta_1.0: mid_turns_avg_gar=0.0349, avg_ppl=1.36\n  - beta_2.0: mid_turns_avg_gar=0.062, avg_ppl=1.411\n  - beta_5.0: mid_turns_avg_gar=0.6795, avg_ppl=1.908\n  - beta_10.0: mid_turns_avg_gar=0.959, avg_ppl=4.22\n  - phase_transition_range: \"[2, 5]\"\n  - baseline_gar: 0.028\n  - max_gar_at_acceptable_ppl: 0.6795\n  - max_gar_at_acceptable_ppl_beta: 5\n\n### 6. d048_eval_ss_s123\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct + SS s123 LoRA, seed=123, N_tf=200, N_ar=39\n- **Metrics:**\n  - tf_gar_ours: 0.5536\n  - tf_gar_dongre: 0.4106\n  - tf_ppl: 2.6123\n  - ar_beta0_gar: 0.4231\n  - ar_beta0_ppl: 1.4408\n  - ar_beta3_gar: 0.5903\n  - ar_beta3_ppl: 1.607\n  - ar_beta5_gar: 0.7174\n  - ar_beta5_ppl: 1.7852\n  - n_convs_tf: 200, n_convs_ar: 39\n\n### 7. d048_eval_ss_s42\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct (SS s42), seed=42\n- **Metrics (TF):**\n  - base_gar_ours_mid: 0.0128\n  - base_gar_dongre_mid: 0.0031\n  - base_ppl: 4.34\n  - base_ntp: 1.4\n  - tg_gar_ours_mid: 0.5025\n  - tg_gar_dongre_mid: 0.389\n  - tg_ppl: 2.78\n  - tg_ntp: 0.98\n  - baseline_mid_gar: 0.0122\n- **Metrics (AR):**\n  - gar_ours_mid: 0.3887\n  - gar_ours_ci_95: [0.3692, 0.3934]\n  - ppl: 1.35\n- gap_ratio: 1.29\n- n_conversations_tf: 50, n_conversations_ar: 5\n\n### 8. d048_eval_ss_s456\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct + SS s456 LoRA, seed=456, N_ar=50\n- **Metrics:**\n  - tf_gar_ours_mid: 0.4964\n  - tf_gar_dongre_mid: 0.3862\n  - ar_beta0_gar: 0.4325\n  - ar_beta0_ppl: 1.4394\n  - ar_beta3_gar: 0.605\n  - ar_beta3_ppl: 1.5868\n  - ar_beta5_gar: 0.7157\n  - ar_beta5_ppl: 1.8045\n  - n_convs_ar: 50\n\n### 9. d048_final_ar_eval\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, 6 conditions, N=50 AR eval\n- **Metrics (beta0):**\n  - base_gar: 0.019\n  - tg_gar: 0.064\n  - ug_gar: 0.033\n  - lo_gar: 0.037\n  - pcgrad_gar: 0.03\n  - ss_gar: 0.347\n- **Metrics (beta3):**\n  - base_gar: 0.531\n  - tg_gar: 0.556\n  - ss_gar: 0.593\n- **Metrics (beta5):**\n  - base_gar: 0.704\n  - tg_gar: 0.727\n  - ss_gar: 0.717\n- **Wilcoxon (beta0):**\n  - tg_vs_base_p: \"<0.001\"\n  - tg_vs_base_r: 0.802\n  - ss_vs_tg_p: \"<0.001\"\n  - ss_vs_tg_r: 0.869\n- **PPL:**\n  - base: 1.447, tg: 1.432, ss: 1.442\n- n_convs: 39\n\n### 10. d048_queue_runner\n- **Status:** PREPARING | **Conclusion:** failed\n- **Metrics:** NONE\n\n### 11. d048_split_softmax_eval\n- **Status:** DONE | **Conclusion:** failed\n- **Metrics:** NONE (bugs: system_prompt_len=0 hardcoded, gen mode NaN)\n\n### 12. d048_ss_s123 (training only)\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=2000, lr=2e-4, epochs=3, batch_size=1, grad_accum=8, ss_ratio=0.3\n- **Metrics:** NONE (training run, see d048_eval_ss_s123 for eval)\n\n### 13. d048_ss_s42\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.3, epochs=3, lr=2e-4, batch_size=1, grad_accum=8\n- **Metrics (training):**\n  - final_avg_loss: 0.9326\n  - final_ntp_loss: 0.932\n  - final_gar_loss: 0.0007\n  - gate_mean: 0.9527\n  - gate_std: 0.0589\n  - gate_min: 0.7383\n  - gate_min_layer: \"L4\"\n  - gate_max: 1\n  - ss_usage: \"4750/16000 (29.7%)\"\n  - ss_fallback: 0\n  - epochs_completed: 3\n  - wall_clock_s: 23418, wall_clock_h: 6.5\n\n### 14. d048_ss_s42_resume\n- **Status:** PREPARING | **Conclusion:** None\n- **Metrics:** NONE\n\n### 15. d048_ss_s456 (training only)\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=456, data=2000, epochs=3, ss_ratio=0.3\n- **Metrics:** NONE (training run, see d048_eval_ss_s456 for eval)\n\n### 16. eval_llama_ar_n20\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct (Base/TG/LoRA-only), seed=42, N=20, T=4\n- **Metrics (base):**\n  - gar_ours_mean: 0.0088, gar_ours_std: 0.0056\n  - gar_ours_median_per_conv: 0.0093\n  - gar_ours_median_per_turn_pool: 0.0071\n  - gar_ours_spike_ratio: \"0%\"\n  - gar_dongre_mean: 0.0049, gar_dongre_std: 0.0013, gar_dongre_median: 0.0047\n  - ngar_ours_mid: 0.1019, ngar_dongre_mid: 0.1171\n  - ppl: 1.293, ppl_std: 0.07, ntp_loss: 0.2552\n- **Metrics (tg):**\n  - gar_ours_mean: 0.0434, gar_ours_std: 0.1002\n  - gar_ours_median_per_conv: 0.0179\n  - gar_ours_median_per_turn_pool: 0.0126\n  - gar_ours_spike_ratio: \"5% (2/40 turns GAR>=0.4)\"\n  - gar_dongre_mean: 0.0183, gar_dongre_std: 0.0198, gar_dongre_median: 0.0152\n  - ngar_ours_mid: 0.5357, ngar_dongre_mid: 0.4436\n  - ppl: 1.437, ppl_std: 0.077, ntp_loss: 0.3612\n- **Metrics (lora_only):**\n  - gar_ours_mean: 0.0284, gar_ours_std: 0.0481\n  - gar_ours_median_per_conv: 0.0184\n  - gar_ours_median_per_turn_pool: 0.0133\n  - gar_ours_spike_ratio: \"0%\"\n  - gar_dongre_mean: 0.0205, gar_dongre_std: 0.0241, gar_dongre_median: 0.016\n  - ngar_ours_mid: 0.3488, ngar_dongre_mid: 0.4997\n  - ppl: 1.419, ppl_std: 0.075, ntp_loss: 0.3483\n- n_conversations: 20, n_turns: 4\n- Rankings: TG(0.0434) > LO(0.0284) > Base(0.0088) [mean]; TG(0.0179) ~= LO(0.0184) > Base(0.0093) [median_per_conv]\n\n### 17. eval_llama_lora_only_s42\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct + LoRA-only, seed=42\n- **Metrics (TF):**\n  - gar_ours: 0.4807, gar_dongre: 0.0188\n  - ngar_ours: 11.8031, ngar_dongre: 0.8261\n  - ppl: 2.6, ntp_loss: 0.9366\n  - N=50, T=4\n- **Metrics (AR):**\n  - gar_ours: 0.0617, gar_dongre: 0.0226\n  - ngar_ours: 0.6065, ngar_dongre: 0.2537\n  - ppl: 1.32, ntp_loss: 0.2787\n  - N=5, T=10\n- gap_ratio_gar_ours: 7.79\n\n### 18. eval_v7_tg_s123\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=123\n- **Metrics (iid_tf):**\n  - gar_ours_mid: 0.5052, gar_dongre_mid: 0.0119\n  - ppl: 2.7802, ntp: 0.9752\n- **Metrics (modelgen_ar):**\n  - gar_ours_mid: 0.0165, gar_dongre_mid: 0.0177\n  - ppl: 1.3855, ntp: 0.3223\n- gap_ratio: 30.6\n- comparison_s42: tf_gar_ours_delta=0.0017, ar_gar_ours_delta=0.0008, gap_ratio_delta=-1.4\n\n### 19. eval_v8b_ss\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, checkpoint=tg_v8b_ss_fixed_s42\n- **Metrics:**\n  - iid_gar_ours: 0.4983, iid_gar_dongre: 0.3855, iid_ppl: 2.78\n  - iid_ngar_ours: 13.5, iid_ngar_dongre: 22.68\n  - modelgen_gar_ours: 0.3177, modelgen_gar_dongre: 0.3533, modelgen_ppl: 1.38\n  - modelgen_ngar_ours: 4.47, modelgen_ngar_dongre: 5.92\n  - iid_turn1_gar_ours: 0.5398\n  - modelgen_turn1_gar_ours: 0.4333\n\n### 20. eval_v8b_ss_s123\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=123\n- **Metrics (iid):**\n  - gar_ours: 0.503, gar_dongre: 0.394\n  - ppl: 2.781, ntp_loss: 0.976\n  - n_conv: 50, n_turns: 3\n- **Metrics (modelgen):**\n  - gar_ours: 0.418, gar_dongre: 0.441\n  - ppl: 1.389, ntp_loss: 0.325\n  - n_conv: 5, n_turns: 10\n- gap_ratio: 1.2\n- base_iid_ppl: 4.338, base_modelgen_ppl: 1.351\n\n### 21. instruction_retention_test\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct + v7 TG LoRA, seed=42, 18 prompts, beta=[0,3], 5 turns each\n- **Metrics:**\n  - late_turn_rate_beta0: 0.759\n  - late_turn_rate_beta3: 0.87\n  - late_turn_delta: 0.111\n  - mcnemar_chi2: 3.125\n  - mcnemar_p: 0.0771\n  - gar_compliance_r: 0.2003\n  - gar_compliance_p: 0.007\n  - category_content_constraint: beta0=0.619, beta3=0.857, delta=0.238\n  - category_count_constraint: beta0=1, beta3=1, delta=0\n  - category_format_constraint: beta0=1, beta3=1, delta=0\n  - category_position_constraint: beta0=0.667, beta3=0.733, delta=0.067\n\n### 22. llama_ar_matched_eval\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct + TG LoRA, seed=42, N=50, T=4\n- **Metrics:**\n  - ar_base_ours: mid_gar=0.0082, ngar=0.1, ppl=1.267\n  - ar_tg_ours: mid_gar=0.0388, ngar=0.493, ppl=1.413\n  - ar_base_dongre: mid_gar=0.0051, ngar=0.12, ppl=1.267\n  - ar_tg_dongre: mid_gar=0.018, ngar=0.431, ppl=1.413\n  - tf_reference: tf_tg_ours_ngar=11.88, tf_base_ours_ngar=0.388, tf_tg_ours_raw=0.4836, tf_tg_dongre_raw=0.018\n  - Matched gap: gar_ours_raw_gap=\"12.5x (TF 0.484 / AR 0.039)\", gar_ours_ngar_gap=\"24.1x\", gar_dongre_raw_gap=\"1.002x (zero gap)\"\n  - tg_over_base_ar_ours: \"4.71x\", tg_over_base_ar_dongre: \"3.54x\"\n\n### 23. llama_eval_s42\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct, seed=42\n- **Metrics (tf_base):** gar_ours=0.0166, ngar_ours=0.3882, gar_dongre=0.0038, ngar_dongre=0.163, ppl=3.45, N=50, T=4\n- **Metrics (tf_tg):** gar_ours=0.4836, ngar_ours=11.8818, gar_dongre=0.018, ngar_dongre=0.7922, ppl=2.57, N=50, T=4\n- **Metrics (ar_base):** gar_ours=0.0086, ngar_ours=0.0798, gar_dongre=0.0118, ngar_dongre=0.1265, ppl=1.24, N=5, T=10\n- **Metrics (ar_tg):** gar_ours=0.0304, ngar_ours=0.2632, gar_dongre=0.0217, ngar_dongre=0.2459, ppl=1.32, N=5, T=10\n- gap_ratio_tg_ours: 15.9\n- gap_ratio_base_ours: 1.93\n- gap_ratio_tg_dongre: 0.83\n- vs_qwen_v7_gap_ratio: 32.1\n- baseline_mid_gar: 0.0122\n\n### 24. llama_lora_only_s42 (training)\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=8000, epochs=3\n- **Metrics:**\n  - final_avg_loss: 0.9288, final_avg_ntp: 0.9279, final_avg_gar: 0.0009\n  - gate_fixed: 1, gate_type: \"none\"\n  - wall_clock_s: 25317, wall_clock_h: 7.03\n  - epochs_completed: 3\n\n### 25. llama_phase1_gar_diag\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct, seed=42, 5 convs x 10 turns, gen mode\n- **Metrics:**\n  - per_turn_gar: turn_1=0.0263, turn_2=0.0183, turn_3=0.0087, turn_4=0.0055, turn_5=0.006, turn_6=0.0035, turn_7=0.0038, turn_8=0.0037, turn_9=0.005, turn_10=0.0026\n  - t1_t10_decay_pct: 90.1\n  - t1_mid38_drop_pct: 80.2\n\n### 26. llama_tg_s42 (training)\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=8000, epochs=3, lr=2e-4, batch_size=1, grad_accum=8\n- **Metrics:**\n  - epochs_completed: 3, total_steps: 3000\n  - wall_clock_seconds: 26212, wall_clock_hours: 7.28\n  - final_avg_loss: 0.9233, final_avg_ntp: 0.9224, final_avg_gar: 0.0009, final_avg_div: 0\n  - final_gate_mean: 0.9099, final_gate_std: 0.0701\n  - final_gate_min: 0.7188, final_gate_max: 0.9922\n  - **Gate profile (32 layers):** L0=0.957, L1=0.973, L2=0.977, L3=0.965, L4=0.992, L5=0.969, L6=0.957, L7=0.957, L8=0.961, L9=0.949, L10=0.938, L11=0.934, L12=0.969, L13=0.953, L14=0.957, L15=0.965, L16=0.953, L17=0.961, L18=0.922, L19=0.902, L20=0.883, L21=0.863, L22=0.836, L23=0.844, L24=0.809, L25=0.719, L26=0.762, L27=0.805, L28=0.801, L29=0.855, L30=0.898, L31=0.934\n  - checkpoint_size_gate_mb: 4.2, checkpoint_size_lora_mb: 26\n  - GPU: NVIDIA RTX PRO 6000 Blackwell, vram_gb: 102, mem_used_gb: 63.4\n\n### 27. llama_tg_training\n- **Status:** PREPARING | **Conclusion:** failed\n- **Metrics:** NONE (phantom duplicate of llama_tg_s42)\n\n### 28. mmlu_eval_all\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, MMLU 5-shot, 14042 examples\n- **Metrics (MMLU scores):**\n  - base_qwen: 0.7423\n  - pcgrad_v9_s42: 0.7386\n  - ss_v8b_s42: 0.7375\n  - lo_s42: 0.7357\n  - tg_v7_s42: 0.7347\n  - ug_s42: 0.7346\n\n### 29. p0_ss_steering_eval\n- **Status:** PREPARING | **Conclusion:** killed\n- **Metrics:** NONE (cancelled, existing data sufficient)\n\n### 30. p1_llama_ss_eval\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct, seed=42, N=50, checkpoint=p1_llama_ss_s42/epoch_1\n- **Metrics:**\n  - ss_tf_gar: 0.477\n  - ss_tf_ppl: 2.82\n  - ss_ar_b0_gar: 0.1662\n  - ss_ar_b0_ppl: 1.37\n  - ss_ar_b5_gar: 0.7905\n  - ss_ar_b5_ppl: 1.81\n  - base_ar_gar: 0.0179\n  - base_ar_ppl: 1.22\n  - tf_ar_gap: 2.87\n\n### 31. p1_llama_ss_training\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=400, lr=2e-4, batch_size=1, grad_accum=8, epochs=3, ss_max_ratio=0.3, lora_rank=16\n- **Metrics:** NONE (training only)\n\n### 32. p1_ss_lora_only\n- **Status:** DONE | **Conclusion:** killed\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=2000, ss_max_ratio=0.3, gate_type=none\n- **Metrics:** NONE\n\n### 33. p1_tf_ar_kl_divergence\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, 30 convs\n- **Metrics:**\n  - tg_delta_gar: 0.0165\n  - base_delta_gar: 0.0122\n  - tg_mean_kl: 0.054\n  - base_mean_kl: 0.043\n  - gate_kl_correlation: 0.11\n  - high_kl_layers: \"L23-L27, L9\"\n  - gar_robustness_ours_tg_base_ratio: 21.4\n  - gar_robustness_goal_only_ratio: 63\n  - gar_robustness_ours_all_ratio: 1.7\n  - gar_robustness_ours_first_ratio: 1.8\n\n### 34. p2_llama_gradient_conflict\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Llama-3.1-8B-Instruct, seed=42, data=400\n- **Metrics:**\n  - cos_sim_mean: 0.0045\n  - cos_sim_std: 0.07\n  - neg_cos_sim_layers_pct: 53.1\n  - mag_ratio_median: 25.7\n\n### 35. phase1_gar_diag\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, 5 convs x 10 turns\n- **Metrics:**\n  - turn1_avg_gar: 0.0418\n  - mid_turns_avg_gar: 0.0122\n  - relative_drop: 0.708\n  - per_turn_avg_gar: [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]\n\n### 36. phase1a_multiseed_8runs\n- **Status:** PREPARING | **Conclusion:** None\n- **Metrics:** NONE\n\n### 37. phase1a_multiseed_qwen\n- **Status:** DONE | **Conclusion:** killed (30min timeout)\n- **Metrics:** NONE\n\n### 38. phase1b_llama_complement\n- **Status:** PREPARING | **Conclusion:** None\n- **Metrics:** NONE\n\n### 39. phase2_4way_eval\n- **Status:** DONE | **Conclusion:** negative\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, training split eval\n- **Metrics:**\n  - base_ours_mid_gar: 0.0107, base_ours_recovery_pp: -0.15\n  - base_dongre_mid_gar: 0.003, base_dongre_recovery_pp: -0.92\n  - base_ppl: 4.23, base_ntp: 1.4162\n  - tg_ours_mid_gar: 0.4866, tg_ours_recovery_pp: 47.44\n  - tg_dongre_mid_gar: 0.0157, tg_dongre_recovery_pp: 0.35\n  - tg_ppl: 2.63, tg_ntp: 0.9484\n  - ug_ours_mid_gar: 0.4923, ug_ours_recovery_pp: 48.01\n  - ug_dongre_mid_gar: 0.013, ug_dongre_recovery_pp: 0.08\n  - ug_ppl: 2.62, ug_ntp: 0.9433\n  - lora_ours_mid_gar: 0.486, lora_ours_recovery_pp: 47.39\n  - lora_dongre_mid_gar: 0.0137, lora_dongre_recovery_pp: 0.15\n  - lora_ppl: 2.63, lora_ntp: 0.9482\n  - route_b_confirmed: true, gating_incremental_benefit: \"none\"\n\n### 40. phase2_4way_eval_heldout\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, held-out eval (50 convs, idx 8843-68199)\n- **Metrics:**\n  - base_ours_mid_gar: 0.0128, base_ours_recovery_pp: 0.06\n  - base_dongre_mid_gar: 0.0031, base_dongre_recovery_pp: -0.91\n  - base_ppl: 4.34, base_ntp: 1.4045\n  - tg_ours_mid_gar: 0.5035, tg_ours_recovery_pp: 49.13\n  - tg_dongre_mid_gar: 0.0152, tg_dongre_recovery_pp: 0.3\n  - tg_ppl: 2.78, tg_ntp: 0.9771\n  - ug_ours_mid_gar: 0.5053, ug_ours_recovery_pp: 49.31\n  - ug_dongre_mid_gar: 0.0124, ug_dongre_recovery_pp: 0.02\n  - ug_ppl: 2.78, ug_ntp: 0.9752\n  - lora_ours_mid_gar: 0.4978, lora_ours_recovery_pp: 48.56\n  - lora_dongre_mid_gar: 0.0132, lora_dongre_recovery_pp: 0.1\n  - lora_ppl: 2.78, lora_ntp: 0.9771\n  - three_way_convergence_confirmed: true\n  - gar_ours_spread_pp: 0.75, ppl_spread: 0, data_overlap: false\n\n### 41. phase2_lora_only_s42\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=8000, epochs=3, gate_type=none\n- **Metrics:**\n  - epochs_completed: 3, global_steps: 3000\n  - training_time_seconds: 20588.6, training_time_hours: 5.7\n  - gate_fixed: 1, gate_type_actual: \"none\"\n  - final_lora_size_mb: 20\n  - eval_modelgen_ours_mid_gar: 0.0245\n  - eval_modelgen_dongre_mid_gar: 0.0185\n  - eval_modelgen_ppl: 1.371\n\n### 42. phase2_switching\n- **Status:** DONE | **Conclusion:** killed\n- **Metrics:** NONE\n\n### 43. phase2_tf_ar_switching\n- **Status:** QUEUED | **Conclusion:** None\n- **Metrics:** NONE\n\n### 44. phase2_tg_s42 (v1)\n- **Status:** DONE | **Conclusion:** negative\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, data=8000\n- **Metrics:**\n  - final_ntp_loss: 0.94\n  - final_gar_loss: 0\n  - gate_mean: 0.988\n  - gar_loss_zero_pct: 87.6\n  - epochs_completed: 1.67\n  - killed_reason: \"SIGTERM by diagnose worker (unauthorized)\"\n\n### 45. phase2_tg_s42_v2\n- **Status:** DONE | **Conclusion:** killed\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=cumulative, gar_epsilon=0.001, init_bias=2.0, lambda_gar=5.0\n- **Metrics:** NONE\n\n### 46. phase2_tg_s42_v3\n- **Status:** DONE | **Conclusion:** negative\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=maximize, lambda_gar=2.0, init_bias=2.0\n- **Metrics:**\n  - gate_mean_step0: 0.8743, gate_mean_step500: 0.8761\n  - gate_delta: 0.004, gate_std: 0.001\n  - final_ntp_loss: 0.94, final_gar_loss: -0.019\n  - gar_contribution_pct: \"2-4%\"\n  - diagnosis: \"gate frozen, GAR indirect gradient too weak\"\n\n### 47. phase2_tg_s42_v3b\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, lambda_gar=10.0, init_bias=0.0, gate_lr_multiplier=10, max_steps=500\n- **Metrics:**\n  - gate_std_final: 0.087\n  - gate_mean_final: 0.9388\n  - gate_min_final: 0.5352\n  - gate_max_final: 0.9922\n  - L4_gate: 0.535, L0_gate: 0.777\n  - L_NTP_final: 0.7787, L_GAR_final: -0.9606\n  - elapsed_seconds: 3565.9, optimizer_steps: 500\n  - gate_grad_received: true\n\n### 48. phase2_tg_s42_v4\n- **Status:** DONE | **Conclusion:** failed (server crash)\n- **Metrics:** NONE\n\n### 49. phase2_tg_s42_v5\n- **Status:** DONE | **Conclusion:** negative\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=maximize, lambda_gar=1.0, init_bias=1.5, gate_lr_multiplier=10, epochs=3\n- **Metrics:**\n  - step2000_gate_std: 0.0225, step2000_gate_mean: 0.9586\n  - step2000_gate_min: 0.9062, step2000_gate_max: 0.9961\n  - step2000_L_GAR: -0.8977, step2000_L_NTP: 0.7611, step2000_total_loss: -0.1365\n  - step2400_gate_std: 0.0219, step2400_gate_mean: 0.9651\n  - step2400_gate_min: 0.918, step2400_gate_max: 0.9961\n  - step2400_profile: \"L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996\"\n  - L_GAR_saturated_at: -0.91\n  - gate_range_compression: \"0.918-0.996\"\n\n### 50. phase2_tg_s42_v6\n- **Status:** DONE | **Conclusion:** negative\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=smooth_saturation, gar_target=0.5, lambda_gar=1.0, init_bias=1.5, gate_lr_multiplier=10, epochs=3\n- **Metrics:**\n  - dryrun_step0: L_NTP=2.0275, L_GAR=-0.0161, total_loss=2.0114\n  - dryrun_step4: L_NTP=1.6544, L_GAR=-0.0147, total_loss=1.6397\n  - dryrun_gate_mean_init: 0.8097, dryrun_gate_std_init: 0.0341\n  - dryrun_gate_min_init: 0.6836, dryrun_gate_max_init: 0.8672\n  - dryrun_gate_mean_step5: 0.8025, dryrun_gate_std_step5: 0.0842\n  - dryrun_gate_min_step5: 0.5547, dryrun_gate_max_step5: 0.9805\n  - gs50: gate_mean=0.8117, gate_std=0.0612, gate_min=0.6836, gate_max=0.9805\n  - gs100: gate_mean=0.8737, gate_std=0.0367, gate_min=0.8164, gate_max=0.9766\n  - gs100: L_NTP=0.8151, L_GAR=-0.158, total_loss=0.6571\n  - gs100_profile_bottom3: \"L12=0.816 L4=0.824 L13=0.824\"\n  - gs100_profile_top3: \"L27=0.977 L26=0.961 L23=0.914\"\n  - gs143_L_GAR: -0.3876, gs143_gate_mean: 0.9227\n\n### 51. phase2_tg_s42_v7 (canonical)\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, gar_loss_mode=mse_target, gar_target=0.5, lambda_gar=1.0, lambda_gate_div=1.0, min_gate_std=0.05, init_bias=1.5, gate_lr_multiplier=10, epochs=3, data=8000\n- **Metrics:**\n  - eval_iid_ours_mid_gar: 0.5035\n  - eval_iid_dongre_mid_gar: 0.0152\n  - eval_iid_ppl: 2.784\n  - eval_heldout_ours_mid_gar: 0.5035\n  - eval_heldout_dongre_mid_gar: 0.0152\n  - eval_heldout_ppl: 2.78\n  - eval_modelgen_ours_mid_gar: 0.0157\n  - eval_modelgen_dongre_mid_gar: 0.0194\n  - eval_modelgen_ppl: 1.36\n  - gate_mean_final: 0.9336\n  - gate_std_final: 0.0492\n\n### 52. phase2_tg_s42_v8_schedsampling\n- **Status:** DONE | **Conclusion:** failed\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.5, lr=2e-4, epochs=3\n- **Metrics:**\n  - killed_at_microstep: 1950, total_microsteps: 24000, completion_pct: 8.1\n  - global_step_approx: 244, total_global_steps: 3000\n  - ss_steps_observed: 1\n  - tf_lgar_mean_step850_1400: 0.0062, tf_lgar_std: 0.0082, tf_lgar_collapse_step: 800\n  - gate_mean_final: 0.93\n  - ss_ratio_at_kill: 0.081\n\n### 53. phase2_tg_s42_v8b_resume\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, ss_max_ratio=0.5, epochs=3\n- **Metrics (training):**\n  - total_steps: 3000, epochs_completed: 3, wall_clock_hours: 8.1\n  - final_loss: 0.933, final_ntp_loss: 0.9322, final_gar_loss: 0.0008\n  - final_gate_mean: 0.9586, final_gate_std: 0.0582, ss_ratio: 0.5\n- **Metrics (eval_iid):**\n  - gar_ours: 0.4983, gar_dongre: 0.3855, ppl: 2.78\n- **Metrics (eval_modelgen):**\n  - gar_ours: 0.3177, gar_dongre: 0.3533, ppl: 1.38\n- **vs_v7:**\n  - iid_gar_ours_delta: -0.005\n  - modelgen_gar_ours_delta: 0.302\n  - gap_ratio_v7: 32, gap_ratio_v8b: 1.57\n\n### 54. phase2_tg_s42_v8b_ss_fixed\n- **Status:** DONE | **Conclusion:** failed (CUDA OOM at epoch 1 step 4300)\n- **Metrics:** NONE (has epoch_0 checkpoint)\n\n### 55. phase2_tg_s42_v9_pcgrad\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, PCGrad, same hyperparams as v7\n- **Metrics:**\n  - eval_iid_ours_mid_gar: 0.5002\n  - eval_iid_dongre_mid_gar: 0.0123\n  - eval_iid_ppl: 2.78\n  - eval_iid_ntp: 0.9752\n  - eval_heldout_ours_mid_gar: 0.5002\n  - eval_heldout_dongre_mid_gar: 0.0123\n  - eval_heldout_ppl: 2.78\n  - eval_heldout_ntp: 0.9752\n  - eval_modelgen_ours_mid_gar: 0.0151\n  - eval_modelgen_dongre_mid_gar: 0.0173\n  - eval_modelgen_ppl: 1.5\n  - vs_v7_iid_ppl_diff: 0.004\n  - vs_v7_iid_gar_diff: -0.0033\n\n### 56. phase2_ug_s42\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, gate_type=uniform, data=8000, epochs=3\n- **Metrics:**\n  - epoch0: avg_loss=1.0019, avg_ntp=0.9755, avg_gar=0.0259, avg_div=0.0005\n  - epoch1: avg_loss=0.9447, avg_ntp=0.9435, avg_gar=0.0013, avg_div=0\n  - epoch2: avg_loss=0.9319, avg_ntp=0.9309, avg_gar=0.001, avg_div=0\n  - final_gate_mean: 0.9598, final_gate_std: 0.0518\n  - final_gate_min: 0.7773, final_gate_max: 1\n  - final_profile: L3=0.777, L5=0.812, L0=0.875, L27=1\n  - training_time_seconds: 21994.5, training_time_hours: 6.1, global_steps: 7950\n  - unexpected_per_layer_variation: true\n  - eval_modelgen_ours_mid_gar: 0.0149\n  - eval_modelgen_dongre_mid_gar: 0.0185\n  - eval_modelgen_ppl: 1.396\n\n### 57. qwen15b_phase1_diag\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-1.5B-Instruct, seed=42, data=400, epochs=3\n- **Metrics:** NONE (registered without metrics)\n\n### 58. trc_baseline_v7_tg\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=42, 5 convs x 10 turns\n- **Metrics (v7_tg):**\n  - tf_trc: 0.3339, gen_trc: 0.3323, trc_gap: 0.0016\n  - tf_tbp_ppl: 1.05, gen_tbp_ppl: 1.05\n- **Metrics (lora_only):**\n  - tf_trc: 0.349, gen_trc: 0.4106, trc_gap: -0.0617\n  - tf_tbp_ppl: 9.5, gen_tbp_ppl: 12\n- **Metrics (base):**\n  - tf_trc: 0.1494, gen_trc: 0.1494, trc_gap: 0\n  - tf_tbp_ppl: 2.05, gen_tbp_ppl: 2.05\n\n### 59. v7_tg_s123 (training)\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=8000\n- **Metrics:**\n  - epoch_1: avg_loss=0.9447, avg_ntp_loss=0.9434, avg_gar_loss=0.0013, avg_div_loss=0\n  - epoch_2: avg_loss=0.9315, avg_ntp_loss=0.9305, avg_gar_loss=0.001, avg_div_loss=0\n  - final_gate: mean=0.9467, std=0.051, min=0.793, max=1\n  - **Gate profile (28 layers):** L0=0.883, L1=0.793, L2=0.996, L3=0.988, L4=0.984, L5=0.797, L6=0.961, L7=0.918, L8=0.965, L9=0.934, L10=0.969, L11=0.918, L12=0.926, L13=0.941, L14=0.93, L15=0.965, L16=0.941, L17=0.91, L18=0.961, L19=0.965, L20=0.973, L21=0.988, L22=0.969, L23=0.98, L24=0.98, L25=0.984, L26=0.988, L27=1\n  - training_time_s: 21425.2\n\n### 60. v8b_ss_s123 (training)\n- **Status:** DONE | **Conclusion:** success\n- **Spec:** Qwen2.5-7B-Instruct, seed=123, data=8000\n- **Metrics:**\n  - final_loss: 0.9316, final_ntp_loss: 0.9307, final_gar_loss: 0.0009\n  - final_gate_mean: 0.9505, final_gate_std: 0.0508\n  - final_gate_min: 0.7383, final_gate_max: 1\n  - ss_used_ratio: 0.371\n  - training_time_s: 38773.4\n  - epoch0_loss: 1.0092, epoch1_loss: 0.9444, epoch2_loss: 0.9316\n\n---\n\n## SUMMARY STATISTICS\n\n- **Total experiments:** 60\n- **With metrics:** 42\n- **Without metrics:** 18 (7 failed/killed, 5 training-only with evals elsewhere, 4 PREPARING/QUEUED, 2 killed by user)\n- **Successful with metrics:** 35\n- **Key gap ratios:** v7 TG s42=32x, v7 TG s123=30.6x, v8b SS s42=1.57x, v8b SS s123=1.2x, d048 SS s42=1.29x, Llama TG=15.9x (raw)/12.5x (matched), Llama SS=2.87x, Llama LoRA-only=7.79x\n- **MMLU retention:** All within 0.77pp of base (0.7423), confirming no general capability degradation\n- **TRC values:** v7_tg tf=0.3339, gen=0.3323 (gap=0.0016); lora_only tf=0.349, gen=0.4106 (gap=-0.0617); base tf/gen=0.1494 (gap=0)"
      }
    ],
    "totalDurationMs": 296098,
    "totalTokens": 92083,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 77295,
      "output_tokens": 13889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 898
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13889,
          "cache_read_input_tokens": 77295,
          "cache_creation_input_tokens": 898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 898,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 0,
      "bashCount": 5,
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

_source line 163_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me systematically go through each section of the paper and audit every number against the registry and figure scripts. Let me organize this carefully.

Let me go through each section:

## Abstract

Numbers in abstract:
1. "five-way testbed" - 5 conditions: ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base → verified
2. "two architectures (Qwen-2.5-7B, Llama-3.1-8B)" - verified, these are the models used


3. "order of magnitude" - qualitative, but AR GAR drops from ~0.50 to ~0.019-0.064, which is roughly 8-27x → verified
4. "near parity on Qwen" - SS gap ~1.3x → verified
5. "substantially on Llama" - SS gap ~2.9x → verified

## Introduction

Numbers:
1. "12 models" - from Dongre et al. citation, not our data → cannot verify directly, but it's a citation
2. "over 70%" - "goal attention drops by over 70% within just five turns". Checking the per-turn GAR from phase1_gar_diag...

Checking the per-turn GAR values and comparing turn 1 against the mid-turns average gives me 70.8%, so the "over 70%" claim checks out.

3. "AUC = 0.98" - This appears to be about residual stream probes, but I'm not finding it directly in the registry. This might be from a separate analysis that wasn't registered, so I should flag this.
4. "85--90% across turns" - from fig1 panel (a), Qwen base shows 84.7% decay and Llama base shows 90.1% decay, which fits the 85-90% range. The registry confirms base Qwen at 87.5% and Llama at 90.1%. ✅
5. "GAR≈0.50" - The fine-tuned variants show GAR values around 0.50 across the board, with the registry showing 0.5035 and 0.5053 for the different conditions.
6. "8--17×" - Looking at the AR gap calculations: TG gives 7.8x, LoRA gives 13.5x, UG gives 14.8x, and PCGrad gives 16.7x. The range 7.8x to 16.7x rounds to 8--17×. ✅
7. "7.8× to 1.3× (Qwen)" - TG gap is 7.8x when comparing TF to AR, and the SS gap calculation is underway.

Continuing with the Qwen SS gap: the ratio works out to about 1.3x across multiple measurements and seeds. ✅
8. "~27× to 2.9× (Llama)" - For Llama, the TG gap is roughly 27x and the SS gap is approximately 2.9x.
9. "1.5B--8B" - The model sizes being compared are Qwen-2.5-1.5B, Qwen-2.5-7B, and Llama-3.1-8B. ✅
10. "p = 0.002" - PCGrad shows statistical significance with a p-value of 0.002 when comparing AR performance against TG. ✅
11. "~1.3× on Qwen" - This matches the Qwen gap calculation from earlier. ✅
12. "~2.9× on Llama" - This matches the Llama SS gap from earlier. ✅
13. "three seeds" - The SS validation used seeds 42, 123, and 456. ✅

For the method section, I'm noting that L and H are generic variable names representing layers and heads respectively, not concrete numbers.

Now checking the GAR-Dongre dilution claim. Looking at the registry data from phase2_4way_eval_heldout, the TG variant shows 0.0152 while other methods range from 0.0031 to 0.0132. For the AR evaluation, I need to verify the exact range, but Table 1 shows IID GAR-Dongre values spanning from near 0 for the base model up to around 0.02 for fine-tuned variants, so 0.01-0.02 appears correct. ✅

Checking the GAR-ours range next... I need to recalculate—the 3.3 percentage point difference is actually from the decay values, not the goal attention metrics. The ThreadGate decay of 77.7% versus LoRA-only's 81.0% gives that 3.3 pp gap. ✅ Base decay sits at 87.5%, Qwen has 28 layers, and sigmoid of 1.5 evaluates to approximately 0.82.

Now I'm verifying the gate architecture details: the hidden dimension projection down to 16, the 16-dimensional turn embedding, and how those combine to form a 32-dimensional input to the 64-unit hidden layer. For Qwen-2.5-7B's 28 layers, I'm calculating the total parameter count—roughly 57K parameters across the gating mechanism. I'm realizing the projection layer alone would account for most of the parameter budget, so maybe it's not projecting from the full 3584 dimensions. The math suggests the gate parameters should total around 2K per layer to hit that 57K figure across 28 layers, which means the projection must be operating on something much smaller than the hidden dimension. ~100K according to the cost table, but the text specifies +57K for just the gate parameters. The rounding in the table (4.2M vs 4.3M) explains the discrepancy—if LoRA is 4.194M and gates add 57K, that totals 4.251M, which rounds to 4.3M. Now I'm working backwards from the 57K figure across 28 layers to understand the gate architecture, which comes out to roughly 2036 parameters per layer. not the projection, assuming the projection is part of LoRA or something. Looking at the code more carefully, the projection might not actually be from the full hidden dimension—it could use average pooling or project from a smaller dimension instead. The cost table consistently shows +57K total, which would only make sense if the projection is shared across all 28 layers rather than applied per-layer, otherwise a 3584→16 linear projection would add up to 1.6M parameters across the network.

Let me check the Llama numbers to see if they're more consistent: with 32 layers and a hidden size of 4096, the gate MLP overhead alone would be around 70K, which is closer to the reported +65K, suggesting the per-layer costs might be slightly different than I'm calculating. I think I've been misunderstanding the projection—it's not a separate component but rather part of the gate computation itself. The proj function reduces the hidden state from 3584 dimensions down to 16, and those projection weights are included in the gate parameters, which would give roughly 57,360 parameters per layer just for that projection alone.

But if proj is shared across all 28 layers instead of per-layer, the math starts to work: a shared projection of 57,360 parameters, plus the per-layer gate MLPs totaling around 61,000 across all layers, plus embeddings, gets me closer to the 119K figure—though still not quite matching the 57K claim. I'm wondering if proj might be implemented as something simpler without learnable parameters, like a random projection or mean pooling operation.

The real check is whether 57K is actually less than 0.001% of 7B parameters: 57,000 / 7,000,000,000 = 0.0008%, which does satisfy the claim. But if the actual gate parameters are closer to 119K, that would be 0.0017%, which would violate the "<0.001%" statement in the paper. So there's a potential inconsistency here depending on how the projection is actually implemented.

I'll mark this as a flag—the 57K figure from the cost table is consistent with the claim, but the architecture description leaves room for doubt about whether that's the true parameter count.

Moving through the hyperparameter claims now. The learning rate multiplier, GAR target, minimum gate standard deviation, and loss weights all check out against the table. For the loss function iterations, I'm seeing seven distinct versions across what appears to be four conceptual families: cumulative approaches, maximize-based variants, smooth saturation, and MSE targeting. (family 4). So four loss families across seven iterations. But there's also v4 which was a server crash, and v8 which was scheduled sampling. The loss iterations table confirms: v1 cumulative, v2 cumulative+epsilon, v3 maximize(λ=2), v3b maximize(λ=10), v5 maximize(λ=1), v6 smooth saturation, v7 MSE+gate div. That's 7 iterations, 4 families: cumulative, maximize, smooth saturation, MSE. ✅

## Experiments

Now I'm verifying the experimental setup details. The model is Qwen-2.5-7B-Instruct with LoRA fine-tuning on 8K multi-turn conversations from UltraChat, trained for 3 epochs with a learning rate of 2×10^{-4}, batch size 1, and gradient accumulation of 8 for an effective batch of 8. The seed is 42, with ThreadGate using seed 123. Training took approximately 6 hours across most variants, though some configurations like smooth saturation and PCGrad ran longer.

For the hardware, I'm checking the GPU specifications against what's reported. The registry shows the RTX PRO 6000 Blackwell with 102 GB VRAM, but there's a discrepancy with the paper's claim of 96 GB—I need to reconcile whether this is the actual GPU capacity or if there's a difference in how the specs are being reported.

For the evaluation metrics, I'm verifying the GAR-ours range across different conditions. The table shows values clustering between 0.49 and 0.51 across IID and held-out evaluations, which matches the claimed 2 percentage point spread.

Now checking the perplexity claim—the table indicates 2.78 PPL for all fine-tuned models on the held-out evaluation set, though the IID training split shows slightly lower values around 2.62-2.63 for some methods. Looking at Table 2, the four-way results show TG at 2.63 and UG at 2.62 for the IID column, which matches the registry's training split eval—so the paper seems to be using "IID" inconsistently between tables, possibly redefining it as held-out conversations from the same distribution rather than the actual training split. on training data versus 2.78 on held-out conversations makes sense given the model would naturally perform better on data it's seen before. The text clarifies that IID uses same-distribution UltraChat text while held-out explicitly uses 50 non-overlapping conversations, but the identical values across both in Table 1 are puzzling—they might be using the same evaluation set despite different labels, or there's something about how the held-out set was constructed that I'm missing.

Digging into the registry data, I'm noticing a discrepancy: the training-split evaluation shows PPL of 2.63-2.63 across the fine-tuned variants, but Table 1 reports 2.78 for IID, which actually matches the held-out evaluation instead. Table 2 then shows 2.63, matching the training-split numbers. This suggests Tables 1 and 2 might be evaluating on different data splits entirely. The v7 experiment's own eval metrics show 2.784 for IID, which appears to be on held-out data, while the separate phase2_4way_eval run that produced 2.63 used training split data. So Table 1 draws from v7's internal evaluation results (all held-out), whereas Table 2 uses the earlier phase2_4way_eval results, explaining the discrepancy.

Now I'm checking the claim about GAR-ours differences between IID and held-out conditions. Looking at Table 1, TG and PCGrad both show 0pp difference, but UG shows a 2pp gap (IID=0.49, held-out=0.51), which contradicts the stated ≤1pp threshold.

Let me verify against the exact registry values to see if rounding is masking the true discrepancy. The held-out GAR-ours for UG is 0.5053, but I'm having trouble locating the precise IID value for UG in the v7 experiment—the registry entry I'm finding appears to be a different metric entirely (0.0149), so there's a mismatch I need to resolve. Oh, I see—the text is saying the difference between IID and held-out GAR-ours *within each method* should be ≤1pp. Looking at Table 1 row by row, most methods show 0pp difference, but UG shows a 2pp gap between IID (0.49) and held-out (0.51), which violates that claim. Looking at the exact values from the registry data, the UG IID entry must be below 0.495 to round down to 0.49, which means the difference from the held-out value of 0.5053 would be over 1pp—contradicting the claimed ≤1pp threshold. I'm trying to trace back which evaluation sets were actually used for each row in the table to understand where this discrepancy comes from. way_eval shows ug=0.4923. If Table 1 uses phase2_4way_eval for IID and phase2_4way_eval_heldout for held-out, then UG diff = 0.5053-0.4923 = 1.3pp. But that's the training split vs held-out comparison. If Table 1 uses a different "IID" set, the values could be different. Without knowing exactly which eval Table 1's IID column comes from, I can't fully verify. The fact that Table 1 shows IID PPL=2.78 for all fine-tuned models matching held-out suggests both columns might come from the same evaluation protocol but different conversation subsets, or a newer evaluation run. So I'm flagging the ≤1pp claim as potentially off by 0.3pp based on available registry data.

For the GAR-Dongre claim, I'm checking the registry values: phase2_tg_s42_v7 shows eval_modelgen_dongre_mid_gar=0.0194 and eval_heldout_dongre_mid_gar=0.0152, which gives AR dongre=0.0194 and TF dongre=0.0152. The ratio is essentially 1, confirming there's no meaningful distribution gap for this metric.

On the N=50 for AR generation, the registry shows n_convs=39 valid conversations out of 50 attempted, which is a discrepancy I need to reconcile with the paper's claim. conversations). Let me check: attention_steering_gen_n50: n_convs_total=50, n_convs_valid=39. So 50 were attempted but only 39 had enough turns (≥3 turns). The paper says N=50 but the actual effective sample size is 39. This should probably be noted. ⚠️

Hmm actually, looking more carefully at the table in the agent output, the 95% CIs are: TG [.041, .091]. These CIs would be based on the actual valid samples. The paper says "Under AR generation (N=50)" but the effective N is 39 for some metrics. The d048_final_ar_eval confirms n_convs=39. Let me check if the paper mentions this anywhere. Looking at the appendix table tab:steering-full, it shows N=50 for gen evaluations. But the actual valid convs for N=50 gen is 39. This is a discrepancy. ⚠️

For the five-way comparison, the AR eval might use a different eval than the steering eval. The d048_final_ar_eval covers "6 conditions, N=50 AR eval" with n_convs=39 valid. So the five-way AR eval used 39 valid conversations out of 50. If the paper reports N=50 without noting the 39 valid, that's a transparency issue but not necessarily a correctness issue since the metrics would be computed on the valid 39. Now I'm checking the AR GAR-ours range from d048_final_ar_eval: base=0.019, tg=0.064, ug=0.033, lo=0.037, pcgrad...

Continuing through the remaining claims: the gap multipliers check out (TG at 7.8x, LoRA at 13.5x, UG at 14.8x, PCGrad at 16.7x, giving the 8-17× range), the ranking of methods matches exactly, and the p-value of 0.004 for TG vs LoRA-only is confirmed in the stat tests.

Now I'm verifying the stability metrics—the second seed shows TF at 0.504 ± 0.001 across different seeds, which is consistent. For the MMLU claim about staying within 0.8 percentage points, I'm checking the actual deltas: the base is 74.23, and the lowest performer (UG) is at 73.46, giving a delta of 0.77pp, which rounds to 0.8pp as stated.

Moving on to the steering recovery range—beta values from 0 to 5 show GAR climbing from 0.064 to 0.727, matching the paper's claim. The perplexity cost at β=3 is about 8.9%, which rounds to the reported 9%. Now I'm looking at the phase transition claim. ±0.061, PPL 1.77. ✅
32. "β ∈ [3, 5] exceeds the TF baseline while PPL remains below 1.8" - TF baseline is around 0.50 GAR, and β=3 hits 0.556 which clears that. At β=5 the mean PPL is 1.77, safely under 1.8, though the standard deviation of 0.27 means some individual samples drift higher. ✅
33. The instruction retention improvement is 11.1 percentage points from the late-turn delta. ✅
34. Now checking the McNemar test p-value... The SS model operates independently from TG rather than modifying it, so the compression metric compares TG's 7.8× gap to SS's ~1.3× gap. For the AR metric across seeds, I'm getting 0.401 ± 0.047, and for TF the mean comes to 0.517, though there's a discrepancy with the stated 0.498 ± 0.004 that I need to reconcile. Looking at the registry entries more carefully, I'm seeing that d048_eval_ss_s42 has tg_gar_ours_mid=0.5025, but the naming convention "eval_ss" suggests it should be evaluating the SS model, not the TG model. I need to figure out whether these values are actually from the SS model evaluations or if there's some confusion in the labeling. I'm noticing a significant mismatch between the per-seed TF GAR values (which average to 0.517±0.032) and what the paper claims (0.498±0.004). Let me check if this 0.498 value appears elsewhere—it shows up in the llama-vs-qwen comparison for Qwen-7B, but that's still different from the per-seed mean. The individual seeds are 0.502, 0.554, and 0.496, so even the median doesn't match 0.498, which suggests there's a discrepancy I need to investigate further. I'm noticing the TF evaluation uses different numbers of conversations across seeds—50 for s42 versus 200 for s123—which could account for some of the variance I'm seeing. But the per-seed table shows fairly consistent TF GAR values (0.502, 0.554, 0.496), so maybe 0.498 is actually from a different model entirely, possibly the non-SS baseline used for comparison. I'm trying different averaging approaches to see if any yield 0.498—averaging just seeds 42 and 456 gets me to 0.499, which is close but not exact. The seed 123 value seems anomalously high at 0.554, so excluding it makes sense. I suspect there might be a different evaluation setup or an updated dataset not reflected in the current registry, so I'll mark this as an unresolved discrepancy and move on to check the per-seed table more carefully. The standard deviation for the TF GAR result doesn't match what I'd expect from three seeds either—if I exclude seed 123 and compute from just seeds 42 and 456, I get 0.499±0.004, which aligns with the paper's reported 0.498±0.004. This suggests they may have only used two seeds for that metric, despite claiming three. For the PPL cost, I'm checking the per-seed values and calculating what the standard deviation should be, but the paper's reported ±0.001 seems tighter than the actual variance across the three seeds.

Now looking at the β=5 results: the per-seed GAR values are all very close (0.717, 0.717, 0.716), giving a mean of 0.717 with std of 0.001, which matches the paper exactly. The text also confirms the comparison between β=0 (mean 0.401±0.047) and β=5 (mean 0.717±0.001), showing how the standard deviation drops dramatically when β increases.

For the mid-turn GA robustness check, all token-position variants exceed the 0.36 threshold: Last at 0.458, All at 0.366, First at 0.412, and Goal-only at 0.444.

The gap compression numbers check out—Llama's TG gap is about 27× (0.484 vs 0.018), while the SS gap is much tighter at 2.9× (0.477 vs 0.166).

For the epoch count, Qwen used 3 epochs for SS training while Llama used 2, though the actual best checkpoint for Llama came from epoch 1, so the effective training was shorter.

Now looking at the statistical analysis: the 27/28 layers figure comes from a Wilcoxon test showing gate inversion across nearly all layers with a p-value of 3.7e-8 and correlation of 0.975, which is highly significant. Wilcoxon test from gate analysis shows Turn 1 vs. Turn 21 with p=3.7e-8 and effect size r=0.975. Layer 23 shifts from 0.769 to 0.979, and inference-time gate values range from 0.93–0.98 (representing 2–7% attenuation). For the unified gate, L3 reaches 0.777 while L27 maxes out at 1.000. The NTP-GAR gradient opposition spans 68–79% across epochs, with cosine similarity moving from −0.089 to −0.042, indicating growing NTP magnitude dominance. %, Base=87.5%. The full range across all variants is 77.7-87.5%, which matches the paper's stated 77-87% range. ✅

For ThreadGate's TF/AR TRC values, I'm verifying the reported 0.334/0.332 with a gap of +0.002 against the experimental data showing tf_trc=0.3339 and gen_trc=0.3323, which rounds to the paper's figures.

⚠️ The actual gap is 0.0016, but rounding the individual values to 0.334 and 0.332 produces the displayed gap of 0.002—this is an acceptable rounding artifact.

Now checking the LoRA-only configuration where the paper reports 0.349/0.411 with a reversed gap of −0.062, comparing against the registry values of tf_trc=0.349 and gen_trc=0.4106.

Moving through the remaining claims: GAR-Dongre shows minimal shifts across both model families (1.002× for Llama, 1.28× for Qwen), the Llama AR evaluation used 20 conversations with 4 turns each, and I'm verifying the TF GAR-ours metric at 0.484 for TG and 0.481 for another condition. Now I'm verifying the median values across the three model variants and confirming the gap calculations—the TG and LoRA-only models show roughly 27× and 26× improvement over the autoregressive baseline when comparing task-focused performance to median latency.

I'm checking the gate profile values for both Qwen and Llama models, pulling the L1 and L25 layer metrics from the respective evaluation runs, then confirming the compression ratio from ~27× down to 2.9× for the Llama configuration.

Looking at the Llama sparse sampling results to verify the task-focused and autoregressive GAR scores, and now examining the epoch comparison data.

I'm trying to pin down where the β=3 recovery values come from—the Qwen sparse sampling shows 0.593 at β=3 from the final evaluation, but for Llama I'm seeing 0.173 in the table yet the registry entry doesn't directly list a β=3 result, only β=0 and β=5 values, so I need to trace where that intermediate value actually originates.

For the β=5 comparison, the registry shows 0.7905 for Llama sparse sampling while the paper reports 0.791—they're essentially the same value with just a rounding difference, though I should note which source each comes from.

Now checking the remaining claims: Qwen's sparse sampling at β=5 gives 0.717, the GAR decay for Qwen-2.5-1.5B is 79.8%, and the β-steering recovery reaches 0.715. All of these match their respective data sources.

Moving into the discussion section, I'm verifying the mechanism specificity claims—the GAR-Dongre shift shows at most a 1.28× change for Qwen. 0.727 from the generation metrics. Now I'm compiling the full audit report and need to double-check the figure captions more carefully.

Looking at Figure 1, the caption numbers all check out—the performance range across turns, the GAR target, the speedup factors for both model families. For Figure 4, I'm verifying the attention heatmap details: 5 conversations with 10 turns each, the decay percentages, and the perplexity difference. Figure 5's caption also validates—the range from 0.064 to 0.727, the perplexity cost at the higher beta value, and the optimal beta range all match what I found in the analysis.

Now checking Figure 3 on the gate shift: 27 out of 28 layers show the effect, the p-value is highly significant, and the pilot study had 5 samples. For the speedup range of 20–34×, I'm cross-referencing the pilot evaluations—the gap ratios vary depending on which phase and seed, ranging from about 15.9× up to 32.1× depending on the configuration, which aligns with that reported range.

For the final N=50 results, the gaps fall between 8–17×, which matches Table 1. The supplementary figure shows a gap reduction from 7.8× down to about 1.3×, and the multiseed analysis with β values of 0 and 5 across three seeds shows the standard deviation improving from 0.047 to 0.001.

Now I'm verifying the Figure 1 panel data against the registry to make sure the per-turn GAR decay values match what's recorded. Now I'm verifying the TF/AR gap metrics from Figure 1 panel (b) against the registry values—the baseline AR matches at 0.019, and all the other methods check out as well. Moving into panel (c) to examine the gap compression results for the SS approach.

I'm noticing a discrepancy with the Llama TG gap value. The figure uses 12.5x based on mean calculations, but the paper text references 27x using median-based analysis. I need to clarify which metric the paper actually emphasizes—it looks like the median approach is what's discussed in the analysis section, so there's an inconsistency between what the figure displays and what the text describes. The 12.5x figure comes from the matched eval data where AR=0.039 (the mean), giving 0.484/0.039 ≈ 12.5x. But there's a real inconsistency here: the text claims Llama TG gap is 27x using the median AR value of 0.018, while Figure 1(c) actually displays 12.5x based on the mean. The caption says "~27×" but the figure shows something different. I'm noticing a discrepancy between the figure and caption for panel (c)—the caption reports Llama's TF-AR gap as ~27×, but the actual bar in the figure shows 12.5×. This appears to stem from different calculation methods: the caption uses median-based gaps from the cross-model analysis while the figure displays mean-based gaps from the matched evaluation, which is confusing and needs to be flagged as inconsistent. gap = 11.3x. Or from llama_ar_matched_eval AR = 0.039, gap = 12.5x.
- Median-based: AR median = 0.018, TF = 0.484, gap = 27x.

The heavy-tailed distribution with CoV > 100% means outliers inflate the mean, so the median-based gap is larger. The paper explicitly uses medians for Llama reporting, making 27x the correct number, but the figures show 12.5x instead—this is a key inconsistency I need to flag.

Now I'm checking the cross-model figure script more carefully...

The cross-model panel correctly uses the median-based values for Llama (0.018, 27x), which aligns with the text. However, the main three-panel figure uses 12.5x for Llama, which is mean-based and inconsistent. Actually, looking closer at panel (c), that 12.5x represents the non-SS gap using the mean, while the SS gap shows 2.9x—so it's specifically about gap compression, not the absolute gap itself.

But this creates a real problem: the compression ratio from those bars would be 12.5x to 2.9x (a 4.3x reduction), whereas the text claims compression from ~27x to 2.9x (a 9.3x reduction using median values). The table confirms the paper uses median-based numbers throughout, so Figure 1(c) is presenting a different baseline gap than what the text describes. That's a clear inconsistency I need to flag.

Now I'm going through the paper systematically to compile all the numerical discrepancies I've found, starting with the abstract and working through each section. to be from the authors' own analysis, but I can't locate it in the registry—there's no probing experiment tracked among the 60 documented experiments. This could mean it was conducted outside the formal tracking system or during early exploration. I should flag this as unverifiable from the registry.

Now I'm checking the model scale claims. The limitations mention "1.5B--8B" as the range, so I need to verify if "0.5B" appears anywhere else in the paper and whether it's consistent with what's documented. The 1.5B validation is only in the appendix with limited scope—just base and ThreadGate, not the full five conditions—so claiming it's reproduced across 1.5B–8B is somewhat generous, though the numbers themselves check out. For the seven loss iterations, v3b is listed as a sub-version of v3 in the table, so I need to verify whether it's being counted as a separate iteration or grouped with v3. Checking the gate profiles from the figure generation scripts against the registry entries—Qwen's L1 value of 0.793 matches, and Llama's L25 value of 0.719 checks out. Now I'm verifying the multi-seed results by comparing the script values against the registry entries for different beta parameters.

I'm noticing a discrepancy between two evaluation runs: one with N=50 gives 0.347, while another with N=5 gives 0.3887 for the same metric. The figure uses the larger N=50 evaluation (0.347 for s42), and I'm cross-referencing the other seed values to ensure they're pulled from the same evaluation set.

Now I'm checking the s456 value more carefully—the raw data shows 0.4325, but the figure has 0.433, and I'm trying to figure out if this is a rounding difference or if there's an actual discrepancy in which evaluation was used. I'm noticing some rounding discrepancies in the seed values—s42 and s456 show minor differences (0.7157 rounds to 0.716, not 0.718; 0.7174 matches 0.717), though these are within acceptable tolerance. The per-seed table reports AR β=5 GAR values of 0.717, 0.717, and 0.716 for the three seeds with a mean of 0.717±0.001, but I need to verify whether the evaluation data directly supports these specific values.

Now I'm cross-referencing the final evaluation results and spotting a small discrepancy: the figure script shows 0.718 for s456 while the table and registry show 0.716—a minor inconsistency worth noting. I've gathered enough data to compile the full audit report and tally up the issues found, starting with the major one about TF GAR not matching the per-seed breakdown. or 0.499±0.004 if excluding seed 123)
2. Figure 1(c) uses Llama TG gap = 12.5x but caption says ~27x

Moderate issues (⚠️):
1. "held-out GAR-ours differs by ≤1 pp" - UG IID vs held-out differs by ~1.3pp
2. AUC = 0.98 - not verifiable from registry
3. N=50 stated but effective N=39 (conversations with ≥3 valid turns)
4. Llama SS β=3 = 0.173 - not directly in registry
5. PPL ±0.001 should be ±0.002

Minor issues:
1. Various rounding artifacts (TRC gap 0.0016 vs 0.002, etc.)
2. Figure script ss_mult
3. iseed β=5 values slightly off (0.716 vs 0.718 for s456)

Now I'm compiling the full report with all numbers organized by section and their verification status, then flagging the discrepancies separately. I'm also noticing the abstract claims a five-way testbed across two architectures, but the Llama replication only covered a subset of those conditions. The wording about the testbed is a bit ambiguous—the five-way comparison was only on Qwen while Llama had three conditions, so calling it a "five-way testbed spanning two architectures" could mislead readers into thinking all five conditions were tested on both. The core finding about exposure bias does replicate across both architectures though, which is what matters.

Now I need to systematically go through the figures and verify their numbers against the generation scripts and registry. Looking at Figure 2's training dynamics panels, I'm checking the convergence curves and loss annotations—like the NTP loss trajectory from around 2.03 down to 0.93—against what the underlying data should show.

For Figure 3, I'm examining the gate shift values across different layers and turns to see if the reported differences match what's in the registry.

Looking at the remaining layers: L12 shows a shift of -0.1265, L14 drops by -0.1803, and L23 has the largest shift at -0.2100. The paper's claim about layer 23 shifting from 0.769 to 0.979 checks out against the script values when accounting for rounding.

Now I'm looking at the distribution shift data from panel (b), comparing the in-distribution values against the mean-gap values across the five measurements.

I need to trace where the IID baseline of 0.0122 comes from—it appears to be from the phase1_gar_diag evaluation rather than phase2_4way_eval_heldout, which gives a slightly different value of 0.0128. These are distinct evaluation setups, so I need to figure out which one the figure actually uses.

Looking at the gap calculations in panel (b), the ratios between IID and model-gen values range from about 20× to 34×, but the figure title claims 20-33×. The discrepancy is minor—the maximum gap of 33.9× rounds up to 34, not 33 as stated. Verifying the remaining model configurations against the registry—LoRA's IID and AR values both check out, and I'm confirming the UG held-out evaluation metrics as well.

Now I'm noticing something odd with the base model: both IID and AR are showing the same value of 0.0122, which seems suspicious since they're pulling from phase1_gar_diag (a TF/gen evaluation on 5 conversations), but there's a discrepancy with the phase2 held-out evaluation showing 0.0128 instead. The script is using the phase1 value, though I should flag that the base metrics come from a different evaluation source with a smaller sample size than the others. I see the discrepancy now—the figure is actually using N=5 pilot data for the base model rather than the final N=50 evaluation, which explains why both TF and AR show 0.0122. The caption explicitly acknowledges this is a pilot study and notes that the smaller sample size inflates the gap estimates compared to the final N=50 results in Table 1, so this is intentional and properly documented. Now I'm ready to put together the full report.

I'll work through the issues systematically, focusing on the major discrepancies. There are six key problems: the TF GAR value for SS appears to use only 2 of 3 seeds instead of all three, the Llama TG bar in Figure 1(c) shows a mean-median mismatch between the plot and caption, the held-out GAR difference for UG exceeds the stated tolerance, the AUC value for residual stream probes lacks verification, the effective sample size for AR generation is 39 not 50, and the Llama SS β=3 coefficient isn't directly verifiable.

Beyond those, I'm noting several minor issues: a PPL standard deviation that should round to 0.002 rather than 0.001, a figure title range that should extend to 34× given the actual maximum gap, and a small discrepancy in one of the multiseed registry values.

Now I need to reconsider issue #1 since the TF GAR value appears in parenthetical context within the results statement, which might indicate it's being used differently than I initially thought. I found it—the 0.498 value comes from a different evaluation run (eval_v8b_ss) that uses the v8b checkpoint, which explains the discrepancy with the per-seed table showing 0.517±0.032. I'm noticing the discrepancy between the two scheduled sampling variants—the d048_ss experiments used ss_max_ratio=0.3 while the v8b run used 0.5, which explains why the results differ. Looking at the actual numbers, if the TF GAR is 0.498 versus the 3-seed mean of 0.517, that shifts the gap calculation between TF and AR performance, and the per-seed ratios show considerable variance across runs, ranging from 1.15x to 1.45x. gap = 1.30x ≈ 1.3x

But 0.498/0.401 = 1.24x which the paper also rounds to ~1.3x. Either way the gap is ~1.3x.

But the TF GAR value of 0.498 with std 0.004 doesn't match the per-seed data. This is factually incorrect. The per-seed table in the same paper shows different numbers.

This is a real error: the paper text reports TF GAR 0.498±0.004 for SS, but the per-seed table in the appendix (tab:perseed-ss) shows TF GAR: s42=0.502, s123=0.554, s456=0.496 with mean 0.517±0.032. The value 0.498 might come from a different SS variant like v8b with ss_ratio=0.5 rather than the d048 with ss_ratio=0.3.

Now I'm seeing that 0.498 appears consistently across the main text and several appendix tables for Qwen's TF GAR, but this directly contradicts the per-seed table which averages to 0.517. The discrepancy suggests either the 0.498 is correct for a specific evaluation configuration while the per-seed table uses different parameters, or there's an inconsistency in how these values were computed. the AR evaluation shows different results depending on the setup. Looking at the seed-specific evaluations, the TF GAR scores vary quite a bit—seed 42 used 50 conversations, seed 123 used 200, and seed 456 didn't specify—which might explain why the reported 0.498 doesn't match any single seed's result perfectly.

But there's a real inconsistency here: the paper text claims "TF GAR 0.498±0.004" while the per-seed table shows 0.517±0.032, which are fundamentally different numbers. This is a clear discrepancy that needs to be addressed, regardless of whether the per-seed table is from the appendix or main text.

Let me also double-check the Llama SS β=3 claim to see if that data actually exists in the evaluation registry.

Looking at the β=5 case, the registry shows 0.7905 which rounds to 0.791 when expressed to three decimal places, so that checks out.

Now I need to systematically go through each section and count how many numerical claims need verification for the full audit report. I've settled on including model identifiers as trivially correct entries since they're external names, so now I'm organizing the audit report with summary statistics, a per-section breakdown table, and a dedicated issues list before generating the final output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "57f91041-d950-431a-9f00-0ab20712a2be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLiEgsi6GUQLzDn8Bp4C8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8821,
      "cache_creation_input_tokens": 14766,
      "cache_read_input_tokens": 54454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14766
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

_source line 164_

All source data collected. Now cross-referencing every number against the registry, figure scripts, and tables. Writing the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "70a8d590-63fe-4602-a0b6-3a7822ec11d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLiEgsi6GUQLzDn8Bp4C8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8821,
      "cache_creation_input_tokens": 14766,
      "cache_read_input_tokens": 54454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14766
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

_source line 165_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LoLtwDN7sSQ5h7f6QJVX3H`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "4736a49a-4244-4774-a85b-49f80fdecbd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLiEgsi6GUQLzDn8Bp4C8c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 8821,
      "cache_creation_input_tokens": 14766,
      "cache_read_input_tokens": 54454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14766
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

_source line 166 · 2026-05-25T20:27:40.457Z_

<details><summary>↩ Tool result · `toolu_01LoLtwDN7sSQ5h7f6QJVX3H`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "41b9a2be-7b4c-4693-a686-90f0913d0530",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 30
  }
}
```

</details>

---


### Tool call

_source line 167_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Mkuhx9Nq6ZzBHQQWaePrsE`</summary>

```json
{
  "todos": [
    {
      "content": "Audit Abstract numbers",
      "status": "completed",
      "activeForm": "Auditing Abstract numbers"
    },
    {
      "content": "Audit Introduction numbers",
      "status": "completed",
      "activeForm": "Auditing Introduction numbers"
    },
    {
      "content": "Audit Method numbers",
      "status": "completed",
      "activeForm": "Auditing Method numbers"
    },
    {
      "content": "Audit Experiments numbers",
      "status": "completed",
      "activeForm": "Auditing Experiments numbers"
    },
    {
      "content": "Audit Analysis numbers",
      "status": "completed",
      "activeForm": "Auditing Analysis numbers"
    },
    {
      "content": "Audit Discussion numbers",
      "status": "completed",
      "activeForm": "Auditing Discussion numbers"
    },
    {
      "content": "Audit Conclusion numbers",
      "status": "completed",
      "activeForm": "Auditing Conclusion numbers"
    },
    {
      "content": "Audit Limitations numbers",
      "status": "completed",
      "activeForm": "Auditing Limitations numbers"
    },
    {
      "content": "Write audit report to artifacts/audit_body_text.md",
      "status": "in_progress",
      "activeForm": "Writing audit report"
    }
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
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "23f856f1-86f0-4bf8-a1d7-d934147831a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167SakkBxsgxtbqcWpzcVm4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 39532,
      "cache_read_input_tokens": 69220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 39532
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 168 · 2026-05-25T20:27:46.970Z_

<details><summary>↩ Tool result · `toolu_01Mkuhx9Nq6ZzBHQQWaePrsE`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "2cb43e4e-a0a8-4bca-83af-0348f47f3bee",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Audit Abstract numbers",
        "status": "completed",
        "activeForm": "Auditing Abstract numbers"
      },
      {
        "content": "Audit Introduction numbers",
        "status": "completed",
        "activeForm": "Auditing Introduction numbers"
      },
      {
        "content": "Audit Method numbers",
        "status": "completed",
        "activeForm": "Auditing Method numbers"
      },
      {
        "content": "Audit Experiments numbers",
        "status": "completed",
        "activeForm": "Auditing Experiments numbers"
      },
      {
        "content": "Audit Analysis numbers",
        "status": "completed",
        "activeForm": "Auditing Analysis numbers"
      },
      {
        "content": "Audit Discussion numbers",
        "status": "completed",
        "activeForm": "Auditing Discussion numbers"
      },
      {
        "content": "Audit Conclusion numbers",
        "status": "completed",
        "activeForm": "Auditing Conclusion numbers"
      },
      {
        "content": "Audit Limitations numbers",
        "status": "completed",
        "activeForm": "Auditing Limitations numbers"
      },
      {
        "content": "Write audit report to artifacts/audit_body_text.md",
        "status": "in_progress",
        "activeForm": "Writing audit report"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 169_

<details><summary>Logged reasoning block</summary>

```text
Now I need to write the comprehensive audit report. Let me compile everything I've found into a well-structured report.

Let me carefully go through all the numbers once more and write the full report.

I need to be very thorough and list every number. Let me organize by section.

Let me also verify one more thing I noticed: the fig1 caption says "85--90%" but let me double-check:
- Qwen base: turn1=0.0418, turn10=0.0064. Decay = (0.0418-0.0064)/0.0418 = 84.7%. But registry analysis_attention_heatmap says base_decay=0.875 (87.5%). 

The 87.5% is from mean GAR across turns, not from turn1→turn10 point-to-point. And the llama_phase1_gar_diag says t1_t10_decay_pct=90.1%. So "85-90%" covers 87.5% (Qwen) and 90.1% (Llama). ✅

Let me also verify one number from the experiments section I might have missed. The text says "A second seed confirms TF stability (0.504±0.001)". From tab:perseed-tg: s42=0.504, s123=0.505, Mean=0.504±0.001. ✅

And "cos = +0.005" for Llama gradients. From p2_llama_gradient_conflict: cos_sim_mean=0.0045. Paper says +0.005. 0.0045 rounds to 0.005. ✅

"25.7×" NTP magnitude dominance for Llama. From p2_llama_gradient_conflict: mag_ratio_median=25.7. ✅

Now I'm going to compile the full report with a table for each section listing every number, its source, and verification status. I'm estimating roughly 160 numbers across all sections from abstract through limitations, so I'll organize this systematically to catch any remaining discrepancies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d70d7bf3-a76c-4cf3-8f74-bbfe748e5a99",
  "uuid": "ff4a9531-f070-43b6-8ea6-4186e10a6894",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMZwDmjrZ88DiEShH6XGzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 108752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 355
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
