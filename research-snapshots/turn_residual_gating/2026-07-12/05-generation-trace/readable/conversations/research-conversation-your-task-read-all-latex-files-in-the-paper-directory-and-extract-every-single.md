# Research conversation: Your task: Read all LaTeX files in the paper directory and extract every single quantitative claim (numbers, percentages

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a868fff727d9f6065.jsonl`
- **Structured JSON:** [`aba7305983df3aed2d25.json`](../../sessions/ab/aba7305983df3aed2d25.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-21T19:45:23.035Z_

Your task: Read all LaTeX files in the paper directory and extract every single quantitative claim (numbers, percentages, ratios, p-values).

The paper files are at:
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex

Read ALL of these files completely. For each quantitative claim found, record:
1. The file name and line number
2. The exact text context (the sentence or phrase containing the number)
3. The number itself
4. What the number represents (GAR, PPL, gap ratio, p-value, percentage point improvement, β value, etc.)
5. Which experiment it likely refers to (if identifiable from context)

Be EXHAUSTIVE. Capture every number that represents an experimental result, including:
- GAR values (like 0.5035, 0.0157, 0.028, 0.6795)
- Gap ratios (like 30×, 12.5×, 1.57×)
- PPL values
- Steering β values
- Percentage point improvements (+23.8pp, etc.)
- p-values (p=0.007, etc.)
- Recovery ratios
- Cosine similarity values
- Any numbers in tables
- Model parameters (125M, 350M, etc. - note these but they're less critical)
- Turn counts, token counts

Output a structured list organized by file, with all the above fields for each claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "8a6e05e4-c0fa-479e-a447-ee0cf130ec3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T19:45:23.038Z_

```json
{
  "parentUuid": "8a6e05e4-c0fa-479e-a447-ee0cf130ec3a",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "4f50d73a-d3b1-4cdf-8b8d-9429aab32006",
  "timestamp": "2026-05-21T19:45:23.038Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T19:45:25.782Z_



I'll read all the LaTeX files systematically to extract every quantitative claim. Let me start by reading all files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f50d73a-d3b1-4cdf-8b8d-9429aab32006",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2790f4b6-40cb-434b-90fe-d201ce9f7a3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T19:45:26.292Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XxT5LM23udonq5kXT9g1uv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2790f4b6-40cb-434b-90fe-d201ce9f7a3a",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9d53d85-fe82-4ad4-a799-e686e02a887c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T19:45:26.313Z_

<details><summary>↩ Tool result · `toolu_01XxT5LM23udonq5kXT9g1uv`</summary>

```text
1	\begin{abstract}
2	Multi-turn dialogue with Large Language Models (LLMs) suffers from progressive attention decay toward system prompt goal tokens. On Qwen-2.5-7B-Instruct, the Goal Attention Ratio (GAR) declines by 70.8\% between early and mid-conversation turns, yet linear probes recover goal content from the residual stream with AUC\,=\,0.98. We introduce ThreadGate, a per-layer content-and-turn-conditioned MLP gate ($x_{l+1} = x_l + g_l \cdot f_l(x_l)$) trained jointly with next-token prediction (NTP) and an auxiliary GAR loss. A five-way comparison reveals that training succeeds (teacher-forced GAR\,=\,0.50) but autoregressive GAR drops to 0.015--0.025, a 20--33$\times$ gap; gating contributes zero measurable benefit and PCGrad-based causal exclusion rules out gradient conflict. The failure traces to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. Inference-time steering ($\beta$\,=\,5) recovers GAR from 0.029 to 0.697, providing constructive evidence that attention misallocation---not representation degradation---is the proximal cause. Scheduled sampling compresses the gap to 1.57$\times$ with no PPL cost (single seed), and cross-model evaluation on Llama-3.1-8B confirms the gap (12.5$\times$). These findings characterize how exposure bias selectively destroys auxiliary objective generalization under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses).
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9d53d85-fe82-4ad4-a799-e686e02a887c",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "ac1d1817-bde6-46f3-bb48-8e050023a216",
  "sourceToolAssistantUUID": "f9d53d85-fe82-4ad4-a799-e686e02a887c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T19:45:26.782Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VWuwU16BMkpHBzzGGeEbQz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac1d1817-bde6-46f3-bb48-8e050023a216",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9eeb3c94-12af-41e6-a47f-b86e9b8e846d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T19:45:26.791Z_

<details><summary>↩ Tool result · `toolu_01VWuwU16BMkpHBzzGGeEbQz`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual update with a content-and-turn-conditioned MLP gate: $x_{l+1} = x_l + g_l \cdot f_l(x_l)$, where $g_l$ is produced by a two-layer network conditioned on the hidden state and turn features, inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}.
6	
7	\begin{figure*}[t]
8	  \centering
9	  \includegraphics[width=\textwidth]{fig1_overview.pdf}
10	  \caption{Overview of ThreadGate and its failure mode. (Left) ThreadGate adds per-layer content-and-turn-conditioned MLP gates to the residual stream, trained jointly with an auxiliary GAR loss that targets goal attention. (Right) Under teacher-forced evaluation, GAR-ours reaches 0.50 across all fine-tuned variants; under autoregressive generation, it drops to 0.015--0.025, a 20--33$\times$ gap. The five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) shows that no intervention provides measurable benefit over LoRA-only fine-tuning.}
11	  \label{fig:overview}
12	\end{figure*}
13	
14	ThreadGate combines per-layer MLP gate networks with a joint training objective: next-token prediction (NTP), an auxiliary GAR loss ($\tau = 0.5$), and a gate diversity loss (\S\ref{sec:method}). The final formulation emerged from seven iterations spanning four loss families; only MSE target with gate diversity converged stably. To diagnose the failure, we construct a five-way factorial comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) where each pair isolates one causal factor (\S\ref{sec:experiments}). PCGrad \citep{yu2020pcgrad} serves a dual role: training strategy and causal exclusion tool that rules out gradient direction conflict.
15	
16	Training succeeds: teacher-forced GAR-ours reaches 0.50 across all fine-tuned variants. The factorial comparison reveals that the failure is specific to autoregressive generation, where GAR-ours drops to 0.015--0.025, a 20--33$\times$ gap that persists across all training strategies. All four fine-tuned variants achieve indistinguishable performance (0.75\,pp spread on GAR-ours, identical PPL at 2.78); the gating contrast confirms that gates contribute zero measurable benefit. The PCGrad causal exclusion eliminates gradient direction conflict without altering any outcome, establishing that conflict is neither necessary nor sufficient for the failure. These four contrasts converge on a single root cause: exposure bias \citep{bengio2015scheduled}, where attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text (Figure~\ref{fig:overview}). An inference-time steering experiment provides constructive evidence that attention misallocation is the proximal cause: additive attention bias recovers autoregressive GAR from 0.029 to 0.697, bypassing the exposure bias barrier (\S\ref{subsec:steering}). A preliminary scheduled sampling experiment confirms that the gap is also mitigable at training time: GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the 30$\times$ gap to 1.57$\times$ with no PPL cost (single seed; \S\ref{sec:discussion}).
17	
18	Our contributions: (1)~a systematic causal diagnostic framework for analyzing auxiliary objective failures in multi-turn dialogue, comprising a five-way factorial comparison that isolates four causal factors (turn conditioning, gating mechanism, gradient conflict, and fine-tuning), PCGrad-based causal exclusion via gradient surgery \citep{yu2020pcgrad}, and per-layer gradient conflict quantification; this design pattern is in principle applicable to other auxiliary objective analyses (\S\ref{sec:method}, \S\ref{sec:experiments}, \S\ref{sec:analysis}); (2)~using this framework, the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization (20--33$\times$ gap) while leaving NTP robust, with evidence that token-level self-recovery \citep{he2019exposure} does not extend to auxiliary objectives, a preliminary demonstration that scheduled sampling compresses this gap from 30$\times$ to 1.57$\times$ (single seed), and cross-model confirmation on Llama-3.1-8B (12.5$\times$ gap); (3)~an inference-time steering experiment: additive attention bias at $\beta$\,=\,5 recovers autoregressive GAR from 0.029 to 0.697, providing constructive evidence that attention misallocation---not representation degradation---is the proximal cause under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses; \S\ref{subsec:steering}); (4)~a principled negative baseline for future attention steering research: ThreadGate with seven loss formulations and four training configurations ruled out (\S\ref{sec:method}, \S\ref{sec:experiments}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9eeb3c94-12af-41e6-a47f-b86e9b8e846d",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "1d4a8684-6835-43eb-b492-2c27b3daa819",
  "sourceToolAssistantUUID": "9eeb3c94-12af-41e6-a47f-b86e9b8e846d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T19:45:27.665Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J3Xi6tk4phpst1i3UDB2Bj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d4a8684-6835-43eb-b492-2c27b3daa819",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e18f26f-8478-4742-b707-322a11f2e935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T19:45:27.671Z_

<details><summary>↩ Tool result · `toolu_01J3Xi6tk4phpst1i3UDB2Bj`</summary>

```text
1	\section{Background}\label{sec:background}
2	
3	\paragraph{Goal Attention Ratio.}
4	Multi-turn instruction-following models receive a system prompt that specifies the task objective. We denote the token subsequence corresponding to the task specification within this system prompt as the \emph{goal tokens} $\mathcal{G}$, excluding formatting markers and role tags. \citet{dongre2026attention} introduced the Goal Attention Ratio (GAR) to quantify how much attention a model allocates to these goal tokens during response generation. Given a model with $L$ layers and $H$ attention heads, GAR at conversation turn $\tau$ is
5	\begin{equation}\label{eq:gar}
6	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
7	\end{equation}
8	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$. This definition averages attention to goal tokens over all response positions, all layers, and all heads.
9	
10	\paragraph{Two GAR variants.}
11	We distinguish two measurement variants throughout this paper. \textbf{GAR-Dongre} refers to the original definition in Equation~\ref{eq:gar}, which averages over the full response token set $\mathcal{R}_\tau$. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
12	\begin{equation}\label{eq:gar-ours}
13	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
14	\end{equation}
15	where $t_\tau$ is the index of the last token in the assistant response at turn $\tau$. The last token is the position at which the model conditions its next generation step, so attention patterns at this position most directly reflect the information the model draws upon for continuation. We use GAR-ours as the optimization target for the auxiliary loss $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}), while GAR-Dongre provides a complementary aggregate measure for comparison.
16	
17	\paragraph{Residual stream persistence.}
18	\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream (probe AUC\,=\,0.98) even at late turns where GAR has collapsed. The information is present but the attention mechanism fails to route it. This dissociation motivates an intervention that targets the residual pathway directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e18f26f-8478-4742-b707-322a11f2e935",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "7b75e2c3-445f-4de3-98db-30c2fa079c59",
  "sourceToolAssistantUUID": "6e18f26f-8478-4742-b707-322a11f2e935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T19:45:27.732Z_

<details open><summary>🔧 Tool call — Read · `toolu_016YfcT1jqrzQpxcZoGqLjm4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b75e2c3-445f-4de3-98db-30c2fa079c59",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "227d3c95-590e-4950-8221-688a6a3f8e9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T19:45:27.740Z_

<details><summary>↩ Tool result · `toolu_016YfcT1jqrzQpxcZoGqLjm4`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Attention Ratio.}
6	We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	Inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is
22	\begin{equation}
23	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
24	\end{equation}
25	where $f_l$ denotes the sublayer computation (self-attention or FFN). The gate $g_l$ is produced by a two-layer MLP:
26	\begin{equation}\label{eq:gate}
27	  g_l = \sigma\!\bigl(W_2\,\text{ReLU}(W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] + b_1) + b_2\bigr),
28	\end{equation}
29	where $\text{proj}(\cdot)$ projects from the hidden dimension to 16 units and $\text{emb}(t_d, t_i)$ is a 16-dimensional turn embedding encoding turn distance $t_d$ (turns since system prompt) and turn index $t_i$ (absolute position) via learned lookup tables. The concatenated 32-dimensional input passes through a 64-unit hidden layer to produce a scalar gate. Each of the 28 layers in Qwen-2.5-7B-Instruct receives its own gate network. Gates are initialized near 0.82 to preserve pretrained computation, with a 10$\times$ learning rate multiplier.
30	
31	\subsection{Training Objective}\label{sec:loss}
32	
33	The training objective combines three terms:
34	\begin{equation}
35	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
36	\end{equation}
37	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. The GAR loss targets a fixed attention level to goal tokens:
38	\begin{equation}
39	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR}, \tau),
40	\end{equation}
41	where $\tau = 0.5$. GAR is measured at the last token of each assistant turn (GAR-ours, \S\ref{sec:background}). The gate diversity loss prevents collapse to a uniform value:
42	\begin{equation}
43	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
44	\end{equation}
45	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min}$ is a minimum standard deviation threshold. Both $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$. We additionally tested three alternative loss families (cumulative, maximize, smooth saturation) across six configurations; only the MSE variant converged during training (Appendix~\ref{sec:appendix-loss}).
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "227d3c95-590e-4950-8221-688a6a3f8e9a",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "43326e88-877c-4057-905e-7f3993c86b15",
  "sourceToolAssistantUUID": "227d3c95-590e-4950-8221-688a6a3f8e9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T19:45:28.401Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ShsfsxqKqadub3WcyT3mhc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43326e88-877c-4057-905e-7f3993c86b15",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8700e28-ed59-4986-bc8b-f001ae8326d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T19:45:28.412Z_

<details><summary>↩ Tool result · `toolu_01ShsfsxqKqadub3WcyT3mhc`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split, a dataset of naturalistic dialogues across diverse topics. LoRA adapters (rank 16, $\alpha$=32) are applied to query and value projection layers (\texttt{q\_proj}, \texttt{v\_proj}). The combined loss $\mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\mathcal{L}_\text{GAR} + \lambda_\text{div}\mathcal{L}_\text{div}$ uses $\lambda_\text{GAR} = \lambda_\text{div} = 1.0$ with MSE target $\tau = 0.5$ (\S\ref{sec:loss}). We train for 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are provided in Appendix~\ref{sec:appendix-hyper}.
7	
8	We evaluate five configurations that form a factorial design isolating four causal factors. \textbf{ThreadGate}: full system with 28 gate networks (Eq.~\ref{eq:gate}) and three-term loss. \textbf{+PCGrad}: ThreadGate with PCGrad \citep{yu2020pcgrad} projecting conflicting gradients (isolates gradient conflict). \textbf{Uniform Gate}: gates without turn embedding (isolates turn conditioning). \textbf{LoRA-only}: gates fixed at 1.0, trained with $\mathcal{L}_\text{NTP} + \mathcal{L}_\text{GAR}$ only (isolates gating mechanism). \textbf{Base}: pretrained model (isolates fine-tuning). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours (last-token attention to goals, \S\ref{sec:background}), GAR-Dongre \citep{dongre2026attention} (all-token average), and PPL.
9	
10	\subsection{Main Results}
11	
12	Table~\ref{tab:four-way} presents the five-way comparison. The central finding is that, under the single seed tested, all four fine-tuned variants converge to nearly identical performance. GAR-ours spans only 0.75 percentage points (pp) across ThreadGate (0.50), +PCGrad (0.50), Uniform Gate (0.51), and LoRA-only (0.50), and PPL is 2.78 for all four on IID evaluation. Neither per-layer gating (ThreadGate), elimination of gradient direction conflict (+PCGrad), nor content-only gating (Uniform Gate) provides any measurable benefit over LoRA-only fine-tuning.
13	
14	The Base model confirms that LoRA fine-tuning is the operative variable: GAR-ours jumps from 0.01 to ${\sim}$0.50, while PPL improves from 4.23 to 2.78. Since all four variants share the same GAR loss ($\tau = 0.5$), convergence near the target is expected and does not demonstrate gating benefit. GAR-Dongre remains uniformly low (0.01--0.02) across all standard-trained conditions, consistent with \citet{dongre2026attention}; a preliminary scheduled sampling experiment breaks this pattern (\S\ref{sec:discussion}).
15	
16	The teacher-forced GAR-ours of 0.50--0.51 stands in sharp contrast to autoregressive generation, where GAR-ours drops to 0.015--0.025 across all fine-tuned variants, a 20--33$\times$ gap. This gap is universal: it persists across all training strategies---gating, gradient conflict elimination, and LoRA-only fine-tuning alike. We analyze this distribution shift in \S\ref{sec:analysis}.
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All four fine-tuned variants converge to within 0.75\,pp on GAR-ours; PPL is indistinguishable. GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
22	\label{tab:four-way}
23	\begin{tabular}{l ccc ccc}
24	\toprule
25	& \multicolumn{3}{c}{\textbf{IID Evaluation}} & \multicolumn{3}{c}{\textbf{Held-out Evaluation}} \\
26	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
27	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL \\
28	\midrule
29	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 \\
30	ThreadGate        & 0.50 & 0.02 & 2.78 & 0.50 & 0.02 & 2.78 \\
31	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 \\
32	Uniform Gate      & 0.51 & 0.01 & 2.78 & 0.51 & 0.01 & 2.78 \\
33	LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 \\
34	\bottomrule
35	\end{tabular}
36	\end{table*}
37	
38	\begin{figure}[t]
39	  \centering
40	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
41	  \caption{Per-turn GAR-ours under teacher-forced evaluation ($N$\,=\,45, $\pm$1\,std). Fine-tuned variants maintain GAR near $\tau$\,=\,0.5 with 7--8\% decay (T1$\to$T4); Base decays 80\%. T5 std inflated by truncated conversations. Despite this preservation, autoregressive GAR collapses to 0.015--0.025 for all variants (Table~\ref{tab:four-way}), distribution shift is the failure mode.}
42	  \label{fig:attention-heatmap}
43	\end{figure}
44	
45	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
46	
47	The preceding sections established that all training-time interventions fail uniformly: exposure bias collapses autoregressive GAR regardless of gating or gradient management. We now test whether inference-time attention manipulation can recover GAR without retraining. We apply an additive bias $\beta$ to goal-token attention logits at every layer of the ThreadGate checkpoint during generation.
48	
49	Figure~\ref{fig:steering}(a) presents initial results on $N$\,=\,5 ten-turn conversations. Low bias values ($\beta \in [0, 2]$) yield negligible GAR change (0.029\,$\to$\,0.075) with stable PPL (${\sim}$1.4). A sharp nonlinearity appears between $\beta$\,=\,2 and $\beta$\,=\,5: GAR increases ${\sim}$9$\times$ (0.075\,$\to$\,0.697$\pm$0.020) while PPL rises only 35\% (1.41\,$\to$\,1.91). At $\beta$\,=\,10, GAR saturates at 0.959 but PPL degrades to 4.22.
50	
51	$N$\,=\,50 conversations from a held-out evaluation set (39 with $\geq$3 turns, mean 3.6 user turns; Figure~\ref{fig:steering}b) confirm the qualitative steering pattern observed in the $N$\,=\,5 pilot (10 turns each), with consistent nonlinearity range and saturation behavior. A finer $\beta$ sweep localizes the nonlinearity: GAR jumps from 0.128$\pm$0.110 ($\beta$\,=\,2) to 0.556$\pm$0.060 ($\beta$\,=\,3), an 8.7$\times$ recovery from baseline with only 9\% PPL increase (1.43\,$\to$\,1.56), identifying $\beta$\,=\,3 as a practical operating point. The $\beta$\,=\,0 distribution is right-skewed (mean 0.064, median 0.031, std 0.081), driven by short conversations with high baseline GAR; absolute baselines therefore differ from the 10-turn $N$\,=\,5 evaluation (0.029).
52	
53	These results provide constructive evidence that attention misallocation---not representation degradation---is the proximal cause of exposure-bias-induced GAR failure under the tested conditions (Qwen-2.5-7B, UltraChat, GAR-family losses): manually correcting attention via $\beta$ bias restores GAR, and inference-time intervention circumvents the exposure bias barrier.
54	
55	\begin{figure}[t]
56	  \centering
57	  \includegraphics[width=\columnwidth]{fig5_attention_steering.pdf}
58	  \caption{Inference-time attention steering: additive bias $\beta$ applied to goal-token attention logits during autoregressive generation (error bars show $\pm$1\,std). (a)~Initial evaluation ($N$\,=\,5, 10-turn conversations): sharp increase at $\beta \in [2, 5]$, GAR ${\sim}$9$\times$ recovery with 35\% PPL rise. (b)~Larger-scale evaluation ($N$\,=\,50, 39 with $\geq$3 turns, mean 3.6 user turns) with finer $\beta$ sweep: the nonlinearity localizes between $\beta$\,=\,2 and $\beta$\,=\,3, identifying $\beta$\,=\,3 as a practical operating point (8.7$\times$ GAR recovery, 9\% PPL cost). High-$\beta$ results are consistent across sample sizes. Dotted line: unsteered teacher-forced baseline.}
59	  \label{fig:steering}
60	\end{figure}
61	
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8700e28-ed59-4986-bc8b-f001ae8326d5",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "3178de9a-d2e6-4752-8f75-977703ee94c3",
  "sourceToolAssistantUUID": "d8700e28-ed59-4986-bc8b-f001ae8326d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T19:45:28.671Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HXoBTU23sn4r5KV4z3oMc4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3178de9a-d2e6-4752-8f75-977703ee94c3",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2d9eda6-036e-4ecd-8d13-baff2edc1cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T19:45:28.680Z_

<details><summary>↩ Tool result · `toolu_01HXoBTU23sn4r5KV4z3oMc4`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step causal chain: we first show that gates learn behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through a causal exclusion experiment (\S\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \S\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
10	
11	The resulting inference-time gate values range from 0.93 to 0.98 (2--7\% attenuation), far below what meaningful modulation would require; this explains the convergence with LoRA-only in Table~\ref{tab:four-way}. Figure~\ref{fig:gate-shift}(a) visualizes the per-layer gate difference. The inverted turn conditioning raises a natural question: does the NTP-GAR gradient conflict prevent gates from learning the intended behavior? If gradient conflict is the root cause, resolving it should rescue gate conditioning.
12	
13	\begin{figure}[t]
14	  \centering
15	  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
16	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift: the 20--33$\times$ GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base), the failure is universal across all configurations.}
17	  \label{fig:gate-shift}
18	\end{figure}
19	
20	\subsection{PCGrad Causal Exclusion}\label{subsec:pcgrad}
21	
22	The NTP and GAR gradients point in opposing directions across 68--79\% of layers throughout training, with mean cosine similarity ranging from $-$0.089 (epoch~0) to $-$0.042 (epoch~2). The NTP gradient magnitude dominates by 7.5--14.7$\times$. This raises a natural hypothesis: perhaps opposing gradient directions prevent the GAR objective from converging. If so, eliminating direction conflict should prevent the collapse. We test this using PCGrad \citep{yu2020pcgrad}, which projects the gradient of one task onto the normal plane of the other whenever two task gradients conflict. We apply PCGrad to gate parameters only, scoping our claim to direction conflict; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibrium violations \citep{navon2022nash} remain untested.
23	
24	Eliminating direction conflict via PCGrad shifts per-step cosine similarity from consistently negative ($-$0.089) to oscillating around zero ($-$0.15 to $+$0.09), yet all outcomes remain unchanged: IID GAR-ours (0.50 vs 0.50), PPL (2.780 vs 2.784), and autoregressive GAR (0.015 vs 0.016) are indistinguishable (Table~\ref{tab:four-way}). $\mathcal{L}_\text{GAR}$ follows a nearly identical training trajectory and collapses in the same manner (Figure~\ref{fig:training-pcgrad}b). The causal exclusion follows by \emph{modus tollens}: if direction conflict causes the failure, removing it should prevent it; PCGrad removes it; the failure persists; therefore direction conflict is not the cause. Direction conflict is neither necessary (removing it does not rescue GAR) nor sufficient ($\mathcal{L}_\text{GAR}$ converges during training despite persistent conflict). The 7.5--14.7$\times$ NTP magnitude dominance renders directional interference inconsequential. With gradient conflict ruled out, the question narrows: the training dynamics are not the problem (GAR converges under teacher forcing), so the failure must occur at the transition from training to inference.
25	
26	\begin{figure}[t]
27	  \centering
28	  \includegraphics[width=\columnwidth]{fig2_training_pcgrad.pdf}
29	  \caption{(a)~Gradient cosine similarity between NTP and GAR objectives. ThreadGate remains consistently negative; +PCGrad oscillates around zero. (b)~IID evaluation outcomes are indistinguishable: eliminating direction conflict changes nothing.}
30	  \label{fig:training-pcgrad}
31	\end{figure}
32	
33	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
34	
35	Gates are ineffective because NTP pressure pushes them toward identity (\S\ref{subsec:gate-conditioning}), and this is not caused by gradient direction conflict (\S\ref{subsec:pcgrad}). The remaining question: why do GAR improvements under teacher forcing fail to transfer to autoregressive generation?
36	
37	The 20--33$\times$ GAR gap (Table~\ref{tab:four-way}) persists across all training strategies: the model learns the intended attention pattern on the training distribution but collapses under model-generated text. GAR-Dongre provides a revealing control: under standard teacher-forced training it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys the concentrated last-token attention pattern while leaving diffuse attention unaffected (scheduled sampling breaks this pattern; \S\ref{sec:discussion}).
38	
39	The mechanism is exposure bias \citep{bengio2015scheduled}: during training, the model conditions on ground-truth prefixes; at inference, on its own outputs. The statistical properties diverge, and the 2--7\% gate attenuation (\S\ref{subsec:gate-conditioning}) cannot compensate. \citet{he2019exposure} showed that language models exhibit token-level self-recovery from exposure bias, and our PPL results confirm this (Table~\ref{tab:four-way}). The critical distinction is between primary and auxiliary objectives: NTP is robust because it is the same task at both training and inference time, while GAR optimizes a distributional property of the input prefix that has no counterpart under autoregressive generation. Figure~\ref{fig:attention-heatmap} confirms teacher-forced GAR-ours remains near $\tau = 0.5$ (7--8\% decay, $N$\,=\,45), yet autoregressive GAR collapses for all variants (Figure~\ref{fig:gate-shift}b).
40	
41	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
42	
43	\S\ref{subsec:dist-shift} showed that exposure bias selectively destroys GAR-ours (20--33$\times$ gap) while, under standard training, GAR-Dongre remains unaffected. We test whether this selectivity extends beyond attention with an orthogonal hidden-state probe.
44	
45	We define Turn-level Residual Coherence (TRC) as the cosine similarity between hidden states at the last-token position of adjacent assistant turns. If exposure bias caused broad representational failure, TRC should show a comparable gap. It does not. For ThreadGate, teacher-forced TRC is 0.334 and autoregressive TRC is 0.332 (gap $= +0.002$). For LoRA-only, teacher-forced TRC is 0.349 and autoregressive TRC is 0.411 (gap $= -0.062$, reversed): autoregressive generation does not degrade hidden-state coherence. Neither checkpoint shows a TRC gap comparable to the 20--33$\times$ GAR collapse.
46	
47	The slightly elevated autoregressive TRC for LoRA-only likely reflects higher token-level predictability in model-generated text, which produces more self-similar hidden states. These results confirm the selectivity from \S\ref{subsec:dist-shift} with an orthogonal metric: exposure bias disrupts a specific learned routing behavior (summary-position attention to goal tokens) while leaving internal representations intact.
48	
49	Cross-model evaluation extends this selectivity: GAR-Dongre shows negligible distribution shift on both Llama-3.1-8B (TF/AR ratio 1.002$\times$) and Qwen-2.5-7B (1.28$\times$), compared to the 12.5--30$\times$ collapse in GAR-ours, confirming that exposure bias primarily disrupts attention concentration at generation boundaries rather than aggregate attention patterns (the scheduled sampling experiment in \S\ref{sec:discussion} breaks this pattern, with GAR-Dongre rising to 0.353).
50	
51	\subsection{Cross-Model Generality}\label{subsec:cross-model}
52	
53	To test whether the exposure bias failure generalizes, we replicate the full evaluation pipeline on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3}. Phase~1 diagnostics confirm goal attention decay (GAR: 0.026$\to$0.003 over 10 turns, 90.1\% decline vs.\ Qwen's 84.7\%). A matched evaluation ($N$\,=\,50, $T$\,=\,4) quantifies the exposure bias gap: teacher-forced GAR-ours is 0.484, autoregressive is 0.039, a 12.5$\times$ gap directionally consistent with Qwen's 20--33$\times$. The gate profile differs---Qwen's minimum at layers~3--4, Llama's at layer~25---yet both converge toward identity under NTP pressure. The exposure bias gap is consistent across architecturally distinct LLMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2d9eda6-036e-4ecd-8d13-baff2edc1cfb",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "f531c41d-1e62-460f-b5af-e265a31c57d7",
  "sourceToolAssistantUUID": "e2d9eda6-036e-4ecd-8d13-baff2edc1cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T19:45:29.120Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rd9Xn4r6X3FN7CDeXUujDM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f531c41d-1e62-460f-b5af-e265a31c57d7",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e59d7ba-b8c1-423f-9c1e-0baf0984f3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T19:45:29.125Z_

<details><summary>↩ Tool result · `toolu_01Rd9Xn4r6X3FN7CDeXUujDM`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.029 to 0.697, providing constructive evidence that attention misallocation is the proximal cause (\S\ref{subsec:steering}).
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, linearly mixing teacher-forced and model-generated contexts. Autoregressive GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the 30$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36). GAR-Dongre also rises (0.019$\to$0.353), suggesting indirect improvement of all-token goal attention. The two paths are complementary: steering trades fluency for goal recall; scheduled sampling incurs no fluency cost but requires retraining.
6	
7	\paragraph{Instruction retention under steering.} Across 18 system-prompt constraint types, $\beta$\,=\,3 steering increases content constraint compliance by +23.8\,pp (GAR-compliance $r$\,=\,0.200, $p$\,=\,0.007; McNemar $p$\,=\,0.077), providing exploratory evidence for downstream benefit pending multi-model confirmation.
8	
9	TRC analysis (\S\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence. We scope claims to GAR losses on Qwen-2.5-7B and Llama-3.1-8B; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibria \citep{navon2022nash} remain untested. Remaining directions include adaptive $\beta$ scheduling and layer-selective steering.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e59d7ba-b8c1-423f-9c1e-0baf0984f3dd",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "8fe8726e-998c-46f6-8b80-2ef4dfa06c64",
  "sourceToolAssistantUUID": "1e59d7ba-b8c1-423f-9c1e-0baf0984f3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T19:45:30.050Z_

<details open><summary>🔧 Tool call — Read · `toolu_012KbAvA9ASu2FGARGg7dEmB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fe8726e-998c-46f6-8b80-2ef4dfa06c64",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ca48cb3e-962b-488c-baaf-8dc3608234a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T19:45:30.056Z_

<details><summary>↩ Tool result · `toolu_012KbAvA9ASu2FGARGg7dEmB`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	ThreadGate modulates the residual stream with per-layer gated MLP networks and an auxiliary GAR loss. Training succeeds (TF GAR\,=\,0.50), but autoregressive GAR collapses 20--33$\times$ (exposure bias), confirmed on Llama-3.1-8B (12.5$\times$). Inference-time steering ($\beta$\,=\,5, GAR 0.697) and scheduled sampling (gap 30$\times$$\to$1.57$\times$, no PPL cost, single seed) both demonstrate attention misallocation---not representation degradation---as the proximal cause.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca48cb3e-962b-488c-baaf-8dc3608234a9",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "fd275010-47b8-47af-a3f6-c49cb60bc258",
  "sourceToolAssistantUUID": "ca48cb3e-962b-488c-baaf-8dc3608234a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T19:45:30.602Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DvfbZ6eY7QkS1SvhJk8LAn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd275010-47b8-47af-a3f6-c49cb60bc258",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dd733df-4fce-4462-8f74-125a73febd86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T19:45:30.612Z_

<details><summary>↩ Tool result · `toolu_01DvfbZ6eY7QkS1SvhJk8LAn`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	Our experiments use a single random seed (seed\,=\,42). While the five-way convergence across ThreadGate, +PCGrad, Uniform Gate, and LoRA-only provides indirect evidence of robustness (four independent configurations reaching indistinguishable performance is unlikely to result from seed-specific artifacts), multi-seed validation would strengthen this conclusion.
4	
5	We test only one type of auxiliary attention loss (GAR with MSE target $\tau = 0.5$). Other attention steering objectives, such as head-specific or layer-specific attention losses, may exhibit different sensitivity to exposure bias. Our negative result applies to the GAR family; it does not rule out all auxiliary attention interventions.
6	
7	Training uses 8K conversations from UltraChat. Larger-scale training could alter gate dynamics, particularly if the model encounters sufficient distributional diversity to reduce the training-inference mismatch.
8	
9	All experiments use two model families (Qwen-2.5-7B and Llama-3.1-8B); while cross-model evaluation confirms the exposure bias gap, $N$\,=\,2 does not establish universality. The Llama evaluation includes only the ThreadGate configuration; the full four-way ablation (LoRA-only, Uniform Gate) has not been replicated, and all experiments use a single dataset (UltraChat). The instruction retention analysis is exploratory: a single model, 18 system-prompt constraint types, and a single $\beta$ value without grid search.
10	
11	The PCGrad causal exclusion addresses gradient direction conflict only. Magnitude imbalance (GradNorm; \citealp{chen2018gradnorm}) and Nash equilibrium approaches (Nash-MTL; \citealp{navon2022nash}) remain untested and could reveal additional failure modes or interaction effects.
12	
13	All four fine-tuned variants share the same GAR auxiliary loss. This design isolates the gating mechanism but does not test whether gating could be effective without an auxiliary attention loss or under a different training objective.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2dd733df-4fce-4462-8f74-125a73febd86",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "62abd0e6-c5e2-4530-8b3c-97ed94b3d9f1",
  "sourceToolAssistantUUID": "2dd733df-4fce-4462-8f74-125a73febd86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T19:45:31.168Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T1LNN5sg3jPKV1grNmsuQf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62abd0e6-c5e2-4530-8b3c-97ed94b3d9f1",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c28c43a1-1246-4739-bde6-08d9f63b2d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T19:45:31.180Z_

<details><summary>↩ Tool result · `toolu_01T1LNN5sg3jPKV1grNmsuQf`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Recent work has established that LLMs systematically degrade across conversation turns. \citet{levy2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Attention Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\% across turns in 12 models, while residual stream probes retain goal information with AUC\,=\,0.98. We observe a steeper 70.8\% decline on Qwen-2.5-7B-Instruct (\S\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.
5	
6	\paragraph{Residual gating and adaptive depth.}
7	ReZero \citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \citep{fan2020layerdrop}, Mixture-of-Depths \citep{raposo2024mixture}, FlexiDepth \citep{luo2025flexidepth}, and CALM \citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.
8	
9	\paragraph{Attention manipulation.}
10	StreamingLLM \citep{xiao2024streaming} identified attention sinks and proposed anchor token retention; \citet{ko2024found} showed positional bias against middle-positioned information; \citet{qiu2025gated} replaced softmax with a learned gate for sparse attention. These approaches intervene inside the attention mechanism, while ThreadGate operates on the residual stream. Our results suggest that neither pathway alone overcomes the distributional gap between teacher-forced training and autoregressive inference.
11	
12	\paragraph{Multi-task gradient conflict.}
13	GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.
14	
15	\paragraph{Exposure bias.}
16	Teacher forcing creates a distributional mismatch between training and inference that compounds over sequence length. Scheduled Sampling \citep{bengio2015scheduled} introduced curriculum-based mixing of ground-truth and model-generated tokens. MIXER \citep{ranzato2016sequence} combined token-level and sequence-level objectives, and Professor Forcing \citep{lamb2016professor} used adversarial regularization to align hidden state distributions under both regimes. \citet{he2019exposure} showed that autoregressive models exhibit self-recovery from exposure bias at the token prediction level. SEARNN \citep{leblond2018searnn} proposed locally recurrent search-based training to avoid the mismatch entirely. This literature focuses on generation quality degradation in primary objectives. No prior work examines how exposure bias affects auxiliary objectives that target attention distributions, nor how it manifests in multi-turn dialogue settings. Our work identifies a distinct failure mode: auxiliary attention losses that converge under teacher forcing fail completely under autoregressive generation, even when NTP remains robust, because token-level self-recovery does not extend to distributional properties of attention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c28c43a1-1246-4739-bde6-08d9f63b2d75",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "a6e21085-b1d3-49f4-b7a0-532075158fe3",
  "sourceToolAssistantUUID": "c28c43a1-1246-4739-bde6-08d9f63b2d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T19:45:31.609Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GiqLMX9tTj97rxJobz7hDi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6e21085-b1d3-49f4-b7a0-532075158fe3",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4b6e458-a9a0-45a2-a0f0-3280451b9130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T19:45:31.615Z_

<details><summary>↩ Tool result · `toolu_01GiqLMX9tTj97rxJobz7hDi`</summary>

```text
1	\section{Training Hyperparameters}\label{sec:appendix-hyper}
2	
3	All fine-tuned variants share the following configuration: Qwen-2.5-7B-Instruct base model, LoRA rank 16 ($\alpha$=32) on \texttt{q\_proj} and \texttt{v\_proj}, AdamW optimizer (lr = $2 \times 10^{-4}$, $\beta_1$=0.9, $\beta_2$=0.999), batch size 1 with gradient accumulation 8, 3 epochs over 8K UltraChat conversations, maximum sequence length 2048, seed 42. ThreadGate gates use a 10$\times$ learning rate multiplier and initial bias 1.5 ($\sigma(1.5) \approx 0.82$).
4	
5	\section{Loss Formulation Search}\label{sec:appendix-loss}
6	
7	Table~\ref{tab:loss-iterations} summarizes the seven loss configurations explored before arriving at the final MSE + gate diversity formulation (\S\ref{sec:loss}). Configurations v1--v6 span three alternative loss families; none converged during training.
8	
9	\begin{table}[h]
10	\centering\small
11	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration.}
12	\label{tab:loss-iterations}
13	\begin{tabular}{l l l c c}
14	\toprule
15	 & \textbf{Loss Family} & \textbf{Status} & \textbf{GAR} & \textbf{PPL} \\
16	\midrule
17	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & ---  & ---  \\
18	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & ---  & ---  \\
19	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & ---  & ---  \\
20	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & ---  & ---  \\
21	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & ---  & ---  \\
22	v6  & Smooth saturation       & \texttimes~identity collapse   & ---  & ---  \\
23	v7  & MSE + gate div          & \checkmark~converged           & 0.50 & 2.78 \\
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
  "parentUuid": "a4b6e458-a9a0-45a2-a0f0-3280451b9130",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "64bacbea-2b9a-46f7-bc09-66fa38c04551",
  "sourceToolAssistantUUID": "a4b6e458-a9a0-45a2-a0f0-3280451b9130",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T19:45:31.791Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RL3Tp2EGNGoNzc2FZiXS8y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64bacbea-2b9a-46f7-bc09-66fa38c04551",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHh8oaSWXsCSBZvUXbb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f06e50c7-af37-4a2e-ad1e-8dae1dc6ea5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JC8GBywnY9jrxumnjwAKT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7179,
      "cache_read_input_tokens": 9308,
      "output_tokens": 911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7179
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 911,
          "cache_read_input_tokens": 9308,
          "cache_creation_input_tokens": 7179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7179,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T19:45:31.796Z_

<details><summary>↩ Tool result · `toolu_01RL3Tp2EGNGoNzc2FZiXS8y`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{url}
16	\usepackage{subcaption}
17	
18	\graphicspath{{../figures/paper/}}
19	
20	\title{Why Lightweight Gating Fails to Fix Multi-Turn Attention Degradation:\\A Mechanistic Analysis}
21	
22	\author{Anonymous}
23	
24	\begin{document}
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliographystyle{acl_natbib}
38	\bibliography{references}
39	
40	\appendix
41	\input{sections/appendix}
42	
43	\end{document}
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f06e50c7-af37-4a2e-ad1e-8dae1dc6ea5a",
  "isSidechain": true,
  "promptId": "8fec2922-ea84-49e8-8c68-b26f8c1ae0a6",
  "agentId": "a868fff727d9f6065",
  "type": "user",
  "uuid": "0e183b2d-2555-404c-9d79-e7c83aa77df2",
  "sourceToolAssistantUUID": "f06e50c7-af37-4a2e-ad1e-8dae1dc6ea5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T19:47:58.190Z_

Now I have all the files. Let me compile the exhaustive list of every quantitative claim.

---

## EXHAUSTIVE QUANTITATIVE CLAIMS BY FILE

### 1. abstract.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 1 | 2 | "GAR declines by 70.8\% between early and mid-conversation turns" | 70.8% | Relative GAR decline | Qwen-2.5-7B baseline GAR decay measurement |
| 2 | 2 | "AUC\,=\,0.98" | 0.98 | Linear probe AUC for goal content recovery from residual stream | Residual stream probing (from Dongre et al.) |
| 3 | 2 | "teacher-forced GAR\,=\,0.50" | 0.50 | Teacher-forced GAR-ours value | All fine-tuned variants, teacher-forced eval |
| 4 | 2 | "autoregressive GAR drops to 0.015--0.025" | 0.015--0.025 | Autoregressive GAR-ours range | All fine-tuned variants, autoregressive eval |
| 5 | 2 | "a 20--33$\times$ gap" | 20--33x | TF-to-AR GAR gap ratio | Exposure bias gap across variants |
| 6 | 2 | "$\beta$\,=\,5" | 5 | Steering bias parameter value | Inference-time attention steering |
| 7 | 2 | "GAR from 0.029 to 0.697" | 0.029, 0.697 | GAR-ours before/after steering | Steering on ThreadGate checkpoint |
| 8 | 2 | "1.57$\times$" | 1.57x | Compressed gap ratio after scheduled sampling | Scheduled sampling experiment |
| 9 | 2 | "no PPL cost" | (qualitative, but implies PPL unchanged) | PPL invariance | Scheduled sampling |
| 10 | 2 | "12.5$\times$" | 12.5x | TF-to-AR GAR gap on Llama | Cross-model eval on Llama-3.1-8B |

### 2. introduction.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 11 | 3 | "27--48\% between early and mid-conversation turns" | 27--48% | GAR decline range across 12 models | Dongre et al. replication |
| 12 | 3 | "70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation" | 70.8%, 0.0418, 0.0122 | GAR decay: relative decline, absolute GAR at turn 1, absolute GAR at mid-conversation | Qwen-2.5-7B baseline measurement |
| 13 | 5 | "AUC\,=\,0.98" | 0.98 | Probe AUC | Dongre et al. residual stream probing |
| 14 | 10 | "GAR-ours reaches 0.50" (figure caption) | 0.50 | Teacher-forced GAR-ours | Five-way comparison, TF eval |
| 15 | 10 | "drops to 0.015--0.025, a 20--33$\times$ gap" (figure caption) | 0.015--0.025, 20--33x | Autoregressive GAR-ours, gap ratio | Five-way comparison, AR eval |
| 16 | 14 | "$\tau = 0.5$" | 0.5 | GAR loss MSE target | Training objective design |
| 17 | 16 | "teacher-forced GAR-ours reaches 0.50" | 0.50 | Teacher-forced GAR-ours | All fine-tuned variants |
| 18 | 16 | "0.015--0.025, a 20--33$\times$ gap" | 0.015--0.025, 20--33x | AR GAR-ours, gap | All variants |
| 19 | 16 | "0.75\,pp spread on GAR-ours" | 0.75 pp | Spread across 4 fine-tuned variants | Teacher-forced evaluation |
| 20 | 16 | "identical PPL at 2.78" | 2.78 | Perplexity | All four fine-tuned variants |
| 21 | 16 | "0.029 to 0.697" | 0.029, 0.697 | GAR before/after steering | Steering at beta=5 |
| 22 | 16 | "0.016 to 0.318 (20$\times$)" | 0.016, 0.318, 20x | GAR-ours before/after scheduled sampling, improvement factor | Scheduled sampling |
| 23 | 16 | "30$\times$ gap to 1.57$\times$" | 30x, 1.57x | Gap before/after scheduled sampling | Scheduled sampling |
| 24 | 16 | "20--33$\times$ gap" (contributions section) | 20--33x | Exposure bias gap | Main result |
| 25 | 16 | "30$\times$ to 1.57$\times$" (contributions section) | 30x, 1.57x | Gap compression | Scheduled sampling |
| 26 | 16 | "12.5$\times$ gap" (contributions) | 12.5x | Cross-model gap | Llama-3.1-8B |
| 27 | 16 | "$\beta$\,=\,5" (contributions) | 5 | Steering bias | Steering experiment |
| 28 | 16 | "0.029 to 0.697" (contributions) | 0.029, 0.697 | GAR before/after steering | Steering experiment |

### 3. background.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 29 | 18 | "probe AUC\,=\,0.98" | 0.98 | Residual stream probe AUC | Dongre et al. probing |

### 4. method.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 30 | 29 | "projects from the hidden dimension to 16 units" | 16 | Projection output dimension | Gate architecture |
| 31 | 29 | "16-dimensional turn embedding" | 16 | Turn embedding dimension | Gate architecture |
| 32 | 29 | "concatenated 32-dimensional input" | 32 | Gate input dimension (16+16) | Gate architecture |
| 33 | 29 | "64-unit hidden layer" | 64 | Gate MLP hidden size | Gate architecture |
| 34 | 29 | "28 layers in Qwen-2.5-7B-Instruct" | 28 | Number of transformer layers / gate networks | Model architecture |
| 35 | 29 | "initialized near 0.82" | 0.82 | Initial gate value (sigma(1.5)) | Gate initialization |
| 36 | 29 | "10$\times$ learning rate multiplier" | 10x | Gate LR multiplier | Training config |
| 37 | 41 | "$\tau = 0.5$" | 0.5 | GAR MSE target | Training objective |
| 38 | 45 | "$\lambda_\text{GAR} = \lambda_\text{div} = 1.0$" | 1.0, 1.0 | Loss weights for GAR and diversity | Training objective |

### 5. experiments.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 39 | 6 | "8K multi-turn conversations from the UltraChat training split" | 8K | Training dataset size | Training setup |
| 40 | 6 | "LoRA adapters (rank 16, $\alpha$=32)" | 16, 32 | LoRA rank and alpha | Training config |
| 41 | 6 | "$\lambda_\text{GAR} = \lambda_\text{div} = 1.0$" | 1.0 | Loss weights | Training config |
| 42 | 6 | "MSE target $\tau = 0.5$" | 0.5 | GAR target | Training config |
| 43 | 6 | "3 epochs" | 3 | Training epochs | Training config |
| 44 | 6 | "lr $= 2 \times 10^{-4}$" | 2e-4 | Learning rate | Training config |
| 45 | 6 | "batch size 1" | 1 | Batch size | Training config |
| 46 | 6 | "gradient accumulation 8" | 8 | Gradient accumulation steps | Training config |
| 47 | 6 | "seed 42" | 42 | Random seed | Training config |
| 48 | 6 | "approximately 6 hours" | 6 hours | Training time per variant | Training config |
| 49 | 6 | "102\,GB" | 102 GB | GPU memory (RTX PRO 6000) | Hardware |
| 50 | 8 | "28 gate networks" | 28 | Number of gates | ThreadGate config |
| 51 | 8 | "50 non-overlapping conversations" | 50 | Held-out eval size | Evaluation setup |
| 52 | 12 | "0.75 percentage points (pp)" | 0.75 pp | GAR-ours spread across variants | Five-way comparison |
| 53 | 12 | "ThreadGate (0.50), +PCGrad (0.50), Uniform Gate (0.51), and LoRA-only (0.50)" | 0.50, 0.50, 0.51, 0.50 | GAR-ours per variant | Five-way TF eval |
| 54 | 12 | "PPL is 2.78 for all four" | 2.78 | PPL for all fine-tuned variants | IID evaluation |
| 55 | 14 | "GAR-ours jumps from 0.01 to ${\sim}$0.50" | 0.01, ~0.50 | Base vs fine-tuned GAR-ours | Base vs fine-tuned comparison |
| 56 | 14 | "PPL improves from 4.23 to 2.78" | 4.23, 2.78 | PPL base vs fine-tuned | Base vs fine-tuned |
| 57 | 14 | "GAR-Dongre remains uniformly low (0.01--0.02)" | 0.01--0.02 | GAR-Dongre range | All standard-trained conditions |
| 58 | 16 | "0.015--0.025 across all fine-tuned variants, a 20--33$\times$ gap" | 0.015--0.025, 20--33x | AR GAR-ours, gap ratio | Autoregressive eval |
| 59 | 21 | "0.75\,pp on GAR-ours" (table caption) | 0.75 pp | GAR-ours spread | Table 1 caption |

**Table 1 values (lines 29--33):**

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 60 | 29 | "Base: 0.01 / 0.00 / 4.23 / 0.01 / 0.00 / 4.34" | 0.01, 0.00, 4.23, 0.01, 0.00, 4.34 | Base: IID GAR-O, IID GAR-D, IID PPL, held-out GAR-O, held-out GAR-D, held-out PPL | Five-way table |
| 61 | 30 | "ThreadGate: 0.50 / 0.02 / 2.78 / 0.50 / 0.02 / 2.78" | 0.50, 0.02, 2.78, 0.50, 0.02, 2.78 | ThreadGate IID & held-out | Five-way table |
| 62 | 31 | "+PCGrad: 0.50 / 0.01 / 2.78 / 0.50 / 0.01 / 2.78" | 0.50, 0.01, 2.78, 0.50, 0.01, 2.78 | +PCGrad IID & held-out | Five-way table |
| 63 | 32 | "Uniform Gate: 0.51 / 0.01 / 2.78 / 0.51 / 0.01 / 2.78" | 0.51, 0.01, 2.78, 0.51, 0.01, 2.78 | Uniform Gate IID & held-out | Five-way table |
| 64 | 33 | "LoRA-only: 0.50 / 0.01 / 2.78 / 0.50 / 0.01 / 2.78" | 0.50, 0.01, 2.78, 0.50, 0.01, 2.78 | LoRA-only IID & held-out | Five-way table |

**Figure captions (lines 41, 49, 51, 58):**

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 65 | 41 | "$N$\,=\,45" | 45 | Number of conversations in per-turn eval | Per-turn GAR figure |
| 66 | 41 | "$\tau$\,=\,0.5" | 0.5 | GAR target | Per-turn figure caption |
| 67 | 41 | "7--8\% decay (T1$\to$T4)" | 7--8% | Teacher-forced GAR decay across turns | Fine-tuned variants TF eval |
| 68 | 41 | "80\%" | 80% | Base model GAR decay | Base model per-turn |
| 69 | 41 | "0.015--0.025" | 0.015--0.025 | AR GAR for all variants | Autoregressive eval |
| 70 | 49 | "$N$\,=\,5 ten-turn conversations" | 5, 10 | Sample size, turn count | Initial steering eval |
| 71 | 49 | "$\beta \in [0, 2]$" | 0, 2 | Steering bias range (low) | Steering experiment |
| 72 | 49 | "0.029\,$\to$\,0.075" | 0.029, 0.075 | GAR at low beta | Steering beta 0-2 |
| 73 | 49 | "${\sim}$1.4" | ~1.4 | PPL at low beta | Steering beta 0-2 |
| 74 | 49 | "$\beta$\,=\,2 and $\beta$\,=\,5" | 2, 5 | Beta range of nonlinearity | Steering transition |
| 75 | 49 | "${\sim}$9$\times$" | ~9x | GAR recovery factor | Steering beta 2->5 |
| 76 | 49 | "0.075\,$\to$\,0.697$\pm$0.020" | 0.075, 0.697, 0.020 (std) | GAR values and std at beta=5 | Steering N=5 |
| 77 | 49 | "35\%" | 35% | PPL increase (beta 0->5) | Steering N=5 |
| 78 | 49 | "1.41\,$\to$\,1.91" | 1.41, 1.91 | PPL at beta=0 and beta=5 | Steering N=5 |
| 79 | 49 | "$\beta$\,=\,10" | 10 | High beta value | Steering extreme |
| 80 | 49 | "GAR saturates at 0.959" | 0.959 | GAR at beta=10 | Steering N=5 |
| 81 | 49 | "PPL degrades to 4.22" | 4.22 | PPL at beta=10 | Steering N=5 |
| 82 | 51 | "$N$\,=\,50" | 50 | Sample size for larger steering eval | Steering N=50 |
| 83 | 51 | "39 with $\geq$3 turns" | 39 | Subset with >= 3 turns | Steering N=50 |
| 84 | 51 | "mean 3.6 user turns" | 3.6 | Mean user turns | Steering N=50 |
| 85 | 51 | "0.128$\pm$0.110 ($\beta$\,=\,2)" | 0.128, 0.110 (std) | GAR at beta=2 | Steering N=50 |
| 86 | 51 | "0.556$\pm$0.060 ($\beta$\,=\,3)" | 0.556, 0.060 (std) | GAR at beta=3 | Steering N=50 |
| 87 | 51 | "8.7$\times$ recovery" | 8.7x | GAR recovery factor at beta=3 | Steering N=50 |
| 88 | 51 | "9\% PPL increase" | 9% | PPL cost at beta=3 | Steering N=50 |
| 89 | 51 | "1.43\,$\to$\,1.56" | 1.43, 1.56 | PPL at beta=0 and beta=3 | Steering N=50 |
| 90 | 51 | "$\beta$\,=\,3 as a practical operating point" | 3 | Recommended beta | Steering N=50 |
| 91 | 51 | "mean 0.064, median 0.031, std 0.081" | 0.064, 0.031, 0.081 | Beta=0 distribution stats (mean, median, std) | Steering N=50 baseline |
| 92 | 51 | "0.029" | 0.029 | Baseline GAR in 10-turn N=5 eval | Steering N=5 baseline |
| 93 | 58 | "${\sim}$9$\times$ recovery with 35\% PPL rise" (figure caption) | 9x, 35% | GAR recovery factor, PPL cost | Steering N=5 fig caption |
| 94 | 58 | "8.7$\times$ GAR recovery, 9\% PPL cost" (figure caption) | 8.7x, 9% | GAR recovery, PPL cost | Steering N=50 fig caption |

### 6. analysis.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 95 | 7 | "turn~1 (early) and turn~21 (late) across all 28 layers" | 1, 21, 28 | Turn indices and layer count | Gate conditioning analysis |
| 96 | 9 | "27 of 28 layers" | 27, 28 | Layers with inverted conditioning | Gate conditioning |
| 97 | 9 | "$p = 3.73 \times 10^{-8}$" | 3.73e-8 | p-value, Wilcoxon signed-rank test | Gate conditioning significance |
| 98 | 9 | "effect size $r = 0.975$" | 0.975 | Effect size (r) | Gate conditioning |
| 99 | 9 | "layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21" | 0.769, 0.979 | Gate values at layer 23 | Gate turn conditioning |
| 100 | 9 | "layer~14, it is 0.747 at turn~1 and 0.928 at turn~21" | 0.747, 0.928 | Gate values at layer 14 | Gate turn conditioning |
| 101 | 11 | "0.93 to 0.98 (2--7\% attenuation)" | 0.93, 0.98, 2--7% | Inference-time gate value range, attenuation range | Gate behavior at inference |
| 102 | 16 | "27/28 layers" (figure caption) | 27, 28 | Layers with inverted conditioning | Fig caption |
| 103 | 16 | "$p = 3.73 \times 10^{-8}$" (figure caption) | 3.73e-8 | p-value | Fig caption |
| 104 | 16 | "20--33$\times$ GAR gap" (figure caption) | 20--33x | GAR gap ratio | Fig caption |
| 105 | 22 | "68--79\% of layers" | 68--79% | Percentage of layers with opposing gradients | Gradient conflict analysis |
| 106 | 22 | "mean cosine similarity ranging from $-$0.089 (epoch~0) to $-$0.042 (epoch~2)" | -0.089, -0.042 | Mean cosine similarity between NTP and GAR gradients | Gradient conflict trajectory |
| 107 | 22 | "NTP gradient magnitude dominates by 7.5--14.7$\times$" | 7.5--14.7x | NTP-to-GAR gradient magnitude ratio | Gradient magnitude analysis |
| 108 | 24 | "$-$0.089" | -0.089 | Cosine similarity (ThreadGate) | Gradient direction before PCGrad |
| 109 | 24 | "$-$0.15 to $+$0.09" | -0.15, +0.09 | Cosine similarity range with PCGrad | After PCGrad |
| 110 | 24 | "0.50 vs 0.50" | 0.50, 0.50 | IID GAR-ours (ThreadGate vs +PCGrad) | PCGrad comparison |
| 111 | 24 | "2.780 vs 2.784" | 2.780, 2.784 | PPL (ThreadGate vs +PCGrad) | PCGrad comparison |
| 112 | 24 | "0.015 vs 0.016" | 0.015, 0.016 | Autoregressive GAR (ThreadGate vs +PCGrad) | PCGrad comparison |
| 113 | 24 | "7.5--14.7$\times$ NTP magnitude dominance" | 7.5--14.7x | Gradient magnitude ratio | PCGrad analysis |
| 114 | 37 | "20--33$\times$ GAR gap" | 20--33x | Distribution shift gap | Distribution shift analysis |
| 115 | 37 | "0.01--0.02" | 0.01--0.02 | GAR-Dongre range under standard training | Distribution shift |
| 116 | 39 | "2--7\% gate attenuation" | 2--7% | Gate attenuation range | Mechanism analysis |
| 117 | 39 | "7--8\% decay, $N$\,=\,45" | 7--8%, 45 | TF GAR decay, sample size | Teacher-forced per-turn |
| 118 | 45 | "TRC is 0.334 and autoregressive TRC is 0.332 (gap $= +0.002$)" | 0.334, 0.332, +0.002 | TRC teacher-forced, autoregressive, gap for ThreadGate | TRC analysis |
| 119 | 45 | "teacher-forced TRC is 0.349 and autoregressive TRC is 0.411 (gap $= -0.062$, reversed)" | 0.349, 0.411, -0.062 | TRC teacher-forced, autoregressive, gap for LoRA-only | TRC analysis |
| 120 | 45 | "20--33$\times$ GAR collapse" | 20--33x | GAR gap (context for TRC comparison) | TRC analysis |
| 121 | 49 | "TF/AR ratio 1.002$\times$" | 1.002x | GAR-Dongre TF/AR ratio for Llama | Cross-model GAR-Dongre |
| 122 | 49 | "1.28$\times$" | 1.28x | GAR-Dongre TF/AR ratio for Qwen | Cross-model GAR-Dongre |
| 123 | 49 | "12.5--30$\times$ collapse in GAR-ours" | 12.5--30x | GAR-ours TF/AR ratio range across models | Cross-model GAR-ours |
| 124 | 49 | "GAR-Dongre rising to 0.353" | 0.353 | GAR-Dongre under scheduled sampling | Scheduled sampling |
| 125 | 53 | "GAR: 0.026$\to$0.003 over 10 turns" | 0.026, 0.003, 10 | Llama GAR decay values, turn count | Llama Phase 1 diagnostics |
| 126 | 53 | "90.1\% decline vs.\ Qwen's 84.7\%" | 90.1%, 84.7% | Relative GAR decline for Llama vs Qwen | Cross-model baseline decay |
| 127 | 53 | "$N$\,=\,50, $T$\,=\,4" | 50, 4 | Sample size, turns for Llama eval | Llama evaluation setup |
| 128 | 53 | "teacher-forced GAR-ours is 0.484" | 0.484 | TF GAR-ours for Llama | Llama TF eval |
| 129 | 53 | "autoregressive is 0.039" | 0.039 | AR GAR-ours for Llama | Llama AR eval |
| 130 | 53 | "12.5$\times$ gap" | 12.5x | TF/AR gap for Llama | Llama exposure bias |
| 131 | 53 | "Qwen's 20--33$\times$" | 20--33x | Qwen gap for comparison | Qwen exposure bias |
| 132 | 53 | "layers~3--4" | 3--4 | Qwen gate minimum layers | Gate profile |
| 133 | 53 | "layer~25" | 25 | Llama gate minimum layer | Gate profile |

### 7. discussion.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 134 | 3 | "7.5--14.7$\times$ the GAR magnitude" | 7.5--14.7x | NTP gradient magnitude dominance | Gradient analysis |
| 135 | 3 | "2--7\% attenuation" | 2--7% | Gate attenuation range | Gate behavior |
| 136 | 3 | "$\beta$\,=\,5" | 5 | Steering bias | Steering experiment |
| 137 | 3 | "0.029 to 0.697" | 0.029, 0.697 | GAR before/after steering | Steering |
| 138 | 5 | "0.016 to 0.318 (20$\times$)" | 0.016, 0.318, 20x | GAR-ours before/after scheduled sampling, improvement factor | Scheduled sampling |
| 139 | 5 | "30$\times$ gap to 1.57$\times$" | 30x, 1.57x | Gap compression | Scheduled sampling |
| 140 | 5 | "1.38 vs.\ 1.36" | 1.38, 1.36 | PPL: scheduled sampling vs standard | Scheduled sampling PPL |
| 141 | 5 | "0.019$\to$0.353" | 0.019, 0.353 | GAR-Dongre before/after scheduled sampling | Scheduled sampling GAR-Dongre |
| 142 | 7 | "18 system-prompt constraint types" | 18 | Number of constraint types tested | Instruction retention |
| 143 | 7 | "$\beta$\,=\,3" | 3 | Steering bias for instruction retention | Instruction retention |
| 144 | 7 | "+23.8\,pp" | +23.8 pp | Content constraint compliance improvement | Instruction retention |
| 145 | 7 | "$r$\,=\,0.200" | 0.200 | GAR-compliance correlation coefficient | Instruction retention |
| 146 | 7 | "$p$\,=\,0.007" | 0.007 | p-value for GAR-compliance correlation | Instruction retention |
| 147 | 7 | "McNemar $p$\,=\,0.077" | 0.077 | McNemar test p-value | Instruction retention |

### 8. conclusion.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 148 | 3 | "TF GAR\,=\,0.50" | 0.50 | Teacher-forced GAR-ours | Summary |
| 149 | 3 | "20--33$\times$" | 20--33x | Exposure bias gap | Summary |
| 150 | 3 | "12.5$\times$" | 12.5x | Llama gap | Summary |
| 151 | 3 | "$\beta$\,=\,5, GAR 0.697" | 5, 0.697 | Steering beta and resulting GAR | Summary |
| 152 | 3 | "30$\times$$\to$1.57$\times$" | 30x, 1.57x | Gap compression | Summary |

### 9. limitations.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 153 | 3 | "seed\,=\,42" | 42 | Random seed | Experimental setup |
| 154 | 5 | "$\tau = 0.5$" | 0.5 | GAR MSE target | Auxiliary loss config |
| 155 | 7 | "8K conversations" | 8K | Training dataset size | Training setup |
| 156 | 9 | "$N$\,=\,2" | 2 | Number of model families tested | Cross-model scope |
| 157 | 9 | "18 system-prompt constraint types" | 18 | Constraint types tested | Instruction retention scope |
| 158 | 9 | "single $\beta$ value" | (qualitative reference to beta=3) | Steering parameter | Instruction retention scope |

### 10. related_work.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 159 | 4 | "1388 turn-level instances" | 1388 | MT-Bench-101 dataset size | Related work (Bai et al.) |
| 160 | 4 | "27--48\%" | 27--48% | GAR decline in 12 models | Dongre et al. |
| 161 | 4 | "12 models" | 12 | Number of models tested | Dongre et al. |
| 162 | 4 | "AUC\,=\,0.98" | 0.98 | Probe AUC | Dongre et al. |
| 163 | 4 | "70.8\% decline" | 70.8% | Qwen GAR decline | This paper's replication |

### 11. appendix.tex

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 164 | 3 | "LoRA rank 16 ($\alpha$=32)" | 16, 32 | LoRA rank and alpha | Hyperparameters |
| 165 | 3 | "lr = $2 \times 10^{-4}$" | 2e-4 | Learning rate | Hyperparameters |
| 166 | 3 | "$\beta_1$=0.9, $\beta_2$=0.999" | 0.9, 0.999 | AdamW beta parameters | Hyperparameters |
| 167 | 3 | "batch size 1 with gradient accumulation 8" | 1, 8 | Batch size, grad accum | Hyperparameters |
| 168 | 3 | "3 epochs over 8K UltraChat conversations" | 3, 8K | Epochs, dataset size | Hyperparameters |
| 169 | 3 | "maximum sequence length 2048" | 2048 | Max seq length | Hyperparameters |
| 170 | 3 | "seed 42" | 42 | Random seed | Hyperparameters |
| 171 | 3 | "10$\times$ learning rate multiplier" | 10x | Gate LR multiplier | Hyperparameters |
| 172 | 3 | "initial bias 1.5 ($\sigma(1.5) \approx 0.82$)" | 1.5, 0.82 | Gate bias init, corresponding sigmoid value | Hyperparameters |

**Appendix Table (loss iterations, lines 17--22):**

| # | Line | Context | Number | Represents | Experiment |
|---|------|---------|--------|-----------|------------|
| 173 | 19 | "v3: Maximize ($\lambda$=2)" | 2 | Lambda for maximize loss v3 | Loss search |
| 174 | 20 | "v3b: Maximize ($\lambda$=10)" | 10 | Lambda for maximize loss v3b | Loss search |
| 175 | 21 | "v5: Maximize ($\lambda$=1)" | 1 | Lambda for maximize loss v5 | Loss search |
| 176 | 23 | "v7: GAR 0.50, PPL 2.78" | 0.50, 2.78 | Converged config results | Loss search final config |

### 12. main.tex

No quantitative claims in main.tex (only document structure/imports).

---

## SUMMARY OF KEY UNIQUE NUMERICAL CLAIMS

**Core experimental results (unique values, not repeated across files):**

- **Baseline GAR decay:** 0.0418 (turn 1) -> 0.0122 (mid-conv), 70.8% decline on Qwen; 0.026->0.003, 90.1% decline on Llama; 84.7% on Qwen (10-turn measurement)
- **Teacher-forced GAR-ours:** 0.50 (ThreadGate, +PCGrad, LoRA-only), 0.51 (Uniform Gate), 0.484 (Llama)
- **Autoregressive GAR-ours:** 0.015-0.025 range (Qwen), 0.039 (Llama); specific: 0.015 (ThreadGate), 0.016 (+PCGrad)
- **TF/AR gap:** 20-33x (Qwen), 12.5x (Llama)
- **PPL:** 2.78 (all fine-tuned), 4.23 (Base IID), 4.34 (Base held-out), 2.780 vs 2.784 (TG vs PCGrad exact)
- **Gate values:** 0.769/0.979 (layer 23 T1/T21), 0.747/0.928 (layer 14 T1/T21), range 0.93-0.98
- **Gate conditioning test:** p=3.73e-8, r=0.975, 27/28 layers inverted
- **Gradient conflict:** 68-79% of layers, cosine sim -0.089 to -0.042, magnitude 7.5-14.7x
- **PCGrad cosine shift:** -0.15 to +0.09
- **Steering N=5:** beta=5, GAR 0.029->0.697 (+/-0.020), PPL 1.41->1.91 (35%), beta=10 GAR 0.959 PPL 4.22
- **Steering N=50:** beta=3, GAR 0.128->0.556 (+/-0.060), 8.7x recovery, PPL 1.43->1.56 (9%); baseline stats mean 0.064, median 0.031, std 0.081
- **Scheduled sampling:** GAR-ours 0.016->0.318 (20x), gap 30x->1.57x, PPL 1.38 vs 1.36, GAR-Dongre 0.019->0.353
- **TRC:** ThreadGate TF 0.334 / AR 0.332 (gap +0.002); LoRA-only TF 0.349 / AR 0.411 (gap -0.062)
- **GAR-Dongre TF/AR ratios:** Llama 1.002x, Qwen 1.28x
- **Instruction retention:** +23.8pp, r=0.200, p=0.007, McNemar p=0.077, 18 constraint types
- **Probe AUC:** 0.98 (from Dongre et al.)

Total unique quantitative claims extracted: **176 entries** across all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e183b2d-2555-404c-9d79-e7c83aa77df2",
  "isSidechain": true,
  "agentId": "a868fff727d9f6065",
  "requestId": "req_011CbGHhnWUSZjV5iija6Nt6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfeb977a-34f7-476c-9ec1-f60ee25fe872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "sessionId": "92adc075-3f6d-4ab0-8ff6-caaf95aa61fe",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FawQm3LFZwUuyk8jGH6RqY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22865,
      "cache_read_input_tokens": 9308,
      "output_tokens": 9907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22865
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9907,
          "cache_read_input_tokens": 9308,
          "cache_creation_input_tokens": 22865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22865,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
