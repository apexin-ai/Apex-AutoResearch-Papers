# paper expand method section

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_expand_method_section_20260528T174644.log`
- **Structured JSON:** [`6e8c9c8624b443138823.json`](../../sessions/6e/6e8c9c8624b443138823.json)

## Before a recorded user message

43 recorded events

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
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
  "uuid": "d5321833-a9d4-4a24-9074-82af6ec68612",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
  "uuid": "e6df15a2-10a7-4ff6-803f-e2ed9d3ce92f",
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac"
}
```

---

### Assistant

_source line 4_

I'll start by reading all the required context files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "8fb81cdd-1b0d-4eb1-abb6-6f95ed3c912c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFrmrqJJ6Ck3K4e8aaXqH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

<details open><summary>🔧 Tool call — Read · `toolu_01ATv4pv85fsGW8aLhSHppZw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/.claude/skills/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "0b268e73-19ae-4ff1-98bd-1a930483fdda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFrmrqJJ6Ck3K4e8aaXqH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 6 · 2026-05-28T17:46:55.139Z_

<details><summary>↩ Tool result · reported error · `toolu_01ATv4pv85fsGW8aLhSHppZw`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "e4e8bfbc-6412-45ef-8d67-79896b852cf7",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_011iWkYUjVdvqWySaU7EPsue`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "8c9df65d-8f10-4fcd-a6a9-7a9ea5bac190",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFrmrqJJ6Ck3K4e8aaXqH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 8 · 2026-05-28T17:46:55.449Z_

<details><summary>↩ Tool result · `toolu_011iWkYUjVdvqWySaU7EPsue`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
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
47	We apply post-connector token pruning at retention ratio $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, retaining $\lfloor k \cdot N \rfloor$ tokens. Two strategies bracket expected performance: \textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \textbf{random subsampling} selects $\lfloor k \cdot N \rfloor$ tokens uniformly at random. The \emph{importance margin} at ratio $k$ is $\text{SR}_{\text{L2}}(k) - \text{SR}_{\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.
48	
49	\subsection{Compressibility Diagnostic: Importance CV}
50	\label{sec:cv_diagnostic}
51	
52	We quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:
53	\begin{equation}
54	\text{CV} = \frac{\sigma\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}{\mu\!\left(\{\|t_i\|_2\}_{i=1}^{N}\right)}
55	\label{eq:cv}
56	\end{equation}
57	CV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\pi_{0}$ (CV$\,{=}\,$0.038, near-uniform norms) to SmolVLA (CV$\,{=}\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \emph{which} tokens are removed matters more than \emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.
58	
59	\subsection{Vision Token Re-encoder (VTR)}
60	\label{sec:vtr}
61	
62	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding: a cross-attention module (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens. The compression ratio is controlled by $M \in \{16, 32, 64, 96, 128\}$; $M{=}N$ serves as a passthrough control.
63	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "2c1e2788-da43-42d2-93e6-ff68ab77be0c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, retaining $\\lfloor k \\cdot N \\rfloor$ tokens. Two strategies bracket expected performance: \\textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \\textbf{random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. The \\emph{importance margin} at ratio $k$ is $\\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nCV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\\pi_{0}$ (CV$\\,{=}\\,$0.038, near-uniform norms) to SmolVLA (CV$\\,{=}\\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding: a cross-attention module (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n",
      "numLines": 63,
      "startLine": 1,
      "totalLines": 63
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01Rp5P72hF2U5j58ekiqEPcE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "715c8376-4c84-4edc-adca-5ef02f813823",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFrmrqJJ6Ck3K4e8aaXqH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 10 · 2026-05-28T17:46:55.888Z_

<details><summary>↩ Tool result · `toolu_01Rp5P72hF2U5j58ekiqEPcE`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$: offline metrics only, no closed-loop evaluation; the 63\,pp gap vs.\ OpenVLA at $k{=}0.1$ mixes offline loss with closed-loop SR. $^\ddagger$X-VLA uses a linear projection followed by a 12-layer BART encoder; the effective pipeline is not purely linear. $^\S$OFT reports attention entropy and CV only (no pruning evaluation); both metrics match OpenVLA, consistent with the connector being associated with token importance structure. $^\|$CogACT: literature result from EfficientVLA~\cite{yang2025efficientvla}, not our evaluation.}
17	\label{tab:taxonomy}
18	\begin{tabular}{llcrcll}
19	\toprule
20	Model & Connector & Params & Tokens & CV & Representative Result & Class \\
21	\midrule
22	$\pi_0$~\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\mathcal{L}_1{=}0.976$ ($+$2.4\%)$^\dagger$ & Uniformly critical \\
23	$\pi_0.5$~\cite{black2025pi05} & Linear proj ($\times\!\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\%, R$=$69.4\% ($\Delta{=}$+36pp) & Uniformly critical \\
24	X-VLA~\cite{zheng2025xvla} & Linear + BART (12L)$^\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\pm}0.4$, $k{=}0.85$: $67.9{\pm}0.3$ & Threshold-graded \\
25	OpenVLA~\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\% SR ($-$49\%) & Smooth graded \\
26	OFT~\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \approx 0.215$; Ent.\ $0.667 \approx 0.661$$^\S$ & Smooth graded \\
27	CogACT~\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\% SR under 78\% prune$^\|$ & Smooth graded \\
28	SmolVLA~\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\% SR & Catastrophic cliff \\
29	\bottomrule
30	\end{tabular}
31	\end{table*}
32	
33	\subsection{Pixel-Shuffle: Catastrophic Cliff-Edge}
34	\label{sec:smolvla_results}
35	
36	The SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result is 87.3\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Every pruning configuration produces 0\% SR across seven configurations varying scoring (learned ACIS vs.\ random), retention ratio ($k \in \{0.50, 0.70, 0.90, 0.95\}$), and mechanism (zero-masking, true removal, token merging). The cliff persists regardless of checkpoint quality: the official SmolVLA HF checkpoint (57.2\%--59.2\% SR across two evaluation protocols; Appendix~\ref{app:smolvla_ablation}) also collapses to 0\% under random $k{=}0.95$ (5\% removal), L2 norm $k{=}0.9$ (10\% removal), and L2 norm $k{=}0.5$ (Table~\ref{tab:smolvla_ablation}). The failure is architectural, not a training artifact.
37	
38	The pattern generalizes across LIBERO suites: Spatial 0.6\%, Goal 0\%. Pixel-shuffle folds each $4{\times}4$ patch block into a single token by channel concatenation; removing one token eliminates an entire $4{\times}4$ receptive field. The resulting spatial entanglement means even 5\% removal ($k{=}0.95$, losing 6 of 128 tokens) destroys task-critical visual information. Full ablation results appear in Table~\ref{tab:smolvla_ablation}, Appendix~\ref{app:smolvla_ablation}.
39	
40	\subsection{MLP Projector: Smooth Graded Degradation}
41	\label{sec:openvla_results}
42	
43	Under random token removal, OpenVLA degrades gracefully across all retention ratios: 74.0\% (baseline) $\rightarrow$ 69.4\% at $k{=}0.95$ ($-4.6$\,pp) $\rightarrow$ 62.0\% at $k{=}0.90$ $\rightarrow$ 49.0\% at $k{=}0.70$ $\rightarrow$ 37.4\% at $k{=}0.50$ $\rightarrow$ 20.6\% at $k{=}0.30$ (Figure~\ref{fig:degradation_curve}; full results with CIs in Table~\ref{tab:openvla_full}, Appendix).\footnote{A second random seed confirms the graded pattern: 62.2\% at $k{=}0.9$ ($+$0.2\,pp), 44.4\% at $k{=}0.7$ ($-$4.6\,pp), 35.6\% at $k{=}0.5$ ($-$1.8\,pp). All within 5\,pp of the primary seed. Per-seed details in Table~\ref{tab:openvla_multiseed}, Appendix~\ref{app:openvla_multiseed}.} At $k{=}0.30$, two tasks reach 0\% SR, but eight retain non-zero performance: degradation is graded, not cliff-edge. Random token removal provides a conservative lower bound on architectural resilience; learned scoring methods would likely yield better retention.
44	
45	OFT~\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\cite{li2024cogact} (MLP projector) retains 74.2\% SR under 78\% pruning.
46	
47	To control for scoring method in cross-architecture comparisons, we evaluate L2 norm-based selection on OpenVLA. At moderate-to-aggressive retention ($k \leq 0.7$), L2 performs within 2--6\,pp of random removal\footnote{OpenVLA random results use seed$\,{=}\,$7; L2 norm results use seed$\,{=}\,$42. Same-seed (seed42) gaps: 5.4\,pp at $k{=}0.7$, 3.6\,pp at $k{=}0.3$ (21.4\% random vs.\ 25.0\% L2); same-seed at $k{=}0.5$: 35.8\% random vs.\ 39.2\% L2 (gap 3.4\,pp).} (Table~\ref{tab:openvla_l2_vs_random}, Appendix~\ref{app:l2_vs_random}). At $k{=}0.9$, L2 outperforms random by 8.6\,pp (70.6\% vs.\ 62.0\%, reproducible across two random seeds), consistent with the weak but non-zero importance gradient predicted by CV$\,{=}\,$0.215: the signal is exploitable only when few tokens are removed.
48	
49	\subsection{Linear Projection: From Uniformly Critical to Threshold-Graded}
50	\label{sec:linear_results}
51	
52	Three models share a linear projection connector yet exhibit qualitatively different pruning responses. The divergence traces to what happens \emph{after} the projection: nothing ($\pi_0$), a learned scaling ($\pi_0.5$), or a full 12-layer encoder (X-VLA).
53	
54	\paragraph{$\pi_0$ (3.3B, 256 tokens, pure linear).} Offline normalized L1 action loss at $k{=}0.1$ is 0.976, a 2.4\% \emph{improvement} over the unpruned baseline.\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation may reveal additional degradation.} CV$\,{=}\,$0.038 indicates near-uniform token norms. Near-uniform L2 norms (CV$\,{=}\,$0.038) suggest that no token subset carries disproportionate information, so random removal approximates uniform spatial downsampling and the model compensates.
55	
56	\paragraph{$\pi_0.5$ (4B, 768 tokens, linear $\times\!\sqrt{d}$).} The baseline achieves 98.2\% SR. This model reveals that low CV does not imply tokens are dispensable; it implies uniform criticality. The response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\% SR ($-$28.8\,pp), while L2 norm-based removal at the same ratio collapses to 33.4\% ($-$64.8\,pp). The gap of 36\,pp is the largest method-dependent effect at $k{=}0.5$ in our study.
57	
58	At $k \leq 0.7$, random removal degrades monotonically (77.2\%, 69.4\%, 36.4\% at $k{=}0.7, 0.5, 0.3$; seed43 within 1\,pp). At higher retention, a task-specific random cliff emerges on LIBERO-Object: SR drops from 69.4\% ($k{=}0.95$) to 5.0\% ($k{=}0.85$) before recovering to 77.2\% ($k{=}0.7$), a 72\,pp swing; the same $k{=}0.85$ on LIBERO-Spatial retains 58.4\% (Appendix~\ref{app:pi05_crosssuite}). L2 norm selection produces a V-shaped curve: 55.0\% at $k{=}0.7$, 33.4\% at $k{=}0.5$ (the valley), 51.0\% at $k{=}0.3$, confirmed across two seeds ($\sigma = 0.1$\,pp at the valley).\footnote{V-shape valley at $k{=}0.5$: 33.4\% (seed42) vs.\ 33.6\% (seed43), $\sigma{=}0.1$\,pp. V-depth: 17.6\,pp (seed42), 21.8\,pp (seed43). Full multi-seed table in Appendix~\ref{app:pi05_multiseed}.} The non-monotonic L2 pattern arises because norm ranking in a low-CV distribution selects spatially clustered tokens (slight norm variations correlate with image regions), and the resulting loss of spatial coverage peaks at intermediate budgets.
59	
60	This result demonstrates that models showing offline pruning tolerance can exhibit severe closed-loop degradation. Low-CV tokens are uniformly critical, not uniformly dispensable. L2 norm-based selection systematically concentrates on spatially correlated tokens and loses coverage; random selection preserves the uniform spatial distribution that these architectures require.
61	
62	\paragraph{X-VLA (880M, 50 tokens, linear + 12-layer BART).} The 99.2\% baseline is maintained at $k{=}0.95$ ($99.1 \pm 0.2$\%, 3 seeds) and $k{=}0.9$ ($97.8 \pm 0.4$\%) under L2 norm-based removal. A sharp cliff appears at $k{=}0.85$ ($67.9 \pm 0.3$\%, $-$31\,pp, 3 seeds), with non-monotonic recovery at $k{=}0.80$ ($89.0 \pm 0.7$\%, 3 seeds) before degradation resumes: $58.6 \pm 0.4$\% at $k{=}0.7$, $43.4 \pm 0.8$\% at $k{=}0.5$, $22.0 \pm 0.9$\% at $k{=}0.3$, $4.7 \pm 0.6$\% at $k{=}0.2$, and near-zero at $k{=}0.1$. The cliff at $k{=}0.85$ (retaining 42 of 50 BART-encoded tokens) is reproducible across seeds (std $\leq$ 1.6\,pp). The non-monotonic dip is task-specific: four tasks lose $\sim$50\,pp each while six remain unaffected (Table~\ref{tab:xvla_cliff_pertask}, Appendix~\ref{app:xvla_cliff}). Under random removal, X-VLA exhibits a plateau: $65.1 \pm 0.1$\% at $k{=}0.7$ and $64.0 \pm 1.6$\% at $k{=}0.3$ (3 seeds each), confirming that L2 norm-based selection ($22.0 \pm 0.9$\% at $k{=}0.3$) is far more destructive than random for this intermediate-CV architecture.
63	
64	That this threshold appears under importance-based removal (the more favorable test) while OpenVLA degrades smoothly under random removal (the harder test) strengthens the architecture-dependent conclusion. The $\pi_0$--OpenVLA comparison (both consuming 256 SigLIP-based tokens, differing in connector, backbone, and encoder fusion) produces a 63\,pp gap at $k{=}0.1$, consistent with the connector-associated pattern observed across all seven models. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation.
65	
66	\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}
67	\label{sec:smart_compress_results}
68	
69	To test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\% SR ($p > 0.9$ vs.\ the 44.8\% baseline); the gain is architectural, not from additional optimization steps.\footnote{The extended baseline also collapses to 0\% SR under pruning ($k{=}0.50$, random, true removal). Additional training does not mitigate the pixel-shuffle vulnerability.}
70	
71	\begin{table}[t]
72	\centering
73	\small
74	\caption{VTR re-encoding vs.\ deletion on SmolVLA (LIBERO-Object). The M-curve is relatively stable: $M{=}16$ (87.5\% compression) matches $M{=}128$ (no compression) within 1.1\,pp. A parameter-matched MLP adapter achieves comparable SR ($p = 0.15$ vs.\ cross-attention). $^\ddagger$Mean $\pm$ std over 3 seeds (500 episodes each). Other rows: single seed with Wilson 95\% CI.}
75	\label{tab:smart_compress}
76	\begin{tabular}{lccrr}
77	\toprule
78	Method & $M$ & Red. & SR (\%) & Seeds \\
79	\midrule
80	\textit{Baseline} & 128 & 0\% & 44.8 & 1 \\
81	\textit{Ext.\ training} & -- & -- & 45.0 & 1 \\
82	\textit{Hard pruning} & -- & 50--90\% & 0.0 & mult. \\
83	\midrule
84	Cross-attn$^\ddagger$ & 16 & 87.5\% & 56.9$\pm$1.3 & 55.8/58.4/56.5 \\
85	Cross-attn$^\ddagger$ & 32 & 75\% & 60.1$\pm$1.3 & 61.6/59.2/59.6 \\
86	Cross-attn$^\ddagger$ & 64 & 50\% & \textbf{62.0}$\pm$2.3 & 61.6/60.0/64.4 \\
87	Cross-attn$^\ddagger$ & 96 & 25\% & 54.5$\pm$3.2 & 52.6/58.2/52.8 \\
88	Cross-attn$^\ddagger$ & 128 & 0\% & 58.0$\pm$3.5 & 59.8/54.0/60.2 \\
89	MLP adapter$^\ddagger$ & 32 & 75\% & 63.4$\pm$2.6 & 65.2/64.6/60.4 \\
90	\midrule
91	\multicolumn{5}{l}{\textit{Official checkpoint (59.2\% baseline)}} \\
92	Cross-attn & 32 & 75\% & 53.4 & 1 \\
93	\bottomrule
94	\end{tabular}
95	\end{table}
96	
97	The M-curve is relatively stable (Table~\ref{tab:smart_compress}): $M{=}16$ (56.9\%, 87.5\% compression) performs within 1.1\,pp of $M{=}128$ (58.0\%, no compression). A parameter-matched MLP adapter achieves 63.4\% $\pm$ 2.6 at $M{=}32$ ($p = 0.15$ vs.\ cross-attention; Figure~\ref{fig:compression_curve}). Cross-suite evaluation confirms generalization: 53.2\% on LIBERO-Spatial and 56.4\% on LIBERO-Goal where hard pruning yields 0\% (Appendix~\ref{app:smart_compress_full}). VTR applied to OpenVLA yields 0\% SR even in passthrough mode: it is a targeted remedy for pixel-shuffle entanglement.
98	
99	\subsection{CV Correlates with Optimal Pruning Strategy}
100	\label{sec:scaling_law}
101	
102	Token importance CV correlates with both pruning tolerance and optimal strategy. Comparing L2 norm-based and random removal across three models, the gap $\Delta$(R$-$L2) decreases monotonically with CV at both $k{=}0.5$ and $k{=}0.7$ (full data in Table~\ref{tab:scaling_law}, Appendix~\ref{app:cv_scaling_table}). At $k{=}0.5$: $+$36.0\,pp ($\pi_0.5$, CV$\,{=}\,$0.055) $\rightarrow$ $+$26.9\,pp (X-VLA, CV$\,{=}\,$0.151) $\rightarrow$ $-$1.8\,pp (OpenVLA, CV$\,{=}\,$0.215). At $k{=}0.7$: $+$22.2\,pp $\rightarrow$ $+$6.5\,pp $\rightarrow$ $-$5.4\,pp. The monotonic ordering holds across a 2$\times$ change in token budget, indicating CV captures a structural property of the connector. Below CV $\approx 0.15$, L2 ranking captures spatial artifacts rather than importance; above it, importance-based scoring becomes beneficial (reversal at $k{=}0.3$; Appendix~\ref{app:cv_strategy_interaction}).
103	
104	\begin{figure}[t]
105	\centering
106	\begin{subfigure}[b]{0.48\linewidth}
107	\includegraphics[width=\linewidth]{figures/paper/fig_degradation_curve.pdf}
108	\caption{Token pruning across connector classes.}
109	\label{fig:degradation_curve}
110	\end{subfigure}
111	\hfill
112	\begin{subfigure}[b]{0.48\linewidth}
113	\includegraphics[width=\linewidth]{figures/paper/fig_compression_curve.pdf}
114	\caption{VTR M-curve and CV-strategy interaction.}
115	\label{fig:compression_curve}
116	\end{subfigure}
117	\caption{Token reduction on LIBERO-Object. (a)~Pruning: linear ($\pi_0$) uniformly critical, linear+encoder (X-VLA) threshold-graded, MLP (OpenVLA) smooth, pixel-shuffle (SmolVLA) collapses. (b)~VTR: $M{=}16 \approx M{=}128$ where deletion yields 0\%; CV-gap monotonic.}
118	\label{fig:results_combined}
119	\end{figure}
120	
121	\enlargethispage{2\baselineskip}
122	\subsection{Cross-Suite Generalization}
123	\label{sec:cross_suite}
124	
125	The cliff zone exhibits a suite $\times$ method interaction: at $k \in [0.85, 0.95]$, Object tasks collapse under random removal while Spatial tasks degrade gracefully (Figure~\ref{fig:crosssuite}, Table~\ref{tab:pi05_crosssuite}). L2 norm maintains a near-baseline plateau on both suites ($\leq 2.4$\,pp at $k \geq 0.85$). CV$\,{=}\,$0.055 correctly predicts this plateau on both suites despite qualitatively different cliff profiles, confirming CV as a model-level diagnostic. Token importance heatmaps reveal a center-high, edge-low spatial pattern (Figure~\ref{fig:token_heatmap}, Appendix~\ref{app:token_heatmap}), formalized by a hypergeometric model $H(N{=}768,\, C{=}91,\, T{=}6)$: cliff onset at $k{=}0.96$ (10\% collapse probability) narrows to $k{=}0.90$ (90\%), RMSE${=}$0.025 (Appendix~\ref{app:cliff_model}). The model captures onset sharpness at high retention but does not generalize to moderate retention ($k \leq 0.7$), where compensatory mechanisms may emerge (\S\ref{sec:analysis}). The cross-suite difference is driven by Object's concentrated criticality ($C{=}91$) versus Spatial's distributed pattern ($C \approx 5$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "76d810f9-b4f2-4ef7-b169-26336689007b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\\% confidence intervals for single-seed results and mean $\\pm$ standard deviation for multi-seed results.\n\n\\subsection{Taxonomy Overview}\n\\label{sec:taxonomy_overview}\n\nTable~\\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\\sim$0.15, smooth graded at $\\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\\ref{sec:linear_results}).\n\nThe four classes differ qualitatively in their failure mode. Uniformly critical models ($\\pi_0$, $\\pi_0.5$~\\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\\dagger\\pi_0$: offline metrics only, no closed-loop evaluation; the 63\\,pp gap vs.\\ OpenVLA at $k{=}0.1$ mixes offline loss with closed-loop SR. $^\\ddagger$X-VLA uses a linear projection followed by a 12-layer BART encoder; the effective pipeline is not purely linear. $^\\S$OFT reports attention entropy and CV only (no pruning evaluation); both metrics match OpenVLA, consistent with the connector being associated with token importance structure. $^\\|$CogACT: literature result from EfficientVLA~\\cite{yang2025efficientvla}, not our evaluation.}\n\\label{tab:taxonomy}\n\\begin{tabular}{llcrcll}\n\\toprule\nModel & Connector & Params & Tokens & CV & Representative Result & Class \\\\\n\\midrule\n$\\pi_0$~\\cite{black2024pi0} & Linear proj & 3.3B & 256 & 0.038 & $k{=}0.1$: $\\mathcal{L}_1{=}0.976$ ($+$2.4\\%)$^\\dagger$ & Uniformly critical \\\\\n$\\pi_0.5$~\\cite{black2025pi05} & Linear proj ($\\times\\!\\sqrt{d}$) & 4B & 768 & 0.055 & $k{=}0.5$: L2$=$33.4\\%, R$=$69.4\\% ($\\Delta{=}$+36pp) & Uniformly critical \\\\\nX-VLA~\\cite{zheng2025xvla} & Linear + BART (12L)$^\\ddagger$ & 880M & 50 & 0.151 & $k{=}0.9$: $97.8{\\pm}0.4$, $k{=}0.85$: $67.9{\\pm}0.3$ & Threshold-graded \\\\\nOpenVLA~\\cite{kim2024openvla} & 3-layer MLP & 7B & 256 & 0.215 & $k{=}0.5$: 37.4\\% SR ($-$49\\%) & Smooth graded \\\\\nOFT~\\cite{kim2025openoft} & 3-layer MLP & 7B & 256 & 0.219 & CV $0.219 \\approx 0.215$; Ent.\\ $0.667 \\approx 0.661$$^\\S$ & Smooth graded \\\\\nCogACT~\\cite{li2024cogact} & MLP proj & -- & -- & -- & 74.2\\% SR under 78\\% prune$^\\|$ & Smooth graded \\\\\nSmolVLA~\\cite{shukor2025smolvla} & Pixel-shuffle & 450M & 128 & 0.314 & $k{=}0.95$: 0\\% SR & Catastrophic cliff \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle: Catastrophic Cliff-Edge}\n\\label{sec:smolvla_results}\n\nThe SmolVLA baseline (bypass mode, all 128 vision tokens) achieves 44.8\\% SR (224/500, CI [40.5\\%, 49.2\\%]).\\footnote{The official SmolVLA result is 87.3\\% SR with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch due to compute constraints.} Every pruning configuration produces 0\\% SR across seven configurations varying scoring (learned ACIS vs.\\ random), retention ratio ($k \\in \\{0.50, 0.70, 0.90, 0.95\\}$), and mechanism (zero-masking, true removal, token merging). The cliff persists regardless of checkpoint quality: the official SmolVLA HF checkpoint (57.2\\%--59.2\\% SR across two evaluation protocols; Appendix~\\ref{app:smolvla_ablation}) also collapses to 0\\% under random $k{=}0.95$ (5\\% removal), L2 norm $k{=}0.9$ (10\\% removal), and L2 norm $k{=}0.5$ (Table~\\ref{tab:smolvla_ablation}). The failure is architectural, not a training artifact.\n\nThe pattern generalizes across LIBERO suites: Spatial 0.6\\%, Goal 0\\%. Pixel-shuffle folds each $4{\\times}4$ patch block into a single token by channel concatenation; removing one token eliminates an entire $4{\\times}4$ receptive field. The resulting spatial entanglement means even 5\\% removal ($k{=}0.95$, losing 6 of 128 tokens) destroys task-critical visual information. Full ablation results appear in Table~\\ref{tab:smolvla_ablation}, Appendix~\\ref{app:smolvla_ablation}.\n\n\\subsection{MLP Projector: Smooth Graded Degradation}\n\\label{sec:openvla_results}\n\nUnder random token removal, OpenVLA degrades gracefully across all retention ratios: 74.0\\% (baseline) $\\rightarrow$ 69.4\\% at $k{=}0.95$ ($-4.6$\\,pp) $\\rightarrow$ 62.0\\% at $k{=}0.90$ $\\rightarrow$ 49.0\\% at $k{=}0.70$ $\\rightarrow$ 37.4\\% at $k{=}0.50$ $\\rightarrow$ 20.6\\% at $k{=}0.30$ (Figure~\\ref{fig:degradation_curve}; full results with CIs in Table~\\ref{tab:openvla_full}, Appendix).\\footnote{A second random seed confirms the graded pattern: 62.2\\% at $k{=}0.9$ ($+$0.2\\,pp), 44.4\\% at $k{=}0.7$ ($-$4.6\\,pp), 35.6\\% at $k{=}0.5$ ($-$1.8\\,pp). All within 5\\,pp of the primary seed. Per-seed details in Table~\\ref{tab:openvla_multiseed}, Appendix~\\ref{app:openvla_multiseed}.} At $k{=}0.30$, two tasks reach 0\\% SR, but eight retain non-zero performance: degradation is graded, not cliff-edge. Random token removal provides a conservative lower bound on architectural resilience; learned scoring methods would likely yield better retention.\n\nOFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\n\nTo control for scoring method in cross-architecture comparisons, we evaluate L2 norm-based selection on OpenVLA. At moderate-to-aggressive retention ($k \\leq 0.7$), L2 performs within 2--6\\,pp of random removal\\footnote{OpenVLA random results use seed$\\,{=}\\,$7; L2 norm results use seed$\\,{=}\\,$42. Same-seed (seed42) gaps: 5.4\\,pp at $k{=}0.7$, 3.6\\,pp at $k{=}0.3$ (21.4\\% random vs.\\ 25.0\\% L2); same-seed at $k{=}0.5$: 35.8\\% random vs.\\ 39.2\\% L2 (gap 3.4\\,pp).} (Table~\\ref{tab:openvla_l2_vs_random}, Appendix~\\ref{app:l2_vs_random}). At $k{=}0.9$, L2 outperforms random by 8.6\\,pp (70.6\\% vs.\\ 62.0\\%, reproducible across two random seeds), consistent with the weak but non-zero importance gradient predicted by CV$\\,{=}\\,$0.215: the signal is exploitable only when few tokens are removed.\n\n\\subsection{Linear Projection: From Uniformly Critical to Threshold-Graded}\n\\label{sec:linear_results}\n\nThree models share a linear projection connector yet exhibit qualitatively different pruning responses. The divergence traces to what happens \\emph{after} the projection: nothing ($\\pi_0$), a learned scaling ($\\pi_0.5$), or a full 12-layer encoder (X-VLA).\n\n\\paragraph{$\\pi_0$ (3.3B, 256 tokens, pure linear).} Offline normalized L1 action loss at $k{=}0.1$ is 0.976, a 2.4\\% \\emph{improvement} over the unpruned baseline.\\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation may reveal additional degradation.} CV$\\,{=}\\,$0.038 indicates near-uniform token norms. Near-uniform L2 norms (CV$\\,{=}\\,$0.038) suggest that no token subset carries disproportionate information, so random removal approximates uniform spatial downsampling and the model compensates.\n\n\\paragraph{$\\pi_0.5$ (4B, 768 tokens, linear $\\times\\!\\sqrt{d}$).} The baseline achieves 98.2\\% SR. This model reveals that low CV does not imply tokens are dispensable; it implies uniform criticality. The response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\\% SR ($-$28.8\\,pp), while L2 norm-based removal at the same ratio collapses to 33.4\\% ($-$64.8\\,pp). The gap of 36\\,pp is the largest method-dependent effect at $k{=}0.5$ in our study.\n\nAt $k \\leq 0.7$, random removal degrades monotonically (77.2\\%, 69.4\\%, 36.4\\% at $k{=}0.7, 0.5, 0.3$; seed43 within 1\\,pp). At higher retention, a task-specific random cliff emerges on LIBERO-Object: SR drops from 69.4\\% ($k{=}0.95$) to 5.0\\% ($k{=}0.85$) before recovering to 77.2\\% ($k{=}0.7$), a 72\\,pp swing; the same $k{=}0.85$ on LIBERO-Spatial retains 58.4\\% (Appendix~\\ref{app:pi05_crosssuite}). L2 norm selection produces a V-shaped curve: 55.0\\% at $k{=}0.7$, 33.4\\% at $k{=}0.5$ (the valley), 51.0\\% at $k{=}0.3$, confirmed across two seeds ($\\sigma = 0.1$\\,pp at the valley).\\footnote{V-shape valley at $k{=}0.5$: 33.4\\% (seed42) vs.\\ 33.6\\% (seed43), $\\sigma{=}0.1$\\,pp. V-depth: 17.6\\,pp (seed42), 21.8\\,pp (seed43). Full multi-seed table in Appendix~\\ref{app:pi05_multiseed}.} The non-monotonic L2 pattern arises because norm ranking in a low-CV distribution selects spatially clustered tokens (slight norm variations correlate with image regions), and the resulting loss of spatial coverage peaks at intermediate budgets.\n\nThis result demonstrates that models showing offline pruning tolerance can exhibit severe closed-loop degradation. Low-CV tokens are uniformly critical, not uniformly dispensable. L2 norm-based selection systematically concentrates on spatially correlated tokens and loses coverage; random selection preserves the uniform spatial distribution that these architectures require.\n\n\\paragraph{X-VLA (880M, 50 tokens, linear + 12-layer BART).} The 99.2\\% baseline is maintained at $k{=}0.95$ ($99.1 \\pm 0.2$\\%, 3 seeds) and $k{=}0.9$ ($97.8 \\pm 0.4$\\%) under L2 norm-based removal. A sharp cliff appears at $k{=}0.85$ ($67.9 \\pm 0.3$\\%, $-$31\\,pp, 3 seeds), with non-monotonic recovery at $k{=}0.80$ ($89.0 \\pm 0.7$\\%, 3 seeds) before degradation resumes: $58.6 \\pm 0.4$\\% at $k{=}0.7$, $43.4 \\pm 0.8$\\% at $k{=}0.5$, $22.0 \\pm 0.9$\\% at $k{=}0.3$, $4.7 \\pm 0.6$\\% at $k{=}0.2$, and near-zero at $k{=}0.1$. The cliff at $k{=}0.85$ (retaining 42 of 50 BART-encoded tokens) is reproducible across seeds (std $\\leq$ 1.6\\,pp). The non-monotonic dip is task-specific: four tasks lose $\\sim$50\\,pp each while six remain unaffected (Table~\\ref{tab:xvla_cliff_pertask}, Appendix~\\ref{app:xvla_cliff}). Under random removal, X-VLA exhibits a plateau: $65.1 \\pm 0.1$\\% at $k{=}0.7$ and $64.0 \\pm 1.6$\\% at $k{=}0.3$ (3 seeds each), confirming that L2 norm-based selection ($22.0 \\pm 0.9$\\% at $k{=}0.3$) is far more destructive than random for this intermediate-CV architecture.\n\nThat this threshold appears under importance-based removal (the more favorable test) while OpenVLA degrades smoothly under random removal (the harder test) strengthens the architecture-dependent conclusion. The $\\pi_0$--OpenVLA comparison (both consuming 256 SigLIP-based tokens, differing in connector, backbone, and encoder fusion) produces a 63\\,pp gap at $k{=}0.1$, consistent with the connector-associated pattern observed across all seven models. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation.\n\n\\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}\n\\label{sec:smart_compress_results}\n\nTo test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR ($p > 0.9$ vs.\\ the 44.8\\% baseline); the gain is architectural, not from additional optimization steps.\\footnote{The extended baseline also collapses to 0\\% SR under pruning ($k{=}0.50$, random, true removal). Additional training does not mitigate the pixel-shuffle vulnerability.}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding vs.\\ deletion on SmolVLA (LIBERO-Object). The M-curve is relatively stable: $M{=}16$ (87.5\\% compression) matches $M{=}128$ (no compression) within 1.1\\,pp. A parameter-matched MLP adapter achieves comparable SR ($p = 0.15$ vs.\\ cross-attention). $^\\ddagger$Mean $\\pm$ std over 3 seeds (500 episodes each). Other rows: single seed with Wilson 95\\% CI.}\n\\label{tab:smart_compress}\n\\begin{tabular}{lccrr}\n\\toprule\nMethod & $M$ & Red. & SR (\\%) & Seeds \\\\\n\\midrule\n\\textit{Baseline} & 128 & 0\\% & 44.8 & 1 \\\\\n\\textit{Ext.\\ training} & -- & -- & 45.0 & 1 \\\\\n\\textit{Hard pruning} & -- & 50--90\\% & 0.0 & mult. \\\\\n\\midrule\nCross-attn$^\\ddagger$ & 16 & 87.5\\% & 56.9$\\pm$1.3 & 55.8/58.4/56.5 \\\\\nCross-attn$^\\ddagger$ & 32 & 75\\% & 60.1$\\pm$1.3 & 61.6/59.2/59.6 \\\\\nCross-attn$^\\ddagger$ & 64 & 50\\% & \\textbf{62.0}$\\pm$2.3 & 61.6/60.0/64.4 \\\\\nCross-attn$^\\ddagger$ & 96 & 25\\% & 54.5$\\pm$3.2 & 52.6/58.2/52.8 \\\\\nCross-attn$^\\ddagger$ & 128 & 0\\% & 58.0$\\pm$3.5 & 59.8/54.0/60.2 \\\\\nMLP adapter$^\\ddagger$ & 32 & 75\\% & 63.4$\\pm$2.6 & 65.2/64.6/60.4 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Official checkpoint (59.2\\% baseline)}} \\\\\nCross-attn & 32 & 75\\% & 53.4 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe M-curve is relatively stable (Table~\\ref{tab:smart_compress}): $M{=}16$ (56.9\\%, 87.5\\% compression) performs within 1.1\\,pp of $M{=}128$ (58.0\\%, no compression). A parameter-matched MLP adapter achieves 63.4\\% $\\pm$ 2.6 at $M{=}32$ ($p = 0.15$ vs.\\ cross-attention; Figure~\\ref{fig:compression_curve}). Cross-suite evaluation confirms generalization: 53.2\\% on LIBERO-Spatial and 56.4\\% on LIBERO-Goal where hard pruning yields 0\\% (Appendix~\\ref{app:smart_compress_full}). VTR applied to OpenVLA yields 0\\% SR even in passthrough mode: it is a targeted remedy for pixel-shuffle entanglement.\n\n\\subsection{CV Correlates with Optimal Pruning Strategy}\n\\label{sec:scaling_law}\n\nToken importance CV correlates with both pruning tolerance and optimal strategy. Comparing L2 norm-based and random removal across three models, the gap $\\Delta$(R$-$L2) decreases monotonically with CV at both $k{=}0.5$ and $k{=}0.7$ (full data in Table~\\ref{tab:scaling_law}, Appendix~\\ref{app:cv_scaling_table}). At $k{=}0.5$: $+$36.0\\,pp ($\\pi_0.5$, CV$\\,{=}\\,$0.055) $\\rightarrow$ $+$26.9\\,pp (X-VLA, CV$\\,{=}\\,$0.151) $\\rightarrow$ $-$1.8\\,pp (OpenVLA, CV$\\,{=}\\,$0.215). At $k{=}0.7$: $+$22.2\\,pp $\\rightarrow$ $+$6.5\\,pp $\\rightarrow$ $-$5.4\\,pp. The monotonic ordering holds across a 2$\\times$ change in token budget, indicating CV captures a structural property of the connector. Below CV $\\approx 0.15$, L2 ranking captures spatial artifacts rather than importance; above it, importance-based scoring becomes beneficial (reversal at $k{=}0.3$; Appendix~\\ref{app:cv_strategy_interaction}).\n\n\\begin{figure}[t]\n\\centering\n\\begin{subfigure}[b]{0.48\\linewidth}\n\\includegraphics[width=\\linewidth]{figures/paper/fig_degradation_curve.pdf}\n\\caption{Token pruning across connector classes.}\n\\label{fig:degradation_curve}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[b]{0.48\\linewidth}\n\\includegraphics[width=\\linewidth]{figures/paper/fig_compression_curve.pdf}\n\\caption{VTR M-curve and CV-strategy interaction.}\n\\label{fig:compression_curve}\n\\end{subfigure}\n\\caption{Token reduction on LIBERO-Object. (a)~Pruning: linear ($\\pi_0$) uniformly critical, linear+encoder (X-VLA) threshold-graded, MLP (OpenVLA) smooth, pixel-shuffle (SmolVLA) collapses. (b)~VTR: $M{=}16 \\approx M{=}128$ where deletion yields 0\\%; CV-gap monotonic.}\n\\label{fig:results_combined}\n\\end{figure}\n\n\\enlargethispage{2\\baselineskip}\n\\subsection{Cross-Suite Generalization}\n\\label{sec:cross_suite}\n\nThe cliff zone exhibits a suite $\\times$ method interaction: at $k \\in [0.85, 0.95]$, Object tasks collapse under random removal while Spatial tasks degrade gracefully (Figure~\\ref{fig:crosssuite}, Table~\\ref{tab:pi05_crosssuite}). L2 norm maintains a near-baseline plateau on both suites ($\\leq 2.4$\\,pp at $k \\geq 0.85$). CV$\\,{=}\\,$0.055 correctly predicts this plateau on both suites despite qualitatively different cliff profiles, confirming CV as a model-level diagnostic. Token importance heatmaps reveal a center-high, edge-low spatial pattern (Figure~\\ref{fig:token_heatmap}, Appendix~\\ref{app:token_heatmap}), formalized by a hypergeometric model $H(N{=}768,\\, C{=}91,\\, T{=}6)$: cliff onset at $k{=}0.96$ (10\\% collapse probability) narrows to $k{=}0.90$ (90\\%), RMSE${=}$0.025 (Appendix~\\ref{app:cliff_model}). The model captures onset sharpness at high retention but does not generalize to moderate retention ($k \\leq 0.7$), where compensatory mechanisms may emerge (\\S\\ref{sec:analysis}). The cross-suite difference is driven by Object's concentrated criticality ($C{=}91$) versus Spatial's distributed pattern ($C \\approx 5$).",
      "numLines": 125,
      "startLine": 1,
      "totalLines": 125
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012ZEkshMW8QpjScSc3zPtDh`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "f7a2b586-2b65-43d6-8498-80d1a2c65835",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFrmrqJJ6Ck3K4e8aaXqH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13084,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13084
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

_source line 12 · 2026-05-28T17:46:56.301Z_

<details><summary>↩ Tool result · `toolu_012ZEkshMW8QpjScSc3zPtDh`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "e70a9bd8-12f9-41cb-bad8-cf25f2e278a3",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper_framing.md and the paper-writing-norms skill. The skill file didn't exist at the first path, let me try the correct path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "e46305b1-cf6c-4004-a707-54db81e4be4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179vkLWpfSGEnnq8pqkConb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9343,
      "cache_read_input_tokens": 24929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9343
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GQsGzoo6GSmBfzBfB3g6oc`</summary>

```json
{
  "project": "importance_margin_vla_compress",
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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "bd140674-830b-4633-99da-edf00dfecbcb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179vkLWpfSGEnnq8pqkConb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9343,
      "cache_read_input_tokens": 24929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9343
      },
      "output_tokens": 23,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01TJqPgWVcLSAoZzQEMhZJ72`</summary>

```json
{
  "pattern": "**/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "8011e8cb-d68b-4db6-8e3c-475e9c44eaf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179vkLWpfSGEnnq8pqkConb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9343,
      "cache_read_input_tokens": 24929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9343
      },
      "output_tokens": 23,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T17:47:01.925Z_

<details><summary>↩ Tool result · `toolu_01GQsGzoo6GSmBfzBfB3g6oc`</summary>

```text
&lt;persisted-output>
Output too large (52.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5c041521-e8e2-414d-abe9-e8e6614720ac/tool-results/toolu_01GQsGzoo6GSmBfzBfB3g6oc.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\", \"content\": \"# Paper Framing — importance_margin_vla_compress\\n\\n## Target Venue\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\n\\n## Title (working)\\n\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\"\\n\\n## Core Insight\\n\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\"threshold-graded\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\n\\n**Axis 1 — Token Coupling (connector architecture):**\\n| Type | Connectors | CV Range | Mechanism |\\n|------|-----------|----------|-----------|\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\n\\n**Axis 2 — Task Complexity:**\\n| Level | Suites | Characteristics |\\n|-------|--------|----------------|\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\\n\\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\\n- X-VLA Long k=0.95: ~53% (-45pp from baseline)
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "05b6692b-ba55-4883-a075-03d4633524d5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — importance_margin_vla_compress\\\\n\\\\n## Target Venue\\\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\\\n\\\\n## Title (working)\\\\n\\\\\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\\\\\"threshold-graded\\\\\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\\\n\\\\n**Axis 1 — Token Coupling (connector architecture):**\\\\n| Type | Connectors | CV Range | Mechanism |\\\\n|------|-----------|----------|-----------|\\\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\\\n\\\\n**Axis 2 — Task Complexity:**\\\\n| Level | Suites | Characteristics |\\\\n|-------|--------|----------------|\\\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\\\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\\\\n\\\\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\\\\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\\\\n- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance\\\\n- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen\\\\n- Token-independent (π0.5 Goal/Long): data collecting, expected smaller amplification\\\\n\\\\n**CV remains the primary Axis-1 diagnostic** — predicts both pruning tolerance and optimal strategy (Claim 5). Task complexity (Axis 2) explains within-model variance across suites that the old taxonomy could not capture.\\\\n\\\\n_Original per-connector evidence (from Object-suite 4-class taxonomy) retained below; reinterpret through 2-axis lens:_\\\\n- **Linear projection** (π0 3.3B, π0.5 4B): **\\\\\\\"Uniformly Critical\\\\\\\" (D139)**. NOT immune. π0.5 baseline=98.2%, random k=0.5=**69.4%** (-28.8pp), L2norm k=0.5=**33.4%** (-64.8pp). Gap=+36.0pp, random wins 9/10 tasks. Low CV (0.038/0.055) = uniformly important tokens → L2norm's systematic bias selects spatially clustered tokens → catastrophic at k≤0.7. Random preserves spatial coverage → 2× better at k=0.5. **L2norm extended curve:** k=0.1=2.6% (collapse) → k=0.3=51.0% → k=0.5=33.4% (valley) → k=0.7=55.0% → k=0.9=98.2%. V-shape with collapse at extreme compression. CV=0.055 makes this the extreme case of the monotonic diagnostic trend. **⚠️ MAJOR FINDING (2026-05-22, fully investigated):** π0.5 random pruning exhibits sharp cliff at k=0.85-0.925 with non-monotonic recovery:\\\\n  - k=0.95: 71.1% FINAL (seed42 500ep; seed43=72.8%) — already 27pp below baseline\\\\n  - k=0.925: **27.6%** FINAL (seed42) — cliff entry point, 43pp drop from k=0.95\\\\n  - k=0.9: 10.8%±1.2pp (dual seed: seed42=12.0%, seed43=9.6%) — **87.4pp gap vs L2norm k=0.9=98.2%**\\\\n  - k=0.85: **5.0%** FINAL (seed42 v2=4.4%) — cliff floor\\\\n  - k=0.7: 75.5% (mean), k=0.5: 68.9%, k=0.3: 36.4% — recovery zone\\\\n  - Cliff profile: 71.1%(k=0.95) → 27.6%(k=0.925) → 10.8%(k=0.9) → 5.0%(k=0.85) — 66pp collapse over 10% keep ratio change\\\\n  **D151 (2026-05-22): Cliff is RANDOM-SPECIFIC.** L2norm maintains 98.0-99.2% plateau across the entire cliff zone:\\\\n  - L2norm k=0.95=98.2%, k=0.925=99.2%, k=0.9=98.2%, k=0.85=98.0% — zero degradation\\\\n  - Random k=0.925: 27.6% vs L2norm=99.2% → **71.6pp gap** (maximum separation)\\\\n  - Random k=0.85: 5.0% vs L2norm=98.0% → **93.0pp gap**\\\\n  - L2norm succeeds because deterministic selection consistently retains the same token subset; random sampling creates variable damage\\\\n  **D152 (2026-05-22): Cliff is TASK-SPECIFIC.** Object tasks collapse catastrophically, Spatial tasks degrade but survive:\\\\n  - Random k=0.9: Object=10.8% vs Spatial=54.6% — Spatial retains 5× more SR\\\\n  - Random k=0.85: Object=5.0% vs Spatial=TBD (collecting)\\\\n  - Within Object suite: all 10 tasks collapse at k=0.9 (2-16%). Within Spatial suite: degradation but not catastrophic.\\\\n  - Mechanism: Object tasks require precise object identity discrimination (visually similar objects); Spatial tasks rely on spatial layout (more distributed visual information). Random token loss destroys fine-grained discriminative features needed for Object before destroying spatial layout features.\\\\n  **Fixed-mask experiment (D149) NEGATES temporal inconsistency hypothesis:** per-episode fixed mask T0=12% = per-call random T0=12%. Temporal mask variation is NOT the cause.\\\\n  **D153: Cross-suite LIBERO-Spatial — weaker non-monotonicity, no catastrophic dip (2026-05-22)**\\\\n  Baseline: 97.2%. Random pruning profile:\\\\n  | k | Object | Spatial | Δ | Pattern |\\\\n  |---|--------|---------|---|---------|\\\\n  | 0.95 | 71.1% | deploying | — | — |\\\\n  | 0.925 | 28.8% (2-seed) | — | — | — |\\\\n  | 0.9 | 10.8% | 54.6% | +43.8pp | Spatial 5× more robust |\\\\n  | 0.85 | 5.0% | **58.4%** | **+53pp** | Maximum divergence |\\\\n  | 0.7 | 75.5% | 74.4% | -1pp | Suite-independent |\\\\n  | 0.5 | 69.4% | 71.6% | +2pp | Suite-independent |\\\\n  | 0.3 | 36.4% | 49.6% | +13pp | Spatial more robust |\\\\n  L2norm Spatial: k=0.9=95.0%, k=0.7=67.0%, k=0.5=55.6%, k=0.3=57.2%. L2norm k=0.95/k=0.85 deploying.\\\\n  **Object has deep V-shape dip**: 5%(k=0.85) → 10.8%(k=0.9) → 75.5%(k=0.7), 70pp recovery from cliff floor. **Spatial has weaker non-monotonicity**: k=0.5(71.6%) > k=0.85(58.4%) > k=0.9(54.6%), but no catastrophic collapse — floor stays above 50% vs Object's 5% floor. The cliff zone gap (Object 5% vs Spatial 58%) reflects concentrated vs distributed critical token patterns.\\\\n  **Mechanism**: Object tasks have **concentrated** critical tokens (object identity discrimination — visually similar objects). Random removal at cliff zone destroys these concentrated patches → catastrophic. Spatial tasks have **distributed** critical information (layout patches spread across image). Random removal damages any random subset but never completely destroys spatial signal → graceful degradation.\\\\n  **Paper value**: Two distinct cliff behavior modes — **concentrated-critical (Object)** vs **distributed-critical (Spatial)** — as a function of task semantics. Pruning sensitivity = f(connector, method, k, task_semantics). Suite-independent at moderate k (0.5-0.7), suite-dependent at cliff zone (0.85-0.95).\\\\n  **Paper value:** strengthens \\\\\\\"uniformly critical\\\\\\\" class — even uniform importance distribution doesn't make pruning safe. Simple deletion fails; learned compression (VTR) needed.\\\\n- **Linear projection + deep post-processing** (X-VLA 880M, linear proj + 12-layer BART encoder): robust k≥0.9 (97.6% SR), **cliff at k=0.7 (56.2% SR, -43pp)**. BART encoder introduces non-linear mixing that creates partial token dependencies. CV=0.151. **D127: random pruning k=0.9=97.8% ≈ L2norm 97.6% — pruning method independence confirmed for low-CV connectors.**\\\\n- **Multi-layer MLP** (OpenVLA 7B, OpenVLA-OFT 7B): graded degradation. k=0.1 normalized loss = 1.608 (+61%). Non-linear mixing creates partial dependencies. OFT entropy (0.667) ≈ Standard (0.661), CV(OFT)=0.219 ≈ CV(OpenVLA)=0.215, confirming connector — not action head — determines attention structure. **D136: OFT LIBERO eval infeasible (Blackwell GPU SDPA incompatibility, requires A100+torch2.2). OFT included via CV/entropy analysis only; cite official baseline ~97% SR.** π0.5 baseline confirmed 98.2% (D135).\\\\n- **Pixel-shuffle** (SmolVLA 450M): catastrophic cliff-edge. k=0.95 (removing 5%) → 0% SR. Spatial folding creates irreversible entanglement. **D147: Official HF checkpoint (HuggingFaceVLA/smolvla_libero) confirms identical cliff — random k=0.95 = 0%, L2norm k=0.95 = 0%. Cliff is architectural, not training artifact. Resolves W-C2.** **Dual-seed confirmed (2026-05-22):** Baseline 59.4%±0.3pp (seed42=59.2%, seed43=59.6%), random k=0.95: 0.1% mean (0.0%/0.2%), random k=0.5: 0.0%, L2norm k=0.95: 0.2% mean (0.4%/0.0%). All pruning ≤0.2% across both seeds. cqa1 supplementary: L2norm k=0.7=0%, random k=0.9=0%.\\\\n\\\\nKey controlled comparison: π0 (256 tokens, linear) vs OpenVLA (256 tokens, 3-layer MLP) — same token count, same encoder lineage, only connector differs. k=0.1: π0 improves 2.4% vs OpenVLA degrades 61%. This isolates connector as the causal factor.\\\\n\\\\nLearned re-encoding (VTR) overcomes the cliff-edge: cross-attention 60.1±1.3% and MLP adapter 63.4±2.6% at M=32 (vs 0% hard pruning), with M=128 passthrough (58.0%±3.5, 3-seed) ≈ baseline 59.2% — VTR recovers to baseline rather than exceeding it. SmolVLA M-curve confirmed flat (D105): M=16 (56.9%±1.3) = M=128 (58.0%±3.5), all 5 M-values within ±3pp of baseline 59.2%. VTR achieves near-lossless compression at any ratio (0-87.5%) for pixel-shuffle connectors.\\\\n\\\\n## Paper Identity (Round 5 Upgrade — D171 2-Axis, 2026-05-22)\\\\n**ANALYSIS + METHOD paper.** (D091 → D097 → D171: 5 models × 3 connector families × 4 LIBERO suites)\\\\n\\\\n**Analysis contribution (primary)**: First systematic study revealing that VLA token pruning robustness is determined by the interaction of two axes: (1) connector architecture (token-independent vs token-entangling, diagnosed by importance CV 0.038→0.314) and (2) task complexity (simple vs multi-step). Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio. 5 models × 4 suites × 4 model sizes (450M-7B) eliminate confounds. No competing work does cross-architecture, cross-task VLA token analysis.\\\\n\\\\n**Method contribution**: Diagnose-then-Compress framework:\\\\n- Step 1: **Connector Compressibility Diagnostic** (D104: resolved)\\\\n  - **Primary metric: Importance CV** (token importance heterogeneity) — zero-cost, one forward pass\\\\n  - CV forms continuous spectrum predicting pruning tolerance: π0=0.038 < π0.5=0.055 < X-VLA=0.151 < OpenVLA=0.215 < OFT=0.219 < SmolVLA=0.314\\\\n  - ⚠️ D106+: X-VLA CV=0.151 correctly predicted its intermediate pruning behavior (k=0.7 ≈50% SR ≈ OpenVLA k=0.7). CV is a valid continuous predictor, NOT a 3-class discrete classifier.\\\\n  - **Key discovery**: X-VLA \\\\\\\"linear projection\\\\\\\" passes through BART encoder (12 transformer layers) before decoder → introduces non-linear mixing → explains CV=0.151 (much higher than π0=0.038 pure linear)\\\\n  - **Entropy as mechanistic supplement** (CV is primary; entropy is supplementary):\\\\n    - π0: entropy=0.959 (per-layer mean, range 0.931–0.983), CV=0.038 — uniform & independent → most tolerant\\\\n    - **π0.5: entropy=0.666, CV=0.055** — similar entropy to OpenVLA (0.661) but vastly different pruning behavior (CV correctly differentiates)\\\\n    - X-VLA: entropy=0.614, CV=0.151 — selective & BART-mixed → intermediate\\\\n    - OpenVLA: entropy=0.661, CV=0.215 — selective & MLP-mixed → graded\\\\n    - SmolVLA: entropy=0.952, CV=0.314 — near-uniform but spatially entangled → catastrophic\\\\n  - **KEY INSIGHT**: Entropy clusters π0.5/X-VLA/OpenVLA together (0.61-0.67) despite very different pruning behaviors. CV correctly separates them (0.055 vs 0.151 vs 0.215). Entropy fails as diagnostic because it doesn't capture token independence structure — only attention distribution shape.\\\\n  - ✅ Batch 2 complete: continuous CV spectrum confirmed (X-VLA full 8-point curve validates threshold-graded class)\\\\n  - Supplementary: lightweight pruning probe (remove 5%, one forward pass) as practitioner-friendly alternative\\\\n- Step 2: VTR (Vision Token Re-encoding) — lightweight cross-attention module (~22M params) for universal compression\\\\n- For entangled tokens (pixel-shuffle): recovers from 0% (hard pruning) to ~59% ≈ baseline, M-curve flat D105 (near-lossless compression at any ratio 0-87.5%)\\\\n- For independent tokens (MLP projector): **D109 C4-ext confirmed 0% SR** at 20K steps (M=128, severe overfitting — model outputs identical action every step). VTR on MLP projector does NOT improve SR; reframed as \\\\\\\"VTR ceiling depends on connector type\\\\\\\" finding. User directive: performance degradation acceptable if efficiency improves — VTR value is 75% KV-cache reduction + attention speedup. VTC-only M=32/M=64 training in progress to test whether smaller M values fare better.\\\\n\\\\n**Differentiation from concurrent work**: 4 concurrent works (Compressor-VLA, SpecPrune-VLA, LightVLA ICRA'26, See What Matters ICML'26) all propose pruning on MLP-projector VLAs. We (1) explain why pruning fails on pixel-shuffle architectures, (2) identify why pruning succeeds on linear projection (tokens are truly independent), and (3) propose a re-encoding method motivated by the diagnostic analysis.\\\\n\\\\n**Model coverage**: 5 VLA models × 3 connector families × 4 LIBERO suites × 4 model sizes (450M-7B). RC1 (only 2 models), RC2 (size confound), and RC7 (only one suite) fully addressed.\\\\n\\\\n## Core Claims (5 claims, expanded from 4)\\\\n\\\\n### Claim 1: 2-Axis Compressibility Framework (D107 → D171 UPGRADED)\\\\nPruning sensitivity = f(connector_architecture, task_complexity). Two axes interact:\\\\n\\\\n**Axis 1 — Token Coupling (connector determines base sensitivity):**\\\\n- **Token-independent** connectors (pure linear π0/π0.5, MLP OpenVLA/OFT): tokens retain spatial meaning → pruning damage is local, graded degradation\\\\n- **Token-entangling** connectors (BART X-VLA, pixel-shuffle SmolVLA): cross-token dependencies → pruning damage cascades\\\\n\\\\n**Axis 2 — Task Complexity (task amplifies entangling-connector sensitivity):**\\\\n- Simple tasks (Object): even entangling connectors tolerate mild pruning (X-VLA k=0.9=97.6%)\\\\n- Complex tasks (Goal/Long): entangling connectors collapse (X-VLA Goal k=0.9=70.2%, Long k=0.95≈53%)\\\\n- Key: same connector, same k, same method — **only task differs** → 27.8pp drop (Object→Goal)\\\\n\\\\n**CV predicts Axis-1 position**: 0.038 (most independent) → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 (most entangled)\\\\n\\\\n**Evidence**: 5 models, 3 connector families, 4 LIBERO suites, 4 model sizes (450M-7B). Key controlled comparisons:\\\\n1. π0 (256 tokens, linear) k=0.1 = 0.976 vs OpenVLA (256 tokens, MLP) k=0.1 = 1.608 → connector isolates base sensitivity\\\\n2. X-VLA Object k=0.9 = 97.6% vs X-VLA Goal k=0.9 = 70.2% → task complexity isolates amplification\\\\n3. SmolVLA Object = 0% at k=0.95 → extreme entanglement dominates even on simple tasks\\\\n\\\\n🔴 **D108→D127→D130→D132: Pruning method comparison — MAJOR REVERSAL at aggressive compression**\\\\n\\\\nBoth L2 norm and random pruning tested on X-VLA and OpenVLA. **CV predicts not just tolerance but optimal strategy**:\\\\n\\\\n- **OpenVLA (MLP, CV=0.215)**: L2 norm consistently ≥ random at all k values. High CV → meaningful importance differentiation → L2 norm selection effective.\\\\n  - k=0.95: L2norm=69.4% ≈ random=69.2% (+0.2pp)\\\\n  - k=0.7: L2norm=49.8%¹ > random=44.4% (+5.4pp). ¹seed43 only, seed42 running on westd-38929:2\\\\n  - k=0.5: L2norm=39.2% > random=35.8% (+3.4pp)\\\\n  - k=0.3: L2norm=25.0%, random=pending (re-running)\\\\n\\\\n- **X-VLA (BART, CV=0.151)**: 🔴 **REVERSAL** — L2 norm ≈ random at mild compression, but **random MASSIVELY outperforms L2 norm at aggressive compression**:\\\\n  - k=0.9: L2norm=97.6% ≈ random=97.8% (≈0pp)\\\\n  - k=0.85: L2norm=68.0% > random=63.6% (+4.4pp, cliff boundary)\\\\n  - k=0.8: L2norm=89.0% ≈ random=89.4% (≈0pp, non-monotonic recovery)\\\\n  - **k=0.5: L2norm=42.6% << random=70.6% (-28.0pp!)** — CI non-overlapping, statistically significant. Random wins 9/10 tasks; T4 ketchup: L2norm=42% vs random=100% (+58pp). Only T6 butter both crash at 2%.\\\\n  - k=0.7: L2norm=56.2% << random=65.2% (+9pp). Crossover confirmed at k≈0.8.\\\\n  - **k=0.3: L2norm=22.8% << random=62.8% (+40pp!)** — gap scales monotonically with compression.\\\\n  - **D137**: seed43 k=0.5=71.0% confirms seed42=70.6% (Δ=0.4pp). Gap reproducible.\\\\n\\\\n- **SmolVLA**: all methods = 0% at all k values → trivially method independent.\\\\n\\\\n**KEY INSIGHT (D132→D137)**: Importance-based pruning can be **actively harmful** on low-CV architectures under aggressive compression, and the harm SCALES: +9pp@k=0.7, +28pp@k=0.5, +40pp@k=0.3. Mechanism: X-VLA's linear projection + BART encoder produces relatively uniform token norms (CV=0.151). L2 norm selection on a near-uniform distribution degenerates into selecting spatially clustered tokens → loses diversity → catastrophic failure. Random pruning preserves spatial coverage → dramatically better. Multi-seed confirmed.\\\\n\\\\n**This strengthens the paper**: CV serves as a dual predictor — predicts both (1) pruning tolerance ceiling and (2) whether importance-based methods help or hurt. Connector architecture determines both via its effect on token importance distribution.\\\\n\\\\n**Paper narrative upgrade**: From \\\\\\\"connector determines compressibility\\\\\\\" to \\\\\\\"connector determines both compressibility AND optimal compression strategy.\\\\\\\" This is a significantly stronger and more novel contribution.\\\\n\\\\n**Pending data**: X-VLA random k=0.7 (crossover characterization), multi-seed k=0.5 random (robustness). OpenVLA L2norm k_ratio=null provenance issue needs fixing.\\\\n\\\\n### Claim 2: Pixel Shuffle Creates Irreversible Token Entanglement\\\\nSmolVLA's pixel_shuffle connector spatially folds 1024 SigLIP patches into 64 tokens per camera (16x compression). Each resulting token encodes a 32x32 pixel region via channel-to-spatial reorganization. This creates extreme cross-token spatial entanglement: removing any single token eliminates an entire spatial quadrant's information with no redundancy to compensate.\\\\n\\\\n**Evidence**:\\\\n- k=0.95 (remove only 7/128 tokens = 5.5%) = 0% SR — even minimal removal is catastrophic\\\\n- k=0.9 (remove 13/128 tokens) = 0% SR\\\\n- Geometric prior (Sobel edge) k=0.5/0.7/0.9 = all 0%\\\\n- Attention entropy ratio 0.952 (near-uniform, TV=0.05)\\\\n- Official checkpoint Object (59.2% baseline) cliff-edge at k=0.5 → 0%\\\\n- Official checkpoint Spatial (43.8% baseline) cliff-edge at k=0.5 → 0.6% (3/500, CI [0.2%, 1.7%])\\\\n\\\\n### Claim 3a: Linear Projection → Depends on Effective Pipeline (D107: RESOLVED)\\\\nPure linear projection (π0): immune. Linear projection + deep post-processing (X-VLA, BART 12L): \\\\\\\"robust-then-cliff\\\\\\\" — immune at k≥0.9, cliff at k=0.7, then graded degradation. The BART encoder introduces non-linear cross-token mixing that explains intermediate CV=0.151 and the cliff pattern.\\\\n\\\\n**Evidence** (X-VLA LIBERO SR — Batch 1 + Batch 2 COMPLETE, full 8-point curve):\\\\n- k=1.0: **99.2%** (baseline, 496/500) — per-task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]\\\\n- k=0.95: **99.0%** (-0.2pp) — per-task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]\\\\n- k=0.9: **97.6%** (-1.6pp) — per-task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]\\\\n- k=0.7: **56.2%** (-43pp, CLIFF — 281/500) — per-task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]\\\\n- k=0.5: **42.6%** (-57pp) — Batch 2 confirmed (MSH fix applied)\\\\n- k=0.3: **23.0%** (-77pp) — graded degradation continues below cliff\\\\n- k=0.2: **~4.0%** (-96pp) — near-zero\\\\n- k=0.1: **~0.0%** (-100pp) — complete failure\\\\n✅ Full curve confirms threshold-graded pattern: immune k≥0.9, cliff at k=0.7, then graded degradation k≤0.5 (42.6%→23.0%→~4%→~0%).\\\\n\\\\n**Cliff localization (D114, D117: 3-seed deterministic, L2norm)**:\\\\n- k=0.80: **89.0% ± 0.72pp** (seeds: 88.8/88.4/89.8)\\\\n- k=0.85: **67.9% ± 0.31pp** (seeds: 68.0/67.6/68.2 — T4=26%, T6=0% across ALL 3 seeds)\\\\n- Non-monotonic: k=0.85 < k=0.80 by **21.1pp**. BART encoder creates length-dependent interactions near critical token density. SD < 1pp confirms fully deterministic, not stochastic.\\\\n\\\\n**Random pruning comparison (D127-D130, D132 REVERSAL)**:\\\\n- k=0.9: random=97.8% ≈ L2norm=97.6% → method independent at mild compression\\\\n- k=0.85: random=63.6% vs L2norm=68.0% (+4.4pp for L2norm at cliff boundary). Both crash on same tasks (T1, T4, T6, T8) → cliff is architectural.\\\\n- k=0.8: random=89.4% ≈ L2norm=89.0% → method independent, non-monotonic recovery confirmed in both\\\\n- 🔴 **k=0.5: random=70.6% >> L2norm=42.6% (+28pp REVERSAL, CI non-overlapping)**. Per-task random: [96, 46, 100, 92, 100, 94, 2, 82, 42, 100]. Random wins 9/10 tasks; L2norm actively harmful. T4: random=100% vs L2norm=42% (+58pp).\\\\n- k=0.7: random=65.2% vs L2norm=56.2% (+9pp random). Crossover confirmed at k≈0.8.\\\\n- 🔴 **k=0.3: random=62.8% vs L2norm=22.8% (+40pp!)** — gap SCALES with compression: +9@k=0.7, +28@k=0.5, +40@k=0.3.\\\\n- **D137 multi-seed confirmed**: seed43 k=0.5=71.0% (seed42=70.6%, Δ=0.4pp). Gap is reproducible.\\\\n- **Random non-monotonicity confirmed**: k=0.5 (70.6%) > k=0.7 (65.2%) > k=0.3 (62.8%). seed43 reproduces (71.0%). L2norm monotonically decreasing (42.6% > 22.8%). Random's k=0.5 \\\\\\\"sweet spot\\\\\\\" may reflect optimal diversity-coverage tradeoff: enough tokens removed to break BART clustering, but enough retained for spatial coverage.\\\\n- k=0.85 per-task (random): [100, 10, 100, 94, 24, 92, 0, 94, 22, 100] = 63.6%.\\\\n- **Non-monotonicity confirmed in both methods**: k=0.85 (42 tokens) cliff vs k=0.8 (40 tokens) recovery. 2-token difference, 21-26pp gap.\\\\n- **D132 KEY INSIGHT**: At aggressive compression (k=0.5), L2 norm is catastrophically worse than random for X-VLA. Low CV=0.151 → near-uniform importance → L2 norm degenerates into spatially clustered selection → loses diversity. This is the opposite of OpenVLA (CV=0.215) where L2 norm helps. **CV predicts optimal pruning strategy, not just tolerance.**\\\\n\\\\n**Cross-suite generalization (D117, updated with full results)**:\\\\n- X-VLA Spatial baseline: **91.6%** [88.8%, 93.7%] (500 eps, T5=48% is hardest task)\\\\n- X-VLA Goal baseline: **98.0%** [96.4%, 98.9%] (500 eps, all tasks ≥92%)\\\\n- X-VLA-Libero checkpoint covers all 4 suites without suite-specific fine-tuning.\\\\n\\\\n**⚠️ Cross-suite pruning sensitivity (key finding — potential new contribution)**:\\\\n\\\\nX-VLA pruning curve comparison across suites:\\\\n\\\\n| Suite | k=1.0 | k=0.9 | k=0.85 (L2/Rand) | k=0.8 (L2/Rand) | k=0.7 (L2/Rand) | k=0.5 (L2/Rand) |\\\\n|-------|-------|-------|-----|-------|----------|----------|\\\\n| Object | 99.2% | 97.8% | 68.0/63.6% | 89.0/89.4% | 56.2/65.2% | 42.6/**70.6%** |\\\\n| Spatial | 91.6% | 79.0% | 66.6/67.6% | — | — | 58.8%/**71.4%** |\\\\n| Goal | 98.0% | 70.2% | — | — | — | 61.0%/— |\\\\n\\\\n**Goal suite FINAL results (10/10 tasks, D123: suite-level monotonic confirmed)**:\\\\n- k=0.9: **70.2%** (351/500) — much larger drop than Object (-1.4pp) despite similar baseline\\\\n- k=0.5: **61.0%** (305/500) — suite-level monotonic (k=0.9 > k=0.5), D123 retracted earlier partial-data non-monotonic claim\\\\n\\\\n**Per-task non-monotonic pruning remains valid (selected tasks)**:\\\\n\\\\n| Task | k=1.0 | k=0.9 | k=0.5 | Pattern |\\\\n|------|-------|-------|-------|---------|\\\\n| T0 open drawer | 100% | 100% | 82% | monotonic ↓ |\\\\n| T2 close drawer | 94% | 96% | **100%** | **pruning improves** |\\\\n| T3 open+put (multi-step) | 100% | **6%** | **40%** | catastrophic + non-monotonic (k=0.5 > k=0.9) |\\\\n| T8 | — | — | — | +46pp non-monotonic (k=0.5 > k=0.9) |\\\\n| T9 | 98% | — | ~0% | catastrophic collapse (-98pp) |\\\\n\\\\n- Suite-level: Goal k=0.5=61.0% > Spatial k=0.5=58.8% — Goal slightly more robust, but both moderate degradation\\\\n- Per-task: T3/T8 show non-monotonicity (k=0.5 > k=0.9), T9 catastrophic collapse. These are genuine misalignments between global L2-norm ranking and task-specific token utility.\\\\n- T2 pruning improvement: consistent with π0 finding — simple tasks benefit from token noise removal\\\\n\\\\n**Key cross-suite finding**: Goal k=0.9 drops **27.8pp** (vs Object -1.4pp). Same connector, same pruning method, different task distribution → **task complexity amplifies pruning sensitivity**. Goal tasks involve multi-step reasoning that depends heavily on precise spatial tokens.\\\\n\\\\n**Task-level analysis (Spatial, k=0.5 vs baseline)**:\\\\n- Robust (Δ≤10pp): T0 \\\\\\\"between plate and ramekin\\\\\\\" (-4pp), T4 \\\\\\\"in top drawer\\\\\\\" (-2pp) — global spatial / unambiguous target\\\\n- Moderate (Δ 10-30pp): T2(-10), T3(-24), T6(-22), T8(-18) — mild spatial precision needed\\\\n- Catastrophic (Δ>40pp): T5 \\\\\\\"on ramekin\\\\\\\" (-48pp, 0%), T9 \\\\\\\"on cabinet\\\\\\\" (-58pp), T7 \\\\\\\"on stove\\\\\\\" (-64pp), T1 \\\\\\\"next to ramekin\\\\\\\" (-78pp)\\\\n- **T1 has 100% baseline but 22% at k=0.5** — high baseline ≠ pruning robustness\\\\n\\\\n**Mechanism**: Goal tasks are semantically diverse (different verbs/objects) → language instruction alone disambiguates → vision tokens are redundant for task selection. Spatial tasks are semantically near-identical (all \\\\\\\"pick bowl...\\\\\\\") → disambiguation relies entirely on spatial vision tokens → pruning destroys the only discriminative signal.\\\\n\\\\n**Paper framing upgrade (Reviewer suggestion, agreed)**:\\\\n- From \\\\\\\"connector determines pruning tolerance\\\\\\\" → \\\\\\\"pruning sensitivity = f(connector_type, task_semantics)\\\\\\\"\\\\n- Connector CV predicts degradation *class* (immune/threshold/graded/catastrophic)\\\\n- Task semantic structure determines degradation *severity* within that class\\\\n- When language disambiguates: aggressive pruning is safe (Goal k=0.5 ≈ baseline)\\\\n- When spatial vision disambiguates: even conservative pruning degrades (Spatial k=0.9 -12.6pp)\\\\n- **Potential new contribution**: first task-level pruning sensitivity analysis in VLAs. §4.6 should include per-task heatmap + the language-vs-spatial disambiguation framework.\\\\n\\\\nπ0 evidence:\\\\n- π0 (3.3B, 256 tokens, pure linear proj): k=0.1 normalized_L1 = 0.976 (-2.4% = improvement), k=0.5 = 0.983\\\\n- Attention entropy: π0 suffix-to-vision mean 0.959 (near-uniform across 18 layers, range [0.931, 0.983])\\\\n- Importance CV: π0 = 0.038 (lowest in spectrum)\\\\n\\\\n**Key insight**: \\\\\\\"Linear projection\\\\\\\" is NOT sufficient for immunity. The effective pipeline matters. X-VLA's BART encoder (12 transformer layers after linear proj) introduces partial dependencies → CV=0.151 → cliff at k=0.7. π0's pure linear proj → CV=0.038 → immune even at k=0.1.\\\\n\\\\n### Claim 3b: MLP Projector → Graded Degradation\\\\nMulti-layer MLP connectors create partial token dependencies through non-linear mixing, enabling graceful but real degradation.\\\\n\\\\n**Evidence** (OpenVLA 6-point degradation curve):\\\\n- k=1.0: 74.0% (baseline)\\\\n- k=0.95: 69.4% (-6% relative)\\\\n- k=0.9: 62.0% (-16% relative)\\\\n- k=0.7: 49.0% (-34% relative)\\\\n- k=0.5: 37.4% (-49% relative)\\\\n- k=0.3: 20.6% (-72% relative)\\\\n- Entropy ratio 0.639 (progressive sharpening L0=0.98→L29=0.48, TV=0.50)\\\\n- **Method independence confirmed**: random k=0.95=69.2% ≈ L2norm k=0.95=69.4%; random k=0.5=35.8% ≈ L2norm k=0.5=37.4%. For MLP projectors, pruning method doesn't matter.\\\\n- OFT (same connector, different action head): entropy 0.667 ≈ Standard 0.661 → connector determines attention structure, not action head\\\\n- CogACT (MLP projector, literature): 74.8% → 74.2% under 78% pruning (EfficientVLA)\\\\n\\\\n### Claim 4: Learned Re-Encoding Achieves Near-Lossless Compression Where Deletion Fails (D072+MLP confirmed → upgraded to METHOD per D091)\\\\n**⚠️ Baseline correction (2026-05-22): SmolVLA Object baseline = 59.2% (official HF checkpoint), NOT 44.8% (old reproduced). VTR narrative reframed from \\\\\\\"re-encoding boost\\\\\\\" to \\\\\\\"near-lossless compression recovery\\\\\\\".**\\\\n\\\\nTwo independent re-encoding architectures (~22M params each) validate that **any learned re-encoding** can recover entangled pixel_shuffle tokens from 0% (hard pruning) to near-baseline levels. Cross-attention (60.1±1.3%, 3-seed) and MLP adapter (63.4±2.6%, 3-seed) both achieve this recovery, with p≈0.15 confirming no significant difference between architectures. M=128 passthrough (58.0±3.5%, 3-seed) ≈ baseline 59.2% (-1.2pp), confirming VTR recovers to baseline rather than exceeding it. **M-curve is flat**: M=16 (56.9%) through M=128 (58.0%), all within ±3pp of baseline 59.2% — VTR achieves near-lossless compression at ANY ratio (0-87.5%) for pixel-shuffle connectors. M=64 achieves best absolute SR at 62.0±2.3% (+2.8pp over baseline) with 50% compression. Cross-suite generalization confirmed: M=32 recovers to 53.2% on Spatial (vs 0.6% pruning cliff-edge) and 56.4% on Goal. M=96 dip statistically confirmed (p=0.034 vs M=64).\\\\n\\\\n**D109 C4-ext on OpenVLA (MLP projector)**: M=128 VTR at 20K steps = **0% SR** (severe overfitting, model outputs identical action every step). This suggests VTR's effectiveness is connector-dependent: pixel-shuffle benefits enormously (0%→~59% ≈ baseline) because re-encoding repairs spatial entanglement, while MLP projector tokens are already individually meaningful and VTR adds unnecessary complexity. VTC-only M=32/M=64 training in progress — if these also fail, VTR is specifically a pixel-shuffle solution, which strengthens the architecture-dependency narrative.\\\\n\\\\n**Evidence** (all confirmed):\\\\n\\\\nCross-attention re-encoding (M sweep, 3-seed where available):\\\\n| M | Compression | SR (3-seed mean±std) | Seeds | Notes |\\\\n|---|------------|-----|-----|-----|\\\\n| 16 | 87.5% | **56.9±1.3%** | 42/43/44 | ✅ ZERO loss vs M=128 |\\\\n| 32 | 75% | **60.1±1.3%** | 42/43/44 | ✅ |\\\\n| 64 | 50% | **62.0±2.3%** | 42/43/44 | ✅ best tradeoff |\\\\n| 96 | 25% | 54.5±3.2% | 42/43/44 | ✅ highest variance |\\\\n| 128 | 0% (passthrough) | **58.0±3.5%** | 42/43/44 | ✅ passthrough control |\\\\n\\\\nMLP adapter control (M=32, ~22.14M params, 3-seed):\\\\n| Architecture | Params | M | Mean SR (3-seed) | Std | Individual seeds |\\\\n|---|---|---|-----|-----|-----|\\\\n| Cross-attention (VTC) | 22.2M | 32 | **60.1%** | ±1.3 | 61.6 / 59.2 / 59.6 |\\\\n| **MLP adapter** | **22.14M** | **32** | **63.4%** | **±2.6** | **65.2 / 64.6 / 60.4** |\\\\n\\\\nTwo-sample t-test: t≈1.94, p≈0.15 → **no significant difference** (α=0.05). Both >> 0% (hard pruning) and ≈ 59.2% (baseline). MLP ≥ VTC in all 3 seeds but difference not statistically significant — confirms any re-encoding architecture recovers to near-baseline, not a specific mechanism. (Note: M=32 seed43 corrected from 62.4% to 59.2% per registry verification; 62.4% was M=96 seed43 CI upper bound misattributed.)\\\\n\\\\n### Claim 5: CV Predicts Optimal Pruning Strategy — Monotonic Diagnostic Trend (D132→D139→D140→D142)\\\\nToken importance CV determines **which pruning method to use**, with the L2norm-vs-random gap scaling monotonically with CV. **Validated at TWO k values (D142):**\\\\n\\\\n**k=0.5 (main table):**\\\\n| Model | CV | Tokens | L2norm k=0.5 | Random k=0.5 | Δ (R-L2) |\\\\n|-------|-----|--------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | **33.4%** | **69.4%** | **+36.0pp** |\\\\n| X-VLA | 0.151 | 50 | 43.4%³ | 70.3%⁴ | +26.9pp |\\\\n| OpenVLA | 0.215 | 256 | 39.2% | 37.4%¹⁰ | -1.8pp |\\\\n\\\\n**k=0.7 (second validation, D142):**\\\\n| Model | CV | Tokens | L2norm k=0.7 | Random k=0.7 | Δ (R-L2) |\\\\n|-------|-----|--------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | **55.0%** | **77.2%** | **+22.2pp** |\\\\n| X-VLA | 0.151 | 50 | 58.6%⁶ | 65.1%⁷ | +6.5pp |\\\\n| OpenVLA | 0.215 | 256 | 49.8% | 44.4% | -5.4pp |\\\\n⁶ X-VLA L2norm k=0.7 2-seed: 58.2/59.0, mean=58.6%, σ=0.4pp (seed44 pending → tri-seed)\\\\n⁷ X-VLA random k=0.7 2-seed: 65.2/65.0, mean=65.1%, σ=0.1pp (seed44 running)\\\\n\\\\n³ X-VLA L2norm k=0.5 3-seed mean: 42.6/43.4/44.2, mean=43.4%, range 1.6pp\\\\n⁴ X-VLA random k=0.5 3-seed mean: 70.6/71.0/69.2, mean=70.3%, σ=0.9pp\\\\n\\\\n¹⁰ OpenVLA random k=0.5 = 37.4% (seed7). Table 3 previously showed 35.8% (unverified source). seed42 running on westd-38929, will replace when available.\\\\n\\\\n✅ **D139+D142 CONFIRMED**: Monotonic trend validated at BOTH k=0.5 (-1.8→+26.9→+36.0) and k=0.7 (-5.4→+6.5→+22.2). Same monotonic pattern. Paper: k=0.5 as main table, k=0.7 as confirmatory second row or separate table.\\\\n\\\\n**D140: k=0.3 interaction — method preference REVERSES at extreme compression for π0.5:**\\\\n\\\\n| Model | CV | Tokens | k=0.3 kept | L2norm k=0.3 | Random k=0.3 | Δ (R-L2) |\\\\n|-------|-----|--------|-----------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | 230 | **51.0%** | 36.4% | **-14.6pp** |\\\\n| X-VLA | 0.151 | 50 | 15 | 22.2%⁸ | **64.5%⁹** | **+42.3pp** |\\\\n| OpenVLA | 0.215 | 256 | 77 | 25.0% | **21.4%** | **+3.6pp** |\\\\n\\\\n⁸ X-VLA L2norm k=0.3 3-seed: 22.2/21.0/22.8 (from D137), mean=22.0%; seed43 running on cqa1\\\\n⁹ X-VLA random k=0.3 2-seed: 62.8/66.2, mean=64.5%, σ=2.4pp; seed44 running on cqa1\\\\n\\\\nAt k=0.3, π0.5 L2norm wins (+14.6pp) while X-VLA random still wins massively (+42.3pp). OpenVLA L2norm also wins (+3.6pp). The pattern: at k=0.3, both high-CV (OpenVLA) and low-CV-with-large-budget (π0.5, 230 tokens) favor L2norm, while mid-CV-with-small-budget (X-VLA, 15 tokens) strongly favors random. Strategy preference is f(CV, k, absolute_token_budget).\\\\n\\\\n**OpenVLA (CV=0.215) full seed42 Δ(L2-R) pattern**: +1.4pp (k=0.95) → +5.4pp (k=0.7) → pending (k=0.5) → +3.6pp (k=0.3). L2norm consistently better at ALL k values — high CV enables meaningful importance-based selection. Peak advantage at k=0.7, not monotonically increasing with compression.\\\\n\\\\n**D141: π0.5 L2norm complete curve — valley at k=0.5 confirmed (multi-seed)**:\\\\n| k | L2norm SR (s42) | L2norm SR (s43) | Random SR | Δ (R-L2) s42 |\\\\n|---|-----------------|-----------------|-----------|---------------|\\\\n| 0.7 | **55.0%** | **57.8%**¹⁰ | **77.2%** / **73.8%** (mean=75.5%) | +22.2pp (s42) / +19.8pp (mean) |\\\\n| 0.5 | **33.4%** | **33.6%** ✅ | **69.4%** / **68.4%** (mean=68.9%) | +36.0pp (s42) / +35.4pp (mean) |\\\\n| 0.3 | **51.0%** | **55.4%** ✅ | 36.4% | -14.6pp |\\\\n\\\\n¹⁰ Agent audit reported 56.4% for L2norm k=0.7 seed43 vs earlier worker result 57.8%. Needs reconciliation. Pattern unchanged.\\\\n\\\\n**V-shape fully confirmed (2 seeds, both methods)**:\\\\n- **Valley (k=0.5)**: L2norm 33.4/33.6% (std=0.1pp); Random 69.4/68.4% (std=0.7pp) — both methods stable\\\\n- **2-seed means**: L2norm k=0.7=56.4%, k=0.5=33.5%, k=0.3=53.2%; Random k=0.7=75.5%, k=0.5=68.9%\\\\n- **V-depth**: seed42=17.6pp, seed43=21.8pp (seed43 deeper because endpoints higher)\\\\n- **Δ(R-L2) dual-seed means**: k=0.7=+19.8pp, k=0.5=+35.4pp — monotonic trend holds with multi-seed\\\\n- seed43 consistently +2-4pp above seed42 but identical shape. Valley position/depth is architectural determinism.\\\\n\\\\n**Mechanism confirmed by token position visualization (D141)**:\\\\n- k=0.7: 2 clusters, 97% in largest, **100% spatial coverage** — enough tokens to maintain coverage\\\\n- k=0.5: **1 cluster, 100% in single region, 78% coverage** — worst-case spatial concentration\\\\n- k=0.3: **3 clusters**, 86% in largest, 78% coverage — cluster breaks apart, better diversity\\\\n\\\\nThe non-monotonicity arises because k=0.5 sits at the worst point of the spatial correlation structure: L2norm selects exactly the number of tokens that maximizes spatial clustering. At k=0.7 there are enough tokens for coverage; at k=0.3 the selection threshold crosses a boundary that fragments the cluster. Per-task variance is extreme at k=0.7 (T1=94%, T5=98% vs T7=0%) — L2norm deterministic selection can catastrophically miss specific task-critical spatial regions.\\\\n\\\\n**Paper strategy**: k=0.5 as **main table** (cleanest monotonic trend, clear gap). Full L2norm curve as **figure** showing pathological valley — strong evidence for spatial clustering mechanism. k=0.3 reversal as supplementary. Key message: \\\\\\\"CV predicts method preference at k=0.5; L2norm's spatial clustering creates pathological non-monotonicity unique to low-CV models.\\\\\\\"\\\\n\\\\n**Notable asymmetry**: Random tolerance is similar for low/medium CV at k=0.5 (π0.5=69.4% ≈ X-VLA=70.6%), while L2norm harm increases dramatically (π0.5=33.4% < X-VLA=43.4%). High CV (OpenVLA=35.8% random) is less random-tolerant because tokens have genuine importance differentiation that random discards.\\\\n\\\\n**Evidence** (Reviewer-verified, D132 PASS):\\\\n\\\\nX-VLA vs OpenVLA full comparison:\\\\n\\\\n| k | X-VLA (CV=0.151) | | OpenVLA (CV=0.215) | |\\\\n|---|---|---|---|---|\\\\n| | L2norm | Random | L2norm | Random |\\\\n| 0.95 | — | — | 70.6% | 69.2% (+1.4 L2norm) |\\\\n| 0.9 | 97.6% | 97.8% (≈0) | 70.6% | 64.6% (+6.0 L2norm) |\\\\n| 0.85 | 68.0% | 63.6% (+4.4 L2norm) | — | — |\\\\n| 0.8 | 89.0% | 89.4% (≈0) | — | — |\\\\n| 0.7 | 56.2% | **65.2% (+9pp random)** | 49.8%¹ | 44.4% (+5.4 L2norm¹) |\\\\n| 0.5 | **42.6%** | **70.6% (+28pp random!)** | 39.2% | 35.8% (+3.4 L2norm) |\\\\n| 0.3 | **22.8%** | **62.8% (+40pp random!)** | 25.0% | pending² |\\\\n\\\\n¹ OpenVLA L2norm k=0.7 = seed43 only, random = seed42; cross-seed caveat. seed42 L2norm k=0.7 running on westd-38929.\\\\n² OpenVLA random k=0.3 result file missing, re-running on westd-38929.\\\\n³ D137 multi-seed: X-VLA random k=0.5 seed43=71.0% (seed42=70.6%, Δ=0.4pp). Gap reproducible.\\\\n\\\\n**Per-task X-VLA k=0.5 (Reviewer-verified, 9/10 tasks random > L2norm):**\\\\n\\\\n| Task | Baseline | L2 s42 | L2 s43 | Random s42 | Δ(R-L2) |\\\\n|------|---------|--------|--------|------------|---------|\\\\n| T0 alphabet_soup | 98% | 58% | 56% | **96%** | +38 |\\\\n| T1 cream_cheese | 100% | 2% | 6% | 46% | +44 |\\\\n| T4 ketchup | 100% | 42% | 40% | **100%** | **+58** |\\\\n| T7 milk | 100% | 38% | 38% | 82% | +44 |\\\\n| T9 orange_juice | 100% | 68% | 70% | **100%** | +32 |\\\\n| T6 butter | 100% | 2% | 2% | 2% | 0 (both crash) |\\\\n\\\\nL2norm two seeds highly consistent (s42 vs s43 diff <6pp) → not RNG noise.\\\\nT6: baseline=100% but both methods=2% → highly localized visual cue, k=0.5 always loses it regardless of method.\\\\nT4/T9: Random recovers to baseline → L2norm systematically discards the critical tokens for these tasks.\\\\n\\\\n**Pattern**: Low CV (X-VLA) → importance-based selection degenerates at aggressive k → random better. High CV (OpenVLA) → meaningful importance differentiation → L2 norm better.\\\\n\\\\n**Mechanism hypothesis** (Reviewer: consistent with data, needs direct evidence): X-VLA's linear projection + BART encoder produces tokens with relatively uniform L2 norms (CV=0.151). At aggressive compression (k=0.5 = keeping 25 of 50 tokens), L2 norm selects the \\\\\\\"slightly larger\\\\\\\" tokens which tend to be spatially clustered → loses spatial diversity → catastrophic. Random preserves spatial coverage stochastically → dramatically better.\\\\n\\\\n**⚠️ Visualization needed (Reviewer warning)**: Must produce token position visualization — for same input image, show which tokens L2 norm vs random retains. If L2 norm shows spatial clustering, mechanism is proven. This should be a key figure (§4.6 or Fig 4).\\\\n\\\\n**Implication for practitioners**: CV diagnoses → predicts tolerance → prescribes strategy at aggressive compression. Low CV + aggressive k (≤0.5) → random/position-based. High CV → importance-based at all k. Mild compression (k≥0.8) → method choice doesn't matter regardless of CV.\\\\n\\\\n**Pending**: X-VLA random k=0.7 (crossover), multi-seed k=0.5, token position visualization, OpenVLA L2norm k=0.7 seed42, k_ratio=null fix.\\\\n\\\\n## Story Spine\\\\n\\\\n**Problem**: Vision token efficiency is critical for real-time VLA deployment. Growing literature proposes inference-time token reduction (FastV, VLA-IAP, H2O, ToMe). These methods succeed on some VLAs but their behavior across different architectures is unstudied.\\\\n\\\\n**Gap**: No work has systematically compared token pruning robustness across VLA architectures. The implicit assumption that \\\\\\\"token pruning works or fails uniformly\\\\\\\" is untested. The critical architectural factor determining prunability is unknown.\\\\n\\\\n**Discovery**: We find that VLA token pruning robustness is governed by two interacting axes. **Axis 1 — Token Coupling**: connector architecture determines whether tokens are independent (linear proj, MLP) or entangled (BART encoder, pixel-shuffle), diagnosed by importance CV (0.038→0.314). **Axis 2 — Task Complexity**: multi-step tasks (Goal/Long) amplify pruning damage on entangling connectors — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at k=0.9. Evidence from 5 VLA models × 4 LIBERO suites:\\\\n- **Token-independent** (π0, π0.5 linear; OpenVLA, OFT MLP): graded degradation, CV 0.038–0.219\\\\n- **Token-entangling** (X-VLA BART 12L; SmolVLA pixel-shuffle): task-dependent collapse — tolerate simple tasks, catastrophic on complex tasks. CV 0.151–0.314\\\\nCV predicts both pruning tolerance and optimal strategy (L2norm hurts low-CV models, helps high-CV).\\\\n\\\\n**Solution**: Diagnose-then-Compress framework. Step 1: Token importance CV provides zero-cost diagnostic for pruning tolerance (one forward pass). Step 2: VTR (Vision Token Re-encoding) provides universal compression. For pixel-shuffle: recovers from 0% (hard pruning) to ~59% ≈ baseline (59.2%), M-curve flat (D105: M=16 56.9% ≈ M=128 58.0%, near-lossless at any compression ratio). For MLP projector: D109 C4-ext = 0% SR (overfitting at M=128); VTC-only M=32/M=64 in progress.\\\\n\\\\n**Headline result**: \\\\\\\"Across 5 VLA models (450M-7B) × 4 task suites, we find that token pruning robustness is governed by two axes: connector architecture (token-independent vs token-entangling, diagnosed by importance CV) and task complexity. Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio; SmolVLA collapses to 0% at 5% removal regardless of task. CV (0.038→0.314) predicts both pruning tolerance and optimal strategy: importance-based pruning is actively harmful on low-CV architectures (+28-36pp gap favoring random), while it helps on high-CV models (+1-6pp). VTR recovers to ~59% (≈baseline) at any compression ratio (0-87.5%) where hard deletion achieves 0%.\\\\\\\"\\\\n\\\\n## Paper Structure (7-model version)\\\\n\\\\n1. **Introduction**: VLA efficiency motivation → diverse connector architectures → 2-axis framework discovery (D171) → Diagnose-then-Compress framework\\\\n2. **Background**: 5 VLA models, 3 connector families (linear/MLP/pixel-shuffle), 4 LIBERO suites, token flow analysis\\\\n3. **Experimental Setup**: 5 models, LIBERO benchmark (4 suites: Object/Spatial/Goal/Long), pruning protocol, VTR compression, diagnostic metrics\\\\n4. **Main Results**:\\\\n   - §4.1: 2-Axis Framework Overview (Table 1: 5 models × token coupling axis; Table 2: cross-suite interaction — connector × task complexity)\\\\n   - §4.2: Token-Entangling Catastrophic — pixel-shuffle cliff-edge (SmolVLA, all configs 0% regardless of task)\\\\n   - §4.3: Token-Independent Graded — MLP degradation (OpenVLA 6-point curve + OFT entropy confirmation)\\\\n   - §4.4: Token-Independent Tolerant — linear projection (π0 + π0.5, controlled comparison with OpenVLA)\\\\n   - §4.5: Task Complexity Amplification — X-VLA cross-suite (Object 97.6% vs Goal 70.2% vs Long ~53% at same k)\\\\n   - §4.6: Pruning Strategy Depends on CV (D132: low-CV random>>L2norm, high-CV L2norm>>random)\\\\n   - §4.7: VTR overcomes cliff-edge (M-curve flat + architecture independence)\\\\n   - (REMOVED — D119: LIBERO-Plus L1 SR=3.3% floor effect, noted in Discussion §6)\\\\n5. **Analysis**:\\\\n   - §5.1: Why pixel_shuffle creates entanglement (spatial folding + controlled comparison)\\\\n   - §5.2: Diagnostic metric — Entropy + CV composite (D104, 4-model validation)\\\\n   - §5.3: Re-encoding mechanism (M=128 passthrough + MLP adapter + M-curve flat D105)\\\\n6. **Discussion**: Design implications, limitations (sim-only, no real robot), future work\\\\n7. **Conclusion**: 5 claims summary\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Only 2 models → **FULLY ADDRESSED**\\\\n**Response**: Now 5 models (SmolVLA, OpenVLA, OpenVLA-OFT, π0, X-VLA) across 3 connector families (pixel-shuffle, 3-layer MLP, linear projection) and 4 model sizes (450M-7B). Each connector class has ≥2 models.\\\\n\\\\n### RC2: Model size confound (450M vs 7B) → **FULLY ADDRESSED**\\\\n**Response**: π0 (3.3B, linear) is pruning-immune while OpenVLA (7B, MLP) degrades 61% at k=0.1. Larger model is MORE vulnerable, not less — directly falsifies \\\\\\\"larger models are more robust\\\\\\\" hypothesis. X-VLA (880M, linear) also immune, matching π0 behavior despite 4× smaller. Size is not the explanatory variable; connector type is.\\\\n\\\\n### RC3: Why not test SmolVLA without pixel_shuffle?\\\\n**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.\\\\n\\\\n### RC4: Smart compression — is re-encoding or compression the mechanism?\\\\n**Response (corrected with baseline=59.2%)**: VTR achieves near-lossless compression at any ratio — the M-curve is flat (M=16: 56.9% → M=128: 58.0%, all within ±3pp of baseline 59.2%). Two lines of evidence: (1) M=128 passthrough (58.0%) ≈ baseline (59.2%) — re-encoding recovers spatial entanglement to baseline level, not above it. (2) Architecture control: MLP adapter (63.4%) ≈ cross-attention (60.1%) with CI overlap — any re-encoding mechanism works. The key contribution is recovery from 0% (hard pruning) to ~59% (baseline), not exceeding baseline. Compression ratio is a free parameter with negligible SR cost.\\\\n\\\\n### RC5: Relationship to VLA-IAP\\\\n**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.\\\\n\\\\n### RC6: Is this just \\\\\\\"different models behave differently\\\\\\\"?\\\\n**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.\\\\n\\\\n### RC7: Only one benchmark (LIBERO-Object) → **ADDRESSING (D115, D119)**\\\\n**Response**: Expanded to ALL 4 LIBERO suites (Object/Spatial/Goal/Long) — 4 genuinely different task distributions (manipulation skills, spatial reasoning, goal-conditioned, long-horizon). Taxonomy consistency validated across suites. LIBERO-Plus robustness benchmark tested (D119) but abandoned: L1 camera perturbation collapses OpenVLA to SR=3.3% (consistent with leaderboard 0.8%), creating floor effect with no room for pruning analysis. This floor effect itself is noted in Discussion as evidence of general VLA brittleness under distribution shift. Sim-only limitation acknowledged.\\\\n\\\\n## All Experimental Evidence (confirmed)\\\\n\\\\n### SmolVLA Cliff-Edge\\\\n- Fine-tuned baseline (Object): 44.8% (224/500) — ⚠️ OLD reproduced checkpoint, superseded by official HF = 59.2%\\\\n- 6 pruning conditions (random/ACIS/ToMe × k=0.5/0.7/0.9): all 0%\\\\n- Geometric prior (Sobel) k=0.5/0.7/0.9: all 0%\\\\n- Attention entropy: 0.952 (flat, TV=0.05)\\\\n- Official checkpoint Object: 59.2% → 0% at k=0.5\\\\n- Official checkpoint Spatial: 43.8% → 0.6% (3/500, CI [0.2%, 1.7%]) at k=0.5 — near-zero, confirms cliff-edge across suites\\\\n- LoRA-FT checkpoint Spatial: 8.0% (per-task: [24,8,4,24,0,2,2,2,14,0]) — LoRA trained on Object only, does not transfer to Spatial. Use official checkpoint for cross-suite SmolVLA analysis.\\\\n\\\\n### OpenVLA Degradation Curve\\\\n- k=1.0: 74.0% (370/500)\\\\n- k=0.95: 69.4% (-6% relative)\\\\n- k=0.9: 62.0% (-16% relative)\\\\n- k=0.7: 49.0% (245/500, -34% relative)\\\\n- k=0.5: 37.4% (187/500, -49% relative)\\\\n- k=0.3: 20.6% (103/500, -72% relative)\\\\n- Entropy: 0.639 (progressive sharpening, TV=0.50)\\\\n\\\\n### Cross-Model Pruning Taxonomy (7 models — D100, D120, D127)\\\\n| Model | Connector | Tokens | k=0.1 norm_L1 | k=0.5 norm_L1 | Class |\\\\n|-------|-----------|--------|---------------|---------------|-------|\\\\n| π0 (3.3B) | Pure linear proj | 256 | 0.976 (-2.4%) | 0.983 | Immune |\\\\n| π0.5 (4B) | Pure linear proj (×√d scaling) | 768 (3×256) | **98.2%** (491/500) | **L2norm=33.4%, random=69.4%** | **Uniformly Critical (D139)**: L2norm catastrophic (-64.8pp), random tolerant (-28.8pp), gap=+36pp. CV=0.055. |\\\\n| X-VLA (880M) | Linear + BART 12L | 50 | ~1.00 | ~1.00 | Threshold-graded (k=0.7: 56.2%) |\\\\n| OpenVLA (7B) | 3-layer MLP | 256 | 1.608 (+61%) | 1.167 (+17%) | Smooth graded |\\\\n| OFT (7B) | 3-layer MLP (DINOv2+SigLIP fused) | **512** | N/A | N/A | D136: Blackwell GPU incompatible. CV=0.219≈OpenVLA → graded. Cite official ~97% baseline. |\\\\n| SmolVLA (450M) | Pixel-shuffle | 128 | — | 0% cliff | Catastrophic |\\\\n\\\\nDiagnostic metrics (D104+D106+D120: CV as continuous predictor, 7 models):\\\\n| Model | Connector (effective) | Entropy | CV | Pruning Behavior |\\\\n|-------|----------------------|---------|------|------------------|\\\\n| π0 | Pure linear proj | 0.959 | 0.038 | Immune (offline, k=0.1 improves) |\\\\n| π0.5 | Pure linear proj (×√d) | pending | 0.055 | **Uniformly Critical (D139)**: L2norm=33.4%, random=69.4%, gap=+36pp. Monotonic trend extreme. |\\\\n| X-VLA | Linear proj + BART enc (12L) | **0.614** | **0.151** | Threshold-graded: robust k≥0.9, cliff k=0.7 (56.2%). D127: random=L2norm at k=0.9 |\\\\n| OpenVLA | 3-layer MLP (GELU) | 0.661 | 0.215 | Graded (74→37.4% at k=0.5) |\\\\n| OFT | 3-layer MLP (DINOv2+SigLIP, **512 tokens**) | 0.667 | 0.219 | D136: Graded expected (CV≈OpenVLA). Blackwell GPU incompatible, no LIBERO SR. |\\\\n| SmolVLA | Pixel-shuffle (16×) | 0.952 | **0.314** | Catastrophic (0% at k=0.95) |\\\\n\\\\nKey insights (updated with 7-model data):\\\\n1. **CV is a continuous predictor**: 0.038 → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 maps to decreasing pruning tolerance. NOT a 3-class discrete classifier.\\\\n2. **X-VLA CV=0.151 correctly predicted its intermediate behavior** — closer to OpenVLA (0.215) than π0 (0.038), matching k=0.7 SR ≈ OpenVLA k=0.7.\\\\n3. **X-VLA entropy=0.614 ≈ OpenVLA 0.661** — both have BART/MLP non-linear mixing. X-VLA is NOT \\\\\\\"high entropy\\\\\\\" like π0.\\\\n4. **Effective connector complexity matters more than nominal label**: X-VLA is \\\\\\\"linear proj\\\\\\\" but BART encoder introduces 12 transformer layers of mixing. Paper should discuss \\\\\\\"effective connector\\\\\\\" = projection + any intermediate processing.\\\\n5. OFT entropy 0.667 ≈ Standard 0.661 → action head does not affect attention structure\\\\n6. Framing: CV captures \\\\\\\"degree of non-linear mixing in the vision-to-LLM pathway.\\\\\\\" More mixing → higher CV → less tolerant of pruning.\\\\n\\\\n### Smart Compress (Learned Re-encoding)\\\\nCross-attention (VTC) M sweep (3-seed where available):\\\\n- M=16: **56.9% ± 1.3pp** (3-seed: 55.8/58.4/56.5) — 87.5% compression, ZERO loss vs M=128\\\\n- M=32: 60.1±1.3% (3-seed: 61.6/59.2/59.6)\\\\n- M=64: 62.0±2.3% (3-seed: 61.6/60.0/64.4)\\\\n- M=96: 54.5±3.2% (3-seed: 52.6/58.2/52.8) — highest variance\\\\n- M=128: 58.0±3.5pp (3-seed: 59.8/54.0/60.2) — passthrough control\\\\n- **D102 CONFIRMED: M-curve is flat.** M=16 (56.9%) = M=128 (58.0%), difference < 1.1pp. VTC achieves near-lossless compression at ANY ratio for pixel-shuffle connector. All M values within ±5pp of baseline ~59%.\\\\n\\\\nMLP adapter (M=32, 3-seed):\\\\n- seed42: 65.2% (326/500), seed43: 64.6% (323/500), seed44: 60.4% (302/500)\\\\n- Mean: 63.4% ± 2.6 vs VTC M=32 mean 60.1% ± 1.3\\\\n- t-test p≈0.15, no significant difference — confirms architecture-independence\\\\n\\\\n### D109: VTR on OpenVLA (MLP projector) — FAILED\\\\n- C4-ext M=128 at 20K steps: **0% SR** (0/44 episodes before eval termination)\\\\n- Failure mode: model outputs identical action every timestep (severe overfitting)\\\\n- Interpretation: VTR adds unnecessary complexity for MLP projector tokens (already individually meaningful). VTR specifically solves pixel-shuffle entanglement.\\\\n- VTC-only M=32 and M=64 training in progress on westd-41074:2-3\\\\n\\\\n### Cross-Suite VTR Generalization (SmolVLA)\\\\n- M=32 Spatial: 53.2% (vs official Spatial baseline 44.6% per ROADMAP, vs pruning 0.6% — recovery from cliff-edge, +8.6pp over baseline)\\\\n- M=32 Goal: 56.4% (vs official Goal baseline 60.8% per ROADMAP, vs pruning 0% — recovery from cliff-edge, -4.4pp below baseline)\\\\n- ⚠️ Cross-suite baselines need reconciliation: paper_framing previously used 43.8%/63.0%, ROADMAP uses 44.6%/60.8%. Use n=500 official checkpoint data as ground truth.\\\\n- Note: VTR trained on Object suite, evaluated cross-suite. Official baselines from different checkpoint (official vs LoRA-FT); comparisons should emphasize recovery from 0% rather than absolute performance vs uncompressed.\\\\n\\\\n### Pairwise Statistical Tests (Welch's t-test, n=3 per condition)\\\\n- M=32 VTC vs M=32 MLP: p=0.150 (not significant) — confirms architecture-independence\\\\n- M=64 VTC vs M=96 VTC: p=0.034 (significant) — M=96 dip confirmed real\\\\n- M=32 MLP vs M=96 VTC: p=0.022 (significant) — M=96 underperforms\\\\n- M=32/M=64/M=128 VTC cluster: all pairwise p>0.25 — robust across M values\\\\n- Bonferroni note: no pair survives correction at 10 tests; n=3 limits power (~0.2 for medium effects)\\\\n\\\\n### Supplementary\\\\n- Inference latency: 6% speedup at M=32\\\\n- KV-cache: 75% memory reduction at M=32\\\\n\\\", \\\"total_chars\\\": 51958, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\", \"content\": \"# Paper Framing — importance_margin_vla_compress\\n\\n## Target Venue\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\n\\n## Title (working)\\n\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\"\\n\\n## Core Insight\\n\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\"threshold-graded\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\n\\n**Axis 1 — Token Coupling (connector architecture):**\\n| Type | Connectors | CV Range | Mechanism |\\n|------|-----------|----------|-----------|\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\n\\n**Axis 2 — Task Complexity:**\\n| Level | Suites | Characteristics |\\n|-------|--------|----------------|\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\\n\\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\\n- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance\\n- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen\\n- Token-independent (π0.5 Goal/Long): data collecting, expected smaller amplification\\n\\n**CV remains the primary Axis-1 diagnostic** — predicts both pruning tolerance and optimal strategy (Claim 5). Task complexity (Axis 2) explains within-model variance across suites that the old taxonomy could not capture.\\n\\n_Original per-connector evidence (from Object-suite 4-class taxonomy) retained below; reinterpret through 2-axis lens:_\\n- **Linear projection** (π0 3.3B, π0.5 4B): **\\\"Uniformly Critical\\\" (D139)**. NOT immune. π0.5 baseline=98.2%, random k=0.5=**69.4%** (-28.8pp), L2norm k=0.5=**33.4%** (-64.8pp). Gap=+36.0pp, random wins 9/10 tasks. Low CV (0.038/0.055) = uniformly important tokens → L2norm's systematic bias selects spatially clustered tokens → catastrophic at k≤0.7. Random preserves spatial coverage → 2× better at k=0.5. **L2norm extended curve:** k=0.1=2.6% (collapse) → k=0.3=51.0% → k=0.5=33.4% (valley) → k=0.7=55.0% → k=0.9=98.2%. V-shape with collapse at extreme compression. CV=0.055 makes this the extreme case of the monotonic diagnostic trend. **⚠️ MAJOR FINDING (2026-05-22, fully investigated):** π0.5 random pruning exhibits sharp cliff at k=0.85-0.925 with non-monotonic recovery:\\n  - k=0.95: 71.1% FINAL (seed42 500ep; seed43=72.8%) — already 27pp below baseline\\n  - k=0.925: **27.6%** FINAL (seed42) — cliff entry point, 43pp drop from k=0.95\\n  - k=0.9: 10.8%±1.2pp (dual seed: seed42=12.0%, seed43=9.6%) — **87.4pp gap vs L2norm k=0.9=98.2%**\\n  - k=0.85: **5.0%** FINAL (seed42 v2=4.4%) — cliff floor\\n  - k=0.7: 75.5% (mean), k=0.5: 68.9%, k=0.3: 36.4% — recovery zone\\n  - Cliff profile: 71.1%(k=0.95) → 27.6%(k=0.925) → 10.8%(k=0.9) → 5.0%(k=0.85) — 66pp collapse over 10% keep ratio change\\n  **D151 (2026-05-22): Cliff is RANDOM-SPECIFIC.** L2norm maintains 98.0-99.2% plateau across the entire cliff zone:\\n  - L2norm k=0.95=98.2%, k=0.925=99.2%, k=0.9=98.2%, k=0.85=98.0% — zero degradation\\n  - Random k=0.925: 27.6% vs L2norm=99.2% → **71.6pp gap** (maximum separation)\\n  - Random k=0.85: 5.0% vs L2norm=98.0% → **93.0pp gap**\\n  - L2norm succeeds because deterministic selection consistently retains the same token subset; random sampling creates variable damage\\n  **D152 (2026-05-22): Cliff is TASK-SPECIFIC.** Object tasks collapse catastrophically, Spatial tasks degrade but survive:\\n  - Random k=0.9: Object=10.8% vs Spatial=54.6% — Spatial retains 5× more SR\\n  - Random k=0.85: Object=5.0% vs Spatial=TBD (collecting)\\n  - Within Object suite: all 10 tasks collapse at k=0.9 (2-16%). Within Spatial suite: degradation but not catastrophic.\\n  - Mechanism: Object tasks require precise object identity discrimination (visually similar objects); Spatial tasks rely on spatial layout (more distributed visual information). Random token loss destroys fine-grained discriminative features needed for Object before destroying spatial layout features.\\n  **Fixed-mask experiment (D149) NEGATES temporal inconsistency hypothesis:** per-episode fixed mask T0=12% = per-call random T0=12%. Temporal mask variation is NOT the cause.\\n  **D153: Cross-suite LIBERO-Spatial — weaker non-monotonicity, no catastrophic dip (2026-05-22)**\\n  Baseline: 97.2%. Random pruning profile:\\n  | k | Object | Spatial | Δ | Pattern |\\n  |---|--------|---------|---|---------|\\n  | 0.95 | 71.1% | deploying | — | — |\\n  | 0.925 | 28.8% (2-seed) | — | — | — |\\n  | 0.9 | 10.8% | 54.6% | +43.8pp | Spatial 5× more robust |\\n  | 0.85 | 5.0% | **58.4%** | **+53pp** | Maximum divergence |\\n  | 0.7 | 75.5% | 74.4% | -1pp | Suite-independent |\\n  | 0.5 | 69.4% | 71.6% | +2pp | Suite-independent |\\n  | 0.3 | 36.4% | 49.6% | +13pp | Spatial more robust |\\n  L2norm Spatial: k=0.9=95.0%, k=0.7=67.0%, k=0.5=55.6%, k=0.3=57.2%. L2norm k=0.95/k=0.85 deploying.\\n  **Object has deep V-shape dip**: 5%(k=0.85) → 10.8%(k=0.9) → 75.5%(k=0.7), 70pp recovery from cliff floor. **Spatial has weaker non-monotonicity**: k=0.5(71.6%) > k=0.85(58.4%) > k=0.9(54.6%), but no catastrophic collapse — floor stays above 50% vs Object's 5% floor. The cliff zone gap (Object 5% vs Spatial 58%) reflects concentrated vs distributed critical token patterns.\\n  **Mechanism**: Object tasks have **concentrated** critical tokens (object identity discrimination — visually similar objects). Random removal at cliff zone destroys these concentrated patches → catastrophic. Spatial tasks have **distributed** critical information (layout patches spread across image). Random removal damages any random subset but never completely destroys spatial signal → graceful degradation.\\n  **Paper value**: Two distinct cliff behavior modes — **concentrated-critical (Object)** vs **distributed-critical (Spatial)** — as a function of task semantics. Pruning sensitivity = f(connector, method, k, task_semantics). Suite-independent at moderate k (0.5-0.7), suite-dependent at cliff zone (0.85-0.95).\\n  **Paper value:** strengthens \\\"uniformly critical\\\" class — even uniform importance distribution doesn't make pruning safe. Simple deletion fails; learned compression (VTR) needed.\\n- **Linear projection + deep post-processing** (X-VLA 880M, linear proj + 12-layer BART encoder): robust k≥0.9 (97.6% SR), **cliff at k=0.7 (56.2% SR, -43pp)**. BART encoder introduces non-linear mixing that creates partial token dependencies. CV=0.151. **D127: random pruning k=0.9=97.8% ≈ L2norm 97.6% — pruning method independence confirmed for low-CV connectors.**\\n- **Multi-layer MLP** (OpenVLA 7B, OpenVLA-OFT 7B): graded degradation. k=0.1 normalized loss = 1.608 (+61%). Non-linear mixing creates partial dependencies. OFT entropy (0.667) ≈ Standard (0.661), CV(OFT)=0.219 ≈ CV(OpenVLA)=0.215, confirming connector — not action head — determines attention structure. **D136: OFT LIBERO eval infeasible (Blackwell GPU SDPA incompatibility, requires A100+torch2.2). OFT included via CV/entropy analysis only; cite official baseline ~97% SR.** π0.5 baseline confirmed 98.2% (D135).\\n- **Pixel-shuffle** (SmolVLA 450M): catastrophic cliff-edge. k=0.95 (removing 5%) → 0% SR. Spatial folding creates irreversible entanglement. **D147: Official HF checkpoint (HuggingFaceVLA/smolvla_libero) confirms identical cliff — random k=0.95 = 0%, L2norm k=0.95 = 0%. Cliff is architectural, not training artifact. Resolves W-C2.** **Dual-seed confirmed (2026-05-22):** Baseline 59.4%±0.3pp (seed42=59.2%, seed43=59.6%), random k=0.95: 0.1% mean (0.0%/0.2%), random k=0.5: 0.0%, L2norm k=0.95: 0.2% mean (0.4%/0.0%). All pruning ≤0.2% across both seeds. cqa1 supplementary: L2norm k=0.7=0%, random k=0.9=0%.\\n\\nKey controlled comparison: π0 (256 tokens, linear) vs OpenVLA (256 tokens, 3-layer MLP) — same token count, same encoder lineage, only connector differs. k=0.1: π0 improves 2.4% vs OpenVLA degrades 61%. This isolates connector as the causal factor.\\n\\nLearned re-encoding (VTR) overcomes the cliff-edge: cross-attention 60.1±1.3% and MLP adapter 63.4±2.6% at M=32 (vs 0% hard pruning), with M=128 passthrough (58.0%±3.5, 3-seed) ≈ baseline 59.2% — VTR recovers to baseline rather than exceeding it. SmolVLA M-curve confirmed flat (D105): M=16 (56.9%±1.3) = M=128 (58.0%±3.5), all 5 M-values within ±3pp of baseline 59.2%. VTR achieves near-lossless compression at any ratio (0-87.5%) for pixel-shuffle connectors.\\n\\n## Paper Identity (Round 5 Upgrade — D171 2-Axis, 2026-05-22)\\n**ANALYSIS + METHOD paper.** (D091 → D097 → D171: 5 models × 3 connector families × 4 LIBERO suites)\\n\\n**Analysis contribution (primary)**: First systematic study revealing that VLA token pruning robustness is determined by the interaction of two axes: (1) connector architecture (token-independent vs token-entangling, diagnosed by importance CV 0.038→0.314) and (2) task complexity (simple vs multi-step). Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio. 5 models × 4 suites × 4 model sizes (450M-7B) eliminate confounds. No competing work does cross-architecture, cross-task VLA token analysis.\\n\\n**Method contribution**: Diagnose-then-Compress framework:\\n- Step 1: **Connector Compressibility Diagnostic** (D104: resolved)\\n  - **Primary metric: Importance CV** (token importance heterogeneity) — zero-cost, one forward pass\\n  - CV forms continuous spectrum predicting pruning tolerance: π0=0.038 < π0.5=0.055 < X-VLA=0.151 < OpenVLA=0.215 < OFT=0.219 < SmolVLA=0.314\\n  - ⚠️ D106+: X-VLA CV=0.151 correctly predicted its intermediate pruning behavior (k=0.7 ≈50% SR ≈ OpenVLA k=0.7). CV is a valid continuous predictor, NOT a 3-class discrete classifier.\\n  - **Key discovery**: X-VLA \\\"linear projection\\\" passes through BART encoder (12 transformer layers) before decoder → introduces non-linear mixing → explains CV=0.151 (much higher than π0=0.038 pure linear)\\n  - **Entropy as mechanistic supplement** (CV is primary; entropy is supplementary):\\n    - π0: entropy=0.959 (per-layer mean, range 0.931–0.983), CV=0.038 — uniform & independent → most tolerant\\n    - **π0.5: entropy=0.666, CV=0.055** — similar entropy to OpenVLA (0.661) but vastly different pruning behavior (CV correctly differentiates)\\n    - X-VLA: entropy=0.614, CV=0.151 — selective & BART-mixed → intermediate\\n    - OpenVLA: entropy=0.661, CV=0.215 — selective & MLP-mixed → graded\\n    - SmolVLA: entropy=0.952, CV=0.314 — near-uniform but spatially entangled → catastrophic\\n  - **KEY INSIGHT**: Entropy clusters π0.5/X-VLA/OpenVLA together (0.61-0.67) despite very different pruning behaviors. CV correctly separates them (0.055 vs 0.151 vs 0.215). Entropy fails as diagnostic because it doesn't capture token independence structure — only attention distribution shape.\\n  - ✅ Batch 2 complete: continuous CV spectrum confirmed (X-VLA full 8-point curve validates threshold-graded class)\\n  - Supplementary: lightweight pruning probe (remove 5%, one forward pass) as practitioner-friendly alternative\\n- Step 2: VTR (Vision Token Re-encoding) — lightweight cross-attention module (~22M params) for universal compression\\n- For entangled tokens (pixel-shuffle): recovers from 0% (hard pruning) to ~59% ≈ baseline, M-curve flat D105 (near-lossless compression at any ratio 0-87.5%)\\n- For independent tokens (MLP projector): **D109 C4-ext confirmed 0% SR** at 20K steps (M=128, severe overfitting — model outputs identical action every step). VTR on MLP projector does NOT improve SR; reframed as \\\"VTR ceiling depends on connector type\\\" finding. User directive: performance degradation acceptable if efficiency improves — VTR value is 75% KV-cache reduction + attention speedup. VTC-only M=32/M=64 training in progress to test whether smaller M values fare better.\\n\\n**Differentiation from concurrent work**: 4 concurrent works (Compressor-VLA, SpecPrune-VLA, LightVLA ICRA'26, See What Matters ICML'26) all propose pruning on MLP-projector VLAs. We (1) explain why pruning fails on pixel-shuffle architectures, (2) identify why pruning succeeds on linear projection (tokens are truly independent), and (3) propose a re-encoding method motivated by the diagnostic analysis.\\n\\n**Model coverage**: 5 VLA models × 3 connector families × 4 LIBERO suites × 4 model sizes (450M-7B). RC1 (only 2 models), RC2 (size confound), and RC7 (only one suite) fully addressed.\\n\\n## Core Claims (5 claims, expanded from 4)\\n\\n### Claim 1: 2-Axis Compressibility Framework (D107 → D171 UPGRADED)\\nPruning sensitivity = f(connector_architecture, task_complexity). Two axes interact:\\n\\n**Axis 1 — Token Coupling (connector determines base sensitivity):**\\n- **Token-independent** connectors (pure linear π0/π0.5, MLP OpenVLA/OFT): tokens retain spatial meaning → pruning damage is local, graded degradation\\n- **Token-entangling** connectors (BART X-VLA, pixel-shuffle SmolVLA): cross-token dependencies → pruning damage cascades\\n\\n**Axis 2 — Task Complexity (task amplifies entangling-connector sensitivity):**\\n- Simple tasks (Object): even entangling connectors tolerate mild pruning (X-VLA k=0.9=97.6%)\\n- Complex tasks (Goal/Long): entangling connectors collapse (X-VLA Goal k=0.9=70.2%, Long k=0.95≈53%)\\n- Key: same connector, same k, same method — **only task differs** → 27.8pp drop (Object→Goal)\\n\\n**CV predicts Axis-1 position**: 0.038 (most independent) → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 (most entangled)\\n\\n**Evidence**: 5 models, 3 connector families, 4 LIBERO suites, 4 model sizes (450M-7B). Key controlled comparisons:\\n1. π0 (256 tokens, linear) k=0.1 = 0.976 vs OpenVLA (256 tokens, MLP) k=0.1 = 1.608 → connector isolates base sensitivity\\n2. X-VLA Object k=0.9 = 97.6% vs X-VLA Goal k=0.9 = 70.2% → task complexity isolates amplification\\n3. SmolVLA Object = 0% at k=0.95 → extreme entanglement dominates even on simple tasks\\n\\n🔴 **D108→D127→D130→D132: Pruning method comparison — MAJOR REVERSAL at aggressive compression**\\n\\nBoth L2 norm and random pruning tested on X-VLA and OpenVLA. **CV predicts not just tolerance but optimal strategy**:\\n\\n- **OpenVLA (MLP, CV=0.215)**: L2 norm consistently ≥ random at all k values. High CV → meaningful importance differentiation → L2 norm selection effective.\\n  - k=0.95: L2norm=69.4% ≈ random=69.2% (+0.2pp)\\n  - k=0.7: L2norm=49.8%¹ > random=44.4% (+5.4pp). ¹seed43 only, seed42 running on westd-38929:2\\n  - k=0.5: L2norm=39.2% > random=35.8% (+3.4pp)\\n  - k=0.3: L2norm=25.0%, random=pending (re-running)\\n\\n- **X-VLA (BART, CV=0.151)**: 🔴 **REVERSAL** — L2 norm ≈ random at mild compression, but **random MASSIVELY outperforms L2 norm at aggressive compression**:\\n  - k=0.9: L2norm=97.6% ≈ random=97.8% (≈0pp)\\n  - k=0.85: L2norm=68.0% > random=63.6% (+4.4pp, cliff boundary)\\n  - k=0.8: L2norm=89.0% ≈ random=89.4% (≈0pp, non-monotonic recovery)\\n  - **k=0.5: L2norm=42.6% << random=70.6% (-28.0pp!)** — CI non-overlapping, statistically significant. Random wins 9/10 tasks; T4 ketchup: L2norm=42% vs random=100% (+58pp). Only T6 butter both crash at 2%.\\n  - k=0.7: L2norm=56.2% << random=65.2% (+9pp). Crossover confirmed at k≈0.8.\\n  - **k=0.3: L2norm=22.8% << random=62.8% (+40pp!)** — gap scales monotonically with compression.\\n  - **D137**: seed43 k=0.5=71.0% confirms seed42=70.6% (Δ=0.4pp). Gap reproducible.\\n\\n- **SmolVLA**: all methods = 0% at all k values → trivially method independent.\\n\\n**KEY INSIGHT (D132→D137)**: Importance-based pruning can be **actively harmful** on low-CV architectures under aggressive compression, and the harm SCALES: +9pp@k=0.7, +28pp@k=0.5, +40pp@k=0.3. Mechanism: X-VLA's linear projection + BART encoder produces relatively uniform token norms (CV=0.151). L2 norm selection on a near-uniform distribution degenerates into selecting spatially clustered tokens → loses diversity → catastrophic failure. Random pruning preserves spatial coverage → dramatically better. Multi-seed confirmed.\\n\\n**This strengthens the paper**: CV serves as a dual predictor — predicts both (1) pruning tolerance ceiling and (2) whether importance-based methods help or hurt. Connector architecture determines both via its effect on token importance distribution.\\n\\n**Paper narrative upgrade**: From \\\"connector determines compressibility\\\" to \\\"connector determines both compressibility AND optimal compression strategy.\\\" This is a significantly stronger and more novel contribution.\\n\\n**Pending data**: X-VLA random k=0.7 (crossover characterization), multi-seed k=0.5 random (robustness). OpenVLA L2norm k_ratio=null provenance issue needs fixing.\\n\\n### Claim 2: Pixel Shuffle Creates Irreversible Token Entanglement\\nSmolVLA's pixel_shuffle connector spatially folds 1024 SigLIP patches into 64 tokens per camera (16x compression). Each resulting token encodes a 32x32 pixel region via channel-to-spatial reorganization. This creates extreme cross-token spatial entanglement: removing any single token eliminates an entire spatial quadrant's information with no redundancy to compensate.\\n\\n**Evidence**:\\n- k=0.95 (remove only 7/128 tokens = 5.5%) = 0% SR — even minimal removal is catastrophic\\n- k=0.9 (remove 13/128 tokens) = 0% SR\\n- Geometric prior (Sobel edge) k=0.5/0.7/0.9 = all 0%\\n- Attention entropy ratio 0.952 (near-uniform, TV=0.05)\\n- Official checkpoint Object (59.2% baseline) cliff-edge at k=0.5 → 0%\\n- Official checkpoint Spatial (43.8% baseline) cliff-edge at k=0.5 → 0.6% (3/500, CI [0.2%, 1.7%])\\n\\n### Claim 3a: Linear Projection → Depends on Effective Pipeline (D107: RESOLVED)\\nPure linear projection (π0): immune. Linear projection + deep post-processing (X-VLA, BART 12L): \\\"robust-then-cliff\\\" — immune at k≥0.9, cliff at k=0.7, then graded degradation. The BART encoder introduces non-linear cross-token mixing that explains intermediate CV=0.151 and the cliff pattern.\\n\\n**Evidence** (X-VLA LIBERO SR — Batch 1 + Batch 2 COMPLETE, full 8-point curve):\\n- k=1.0: **99.2%** (baseline, 496/500) — per-task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]\\n- k=0.95: **99.0%** (-0.2pp) — per-task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]\\n- k=0.9: **97.6%** (-1.6pp) — per-task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]\\n- k=0.7: **56.2%** (-43pp, CLIFF — 281/500) — per-task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]\\n- k=0.5: **42.6%** (-57pp) — Batch 2 confirmed (MSH fix applied)\\n- k=0.3: **23.0%** (-77pp) — graded degradation continues below cliff\\n- k=0.2: **~4.0%** (-96pp) — near-zero\\n- k=0.1: **~0.0%** (-100pp) — complete failure\\n✅ Full curve confirms threshold-graded pattern: immune k≥0.9, cliff at k=0.7, then graded degradation k≤0.5 (42.6%→23.0%→~4%→~0%).\\n\\n**Cliff localization (D114, D117: 3-seed deterministic, L2norm)**:\\n- k=0.80: **89.0% ± 0.72pp** (seeds: 88.8/88.4/89.8)\\n- k=0.85: **67.9% ± 0.31pp** (seeds: 68.0/67.6/68.2 — T4=26%, T6=0% across ALL 3 seeds)\\n- Non-monotonic: k=0.85 < k=0.80 by **21.1pp**. BART encoder creates length-dependent interactions near critical token density. SD < 1pp confirms fully deterministic, not stochastic.\\n\\n**Random pruning comparison (D127-D130, D132 REVERSAL)**:\\n- k=0.9: random=97.8% ≈ L2norm=97.6% → method independent at mild compression\\n- k=0.85: random=63.6% vs L2norm=68.0% (+4.4pp for L2norm at cliff boundary). Both crash on same tasks (T1, T4, T6, T8) → cliff is architectural.\\n- k=0.8: random=89.4% ≈ L2norm=89.0% → method independent, non-monotonic recovery confirmed in both\\n- 🔴 **k=0.5: random=70.6% >> L2norm=42.6% (+28pp REVERSAL, CI non-overlapping)**. Per-task random: [96, 46, 100, 92, 100, 94, 2, 82, 42, 100]. Random wins 9/10 tasks; L2norm actively harmful. T4: random=100% vs L2norm=42% (+58pp).\\n- k=0.7: random=65.2% vs L2norm=56.2% (+9pp random). Crossover confirmed at k≈0.8.\\n- 🔴 **k=0.3: random=62.8% vs L2norm=22.8% (+40pp!)** — gap SCALES with compression: +9@k=0.7, +28@k=0.5, +40@k=0.3.\\n- **D137 multi-seed confirmed**: seed43 k=0.5=71.0% (seed42=70.6%, Δ=0.4pp). Gap is reproducible.\\n- **Random non-monotonicity confirmed**: k=0.5 (70.6%) > k=0.7 (65.2%) > k=0.3 (62.8%). seed43 reproduces (71.0%). L2norm monotonically decreasing (42.6% > 22.8%). Random's k=0.5 \\\"sweet spot\\\" may reflect optimal diversity-coverage tradeoff: enough tokens removed to break BART clustering, but enough retained for spatial coverage.\\n- k=0.85 per-task (random): [100, 10, 100, 94, 24, 92, 0, 94, 22, 100] = 63.6%.\\n- **Non-monotonicity confirmed in both methods**: k=0.85 (42 tokens) cliff vs k=0.8 (40 tokens) recovery. 2-token difference, 21-26pp gap.\\n- **D132 KEY INSIGHT**: At aggressive compression (k=0.5), L2 norm is catastrophically worse than random for X-VLA. Low CV=0.151 → near-uniform importance → L2 norm degenerates into spatially clustered selection → loses diversity. This is the opposite of OpenVLA (CV=0.215) where L2 norm helps. **CV predicts optimal pruning strategy, not just tolerance.**\\n\\n**Cross-suite generalization (D117, updated with full results)**:\\n- X-VLA Spatial baseline: **91.6%** [88.8%, 93.7%] (500 eps, T5=48% is hardest task)\\n- X-VLA Goal baseline: **98.0%** [96.4%, 98.9%] (500 eps, all tasks ≥92%)\\n- X-VLA-Libero checkpoint covers all 4 suites without suite-specific fine-tuning.\\n\\n**⚠️ Cross-suite pruning sensitivity (key finding — potential new contribution)**:\\n\\nX-VLA pruning curve comparison across suites:\\n\\n| Suite | k=1.0 | k=0.9 | k=0.85 (L2/Rand) | k=0.8 (L2/Rand) | k=0.7 (L2/Rand) | k=0.5 (L2/Rand) |\\n|-------|-------|-------|-----|-------|----------|----------|\\n| Object | 99.2% | 97.8% | 68.0/63.6% | 89.0/89.4% | 56.2/65.2% | 42.6/**70.6%** |\\n| Spatial | 91.6% | 79.0% | 66.6/67.6% | — | — | 58.8%/**71.4%** |\\n| Goal | 98.0% | 70.2% | — | — | — | 61.0%/— |\\n\\n**Goal suite FINAL results (10/10 tasks, D123: suite-level monotonic confirmed)**:\\n- k=0.9: **70.2%** (351/500) — much larger drop than Object (-1.4pp) despite similar baseline\\n- k=0.5: **61.0%** (305/500) — suite-level monotonic (k=0.9 > k=0.5), D123 retracted earlier partial-data non-monotonic claim\\n\\n**Per-task non-monotonic pruning remains valid (selected tasks)**:\\n\\n| Task | k=1.0 | k=0.9 | k=0.5 | Pattern |\\n|------|-------|-------|-------|---------|\\n| T0 open drawer | 100% | 100% | 82% | monotonic ↓ |\\n| T2 close drawer | 94% | 96% | **100%** | **pruning improves** |\\n| T3 open+put (multi-step) | 100% | **6%** | **40%** | catastrophic + non-monotonic (k=0.5 > k=0.9) |\\n| T8 | — | — | — | +46pp non-monotonic (k=0.5 > k=0.9) |\\n| T9 | 98% | — | ~0% | catastrophic collapse (-98pp) |\\n\\n- Suite-level: Goal k=0.5=61.0% > Spatial k=0.5=58.8% — Goal slightly more robust, but both moderate degradation\\n- Per-task: T3/T8 show non-monotonicity (k=0.5 > k=0.9), T9 catastrophic collapse. These are genuine misalignments between global L2-norm ranking and task-specific token utility.\\n- T2 pruning improvement: consistent with π0 finding — simple tasks benefit from token noise removal\\n\\n**Key cross-suite finding**: Goal k=0.9 drops **27.8pp** (vs Object -1.4pp). Same connector, same pruning method, different task distribution → **task complexity amplifies pruning sensitivity**. Goal tasks involve multi-step reasoning that depends heavily on precise spatial tokens.\\n\\n**Task-level analysis (Spatial, k=0.5 vs baseline)**:\\n- Robust (Δ≤10pp): T0 \\\"between plate and ramekin\\\" (-4pp), T4 \\\"in top drawer\\\" (-2pp) — global spatial / unambiguous target\\n- Moderate (Δ 10-30pp): T2(-10), T3(-24), T6(-22), T8(-18) — mild spatial precision needed\\n- Catastrophic (Δ>40pp): T5 \\\"on ramekin\\\" (-48pp, 0%), T9 \\\"on cabinet\\\" (-58pp), T7 \\\"on stove\\\" (-64pp), T1 \\\"next to ramekin\\\" (-78pp)\\n- **T1 has 100% baseline but 22% at k=0.5** — high baseline ≠ pruning robustness\\n\\n**Mechanism**: Goal tasks are semantically diverse (different verbs/objects) → language instruction alone disambiguates → vision tokens are redundant for task selection. Spatial tasks are semantically near-identical (all \\\"pick bowl...\\\") → disambiguation relies entirely on spatial vision tokens → pruning destroys the only discriminative signal.\\n\\n**Paper framing upgrade (Reviewer suggestion, agreed)**:\\n- From \\\"connector determines pruning tolerance\\\" → \\\"pruning sensitivity = f(connector_type, task_semantics)\\\"\\n- Connector CV predicts degradation *class* (immune/threshold/graded/catastrophic)\\n- Task semantic structure determines degradation *severity* within that class\\n- When language disambiguates: aggressive pruning is safe (Goal k=0.5 ≈ baseline)\\n- When spatial vision disambiguates: even conservative pruning degrades (Spatial k=0.9 -12.6pp)\\n- **Potential new contribution**: first task-level pruning sensitivity analysis in VLAs. §4.6 should include per-task heatmap + the language-vs-spatial disambiguation framework.\\n\\nπ0 evidence:\\n- π0 (3.3B, 256 tokens, pure linear proj): k=0.1 normalized_L1 = 0.976 (-2.4% = improvement), k=0.5 = 0.983\\n- Attention entropy: π0 suffix-to-vision mean 0.959 (near-uniform across 18 layers, range [0.931, 0.983])\\n- Importance CV: π0 = 0.038 (lowest in spectrum)\\n\\n**Key insight**: \\\"Linear projection\\\" is NOT sufficient for immunity. The effective pipeline matters. X-VLA's BART encoder (12 transformer layers after linear proj) introduces partial dependencies → CV=0.151 → cliff at k=0.7. π0's pure linear proj → CV=0.038 → immune even at k=0.1.\\n\\n### Claim 3b: MLP Projector → Graded Degradation\\nMulti-layer MLP connectors create partial token dependencies through non-linear mixing, enabling graceful but real degradation.\\n\\n**Evidence** (OpenVLA 6-point degradation curve):\\n- k=1.0: 74.0% (baseline)\\n- k=0.95: 69.4% (-6% relative)\\n- k=0.9: 62.0% (-16% relative)\\n- k=0.7: 49.0% (-34% relative)\\n- k=0.5: 37.4% (-49% relative)\\n- k=0.3: 20.6% (-72% relative)\\n- Entropy ratio 0.639 (progressive sharpening L0=0.98→L29=0.48, TV=0.50)\\n- **Method independence confirmed**: random k=0.95=69.2% ≈ L2norm k=0.95=69.4%; random k=0.5=35.8% ≈ L2norm k=0.5=37.4%. For MLP projectors, pruning method doesn't matter.\\n- OFT (same connector, different action head): entropy 0.667 ≈ Standard 0.661 → connector determines attention structure, not action head\\n- CogACT (MLP projector, literature): 74.8% → 74.2% under 78% pruning (EfficientVLA)\\n\\n### Claim 4: Learned Re-Encoding Achieves Near-Lossless Compression Where Deletion Fails (D072+MLP confirmed → upgraded to METHOD per D091)\\n**⚠️ Baseline correction (2026-05-22): SmolVLA Object baseline = 59.2% (official HF checkpoint), NOT 44.8% (old reproduced). VTR narrative reframed from \\\"re-encoding boost\\\" to \\\"near-lossless compression recovery\\\".**\\n\\nTwo independent re-encoding architectures (~22M params each) validate that **any learned re-encoding** can recover entangled pixel_shuffle tokens from 0% (hard pruning) to near-baseline levels. Cross-attention (60.1±1.3%, 3-seed) and MLP adapter (63.4±2.6%, 3-seed) both achieve this recovery, with p≈0.15 confirming no significant difference between architectures. M=128 passthrough (58.0±3.5%, 3-seed) ≈ baseline 59.2% (-1.2pp), confirming VTR recovers to baseline rather than exceeding it. **M-curve is flat**: M=16 (56.9%) through M=128 (58.0%), all within ±3pp of baseline 59.2% — VTR achieves near-lossless compression at ANY ratio (0-87.5%) for pixel-shuffle connectors. M=64 achieves best absolute SR at 62.0±2.3% (+2.8pp over baseline) with 50% compression. Cross-suite generalization confirmed: M=32 recovers to 53.2% on Spatial (vs 0.6% pruning cliff-edge) and 56.4% on Goal. M=96 dip statistically confirmed (p=0.034 vs M=64).\\n\\n**D109 C4-ext on OpenVLA (MLP projector)**: M=128 VTR at 20K steps = **0% SR** (severe overfitting, model outputs identical action every step). This suggests VTR's effectiveness is connector-dependent: pixel-shuffle benefits enormously (0%→~59% ≈ baseline) because re-encoding repairs spatial entanglement, while MLP projector tokens are already individually meaningful and VTR adds unnecessary complexity. VTC-only M=32/M=64 training in progress — if these also fail, VTR is specifically a pixel-shuffle solution, which strengthens the architecture-dependency narrative.\\n\\n**Evidence** (all confirmed):\\n\\nCross-attention re-encoding (M sweep, 3-seed where available):\\n| M | Compression | SR (3-seed mean±std) | Seeds | Notes |\\n|---|------------|-----|-----|-----|\\n| 16 | 87.5% | **56.9±1.3%** | 42/43/44 | ✅ ZERO loss vs M=128 |\\n| 32 | 75% | **60.1±1.3%** | 42/43/44 | ✅ |\\n| 64 | 50% | **62.0±2.3%** | 42/43/44 | ✅ best tradeoff |\\n| 96 | 25% | 54.5±3.2% | 42/43/44 | ✅ highest variance |\\n| 128 | 0% (passthrough) | **58.0±3.5%** | 42/43/44 | ✅ passthrough control |\\n\\nMLP adapter control (M=32, ~22.14M params, 3-seed):\\n| Architecture | Params | M | Mean SR (3-seed) | Std | Individual seeds |\\n|---|---|---|-----|-----|-----|\\n| Cross-attention (VTC) | 22.2M | 32 | **60.1%** | ±1.3 | 61.6 / 59.2 / 59.6 |\\n| **MLP adapter** | **22.14M** | **32** | **63.4%** | **±2.6** | **65.2 / 64.6 / 60.4** |\\n\\nTwo-sample t-test: t≈1.94, p≈0.15 → **no significant difference** (α=0.05). Both >> 0% (hard pruning) and ≈ 59.2% (baseline). MLP ≥ VTC in all 3 seeds but difference not statistically significant — confirms any re-encoding architecture recovers to near-baseline, not a specific mechanism. (Note: M=32 seed43 corrected from 62.4% to 59.2% per registry verification; 62.4% was M=96 seed43 CI upper bound misattributed.)\\n\\n### Claim 5: CV Predicts Optimal Pruning Strategy — Monotonic Diagnostic Trend (D132→D139→D140→D142)\\nToken importance CV determines **which pruning method to use**, with the L2norm-vs-random gap scaling monotonically with CV. **Validated at TWO k values (D142):**\\n\\n**k=0.5 (main table):**\\n| Model | CV | Tokens | L2norm k=0.5 | Random k=0.5 | Δ (R-L2) |\\n|-------|-----|--------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | **33.4%** | **69.4%** | **+36.0pp** |\\n| X-VLA | 0.151 | 50 | 43.4%³ | 70.3%⁴ | +26.9pp |\\n| OpenVLA | 0.215 | 256 | 39.2% | 37.4%¹⁰ | -1.8pp |\\n\\n**k=0.7 (second validation, D142):**\\n| Model | CV | Tokens | L2norm k=0.7 | Random k=0.7 | Δ (R-L2) |\\n|-------|-----|--------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | **55.0%** | **77.2%** | **+22.2pp** |\\n| X-VLA | 0.151 | 50 | 58.6%⁶ | 65.1%⁷ | +6.5pp |\\n| OpenVLA | 0.215 | 256 | 49.8% | 44.4% | -5.4pp |\\n⁶ X-VLA L2norm k=0.7 2-seed: 58.2/59.0, mean=58.6%, σ=0.4pp (seed44 pending → tri-seed)\\n⁷ X-VLA random k=0.7 2-seed: 65.2/65.0, mean=65.1%, σ=0.1pp (seed44 running)\\n\\n³ X-VLA L2norm k=0.5 3-seed mean: 42.6/43.4/44.2, mean=43.4%, range 1.6pp\\n⁴ X-VLA random k=0.5 3-seed mean: 70.6/71.0/69.2, mean=70.3%, σ=0.9pp\\n\\n¹⁰ OpenVLA random k=0.5 = 37.4% (seed7). Table 3 previously showed 35.8% (unverified source). seed42 running on westd-38929, will replace when available.\\n\\n✅ **D139+D142 CONFIRMED**: Monotonic trend validated at BOTH k=0.5 (-1.8→+26.9→+36.0) and k=0.7 (-5.4→+6.5→+22.2). Same monotonic pattern. Paper: k=0.5 as main table, k=0.7 as confirmatory second row or separate table.\\n\\n**D140: k=0.3 interaction — method preference REVERSES at extreme compression for π0.5:**\\n\\n| Model | CV | Tokens | k=0.3 kept | L2norm k=0.3 | Random k=0.3 | Δ (R-L2) |\\n|-------|-----|--------|-----------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | 230 | **51.0%** | 36.4% | **-14.6pp** |\\n| X-VLA | 0.151 | 50 | 15 | 22.2%⁸ | **64.5%⁹** | **+42.3pp** |\\n| OpenVLA | 0.215 | 256 | 77 | 25.0% | **21.4%** | **+3.6pp** |\\n\\n⁸ X-VLA L2norm k=0.3 3-seed: 22.2/21.0/22.8 (from D137), mean=22.0%; seed43 running on cqa1\\n⁹ X-VLA random k=0.3 2-seed: 62.8/66.2, mean=64.5%, σ=2.4pp; seed44 running on cqa1\\n\\nAt k=0.3, π0.5 L2norm wins (+14.6pp) while X-VLA random still wins massively (+42.3pp). OpenVLA L2norm also wins (+3.6pp). The pattern: at k=0.3, both high-CV (OpenVLA) and low-CV-with-large-budget (π0.5, 230 tokens) favor L2norm, while mid-CV-with-small-budget (X-VLA, 15 tokens) strongly favors random. Strategy preference is f(CV, k, absolute_token_budget).\\n\\n**OpenVLA (CV=0.215) full seed42 Δ(L2-R) pattern**: +1.4pp (k=0.95) → +5.4pp (k=0.7) → pending (k=0.5) → +3.6pp (k=0.3). L2norm consistently better at ALL k values — high CV enables meaningful importance-based selection. Peak advantage at k=0.7, not monotonically increasing with compression.\\n\\n**D141: π0.5 L2norm complete curve — valley at k=0.5 confirmed (multi-seed)**:\\n| k | L2norm SR (s42) | L2norm SR (s43) | Random SR | Δ (R-L2) s42 |\\n|---|-----------------|-----------------|-----------|---------------|\\n| 0.7 | **55.0%** | **57.8%**¹⁰ | **77.2%** / **73.8%** (mean=75.5%) | +22.2pp (s42) / +19.8pp (mean) |\\n| 0.5 | **33.4%** | **33.6%** ✅ | **69.4%** / **68.4%** (mean=68.9%) | +36.0pp (s42) / +35.4pp (mean) |\\n| 0.3 | **51.0%** | **55.4%** ✅ | 36.4% | -14.6pp |\\n\\n¹⁰ Agent audit reported 56.4% for L2norm k=0.7 seed43 vs earlier worker result 57.8%. Needs reconciliation. Pattern unchanged.\\n\\n**V-shape fully confirmed (2 seeds, both methods)**:\\n- **Valley (k=0.5)**: L2norm 33.4/33.6% (std=0.1pp); Random 69.4/68.4% (std=0.7pp) — both methods stable\\n- **2-seed means**: L2norm k=0.7=56.4%, k=0.5=33.5%, k=0.3=53.2%; Random k=0.7=75.5%, k=0.5=68.9%\\n- **V-depth**: seed42=17.6pp, seed43=21.8pp (seed43 deeper because endpoints higher)\\n- **Δ(R-L2) dual-seed means**: k=0.7=+19.8pp, k=0.5=+35.4pp — monotonic trend holds with multi-seed\\n- seed43 consistently +2-4pp above seed42 but identical shape. Valley position/depth is architectural determinism.\\n\\n**Mechanism confirmed by token position visualization (D141)**:\\n- k=0.7: 2 clusters, 97% in largest, **100% spatial coverage** — enough tokens to maintain coverage\\n- k=0.5: **1 cluster, 100% in single region, 78% coverage** — worst-case spatial concentration\\n- k=0.3: **3 clusters**, 86% in largest, 78% coverage — cluster breaks apart, better diversity\\n\\nThe non-monotonicity arises because k=0.5 sits at the worst point of the spatial correlation structure: L2norm selects exactly the number of tokens that maximizes spatial clustering. At k=0.7 there are enough tokens for coverage; at k=0.3 the selection threshold crosses a boundary that fragments the cluster. Per-task variance is extreme at k=0.7 (T1=94%, T5=98% vs T7=0%) — L2norm deterministic selection can catastrophically miss specific task-critical spatial regions.\\n\\n**Paper strategy**: k=0.5 as **main table** (cleanest monotonic trend, clear gap). Full L2norm curve as **figure** showing pathological valley — strong evidence for spatial clustering mechanism. k=0.3 reversal as supplementary. Key message: \\\"CV predicts method preference at k=0.5; L2norm's spatial clustering creates pathological non-monotonicity unique to low-CV models.\\\"\\n\\n**Notable asymmetry**: Random tolerance is similar for low/medium CV at k=0.5 (π0.5=69.4% ≈ X-VLA=70.6%), while L2norm harm increases dramatically (π0.5=33.4% < X-VLA=43.4%). High CV (OpenVLA=35.8% random) is less random-tolerant because tokens have genuine importance differentiation that random discards.\\n\\n**Evidence** (Reviewer-verified, D132 PASS):\\n\\nX-VLA vs OpenVLA full comparison:\\n\\n| k | X-VLA (CV=0.151) | | OpenVLA (CV=0.215) | |\\n|---|---|---|---|---|\\n| | L2norm | Random | L2norm | Random |\\n| 0.95 | — | — | 70.6% | 69.2% (+1.4 L2norm) |\\n| 0.9 | 97.6% | 97.8% (≈0) | 70.6% | 64.6% (+6.0 L2norm) |\\n| 0.85 | 68.0% | 63.6% (+4.4 L2norm) | — | — |\\n| 0.8 | 89.0% | 89.4% (≈0) | — | — |\\n| 0.7 | 56.2% | **65.2% (+9pp random)** | 49.8%¹ | 44.4% (+5.4 L2norm¹) |\\n| 0.5 | **42.6%** | **70.6% (+28pp random!)** | 39.2% | 35.8% (+3.4 L2norm) |\\n| 0.3 | **22.8%** | **62.8% (+40pp random!)** | 25.0% | pending² |\\n\\n¹ OpenVLA L2norm k=0.7 = seed43 only, random = seed42; cross-seed caveat. seed42 L2norm k=0.7 running on westd-38929.\\n² OpenVLA random k=0.3 result file missing, re-running on westd-38929.\\n³ D137 multi-seed: X-VLA random k=0.5 seed43=71.0% (seed42=70.6%, Δ=0.4pp). Gap reproducible.\\n\\n**Per-task X-VLA k=0.5 (Reviewer-verified, 9/10 tasks random > L2norm):**\\n\\n| Task | Baseline | L2 s42 | L2 s43 | Random s42 | Δ(R-L2) |\\n|------|---------|--------|--------|------------|---------|\\n| T0 alphabet_soup | 98% | 58% | 56% | **96%** | +38 |\\n| T1 cream_cheese | 100% | 2% | 6% | 46% | +44 |\\n| T4 ketchup | 100% | 42% | 40% | **100%** | **+58** |\\n| T7 milk | 100% | 38% | 38% | 82% | +44 |\\n| T9 orange_juice | 100% | 68% | 70% | **100%** | +32 |\\n| T6 butter | 100% | 2% | 2% | 2% | 0 (both crash) |\\n\\nL2norm two seeds highly consistent (s42 vs s43 diff <6pp) → not RNG noise.\\nT6: baseline=100% but both methods=2% → highly localized visual cue, k=0.5 always loses it regardless of method.\\nT4/T9: Random recovers to baseline → L2norm systematically discards the critical tokens for these tasks.\\n\\n**Pattern**: Low CV (X-VLA) → importance-based selection degenerates at aggressive k → random better. High CV (OpenVLA) → meaningful importance differentiation → L2 norm better.\\n\\n**Mechanism hypothesis** (Reviewer: consistent with data, needs direct evidence): X-VLA's linear projection + BART encoder produces tokens with relatively uniform L2 norms (CV=0.151). At aggressive compression (k=0.5 = keeping 25 of 50 tokens), L2 norm selects the \\\"slightly larger\\\" tokens which tend to be spatially clustered → loses spatial diversity → catastrophic. Random preserves spatial coverage stochastically → dramatically better.\\n\\n**⚠️ Visualization needed (Reviewer warning)**: Must produce token position visualization — for same input image, show which tokens L2 norm vs random retains. If L2 norm shows spatial clustering, mechanism is proven. This should be a key figure (§4.6 or Fig 4).\\n\\n**Implication for practitioners**: CV diagnoses → predicts tolerance → prescribes strategy at aggressive compression. Low CV + aggressive k (≤0.5) → random/position-based. High CV → importance-based at all k. Mild compression (k≥0.8) → method choice doesn't matter regardless of CV.\\n\\n**Pending**: X-VLA random k=0.7 (crossover), multi-seed k=0.5, token position visualization, OpenVLA L2norm k=0.7 seed42, k_ratio=null fix.\\n\\n## Story Spine\\n\\n**Problem**: Vision token efficiency is critical for real-time VLA deployment. Growing literature proposes inference-time token reduction (FastV, VLA-IAP, H2O, ToMe). These methods succeed on some VLAs but their behavior across different architectures is unstudied.\\n\\n**Gap**: No work has systematically compared token pruning robustness across VLA architectures. The implicit assumption that \\\"token pruning works or fails uniformly\\\" is untested. The critical architectural factor determining prunability is unknown.\\n\\n**Discovery**: We find that VLA token pruning robustness is governed by two interacting axes. **Axis 1 — Token Coupling**: connector architecture determines whether tokens are independent (linear proj, MLP) or entangled (BART encoder, pixel-shuffle), diagnosed by importance CV (0.038→0.314). **Axis 2 — Task Complexity**: multi-step tasks (Goal/Long) amplify pruning damage on entangling connectors — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at k=0.9. Evidence from 5 VLA models × 4 LIBERO suites:\\n- **Token-independent** (π0, π0.5 linear; OpenVLA, OFT MLP): graded degradation, CV 0.038–0.219\\n- **Token-entangling** (X-VLA BART 12L; SmolVLA pixel-shuffle): task-dependent collapse — tolerate simple tasks, catastrophic on complex tasks. CV 0.151–0.314\\nCV predicts both pruning tolerance and optimal strategy (L2norm hurts low-CV models, helps high-CV).\\n\\n**Solution**: Diagnose-then-Compress framework. Step 1: Token importance CV provides zero-cost diagnostic for pruning tolerance (one forward pass). Step 2: VTR (Vision Token Re-encoding) provides universal compression. For pixel-shuffle: recovers from 0% (hard pruning) to ~59% ≈ baseline (59.2%), M-curve flat (D105: M=16 56.9% ≈ M=128 58.0%, near-lossless at any compression ratio). For MLP projector: D109 C4-ext = 0% SR (overfitting at M=128); VTC-only M=32/M=64 in progress.\\n\\n**Headline result**: \\\"Across 5 VLA models (450M-7B) × 4 task suites, we find that token pruning robustness is governed by two axes: connector architecture (token-independent vs token-entangling, diagnosed by importance CV) and task complexity. Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio; SmolVLA collapses to 0% at 5% removal regardless of task. CV (0.038→0.314) predicts both pruning tolerance and optimal strategy: importance-based pruning is actively harmful on low-CV architectures (+28-36pp gap favoring random), while it helps on high-CV models (+1-6pp). VTR recovers to ~59% (≈baseline) at any compression ratio (0-87.5%) where hard deletion achieves 0%.\\\"\\n\\n## Paper Structure (7-model version)\\n\\n1. **Introduction**: VLA efficiency motivation → diverse connector architectures → 2-axis framework discovery (D171) → Diagnose-then-Compress framework\\n2. **Background**: 5 VLA models, 3 connector families (linear/MLP/pixel-shuffle), 4 LIBERO suites, token flow analysis\\n3. **Experimental Setup**: 5 models, LIBERO benchmark (4 suites: Object/Spatial/Goal/Long), pruning protocol, VTR compression, diagnostic metrics\\n4. **Main Results**:\\n   - §4.1: 2-Axis Framework Overview (Table 1: 5 models × token coupling axis; Table 2: cross-suite interaction — connector × task complexity)\\n   - §4.2: Token-Entangling Catastrophic — pixel-shuffle cliff-edge (SmolVLA, all configs 0% regardless of task)\\n   - §4.3: Token-Independent Graded — MLP degradation (OpenVLA 6-point curve + OFT entropy confirmation)\\n   - §4.4: Token-Independent Tolerant — linear projection (π0 + π0.5, controlled comparison with OpenVLA)\\n   - §4.5: Task Complexity Amplification — X-VLA cross-suite (Object 97.6% vs Goal 70.2% vs Long ~53% at same k)\\n   - §4.6: Pruning Strategy Depends on CV (D132: low-CV random>>L2norm, high-CV L2norm>>random)\\n   - §4.7: VTR overcomes cliff-edge (M-curve flat + architecture independence)\\n   - (REMOVED — D119: LIBERO-Plus L1 SR=3.3% floor effect, noted in Discussion §6)\\n5. **Analysis**:\\n   - §5.1: Why pixel_shuffle creates entanglement (spatial folding + controlled comparison)\\n   - §5.2: Diagnostic metric — Entropy + CV composite (D104, 4-model validation)\\n   - §5.3: Re-encoding mechanism (M=128 passthrough + MLP adapter + M-curve flat D105)\\n6. **Discussion**: Design implications, limitations (sim-only, no real robot), future work\\n7. **Conclusion**: 5 claims summary\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Only 2 models → **FULLY ADDRESSED**\\n**Response**: Now 5 models (SmolVLA, OpenVLA, OpenVLA-OFT, π0, X-VLA) across 3 connector families (pixel-shuffle, 3-layer MLP, linear projection) and 4 model sizes (450M-7B). Each connector class has ≥2 models.\\n\\n### RC2: Model size confound (450M vs 7B) → **FULLY ADDRESSED**\\n**Response**: π0 (3.3B, linear) is pruning-immune while OpenVLA (7B, MLP) degrades 61% at k=0.1. Larger model is MORE vulnerable, not less — directly falsifies \\\"larger models are more robust\\\" hypothesis. X-VLA (880M, linear) also immune, matching π0 behavior despite 4× smaller. Size is not the explanatory variable; connector type is.\\n\\n### RC3: Why not test SmolVLA without pixel_shuffle?\\n**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.\\n\\n### RC4: Smart compression — is re-encoding or compression the mechanism?\\n**Response (corrected with baseline=59.2%)**: VTR achieves near-lossless compression at any ratio — the M-curve is flat (M=16: 56.9% → M=128: 58.0%, all within ±3pp of baseline 59.2%). Two lines of evidence: (1) M=128 passthrough (58.0%) ≈ baseline (59.2%) — re-encoding recovers spatial entanglement to baseline level, not above it. (2) Architecture control: MLP adapter (63.4%) ≈ cross-attention (60.1%) with CI overlap — any re-encoding mechanism works. The key contribution is recovery from 0% (hard pruning) to ~59% (baseline), not exceeding baseline. Compression ratio is a free parameter with negligible SR cost.\\n\\n### RC5: Relationship to VLA-IAP\\n**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.\\n\\n### RC6: Is this just \\\"different models behave differently\\\"?\\n**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.\\n\\n### RC7: Only one benchmark (LIBERO-Object) → **ADDRESSING (D115, D119)**\\n**Response**: Expanded to ALL 4 LIBERO suites (Object/Spatial/Goal/Long) — 4 genuinely different task distributions (manipulation skills, spatial reasoning, goal-conditioned, long-horizon). Taxonomy consistency validated across suites. LIBERO-Plus robustness benchmark tested (D119) but abandoned: L1 camera perturbation collapses OpenVLA to SR=3.3% (consistent with leaderboard 0.8%), creating floor effect with no room for pruning analysis. This floor effect itself is noted in Discussion as evidence of general VLA brittleness under distribution shift. Sim-only limitation acknowledged.\\n\\n## All Experimental Evidence (confirmed)\\n\\n### SmolVLA Cliff-Edge\\n- Fine-tuned baseline (Object): 44.8% (224/500) — ⚠️ OLD reproduced checkpoint, superseded by official HF = 59.2%\\n- 6 pruning conditions (random/ACIS/ToMe × k=0.5/0.7/0.9): all 0%\\n- Geometric prior (Sobel) k=0.5/0.7/0.9: all 0%\\n- Attention entropy: 0.952 (flat, TV=0.05)\\n- Official checkpoint Object: 59.2% → 0% at k=0.5\\n- Official checkpoint Spatial: 43.8% → 0.6% (3/500, CI [0.2%, 1.7%]) at k=0.5 — near-zero, confirms cliff-edge across suites\\n- LoRA-FT checkpoint Spatial: 8.0% (per-task: [24,8,4,24,0,2,2,2,14,0]) — LoRA trained on Object only, does not transfer to Spatial. Use official checkpoint for cross-suite SmolVLA analysis.\\n\\n### OpenVLA Degradation Curve\\n- k=1.0: 74.0% (370/500)\\n- k=0.95: 69.4% (-6% relative)\\n- k=0.9: 62.0% (-16% relative)\\n- k=0.7: 49.0% (245/500, -34% relative)\\n- k=0.5: 37.4% (187/500, -49% relative)\\n- k=0.3: 20.6% (103/500, -72% relative)\\n- Entropy: 0.639 (progressive sharpening, TV=0.50)\\n\\n### Cross-Model Pruning Taxonomy (7 models — D100, D120, D127)\\n| Model | Connector | Tokens | k=0.1 norm_L1 | k=0.5 norm_L1 | Class |\\n|-------|-----------|--------|---------------|---------------|-------|\\n| π0 (3.3B) | Pure linear proj | 256 | 0.976 (-2.4%) | 0.983 | Immune |\\n| π0.5 (4B) | Pure linear proj (×√d scaling) | 768 (3×256) | **98.2%** (491/500) | **L2norm=33.4%, random=69.4%** | **Uniformly Critical (D139)**: L2norm catastrophic (-64.8pp), random tolerant (-28.8pp), gap=+36pp. CV=0.055. |\\n| X-VLA (880M) | Linear + BART 12L | 50 | ~1.00 | ~1.00 | Threshold-graded (k=0.7: 56.2%) |\\n| OpenVLA (7B) | 3-layer MLP | 256 | 1.608 (+61%) | 1.167 (+17%) | Smooth graded |\\n| OFT (7B) | 3-layer MLP (DINOv2+SigLIP fused) | **512** | N/A | N/A | D136: Blackwell GPU incompatible. CV=0.219≈OpenVLA → graded. Cite official ~97% baseline. |\\n| SmolVLA (450M) | Pixel-shuffle | 128 | — | 0% cliff | Catastrophic |\\n\\nDiagnostic metrics (D104+D106+D120: CV as continuous predictor, 7 models):\\n| Model | Connector (effective) | Entropy | CV | Pruning Behavior |\\n|-------|----------------------|---------|------|------------------|\\n| π0 | Pure linear proj | 0.959 | 0.038 | Immune (offline, k=0.1 improves) |\\n| π0.5 | Pure linear proj (×√d) | pending | 0.055 | **Uniformly Critical (D139)**: L2norm=33.4%, random=69.4%, gap=+36pp. Monotonic trend extreme. |\\n| X-VLA | Linear proj + BART enc (12L) | **0.614** | **0.151** | Threshold-graded: robust k≥0.9, cliff k=0.7 (56.2%). D127: random=L2norm at k=0.9 |\\n| OpenVLA | 3-layer MLP (GELU) | 0.661 | 0.215 | Graded (74→37.4% at k=0.5) |\\n| OFT | 3-layer MLP (DINOv2+SigLIP, **512 tokens**) | 0.667 | 0.219 | D136: Graded expected (CV≈OpenVLA). Blackwell GPU incompatible, no LIBERO SR. |\\n| SmolVLA | Pixel-shuffle (16×) | 0.952 | **0.314** | Catastrophic (0% at k=0.95) |\\n\\nKey insights (updated with 7-model data):\\n1. **CV is a continuous predictor**: 0.038 → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 maps to decreasing pruning tolerance. NOT a 3-class discrete classifier.\\n2. **X-VLA CV=0.151 correctly predicted its intermediate behavior** — closer to OpenVLA (0.215) than π0 (0.038), matching k=0.7 SR ≈ OpenVLA k=0.7.\\n3. **X-VLA entropy=0.614 ≈ OpenVLA 0.661** — both have BART/MLP non-linear mixing. X-VLA is NOT \\\"high entropy\\\" like π0.\\n4. **Effective connector complexity matters more than nominal label**: X-VLA is \\\"linear proj\\\" but BART encoder introduces 12 transformer layers of mixing. Paper should discuss \\\"effective connector\\\" = projection + any intermediate processing.\\n5. OFT entropy 0.667 ≈ Standard 0.661 → action head does not affect attention structure\\n6. Framing: CV captures \\\"degree of non-linear mixing in the vision-to-LLM pathway.\\\" More mixing → higher CV → less tolerant of pruning.\\n\\n### Smart Compress (Learned Re-encoding)\\nCross-attention (VTC) M sweep (3-seed where available):\\n- M=16: **56.9% ± 1.3pp** (3-seed: 55.8/58.4/56.5) — 87.5% compression, ZERO loss vs M=128\\n- M=32: 60.1±1.3% (3-seed: 61.6/59.2/59.6)\\n- M=64: 62.0±2.3% (3-seed: 61.6/60.0/64.4)\\n- M=96: 54.5±3.2% (3-seed: 52.6/58.2/52.8) — highest variance\\n- M=128: 58.0±3.5pp (3-seed: 59.8/54.0/60.2) — passthrough control\\n- **D102 CONFIRMED: M-curve is flat.** M=16 (56.9%) = M=128 (58.0%), difference < 1.1pp. VTC achieves near-lossless compression at ANY ratio for pixel-shuffle connector. All M values within ±5pp of baseline ~59%.\\n\\nMLP adapter (M=32, 3-seed):\\n- seed42: 65.2% (326/500), seed43: 64.6% (323/500), seed44: 60.4% (302/500)\\n- Mean: 63.4% ± 2.6 vs VTC M=32 mean 60.1% ± 1.3\\n- t-test p≈0.15, no significant difference — confirms architecture-independence\\n\\n### D109: VTR on OpenVLA (MLP projector) — FAILED\\n- C4-ext M=128 at 20K steps: **0% SR** (0/44 episodes before eval termination)\\n- Failure mode: model outputs identical action every timestep (severe overfitting)\\n- Interpretation: VTR adds unnecessary complexity for MLP projector tokens (already individually meaningful). VTR specifically solves pixel-shuffle entanglement.\\n- VTC-only M=32 and M=64 training in progress on westd-41074:2-3\\n\\n### Cross-Suite VTR Generalization (SmolVLA)\\n- M=32 Spatial: 53.2% (vs official Spatial baseline 44.6% per ROADMAP, vs pruning 0.6% — recovery from cliff-edge, +8.6pp over baseline)\\n- M=32 Goal: 56.4% (vs official Goal baseline 60.8% per ROADMAP, vs pruning 0% — recovery from cliff-edge, -4.4pp below baseline)\\n- ⚠️ Cross-suite baselines need reconciliation: paper_framing previously used 43.8%/63.0%, ROADMAP uses 44.6%/60.8%. Use n=500 official checkpoint data as ground truth.\\n- Note: VTR trained on Object suite, evaluated cross-suite. Official baselines from different checkpoint (official vs LoRA-FT); comparisons should emphasize recovery from 0% rather than absolute performance vs uncompressed.\\n\\n### Pairwise Statistical Tests (Welch's t-test, n=3 per condition)\\n- M=32 VTC vs M=32 MLP: p=0.150 (not significant) — confirms architecture-independence\\n- M=64 VTC vs M=96 VTC: p=0.034 (significant) — M=96 dip confirmed real\\n- M=32 MLP vs M=96 VTC: p=0.022 (significant) — M=96 underperforms\\n- M=32/M=64/M=128 VTC cluster: all pairwise p>0.25 — robust across M values\\n- Bonferroni note: no pair survives correction at 10 tests; n=3 limits power (~0.2 for medium effects)\\n\\n### Supplementary\\n- Inference latency: 6% speedup at M=32\\n- KV-cache: 75% memory reduction at M=32\\n\", \"total_chars\": 51958, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-28T17:47:02.017Z_

<details><summary>↩ Tool result · `toolu_01TJqPgWVcLSAoZzQEMhZJ72`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "8cbcbfe1-d941-4253-a5a5-61f89691efab",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 88,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01J1y29GPiZV7M8vTV5JsqBe`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5c041521-e8e2-414d-abe9-e8e6614720ac/tool-results/toolu_01GQsGzoo6GSmBfzBfB3g6oc.txt",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "290adc0f-698b-4162-acdc-6f5194721640",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeGzdXHoH2giHQm54ypvZV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 34272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1085
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-28T17:47:05.761Z_

<details><summary>↩ Tool result · `toolu_01J1y29GPiZV7M8vTV5JsqBe`</summary>

```text
1	{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\", \"content\": \"# Paper Framing — importance_margin_vla_compress\\n\\n## Target Venue\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\n\\n## Title (working)\\n\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\"\\n\\n## Core Insight\\n\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\"threshold-graded\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\n\\n**Axis 1 — Token Coupling (connector architecture):**\\n| Type | Connectors | CV Range | Mechanism |\\n|------|-----------|----------|-----------|\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\n\\n**Axis 2 — Task Complexity:**\\n| Level | Suites | Characteristics |\\n|-------|--------|----------------|\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\\n\\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\\n- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance\\n- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen\\n- Token-independent (π0.5 Goal/Long): data collecting, expected smaller amplification\\n\\n**CV remains the primary Axis-1 diagnostic** — predicts both pruning tolerance and optimal strategy (Claim 5). Task complexity (Axis 2) explains within-model variance across suites that the old taxonomy could not capture.\\n\\n_Original per-connector evidence (from Object-suite 4-class taxonomy) retained below; reinterpret through 2-axis lens:_\\n- **Linear projection** (π0 3.3B, π0.5 4B): **\\\"Uniformly Critical\\\" (D139)**. NOT immune. π0.5 baseline=98.2%, random k=0.5=**69.4%** (-28.8pp), L2norm k=0.5=**33.4%** (-64.8pp). Gap=+36.0pp, random wins 9/10 tasks. Low CV (0.038/0.055) = uniformly important tokens → L2norm's systematic bias selects spatially clustered tokens → catastrophic at k≤0.7. Random preserves spatial coverage → 2× better at k=0.5. **L2norm extended curve:** k=0.1=2.6% (collapse) → k=0.3=51.0% → k=0.5=33.4% (valley) → k=0.7=55.0% → k=0.9=98.2%. V-shape with collapse at extreme compression. CV=0.055 makes this the extreme case of the monotonic diagnostic trend. **⚠️ MAJOR FINDING (2026-05-22, fully investigated):** π0.5 random pruning exhibits sharp cliff at k=0.85-0.925 with non-monotonic recovery:\\n  - k=0.95: 71.1% FINAL (seed42 500ep; seed43=72.8%) — already 27pp below baseline\\n  - k=0.925: **27.6%** FINAL (seed42) — cliff entry point, 43pp drop from k=0.95\\n  - k=0.9: 10.8%±1.2pp (dual seed: seed42=12.0%, seed43=9.6%) — **87.4pp gap vs L2norm k=0.9=98.2%**\\n  - k=0.85: **5.0%** FINAL (seed42 v2=4.4%) — cliff floor\\n  - k=0.7: 75.5% (mean), k=0.5: 68.9%, k=0.3: 36.4% — recovery zone\\n  - Cliff profile: 71.1%(k=0.95) → 27.6%(k=0.925) → 10.8%(k=0.9) → 5.0%(k=0.85) — 66pp collapse over 10% keep ratio change\\n  **D151 (2026-05-22): Cliff is RANDOM-SPECIFIC.** L2norm maintains 98.0-99.2% plateau across the entire cliff zone:\\n  - L2norm k=0.95=98.2%, k=0.925=99.2%, k=0.9=98.2%, k=0.85=98.0% — zero degradation\\n  - Random k=0.925: 27.6% vs L2norm=99.2% → **71.6pp gap** (maximum separation)\\n  - Random k=0.85: 5.0% vs L2norm=98.0% → **93.0pp gap**\\n  - L2norm succeeds because deterministic selection consistently retains the same token subset; random sampling creates variable damage\\n  **D152 (2026-05-22): Cliff is TASK-SPECIFIC.** Object tasks collapse catastrophically, Spatial tasks degrade but survive:\\n  - Random k=0.9: Object=10.8% vs Spatial=54.6% — Spatial retains 5× more SR\\n  - Random k=0.85: Object=5.0% vs Spatial=TBD (collecting)\\n  - Within Object suite: all 10 tasks collapse at k=0.9 (2-16%). Within Spatial suite: degradation but not catastrophic.\\n  - Mechanism: Object tasks require precise object identity discrimination (visually similar objects); Spatial tasks rely on spatial layout (more distributed visual information). Random token loss destroys fine-grained discriminative features needed for Object before destroying spatial layout features.\\n  **Fixed-mask experiment (D149) NEGATES temporal inconsistency hypothesis:** per-episode fixed mask T0=12% = per-call random T0=12%. Temporal mask variation is NOT the cause.\\n  **D153: Cross-suite LIBERO-Spatial — weaker non-monotonicity, no catastrophic dip (2026-05-22)**\\n  Baseline: 97.2%. Random pruning profile:\\n  | k | Object | Spatial | Δ | Pattern |\\n  |---|--------|---------|---|---------|\\n  | 0.95 | 71.1% | deploying | — | — |\\n  | 0.925 | 28.8% (2-seed) | — | — | — |\\n  | 0.9 | 10.8% | 54.6% | +43.8pp | Spatial 5× more robust |\\n  | 0.85 | 5.0% | **58.4%** | **+53pp** | Maximum divergence |\\n  | 0.7 | 75.5% | 74.4% | -1pp | Suite-independent |\\n  | 0.5 | 69.4% | 71.6% | +2pp | Suite-independent |\\n  | 0.3 | 36.4% | 49.6% | +13pp | Spatial more robust |\\n  L2norm Spatial: k=0.9=95.0%, k=0.7=67.0%, k=0.5=55.6%, k=0.3=57.2%. L2norm k=0.95/k=0.85 deploying.\\n  **Object has deep V-shape dip**: 5%(k=0.85) → 10.8%(k=0.9) → 75.5%(k=0.7), 70pp recovery from cliff floor. **Spatial has weaker non-monotonicity**: k=0.5(71.6%) > k=0.85(58.4%) > k=0.9(54.6%), but no catastrophic collapse — floor stays above 50% vs Object's 5% floor. The cliff zone gap (Object 5% vs Spatial 58%) reflects concentrated vs distributed critical token patterns.\\n  **Mechanism**: Object tasks have **concentrated** critical tokens (object identity discrimination — visually similar objects). Random removal at cliff zone destroys these concentrated patches → catastrophic. Spatial tasks have **distributed** critical information (layout patches spread across image). Random removal damages any random subset but never completely destroys spatial signal → graceful degradation.\\n  **Paper value**: Two distinct cliff behavior modes — **concentrated-critical (Object)** vs **distributed-critical (Spatial)** — as a function of task semantics. Pruning sensitivity = f(connector, method, k, task_semantics). Suite-independent at moderate k (0.5-0.7), suite-dependent at cliff zone (0.85-0.95).\\n  **Paper value:** strengthens \\\"uniformly critical\\\" class — even uniform importance distribution doesn't make pruning safe. Simple deletion fails; learned compression (VTR) needed.\\n- **Linear projection + deep post-processing** (X-VLA 880M, linear proj + 12-layer BART encoder): robust k≥0.9 (97.6% SR), **cliff at k=0.7 (56.2% SR, -43pp)**. BART encoder introduces non-linear mixing that creates partial token dependencies. CV=0.151. **D127: random pruning k=0.9=97.8% ≈ L2norm 97.6% — pruning method independence confirmed for low-CV connectors.**\\n- **Multi-layer MLP** (OpenVLA 7B, OpenVLA-OFT 7B): graded degradation. k=0.1 normalized loss = 1.608 (+61%). Non-linear mixing creates partial dependencies. OFT entropy (0.667) ≈ Standard (0.661), CV(OFT)=0.219 ≈ CV(OpenVLA)=0.215, confirming connector — not action head — determines attention structure. **D136: OFT LIBERO eval infeasible (Blackwell GPU SDPA incompatibility, requires A100+torch2.2). OFT included via CV/entropy analysis only; cite official baseline ~97% SR.** π0.5 baseline confirmed 98.2% (D135).\\n- **Pixel-shuffle** (SmolVLA 450M): catastrophic cliff-edge. k=0.95 (removing 5%) → 0% SR. Spatial folding creates irreversible entanglement. **D147: Official HF checkpoint (HuggingFaceVLA/smolvla_libero) confirms identical cliff — random k=0.95 = 0%, L2norm k=0.95 = 0%. Cliff is architectural, not training artifact. Resolves W-C2.** **Dual-seed confirmed (2026-05-22):** Baseline 59.4%±0.3pp (seed42=59.2%, seed43=59.6%), random k=0.95: 0.1% mean (0.0%/0.2%), random k=0.5: 0.0%, L2norm k=0.95: 0.2% mean (0.4%/0.0%). All pruning ≤0.2% across both seeds. cqa1 supplementary: L2norm k=0.7=0%, random k=0.9=0%.\\n\\nKey controlled comparison: π0 (256 tokens, linear) vs OpenVLA (256 tokens, 3-layer MLP) — same token count, same encoder lineage, only connector differs. k=0.1: π0 improves 2.4% vs OpenVLA degrades 61%. This isolates connector as the causal factor.\\n\\nLearned re-encoding (VTR) overcomes the cliff-edge: cross-attention 60.1±1.3% and MLP adapter 63.4±2.6% at M=32 (vs 0% hard pruning), with M=128 passthrough (58.0%±3.5, 3-seed) ≈ baseline 59.2% — VTR recovers to baseline rather than exceeding it. SmolVLA M-curve confirmed flat (D105): M=16 (56.9%±1.3) = M=128 (58.0%±3.5), all 5 M-values within ±3pp of baseline 59.2%. VTR achieves near-lossless compression at any ratio (0-87.5%) for pixel-shuffle connectors.\\n\\n## Paper Identity (Round 5 Upgrade — D171 2-Axis, 2026-05-22)\\n**ANALYSIS + METHOD paper.** (D091 → D097 → D171: 5 models × 3 connector families × 4 LIBERO suites)\\n\\n**Analysis contribution (primary)**: First systematic study revealing that VLA token pruning robustness is determined by the interaction of two axes: (1) connector architecture (token-independent vs token-entangling, diagnosed by importance CV 0.038→0.314) and (2) task complexity (simple vs multi-step). Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio. 5 models × 4 suites × 4 model sizes (450M-7B) eliminate confounds. No competing work does cross-architecture, cross-task VLA token analysis.\\n\\n**Method contribution**: Diagnose-then-Compress framework:\\n- Step 1: **Connector Compressibility Diagnostic** (D104: resolved)\\n  - **Primary metric: Importance CV** (token importance heterogeneity) — zero-cost, one forward pass\\n  - CV forms continuous spectrum predicting pruning tolerance: π0=0.038 < π0.5=0.055 < X-VLA=0.151 < OpenVLA=0.215 < OFT=0.219 < SmolVLA=0.314\\n  - ⚠️ D106+: X-VLA CV=0.151 correctly predicted its intermediate pruning behavior (k=0.7 ≈50% SR ≈ OpenVLA k=0.7). CV is a valid continuous predictor, NOT a 3-class discrete classifier.\\n  - **Key discovery**: X-VLA \\\"linear projection\\\" passes through BART encoder (12 transformer layers) before decoder → introduces non-linear mixing → explains CV=0.151 (much higher than π0=0.038 pure linear)\\n  - **Entropy as mechanistic supplement** (CV is primary; entropy is supplementary):\\n    - π0: entropy=0.959 (per-layer mean, range 0.931–0.983), CV=0.038 — uniform & independent → most tolerant\\n    - **π0.5: entropy=0.666, CV=0.055** — similar entropy to OpenVLA (0.661) but vastly different pruning behavior (CV correctly differentiates)\\n    - X-VLA: entropy=0.614, CV=0.151 — selective & BART-mixed → intermediate\\n    - OpenVLA: entropy=0.661, CV=0.215 — selective & MLP-mixed → graded\\n    - SmolVLA: entropy=0.952, CV=0.314 — near-uniform but spatially entangled → catastrophic\\n  - **KEY INSIGHT**: Entropy clusters π0.5/X-VLA/OpenVLA together (0.61-0.67) despite very different pruning behaviors. CV correctly separates them (0.055 vs 0.151 vs 0.215). Entropy fails as diagnostic because it doesn't capture token independence structure — only attention distribution shape.\\n  - ✅ Batch 2 complete: continuous CV spectrum confirmed (X-VLA full 8-point curve validates threshold-graded class)\\n  - Supplementary: lightweight pruning probe (remove 5%, one forward pass) as practitioner-friendly alternative\\n- Step 2: VTR (Vision Token Re-encoding) — lightweight cross-attention module (~22M params) for universal compression\\n- For entangled tokens (pixel-shuffle): recovers from 0% (hard pruning) to ~59% ≈ baseline, M-curve flat D105 (near-lossless compression at any ratio 0-87.5%)\\n- For independent tokens (MLP projector): **D109 C4-ext confirmed 0% SR** at 20K steps (M=128, severe overfitting — model outputs identical action every step). VTR on MLP projector does NOT improve SR; reframed as \\\"VTR ceiling depends on connector type\\\" finding. User directive: performance degradation acceptable if efficiency improves — VTR value is 75% KV-cache reduction + attention speedup. VTC-only M=32/M=64 training in progress to test whether smaller M values fare better.\\n\\n**Differentiation from concurrent work**: 4 concurrent works (Compressor-VLA, SpecPrune-VLA, LightVLA ICRA'26, See What Matters ICML'26) all propose pruning on MLP-projector VLAs. We (1) explain why pruning fails on pixel-shuffle architectures, (2) identify why pruning succeeds on linear projection (tokens are truly independent), and (3) propose a re-encoding method motivated by the diagnostic analysis.\\n\\n**Model coverage**: 5 VLA models × 3 connector families × 4 LIBERO suites × 4 model sizes (450M-7B). RC1 (only 2 models), RC2 (size confound), and RC7 (only one suite) fully addressed.\\n\\n## Core Claims (5 claims, expanded from 4)\\n\\n### Claim 1: 2-Axis Compressibility Framework (D107 → D171 UPGRADED)\\nPruning sensitivity = f(connector_architecture, task_complexity). Two axes interact:\\n\\n**Axis 1 — Token Coupling (connector determines base sensitivity):**\\n- **Token-independent** connectors (pure linear π0/π0.5, MLP OpenVLA/OFT): tokens retain spatial meaning → pruning damage is local, graded degradation\\n- **Token-entangling** connectors (BART X-VLA, pixel-shuffle SmolVLA): cross-token dependencies → pruning damage cascades\\n\\n**Axis 2 — Task Complexity (task amplifies entangling-connector sensitivity):**\\n- Simple tasks (Object): even entangling connectors tolerate mild pruning (X-VLA k=0.9=97.6%)\\n- Complex tasks (Goal/Long): entangling connectors collapse (X-VLA Goal k=0.9=70.2%, Long k=0.95≈53%)\\n- Key: same connector, same k, same method — **only task differs** → 27.8pp drop (Object→Goal)\\n\\n**CV predicts Axis-1 position**: 0.038 (most independent) → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 (most entangled)\\n\\n**Evidence**: 5 models, 3 connector families, 4 LIBERO suites, 4 model sizes (450M-7B). Key controlled comparisons:\\n1. π0 (256 tokens, linear) k=0.1 = 0.976 vs OpenVLA (256 tokens, MLP) k=0.1 = 1.608 → connector isolates base sensitivity\\n2. X-VLA Object k=0.9 = 97.6% vs X-VLA Goal k=0.9 = 70.2% → task complexity isolates amplification\\n3. SmolVLA Object = 0% at k=0.95 → extreme entanglement dominates even on simple tasks\\n\\n🔴 **D108→D127→D130→D132: Pruning method comparison — MAJOR REVERSAL at aggressive compression**\\n\\nBoth L2 norm and random pruning tested on X-VLA and OpenVLA. **CV predicts not just tolerance but optimal strategy**:\\n\\n- **OpenVLA (MLP, CV=0.215)**: L2 norm consistently ≥ random at all k values. High CV → meaningful importance differentiation → L2 norm selection effective.\\n  - k=0.95: L2norm=69.4% ≈ random=69.2% (+0.2pp)\\n  - k=0.7: L2norm=49.8%¹ > random=44.4% (+5.4pp). ¹seed43 only, seed42 running on westd-38929:2\\n  - k=0.5: L2norm=39.2% > random=35.8% (+3.4pp)\\n  - k=0.3: L2norm=25.0%, random=pending (re-running)\\n\\n- **X-VLA (BART, CV=0.151)**: 🔴 **REVERSAL** — L2 norm ≈ random at mild compression, but **random MASSIVELY outperforms L2 norm at aggressive compression**:\\n  - k=0.9: L2norm=97.6% ≈ random=97.8% (≈0pp)\\n  - k=0.85: L2norm=68.0% > random=63.6% (+4.4pp, cliff boundary)\\n  - k=0.8: L2norm=89.0% ≈ random=89.4% (≈0pp, non-monotonic recovery)\\n  - **k=0.5: L2norm=42.6% << random=70.6% (-28.0pp!)** — CI non-overlapping, statistically significant. Random wins 9/10 tasks; T4 ketchup: L2norm=42% vs random=100% (+58pp). Only T6 butter both crash at 2%.\\n  - k=0.7: L2norm=56.2% << random=65.2% (+9pp). Crossover confirmed at k≈0.8.\\n  - **k=0.3: L2norm=22.8% << random=62.8% (+40pp!)** — gap scales monotonically with compression.\\n  - **D137**: seed43 k=0.5=71.0% confirms seed42=70.6% (Δ=0.4pp). Gap reproducible.\\n\\n- **SmolVLA**: all methods = 0% at all k values → trivially method independent.\\n\\n**KEY INSIGHT (D132→D137)**: Importance-based pruning can be **actively harmful** on low-CV architectures under aggressive compression, and the harm SCALES: +9pp@k=0.7, +28pp@k=0.5, +40pp@k=0.3. Mechanism: X-VLA's linear projection + BART encoder produces relatively uniform token norms (CV=0.151). L2 norm selection on a near-uniform distribution degenerates into selecting spatially clustered tokens → loses diversity → catastrophic failure. Random pruning preserves spatial coverage → dramatically better. Multi-seed confirmed.\\n\\n**This strengthens the paper**: CV serves as a dual predictor — predicts both (1) pruning tolerance ceiling and (2) whether importance-based methods help or hurt. Connector architecture determines both via its effect on token importance distribution.\\n\\n**Paper narrative upgrade**: From \\\"connector determines compressibility\\\" to \\\"connector determines both compressibility AND optimal compression strategy.\\\" This is a significantly stronger and more novel contribution.\\n\\n**Pending data**: X-VLA random k=0.7 (crossover characterization), multi-seed k=0.5 random (robustness). OpenVLA L2norm k_ratio=null provenance issue needs fixing.\\n\\n### Claim 2: Pixel Shuffle Creates Irreversible Token Entanglement\\nSmolVLA's pixel_shuffle connector spatially folds 1024 SigLIP patches into 64 tokens per camera (16x compression). Each resulting token encodes a 32x32 pixel region via channel-to-spatial reorganization. This creates extreme cross-token spatial entanglement: removing any single token eliminates an entire spatial quadrant's information with no redundancy to compensate.\\n\\n**Evidence**:\\n- k=0.95 (remove only 7/128 tokens = 5.5%) = 0% SR — even minimal removal is catastrophic\\n- k=0.9 (remove 13/128 tokens) = 0% SR\\n- Geometric prior (Sobel edge) k=0.5/0.7/0.9 = all 0%\\n- Attention entropy ratio 0.952 (near-uniform, TV=0.05)\\n- Official checkpoint Object (59.2% baseline) cliff-edge at k=0.5 → 0%\\n- Official checkpoint Spatial (43.8% baseline) cliff-edge at k=0.5 → 0.6% (3/500, CI [0.2%, 1.7%])\\n\\n### Claim 3a: Linear Projection → Depends on Effective Pipeline (D107: RESOLVED)\\nPure linear projection (π0): immune. Linear projection + deep post-processing (X-VLA, BART 12L): \\\"robust-then-cliff\\\" — immune at k≥0.9, cliff at k=0.7, then graded degradation. The BART encoder introduces non-linear cross-token mixing that explains intermediate CV=0.151 and the cliff pattern.\\n\\n**Evidence** (X-VLA LIBERO SR — Batch 1 + Batch 2 COMPLETE, full 8-point curve):\\n- k=1.0: **99.2%** (baseline, 496/500) — per-task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]\\n- k=0.95: **99.0%** (-0.2pp) — per-task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]\\n- k=0.9: **97.6%** (-1.6pp) — per-task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]\\n- k=0.7: **56.2%** (-43pp, CLIFF — 281/500) — per-task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]\\n- k=0.5: **42.6%** (-57pp) — Batch 2 confirmed (MSH fix applied)\\n- k=0.3: **23.0%** (-77pp) — graded degradation continues below cliff\\n- k=0.2: **~4.0%** (-96pp) — near-zero\\n- k=0.1: **~0.0%** (-100pp) — complete failure\\n✅ Full curve confirms threshold-graded pattern: immune k≥0.9, cliff at k=0.7, then graded degradation k≤0.5 (42.6%→23.0%→~4%→~0%).\\n\\n**Cliff localization (D114, D117: 3-seed deterministic, L2norm)**:\\n- k=0.80: **89.0% ± 0.72pp** (seeds: 88.8/88.4/89.8)\\n- k=0.85: **67.9% ± 0.31pp** (seeds: 68.0/67.6/68.2 — T4=26%, T6=0% across ALL 3 seeds)\\n- Non-monotonic: k=0.85 < k=0.80 by **21.1pp**. BART encoder creates length-dependent interactions near critical token density. SD < 1pp confirms fully deterministic, not stochastic.\\n\\n**Random pruning comparison (D127-D130, D132 REVERSAL)**:\\n- k=0.9: random=97.8% ≈ L2norm=97.6% → method independent at mild compression\\n- k=0.85: random=63.6% vs L2norm=68.0% (+4.4pp for L2norm at cliff boundary). Both crash on same tasks (T1, T4, T6, T8) → cliff is architectural.\\n- k=0.8: random=89.4% ≈ L2norm=89.0% → method independent, non-monotonic recovery confirmed in both\\n- 🔴 **k=0.5: random=70.6% >> L2norm=42.6% (+28pp REVERSAL, CI non-overlapping)**. Per-task random: [96, 46, 100, 92, 100, 94, 2, 82, 42, 100]. Random wins 9/10 tasks; L2norm actively harmful. T4: random=100% vs L2norm=42% (+58pp).\\n- k=0.7: random=65.2% vs L2norm=56.2% (+9pp random). Crossover confirmed at k≈0.8.\\n- 🔴 **k=0.3: random=62.8% vs L2norm=22.8% (+40pp!)** — gap SCALES with compression: +9@k=0.7, +28@k=0.5, +40@k=0.3.\\n- **D137 multi-seed confirmed**: seed43 k=0.5=71.0% (seed42=70.6%, Δ=0.4pp). Gap is reproducible.\\n- **Random non-monotonicity confirmed**: k=0.5 (70.6%) > k=0.7 (65.2%) > k=0.3 (62.8%). seed43 reproduces (71.0%). L2norm monotonically decreasing (42.6% > 22.8%). Random's k=0.5 \\\"sweet spot\\\" may reflect optimal diversity-coverage tradeoff: enough tokens removed to break BART clustering, but enough retained for spatial coverage.\\n- k=0.85 per-task (random): [100, 10, 100, 94, 24, 92, 0, 94, 22, 100] = 63.6%.\\n- **Non-monotonicity confirmed in both methods**: k=0.85 (42 tokens) cliff vs k=0.8 (40 tokens) recovery. 2-token difference, 21-26pp gap.\\n- **D132 KEY INSIGHT**: At aggressive compression (k=0.5), L2 norm is catastrophically worse than random for X-VLA. Low CV=0.151 → near-uniform importance → L2 norm degenerates into spatially clustered selection → loses diversity. This is the opposite of OpenVLA (CV=0.215) where L2 norm helps. **CV predicts optimal pruning strategy, not just tolerance.**\\n\\n**Cross-suite generalization (D117, updated with full results)**:\\n- X-VLA Spatial baseline: **91.6%** [88.8%, 93.7%] (500 eps, T5=48% is hardest task)\\n- X-VLA Goal baseline: **98.0%** [96.4%, 98.9%] (500 eps, all tasks ≥92%)\\n- X-VLA-Libero checkpoint covers all 4 suites without suite-specific fine-tuning.\\n\\n**⚠️ Cross-suite pruning sensitivity (key finding — potential new contribution)**:\\n\\nX-VLA pruning curve comparison across suites:\\n\\n| Suite | k=1.0 | k=0.9 | k=0.85 (L2/Rand) | k=0.8 (L2/Rand) | k=0.7 (L2/Rand) | k=0.5 (L2/Rand) |\\n|-------|-------|-------|-----|-------|----------|----------|\\n| Object | 99.2% | 97.8% | 68.0/63.6% | 89.0/89.4% | 56.2/65.2% | 42.6/**70.6%** |\\n| Spatial | 91.6% | 79.0% | 66.6/67.6% | — | — | 58.8%/**71.4%** |\\n| Goal | 98.0% | 70.2% | — | — | — | 61.0%/— |\\n\\n**Goal suite FINAL results (10/10 tasks, D123: suite-level monotonic confirmed)**:\\n- k=0.9: **70.2%** (351/500) — much larger drop than Object (-1.4pp) despite similar baseline\\n- k=0.5: **61.0%** (305/500) — suite-level monotonic (k=0.9 > k=0.5), D123 retracted earlier partial-data non-monotonic claim\\n\\n**Per-task non-monotonic pruning remains valid (selected tasks)**:\\n\\n| Task | k=1.0 | k=0.9 | k=0.5 | Pattern |\\n|------|-------|-------|-------|---------|\\n| T0 open drawer | 100% | 100% | 82% | monotonic ↓ |\\n| T2 close drawer | 94% | 96% | **100%** | **pruning improves** |\\n| T3 open+put (multi-step) | 100% | **6%** | **40%** | catastrophic + non-monotonic (k=0.5 > k=0.9) |\\n| T8 | — | — | — | +46pp non-monotonic (k=0.5 > k=0.9) |\\n| T9 | 98% | — | ~0% | catastrophic collapse (-98pp) |\\n\\n- Suite-level: Goal k=0.5=61.0% > Spatial k=0.5=58.8% — Goal slightly more robust, but both moderate degradation\\n- Per-task: T3/T8 show non-monotonicity (k=0.5 > k=0.9), T9 catastrophic collapse. These are genuine misalignments between global L2-norm ranking and task-specific token utility.\\n- T2 pruning improvement: consistent with π0 finding — simple tasks benefit from token noise removal\\n\\n**Key cross-suite finding**: Goal k=0.9 drops **27.8pp** (vs Object -1.4pp). Same connector, same pruning method, different task distribution → **task complexity amplifies pruning sensitivity**. Goal tasks involve multi-step reasoning that depends heavily on precise spatial tokens.\\n\\n**Task-level analysis (Spatial, k=0.5 vs baseline)**:\\n- Robust (Δ≤10pp): T0 \\\"between plate and ramekin\\\" (-4pp), T4 \\\"in top drawer\\\" (-2pp) — global spatial / unambiguous target\\n- Moderate (Δ 10-30pp): T2(-10), T3(-24), T6(-22), T8(-18) — mild spatial precision needed\\n- Catastrophic (Δ>40pp): T5 \\\"on ramekin\\\" (-48pp, 0%), T9 \\\"on cabinet\\\" (-58pp), T7 \\\"on stove\\\" (-64pp), T1 \\\"next to ramekin\\\" (-78pp)\\n- **T1 has 100% baseline but 22% at k=0.5** — high baseline ≠ pruning robustness\\n\\n**Mechanism**: Goal tasks are semantically diverse (different verbs/objects) → language instruction alone disambiguates → vision tokens are redundant for task selection. Spatial tasks are semantically near-identical (all \\\"pick bowl...\\\") → disambiguation relies entirely on spatial vision tokens → pruning destroys the only discriminative signal.\\n\\n**Paper framing upgrade (Reviewer suggestion, agreed)**:\\n- From \\\"connector determines pruning tolerance\\\" → \\\"pruning sensitivity = f(connector_type, task_semantics)\\\"\\n- Connector CV predicts degradation *class* (immune/threshold/graded/catastrophic)\\n- Task semantic structure determines degradation *severity* within that class\\n- When language disambiguates: aggressive pruning is safe (Goal k=0.5 ≈ baseline)\\n- When spatial vision disambiguates: even conservative pruning degrades (Spatial k=0.9 -12.6pp)\\n- **Potential new contribution**: first task-level pruning sensitivity analysis in VLAs. §4.6 should include per-task heatmap + the language-vs-spatial disambiguation framework.\\n\\nπ0 evidence:\\n- π0 (3.3B, 256 tokens, pure linear proj): k=0.1 normalized_L1 = 0.976 (-2.4% = improvement), k=0.5 = 0.983\\n- Attention entropy: π0 suffix-to-vision mean 0.959 (near-uniform across 18 layers, range [0.931, 0.983])\\n- Importance CV: π0 = 0.038 (lowest in spectrum)\\n\\n**Key insight**: \\\"Linear projection\\\" is NOT sufficient for immunity. The effective pipeline matters. X-VLA's BART encoder (12 transformer layers after linear proj) introduces partial dependencies → CV=0.151 → cliff at k=0.7. π0's pure linear proj → CV=0.038 → immune even at k=0.1.\\n\\n### Claim 3b: MLP Projector → Graded Degradation\\nMulti-layer MLP connectors create partial token dependencies through non-linear mixing, enabling graceful but real degradation.\\n\\n**Evidence** (OpenVLA 6-point degradation curve):\\n- k=1.0: 74.0% (baseline)\\n- k=0.95: 69.4% (-6% relative)\\n- k=0.9: 62.0% (-16% relative)\\n- k=0.7: 49.0% (-34% relative)\\n- k=0.5: 37.4% (-49% relative)\\n- k=0.3: 20.6% (-72% relative)\\n- Entropy ratio 0.639 (progressive sharpening L0=0.98→L29=0.48, TV=0.50)\\n- **Method independence confirmed**: random k=0.95=69.2% ≈ L2norm k=0.95=69.4%; random k=0.5=35.8% ≈ L2norm k=0.5=37.4%. For MLP projectors, pruning method doesn't matter.\\n- OFT (same connector, different action head): entropy 0.667 ≈ Standard 0.661 → connector determines attention structure, not action head\\n- CogACT (MLP projector, literature): 74.8% → 74.2% under 78% pruning (EfficientVLA)\\n\\n### Claim 4: Learned Re-Encoding Achieves Near-Lossless Compression Where Deletion Fails (D072+MLP confirmed → upgraded to METHOD per D091)\\n**⚠️ Baseline correction (2026-05-22): SmolVLA Object baseline = 59.2% (official HF checkpoint), NOT 44.8% (old reproduced). VTR narrative reframed from \\\"re-encoding boost\\\" to \\\"near-lossless compression recovery\\\".**\\n\\nTwo independent re-encoding architectures (~22M params each) validate that **any learned re-encoding** can recover entangled pixel_shuffle tokens from 0% (hard pruning) to near-baseline levels. Cross-attention (60.1±1.3%, 3-seed) and MLP adapter (63.4±2.6%, 3-seed) both achieve this recovery, with p≈0.15 confirming no significant difference between architectures. M=128 passthrough (58.0±3.5%, 3-seed) ≈ baseline 59.2% (-1.2pp), confirming VTR recovers to baseline rather than exceeding it. **M-curve is flat**: M=16 (56.9%) through M=128 (58.0%), all within ±3pp of baseline 59.2% — VTR achieves near-lossless compression at ANY ratio (0-87.5%) for pixel-shuffle connectors. M=64 achieves best absolute SR at 62.0±2.3% (+2.8pp over baseline) with 50% compression. Cross-suite generalization confirmed: M=32 recovers to 53.2% on Spatial (vs 0.6% pruning cliff-edge) and 56.4% on Goal. M=96 dip statistically confirmed (p=0.034 vs M=64).\\n\\n**D109 C4-ext on OpenVLA (MLP projector)**: M=128 VTR at 20K steps = **0% SR** (severe overfitting, model outputs identical action every step). This suggests VTR's effectiveness is connector-dependent: pixel-shuffle benefits enormously (0%→~59% ≈ baseline) because re-encoding repairs spatial entanglement, while MLP projector tokens are already individually meaningful and VTR adds unnecessary complexity. VTC-only M=32/M=64 training in progress — if these also fail, VTR is specifically a pixel-shuffle solution, which strengthens the architecture-dependency narrative.\\n\\n**Evidence** (all confirmed):\\n\\nCross-attention re-encoding (M sweep, 3-seed where available):\\n| M | Compression | SR (3-seed mean±std) | Seeds | Notes |\\n|---|------------|-----|-----|-----|\\n| 16 | 87.5% | **56.9±1.3%** | 42/43/44 | ✅ ZERO loss vs M=128 |\\n| 32 | 75% | **60.1±1.3%** | 42/43/44 | ✅ |\\n| 64 | 50% | **62.0±2.3%** | 42/43/44 | ✅ best tradeoff |\\n| 96 | 25% | 54.5±3.2% | 42/43/44 | ✅ highest variance |\\n| 128 | 0% (passthrough) | **58.0±3.5%** | 42/43/44 | ✅ passthrough control |\\n\\nMLP adapter control (M=32, ~22.14M params, 3-seed):\\n| Architecture | Params | M | Mean SR (3-seed) | Std | Individual seeds |\\n|---|---|---|-----|-----|-----|\\n| Cross-attention (VTC) | 22.2M | 32 | **60.1%** | ±1.3 | 61.6 / 59.2 / 59.6 |\\n| **MLP adapter** | **22.14M** | **32** | **63.4%** | **±2.6** | **65.2 / 64.6 / 60.4** |\\n\\nTwo-sample t-test: t≈1.94, p≈0.15 → **no significant difference** (α=0.05). Both >> 0% (hard pruning) and ≈ 59.2% (baseline). MLP ≥ VTC in all 3 seeds but difference not statistically significant — confirms any re-encoding architecture recovers to near-baseline, not a specific mechanism. (Note: M=32 seed43 corrected from 62.4% to 59.2% per registry verification; 62.4% was M=96 seed43 CI upper bound misattributed.)\\n\\n### Claim 5: CV Predicts Optimal Pruning Strategy — Monotonic Diagnostic Trend (D132→D139→D140→D142)\\nToken importance CV determines **which pruning method to use**, with the L2norm-vs-random gap scaling monotonically with CV. **Validated at TWO k values (D142):**\\n\\n**k=0.5 (main table):**\\n| Model | CV | Tokens | L2norm k=0.5 | Random k=0.5 | Δ (R-L2) |\\n|-------|-----|--------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | **33.4%** | **69.4%** | **+36.0pp** |\\n| X-VLA | 0.151 | 50 | 43.4%³ | 70.3%⁴ | +26.9pp |\\n| OpenVLA | 0.215 | 256 | 39.2% | 37.4%¹⁰ | -1.8pp |\\n\\n**k=0.7 (second validation, D142):**\\n| Model | CV | Tokens | L2norm k=0.7 | Random k=0.7 | Δ (R-L2) |\\n|-------|-----|--------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | **55.0%** | **77.2%** | **+22.2pp** |\\n| X-VLA | 0.151 | 50 | 58.6%⁶ | 65.1%⁷ | +6.5pp |\\n| OpenVLA | 0.215 | 256 | 49.8% | 44.4% | -5.4pp |\\n⁶ X-VLA L2norm k=0.7 2-seed: 58.2/59.0, mean=58.6%, σ=0.4pp (seed44 pending → tri-seed)\\n⁷ X-VLA random k=0.7 2-seed: 65.2/65.0, mean=65.1%, σ=0.1pp (seed44 running)\\n\\n³ X-VLA L2norm k=0.5 3-seed mean: 42.6/43.4/44.2, mean=43.4%, range 1.6pp\\n⁴ X-VLA random k=0.5 3-seed mean: 70.6/71.0/69.2, mean=70.3%, σ=0.9pp\\n\\n¹⁰ OpenVLA random k=0.5 = 37.4% (seed7). Table 3 previously showed 35.8% (unverified source). seed42 running on westd-38929, will replace when available.\\n\\n✅ **D139+D142 CONFIRMED**: Monotonic trend validated at BOTH k=0.5 (-1.8→+26.9→+36.0) and k=0.7 (-5.4→+6.5→+22.2). Same monotonic pattern. Paper: k=0.5 as main table, k=0.7 as confirmatory second row or separate table.\\n\\n**D140: k=0.3 interaction — method preference REVERSES at extreme compression for π0.5:**\\n\\n| Model | CV | Tokens | k=0.3 kept | L2norm k=0.3 | Random k=0.3 | Δ (R-L2) |\\n|-------|-----|--------|-----------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | 230 | **51.0%** | 36.4% | **-14.6pp** |\\n| X-VLA | 0.151 | 50 | 15 | 22.2%⁸ | **64.5%⁹** | **+42.3pp** |\\n| OpenVLA | 0.215 | 256 | 77 | 25.0% | **21.4%** | **+3.6pp** |\\n\\n⁸ X-VLA L2norm k=0.3 3-seed: 22.2/21.0/22.8 (from D137), mean=22.0%; seed43 running on cqa1\\n⁹ X-VLA random k=0.3 2-seed: 62.8/66.2, mean=64.5%, σ=2.4pp; seed44 running on cqa1\\n\\nAt k=0.3, π0.5 L2norm wins (+14.6pp) while X-VLA random still wins massively (+42.3pp). OpenVLA L2norm also wins (+3.6pp). The pattern: at k=0.3, both high-CV (OpenVLA) and low-CV-with-large-budget (π0.5, 230 tokens) favor L2norm, while mid-CV-with-small-budget (X-VLA, 15 tokens) strongly favors random. Strategy preference is f(CV, k, absolute_token_budget).\\n\\n**OpenVLA (CV=0.215) full seed42 Δ(L2-R) pattern**: +1.4pp (k=0.95) → +5.4pp (k=0.7) → pending (k=0.5) → +3.6pp (k=0.3). L2norm consistently better at ALL k values — high CV enables meaningful importance-based selection. Peak advantage at k=0.7, not monotonically increasing with compression.\\n\\n**D141: π0.5 L2norm complete curve — valley at k=0.5 confirmed (multi-seed)**:\\n| k | L2norm SR (s42) | L2norm SR (s43) | Random SR | Δ (R-L2) s42 |\\n|---|-----------------|-----------------|-----------|---------------|\\n| 0.7 | **55.0%** | **57.8%**¹⁰ | **77.2%** / **73.8%** (mean=75.5%) | +22.2pp (s42) / +19.8pp (mean) |\\n| 0.5 | **33.4%** | **33.6%** ✅ | **69.4%** / **68.4%** (mean=68.9%) | +36.0pp (s42) / +35.4pp (mean) |\\n| 0.3 | **51.0%** | **55.4%** ✅ | 36.4% | -14.6pp |\\n\\n¹⁰ Agent audit reported 56.4% for L2norm k=0.7 seed43 vs earlier worker result 57.8%. Needs reconciliation. Pattern unchanged.\\n\\n**V-shape fully confirmed (2 seeds, both methods)**:\\n- **Valley (k=0.5)**: L2norm 33.4/33.6% (std=0.1pp); Random 69.4/68.4% (std=0.7pp) — both methods stable\\n- **2-seed means**: L2norm k=0.7=56.4%, k=0.5=33.5%, k=0.3=53.2%; Random k=0.7=75.5%, k=0.5=68.9%\\n- **V-depth**: seed42=17.6pp, seed43=21.8pp (seed43 deeper because endpoints higher)\\n- **Δ(R-L2) dual-seed means**: k=0.7=+19.8pp, k=0.5=+35.4pp — monotonic trend holds with multi-seed\\n- seed43 consistently +2-4pp above seed42 but identical shape. Valley position/depth is architectural determinism.\\n\\n**Mechanism confirmed by token position visualization (D141)**:\\n- k=0.7: 2 clusters, 97% in largest, **100% spatial coverage** — enough tokens to maintain coverage\\n- k=0.5: **1 cluster, 100% in single region, 78% coverage** — worst-case spatial concentration\\n- k=0.3: **3 clusters**, 86% in largest, 78% coverage — cluster breaks apart, better diversity\\n\\nThe non-monotonicity arises because k=0.5 sits at the worst point of the spatial correlation structure: L2norm selects exactly the number of tokens that maximizes spatial clustering. At k=0.7 there are enough tokens for coverage; at k=0.3 the selection threshold crosses a boundary that fragments the cluster. Per-task variance is extreme at k=0.7 (T1=94%, T5=98% vs T7=0%) — L2norm deterministic selection can catastrophically miss specific task-critical spatial regions.\\n\\n**Paper strategy**: k=0.5 as **main table** (cleanest monotonic trend, clear gap). Full L2norm curve as **figure** showing pathological valley — strong evidence for spatial clustering mechanism. k=0.3 reversal as supplementary. Key message: \\\"CV predicts method preference at k=0.5; L2norm's spatial clustering creates pathological non-monotonicity unique to low-CV models.\\\"\\n\\n**Notable asymmetry**: Random tolerance is similar for low/medium CV at k=0.5 (π0.5=69.4% ≈ X-VLA=70.6%), while L2norm harm increases dramatically (π0.5=33.4% < X-VLA=43.4%). High CV (OpenVLA=35.8% random) is less random-tolerant because tokens have genuine importance differentiation that random discards.\\n\\n**Evidence** (Reviewer-verified, D132 PASS):\\n\\nX-VLA vs OpenVLA full comparison:\\n\\n| k | X-VLA (CV=0.151) | | OpenVLA (CV=0.215) | |\\n|---|---|---|---|---|\\n| | L2norm | Random | L2norm | Random |\\n| 0.95 | — | — | 70.6% | 69.2% (+1.4 L2norm) |\\n| 0.9 | 97.6% | 97.8% (≈0) | 70.6% | 64.6% (+6.0 L2norm) |\\n| 0.85 | 68.0% | 63.6% (+4.4 L2norm) | — | — |\\n| 0.8 | 89.0% | 89.4% (≈0) | — | — |\\n| 0.7 | 56.2% | **65.2% (+9pp random)** | 49.8%¹ | 44.4% (+5.4 L2norm¹) |\\n| 0.5 | **42.6%** | **70.6% (+28pp random!)** | 39.2% | 35.8% (+3.4 L2norm) |\\n| 0.3 | **22.8%** | **62.8% (+40pp random!)** | 25.0% | pending² |\\n\\n¹ OpenVLA L2norm k=0.7 = seed43 only, random = seed42; cross-seed caveat. seed42 L2norm k=0.7 running on westd-38929.\\n² OpenVLA random k=0.3 result file missing, re-running on westd-38929.\\n³ D137 multi-seed: X-VLA random k=0.5 seed43=71.0% (seed42=70.6%, Δ=0.4pp). Gap reproducible.\\n\\n**Per-task X-VLA k=0.5 (Reviewer-verified, 9/10 tasks random > L2norm):**\\n\\n| Task | Baseline | L2 s42 | L2 s43 | Random s42 | Δ(R-L2) |\\n|------|---------|--------|--------|------------|---------|\\n| T0 alphabet_soup | 98% | 58% | 56% | **96%** | +38 |\\n| T1 cream_cheese | 100% | 2% | 6% | 46% | +44 |\\n| T4 ketchup | 100% | 42% | 40% | **100%** | **+58** |\\n| T7 milk | 100% | 38% | 38% | 82% | +44 |\\n| T9 orange_juice | 100% | 68% | 70% | **100%** | +32 |\\n| T6 butter | 100% | 2% | 2% | 2% | 0 (both crash) |\\n\\nL2norm two seeds highly consistent (s42 vs s43 diff <6pp) → not RNG noise.\\nT6: baseline=100% but both methods=2% → highly localized visual cue, k=0.5 always loses it regardless of method.\\nT4/T9: Random recovers to baseline → L2norm systematically discards the critical tokens for these tasks.\\n\\n**Pattern**: Low CV (X-VLA) → importance-based selection degenerates at aggressive k → random better. High CV (OpenVLA) → meaningful importance differentiation → L2 norm better.\\n\\n**Mechanism hypothesis** (Reviewer: consistent with data, needs direct evidence): X-VLA's linear projection + BART encoder produces tokens with relatively uniform L2 norms (CV=0.151). At aggressive compression (k=0.5 = keeping 25 of 50 tokens), L2 norm selects the \\\"slightly larger\\\" tokens which tend to be spatially clustered → loses spatial diversity → catastrophic. Random preserves spatial coverage stochastically → dramatically better.\\n\\n**⚠️ Visualization needed (Reviewer warning)**: Must produce token position visualization — for same input image, show which tokens L2 norm vs random retains. If L2 norm shows spatial clustering, mechanism is proven. This should be a key figure (§4.6 or Fig 4).\\n\\n**Implication for practitioners**: CV diagnoses → predicts tolerance → prescribes strategy at aggressive compression. Low CV + aggressive k (≤0.5) → random/position-based. High CV → importance-based at all k. Mild compression (k≥0.8) → method choice doesn't matter regardless of CV.\\n\\n**Pending**: X-VLA random k=0.7 (crossover), multi-seed k=0.5, token position visualization, OpenVLA L2norm k=0.7 seed42, k_ratio=null fix.\\n\\n## Story Spine\\n\\n**Problem**: Vision token efficiency is critical for real-time VLA deployment. Growing literature proposes inference-time token reduction (FastV, VLA-IAP, H2O, ToMe). These methods succeed on some VLAs but their behavior across different architectures is unstudied.\\n\\n**Gap**: No work has systematically compared token pruning robustness across VLA architectures. The implicit assumption that \\\"token pruning works or fails uniformly\\\" is untested. The critical architectural factor determining prunability is unknown.\\n\\n**Discovery**: We find that VLA token pruning robustness is governed by two interacting axes. **Axis 1 — Token Coupling**: connector architecture determines whether tokens are independent (linear proj, MLP) or entangled (BART encoder, pixel-shuffle), diagnosed by importance CV (0.038→0.314). **Axis 2 — Task Complexity**: multi-step tasks (Goal/Long) amplify pruning damage on entangling connectors — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at k=0.9. Evidence from 5 VLA models × 4 LIBERO suites:\\n- **Token-independent** (π0, π0.5 linear; OpenVLA, OFT MLP): graded degradation, CV 0.038–0.219\\n- **Token-entangling** (X-VLA BART 12L; SmolVLA pixel-shuffle): task-dependent collapse — tolerate simple tasks, catastrophic on complex tasks. CV 0.151–0.314\\nCV predicts both pruning tolerance and optimal strategy (L2norm hurts low-CV models, helps high-CV).\\n\\n**Solution**: Diagnose-then-Compress framework. Step 1: Token importance CV provides zero-cost diagnostic for pruning tolerance (one forward pass). Step 2: VTR (Vision Token Re-encoding) provides universal compression. For pixel-shuffle: recovers from 0% (hard pruning) to ~59% ≈ baseline (59.2%), M-curve flat (D105: M=16 56.9% ≈ M=128 58.0%, near-lossless at any compression ratio). For MLP projector: D109 C4-ext = 0% SR (overfitting at M=128); VTC-only M=32/M=64 in progress.\\n\\n**Headline result**: \\\"Across 5 VLA models (450M-7B) × 4 task suites, we find that token pruning robustness is governed by two axes: connector architecture (token-independent vs token-entangling, diagnosed by importance CV) and task complexity. Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio; SmolVLA collapses to 0% at 5% removal regardless of task. CV (0.038→0.314) predicts both pruning tolerance and optimal strategy: importance-based pruning is actively harmful on low-CV architectures (+28-36pp gap favoring random), while it helps on high-CV models (+1-6pp). VTR recovers to ~59% (≈baseline) at any compression ratio (0-87.5%) where hard deletion achieves 0%.\\\"\\n\\n## Paper Structure (7-model version)\\n\\n1. **Introduction**: VLA efficiency motivation → diverse connector architectures → 2-axis framework discovery (D171) → Diagnose-then-Compress framework\\n2. **Background**: 5 VLA models, 3 connector families (linear/MLP/pixel-shuffle), 4 LIBERO suites, token flow analysis\\n3. **Experimental Setup**: 5 models, LIBERO benchmark (4 suites: Object/Spatial/Goal/Long), pruning protocol, VTR compression, diagnostic metrics\\n4. **Main Results**:\\n   - §4.1: 2-Axis Framework Overview (Table 1: 5 models × token coupling axis; Table 2: cross-suite interaction — connector × task complexity)\\n   - §4.2: Token-Entangling Catastrophic — pixel-shuffle cliff-edge (SmolVLA, all configs 0% regardless of task)\\n   - §4.3: Token-Independent Graded — MLP degradation (OpenVLA 6-point curve + OFT entropy confirmation)\\n   - §4.4: Token-Independent Tolerant — linear projection (π0 + π0.5, controlled comparison with OpenVLA)\\n   - §4.5: Task Complexity Amplification — X-VLA cross-suite (Object 97.6% vs Goal 70.2% vs Long ~53% at same k)\\n   - §4.6: Pruning Strategy Depends on CV (D132: low-CV random>>L2norm, high-CV L2norm>>random)\\n   - §4.7: VTR overcomes cliff-edge (M-curve flat + architecture independence)\\n   - (REMOVED — D119: LIBERO-Plus L1 SR=3.3% floor effect, noted in Discussion §6)\\n5. **Analysis**:\\n   - §5.1: Why pixel_shuffle creates entanglement (spatial folding + controlled comparison)\\n   - §5.2: Diagnostic metric — Entropy + CV composite (D104, 4-model validation)\\n   - §5.3: Re-encoding mechanism (M=128 passthrough + MLP adapter + M-curve flat D105)\\n6. **Discussion**: Design implications, limitations (sim-only, no real robot), future work\\n7. **Conclusion**: 5 claims summary\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Only 2 models → **FULLY ADDRESSED**\\n**Response**: Now 5 models (SmolVLA, OpenVLA, OpenVLA-OFT, π0, X-VLA) across 3 connector families (pixel-shuffle, 3-layer MLP, linear projection) and 4 model sizes (450M-7B). Each connector class has ≥2 models.\\n\\n### RC2: Model size confound (450M vs 7B) → **FULLY ADDRESSED**\\n**Response**: π0 (3.3B, linear) is pruning-immune while OpenVLA (7B, MLP) degrades 61% at k=0.1. Larger model is MORE vulnerable, not less — directly falsifies \\\"larger models are more robust\\\" hypothesis. X-VLA (880M, linear) also immune, matching π0 behavior despite 4× smaller. Size is not the explanatory variable; connector type is.\\n\\n### RC3: Why not test SmolVLA without pixel_shuffle?\\n**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.\\n\\n### RC4: Smart compression — is re-encoding or compression the mechanism?\\n**Response (corrected with baseline=59.2%)**: VTR achieves near-lossless compression at any ratio — the M-curve is flat (M=16: 56.9% → M=128: 58.0%, all within ±3pp of baseline 59.2%). Two lines of evidence: (1) M=128 passthrough (58.0%) ≈ baseline (59.2%) — re-encoding recovers spatial entanglement to baseline level, not above it. (2) Architecture control: MLP adapter (63.4%) ≈ cross-attention (60.1%) with CI overlap — any re-encoding mechanism works. The key contribution is recovery from 0% (hard pruning) to ~59% (baseline), not exceeding baseline. Compression ratio is a free parameter with negligible SR cost.\\n\\n### RC5: Relationship to VLA-IAP\\n**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.\\n\\n### RC6: Is this just \\\"different models behave differently\\\"?\\n**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.\\n\\n### RC7: Only one benchmark (LIBERO-Object) → **ADDRESSING (D115, D119)**\\n**Response**: Expanded to ALL 4 LIBERO suites (Object/Spatial/Goal/Long) — 4 genuinely different task distributions (manipulation skills, spatial reasoning, goal-conditioned, long-horizon). Taxonomy consistency validated across suites. LIBERO-Plus robustness benchmark tested (D119) but abandoned: L1 camera perturbation collapses OpenVLA to SR=3.3% (consistent with leaderboard 0.8%), creating floor effect with no room for pruning analysis. This floor effect itself is noted in Discussion as evidence of general VLA brittleness under distribution shift. Sim-only limitation acknowledged.\\n\\n## All Experimental Evidence (confirmed)\\n\\n### SmolVLA Cliff-Edge\\n- Fine-tuned baseline (Object): 44.8% (224/500) — ⚠️ OLD reproduced checkpoint, superseded by official HF = 59.2%\\n- 6 pruning conditions (random/ACIS/ToMe × k=0.5/0.7/0.9): all 0%\\n- Geometric prior (Sobel) k=0.5/0.7/0.9: all 0%\\n- Attention entropy: 0.952 (flat, TV=0.05)\\n- Official checkpoint Object: 59.2% → 0% at k=0.5\\n- Official checkpoint Spatial: 43.8% → 0.6% (3/500, CI [0.2%, 1.7%]) at k=0.5 — near-zero, confirms cliff-edge across suites\\n- LoRA-FT checkpoint Spatial: 8.0% (per-task: [24,8,4,24,0,2,2,2,14,0]) — LoRA trained on Object only, does not transfer to Spatial. Use official checkpoint for cross-suite SmolVLA analysis.\\n\\n### OpenVLA Degradation Curve\\n- k=1.0: 74.0% (370/500)\\n- k=0.95: 69.4% (-6% relative)\\n- k=0.9: 62.0% (-16% relative)\\n- k=0.7: 49.0% (245/500, -34% relative)\\n- k=0.5: 37.4% (187/500, -49% relative)\\n- k=0.3: 20.6% (103/500, -72% relative)\\n- Entropy: 0.639 (progressive sharpening, TV=0.50)\\n\\n### Cross-Model Pruning Taxonomy (7 models — D100, D120, D127)\\n| Model | Connector | Tokens | k=0.1 norm_L1 | k=0.5 norm_L1 | Class |\\n|-------|-----------|--------|---------------|---------------|-------|\\n| π0 (3.3B) | Pure linear proj | 256 | 0.976 (-2.4%) | 0.983 | Immune |\\n| π0.5 (4B) | Pure linear proj (×√d scaling) | 768 (3×256) | **98.2%** (491/500) | **L2norm=33.4%, random=69.4%** | **Uniformly Critical (D139)**: L2norm catastrophic (-64.8pp), random tolerant (-28.8pp), gap=+36pp. CV=0.055. |\\n| X-VLA (880M) | Linear + BART 12L | 50 | ~1.00 | ~1.00 | Threshold-graded (k=0.7: 56.2%) |\\n| OpenVLA (7B) | 3-layer MLP | 256 | 1.608 (+61%) | 1.167 (+17%) | Smooth graded |\\n| OFT (7B) | 3-layer MLP (DINOv2+SigLIP fused) | **512** | N/A | N/A | D136: Blackwell GPU incompatible. CV=0.219≈OpenVLA → graded. Cite official ~97% baseline. |\\n| SmolVLA (450M) | Pixel-shuffle | 128 | — | 0% cliff | Catastrophic |\\n\\nDiagnostic metrics (D104+D106+D120: CV as continuous predictor, 7 models):\\n| Model | Connector (effective) | Entropy | CV | Pruning Behavior |\\n|-------|----------------------|---------|------|------------------|\\n| π0 | Pure linear proj | 0.959 | 0.038 | Immune (offline, k=0.1 improves) |\\n| π0.5 | Pure linear proj (×√d) | pending | 0.055 | **Uniformly Critical (D139)**: L2norm=33.4%, random=69.4%, gap=+36pp. Monotonic trend extreme. |\\n| X-VLA | Linear proj + BART enc (12L) | **0.614** | **0.151** | Threshold-graded: robust k≥0.9, cliff k=0.7 (56.2%). D127: random=L2norm at k=0.9 |\\n| OpenVLA | 3-layer MLP (GELU) | 0.661 | 0.215 | Graded (74→37.4% at k=0.5) |\\n| OFT | 3-layer MLP (DINOv2+SigLIP, **512 tokens**) | 0.667 | 0.219 | D136: Graded expected (CV≈OpenVLA). Blackwell GPU incompatible, no LIBERO SR. |\\n| SmolVLA | Pixel-shuffle (16×) | 0.952 | **0.314** | Catastrophic (0% at k=0.95) |\\n\\nKey insights (updated with 7-model data):\\n1. **CV is a continuous predictor**: 0.038 → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 maps to decreasing pruning tolerance. NOT a 3-class discrete classifier.\\n2. **X-VLA CV=0.151 correctly predicted its intermediate behavior** — closer to OpenVLA (0.215) than π0 (0.038), matching k=0.7 SR ≈ OpenVLA k=0.7.\\n3. **X-VLA entropy=0.614 ≈ OpenVLA 0.661** — both have BART/MLP non-linear mixing. X-VLA is NOT \\\"high entropy\\\" like π0.\\n4. **Effective connector complexity matters more than nominal label**: X-VLA is \\\"linear proj\\\" but BART encoder introduces 12 transformer layers of mixing. Paper should discuss \\\"effective connector\\\" = projection + any intermediate processing.\\n5. OFT entropy 0.667 ≈ Standard 0.661 → action head does not affect attention structure\\n6. Framing: CV captures \\\"degree of non-linear mixing in the vision-to-LLM pathway.\\\" More mixing → higher CV → less tolerant of pruning.\\n\\n### Smart Compress (Learned Re-encoding)\\nCross-attention (VTC) M sweep (3-seed where available):\\n- M=16: **56.9% ± 1.3pp** (3-seed: 55.8/58.4/56.5) — 87.5% compression, ZERO loss vs M=128\\n- M=32: 60.1±1.3% (3-seed: 61.6/59.2/59.6)\\n- M=64: 62.0±2.3% (3-seed: 61.6/60.0/64.4)\\n- M=96: 54.5±3.2% (3-seed: 52.6/58.2/52.8) — highest variance\\n- M=128: 58.0±3.5pp (3-seed: 59.8/54.0/60.2) — passthrough control\\n- **D102 CONFIRMED: M-curve is flat.** M=16 (56.9%) = M=128 (58.0%), difference < 1.1pp. VTC achieves near-lossless compression at ANY ratio for pixel-shuffle connector. All M values within ±5pp of baseline ~59%.\\n\\nMLP adapter (M=32, 3-seed):\\n- seed42: 65.2% (326/500), seed43: 64.6% (323/500), seed44: 60.4% (302/500)\\n- Mean: 63.4% ± 2.6 vs VTC M=32 mean 60.1% ± 1.3\\n- t-test p≈0.15, no significant difference — confirms architecture-independence\\n\\n### D109: VTR on OpenVLA (MLP projector) — FAILED\\n- C4-ext M=128 at 20K steps: **0% SR** (0/44 episodes before eval termination)\\n- Failure mode: model outputs identical action every timestep (severe overfitting)\\n- Interpretation: VTR adds unnecessary complexity for MLP projector tokens (already individually meaningful). VTR specifically solves pixel-shuffle entanglement.\\n- VTC-only M=32 and M=64 training in progress on westd-41074:2-3\\n\\n### Cross-Suite VTR Generalization (SmolVLA)\\n- M=32 Spatial: 53.2% (vs official Spatial baseline 44.6% per ROADMAP, vs pruning 0.6% — recovery from cliff-edge, +8.6pp over baseline)\\n- M=32 Goal: 56.4% (vs official Goal baseline 60.8% per ROADMAP, vs pruning 0% — recovery from cliff-edge, -4.4pp below baseline)\\n- ⚠️ Cross-suite baselines need reconciliation: paper_framing previously used 43.8%/63.0%, ROADMAP uses 44.6%/60.8%. Use n=500 official checkpoint data as ground truth.\\n- Note: VTR trained on Object suite, evaluated cross-suite. Official baselines from different checkpoint (official vs LoRA-FT); comparisons should emphasize recovery from 0% rather than absolute performance vs uncompressed.\\n\\n### Pairwise Statistical Tests (Welch's t-test, n=3 per condition)\\n- M=32 VTC vs M=32 MLP: p=0.150 (not significant) — confirms architecture-independence\\n- M=64 VTC vs M=96 VTC: p=0.034 (significant) — M=96 dip confirmed real\\n- M=32 MLP vs M=96 VTC: p=0.022 (significant) — M=96 underperforms\\n- M=32/M=64/M=128 VTC cluster: all pairwise p>0.25 — robust across M values\\n- Bonferroni note: no pair survives correction at 10 tests; n=3 limits power (~0.2 for medium effects)\\n\\n### Supplementary\\n- Inference latency: 6% speedup at M=32\\n- KV-cache: 75% memory reduction at M=32\\n\", \"total_chars\": 51958, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "a17e734f-afd5-4cea-84bc-58c3c91ae9af",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/5c041521-e8e2-414d-abe9-e8e6614720ac/tool-results/toolu_01GQsGzoo6GSmBfzBfB3g6oc.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — importance_margin_vla_compress\\\\n\\\\n## Target Venue\\\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\\\n\\\\n## Title (working)\\\\n\\\\\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\\\\\"threshold-graded\\\\\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\\\n\\\\n**Axis 1 — Token Coupling (connector architecture):**\\\\n| Type | Connectors | CV Range | Mechanism |\\\\n|------|-----------|----------|-----------|\\\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\\\n\\\\n**Axis 2 — Task Complexity:**\\\\n| Level | Suites | Characteristics |\\\\n|-------|--------|----------------|\\\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\\\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\\\\n\\\\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\\\\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\\\\n- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance\\\\n- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen\\\\n- Token-independent (π0.5 Goal/Long): data collecting, expected smaller amplification\\\\n\\\\n**CV remains the primary Axis-1 diagnostic** — predicts both pruning tolerance and optimal strategy (Claim 5). Task complexity (Axis 2) explains within-model variance across suites that the old taxonomy could not capture.\\\\n\\\\n_Original per-connector evidence (from Object-suite 4-class taxonomy) retained below; reinterpret through 2-axis lens:_\\\\n- **Linear projection** (π0 3.3B, π0.5 4B): **\\\\\\\"Uniformly Critical\\\\\\\" (D139)**. NOT immune. π0.5 baseline=98.2%, random k=0.5=**69.4%** (-28.8pp), L2norm k=0.5=**33.4%** (-64.8pp). Gap=+36.0pp, random wins 9/10 tasks. Low CV (0.038/0.055) = uniformly important tokens → L2norm's systematic bias selects spatially clustered tokens → catastrophic at k≤0.7. Random preserves spatial coverage → 2× better at k=0.5. **L2norm extended curve:** k=0.1=2.6% (collapse) → k=0.3=51.0% → k=0.5=33.4% (valley) → k=0.7=55.0% → k=0.9=98.2%. V-shape with collapse at extreme compression. CV=0.055 makes this the extreme case of the monotonic diagnostic trend. **⚠️ MAJOR FINDING (2026-05-22, fully investigated):** π0.5 random pruning exhibits sharp cliff at k=0.85-0.925 with non-monotonic recovery:\\\\n  - k=0.95: 71.1% FINAL (seed42 500ep; seed43=72.8%) — already 27pp below baseline\\\\n  - k=0.925: **27.6%** FINAL (seed42) — cliff entry point, 43pp drop from k=0.95\\\\n  - k=0.9: 10.8%±1.2pp (dual seed: seed42=12.0%, seed43=9.6%) — **87.4pp gap vs L2norm k=0.9=98.2%**\\\\n  - k=0.85: **5.0%** FINAL (seed42 v2=4.4%) — cliff floor\\\\n  - k=0.7: 75.5% (mean), k=0.5: 68.9%, k=0.3: 36.4% — recovery zone\\\\n  - Cliff profile: 71.1%(k=0.95) → 27.6%(k=0.925) → 10.8%(k=0.9) → 5.0%(k=0.85) — 66pp collapse over 10% keep ratio change\\\\n  **D151 (2026-05-22): Cliff is RANDOM-SPECIFIC.** L2norm maintains 98.0-99.2% plateau across the entire cliff zone:\\\\n  - L2norm k=0.95=98.2%, k=0.925=99.2%, k=0.9=98.2%, k=0.85=98.0% — zero degradation\\\\n  - Random k=0.925: 27.6% vs L2norm=99.2% → **71.6pp gap** (maximum separation)\\\\n  - Random k=0.85: 5.0% vs L2norm=98.0% → **93.0pp gap**\\\\n  - L2norm succeeds because deterministic selection consistently retains the same token subset; random sampling creates variable damage\\\\n  **D152 (2026-05-22): Cliff is TASK-SPECIFIC.** Object tasks collapse catastrophically, Spatial tasks degrade but survive:\\\\n  - Random k=0.9: Object=10.8% vs Spatial=54.6% — Spatial retains 5× more SR\\\\n  - Random k=0.85: Object=5.0% vs Spatial=TBD (collecting)\\\\n  - Within Object suite: all 10 tasks collapse at k=0.9 (2-16%). Within Spatial suite: degradation but not catastrophic.\\\\n  - Mechanism: Object tasks require precise object identity discrimination (visually similar objects); Spatial tasks rely on spatial layout (more distributed visual information). Random token loss destroys fine-grained discriminative features needed for Object before destroying spatial layout features.\\\\n  **Fixed-mask experiment (D149) NEGATES temporal inconsistency hypothesis:** per-episode fixed mask T0=12% = per-call random T0=12%. Temporal mask variation is NOT the cause.\\\\n  **D153: Cross-suite LIBERO-Spatial — weaker non-monotonicity, no catastrophic dip (2026-05-22)**\\\\n  Baseline: 97.2%. Random pruning profile:\\\\n  | k | Object | Spatial | Δ | Pattern |\\\\n  |---|--------|---------|---|---------|\\\\n  | 0.95 | 71.1% | deploying | — | — |\\\\n  | 0.925 | 28.8% (2-seed) | — | — | — |\\\\n  | 0.9 | 10.8% | 54.6% | +43.8pp | Spatial 5× more robust |\\\\n  | 0.85 | 5.0% | **58.4%** | **+53pp** | Maximum divergence |\\\\n  | 0.7 | 75.5% | 74.4% | -1pp | Suite-independent |\\\\n  | 0.5 | 69.4% | 71.6% | +2pp | Suite-independent |\\\\n  | 0.3 | 36.4% | 49.6% | +13pp | Spatial more robust |\\\\n  L2norm Spatial: k=0.9=95.0%, k=0.7=67.0%, k=0.5=55.6%, k=0.3=57.2%. L2norm k=0.95/k=0.85 deploying.\\\\n  **Object has deep V-shape dip**: 5%(k=0.85) → 10.8%(k=0.9) → 75.5%(k=0.7), 70pp recovery from cliff floor. **Spatial has weaker non-monotonicity**: k=0.5(71.6%) > k=0.85(58.4%) > k=0.9(54.6%), but no catastrophic collapse — floor stays above 50% vs Object's 5% floor. The cliff zone gap (Object 5% vs Spatial 58%) reflects concentrated vs distributed critical token patterns.\\\\n  **Mechanism**: Object tasks have **concentrated** critical tokens (object identity discrimination — visually similar objects). Random removal at cliff zone destroys these concentrated patches → catastrophic. Spatial tasks have **distributed** critical information (layout patches spread across image). Random removal damages any random subset but never completely destroys spatial signal → graceful degradation.\\\\n  **Paper value**: Two distinct cliff behavior modes — **concentrated-critical (Object)** vs **distributed-critical (Spatial)** — as a function of task semantics. Pruning sensitivity = f(connector, method, k, task_semantics). Suite-independent at moderate k (0.5-0.7), suite-dependent at cliff zone (0.85-0.95).\\\\n  **Paper value:** strengthens \\\\\\\"uniformly critical\\\\\\\" class — even uniform importance distribution doesn't make pruning safe. Simple deletion fails; learned compression (VTR) needed.\\\\n- **Linear projection + deep post-processing** (X-VLA 880M, linear proj + 12-layer BART encoder): robust k≥0.9 (97.6% SR), **cliff at k=0.7 (56.2% SR, -43pp)**. BART encoder introduces non-linear mixing that creates partial token dependencies. CV=0.151. **D127: random pruning k=0.9=97.8% ≈ L2norm 97.6% — pruning method independence confirmed for low-CV connectors.**\\\\n- **Multi-layer MLP** (OpenVLA 7B, OpenVLA-OFT 7B): graded degradation. k=0.1 normalized loss = 1.608 (+61%). Non-linear mixing creates partial dependencies. OFT entropy (0.667) ≈ Standard (0.661), CV(OFT)=0.219 ≈ CV(OpenVLA)=0.215, confirming connector — not action head — determines attention structure. **D136: OFT LIBERO eval infeasible (Blackwell GPU SDPA incompatibility, requires A100+torch2.2). OFT included via CV/entropy analysis only; cite official baseline ~97% SR.** π0.5 baseline confirmed 98.2% (D135).\\\\n- **Pixel-shuffle** (SmolVLA 450M): catastrophic cliff-edge. k=0.95 (removing 5%) → 0% SR. Spatial folding creates irreversible entanglement. **D147: Official HF checkpoint (HuggingFaceVLA/smolvla_libero) confirms identical cliff — random k=0.95 = 0%, L2norm k=0.95 = 0%. Cliff is architectural, not training artifact. Resolves W-C2.** **Dual-seed confirmed (2026-05-22):** Baseline 59.4%±0.3pp (seed42=59.2%, seed43=59.6%), random k=0.95: 0.1% mean (0.0%/0.2%), random k=0.5: 0.0%, L2norm k=0.95: 0.2% mean (0.4%/0.0%). All pruning ≤0.2% across both seeds. cqa1 supplementary: L2norm k=0.7=0%, random k=0.9=0%.\\\\n\\\\nKey controlled comparison: π0 (256 tokens, linear) vs OpenVLA (256 tokens, 3-layer MLP) — same token count, same encoder lineage, only connector differs. k=0.1: π0 improves 2.4% vs OpenVLA degrades 61%. This isolates connector as the causal factor.\\\\n\\\\nLearned re-encoding (VTR) overcomes the cliff-edge: cross-attention 60.1±1.3% and MLP adapter 63.4±2.6% at M=32 (vs 0% hard pruning), with M=128 passthrough (58.0%±3.5, 3-seed) ≈ baseline 59.2% — VTR recovers to baseline rather than exceeding it. SmolVLA M-curve confirmed flat (D105): M=16 (56.9%±1.3) = M=128 (58.0%±3.5), all 5 M-values within ±3pp of baseline 59.2%. VTR achieves near-lossless compression at any ratio (0-87.5%) for pixel-shuffle connectors.\\\\n\\\\n## Paper Identity (Round 5 Upgrade — D171 2-Axis, 2026-05-22)\\\\n**ANALYSIS + METHOD paper.** (D091 → D097 → D171: 5 models × 3 connector families × 4 LIBERO suites)\\\\n\\\\n**Analysis contribution (primary)**: First systematic study revealing that VLA token pruning robustness is determined by the interaction of two axes: (1) connector architecture (token-independent vs token-entangling, diagnosed by importance CV 0.038→0.314) and (2) task complexity (simple vs multi-step). Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio. 5 models × 4 suites × 4 model sizes (450M-7B) eliminate confounds. No competing work does cross-architecture, cross-task VLA token analysis.\\\\n\\\\n**Method contribution**: Diagnose-then-Compress framework:\\\\n- Step 1: **Connector Compressibility Diagnostic** (D104: resolved)\\\\n  - **Primary metric: Importance CV** (token importance heterogeneity) — zero-cost, one forward pass\\\\n  - CV forms continuous spectrum predicting pruning tolerance: π0=0.038 < π0.5=0.055 < X-VLA=0.151 < OpenVLA=0.215 < OFT=0.219 < SmolVLA=0.314\\\\n  - ⚠️ D106+: X-VLA CV=0.151 correctly predicted its intermediate pruning behavior (k=0.7 ≈50% SR ≈ OpenVLA k=0.7). CV is a valid continuous predictor, NOT a 3-class discrete classifier.\\\\n  - **Key discovery**: X-VLA \\\\\\\"linear projection\\\\\\\" passes through BART encoder (12 transformer layers) before decoder → introduces non-linear mixing → explains CV=0.151 (much higher than π0=0.038 pure linear)\\\\n  - **Entropy as mechanistic supplement** (CV is primary; entropy is supplementary):\\\\n    - π0: entropy=0.959 (per-layer mean, range 0.931–0.983), CV=0.038 — uniform & independent → most tolerant\\\\n    - **π0.5: entropy=0.666, CV=0.055** — similar entropy to OpenVLA (0.661) but vastly different pruning behavior (CV correctly differentiates)\\\\n    - X-VLA: entropy=0.614, CV=0.151 — selective & BART-mixed → intermediate\\\\n    - OpenVLA: entropy=0.661, CV=0.215 — selective & MLP-mixed → graded\\\\n    - SmolVLA: entropy=0.952, CV=0.314 — near-uniform but spatially entangled → catastrophic\\\\n  - **KEY INSIGHT**: Entropy clusters π0.5/X-VLA/OpenVLA together (0.61-0.67) despite very different pruning behaviors. CV correctly separates them (0.055 vs 0.151 vs 0.215). Entropy fails as diagnostic because it doesn't capture token independence structure — only attention distribution shape.\\\\n  - ✅ Batch 2 complete: continuous CV spectrum confirmed (X-VLA full 8-point curve validates threshold-graded class)\\\\n  - Supplementary: lightweight pruning probe (remove 5%, one forward pass) as practitioner-friendly alternative\\\\n- Step 2: VTR (Vision Token Re-encoding) — lightweight cross-attention module (~22M params) for universal compression\\\\n- For entangled tokens (pixel-shuffle): recovers from 0% (hard pruning) to ~59% ≈ baseline, M-curve flat D105 (near-lossless compression at any ratio 0-87.5%)\\\\n- For independent tokens (MLP projector): **D109 C4-ext confirmed 0% SR** at 20K steps (M=128, severe overfitting — model outputs identical action every step). VTR on MLP projector does NOT improve SR; reframed as \\\\\\\"VTR ceiling depends on connector type\\\\\\\" finding. User directive: performance degradation acceptable if efficiency improves — VTR value is 75% KV-cache reduction + attention speedup. VTC-only M=32/M=64 training in progress to test whether smaller M values fare better.\\\\n\\\\n**Differentiation from concurrent work**: 4 concurrent works (Compressor-VLA, SpecPrune-VLA, LightVLA ICRA'26, See What Matters ICML'26) all propose pruning on MLP-projector VLAs. We (1) explain why pruning fails on pixel-shuffle architectures, (2) identify why pruning succeeds on linear projection (tokens are truly independent), and (3) propose a re-encoding method motivated by the diagnostic analysis.\\\\n\\\\n**Model coverage**: 5 VLA models × 3 connector families × 4 LIBERO suites × 4 model sizes (450M-7B). RC1 (only 2 models), RC2 (size confound), and RC7 (only one suite) fully addressed.\\\\n\\\\n## Core Claims (5 claims, expanded from 4)\\\\n\\\\n### Claim 1: 2-Axis Compressibility Framework (D107 → D171 UPGRADED)\\\\nPruning sensitivity = f(connector_architecture, task_complexity). Two axes interact:\\\\n\\\\n**Axis 1 — Token Coupling (connector determines base sensitivity):**\\\\n- **Token-independent** connectors (pure linear π0/π0.5, MLP OpenVLA/OFT): tokens retain spatial meaning → pruning damage is local, graded degradation\\\\n- **Token-entangling** connectors (BART X-VLA, pixel-shuffle SmolVLA): cross-token dependencies → pruning damage cascades\\\\n\\\\n**Axis 2 — Task Complexity (task amplifies entangling-connector sensitivity):**\\\\n- Simple tasks (Object): even entangling connectors tolerate mild pruning (X-VLA k=0.9=97.6%)\\\\n- Complex tasks (Goal/Long): entangling connectors collapse (X-VLA Goal k=0.9=70.2%, Long k=0.95≈53%)\\\\n- Key: same connector, same k, same method — **only task differs** → 27.8pp drop (Object→Goal)\\\\n\\\\n**CV predicts Axis-1 position**: 0.038 (most independent) → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 (most entangled)\\\\n\\\\n**Evidence**: 5 models, 3 connector families, 4 LIBERO suites, 4 model sizes (450M-7B). Key controlled comparisons:\\\\n1. π0 (256 tokens, linear) k=0.1 = 0.976 vs OpenVLA (256 tokens, MLP) k=0.1 = 1.608 → connector isolates base sensitivity\\\\n2. X-VLA Object k=0.9 = 97.6% vs X-VLA Goal k=0.9 = 70.2% → task complexity isolates amplification\\\\n3. SmolVLA Object = 0% at k=0.95 → extreme entanglement dominates even on simple tasks\\\\n\\\\n🔴 **D108→D127→D130→D132: Pruning method comparison — MAJOR REVERSAL at aggressive compression**\\\\n\\\\nBoth L2 norm and random pruning tested on X-VLA and OpenVLA. **CV predicts not just tolerance but optimal strategy**:\\\\n\\\\n- **OpenVLA (MLP, CV=0.215)**: L2 norm consistently ≥ random at all k values. High CV → meaningful importance differentiation → L2 norm selection effective.\\\\n  - k=0.95: L2norm=69.4% ≈ random=69.2% (+0.2pp)\\\\n  - k=0.7: L2norm=49.8%¹ > random=44.4% (+5.4pp). ¹seed43 only, seed42 running on westd-38929:2\\\\n  - k=0.5: L2norm=39.2% > random=35.8% (+3.4pp)\\\\n  - k=0.3: L2norm=25.0%, random=pending (re-running)\\\\n\\\\n- **X-VLA (BART, CV=0.151)**: 🔴 **REVERSAL** — L2 norm ≈ random at mild compression, but **random MASSIVELY outperforms L2 norm at aggressive compression**:\\\\n  - k=0.9: L2norm=97.6% ≈ random=97.8% (≈0pp)\\\\n  - k=0.85: L2norm=68.0% > random=63.6% (+4.4pp, cliff boundary)\\\\n  - k=0.8: L2norm=89.0% ≈ random=89.4% (≈0pp, non-monotonic recovery)\\\\n  - **k=0.5: L2norm=42.6% << random=70.6% (-28.0pp!)** — CI non-overlapping, statistically significant. Random wins 9/10 tasks; T4 ketchup: L2norm=42% vs random=100% (+58pp). Only T6 butter both crash at 2%.\\\\n  - k=0.7: L2norm=56.2% << random=65.2% (+9pp). Crossover confirmed at k≈0.8.\\\\n  - **k=0.3: L2norm=22.8% << random=62.8% (+40pp!)** — gap scales monotonically with compression.\\\\n  - **D137**: seed43 k=0.5=71.0% confirms seed42=70.6% (Δ=0.4pp). Gap reproducible.\\\\n\\\\n- **SmolVLA**: all methods = 0% at all k values → trivially method independent.\\\\n\\\\n**KEY INSIGHT (D132→D137)**: Importance-based pruning can be **actively harmful** on low-CV architectures under aggressive compression, and the harm SCALES: +9pp@k=0.7, +28pp@k=0.5, +40pp@k=0.3. Mechanism: X-VLA's linear projection + BART encoder produces relatively uniform token norms (CV=0.151). L2 norm selection on a near-uniform distribution degenerates into selecting spatially clustered tokens → loses diversity → catastrophic failure. Random pruning preserves spatial coverage → dramatically better. Multi-seed confirmed.\\\\n\\\\n**This strengthens the paper**: CV serves as a dual predictor — predicts both (1) pruning tolerance ceiling and (2) whether importance-based methods help or hurt. Connector architecture determines both via its effect on token importance distribution.\\\\n\\\\n**Paper narrative upgrade**: From \\\\\\\"connector determines compressibility\\\\\\\" to \\\\\\\"connector determines both compressibility AND optimal compression strategy.\\\\\\\" This is a significantly stronger and more novel contribution.\\\\n\\\\n**Pending data**: X-VLA random k=0.7 (crossover characterization), multi-seed k=0.5 random (robustness). OpenVLA L2norm k_ratio=null provenance issue needs fixing.\\\\n\\\\n### Claim 2: Pixel Shuffle Creates Irreversible Token Entanglement\\\\nSmolVLA's pixel_shuffle connector spatially folds 1024 SigLIP patches into 64 tokens per camera (16x compression). Each resulting token encodes a 32x32 pixel region via channel-to-spatial reorganization. This creates extreme cross-token spatial entanglement: removing any single token eliminates an entire spatial quadrant's information with no redundancy to compensate.\\\\n\\\\n**Evidence**:\\\\n- k=0.95 (remove only 7/128 tokens = 5.5%) = 0% SR — even minimal removal is catastrophic\\\\n- k=0.9 (remove 13/128 tokens) = 0% SR\\\\n- Geometric prior (Sobel edge) k=0.5/0.7/0.9 = all 0%\\\\n- Attention entropy ratio 0.952 (near-uniform, TV=0.05)\\\\n- Official checkpoint Object (59.2% baseline) cliff-edge at k=0.5 → 0%\\\\n- Official checkpoint Spatial (43.8% baseline) cliff-edge at k=0.5 → 0.6% (3/500, CI [0.2%, 1.7%])\\\\n\\\\n### Claim 3a: Linear Projection → Depends on Effective Pipeline (D107: RESOLVED)\\\\nPure linear projection (π0): immune. Linear projection + deep post-processing (X-VLA, BART 12L): \\\\\\\"robust-then-cliff\\\\\\\" — immune at k≥0.9, cliff at k=0.7, then graded degradation. The BART encoder introduces non-linear cross-token mixing that explains intermediate CV=0.151 and the cliff pattern.\\\\n\\\\n**Evidence** (X-VLA LIBERO SR — Batch 1 + Batch 2 COMPLETE, full 8-point curve):\\\\n- k=1.0: **99.2%** (baseline, 496/500) — per-task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]\\\\n- k=0.95: **99.0%** (-0.2pp) — per-task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]\\\\n- k=0.9: **97.6%** (-1.6pp) — per-task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]\\\\n- k=0.7: **56.2%** (-43pp, CLIFF — 281/500) — per-task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]\\\\n- k=0.5: **42.6%** (-57pp) — Batch 2 confirmed (MSH fix applied)\\\\n- k=0.3: **23.0%** (-77pp) — graded degradation continues below cliff\\\\n- k=0.2: **~4.0%** (-96pp) — near-zero\\\\n- k=0.1: **~0.0%** (-100pp) — complete failure\\\\n✅ Full curve confirms threshold-graded pattern: immune k≥0.9, cliff at k=0.7, then graded degradation k≤0.5 (42.6%→23.0%→~4%→~0%).\\\\n\\\\n**Cliff localization (D114, D117: 3-seed deterministic, L2norm)**:\\\\n- k=0.80: **89.0% ± 0.72pp** (seeds: 88.8/88.4/89.8)\\\\n- k=0.85: **67.9% ± 0.31pp** (seeds: 68.0/67.6/68.2 — T4=26%, T6=0% across ALL 3 seeds)\\\\n- Non-monotonic: k=0.85 < k=0.80 by **21.1pp**. BART encoder creates length-dependent interactions near critical token density. SD < 1pp confirms fully deterministic, not stochastic.\\\\n\\\\n**Random pruning comparison (D127-D130, D132 REVERSAL)**:\\\\n- k=0.9: random=97.8% ≈ L2norm=97.6% → method independent at mild compression\\\\n- k=0.85: random=63.6% vs L2norm=68.0% (+4.4pp for L2norm at cliff boundary). Both crash on same tasks (T1, T4, T6, T8) → cliff is architectural.\\\\n- k=0.8: random=89.4% ≈ L2norm=89.0% → method independent, non-monotonic recovery confirmed in both\\\\n- 🔴 **k=0.5: random=70.6% >> L2norm=42.6% (+28pp REVERSAL, CI non-overlapping)**. Per-task random: [96, 46, 100, 92, 100, 94, 2, 82, 42, 100]. Random wins 9/10 tasks; L2norm actively harmful. T4: random=100% vs L2norm=42% (+58pp).\\\\n- k=0.7: random=65.2% vs L2norm=56.2% (+9pp random). Crossover confirmed at k≈0.8.\\\\n- 🔴 **k=0.3: random=62.8% vs L2norm=22.8% (+40pp!)** — gap SCALES with compression: +9@k=0.7, +28@k=0.5, +40@k=0.3.\\\\n- **D137 multi-seed confirmed**: seed43 k=0.5=71.0% (seed42=70.6%, Δ=0.4pp). Gap is reproducible.\\\\n- **Random non-monotonicity confirmed**: k=0.5 (70.6%) > k=0.7 (65.2%) > k=0.3 (62.8%). seed43 reproduces (71.0%). L2norm monotonically decreasing (42.6% > 22.8%). Random's k=0.5 \\\\\\\"sweet spot\\\\\\\" may reflect optimal diversity-coverage tradeoff: enough tokens removed to break BART clustering, but enough retained for spatial coverage.\\\\n- k=0.85 per-task (random): [100, 10, 100, 94, 24, 92, 0, 94, 22, 100] = 63.6%.\\\\n- **Non-monotonicity confirmed in both methods**: k=0.85 (42 tokens) cliff vs k=0.8 (40 tokens) recovery. 2-token difference, 21-26pp gap.\\\\n- **D132 KEY INSIGHT**: At aggressive compression (k=0.5), L2 norm is catastrophically worse than random for X-VLA. Low CV=0.151 → near-uniform importance → L2 norm degenerates into spatially clustered selection → loses diversity. This is the opposite of OpenVLA (CV=0.215) where L2 norm helps. **CV predicts optimal pruning strategy, not just tolerance.**\\\\n\\\\n**Cross-suite generalization (D117, updated with full results)**:\\\\n- X-VLA Spatial baseline: **91.6%** [88.8%, 93.7%] (500 eps, T5=48% is hardest task)\\\\n- X-VLA Goal baseline: **98.0%** [96.4%, 98.9%] (500 eps, all tasks ≥92%)\\\\n- X-VLA-Libero checkpoint covers all 4 suites without suite-specific fine-tuning.\\\\n\\\\n**⚠️ Cross-suite pruning sensitivity (key finding — potential new contribution)**:\\\\n\\\\nX-VLA pruning curve comparison across suites:\\\\n\\\\n| Suite | k=1.0 | k=0.9 | k=0.85 (L2/Rand) | k=0.8 (L2/Rand) | k=0.7 (L2/Rand) | k=0.5 (L2/Rand) |\\\\n|-------|-------|-------|-----|-------|----------|----------|\\\\n| Object | 99.2% | 97.8% | 68.0/63.6% | 89.0/89.4% | 56.2/65.2% | 42.6/**70.6%** |\\\\n| Spatial | 91.6% | 79.0% | 66.6/67.6% | — | — | 58.8%/**71.4%** |\\\\n| Goal | 98.0% | 70.2% | — | — | — | 61.0%/— |\\\\n\\\\n**Goal suite FINAL results (10/10 tasks, D123: suite-level monotonic confirmed)**:\\\\n- k=0.9: **70.2%** (351/500) — much larger drop than Object (-1.4pp) despite similar baseline\\\\n- k=0.5: **61.0%** (305/500) — suite-level monotonic (k=0.9 > k=0.5), D123 retracted earlier partial-data non-monotonic claim\\\\n\\\\n**Per-task non-monotonic pruning remains valid (selected tasks)**:\\\\n\\\\n| Task | k=1.0 | k=0.9 | k=0.5 | Pattern |\\\\n|------|-------|-------|-------|---------|\\\\n| T0 open drawer | 100% | 100% | 82% | monotonic ↓ |\\\\n| T2 close drawer | 94% | 96% | **100%** | **pruning improves** |\\\\n| T3 open+put (multi-step) | 100% | **6%** | **40%** | catastrophic + non-monotonic (k=0.5 > k=0.9) |\\\\n| T8 | — | — | — | +46pp non-monotonic (k=0.5 > k=0.9) |\\\\n| T9 | 98% | — | ~0% | catastrophic collapse (-98pp) |\\\\n\\\\n- Suite-level: Goal k=0.5=61.0% > Spatial k=0.5=58.8% — Goal slightly more robust, but both moderate degradation\\\\n- Per-task: T3/T8 show non-monotonicity (k=0.5 > k=0.9), T9 catastrophic collapse. These are genuine misalignments between global L2-norm ranking and task-specific token utility.\\\\n- T2 pruning improvement: consistent with π0 finding — simple tasks benefit from token noise removal\\\\n\\\\n**Key cross-suite finding**: Goal k=0.9 drops **27.8pp** (vs Object -1.4pp). Same connector, same pruning method, different task distribution → **task complexity amplifies pruning sensitivity**. Goal tasks involve multi-step reasoning that depends heavily on precise spatial tokens.\\\\n\\\\n**Task-level analysis (Spatial, k=0.5 vs baseline)**:\\\\n- Robust (Δ≤10pp): T0 \\\\\\\"between plate and ramekin\\\\\\\" (-4pp), T4 \\\\\\\"in top drawer\\\\\\\" (-2pp) — global spatial / unambiguous target\\\\n- Moderate (Δ 10-30pp): T2(-10), T3(-24), T6(-22), T8(-18) — mild spatial precision needed\\\\n- Catastrophic (Δ>40pp): T5 \\\\\\\"on ramekin\\\\\\\" (-48pp, 0%), T9 \\\\\\\"on cabinet\\\\\\\" (-58pp), T7 \\\\\\\"on stove\\\\\\\" (-64pp), T1 \\\\\\\"next to ramekin\\\\\\\" (-78pp)\\\\n- **T1 has 100% baseline but 22% at k=0.5** — high baseline ≠ pruning robustness\\\\n\\\\n**Mechanism**: Goal tasks are semantically diverse (different verbs/objects) → language instruction alone disambiguates → vision tokens are redundant for task selection. Spatial tasks are semantically near-identical (all \\\\\\\"pick bowl...\\\\\\\") → disambiguation relies entirely on spatial vision tokens → pruning destroys the only discriminative signal.\\\\n\\\\n**Paper framing upgrade (Reviewer suggestion, agreed)**:\\\\n- From \\\\\\\"connector determines pruning tolerance\\\\\\\" → \\\\\\\"pruning sensitivity = f(connector_type, task_semantics)\\\\\\\"\\\\n- Connector CV predicts degradation *class* (immune/threshold/graded/catastrophic)\\\\n- Task semantic structure determines degradation *severity* within that class\\\\n- When language disambiguates: aggressive pruning is safe (Goal k=0.5 ≈ baseline)\\\\n- When spatial vision disambiguates: even conservative pruning degrades (Spatial k=0.9 -12.6pp)\\\\n- **Potential new contribution**: first task-level pruning sensitivity analysis in VLAs. §4.6 should include per-task heatmap + the language-vs-spatial disambiguation framework.\\\\n\\\\nπ0 evidence:\\\\n- π0 (3.3B, 256 tokens, pure linear proj): k=0.1 normalized_L1 = 0.976 (-2.4% = improvement), k=0.5 = 0.983\\\\n- Attention entropy: π0 suffix-to-vision mean 0.959 (near-uniform across 18 layers, range [0.931, 0.983])\\\\n- Importance CV: π0 = 0.038 (lowest in spectrum)\\\\n\\\\n**Key insight**: \\\\\\\"Linear projection\\\\\\\" is NOT sufficient for immunity. The effective pipeline matters. X-VLA's BART encoder (12 transformer layers after linear proj) introduces partial dependencies → CV=0.151 → cliff at k=0.7. π0's pure linear proj → CV=0.038 → immune even at k=0.1.\\\\n\\\\n### Claim 3b: MLP Projector → Graded Degradation\\\\nMulti-layer MLP connectors create partial token dependencies through non-linear mixing, enabling graceful but real degradation.\\\\n\\\\n**Evidence** (OpenVLA 6-point degradation curve):\\\\n- k=1.0: 74.0% (baseline)\\\\n- k=0.95: 69.4% (-6% relative)\\\\n- k=0.9: 62.0% (-16% relative)\\\\n- k=0.7: 49.0% (-34% relative)\\\\n- k=0.5: 37.4% (-49% relative)\\\\n- k=0.3: 20.6% (-72% relative)\\\\n- Entropy ratio 0.639 (progressive sharpening L0=0.98→L29=0.48, TV=0.50)\\\\n- **Method independence confirmed**: random k=0.95=69.2% ≈ L2norm k=0.95=69.4%; random k=0.5=35.8% ≈ L2norm k=0.5=37.4%. For MLP projectors, pruning method doesn't matter.\\\\n- OFT (same connector, different action head): entropy 0.667 ≈ Standard 0.661 → connector determines attention structure, not action head\\\\n- CogACT (MLP projector, literature): 74.8% → 74.2% under 78% pruning (EfficientVLA)\\\\n\\\\n### Claim 4: Learned Re-Encoding Achieves Near-Lossless Compression Where Deletion Fails (D072+MLP confirmed → upgraded to METHOD per D091)\\\\n**⚠️ Baseline correction (2026-05-22): SmolVLA Object baseline = 59.2% (official HF checkpoint), NOT 44.8% (old reproduced). VTR narrative reframed from \\\\\\\"re-encoding boost\\\\\\\" to \\\\\\\"near-lossless compression recovery\\\\\\\".**\\\\n\\\\nTwo independent re-encoding architectures (~22M params each) validate that **any learned re-encoding** can recover entangled pixel_shuffle tokens from 0% (hard pruning) to near-baseline levels. Cross-attention (60.1±1.3%, 3-seed) and MLP adapter (63.4±2.6%, 3-seed) both achieve this recovery, with p≈0.15 confirming no significant difference between architectures. M=128 passthrough (58.0±3.5%, 3-seed) ≈ baseline 59.2% (-1.2pp), confirming VTR recovers to baseline rather than exceeding it. **M-curve is flat**: M=16 (56.9%) through M=128 (58.0%), all within ±3pp of baseline 59.2% — VTR achieves near-lossless compression at ANY ratio (0-87.5%) for pixel-shuffle connectors. M=64 achieves best absolute SR at 62.0±2.3% (+2.8pp over baseline) with 50% compression. Cross-suite generalization confirmed: M=32 recovers to 53.2% on Spatial (vs 0.6% pruning cliff-edge) and 56.4% on Goal. M=96 dip statistically confirmed (p=0.034 vs M=64).\\\\n\\\\n**D109 C4-ext on OpenVLA (MLP projector)**: M=128 VTR at 20K steps = **0% SR** (severe overfitting, model outputs identical action every step). This suggests VTR's effectiveness is connector-dependent: pixel-shuffle benefits enormously (0%→~59% ≈ baseline) because re-encoding repairs spatial entanglement, while MLP projector tokens are already individually meaningful and VTR adds unnecessary complexity. VTC-only M=32/M=64 training in progress — if these also fail, VTR is specifically a pixel-shuffle solution, which strengthens the architecture-dependency narrative.\\\\n\\\\n**Evidence** (all confirmed):\\\\n\\\\nCross-attention re-encoding (M sweep, 3-seed where available):\\\\n| M | Compression | SR (3-seed mean±std) | Seeds | Notes |\\\\n|---|------------|-----|-----|-----|\\\\n| 16 | 87.5% | **56.9±1.3%** | 42/43/44 | ✅ ZERO loss vs M=128 |\\\\n| 32 | 75% | **60.1±1.3%** | 42/43/44 | ✅ |\\\\n| 64 | 50% | **62.0±2.3%** | 42/43/44 | ✅ best tradeoff |\\\\n| 96 | 25% | 54.5±3.2% | 42/43/44 | ✅ highest variance |\\\\n| 128 | 0% (passthrough) | **58.0±3.5%** | 42/43/44 | ✅ passthrough control |\\\\n\\\\nMLP adapter control (M=32, ~22.14M params, 3-seed):\\\\n| Architecture | Params | M | Mean SR (3-seed) | Std | Individual seeds |\\\\n|---|---|---|-----|-----|-----|\\\\n| Cross-attention (VTC) | 22.2M | 32 | **60.1%** | ±1.3 | 61.6 / 59.2 / 59.6 |\\\\n| **MLP adapter** | **22.14M** | **32** | **63.4%** | **±2.6** | **65.2 / 64.6 / 60.4** |\\\\n\\\\nTwo-sample t-test: t≈1.94, p≈0.15 → **no significant difference** (α=0.05). Both >> 0% (hard pruning) and ≈ 59.2% (baseline). MLP ≥ VTC in all 3 seeds but difference not statistically significant — confirms any re-encoding architecture recovers to near-baseline, not a specific mechanism. (Note: M=32 seed43 corrected from 62.4% to 59.2% per registry verification; 62.4% was M=96 seed43 CI upper bound misattributed.)\\\\n\\\\n### Claim 5: CV Predicts Optimal Pruning Strategy — Monotonic Diagnostic Trend (D132→D139→D140→D142)\\\\nToken importance CV determines **which pruning method to use**, with the L2norm-vs-random gap scaling monotonically with CV. **Validated at TWO k values (D142):**\\\\n\\\\n**k=0.5 (main table):**\\\\n| Model | CV | Tokens | L2norm k=0.5 | Random k=0.5 | Δ (R-L2) |\\\\n|-------|-----|--------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | **33.4%** | **69.4%** | **+36.0pp** |\\\\n| X-VLA | 0.151 | 50 | 43.4%³ | 70.3%⁴ | +26.9pp |\\\\n| OpenVLA | 0.215 | 256 | 39.2% | 37.4%¹⁰ | -1.8pp |\\\\n\\\\n**k=0.7 (second validation, D142):**\\\\n| Model | CV | Tokens | L2norm k=0.7 | Random k=0.7 | Δ (R-L2) |\\\\n|-------|-----|--------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | **55.0%** | **77.2%** | **+22.2pp** |\\\\n| X-VLA | 0.151 | 50 | 58.6%⁶ | 65.1%⁷ | +6.5pp |\\\\n| OpenVLA | 0.215 | 256 | 49.8% | 44.4% | -5.4pp |\\\\n⁶ X-VLA L2norm k=0.7 2-seed: 58.2/59.0, mean=58.6%, σ=0.4pp (seed44 pending → tri-seed)\\\\n⁷ X-VLA random k=0.7 2-seed: 65.2/65.0, mean=65.1%, σ=0.1pp (seed44 running)\\\\n\\\\n³ X-VLA L2norm k=0.5 3-seed mean: 42.6/43.4/44.2, mean=43.4%, range 1.6pp\\\\n⁴ X-VLA random k=0.5 3-seed mean: 70.6/71.0/69.2, mean=70.3%, σ=0.9pp\\\\n\\\\n¹⁰ OpenVLA random k=0.5 = 37.4% (seed7). Table 3 previously showed 35.8% (unverified source). seed42 running on westd-38929, will replace when available.\\\\n\\\\n✅ **D139+D142 CONFIRMED**: Monotonic trend validated at BOTH k=0.5 (-1.8→+26.9→+36.0) and k=0.7 (-5.4→+6.5→+22.2). Same monotonic pattern. Paper: k=0.5 as main table, k=0.7 as confirmatory second row or separate table.\\\\n\\\\n**D140: k=0.3 interaction — method preference REVERSES at extreme compression for π0.5:**\\\\n\\\\n| Model | CV | Tokens | k=0.3 kept | L2norm k=0.3 | Random k=0.3 | Δ (R-L2) |\\\\n|-------|-----|--------|-----------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | 230 | **51.0%** | 36.4% | **-14.6pp** |\\\\n| X-VLA | 0.151 | 50 | 15 | 22.2%⁸ | **64.5%⁹** | **+42.3pp** |\\\\n| OpenVLA | 0.215 | 256 | 77 | 25.0% | **21.4%** | **+3.6pp** |\\\\n\\\\n⁸ X-VLA L2norm k=0.3 3-seed: 22.2/21.0/22.8 (from D137), mean=22.0%; seed43 running on cqa1\\\\n⁹ X-VLA random k=0.3 2-seed: 62.8/66.2, mean=64.5%, σ=2.4pp; seed44 running on cqa1\\\\n\\\\nAt k=0.3, π0.5 L2norm wins (+14.6pp) while X-VLA random still wins massively (+42.3pp). OpenVLA L2norm also wins (+3.6pp). The pattern: at k=0.3, both high-CV (OpenVLA) and low-CV-with-large-budget (π0.5, 230 tokens) favor L2norm, while mid-CV-with-small-budget (X-VLA, 15 tokens) strongly favors random. Strategy preference is f(CV, k, absolute_token_budget).\\\\n\\\\n**OpenVLA (CV=0.215) full seed42 Δ(L2-R) pattern**: +1.4pp (k=0.95) → +5.4pp (k=0.7) → pending (k=0.5) → +3.6pp (k=0.3). L2norm consistently better at ALL k values — high CV enables meaningful importance-based selection. Peak advantage at k=0.7, not monotonically increasing with compression.\\\\n\\\\n**D141: π0.5 L2norm complete curve — valley at k=0.5 confirmed (multi-seed)**:\\\\n| k | L2norm SR (s42) | L2norm SR (s43) | Random SR | Δ (R-L2) s42 |\\\\n|---|-----------------|-----------------|-----------|---------------|\\\\n| 0.7 | **55.0%** | **57.8%**¹⁰ | **77.2%** / **73.8%** (mean=75.5%) | +22.2pp (s42) / +19.8pp (mean) |\\\\n| 0.5 | **33.4%** | **33.6%** ✅ | **69.4%** / **68.4%** (mean=68.9%) | +36.0pp (s42) / +35.4pp (mean) |\\\\n| 0.3 | **51.0%** | **55.4%** ✅ | 36.4% | -14.6pp |\\\\n\\\\n¹⁰ Agent audit reported 56.4% for L2norm k=0.7 seed43 vs earlier worker result 57.8%. Needs reconciliation. Pattern unchanged.\\\\n\\\\n**V-shape fully confirmed (2 seeds, both methods)**:\\\\n- **Valley (k=0.5)**: L2norm 33.4/33.6% (std=0.1pp); Random 69.4/68.4% (std=0.7pp) — both methods stable\\\\n- **2-seed means**: L2norm k=0.7=56.4%, k=0.5=33.5%, k=0.3=53.2%; Random k=0.7=75.5%, k=0.5=68.9%\\\\n- **V-depth**: seed42=17.6pp, seed43=21.8pp (seed43 deeper because endpoints higher)\\\\n- **Δ(R-L2) dual-seed means**: k=0.7=+19.8pp, k=0.5=+35.4pp — monotonic trend holds with multi-seed\\\\n- seed43 consistently +2-4pp above seed42 but identical shape. Valley position/depth is architectural determinism.\\\\n\\\\n**Mechanism confirmed by token position visualization (D141)**:\\\\n- k=0.7: 2 clusters, 97% in largest, **100% spatial coverage** — enough tokens to maintain coverage\\\\n- k=0.5: **1 cluster, 100% in single region, 78% coverage** — worst-case spatial concentration\\\\n- k=0.3: **3 clusters**, 86% in largest, 78% coverage — cluster breaks apart, better diversity\\\\n\\\\nThe non-monotonicity arises because k=0.5 sits at the worst point of the spatial correlation structure: L2norm selects exactly the number of tokens that maximizes spatial clustering. At k=0.7 there are enough tokens for coverage; at k=0.3 the selection threshold crosses a boundary that fragments the cluster. Per-task variance is extreme at k=0.7 (T1=94%, T5=98% vs T7=0%) — L2norm deterministic selection can catastrophically miss specific task-critical spatial regions.\\\\n\\\\n**Paper strategy**: k=0.5 as **main table** (cleanest monotonic trend, clear gap). Full L2norm curve as **figure** showing pathological valley — strong evidence for spatial clustering mechanism. k=0.3 reversal as supplementary. Key message: \\\\\\\"CV predicts method preference at k=0.5; L2norm's spatial clustering creates pathological non-monotonicity unique to low-CV models.\\\\\\\"\\\\n\\\\n**Notable asymmetry**: Random tolerance is similar for low/medium CV at k=0.5 (π0.5=69.4% ≈ X-VLA=70.6%), while L2norm harm increases dramatically (π0.5=33.4% < X-VLA=43.4%). High CV (OpenVLA=35.8% random) is less random-tolerant because tokens have genuine importance differentiation that random discards.\\\\n\\\\n**Evidence** (Reviewer-verified, D132 PASS):\\\\n\\\\nX-VLA vs OpenVLA full comparison:\\\\n\\\\n| k | X-VLA (CV=0.151) | | OpenVLA (CV=0.215) | |\\\\n|---|---|---|---|---|\\\\n| | L2norm | Random | L2norm | Random |\\\\n| 0.95 | — | — | 70.6% | 69.2% (+1.4 L2norm) |\\\\n| 0.9 | 97.6% | 97.8% (≈0) | 70.6% | 64.6% (+6.0 L2norm) |\\\\n| 0.85 | 68.0% | 63.6% (+4.4 L2norm) | — | — |\\\\n| 0.8 | 89.0% | 89.4% (≈0) | — | — |\\\\n| 0.7 | 56.2% | **65.2% (+9pp random)** | 49.8%¹ | 44.4% (+5.4 L2norm¹) |\\\\n| 0.5 | **42.6%** | **70.6% (+28pp random!)** | 39.2% | 35.8% (+3.4 L2norm) |\\\\n| 0.3 | **22.8%** | **62.8% (+40pp random!)** | 25.0% | pending² |\\\\n\\\\n¹ OpenVLA L2norm k=0.7 = seed43 only, random = seed42; cross-seed caveat. seed42 L2norm k=0.7 running on westd-38929.\\\\n² OpenVLA random k=0.3 result file missing, re-running on westd-38929.\\\\n³ D137 multi-seed: X-VLA random k=0.5 seed43=71.0% (seed42=70.6%, Δ=0.4pp). Gap reproducible.\\\\n\\\\n**Per-task X-VLA k=0.5 (Reviewer-verified, 9/10 tasks random > L2norm):**\\\\n\\\\n| Task | Baseline | L2 s42 | L2 s43 | Random s42 | Δ(R-L2) |\\\\n|------|---------|--------|--------|------------|---------|\\\\n| T0 alphabet_soup | 98% | 58% | 56% | **96%** | +38 |\\\\n| T1 cream_cheese | 100% | 2% | 6% | 46% | +44 |\\\\n| T4 ketchup | 100% | 42% | 40% | **100%** | **+58** |\\\\n| T7 milk | 100% | 38% | 38% | 82% | +44 |\\\\n| T9 orange_juice | 100% | 68% | 70% | **100%** | +32 |\\\\n| T6 butter | 100% | 2% | 2% | 2% | 0 (both crash) |\\\\n\\\\nL2norm two seeds highly consistent (s42 vs s43 diff <6pp) → not RNG noise.\\\\nT6: baseline=100% but both methods=2% → highly localized visual cue, k=0.5 always loses it regardless of method.\\\\nT4/T9: Random recovers to baseline → L2norm systematically discards the critical tokens for these tasks.\\\\n\\\\n**Pattern**: Low CV (X-VLA) → importance-based selection degenerates at aggressive k → random better. High CV (OpenVLA) → meaningful importance differentiation → L2 norm better.\\\\n\\\\n**Mechanism hypothesis** (Reviewer: consistent with data, needs direct evidence): X-VLA's linear projection + BART encoder produces tokens with relatively uniform L2 norms (CV=0.151). At aggressive compression (k=0.5 = keeping 25 of 50 tokens), L2 norm selects the \\\\\\\"slightly larger\\\\\\\" tokens which tend to be spatially clustered → loses spatial diversity → catastrophic. Random preserves spatial coverage stochastically → dramatically better.\\\\n\\\\n**⚠️ Visualization needed (Reviewer warning)**: Must produce token position visualization — for same input image, show which tokens L2 norm vs random retains. If L2 norm shows spatial clustering, mechanism is proven. This should be a key figure (§4.6 or Fig 4).\\\\n\\\\n**Implication for practitioners**: CV diagnoses → predicts tolerance → prescribes strategy at aggressive compression. Low CV + aggressive k (≤0.5) → random/position-based. High CV → importance-based at all k. Mild compression (k≥0.8) → method choice doesn't matter regardless of CV.\\\\n\\\\n**Pending**: X-VLA random k=0.7 (crossover), multi-seed k=0.5, token position visualization, OpenVLA L2norm k=0.7 seed42, k_ratio=null fix.\\\\n\\\\n## Story Spine\\\\n\\\\n**Problem**: Vision token efficiency is critical for real-time VLA deployment. Growing literature proposes inference-time token reduction (FastV, VLA-IAP, H2O, ToMe). These methods succeed on some VLAs but their behavior across different architectures is unstudied.\\\\n\\\\n**Gap**: No work has systematically compared token pruning robustness across VLA architectures. The implicit assumption that \\\\\\\"token pruning works or fails uniformly\\\\\\\" is untested. The critical architectural factor determining prunability is unknown.\\\\n\\\\n**Discovery**: We find that VLA token pruning robustness is governed by two interacting axes. **Axis 1 — Token Coupling**: connector architecture determines whether tokens are independent (linear proj, MLP) or entangled (BART encoder, pixel-shuffle), diagnosed by importance CV (0.038→0.314). **Axis 2 — Task Complexity**: multi-step tasks (Goal/Long) amplify pruning damage on entangling connectors — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at k=0.9. Evidence from 5 VLA models × 4 LIBERO suites:\\\\n- **Token-independent** (π0, π0.5 linear; OpenVLA, OFT MLP): graded degradation, CV 0.038–0.219\\\\n- **Token-entangling** (X-VLA BART 12L; SmolVLA pixel-shuffle): task-dependent collapse — tolerate simple tasks, catastrophic on complex tasks. CV 0.151–0.314\\\\nCV predicts both pruning tolerance and optimal strategy (L2norm hurts low-CV models, helps high-CV).\\\\n\\\\n**Solution**: Diagnose-then-Compress framework. Step 1: Token importance CV provides zero-cost diagnostic for pruning tolerance (one forward pass). Step 2: VTR (Vision Token Re-encoding) provides universal compression. For pixel-shuffle: recovers from 0% (hard pruning) to ~59% ≈ baseline (59.2%), M-curve flat (D105: M=16 56.9% ≈ M=128 58.0%, near-lossless at any compression ratio). For MLP projector: D109 C4-ext = 0% SR (overfitting at M=128); VTC-only M=32/M=64 in progress.\\\\n\\\\n**Headline result**: \\\\\\\"Across 5 VLA models (450M-7B) × 4 task suites, we find that token pruning robustness is governed by two axes: connector architecture (token-independent vs token-entangling, diagnosed by importance CV) and task complexity. Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio; SmolVLA collapses to 0% at 5% removal regardless of task. CV (0.038→0.314) predicts both pruning tolerance and optimal strategy: importance-based pruning is actively harmful on low-CV architectures (+28-36pp gap favoring random), while it helps on high-CV models (+1-6pp). VTR recovers to ~59% (≈baseline) at any compression ratio (0-87.5%) where hard deletion achieves 0%.\\\\\\\"\\\\n\\\\n## Paper Structure (7-model version)\\\\n\\\\n1. **Introduction**: VLA efficiency motivation → diverse connector architectures → 2-axis framework discovery (D171) → Diagnose-then-Compress framework\\\\n2. **Background**: 5 VLA models, 3 connector families (linear/MLP/pixel-shuffle), 4 LIBERO suites, token flow analysis\\\\n3. **Experimental Setup**: 5 models, LIBERO benchmark (4 suites: Object/Spatial/Goal/Long), pruning protocol, VTR compression, diagnostic metrics\\\\n4. **Main Results**:\\\\n   - §4.1: 2-Axis Framework Overview (Table 1: 5 models × token coupling axis; Table 2: cross-suite interaction — connector × task complexity)\\\\n   - §4.2: Token-Entangling Catastrophic — pixel-shuffle cliff-edge (SmolVLA, all configs 0% regardless of task)\\\\n   - §4.3: Token-Independent Graded — MLP degradation (OpenVLA 6-point curve + OFT entropy confirmation)\\\\n   - §4.4: Token-Independent Tolerant — linear projection (π0 + π0.5, controlled comparison with OpenVLA)\\\\n   - §4.5: Task Complexity Amplification — X-VLA cross-suite (Object 97.6% vs Goal 70.2% vs Long ~53% at same k)\\\\n   - §4.6: Pruning Strategy Depends on CV (D132: low-CV random>>L2norm, high-CV L2norm>>random)\\\\n   - §4.7: VTR overcomes cliff-edge (M-curve flat + architecture independence)\\\\n   - (REMOVED — D119: LIBERO-Plus L1 SR=3.3% floor effect, noted in Discussion §6)\\\\n5. **Analysis**:\\\\n   - §5.1: Why pixel_shuffle creates entanglement (spatial folding + controlled comparison)\\\\n   - §5.2: Diagnostic metric — Entropy + CV composite (D104, 4-model validation)\\\\n   - §5.3: Re-encoding mechanism (M=128 passthrough + MLP adapter + M-curve flat D105)\\\\n6. **Discussion**: Design implications, limitations (sim-only, no real robot), future work\\\\n7. **Conclusion**: 5 claims summary\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Only 2 models → **FULLY ADDRESSED**\\\\n**Response**: Now 5 models (SmolVLA, OpenVLA, OpenVLA-OFT, π0, X-VLA) across 3 connector families (pixel-shuffle, 3-layer MLP, linear projection) and 4 model sizes (450M-7B). Each connector class has ≥2 models.\\\\n\\\\n### RC2: Model size confound (450M vs 7B) → **FULLY ADDRESSED**\\\\n**Response**: π0 (3.3B, linear) is pruning-immune while OpenVLA (7B, MLP) degrades 61% at k=0.1. Larger model is MORE vulnerable, not less — directly falsifies \\\\\\\"larger models are more robust\\\\\\\" hypothesis. X-VLA (880M, linear) also immune, matching π0 behavior despite 4× smaller. Size is not the explanatory variable; connector type is.\\\\n\\\\n### RC3: Why not test SmolVLA without pixel_shuffle?\\\\n**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.\\\\n\\\\n### RC4: Smart compression — is re-encoding or compression the mechanism?\\\\n**Response (corrected with baseline=59.2%)**: VTR achieves near-lossless compression at any ratio — the M-curve is flat (M=16: 56.9% → M=128: 58.0%, all within ±3pp of baseline 59.2%). Two lines of evidence: (1) M=128 passthrough (58.0%) ≈ baseline (59.2%) — re-encoding recovers spatial entanglement to baseline level, not above it. (2) Architecture control: MLP adapter (63.4%) ≈ cross-attention (60.1%) with CI overlap — any re-encoding mechanism works. The key contribution is recovery from 0% (hard pruning) to ~59% (baseline), not exceeding baseline. Compression ratio is a free parameter with negligible SR cost.\\\\n\\\\n### RC5: Relationship to VLA-IAP\\\\n**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.\\\\n\\\\n### RC6: Is this just \\\\\\\"different models behave differently\\\\\\\"?\\\\n**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.\\\\n\\\\n### RC7: Only one benchmark (LIBERO-Object) → **ADDRESSING (D115, D119)**\\\\n**Response**: Expanded to ALL 4 LIBERO suites (Object/Spatial/Goal/Long) — 4 genuinely different task distributions (manipulation skills, spatial reasoning, goal-conditioned, long-horizon). Taxonomy consistency validated across suites. LIBERO-Plus robustness benchmark tested (D119) but abandoned: L1 camera perturbation collapses OpenVLA to SR=3.3% (consistent with leaderboard 0.8%), creating floor effect with no room for pruning analysis. This floor effect itself is noted in Discussion as evidence of general VLA brittleness under distribution shift. Sim-only limitation acknowledged.\\\\n\\\\n## All Experimental Evidence (confirmed)\\\\n\\\\n### SmolVLA Cliff-Edge\\\\n- Fine-tuned baseline (Object): 44.8% (224/500) — ⚠️ OLD reproduced checkpoint, superseded by official HF = 59.2%\\\\n- 6 pruning conditions (random/ACIS/ToMe × k=0.5/0.7/0.9): all 0%\\\\n- Geometric prior (Sobel) k=0.5/0.7/0.9: all 0%\\\\n- Attention entropy: 0.952 (flat, TV=0.05)\\\\n- Official checkpoint Object: 59.2% → 0% at k=0.5\\\\n- Official checkpoint Spatial: 43.8% → 0.6% (3/500, CI [0.2%, 1.7%]) at k=0.5 — near-zero, confirms cliff-edge across suites\\\\n- LoRA-FT checkpoint Spatial: 8.0% (per-task: [24,8,4,24,0,2,2,2,14,0]) — LoRA trained on Object only, does not transfer to Spatial. Use official checkpoint for cross-suite SmolVLA analysis.\\\\n\\\\n### OpenVLA Degradation Curve\\\\n- k=1.0: 74.0% (370/500)\\\\n- k=0.95: 69.4% (-6% relative)\\\\n- k=0.9: 62.0% (-16% relative)\\\\n- k=0.7: 49.0% (245/500, -34% relative)\\\\n- k=0.5: 37.4% (187/500, -49% relative)\\\\n- k=0.3: 20.6% (103/500, -72% relative)\\\\n- Entropy: 0.639 (progressive sharpening, TV=0.50)\\\\n\\\\n### Cross-Model Pruning Taxonomy (7 models — D100, D120, D127)\\\\n| Model | Connector | Tokens | k=0.1 norm_L1 | k=0.5 norm_L1 | Class |\\\\n|-------|-----------|--------|---------------|---------------|-------|\\\\n| π0 (3.3B) | Pure linear proj | 256 | 0.976 (-2.4%) | 0.983 | Immune |\\\\n| π0.5 (4B) | Pure linear proj (×√d scaling) | 768 (3×256) | **98.2%** (491/500) | **L2norm=33.4%, random=69.4%** | **Uniformly Critical (D139)**: L2norm catastrophic (-64.8pp), random tolerant (-28.8pp), gap=+36pp. CV=0.055. |\\\\n| X-VLA (880M) | Linear + BART 12L | 50 | ~1.00 | ~1.00 | Threshold-graded (k=0.7: 56.2%) |\\\\n| OpenVLA (7B) | 3-layer MLP | 256 | 1.608 (+61%) | 1.167 (+17%) | Smooth graded |\\\\n| OFT (7B) | 3-layer MLP (DINOv2+SigLIP fused) | **512** | N/A | N/A | D136: Blackwell GPU incompatible. CV=0.219≈OpenVLA → graded. Cite official ~97% baseline. |\\\\n| SmolVLA (450M) | Pixel-shuffle | 128 | — | 0% cliff | Catastrophic |\\\\n\\\\nDiagnostic metrics (D104+D106+D120: CV as continuous predictor, 7 models):\\\\n| Model | Connector (effective) | Entropy | CV | Pruning Behavior |\\\\n|-------|----------------------|---------|------|------------------|\\\\n| π0 | Pure linear proj | 0.959 | 0.038 | Immune (offline, k=0.1 improves) |\\\\n| π0.5 | Pure linear proj (×√d) | pending | 0.055 | **Uniformly Critical (D139)**: L2norm=33.4%, random=69.4%, gap=+36pp. Monotonic trend extreme. |\\\\n| X-VLA | Linear proj + BART enc (12L) | **0.614** | **0.151** | Threshold-graded: robust k≥0.9, cliff k=0.7 (56.2%). D127: random=L2norm at k=0.9 |\\\\n| OpenVLA | 3-layer MLP (GELU) | 0.661 | 0.215 | Graded (74→37.4% at k=0.5) |\\\\n| OFT | 3-layer MLP (DINOv2+SigLIP, **512 tokens**) | 0.667 | 0.219 | D136: Graded expected (CV≈OpenVLA). Blackwell GPU incompatible, no LIBERO SR. |\\\\n| SmolVLA | Pixel-shuffle (16×) | 0.952 | **0.314** | Catastrophic (0% at k=0.95) |\\\\n\\\\nKey insights (updated with 7-model data):\\\\n1. **CV is a continuous predictor**: 0.038 → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 maps to decreasing pruning tolerance. NOT a 3-class discrete classifier.\\\\n2. **X-VLA CV=0.151 correctly predicted its intermediate behavior** — closer to OpenVLA (0.215) than π0 (0.038), matching k=0.7 SR ≈ OpenVLA k=0.7.\\\\n3. **X-VLA entropy=0.614 ≈ OpenVLA 0.661** — both have BART/MLP non-linear mixing. X-VLA is NOT \\\\\\\"high entropy\\\\\\\" like π0.\\\\n4. **Effective connector complexity matters more than nominal label**: X-VLA is \\\\\\\"linear proj\\\\\\\" but BART encoder introduces 12 transformer layers of mixing. Paper should discuss \\\\\\\"effective connector\\\\\\\" = projection + any intermediate processing.\\\\n5. OFT entropy 0.667 ≈ Standard 0.661 → action head does not affect attention structure\\\\n6. Framing: CV captures \\\\\\\"degree of non-linear mixing in the vision-to-LLM pathway.\\\\\\\" More mixing → higher CV → less tolerant of pruning.\\\\n\\\\n### Smart Compress (Learned Re-encoding)\\\\nCross-attention (VTC) M sweep (3-seed where available):\\\\n- M=16: **56.9% ± 1.3pp** (3-seed: 55.8/58.4/56.5) — 87.5% compression, ZERO loss vs M=128\\\\n- M=32: 60.1±1.3% (3-seed: 61.6/59.2/59.6)\\\\n- M=64: 62.0±2.3% (3-seed: 61.6/60.0/64.4)\\\\n- M=96: 54.5±3.2% (3-seed: 52.6/58.2/52.8) — highest variance\\\\n- M=128: 58.0±3.5pp (3-seed: 59.8/54.0/60.2) — passthrough control\\\\n- **D102 CONFIRMED: M-curve is flat.** M=16 (56.9%) = M=128 (58.0%), difference < 1.1pp. VTC achieves near-lossless compression at ANY ratio for pixel-shuffle connector. All M values within ±5pp of baseline ~59%.\\\\n\\\\nMLP adapter (M=32, 3-seed):\\\\n- seed42: 65.2% (326/500), seed43: 64.6% (323/500), seed44: 60.4% (302/500)\\\\n- Mean: 63.4% ± 2.6 vs VTC M=32 mean 60.1% ± 1.3\\\\n- t-test p≈0.15, no significant difference — confirms architecture-independence\\\\n\\\\n### D109: VTR on OpenVLA (MLP projector) — FAILED\\\\n- C4-ext M=128 at 20K steps: **0% SR** (0/44 episodes before eval termination)\\\\n- Failure mode: model outputs identical action every timestep (severe overfitting)\\\\n- Interpretation: VTR adds unnecessary complexity for MLP projector tokens (already individually meaningful). VTR specifically solves pixel-shuffle entanglement.\\\\n- VTC-only M=32 and M=64 training in progress on westd-41074:2-3\\\\n\\\\n### Cross-Suite VTR Generalization (SmolVLA)\\\\n- M=32 Spatial: 53.2% (vs official Spatial baseline 44.6% per ROADMAP, vs pruning 0.6% — recovery from cliff-edge, +8.6pp over baseline)\\\\n- M=32 Goal: 56.4% (vs official Goal baseline 60.8% per ROADMAP, vs pruning 0% — recovery from cliff-edge, -4.4pp below baseline)\\\\n- ⚠️ Cross-suite baselines need reconciliation: paper_framing previously used 43.8%/63.0%, ROADMAP uses 44.6%/60.8%. Use n=500 official checkpoint data as ground truth.\\\\n- Note: VTR trained on Object suite, evaluated cross-suite. Official baselines from different checkpoint (official vs LoRA-FT); comparisons should emphasize recovery from 0% rather than absolute performance vs uncompressed.\\\\n\\\\n### Pairwise Statistical Tests (Welch's t-test, n=3 per condition)\\\\n- M=32 VTC vs M=32 MLP: p=0.150 (not significant) — confirms architecture-independence\\\\n- M=64 VTC vs M=96 VTC: p=0.034 (significant) — M=96 dip confirmed real\\\\n- M=32 MLP vs M=96 VTC: p=0.022 (significant) — M=96 underperforms\\\\n- M=32/M=64/M=128 VTC cluster: all pairwise p>0.25 — robust across M values\\\\n- Bonferroni note: no pair survives correction at 10 tests; n=3 limits power (~0.2 for medium effects)\\\\n\\\\n### Supplementary\\\\n- Inference latency: 6% speedup at M=32\\\\n- KV-cache: 75% memory reduction at M=32\\\\n\\\", \\\"total_chars\\\": 51958, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01ADTZDiQAZ8eADyvyvPbthy`</summary>

```json
{
  "pattern": "**/skills/**/*.skill.md",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "723beb1e-057e-432e-a5cb-4b22d5d1eb77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeGzdXHoH2giHQm54ypvZV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 34272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1085
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-28T17:47:09.716Z_

<details><summary>↩ Tool result · `toolu_01ADTZDiQAZ8eADyvyvPbthy`</summary>

```text
/home/ubuntu/agent-ml-research/skills/global/academic-writer.skill.md
/home/ubuntu/agent-ml-research/skills/global/code-survey.skill.md
/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md
/home/ubuntu/agent-ml-research/skills/global/dataset-discovery.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-reviewer-synthesis.skill.md
/home/ubuntu/agent-ml-research/skills/global/data-snapshot.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md
/home/ubuntu/agent-ml-research/skills/global/check-key.skill.md
/home/ubuntu/agent-ml-research/skills/global/distill-session.skill.md
/home/ubuntu/agent-ml-research/skills/global/elastic-gpu.skill.md
/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md
/home/ubuntu/agent-ml-research/skills/global/first-project-entry.skill.md
/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-generation.skill.md
/home/ubuntu/agent-ml-research/skills/global/idea-proposal.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-cloud-rental.skill.md
/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-claude-pool.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md
/home/ubuntu/agent-ml-research/skills/global/novelty-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/narrative-animation.skill.md
/home/ubuntu/agent-ml-research/skills/global/mvp-validation.skill.md
/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-datagen-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/negative-framing-review.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-pending.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-worker-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-research.skill.md
/home/ubuntu/agent-ml-research/skills/global/research-kickoff.skill.md
/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md
/home/ubuntu/agent-ml-research/skills/global/research-health-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-research-standalone.skill.md
/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md
/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md
/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md
/home/ubuntu/agent-ml-research/skills/global/review-report-action.skill.md
/home/ubuntu/agent-ml-research/skills/global/skill-creator.skill.md
/home/ubuntu/agent-ml-research/skills/global/study-director-session-start.skill.md
/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md
/home/ubuntu/agent-ml-research/skills/global/s3-backup.skill.md
/home/ubuntu/agent-ml-research/skills/global/session-start.skill.md
/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md
/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md
/home/ubuntu/agent-ml-research/skills/global/study-agent-assembly.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-research-steering.skill.md
/home/ubuntu/agent-ml-research/skills/global/dream-cron.skill.md
/home/ubuntu/agent-ml-research/skills/global/experiment-matrix.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-async-ops.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-ec2-provisioning.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-readiness-check.skill.md
/home/ubuntu/agent-ml-research/skills/global/manager-state-verification.skill.md
/home/ubuntu/agent-ml-research/skills/global/literature-scan.skill.md
/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md
/home/ubuntu/agent-ml-research/skills/global/post-mvp-kickoff.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-from-scratch.skill.md
/home/ubuntu/agent-ml-research/skills/global/competitor-experiment-reference.skill.md
/home/ubuntu/agent-ml-research/skills/global/director-experiment-review.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md
/home/ubuntu/agent-ml-research/skills/global/ai-time-discipline.skill.md
/home/ubuntu/agent-ml-research/skills/global/on-experiment-done.skill.md
/home/ubuntu/agent-ml-research/skills/global/progress-report.skill.md
/home/ubuntu/agent-ml-research/skills/global/submit-experiment.skill.md
/home/ubuntu/agent-ml-research/skills/global/plan-next-experiment.skill.md
/home/ubuntu/agent-ml-research/skills/global/write-paper-section.skill.md
/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md
/home/ubuntu/agent-ml-research/skills/global/framing-reaudit.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-plan.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-refinement.skill.md
/home/ubuntu/agent-ml-research/skills/global/reviewer-audit-checklist.skill.md
/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-visual-review.skill.md
/home/ubuntu/agent-ml-research/skills/global/dream-report-action.skill.md
/home/ubuntu/agent-ml-research/skills/global/method-improvement.skill.md
/home/ubuntu/agent-ml-research/skills/global/dream-review-full.skill.md
/home/ubuntu/agent-ml-research/skills/global/dream-review-simple.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md
/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md
/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md
/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "a823fd5d-cbe2-429c-ad23-a12c6d992989",
  "tool_use_result": {
    "filenames": [
      "/home/ubuntu/agent-ml-research/skills/global/academic-writer.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/code-survey.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/dataset-discovery.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/director-reviewer-synthesis.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/data-snapshot.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/check-key.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/distill-session.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/elastic-gpu.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/first-project-entry.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/idea-generation.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/idea-proposal.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-cloud-rental.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-claude-pool.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/novelty-check.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/narrative-animation.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/mvp-validation.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-datagen-done.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/negative-framing-review.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-experiment-pending.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-worker-done.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-research.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/research-kickoff.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/research-health-check.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-research-standalone.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/review-report-action.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/skill-creator.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/study-director-session-start.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/s3-backup.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/session-start.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/study-agent-assembly.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/director-research-steering.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/dream-cron.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/experiment-matrix.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-async-ops.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-ec2-provisioning.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-readiness-check.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/manager-state-verification.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/literature-scan.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/post-mvp-kickoff.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-from-scratch.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/competitor-experiment-reference.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/director-experiment-review.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-quality-lessons.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/ai-time-discipline.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/on-experiment-done.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/progress-report.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/submit-experiment.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/plan-next-experiment.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/write-paper-section.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/framing-reaudit.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-plan.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-refinement.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/reviewer-audit-checklist.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-visual-review.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/dream-report-action.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/method-improvement.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/dream-review-full.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/dream-review-simple.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md",
      "/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md"
    ],
    "durationMs": 690,
    "numFiles": 82,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me read the paper-writing-norms skill to understand style guidelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "eb62f7d8-6788-4089-aa21-fd4990e26910",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHFHqentk9gwyKuzcXjMGN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22122,
      "cache_read_input_tokens": 35357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22122
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Y4hAyLAqsWjBuRHxpeUKvX`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "8e42b4b5-c9a0-41df-9e3e-0a6a958a224b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHFHqentk9gwyKuzcXjMGN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22122,
      "cache_read_input_tokens": 35357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22122
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

_source line 24 · 2026-05-28T17:47:13.454Z_

<details><summary>↩ Tool result · `toolu_01Y4hAyLAqsWjBuRHxpeUKvX`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "95f8f733-ef48-4bfd-8d69-08835cdf9b6d",
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

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me analyze what I need to do:

1. The current method.tex has 4 subsections:
   - 3.1 Models and Connectors
   - 3.2 Pruning Protocol (very short)
   - 3.3 Compressibility Diagnostic: Importance CV
   - 3.4 Vision Token Re-encoder (VTR) (very short)

2. The director wants me to expand:
   a) Importance Scoring methods (L2-norm, Random, Attention-based) - currently just briefly mentioned in §3.2
   b) Keep Ratio k design space - currently just a list of values in §3.2
   c) Connector type's effect on Token Importance distribution with CV as diagnostic - partially covered in §3.3 but needs deepening

For the expansion, I need to substantially develop §3.2 with formal definitions of the pruning operation, mathematical formulations for L2-norm scoring and its justification, a random baseline for comparison, detailed attention-based scoring approaches including column-sum and rollout methods, a thorough exploration of the keep ratio k design space, and the importance margin definition.

§3.3 requires deepening as well—I need to formalize the CV definition beyond just the equation, discuss how CV operates as a continuous spectrum, explain why it predicts pruning tolerance better than alternatives, clarify why entropy alone is insufficient, and establish the connection to connector architecture.

Looking at the current structure in method.tex, §3.2 is compressed into a single paragraph covering multiple concepts, §3.3 is brief with just the CV equation, and §3.4 on VTR is similarly condensed. My strategy is to break §3.2 into distinct subsections addressing each scoring method and the k design space systematically, while expanding §3.3 to build the theoretical foundation for why CV serves as a diagnostic for pruning tolerance and how it relates to the connector design choices.

For the actual writing, I need to maintain the paper's conventions—using proper dashes for explanations, avoiding gerund phrase endings, and steering clear of colloquial phrasing—while keeping all mathematical content in proper equation environments and ensuring no new claims slip in beyond what's already established.

Within §3.2, I'll add a formal definition of the pruning operation itself: given a set of N tokens, a scoring function assigns importance values to each, and we retain only the top k fraction by score before physically removing and re-indexing the rest. This grounds the existing description in clearer mathematical language without restructuring the section.

For the scoring methods, I need to clarify what's actually tested versus what's mentioned in framing. The L2-norm approach uses activation magnitude as a proxy for information density, though it tends to favor high-activation tokens that may cluster together spatially. Random scoring serves as a null baseline to test whether token selection matters at all. Regarding attention-based scoring—the paper discusses attention entropy analysis in the framing, but doesn't actually use attention as a pruning criterion in the main experiments, so I should note this distinction rather than describe it as an implemented method. I need to be careful here—the director wants me to describe attention-based scoring variants as part of the design space, but I should make clear that we only actually evaluated L2-norm and random pruning. I can frame attention-based methods as theoretically motivated alternatives that exist in the literature without claiming we tested them, and use them to contextualize why we chose the simpler baselines that bracket the expected performance range.

For the CV diagnostic expansion, I'm adding mathematical rigor and listing all six models across the spectrum to show how coefficient of variation predicts pruning tolerance—high CV means tokens have differentiated importance so pruning can be selective, while low CV suggests uniform importance where there's less room to find dispensable tokens.

I also need to explain why entropy fails as a predictor despite being related, since it groups models with very different pruning behaviors together. Then I'll frame CV as a dual predictor that indicates both tolerance and optimal strategy.

For the k design space, I'm defining the parameter range and justifying the specific values chosen—0.3 for extreme pruning, 0.5 for moderate, 0.7 for mild, and 0.85-0.95 for conservative—plus introducing the cliff zone concept where different connectors have performance cliffs at different k thresholds.

Now I'm writing the LaTeX carefully, avoiding em-dashes and explanatory en-dashes, -ing phrase endings, and AI jargon like "leverage" or "facilitate."

Writing the pruning protocol section... L2 scoring can concentrate tokens in high-activation regions, losing spatial diversity. Random subsampling serves as a baseline—if L2 doesn't beat random selection, there's no exploitable signal in token norms—and naturally preserves spatial distribution across the token set, though it introduces sampling variance that we'll control through multiple evaluation runs. I'm defining the importance margin metric to compare L2 and random performance.

Attention-based methods like column sums and attention rollout offer another approach by extracting importance from the LLM's internal weights, but they require forward passes and are architecture-specific. Since L2-norm and random selection are backbone-agnostic and computationally efficient, they're better suited for revealing the connector-dependent structure we're investigating, though I'll use attention entropy as a diagnostic tool rather than a selection criterion.

Now I'm examining the retention ratio design space, testing values from 0.30 to 0.95 to map out how each connector type degrades under compression—from extreme token loss to minimal pruning—with intermediate points chosen to identify performance cliffs where small changes in retention cause sharp drops.

The empirical results show these cliffs manifest at different thresholds depending on architecture: pixel-shuffle connectors hit their breaking point at the most conservative ratio tested (0.95), BART-encoded connectors around 0.85, while MLPs degrade gradually without a sharp transition. This variation means I need denser sampling in the high-retention region to pinpoint exactly where each architecture fails.

Now I'm working through the expanded diagnostic section, defining the coefficient of variation metric for post-connector token norms as a single-pass predictor of pruning tolerance...

Writing LaTeX equations... token attention, raising CV to 0.151. The coefficient of variation essentially captures how unevenly token importance is distributed—high CV means some tokens matter far more than others and can be selectively pruned, while low CV suggests all tokens contribute similarly, making random removal as effective as importance-based selection. This also determines which pruning strategy works best: when CV is low, L2-norm ranking picks up spatial noise rather than real importance, so random pruning preserves coverage better, but when CV is high, norm-based ranking reliably identifies the most critical tokens.

Entropy alone doesn't provide enough discrimination between models with genuinely different pruning behaviors, since models like π₀.₅, X-VLA, and OpenVLA cluster together in entropy space despite responding very differently to pruning strategies.  The real insight is that entropy captures how the LLM reads and distributes its attention across tokens, while coefficient of variation captures how the connector itself structures its output—and it's the connector's output structure that actually determines robustness to pruning. I'm checking the file structure to see where the new content fits. The method.tex file has the section headers and subsections laid out, and I need to replace the existing §3.2 and §3.3 content with expanded versions while keeping the overall structure intact. Let me identify the exact line ranges for each section so I can make the replacements cleanly. I'm measuring token heterogeneity using the coefficient of variation of L2 norms—a single-pass diagnostic that captures how uniformly distributed token magnitudes are across the model. This metric ranges from near-uniform (π₀ at 0.038) to highly heterogeneous (SmolVLA at 0.314), revealing whether token importance is concentrated or spread evenly.

Now I'm thinking through how to write up the expanded method sections. I need to describe the attention-based scoring variants—column-sum, mean, and rollout approaches—but I should be careful about citations and make sure I'm only referencing papers already in the bibliography rather than adding new ones. I need to avoid citing papers that aren't in the bibliography, so I'll describe the attention flow methods without specific citations—framing them as established techniques from the token pruning literature. Now I'm thinking through the structure: my expanded §3.2 needs roughly 30-40 lines to substantially grow from its current 4, and §3.3 should expand from 9 lines to 25-35 lines to help reach the 8-page target. I should also make sure not to use "novel" in the descriptions.

For §3.2, I'm planning to cover the formal pruning setup with tokens and scoring functions, the L2-norm scoring approach with its justification and bias considerations, random subsampling as a baseline, the importance margin concept, a brief discussion of why attention-based alternatives aren't used, and the retention ratio design space with the cliff zone concept. For §3.3, I'll present the CV formula, show the CV spectrum across all six models, explain why CV predicts pruning tolerance and optimal strategy, and discuss why entropy alone isn't sufficient as a diagnostic.

I'm checking whether the paper already addresses attention entropy—I can see entropy values mentioned in the results but no dedicated subsection. The method section should explain what CV is and why it's the right metric for predicting pruning tolerance, while the results section presents the actual correlation data. Let me finalize the text now.

I should formalize the Importance CV definition and discussion in §3.3, then keep the attention-based scoring paragraph brief since we don't actually evaluate those methods. I'm also double-checking the formatting conventions for dashes in the existing method.tex to stay consistent.

The director also wants me to cover the "cliff zone" concept in the k design space section—that narrow range where performance drops sharply, which varies by architecture. I'll describe this conceptually in the methods and let the results section show where each model's cliff actually occurs, avoiding duplication.

Now I need to think through the attention-based scoring section more carefully before writing the actual edits. I need to decide whether to expand the VTR section or leave it as-is. The director gave three specific expansion directions, and VTR wasn't mentioned, so I'll hold off on that for now. Before I start writing, let me check the paper-writing norms about the text-equation-figure progression—my expanded §3.2 should include the scoring function definitions, and §3.3 already has the CV equation plus the spectrum visualization I'm adding. That covers the pattern well. Let me draft the edits now in two separate calls to keep things organized.

For §3.2, I'm planning to replace the single paragraph with an intro, then add separate sections on the importance scoring functions with L2-norm and random baselines, the importance margin concept, attention-based alternatives, and the retention ratio design space with the cliff zone discussion. For §3.3, I'll expand the CV equation text, add a dedicated paragraph on the CV spectrum with the align environment, then explain why CV predicts pruning tolerance and optimal strategy, plus the complementary role of attention entropy. Now I need to carefully match the exact old_string from the file to make sure the edits land correctly.

Looking at the specific lines, I can see the pruning setup describes the retention ratios and two bracketing strategies—L2 norm selection versus random subsampling—with the importance margin measuring the gap between them. The CV equation follows, quantifying token heterogeneity through the coefficient of variation of L2 norms, and it's designed as a single-pass diagnostic.

The next thinking extends this by showing how CV captures a spectrum from near-uniform tokens in π₀ to high heterogeneity in SmolVLA, where low-CV models are sensitive to which tokens get removed while high-CV models with entangling connectors degrade under any removal strategy.

I'll rewrite this as a natural continuation:

The coefficient of variation captures a spectrum from near-uniform token norms in π₀ to highly heterogeneous distributions in SmolVLA, revealing that low-CV models are sensitive to which tokens are pruned while high-CV models with entangling connectors fail regardless of the removal strategy. L2-norm scoring can suffer from spatial clustering under aggressive pruning, especially when token activations are nearly uniform. Random subsampling serves as a baseline to test whether the norm distribution contains meaningful signal—if L2 scoring doesn't beat random selection, there's no exploitable structure to leverage. Random selection also maintains spatial distribution in expectation, though sampling variance across runs requires multi-seed evaluation to control. Now I'm defining the importance margin metric to measure... I'm contrasting attention-based scoring methods—which require full forward passes through the LLM and are architecture-specific—with L2-norm and random scoring, which operate only on the connector output and remain backbone-agnostic. I'm using attention entropy as a diagnostic tool rather than a pruning strategy. Now I'm defining the retention ratio space, testing values from 30% to 95% of tokens to map out how each connector type degrades across the full compression spectrum. higher resolution in the results section. I'm also thinking about the overall length of this method section—it's grown substantially from the original, and I need to make sure it fits within the page constraints for a conference paper. The expansion from about 0.4 columns to roughly 1.2-1.5 columns is reasonable for a methods section, but I should be mindful not to let it balloon further. the end of a clause, not a sentence-ending phrase. Actually, let me reread: "allowing us to localize the transition with higher resolution" - this modifies the preceding clause, so it's acceptable as a modifier. But to be safe, I could restructure it.

Let me focus on the clear violations and fix those first. The main issue is "sacrificing spatial coverage for magnitude" - I need to rephrase that to avoid the -ing ending. And I should double-check if there are other sentence-final -ing phrases I'm missing.

Actually, I'm being too strict here. The style guide is specifically about dangling participial phrases at sentence ends like "demonstrating the effectiveness of..." These are weak constructions. My uses seem more integrated into the sentence structure. But let me be conservative and fix the clearest case anyway.

I'm noticing I need to be more careful about distinguishing between -ing forms that are genuinely problematic (dangling participials at sentence end) versus those that are fine (gerunds as objects, -ing as part of compound predicates, etc.). Let me revise my approach and focus on the actual violations rather than over-correcting. I'm checking the forward reference to the CV diagnostic section—it mentions attention entropy as a diagnostic metric, which my expanded version will cover, so that's consistent. Now I need to tighten the VTR section to be more specific about how the mechanism works: the cross-attention module with learned queries attends over all retained tokens to reconstruct the information that would be lost through hard pruning.

For the CV section expansion, I should clarify which three closed-loop models I'm referencing—π0.5, X-VLA, and OpenVLA—rather than leaving it vague. And when discussing entropy, I need to be careful to use the right values: the existing results mention OFT's attention entropy matching OpenVLA's, but I should pull the full entropy comparison from the paper framing to make the analysis more complete. I'm identifying the exact text spans for each section so I can make precise replacements—the old_string for §3.2 runs from "We apply post-connector" through "on token information structure," and §3.3 goes from "We quantify post-connector" to "under any removal strategy." For the attention-based scoring description, I'm keeping it intuitive without formulas since those methods aren't evaluated, and I'm being careful with punctuation like em-dashes in compound modifiers like "backbone-agnostic."

I'm also verifying my LaTeX formatting—using tildes for non-breaking spaces before the scoring method labels and adding proper equation labels for the L2-norm and random scoring formulas. Now I'm reconsidering whether the L2-norm formula needs expansion beyond the basic norm notation, or if that's sufficient for what the director requested.

Looking at the retention ratio values across the models—k=0.80 and 0.85 for X-VLA, k=0.925 for π0.5—these align with the results section. I want to clarify what "cliff zone" means in the retention ratio design space paragraph: it's where small decreases in k cause disproportionately large drops in success rate, as opposed to smooth proportional degradation.

Now I'm ready to finalize the edits. Let me verify the equation labels first—the existing §3.3 has its label intact, and my revised version keeps the same equation and label, so there's no conflict. Time to write out the actual edit commands for §3.2.

For the first section, I need to replace the text about post-connector token pruning, including the part about retention ratios, the L2 norm and random subsampling strategies, and the importance margin calculation that shows whether token importance structure is meaningful. Both approaches physically remove tokens and re-index positions, with pruning happening post-connector to isolate its effect on token information structure.

For the second section, I'm replacing the coefficient of variation definition that measures post-connector token heterogeneity through L2 norms, along with the equation and its label, and the explanation of CV as a single-pass diagnostic that captures the spectrum from one state to another.

Now I'm reconsidering how to present the CV spectrum across different models—whether to keep the underbrace notation or try a cleaner inline format instead. I'm reconsidering whether to use underbrace for the grouping—it could have rendering issues in the equation environment. Instead, I'll describe the connector types in surrounding text to show the spectrum clearly while keeping the equation itself simple and clean. I'm trying to figure out the document format—whether it's single or double column. The mix of `figure*` and regular `figure` environments suggests two columns, but I need to verify this against the actual CoRL 2025 template to know if my wide equation will fit properly.

Rather than risk overflow, I'll simplify the presentation by using a compact display format that shows the key comparison between models without trying to fit everything into one unwieldy equation.

Now I'm planning out the final structure for section 3.2—I want to expand it substantially with clear subsections on pruning operations, importance scoring functions, and attention-based alternatives, while keeping the prose tight and avoiding redundancy.

For section 3.3, I'm organizing the coefficient of variation discussion into focused paragraphs that explain the CV spectrum, how it predicts pruning tolerance, and why attention entropy alone isn't sufficient.

The total expansion should land around 1.7 to 1.8 columns, which feels like a meaningful addition without bloating the paper. Let me finalize the edits now.

Actually, I need to clarify something about the attention-based scoring methods the director mentioned. Column-sum, cross-layer mean, and attention rollout are established techniques in the NLP literature for identifying important tokens—they measure how much attention a token receives across the network or how information flows through layers. That's distinct from the attention entropy concept I'm discussing in the expansion, which focuses on the uniformity of the attention distribution itself rather than token importance scoring.

I should preserve the LaTeX conventions used throughout the paper—`\textbf{}` for bold, `\emph{}` for emphasis, the tight equals signs, citation formatting, and math variables in text. Now I'll write the actual edits, though I should be careful not to overstate the connection to concurrent work on VLM pruning methods like FastV and H2O, since that's already covered elsewhere in the framing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "40e2ebc7-8c94-4ea6-b0fb-4160f1abc269",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QzMG1RFAihrfARXgU9FiY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5716,
      "cache_read_input_tokens": 57479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5716
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

Now I have all the context. Let me expand method.tex with the three directions specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "abbd60aa-6970-4154-8251-f5bc20421ba9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QzMG1RFAihrfARXgU9FiY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5716,
      "cache_read_input_tokens": 57479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5716
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

<details open><summary>🔧 Tool call — Edit · `toolu_01UAYwZvTEC8KJDiC9ehjyte`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "We apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, retaining $\\lfloor k \\cdot N \\rfloor$ tokens. Two strategies bracket expected performance: \\textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \\textbf{random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. The \\emph{importance margin} at ratio $k$ is $\\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.",
  "new_string": "Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.85, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "cbe790af-e24d-44fb-9003-348b53284175",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QzMG1RFAihrfARXgU9FiY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5716,
      "cache_read_input_tokens": 57479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5716
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

_source line 28 · 2026-05-28T17:52:15.933Z_

<details><summary>↩ Tool result · `toolu_01UAYwZvTEC8KJDiC9ehjyte`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "b0563cc6-23b9-44ea-a392-a0a92eaac087",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "We apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, retaining $\\lfloor k \\cdot N \\rfloor$ tokens. Two strategies bracket expected performance: \\textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \\textbf{random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. The \\emph{importance margin} at ratio $k$ is $\\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.",
    "newString": "Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.85, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nWe apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, retaining $\\lfloor k \\cdot N \\rfloor$ tokens. Two strategies bracket expected performance: \\textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \\textbf{random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. The \\emph{importance margin} at ratio $k$ is $\\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nCV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\\pi_{0}$ (CV$\\,{=}\\,$0.038, near-uniform norms) to SmolVLA (CV$\\,{=}\\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding: a cross-attention module (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n",
    "structuredPatch": [
      {
        "oldStart": 44,
        "oldLines": 8,
        "newStart": 44,
        "newLines": 33,
        "lines": [
          " \\subsection{Pruning Protocol}",
          " \\label{sec:pruning_protocol}",
          " ",
          "-We apply post-connector token pruning at retention ratio $k \\in \\{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\\}$, retaining $\\lfloor k \\cdot N \\rfloor$ tokens. Two strategies bracket expected performance: \\textbf{L2 norm selection} retains the top-$k$ fraction by L2 norm, and \\textbf{random subsampling} selects $\\lfloor k \\cdot N \\rfloor$ tokens uniformly at random. The \\emph{importance margin} at ratio $k$ is $\\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$; a positive margin indicates token importance structure is informative. Both strategies physically remove unselected tokens and re-index position IDs. We prune post-connector to isolate the connector's effect on token information structure.",
          "+Given $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.",
          " ",
          "+\\paragraph{Importance scoring functions.}",
          "+A scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.",
          "+",
          "+\\textbf{L2-norm scoring} assigns each token its activation magnitude:",
          "+\\begin{equation}",
          "+s_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.",
          "+\\label{eq:l2_score}",
          "+\\end{equation}",
          "+The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).",
          "+",
          "+\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:",
          "+\\begin{equation}",
          "+s_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.",
          "+\\label{eq:random_score}",
          "+\\end{equation}",
          "+Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).",
          "+",
          "+The \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).",
          "+",
          "+\\paragraph{Attention-based alternatives.}",
          "+Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.",
          "+",
          "+\\paragraph{Retention ratio design space.}",
          "+We evaluate $k \\in \\{0.30, 0.50, 0.70, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.85, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results}).",
          "+",
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

_source line 29_

Now expanding §3.3 (Compressibility Diagnostic).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "4807b2f4-b6c4-4eb4-a2d8-7ea0482cd456",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DovzveQ554Ahd2QYKi63HR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15969,
      "cache_read_input_tokens": 63195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15969
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_019FNhegVxwi1BZASMqpXB5j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "We quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nCV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\\pi_{0}$ (CV$\\,{=}\\,$0.038, near-uniform norms) to SmolVLA (CV$\\,{=}\\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.",
  "new_string": "We seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{Random} - \\text{L2})$ decreases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "ea10fade-1dd0-448e-b00b-4fc271aa8bae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DovzveQ554Ahd2QYKi63HR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15969,
      "cache_read_input_tokens": 63195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15969
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

_source line 31 · 2026-05-28T17:52:54.696Z_

<details><summary>↩ Tool result · `toolu_019FNhegVxwi1BZASMqpXB5j`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "0727af34-3435-4d5d-8231-51272cdfdbab",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "We quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nCV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\\pi_{0}$ (CV$\\,{=}\\,$0.038, near-uniform norms) to SmolVLA (CV$\\,{=}\\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.",
    "newString": "We seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{Random} - \\text{L2})$ decreases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.85, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nCV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\\pi_{0}$ (CV$\\,{=}\\,$0.038, near-uniform norms) to SmolVLA (CV$\\,{=}\\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding: a cross-attention module (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 13,
        "newStart": 74,
        "newLines": 29,
        "lines": [
          " \\subsection{Compressibility Diagnostic: Importance CV}",
          " \\label{sec:cv_diagnostic}",
          " ",
          "-We quantify post-connector token heterogeneity via the coefficient of variation (CV) of L2 norms:",
          "+We seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:",
          " \\begin{equation}",
          " \\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}",
          " \\label{eq:cv}",
          " \\end{equation}",
          "-CV is a single-pass diagnostic requiring one forward pass with no downstream evaluation. It captures a continuous spectrum from $\\pi_{0}$ (CV$\\,{=}\\,$0.038, near-uniform norms) to SmolVLA (CV$\\,{=}\\,$0.314, high heterogeneity). Low-CV models have near-uniform tokens where \\emph{which} tokens are removed matters more than \\emph{how many}; high-CV entangling connectors fail catastrophically under any removal strategy.",
          "+where $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.",
          " ",
          "+\\paragraph{The CV spectrum.}",
          "+CV captures a continuous ordering across six models and three connector families:",
          "+\\begin{equation}",
          "+\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}",
          "+\\label{eq:cv_spectrum}",
          "+\\end{equation}",
          "+This ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.",
          "+",
          "+\\paragraph{CV as pruning tolerance predictor.}",
          "+CV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.",
          "+",
          "+CV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{Random} - \\text{L2})$ decreases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).",
          "+",
          "+\\paragraph{Complementary role of attention entropy.}",
          "+Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.",
          "+",
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

_source line 32_

Let me verify the final file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "9aa690b4-79f1-4a9b-b377-c5e01e3eef17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017G32mJGtUf4h9W1LrgRNSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 79164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1642
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

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01WYzU1TAR4RjUBRQGMqgUDX`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "64aaa12e-25a1-441f-851d-df3643eb08f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017G32mJGtUf4h9W1LrgRNSJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 79164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1642
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

_source line 34 · 2026-05-28T17:52:59.137Z_

<details><summary>↩ Tool result · `toolu_01WYzU1TAR4RjUBRQGMqgUDX`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
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
57	The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\ref{sec:linear_results}).
58	
59	\textbf{Random subsampling} draws $\lfloor kN \rfloor$ tokens uniformly at random:
60	\begin{equation}
61	s_{\text{rand}}(t_i) \sim \mathcal{U}(0, 1)\,.
62	\label{eq:random_score}
63	\end{equation}
64	Random selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\ref{sec:openvla_results}).
65	
66	The \emph{importance margin} at ratio $k$ is defined as $\Delta(k) = \text{SR}_{\text{L2}}(k) - \text{SR}_{\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\ref{sec:scaling_law}).
67	
68	\paragraph{Attention-based alternatives.}
69	Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\ref{sec:cv_diagnostic}), not as a pruning criterion.
70	
71	\paragraph{Retention ratio design space.}
72	We evaluate $k \in \{0.30, 0.50, 0.70, 0.85, 0.90, 0.95\}$, spanning from extreme compression (retaining 30\% of tokens) to conservative trimming (retaining 95\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \in \{0.80, 0.85, 0.925\}$) to localize the transition boundary (Section~\ref{sec:linear_results}).
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
87	\underbrace{\pi_0\,(0.038) \;<\; \pi_{0.5}\,(0.055)}_{\text{linear proj.}} \;<\; \underbrace{\text{X-VLA}\,(0.151)}_{\text{linear + BART}} \;<\; \underbrace{\text{OpenVLA}\,(0.215) \;\approx\; \text{OFT}\,(0.219)}_{\text{MLP proj.}} \;<\; \underbrace{\text{SmolVLA}\,(0.314)}_{\text{pixel-shuffle}}
88	\label{eq:cv_spectrum}
89	\end{equation}
90	This ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\,{<}\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\,{\approx}\,$0.22). Pixel-shuffle folds $4 \times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\,{=}\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\sim}$0.04) to 0.151.
91	
92	\paragraph{CV as pruning tolerance predictor.}
93	CV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.
94	
95	CV also predicts the \emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\Delta(\text{Random} - \text{L2})$ decreases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\ref{sec:scaling_law}).
96	
97	\paragraph{Complementary role of attention entropy.}
98	Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.
99	
100	\subsection{Vision Token Re-encoder (VTR)}
101	\label{sec:vtr}
102	
103	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding: a cross-attention module (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens. The compression ratio is controlled by $M \in \{16, 32, 64, 96, 128\}$; $M{=}N$ serves as a passthrough control.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "deaa7f2a-e28b-498f-860d-21302f689799",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.85, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{Random} - \\text{L2})$ decreases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding: a cross-attention module (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA) uses $M$ learned queries to attend over all $N$ source tokens. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
The file looks good. Let me do a quick quality check:

1. No em-dashes (—): ✓ (I used commas, semicolons, and parentheses instead)
2. No -ing phrase endings: Let me check...
   - Line 57: "at the cost of spatial coverage" ✓ (fixed from original draft)
   - Line 69: "not as a pruning criterion" ✓
   - Line 72: "to localize the transition boundary" ✓
   - Line 90: "raising CV from what..." ✓
   - No problematic -ing endings found. ✓
3. No AI-style words (leverage, utilize, delve, facilitate, etc.): ✓
4. No excessive "Furthermore/Moreover/Additionally": ✓
5. Mathematical formulas in equation environments: ✓ (eq:l2_score, eq:random_score, eq:cv, eq:cv_spectrum)
6. Consistent style with existing text: ✓ (uses \textbf{}, \emph{}, CV$\,{=}\,$, etc.)
7. No new claims or data introduced: ✓ (all numbers reference existing results)
8. Now I need to address the CoRL 2026 Limitations section.

The expansion is substantial—sections 3.2 and 3.3 together add roughly two columns of content with new equations and structured paragraphs, which should help reach the 8-page target. I'm checking that all labels are unique and references point to valid sections, and so far the new equation labels and cross-references check out. I've verified the citation reuse is acceptable, and the expansion successfully addresses all three areas the director requested: the importance scoring methods with their mathematical foundations and intuitions, the keep ratio design space with formal definitions and the cliff zone concept, and the connector-CV relationship explaining why CV predicts both tolerance and optimal strategy while entropy alone falls short. The document is ready.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "feb44d3b-1857-44ab-b0d0-b2e61d2a612c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6eEXptfZdTqL2gM52TwMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4133,
      "cache_read_input_tokens": 80806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4133
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

File is clean and well-structured. Let me run a quick check for style violations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "842b6362-0115-423d-a4c8-10dd1c5f7696",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6eEXptfZdTqL2gM52TwMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4133,
      "cache_read_input_tokens": 80806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4133
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

<details open><summary>🔧 Tool call — Bash · `toolu_01NWfVE2DRWBN1WYtDTeYYrS`</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "description": "Check for em-dashes (AI style violation)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "0e9007cc-2221-444e-b691-30ffd8147112",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6eEXptfZdTqL2gM52TwMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4133,
      "cache_read_input_tokens": 80806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4133
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_0139sLrStzuHzjBCGmMo53bf`</summary>

```json
{
  "command": "grep -n \"ing,\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex | head -20",
  "description": "Check for -ing participial phrases"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "7d953143-4576-4bd3-97bc-ef62e6db2199",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6eEXptfZdTqL2gM52TwMR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4133,
      "cache_read_input_tokens": 80806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4133
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

_source line 39 · 2026-05-28T17:53:21.185Z_

<details><summary>↩ Tool result · `toolu_01NWfVE2DRWBN1WYtDTeYYrS`</summary>

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
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "40d81c93-11a8-41ff-812a-89a905fedca2",
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

### Tool result

_source line 40 · 2026-05-28T17:53:21.195Z_

<details><summary>↩ Tool result · `toolu_0139sLrStzuHzjBCGmMo53bf`</summary>

```text
13:\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).
57:The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\ref{sec:linear_results}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "cdb55b6d-3a6f-470d-90a2-ce733ecb5933",
  "tool_use_result": {
    "stdout": "13:\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n57:The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).",
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

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Let me check: 
- Line 13: "concatenating 16 contiguous patches" - this is a participial phrase in the middle of a sentence, not at the end. It's part of the original text (§3.1 which I didn't modify). The grep matched "ing," but actually looking at it, it's "folding, concatenating" - "concatenating" is a participial phrase that continues after a comma. This is from the original text, not my additions.
- Line 57: "however, because" - the grep matched "however," which contains "ing" - wait no, "however" doesn't have "ing". Let me re-check. 

Actually, I need to look more carefully at what the grep pattern is matching. The pattern "ing," would catch any occurrence of those exact characters in sequence. Looking at line 57 again: "L2 scoring introduces a spatial bias, however," - the "scoring," part would match the pattern since it ends with "ing,". So "scoring" here is functioning as a noun in the phrase "L2 scoring introduces," not as a participial phrase, which means it shouldn't be flagged by my search criteria. The matches are all just nouns used in regular sentence construction, not participial phrases. No em-dashes either, so the expansion is done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "94418c95-2f6e-4ead-82d9-c1f930affdf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155DMrMLF7oJRgNPM4ZpZXe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1263,
      "cache_read_input_tokens": 84939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1263
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

_source line 42_

Zero em-dashes. The `ing,` matches are all nouns (scoring, pruning, folding) in normal sentence structure, not dangling participial phrases.

Expansion complete. Summary of changes to `method.tex`:

**§3.2 Pruning Protocol** (was 1 paragraph, now 4 `\paragraph` blocks + 2 equations):
- Formal pruning operation definition with $\lfloor kN \rfloor$ notation
- **L2-norm scoring**: formula (Eq. 3), information density justification, spatial bias analysis
- **Random subsampling**: formula (Eq. 4), null hypothesis framing, spatial preservation property
- **Importance margin**: formal definition $\Delta(k)$, interpretation of positive/negative margins
- **Attention-based alternatives**: column-sum, cross-layer mean, attention rollout with intuitions; why we use L2/random instead
- **Retention ratio design space**: $k$ range rationale, cliff zone concept, per-architecture cliff locations

**§3.3 Compressibility Diagnostic** (was 1 equation + 1 paragraph, now 1 equation + spectrum equation + 4 `\paragraph` blocks):
- **CV spectrum** (Eq. 6): all 6 models ordered with connector-family grouping via `\underbrace`
- **CV as tolerance predictor**: high CV = dispensable tokens exist, low CV = uniform criticality; CV also predicts optimal strategy (L2 vs random)
- **Entropy comparison**: entropy clusters π0.5/X-VLA/OpenVLA (0.61--0.67) despite different pruning behaviors; "reading pattern" vs "writing pattern" distinction

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "uuid": "4ac2928a-f0e5-4404-940e-4824063be519",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155DMrMLF7oJRgNPM4ZpZXe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1263,
      "cache_read_input_tokens": 84939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1263
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

### Task result

_source line 43_

Zero em-dashes. The `ing,` matches are all nouns (scoring, pruning, folding) in normal sentence structure, not dangling participial phrases.

Expansion complete. Summary of changes to `method.tex`:

**§3.2 Pruning Protocol** (was 1 paragraph, now 4 `\paragraph` blocks + 2 equations):
- Formal pruning operation definition with $\lfloor kN \rfloor$ notation
- **L2-norm scoring**: formula (Eq. 3), information density justification, spatial bias analysis
- **Random subsampling**: formula (Eq. 4), null hypothesis framing, spatial preservation property
- **Importance margin**: formal definition $\Delta(k)$, interpretation of positive/negative margins
- **Attention-based alternatives**: column-sum, cross-layer mean, attention rollout with intuitions; why we use L2/random instead
- **Retention ratio design space**: $k$ range rationale, cliff zone concept, per-architecture cliff locations

**§3.3 Compressibility Diagnostic** (was 1 equation + 1 paragraph, now 1 equation + spectrum equation + 4 `\paragraph` blocks):
- **CV spectrum** (Eq. 6): all 6 models ordered with connector-family grouping via `\underbrace`
- **CV as tolerance predictor**: high CV = dispensable tokens exist, low CV = uniform criticality; CV also predicts optimal strategy (L2 vs random)
- **Entropy comparison**: entropy clusters π0.5/X-VLA/OpenVLA (0.61--0.67) despite different pruning behaviors; "reading pattern" vs "writing pattern" distinction

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 414560,
  "duration_api_ms": 415556,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "5c041521-e8e2-414d-abe9-e8e6614720ac",
  "total_cost_usd": 1.2132082499999999,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 74357,
    "cache_read_input_tokens": 471986,
    "output_tokens": 20384,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 74357,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 969,
        "cache_read_input_tokens": 84939,
        "cache_creation_input_tokens": 1263,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1263
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2724,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002819,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 20384,
      "cacheReadInputTokens": 471986,
      "cacheCreationInputTokens": 74357,
      "webSearchRequests": 0,
      "costUSD": 1.21038925,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ca7a2d74-6f21-4d39-9fc2-bb15e645b380"
}
```

</details>

---
