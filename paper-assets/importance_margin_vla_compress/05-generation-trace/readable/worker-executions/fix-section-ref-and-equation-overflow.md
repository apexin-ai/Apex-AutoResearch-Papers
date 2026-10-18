# fix section ref and equation overflow

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_fix_section_ref_and_equation_overflow_20260528T181422.log`
- **Structured JSON:** [`0969186e38b47cd6cb33.json`](../../sessions/09/0969186e38b47cd6cb33.json)

## Before a recorded user message

34 recorded events

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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
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
  "uuid": "90cf0461-885a-41d0-b283-b90906f24be1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1780003800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "48a4249b-7317-4020-aea6-2b90f785ab52",
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec"
}
```

---

### Assistant

_source line 4_

Looking at method.tex to find both issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "cae97dd0-e908-44b1-a1d6-27493a4462a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaGWkYApwRXkG346arn2xd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12675,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12675
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

<details open><summary>🔧 Tool call — Read · `toolu_01Jzy1zhqnaUE1Sd4KtqceQb`</summary>

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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "b5f0c9cc-d4c5-408b-8fe9-5e31b30879d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaGWkYApwRXkG346arn2xd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12675,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12675
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

_source line 6 · 2026-05-28T18:14:35.258Z_

<details><summary>↩ Tool result · `toolu_01Jzy1zhqnaUE1Sd4KtqceQb`</summary>

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
72	We evaluate $k \in \{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\}$, spanning from extreme compression (retaining 30\% of tokens) to conservative trimming (retaining 95\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \in \{0.80, 0.925\}$) to localize the transition boundary (Section~\ref{sec:linear_results}).
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
95	CV also predicts the \emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\Delta(\text{L2} - \text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\ref{sec:scaling_law}).
96	
97	\paragraph{Complementary role of attention entropy.}
98	Attention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.
99	
100	\subsection{Vision Token Re-encoder (VTR)}
101	\label{sec:vtr}
102	
103	Hard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.
104	
105	\paragraph{Architecture.}
106	VTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \in \{16, 32, 64, 96, 128\}$; $M{=}N$ serves as a passthrough control.
107	
108	\paragraph{Training and cost.}
109	The module adds ${\sim}$22M trainable parameters ($<$5\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\ref{app:smart_compress_details}.
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "8aef9350-3a15-420e-ba63-cd2228f40196",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze both issues:

**Issue 1: "Section ??"**
Looking at line 72, I see:
`to localize the transition boundary (Section~\ref{sec:linear_results})`

But wait, the user mentions "Section ??". Let me look more carefully. Line 72 references `\ref{sec:linear_results}`. Let me check if this label exists.

Actually, looking at line 72 more carefully:
`we add finer-grained ratios ($k \in \{0.80, 0.925\}$) to localize the transition boundary (Section~\ref{sec:linear_results}).`


The "Section ??" error means that `sec:linear_results` label isn't defined anywhere in the document, so I need to find where this section should be labeled or fix the reference.

**Issue 2: Equation 4**
Looking at the equations I've found so far, I'm counting them in order: the L2 score equation, the random score equation, the CV equation, and the CV spectrum equation. That last one at lines 86-89 should be Equation 4, so I need to verify it has the correct label.

The CV spectrum equation is quite complex with multiple underbrace groups comparing different model projections and their performance values. It's definitely too wide for a two-column layout and will overflow. I should search through the experiments.tex and results files to understand the full context and find where the `sec:linear_results` label should be defined.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "ebf02d72-83bf-4c1c-9641-35492994248c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6R7aGTVSRcQhSEZR3zNRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4296,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4296
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

_source line 8_

Found the file. Now searching for the referenced label `sec:linear_results` and checking Equation 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "977b9903-fda3-4a28-83f8-a17b57b6c79d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6R7aGTVSRcQhSEZR3zNRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4296,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4296
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

_source line 9_

<details open><summary>🔧 Tool call — Grep · `toolu_01CsVhwQ1JF8uTWCTTjn3vxg`</summary>

```json
{
  "pattern": "\\\\label\\{sec:linear_results\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "f5461be0-35e0-4698-b146-18cc50c0e495",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6R7aGTVSRcQhSEZR3zNRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4296,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4296
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

_source line 10 · 2026-05-28T18:14:48.975Z_

<details><summary>↩ Tool result · `toolu_01CsVhwQ1JF8uTWCTTjn3vxg`</summary>

```text
Found 2 files
docs/paper/results.tex
docs/paper/results_v2.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "8bf9642b-aa6b-4cdc-8053-9aececeb0eb7",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "docs/paper/results.tex",
      "docs/paper/results_v2.tex"
    ],
    "numFiles": 2
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Grep · `toolu_014GfjAXuGA3EDTvFJBqZ7dX`</summary>

```json
{
  "pattern": "\\\\ref\\{sec:linear_results\\}",
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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "f02e772f-1ea8-4154-899b-606c74297d58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6R7aGTVSRcQhSEZR3zNRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4296,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4296
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

_source line 12 · 2026-05-28T18:14:49.968Z_

<details><summary>↩ Tool result · `toolu_014GfjAXuGA3EDTvFJBqZ7dX`</summary>

```text
docs/paper/results_v2.tex:9:[Omitted long matching line]
docs/paper/method.tex:57:[Omitted long matching line]
docs/paper/method.tex:72:[Omitted long matching line]
docs/paper/results.tex:9:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "9f0ad68f-ae59-4966-bc16-67fbfd00fdd2",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/results_v2.tex:9:[Omitted long matching line]\ndocs/paper/method.tex:57:[Omitted long matching line]\ndocs/paper/method.tex:72:[Omitted long matching line]\ndocs/paper/results.tex:9:[Omitted long matching line]",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ek7DDbrSxiFFBAuWGKnkJn`</summary>

```json
{
  "pattern": "linear.results|pi.*0\\.5.*results|\\\\label\\{sec:",
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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "efabe75e-784c-42e7-864f-d2133d9566e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6R7aGTVSRcQhSEZR3zNRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4296,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4296
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

_source line 14 · 2026-05-28T18:14:51.579Z_

<details><summary>↩ Tool result · `toolu_01Ek7DDbrSxiFFBAuWGKnkJn`</summary>

```text
docs/paper/analysis.tex:2:\label{sec:analysis}
docs/paper/related_work.tex:2:\label{sec:related_work}
docs/paper/experiments.tex:2:\label{sec:experiments}
docs/paper/experiments.tex:5:\label{sec:exp_setup}
docs/paper/experiments.tex:12:\label{sec:two_axis}
docs/paper/experiments.tex:34:\caption{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\leq}$6.6\% across all conditions. $\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\ref{tab:full_results}.}
docs/paper/experiments.tex:62:\label{sec:pixel_shuffle}
docs/paper/experiments.tex:84:\label{sec:zeromask}
docs/paper/experiments.tex:89:\label{sec:cv_sensitivity}
docs/paper/experiments.tex:107:\label{sec:vtr_recovery}
docs/paper/experiments.tex:130:\textbf{Efficiency.}\label{sec:efficiency} For $\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\sim}$16\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\% compression with ${\leq}$1.1\,pp below passthrough.
docs/paper/conclusion.tex:2:\label{sec:conclusion}
docs/paper/conclusion.tex:3:\label{sec:analysis}
docs/paper/main.log:561:LaTeX Warning: Reference `sec:linear_results' on page 4 undefined on input line
docs/paper/main.log:574:LaTeX Warning: Reference `sec:linear_results' on page 5 undefined on input line
docs/paper/results_v2.tex:2:\label{sec:results}
docs/paper/results_v2.tex:7:\label{sec:taxonomy_overview}
docs/paper/results_v2.tex:9:[Omitted long matching line]
docs/paper/results_v2.tex:34:\label{sec:smolvla_results}
docs/paper/results_v2.tex:41:\label{sec:openvla_results}
docs/paper/results_v2.tex:50:\label{sec:linear_results}
docs/paper/results_v2.tex:67:\label{sec:smart_compress_results}
docs/paper/results_v2.tex:100:\label{sec:scaling_law}
docs/paper/sections/analysis.tex:10:\label{sec:analysis}
docs/paper/sections/analysis.tex:18:\label{sec:uniform_attention}
docs/paper/sections/analysis.tex:47:\label{sec:action_disruption}
docs/paper/sections/analysis.tex:77:\label{sec:metric_disconnect}
docs/paper/sections/analysis.tex:118:\label{sec:why_vit_works}
docs/paper/sections/related_work_draft.tex:2:\label{sec:related_work}
docs/paper/sections/experiments.tex:14:\label{sec:results}
docs/paper/sections/results_draft.tex:2:\label{sec:results}
docs/paper/sections/results_draft.tex:7:\label{sec:smolvla_results}
docs/paper/sections/results_draft.tex:57:\label{sec:openvla_results}
docs/paper/sections/analysis_draft.tex:2:\label{sec:analysis}
docs/paper/sections/analysis_draft.tex:7:\label{sec:pixel_shuffle}
docs/paper/sections/analysis_draft.tex:14:\label{sec:attention_distribution}
docs/paper/sections/analysis_draft.tex:25:\label{sec:learned_compression}
docs/paper/sections/background.tex:4:\label{sec:background}
docs/paper/sections/background.tex:9:\label{sec:smolvla_arch}
docs/paper/sections/background.tex:57:\label{sec:libero_bench}
docs/paper/sections/experimental_setup.tex:4:\label{sec:experimental_setup}
docs/paper/sections/experimental_setup.tex:9:\label{sec:acis_scorer}
docs/paper/sections/experimental_setup.tex:18:\label{sec:ablation_design}
docs/paper/sections/experimental_setup.tex:40:\label{sec:eval_protocol}
docs/paper/sections/introduction.tex:4:\label{sec:introduction}
docs/paper/method.tex:2:\label{sec:method}
docs/paper/method.tex:5:\label{sec:models}
docs/paper/method.tex:45:\label{sec:pruning_protocol}
docs/paper/method.tex:57:[Omitted long matching line]
docs/paper/method.tex:72:[Omitted long matching line]
docs/paper/method.tex:75:\label{sec:cv_diagnostic}
docs/paper/method.tex:101:\label{sec:vtr}
docs/paper/introduction.tex:2:\label{sec:introduction}
docs/paper/limitations.tex:2:\label{sec:limitations}
docs/paper/background.tex:4:\label{sec:background}
docs/paper/background.tex:9:\label{sec:smolvla_arch}
docs/paper/background.tex:47:\label{sec:openvla_arch}
docs/paper/background.tex:61:\label{sec:libero_bench}
docs/paper/appendix.tex:93:[Omitted long matching line]
docs/paper/appendix.tex:756:\label{sec:diagnostic}
docs/paper/appendix.tex:771:\label{sec:learned_compression}
docs/paper/appendix.tex:784:\label{sec:metric_disconnect}
docs/paper/results.tex:2:\label{sec:results}
docs/paper/results.tex:7:\label{sec:taxonomy_overview}
docs/paper/results.tex:9:[Omitted long matching line]
docs/paper/results.tex:34:\label{sec:smolvla_results}
docs/paper/results.tex:41:\label{sec:openvla_results}
docs/paper/results.tex:50:\label{sec:linear_results}
docs/paper/results.tex:67:\label{sec:smart_compress_results}
docs/paper/results.tex:100:\label{sec:scaling_law}
docs/paper/results.tex:123:\label{sec:cross_suite}
docs/paper/experimental_setup.tex:2:\label{sec:experimental_setup}
docs/paper/experimental_setup.tex:5:\label{sec:setup_overview}
docs/paper/experimental_setup.tex:14:\label{sec:pruning_protocol}
docs/paper/experimental_setup.tex:19:\label{sec:smart_compress_setup}
docs/paper/experimental_setup.tex:24:\label{sec:diagnostic_metrics}
docs/paper/experiments_deprecated.tex:3:\label{sec:results}
docs/paper/main.aux:85:\@writefile{lot}{\contentsline {table}{\numberline {2}{\ignorespaces Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\leq }$6.6\% across all conditions. $\pi _{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\ref {tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\ref {tab:full_results}.}}{7}{table.caption.17}\protected@file@percent }
docs/paper/main.aux:86:\newlabel{tab:main_results}{{2}{7}{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\leq }$6.6\% across all conditions. $\pi _{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\ref {tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\ref {tab:full_results}}{table.caption.17}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "edbab0a0-4c03-40ab-955b-c9494d1cd661",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/analysis.tex:2:\\label{sec:analysis}\ndocs/paper/related_work.tex:2:\\label{sec:related_work}\ndocs/paper/experiments.tex:2:\\label{sec:experiments}\ndocs/paper/experiments.tex:5:\\label{sec:exp_setup}\ndocs/paper/experiments.tex:12:\\label{sec:two_axis}\ndocs/paper/experiments.tex:34:\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\ndocs/paper/experiments.tex:62:\\label{sec:pixel_shuffle}\ndocs/paper/experiments.tex:84:\\label{sec:zeromask}\ndocs/paper/experiments.tex:89:\\label{sec:cv_sensitivity}\ndocs/paper/experiments.tex:107:\\label{sec:vtr_recovery}\ndocs/paper/experiments.tex:130:\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\ndocs/paper/conclusion.tex:2:\\label{sec:conclusion}\ndocs/paper/conclusion.tex:3:\\label{sec:analysis}\ndocs/paper/main.log:561:LaTeX Warning: Reference `sec:linear_results' on page 4 undefined on input line\ndocs/paper/main.log:574:LaTeX Warning: Reference `sec:linear_results' on page 5 undefined on input line\ndocs/paper/results_v2.tex:2:\\label{sec:results}\ndocs/paper/results_v2.tex:7:\\label{sec:taxonomy_overview}\ndocs/paper/results_v2.tex:9:[Omitted long matching line]\ndocs/paper/results_v2.tex:34:\\label{sec:smolvla_results}\ndocs/paper/results_v2.tex:41:\\label{sec:openvla_results}\ndocs/paper/results_v2.tex:50:\\label{sec:linear_results}\ndocs/paper/results_v2.tex:67:\\label{sec:smart_compress_results}\ndocs/paper/results_v2.tex:100:\\label{sec:scaling_law}\ndocs/paper/sections/analysis.tex:10:\\label{sec:analysis}\ndocs/paper/sections/analysis.tex:18:\\label{sec:uniform_attention}\ndocs/paper/sections/analysis.tex:47:\\label{sec:action_disruption}\ndocs/paper/sections/analysis.tex:77:\\label{sec:metric_disconnect}\ndocs/paper/sections/analysis.tex:118:\\label{sec:why_vit_works}\ndocs/paper/sections/related_work_draft.tex:2:\\label{sec:related_work}\ndocs/paper/sections/experiments.tex:14:\\label{sec:results}\ndocs/paper/sections/results_draft.tex:2:\\label{sec:results}\ndocs/paper/sections/results_draft.tex:7:\\label{sec:smolvla_results}\ndocs/paper/sections/results_draft.tex:57:\\label{sec:openvla_results}\ndocs/paper/sections/analysis_draft.tex:2:\\label{sec:analysis}\ndocs/paper/sections/analysis_draft.tex:7:\\label{sec:pixel_shuffle}\ndocs/paper/sections/analysis_draft.tex:14:\\label{sec:attention_distribution}\ndocs/paper/sections/analysis_draft.tex:25:\\label{sec:learned_compression}\ndocs/paper/sections/background.tex:4:\\label{sec:background}\ndocs/paper/sections/background.tex:9:\\label{sec:smolvla_arch}\ndocs/paper/sections/background.tex:57:\\label{sec:libero_bench}\ndocs/paper/sections/experimental_setup.tex:4:\\label{sec:experimental_setup}\ndocs/paper/sections/experimental_setup.tex:9:\\label{sec:acis_scorer}\ndocs/paper/sections/experimental_setup.tex:18:\\label{sec:ablation_design}\ndocs/paper/sections/experimental_setup.tex:40:\\label{sec:eval_protocol}\ndocs/paper/sections/introduction.tex:4:\\label{sec:introduction}\ndocs/paper/method.tex:2:\\label{sec:method}\ndocs/paper/method.tex:5:\\label{sec:models}\ndocs/paper/method.tex:45:\\label{sec:pruning_protocol}\ndocs/paper/method.tex:57:[Omitted long matching line]\ndocs/paper/method.tex:72:[Omitted long matching line]\ndocs/paper/method.tex:75:\\label{sec:cv_diagnostic}\ndocs/paper/method.tex:101:\\label{sec:vtr}\ndocs/paper/introduction.tex:2:\\label{sec:introduction}\ndocs/paper/limitations.tex:2:\\label{sec:limitations}\ndocs/paper/background.tex:4:\\label{sec:background}\ndocs/paper/background.tex:9:\\label{sec:smolvla_arch}\ndocs/paper/background.tex:47:\\label{sec:openvla_arch}\ndocs/paper/background.tex:61:\\label{sec:libero_bench}\ndocs/paper/appendix.tex:93:[Omitted long matching line]\ndocs/paper/appendix.tex:756:\\label{sec:diagnostic}\ndocs/paper/appendix.tex:771:\\label{sec:learned_compression}\ndocs/paper/appendix.tex:784:\\label{sec:metric_disconnect}\ndocs/paper/results.tex:2:\\label{sec:results}\ndocs/paper/results.tex:7:\\label{sec:taxonomy_overview}\ndocs/paper/results.tex:9:[Omitted long matching line]\ndocs/paper/results.tex:34:\\label{sec:smolvla_results}\ndocs/paper/results.tex:41:\\label{sec:openvla_results}\ndocs/paper/results.tex:50:\\label{sec:linear_results}\ndocs/paper/results.tex:67:\\label{sec:smart_compress_results}\ndocs/paper/results.tex:100:\\label{sec:scaling_law}\ndocs/paper/results.tex:123:\\label{sec:cross_suite}\ndocs/paper/experimental_setup.tex:2:\\label{sec:experimental_setup}\ndocs/paper/experimental_setup.tex:5:\\label{sec:setup_overview}\ndocs/paper/experimental_setup.tex:14:\\label{sec:pruning_protocol}\ndocs/paper/experimental_setup.tex:19:\\label{sec:smart_compress_setup}\ndocs/paper/experimental_setup.tex:24:\\label{sec:diagnostic_metrics}\ndocs/paper/experiments_deprecated.tex:3:\\label{sec:results}\ndocs/paper/main.aux:85:\\@writefile{lot}{\\contentsline {table}{\\numberline {2}{\\ignorespaces Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq }$6.6\\% across all conditions. $\\pi _{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref {tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref {tab:full_results}.}}{7}{table.caption.17}\\protected@file@percent }\ndocs/paper/main.aux:86:\\newlabel{tab:main_results}{{2}{7}{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq }$6.6\\% across all conditions. $\\pi _{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref {tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref {tab:full_results}}{table.caption.17}{}}",
    "numLines": 79
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture:

**Issue 1**: `sec:linear_results` is referenced in method.tex lines 57 and 72. The label exists in both `results.tex:50` and `results_v2.tex:50`. The LaTeX log confirms it's undefined on pages 4-5. Let me check which results file is actually included in main.tex to understand why the reference is broken.

Wait, actually the log says the reference is undefined. Let me check main.tex to see which files are included.

Actually, looking at the grep results more carefully, the label `sec:linear_results` IS defined in `results.tex:50` and `results_v2.tex:50`. 

The LaTeX warning about the undefined reference suggests either results.tex isn't being included in main.tex, or results_v2.tex is being used instead. The "Section ??" display confirms the reference isn't resolving. I need to check main.tex to see which file is actually being input, since the label definitely exists in the source files. I need to see the next thinking to rewrite it. Could you provide the next thinking chunk that follows the current rewritten thinking?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "d609d309-5dc6-4257-b5c0-4f0242e132ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NzTCcEUq3xuqpuyHSQjtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 28816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3204
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

_source line 16_

The label `sec:linear_results` exists in results.tex (line 50) and results_v2.tex (line 50), but the LaTeX log says it's undefined. Let me check which files main.tex includes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "4e50d7f3-66f8-468e-afad-6d415c4fc267",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NzTCcEUq3xuqpuyHSQjtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 28816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3204
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

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01MBQh7XCrCTjnigawbgqu81`</summary>

```json
{
  "pattern": "\\\\input|\\\\include",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex",
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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "74f52b26-8001-43be-ae14-28c0a93fb54f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NzTCcEUq3xuqpuyHSQjtJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 28816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3204
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

_source line 18 · 2026-05-28T18:15:07.479Z_

<details><summary>↩ Tool result · `toolu_01MBQh7XCrCTjnigawbgqu81`</summary>

```text
26:\input{abstract}
30:\input{introduction}
32:\input{related_work}
34:\input{method}
36:\input{experiments}
38:\input{conclusion}
40:\input{limitations}
44:\input{appendix}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "5ace450e-5dd4-4c58-8de9-657c5e3e4dc3",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "26:\\input{abstract}\n30:\\input{introduction}\n32:\\input{related_work}\n34:\\input{method}\n36:\\input{experiments}\n38:\\input{conclusion}\n40:\\input{limitations}\n44:\\input{appendix}",
    "numLines": 8
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The main.tex includes `experiments.tex`, not `results.tex` or `results_v2.tex`. Looking at the labels in experiments.tex, I see labels like `sec:experiments`, `sec:exp_setup`, `sec:two_axis`, `sec:pixel_shuffle`, `sec:zeromask`, `sec:cv_sensitivity`, `sec:vtr_recovery`, `sec:efficiency`. There is NO `sec:linear_results` in experiments.tex.

So the issue is that method.tex references `\ref{sec:linear_results}` which is defined in results.tex, but main.tex includes experiments.tex instead of results.tex. 

The label doesn't exist in the included files, so I need to check what `sec:linear_results` actually covers in results.tex and find the corresponding section in experiments.tex that discusses L2 scoring spatial bias at low k values and the transition boundary localization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "773771f4-3391-4689-a2b8-41a2a3ce49c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqfXKUJK9tHLhngucJhXsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 32020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 781
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

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01MH1xheZGQrZFYBsCGjKaGF`</summary>

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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "daffdf91-d310-4342-b127-72b7d12eafd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XqfXKUJK9tHLhngucJhXsZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 32020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 781
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

_source line 21 · 2026-05-28T18:15:16.613Z_

<details><summary>↩ Tool result · `toolu_01MH1xheZGQrZFYBsCGjKaGF`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\times$ 50 episodes each).
8	
9	Four models are evaluated in closed-loop control: $\pi_{0.5}$~\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$, 128 tokens, CV$\,{=}\,$0.314). Two additional models ($\pi_{0}$~\cite{black2024pi0}, OFT~\cite{kim2025openoft}) are analyzed via offline metrics only. Table~\ref{tab:model_properties} summarizes all six architectures. We prune at $k \in \{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\}$, reporting mean success rate (SR) over 500 episodes.
10	
11	\subsection{Two-Axis Framework Overview}
12	\label{sec:two_axis}
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
17	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
18	\label{fig:pruning_overview}
19	\end{figure}
20	
21	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
22	
23	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. L2 maintains ${\geq}$98.0\% through $k{=}0.85$, while random at $k{=}0.9$ collapses to 9.0\%---an 89\,pp method gap from identical removal fractions.
24	
25	\textbf{X-VLA (BART encoder, CV$\,{=}\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\,pp, yet the same model drops 27.4\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.
26	
27	\textbf{OpenVLA (MLP, CV$\,{=}\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\ref{tab:full_results}; Section~\ref{sec:analysis}).
28	
29	\textbf{SmolVLA (pixel-shuffle, CV$\,{=}\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\leq}$6.6\% across all suites and methods---a catastrophic cliff detailed below.
30	
31	\begin{table*}[t]
32	\centering
33	\small
34	\caption{Closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\leq}$6.6\% across all conditions. $\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\ref{tab:full_results}.}
35	\label{tab:main_results}
36	\begin{tabular}{llcccc}
37	\toprule
38	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
39	\midrule
40	\multirow{4}{*}{$\pi_{0.5}$}
41	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 33.4 / 69.4 \\
42	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\
43	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\
44	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\
45	\midrule
46	\multirow{4}{*}{X-VLA}
47	& Object  & \textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\
48	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\
49	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\
50	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\
51	\midrule
52	\multirow{4}{*}{SmolVLA}
53	& Object  & \textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
54	& Spatial & \textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
55	& Goal    & \textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\
56	& Long    & \textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\
57	\bottomrule
58	\end{tabular}
59	\end{table*}
60	
61	\subsection{Pixel-Shuffle Entanglement}
62	\label{sec:pixel_shuffle}
63	
64	\begin{figure*}[t]
65	\centering
66	\begin{subfigure}[t]{0.495\textwidth}
67	\centering
68	\includegraphics[width=\linewidth]{figures/paper/fig_pixel_shuffle.pdf}
69	\caption{}\label{fig:pixel_shuffle}
70	\end{subfigure}
71	\hfill
72	\begin{subfigure}[t]{0.495\textwidth}
73	\centering
74	\includegraphics[width=\linewidth]{figures/paper/fig_method_gap.pdf}
75	\caption{}\label{fig:method_gap}
76	\end{subfigure}
77	\caption{Token entanglement and scoring sensitivity. \textbf{(a)}~Pixel-shuffle $4{\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \textbf{(b)}~Method gap $|\text{SR(L2)} - \text{SR(Random)}|$ at $k{=}0.95$: $\pi_{0.5}$'s Object gap (24.2\,pp) exceeds X-VLA's maximum (1.4\,pp) by $17{\times}$ (single seed except $\pi_{0.5}$ Long, $n{=}5$).}
78	\label{fig:entanglement_scoring}
79	\end{figure*}
80	
81	SmolVLA's pixel-shuffle $4{\times}4$ folding concatenates 16 patches per token (Figure~\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\leq}$6.6\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.
82	
83	\subsection{Position Disruption vs.\ Information Loss}
84	\label{sec:zeromask}
85	
86	$\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\% on Object despite removing only 10\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\% SR while hard pruning collapses to 9.0\%. The 89\,pp gap is entirely attributable to position disruption---$\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.
87	
88	\subsection{Scoring Method Sensitivity and CV Diagnostic}
89	\label{sec:cv_sensitivity}
90	
91	CV predicts where scoring method choice becomes critical (Figure~\ref{fig:method_gap}). $\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\,pp, exceeding X-VLA's maximum (1.4\,pp) by $17{\times}$. At $k{=}0.5$, $\Delta$(L2$-$R) on Object is $-$36.0\,pp ($\pi_{0.5}$), $-$27.2\,pp (X-VLA), confirming random preserves spatial diversity while L2 clusters correlated tokens.
92	
93	\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\geq}$92.8\% while L2 falls 8--27\,pp below random; on $\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\,pp). On Long, attention cliffs $-$26.5\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\ref{fig:cliff_highlight}).
94	
95	\textbf{Disruption peak.} Random pruning on $\pi_{0.5}$ is \emph{more} destructive at intermediate than aggressive ratios. On Long at $k{=}0.9$, the margin peaks at 46.9\,pp (L2 80.4\% vs.\ Random 33.6\%; Figure~\ref{fig:cliff_highlight}); at $k{=}0.5$ all methods converge within ${\sim}$2\,pp (Appendix Figure~\ref{fig:margin_profile}). The V-shaped random recovery arises from position aliasing under scattered removal (Section~\ref{sec:analysis}).
96	
97	\begin{figure}[t]
98	\centering
99	\includegraphics[width=0.75\linewidth]{figures/paper/fig_cliff_highlight.pdf}
100	\caption{Scoring method determines cliff behavior on $\pi_{0.5}$ Long (five-seed mean $\pm$ s.d.\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\,pp gap vs.\ L2) and recovery at $k{\leq}0.7$.}
101	\label{fig:cliff_highlight}
102	\end{figure}
103	
104	\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\pi_{0.5}$ at $k{=}0.85$: Object $+$93\,pp $>$ Goal $+$35.2\,pp $>$ Long $+$33.2\,pp, as multi-step tasks distribute critical information across heterogeneous norm profiles.
105	
106	\subsection{VTR Recovery}
107	\label{sec:vtr_recovery}
108	
109	VTR uses $M$ learned queries cross-attending over all 128 source tokens (${\sim}$22M parameters, ${\sim}$5\% of SmolVLA), recovering from 0.0\% to over 60\% SR at 75\% compression ($M{=}32$: 60.1 $\pm$ 1.3\%, 3 seeds; Table~\ref{tab:vtr_main}). A parameter-matched MLP adapter achieves 63.4 $\pm$ 2.6\% ($p{=}0.15$), confirming the gain stems from re-encoding, not cross-attention. Cross-suite: Spatial 53.2\%, Goal 56.4\%, both from 0.0\%.
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\%; VTR recovers ${\geq}$57\% at up to 87.5\% compression.}
115	\label{tab:vtr_main}
116	\begin{tabular}{lccr}
117	\toprule
118	Configuration & $M$ & Compress.\ & SR (\%) \\
119	\midrule
120	\textit{Baseline (unpruned)} & 128 & 0\% & 44.8 \\
121	\textit{Hard pruning (any)} & -- & 5--50\% & 0.0 \\
122	\midrule
123	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
124	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
125	MLP adapter & 32 & 75\% & 63.4 $\pm$ 2.6 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	\textbf{Efficiency.}\label{sec:efficiency} For $\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\sim}$16\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\% compression with ${\leq}$1.1\,pp below passthrough.
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "418671a1-278a-4144-9447-26861362490e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\nWe evaluate vision token pruning across six VLA architectures spanning three connector families on LIBERO~\\cite{liu2023libero}, which provides four task suites of increasing complexity: Object, Spatial, Goal, and Long (10 tasks $\\times$ 50 episodes each).\n\nFour models are evaluated in closed-loop control: $\\pi_{0.5}$~\\cite{black2025pi05} (4B, linear projection, 768 tokens, CV$\\,{=}\\,$0.055), X-VLA~\\cite{zheng2025xvla} (0.9B, linear + 12-layer BART encoder, 50 tokens, CV$\\,{=}\\,$0.151), OpenVLA~\\cite{kim2024openvla} (7B, 3-layer MLP, 256 tokens, CV$\\,{=}\\,$0.215), and SmolVLA~\\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\\times}4$, 128 tokens, CV$\\,{=}\\,$0.314). Two additional models ($\\pi_{0}$~\\cite{black2024pi0}, OFT~\\cite{kim2025openoft}) are analyzed via offline metrics only. Table~\\ref{tab:model_properties} summarizes all six architectures. We prune at $k \\in \\{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\\}$, reporting mean success rate (SR) over 500 episodes.\n\n\\subsection{Two-Axis Framework Overview}\n\\label{sec:two_axis}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_pruning_overview.pdf}\n\\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\\pi_{0.5}$ maintains ${\\geq}$98\\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\\% at $k{=}0.95$.}\n\\label{fig:pruning_overview}\n\\end{figure}\n\nThree qualitatively distinct response patterns emerge across the connector spectrum (Table~\\ref{tab:main_results}; Figure~\\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\\ref{tab:full_results}.\n\n\\textbf{$\\pi_{0.5}$ (linear, CV$\\,{=}\\,$0.055).} Low-CV models are \\emph{uniformly critical}: which tokens are removed matters more than how many. L2 maintains ${\\geq}$98.0\\% through $k{=}0.85$, while random at $k{=}0.9$ collapses to 9.0\\%---an 89\\,pp method gap from identical removal fractions.\n\n\\textbf{X-VLA (BART encoder, CV$\\,{=}\\,$0.151).} Method-insensitive but task-sensitive: at $k{=}0.9$ on Object, L2 and random differ by 0.4\\,pp, yet the same model drops 27.4\\,pp on Goal. Removing 3 of 50 tokens ($k{=}0.95$) halves Long SR regardless of method.\n\n\\textbf{OpenVLA (MLP, CV$\\,{=}\\,$0.215).} OpenVLA exhibits scoring crossover: L2 outperforms random on Object but the ranking inverts on Spatial and Goal at $k{=}0.9$ (Appendix Table~\\ref{tab:full_results}; Section~\\ref{sec:analysis}).\n\n\\textbf{SmolVLA (pixel-shuffle, CV$\\,{=}\\,$0.314).} Removing 6 of 128 tokens ($k{=}0.95$) collapses SR to ${\\leq}$6.6\\% across all suites and methods---a catastrophic cliff detailed below.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Closed-loop success rates (\\%) on LIBERO under L2 norm (L2) and random (R) token pruning. SmolVLA collapses to ${\\leq}$6.6\\% across all conditions. $\\pi_{0.5}$ Long: five-seed mean ($n{=}5$; per-seed in Appendix Table~\\ref{tab:pi05_long_multiseed}). Full results including OpenVLA in Appendix Table~\\ref{tab:full_results}.}\n\\label{tab:main_results}\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.5$ (L2 / R) \\\\\n\\midrule\n\\multirow{4}{*}{$\\pi_{0.5}$}\n& Object  & \\textbf{98.2} & 98.2 / 74.0 & \\textbf{98.2} / 9.0 & 33.4 / 69.4 \\\\\n& Spatial & \\textbf{97.2} & \\textbf{97.8} / 76.4 & 95.0 / 54.6 & 55.6 / 71.6 \\\\\n& Goal    & \\textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 59.2 / 73.6 \\\\\n& Long    & \\textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 51.7 / 50.4 \\\\\n\\midrule\n\\multirow{4}{*}{X-VLA}\n& Object  & \\textbf{99.2} & 99.0 / 98.8 & 97.6 / 97.8 & 43.4 / 70.6 \\\\\n& Spatial & \\textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 58.8 / 71.4 \\\\\n& Goal    & \\textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 59.0 / 67.2 \\\\\n& Long    & \\textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & 45.0 / 61.6 \\\\\n\\midrule\n\\multirow{4}{*}{SmolVLA}\n& Object  & \\textbf{59.2} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Spatial & \\textbf{44.6} & 6.6 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Goal    & \\textbf{60.8} & 3.4 / 4.2 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n& Long    & \\textbf{36.6} & 0.0 / 0.0 & 0.0 / 0.0 & 0.0 / 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Pixel-Shuffle Entanglement}\n\\label{sec:pixel_shuffle}\n\n\\begin{figure*}[t]\n\\centering\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_pixel_shuffle.pdf}\n\\caption{}\\label{fig:pixel_shuffle}\n\\end{subfigure}\n\\hfill\n\\begin{subfigure}[t]{0.495\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{figures/paper/fig_method_gap.pdf}\n\\caption{}\\label{fig:method_gap}\n\\end{subfigure}\n\\caption{Token entanglement and scoring sensitivity. \\textbf{(a)}~Pixel-shuffle $4{\\times}4$ folding: each 16-patch block is channel-concatenated into one token; removing any token eliminates a non-overlapping receptive field. \\textbf{(b)}~Method gap $|\\text{SR(L2)} - \\text{SR(Random)}|$ at $k{=}0.95$: $\\pi_{0.5}$'s Object gap (24.2\\,pp) exceeds X-VLA's maximum (1.4\\,pp) by $17{\\times}$ (single seed except $\\pi_{0.5}$ Long, $n{=}5$).}\n\\label{fig:entanglement_scoring}\n\\end{figure*}\n\nSmolVLA's pixel-shuffle $4{\\times}4$ folding concatenates 16 patches per token (Figure~\\ref{fig:pixel_shuffle}), creating non-overlapping receptive fields that collapse SR to ${\\leq}$6.6\\% at $k{=}0.95$ across all suites and methods (verified on two checkpoints). No scoring function can identify dispensable tokens because all carry spatially entangled information.\n\n\\subsection{Position Disruption vs.\\ Information Loss}\n\\label{sec:zeromask}\n\n$\\pi_{0.5}$'s random pruning at $k{=}0.9$ collapses to 9.0\\% on Object despite removing only 10\\% of tokens. We compare hard pruning (removes tokens, re-indexes positions) with zero-masking (zeros embeddings, preserves positions): zero-masking preserves 98.0\\% SR while hard pruning collapses to 9.0\\%. The 89\\,pp gap is entirely attributable to position disruption---$\\pi_{0.5}$'s linear connector tolerates complete signal destruction but not index shifts.\n\n\\subsection{Scoring Method Sensitivity and CV Diagnostic}\n\\label{sec:cv_sensitivity}\n\nCV predicts where scoring method choice becomes critical (Figure~\\ref{fig:method_gap}). $\\pi_{0.5}$'s Object gap at $k{=}0.95$ reaches 24.2\\,pp, exceeding X-VLA's maximum (1.4\\,pp) by $17{\\times}$. At $k{=}0.5$, $\\Delta$(L2$-$R) on Object is $-$36.0\\,pp ($\\pi_{0.5}$), $-$27.2\\,pp (X-VLA), confirming random preserves spatial diversity while L2 clusters correlated tokens.\n\n\\textbf{Architecture-dependent scoring.} The optimal scoring method depends on the connector (Table~\\ref{tab:attention_pruning}). On X-VLA at $k{=}0.5$, attention recovers ${\\geq}$92.8\\% while L2 falls 8--27\\,pp below random; on $\\pi_{0.5}$, attention is catastrophically harmful on Object ($-$30.4\\,pp). On Long, attention cliffs $-$26.5\\,pp from $k{=}0.95$ to $k{=}0.85$, then plateaus (Figure~\\ref{fig:cliff_highlight}).\n\n\\textbf{Disruption peak.} Random pruning on $\\pi_{0.5}$ is \\emph{more} destructive at intermediate than aggressive ratios. On Long at $k{=}0.9$, the margin peaks at 46.9\\,pp (L2 80.4\\% vs.\\ Random 33.6\\%; Figure~\\ref{fig:cliff_highlight}); at $k{=}0.5$ all methods converge within ${\\sim}$2\\,pp (Appendix Figure~\\ref{fig:margin_profile}). The V-shaped random recovery arises from position aliasing under scattered removal (Section~\\ref{sec:analysis}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\linewidth]{figures/paper/fig_cliff_highlight.pdf}\n\\caption{Scoring method determines cliff behavior on $\\pi_{0.5}$ Long (five-seed mean $\\pm$ s.d.\\ shaded; $n{=}5$). L2 degrades monotonically; attention exhibits a sharp cliff from $k{=}0.95$ to $k{=}0.85$ ($-$26.5\\,pp), then plateaus; random exhibits a V-shape with collapse at $k{=}0.9$ (46.9\\,pp gap vs.\\ L2) and recovery at $k{\\leq}0.7$.}\n\\label{fig:cliff_highlight}\n\\end{figure}\n\n\\textbf{Importance margin gradient.} L2's advantage shrinks with task complexity on $\\pi_{0.5}$ at $k{=}0.85$: Object $+$93\\,pp $>$ Goal $+$35.2\\,pp $>$ Long $+$33.2\\,pp, as multi-step tasks distribute critical information across heterogeneous norm profiles.\n\n\\subsection{VTR Recovery}\n\\label{sec:vtr_recovery}\n\nVTR uses $M$ learned queries cross-attending over all 128 source tokens (${\\sim}$22M parameters, ${\\sim}$5\\% of SmolVLA), recovering from 0.0\\% to over 60\\% SR at 75\\% compression ($M{=}32$: 60.1 $\\pm$ 1.3\\%, 3 seeds; Table~\\ref{tab:vtr_main}). A parameter-matched MLP adapter achieves 63.4 $\\pm$ 2.6\\% ($p{=}0.15$), confirming the gain stems from re-encoding, not cross-attention. Cross-suite: Spatial 53.2\\%, Goal 56.4\\%, both from 0.0\\%.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Hard pruning collapses all configurations to 0\\%; VTR recovers ${\\geq}$57\\% at up to 87.5\\% compression.}\n\\label{tab:vtr_main}\n\\begin{tabular}{lccr}\n\\toprule\nConfiguration & $M$ & Compress.\\ & SR (\\%) \\\\\n\\midrule\n\\textit{Baseline (unpruned)} & 128 & 0\\% & 44.8 \\\\\n\\textit{Hard pruning (any)} & -- & 5--50\\% & 0.0 \\\\\n\\midrule\nCross-attn VTR & 32 & 75\\% & 60.1 $\\pm$ 1.3 \\\\\nCross-attn VTR & 16 & 87.5\\% & 56.9 $\\pm$ 1.3 \\\\\nMLP adapter & 32 & 75\\% & 63.4 $\\pm$ 2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Efficiency.}\\label{sec:efficiency} For $\\pi_{0.5}$, $k{=}0.9$ cuts attention FLOPs by ${\\sim}$16\\% while preserving full SR; VTR at $M{=}16$ achieves 87.5\\% compression with ${\\leq}$1.1\\,pp below passthrough.\n",
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

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the full picture:

**Issue 1: "Section ??"**
- method.tex lines 57 and 72 reference `\ref{sec:linear_results}`
- `sec:linear_results` is defined in `results.tex:50` and `results_v2.tex:50`
- But main.tex includes `experiments.tex`, not `results.tex` or `results_v2.tex`
- experiments.tex does NOT have `sec:linear_results`
- So the reference is broken because the label doesn't exist in the compiled document


- The content these references point to—about L2 scoring's pathological behavior at low k and localizing transition boundaries—actually appears in experiments.tex under the Two-Axis Framework Overview section, so I need to update the references to point there instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "d578b1bb-3603-4f9a-9f69-edafbd30ece9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CL4epUuKv15s5HcQ42JKP4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 32801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4771
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_018Joc1YYds5RUaohPp4pSVS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex",
  "offset": 45,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "74454021-d365-4c00-8c9e-378863d6a7ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CL4epUuKv15s5HcQ42JKP4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4771,
      "cache_read_input_tokens": 32801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4771
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

_source line 24 · 2026-05-28T18:15:29.097Z_

<details><summary>↩ Tool result · `toolu_018Joc1YYds5RUaohPp4pSVS`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "4cc50334-0ceb-4d8c-af1d-cc9701a22383",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex",
      "content": "OFT~\\cite{kim2025openoft} retains OpenVLA's MLP connector but replaces the action head; its attention entropy (0.667) matches standard OpenVLA (0.661). The connector, not the action head, is associated with token importance structure. EfficientVLA~\\cite{yang2025efficientvla} corroborates the graded pattern from the literature: CogACT~\\cite{li2024cogact} (MLP projector) retains 74.2\\% SR under 78\\% pruning.\n\nTo control for scoring method in cross-architecture comparisons, we evaluate L2 norm-based selection on OpenVLA. At moderate-to-aggressive retention ($k \\leq 0.7$), L2 performs within 2--6\\,pp of random removal\\footnote{OpenVLA random results use seed$\\,{=}\\,$7; L2 norm results use seed$\\,{=}\\,$42. Same-seed (seed42) gaps: 5.4\\,pp at $k{=}0.7$, 3.6\\,pp at $k{=}0.3$ (21.4\\% random vs.\\ 25.0\\% L2); same-seed at $k{=}0.5$: 35.8\\% random vs.\\ 39.2\\% L2 (gap 3.4\\,pp).} (Table~\\ref{tab:openvla_l2_vs_random}, Appendix~\\ref{app:l2_vs_random}). At $k{=}0.9$, L2 outperforms random by 8.6\\,pp (70.6\\% vs.\\ 62.0\\%, reproducible across two random seeds), consistent with the weak but non-zero importance gradient predicted by CV$\\,{=}\\,$0.215: the signal is exploitable only when few tokens are removed.\n\n\\subsection{Linear Projection: From Uniformly Critical to Threshold-Graded}\n\\label{sec:linear_results}\n\nThree models share a linear projection connector yet exhibit qualitatively different pruning responses. The divergence traces to what happens \\emph{after} the projection: nothing ($\\pi_0$), a learned scaling ($\\pi_0.5$), or a full 12-layer encoder (X-VLA).\n\n\\paragraph{$\\pi_0$ (3.3B, 256 tokens, pure linear).} Offline normalized L1 action loss at $k{=}0.1$ is 0.976, a 2.4\\% \\emph{improvement} over the unpruned baseline.\\footnote{Offline action loss measures single-step prediction quality; closed-loop evaluation may reveal additional degradation.} CV$\\,{=}\\,$0.038 indicates near-uniform token norms. Near-uniform L2 norms (CV$\\,{=}\\,$0.038) suggest that no token subset carries disproportionate information, so random removal approximates uniform spatial downsampling and the model compensates.\n\n\\paragraph{$\\pi_0.5$ (4B, 768 tokens, linear $\\times\\!\\sqrt{d}$).} The baseline achieves 98.2\\% SR. This model reveals that low CV does not imply tokens are dispensable; it implies uniform criticality. The response is strongly method-dependent: random removal at $k{=}0.5$ retains 69.4\\% SR ($-$28.8\\,pp), while L2 norm-based removal at the same ratio collapses to 33.4\\% ($-$64.8\\,pp). The gap of 36\\,pp is the largest method-dependent effect at $k{=}0.5$ in our study.\n\nAt $k \\leq 0.7$, random removal degrades monotonically (77.2\\%, 69.4\\%, 36.4\\% at $k{=}0.7, 0.5, 0.3$; seed43 within 1\\,pp). At higher retention, a task-specific random cliff emerges on LIBERO-Object: SR drops from 69.4\\% ($k{=}0.95$) to 5.0\\% ($k{=}0.85$) before recovering to 77.2\\% ($k{=}0.7$), a 72\\,pp swing; the same $k{=}0.85$ on LIBERO-Spatial retains 58.4\\% (Appendix~\\ref{app:pi05_crosssuite}). L2 norm selection produces a V-shaped curve: 55.0\\% at $k{=}0.7$, 33.4\\% at $k{=}0.5$ (the valley), 51.0\\% at $k{=}0.3$, confirmed across two seeds ($\\sigma = 0.1$\\,pp at the valley).\\footnote{V-shape valley at $k{=}0.5$: 33.4\\% (seed42) vs.\\ 33.6\\% (seed43), $\\sigma{=}0.1$\\,pp. V-depth: 17.6\\,pp (seed42), 21.8\\,pp (seed43). Full multi-seed table in Appendix~\\ref{app:pi05_multiseed}.} The non-monotonic L2 pattern arises because norm ranking in a low-CV distribution selects spatially clustered tokens (slight norm variations correlate with image regions), and the resulting loss of spatial coverage peaks at intermediate budgets.\n\nThis result demonstrates that models showing offline pruning tolerance can exhibit severe closed-loop degradation. Low-CV tokens are uniformly critical, not uniformly dispensable. L2 norm-based selection systematically concentrates on spatially correlated tokens and loses coverage; random selection preserves the uniform spatial distribution that these architectures require.\n\n\\paragraph{X-VLA (880M, 50 tokens, linear + 12-layer BART).} The 99.2\\% baseline is maintained at $k{=}0.95$ ($99.1 \\pm 0.2$\\%, 3 seeds) and $k{=}0.9$ ($97.8 \\pm 0.4$\\%) under L2 norm-based removal. A sharp cliff appears at $k{=}0.85$ ($67.9 \\pm 0.3$\\%, $-$31\\,pp, 3 seeds), with non-monotonic recovery at $k{=}0.80$ ($89.0 \\pm 0.7$\\%, 3 seeds) before degradation resumes: $58.6 \\pm 0.4$\\% at $k{=}0.7$, $43.4 \\pm 0.8$\\% at $k{=}0.5$, $22.0 \\pm 0.9$\\% at $k{=}0.3$, $4.7 \\pm 0.6$\\% at $k{=}0.2$, and near-zero at $k{=}0.1$. The cliff at $k{=}0.85$ (retaining 42 of 50 BART-encoded tokens) is reproducible across seeds (std $\\leq$ 1.6\\,pp). The non-monotonic dip is task-specific: four tasks lose $\\sim$50\\,pp each while six remain unaffected (Table~\\ref{tab:xvla_cliff_pertask}, Appendix~\\ref{app:xvla_cliff}). Under random removal, X-VLA exhibits a plateau: $65.1 \\pm 0.1$\\% at $k{=}0.7$ and $64.0 \\pm 1.6$\\% at $k{=}0.3$ (3 seeds each), confirming that L2 norm-based selection ($22.0 \\pm 0.9$\\% at $k{=}0.3$) is far more destructive than random for this intermediate-CV architecture.\n\nThat this threshold appears under importance-based removal (the more favorable test) while OpenVLA degrades smoothly under random removal (the harder test) strengthens the architecture-dependent conclusion. The $\\pi_0$--OpenVLA comparison (both consuming 256 SigLIP-based tokens, differing in connector, backbone, and encoder fusion) produces a 63\\,pp gap at $k{=}0.1$, consistent with the connector-associated pattern observed across all seven models. This comparison involves differences in connector, backbone, and encoder fusion, limiting causal interpretation.\n\n\\subsection{VTR: Re-Encoding Overcomes Cliff-Edge}\n\\label{sec:smart_compress_results}\n\nTo test whether learned re-encoding can overcome the pixel-shuffle cliff-edge, we insert a 22.2M-parameter cross-attention module (Vision Token Re-encoder, VTR) between the vision connector and the LLM backbone (details in Appendix~\\ref{app:smart_compress_details}). VTR compresses 128 input tokens to $M$ output tokens. Both VTR and the baseline train from the same SmolVLA-Base checkpoint for 100K steps with identical hyperparameters. An extended training control (same procedure without the compressor) achieves 45.0\\% SR ($p > 0.9$ vs.\\ the 44.8\\% baseline); the gain is architectural, not from additional optimization steps.\\footnote{The extended baseline also collapses to 0\\% SR under pruning ($k{=}0.50$, random, true removal). Additional training does not mitigate the pixel-shuffle vulnerability.}",
      "numLines": 25,
      "startLine": 45,
      "totalLines": 125
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
Now I understand the full picture for Issue 1:

The `sec:linear_results` label exists in results.tex (line 50), which labels the subsection "Linear Projection: From Uniformly Critical to Threshold-Graded". But main.tex includes `experiments.tex`, not `results.tex`. The experiments.tex file has restructured content and doesn't have this specific subsection.

Looking at the two references in method.tex:

1. **Line 57**: "This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\ref{sec:linear_results})." - This is about π0.5's behavior. 

2. **Line 72**: "we add finer-grained ratios ($k \in \{0.80, 0.925\}$) to localize the transition boundary (Section~\ref{sec:linear_results})." - This is about X-VLA's cliff behavior.

Both references point to linear-projection results that are now scattered across experiments.tex—the π0.5 behavior and X-VLA's transition dynamics are covered in `sec:two_axis`, while the sensitivity analysis appears in `sec:cv_sensitivity`.

For line 57 about L2 spatial bias at low k, `sec:cv_sensitivity` is the right fit since it discusses how the scoring method affects spatial diversity. For line 72 about the finer-grained ratios, the cliff behavior is mentioned in `sec:two_axis` for X-VLA, but those specific k values don't appear to be documented in the current experiments.tex—I need to check if this detail was omitted or if it belongs in a different section. Looking at the full sentence about X-VLA's cliff and the finer-grained ratios, this is describing how we add k values of 0.80 and 0.925 to pinpoint where the transition happens. The reference should point to where those detailed ratio results actually appear in the document, which is in the two-axis framework section where the cliff behavior is discussed. So line 72 should reference `sec:two_axis` instead of `sec:linear_results`.

For the L2 scoring bias issue, I'm seeing that the spatial clustering problem becomes severe at low retention ratios, especially for models with uniform norm distributions. The experiments section on coefficient of variation sensitivity has the concrete numbers showing L2 performs much worse than random at k=0.5, confirming that random selection better preserves spatial diversity. So line 57 should point to `sec:cv_sensitivity` where this empirical evidence is presented, not `sec:linear_results`.

For line 72, I'm reconsidering which section best supports the claim about finer-grained ratios for cliff localization. The two-axis section does show cliff behavior for X-VLA, which is the targeted model being referenced, so `sec:two_axis` seems like the right reference even though the specific ratio details aren't exhaustively laid out there.

Now I need to address the Equation 4 issue.  The CV spectrum equation is a single long line with multiple underbraces showing different model architectures and their corresponding values. In a two-column conference format, this will definitely overflow the page width, so I need to split it into multiple lines while preserving the comparison structure and readability.

I'll use a `split` environment to break the equation at a natural point — after X-VLA — and align the inequality signs properly so the chain of comparisons remains clear across both lines. Writing LaTeX equation... Checking the column width constraints for the two-line format in a two-column paper layout. The second line with the MLP projector and pixel-shuffle comparisons fits comfortably, and the first line grouping the linear projector and linear + BART also stays within bounds. Both lines work well, so I'll proceed with writing the edit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "d5a57b4b-482a-4676-aa13-3ba3c149d93b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189FtFWCm569oVsiqawFh5d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 37572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

Found both issues. Here's the situation:

**Issue 1**: method.tex references `\ref{sec:linear_results}` (lines 57 and 72), but main.tex includes `experiments.tex`, not `results.tex`. The label `sec:linear_results` exists only in the unused `results.tex`. Need to remap to labels in experiments.tex.

**Issue 2**: Equation 4 (the CV spectrum, lines 86-89) has a very long single-line chain of underbraces that overflows column width.

Fixing both now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "2cb79c74-d230-4d96-a1f2-fa08f777e511",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189FtFWCm569oVsiqawFh5d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 37572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

<details open><summary>🔧 Tool call — Edit · `toolu_01LpC2WtosVQipyyB2qvksCv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).",
  "new_string": "This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "3edaeffb-89d4-41c8-bdae-05c3332acf6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189FtFWCm569oVsiqawFh5d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 37572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

_source line 28 · 2026-05-28T18:16:24.407Z_

<details><summary>↩ Tool result · `toolu_01LpC2WtosVQipyyB2qvksCv`</summary>

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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "4c56ee6c-7f98-4c48-948d-29128ae2af5b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).",
    "newString": "This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 54,
        "oldLines": 7,
        "newStart": 54,
        "newLines": 7,
        "lines": [
          " s_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.",
          " \\label{eq:l2_score}",
          " \\end{equation}",
          "-The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:linear_results}).",
          "+The L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).",
          " ",
          " \\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:",
          " \\begin{equation}"
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_018oidhD2H7nZ2GPW8nicwkF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "to localize the transition boundary (Section~\\ref{sec:linear_results}).",
  "new_string": "to localize the transition boundary (Section~\\ref{sec:two_axis})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "3e33954a-6a73-4c45-ba82-0f79e7b7d38f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRngDxVUHF2sFcoTwz8uVV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3256,
      "cache_read_input_tokens": 40508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3256
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

_source line 30 · 2026-05-28T18:16:28.835Z_

<details><summary>↩ Tool result · `toolu_018oidhD2H7nZ2GPW8nicwkF`</summary>

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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "38e42d69-0bb1-4f62-85fd-0b59f1e5cafa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "to localize the transition boundary (Section~\\ref{sec:linear_results}).",
    "newString": "to localize the transition boundary (Section~\\ref{sec:two_axis}).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 69,
        "oldLines": 7,
        "newStart": 69,
        "newLines": 7,
        "lines": [
          " Attention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.",
          " ",
          " \\paragraph{Retention ratio design space.}",
          "-We evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:linear_results}).",
          "+We evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).",
          " ",
          " \\subsection{Compressibility Diagnostic: Importance CV}",
          " \\label{sec:cv_diagnostic}"
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01U99Xujhe8YpsafYqqYFwEm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
  "old_string": "\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}",
  "new_string": "\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "fa390ba3-a358-433b-9cbc-fd6c92b0637e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zshMcYe9jnBWAybcyg8Sr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 241,
      "cache_read_input_tokens": 43764,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 241
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

_source line 32 · 2026-05-28T18:16:35.932Z_

<details><summary>↩ Tool result · `toolu_01U99Xujhe8YpsafYqqYFwEm`</summary>

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
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "8c160ba4-c79b-4c71-aa19-dd74a3f32b28",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex",
    "oldString": "\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}",
    "newString": "\\begin{equation}\n\\begin{split}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\\n&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\end{split}\n\\label{eq:cv_spectrum}\n\\end{equation}",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Models and Connectors}\n\\label{sec:models}\n\nWe evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\\ref{tab:model_properties}; Figure~\\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies.\n\n\\textbf{Linear projection} applies a single matrix multiplication per patch. $\\pi_{0}$~\\cite{black2024pi0} projects 256 patches through a linear layer; $\\pi_{0.5}$~\\cite{black2025pi05} uses a $\\times\\!\\sqrt{d}$-scaled linear projection across 768 tokens from three image slots (two active cameras in LIBERO; CV$\\,{<}\\,$0.06).\n\n\\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\\,{=}\\,$0.215); OFT~\\cite{kim2025openoft} shares the same connector (512 tokens; CV$\\,{=}\\,$0.219).\n\n\\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\\cite{zheng2025xvla} feeds tokens through a 12-layer BART encoder~\\cite{lewis2020bart} (50 tokens). SmolVLA~\\cite{shukor2025smolvla} applies pixel-shuffle $4{\\times}4$ folding, concatenating 16 contiguous patches per output token (128 tokens).\n\nWe classify coupling as \\emph{independent} when each output token depends on a single input patch, and \\emph{entangling} when output tokens encode information from multiple patches. Four models are evaluated in closed-loop control on LIBERO~\\cite{liu2023libero}; $\\pi_{0}$ and OFT contribute to the CV diagnostic only.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig_architecture_v4.pdf}\n\\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Token-independent connectors ($\\pi_{0.5}$: linear; OpenVLA: MLP) yield low CV. Token-entangling connectors (X-VLA: BART encoder; SmolVLA: pixel-shuffle) create cross-token dependencies and higher CV, predicting threshold-graded or catastrophic pruning failure.}\n\\label{fig:architecture}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{VLA models evaluated. Coupling indicates independent vs.\\ cross-token processing. $N$ = vision tokens input to the LLM. $^\\dagger$OFT is an OpenVLA fine-tuning variant, included for CV calibration (offline metrics only).}\n\\label{tab:model_properties}\n\\begin{tabular}{lrlcrll}\n\\toprule\nModel & Params & Connector & $N$ & CV & Coupling & Eval \\\\\n\\midrule\n$\\pi_{0.5}$ & 4B & Linear ($\\times\\!\\sqrt{d}$) & 768 & 0.055 & Indep.\\ & Closed-loop \\\\\nX-VLA & 0.9B & Linear + BART & 50 & 0.151 & Entangling & Closed-loop \\\\\nOpenVLA & 7B & 3-layer MLP & 256 & 0.215 & Indep.\\ & Closed-loop \\\\\nSmolVLA & 450M & Pixel-shuffle $4{\\times}4$ & 128 & 0.314 & Entangling & Closed-loop \\\\\n\\midrule\n$\\pi_{0}$ & 3.3B & Linear & 256 & 0.038 & Indep.\\ & Offline \\\\\nOFT$^\\dagger$ & 7B & 3-layer MLP & 512 & 0.219 & Indep.\\ & Offline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Pruning Protocol}\n\\label{sec:pruning_protocol}\n\nGiven $N$ post-connector vision tokens $\\{t_1, \\ldots, t_N\\}$ with $t_i \\in \\mathbb{R}^d$, token pruning selects a subset of size $\\lfloor k \\cdot N \\rfloor$ for retention ratio $k \\in (0, 1]$ and discards the rest. Unselected tokens are physically removed and position IDs are re-indexed to close gaps. We prune between the vision connector output and the LLM backbone input to isolate the connector's effect on token information structure: pruning before the connector would alter its input distribution, confounding architectural analysis with input perturbation.\n\n\\paragraph{Importance scoring functions.}\nA scoring function $s\\colon \\mathbb{R}^d \\to \\mathbb{R}$ assigns each token an importance score; the top-$\\lfloor kN \\rfloor$ tokens by score are retained. We evaluate two strategies that bracket expected performance.\n\n\\textbf{L2-norm scoring} assigns each token its activation magnitude:\n\\begin{equation}\ns_{\\text{L2}}(t_i) = \\|t_i\\|_2\\,.\n\\label{eq:l2_score}\n\\end{equation}\nThe L2 norm serves as a proxy for information density: tokens with larger norms carry stronger activations that exert greater influence on downstream attention computation. This proxy is architecture-agnostic and requires no access to the LLM backbone. L2 scoring introduces a spatial bias, however, because nearby patches share visual content and produce correlated norms. Under aggressive pruning, L2 selection can concentrate retained tokens in a single high-activation region at the cost of spatial coverage. This bias is benign at high retention ratios but becomes pathological at low $k$ for models with near-uniform norm distributions (Section~\\ref{sec:cv_sensitivity}).\n\n\\textbf{Random subsampling} draws $\\lfloor kN \\rfloor$ tokens uniformly at random:\n\\begin{equation}\ns_{\\text{rand}}(t_i) \\sim \\mathcal{U}(0, 1)\\,.\n\\label{eq:random_score}\n\\end{equation}\nRandom selection provides the null hypothesis that all post-connector tokens are interchangeable. If L2 scoring cannot outperform random, the token norm distribution carries no exploitable signal. Random selection also preserves the spatial distribution of the original token set in expectation, making it the natural baseline for spatially uniform architectures. Its primary limitation is sampling variance across episodes, which we control through multi-seed evaluation (Section~\\ref{sec:openvla_results}).\n\nThe \\emph{importance margin} at ratio $k$ is defined as $\\Delta(k) = \\text{SR}_{\\text{L2}}(k) - \\text{SR}_{\\text{Random}}(k)$. A positive margin indicates that the norm distribution contains exploitable importance structure. A negative margin indicates that L2 selection is actively harmful, typically because spatial clustering outweighs the benefit of importance ranking. The sign and magnitude of the importance margin vary systematically with both connector CV and $k$ (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Attention-based alternatives.}\nAttention-based scoring functions estimate token importance from the LLM's internal attention weights. Three principal variants exist: (i)~\\emph{column-sum scoring} sums each vision token's received attention weight in the last transformer layer, capturing direct query-key dependencies at the final processing stage; (ii)~\\emph{cross-layer mean scoring} averages column-sum scores across all layers, aggregating importance signals over the full transformer stack; (iii)~\\emph{attention rollout} multiplies attention matrices layer by layer (adding identity matrices for residual connections) to approximate cumulative information flow from input tokens to the output. These methods rest on the premise that tokens receiving more attention contribute more to the model's prediction. Their primary limitation is computational: they require a full LLM forward pass and are backbone-specific. We focus on L2-norm and random scoring because they operate solely on the connector output, are backbone-agnostic, and suffice to reveal the connector-dependent importance structure that is our primary object of study. Attention entropy enters our analysis as a diagnostic metric (Section~\\ref{sec:cv_diagnostic}), not as a pruning criterion.\n\n\\paragraph{Retention ratio design space.}\nWe evaluate $k \\in \\{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95\\}$, spanning from extreme compression (retaining 30\\% of tokens) to conservative trimming (retaining 95\\%). This range captures the full degradation profile of each connector type. At one end, $k = 0.95$ tests whether even minimal removal is tolerable (e.g., 6 of 128 tokens for SmolVLA). At the other, $k = 0.30$ probes behavior under severe information loss (e.g., 15 of 50 tokens for X-VLA). The intermediate values are chosen to identify \\emph{cliff zones}: narrow $k$ intervals where success rate drops discontinuously rather than degrading proportionally. A cliff zone indicates a critical token density below which the model's visual representation breaks down. Different connector architectures exhibit cliffs at qualitatively different retention ratios: pixel-shuffle connectors cliff at $k = 0.95$ (the most conservative ratio tested), BART-encoded connectors near $k \\approx 0.85$, and MLP connectors degrade without a sharp cliff at any tested ratio. For targeted models where initial results indicate a cliff, we add finer-grained ratios ($k \\in \\{0.80, 0.925\\}$) to localize the transition boundary (Section~\\ref{sec:two_axis}).\n\n\\subsection{Compressibility Diagnostic: Importance CV}\n\\label{sec:cv_diagnostic}\n\nWe seek a zero-cost diagnostic that predicts a model's pruning tolerance without running closed-loop evaluation. The coefficient of variation (CV) of post-connector token L2 norms provides this:\n\\begin{equation}\n\\text{CV} = \\frac{\\sigma\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}{\\mu\\!\\left(\\{\\|t_i\\|_2\\}_{i=1}^{N}\\right)}\n\\label{eq:cv}\n\\end{equation}\nwhere $\\sigma$ and $\\mu$ denote the standard deviation and mean over all $N$ post-connector tokens from a single forward pass. CV requires no labeled data, no downstream task evaluation, and no access to the LLM backbone.\n\n\\paragraph{The CV spectrum.}\nCV captures a continuous ordering across six models and three connector families:\n\\begin{equation}\n\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}\n\\label{eq:cv_spectrum}\n\\end{equation}\nThis ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151.\n\n\\paragraph{CV as pruning tolerance predictor.}\nCV measures the dispersion of token importance under the L2-norm proxy. High CV indicates that some tokens carry substantially larger norms than others; these high-norm tokens can be identified and retained while low-norm tokens are removed with limited information loss. Low CV indicates near-uniform norms: no token subset is dispensable because all tokens contribute comparably. Pruning a low-CV model is equivalent to downsampling a uniform signal, where the spatial pattern of removal matters more than which specific tokens are selected by importance.\n\nCV also predicts the \\emph{optimal pruning strategy}, not only the tolerance ceiling. When CV is low ($< 0.15$), L2-norm ranking captures spatial artifacts rather than genuine importance differences, and random selection outperforms L2 by preserving spatial coverage. When CV is high ($> 0.20$), L2-norm ranking exploits real importance differentiation and outperforms random. The importance margin $\\Delta(\\text{L2} - \\text{Random})$ increases monotonically with CV at both $k = 0.5$ and $k = 0.7$ across three closed-loop models ($\\pi_{0.5}$, X-VLA, OpenVLA), confirming that CV captures a structural property of the connector rather than an artifact of a particular retention ratio (Section~\\ref{sec:scaling_law}).\n\n\\paragraph{Complementary role of attention entropy.}\nAttention entropy, defined as the mean Shannon entropy of the LLM's attention weight distribution over vision tokens, provides a complementary but less discriminative signal. Entropy measures how uniformly the LLM attends across vision tokens: high entropy indicates distributed attention, low entropy indicates selective focus. Three models with qualitatively different pruning behaviors, however, cluster within a narrow entropy band: $\\pi_{0.5}$ (0.666), X-VLA (0.614), and OpenVLA (0.661) span only 0.05 in entropy despite spanning 0.055 to 0.215 in CV and exhibiting uniformly critical, threshold-graded, and smooth graded pruning responses respectively. SmolVLA's entropy (0.952) is near-maximal, yet it is the least pruning-tolerant model. The discrepancy arises because entropy reflects the LLM's \\emph{reading pattern} (how attention is distributed across tokens), while CV reflects the connector's \\emph{writing pattern} (how information is distributed into tokens). The connector's output structure, not the downstream attention allocation, determines pruning robustness. We report entropy values alongside CV in our taxonomy (Table~\\ref{tab:taxonomy}) as a mechanistic supplement, but use CV as the primary diagnostic throughout.\n\n\\subsection{Vision Token Re-encoder (VTR)}\n\\label{sec:vtr}\n\nHard pruning fails for token-entangling connectors because removing any token destroys spatially distributed information. VTR addresses this through learned re-encoding rather than deletion.\n\n\\paragraph{Architecture.}\nVTR inserts a 2-layer cross-attention module between the vision connector output and the LLM backbone input. Each layer uses 12 attention heads with dropout 0.1. A set of $M$ learned query vectors attends over all $N$ source tokens via standard multi-head cross-attention, producing $M$ compressed tokens as input to the LLM. The compression ratio is controlled by $M \\in \\{16, 32, 64, 96, 128\\}$; $M{=}N$ serves as a passthrough control.\n\n\\paragraph{Training and cost.}\nThe module adds ${\\sim}$22M trainable parameters ($<$5\\% of SmolVLA, the smallest VLA tested) and is trained end-to-end: compressor and action head parameters are jointly optimized. Architecture and training hyperparameters are detailed in Appendix~\\ref{app:smart_compress_details}.\n",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 10,
        "lines": [
          " \\paragraph{The CV spectrum.}",
          " CV captures a continuous ordering across six models and three connector families:",
          " \\begin{equation}",
          "-\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} \\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}",
          "+\\begin{split}",
          "+\\underbrace{\\pi_0\\,(0.038) \\;<\\; \\pi_{0.5}\\,(0.055)}_{\\text{linear proj.}} &\\;<\\; \\underbrace{\\text{X-VLA}\\,(0.151)}_{\\text{linear + BART}} \\\\",
          "+&\\;<\\; \\underbrace{\\text{OpenVLA}\\,(0.215) \\;\\approx\\; \\text{OFT}\\,(0.219)}_{\\text{MLP proj.}} \\;<\\; \\underbrace{\\text{SmolVLA}\\,(0.314)}_{\\text{pixel-shuffle}}",
          "+\\end{split}",
          " \\label{eq:cv_spectrum}",
          " \\end{equation}",
          " This ordering reflects the degree of cross-token mixing in each connector. Pure linear projections process patches independently, producing near-uniform norms (CV$\\,{<}\\,$0.06). MLP projectors apply nonlinear transformations per token, amplifying norm variance through activation functions and layered composition (CV$\\,{\\approx}\\,$0.22). Pixel-shuffle folds $4 \\times 4$ patch blocks into single tokens by channel concatenation, creating maximal cross-patch entanglement and the highest norm heterogeneity (CV$\\,{=}\\,$0.314). X-VLA occupies an intermediate position: its linear projection is followed by a 12-layer BART encoder~\\cite{lewis2020bart} that introduces cross-token attention, raising CV from what a pure linear projection would produce (${\\sim}$0.04) to 0.151."
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

_source line 33_

两处修复完成：

1. **Section ??**: method.tex 中两处 `\ref{sec:linear_results}` 指向了未被 main.tex 引入的 results.tex。已改为 experiments.tex 中对应的 label：
   - 第 57 行 → `sec:cv_sensitivity`（讨论 L2 空间聚集 vs random 的 scoring 差异）
   - 第 72 行 → `sec:two_axis`（报告 cliff 行为和精细化 k 值结果）

2. **公式 4 溢出**: CV spectrum 链式不等式用 `split` 环境拆为两行，在 X-VLA 后断行，`<` 符号对齐。公式编号 (4) 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "uuid": "cd15ab57-ed19-4fcc-829f-22d2708469b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgqBT5s4JWu53kgtV8gbvW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 44005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 552
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

_source line 34_

两处修复完成：

1. **Section ??**: method.tex 中两处 `\ref{sec:linear_results}` 指向了未被 main.tex 引入的 results.tex。已改为 experiments.tex 中对应的 label：
   - 第 57 行 → `sec:cv_sensitivity`（讨论 L2 空间聚集 vs random 的 scoring 差异）
   - 第 72 行 → `sec:two_axis`（报告 cliff 行为和精细化 k 值结果）

2. **公式 4 溢出**: CV spectrum 链式不等式用 `split` 环境拆为两行，在 X-VLA 后断行，`<` 符号对齐。公式编号 (4) 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 131617,
  "duration_api_ms": 132937,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "82625594-dd42-425b-9dc7-58b7603d14ec",
  "total_cost_usd": 0.5224825000000001,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 32712,
    "cache_read_input_tokens": 295851,
    "output_tokens": 6706,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32712,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 218,
        "cache_read_input_tokens": 44005,
        "cache_creation_input_tokens": 552,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 552
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2317,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002402,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 6706,
      "cacheReadInputTokens": 295851,
      "cacheCreationInputTokens": 32712,
      "webSearchRequests": 0,
      "costUSD": 0.5200805000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "58de51fb-323f-4194-bddf-d3c55442f942"
}
```

</details>

---
