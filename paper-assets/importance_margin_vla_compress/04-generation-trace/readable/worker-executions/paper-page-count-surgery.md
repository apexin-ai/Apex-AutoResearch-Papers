# paper page count surgery

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 165
- **Recorded user turns:** 0
- **Tool calls:** 57
- **Original source:** `logs/workers/worker_paper_page_count_surgery_20260528T182642.log`
- **Structured JSON:** [`208cad122005e588288d.json`](../../sessions/20/208cad122005e588288d.json)

## Before a recorded user message

165 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
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
  "uuid": "a8d843b2-59c8-45fe-99e3-dd1bf90c0422",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1780004400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1b8c0c10-1109-4043-8c8a-49cb4c717623",
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the necessary files to understand the current state of the paper. I'll read them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "e3bfb0dd-9e48-4c7c-a802-40039030bf35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

Reading all paper source files to assess current content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "aa8df26f-68e4-459e-90be-88eb5e839746",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_011DE7D1fPKtG1uEiiCEDgV7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "f6b722ba-3b2e-4c43-8743-6d204c46a54a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-28T18:26:58.143Z_

<details><summary>↩ Tool result · `toolu_011DE7D1fPKtG1uEiiCEDgV7`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to near-zero (${\leq}$6.6\%). Apply the same reduction to $\pi_{0.5}$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a ViT encoder feeding tokens through a connector into a language model backbone; the critical difference is the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and extends to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture, implicitly assuming pruning transfers across designs.
15	
16	Yet current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure.
17	
18	We present an empirical study of VLA token compressibility, identifying the vision-language connector as the primary determinant of pruning robustness (Figure~\ref{fig:teaser}). Token-independent connectors degrade gracefully; entangling connectors produce catastrophic failures amplified by task complexity ($20{\times}$ from Object to Goal at $k{=}0.9$). The coefficient of variation (CV) of post-connector token L2 norms captures this on a continuous spectrum (0.038 to 0.314). Under sufficient compression, scoring effectiveness becomes connector-dependent: L2 norm aids $\pi_{0.5}$ (up to $+$46.9\,pp on Long at $k{=}0.9$; $+$35.2\,pp on Goal at $k{=}0.85$) but reverses at aggressive ratios ($-$36\,pp at $k{=}0.5$); on X-VLA it is anti-informative ($-$8 to $-$27\,pp), while attention recovers near-baseline performance. For pixel-shuffle connectors where all pruning fails, Vision Token Re-encoder (VTR, ${\sim}$5\% extra parameters) recovers over 60\% SR at 75\% compression.
19	
20	Our contributions are:
21	\begin{itemize}[nosep]
22	    \item A compressibility analysis across six VLA architectures (450M--7B) on four LIBERO suites, identifying connector architecture as the primary determinant of pruning robustness.
23	    \item CV of token L2 norms as a single-pass diagnostic for connector compressibility type (uniform, graded, catastrophic), validated on four closed-loop architectures.
24	    \item A zero-mask ablation proving position disruption---not information loss---drives $\pi_{0.5}$'s 89\,pp failure gap. VTR recovers a pixel-shuffle VLA from 0\% to over 60\% at 75\% compression.
25	\end{itemize}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "dfa13a50-802a-4b11-927f-5bd2b0f8f603",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_hero_overview.pdf}\n\\caption{Overview of VLA token compressibility.\n\\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.\n\\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.\n\\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}\n\\label{fig:teaser}\n\\end{figure*}\n\nRemove 5\\% of vision tokens from SmolVLA and its success rate collapses from 59.2\\% to near-zero (${\\leq}$6.6\\%). Apply the same reduction to $\\pi_{0.5}$ and it retains 98.2\\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a ViT encoder feeding tokens through a connector into a language model backbone; the critical difference is the connector architecture. Token pruning is well-established for ViTs~\\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and extends to VLAs~\\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture, implicitly assuming pruning transfers across designs.\n\nYet current VLAs employ fundamentally different vision connectors---linear projections~\\cite{black2024pi0}, MLP projectors~\\cite{kim2024openvla}, pixel-shuffle folding~\\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Deploying a pruning method validated on one connector type to another risks silent degradation or complete failure.\n\nWe present an empirical study of VLA token compressibility, identifying the vision-language connector as the primary determinant of pruning robustness (Figure~\\ref{fig:teaser}). Token-independent connectors degrade gracefully; entangling connectors produce catastrophic failures amplified by task complexity ($20{\\times}$ from Object to Goal at $k{=}0.9$). The coefficient of variation (CV) of post-connector token L2 norms captures this on a continuous spectrum (0.038 to 0.314). Under sufficient compression, scoring effectiveness becomes connector-dependent: L2 norm aids $\\pi_{0.5}$ (up to $+$46.9\\,pp on Long at $k{=}0.9$; $+$35.2\\,pp on Goal at $k{=}0.85$) but reverses at aggressive ratios ($-$36\\,pp at $k{=}0.5$); on X-VLA it is anti-informative ($-$8 to $-$27\\,pp), while attention recovers near-baseline performance. For pixel-shuffle connectors where all pruning fails, Vision Token Re-encoder (VTR, ${\\sim}$5\\% extra parameters) recovers over 60\\% SR at 75\\% compression.\n\nOur contributions are:\n\\begin{itemize}[nosep]\n    \\item A compressibility analysis across six VLA architectures (450M--7B) on four LIBERO suites, identifying connector architecture as the primary determinant of pruning robustness.\n    \\item CV of token L2 norms as a single-pass diagnostic for connector compressibility type (uniform, graded, catastrophic), validated on four closed-loop architectures.\n    \\item A zero-mask ablation proving position disruption---not information loss---drives $\\pi_{0.5}$'s 89\\,pp failure gap. VTR recovers a pixel-shuffle VLA from 0\\% to over 60\\% at 75\\% compression.\n\\end{itemize}\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01UZMcwvuT6i1uRARbRTVD5g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ef5dbe13-b598-45a2-977d-fe51072c5e12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-28T18:26:58.501Z_

<details><summary>↩ Tool result · `toolu_01UZMcwvuT6i1uRARbRTVD5g`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using attention signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, and Compressor-VLA~\cite{gao2025compressorvla}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Vision connectors.}
11	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "323d3082-b242-45bb-a2f7-4bfc6a883a37",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{ViT token pruning.}\nDynamicViT~\\cite{rao2021dynamicvit}, EViT~\\cite{liang2022evit}, A-ViT~\\cite{yin2022avit}, and Token Merging~\\cite{bolya2023tome} remove 50--66\\% of tokens with under 0.5\\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.\n\n\\paragraph{Token efficiency in VLMs and VLAs.}\nFastV~\\cite{chen2024fastv} and PruMerge~\\cite{shang2024prumerge} reduce vision tokens in VLMs using attention signals. VLA-specific methods have emerged: VLA-IAP~\\cite{cheng2026vlaiap}, VLA-Cache~\\cite{xu2025vlacache}, EfficientVLA~\\cite{yang2025efficientvla}, VLA-Pruner~\\cite{liu2025vlapruner}, LightVLA~\\cite{jiang2026lightvla}, and Compressor-VLA~\\cite{gao2025compressorvla}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.\n\n\\paragraph{Vision connectors.}\nLLaVA~\\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized. We provide the first cross-architecture analysis of how connector coupling and task complexity jointly govern VLA token compressibility.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_014X4uaudTRCzvS38Qych9jo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "130d5d02-6ece-4e69-bd22-ced086c9b8ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-28T18:26:59.436Z_

<details><summary>↩ Tool result · `toolu_014X4uaudTRCzvS38Qych9jo`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft} shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}
21	\label{fig:architecture}
22	\end{figure*}
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{VLA models evaluated. Coupling indicates independent vs.\ cross-token processing. $N$ = vision tokens input to the LLM. $^\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}
28	\label{tab:model_properties}
29	\begin{tabular}{lrlcrll}
30	\toprule
31	Model & Params & Connector & $N$ & CV & Coupling & Eval \\
32	\midrule
33	$\pi_{0.5}$ & 4B & Linear ($\times\!\sqrt{d}$) & 768 & 0.055 & Indep.\ & Closed-loop \\
34	X-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\
35	OpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\ & Closed-loop \\
36	SmolVLA & 450M & Pixel-shuffle $4{\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\
37	\midrule
38	$\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\ & Offline \\
39	OFT$^\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\ & Offline \\
40	\bottomrule
41	\end{tabular}
42	\end{table}
43	
44	\subsection{Pruning Protocol}
45	\label{sec:pruning_protocol}
46	
47	Given $N$ post-connector vision tokens $\{t_1, \ldots, t_N\}$ with $t_i \in \mathbb{R}^d$, token pruning selects a subset of size $\lfloor k \cdot N \rfloor$ for retention ratio $k \in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.
48	
49	\paragraph{Importance scoring functions.}
50	A scoring function $s\colon \mathbb{R}^d \to \mathbb{R}$ assigns each token an importance score; the top-$\lfloor kN \rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.
51	
52	\textbf{L2-norm scoring} assigns each token its activation magnitude:
53	\begin{equation}
54	s_{\text{L2}}(t_i) = \|t_i\|_2\,.
55	\label{eq:l2_score}
56	\end{equation}
57	The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\ref{sec:cv_sensitivity}).
58	
59	\textbf{Random subsampling} draws $\lfloor kN \rfloor$ tokens uniformly at random:
60	\begin{equation}
61	s_{\text{rand}}(t_i) \sim \mathcal{U}(0, 1)\,.
62	\label{eq:random_score}
63	\end{equation}
64	Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\ref{sec:exp_setup}).
65	
66	The \emph{importance margin} at ratio $k$ is defined as $\Delta(k) = \text{SR}_{\text{L2}}(k) - \text{SR}_{\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\ref{sec:cv_sensitivity}).
67	
68	\paragraph{Attention-based alternatives.}
69	Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\ref{sec:cv_diagnostic}), not as a pruning criterion.
70	
71	\paragraph{Retention ratio design space.}
72	We evaluate $k \in \{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\}$, spanning from extreme compression (retaining 30\% of tokens) to conservative trimming (retaining 95\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \in \{0.80, 0.925\}$) to localize the transition boundary (Section~\ref{sec:two_axis}).
73	
74	\subsection{Compressibility Diagnostic: Importance CV}
75	\label{sec:cv_diagnostic}
76	
77	We seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:
78	\begin{equation}
79	\text{CV} = \frac{\sigma\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}{\mu\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}
80	\label{eq:cv}
81	\end{equation}
82	where $\sigma$ and $\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.
83	
84	\paragraph{The CV spectrum.}
85	CV captures a continuous ordering across six models and three connector families:
86	\begin{equation}
87	\begin{split}
88	\underbrace{\pi_0\,(0.038) \;<\; \pi_{0.5}\,(0.055)}_{\text{linear proj.}} &\;<\; \underbrace{\text{X-VLA}\,(0.151)}_{\text{linear + BART}} \\
89	&\;<\; \underbrace{\text{OpenVLA}\,(0.215) \;\approx\; \text{OFT}\,(0.219)}_{\text{MLP proj.}} \;<\; \underbrace{\text{SmolVLA}\,(0.314)}_{\text{pixel-shuffle}}
90	\end{split}
91	\label{eq:cv_spectrum}
92	\end{equation}
93	This ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\,{<}\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\,{\approx}\,$0.22). Pixel-shuffle folds $4 \times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\,{=}\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\sim}$0.04) to 0.151.
94	
95	\paragraph{CV as pruning tolerance predictor.}
96	CV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.
97	
98	CV also predicts the \emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\Delta(\text{L2} - \text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\ref{sec:cv_sensitivity}).
99	
100	\paragraph{Complementary role of attention entropy.}
101	Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.
102	
103	\subsection{Vision Token Re-encoder (VTR)}
104	\label{sec:vtr}
105	
106	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.
107	
108	\paragraph{Architecture.}
109	VTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \in \{16, 32, 64, 96, 128\}$; $M{=}N$ serves as a passthrough control.
110	
111	\paragraph{Training and cost.}
112	The module adds ${\sim}$22M trainable parameters ($<$5\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\ref{app:smart_compress_details}.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "efdf1021-756d-41c6-825f-bfc106808a8c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01EnxU18cQKxwKzuJVRy1Wab`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "4c32e57b-af92-4009-a377-12e0b8a2a33e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-28T18:27:00.019Z_

<details><summary>↩ Tool result · `toolu_01EnxU18cQKxwKzuJVRy1Wab`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.
8	
9	\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\pi_{0.5}$~\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$, 128 tokens, CV$\,{=}\,$0.314). Two additional models ($\pi_{0}$~\cite{black2024pi0}, OFT~\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\ref{tab:model_properties} summarizes all six architectures.
10	
11	\paragraph{Protocol.} We prune at $k \in \{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\% confidence intervals.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
19	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
20	\label{fig:pruning_overview}
21	\end{figure}
22	
23	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
24	
25	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\geq}$98.0\% through $k{=}0.85$ (Appendix Table~\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\%, an 89\,pp method gap from identical removal fractions.
26	
27	\textbf{X-VLA (BART encoder, CV$\,{=}\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\,pp, yet the same model drops 27.4\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.
28	
29	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\ref{tab:full_results}; Section~\ref{sec:analysis}).
30	
31	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\leq}$6.6\% across all suites and methods, a catastrophic cliff detailed in Section~\ref{sec:pixel_shuffle}.
32	
33	\begin{table*}[t]
34	\centering
35	\small
36	\caption{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\leq}$6.6\% across all conditions. $\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\ref{tab:full_results}.}
37	\label{tab:main_results}
38	\begin{tabular}{llcccc}
39	\toprule
40	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
41	\midrule
42	\multirow{4}{*}{$\pi_{0.5}$}
43	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 33.4 / 69.4 \\
44	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\
45	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\
46	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\
47	\midrule
48	\multirow{4}{*}{X-VLA}
49	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\
50	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\
51	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\
52	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\
53	\midrule
54	\multirow{4}{*}{SmolVLA}
55	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
56	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
57	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
58	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
59	\bottomrule
60	\end{tabular}
61	\end{table*}
62	
63	\subsection{Pixel-Shuffle Entanglement}
64	\label{sec:pixel_shuffle}
65	
66	\begin{figure*}[t]
67	\centering
68	\begin{subfigure}[t]{0.495\textwidth}
69	\centering
70	\includegraphics[width=\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
71	\caption{}\label{fig:pixel_shuffle}
72	\end{subfigure}
73	\hfill
74	\begin{subfigure}[t]{0.495\textwidth}
75	\centering
76	\includegraphics[width=\linewidth]{figures/paper/fig_method_gap.pdf}
77	\caption{}\label{fig:method_gap}
78	\end{subfigure}
79	\caption{Token entanglement and scoring sensitivity. \textbf{(a)}~Pixel-shuffle $4{\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \textbf{(b)}~Method gap $|\text{SR(L2)} - \text{SR(Random)}|$ at $k{=}0.95$: $\pi_{0.5}$'s Object gap (24.2\,pp) exceeds X-VLA's maximum (1.4\,pp) by $17{\times}$ (single seed except $\pi_{0.5}$ Long, $n{=}5$).}
80	\label{fig:entanglement_scoring}
81	\end{figure*}
82	
83	SmolVLA's pixel-shuffle $4{\times}4$ folding concatenates 16 patches per token (Figure~\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\leq}$6.6\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.
84	
85	\subsection{Position Disruption vs.\ Information Loss}
86	\label{sec:zeromask}
87	
88	$\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\% on Object despite removing only 10\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\% SR while hard pruning collapses to 9.0\%. The 89\,pp gap is entirely attributable to position disruption: $\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.
89	
90	\subsection{Scoring Method Sensitivity and CV Diagnostic}
91	\label{sec:cv_sensitivity}
92	
93	CV predicts where scoring method choice becomes critical (Figure~\ref{fig:method_gap}). $\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\,pp, exceeding X-VLA's maximum (1.4\,pp) by $17{\times}$. At $k{=}0.5$, the importance margin on Object is $\Delta{=}{-}36.0$\,pp ($\pi_{0.5}$) and ${-}27.2$\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.
94	
95	\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\geq}$92.8\% while L2 falls 8--27\,pp below random; on $\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\,pp). On Long, attention cliffs $-$26.5\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\ref{fig:cliff_highlight}).
96	
97	\textbf{Cliff vs.\ graded degradation.} The divergent response patterns in the cliff zone ($k \in [0.85, 0.95]$) reflect a statistical distinction between the two scoring methods. Random removal samples a different token subset at each control step; in this interval, the probability of destroying at least one critical token combination transitions from low to near-certain, which produces a binary collapse. L2 scoring deterministically retains the same high-norm subset at every step. This determinism explains the 93\,pp gap at $k{=}0.85$ on Object (L2 98.0\% vs.\ random 5.0\%; Appendix Table~\ref{tab:full_results}).
98	
99	\textbf{Inverted-U importance margin.} The importance margin $\Delta$ on $\pi_{0.5}$ Long follows an inverted-U profile across retention ratios (Figure~\ref{fig:cliff_highlight}; Appendix Figure~\ref{fig:margin_profile}). The margin peaks at $k{=}0.9$ ($\Delta{=}+$46.9\,pp: L2 80.4\% vs.\ random 33.6\%), the retention ratio where importance-aware selection provides maximum value. Above this peak ($k{=}0.95$, $\Delta{=}+$25.6\,pp), both methods retain enough tokens for adequate performance and the advantage of targeted selection diminishes. Below it ($k{=}0.5$, $\Delta{\approx}+$1.3\,pp), both methods lose enough information that their strategies become equally inadequate. Near $k{\approx}0.7$, the ranking inverts: random surpasses L2 (64.6\% vs.\ 63.2\%; Appendix Table~\ref{tab:full_results}) because L2 concentrates retained tokens in a single high-activation region at the cost of the spatial coverage that multi-step tasks require. The V-shaped random recovery at lower $k$ arises from position aliasing under scattered removal (Section~\ref{sec:analysis}).
100	
101	\begin{figure}[t]
102	\centering
103	\includegraphics[width=0.75\linewidth]{figures/paper/fig_cliff_highlight.pdf}
104	\caption{Scoring method determines cliff behavior on $\pi_{0.5}$ Long (five-seed mean $\pm$ s.d.\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\,pp gap vs.\ L2) and recovery at $k{\leq}0.7$.}
105	\label{fig:cliff_highlight}
106	\end{figure}
107	
108	\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\ref{tab:full_results}): Object $\Delta{=}+$93\,pp $>$ Goal $+$35.2\,pp $>$ Long $+$33.2\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.
109	
110	\subsection{VTR Recovery}
111	\label{sec:vtr_recovery}
112	
113	VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA). At 75\% compression, VTR achieves 60.1 $\pm$ 1.3\% SR ($M{=}32$, 3 seeds; Table~\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\%) by 15.3\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\% ($p > 0.9$ vs.\ baseline; Appendix~\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\pm$ 2.6\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\%, Goal 56.4\%, both recovered from 0.0\% under hard pruning.
114	
115	\begin{table}[t]
116	\centering
117	\small
118	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\%; VTR achieves ${\geq}$57\% at up to 87.5\% compression, exceeding the unpruned baseline. Baseline (44.8\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\% (Table~\ref{tab:main_results}). See Appendix~\ref{app:smart_compress_details} for training details.}
119	\label{tab:vtr_main}
120	\begin{tabular}{lccr}
121	\toprule
122	Configuration & $M$ & Compress.\ & SR (\%) \\
123	\midrule
124	\textit{Baseline (unpruned)} & 128 & 0\% & 44.8 \\
125	\textit{Hard pruning (any)} & -- & 5--50\% & 0.0 \\
126	\midrule
127	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
128	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
129	MLP adapter & 32 & 75\% & 63.4 $\pm$ 2.6 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	\textbf{Efficiency.}\label{sec:efficiency} For $\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\sim}$16\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\% compression with ${\leq}$1.1\,pp below passthrough.
135	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ad87ba85-2966-4ef8-8054-868c9c7a7f2c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \\textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \\textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \\textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \\textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\\% confidence intervals.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Cliff vs.\\ graded degradation.} The divergent response patterns in the cliff zone ($k \\in [0.85, 0.95]$) reflect a statistical distinction between the two scoring methods. Random removal samples a different token subset at each control step; in this interval, the probability of destroying at least one critical token combination transitions from low to near-certain, which produces a binary collapse. L2 scoring deterministically retains the same high-norm subset at every step. This determinism explains the 93\\,pp gap at $k{=}0.85$ on Object (L2 98.0\\% vs.\\ random 5.0\\%; Appendix Table~\\ref{tab:full_results}).\n\n\\textbf{Inverted-U importance margin.} The importance margin $\\Delta$ on $\\pi_{0.5}$ Long follows an inverted-U profile across retention ratios (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}). The margin peaks at $k{=}0.9$ ($\\Delta{=}+$46.9\\,pp: L2 80.4\\% vs.\\ random 33.6\\%), the retention ratio where importance-aware selection provides maximum value. Above this peak ($k{=}0.95$, $\\Delta{=}+$25.6\\,pp), both methods retain enough tokens for adequate performance and the advantage of targeted selection diminishes. Below it ($k{=}0.5$, $\\Delta{\\approx}+$1.3\\,pp), both methods lose enough information that their strategies become equally inadequate. Near $k{\\approx}0.7$, the ranking inverts: random surpasses L2 (64.6\\% vs.\\ 63.2\\%; Appendix Table~\\ref{tab:full_results}) because L2 concentrates retained tokens in a single high-activation region at the cost of the spatial coverage that multi-step tasks require. The V-shaped random recovery at lower $k$ arises from position aliasing under scattered removal (Section~\\ref{sec:analysis}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}): Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\n",
      "numLines": 135,
      "startLine": 1,
      "totalLines": 135
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01M4LVHmBGbeRar9AXDpNFNx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "23af2660-c25b-41c5-bfd2-266660acbc56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-28T18:27:00.517Z_

<details><summary>↩ Tool result · `toolu_01M4LVHmBGbeRar9AXDpNFNx`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector---L2 leads on $\pi_{0.5}$ Object but inverts on Long; on X-VLA, attention recovers near-baseline while L2 is anti-informative (Appendix~\ref{app:extended_discussion}). The V-shaped random recovery on $\pi_{0.5}$ Long reflects position encoding sensitivity: scattered gaps maximally disrupt RoPE at $k{\approx}0.9$, recovering as surviving positions become approximately uniform.
6	
7	Connector architecture is the primary factor governing VLA token compressibility. Token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity (up to $20{\times}$ from Object to Goal at $k{=}0.9$). CV partitions models in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and $k$-dependent. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression. Real-robot validation and adaptive per-task pruning schedules remain open.
8	
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "8552d80f-0a11-4222-9767-52c7ee776fa1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:conclusion}\n\\label{sec:analysis}\n\nCV predicts connector-level compressibility, but task complexity determines \\emph{which} scoring method succeeds within a given connector---L2 leads on $\\pi_{0.5}$ Object but inverts on Long; on X-VLA, attention recovers near-baseline while L2 is anti-informative (Appendix~\\ref{app:extended_discussion}). The V-shaped random recovery on $\\pi_{0.5}$ Long reflects position encoding sensitivity: scattered gaps maximally disrupt RoPE at $k{\\approx}0.9$, recovering as surviving positions become approximately uniform.\n\nConnector architecture is the primary factor governing VLA token compressibility. Token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity (up to $20{\\times}$ from Object to Goal at $k{=}0.9$). CV partitions models in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and $k$-dependent. Where all deletion fails, VTR recovers over 60\\% SR at 75\\% compression. Real-robot validation and adaptive per-task pruning schedules remain open.\n\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_0158CXAPfWynj34nwU1itWiL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "96463449-86ca-4e1a-bff0-ea06ba0da08a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T18:27:00.993Z_

<details><summary>↩ Tool result · `toolu_0158CXAPfWynj34nwU1itWiL`</summary>

```text
1	\section{Limitations}
2	\label{sec:limitations}
3	
4	All evaluations use LIBERO simulation; no sim-to-real evidence is provided; real-robot evaluation with domain shift would strengthen practical applicability. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing full causal isolation of the connector effect; controlled studies varying only the connector within a fixed backbone would sharpen causal claims. The CV--SR correlation relies on four closed-loop models, too few for a general law; expanding the model pool as new VLA architectures emerge will test whether CV generalizes as a universal diagnostic. VTR is validated on SmolVLA only; extending to other entangling connectors (e.g., cross-attention encoders) would test generality of the re-encoding approach. Only L2-norm and random scoring are systematically compared; gradient-based importance scoring or learned pruning masks could yield better token selection. Most conditions use a single seed; $\pi_{0.5}$ Long uses five-seed means ($n{=}5$, s.d.\ ${\leq}$2.7\,pp); future work should adopt multi-seed evaluation across all conditions to quantify variance. \textbf{AI disclosure:} This work used AI tools (Claude) for code development and manuscript drafting; all scientific claims are the authors' own.
5	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "1aedc9fc-fab9-40ab-af96-fc7109ed4ebb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex",
      "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nAll evaluations use LIBERO simulation; no sim-to-real evidence is provided; real-robot evaluation with domain shift would strengthen practical applicability. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing full causal isolation of the connector effect; controlled studies varying only the connector within a fixed backbone would sharpen causal claims. The CV--SR correlation relies on four closed-loop models, too few for a general law; expanding the model pool as new VLA architectures emerge will test whether CV generalizes as a universal diagnostic. VTR is validated on SmolVLA only; extending to other entangling connectors (e.g., cross-attention encoders) would test generality of the re-encoding approach. Only L2-norm and random scoring are systematically compared; gradient-based importance scoring or learned pruning masks could yield better token selection. Most conditions use a single seed; $\\pi_{0.5}$ Long uses five-seed means ($n{=}5$, s.d.\\ ${\\leq}$2.7\\,pp); future work should adopt multi-seed evaluation across all conditions to quantify variance. \\textbf{AI disclosure:} This work used AI tools (Claude) for code development and manuscript drafting; all scientific claims are the authors' own.\n",
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

<details open><summary>🔧 Tool call — Read · `toolu_017GRY64X1SQYKc94eygrgc2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "558cb264-b5a6-4674-a737-366cf2628c6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T18:27:01.749Z_

<details><summary>↩ Tool result · reported error · `toolu_017GRY64X1SQYKc94eygrgc2`</summary>

```text
File content (26911 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "23381fd2-a9bc-4ff8-8c8c-5c8f42910d1f",
  "tool_use_result": "Error: File content (26911 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01KfudbERdri8sG5a2u6nL3M`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "97c738ba-bd4c-4b75-bd13-53bc34f091b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016LCeZLwTrBJhUWK8bgSerm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13838,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13838
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T18:27:02.451Z_

<details><summary>↩ Tool result · `toolu_01KfudbERdri8sG5a2u6nL3M`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "af3eb7d0-0591-4694-9f3c-539a60a3d4e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
````

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Let me read the appendix.tex in parts since it's too large.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "bda09692-33f8-4e2d-8c39-96e37248176a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4UcR7KhdzM16ZUmbr9oSw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17915,
      "cache_read_input_tokens": 25683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17915
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

_source line 23_

Let me read the appendix in parts and the main.tex to understand the structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "c4d7b713-1223-4a95-9e1f-1e813d8aba01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4UcR7KhdzM16ZUmbr9oSw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17915,
      "cache_read_input_tokens": 25683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17915
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

<details open><summary>🔧 Tool call — Read · `toolu_01WwQFsV3JHnFo3cT1tKDjgx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "c2ec4296-7d9f-4031-8932-578870e07f11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4UcR7KhdzM16ZUmbr9oSw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17915,
      "cache_read_input_tokens": 25683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17915
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

_source line 25 · 2026-05-28T18:27:09.556Z_

<details><summary>↩ Tool result · `toolu_01WwQFsV3JHnFo3cT1tKDjgx`</summary>

```text
1	\appendix
2	
3	\section{Full Pruning Results}
4	\label{app:full_results}
5	
6	Table~\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\ref{tab:main_results} for space.
7	
8	\begin{table*}[ht]
9	\centering
10	\footnotesize
11	\caption{Full closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
12	\label{tab:full_results}
13	\setlength{\tabcolsep}{4pt}
14	\begin{tabular}{llccccc}
15	\toprule
16	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
17	\midrule
18	\multirow{4}{*}{$\pi_{0.5}$}
19	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
20	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
21	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
22	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\
23	\midrule
24	\multirow{4}{*}{X-VLA}
25	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
26	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
27	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
28	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
29	\midrule
30	\multirow{4}{*}{OpenVLA}
31	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
32	& Goal    & \textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
33	& Spatial & \textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
34	& Long    & \textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\textsuperscript{$\dagger$} & -- / -- & -- / -- \\
35	\midrule
36	\multirow{4}{*}{SmolVLA}
37	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
38	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
39	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
40	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
41	\bottomrule
42	\end{tabular}
43	\end{table*}
44	
45	
46	\section{Extended Discussion}
47	\label{app:extended_discussion}
48	\label{app:discussion}
49	
50	\paragraph{Re-encoding and CV diagnostics.}
51	Both cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\,{=}\,$0.151) from $\pi_0$'s uniformly critical profile (CV$\,{=}\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\ref{app:cv_strategy_interaction},~\ref{app:cv_extended}).
52	
53	\paragraph{Task complexity compresses the importance margin.}
54	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector. OpenVLA illustrates the full pattern across LIBERO's complexity gradient (Figure~\ref{fig:openvla_sweep}).
55	
56	On single-step Object, L2 leads at moderate pruning ($+$7.8\,pp at $k{=}0.9$), but the three methods exhibit staggered cliffs---L2 earliest ($k{=}0.9{\to}0.85$, $-$15.4\,pp), random next, attention latest---each defining a distinct effective compression window before converging at $k{=}0.5$ ($<$4.8\,pp spread). As task complexity increases, the scoring hierarchy inverts. On Goal, random pruning at $k{=}0.9$ \emph{exceeds} the unpruned baseline ($+$4.8\,pp; cross-seed confirmed), suggesting OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization. On Long, the inversion is complete: at $k{=}0.7$, Random (38.8\%) $>$ L2 (31.2\%) $>$ Attention (24.0\%), with attention degrading $2.5{\times}$ faster than random. The mechanism is consistent: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles; L2 and attention both cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires.
57	
58	\begin{figure}[ht]
59	\centering
60	\includegraphics[width=\linewidth]{figures/paper/fig_openvla_sweep.pdf}
61	\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}
62	\label{fig:openvla_sweep}
63	\end{figure}
64	
65	This is a concrete manifestation of the two-axis framework (Section~\ref{sec:two_axis}): Axis~1 (connector architecture) determines \emph{whether} pruning is viable; Axis~2 (task complexity) determines \emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.
66	
67	\paragraph{Position encoding mediates the V-shape recovery.}
68	The monotonic L2 curve versus the non-monotonic random curve on $\pi_{0.5}$ Long (Figure~\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\% $\to$ 51.7\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 33.6\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\% at $k{=}0.7$ to 12\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\%---exceeding the $k{=}0.9$ level by ${\sim}2{\times}$. The zero-mask ablation (Section~\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\% SR, while physically removing the same tokens collapses to 9.0\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.
69	
70	\paragraph{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$33.2\,pp for L2) masks extreme per-task heterogeneity (per-task $\sigma{=}$21.5\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\% while random achieves 52\% ($-$44\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.
71	
72	\begin{figure}[ht]
73	\centering
74	\includegraphics[width=0.85\linewidth]{figures/paper/fig_scoring_crossover.pdf}
75	\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\Delta{<}3.5$\,pp). $\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\% regardless of method. Compact 2$\times$2 summary in Appendix Table~\ref{tab:scoring_crossover_summary}.}
76	\label{fig:scoring_crossover}
77	\end{figure}
78	
79	\begin{figure}[ht]
80	\centering
81	\includegraphics[width=0.85\linewidth]{figures/paper/fig_margin_profile.pdf}
82	\caption{Importance margin (L2 $-$ Random SR) on $\pi_{0.5}$ Long across retention ratios (multi-seed mean $\pm$ s.d.; $n{=}5$). The margin peaks sharply at $k{=}0.9$ (46.9\,pp) where random pruning is maximally destructive, then declines asymmetrically: one step above the peak ($k{=}0.95$: 25.6\,pp) versus four steps below before crossing zero at $k{\approx}0.71$. At $k{=}0.5$, L2 and Random converge ($|\Delta|{\approx}1.3$\,pp), indicating that scoring method choice matters only in the moderate-pruning window.}
83	\label{fig:margin_profile}
84	\end{figure}
85	
86	\paragraph{Limitations (extended).}
87	All closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\% official, 44.8\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.
88	
89	\paragraph{Non-monotonicity as structural property.}
90	X-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\% (L2) and 54.0\% (random), while $k{=}0.9$ recovers to 70.2\% under L2 selection (Table~\ref{tab:main_results}). The 0.2\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.
91	
92	\paragraph{$\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}
93	Random selection on $\pi_{0.5}$ Object collapses from 74.0\% at $k{=}0.95$ to 9.0\% at $k{=}0.9$, then recovers to 74.0\% at $k{=}0.7$ (Table~\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\%, Object~65.0\%, Goal~60.4\%), but Long drops to 35.0\%, below its $k{=}0.5$ performance of 61.6\% (Table~\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\pi_{0.5}$ Object drops to 5.6\% at $k{=}0.85$ versus 69.4\% at $k{=}0.5$ ($-$63.8\,pp), more than double X-VLA Long's $-$26.6\,pp. The V-shaped recovery at $k \leq 0.7$ remains unexplained.
94	
95	\begin{table}[ht]
96	\centering
97	\small
98	\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\ $\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\%) but drops to 35.0\% on Long (below $k{=}0.5$); $\pi_{0.5}$ exhibits a severe disruption peak on Object.}
99	\label{tab:xvla_k085_crosssuite}
100	\begin{tabular}{lcccc}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "d5db7119-18b9-431e-86e8-55ffe0a83529",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{Full Pruning Results}\n\\label{app:full_results}\n\nTable~\\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\\ref{tab:main_results} for space.\n\n\\begin{table*}[ht]\n\\centering\n\\footnotesize\n\\caption{Full closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \\textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \\textsuperscript{$\\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}\n\\label{tab:full_results}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{OpenVLA}\n& Object  & \\textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\\textsuperscript{$\\dagger$} & -- / -- & 39.2 / 35.8 \\\\\n& Goal    & \\textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Spatial & \\textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Long    & \\textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Extended Discussion}\n\\label{app:extended_discussion}\n\\label{app:discussion}\n\n\\paragraph{Re-encoding and CV diagnostics.}\nBoth cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \\approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\\,{=}\\,$0.151) from $\\pi_0$'s uniformly critical profile (CV$\\,{=}\\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\\ref{app:cv_strategy_interaction},~\\ref{app:cv_extended}).\n\n\\paragraph{Task complexity compresses the importance margin.}\nCV predicts connector-level compressibility, but task complexity determines \\emph{which} scoring method succeeds within a given connector. OpenVLA illustrates the full pattern across LIBERO's complexity gradient (Figure~\\ref{fig:openvla_sweep}).\n\nOn single-step Object, L2 leads at moderate pruning ($+$7.8\\,pp at $k{=}0.9$), but the three methods exhibit staggered cliffs---L2 earliest ($k{=}0.9{\\to}0.85$, $-$15.4\\,pp), random next, attention latest---each defining a distinct effective compression window before converging at $k{=}0.5$ ($<$4.8\\,pp spread). As task complexity increases, the scoring hierarchy inverts. On Goal, random pruning at $k{=}0.9$ \\emph{exceeds} the unpruned baseline ($+$4.8\\,pp; cross-seed confirmed), suggesting OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization. On Long, the inversion is complete: at $k{=}0.7$, Random (38.8\\%) $>$ L2 (31.2\\%) $>$ Attention (24.0\\%), with attention degrading $2.5{\\times}$ faster than random. The mechanism is consistent: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles; L2 and attention both cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_openvla_sweep.pdf}\n\\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}\n\\label{fig:openvla_sweep}\n\\end{figure}\n\nThis is a concrete manifestation of the two-axis framework (Section~\\ref{sec:two_axis}): Axis~1 (connector architecture) determines \\emph{whether} pruning is viable; Axis~2 (task complexity) determines \\emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.\n\n\\paragraph{Position encoding mediates the V-shape recovery.}\nThe monotonic L2 curve versus the non-monotonic random curve on $\\pi_{0.5}$ Long (Figure~\\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\\% $\\to$ 51.7\\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 33.6\\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\\% at $k{=}0.7$ to 12\\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\\%---exceeding the $k{=}0.9$ level by ${\\sim}2{\\times}$. The zero-mask ablation (Section~\\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\\% SR, while physically removing the same tokens collapses to 9.0\\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.\n\n\\paragraph{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$33.2\\,pp for L2) masks extreme per-task heterogeneity (per-task $\\sigma{=}$21.5\\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \\emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\\% while random achieves 52\\% ($-$44\\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_scoring_crossover.pdf}\n\\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\\Delta{<}3.5$\\,pp). $\\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\\% regardless of method. Compact 2$\\times$2 summary in Appendix Table~\\ref{tab:scoring_crossover_summary}.}\n\\label{fig:scoring_crossover}\n\\end{figure}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_margin_profile.pdf}\n\\caption{Importance margin (L2 $-$ Random SR) on $\\pi_{0.5}$ Long across retention ratios (multi-seed mean $\\pm$ s.d.; $n{=}5$). The margin peaks sharply at $k{=}0.9$ (46.9\\,pp) where random pruning is maximally destructive, then declines asymmetrically: one step above the peak ($k{=}0.95$: 25.6\\,pp) versus four steps below before crossing zero at $k{\\approx}0.71$. At $k{=}0.5$, L2 and Random converge ($|\\Delta|{\\approx}1.3$\\,pp), indicating that scoring method choice matters only in the moderate-pruning window.}\n\\label{fig:margin_profile}\n\\end{figure}\n\n\\paragraph{Limitations (extended).}\nAll closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\\% official, 44.8\\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.\n\n\\paragraph{Non-monotonicity as structural property.}\nX-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\\% (L2) and 54.0\\% (random), while $k{=}0.9$ recovers to 70.2\\% under L2 selection (Table~\\ref{tab:main_results}). The 0.2\\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.\n\n\\paragraph{$\\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}\nRandom selection on $\\pi_{0.5}$ Object collapses from 74.0\\% at $k{=}0.95$ to 9.0\\% at $k{=}0.9$, then recovers to 74.0\\% at $k{=}0.7$ (Table~\\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\\%, Object~65.0\\%, Goal~60.4\\%), but Long drops to 35.0\\%, below its $k{=}0.5$ performance of 61.6\\% (Table~\\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\\pi_{0.5}$ Object drops to 5.6\\% at $k{=}0.85$ versus 69.4\\% at $k{=}0.5$ ($-$63.8\\,pp), more than double X-VLA Long's $-$26.6\\,pp. The V-shaped recovery at $k \\leq 0.7$ remains unexplained.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\\ $\\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\\%) but drops to 35.0\\% on Long (below $k{=}0.5$); $\\pi_{0.5}$ exhibits a severe disruption peak on Object.}\n\\label{tab:xvla_k085_crosssuite}\n\\begin{tabular}{lcccc}",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 921
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_013wcoFzWAzUtyVwhvFZZf2E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "8a99bbc9-c7f0-4ff3-b7a1-7af1ed9cee06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4UcR7KhdzM16ZUmbr9oSw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17915,
      "cache_read_input_tokens": 25683,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17915
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

_source line 27 · 2026-05-28T18:27:10.282Z_

<details><summary>↩ Tool result · `toolu_013wcoFzWAzUtyVwhvFZZf2E`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	\usepackage{wrapfig}
13	
14	% Tighten float spacing for page limit
15	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{8pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{0pt}
20	
21	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{abstract}
27	
28	\keywords{vision-language-action models, token pruning, robot learning}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	\input{experiments}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\input{appendix}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "55521879-f38d-4feb-94a8-63615c68551c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.\n% \\usepackage[final]{corl_2026} % Uncomment for camera-ready.\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{wrapfig}\n\n% Tighten float spacing for page limit\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\n\\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\\\Vision Connectors and VLA Token Compressibility}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\keywords{vision-language-action models, token pruning, robot learning}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile the paper first to see the current page count, and then plan the slimming strategy.

Let me also read the abstract.tex and check current figure placements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "890b5bb5-5b7b-4e45-a618-56b65e73395f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rHsYp2KUbDvndcXRe7j7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5533,
      "cache_read_input_tokens": 43598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5533
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

_source line 29_

Let me compile the paper first to see the exact current page count, and read the abstract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "416867d9-9531-499a-aba3-a033eacb4768",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rHsYp2KUbDvndcXRe7j7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5533,
      "cache_read_input_tokens": 43598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5533
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

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01UWyRLvEefJT6DsbwAekqj4`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && rm -f main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out main.pdf && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -15",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "acc4e791-884f-4c6c-a78d-b648139ca7b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rHsYp2KUbDvndcXRe7j7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5533,
      "cache_read_input_tokens": 43598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5533
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

<details open><summary>🔧 Tool call — Read · `toolu_01H5bvtj2kXJECDRcoG7pVbC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "c00c8dd0-c21f-4e6e-919e-1d7b0984e0b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rHsYp2KUbDvndcXRe7j7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5533,
      "cache_read_input_tokens": 43598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5533
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

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bn1djbhwt",
  "tool_use_id": "toolu_01UWyRLvEefJT6DsbwAekqj4",
  "description": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && rm -f main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out main.pdf && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -15",
  "task_type": "local_bash",
  "uuid": "10c5c617-2021-433f-81bb-3d88ac4ff670",
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f"
}
```

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bn1djbhwt",
  "tool_use_id": "toolu_01UWyRLvEefJT6DsbwAekqj4",
  "status": "completed",
  "output_file": "",
  "summary": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper && rm -f main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out main.pdf && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -15",
  "uuid": "7503b246-5743-4735-a726-a243fb647f76",
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f"
}
```

---

### Tool result

_source line 34 · 2026-05-28T18:27:21.641Z_

<details><summary>↩ Tool result · `toolu_01UWyRLvEefJT6DsbwAekqj4`</summary>

```text
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (33 pages, 1304061 bytes).
Transcript written on main.log.
Latexmk: Getting log file 'main.log'
Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ec8ba5f2-915c-422f-8d17-3e60dee1daa9",
  "tool_use_result": {
    "stdout": "sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (33 pages, 1304061 bytes).\nTranscript written on main.log.\nLatexmk: Getting log file 'main.log'\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-28T18:27:21.647Z_

<details><summary>↩ Tool result · `toolu_01H5bvtj2kXJECDRcoG7pVbC`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across six VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. No scoring method is universally safe: task complexity amplifies connector-dependent patterns (up to $20{\times}$ from Object to Goal at $k{=}0.9$). A zero-mask ablation isolates the mechanism: zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion fails, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
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
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "19712ab3-7338-47e5-886a-d09a1389f8e3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nVision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\\pi_{0.5}$ preserves 98\\% task success while SmolVLA collapses to 0\\%---why?\n\nWe identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\\,{=}\\,$0.038 (near-immune linear projection) to CV$\\,{=}\\,$0.314 (catastrophic pixel-shuffle collapse). Across six VLA architectures (450\\,M--7\\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.\n\nImportance-based selection is not universally beneficial---it can be actively harmful. L2 norm selection preserves 98\\% success on $\\pi_{0.5}$ where random yields 5\\% (93\\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\\,pp. No scoring method is universally safe: task complexity amplifies connector-dependent patterns (up to $20{\\times}$ from Object to Goal at $k{=}0.9$). A zero-mask ablation isolates the mechanism: zeroing 10\\% of tokens preserves 98.0\\% SR while physical removal collapses to 9.0\\%---the 89\\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion fails, a lightweight re-encoding module (${\\sim}$5\\% extra parameters) recovers $>$60\\% success at 75\\% compression.\n\\end{abstract}\n",
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01KAPvN7rJvp2HRZPvsW7rka`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\nfor i, p in enumerate(pages):\n    lines = p.strip().split('\\n')\n    first = next((l.strip() for l in lines if l.strip()), '')\n    if 'References' == first or first.startswith('[1]'):\n        print(f'References start at page {i+1}')\n        print(f'Body pages: {i}')\n        break\n    # Also check for bibliography header\n    if 'references' in first.lower():\n        print(f'References start at page {i+1} (header: {first})')\n        print(f'Body pages: {i}')\n        break\nprint(f'Total pages: {len(pages)-1}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "36266217-b6c1-402d-85e6-f7f17767ed08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XyfC6SmbGWMAede64u9qRj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 49131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
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

_source line 37 · 2026-05-28T18:27:28.507Z_

<details><summary>↩ Tool result · `toolu_01KAPvN7rJvp2HRZPvsW7rka`</summary>

```text
Total pages: 33
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "62ec3a97-0c06-4352-8a31-485ca92c3bb3",
  "tool_use_result": {
    "stdout": "Total pages: 33",
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01EuyJrZZgfWDXtGKevyj12R`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\nfor i, p in enumerate(pages):\n    lines = p.strip().split('\\n')\n    # Print first non-empty line of each page\n    first = next((l.strip() for l in lines if l.strip()), '')\n    print(f'Page {i+1}: {first[:80]}')\n\" 2>&1 | head -20\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "e8f829b5-b30e-403a-a810-ef417bfcbec8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QghRGyABw1r4N4tCawFsK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 293,
      "cache_read_input_tokens": 50279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 293
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

_source line 39 · 2026-05-28T18:27:34.322Z_

<details><summary>↩ Tool result · `toolu_01EuyJrZZgfWDXtGKevyj12R`</summary>

```text
Page 1: Why Token Pruning Crashes Some Robot Policies but
Page 2: Figure 1: Overview of VLA token compressibility. (a) The same robot observation 
Page 3: Figure 2: Vision connector architectures across four closed-loop VLAs, ordered b
Page 4: Table 1: VLA models evaluated. Coupling indicates independent vs. cross-token pr
Page 5: 121   connections) to approximate cumulative information flow from input tokens 
Page 6: 162   a uniform signal, where the spatial pattern of removal matters more than w
Page 7: 100                                    π0.5 (CV=0.055, L2)
Page 8: Table 2: Closed-loop success rates (%) on LIBERO under L2 norm (L2) and random (
Page 9: π0.5 Long — Scoring Method Determines Cliff Behavior
Page 10: Table 3: VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all 
Page 11: 314    [3] Y. Liang, C. Ge, Z. Tong, Y. Song, J. Wang, and P. Xie. Not all patch
Page 12: 357   [19] W. Shi, J. Caballero, F. Huszar, J. Totz, A. P. Aitken, R. Bishop, D.
Page 13: Table 4: Full closed-loop success rates (%) on LIBERO under L2 norm (L2) and ran
Page 14: OpenVLA — Suite-Dependent Method Crossover
Page 15: Success Rate (%) at k = 0.9
Page 16: π0.5 Long — Importance Margin Profile
Page 17: 490   D    Pruning Protocol Details
Page 18: 517   F     Per-Task Breakdown Tables
Page 19: Table 9: OpenVLA per-task success rates (%) on LIBERO-Object under random token 
Page 20: Table 11: π0.5 LIBERO-Long success rates (%) across five seeds (500 episodes eac
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "41eb252f-73aa-42e7-a579-047a7d0519b8",
  "tool_use_result": {
    "stdout": "Page 1: Why Token Pruning Crashes Some Robot Policies but\nPage 2: Figure 1: Overview of VLA token compressibility. (a) The same robot observation \nPage 3: Figure 2: Vision connector architectures across four closed-loop VLAs, ordered b\nPage 4: Table 1: VLA models evaluated. Coupling indicates independent vs. cross-token pr\nPage 5: 121   connections) to approximate cumulative information flow from input tokens \nPage 6: 162   a uniform signal, where the spatial pattern of removal matters more than w\nPage 7: 100                                    π0.5 (CV=0.055, L2)\nPage 8: Table 2: Closed-loop success rates (%) on LIBERO under L2 norm (L2) and random (\nPage 9: π0.5 Long — Scoring Method Determines Cliff Behavior\nPage 10: Table 3: VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all \nPage 11: 314    [3] Y. Liang, C. Ge, Z. Tong, Y. Song, J. Wang, and P. Xie. Not all patch\nPage 12: 357   [19] W. Shi, J. Caballero, F. Huszar, J. Totz, A. P. Aitken, R. Bishop, D.\nPage 13: Table 4: Full closed-loop success rates (%) on LIBERO under L2 norm (L2) and ran\nPage 14: OpenVLA — Suite-Dependent Method Crossover\nPage 15: Success Rate (%) at k = 0.9\nPage 16: π0.5 Long — Importance Margin Profile\nPage 17: 490   D    Pruning Protocol Details\nPage 18: 517   F     Per-Task Breakdown Tables\nPage 19: Table 9: OpenVLA per-task success rates (%) on LIBERO-Object under random token \nPage 20: Table 11: π0.5 LIBERO-Long success rates (%) across five seeds (500 episodes eac",
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

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
So the body pages are 10 (pages 1-10), with references starting at page 11. I need to cut it to 8 pages. Let me check more carefully.

Looking at the page structure:
- Page 1: Title + Abstract + beginning of Introduction
- Page 2: Figure 1 (teaser) 
- Page 3: Figure 2 (architecture) + method start
- Page 4: Table 1 + method continues
- Page 5-6: Method continues (scoring functions, pruning protocol, CV diagnostic)


- Page 7: Figure 3 (pruning overview)
- Page 8: Table 2 (main results) + experiments
- Page 9: Figure (cliff highlight)
- Page 10: Table 3 (VTR) + conclusion + limitations

So I need to cut 2 full pages. The method section is quite dense, especially the importance scoring functions part with all the variants. The attention-based alternatives paragraph is particularly long and could be trimmed significantly without losing the core contribution.

The experiments section also has a lot of granular analysis in the sensitivity and diagnostic parts that could be condensed. The retention ratio design space discussion is verbose and could be shortened. Some of the longer paragraphs about attention entropy and CV as a predictor could move to the appendix with just a brief mention in the main text.

My strategy is to move the attention alternatives and some of the detailed design space analysis to the appendix, compress the sensitivity analysis section, and trim the longer explanatory paragraphs while keeping the essential findings.

Let me start working through the files and making these edits systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "b3d4c5ce-42c5-4565-9b2e-c7c3438b10bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TsYN58xDP4Nw3GRNS5PDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 50572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 41_

Current body is 10 pages (references start page 11). Need to cut 2 pages. Let me first read the appendix structure to know where to place moved content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "14dfb060-9765-41cd-bc19-ca05f7c26f21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TsYN58xDP4Nw3GRNS5PDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 50572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01YSuq3Sx6xDeZSxuax3oFvy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": 100,
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "c5db7d3c-0c6e-427b-b8fb-7c04541a1d94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011TsYN58xDP4Nw3GRNS5PDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 50572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 43 · 2026-05-28T18:27:56.045Z_

<details><summary>↩ Tool result · `toolu_01YSuq3Sx6xDeZSxuax3oFvy`</summary>

```text
100	\begin{tabular}{lcccc}
101	\toprule
102	Suite & X-VLA SR (\%) & $\Delta$ & $\pi_{0.5}$ SR (\%) & $\Delta$ \\
103	\midrule
104	Object & 65.0 & $-$34.2 & 3.6--5.6\textsuperscript{$\dagger$} & $-$93 to $-$95 \\
105	Goal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\
106	Spatial & 68.2 & $-$24.8 & --- & --- \\
107	Long & 35.0 & $-$59.0 & --- & --- \\
108	\bottomrule
109	\multicolumn{5}{l}{\footnotesize\textsuperscript{$\dagger$}Two seeds: seed42$\,{=}\,$5.6\% (post-fix), seed43$\,{=}\,$3.6\%. $\Delta$ from respective baselines.}
110	\end{tabular}
111	\end{table}
112	
113	\paragraph{Small-$N$ interactions.}
114	X-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\,pp on Goal and $-$47.0\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.
115	
116	\paragraph{Design implications.}
117	Practitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.
118	
119	
120	\section{Cross-Suite Task Complexity Analysis}
121	\label{app:cross_suite_extended}
122	
123	LIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.
124	
125	$\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\% (matching the baseline), Spatial retains 97.8\% (within noise of the 97.2\% baseline), and Goal drops to 89.4\% ($-$7.0\,pp from 96.4\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\% token removal.
126	
127	X-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 97.6\% ($-$1.6\,pp from the 99.2\% baseline), while Goal drops to 70.2\% ($-$28.2\,pp from 98.4\% baseline). Under random pruning at the same ratio, Object loses just 1.4\,pp (97.8\%) while Goal loses 27.8\,pp (70.6\%), a $20{\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\% to 47.0\% (L2) and 48.2\% (random), a 47.0\,pp loss with only 1.2\,pp method gap, while Object at the same ratio loses only 0.2\,pp.
128	
129	Token-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.
130	
131	
132	\section{Pruning Protocol Details}
133	\label{app:pruning_details}
134	
135	Both pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.
136	
137	Model-specific retention ratios reflect each architecture's token count and expected sensitivity. $\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\pi_{0.5}$ uses $k \in \{0.3, 0.5, 0.7\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \in \{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \in \{0.3, 0.5, 0.7, 0.9, 0.95\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\cite{bolya2023tome}).
138	
139	The $\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\ three-layer MLP), backbone (PaliGemma vs.\ Llama-2), and encoder fusion strategy (single SigLIP vs.\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.
140	
141	
142	\section{SmolVLA Pruning Ablation}
143	\label{app:smolvla_ablation}
144	
145	\begin{table}[ht]
146	\centering
147	\small
148	\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\% SR. Two independent evaluations of the official HF checkpoint (59.2\% and 57.2\% baseline, within CI) confirm the cliff-edge across scoring methods.}
149	\label{tab:smolvla_ablation}
150	\begin{tabular}{llccrr}
151	\toprule
152	Scoring & $k$ & Mechanism & SR (\%) & Episodes & Wilson 95\% CI \\
153	\midrule
154	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\
155	\midrule
156	ACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
157	ACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
158	ACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
159	Random & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
160	Random & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\
161	ACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\
162	ACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\
163	\midrule
164	\multicolumn{6}{l}{\textit{Official checkpoint, eval protocol A (59.2\% baseline)}} \\
165	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\
166	Random & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
167	\midrule
168	\multicolumn{6}{l}{\textit{Official checkpoint, eval protocol B (57.2\% baseline)}} \\
169	\multicolumn{2}{l}{\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\
170	Random & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\
171	L2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\
172	L2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\
173	\bottomrule
174	\end{tabular}
175	\end{table}
176	
177	
178	\section{Per-Task Breakdown Tables}
179	\label{app:per_task}
180	
181	\subsection{SmolVLA Baseline Per-Task Results}
182	
183	Table~\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\ref{tab:smolvla_ablation}) produce 0\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\% already reported.
184	
185	\begin{table}[ht]
186	\centering
187	\small
188	\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\%.}
189	\label{tab:smolvla_baseline_pertask}
190	\begin{tabular}{lc}
191	\toprule
192	Task & SR (\%) \\
193	\midrule
194	alphabet\_soup & 22 \\
195	bbq\_sauce & 60 \\
196	butter & 42 \\
197	chocolate\_pudding & 38 \\
198	cream\_cheese & 58 \\
199	ketchup & 26 \\
200	milk & 62 \\
201	orange\_juice & 38 \\
202	salad\_dressing & 50 \\
203	tomato\_sauce & 52 \\
204	\midrule
205	\textbf{Overall} & \textbf{44.8} \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	\subsection{Official SmolVLA Checkpoint Per-Task Results}
211	
212	Table~\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\_libero). Under 50\% random token removal, all tasks produce 0\% SR, identical to the fine-tuned checkpoint results.
213	
214	\begin{table}[ht]
215	\centering
216	\small
217	\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\%. Under 50\% random pruning, all tasks collapse to 0\%. An independent evaluation (protocol B) yields 57.2\% baseline with identical cliff-edge (Table~\ref{tab:smolvla_ablation}).}
218	\label{tab:smolvla_official_pertask}
219	\begin{tabular}{lcc}
220	\toprule
221	Task & Baseline SR (\%) & $k{=}0.5$ SR (\%) \\
222	\midrule
223	alphabet\_soup & 64 & 0 \\
224	bbq\_sauce & 38 & 0 \\
225	butter & 78 & 0 \\
226	chocolate\_pudding & 90 & 0 \\
227	cream\_cheese & 40 & 0 \\
228	ketchup & 60 & 0 \\
229	milk & 52 & 0 \\
230	orange\_juice & 80 & 0 \\
231	salad\_dressing & 44 & 0 \\
232	tomato\_sauce & 46 & 0 \\
233	\midrule
234	\textbf{Overall} & \textbf{59.2} & \textbf{0.0} \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
239	\subsection{OpenVLA Per-Task Results Under Pruning}
240	
241	\begin{table}[ht]
242	\centering
243	\small
244	\caption{OpenVLA per-task success rates (\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\%. Tasks requiring fine-grained discrimination (butter, cream\_cheese) degrade earliest; visually distinctive targets (orange\_juice, salad\_dressing) are most resilient.}
245	\label{tab:openvla_pertask}
246	\begin{tabular}{lccccc}
247	\toprule
248	Task & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\
249	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "b1271ef1-7ef0-4ea7-9e9d-9b502f196def",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
      "content": "\\begin{tabular}{lcccc}\n\\toprule\nSuite & X-VLA SR (\\%) & $\\Delta$ & $\\pi_{0.5}$ SR (\\%) & $\\Delta$ \\\\\n\\midrule\nObject & 65.0 & $-$34.2 & 3.6--5.6\\textsuperscript{$\\dagger$} & $-$93 to $-$95 \\\\\nGoal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\\\\nSpatial & 68.2 & $-$24.8 & --- & --- \\\\\nLong & 35.0 & $-$59.0 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize\\textsuperscript{$\\dagger$}Two seeds: seed42$\\,{=}\\,$5.6\\% (post-fix), seed43$\\,{=}\\,$3.6\\%. $\\Delta$ from respective baselines.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Small-$N$ interactions.}\nX-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\\,pp on Goal and $-$47.0\\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.\n\n\\paragraph{Design implications.}\nPractitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.\n\n\n\\section{Cross-Suite Task Complexity Analysis}\n\\label{app:cross_suite_extended}\n\nLIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.\n\n$\\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\\% (matching the baseline), Spatial retains 97.8\\% (within noise of the 97.2\\% baseline), and Goal drops to 89.4\\% ($-$7.0\\,pp from 96.4\\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\\% token removal.\n\nX-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 97.6\\% ($-$1.6\\,pp from the 99.2\\% baseline), while Goal drops to 70.2\\% ($-$28.2\\,pp from 98.4\\% baseline). Under random pruning at the same ratio, Object loses just 1.4\\,pp (97.8\\%) while Goal loses 27.8\\,pp (70.6\\%), a $20{\\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\\% to 47.0\\% (L2) and 48.2\\% (random), a 47.0\\,pp loss with only 1.2\\,pp method gap, while Object at the same ratio loses only 0.2\\,pp.\n\nToken-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.\n\n\n\\section{Pruning Protocol Details}\n\\label{app:pruning_details}\n\nBoth pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\\pi_{0.5}$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\\ three-layer MLP), backbone (PaliGemma vs.\\ Llama-2), and encoder fusion strategy (single SigLIP vs.\\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.\n\n\n\\section{SmolVLA Pruning Ablation}\n\\label{app:smolvla_ablation}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\\% SR. Two independent evaluations of the official HF checkpoint (59.2\\% and 57.2\\% baseline, within CI) confirm the cliff-edge across scoring methods.}\n\\label{tab:smolvla_ablation}\n\\begin{tabular}{llccrr}\n\\toprule\nScoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\\\\n\\midrule\nACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\\\\nACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol A (59.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\\\\nRandom & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol B (57.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\\\\nRandom & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task Breakdown Tables}\n\\label{app:per_task}\n\n\\subsection{SmolVLA Baseline Per-Task Results}\n\nTable~\\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\\ref{tab:smolvla_ablation}) produce 0\\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\\% already reported.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\\%.}\n\\label{tab:smolvla_baseline_pertask}\n\\begin{tabular}{lc}\n\\toprule\nTask & SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 22 \\\\\nbbq\\_sauce & 60 \\\\\nbutter & 42 \\\\\nchocolate\\_pudding & 38 \\\\\ncream\\_cheese & 58 \\\\\nketchup & 26 \\\\\nmilk & 62 \\\\\norange\\_juice & 38 \\\\\nsalad\\_dressing & 50 \\\\\ntomato\\_sauce & 52 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{44.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Official SmolVLA Checkpoint Per-Task Results}\n\nTable~\\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\\_libero). Under 50\\% random token removal, all tasks produce 0\\% SR, identical to the fine-tuned checkpoint results.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\\%. Under 50\\% random pruning, all tasks collapse to 0\\%. An independent evaluation (protocol B) yields 57.2\\% baseline with identical cliff-edge (Table~\\ref{tab:smolvla_ablation}).}\n\\label{tab:smolvla_official_pertask}\n\\begin{tabular}{lcc}\n\\toprule\nTask & Baseline SR (\\%) & $k{=}0.5$ SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 64 & 0 \\\\\nbbq\\_sauce & 38 & 0 \\\\\nbutter & 78 & 0 \\\\\nchocolate\\_pudding & 90 & 0 \\\\\ncream\\_cheese & 40 & 0 \\\\\nketchup & 60 & 0 \\\\\nmilk & 52 & 0 \\\\\norange\\_juice & 80 & 0 \\\\\nsalad\\_dressing & 44 & 0 \\\\\ntomato\\_sauce & 46 & 0 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{59.2} & \\textbf{0.0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Per-Task Results Under Pruning}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA per-task success rates (\\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\\%. Tasks requiring fine-grained discrimination (butter, cream\\_cheese) degrade earliest; visually distinctive targets (orange\\_juice, salad\\_dressing) are most resilient.}\n\\label{tab:openvla_pertask}\n\\begin{tabular}{lccccc}\n\\toprule\nTask & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\\\\n\\midrule",
      "numLines": 150,
      "startLine": 100,
      "totalLines": 921
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the appendix to understand the full structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "7eff1044-d437-4039-875b-aa4776a214ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKtBW2exthGkJjJ6WCefq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4693,
      "cache_read_input_tokens": 51292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4693
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 45_

Now I have a clear picture. Body = 10 pages, need to cut to 8. Let me execute a comprehensive slimming plan. I'll work on the biggest savings first.

**Strategy:**
1. Move attention-based alternatives paragraph to appendix (~0.3 page)
2. Move retention ratio design space details to appendix (~0.3 page)  
3. Move attention entropy paragraph to appendix (~0.3 page)
4. Compress scoring function descriptions (~0.2 page)
5. Compress experiments detailed analysis (~0.3 page)
6. Fix Eq. 4 to be more compact (~0.1 page)
7. Fix figure placements
8. Tighten LaTeX spacing as needed

Let me start with the major cuts to method.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "6f2f44d4-3c78-4bec-a9a8-a0497abe3e7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKtBW2exthGkJjJ6WCefq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4693,
      "cache_read_input_tokens": 51292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4693
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_015ePfvERLqhz41M34tdjne7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).",
  "new_string": "\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ec262119-4161-4c4f-9bf9-78ca6b196c13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKtBW2exthGkJjJ6WCefq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4693,
      "cache_read_input_tokens": 51292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4693
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-28T18:28:46.280Z_

<details><summary>↩ Tool result · `toolu_015ePfvERLqhz41M34tdjne7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "d7eb0f1d-6dae-44f8-a9e5-ba98de0dfdd5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).",
    "newString": "\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 47,
        "oldLines": 30,
        "newStart": 47,
        "newLines": 17,
        "lines": [
          " Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.",
          " ",
          " \\paragraph{Importance scoring functions.}",
          "-A scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.",
          "+A scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.",
          " ",
          "-\\textbf{L2-norm scoring} assigns each token its activation magnitude:",
          "-\\begin{equation}",
          "-s_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.",
          "-\\label{eq:l2_score}",
          "-\\end{equation}",
          "-The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).",
          "+\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).",
          " ",
          "-\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:",
          "-\\begin{equation}",
          "-s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.",
          "-\\label{eq:random_score}",
          "-\\end{equation}",
          "-Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:exp_setup}).",
          "+\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).",
          " ",
          "-The \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}).",
          "+The \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.",
          " ",
          "-\\paragraph{Attention-based alternatives.}",
          "-Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.",
          "+\\paragraph{Retention ratios.}",
          "+We evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).",
          " ",
          "-\\paragraph{Retention ratio design space.}",
          "-We evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).",
          "-",
          " \\subsection{Compressibility Diagnostic: Importance CV}",
          " \\label{sec:cv_diagnostic}",
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

_source line 48_

Now compress the CV diagnostic section: move attention entropy to appendix, compact the CV spectrum equation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "c7bc8a98-7902-47bc-8468-70d7dfeec595",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ygGkxf7yocEBKqNBKgf4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 55985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2187
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

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_01QKfSp7N74dKKWdLPhRFkDV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.",
  "new_string": "\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "67cbc808-f5d5-4cc2-b497-d3fbe67cb4a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ygGkxf7yocEBKqNBKgf4h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2187,
      "cache_read_input_tokens": 55985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2187
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

_source line 50 · 2026-05-28T18:29:03.615Z_

<details><summary>↩ Tool result · `toolu_01QKfSp7N74dKKWdLPhRFkDV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "4b081c3f-a4f5-420d-b3fc-8730378234e0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.",
    "newString": "\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 69,
        "oldLines": 15,
        "newStart": 69,
        "newLines": 9,
        "lines": [
          " where $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.",
          " ",
          " \\paragraph{The CV spectrum.}",
          "-CV captures a continuous ordering across six models and three connector families:",
          "-\\begin{equation}",
          "-\\begin{split}",
          "-\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\",
          "-&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}",
          "-\\end{split}",
          "-\\label{eq:cv_spectrum}",
          "-\\end{equation}",
          "-This ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.",
          "+CV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):",
          "+$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.",
          "+Linear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.",
          " ",
          " \\paragraph{CV as pruning tolerance predictor.}",
          " CV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance."
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

_source line 51_

Now compress the "CV as pruning tolerance predictor" and move attention entropy entirely to appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "23cbf668-d0f6-4653-92c6-dce62aab187a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vj7kLKPVZPGxNFjBRKFEXz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 58172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01KxcxmTKffdsrg2V6TyN5uP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.",
  "new_string": "\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "834251d8-4219-4e51-956b-df107c948ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vj7kLKPVZPGxNFjBRKFEXz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 58172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

_source line 53 · 2026-05-28T18:29:32.193Z_

<details><summary>↩ Tool result · `toolu_01KxcxmTKffdsrg2V6TyN5uP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ceb16977-518f-42eb-b5f7-b7794a4ea6b2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.",
    "newString": "\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:cv_sensitivity}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 13,
        "newStart": 74,
        "newLines": 8,
        "lines": [
          " Linear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.",
          " ",
          " \\paragraph{CV as pruning tolerance predictor.}",
          "-CV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.",
          "+High CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).",
          " ",
          "-CV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:cv_sensitivity}).",
          "-",
          "-\\paragraph{Complementary role of attention entropy.}",
          "-Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:model_properties}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.",
          "-",
          " \\subsection{Vision Token Re-encoder (VTR)}",
          " \\label{sec:vtr}",
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

_source line 54_

Now compress experiments.tex. The scoring method sensitivity section is the longest.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "2ddf7f3a-f918-4dd5-895f-0c1c6b6f4499",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdPKuhTTiKXKbTaQ1KchC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 59165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1031
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

_source line 55_

<details open><summary>🔧 Tool call — Edit · `toolu_01TZCatHNPVMmUFP2m4Nos66`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Cliff vs.\\ graded degradation.} The divergent response patterns in the cliff zone ($k \\in [0.85, 0.95]$) reflect a statistical distinction between the two scoring methods. Random removal samples a different token subset at each control step; in this interval, the probability of destroying at least one critical token combination transitions from low to near-certain, which produces a binary collapse. L2 scoring deterministically retains the same high-norm subset at every step. This determinism explains the 93\\,pp gap at $k{=}0.85$ on Object (L2 98.0\\% vs.\\ random 5.0\\%; Appendix Table~\\ref{tab:full_results}).\n\n\\textbf{Inverted-U importance margin.} The importance margin $\\Delta$ on $\\pi_{0.5}$ Long follows an inverted-U profile across retention ratios (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}). The margin peaks at $k{=}0.9$ ($\\Delta{=}+$46.9\\,pp: L2 80.4\\% vs.\\ random 33.6\\%), the retention ratio where importance-aware selection provides maximum value. Above this peak ($k{=}0.95$, $\\Delta{=}+$25.6\\,pp), both methods retain enough tokens for adequate performance and the advantage of targeted selection diminishes. Below it ($k{=}0.5$, $\\Delta{\\approx}+$1.3\\,pp), both methods lose enough information that their strategies become equally inadequate. Near $k{\\approx}0.7$, the ranking inverts: random surpasses L2 (64.6\\% vs.\\ 63.2\\%; Appendix Table~\\ref{tab:full_results}) because L2 concentrates retained tokens in a single high-activation region at the cost of the spatial coverage that multi-step tasks require. The V-shaped random recovery at lower $k$ arises from position aliasing under scattered removal (Section~\\ref{sec:analysis}).",
  "new_string": "\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "1c4bcc08-0fc9-4ac6-9b55-d4b11c503c04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdPKuhTTiKXKbTaQ1KchC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1031,
      "cache_read_input_tokens": 59165,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1031
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

_source line 56 · 2026-05-28T18:29:56.837Z_

<details><summary>↩ Tool result · `toolu_01TZCatHNPVMmUFP2m4Nos66`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "4d23d148-e376-4abc-85ba-a138243ba8cc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "oldString": "\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Cliff vs.\\ graded degradation.} The divergent response patterns in the cliff zone ($k \\in [0.85, 0.95]$) reflect a statistical distinction between the two scoring methods. Random removal samples a different token subset at each control step; in this interval, the probability of destroying at least one critical token combination transitions from low to near-certain, which produces a binary collapse. L2 scoring deterministically retains the same high-norm subset at every step. This determinism explains the 93\\,pp gap at $k{=}0.85$ on Object (L2 98.0\\% vs.\\ random 5.0\\%; Appendix Table~\\ref{tab:full_results}).\n\n\\textbf{Inverted-U importance margin.} The importance margin $\\Delta$ on $\\pi_{0.5}$ Long follows an inverted-U profile across retention ratios (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}). The margin peaks at $k{=}0.9$ ($\\Delta{=}+$46.9\\,pp: L2 80.4\\% vs.\\ random 33.6\\%), the retention ratio where importance-aware selection provides maximum value. Above this peak ($k{=}0.95$, $\\Delta{=}+$25.6\\,pp), both methods retain enough tokens for adequate performance and the advantage of targeted selection diminishes. Below it ($k{=}0.5$, $\\Delta{\\approx}+$1.3\\,pp), both methods lose enough information that their strategies become equally inadequate. Near $k{\\approx}0.7$, the ranking inverts: random surpasses L2 (64.6\\% vs.\\ 63.2\\%; Appendix Table~\\ref{tab:full_results}) because L2 concentrates retained tokens in a single high-activation region at the cost of the spatial coverage that multi-step tasks require. The V-shaped random recovery at lower $k$ arises from position aliasing under scattered removal (Section~\\ref{sec:analysis}).",
    "newString": "\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \\textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \\textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \\textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \\textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\\% confidence intervals.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Cliff vs.\\ graded degradation.} The divergent response patterns in the cliff zone ($k \\in [0.85, 0.95]$) reflect a statistical distinction between the two scoring methods. Random removal samples a different token subset at each control step; in this interval, the probability of destroying at least one critical token combination transitions from low to near-certain, which produces a binary collapse. L2 scoring deterministically retains the same high-norm subset at every step. This determinism explains the 93\\,pp gap at $k{=}0.85$ on Object (L2 98.0\\% vs.\\ random 5.0\\%; Appendix Table~\\ref{tab:full_results}).\n\n\\textbf{Inverted-U importance margin.} The importance margin $\\Delta$ on $\\pi_{0.5}$ Long follows an inverted-U profile across retention ratios (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}). The margin peaks at $k{=}0.9$ ($\\Delta{=}+$46.9\\,pp: L2 80.4\\% vs.\\ random 33.6\\%), the retention ratio where importance-aware selection provides maximum value. Above this peak ($k{=}0.95$, $\\Delta{=}+$25.6\\,pp), both methods retain enough tokens for adequate performance and the advantage of targeted selection diminishes. Below it ($k{=}0.5$, $\\Delta{\\approx}+$1.3\\,pp), both methods lose enough information that their strategies become equally inadequate. Near $k{\\approx}0.7$, the ranking inverts: random surpasses L2 (64.6\\% vs.\\ 63.2\\%; Appendix Table~\\ref{tab:full_results}) because L2 concentrates retained tokens in a single high-activation region at the cost of the spatial coverage that multi-step tasks require. The V-shaped random recovery at lower $k$ arises from position aliasing under scattered removal (Section~\\ref{sec:analysis}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}): Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\n",
    "structuredPatch": [
      {
        "oldStart": 94,
        "oldLines": 10,
        "newStart": 94,
        "newLines": 8,
        "lines": [
          " ",
          " \\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).",
          " ",
          "-\\textbf{Cliff vs.\\ graded degradation.} The divergent response patterns in the cliff zone ($k \\in [0.85, 0.95]$) reflect a statistical distinction between the two scoring methods. Random removal samples a different token subset at each control step; in this interval, the probability of destroying at least one critical token combination transitions from low to near-certain, which produces a binary collapse. L2 scoring deterministically retains the same high-norm subset at every step. This determinism explains the 93\\,pp gap at $k{=}0.85$ on Object (L2 98.0\\% vs.\\ random 5.0\\%; Appendix Table~\\ref{tab:full_results}).",
          "+\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).",
          " ",
          "-\\textbf{Inverted-U importance margin.} The importance margin $\\Delta$ on $\\pi_{0.5}$ Long follows an inverted-U profile across retention ratios (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}). The margin peaks at $k{=}0.9$ ($\\Delta{=}+$46.9\\,pp: L2 80.4\\% vs.\\ random 33.6\\%), the retention ratio where importance-aware selection provides maximum value. Above this peak ($k{=}0.95$, $\\Delta{=}+$25.6\\,pp), both methods retain enough tokens for adequate performance and the advantage of targeted selection diminishes. Below it ($k{=}0.5$, $\\Delta{\\approx}+$1.3\\,pp), both methods lose enough information that their strategies become equally inadequate. Near $k{\\approx}0.7$, the ranking inverts: random surpasses L2 (64.6\\% vs.\\ 63.2\\%; Appendix Table~\\ref{tab:full_results}) because L2 concentrates retained tokens in a single high-activation region at the cost of the spatial coverage that multi-step tasks require. The V-shaped random recovery at lower $k$ arises from position aliasing under scattered removal (Section~\\ref{sec:analysis}).",
          "-",
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}"
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

_source line 57_

<details open><summary>🔧 Tool call — Edit · `toolu_013sYkS2NCTcmE3kfR6Hccrc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}): Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.",
  "new_string": "\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "b1e3bf89-bd95-40cc-aa84-9a12393369f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7eRFgX8WMXMTNHDsbCw1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 60196,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1195
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

_source line 58 · 2026-05-28T18:30:03.899Z_

<details><summary>↩ Tool result · `toolu_013sYkS2NCTcmE3kfR6Hccrc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ea06d84f-ca5b-407d-a47f-92680cbc271b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "oldString": "\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}): Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.",
    "newString": "\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \\textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \\textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \\textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \\textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\\% confidence intervals.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}): Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\n",
    "structuredPatch": [
      {
        "oldStart": 103,
        "oldLines": 7,
        "newStart": 103,
        "newLines": 7,
        "lines": [
          " \\label{fig:cliff_highlight}",
          " \\end{figure}",
          " ",
          "-\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}): Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp. Multi-step tasks distribute critical information across tokens with more heterogeneous norm profiles, which reduces the effectiveness of magnitude-based selection.",
          "+\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).",
          " ",
          " \\subsection{VTR Recovery}",
          " \\label{sec:vtr_recovery}"
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

_source line 59_

Now compress the experimental setup section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "8e09415c-78cf-4ed1-8307-b930bacf2e7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5iXVFiUCJfM6WnNbZFoy9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 422,
      "cache_read_input_tokens": 61391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 422
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01BgYjHVwQqCkSMHYJFdoxFZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \\textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \\textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \\textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \\textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\\% confidence intervals.",
  "new_string": "\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "67bfd6dd-7b92-423b-aecf-2ccd8ac7cb10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5iXVFiUCJfM6WnNbZFoy9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 422,
      "cache_read_input_tokens": 61391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 422
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

_source line 61 · 2026-05-28T18:30:27.349Z_

<details><summary>↩ Tool result · `toolu_01BgYjHVwQqCkSMHYJFdoxFZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "d4864619-b554-46ea-ae58-e7faec748845",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "oldString": "\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \\textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \\textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \\textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \\textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\\% confidence intervals.",
    "newString": "\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \\textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \\textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \\textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \\textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\\% confidence intervals.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 11,
        "newStart": 4,
        "newLines": 11,
        "lines": [
          " \\subsection{Experimental Setup}",
          " \\label{sec:exp_setup}",
          " ",
          "-\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark comprising four task suites of increasing complexity. \\textbf{Object} (10 tasks) requires discriminating among visually similar objects at identical locations. \\textbf{Spatial} (10 tasks) requires understanding relative spatial layouts (e.g., ``pick the bowl on the left of the plate''), where critical information is distributed across the visual field. \\textbf{Goal} (10 tasks) involves goal-conditioned manipulation with varied target configurations. \\textbf{Long} (10 tasks) chains 3--5 manipulation primitives into multi-step sequences, where token loss at any step can cascade through the remainder of the trajectory. Each task provides 50 demonstration episodes for fine-tuning and 50 evaluation episodes, yielding 500 episodes per suite.",
          "+\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).",
          " ",
          "-\\paragraph{Models.} Four VLAs are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) contribute to the CV diagnostic via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures.",
          "+\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.",
          " ",
          "-\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean success rate (SR) over 500 episodes in strict evaluation mode (episodes run to completion regardless of intermediate failures). Multi-seed results ($\\pi_{0.5}$ Long: five seeds, 42--46; VTR: three seeds, 42--44) report mean $\\pm$ standard deviation with per-seed breakdowns in the appendix. Single-seed results report Wilson 95\\% confidence intervals.",
          "+\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.",
          " ",
          " \\subsection{Two-Axis Framework Overview}",
          " \\label{sec:two_axis}"
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

_source line 62_

Compress the pixel-shuffle entanglement section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "41ad0541-d960-45ed-9873-6c930f9dfc0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDscs86JufG4BT2yrapKfU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1196,
      "cache_read_input_tokens": 61813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1196
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

_source line 63_

<details open><summary>🔧 Tool call — Edit · `toolu_01KjTvYPtj3DVdyJ1Z181LbT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "SmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.",
  "new_string": "SmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "c7a81235-4749-4ea2-88c7-6619d3df8852",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDscs86JufG4BT2yrapKfU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1196,
      "cache_read_input_tokens": 61813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1196
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

_source line 64 · 2026-05-28T18:30:35.395Z_

<details><summary>↩ Tool result · `toolu_01KjTvYPtj3DVdyJ1Z181LbT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "4c30d71f-19c0-4e93-85f7-bb99b3d64f2a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "oldString": "SmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.",
    "newString": "SmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation}).",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\n",
    "structuredPatch": [
      {
        "oldStart": 80,
        "oldLines": 7,
        "newStart": 80,
        "newLines": 7,
        "lines": [
          " \\label{fig:entanglement_scoring}",
          " \\end{figure*}",
          " ",
          "-SmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.",
          "+SmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation}).",
          " ",
          " \\subsection{Position Disruption vs.\\ Information Loss}",
          " \\label{sec:zeromask}"
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

_source line 65_

Now compress the VTR recovery section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ff02b805-08c7-4fc6-ae6c-d104db0b8065",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015v6aq5vnv3CMooGPNsfuiE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 63009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 431
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

_source line 66_

<details open><summary>🔧 Tool call — Edit · `toolu_01AAQFNhvWSEt5MrRFzJvhvD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.",
  "new_string": "VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, $<$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, $n{=}3$; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), indicating the benefit stems from re-encoding, not the cross-attention mechanism. Cross-suite generalization: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning. For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\\%; VTR exceeds the unpruned baseline at up to 87.5\\% compression. Baseline (44.8\\%) is our LoRA reproduction; official checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}).}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "212fc4bc-3303-49f5-9471-ea5b955cd534",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015v6aq5vnv3CMooGPNsfuiE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 63009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 431
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

_source line 67 · 2026-05-28T18:31:05.450Z_

<details><summary>↩ Tool result · `toolu_01AAQFNhvWSEt5MrRFzJvhvD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "78babc5d-4485-4df6-ac4e-0d6536324fae",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "oldString": "VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.",
    "newString": "VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, $<$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, $n{=}3$; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), indicating the benefit stems from re-encoding, not the cross-attention mechanism. Cross-suite generalization: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning. For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\\%; VTR exceeds the unpruned baseline at up to 87.5\\% compression. Baseline (44.8\\%) is our LoRA reproduction; official checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}).}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation}).\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\n",
    "structuredPatch": [
      {
        "oldStart": 108,
        "oldLines": 12,
        "newStart": 108,
        "newLines": 12,
        "lines": [
          " \\subsection{VTR Recovery}",
          " \\label{sec:vtr_recovery}",
          " ",
          "-VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, 3 seeds; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control (100K steps, identical recipe, no compressor) reaches only 45.0\\% ($p > 0.9$ vs.\\ baseline; Appendix~\\ref{app:smart_compress_details}), which rules out additional optimization as the source of improvement. The re-encoding module provides a beneficial inductive bias: by restructuring entangled pixel-shuffle tokens, VTR produces a representation that is both more compact and more effective than the original. A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), which indicates the benefit stems from re-encoding itself, not the cross-attention mechanism. Cross-suite generalization confirms the pattern: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning.",
          "+VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, $<$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, $n{=}3$; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), indicating the benefit stems from re-encoding, not the cross-attention mechanism. Cross-suite generalization: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning. For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR.",
          " ",
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR achieves ${\\geq}$57\\% at up to 87.5\\% compression, exceeding the unpruned baseline. Baseline (44.8\\%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}). See Appendix~\\ref{app:smart_compress_details} for training details.}",
          "+\\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\\%; VTR exceeds the unpruned baseline at up to 87.5\\% compression. Baseline (44.8\\%) is our LoRA reproduction; official checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}).}",
          " \\label{tab:vtr_main}",
          " \\begin{tabular}{lccr}",
          " \\toprule"
        ]
      },
      {
        "oldStart": 128,
        "oldLines": 5,
        "newStart": 128,
        "newLines": 3,
        "lines": [
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}",
          "-",
          "-\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough."
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

_source line 68_

Now compress the VTR architecture description in method.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "8068ab2c-5259-4f23-992b-610092ffd0a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrCuatMhqnEn8r51QVCK4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1728,
      "cache_read_input_tokens": 63440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1728
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

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_01BUme7UJufxq6RfUqcVXsjh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.",
  "new_string": "\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "58704df6-affb-42d8-8966-8d140563444c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NrCuatMhqnEn8r51QVCK4z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1728,
      "cache_read_input_tokens": 63440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1728
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

_source line 70 · 2026-05-28T18:31:18.582Z_

<details><summary>↩ Tool result · `toolu_01BUme7UJufxq6RfUqcVXsjh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "99bd6c20-e3f9-41e3-8fd3-9a6c4147b48f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.",
    "newString": "\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.\n\n\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 82,
        "oldLines": 7,
        "newStart": 82,
        "newLines": 4,
        "lines": [
          " Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.",
          " ",
          " \\paragraph{Architecture.}",
          "-VTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.",
          "-",
          "-\\paragraph{Training and cost.}",
          "-The module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.",
          "+VTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details})."
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

_source line 71_

Now compress the pruning protocol description.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "d24eace2-cbb3-4726-92bf-646c40c5db08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkUjUJou9Ek1tVWmgr6EeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 65168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
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

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01QfKGcfVhGPqzDEMh3LtsbG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.",
  "new_string": "Given $N$ post-connector tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning retains $\\lfloor k \\cdot N \\rfloor$ tokens for $k \\in (0, 1]$ and physically removes the rest, re-indexing positions to close gaps. We prune between the connector output and LLM input to isolate the connector's effect on token information structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "d506fa92-a2dc-4f2d-a57b-62a489b292c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkUjUJou9Ek1tVWmgr6EeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 65168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
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

_source line 73 · 2026-05-28T18:31:27.483Z_

<details><summary>↩ Tool result · `toolu_01QfKGcfVhGPqzDEMh3LtsbG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "2d635d1d-3410-4481-99ce-aa4467896a59",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.",
    "newString": "Given $N$ post-connector tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning retains $\\lfloor k \\cdot N \\rfloor$ tokens for $k \\in (0, 1]$ and physically removes the rest, re-indexing positions to close gaps. We prune between the connector output and LLM input to isolate the connector's effect on token information structure.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.\n\n\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details}).\n",
    "structuredPatch": [
      {
        "oldStart": 44,
        "oldLines": 7,
        "newStart": 44,
        "newLines": 7,
        "lines": [
          " \\subsection{Pruning Protocol}",
          " \\label{sec:pruning_protocol}",
          " ",
          "-Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.",
          "+Given $N$ post-connector tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning retains $\\lfloor k \\cdot N \\rfloor$ tokens for $k \\in (0, 1]$ and physically removes the rest, re-indexing positions to close gaps. We prune between the connector output and LLM input to isolate the connector's effect on token information structure.",
          " ",
          " \\paragraph{Importance scoring functions.}",
          " A scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies."
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

Now compress the models/connectors section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "5f918f76-d8d4-416e-9260-a925b2b8bf9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E88RVJwhJuERXLrVEEQ7zd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 65733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
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

_source line 75_

<details open><summary>🔧 Tool call — Edit · `toolu_019urRZPTvJPc6E6Bi5m4Lfz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.",
  "new_string": "We evaluate token pruning across six VLA architectures spanning three connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). \\textbf{Linear projection} applies a per-patch matrix multiplication ($\\pi_{0}$~\\cite{black2024pi0}, $\\pi_{0.5}$~\\cite{black2025pi05}; CV$\\,{<}\\,$0.06). \\textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\\cite{kim2024openvla}, OFT~\\cite{kim2025openoft}; CV$\\,{\\approx}\\,$0.22). \\textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\\cite{zheng2025xvla} uses a 12-layer BART encoder~\\cite{lewis2020bart} (CV$\\,{=}\\,$0.151); SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 patches per token (CV$\\,{=}\\,$0.314). We classify coupling as \\emph{independent} (one patch per output token) or \\emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "25d05f84-816a-4fd6-8732-99df6639c85d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E88RVJwhJuERXLrVEEQ7zd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 65733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
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

_source line 76 · 2026-05-28T18:31:48.473Z_

<details><summary>↩ Tool result · reported error · `toolu_019urRZPTvJPc6E6Bi5m4Lfz`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "29bbc7eb-0c2c-4e6f-a7a2-1ca291d450d0",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01E9kYjwqFpXa46FmoEqGjjZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
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
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "2de69177-5da4-48e1-9414-7e59e723f8c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01116KvASDbDsietctApjVps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3826,
      "cache_read_input_tokens": 66214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3826
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

_source line 78 · 2026-05-28T18:31:52.913Z_

<details><summary>↩ Tool result · `toolu_01E9kYjwqFpXa46FmoEqGjjZ`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft} shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "5e684abc-afe6-4111-b993-1ce09fdbbccf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 86
    }
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Edit · `toolu_01CCuR7J8Uid7VJ9cpX7qVzJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.",
  "new_string": "We evaluate token pruning across six VLA architectures spanning three connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). \\textbf{Linear projection} applies a per-patch matrix multiplication ($\\pi_{0}$~\\cite{black2024pi0}, $\\pi_{0.5}$~\\cite{black2025pi05}; CV$\\,{<}\\,$0.06). \\textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\\cite{kim2024openvla}, OFT~\\cite{kim2025openoft}; CV$\\,{\\approx}\\,$0.22). \\textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\\cite{zheng2025xvla} uses a 12-layer BART encoder~\\cite{lewis2020bart} (CV$\\,{=}\\,$0.151); SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 patches per token (CV$\\,{=}\\,$0.314). We classify coupling as \\emph{independent} (one patch per output) or \\emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "34d87344-60f3-4cce-8b29-1dd4f544f78b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014iSSBZhwQXhW1qpvYzrZm7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 70040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 797
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

_source line 80 · 2026-05-28T18:32:03.228Z_

<details><summary>↩ Tool result · `toolu_01CCuR7J8Uid7VJ9cpX7qVzJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "5b432309-e132-409a-89ef-1ff3fcae2e25",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.",
    "newString": "We evaluate token pruning across six VLA architectures spanning three connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). \\textbf{Linear projection} applies a per-patch matrix multiplication ($\\pi_{0}$~\\cite{black2024pi0}, $\\pi_{0.5}$~\\cite{black2025pi05}; CV$\\,{<}\\,$0.06). \\textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\\cite{kim2024openvla}, OFT~\\cite{kim2025openoft}; CV$\\,{\\approx}\\,$0.22). \\textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\\cite{zheng2025xvla} uses a 12-layer BART encoder~\\cite{lewis2020bart} (CV$\\,{=}\\,$0.151); SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 patches per token (CV$\\,{=}\\,$0.314). We classify coupling as \\emph{independent} (one patch per output) or \\emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning retains $\\lfloor k \\cdot N \\rfloor$ tokens for $k \\in (0, 1]$ and physically removes the rest, re-indexing positions to close gaps. We prune between the connector output and LLM input to isolate the connector's effect on token information structure.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_pruning}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.\n\n\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details}).\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 16,
        "newStart": 4,
        "newLines": 8,
        "lines": [
          " \\subsection{Models and Connectors}",
          " \\label{sec:models}",
          " ",
          "-We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.",
          "+We evaluate token pruning across six VLA architectures spanning three connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). \\textbf{Linear projection} applies a per-patch matrix multiplication ($\\pi_{0}$~\\cite{black2024pi0}, $\\pi_{0.5}$~\\cite{black2025pi05}; CV$\\,{<}\\,$0.06). \\textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\\cite{kim2024openvla}, OFT~\\cite{kim2025openoft}; CV$\\,{\\approx}\\,$0.22). \\textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\\cite{zheng2025xvla} uses a 12-layer BART encoder~\\cite{lewis2020bart} (CV$\\,{=}\\,$0.151); SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 patches per token (CV$\\,{=}\\,$0.314). We classify coupling as \\emph{independent} (one patch per output) or \\emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.",
          " ",
          "-\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).",
          "-",
          "-\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).",
          "-",
          "-\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).",
          "-",
          "-We classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.",
          "-",
          " \\begin{figure*}[t]",
          " \\centering",
          " \\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}"
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

_source line 81_

Now I need to add the moved content to appendix. Let me add appendix sections for attention scoring and attention entropy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "04b8476f-7468-4e4e-ac27-6c4a788aecb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4EY8AxUFsGYZSXuV3LVmj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1011,
      "cache_read_input_tokens": 70837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1011
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

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_01962FR8zN5qHE6wWZkAXHSy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": 130,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ce8c7504-529a-4da0-be3d-0e4dbdfafe83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4EY8AxUFsGYZSXuV3LVmj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1011,
      "cache_read_input_tokens": 70837,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1011
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

_source line 83 · 2026-05-28T18:32:07.196Z_

<details><summary>↩ Tool result · `toolu_01962FR8zN5qHE6wWZkAXHSy`</summary>

```text
130	
131	
132	\section{Pruning Protocol Details}
133	\label{app:pruning_details}
134	
135	Both pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.
136	
137	Model-specific retention ratios reflect each architecture's token count and expected sensitivity. $\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\pi_{0.5}$ uses $k \in \{0.3, 0.5, 0.7\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \in \{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \in \{0.3, 0.5, 0.7, 0.9, 0.95\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.5, 0.7, 0.9, 0.95\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\cite{bolya2023tome}).
138	
139	The $\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\ three-layer MLP), backbone (PaliGemma vs.\ Llama-2), and encoder fusion strategy (single SigLIP vs.\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.
140	
141	
142	\section{SmolVLA Pruning Ablation}
143	\label{app:smolvla_ablation}
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "d45a3068-a094-423c-9e45-4cd6a6b58f9b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
      "content": "\n\n\\section{Pruning Protocol Details}\n\\label{app:pruning_details}\n\nBoth pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\\pi_{0.5}$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\\ three-layer MLP), backbone (PaliGemma vs.\\ Llama-2), and encoder fusion strategy (single SigLIP vs.\\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.\n\n\n\\section{SmolVLA Pruning Ablation}\n\\label{app:smolvla_ablation}\n",
      "numLines": 15,
      "startLine": 130,
      "totalLines": 921
    }
  }
}
```

</details>

---

### Assistant

_source line 84_

Now let me check if there's already an `app:attention_scoring` or `app:attention_pruning` label in the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "64c36155-41d6-4b07-8406-caab257bfc78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1TqASt359XJBWP2BDv5sp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 71848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1017
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

_source line 85_

<details open><summary>🔧 Tool call — Grep · `toolu_0145zn1RW5PzPBdDNsZU9z6Z`</summary>

```json
{
  "pattern": "attention_scoring|attention_pruning|attention_entropy|app:attention",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
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
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "80c93db1-be7a-4fbc-b9f3-aa111807d866",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1TqASt359XJBWP2BDv5sp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 71848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1017
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

_source line 86 · 2026-05-28T18:32:11.593Z_

<details><summary>↩ Tool result · `toolu_0145zn1RW5PzPBdDNsZU9z6Z`</summary>

```text
experiments.tex:95:\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\geq}$92.8\% while L2 falls 8--27\,pp below random; on $\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\,pp). On Long, attention cliffs $-$26.5\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\ref{fig:cliff_highlight}).
main.log:579:LaTeX Warning: Reference `app:attention_entropy' on page 5 undefined on input l
sections/analysis.tex:3:%   Attention entropy analysis:     attention_entropy_analysis
appendix.tex:865:\label{app:attention_pruning}
appendix.tex:867:Table~\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\_last), mean attention across all decoder layers (attn\_mean), and attention rollout~\cite{abnar2020quantifying}.
appendix.tex:873:\label{tab:attention_pruning}
main.aux:282:\newlabel{app:attention_pruning}{{V.1}{30}{Attention-Based Scoring}{subsection.V.1}{}}
main.aux:284:\newlabel{tab:attention_pruning}{{25}{30}{X-VLA success rates (\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \textsuperscript {*}Best of three attention variants}{table.caption.64}{}}
method.tex:48:[Omitted long matching line]
method.tex:69:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "4a8de913-4f6d-4cae-aa89-bbb070c3de1c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "experiments.tex:95:\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\nmain.log:579:LaTeX Warning: Reference `app:attention_entropy' on page 5 undefined on input l\nsections/analysis.tex:3:%   Attention entropy analysis:     attention_entropy_analysis\nappendix.tex:865:\\label{app:attention_pruning}\nappendix.tex:867:Table~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\nappendix.tex:873:\\label{tab:attention_pruning}\nmain.aux:282:\\newlabel{app:attention_pruning}{{V.1}{30}{Attention-Based Scoring}{subsection.V.1}{}}\nmain.aux:284:\\newlabel{tab:attention_pruning}{{25}{30}{X-VLA success rates (\\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \\textsuperscript {*}Best of three attention variants}{table.caption.64}{}}\nmethod.tex:48:[Omitted long matching line]\nmethod.tex:69:[Omitted long matching line]",
    "numLines": 10
  }
}
```

</details>

---

### Assistant

_source line 87_

Good, `app:attention_pruning` exists at line 865. Now I need to add `app:attention_entropy` and `app:attention_scoring` labels. Let me check what's around line 865.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "f6ad70b7-bf7b-4dbc-87f6-7f694e1bf69a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqFoaMetgVD5uZdn3ct6L4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 72865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 700
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

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_01FaHgWxG9NGLdGZ6pzzxejM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": 855,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ffeeb5cb-6afe-42f4-9583-f934b6072875",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqFoaMetgVD5uZdn3ct6L4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 72865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 700
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

_source line 89 · 2026-05-28T18:32:16.151Z_

<details><summary>↩ Tool result · `toolu_01FaHgWxG9NGLdGZ6pzzxejM`</summary>

```text
855	\label{app:cost_benefit}
856	
857	The primary deployment benefit of VTR at this model scale is memory, not latency. Reducing from 128 to 32 vision tokens shrinks the KV-cache footprint for the vision portion by 75\%, a meaningful reduction for memory-constrained robotic hardware where KV-cache size can limit the number of concurrent policy instances or maximum context length.
858	
859	End-to-end inference latency improves only modestly: 154.78\,ms at $M{=}32$ versus 164.33\,ms at full token count, a $1.06\times$ speedup (6\% reduction). At $M{=}64$: 156.16\,ms ($1.05\times$). The gap between token reduction and latency gain reflects SmolVLA's compact size (450M parameters): self-attention over 128 vision tokens is not the inference bottleneck, and the compressor's 22.2M-parameter cross-attention computation partially offsets downstream savings. Token pruning becomes a more compelling latency optimization for VLAs with larger token budgets ($>$256 tokens) or larger backbones (7B+ parameters), where attention cost scales quadratically with sequence length. Whether the training cost (100K steps, 6.5 hours per configuration) is justified depends on deployment context: for VLAs deployed across many tasks, the one-time training cost is amortized; for rapid prototyping, retraining is a barrier.
860	
861	\paragraph{Comparison with the official checkpoint.}
862	VTR at $M = 32$ ($60.1 \pm 1.3$\% over 3 seeds) recovers from 0\% SR under hard pruning to performance comparable to the official SmolVLA checkpoint (59.2\%, CI [54.8\%, 63.4\%]). However, the difference is not statistically significant (two-sample $t$-test, $p \approx 0.72$), and the comparison should be interpreted cautiously given different training conditions (batch size 4 vs.\ 64, single vs.\ 8 GPUs). The primary contribution of VTR is recovering functional performance where all deletion methods yield 0\%, not matching the official baseline.
863	
864	\subsection{Attention-Based Scoring}
865	\label{app:attention_pruning}
866	
867	Table~\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\_last), mean attention across all decoder layers (attn\_mean), and attention rollout~\cite{abnar2020quantifying}.
868	
869	\begin{table}[h]
870	\centering
871	\small
872	\caption{X-VLA success rates (\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \textsuperscript{*}Best of three attention variants.}
873	\label{tab:attention_pruning}
874	\begin{tabular}{lccccc}
875	\toprule
876	Suite & attn\_last & attn\_mean & attn\_rollout & L2 & Random \\
877	\midrule
878	Object & \textbf{99.2} & 98.4 & 97.4 & 43.4 & 70.6 \\
879	Spatial & 88.8 & 91.6 & \textbf{92.8} & 58.8 & 71.4 \\
880	Long & 90.2 & 94.0 & \textbf{94.8} & 45.0 & 61.6 \\
881	Goal & \multicolumn{3}{c}{\textbf{98.2}\textsuperscript{*}} & 59.0 & 67.2 \\
882	\bottomrule
883	\end{tabular}
884	\end{table}
885	
886	L2 norm selection is anti-informative on X-VLA's entangling connector: L2 falls below random on all four suites, with gaps ranging from $-$8.2\,pp (Goal) to $-$27.2\,pp (Object). Attention-based scoring recovers near-baseline performance across all suites (${\geq}$92.8\%), with rollout peaking at 94.8\% on Long (seed43 confirms $\Delta{\leq}$0.6\,pp). On Object, all three attention variants achieve ${\geq}$97.4\%, far exceeding both L2 (43.4\%) and random (70.6\%). The mode ranking reverses across suites: last-layer attention is best on Object (99.2\%) but worst among attention methods on Spatial (88.8\%) and Long (90.2\%), while rollout shows the opposite pattern.
887	
888	The L2 failure has a structural explanation. The BART encoder's 12-layer self-attention redistributes information across tokens, equalizing activation magnitudes (CV$\,{=}\,$0.151). L2 norms no longer reflect token importance; instead, they select spatially correlated clusters that miss critical information. Goal L2 exhibits non-monotonic behavior ($k{=}0.7$: 53.4\% $<$ $k{=}0.5$: 59.0\%), confirming that retaining more L2-selected tokens is actively harmful. Per-task variance under L2 pruning is extreme on Spatial (std$\,{=}\,$31.5\,pp, range 0--92\%), while attention scoring keeps all tasks above 80\%. The double dissociation extends to $\pi_{0.5}$, where attention scoring at $k{=}0.5$ exhibits suite-dependent failure (Table~\ref{tab:pi05_attention_crosssuite}). On three suites (Goal, Spatial, Long), attention performs within noise of random ($\pm$3\,pp). On Object, attention collapses to 37.8\% ($-$31.6\,pp vs.\ random's 69.4\%), a catastrophic failure unique to tasks requiring spatial discrimination among visually similar alternatives. The linear connector produces an extremely narrow attention score range ($[2{\times}10^{-6},\, 3.6{\times}10^{-3}]$) with systematic position bias favoring early tokens; on Object, this bias selects semantically relevant but spatially uninformative tokens, destroying the fine-grained spatial information needed for target identification.
889	
890	\begin{table}[ht]
891	\centering
892	\small
893	\caption{$\pi_{0.5}$ attention vs.\ random at $k{=}0.5$ across LIBERO suites. Attention is neutral on 3/4 suites but catastrophically harmful on Object.}
894	\label{tab:pi05_attention_crosssuite}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "4487b69a-814b-4287-bd92-961eba36f95c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
      "content": "\\label{app:cost_benefit}\n\nThe primary deployment benefit of VTR at this model scale is memory, not latency. Reducing from 128 to 32 vision tokens shrinks the KV-cache footprint for the vision portion by 75\\%, a meaningful reduction for memory-constrained robotic hardware where KV-cache size can limit the number of concurrent policy instances or maximum context length.\n\nEnd-to-end inference latency improves only modestly: 154.78\\,ms at $M{=}32$ versus 164.33\\,ms at full token count, a $1.06\\times$ speedup (6\\% reduction). At $M{=}64$: 156.16\\,ms ($1.05\\times$). The gap between token reduction and latency gain reflects SmolVLA's compact size (450M parameters): self-attention over 128 vision tokens is not the inference bottleneck, and the compressor's 22.2M-parameter cross-attention computation partially offsets downstream savings. Token pruning becomes a more compelling latency optimization for VLAs with larger token budgets ($>$256 tokens) or larger backbones (7B+ parameters), where attention cost scales quadratically with sequence length. Whether the training cost (100K steps, 6.5 hours per configuration) is justified depends on deployment context: for VLAs deployed across many tasks, the one-time training cost is amortized; for rapid prototyping, retraining is a barrier.\n\n\\paragraph{Comparison with the official checkpoint.}\nVTR at $M = 32$ ($60.1 \\pm 1.3$\\% over 3 seeds) recovers from 0\\% SR under hard pruning to performance comparable to the official SmolVLA checkpoint (59.2\\%, CI [54.8\\%, 63.4\\%]). However, the difference is not statistically significant (two-sample $t$-test, $p \\approx 0.72$), and the comparison should be interpreted cautiously given different training conditions (batch size 4 vs.\\ 64, single vs.\\ 8 GPUs). The primary contribution of VTR is recovering functional performance where all deletion methods yield 0\\%, not matching the official baseline.\n\n\\subsection{Attention-Based Scoring}\n\\label{app:attention_pruning}\n\nTable~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{X-VLA success rates (\\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \\textsuperscript{*}Best of three attention variants.}\n\\label{tab:attention_pruning}\n\\begin{tabular}{lccccc}\n\\toprule\nSuite & attn\\_last & attn\\_mean & attn\\_rollout & L2 & Random \\\\\n\\midrule\nObject & \\textbf{99.2} & 98.4 & 97.4 & 43.4 & 70.6 \\\\\nSpatial & 88.8 & 91.6 & \\textbf{92.8} & 58.8 & 71.4 \\\\\nLong & 90.2 & 94.0 & \\textbf{94.8} & 45.0 & 61.6 \\\\\nGoal & \\multicolumn{3}{c}{\\textbf{98.2}\\textsuperscript{*}} & 59.0 & 67.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nL2 norm selection is anti-informative on X-VLA's entangling connector: L2 falls below random on all four suites, with gaps ranging from $-$8.2\\,pp (Goal) to $-$27.2\\,pp (Object). Attention-based scoring recovers near-baseline performance across all suites (${\\geq}$92.8\\%), with rollout peaking at 94.8\\% on Long (seed43 confirms $\\Delta{\\leq}$0.6\\,pp). On Object, all three attention variants achieve ${\\geq}$97.4\\%, far exceeding both L2 (43.4\\%) and random (70.6\\%). The mode ranking reverses across suites: last-layer attention is best on Object (99.2\\%) but worst among attention methods on Spatial (88.8\\%) and Long (90.2\\%), while rollout shows the opposite pattern.\n\nThe L2 failure has a structural explanation. The BART encoder's 12-layer self-attention redistributes information across tokens, equalizing activation magnitudes (CV$\\,{=}\\,$0.151). L2 norms no longer reflect token importance; instead, they select spatially correlated clusters that miss critical information. Goal L2 exhibits non-monotonic behavior ($k{=}0.7$: 53.4\\% $<$ $k{=}0.5$: 59.0\\%), confirming that retaining more L2-selected tokens is actively harmful. Per-task variance under L2 pruning is extreme on Spatial (std$\\,{=}\\,$31.5\\,pp, range 0--92\\%), while attention scoring keeps all tasks above 80\\%. The double dissociation extends to $\\pi_{0.5}$, where attention scoring at $k{=}0.5$ exhibits suite-dependent failure (Table~\\ref{tab:pi05_attention_crosssuite}). On three suites (Goal, Spatial, Long), attention performs within noise of random ($\\pm$3\\,pp). On Object, attention collapses to 37.8\\% ($-$31.6\\,pp vs.\\ random's 69.4\\%), a catastrophic failure unique to tasks requiring spatial discrimination among visually similar alternatives. The linear connector produces an extremely narrow attention score range ($[2{\\times}10^{-6},\\, 3.6{\\times}10^{-3}]$) with systematic position bias favoring early tokens; on Object, this bias selects semantically relevant but spatially uninformative tokens, destroying the fine-grained spatial information needed for target identification.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ attention vs.\\ random at $k{=}0.5$ across LIBERO suites. Attention is neutral on 3/4 suites but catastrophically harmful on Object.}\n\\label{tab:pi05_attention_crosssuite}",
      "numLines": 40,
      "startLine": 855,
      "totalLines": 921
    }
  }
}
```

</details>

---

### Assistant

_source line 90_

Good. Now I need to add the attention-based alternatives description (moved from method.tex) and the attention entropy content. Let me add these to the appendix before the existing attention-based scoring subsection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "dd97bf17-08e8-474e-9c57-59dbedae51a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vvp6kEeTu7WMUjVy5DQr5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1932,
      "cache_read_input_tokens": 73565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1932
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

_source line 91_

<details open><summary>🔧 Tool call — Edit · `toolu_01PJt72dTGK8Aj5NQjLpiD4W`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "old_string": "\\subsection{Attention-Based Scoring}\n\\label{app:attention_pruning}",
  "new_string": "\\subsection{Attention-Based Scoring Methods}\n\\label{app:attention_scoring}\n\\label{app:attention_pruning}\n\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity for residual connections) to approximate cumulative information flow. These methods require a full LLM forward pass and are backbone-specific. We focus on L2 and random in the main text because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\subsection{Attention Entropy as Diagnostic}\n\\label{app:attention_entropy}\n\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention distribution over vision tokens, provides a complementary but less discriminative signal than CV. Three models with qualitatively different pruning behaviors cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness.\n\n\\subsection{Attention-Based Scoring Results}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "f4800e04-f3fb-4e69-8c57-f7197b4418c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vvp6kEeTu7WMUjVy5DQr5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1932,
      "cache_read_input_tokens": 73565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1932
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

_source line 92 · 2026-05-28T18:32:35.930Z_

<details><summary>↩ Tool result · `toolu_01PJt72dTGK8Aj5NQjLpiD4W`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "af152d76-200c-4fca-8bef-ea853879640b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "oldString": "\\subsection{Attention-Based Scoring}\n\\label{app:attention_pruning}",
    "newString": "\\subsection{Attention-Based Scoring Methods}\n\\label{app:attention_scoring}\n\\label{app:attention_pruning}\n\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity for residual connections) to approximate cumulative information flow. These methods require a full LLM forward pass and are backbone-specific. We focus on L2 and random in the main text because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\subsection{Attention Entropy as Diagnostic}\n\\label{app:attention_entropy}\n\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention distribution over vision tokens, provides a complementary but less discriminative signal than CV. Three models with qualitatively different pruning behaviors cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness.\n\n\\subsection{Attention-Based Scoring Results}",
    "originalFile": "\\appendix\n\n\\section{Full Pruning Results}\n\\label{app:full_results}\n\nTable~\\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\\ref{tab:main_results} for space.\n\n\\begin{table*}[ht]\n\\centering\n\\footnotesize\n\\caption{Full closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \\textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \\textsuperscript{$\\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}\n\\label{tab:full_results}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{OpenVLA}\n& Object  & \\textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\\textsuperscript{$\\dagger$} & -- / -- & 39.2 / 35.8 \\\\\n& Goal    & \\textbf{74.8} & -- / -- & 74.8 / 79.6 / 73.2\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Spatial & \\textbf{80.0} & -- / -- & 75.0 / 79.8 / 80.4\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n& Long    & \\textbf{52.8} & -- / -- & 43.6 / 46.8 / 44.0\\textsuperscript{$\\dagger$} & -- / -- & -- / -- \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\n\\section{Extended Discussion}\n\\label{app:extended_discussion}\n\\label{app:discussion}\n\n\\paragraph{Re-encoding and CV diagnostics.}\nBoth cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \\approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\\,{=}\\,$0.151) from $\\pi_0$'s uniformly critical profile (CV$\\,{=}\\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\\ref{app:cv_strategy_interaction},~\\ref{app:cv_extended}).\n\n\\paragraph{Task complexity compresses the importance margin.}\nCV predicts connector-level compressibility, but task complexity determines \\emph{which} scoring method succeeds within a given connector. OpenVLA illustrates the full pattern across LIBERO's complexity gradient (Figure~\\ref{fig:openvla_sweep}).\n\nOn single-step Object, L2 leads at moderate pruning ($+$7.8\\,pp at $k{=}0.9$), but the three methods exhibit staggered cliffs---L2 earliest ($k{=}0.9{\\to}0.85$, $-$15.4\\,pp), random next, attention latest---each defining a distinct effective compression window before converging at $k{=}0.5$ ($<$4.8\\,pp spread). As task complexity increases, the scoring hierarchy inverts. On Goal, random pruning at $k{=}0.9$ \\emph{exceeds} the unpruned baseline ($+$4.8\\,pp; cross-seed confirmed), suggesting OpenVLA's 256 vision tokens are over-provisioned for goal-conditioned tasks---random removal acts as implicit regularization. On Long, the inversion is complete: at $k{=}0.7$, Random (38.8\\%) $>$ L2 (31.2\\%) $>$ Attention (24.0\\%), with attention degrading $2.5{\\times}$ faster than random. The mechanism is consistent: multi-step tasks distribute critical information across tokens with heterogeneous norm profiles; L2 and attention both cluster on locally salient tokens, sacrificing the spatial diversity that compositional reasoning requires.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_openvla_sweep.pdf}\n\\caption{OpenVLA scoring method comparison across four LIBERO suites. On Object, L2 leads at $k{=}0.9$ ($+$7.8\\,pp) but the margin flips at $k{=}0.85$ ($-$5.2\\,pp, Random wins). Goal degrades smoothly with three-method convergence at $k{=}0.7$. On Long, the ranking inverts with compression. No single scoring method dominates across suites or retention ratios.}\n\\label{fig:openvla_sweep}\n\\end{figure}\n\nThis is a concrete manifestation of the two-axis framework (Section~\\ref{sec:two_axis}): Axis~1 (connector architecture) determines \\emph{whether} pruning is viable; Axis~2 (task complexity) determines \\emph{which} scoring method succeeds. CV remains a valid connector diagnostic, but the optimal scoring strategy requires knowledge of both axes.\n\n\\paragraph{Position encoding mediates the V-shape recovery.}\nThe monotonic L2 curve versus the non-monotonic random curve on $\\pi_{0.5}$ Long (Figure~\\ref{fig:cliff_highlight}) reflects an interaction between token selection strategy and positional encoding. L2 norm scoring preserves spatial locality: retained tokens form near-contiguous clusters in the ViT grid, producing continuous position shifts after re-indexing that Gemma's RoPE accommodates smoothly---hence monotonic degradation (86.8\\% $\\to$ 51.7\\% from $k{=}0.95$ to $k{=}0.5$). Random selection creates scattered gaps that produce position aliasing after re-indexing. At $k{\\approx}0.9$, the aliasing is maximally destructive: a small number of randomly placed gaps create highly irregular inter-token spacing, collapsing SR to 33.6\\%. Per-task analysis reveals this aggregate is driven by specific tasks with position-sensitive spatial reasoning: Task~4 (``put mugs on plates'') drops from 80\\% at $k{=}0.7$ to 12\\% at $k{=}0.85$, contributing disproportionately to the V-shape minimum. At $k{=}0.7$, enough tokens are removed that the surviving positions become approximately uniform again, and SR recovers to 64.6\\%---exceeding the $k{=}0.9$ level by ${\\sim}2{\\times}$. The zero-mask ablation (Section~\\ref{sec:zeromask}) provides causal confirmation: zeroing token content while preserving positions yields 98.0\\% SR, while physically removing the same tokens collapses to 9.0\\%. Position encoding, not information content, is the binding constraint---and scoring method determines whether that constraint is violated.\n\n\\paragraph{Per-task reversal within L2-dominant regimes.} The Long $k{=}0.85$ aggregate ($+$33.2\\,pp for L2) masks extreme per-task heterogeneity (per-task $\\sigma{=}$21.5\\,pp). L2 outperforms random on 9 of 10 tasks ($+$16 to $+$52\\,pp), but on Task~6---a dual-object spatial-relation task (``place white mug on plate \\emph{and} chocolate pudding to the right of plate'')---L2 collapses to 8\\% while random achieves 52\\% ($-$44\\,pp reversal). L2 scoring systematically undervalues tokens encoding spatial relationships, which carry low norms but are critical for relational reasoning. This per-task sign flip within an architecture where L2 dominates overall reinforces that no single scoring method is universally safe: task semantics, not just connector architecture or suite-level statistics, determine optimal strategy.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_scoring_crossover.pdf}\n\\caption{Scoring method comparison at $k{=}0.9$ across three models and four LIBERO suites. Cell color encodes SR as a fraction of unpruned baseline; blue bars mark the best method per condition; dashed borders indicate method-indifferent cells ($\\Delta{<}3.5$\\,pp). $\\pi_{0.5}$'s linear connector strongly favors L2 selection, while X-VLA's BART encoder is largely method-indifferent. SmolVLA collapses to 0\\% regardless of method. Compact 2$\\times$2 summary in Appendix Table~\\ref{tab:scoring_crossover_summary}.}\n\\label{fig:scoring_crossover}\n\\end{figure}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_margin_profile.pdf}\n\\caption{Importance margin (L2 $-$ Random SR) on $\\pi_{0.5}$ Long across retention ratios (multi-seed mean $\\pm$ s.d.; $n{=}5$). The margin peaks sharply at $k{=}0.9$ (46.9\\,pp) where random pruning is maximally destructive, then declines asymmetrically: one step above the peak ($k{=}0.95$: 25.6\\,pp) versus four steps below before crossing zero at $k{\\approx}0.71$. At $k{=}0.5$, L2 and Random converge ($|\\Delta|{\\approx}1.3$\\,pp), indicating that scoring method choice matters only in the moderate-pruning window.}\n\\label{fig:margin_profile}\n\\end{figure}\n\n\\paragraph{Limitations (extended).}\nAll closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\\% official, 44.8\\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.\n\n\\paragraph{Non-monotonicity as structural property.}\nX-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\\% (L2) and 54.0\\% (random), while $k{=}0.9$ recovers to 70.2\\% under L2 selection (Table~\\ref{tab:main_results}). The 0.2\\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.\n\n\\paragraph{$\\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}\nRandom selection on $\\pi_{0.5}$ Object collapses from 74.0\\% at $k{=}0.95$ to 9.0\\% at $k{=}0.9$, then recovers to 74.0\\% at $k{=}0.7$ (Table~\\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\\cite{su2024roformer} encode spatial content at unfamiliar positions, amplifying disruption of learned attention patterns. X-VLA's BART encoder, which redistributes spatial information via cross-attention and lacks RoPE, provides a partial control. At $k{=}0.85$, single-step suites degrade smoothly (Spatial~68.2\\%, Object~65.0\\%, Goal~60.4\\%), but Long drops to 35.0\\%, below its $k{=}0.5$ performance of 61.6\\% (Table~\\ref{tab:xvla_k085_crosssuite}). Random re-indexing thus induces non-monotonic behavior for complex tasks even without RoPE, but RoPE amplifies the reversal: $\\pi_{0.5}$ Object drops to 5.6\\% at $k{=}0.85$ versus 69.4\\% at $k{=}0.5$ ($-$63.8\\,pp), more than double X-VLA Long's $-$26.6\\,pp. The V-shaped recovery at $k \\leq 0.7$ remains unexplained.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Random pruning at $k{=}0.85$: X-VLA (BART encoder) vs.\\ $\\pi_{0.5}$ (linear connector). X-VLA degrades smoothly on single-step suites (60--68\\%) but drops to 35.0\\% on Long (below $k{=}0.5$); $\\pi_{0.5}$ exhibits a severe disruption peak on Object.}\n\\label{tab:xvla_k085_crosssuite}\n\\begin{tabular}{lcccc}\n\\toprule\nSuite & X-VLA SR (\\%) & $\\Delta$ & $\\pi_{0.5}$ SR (\\%) & $\\Delta$ \\\\\n\\midrule\nObject & 65.0 & $-$34.2 & 3.6--5.6\\textsuperscript{$\\dagger$} & $-$93 to $-$95 \\\\\nGoal & 60.4 & $-$38.0 & 52.4 & $-$44.0 \\\\\nSpatial & 68.2 & $-$24.8 & --- & --- \\\\\nLong & 35.0 & $-$59.0 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize\\textsuperscript{$\\dagger$}Two seeds: seed42$\\,{=}\\,$5.6\\% (post-fix), seed43$\\,{=}\\,$3.6\\%. $\\Delta$ from respective baselines.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Small-$N$ interactions.}\nX-VLA operates with only 50 vision tokens. At $k{=}0.95$, removing 3 tokens produces $-$44.6\\,pp on Goal and $-$47.0\\,pp on Long (L2 norm selection). Absolute token count interacts with CV: identical retention ratios impose qualitatively different damage when the token budget is small.\n\n\\paragraph{Design implications.}\nPractitioners should compute importance CV before deploying token pruning, as low-CV and entangling-connector models require distinct compression strategies. Pixel-shuffle connectors need learned re-encoding rather than hard deletion. Task complexity must factor into pruning budget decisions: retention ratios safe for simple manipulation may fail on compositional tasks.\n\n\n\\section{Cross-Suite Task Complexity Analysis}\n\\label{app:cross_suite_extended}\n\nLIBERO's four suites form a complexity gradient: Object and Spatial require single-step manipulation with explicit spatial cues, while Goal and Long demand multi-step planning, goal inference, or extended temporal coordination. This gradient interacts with pruning tolerance in a connector-dependent manner.\n\n$\\pi_{0.5}$ shows moderate complexity amplification under L2 norm pruning at $k{=}0.95$: Object retains 98.2\\% (matching the baseline), Spatial retains 97.8\\% (within noise of the 97.2\\% baseline), and Goal drops to 89.4\\% ($-$7.0\\,pp from 96.4\\%). Simple tasks absorb mild pruning with negligible loss; compositional tasks expose measurable degradation even at 5\\% token removal.\n\nX-VLA exhibits dramatic complexity amplification. At $k{=}0.9$ with L2 norm selection, Object retains 97.6\\% ($-$1.6\\,pp from the 99.2\\% baseline), while Goal drops to 70.2\\% ($-$28.2\\,pp from 98.4\\% baseline). Under random pruning at the same ratio, Object loses just 1.4\\,pp (97.8\\%) while Goal loses 27.8\\,pp (70.6\\%), a $20{\\times}$ amplification. The effect is even more pronounced at $k{=}0.95$ on Long: removing just 3 of 50 tokens collapses SR from 94.0\\% to 47.0\\% (L2) and 48.2\\% (random), a 47.0\\,pp loss with only 1.2\\,pp method gap, while Object at the same ratio loses only 0.2\\,pp.\n\nToken-entangling connectors (X-VLA's BART encoder) amplify task complexity because compositional tasks require integrating information across spatial locations. When the BART encoder creates cross-token dependencies, removing even a few tokens disrupts the distributed representations that multi-step tasks rely on. Token-independent connectors ($\\pi_{0.5}$'s linear projection, OpenVLA's MLP) show moderate complexity amplification because each token's contribution is self-contained: removing tokens reduces spatial coverage proportionally, and simple tasks tolerate the resulting gaps.\n\n\n\\section{Pruning Protocol Details}\n\\label{app:pruning_details}\n\nBoth pruning methods physically remove unselected tokens from the sequence, reducing the actual input length to the LLM rather than zeroing them out; zero-masking preserves positional structure while physical removal does not. After removal, remaining tokens retain their original spatial ordering; position IDs are re-indexed contiguously.\n\nModel-specific retention ratios reflect each architecture's token count and expected sensitivity. $\\pi_{0}$ is evaluated offline only ($k{=}0.1$, normalized L1 action loss; offline metrics only, no closed-loop evaluation available) because its deployment environment precludes closed-loop testing. $\\pi_{0.5}$ uses $k \\in \\{0.3, 0.5, 0.7\\}$ under both L2 and random removal; the dual-method design enables direct comparison within a single architecture. Pruning is applied per-image: each camera view independently retains the top-$k$ fraction. X-VLA spans $k \\in \\{0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95\\}$ with L2 removal across three seeds, supplemented by random removal at selected $k$ values. OpenVLA uses $k \\in \\{0.3, 0.5, 0.7, 0.9, 0.95\\}$ with random removal as the primary protocol and L2 for direct comparison. SmolVLA tests seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.5, 0.7, 0.9, 0.95\\}$), and mechanism (zero-masking, true removal, token merging via ToMe~\\cite{bolya2023tome}).\n\nThe $\\pi_{0}$--OpenVLA pair provides the closest available comparison: both consume 256 vision tokens from SigLIP-based encoders, but differ in connector (linear projection vs.\\ three-layer MLP), backbone (PaliGemma vs.\\ Llama-2), and encoder fusion strategy (single SigLIP vs.\\ DINOv2+SigLIP). This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation; the primary evidence for the connector's role comes from the monotonic CV-degradation relationship across all six architectures (Section~\\ref{sec:cv_sensitivity}). Retention ratio $k$ controls the fraction retained within each model, but absolute token counts vary across architectures at matched $k$: $k{=}0.7$ retains 35 tokens for X-VLA, 179 for OpenVLA, and 538 for $\\pi_{0.5}$. The CV analysis derives from within-model comparisons where each model serves as its own control, eliminating this confounder.\n\n\n\\section{SmolVLA Pruning Ablation}\n\\label{app:smolvla_ablation}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA pruning ablation on LIBERO-Object. All configurations collapse to 0\\% SR. Two independent evaluations of the official HF checkpoint (59.2\\% and 57.2\\% baseline, within CI) confirm the cliff-edge across scoring methods.}\n\\label{tab:smolvla_ablation}\n\\begin{tabular}{llccrr}\n\\toprule\nScoring & $k$ & Mechanism & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 44.8 & 500 & [40.5, 49.2] \\\\\n\\midrule\nACIS & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.70 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.90 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.95 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nRandom & 0.50 & Zero-mask & 0.0 & 500 & [0, 0.76] \\\\\nACIS & 0.50 & True removal & 0.0 & 500 & [0, 0.80] \\\\\nACIS & 0.50 & Merge (ToMe) & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol A (59.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 59.2 & 500 & [54.8, 63.4] \\\\\nRandom & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Official checkpoint, eval protocol B (57.2\\% baseline)}} \\\\\n\\multicolumn{2}{l}{\\textit{Baseline (bypass)}} & -- & 57.2 & 500 & [52.9, 61.4] \\\\\nRandom & 0.95 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.90 & True removal & 0.0 & 500 & [0, 0.76] \\\\\nL2 norm & 0.50 & True removal & 0.0 & 500 & [0, 0.76] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task Breakdown Tables}\n\\label{app:per_task}\n\n\\subsection{SmolVLA Baseline Per-Task Results}\n\nTable~\\ref{tab:smolvla_baseline_pertask} reports per-task success rates for the SmolVLA baseline (bypass mode, no pruning) on LIBERO-Object. All pruning conditions (Table~\\ref{tab:smolvla_ablation}) produce 0\\% success rate on every task; we omit per-task breakdowns for pruning conditions as they carry no additional information beyond the aggregate 0\\% already reported.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object (50 episodes per task, 500 total). Overall SR: 44.8\\%.}\n\\label{tab:smolvla_baseline_pertask}\n\\begin{tabular}{lc}\n\\toprule\nTask & SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 22 \\\\\nbbq\\_sauce & 60 \\\\\nbutter & 42 \\\\\nchocolate\\_pudding & 38 \\\\\ncream\\_cheese & 58 \\\\\nketchup & 26 \\\\\nmilk & 62 \\\\\norange\\_juice & 38 \\\\\nsalad\\_dressing & 50 \\\\\ntomato\\_sauce & 52 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{44.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Official SmolVLA Checkpoint Per-Task Results}\n\nTable~\\ref{tab:smolvla_official_pertask} reports per-task success rates for the official SmolVLA LIBERO checkpoint (HuggingFaceVLA/smolvla\\_libero). Under 50\\% random token removal, all tasks produce 0\\% SR, identical to the fine-tuned checkpoint results.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Official SmolVLA checkpoint per-task success rates on LIBERO-Object (eval protocol A; 50 episodes per task, 500 total). Overall SR: 59.2\\%. Under 50\\% random pruning, all tasks collapse to 0\\%. An independent evaluation (protocol B) yields 57.2\\% baseline with identical cliff-edge (Table~\\ref{tab:smolvla_ablation}).}\n\\label{tab:smolvla_official_pertask}\n\\begin{tabular}{lcc}\n\\toprule\nTask & Baseline SR (\\%) & $k{=}0.5$ SR (\\%) \\\\\n\\midrule\nalphabet\\_soup & 64 & 0 \\\\\nbbq\\_sauce & 38 & 0 \\\\\nbutter & 78 & 0 \\\\\nchocolate\\_pudding & 90 & 0 \\\\\ncream\\_cheese & 40 & 0 \\\\\nketchup & 60 & 0 \\\\\nmilk & 52 & 0 \\\\\norange\\_juice & 80 & 0 \\\\\nsalad\\_dressing & 44 & 0 \\\\\ntomato\\_sauce & 46 & 0 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{59.2} & \\textbf{0.0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Per-Task Results Under Pruning}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA per-task success rates (\\%) on LIBERO-Object under random token removal across five retention ratios (50 episodes per task). Baseline overall SR: 74.0\\%. Tasks requiring fine-grained discrimination (butter, cream\\_cheese) degrade earliest; visually distinctive targets (orange\\_juice, salad\\_dressing) are most resilient.}\n\\label{tab:openvla_pertask}\n\\begin{tabular}{lccccc}\n\\toprule\nTask & $k{=}0.95$ & $k{=}0.90$ & $k{=}0.70$ & $k{=}0.50$ & $k{=}0.30$ \\\\\n\\midrule\nalphabet\\_soup & 76 & 70 & 74 & 60 & 14 \\\\\nbbq\\_sauce & 38 & 28 & 46 & 44 & 30 \\\\\nbutter & 84 & 76 & 10 & 2 & 0 \\\\\nchocolate\\_pudding & 54 & 56 & 32 & 40 & 10 \\\\\ncream\\_cheese & 84 & 78 & 18 & 8 & 0 \\\\\nketchup & 82 & 70 & 68 & 50 & 30 \\\\\nmilk & 46 & 42 & 40 & 24 & 8 \\\\\norange\\_juice & 74 & 60 & 76 & 72 & 42 \\\\\nsalad\\_dressing & 64 & 54 & 64 & 36 & 64 \\\\\ntomato\\_sauce & 92 & 86 & 62 & 38 & 8 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{69.4} & \\textbf{62.0} & \\textbf{49.0} & \\textbf{37.4} & \\textbf{20.6} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{OpenVLA Full Degradation Curve}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA success rates on LIBERO-Object under random token removal at six retention ratios (50 episodes per task, 500 total per ratio). Baseline SR: 74.0\\%. All confidence intervals are Wilson 95\\%.}\n\\label{tab:openvla_full}\n\\begin{tabular}{ccrr}\n\\toprule\n$k$ & Tokens Retained & SR (\\%) & Wilson 95\\% CI \\\\\n\\midrule\n1.00 (baseline) & 256 & 74.0 & [69.9, 77.7] \\\\\n0.95 & 243 & 69.4 & [65.2, 73.3] \\\\\n0.90 & 230 & 62.0 & [57.7, 66.2] \\\\\n0.70 & 179 & 49.0 & [44.6, 53.4] \\\\\n0.50 & 128 & 37.4 & [33.3, 41.7] \\\\\n0.30 & 77 & 20.6 & [17.2, 24.4] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ LIBERO-Long Five-Seed Results}\n\\label{app:pi05_long_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ LIBERO-Long success rates (\\%) across five seeds (500 episodes each). All values are means over seeds 42--46 with sample standard deviation (ddof$\\,{=}\\,$1). The importance margin (L2$-$Random) peaks at $k{=}0.9$ (46.9\\,pp) and crosses zero near $k{\\approx}0.71$. Maximum per-seed range is 5.8\\,pp (L2, $k{=}0.75$).}\n\\label{tab:pi05_long_multiseed}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & L2 Norm (\\%) & Random (\\%) & Attention (\\%) \\\\\n\\midrule\n0.95 & $86.8 \\pm 0.8$ & $61.2 \\pm 0.7$ & $77.3 \\pm 1.2$ \\\\\n0.90 & $80.4 \\pm 0.5$ & $33.6 \\pm 1.2$ & $64.2 \\pm 1.0$ \\\\\n0.85 & $78.1 \\pm 1.0$ & $44.9 \\pm 1.3$ & $50.8 \\pm 1.3$ \\\\\n0.75 & $70.6 \\pm 2.7$ & $63.0 \\pm 1.7$ & $51.4 \\pm 1.2$ \\\\\n0.70 & $63.2 \\pm 1.5$ & $64.6 \\pm 1.8$ & $53.0 \\pm 1.1$ \\\\\n0.50 & $51.7 \\pm 1.5$ & $50.4 \\pm 0.6$ & $49.4 \\pm 1.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ L2 Norm Multi-Seed Consistency}\n\\label{app:pi05_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ L2 norm-based removal across two seeds (500 episodes each). The V-shaped curve is reproduced with near-identical valleys ($\\sigma{=}0.1$\\,pp at $k{=}0.5$). V-depth: 17.6\\,pp (seed42), 21.8\\,pp (seed43).}\n\\label{tab:pi05_l2_multiseed}\n\\begin{tabular}{ccccc}\n\\toprule\n$k$ & Seed 42 (\\%) & Seed 43 (\\%) & Mean $\\pm$ Std & $\\Delta$ (pp) \\\\\n\\midrule\n0.70 & 55.0 & 57.8 & $56.4 \\pm 2.0$ & $+$2.8 \\\\\n0.50 & 33.4 & 33.6 & $33.5 \\pm 0.1$ & $+$0.2 \\\\\n0.30 & 51.0 & 55.4 & $53.2 \\pm 3.1$ & $+$4.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$\\pi_{0.5}$ Cross-Suite Comparison}\n\\label{app:pi05_crosssuite}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ pruning across LIBERO-Object (baseline 98.2\\%) and LIBERO-Spatial (baseline 97.2\\%), seed\\,42, 500 episodes each. Object random exhibits a deep cliff at $k \\in [0.85, 0.925]$ absent on Spatial; L2 norm maintains a plateau across suites at high retention ($\\leq 2.4$\\,pp difference at $k \\geq 0.85$).}\n\\label{tab:pi05_crosssuite}\n\\begin{tabular}{ccccc}\n\\toprule\n\\multirow{2}{*}{$k$} & \\multicolumn{2}{c}{LIBERO-Object (\\%)} & \\multicolumn{2}{c}{LIBERO-Spatial (\\%)} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & L2 Norm & Random & L2 Norm & Random \\\\\n\\midrule\n1.00 & 98.2 & 98.2 & 97.2 & 97.2 \\\\\n0.95 & 98.2 & 74.0 & 97.8 & 76.4 \\\\\n0.925 & 99.2 & 27.6 & 97.0 & 60.4 \\\\\n0.90 & 98.2 & 9.0 & 95.0 & 54.6 \\\\\n0.85 & 98.0 & 5.6 & 90.4 & 58.4 \\\\\n0.70 & 55.0 & 74.0 & 67.0 & 74.4 \\\\\n0.50 & 33.4 & 69.4 & 55.6 & 71.6 \\\\\n0.30 & 51.0 & 36.4 & 57.2 & 49.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_crosssuite.pdf}\n\\caption{$\\pi_{0.5}$ cross-suite pruning profiles. Object random (green solid) exhibits a deep cliff at $k \\in [0.85, 0.925]$ with 68\\,pp recovery, absent on Spatial (blue solid). L2 norm (dashed) maintains a plateau on both suites through the cliff zone.}\n\\label{fig:crosssuite}\n\\end{figure}\n\nThe random cliff at $k \\in [0.85, 0.925]$ is task-specific: Object collapses from 74.0\\% ($k{=}0.95$) to 5.6\\% ($k{=}0.85$), whereas Spatial retains 58.4\\% at $k{=}0.85$ ($\\Delta{=}53$\\,pp between suites). Spatial random also exhibits mild non-monotonicity ($k{=}0.925$: 60.4\\% $>$ $k{=}0.9$: 54.6\\%, $\\Delta{=}5.8$\\,pp), but this is an order of magnitude smaller than Object's 68\\,pp V-dip. The cliff pattern suggests Object manipulation concentrates critical information in specific token subsets whose removal is catastrophic at narrow retention bands; Spatial tasks distribute critical information more uniformly, tolerating moderate random removal without catastrophic failure.\n\nL2 norm selection is consistent across suites at high retention ($k \\geq 0.85$): Object and Spatial differ by $\\leq 2.4$\\,pp (Table~\\ref{tab:pi05_crosssuite}). At $k \\leq 0.7$, both suites exhibit the L2 V-shape (Object valley: 33.4\\% at $k{=}0.5$; Spatial valley: 55.6\\% at $k{=}0.5$), with Spatial maintaining higher absolute SR throughout. The method preference (random $>$ L2 at $k{=}0.5$; L2 $>$ random at $k{=}0.3$) is consistent across the two suites tested, suggesting the CV-strategy interaction may extend beyond a single task distribution.\n\n\\subsection{Token Importance Spatial Distribution}\n\\label{app:token_heatmap}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_token_heatmap.pdf}\n\\caption{$\\pi_{0.5}$ token importance spatial distribution (16$\\times$16 grid, averaged over timesteps). Left: LIBERO-Object shows a pronounced center-high, edge-low pattern (center rows 7--9: norm $\\sim$265--267; edge rows 0, 14--15: norm $\\sim$235--236; CV${=}$0.066). Right: LIBERO-Spatial exhibits a flatter distribution (center-edge gap 14.67 vs.\\ 21.87; CV${=}$0.059). The 33\\% center-edge gap difference quantitatively explains Object's sharp cliff versus Spatial's graceful degradation under random removal.}\n\\label{fig:token_heatmap}\n\\end{figure}\n\nToken importance heatmaps reveal that $\\pi_{0.5}$'s 768 vision tokens (reshaped to a 16$\\times$16 spatial grid after the $\\sqrt{d}$-scaled linear projection) exhibit a center-high, edge-low L2 norm pattern. At $k{=}0.9$ (26 tokens removed), L2 norm-based selection discards predominantly edge tokens: 50\\% of removed tokens fall in the outermost ring despite edge positions comprising only 23\\% of the grid. This spatial concentration is consistent with the center tokens encoding the robot arm and target object, while edge tokens capture less task-relevant background.\n\nRandom removal at the same ratio samples deletions uniformly across the spatial grid, creating a combinatorial probability of simultaneously removing multiple high-importance center tokens. As more tokens are removed ($k{=}0.925 \\to 0.85$), this probability increases sharply, consistent with the observed cliff onset. The asymmetry explains why L2 norm selection maintains a near-baseline plateau through the cliff zone: it preferentially preserves the high-importance center region that random removal disrupts by chance.\n\n\\subsection{Hypergeometric Cliff Model}\n\\label{app:cliff_model}\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{figures/paper/fig_cliff_model.pdf}\n\\caption{Hypergeometric cliff model for $\\pi_{0.5}$ Object random pruning. (a)~Model-predicted collapse probability (dashed) vs.\\ observed success rate (solid) across the cliff zone $k \\in [0.85, 0.95]$; RMSE${=}$0.025. (b)~$P(\\text{collapse})$ curves for Object ($C{=}91$, concentrated) and Spatial ($C \\approx 5$, distributed), illustrating why Object exhibits a sharp phase transition absent on Spatial.}\n\\label{fig:cliff_model}\n\\end{figure}\n\nThe random cliff on $\\pi_{0.5}$ Object (Section~\\ref{app:cross_suite_extended}) can be modeled as a hypergeometric sampling problem. Among $N{=}768$ vision tokens, $C{=}106$ are critical. $C$ and $T$ are jointly fit by minimizing RMSE against three cliff-zone data points ($k \\in \\{0.9, 0.925, 0.95\\}$; all post-fix confirmed). When $\\lfloor N(1{-}k) \\rfloor$ tokens are removed uniformly at random, the number of critical tokens removed follows a hypergeometric distribution $\\mathrm{Hypergeometric}(N, C, \\lfloor N(1{-}k) \\rfloor)$. We define performance collapse as removing $\\geq T{=}7$ critical tokens simultaneously; the fit yields $C{=}106$, $T{=}7$ with RMSE${=}$0.018. The fitted $C{=}106$ (13.8\\% of tokens) is broadly consistent with the top-importance center region identified in the token heatmap (Figure~\\ref{fig:token_heatmap}), providing post-hoc interpretability: the ``critical tokens'' correspond to spatially concentrated, high-norm positions encoding the robot arm and target object.\n\nThe model predicts three characteristic retention ratios: $k{=}0.960$ where $P(\\text{collapse}){=}10\\%$ (cliff onset), $k{=}0.937$ where $P(\\text{collapse}){=}50\\%$ (midpoint), and $k{=}0.904$ where $P(\\text{collapse}){=}90\\%$ (near-complete collapse). The cliff width $\\Delta k \\approx 0.056$ between 10\\% and 90\\% collapse probability matches the observed transition from 74.0\\% SR ($k{=}0.95$) to 9.0\\% SR ($k{=}0.90$). At $k{=}0.85$ the model predicts near-certain collapse ($P{>}0.999$), consistent with the observed 5.6\\% SR. The model captures the cliff onset and sharpness but does not explain the V-shape recovery at $k \\leq 0.7$, where success rate rebounds to 74.0\\%. The recovery lies outside the model's scope (which assumes monotonic collapse probability). We hypothesize that at aggressive pruning the model transitions to a qualitatively different computation regime, potentially relying on coarser spatial features that survive uniform subsampling, but this remains untested.\n\nThe cross-suite difference emerges naturally from the critical token count. Object manipulation concentrates critical information in $C{=}106$ tokens (13.8\\% of the grid), creating a steep increase in $P(\\text{collapse} \\geq T)$ over a narrow $k$ range. Spatial tasks distribute critical information across approximately $C \\approx 5$ tokens, making the probability of simultaneously removing $\\geq T$ critical tokens negligible at all tested retention ratios, consistent with Spatial's graceful degradation (58.4\\% at $k{=}0.85$ vs.\\ Object's 5.6\\%).\n\n\\subsection{OpenVLA Multi-Seed Consistency}\n\\label{app:openvla_multiseed}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA success rates (\\%) on LIBERO-Object under random token removal across two seeds (500 episodes each). All values are within 5\\,pp, confirming the graded degradation curve is reproducible. Main text (Table~\\ref{tab:main_results}) uses seed 42 for both L2 and random.}\n\\label{tab:openvla_multiseed}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & Seed 7 (\\%) & Seed 43 (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n0.90 & 62.0 & 62.2 & $+$0.2 \\\\\n0.70 & 49.0 & 44.4 & $-$4.6 \\\\\n0.50 & 37.4 & 35.6 & $-$1.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{L2 Norm vs.\\ Random Scoring on OpenVLA}\n\\label{app:l2_vs_random}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{OpenVLA cross-seed comparison on LIBERO-Object (500 episodes per configuration). L2 uses seed$\\,{=}\\,$42; random uses seed$\\,{=}\\,$7. Main text (Table~\\ref{tab:main_results}) reports seed-42 random where available ($k{=}0.9$: 62.8\\%, $k{=}0.5$: 35.8\\%). Same-seed (seed42) random at $k{=}0.3$ yields 21.4\\% (L2 outperforms by 3.6\\,pp); same-seed at $k{=}0.7$ yields 44.4\\% (L2 outperforms by 5.4\\,pp). $\\Delta$ is defined as L2$-$Random (positive indicates L2 advantage).}\n\\label{tab:openvla_l2_vs_random}\n\\begin{tabular}{cccc}\n\\toprule\n$k$ & L2 Norm SR (\\%) & Random SR (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n0.95 & 70.6 & 69.4 & $+$1.2 \\\\\n0.90 & 70.6 & 62.0 & $+$8.6 \\\\\n0.70 & 49.8 & 49.0 & $+$0.8 \\\\\n0.50 & 39.2 & 37.4 & $+$1.8 \\\\\n0.30 & 25.0 & 20.6 & $+$4.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{X-VLA Cliff Localization: Per-Task Analysis}\n\\label{app:xvla_cliff}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{X-VLA per-task success rates (\\%) at $k{=}0.80$ (40 of 50 tokens) and $k{=}0.85$ (42 of 50 tokens) on LIBERO-Object. Per-task breakdown is mean of 2 seeds (50 episodes per task per seed, 100 total); overall values are confirmed across 3 seeds ($89.0 \\pm 0.7$\\% at $k{=}0.80$, $67.9 \\pm 0.3$\\% at $k{=}0.85$). Despite retaining \\emph{fewer} tokens, $k{=}0.80$ outperforms $k{=}0.85$ by 21.1\\,pp overall. Four tasks (\\textbf{bold}) suffer catastrophic interference ($\\Delta \\leq -50$\\,pp) from two additional low-importance tokens (L2 rank 41--42 of 50) at $k{=}0.85$; the remaining six are unaffected ($|\\Delta| \\leq 10$\\,pp). Cross-seed variance is $\\leq 4$\\,pp per task.}\n\\label{tab:xvla_cliff_pertask}\n\\begin{tabular}{lccr}\n\\toprule\nTask & $k{=}0.80$ (\\%) & $k{=}0.85$ (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nalphabet\\_soup & 100.0 & 100.0 & 0 \\\\\nbbq\\_sauce & 85.0 & 87.0 & $+$2 \\\\\n\\textbf{butter} & \\textbf{57.0} & \\textbf{0.0} & $\\boldsymbol{-57}$ \\\\\n\\textbf{chocolate\\_pudding} & \\textbf{88.0} & \\textbf{35.0} & $\\boldsymbol{-53}$ \\\\\n\\textbf{cream\\_cheese} & \\textbf{98.0} & \\textbf{45.0} & $\\boldsymbol{-53}$ \\\\\n\\textbf{ketchup} & \\textbf{79.0} & \\textbf{27.0} & $\\boldsymbol{-52}$ \\\\\nmilk & 85.0 & 95.0 & $+$10 \\\\\norange\\_juice & 96.0 & 98.0 & $+$2 \\\\\nsalad\\_dressing & 100.0 & 100.0 & 0 \\\\\ntomato\\_sauce & 98.0 & 91.0 & $-$7 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{89.0} & \\textbf{67.9} & $\\boldsymbol{-21.1}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe non-monotonic pattern is reproducible across both seeds: the same four tasks (butter, chocolate\\_pudding, cream\\_cheese, ketchup) exhibit catastrophic drops at $k{=}0.85$, while the remaining six maintain or improve performance. This task-specific sensitivity is consistent with the BART encoder creating entangled dependencies among marginal tokens: at $k{=}0.85$, two additional low-importance tokens (L2 rank 41--42) introduce interference that selectively disrupts tasks requiring fine-grained spatial discrimination. The four affected tasks all involve small, visually similar grocery items, while the robust tasks (alphabet\\_soup, salad\\_dressing) feature distinctive objects or high-contrast targets.\n\n\\subsection{VTR Per-Task Comparison}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR per-task success rates on LIBERO-Object for $M \\in \\{32, 64, 128\\}$ (seed 42; 3-seed means are reported in Table~\\ref{tab:vtr_results}). All three achieve similar overall SR (59.8\\%--61.6\\%), but individual task performance varies substantially across configurations, with per-task differences up to 30 percentage points.}\n\\label{tab:smart_compress_pertask}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & $M{=}32$ (\\%) & $M{=}64$ (\\%) & $M{=}128$ (\\%) \\\\\n\\midrule\nalphabet\\_soup & 68 & 74 & 62 \\\\\nbbq\\_sauce & 46 & 56 & 34 \\\\\nbutter & 82 & 84 & 82 \\\\\nchocolate\\_pudding & 90 & 74 & 82 \\\\\ncream\\_cheese & 64 & 38 & 58 \\\\\nketchup & 66 & 64 & 62 \\\\\nmilk & 76 & 62 & 56 \\\\\norange\\_juice & 28 & 46 & 58 \\\\\nsalad\\_dressing & 60 & 64 & 54 \\\\\ntomato\\_sauce & 36 & 54 & 50 \\\\\n\\midrule\n\\textbf{Overall} & \\textbf{61.6} & \\textbf{61.6} & \\textbf{59.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{VTR Multi-Seed Results}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR success rates across three seeds on LIBERO-Object (500 episodes each). Mean $\\pm$ std reported.}\n\\label{tab:multi_seed}\n\\begin{tabular}{lccccr}\n\\toprule\n$M$ & Seed 42 & Seed 43 & Seed 44 & Mean $\\pm$ Std \\\\\n\\midrule\n32 & 61.6 & 59.2 & 59.6 & 60.1 $\\pm$ 1.3 \\\\\n64 & 61.6 & 60.0 & 64.4 & 62.0 $\\pm$ 2.3 \\\\\n96 & 52.6 & 58.2 & 52.8 & 54.5 $\\pm$ 3.2 \\\\\n128 & 59.8 & 54.0 & 60.2 & 58.0 $\\pm$ 3.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{VTR Full Results}\n\\label{app:vtr_full}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (passthrough) within 1.1\\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}\n\\label{tab:vtr_results}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compression & SR (\\%) \\\\\n\\midrule\n\\textit{SmolVLA-Base (LoRA)} & 128 & 0\\% & 44.8 \\\\\n\\textit{SmolVLA official} & 128 & 0\\% & 59.2 \\\\\n\\textit{Baseline control (+100K steps)} & 128 & 0\\% & 45.0 \\\\\n\\textit{Hard pruning (any $k$)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 64 & 50\\% & \\textbf{62.0 $\\pm$ 2.2} \\\\\nCross-attn VTR & 96 & 25\\% & 54.5 $\\pm$ 3.2 \\\\\nCross-attn VTR & 128 & 0\\% & 58.0 $\\pm$ 3.5 \\\\\n\\midrule\nMLP adapter ($\\sim$22M) & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Full VTR Ablation}\n\\label{app:smart_compress_full}\n\nTable~\\ref{tab:smart_compress_full} reports all five VTR configurations. The cross-attention module improves performance regardless of compression: $M \\in \\{32, 64, 128\\}$ all achieve $\\sim$60\\% SR, exceeding the 44.8\\% baseline by 15--17 points ($p < 0.001$, two-proportion $z$-test). Only at $M = 16$ (87.5\\% compression) does performance decline modestly to 55.8\\%, still 11 points above baseline. The $M{=}96$ dip (mean 54.5\\% across three seeds, Table~\\ref{tab:multi_seed}) may reflect an intermediate bottleneck that introduces representational redundancy without the regularization benefit of stronger compression ($M{=}32$, $M{=}64$).\n\nTable~\\ref{tab:cross_suite} reports performance across task suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long. On LIBERO-Spatial, VTR achieves 53.2\\% SR (vs.\\ 0\\% under hard pruning); on LIBERO-Goal, 56.4\\% SR ($-6.6$pp from the 63.0\\% unpruned baseline, vs.\\ 0\\% under pruning). The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures even within the training distribution. Per-task results are in Table~\\ref{tab:smart_compress_pertask}.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Full VTR ablation on LIBERO-Object across five compression levels. $M{=}32$ and $M{=}64$ achieve similar SR ($\\sim$60\\%); $M{=}96$ shows a modest dip; the $M{=}128$ passthrough confirms the gain originates from re-encoding.}\n\\label{tab:smart_compress_full}\n\\begin{tabular}{lcccrr}\n\\toprule\nMethod & $M$ & Reduction & SR (\\%) & Episodes & Wilson 95\\% CI \\\\\n\\midrule\n\\textit{Baseline} & 128 & 0\\% & 44.8 & 500 & [40.5, 49.2] \\\\\n\\textit{Extended training} & -- & -- & 45.0 & 500 & [40.7, 49.3] \\\\\n\\textit{Hard pruning} & -- & 50--90\\% & 0.0 & 500+ & [0, 0.76] \\\\\n\\midrule\nVTR & 128 & 0\\% & 58.0 & 1500 & $\\pm$3.5 \\\\\nVTR & 96 & 25\\% & 52.6 & 500 & [48.2, 56.9] \\\\\nVTR & 64 & 50\\% & 61.6 & 500 & [57.3, 65.8] \\\\\nVTR & 32 & 75\\% & 61.6 & 500 & [57.3, 65.8] \\\\\nVTR & 16 & 87.5\\% & 55.8 & 500 & [51.4, 60.1] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize $M{=}128$ reports mean $\\pm$ std over 3 seeds (500 episodes each). Other VTR rows report single seed (seed 42) with Wilson 95\\% CI. See Table~\\ref{tab:multi_seed} for full multi-seed results.}\n\\end{table}\n\n\n\\section{VTR Evaluation Across Task Suites}\n\\label{app:cross_suite}\n\nTable~\\ref{tab:cross_suite} reports the performance of VTR ($M{=}32$) across three LIBERO suites. All suites are in-distribution: the training set (HuggingFaceVLA/libero) covers Object, Spatial, Goal, and Long (40 tasks, 1693 episodes total). On LIBERO-Goal, performance drops from 63.0\\% to 56.4\\% ($-6.6$pp). On LIBERO-Spatial, VTR achieves 53.2\\% SR, where the official SmolVLA checkpoint scores 43.8\\% and hard pruning yields near-zero (0.6\\%). While 53.2\\% nominally exceeds the official Spatial baseline, this difference concentrates in two of ten tasks (+44pp and +48pp respectively); the remaining eight tasks show a net difference of only +0.2pp. We therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline. The qualitative pattern (cliff-edge vulnerability and re-encoding recovery) extends across the three tested task structures within the training distribution. The LIBERO-Goal decline indicates that re-encoding benefits vary across task structures.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR ($M{=}32$) evaluation across LIBERO task suites. All suites are in-distribution (training covers Object, Spatial, Goal, Long). Hard pruning (any method, $k{=}0.50$) produces 0\\% or near-zero on all suites.}\n\\label{tab:cross_suite}\n\\begin{tabular}{lccc}\n\\toprule\nSuite & Baseline (unpruned) & VTR $M{=}32$ & Hard Pruning $k{=}0.50$ \\\\\n\\midrule\nObject & 44.8\\% & 61.6\\% & 0\\% \\\\\nSpatial & 51.8\\% & 53.2\\% & 0.6\\% \\\\\nGoal & 63.0\\% & 56.4\\% & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{VTR Training Details}\n\\label{app:smart_compress_details}\n\nThe VTR module is a cross-attention pooling layer inserted between SmolVLA's pixel-shuffle vision connector and the SmolLM2 language backbone. It consists of $M$ learned query vectors that attend over the 128 vision tokens through standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compressor adds 22.2M trainable parameters (approximately 5\\% of SmolVLA's 450M total). Training is end-to-end: compressor and VLA policy parameters are jointly optimized.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{VTR training hyperparameters. All configurations ($M \\in \\{16, 32, 64, 96, 128\\}$) use identical procedures; only the number of query vectors differs.}\n\\label{tab:training_hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nHyperparameter & Value \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Model}} \\\\\n\\quad Base checkpoint & SmolVLA-Base (pretrained, before LIBERO fine-tuning) \\\\\n\\quad Compressor architecture & Cross-attention, 2 layers, 12 heads, dropout 0.1 \\\\\n\\quad Compressor parameters & 22.2M \\\\\n\\quad Total trainable parameters & 122.1M / 472.2M (25.85\\%) \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Optimization}} \\\\\n\\quad Optimizer & AdamW ($\\beta_1{=}0.9$, $\\beta_2{=}0.95$, weight decay $10^{-10}$) \\\\\n\\quad Learning rate & $10^{-4}$ \\\\\n\\quad Schedule & Linear warmup (1K steps, start factor 0.01) $\\to$ cosine \\\\\n\\quad & annealing ($\\eta_{\\min}{=}2.5 \\times 10^{-6}$) \\\\\n\\quad Max gradient norm & 10.0 \\\\\n\\quad Total training steps & 100,000 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Data \\& batching}} \\\\\n\\quad Dataset & HuggingFaceVLA/libero (40 tasks, 1693 episodes across \\\\\n\\quad & Object, Spatial, Goal, Long suites) \\\\\n\\quad Batch size & 4 (no gradient accumulation)$^\\dagger$ \\\\\n\\quad Num workers & 4 \\\\\n\\quad Eval interval & every 5K steps \\\\\n\\quad Checkpoint interval & every 1K steps \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Hardware \\& runtime}} \\\\\n\\quad Hardware & 1$\\times$ NVIDIA RTX 4090 D (24GB) \\\\\n\\quad Precision & fp32 (no mixed precision) \\\\\n\\quad Wall clock & $\\sim$6h 43m per configuration \\\\\n\\quad Training speed & 4.1 samples/sec \\\\\n\\quad Seed & 42 (seeds 43, 44 for multi-seed runs) \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{$M=32$ final metrics}} \\\\\n\\quad Train action loss & 0.11 \\\\\n\\quad Eval action loss & 0.052 \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{$M=64$ final metrics}} \\\\\n\\quad Train action loss & 0.045 \\\\\n\\quad Eval action loss & 0.062 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{2pt}\n{\\footnotesize $^\\dagger$The official SmolVLA checkpoint uses batch size 64 across 8 GPUs (effective batch size 512). Our batch size 4 on a single GPU contributes to the lower baseline SR (44.8\\% vs.\\ 87.3\\%). All VTR configurations and the extended training control use this same batch size for fair comparison.}\n\\end{table}\n\nThe loss profile differs between configurations: $M=32$ has higher train loss (0.11 vs.\\ 0.045) but lower eval loss (0.052 vs.\\ 0.062), consistent with the smaller bottleneck acting as a stronger regularizer. Despite this loss difference, both achieve identical closed-loop success rates (61.6\\%), reinforcing the finding that offline loss does not predict closed-loop performance (Section~\\ref{sec:metric_disconnect}).\n\n\\subsection{MLP Adapter Control}\n\\label{app:mlp_adapter}\n\nTo verify that re-encoding effectiveness is not specific to cross-attention, we train a parameter-matched MLP adapter as a control. The adapter is a 3-layer feed-forward network with expansion ratio 4 (hidden dimension $4 \\times d_{\\text{model}}$), using average pooling for token reduction from 128 to $M$ tokens. Total parameters: 22.14M, matched to the cross-attention module's 22.2M. Training follows the identical protocol as VTR: SmolVLA-Base checkpoint, 100K steps, learning rate $10^{-4}$, batch size 4, same LIBERO dataset. At $M = 32$ (75\\% reduction), the MLP adapter achieves $63.4 \\pm 2.6$\\% SR over 3 seeds, statistically indistinguishable from the cross-attention result ($60.1 \\pm 1.3$\\%; two-sample $t$-test, $p = 0.15$). This confirms that the re-encoding benefit does not depend on the specific module architecture.\n\n\n\\section{Offline Single-Step Action Error Analysis}\n\\label{app:offline_error}\n\nTable~\\ref{tab:offline_action_error} reports the single-step action prediction error under pruning, computed over 200 evaluation frames from LIBERO-Object. The unpruned model (bypass mode) produces actions with an L2 distance of 0.414 from ground truth; under ACIS pruning at $k{=}0.50$, this increases to 1.391 ($3.4\\times$). The per-dimension breakdown of the pruned-vs-unpruned difference reveals that the gripper dimension dominates (L2 = 1.02), corresponding to complete gripper state inversion on many frames. Position errors (0.20--0.30 per axis) are moderate individually but compound across the 7-dimensional action space. These single-step errors are large enough to push the robot off-trajectory within a few steps, explaining why 0\\% of pruned episodes succeed in closed-loop evaluation despite moderate average offline metrics.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{Single-step action prediction error (SmolVLA, $k{=}0.50$, ACIS, zero-mask, 200 LIBERO-Object evaluation frames). Pruning increases action error by $3.4\\times$ and introduces catastrophic gripper inversions.}\n\\label{tab:offline_action_error}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Unpruned & Pruned ($k{=}0.50$) \\\\\n\\midrule\nAction L2 vs.\\ ground truth & 0.414 & 1.391 \\\\\nPruned vs.\\ unpruned L2 & \\multicolumn{2}{c}{1.284} \\\\\nRelative action error & -- & 111.5\\% \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Per-dimension L2 (pruned vs.\\ unpruned)}} \\\\\n\\quad Position $(x, y, z)$ & -- & 0.20, 0.25, 0.30 \\\\\n\\quad Rotation $(r_x, r_y, r_z)$ & -- & 0.01, 0.02, 0.01 \\\\\n\\quad Gripper & -- & 1.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Supplementary Figures}\n\\label{app:supplementary_figures}\n\n% fig_pixel_shuffle moved to Section~\\ref{sec:pixel_shuffle} in main text.\n\n\\begin{figure}[ht]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_entropy_layers.pdf}\n\\caption{Per-layer attention entropy ratio for SmolVLA (16 layers), OpenVLA (32 layers), and $\\pi_{0}$ (18 layers). SmolVLA and $\\pi_{0}$ maintain near-uniform attention throughout, while OpenVLA progressively sharpens from 0.98 to 0.48. Despite similar entropy, SmolVLA and $\\pi_{0}$ exhibit opposite pruning outcomes due to token importance heterogeneity (CV $= 0.314$ vs.\\ $0.038$). X-VLA (entropy $= 0.614$, CV $= 0.151$) occupies an intermediate position, consistent with its threshold-graded pattern (onset at $k{=}0.85$).}\n\\label{fig:entropy_layers}\n\\end{figure}\n\n\n\\section{Attention Entropy Measurement Details}\n\\label{app:entropy_details}\n\nWe measure the attention entropy ratio as the normalized Shannon entropy of the attention weights that the action decoder assigns to vision token positions. For a model with $N$ vision tokens, the entropy ratio is:\n\\begin{equation}\nH_{\\text{ratio}} = \\frac{-\\sum_{i=1}^{N} \\alpha_i \\log \\alpha_i}{\\log N}\n\\end{equation}\nwhere $\\alpha_i$ is the attention weight on the $i$-th vision token. The ratio ranges from 0 (all attention on one token) to 1 (uniform attention).\n\n\\paragraph{SmolVLA.} Measured on 2400 frames from LIBERO rollouts (overall entropy) and 260 frames across all 10 LIBERO-Object tasks (per-layer analysis across 16 layers). The mean per-layer entropy ratio is 0.95 (range: 0.93 to 0.98), consistent with near-uniform attention across all 128 vision tokens. The per-layer breakdown confirms this uniformity is not an averaging artifact:\n\\begin{itemize}[nosep]\n    \\item All 16 layers: 0.93--0.98 (spread 0.05)\n    \\item Minimum: layer 13 (0.93)\n\\end{itemize}\nThe flat profile across all processing depths confirms that pixel-shuffle tokens resist selective attention at every layer: because each token encodes 16 spatially contiguous patches via channel concatenation, all tokens are comparably information-dense, and the transformer has no basis for developing spatial selectivity.\n\n\\paragraph{$\\pi_{0}$.} Measured on 100 frames from LIBERO-Object (tasks 20--29) across all 18 layers of the Gemma-based PaliGemma backbone (512 vision tokens: 256 per image $\\times$ 2 cameras). The mean suffix-to-vision entropy ratio is 0.959 (range: 0.931--0.983, std 0.013), near-uniform across all layers with no progressive sharpening:\n\\begin{itemize}[nosep]\n    \\item All 18 layers: 0.931--0.983 (spread 0.052)\n    \\item Minimum: 0.931; Maximum: 0.983\n\\end{itemize}\nThe flat entropy profile, combined with $\\pi_{0}$'s extremely low CV (0.038), is consistent with its high tolerance to pruning: tokens carry near-equal importance and receive near-equal attention. Removing any subset approximates uniform spatial downsampling, preserving a proportional share of the visual field without disrupting the attention distribution.\n\n\\paragraph{OpenVLA.} Measured on 250 frames from real LIBERO rollouts. The overall entropy ratio is 0.64. The layer-wise breakdown reveals progressive sharpening:\n\\begin{itemize}[nosep]\n    \\item Shallow layers (0--1): 0.95--0.98\n    \\item Early layers (2--4): 0.70--0.80\n    \\item Mid layers (12--20): 0.57--0.66\n    \\item Deep layers (24--30): 0.48--0.57 (minimum 0.48 at layer 29)\n\\end{itemize}\n12.1\\% of total attention weight falls on vision tokens overall, and within that fraction, the distribution is non-uniform in deeper layers. This progressive concentration indicates that OpenVLA has learned to selectively attend to task-relevant spatial locations, a pattern enabled by the MLP projector's preservation of per-patch spatial granularity.\n\n\\paragraph{Measurement conditions.} All models are measured on real LIBERO rollout data: SmolVLA on 2400 frames (overall entropy) and 260 frames (per-layer analysis), $\\pi_{0}$ on 100 frames from LIBERO-Object, OpenVLA on 250 frames from 50 episodes $\\times$ 5 initial frames. Sample size differences reflect computational constraints (OpenVLA's 7B forward pass is substantially more expensive), but all measurements use task-relevant visual inputs. Entropy statistics show low variance across frames (std $< 0.02$ for OpenVLA, std $= 0.013$ for $\\pi_{0}$).\n\n\n\\section{Connector Architecture and Token Independence}\n\\label{app:connector_analysis}\n\nThe six-architecture taxonomy (Table~\\ref{tab:model_properties}) spans a continuous spectrum of token independence structures, each associated with the vision-to-LLM connector rather than model scale or action head design.\n\nPixel-shuffle connectors create maximal entanglement. SmolVLA's $4 \\times 4$ spatial folding packs 16 patches into each token by channel concatenation (CV $= 0.314$, the highest in our study). The folding is fixed and irreversible: removing one token eliminates an entire receptive field, and no downstream layer can recover the discarded content. Tokens encode non-overlapping spatial regions with heterogeneous visual content, making every token simultaneously essential and non-redundant.\n\nPure linear projections produce the opposite extreme. $\\pi_{0}$ maps each SigLIP patch through a single linear layer with no cross-token interaction, yielding CV $= 0.038$ and near-maximal entropy (0.959). Tokens are genuinely interchangeable: any subset preserves the same per-patch information density as any other subset of equal size.\n\n$\\pi_{0.5}$ reveals a subtlety that $\\pi_{0}$'s offline-only evaluation conceals. The $\\times\\!\\sqrt{d}$ learned scaling preserves near-uniform norms (CV $= 0.055$), yet the closed-loop response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\\% SR while L2 norm-based removal collapses to 33.4\\%. The 36\\,pp gap arises because L2 ranking in a low-CV distribution selects spatially clustered tokens whose slight norm variations correlate with image regions, destroying the spatial coverage that this architecture requires. Token position analysis confirms this mechanism: at $k{=}0.5$, L2 selection produces a single dominant cluster containing 100\\% of retained tokens with only 78\\% spatial coverage, whereas $k{=}0.7$ yields two clusters with 97\\% in the largest and 100\\% coverage (Appendix~\\ref{app:token_position}).\n\nX-VLA's 12-layer BART encoder~\\cite{lewis2020bart} introduces cross-token mixing through self-attention, creating partial dependencies that place it between the linear and MLP extremes (CV $= 0.151$, entropy $= 0.614$, the lowest among models). The resulting behavior is threshold-graded: performance holds through $k{=}0.9$ before a sharp cliff at $k{=}0.85$ ($-$31\\,pp). The cliff onset is reproducible across three seeds (std $= 0.3$\\,pp), confirming it as an architectural property.\n\nMLP projectors (OpenVLA, OFT) apply per-patch non-linear transformations that create partial importance differentiation without cross-token entanglement. OpenVLA's CV (0.215) and OFT's CV (0.219) match within measurement noise, as do their entropy values (0.661 vs.\\ 0.667); the connector, not the action head, is associated with token importance structure. CogACT~\\cite{li2024cogact} corroborates the graded pattern from the literature (74.2\\% SR under 78\\% pruning).\n\nParameter count does not predict pruning tolerance. Ordered by scale: SmolVLA (450M) $<$ X-VLA (0.9B) $<$ $\\pi_{0}$ (3.3B) $<$ $\\pi_{0.5}$ (4B) $<$ OpenVLA (7B). Ordered by tolerance, SmolVLA remains the minimum, but $\\pi_{0}$ and $\\pi_{0.5}$ at 3.3--4B surpass OpenVLA at 7B, and X-VLA at 0.9B tolerates more aggressive pruning than OpenVLA. The CV spectrum (0.038 to 0.314) tracks connector complexity rather than parameter count across a 16$\\times$ scale range.\n\n\n\\section{CV as Diagnostic Metric: Extended Analysis}\n\\label{app:cv_extended}\n\\label{sec:diagnostic}\n\nToken importance CV correlates with both the tolerance class of a model and the optimal pruning strategy, a correlation that emerges from a single mechanistic principle: CV measures the strength of the importance gradient that scoring methods can exploit.\n\nLow-CV models have near-uniform L2 norms. L2 norm ranking in this regime captures spatial artifacts (slight norm variations that correlate with image position) rather than genuine importance differences. Selection based on these artifacts concentrates retained tokens on spatially correlated patches, destroying the uniform coverage that low-CV architectures depend on. Random selection preserves spatial uniformity by construction. The mechanism predicts that the L2-over-random advantage should grow as CV increases, and the data in Table~\\ref{tab:scaling_law} confirm this. On LIBERO-Object at $k{=}0.5$: $\\Delta = -$36.0\\,pp ($\\pi_{0.5}$, CV $= 0.055$) $\\to$ $-$26.9\\,pp (X-VLA, CV $= 0.151$) $\\to$ $+$3.4\\,pp (OpenVLA, CV $= 0.215$). At $k{=}0.7$, the same ordering holds for $\\pi_{0.5}$ and X-VLA ($-$22.2\\,pp $\\to$ $-$6.5\\,pp); OpenVLA lacks a seed-matched pair at this ratio. The pattern persists across retention ratios, strengthening the interpretation from a coincidence at a single operating point to a structural property of the connector.\n\nOn simple manipulation tasks (Object), high-CV models present a genuine importance gradient where L2 norm ranking aligns with actual information content. OpenVLA (CV $= 0.215$) sits near the crossover on Object: L2 outperforms random by 7.8\\,pp at $k{=}0.9$ where the gradient is most exploitable, shrinking to 3.4\\,pp at $k{=}0.5$ as the proportion of removed tokens exceeds the gradient's discriminative range. On complex multi-step tasks, this advantage diminishes or reverses: OpenVLA Long at $k{=}0.9$ shows Random outperforming L2 by 3.2\\,pp (46.8\\% vs.\\ 43.6\\%), as compositional tasks distribute critical information across tokens with heterogeneous norm profiles (Section~\\ref{sec:analysis}).\n\nExtreme compression introduces a partial reversal. At $k{=}0.3$, $\\pi_{0.5}$'s L2 selection achieves $53.2 \\pm 3.1$\\% SR (2 seeds) vs.\\ random's 36.4\\%. When very few tokens remain, even spatially clustered high-norm tokens provide more signal than a sparse random sample. The V-shaped L2 curve is confirmed across seeds ($\\sigma{=}0.1$\\,pp at the $k{=}0.5$ valley). The reversal does not invalidate the CV diagnostic; it adds a budget-dependent interaction that future work should characterize across more models.\n\nAttention entropy provides a mechanistic supplement that resolves an apparent paradox. SmolVLA's entropy (0.952) is nearly as high as $\\pi_{0}$'s (0.959), yet SmolVLA collapses under any pruning. SmolVLA's tokens are uniformly \\emph{attended} but carry heterogeneous \\emph{content} due to pixel-shuffle folding. Entropy captures how the LLM allocates attention across tokens; CV captures the input-side importance structure. Entropy alone cannot distinguish ``interchangeable'' ($\\pi_{0}$) from ``entangled'' (SmolVLA), but CV separates them cleanly (0.038 vs.\\ 0.314). OpenVLA's progressive entropy sharpening from 0.98 to 0.48 across layers (Figure~\\ref{fig:entropy_layers}) is consistent with a graded regime where the LLM progressively concentrates on higher-importance tokens.\n\n\n\\section{Why Re-Encoding Succeeds: Extended Analysis}\n\\label{app:reencoding_analysis}\n\\label{sec:learned_compression}\n\nLearned re-encoding overcomes pixel-shuffle failure because it breaks the rigid spatial entanglement that the $4 \\times 4$ folding creates. Cross-attention pooling integrates information across receptive field boundaries, redistributing content from the original 128 tokens into $M$ compressed representations no longer tied to fixed spatial blocks.\n\nThe $M{=}128$ passthrough configuration suggests that re-encoding, not compression, is the key factor. Passthrough adds parameters without reducing token count, yet gains 13\\,pp over the baseline (44.8\\% $\\to$ 58.0\\%). The relatively stable M-curve ($M{=}16$: 56.9\\% closely matches $M{=}128$: 58.0\\%, within 1.1\\,pp) shows that once entanglement is broken, token count is secondary.\n\nA parameter-matched MLP adapter (22.14M parameters) achieves 63.4\\% SR at $M{=}32$, statistically indistinguishable from cross-attention ($p = 0.15$). Re-encoding through any learned mapping that integrates across token boundaries suffices; the attention mechanism itself is not essential.\n\nThe remedy is specific to the pathology. VTR succeeds precisely on architectures whose rigid spatial entanglement demands learned redistribution; for token-independent connectors where each patch already carries self-contained information, re-encoding is unnecessary.\n\n\n\\section{Offline Metrics Underestimate Closed-Loop Failure}\n\\label{app:offline_disconnect}\n\\label{sec:metric_disconnect}\n\nOffline evaluation systematically underestimates pruning-induced failure because per-step averages dilute catastrophic single-step events that individually terminate episodes.\n\nX-VLA at $k{=}0.3$ demonstrates the gap directly: offline loss is 1.0014 (near-baseline), yet closed-loop SR drops to $22.0 \\pm 0.9$\\% ($-$77\\,pp). A single gripper inversion (L2 $= 1.02$) is a minor perturbation in average action error but terminates an episode irreversibly. $\\pi_{0}$'s offline loss at $k{=}0.1$ shows a 2.4\\% \\emph{improvement} over the unpruned baseline (offline metrics only; no closed-loop evaluation available), a result that closed-loop evaluation may contradict if similar catastrophic events occur at deployment frequency.\n\n$\\pi_{0.5}$ adds a distinct form of evidence: the 36\\,pp gap between L2 and random removal at $k{=}0.5$ is invisible to any offline metric that averages across token subsets or selection methods. Offline evaluation would report degradation for both methods; only closed-loop evaluation reveals that the \\emph{choice} of pruning strategy, not just the pruning ratio, is associated with whether the model remains functional.\n\n\n\\section{Confounder Analysis}\n\\label{app:confounders}\n\nThe six architectures span three connector families but differ simultaneously in LLM backbone (PaliGemma for $\\pi_{0}$/$\\pi_{0.5}$, Llama-2 for OpenVLA, Florence-2 for X-VLA, SmolLM2 for SmolVLA), preventing clean isolation of the connector effect from backbone differences. The $\\pi_{0}$--OpenVLA comparison (same 256 SigLIP-based tokens, different connector, backbone, and encoder fusion strategy) provides the closest available approximation, but a matched-backbone experiment remains the ideal control. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation. Token count also varies across models (50 for X-VLA, 128 for SmolVLA, 256 for $\\pi_{0}$/OpenVLA, 768 for $\\pi_{0.5}$); the $\\pi_{0}$--OpenVLA pair controls for this confounder within the CV analysis while still exhibiting the predicted CV-gap relationship.\n\nThe spatial clustering hypothesis for L2 failure on low-CV models is confirmed by token position analysis (Appendix~\\ref{app:token_position}).\n\nOpenVLA main-text results use seed 42 for both L2 and random. Cross-seed (seed 7) random comparison in Table~\\ref{tab:openvla_l2_vs_random} confirms the L2 advantage is seed-independent: the gap ranges from $+$0.8 to $+$8.6\\,pp across retention ratios regardless of random seed.\n\n\n\\section{Token Position Analysis}\n\\label{app:token_position}\n\nTo validate the spatial clustering hypothesis for L2 norm failure on low-CV models, we analyze the spatial distribution of tokens selected by L2 norm ranking on $\\pi_{0.5}$ across three retention ratios.\n\nAt $k{=}0.7$ (538 of 768 tokens retained): DBSCAN clustering identifies 2 spatial clusters, with 97\\% of retained tokens in the largest cluster and 100\\% spatial coverage of the original image grid. The broad coverage explains why L2 selection still achieves 55.0\\% SR at this retention ratio.\n\nAt $k{=}0.5$ (384 tokens retained): a single dominant cluster contains 100\\% of retained tokens with only 78\\% spatial coverage. The complete concentration into one spatial region confirms the clustering hypothesis: L2 norm ranking selects tokens from a contiguous high-norm region while abandoning 22\\% of the spatial field. This is the retention ratio where L2 performance reaches its minimum (33.4\\% SR, the V-shape valley).\n\nAt $k{=}0.3$ (230 tokens retained): 3 clusters emerge, with 86\\% in the largest and 78\\% spatial coverage. The fragmentation into multiple clusters at extreme compression is consistent with the partial L2 recovery observed at this ratio ($53.2 \\pm 3.1$\\% SR): when the budget is very small, L2 selection is forced to sample from multiple spatial regions, partially restoring coverage.\n\nThese results directly confirm that L2 norm ranking on low-CV models introduces spatial bias that degrades performance, and that the severity peaks at intermediate retention ratios where concentration is maximal.\n\n\n\\section{CV Scaling Law: Full Data}\n\\label{app:cv_scaling_table}\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{L2 norm vs.\\ random removal at two retention ratios. The importance margin $\\Delta$(L2$-$R) increases monotonically with CV at both $k{=}0.5$ and $k{=}0.7$: low-CV models require random selection (uniform importance $\\rightarrow$ L2 degenerates to spatial clustering), while high-CV models tolerate either strategy on simple tasks (see Section~\\ref{sec:analysis} for task-dependent caveats). Data shown for LIBERO-Object; the monotonic ordering holds across retention ratios despite a 2$\\times$ change in token budget.}\n\\label{tab:scaling_law}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & CV & Tokens & L2 SR (\\%) & Random SR (\\%) & $\\Delta$(L2$-$R) \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$k{=}0.5$ (50\\% retention)}} \\\\\n$\\pi_{0.5}$ & 0.055 & 768 & 33.4 & \\textbf{69.4} & $-$36.0 \\\\\nX-VLA & 0.151 & 50 & 43.4$\\pm$0.8 & \\textbf{70.3}$\\pm$0.9 & $-$26.9 \\\\\nOpenVLA & 0.215 & 256 & \\textbf{39.2} & 35.8 & $+$3.4 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$k{=}0.7$ (70\\% retention)}} \\\\\n$\\pi_{0.5}$ & 0.055 & 768 & 55.0 & \\textbf{74.0} & $-$19.0 \\\\\nX-VLA & 0.151 & 50 & 58.6$\\pm$0.4 & \\textbf{65.1}$\\pm$0.1 & $-$6.5 \\\\\nOpenVLA\\textsuperscript{$\\dagger$} & 0.215 & 256 & -- & -- & -- \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize\\textsuperscript{$\\dagger$}$k{=}0.7$ omitted: no seed-matched L2/Random pair available.}\n\\end{tabular}\n\\end{table}\n\n\n\\section{CV-Strategy Interaction at Extreme Compression}\n\\label{app:cv_strategy_interaction}\n\nThe monotonic CV-gap relationship (Table~\\ref{tab:scaling_law}) holds at $k{=}0.5$ and $k{=}0.7$, but partially reverses at $k{=}0.3$ for $\\pi_{0.5}$. At this extreme budget, L2 norm selection achieves $53.2 \\pm 3.1$\\% SR (2 seeds) vs.\\ random's 36.4\\%, favoring L2 by $\\sim$17\\,pp. The reversal is consistent across both seeds (seed42: 51.0\\%, seed43: 55.4\\%; Table~\\ref{tab:pi05_l2_multiseed}).\n\nThe mechanism is intuitive: when very few tokens remain ($k{=}0.3$ retains 230 of 768 tokens), even spatially clustered high-norm tokens provide more visual signal than a sparse random sample. At intermediate budgets ($k{=}0.5$, 384 tokens), random selection preserves enough spatial coverage to outperform L2's clustered selection; at extreme budgets, coverage from random selection becomes too sparse to be useful, and the concentrated signal from L2 selection dominates.\n\nThe interaction implies that the optimal pruning strategy depends on both CV and the absolute token budget. For low-CV models, the crossover point between random-preferred and L2-preferred regimes lies between $k{=}0.3$ and $k{=}0.5$. Characterizing this crossover across additional models and budgets is left to future work.\n\n\n\\section{Inference Cost-Benefit Analysis}\n\\label{app:cost_benefit}\n\nThe primary deployment benefit of VTR at this model scale is memory, not latency. Reducing from 128 to 32 vision tokens shrinks the KV-cache footprint for the vision portion by 75\\%, a meaningful reduction for memory-constrained robotic hardware where KV-cache size can limit the number of concurrent policy instances or maximum context length.\n\nEnd-to-end inference latency improves only modestly: 154.78\\,ms at $M{=}32$ versus 164.33\\,ms at full token count, a $1.06\\times$ speedup (6\\% reduction). At $M{=}64$: 156.16\\,ms ($1.05\\times$). The gap between token reduction and latency gain reflects SmolVLA's compact size (450M parameters): self-attention over 128 vision tokens is not the inference bottleneck, and the compressor's 22.2M-parameter cross-attention computation partially offsets downstream savings. Token pruning becomes a more compelling latency optimization for VLAs with larger token budgets ($>$256 tokens) or larger backbones (7B+ parameters), where attention cost scales quadratically with sequence length. Whether the training cost (100K steps, 6.5 hours per configuration) is justified depends on deployment context: for VLAs deployed across many tasks, the one-time training cost is amortized; for rapid prototyping, retraining is a barrier.\n\n\\paragraph{Comparison with the official checkpoint.}\nVTR at $M = 32$ ($60.1 \\pm 1.3$\\% over 3 seeds) recovers from 0\\% SR under hard pruning to performance comparable to the official SmolVLA checkpoint (59.2\\%, CI [54.8\\%, 63.4\\%]). However, the difference is not statistically significant (two-sample $t$-test, $p \\approx 0.72$), and the comparison should be interpreted cautiously given different training conditions (batch size 4 vs.\\ 64, single vs.\\ 8 GPUs). The primary contribution of VTR is recovering functional performance where all deletion methods yield 0\\%, not matching the official baseline.\n\n\\subsection{Attention-Based Scoring}\n\\label{app:attention_pruning}\n\nTable~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{X-VLA success rates (\\%) at $k{=}0.5$ across five scoring methods. Attention-based scoring recovers near-baseline performance across all suites while L2 norm falls below random on every suite. Bold indicates best per suite. \\textsuperscript{*}Best of three attention variants.}\n\\label{tab:attention_pruning}\n\\begin{tabular}{lccccc}\n\\toprule\nSuite & attn\\_last & attn\\_mean & attn\\_rollout & L2 & Random \\\\\n\\midrule\nObject & \\textbf{99.2} & 98.4 & 97.4 & 43.4 & 70.6 \\\\\nSpatial & 88.8 & 91.6 & \\textbf{92.8} & 58.8 & 71.4 \\\\\nLong & 90.2 & 94.0 & \\textbf{94.8} & 45.0 & 61.6 \\\\\nGoal & \\multicolumn{3}{c}{\\textbf{98.2}\\textsuperscript{*}} & 59.0 & 67.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nL2 norm selection is anti-informative on X-VLA's entangling connector: L2 falls below random on all four suites, with gaps ranging from $-$8.2\\,pp (Goal) to $-$27.2\\,pp (Object). Attention-based scoring recovers near-baseline performance across all suites (${\\geq}$92.8\\%), with rollout peaking at 94.8\\% on Long (seed43 confirms $\\Delta{\\leq}$0.6\\,pp). On Object, all three attention variants achieve ${\\geq}$97.4\\%, far exceeding both L2 (43.4\\%) and random (70.6\\%). The mode ranking reverses across suites: last-layer attention is best on Object (99.2\\%) but worst among attention methods on Spatial (88.8\\%) and Long (90.2\\%), while rollout shows the opposite pattern.\n\nThe L2 failure has a structural explanation. The BART encoder's 12-layer self-attention redistributes information across tokens, equalizing activation magnitudes (CV$\\,{=}\\,$0.151). L2 norms no longer reflect token importance; instead, they select spatially correlated clusters that miss critical information. Goal L2 exhibits non-monotonic behavior ($k{=}0.7$: 53.4\\% $<$ $k{=}0.5$: 59.0\\%), confirming that retaining more L2-selected tokens is actively harmful. Per-task variance under L2 pruning is extreme on Spatial (std$\\,{=}\\,$31.5\\,pp, range 0--92\\%), while attention scoring keeps all tasks above 80\\%. The double dissociation extends to $\\pi_{0.5}$, where attention scoring at $k{=}0.5$ exhibits suite-dependent failure (Table~\\ref{tab:pi05_attention_crosssuite}). On three suites (Goal, Spatial, Long), attention performs within noise of random ($\\pm$3\\,pp). On Object, attention collapses to 37.8\\% ($-$31.6\\,pp vs.\\ random's 69.4\\%), a catastrophic failure unique to tasks requiring spatial discrimination among visually similar alternatives. The linear connector produces an extremely narrow attention score range ($[2{\\times}10^{-6},\\, 3.6{\\times}10^{-3}]$) with systematic position bias favoring early tokens; on Object, this bias selects semantically relevant but spatially uninformative tokens, destroying the fine-grained spatial information needed for target identification.\n\n\\begin{table}[ht]\n\\centering\n\\small\n\\caption{$\\pi_{0.5}$ attention vs.\\ random at $k{=}0.5$ across LIBERO suites. Attention is neutral on 3/4 suites but catastrophically harmful on Object.}\n\\label{tab:pi05_attention_crosssuite}\n\\begin{tabular}{lccc}\n\\toprule\nSuite & Attention (\\%) & Random (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\nGoal & 71.2 & 73.6 & $-$2.4 \\\\\nSpatial & 72.6 & 71.6 & $+$1.0 \\\\\nLong & 49.4 & 46.8 & $+$2.6 \\\\\nObject & 37.8 & 69.4 & $-$31.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table} By contrast, $\\pi_{0.5}$'s L2 norms do reflect importance: on Goal, L2 outperforms random by $+$35.2\\,pp at $k{=}0.85$, decaying to $+$5.6\\,pp at $k{=}0.95$ (log-decay trend across four retention ratios). This yields a connector-dependent scoring reversal: attention is effective on entangling connectors but not token-independent ones, while L2 norm shows the converse (Figure~\\ref{fig:scoring_crossover}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Scoring reversal summary: $\\Delta$ vs.\\ random at $k{=}0.5$, except \\textsuperscript{*}Goal suite across $k \\in [0.85, 0.95]$. Compact view of the pattern shown in Figure~\\ref{fig:scoring_crossover}.}\n\\label{tab:scoring_crossover_summary}\n\\begin{tabular}{lcc}\n\\toprule\n& Attention & L2 norm \\\\\n\\midrule\nEntangling (X-VLA) & Effective ($+$31\\,pp) & Anti-inform.\\ ($-$8 to $-$27\\,pp) \\\\\nToken-indep.\\ ($\\pi_{0.5}$) & Ineffective\\textsuperscript{$\\dagger$} ($-$2 to $-$30\\,pp) & Effective\\textsuperscript{*} ($+$35.2$\\to$$+$5.6\\,pp) \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize\\textsuperscript{$\\dagger$}Neutral on 3/4 suites ($\\pm$3\\,pp); harmful on Object ($-$30.4\\,pp).}\n\\end{tabular}\n\\end{table}",
    "structuredPatch": [
      {
        "oldStart": 861,
        "oldLines": 9,
        "newStart": 861,
        "newLines": 19,
        "lines": [
          " \\paragraph{Comparison with the official checkpoint.}",
          " VTR at $M = 32$ ($60.1 \\pm 1.3$\\% over 3 seeds) recovers from 0\\% SR under hard pruning to performance comparable to the official SmolVLA checkpoint (59.2\\%, CI [54.8\\%, 63.4\\%]). However, the difference is not statistically significant (two-sample $t$-test, $p \\approx 0.72$), and the comparison should be interpreted cautiously given different training conditions (batch size 4 vs.\\ 64, single vs.\\ 8 GPUs). The primary contribution of VTR is recovering functional performance where all deletion methods yield 0\\%, not matching the official baseline.",
          " ",
          "-\\subsection{Attention-Based Scoring}",
          "+\\subsection{Attention-Based Scoring Methods}",
          "+\\label{app:attention_scoring}",
          " \\label{app:attention_pruning}",
          " ",
          "+Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity for residual connections) to approximate cumulative information flow. These methods require a full LLM forward pass and are backbone-specific. We focus on L2 and random in the main text because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.",
          "+",
          "+\\subsection{Attention Entropy as Diagnostic}",
          "+\\label{app:attention_entropy}",
          "+",
          "+Attention entropy, defined as the mean Shannon entropy of the LLM's attention distribution over vision tokens, provides a complementary but less discriminative signal than CV. Three models with qualitatively different pruning behaviors cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness.",
          "+",
          "+\\subsection{Attention-Based Scoring Results}",
          "+",
          " Table~\\ref{tab:attention_pruning} compares attention-based token scoring with L2 norm and random selection on X-VLA at $k{=}0.5$ (25 of 50 tokens retained). Three attention variants are evaluated: last-layer attention (attn\\_last), mean attention across all decoder layers (attn\\_mean), and attention rollout~\\cite{abnar2020quantifying}.",
          " ",
          " \\begin{table}[h]"
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

_source line 93_

Now fix the reference in method.tex to point to `app:attention_scoring` instead of `app:attention_pruning`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "9d67b7ea-8f19-41d4-8d94-2f3cc24e9848",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3zEU1zNMBuKiu2S8w92cT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 75497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 705
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

_source line 94_

<details open><summary>🔧 Tool call — Edit · `toolu_01KHzDXJMaicEJfuJgcRrvPK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_pruning}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.",
  "new_string": "We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "5d348d86-2bf3-4c62-8fa2-199d3dedd466",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3zEU1zNMBuKiu2S8w92cT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 75497,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 705
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

_source line 95 · 2026-05-28T18:32:42.508Z_

<details><summary>↩ Tool result · `toolu_01KHzDXJMaicEJfuJgcRrvPK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "814e45dd-9aa5-470a-9d75-10d1556a6456",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_pruning}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.",
    "newString": "We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). \\textbf{Linear projection} applies a per-patch matrix multiplication ($\\pi_{0}$~\\cite{black2024pi0}, $\\pi_{0.5}$~\\cite{black2025pi05}; CV$\\,{<}\\,$0.06). \\textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\\cite{kim2024openvla}, OFT~\\cite{kim2025openoft}; CV$\\,{\\approx}\\,$0.22). \\textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\\cite{zheng2025xvla} uses a 12-layer BART encoder~\\cite{lewis2020bart} (CV$\\,{=}\\,$0.151); SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 patches per token (CV$\\,{=}\\,$0.314). We classify coupling as \\emph{independent} (one patch per output) or \\emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning retains $\\lfloor k \\cdot N \\rfloor$ tokens for $k \\in (0, 1]$ and physically removes the rest, re-indexing positions to close gaps. We prune between the connector output and LLM input to isolate the connector's effect on token information structure.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_pruning}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.\n\n\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details}).\n",
    "structuredPatch": [
      {
        "oldStart": 45,
        "oldLines": 7,
        "newStart": 45,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).",
          " ",
          "-The \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_pruning}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.",
          "+The \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.",
          " ",
          " \\paragraph{Retention ratios.}",
          " We evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details})."
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

_source line 96_

Now let me also compress the introduction slightly. The abstract + intro together take a lot of space. Let me also compress the figure 2 caption and table 1 caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "cd3ff3d8-4a84-4f94-8188-c206c7a616da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTbFeeeVqsEMm4kcioVMdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 337,
      "cache_read_input_tokens": 76202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 337
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 97_

<details open><summary>🔧 Tool call — Edit · `toolu_011ZugA7idVuR57HFYMsphYk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}",
  "new_string": "\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "27274043-5458-413b-9aff-32795dece4e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TTbFeeeVqsEMm4kcioVMdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 337,
      "cache_read_input_tokens": 76202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 337
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-28T18:32:51.643Z_

<details><summary>↩ Tool result · `toolu_011ZugA7idVuR57HFYMsphYk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "0aebc58a-7f3e-4fc9-a69d-2c6e2268db38",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}",
    "newString": "\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). \\textbf{Linear projection} applies a per-patch matrix multiplication ($\\pi_{0}$~\\cite{black2024pi0}, $\\pi_{0.5}$~\\cite{black2025pi05}; CV$\\,{<}\\,$0.06). \\textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\\cite{kim2024openvla}, OFT~\\cite{kim2025openoft}; CV$\\,{\\approx}\\,$0.22). \\textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\\cite{zheng2025xvla} uses a 12-layer BART encoder~\\cite{lewis2020bart} (CV$\\,{=}\\,$0.151); SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 patches per token (CV$\\,{=}\\,$0.314). We classify coupling as \\emph{independent} (one patch per output) or \\emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning retains $\\lfloor k \\cdot N \\rfloor$ tokens for $k \\in (0, 1]$ and physically removes the rest, re-indexing positions to close gaps. We prune between the connector output and LLM input to isolate the connector's effect on token information structure.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.\n\n\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details}).\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\begin{figure*}[t]",
          " \\centering",
          " \\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}",
          "-\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}",
          "+\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}",
          " \\label{fig:architecture}",
          " \\end{figure*}",
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

_source line 99_

Now let me also compress some experiment captions and the main results table caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "0294514c-e810-4e5e-b5b0-926ff27e0de1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RV4ZdCf9SY7drn56eC9zyK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 494,
      "cache_read_input_tokens": 76539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 494
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

_source line 100_

<details open><summary>🔧 Tool call — Edit · `toolu_011QVzBaXUihoWqSnveFWGho`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}",
  "new_string": "\\caption{Closed-loop SR (\\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "53a0f174-c46c-4ba0-ab2f-21e844a7c0fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RV4ZdCf9SY7drn56eC9zyK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 494,
      "cache_read_input_tokens": 76539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 494
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

_source line 101 · 2026-05-28T18:32:59.196Z_

<details><summary>↩ Tool result · `toolu_011QVzBaXUihoWqSnveFWGho`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "7095eed7-391c-4b38-994a-32867dbc6166",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "oldString": "\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}",
    "newString": "\\caption{Closed-loop SR (\\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation}).\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, $<$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, $n{=}3$; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), indicating the benefit stems from re-encoding, not the cross-attention mechanism. Cross-suite generalization: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning. For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\\%; VTR exceeds the unpruned baseline at up to 87.5\\% compression. Baseline (44.8\\%) is our LoRA reproduction; official checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}).}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 33,
        "oldLines": 7,
        "newStart": 33,
        "newLines": 7,
        "lines": [
          " \\begin{table*}[t]",
          " \\centering",
          " \\small",
          "-\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}",
          "+\\caption{Closed-loop SR (\\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}",
          " \\label{tab:main_results}",
          " \\begin{tabular}{llcccc}",
          " \\toprule"
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

_source line 102_

I notice the reference is `app:entropy_details` in the auto-modified version but I wrote `app:attention_entropy`. Let me check the actual file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "bea9106a-2a80-402b-a245-621ff891b600",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPq4byjzMQZr5Rxhx8P2Gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 77033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3165
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

_source line 103_

<details open><summary>🔧 Tool call — Grep · `toolu_019DUCxYsbLFfcEhRDvy2b9y`</summary>

```json
{
  "pattern": "app:entropy_details|app:attention_entropy",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
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
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "163015b2-ebed-4c2b-8407-fcde1707dd77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FPq4byjzMQZr5Rxhx8P2Gz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 77033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3165
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

_source line 104 · 2026-05-28T18:33:05.232Z_

<details><summary>↩ Tool result · `toolu_019DUCxYsbLFfcEhRDvy2b9y`</summary>

```text
method.tex:69:[Omitted long matching line]
main.aux:235:\newlabel{app:entropy_details}{{M}{22}{Attention Entropy Measurement Details}{appendix.M}{}}
main.aux:285:\newlabel{app:attention_entropy}{{V.2}{30}{Attention Entropy as Diagnostic}{subsection.V.2}{}}
appendix.tex:702:\label{app:entropy_details}
appendix.tex:871:\label{app:attention_entropy}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "d9c8f931-0566-48dc-a48d-609d5a8984de",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "method.tex:69:[Omitted long matching line]\nmain.aux:235:\\newlabel{app:entropy_details}{{M}{22}{Attention Entropy Measurement Details}{appendix.M}{}}\nmain.aux:285:\\newlabel{app:attention_entropy}{{V.2}{30}{Attention Entropy as Diagnostic}{subsection.V.2}{}}\nappendix.tex:702:\\label{app:entropy_details}\nappendix.tex:871:\\label{app:attention_entropy}",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 105_

There's already an `app:entropy_details` at line 702 and my new `app:attention_entropy` at 871. The method.tex reference points to `app:entropy_details`. But I should make it consistent. Let me update to use `app:attention_entropy` since that's where the substantive content now lives.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "fec2758f-9421-4ab2-b0ed-8f1c85eb7da1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KmeJuXQv4xtw2W1U732Gm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 80198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 301
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

_source line 106_

<details open><summary>🔧 Tool call — Read · `toolu_014jc5T6H2KA9FDjRj7cNHyN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "offset": 65,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "6a3eb392-8f3b-4994-a216-767e7f290d56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KmeJuXQv4xtw2W1U732Gm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 80198,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 301
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

_source line 107 · 2026-05-28T18:33:13.346Z_

<details><summary>↩ Tool result · `toolu_014jc5T6H2KA9FDjRj7cNHyN`</summary>

```text
65	$\underbrace{\pi_0\,(0.038) < \pi_{0.5}\,(0.055)}_{\text{linear}} < \underbrace{\text{X-VLA}\,(0.151)}_{\text{BART}} < \underbrace{\text{OpenVLA}\,(0.215) \approx \text{OFT}\,(0.219)}_{\text{MLP}} < \underbrace{\text{SmolVLA}\,(0.314)}_{\text{pixel-shuffle}}$.
66	Linear projections produce near-uniform norms (CV$\,{<}\,$0.06); MLP nonlinearities amplify variance (CV$\,{\approx}\,$0.22); pixel-shuffle creates maximal entanglement (CV$\,{=}\,$0.314). X-VLA's BART encoder raises CV from ${\sim}$0.04 to 0.151 via cross-token attention.
67	
68	\paragraph{CV as pruning tolerance predictor.}
69	High CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\,{<}\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\,{>}\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\Delta$ increases monotonically with CV across three closed-loop models (Section~\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\ref{app:entropy_details}).
70	
71	\subsection{Vision Token Re-encoder (VTR)}
72	\label{sec:vtr}
73	
74	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "77cecc32-cda4-40aa-b683-a2c2a5be5e84",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.\n\n\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:entropy_details}).\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.",
      "numLines": 10,
      "startLine": 65,
      "totalLines": 78
    }
  }
}
```

</details>

---

### Assistant

_source line 108_

Good, it references `app:entropy_details` which already exists. That's fine. Let me now also update `app:attention_entropy` label to also include `app:entropy_details` in my new section so both references resolve.

Actually, both labels exist and point to different places. Let me update the method.tex reference to point to `app:attention_entropy` which has the moved substantive content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "bb7acc5c-aea3-44cc-902f-3602bacd1b6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3hrzpztheXAmCvLqfdAZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 80499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 109_

<details open><summary>🔧 Tool call — Edit · `toolu_018ujPUkEgwbH5hGEApXscjE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:entropy_details}).",
  "new_string": "Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "91faa486-d588-4b08-935e-20c2c617bd65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3hrzpztheXAmCvLqfdAZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 80499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 110 · 2026-05-28T18:33:25.291Z_

<details><summary>↩ Tool result · `toolu_018ujPUkEgwbH5hGEApXscjE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "70b1ed92-d350-411d-b9e1-286aa9730f3f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:entropy_details}).",
    "newString": "Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). \\textbf{Linear projection} applies a per-patch matrix multiplication ($\\pi_{0}$~\\cite{black2024pi0}, $\\pi_{0.5}$~\\cite{black2025pi05}; CV$\\,{<}\\,$0.06). \\textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\\cite{kim2024openvla}, OFT~\\cite{kim2025openoft}; CV$\\,{\\approx}\\,$0.22). \\textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\\cite{zheng2025xvla} uses a 12-layer BART encoder~\\cite{lewis2020bart} (CV$\\,{=}\\,$0.151); SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 patches per token (CV$\\,{=}\\,$0.314). We classify coupling as \\emph{independent} (one patch per output) or \\emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning retains $\\lfloor k \\cdot N \\rfloor$ tokens for $k \\in (0, 1]$ and physically removes the rest, re-indexing positions to close gaps. We prune between the connector output and LLM input to isolate the connector's effect on token information structure.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two backbone-agnostic strategies.\n\n\\textbf{L2-norm scoring} uses activation magnitude $s_{\\text{L2}}(t_i) = \\|t_i\\|_2$ as a proxy for information density. L2 scoring introduces spatial bias: nearby patches produce correlated norms, so aggressive pruning can concentrate retained tokens in a single region (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly ($s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)$), providing a null hypothesis that all tokens are interchangeable. Random selection preserves spatial coverage in expectation, making it the natural baseline for spatially uniform architectures. Sampling variance is controlled through multi-seed evaluation (Section~\\ref{sec:exp_setup}).\n\nThe \\emph{importance margin} $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$ quantifies exploitable importance structure. A negative margin indicates L2 selection is actively harmful. The sign and magnitude of $\\Delta$ vary systematically with connector CV and $k$ (Section~\\ref{sec:cv_sensitivity}). We also evaluate attention-based scoring on selected conditions (Appendix~\\ref{app:attention_scoring}); we focus on L2 and random because they operate solely on the connector output and suffice to reveal connector-dependent importance structure.\n\n\\paragraph{Retention ratios.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning extreme compression to conservative trimming. This range identifies \\emph{cliff zones}: narrow $k$ intervals where SR drops discontinuously. Different connectors cliff at different ratios: pixel-shuffle at $k{=}0.95$, BART-encoded near $k{\\approx}0.85$, MLP without a sharp cliff (Appendix~\\ref{app:pruning_details}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families (Table~\\ref{tab:model_properties}):\n$\\underbrace{\\pi_0\\,(0.038) < \\pi_{0.5}\\,(0.055)}_{\\text{linear}} < \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{BART}} < \\underbrace{\\text{OpenVLA}\\,(0.215) \\approx \\text{OFT}\\,(0.219)}_{\\text{MLP}} < \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}$.\nLinear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.\n\n\\paragraph{CV as pruning tolerance predictor.}\nHigh CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:entropy_details}).\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module (12 heads) between the connector output and the LLM input. $M$ learned queries attend over all $N$ source tokens, producing $M$ compressed tokens ($M \\in \\{16, 32, 64, 96, 128\\}$). The module adds ${\\sim}$22M parameters ($<$5\\% of SmolVLA) and is trained end-to-end (Appendix~\\ref{app:smart_compress_details}).\n",
    "structuredPatch": [
      {
        "oldStart": 66,
        "oldLines": 7,
        "newStart": 66,
        "newLines": 7,
        "lines": [
          " Linear projections produce near-uniform norms (CV$\\,{<}\\,$0.06); MLP nonlinearities amplify variance (CV$\\,{\\approx}\\,$0.22); pixel-shuffle creates maximal entanglement (CV$\\,{=}\\,$0.314). X-VLA's BART encoder raises CV from ${\\sim}$0.04 to 0.151 via cross-token attention.",
          " ",
          " \\paragraph{CV as pruning tolerance predictor.}",
          "-High CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:entropy_details}).",
          "+High CV means some tokens carry substantially larger norms; these can be retained while low-norm tokens are removed with limited loss. Low CV means near-uniform norms: pruning becomes equivalent to downsampling a uniform signal, where spatial coverage matters more than importance ranking. CV also predicts the optimal scoring strategy: when CV$\\,{<}\\,$0.15, random outperforms L2 by preserving spatial coverage; when CV$\\,{>}\\,$0.20, L2 exploits genuine importance differentiation. The importance margin $\\Delta$ increases monotonically with CV across three closed-loop models (Section~\\ref{sec:cv_sensitivity}). Attention entropy provides a complementary but less discriminative signal (Appendix~\\ref{app:attention_entropy}).",
          " ",
          " \\subsection{Vision Token Re-encoder (VTR)}",
          " \\label{sec:vtr}"
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

_source line 111_

Now let me also compress the figure captions in experiments.tex and fix float positions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "532926da-43cb-43f9-b358-8370f894d8ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzbASa1LhZd3y4FareHBMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 81207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 112_

<details open><summary>🔧 Tool call — Read · `toolu_01QAeEmUTDMYSb9H1rk7vkoJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "b22bf14c-c92e-40dc-8de3-811679de1b21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzbASa1LhZd3y4FareHBMC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 81207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-28T18:33:29.813Z_

<details><summary>↩ Tool result · `toolu_01QAeEmUTDMYSb9H1rk7vkoJ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
8	
9	\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.
10	
11	\paragraph{Protocol.} We prune at $k \in \{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\}$ and report mean SR over 500 episodes. Multi-seed results ($\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\pm$ s.d.\ with per-seed breakdowns in the appendix.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
19	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
20	\label{fig:pruning_overview}
21	\end{figure}
22	
23	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
24	
25	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\geq}$98.0\% through $k{=}0.85$ (Appendix Table~\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\%, an 89\,pp method gap from identical removal fractions.
26	
27	\textbf{X-VLA (BART encoder, CV$\,{=}\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\,pp, yet the same model drops 27.4\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.
28	
29	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\ref{tab:full_results}; Section~\ref{sec:analysis}).
30	
31	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\leq}$6.6\% across all suites and methods, a catastrophic cliff detailed in Section~\ref{sec:pixel_shuffle}.
32	
33	\begin{table*}[t]
34	\centering
35	\small
36	\caption{Closed-loop SR (\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\ref{tab:full_results}.}
37	\label{tab:main_results}
38	\begin{tabular}{llcccc}
39	\toprule
40	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
41	\midrule
42	\multirow{4}{*}{$\pi_{0.5}$}
43	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 33.4 / 69.4 \\
44	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\
45	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\
46	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\
47	\midrule
48	\multirow{4}{*}{X-VLA}
49	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\
50	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\
51	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\
52	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\
53	\midrule
54	\multirow{4}{*}{SmolVLA}
55	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
56	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
57	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
58	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
59	\bottomrule
60	\end{tabular}
61	\end{table*}
62	
63	\subsection{Pixel-Shuffle Entanglement}
64	\label{sec:pixel_shuffle}
65	
66	\begin{figure*}[t]
67	\centering
68	\begin{subfigure}[t]{0.495\textwidth}
69	\centering
70	\includegraphics[width=\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
71	\caption{}\label{fig:pixel_shuffle}
72	\end{subfigure}
73	\hfill
74	\begin{subfigure}[t]{0.495\textwidth}
75	\centering
76	\includegraphics[width=\linewidth]{figures/paper/fig_method_gap.pdf}
77	\caption{}\label{fig:method_gap}
78	\end{subfigure}
79	\caption{Token entanglement and scoring sensitivity. \textbf{(a)}~Pixel-shuffle $4{\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \textbf{(b)}~Method gap $|\text{SR(L2)} - \text{SR(Random)}|$ at $k{=}0.95$: $\pi_{0.5}$'s Object gap (24.2\,pp) exceeds X-VLA's maximum (1.4\,pp) by $17{\times}$ (single seed except $\pi_{0.5}$ Long, $n{=}5$).}
80	\label{fig:entanglement_scoring}
81	\end{figure*}
82	
83	SmolVLA's pixel-shuffle $4{\times}4$ folding concatenates 16 patches per token (Figure~\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\leq}$6.6\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\ref{app:smolvla_ablation}).
84	
85	\subsection{Position Disruption vs.\ Information Loss}
86	\label{sec:zeromask}
87	
88	$\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\% on Object despite removing only 10\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\% SR while hard pruning collapses to 9.0\%. The 89\,pp gap is entirely attributable to position disruption: $\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.
89	
90	\subsection{Scoring Method Sensitivity and CV Diagnostic}
91	\label{sec:cv_sensitivity}
92	
93	CV predicts where scoring method choice becomes critical (Figure~\ref{fig:method_gap}). $\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\,pp, exceeding X-VLA's maximum (1.4\,pp) by $17{\times}$. At $k{=}0.5$, the importance margin on Object is $\Delta{=}{-}36.0$\,pp ($\pi_{0.5}$) and ${-}27.2$\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.
94	
95	\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\geq}$92.8\% while L2 falls 8--27\,pp below random; on $\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\,pp). On Long, attention cliffs $-$26.5\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\ref{fig:cliff_highlight}).
96	
97	\textbf{Inverted-U importance margin.} On $\pi_{0.5}$ Long, $\Delta$ peaks at $k{=}0.9$ ($+$46.9\,pp), diminishes at $k{=}0.95$ ($+$25.6\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\,pp) where both are inadequate. Near $k{\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\ref{fig:cliff_highlight}; Appendix Figure~\ref{fig:margin_profile}).
98	
99	\begin{figure}[t]
100	\centering
101	\includegraphics[width=0.75\linewidth]{figures/paper/fig_cliff_highlight.pdf}
102	\caption{Scoring method determines cliff behavior on $\pi_{0.5}$ Long (five-seed mean $\pm$ s.d.\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\,pp gap vs.\ L2) and recovery at $k{\leq}0.7$.}
103	\label{fig:cliff_highlight}
104	\end{figure}
105	
106	\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\pi_{0.5}$ at $k{=}0.85$: Object $\Delta{=}+$93\,pp $>$ Goal $+$35.2\,pp $>$ Long $+$33.2\,pp (Appendix Table~\ref{tab:full_results}).
107	
108	\subsection{VTR Recovery}
109	\label{sec:vtr_recovery}
110	
111	VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\sim}$22M parameters, $<$5\% of SmolVLA). At 75\% compression, VTR achieves 60.1 $\pm$ 1.3\% SR ($M{=}32$, $n{=}3$; Table~\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\%) by 15.3\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\pm$ 2.6\% ($p{=}0.15$), indicating the benefit stems from re-encoding, not the cross-attention mechanism. Cross-suite generalization: Spatial 53.2\%, Goal 56.4\%, both recovered from 0.0\% under hard pruning. For $\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\sim}$16\% while preserving full SR.
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\%; VTR exceeds the unpruned baseline at up to 87.5\% compression. Baseline (44.8\%) is our LoRA reproduction; official checkpoint achieves 59.2\% (Table~\ref{tab:main_results}).}
117	\label{tab:vtr_main}
118	\begin{tabular}{lccr}
119	\toprule
120	Configuration & $M$ & Compress.\ & SR (\%) \\
121	\midrule
122	\textit{Baseline (unpruned)} & 128 & 0\% & 44.8 \\
123	\textit{Hard pruning (any)} & -- & 5--50\% & 0.0 \\
124	\midrule
125	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
126	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
127	MLP adapter & 32 & 75\% & 63.4 $\pm$ 2.6 \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "9b5e3398-6b48-4cc6-b3e8-aff5879ac15a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop SR (\\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation}).\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, $<$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, $n{=}3$; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), indicating the benefit stems from re-encoding, not the cross-attention mechanism. Cross-suite generalization: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning. For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\\%; VTR exceeds the unpruned baseline at up to 87.5\\% compression. Baseline (44.8\\%) is our LoRA reproduction; official checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}).}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 131,
      "startLine": 1,
      "totalLines": 131
    }
  }
}
```

</details>

---

### Assistant

_source line 114_

Good. The experiments.tex looks well compressed. Now let me compress the cliff_highlight figure caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "6e56c504-49c7-43ba-9505-c2614c372db5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017u3kMYgz7ib76hMDgGZXRE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4570,
      "cache_read_input_tokens": 81554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4570
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

_source line 115_

<details open><summary>🔧 Tool call — Edit · `toolu_01EJpv31crV2xVmJXVdfcXRR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}",
  "new_string": "\\caption{Scoring method cliff behavior on $\\pi_{0.5}$ Long ($n{=}5$, mean $\\pm$ s.d.). L2 degrades monotonically; attention cliffs at $k{=}0.85$; random V-shapes with collapse at $k{=}0.9$.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "4490a4b9-589f-4829-8239-6898c156430a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017u3kMYgz7ib76hMDgGZXRE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4570,
      "cache_read_input_tokens": 81554,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4570
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

_source line 116 · 2026-05-28T18:33:40.388Z_

<details><summary>↩ Tool result · `toolu_01EJpv31crV2xVmJXVdfcXRR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "31ef99e4-6937-4b4a-84b7-2be99f9999c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "oldString": "\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}",
    "newString": "\\caption{Scoring method cliff behavior on $\\pi_{0.5}$ Long ($n{=}5$, mean $\\pm$ s.d.). L2 degrades monotonically; attention cliffs at $k{=}0.85$; random V-shapes with collapse at $k{=}0.9$.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop SR (\\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation}).\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, $<$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, $n{=}3$; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), indicating the benefit stems from re-encoding, not the cross-attention mechanism. Cross-suite generalization: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning. For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\\%; VTR exceeds the unpruned baseline at up to 87.5\\% compression. Baseline (44.8\\%) is our LoRA reproduction; official checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}).}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 99,
        "oldLines": 7,
        "newStart": 99,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}",
          "-\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}",
          "+\\caption{Scoring method cliff behavior on $\\pi_{0.5}$ Long ($n{=}5$, mean $\\pm$ s.d.). L2 degrades monotonically; attention cliffs at $k{=}0.85$; random V-shapes with collapse at $k{=}0.9$.}",
          " \\label{fig:cliff_highlight}",
          " \\end{figure}",
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

_source line 117_

Now let me also compress the entanglement_scoring figure caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "25ddd6e9-f50d-41db-9023-2a8365728258",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gxu1CEKTtDuxfzx7tKB7TD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 86124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 440
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

_source line 118_

<details open><summary>🔧 Tool call — Edit · `toolu_01Bz5kepnFUps8FdVNs3foqe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
  "old_string": "\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}",
  "new_string": "\\caption{\\textbf{(a)}~Pixel-shuffle $4{\\times}4$: each 16-patch block forms one token; removing any eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "b997eabb-a8f1-49ff-891a-d8e5da90e072",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gxu1CEKTtDuxfzx7tKB7TD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 86124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 440
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

_source line 119 · 2026-05-28T18:33:50.087Z_

<details><summary>↩ Tool result · `toolu_01Bz5kepnFUps8FdVNs3foqe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "34734ce9-7c77-4395-af3f-0f80b3bc6b72",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
    "oldString": "\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}",
    "newString": "\\caption{\\textbf{(a)}~Pixel-shuffle $4{\\times}4$: each 16-patch block forms one token; removing any eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$.}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmark.} We evaluate on LIBERO~\\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \\textbf{Object} (10 tasks, visually similar objects), \\textbf{Spatial} (10, relative spatial layouts), \\textbf{Goal} (10, goal-conditioned manipulation), and \\textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).\n\n\\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\\ref{tab:model_properties}): $\\pi_{0.5}$~\\cite{black2025pi05}, X-VLA~\\cite{zheng2025xvla}, OpenVLA~\\cite{kim2024openvla}, and SmolVLA~\\cite{shukor2025smolvla}. Two additional models ($\\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.\n\n\\paragraph{Protocol.} We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$ and report mean SR over 500 episodes. Multi-seed results ($\\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\\pm$ s.d.\\ with per-seed breakdowns in the appendix.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. On Object, L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$ (Appendix Table~\\ref{tab:full_results}), while random at $k{=}0.9$ collapses to 9.0\\%, an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods, a catastrophic cliff detailed in Section~\\ref{sec:pixel_shuffle}.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop SR (\\%) on LIBERO under L2 norm (L2) and random (R) pruning. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields. Removing any token eliminates an entire spatial block, collapsing SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints; Appendix~\\ref{app:smolvla_ablation}).\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption: $\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, the importance margin on Object is $\\Delta{=}{-}36.0$\\,pp ($\\pi_{0.5}$) and ${-}27.2$\\,pp (X-VLA): L2 scoring clusters spatially correlated tokens at the cost of spatial diversity.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Inverted-U importance margin.} On $\\pi_{0.5}$ Long, $\\Delta$ peaks at $k{=}0.9$ ($+$46.9\\,pp), diminishes at $k{=}0.95$ ($+$25.6\\,pp) where both methods suffice, and converges at $k{=}0.5$ ($+$1.3\\,pp) where both are inadequate. Near $k{\\approx}0.7$, the ranking inverts as L2 concentrates tokens spatially at the cost of coverage (Figure~\\ref{fig:cliff_highlight}; Appendix Figure~\\ref{fig:margin_profile}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method cliff behavior on $\\pi_{0.5}$ Long ($n{=}5$, mean $\\pm$ s.d.). L2 degrades monotonically; attention cliffs at $k{=}0.85$; random V-shapes with collapse at $k{=}0.9$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $\\Delta{=}+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp (Appendix Table~\\ref{tab:full_results}).\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, $<$5\\% of SmolVLA). At 75\\% compression, VTR achieves 60.1 $\\pm$ 1.3\\% SR ($M{=}32$, $n{=}3$; Table~\\ref{tab:vtr_main}), exceeding the unpruned LoRA baseline (44.8\\%) by 15.3\\,pp. An extended training control rules out additional optimization as the source ($p > 0.9$; Appendix~\\ref{app:smart_compress_details}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), indicating the benefit stems from re-encoding, not the cross-attention mechanism. Cross-suite generalization: Spatial 53.2\\%, Goal 56.4\\%, both recovered from 0.0\\% under hard pruning. For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0\\%; VTR exceeds the unpruned baseline at up to 87.5\\% compression. Baseline (44.8\\%) is our LoRA reproduction; official checkpoint achieves 59.2\\% (Table~\\ref{tab:main_results}).}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
    "structuredPatch": [
      {
        "oldStart": 76,
        "oldLines": 7,
        "newStart": 76,
        "newLines": 7,
        "lines": [
          " \\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}",
          " \\caption{}\\label{fig:method_gap}",
          " \\end{subfigure}",
          "-\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}",
          "+\\caption{\\textbf{(a)}~Pixel-shuffle $4{\\times}4$: each 16-patch block forms one token; removing any eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$.}",
          " \\label{fig:entanglement_scoring}",
          " \\end{figure*}",
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

_source line 120_

Now let me also add some LaTeX spacing optimization to main.tex to tighten things up.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "9b30262f-eea1-47a8-b244-5a7ecd917983",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLudH6sgzDkTutEJ7i41f9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 86564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 121_

<details open><summary>🔧 Tool call — Read · `toolu_0112DeP3mdxBibjwDRBepewZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ce75fc27-d292-4d60-9e39-aac1179e6d74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FLudH6sgzDkTutEJ7i41f9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 86564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 122 · 2026-05-28T18:33:54.532Z_

<details><summary>↩ Tool result · `toolu_0112DeP3mdxBibjwDRBepewZ`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	\usepackage{wrapfig}
13	
14	% Tighten float spacing for page limit
15	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{8pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{0pt}
20	
21	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{abstract}
27	
28	\keywords{vision-language-action models, token pruning, robot learning}
29	
30	\input{introduction}
31	
32	\input{related_work}
33	
34	\input{method}
35	
36	\input{experiments}
37	
38	\input{conclusion}
39	
40	\input{limitations}
41	
42	\bibliography{references}
43	
44	\input{appendix}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "7f42c6a5-2bb9-41de-9bd2-6ad1e0ea39be",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.\n% \\usepackage[final]{corl_2026} % Uncomment for camera-ready.\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{wrapfig}\n\n% Tighten float spacing for page limit\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\n\\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\\\Vision Connectors and VLA Token Compressibility}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\keywords{vision-language-action models, token pruning, robot learning}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
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

_source line 123_

<details open><summary>🔧 Tool call — Edit · `toolu_016Z82DAzQ7NSBZamcW3SkSR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
  "old_string": "% Tighten float spacing for page limit\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{0pt}",
  "new_string": "% Tighten float spacing for page limit\n\\setlength{\\textfloatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{3pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\\setlength{\\abovedisplayskip}{6pt plus 2pt minus 4pt}\n\\setlength{\\belowdisplayskip}{6pt plus 2pt minus 4pt}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "7a203ebf-5b75-4605-871b-d0d3adc31e75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TG2eENai5ZSVf7vZSykA2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 87067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 599
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

_source line 124 · 2026-05-28T18:34:01.373Z_

<details><summary>↩ Tool result · `toolu_016Z82DAzQ7NSBZamcW3SkSR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ee550db0-ea57-42b0-97fd-1791e8c3400d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
    "oldString": "% Tighten float spacing for page limit\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{0pt}",
    "newString": "% Tighten float spacing for page limit\n\\setlength{\\textfloatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{6pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{3pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\\setlength{\\abovedisplayskip}{6pt plus 2pt minus 4pt}\n\\setlength{\\belowdisplayskip}{6pt plus 2pt minus 4pt}",
    "originalFile": "\\documentclass{article}\n\n\\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.\n% \\usepackage[final]{corl_2026} % Uncomment for camera-ready.\n\n\\usepackage{amsmath,amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{wrapfig}\n\n% Tighten float spacing for page limit\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\n\\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\\\Vision Connectors and VLA Token Compressibility}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\keywords{vision-language-action models, token pruning, robot learning}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{conclusion}\n\n\\input{limitations}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 11,
        "newStart": 12,
        "newLines": 13,
        "lines": [
          " \\usepackage{wrapfig}",
          " ",
          " % Tighten float spacing for page limit",
          "-\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}",
          "-\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}",
          "-\\setlength{\\intextsep}{8pt plus 2pt minus 4pt}",
          "-\\setlength{\\abovecaptionskip}{4pt}",
          "+\\setlength{\\textfloatsep}{6pt plus 2pt minus 4pt}",
          "+\\setlength{\\floatsep}{6pt plus 2pt minus 4pt}",
          "+\\setlength{\\intextsep}{6pt plus 2pt minus 4pt}",
          "+\\setlength{\\abovecaptionskip}{3pt}",
          " \\setlength{\\belowcaptionskip}{0pt}",
          "+\\setlength{\\abovedisplayskip}{6pt plus 2pt minus 4pt}",
          "+\\setlength{\\belowdisplayskip}{6pt plus 2pt minus 4pt}",
          " ",
          " \\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\\\Vision Connectors and VLA Token Compressibility}",
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

_source line 125_

Now let me compile and check the page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "752bd882-edc1-4afe-a3e9-cfbb08f0ceed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRbDC8gkeDYbH58zxVH99S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 473,
      "cache_read_input_tokens": 87666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 473
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 126_

<details open><summary>🔧 Tool call — Bash · `toolu_01LoKB72zCbMCEaTKHDspQt8`</summary>

```json
{
  "command": "rm -f main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out main.pdf && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -10",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "a3ef870e-98d6-4010-8489-2b851a4d34a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRbDC8gkeDYbH58zxVH99S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 473,
      "cache_read_input_tokens": 87666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 473
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-28T18:34:13.484Z_

<details><summary>↩ Tool result · `toolu_01LoKB72zCbMCEaTKHDspQt8`</summary>

```text
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "f2cf5130-2c1e-40c7-a6c0-04042c594119",
  "tool_use_result": {
    "stdout": "Latexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 128_

<details open><summary>🔧 Tool call — Bash · `toolu_017pky72Bk86G5n682eUJLR6`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\nfor i, p in enumerate(pages):\n    lines = p.strip().split('\\n')\n    first = next((l.strip() for l in lines if l.strip()), '')\n    print(f'Page {i+1}: {first[:80]}')\n    if 'references' in first.lower() or first.startswith('[1]'):\n        print(f'=> References start at page {i+1}')\n        print(f'=> Body pages: {i}')\n        break\nprint(f'Total pages: {len(pages)-1}')\n\" 2>&1 | head -20\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "0eee10de-d4da-4416-94f7-e68cafa56780",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HEFyfXntNXtCg5sRbRHHhH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 303,
      "cache_read_input_tokens": 88139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 303
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-28T18:34:19.887Z_

<details><summary>↩ Tool result · `toolu_017pky72Bk86G5n682eUJLR6`</summary>

```text
Page 1: Why Token Pruning Crashes Some Robot Policies but
Page 2: Figure 1: Overview of VLA token compressibility. (a) The same robot observation 
Page 3: Figure 2: Vision connector architectures across four closed-loop VLAs, ordered b
Page 4: Table 1: VLA models evaluated. Coupling indicates independent vs. cross-token pr
Page 5: 100                                    π0.5 (CV=0.055, L2)
Page 6: Table 2: Closed-loop SR (%) on LIBERO under L2 norm (L2) and random (R) pruning.
Page 7: π0.5 Long — Scoring Method Determines Cliff Behavior
Page 8: Table 3: VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0%; VTR excee
Page 9: 221    [4] J. Cheng, H. Wang, W. Li, G. Wang, Y. Zhang, X. Tang, J. Wu, X. Chen,
Page 10: 265   [20] K. Black, N. Brown, N. M. M. Shafiullah, et al. π0.5 : a vision-langu
Page 11: 289   B         Extended Discussion
Page 12: 311   method succeeds. CV remains a valid connector diagnostic, but the optimal 
Page 13: Success Rate (%) at k = 0.9
Page 14: π0.5 Long — Importance Margin Profile
Page 15: 399   Model-specific retention ratios reflect each architecture’s token count an
Page 16: Table 7: SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object 
Page 17: 432   F.4   OpenVLA Full Degradation Curve
Page 18: Table 13: π0.5 pruning across LIBERO-Object (baseline 98.2%) and LIBERO-Spatial 
Page 19: LIBERO-Object (CV=0.066)                                                        
Page 20: 479   qualitatively different computation regime, potentially relying on coarser
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "3aff5a26-c3eb-4814-af07-69881e0b2b74",
  "tool_use_result": {
    "stdout": "Page 1: Why Token Pruning Crashes Some Robot Policies but\nPage 2: Figure 1: Overview of VLA token compressibility. (a) The same robot observation \nPage 3: Figure 2: Vision connector architectures across four closed-loop VLAs, ordered b\nPage 4: Table 1: VLA models evaluated. Coupling indicates independent vs. cross-token pr\nPage 5: 100                                    π0.5 (CV=0.055, L2)\nPage 6: Table 2: Closed-loop SR (%) on LIBERO under L2 norm (L2) and random (R) pruning.\nPage 7: π0.5 Long — Scoring Method Determines Cliff Behavior\nPage 8: Table 3: VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0%; VTR excee\nPage 9: 221    [4] J. Cheng, H. Wang, W. Li, G. Wang, Y. Zhang, X. Tang, J. Wu, X. Chen,\nPage 10: 265   [20] K. Black, N. Brown, N. M. M. Shafiullah, et al. π0.5 : a vision-langu\nPage 11: 289   B         Extended Discussion\nPage 12: 311   method succeeds. CV remains a valid connector diagnostic, but the optimal \nPage 13: Success Rate (%) at k = 0.9\nPage 14: π0.5 Long — Importance Margin Profile\nPage 15: 399   Model-specific retention ratios reflect each architecture’s token count an\nPage 16: Table 7: SmolVLA baseline (bypass mode) per-task success rates on LIBERO-Object \nPage 17: 432   F.4   OpenVLA Full Degradation Curve\nPage 18: Table 13: π0.5 pruning across LIBERO-Object (baseline 98.2%) and LIBERO-Spatial \nPage 19: LIBERO-Object (CV=0.066)                                                        \nPage 20: 479   qualitatively different computation regime, potentially relying on coarser",
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

_source line 130_

Progress: body is now 8 pages (references start page 9). But let me check more carefully - page 8 has Table 3 + Conclusion + Limitations. Let me verify the content of page 8 more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "66b17db3-be88-416a-8e6d-87ae61cecdc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zqua1Bffw7ux7N6m3y6nc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 88442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 886
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

_source line 131_

<details open><summary>🔧 Tool call — Bash · `toolu_01XXVZAnRpMvBTrkQbYYB7pt`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\n# Check page 8 and 9 content\nfor i in [7, 8]:\n    print(f'=== PAGE {i+1} ===')\n    print(pages[i][:500])\n    print('...')\n    print(pages[i][-300:])\n    print()\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "42613d59-40c8-4f97-ac68-2658efc0c5fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zqua1Bffw7ux7N6m3y6nc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 88442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 886
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

_source line 132 · 2026-05-28T18:34:29.388Z_

<details><summary>↩ Tool result · `toolu_01XXVZAnRpMvBTrkQbYYB7pt`</summary>

```text
=== PAGE 8 ===
      Table 3: VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0%; VTR exceeds the
      unpruned baseline at up to 87.5% compression. Baseline (44.8%) is our LoRA reproduction; official
      checkpoint achieves 59.2% (Table 2).
                               Configuration         M        Compress.      SR (%)
                               Baseline (unpruned)   128         0%            44.8
                               Hard pruning (any)     –        5–50%            0.0
        
...
g, C. Ge, Z. Tong, Y. Song, J. Wang, and P. Xie. Not all patches are what you need: Ex-
219        pediting vision transformers via token reorganizations. In International Conference on Learn-
220        ing Representations (ICLR), 2022.


                                                          8


=== PAGE 9 ===
221    [4] J. Cheng, H. Wang, W. Li, G. Wang, Y. Zhang, X. Tang, J. Wu, X. Chen, Y. Liu, and W. Zhang.
222        VLA-IAP: Training-free visual token pruning via interaction alignment for vision-language-
223        action models. arXiv preprint arXiv:2603.22991, 2026.

224    [5] S. Xu, Y. Wang, C. Xia, D. Zhu, T. Huang, and C. Xu. VLA-Cache: Efficient vision-language-
225        action manipulation via adaptive token caching. In Advances in Neural Information Processing
226        Systems (Neu
...
kert, and Z. Wang.
262        Real-time single image and video super-resolution using an efficient sub-pixel convolutional
263        neural network. In IEEE/CVF Conference on Computer Vision and Pattern Recognition
264        (CVPR), 2016.


                                                       9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "5c0509c1-0d5b-40f1-847a-dc7ad565fe20",
  "tool_use_result": {
    "stdout": "=== PAGE 8 ===\n      Table 3: VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0%; VTR exceeds the\n      unpruned baseline at up to 87.5% compression. Baseline (44.8%) is our LoRA reproduction; official\n      checkpoint achieves 59.2% (Table 2).\n                               Configuration         M        Compress.      SR (%)\n                               Baseline (unpruned)   128         0%            44.8\n                               Hard pruning (any)     –        5–50%            0.0\n        \n...\ng, C. Ge, Z. Tong, Y. Song, J. Wang, and P. Xie. Not all patches are what you need: Ex-\n219        pediting vision transformers via token reorganizations. In International Conference on Learn-\n220        ing Representations (ICLR), 2022.\n\n\n                                                          8\n\n\n=== PAGE 9 ===\n221    [4] J. Cheng, H. Wang, W. Li, G. Wang, Y. Zhang, X. Tang, J. Wu, X. Chen, Y. Liu, and W. Zhang.\n222        VLA-IAP: Training-free visual token pruning via interaction alignment for vision-language-\n223        action models. arXiv preprint arXiv:2603.22991, 2026.\n\n224    [5] S. Xu, Y. Wang, C. Xia, D. Zhu, T. Huang, and C. Xu. VLA-Cache: Efficient vision-language-\n225        action manipulation via adaptive token caching. In Advances in Neural Information Processing\n226        Systems (Neu\n...\nkert, and Z. Wang.\n262        Real-time single image and video super-resolution using an efficient sub-pixel convolutional\n263        neural network. In IEEE/CVF Conference on Computer Vision and Pattern Recognition\n264        (CVPR), 2016.\n\n\n                                                       9",
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

_source line 133_

Body pages = 8 (page 8 ends with references starting on the same page). Wait, it looks like references actually start on page 8. Let me check more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "971765fd-66bf-40f8-941d-1a7865ed8839",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALGqY5wGNvBK2dwxKD3PPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 89328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 723
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

_source line 134_

<details open><summary>🔧 Tool call — Bash · `toolu_01VvZ2rGVvD5ZMU6avrnZNeX`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\npage8 = pages[7]\n# Find if 'References' or numbered refs appear\nlines = page8.split('\\n')\nfor i, line in enumerate(lines):\n    stripped = line.strip()\n    if stripped and ('References' in stripped or stripped.startswith('[1]') or stripped.startswith('[2]') or stripped.startswith('[3]')):\n        print(f'Line {i}: {stripped[:100]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "9fbdffe8-a749-4ec9-a2b7-b6cfeacdfc75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALGqY5wGNvBK2dwxKD3PPB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 89328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 723
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

_source line 135 · 2026-05-28T18:34:35.797Z_

<details><summary>↩ Tool result · `toolu_01VvZ2rGVvD5ZMU6avrnZNeX`</summary>

```text
Line 42: 212   References
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "7b7c5309-b053-4b1e-b858-75ef6401db53",
  "tool_use_result": {
    "stdout": "Line 42: 212   References",
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

_source line 136_

References header appears on page 8. So the body is only 8 pages (content through page 8 including some references). But wait, for CoRL the body pages should be counted as everything before References. Let me check more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "45990914-9662-4be1-894c-8abc8aeecc05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGP3Jk1AtMEhK6c1sSNKDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 90051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 137_

<details open><summary>🔧 Tool call — Bash · `toolu_019KNuknAKS6pK7V8mRTNPfE`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\npage8 = pages[7]\nlines = page8.split('\\n')\n# print what's on page 8 after line 30\nfor i, line in enumerate(lines):\n    if i >= 25:\n        print(f'{i}: {line.rstrip()[:100]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "d878e2d8-de8c-4bd1-b087-5154be39c8f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGP3Jk1AtMEhK6c1sSNKDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 90051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 138 · 2026-05-28T18:34:41.949Z_

<details><summary>↩ Tool result · `toolu_019KNuknAKS6pK7V8mRTNPfE`</summary>

```text
25: 198   6   Limitations
26: 
27: 199   All evaluations use LIBERO simulation; no sim-to-real evidence is provided; real-robot evaluat
28: 200   with domain shift would strengthen practical applicability. The six architectures differ in ba
29: 201   encoder, and scale beyond the connector, preventing full causal isolation of the connector eff
30: 202   controlled studies varying only the connector within a fixed backbone would sharpen causal cla
31: 203   The CV–SR correlation relies on four closed-loop models, too few for a general law; expanding
32: 204   the model pool as new VLA architectures emerge will test whether CV generalizes as a universal
33: 205   diagnostic. VTR is validated on SmolVLA only; extending to other entangling connectors (e.g.,
34: 206   cross-attention encoders) would test generality of the re-encoding approach. Only L2-norm and
35: 207   random scoring are systematically compared; gradient-based importance scoring or learned pruni
36: 208   masks could yield better token selection. Most conditions use a single seed; π0.5 Long uses fi
37: 209   means (n=5, s.d. ≤2.7 pp); future work should adopt multi-seed evaluation across all condition
38: 210   quantify variance. AI disclosure: This work used AI tools (Claude) for code development and
39: 211   manuscript drafting; all scientific claims are the authors’ own.
40: 
41: 
42: 212   References
43: 213    [1] Y. Rao, W. Zhao, B. Liu, J. Lu, J. Zhou, and C.-J. Hsieh. DynamicViT: Efficient vision tr
44: 214        formers with dynamic token sparsification. In Advances in Neural Information Processing
45: 215        Systems (NeurIPS), 2021.
46: 
47: 216    [2] D. Bolya, C.-Y. Fu, X. Dai, P. Zhang, C. Feichtenhofer, and J. Hoffman. Token merging: Yo
48: 217        ViT but faster. In International Conference on Learning Representations (ICLR), 2023.
49: 
50: 218    [3] Y. Liang, C. Ge, Z. Tong, Y. Song, J. Wang, and P. Xie. Not all patches are what you need
51: 219        pediting vision transformers via token reorganizations. In International Conference on Le
52: 220        ing Representations (ICLR), 2022.
53: 
54: 
55:                                                           8
56:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "e7a84cdb-6a0f-4162-af07-475c499df672",
  "tool_use_result": {
    "stdout": "25: 198   6   Limitations\n26: \n27: 199   All evaluations use LIBERO simulation; no sim-to-real evidence is provided; real-robot evaluat\n28: 200   with domain shift would strengthen practical applicability. The six architectures differ in ba\n29: 201   encoder, and scale beyond the connector, preventing full causal isolation of the connector eff\n30: 202   controlled studies varying only the connector within a fixed backbone would sharpen causal cla\n31: 203   The CV–SR correlation relies on four closed-loop models, too few for a general law; expanding\n32: 204   the model pool as new VLA architectures emerge will test whether CV generalizes as a universal\n33: 205   diagnostic. VTR is validated on SmolVLA only; extending to other entangling connectors (e.g.,\n34: 206   cross-attention encoders) would test generality of the re-encoding approach. Only L2-norm and\n35: 207   random scoring are systematically compared; gradient-based importance scoring or learned pruni\n36: 208   masks could yield better token selection. Most conditions use a single seed; π0.5 Long uses fi\n37: 209   means (n=5, s.d. ≤2.7 pp); future work should adopt multi-seed evaluation across all condition\n38: 210   quantify variance. AI disclosure: This work used AI tools (Claude) for code development and\n39: 211   manuscript drafting; all scientific claims are the authors’ own.\n40: \n41: \n42: 212   References\n43: 213    [1] Y. Rao, W. Zhao, B. Liu, J. Lu, J. Zhou, and C.-J. Hsieh. DynamicViT: Efficient vision tr\n44: 214        formers with dynamic token sparsification. In Advances in Neural Information Processing\n45: 215        Systems (NeurIPS), 2021.\n46: \n47: 216    [2] D. Bolya, C.-Y. Fu, X. Dai, P. Zhang, C. Feichtenhofer, and J. Hoffman. Token merging: Yo\n48: 217        ViT but faster. In International Conference on Learning Representations (ICLR), 2023.\n49: \n50: 218    [3] Y. Liang, C. Ge, Z. Tong, Y. Song, J. Wang, and P. Xie. Not all patches are what you need\n51: 219        pediting vision transformers via token reorganizations. In International Conference on Le\n52: 220        ing Representations (ICLR), 2022.\n53: \n54: \n55:                                                           8\n56:",
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

_source line 139_

The Limitations section ends on page 8, and References also begin on page 8. This means the body content (including Limitations) fits within 8 pages. The fact that References start on the same page is fine since CoRL counts body pages as content before References.

Let me now check for undefined references and compile warnings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "71fc2e0e-34fb-487b-939e-94c38c3afa54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gMddxCpSSGRQhw8cZ6DJr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 90323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 898
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

_source line 140_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ru35fC53D5bpVdvGZFvwgq`</summary>

```json
{
  "command": "grep -c \"undefined\" main.log 2>/dev/null; grep \"Warning.*undefined\" main.log 2>/dev/null | head -10; grep \"Warning.*multiply\" main.log 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "64dd67cf-957d-4b67-88c1-0336003bbc9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gMddxCpSSGRQhw8cZ6DJr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 90323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 898
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

_source line 141 · 2026-05-28T18:34:52.430Z_

<details><summary>↩ Tool result · `toolu_01Ru35fC53D5bpVdvGZFvwgq`</summary>

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
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "18dbe0e9-60c5-4f0f-a09e-514cfa064bcf",
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

### Assistant

_source line 142_

No undefined references. Let me also check for "??" in the PDF output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "90922a23-8800-4ff1-99d6-a03a6e450712",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyhxBCTHU3xnTto2DeGUAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 91221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 143_

<details open><summary>🔧 Tool call — Bash · `toolu_01TPRvHVwj7PttqvsrrjGeij`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = r.stdout\n# Find ?? patterns\nimport re\nmatches = re.findall(r'\\?\\?', text)\nprint(f'Number of ?? occurrences: {len(matches)}')\nif matches:\n    for m in re.finditer(r'.{20}\\?\\?.{20}', text):\n        print(f'  Context: ...{m.group()}...')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "61f22c67-83cd-4222-a77e-3e817bfc9504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LyhxBCTHU3xnTto2DeGUAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 91221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 190
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

_source line 144 · 2026-05-28T18:34:57.807Z_

<details><summary>↩ Tool result · `toolu_01TPRvHVwj7PttqvsrrjGeij`</summary>

```text
Number of ?? occurrences: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "cf60a897-71f1-46b1-964b-a927dae2e1e1",
  "tool_use_result": {
    "stdout": "Number of ?? occurrences: 0",
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

_source line 145_

Zero undefined refs, zero "??". Now let me verify the figure float positions (Task 3).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "e4964683-c806-404d-82b7-9f96dc820754",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M7TGyoBgHmSYVmyNAo6gBm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 91411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 326
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

_source line 146_

<details open><summary>🔧 Tool call — Grep · `toolu_01MYKNyXFwVqAFkUp1xKY1xk`</summary>

```json
{
  "pattern": "\\\\begin\\{figure\\}|\\\\begin\\{figure\\*\\}|\\\\begin\\{table\\}|\\\\begin\\{table\\*\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "glob": "*.tex",
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
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "2aefc7cc-6d0b-47b5-931b-ce9eb6b1b622",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M7TGyoBgHmSYVmyNAo6gBm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 91411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 326
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

_source line 147 · 2026-05-28T18:35:04.217Z_

<details><summary>↩ Tool result · `toolu_01MYKNyXFwVqAFkUp1xKY1xk`</summary>

```text
experiments.tex:16:\begin{figure}[t]
experiments.tex:33:\begin{table*}[t]
experiments.tex:66:\begin{figure*}[t]
experiments.tex:99:\begin{figure}[t]
experiments.tex:113:\begin{table}[t]
results_v2.tex:13:\begin{table*}[t]
results_v2.tex:71:\begin{table}[t]
results_v2.tex:104:\begin{table}[t]
results_v2.tex:134:\begin{figure}[t]
sections/analysis.tex:39:\begin{figure}[t]
sections/analysis.tex:69:\begin{figure}[t]
sections/analysis.tex:85:\begin{table}[t]
sections/experiments.tex:24:\begin{table}[t]
sections/experiments.tex:70:\begin{figure}[t]
sections/results_draft.tex:25:\begin{table}[t]
sections/results_draft.tex:67:\begin{table}[t]
sections/background.tex:15:\begin{figure}[t]
method.tex:9:\begin{figure*}[t]
method.tex:16:\begin{table}[t]
background.tex:15:\begin{figure}[t]
appendix.tex:8:\begin{table*}[ht]
appendix.tex:58:\begin{figure}[ht]
appendix.tex:72:\begin{figure}[ht]
appendix.tex:79:\begin{figure}[ht]
appendix.tex:95:\begin{table}[ht]
appendix.tex:145:\begin{table}[ht]
appendix.tex:185:\begin{table}[ht]
appendix.tex:214:\begin{table}[ht]
appendix.tex:241:\begin{table}[ht]
appendix.tex:268:\begin{table}[ht]
appendix.tex:290:\begin{table}[ht]
appendix.tex:312:\begin{table}[ht]
appendix.tex:331:\begin{table}[ht]
appendix.tex:354:\begin{figure}[ht]
appendix.tex:368:\begin{figure}[ht]
appendix.tex:382:\begin{figure}[ht]
appendix.tex:398:\begin{table}[ht]
appendix.tex:417:\begin{table}[ht]
appendix.tex:438:\begin{table}[ht]
appendix.tex:467:\begin{table}[ht]
appendix.tex:494:\begin{table}[ht]
appendix.tex:515:\begin{table}[ht]
appendix.tex:548:\begin{table}[ht]
appendix.tex:579:\begin{table}[ht]
appendix.tex:601:\begin{table}[ht]
appendix.tex:666:\begin{table}[ht]
appendix.tex:693:\begin{figure}[ht]
appendix.tex:820:\begin{table}[ht]
appendix.tex:879:\begin{table}[h]
appendix.tex:900:\begin{table}[ht]
appendix.tex:917:\begin{table}[h]
introduction.tex:4:\begin{figure*}[t]
results.tex:13:\begin{table*}[t]
results.tex:71:\begin{table}[t]
results.tex:104:\begin{figure}[t]
experiments_deprecated.tex:13:\begin{table}[t]
experiments_deprecated.tex:59:\begin{figure}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "6aeddb35-4cc6-4bfe-8001-d862d5736456",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "experiments.tex:16:\\begin{figure}[t]\nexperiments.tex:33:\\begin{table*}[t]\nexperiments.tex:66:\\begin{figure*}[t]\nexperiments.tex:99:\\begin{figure}[t]\nexperiments.tex:113:\\begin{table}[t]\nresults_v2.tex:13:\\begin{table*}[t]\nresults_v2.tex:71:\\begin{table}[t]\nresults_v2.tex:104:\\begin{table}[t]\nresults_v2.tex:134:\\begin{figure}[t]\nsections/analysis.tex:39:\\begin{figure}[t]\nsections/analysis.tex:69:\\begin{figure}[t]\nsections/analysis.tex:85:\\begin{table}[t]\nsections/experiments.tex:24:\\begin{table}[t]\nsections/experiments.tex:70:\\begin{figure}[t]\nsections/results_draft.tex:25:\\begin{table}[t]\nsections/results_draft.tex:67:\\begin{table}[t]\nsections/background.tex:15:\\begin{figure}[t]\nmethod.tex:9:\\begin{figure*}[t]\nmethod.tex:16:\\begin{table}[t]\nbackground.tex:15:\\begin{figure}[t]\nappendix.tex:8:\\begin{table*}[ht]\nappendix.tex:58:\\begin{figure}[ht]\nappendix.tex:72:\\begin{figure}[ht]\nappendix.tex:79:\\begin{figure}[ht]\nappendix.tex:95:\\begin{table}[ht]\nappendix.tex:145:\\begin{table}[ht]\nappendix.tex:185:\\begin{table}[ht]\nappendix.tex:214:\\begin{table}[ht]\nappendix.tex:241:\\begin{table}[ht]\nappendix.tex:268:\\begin{table}[ht]\nappendix.tex:290:\\begin{table}[ht]\nappendix.tex:312:\\begin{table}[ht]\nappendix.tex:331:\\begin{table}[ht]\nappendix.tex:354:\\begin{figure}[ht]\nappendix.tex:368:\\begin{figure}[ht]\nappendix.tex:382:\\begin{figure}[ht]\nappendix.tex:398:\\begin{table}[ht]\nappendix.tex:417:\\begin{table}[ht]\nappendix.tex:438:\\begin{table}[ht]\nappendix.tex:467:\\begin{table}[ht]\nappendix.tex:494:\\begin{table}[ht]\nappendix.tex:515:\\begin{table}[ht]\nappendix.tex:548:\\begin{table}[ht]\nappendix.tex:579:\\begin{table}[ht]\nappendix.tex:601:\\begin{table}[ht]\nappendix.tex:666:\\begin{table}[ht]\nappendix.tex:693:\\begin{figure}[ht]\nappendix.tex:820:\\begin{table}[ht]\nappendix.tex:879:\\begin{table}[h]\nappendix.tex:900:\\begin{table}[ht]\nappendix.tex:917:\\begin{table}[h]\nintroduction.tex:4:\\begin{figure*}[t]\nresults.tex:13:\\begin{table*}[t]\nresults.tex:71:\\begin{table}[t]\nresults.tex:104:\\begin{figure}[t]\nexperiments_deprecated.tex:13:\\begin{table}[t]\nexperiments_deprecated.tex:59:\\begin{figure}[t]",
    "numLines": 57
  }
}
```

</details>

---

### Assistant

_source line 148_

All main body figures/tables already use `[t]`. The appendix uses `[ht]` which is fine. Everything looks correct for figure positioning.

Let me do a final compile and full verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "e31556c8-65b3-4a7d-a461-9d2e19ac99ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6ABZAukc1GraoSgwH8EWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 91737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1108
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

_source line 149_

<details open><summary>🔧 Tool call — Bash · `toolu_0115ExSe5Z8y9RFVJZ3Q3c7Q`</summary>

```json
{
  "command": "rm -f main.aux main.bbl main.blg main.fdb_latexmk main.fls main.log main.out main.pdf && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tail -10",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "e911d0a6-813f-42f0-96e6-35b07faeca62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6ABZAukc1GraoSgwH8EWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 91737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1108
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

_source line 150 · 2026-05-28T18:35:14.484Z_

<details><summary>↩ Tool result · `toolu_0115ExSe5Z8y9RFVJZ3Q3c7Q`</summary>

```text
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "6544684d-7014-4d55-98e1-fcb8b87571d9",
  "tool_use_result": {
    "stdout": "Latexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 151_

<details open><summary>🔧 Tool call — Bash · `toolu_01UsUVEghTyzMgneVuMvy3Jj`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\nimport re\n\n# Find references page\nfor i, p in enumerate(pages):\n    lines = p.strip().split('\\n')\n    for line in lines:\n        stripped = line.strip()\n        if stripped == 'References' or (stripped.startswith('[1]') and i > 2):\n            print(f'References start at page {i+1}')\n            print(f'Body pages: {i}')\n            break\n    else:\n        continue\n    break\n\n# Check for ??\ntext = r.stdout\nqq = len(re.findall(r'\\?\\?', text))\nprint(f'Undefined refs (??): {qq}')\nprint(f'Total pages: {len(pages)-1}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "0cef45c5-234a-4e61-ae60-a985c5d56a93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155BGJMkzVjZxS9Xe96ESCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 92845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 338
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-28T18:35:21.160Z_

<details><summary>↩ Tool result · `toolu_01UsUVEghTyzMgneVuMvy3Jj`</summary>

```text
Undefined refs (??): 0
Total pages: 31
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "dcfc67bf-0426-4fed-8658-14fbcd1de80e",
  "tool_use_result": {
    "stdout": "Undefined refs (??): 0\nTotal pages: 31",
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

_source line 153_

<details><summary>Logged reasoning block</summary>

```text
The script didn't print "References start at page" or "Body pages" because the logic to find "References" wasn't working correctly. Let me try a simpler approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ec5ba8be-a125-466a-88d2-11d0a5802831",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYPNvWRyTKXFCHvbXPEtYy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 93183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 307
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

_source line 154_

<details open><summary>🔧 Tool call — Bash · `toolu_01NptsSLYgFuCBvkpSQoYzaE`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\nfor i, p in enumerate(pages):\n    lines = p.strip().split('\\n')\n    first = next((l.strip() for l in lines if l.strip()), '')\n    print(f'Page {i+1}: {first[:90]}')\n\" 2>&1 | head -15\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "58fae0b0-356d-423f-95c1-aa576d189c48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WYPNvWRyTKXFCHvbXPEtYy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 307,
      "cache_read_input_tokens": 93183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 307
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

_source line 155 · 2026-05-28T18:35:27.187Z_

<details><summary>↩ Tool result · `toolu_01NptsSLYgFuCBvkpSQoYzaE`</summary>

```text
Page 1: Why Token Pruning Crashes Some Robot Policies but
Page 2: Figure 1: Overview of VLA token compressibility. (a) The same robot observation produces q
Page 3: Figure 2: Vision connector architectures across four closed-loop VLAs, ordered by increasi
Page 4: Table 1: VLA models evaluated. Coupling indicates independent vs. cross-token processing. 
Page 5: 100                                    π0.5 (CV=0.055, L2)
Page 6: Table 2: Closed-loop SR (%) on LIBERO under L2 norm (L2) and random (R) pruning. π0.5 Long
Page 7: π0.5 Long — Scoring Method Determines Cliff Behavior
Page 8: Table 3: VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0%; VTR exceeds the
Page 9: 221    [4] J. Cheng, H. Wang, W. Li, G. Wang, Y. Zhang, X. Tang, J. Wu, X. Chen, Y. Liu, a
Page 10: 265   [20] K. Black, N. Brown, N. M. M. Shafiullah, et al. π0.5 : a vision-language-action
Page 11: 289   B         Extended Discussion
Page 12: 311   method succeeds. CV remains a valid connector diagnostic, but the optimal scoring st
Page 13: Success Rate (%) at k = 0.9
Page 14: π0.5 Long — Importance Margin Profile
Page 15: 399   Model-specific retention ratios reflect each architecture’s token count and expected
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "69e70f62-b1bb-416d-8103-a1a06ce7430f",
  "tool_use_result": {
    "stdout": "Page 1: Why Token Pruning Crashes Some Robot Policies but\nPage 2: Figure 1: Overview of VLA token compressibility. (a) The same robot observation produces q\nPage 3: Figure 2: Vision connector architectures across four closed-loop VLAs, ordered by increasi\nPage 4: Table 1: VLA models evaluated. Coupling indicates independent vs. cross-token processing. \nPage 5: 100                                    π0.5 (CV=0.055, L2)\nPage 6: Table 2: Closed-loop SR (%) on LIBERO under L2 norm (L2) and random (R) pruning. π0.5 Long\nPage 7: π0.5 Long — Scoring Method Determines Cliff Behavior\nPage 8: Table 3: VTR on SmolVLA (LIBERO-Object). Hard pruning collapses to 0%; VTR exceeds the\nPage 9: 221    [4] J. Cheng, H. Wang, W. Li, G. Wang, Y. Zhang, X. Tang, J. Wu, X. Chen, Y. Liu, a\nPage 10: 265   [20] K. Black, N. Brown, N. M. M. Shafiullah, et al. π0.5 : a vision-language-action\nPage 11: 289   B         Extended Discussion\nPage 12: 311   method succeeds. CV remains a valid connector diagnostic, but the optimal scoring st\nPage 13: Success Rate (%) at k = 0.9\nPage 14: π0.5 Long — Importance Margin Profile\nPage 15: 399   Model-specific retention ratios reflect each architecture’s token count and expected",
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

_source line 156_

Body = pages 1-8, References start on page 8 (bottom) and continue on page 9+. Appendix starts on page 11.

Let me verify page 8 to confirm Limitations is fully on page 8.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "98b727b3-dccf-4e6b-9ee4-6ca899347bb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2EsEqWMdu3GqrrmUYCLEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 93490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 653
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

_source line 157_

<details open><summary>🔧 Tool call — Bash · `toolu_018WbnPhZwcuRwj6c7s4P2Gs`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = r.stdout.split('\\x0c')\n# Check if 'Limitations' appears on page 8\npage8 = pages[7]\nif 'Limitations' in page8:\n    print('Limitations section IS on page 8')\nelse:\n    print('Limitations section NOT on page 8')\n    for i, p in enumerate(pages):\n        if 'Limitations' in p:\n            print(f'  Found on page {i+1}')\n            break\n# Check if 'References' appears on page 8\nif 'References' in page8:\n    print('References header IS on page 8')\n# Count body pages (content before References)\nfor i, p in enumerate(pages):\n    if 'References' in p:\n        lines = p.split('\\n')\n        for li, line in enumerate(lines):\n            if 'References' in line.strip() and line.strip().endswith('References'):\n                print(f'References on page {i+1}, line {li}')\n                break\n        break\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "328092a6-5c96-4199-9b80-00cde2b06dfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2EsEqWMdu3GqrrmUYCLEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 93490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 653
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

_source line 158 · 2026-05-28T18:35:37.193Z_

<details><summary>↩ Tool result · `toolu_018WbnPhZwcuRwj6c7s4P2Gs`</summary>

```text
Limitations section IS on page 8
References header IS on page 8
References on page 8, line 42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "dd22a6f9-ddb3-49da-a447-02dfc1df3980",
  "tool_use_result": {
    "stdout": "Limitations section IS on page 8\nReferences header IS on page 8\nReferences on page 8, line 42",
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

_source line 159_

Body (including Limitations) = 8 pages. References start at the bottom of page 8 (which is fine per CoRL rules: body pages = 8, references don't count against the limit).

Final verification summary:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "78a082d9-eb16-4bf8-bbb2-1c274536cdf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vvkYGZLa5TNiS3jnsM6yX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 94143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 439
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

_source line 160_

<details open><summary>🔧 Tool call — Bash · `toolu_01HWUcwKtfQQ1CfYcE9h72Mg`</summary>

```json
{
  "command": "grep -c \"Warning.*undefined\\|Warning.*multiply defined\" main.log 2>/dev/null; echo \"---\"; python3 -c \"\nimport subprocess, re\nr = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\nprint(f'Undefined refs: {len(re.findall(chr(63)+chr(63), r.stdout))}')\npages = r.stdout.split(chr(12))\nprint(f'Total PDF pages: {len(pages)-1}')\nprint(f'Body pages: 8 (Limitations + References header on page 8)')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "16b1f23b-7e90-4fc0-b026-0a71e1776c34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vvkYGZLa5TNiS3jnsM6yX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 94143,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 439
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

_source line 161 · 2026-05-28T18:35:50.963Z_

<details><summary>↩ Tool result · reported error · `toolu_01HWUcwKtfQQ1CfYcE9h72Mg`</summary>

```text
Exit code 1
0
---
Traceback (most recent call last):
  File "&lt;string>", line 4, in &lt;module>
    print(f'Undefined refs: {len(re.findall(chr(63)+chr(63), r.stdout))}')
                                 ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 278, in findall
    return _compile(pattern, flags).findall(string)
           ~~~~~~~~^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/__init__.py", line 350, in _compile
    p = _compiler.compile(pattern, flags)
  File "/usr/lib/python3.14/re/_compiler.py", line 762, in compile
    p = _parser.parse(p, flags)
  File "/usr/lib/python3.14/re/_parser.py", line 973, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.14/re/_parser.py", line 460, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       not nested and not items))
                       ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/re/_parser.py", line 687, in _parse
    raise source.error("nothing to repeat",
                       source.tell() - here + len(this))
re.PatternError: nothing to repeat at position 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "3b55bb59-719f-4b7d-b6da-bc56f2963e0f",
  "tool_use_result": "Error: Exit code 1\n0\n---\nTraceback (most recent call last):\n  File \"&lt;string>\", line 4, in &lt;module>\n    print(f'Undefined refs: {len(re.findall(chr(63)+chr(63), r.stdout))}')\n                                 ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/re/__init__.py\", line 278, in findall\n    return _compile(pattern, flags).findall(string)\n           ~~~~~~~~^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/re/__init__.py\", line 350, in _compile\n    p = _compiler.compile(pattern, flags)\n  File \"/usr/lib/python3.14/re/_compiler.py\", line 762, in compile\n    p = _parser.parse(p, flags)\n  File \"/usr/lib/python3.14/re/_parser.py\", line 973, in parse\n    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)\n  File \"/usr/lib/python3.14/re/_parser.py\", line 460, in _parse_sub\n    itemsappend(_parse(source, state, verbose, nested + 1,\n                ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                       not nested and not items))\n                       ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/re/_parser.py\", line 687, in _parse\n    raise source.error(\"nothing to repeat\",\n                       source.tell() - here + len(this))\nre.PatternError: nothing to repeat at position 0"
}
```

</details>

---

### Tool call

_source line 162_

<details open><summary>🔧 Tool call — Bash · `toolu_012mfew7bQvUp4mk6EtUb8SJ`</summary>

```json
{
  "command": "grep -c \"LaTeX Warning.*undefined\" main.log; echo \"---\"; python3 -c \"\nimport subprocess\nr = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = r.stdout\ncount = text.count('??')\nprint(f'Undefined refs: {count}')\npages = text.split('\\x0c')\nprint(f'Total PDF pages: {len(pages)-1}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "ca18224e-2f00-4af8-8824-2a23d3c591a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MENTG1r2P7UPXmAwRSoy3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 94582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 769
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

_source line 163 · 2026-05-28T18:35:56.257Z_

<details><summary>↩ Tool result · `toolu_012mfew7bQvUp4mk6EtUb8SJ`</summary>

```text
0
---
Undefined refs: 0
Total PDF pages: 31
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "b08c054b-45ef-4801-8002-23aef16c0f6d",
  "tool_use_result": {
    "stdout": "0\n---\nUndefined refs: 0\nTotal PDF pages: 31",
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

_source line 164_

All checks pass:
- **Body pages: 8** (Limitations section ends on page 8, References begin at bottom of page 8)
- **Undefined references: 0**
- **"??" occurrences: 0**
- **Total PDF pages: 31**

Changes made:
1. **method.tex**: Compressed models/connectors description (4 paragraphs → 1), scoring functions (3 long paragraphs → 2 compact ones + moved attention alternatives to appendix), retention ratio paragraph (1 long → 3 sentences), CV spectrum equation (split `\begin{split}` → inline math), CV predictor paragraph (2 paragraphs → 1 + moved attention entropy to appendix), VTR section (2 paragraphs → 1)
2. **experiments.tex**: Compressed benchmark/models/protocol descriptions, removed cliff-vs-graded paragraph, shortened inverted-U margin paragraph, shortened figure captions
3. **appendix.tex**: Added "Attention-Based Scoring Methods" (moved from method), "Attention Entropy as Diagnostic" (moved from method), renamed existing subsection to "Attention-Based Scoring Results"
4. **main.tex**: Tightened float spacing (`textfloatsep` 8→6pt, `abovecaptionskip` 4→3pt) and added display math spacing controls

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "uuid": "37d44e36-caa4-4f19-ade5-293a8d327146",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018MMXBp1QHmcejPjEwbNdZV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 195,
      "cache_read_input_tokens": 95351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 195
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

_source line 165_

All checks pass:
- **Body pages: 8** (Limitations section ends on page 8, References begin at bottom of page 8)
- **Undefined references: 0**
- **"??" occurrences: 0**
- **Total PDF pages: 31**

Changes made:
1. **method.tex**: Compressed models/connectors description (4 paragraphs → 1), scoring functions (3 long paragraphs → 2 compact ones + moved attention alternatives to appendix), retention ratio paragraph (1 long → 3 sentences), CV spectrum equation (split `\begin{split}` → inline math), CV predictor paragraph (2 paragraphs → 1 + moved attention entropy to appendix), VTR section (2 paragraphs → 1)
2. **experiments.tex**: Compressed benchmark/models/protocol descriptions, removed cliff-vs-graded paragraph, shortened inverted-U margin paragraph, shortened figure captions
3. **appendix.tex**: Added "Attention-Based Scoring Methods" (moved from method), "Attention Entropy as Diagnostic" (moved from method), renamed existing subsection to "Attention-Based Scoring Results"
4. **main.tex**: Tightened float spacing (`textfloatsep` 8→6pt, `abovecaptionskip` 4→3pt) and added display math spacing controls

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 555580,
  "duration_api_ms": 543671,
  "num_turns": 58,
  "stop_reason": "end_turn",
  "session_id": "bdd638a8-8a12-4f19-a17c-278bbbf1785f",
  "total_cost_usd": 2.863780750000001,
  "usage": {
    "input_tokens": 51,
    "cache_creation_input_tokens": 83701,
    "cache_read_input_tokens": 3582237,
    "output_tokens": 21828,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 83701,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 323,
        "cache_read_input_tokens": 95351,
        "cache_creation_input_tokens": 195,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 195
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3481,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003576,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 51,
      "outputTokens": 21828,
      "cacheReadInputTokens": 3582237,
      "cacheCreationInputTokens": 83701,
      "webSearchRequests": 0,
      "costUSD": 2.860204750000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1b9cdf26-1dc7-4b17-b161-8a829f827989"
}
```

</details>

---
