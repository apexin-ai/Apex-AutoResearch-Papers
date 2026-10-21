# paper writing introduction

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260515T050718.log`
- **Structured JSON:** [`b087816f6d0c40039fe4.json`](../../sessions/b0/b087816f6d0c40039fe4.json)

## Before a recorded user message

29 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
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
  "uuid": "f1f5864a-ff59-4b64-a354-d38af408939c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1778838000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7da9e5a2-7e14-4ab9-8b33-6f0c01101fae",
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec"
}
```

---

### Assistant

_source line 4_

Let me read the reference files to understand the technical details, positioning, and available citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "5d7d25b4-24b4-46e4-86c0-d0814c60d703",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ChAi8VmRHdmTwwGZLqREz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11640
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

<details open><summary>🔧 Tool call — Read · `toolu_0145cqp4S1NNYRGvrQsRcAJT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "bed88458-a341-439b-9ac8-25a68941c242",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ChAi8VmRHdmTwwGZLqREz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11640
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

_source line 6 · 2026-05-15T05:07:32.534Z_

<details><summary>↩ Tool result · `toolu_0145cqp4S1NNYRGvrQsRcAJT`</summary>

```text
1	\section{Method: Recovery-Aware Structured Pruning}
2	\label{sec:method}
3	
4	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.
5	The core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\citep{rlsqueezes2026}.
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	
14	\paragraph{Grouped Query Attention (GQA).}
15	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.
16	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.
17	We treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.
18	
19	\paragraph{RLVR and GRPO.}
20	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
21	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm, following~\citet{selfhealing2025}.
22	
23	\subsection{Stage 1: Reasoning-Trace Structural Analysis}
24	\label{sec:stage1}
25	
26	\rasp{} computes two complementary scores per structure: \emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.
27	
28	\paragraph{Calibration data.}
29	We compute importance and overlap scores on chain-of-thought reasoning data from GSM8K~\citep{cobbe2021gsm8k} training examples, using question--answer pairs as calibration traces.
30	Given a calibration set $\mathcal{D}_\text{cal} = \{(x_j, y_j)\}_{j=1}^{M}$, we compute activations and gradients on the concatenated sequences $(x_j, y_j)$.
31	This ensures importance scores reflect the model's behavior on representative reasoning tasks.
32	
33	\paragraph{Structural importance.}
34	For each structure $h$, we compute importance $I(h)$ via first-order Taylor expansion on the reasoning trace loss:
35	\begin{equation}
36	    I(h) = \left| \sum_{(x,y) \in \mathcal{D}_\text{cal}} \mathbf{a}_h(x, y)^\top \frac{\partial \mathcal{L}(x, y)}{\partial \mathbf{a}_h} \right|,
37	    \label{eq:importance}
38	\end{equation}
39	where $\mathbf{a}_h$ denotes the activation of structure $h$ and $\mathcal{L}$ is the language modeling loss over the reasoning trace.
40	For a GQA group $g$ containing Q heads $\{q_1, \ldots, q_G\}$ and KV head $k$, we aggregate: $I(g) = \sum_{i=1}^{G} I(q_i) + I(k)$.
41	
42	\paragraph{Functional overlap via CKA.}
43	We measure functional overlap using linear Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.
44	Given activation matrices $\mathbf{X}, \mathbf{Y} \in \mathbb{R}^{n \times d}$ collected over $n$ calibration examples, linear CKA is:
45	\begin{equation}
46	    \text{CKA}(\mathbf{X}, \mathbf{Y}) = \frac{\text{HSIC}(\mathbf{X}, \mathbf{Y})}{\sqrt{\text{HSIC}(\mathbf{X}, \mathbf{X}) \cdot \text{HSIC}(\mathbf{Y}, \mathbf{Y})}},
47	    \label{eq:cka}
48	\end{equation}
49	where $\text{HSIC}(\mathbf{X}, \mathbf{Y}) = \frac{1}{(n-1)^2} \operatorname{tr}(\mathbf{K} \mathbf{H} \mathbf{L} \mathbf{H})$, with $\mathbf{K} = \mathbf{X}\mathbf{X}^\top$, $\mathbf{L} = \mathbf{Y}\mathbf{Y}^\top$, and $\mathbf{H} = \mathbf{I}_n - \frac{1}{n}\mathbf{1}\mathbf{1}^\top$.
50	
51	For a GQA group $g_i$ in layer $\ell$, we form its representation by concatenating its constituent Q head activations: $\mathbf{X}_{g_i} = [\mathbf{a}_{q_1}; \ldots; \mathbf{a}_{q_G}] \in \mathbb{R}^{n \times Gd_h}$.
52	The functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:
53	\begin{equation}
54	    F(g_i) = \frac{1}{|\mathcal{G}_\ell| - 1} \sum_{\substack{g_j \in \mathcal{G}_\ell \\ j \neq i}} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j}),
55	    \label{eq:overlap}
56	\end{equation}
57	where $\mathcal{G}_\ell$ is the set of GQA groups in layer $\ell$.
58	Unlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.
59	
60	\paragraph{MLP channel group overlap.}
61	We apply the same intra-layer CKA overlap to MLP channel groups.
62	Each MLP intermediate dimension is partitioned into equal-sized groups; for group $m_i$ in layer $\ell$, we compute $F(m_i) = \frac{1}{|\mathcal{M}_\ell| - 1} \sum_{m_j \in \mathcal{M}_\ell, j \neq i} \text{CKA}(\mathbf{X}_{m_i}, \mathbf{X}_{m_j})$, where $\mathcal{M}_\ell$ is the set of MLP groups in layer $\ell$.
63	Attention GQA groups and MLP channel groups are then scored and ranked jointly in Stage~2.
64	
65	\subsection{Stage 2: Recovery-Aware Scoring}
66	\label{sec:stage2}
67	
68	The recovery-aware score combines importance and functional overlap:
69	\begin{equation}
70	    S(h) = I(h) \times \big(1 - F(h)\big)^\alpha,
71	    \label{eq:score}
72	\end{equation}
73	where $\alpha \ge 0$ controls the strength of the recoverability penalty ($\alpha{=}0$ reduces to standard importance-only pruning).
74	Structures with the lowest $S(h)$ are pruned up to the target sparsity ratio.
75	
76	The scoring captures three regimes:
77	\begin{itemize}[nosep,leftmargin=*]
78	    \item \textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\rightarrow$ \emph{protected}.
79	    \item \textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\rightarrow$ \emph{pruned preferentially}.
80	    \item \textbf{Low $I$} (unimportant): Pruned regardless of overlap.
81	\end{itemize}
82	
83	The key distinction from standard pruning---which ranks solely by $I(h)$---is that \rasp{} additionally down-weights protection of structures whose function overlaps with retained structures.
84	This is motivated by the finding that RLVR recovers through global exploration and path compression~\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.
85	
86	\paragraph{Per-layer capacity floor.}
87	Global ranking by $S(h)$ can concentrate pruning in layers where many structures have high overlap, collapsing that layer's representational capacity.
88	To prevent this, we enforce a per-layer capacity floor: each layer must retain at least 40\% of its MLP channel groups after pruning.
89	For DeepSeek-R1-Distill-Qwen-7B, this requires ${\ge}12$ of 28 MLP groups per layer.
90	During structure selection, if removing a candidate would violate this constraint, it is skipped in favor of the next lowest-scoring structure.
91	This constraint adds negligible overhead to the scoring procedure but prevents representational collapse in individual layers---a failure mode we observed when unconstrained global ranking was applied at 20\% sparsity.
92	
93	Attention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions subject to the per-layer floor.
94	Algorithm~\ref{alg:rasp} summarizes the complete pipeline.
95	
96	\subsection{Stage 3: Two-Stage Recovery}
97	\label{sec:stage3}
98	
99	After pruning, we recover reasoning ability through two stages: supervised finetuning (SFT) warmup followed by GRPO-based RLVR.
100	
101	\paragraph{Motivation for two-stage recovery.}
102	Directly applying GRPO to a pruned model fails.
103	Structured pruning disrupts the model's ability to generate end-of-sequence (EOS) tokens: in sampling mode, pruned models produce repetitive digit loops without termination, yielding sequences that are truncated at the maximum length.
104	Since GRPO computes rewards only from completed generations, this EOS collapse means no valid completions are produced, the clipped ratio reaches 1.0, and gradient norms drop to zero---making direct RLVR recovery impossible.
105	
106	\paragraph{Stage 3a: SFT warmup.}
107	We first apply a short SFT phase on reasoning demonstrations to restore two capabilities destroyed by pruning: (1) EOS token generation, ensuring the model can terminate sequences, and (2) basic format compliance, so that outputs follow the expected answer extraction pattern.
108	SFT warmup uses teacher-forced training on chain-of-thought traces, which does not require the model to produce complete generations and thus bypasses the EOS collapse problem.
109	This stage is intentionally brief---its purpose is to restore the minimal generation competence needed for GRPO, not to recover full reasoning ability.
110	
111	\paragraph{Stage 3b: GRPO recovery.}
112	With generation competence restored, we apply GRPO-based RLVR on mathematical reasoning data to recover the pruned model's reasoning ability.
113	The reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.
114	RLVR is preferred over extended SFT for reasoning recovery because of their fundamentally different training dynamics: \citet{rlsqueezes2026} show that RLVR \emph{compresses} incorrect reasoning trajectories while SFT \emph{expands} correct ones.
115	For a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.
116	Structures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for \rasp{}'s scoring criterion.
117	
118	\begin{algorithm}[t]
119	\caption{Recovery-Aware Structured Pruning (\rasp{})}
120	\label{alg:rasp}
121	\begin{algorithmic}[1]
122	\Require Model $\mathcal{M}$, calibration problems $\mathcal{D}_\text{cal}$, target sparsity $s$, overlap weight $\alpha$, SFT data $\mathcal{D}_\text{sft}$, RLVR data $\mathcal{D}_\text{rlvr}$, layer floor $\tau$
123	\Ensure Pruned and recovered model $\mathcal{M}'$
124	\Statex \textit{\% Stage 1: Reasoning-Trace Structural Analysis}
125	\State Load calibration pairs $\{(x_j, y_j)\}$ from $\mathcal{D}_\text{cal}$
126	\For{each structure $h \in \mathcal{H}$}
127	    \State Compute $I(h)$ via Eq.~\eqref{eq:importance}
128	    \State Collect activations $\mathbf{X}_h$
129	\EndFor
130	\For{each layer $\ell = 1, \ldots, L$}
131	    \For{each group $g_i \in \mathcal{G}_\ell$}
132	        \State $F(g_i) \gets \frac{1}{|\mathcal{G}_\ell|-1} \sum_{j \neq i} \text{CKA}(\mathbf{X}_{g_i}, \mathbf{X}_{g_j})$
133	    \EndFor
134	\EndFor
135	\Statex \textit{\% Stage 2: Recovery-Aware Scoring}
136	\For{each structure $h \in \mathcal{H}$}
137	    \State $S(h) \gets I(h) \times (1 - F(h))^\alpha$
138	\EndFor
139	\State Sort $\mathcal{H}$ by $S(h)$ ascending
140	\State $\mathcal{P} \gets \emptyset$
141	\For{each $h$ in sorted $\mathcal{H}$}
142	    \If{layer($h$) retains $< \tau$ fraction after adding $h$ to $\mathcal{P}$}
143	        \State \textbf{continue}
144	    \EndIf
145	    \State $\mathcal{P} \gets \mathcal{P} \cup \{h\}$
146	    \If{$\sum_{h' \in \mathcal{P}} \text{params}(h') \ge s \cdot |\theta|$}
147	        \State \textbf{break}
148	    \EndIf
149	\EndFor
150	\State $\mathcal{M}_\text{pruned} \gets \text{Remove}(\mathcal{M}, \mathcal{P})$
151	\Statex \textit{\% Stage 3: Two-Stage Recovery}
152	\State $\mathcal{M}_\text{warm} \gets \text{SFT}(\mathcal{M}_\text{pruned}, \mathcal{D}_\text{sft})$ \hfill $\triangleright$ restore EOS \& format
153	\State $\mathcal{M}' \gets \text{GRPO}(\mathcal{M}_\text{warm}, \mathcal{D}_\text{rlvr})$ \hfill $\triangleright$ restore reasoning
154	\State \Return $\mathcal{M}'$
155	\end{algorithmic}
156	\end{algorithm}
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "40c96d14-baca-43a0-a424-0753c7a66471",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex",
      "content": "\\section{Method: Recovery-Aware Structured Pruning}\n\\label{sec:method}\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.\nThe core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\\citep{rlsqueezes2026}.\n\n\\subsection{Preliminaries and Notation}\n\\label{sec:prelim}\n\n\\paragraph{Structured pruning.}\nGiven a pretrained transformer $\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.\nWe denote the set of prunable structures as $\\mathcal{H} = \\{h_1, h_2, \\ldots, h_N\\}$.\n\n\\paragraph{Grouped Query Attention (GQA).}\nIn GQA architectures~\\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.\nFor DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.\nWe treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.\n\n\\paragraph{RLVR and GRPO.}\nReinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.\nWe use Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) as the recovery algorithm, following~\\citet{selfhealing2025}.\n\n\\subsection{Stage 1: Reasoning-Trace Structural Analysis}\n\\label{sec:stage1}\n\n\\rasp{} computes two complementary scores per structure: \\emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \\emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.\n\n\\paragraph{Calibration data.}\nWe compute importance and overlap scores on chain-of-thought reasoning data from GSM8K~\\citep{cobbe2021gsm8k} training examples, using question--answer pairs as calibration traces.\nGiven a calibration set $\\mathcal{D}_\\text{cal} = \\{(x_j, y_j)\\}_{j=1}^{M}$, we compute activations and gradients on the concatenated sequences $(x_j, y_j)$.\nThis ensures importance scores reflect the model's behavior on representative reasoning tasks.\n\n\\paragraph{Structural importance.}\nFor each structure $h$, we compute importance $I(h)$ via first-order Taylor expansion on the reasoning trace loss:\n\\begin{equation}\n    I(h) = \\left| \\sum_{(x,y) \\in \\mathcal{D}_\\text{cal}} \\mathbf{a}_h(x, y)^\\top \\frac{\\partial \\mathcal{L}(x, y)}{\\partial \\mathbf{a}_h} \\right|,\n    \\label{eq:importance}\n\\end{equation}\nwhere $\\mathbf{a}_h$ denotes the activation of structure $h$ and $\\mathcal{L}$ is the language modeling loss over the reasoning trace.\nFor a GQA group $g$ containing Q heads $\\{q_1, \\ldots, q_G\\}$ and KV head $k$, we aggregate: $I(g) = \\sum_{i=1}^{G} I(q_i) + I(k)$.\n\n\\paragraph{Functional overlap via CKA.}\nWe measure functional overlap using linear Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.\nGiven activation matrices $\\mathbf{X}, \\mathbf{Y} \\in \\mathbb{R}^{n \\times d}$ collected over $n$ calibration examples, linear CKA is:\n\\begin{equation}\n    \\text{CKA}(\\mathbf{X}, \\mathbf{Y}) = \\frac{\\text{HSIC}(\\mathbf{X}, \\mathbf{Y})}{\\sqrt{\\text{HSIC}(\\mathbf{X}, \\mathbf{X}) \\cdot \\text{HSIC}(\\mathbf{Y}, \\mathbf{Y})}},\n    \\label{eq:cka}\n\\end{equation}\nwhere $\\text{HSIC}(\\mathbf{X}, \\mathbf{Y}) = \\frac{1}{(n-1)^2} \\operatorname{tr}(\\mathbf{K} \\mathbf{H} \\mathbf{L} \\mathbf{H})$, with $\\mathbf{K} = \\mathbf{X}\\mathbf{X}^\\top$, $\\mathbf{L} = \\mathbf{Y}\\mathbf{Y}^\\top$, and $\\mathbf{H} = \\mathbf{I}_n - \\frac{1}{n}\\mathbf{1}\\mathbf{1}^\\top$.\n\nFor a GQA group $g_i$ in layer $\\ell$, we form its representation by concatenating its constituent Q head activations: $\\mathbf{X}_{g_i} = [\\mathbf{a}_{q_1}; \\ldots; \\mathbf{a}_{q_G}] \\in \\mathbb{R}^{n \\times Gd_h}$.\nThe functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:\n\\begin{equation}\n    F(g_i) = \\frac{1}{|\\mathcal{G}_\\ell| - 1} \\sum_{\\substack{g_j \\in \\mathcal{G}_\\ell \\\\ j \\neq i}} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j}),\n    \\label{eq:overlap}\n\\end{equation}\nwhere $\\mathcal{G}_\\ell$ is the set of GQA groups in layer $\\ell$.\nUnlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.\n\n\\paragraph{MLP channel group overlap.}\nWe apply the same intra-layer CKA overlap to MLP channel groups.\nEach MLP intermediate dimension is partitioned into equal-sized groups; for group $m_i$ in layer $\\ell$, we compute $F(m_i) = \\frac{1}{|\\mathcal{M}_\\ell| - 1} \\sum_{m_j \\in \\mathcal{M}_\\ell, j \\neq i} \\text{CKA}(\\mathbf{X}_{m_i}, \\mathbf{X}_{m_j})$, where $\\mathcal{M}_\\ell$ is the set of MLP groups in layer $\\ell$.\nAttention GQA groups and MLP channel groups are then scored and ranked jointly in Stage~2.\n\n\\subsection{Stage 2: Recovery-Aware Scoring}\n\\label{sec:stage2}\n\nThe recovery-aware score combines importance and functional overlap:\n\\begin{equation}\n    S(h) = I(h) \\times \\big(1 - F(h)\\big)^\\alpha,\n    \\label{eq:score}\n\\end{equation}\nwhere $\\alpha \\ge 0$ controls the strength of the recoverability penalty ($\\alpha{=}0$ reduces to standard importance-only pruning).\nStructures with the lowest $S(h)$ are pruned up to the target sparsity ratio.\n\nThe scoring captures three regimes:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\\rightarrow$ \\emph{protected}.\n    \\item \\textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\\rightarrow$ \\emph{pruned preferentially}.\n    \\item \\textbf{Low $I$} (unimportant): Pruned regardless of overlap.\n\\end{itemize}\n\nThe key distinction from standard pruning---which ranks solely by $I(h)$---is that \\rasp{} additionally down-weights protection of structures whose function overlaps with retained structures.\nThis is motivated by the finding that RLVR recovers through global exploration and path compression~\\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.\n\n\\paragraph{Per-layer capacity floor.}\nGlobal ranking by $S(h)$ can concentrate pruning in layers where many structures have high overlap, collapsing that layer's representational capacity.\nTo prevent this, we enforce a per-layer capacity floor: each layer must retain at least 40\\% of its MLP channel groups after pruning.\nFor DeepSeek-R1-Distill-Qwen-7B, this requires ${\\ge}12$ of 28 MLP groups per layer.\nDuring structure selection, if removing a candidate would violate this constraint, it is skipped in favor of the next lowest-scoring structure.\nThis constraint adds negligible overhead to the scoring procedure but prevents representational collapse in individual layers---a failure mode we observed when unconstrained global ranking was applied at 20\\% sparsity.\n\nAttention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions subject to the per-layer floor.\nAlgorithm~\\ref{alg:rasp} summarizes the complete pipeline.\n\n\\subsection{Stage 3: Two-Stage Recovery}\n\\label{sec:stage3}\n\nAfter pruning, we recover reasoning ability through two stages: supervised finetuning (SFT) warmup followed by GRPO-based RLVR.\n\n\\paragraph{Motivation for two-stage recovery.}\nDirectly applying GRPO to a pruned model fails.\nStructured pruning disrupts the model's ability to generate end-of-sequence (EOS) tokens: in sampling mode, pruned models produce repetitive digit loops without termination, yielding sequences that are truncated at the maximum length.\nSince GRPO computes rewards only from completed generations, this EOS collapse means no valid completions are produced, the clipped ratio reaches 1.0, and gradient norms drop to zero---making direct RLVR recovery impossible.\n\n\\paragraph{Stage 3a: SFT warmup.}\nWe first apply a short SFT phase on reasoning demonstrations to restore two capabilities destroyed by pruning: (1) EOS token generation, ensuring the model can terminate sequences, and (2) basic format compliance, so that outputs follow the expected answer extraction pattern.\nSFT warmup uses teacher-forced training on chain-of-thought traces, which does not require the model to produce complete generations and thus bypasses the EOS collapse problem.\nThis stage is intentionally brief---its purpose is to restore the minimal generation competence needed for GRPO, not to recover full reasoning ability.\n\n\\paragraph{Stage 3b: GRPO recovery.}\nWith generation competence restored, we apply GRPO-based RLVR on mathematical reasoning data to recover the pruned model's reasoning ability.\nThe reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.\nRLVR is preferred over extended SFT for reasoning recovery because of their fundamentally different training dynamics: \\citet{rlsqueezes2026} show that RLVR \\emph{compresses} incorrect reasoning trajectories while SFT \\emph{expands} correct ones.\nFor a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.\nStructures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for \\rasp{}'s scoring criterion.\n\n\\begin{algorithm}[t]\n\\caption{Recovery-Aware Structured Pruning (\\rasp{})}\n\\label{alg:rasp}\n\\begin{algorithmic}[1]\n\\Require Model $\\mathcal{M}$, calibration problems $\\mathcal{D}_\\text{cal}$, target sparsity $s$, overlap weight $\\alpha$, SFT data $\\mathcal{D}_\\text{sft}$, RLVR data $\\mathcal{D}_\\text{rlvr}$, layer floor $\\tau$\n\\Ensure Pruned and recovered model $\\mathcal{M}'$\n\\Statex \\textit{\\% Stage 1: Reasoning-Trace Structural Analysis}\n\\State Load calibration pairs $\\{(x_j, y_j)\\}$ from $\\mathcal{D}_\\text{cal}$\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State Compute $I(h)$ via Eq.~\\eqref{eq:importance}\n    \\State Collect activations $\\mathbf{X}_h$\n\\EndFor\n\\For{each layer $\\ell = 1, \\ldots, L$}\n    \\For{each group $g_i \\in \\mathcal{G}_\\ell$}\n        \\State $F(g_i) \\gets \\frac{1}{|\\mathcal{G}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j})$\n    \\EndFor\n\\EndFor\n\\Statex \\textit{\\% Stage 2: Recovery-Aware Scoring}\n\\For{each structure $h \\in \\mathcal{H}$}\n    \\State $S(h) \\gets I(h) \\times (1 - F(h))^\\alpha$\n\\EndFor\n\\State Sort $\\mathcal{H}$ by $S(h)$ ascending\n\\State $\\mathcal{P} \\gets \\emptyset$\n\\For{each $h$ in sorted $\\mathcal{H}$}\n    \\If{layer($h$) retains $< \\tau$ fraction after adding $h$ to $\\mathcal{P}$}\n        \\State \\textbf{continue}\n    \\EndIf\n    \\State $\\mathcal{P} \\gets \\mathcal{P} \\cup \\{h\\}$\n    \\If{$\\sum_{h' \\in \\mathcal{P}} \\text{params}(h') \\ge s \\cdot |\\theta|$}\n        \\State \\textbf{break}\n    \\EndIf\n\\EndFor\n\\State $\\mathcal{M}_\\text{pruned} \\gets \\text{Remove}(\\mathcal{M}, \\mathcal{P})$\n\\Statex \\textit{\\% Stage 3: Two-Stage Recovery}\n\\State $\\mathcal{M}_\\text{warm} \\gets \\text{SFT}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{sft})$ \\hfill $\\triangleright$ restore EOS \\& format\n\\State $\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{warm}, \\mathcal{D}_\\text{rlvr})$ \\hfill $\\triangleright$ restore reasoning\n\\State \\Return $\\mathcal{M}'$\n\\end{algorithmic}\n\\end{algorithm}\n",
      "numLines": 157,
      "startLine": 1,
      "totalLines": 157
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_0132FQYgBTc4XsGFGk5p1GKS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "f1b1c47f-c1c1-496c-a9af-5b012fdc4ed1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ChAi8VmRHdmTwwGZLqREz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11640
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

_source line 8 · 2026-05-15T05:07:33.003Z_

<details><summary>↩ Tool result · `toolu_0132FQYgBTc4XsGFGk5p1GKS`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Structured Pruning of Large Language Models}
5	\label{sec:rw_pruning}
6	
7	Structured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.
8	LLM-Pruner~\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.
9	Bonsai~\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.
10	GRASPrune~\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.
11	ShortGPT~\citep{shortgpt2024} and SliceGPT~\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.
12	
13	For reasoning models specifically, RESP~\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\% on GSM8K at 40\% structured sparsity without any recovery training.
14	SSGR~\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.
15	\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.
16	RAC~\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.
17	\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \emph{which} structures are removed critically shapes recovery potential.
18	
19	A parallel line of work recognizes that \emph{functional structure} within networks should guide pruning decisions.
20	FANG~\citep{fang_2025} groups FFN neurons by functional roles via activation clustering and retains shared neurons to prevent cross-task accuracy loss, outperforming FLAP/OBC by 1.5--8.5\% at 30--40\% sparsity.
21	FuncNet~\citep{funcnet_2025} applies Independent Component Analysis (borrowed from neuroimaging) to decompose LLMs into functional networks and preserves key neurons within each.
22	Both share RASP's motivation of identifying functionally critical structures, but neither incorporates a recovery component: they optimize for immediate post-pruning accuracy rather than recoverability under a downstream training paradigm.
23	RASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.
24	
25	\subsection{Pruning-Aware Recovery and Re-training}
26	\label{sec:rw_recovery}
27	
28	Post-pruning recovery is essential at moderate to high compression ratios.
29	\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\%+ accuracy at 25\% compression, significantly outperforming SFT recovery (${\sim}$80\%).
30	This establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \emph{choice} of what to prune affects how well RLVR can recover.
31	
32	P\textsuperscript{2} Law~\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \propto (1/\rho)^\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.
33	PASER~\citep{paser2025} optimizes which recovery \emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \emph{structures} to prune for recoverability.
34	PAT~\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.
35	RestoreLCC~\citep{restorelcc_2025} proposes a plug-and-play recovery method that contrastively probes critical attention heads and injects lost activation components back into the pruned model, achieving consistent gains across pruning methods (NeurIPS 2025 Spotlight).
36	\citet{boiling_frog_2026} adopt an iterative prune-tune loop that gradually compresses reasoning models, avoiding abrupt performance collapse through incremental SFT recovery.
37	Both represent alternative recovery strategies; RASP is complementary in that it optimizes \emph{what} to prune for RLVR recoverability, whereas RestoreLCC optimizes \emph{how} to compensate after pruning and Boiling Frog optimizes the \emph{schedule} of pruning-recovery iterations.
38	
39	The Lottery Ticket Hypothesis~\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.
40	RASP extends this notion to what we term \emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.
41	
42	\subsection{RLVR Training Dynamics}
43	\label{sec:rw_rlvr}
44	
45	Understanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.
46	\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \emph{expands} correct trajectories via local imitation.
47	This asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.
48	OPSD~\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.
49	
50	\paragraph{CKA-based pruning.}
51	CKA~\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.
52	Among representation similarity measures (CCA, SVCCA, PWCCA, CKA), \citet{klabunde_similarity_survey_2025} show that CKA achieves 99.3\% layer identification accuracy versus 45.4\% for SVCCA, owing to its invariance to invertible linear transforms and isotropic scaling---properties critical for comparing heterogeneous structures (GQA groups vs.\ MLP channels) within the same layer.
53	MPruner~\citep{mpruner2024} uses \emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.
54	\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.
55	Both operate at the \emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.
56	In contrast, RASP uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\ immediate accuracy preservation).
57	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "3c89f929-b987-4483-9b10-60976909313b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Structured Pruning of Large Language Models}\n\\label{sec:rw_pruning}\n\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\nBonsai~\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.\nGRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\nShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n\nFor reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\nSSGR~\\citep{ssgr2025} shows that selective self-generated calibration with challenging, moderately-lengthy reasoning examples further improves pruning quality for reasoning LLMs.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\nRAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.\n\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\n\nA parallel line of work recognizes that \\emph{functional structure} within networks should guide pruning decisions.\nFANG~\\citep{fang_2025} groups FFN neurons by functional roles via activation clustering and retains shared neurons to prevent cross-task accuracy loss, outperforming FLAP/OBC by 1.5--8.5\\% at 30--40\\% sparsity.\nFuncNet~\\citep{funcnet_2025} applies Independent Component Analysis (borrowed from neuroimaging) to decompose LLMs into functional networks and preserves key neurons within each.\nBoth share RASP's motivation of identifying functionally critical structures, but neither incorporates a recovery component: they optimize for immediate post-pruning accuracy rather than recoverability under a downstream training paradigm.\nRASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.\n\n\\subsection{Pruning-Aware Recovery and Re-training}\n\\label{sec:rw_recovery}\n\nPost-pruning recovery is essential at moderate to high compression ratios.\n\\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\\%+ accuracy at 25\\% compression, significantly outperforming SFT recovery (${\\sim}$80\\%).\nThis establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects how well RLVR can recover.\n\nP\\textsuperscript{2} Law~\\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \\propto (1/\\rho)^\\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.\nPASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \\emph{structures} to prune for recoverability.\nPAT~\\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.\nRestoreLCC~\\citep{restorelcc_2025} proposes a plug-and-play recovery method that contrastively probes critical attention heads and injects lost activation components back into the pruned model, achieving consistent gains across pruning methods (NeurIPS 2025 Spotlight).\n\\citet{boiling_frog_2026} adopt an iterative prune-tune loop that gradually compresses reasoning models, avoiding abrupt performance collapse through incremental SFT recovery.\nBoth represent alternative recovery strategies; RASP is complementary in that it optimizes \\emph{what} to prune for RLVR recoverability, whereas RestoreLCC optimizes \\emph{how} to compensate after pruning and Boiling Frog optimizes the \\emph{schedule} of pruning-recovery iterations.\n\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.\nRASP extends this notion to what we term \\emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.\n\n\\subsection{RLVR Training Dynamics}\n\\label{sec:rw_rlvr}\n\nUnderstanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.\n\\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct trajectories via local imitation.\nThis asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.\nOPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n\n\\paragraph{CKA-based pruning.}\nCKA~\\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.\nAmong representation similarity measures (CCA, SVCCA, PWCCA, CKA), \\citet{klabunde_similarity_survey_2025} show that CKA achieves 99.3\\% layer identification accuracy versus 45.4\\% for SVCCA, owing to its invariance to invertible linear transforms and isotropic scaling---properties critical for comparing heterogeneous structures (GQA groups vs.\\ MLP channels) within the same layer.\nMPruner~\\citep{mpruner2024} uses \\emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.\n\\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.\nBoth operate at the \\emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.\nIn contrast, RASP uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\\ immediate accuracy preservation).\n",
      "numLines": 57,
      "startLine": 1,
      "totalLines": 57
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01WrmSCEtLzZZ7i4XxnvCfQx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "0356e866-6b06-4a6b-82ec-69da37eacb55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ChAi8VmRHdmTwwGZLqREz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11640
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

_source line 10 · 2026-05-15T05:07:33.527Z_

<details><summary>↩ Tool result · `toolu_01WrmSCEtLzZZ7i4XxnvCfQx`</summary>

```text
1	@article{deepseek2025r1,
2	  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},
3	  author={{DeepSeek-AI}},
4	  journal={arXiv preprint arXiv:2501.12948},
5	  year={2025},
6	  url={https://arxiv.org/abs/2501.12948}
7	}
8	
9	@article{qwen2.5,
10	  title={Qwen2.5 Technical Report},
11	  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},
12	  journal={arXiv preprint arXiv:2412.15115},
13	  year={2024},
14	  url={https://arxiv.org/abs/2412.15115}
15	}
16	
17	@article{cobbe2021gsm8k,
18	  title={Training Verifiers to Solve Math Word Problems},
19	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
20	  journal={arXiv preprint arXiv:2110.14168},
21	  year={2021},
22	  url={https://arxiv.org/abs/2110.14168}
23	}
24	
25	@article{shao2024grpo,
26	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
27	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
28	  journal={arXiv preprint arXiv:2402.03300},
29	  year={2024},
30	  url={https://arxiv.org/abs/2402.03300}
31	}
32	
33	@inproceedings{llmpruner2023,
34	  title={LLM-Pruner: On the Structural Pruning of Large Language Models},
35	  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},
36	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
37	  year={2023},
38	  url={https://arxiv.org/abs/2305.11627}
39	}
40	
41	@inproceedings{graspprune2026,
42	  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},
43	  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
44	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
45	  year={2026},
46	  url={https://arxiv.org/abs/2604.19398}
47	}
48	
49	@article{resp2025,
50	  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},
51	  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},
52	  journal={arXiv preprint arXiv:2512.02185},
53	  year={2025},
54	  url={https://arxiv.org/abs/2512.02185}
55	}
56	
57	@article{selfhealing2025,
58	  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},
59	  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},
60	  year={2025},
61	  note={Under review},
62	  url={https://openreview.net/forum?id=Cy8Qa4gAst}
63	}
64	
65	@inproceedings{bonsai2025,
66	  title={Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes},
67	  author={Kolawole, Steven and Dery, Lucio and Kagy, Jean-Fran\c{c}ois and Smith, Virginia and Neubig, Graham and Talwalkar, Ameet},
68	  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},
69	  year={2025},
70	  url={https://arxiv.org/abs/2402.05406}
71	}
72	
73	@article{paser2025,
74	  title={PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},
75	  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},
76	  journal={arXiv preprint arXiv:2502.12594},
77	  year={2025},
78	  url={https://arxiv.org/abs/2502.12594},
79	  note={Under review}
80	}
81	
82	@inproceedings{rlsqueezes2026,
83	  title={RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs},
84	  author={Matsutani, Kohsei and Takashiro, Shota and Minegishi, Gouki and Kojima, Takeshi and Iwasawa, Yusuke and Matsuo, Yutaka},
85	  booktitle={Proceedings of the 14th International Conference on Learning Representations (ICLR)},
86	  year={2026},
87	  url={https://arxiv.org/abs/2509.21128}
88	}
89	
90	@inproceedings{kornblith2019cka,
91	  title={Similarity of Neural Network Representations Revisited},
92	  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},
93	  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},
94	  year={2019},
95	  url={https://arxiv.org/abs/1905.00414}
96	}
97	
98	@article{mpruner2024,
99	  title={MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning},
100	  author={Hu, Seungbeom and Park, Chanjun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},
101	  journal={arXiv preprint arXiv:2408.13482},
102	  year={2024},
103	  url={https://arxiv.org/abs/2408.13482}
104	}
105	
106	@mastersthesis{lachance2024cka,
107	  title={Using Centered Kernel Alignment for Understanding and Pruning Neural Networks},
108	  author={Lachance, Alex},
109	  school={University of Rhode Island},
110	  year={2024},
111	  url={https://digitalcommons.uri.edu/theses/2283/}
112	}
113	
114	@inproceedings{frankle2019lth,
115	  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},
116	  author={Frankle, Jonathan and Carbin, Michael},
117	  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},
118	  year={2019},
119	  url={https://arxiv.org/abs/1803.03635}
120	}
121	
122	@inproceedings{ainslie2023gqa,
123	  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},
124	  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\'o}n, Federico and Sanghai, Sumit},
125	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
126	  year={2023},
127	  url={https://arxiv.org/abs/2305.13245}
128	}
129	
130	@article{shortgpt2024,
131	  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},
132	  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},
133	  journal={arXiv preprint arXiv:2403.03853},
134	  year={2024},
135	  url={https://arxiv.org/abs/2403.03853}
136	}
137	
138	@inproceedings{slicegpt2024,
139	  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},
140	  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},
141	  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},
142	  year={2024},
143	  url={https://arxiv.org/abs/2401.15024}
144	}
145	
146	@inproceedings{wanda2024,
147	  title={A Simple and Effective Pruning Approach for Large Language Models},
148	  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},
149	  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},
150	  year={2024},
151	  url={https://arxiv.org/abs/2306.11695}
152	}
153	
154	@article{llms2lrms2026,
155	  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},
156	  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},
157	  journal={arXiv preprint arXiv:2601.18091},
158	  year={2026},
159	  url={https://arxiv.org/abs/2601.18091}
160	}
161	
162	@inproceedings{rac2025,
163	  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},
164	  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},
165	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
166	  year={2025},
167	  url={https://arxiv.org/abs/2509.12464}
168	}
169	
170	@article{ssgr2025,
171	  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},
172	  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},
173	  journal={arXiv preprint arXiv:2511.18864},
174	  year={2025},
175	  url={https://arxiv.org/abs/2511.18864}
176	}
177	
178	@article{doingmore2026,
179	  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
180	  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
181	  journal={arXiv preprint arXiv:2604.25098},
182	  year={2026},
183	  url={https://arxiv.org/abs/2604.25098}
184	}
185	
186	@inproceedings{p2law2025,
187	  title={{P\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},
188	  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},
189	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
190	  year={2025},
191	  url={https://arxiv.org/abs/2411.10272}
192	}
193	
194	@inproceedings{pat2025,
195	  title={{PAT}: Pruning-Aware Tuning for Large Language Models},
196	  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},
197	  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},
198	  year={2025},
199	  url={https://arxiv.org/abs/2408.14721}
200	}
201	
202	@article{fang_2025,
203	  title={{FANG}: Improving Generalization in {LLM} Structured Pruning via Function-Aware Neuron Grouping},
204	  author={Yu, Tao and An, Yongqi and Zhu, Kuan and Zhu, Guibo and Tang, Ming and Wang, Jinqiao},
205	  journal={arXiv preprint arXiv:2512.23014},
206	  year={2025},
207	  url={https://arxiv.org/abs/2512.23014}
208	}
209	
210	@article{funcnet_2025,
211	  title={Pruning Large Language Models by Identifying and Preserving Functional Networks},
212	  author={Liu, Yiheng and Ning, Junhao and Xia, Sichen and Gao, Xiaohui and Qiang, Ning and Ge, Bao and Han, Junwei and Hu, Xintao},
213	  journal={arXiv preprint arXiv:2508.05239},
214	  year={2025},
215	  url={https://arxiv.org/abs/2508.05239}
216	}
217	
218	@article{klabunde_similarity_survey_2025,
219	  title={Similarity of Neural Network Models: A Survey of Functional and Representational Measures},
220	  author={Klabunde, Max and Schumacher, Tobias and Strohmaier, Markus and Lemmerich, Florian},
221	  journal={ACM Computing Surveys},
222	  volume={57},
223	  number={9},
224	  year={2025},
225	  url={https://arxiv.org/abs/2305.06329}
226	}
227	
228	@inproceedings{restorelcc_2025,
229	  title={{RestoreLCC}: Restoring Pruned Large Language Models via Lost Component Compensation},
230	  author={Feng, Zijian and Zhou, Hanzhang and Zhu, Zixiao and Li, Tianjiao and Chua, Jia Jim Deryl and Mak, Lee Onn and Ng, Gee Wah and Mao, Kezhi},
231	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
232	  year={2025},
233	  note={Spotlight},
234	  url={https://arxiv.org/abs/2510.21834}
235	}
236	
237	@article{boiling_frog_2026,
238	  title={Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog},
239	  author={Zhao, Yiran and Zhou, Shengyang and Wu, Zijian and Hu, Tongyan and Xu, Yuhui and Dou, Rengan and Kawaguchi, Kenji and Joty, Shafiq and Li, Junnan and Shieh, Michael Qizhe},
240	  journal={arXiv preprint arXiv:2602.04919},
241	  year={2026},
242	  url={https://arxiv.org/abs/2602.04919}
243	}
244	
245	@article{opsd2026,
246	  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},
247	  author={Kim, Jaehoon and Lee, Dongha},
248	  journal={arXiv preprint arXiv:2605.06188},
249	  year={2026},
250	  url={https://arxiv.org/abs/2605.06188}
251	}
252	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "5d46cd30-5727-40bc-978f-e0b89a11bd21",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
      "content": "@article{deepseek2025r1,\n  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025},\n  url={https://arxiv.org/abs/2501.12948}\n}\n\n@article{qwen2.5,\n  title={Qwen2.5 Technical Report},\n  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},\n  journal={arXiv preprint arXiv:2412.15115},\n  year={2024},\n  url={https://arxiv.org/abs/2412.15115}\n}\n\n@article{cobbe2021gsm8k,\n  title={Training Verifiers to Solve Math Word Problems},\n  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal={arXiv preprint arXiv:2110.14168},\n  year={2021},\n  url={https://arxiv.org/abs/2110.14168}\n}\n\n@article{shao2024grpo,\n  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal={arXiv preprint arXiv:2402.03300},\n  year={2024},\n  url={https://arxiv.org/abs/2402.03300}\n}\n\n@inproceedings{llmpruner2023,\n  title={LLM-Pruner: On the Structural Pruning of Large Language Models},\n  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.11627}\n}\n\n@inproceedings{graspprune2026,\n  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},\n  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2026},\n  url={https://arxiv.org/abs/2604.19398}\n}\n\n@article{resp2025,\n  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},\n  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},\n  journal={arXiv preprint arXiv:2512.02185},\n  year={2025},\n  url={https://arxiv.org/abs/2512.02185}\n}\n\n@article{selfhealing2025,\n  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},\n  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},\n  year={2025},\n  note={Under review},\n  url={https://openreview.net/forum?id=Cy8Qa4gAst}\n}\n\n@inproceedings{bonsai2025,\n  title={Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes},\n  author={Kolawole, Steven and Dery, Lucio and Kagy, Jean-Fran\\c{c}ois and Smith, Virginia and Neubig, Graham and Talwalkar, Ameet},\n  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2402.05406}\n}\n\n@article{paser2025,\n  title={PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},\n  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},\n  journal={arXiv preprint arXiv:2502.12594},\n  year={2025},\n  url={https://arxiv.org/abs/2502.12594},\n  note={Under review}\n}\n\n@inproceedings{rlsqueezes2026,\n  title={RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs},\n  author={Matsutani, Kohsei and Takashiro, Shota and Minegishi, Gouki and Kojima, Takeshi and Iwasawa, Yusuke and Matsuo, Yutaka},\n  booktitle={Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2509.21128}\n}\n\n@inproceedings{kornblith2019cka,\n  title={Similarity of Neural Network Representations Revisited},\n  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},\n  year={2019},\n  url={https://arxiv.org/abs/1905.00414}\n}\n\n@article{mpruner2024,\n  title={MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning},\n  author={Hu, Seungbeom and Park, Chanjun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},\n  journal={arXiv preprint arXiv:2408.13482},\n  year={2024},\n  url={https://arxiv.org/abs/2408.13482}\n}\n\n@mastersthesis{lachance2024cka,\n  title={Using Centered Kernel Alignment for Understanding and Pruning Neural Networks},\n  author={Lachance, Alex},\n  school={University of Rhode Island},\n  year={2024},\n  url={https://digitalcommons.uri.edu/theses/2283/}\n}\n\n@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carbin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}\n\n@inproceedings{ainslie2023gqa,\n  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},\n  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\\'o}n, Federico and Sanghai, Sumit},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.13245}\n}\n\n@article{shortgpt2024,\n  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},\n  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},\n  journal={arXiv preprint arXiv:2403.03853},\n  year={2024},\n  url={https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{slicegpt2024,\n  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},\n  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.15024}\n}\n\n@inproceedings{wanda2024,\n  title={A Simple and Effective Pruning Approach for Large Language Models},\n  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2306.11695}\n}\n\n@article{llms2lrms2026,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026},\n  url={https://arxiv.org/abs/2601.18091}\n}\n\n@inproceedings{rac2025,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2509.12464}\n}\n\n@article{ssgr2025,\n  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},\n  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},\n  journal={arXiv preprint arXiv:2511.18864},\n  year={2025},\n  url={https://arxiv.org/abs/2511.18864}\n}\n\n@article{doingmore2026,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026},\n  url={https://arxiv.org/abs/2604.25098}\n}\n\n@inproceedings{p2law2025,\n  title={{P\\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},\n  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2411.10272}\n}\n\n@inproceedings{pat2025,\n  title={{PAT}: Pruning-Aware Tuning for Large Language Models},\n  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},\n  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.14721}\n}\n\n@article{fang_2025,\n  title={{FANG}: Improving Generalization in {LLM} Structured Pruning via Function-Aware Neuron Grouping},\n  author={Yu, Tao and An, Yongqi and Zhu, Kuan and Zhu, Guibo and Tang, Ming and Wang, Jinqiao},\n  journal={arXiv preprint arXiv:2512.23014},\n  year={2025},\n  url={https://arxiv.org/abs/2512.23014}\n}\n\n@article{funcnet_2025,\n  title={Pruning Large Language Models by Identifying and Preserving Functional Networks},\n  author={Liu, Yiheng and Ning, Junhao and Xia, Sichen and Gao, Xiaohui and Qiang, Ning and Ge, Bao and Han, Junwei and Hu, Xintao},\n  journal={arXiv preprint arXiv:2508.05239},\n  year={2025},\n  url={https://arxiv.org/abs/2508.05239}\n}\n\n@article{klabunde_similarity_survey_2025,\n  title={Similarity of Neural Network Models: A Survey of Functional and Representational Measures},\n  author={Klabunde, Max and Schumacher, Tobias and Strohmaier, Markus and Lemmerich, Florian},\n  journal={ACM Computing Surveys},\n  volume={57},\n  number={9},\n  year={2025},\n  url={https://arxiv.org/abs/2305.06329}\n}\n\n@inproceedings{restorelcc_2025,\n  title={{RestoreLCC}: Restoring Pruned Large Language Models via Lost Component Compensation},\n  author={Feng, Zijian and Zhou, Hanzhang and Zhu, Zixiao and Li, Tianjiao and Chua, Jia Jim Deryl and Mak, Lee Onn and Ng, Gee Wah and Mao, Kezhi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  note={Spotlight},\n  url={https://arxiv.org/abs/2510.21834}\n}\n\n@article{boiling_frog_2026,\n  title={Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog},\n  author={Zhao, Yiran and Zhou, Shengyang and Wu, Zijian and Hu, Tongyan and Xu, Yuhui and Dou, Rengan and Kawaguchi, Kenji and Joty, Shafiq and Li, Junnan and Shieh, Michael Qizhe},\n  journal={arXiv preprint arXiv:2602.04919},\n  year={2026},\n  url={https://arxiv.org/abs/2602.04919}\n}\n\n@article{opsd2026,\n  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},\n  author={Kim, Jaehoon and Lee, Dongha},\n  journal={arXiv preprint arXiv:2605.06188},\n  year={2026},\n  url={https://arxiv.org/abs/2605.06188}\n}\n",
      "numLines": 252,
      "startLine": 1,
      "totalLines": 252
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01HLezh8tZzeibtiaZeTHQRH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "ea6661cf-fd87-4fbc-8cd1-0f3b67f5abfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ChAi8VmRHdmTwwGZLqREz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11640,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11640
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

_source line 12 · 2026-05-15T05:07:34.056Z_

<details><summary>↩ Tool result · `toolu_01HLezh8tZzeibtiaZeTHQRH`</summary>

```text
1	# recovery_aware_struct_prune — Research Dashboard
2	
3	> 最后更新: 2026-05-15 01:57 UTC | 更新原因: Dream dream_20260514T233950 分析完成 + 新增 plan_015-017 + 扩展 plan_006
4	
5	## 核心方向
6	Recovery-Aware Structured Pruning (RASP)：CKA functional overlap 指导结构化剪枝，在 matched sparsity 下比 importance-only 剪枝显著更好地保留推理能力（**Redundancy Paradox**）。详见 paper_framing.md。
7	
8	## 目标会议
9	EMNLP 2026 ARR May 25 提交（距今 10 天）
10	
11	## 当前阶段
12	**Research Phase** — GRPO Stage 2 决定性实验进行中（D015）。Dream 分析完成（D016）。
13	
14	## 核心证据
15	- Post-prune GSM8K (N=100): RASP 29% vs Standard 1% (p<0.0001, matched 20% sparsity)
16	- Post-SFT GSM8K (N=100): RASP 57% vs Standard 64%（Standard 反超 7pp，SFT 偏好 Standard）
17	- GRPO Stage 2 双卡并行运行中——**决定性实验**
18	
19	## Dream 分析 (D016, dream_20260514T233950)
20	- Best=Weak Accept (4/6), Median=Weak Reject (3/6), Worst=Weak Reject (3/6)
21	- **三档一致结构性问题**：α ablation 缺失(Critical)、single model、no inference speedup、multi-seed 不足(3→5+)、scope overclaim
22	- **两档一致**：missing related work(FANG/FuncNet)、CKA justification、unstructured baseline、per-layer floor confound
23	- **数据依赖(等GRPO)**：RASP vs GRASPrune ranking、CKA predictivity
24	- 新增 plan_015(α ablation P0), plan_016(inference speedup P1), plan_017(unstructured baseline P1)
25	
26	## Claims & 实验覆盖
27	| Claim | P0 实验 | 状态 |
28	|-------|---------|------|
29	| C1: CKA-aware pruning preserves reasoning | plan_001-006, plan_015 | ⏳ GRPO Stage 2 运行中 |
30	| C2: F(h) predicts recoverability | plan_007-008, plan_014-015 | 待 GRPO 完成 |
31	| C3: Recovery method conditions pruning order | plan_009 | SFT 证据已有，待 GRPO 确认反转 |
32	
33	## 近期任务
34	- [ ] GRPO Stage 2 双卡运行中 → plan_003（cuda:0 RASP, cuda:1 Standard）
35	- [ ] GRASPrune 代码准备（Agent 进行中，不占 GPU）→ plan_005 前置
36	- [ ] Full GSM8K eval 脚本准备（Agent 进行中）→ plan_001 前置
37	- [ ] **[Dream 行动] α ablation plan_015 — GRPO 完成后立即执行(P0)**
38	- [ ] **[Dream 行动] Inference speedup plan_016 — GRPO 完成后执行(P1)**
39	- [ ] **[Dream 行动] Unstructured baseline plan_017 — GRPO 完成后执行(P1)**
40	- [ ] **[Dream 行动] Multi-seed 扩展 plan_006 到 5 seeds**
41	- [ ] [Dream 观察] RASP vs GRASPrune ranking（plan_005 结果出来后评估）
42	- [ ] [Dream 观察] CKA predictivity（plan_008 结果出来后评估）
43	- [ ] [Dream 观察] Per-layer floor ablation（GRPO 后评估是否需要）
44	- [x] D013 SFT warmup → 完成，RASP 57% / Standard 64%
45	- [x] D015 判断：SFT Standard>RASP 不改方向，GRPO 是决定性实验
46	- [x] D016 Dream 分析完成，新增 3 个 plan + 扩展 plan_006
47	
48	## GRPO 结果 Contingency
49	| GRPO 结果 | 影响 | 行动 |
50	|-----------|------|------|
51	| RASP >> Standard (>10pp) | Claim 1+3 强支撑 | 全面推进 plan_001-017 |
52	| RASP > Standard (5-10pp) | Claim 1 成立，需 full eval 确认显著性 | 优先 plan_001 + plan_006 + plan_015 |
53	| RASP ≈ Standard (<5pp) | Claim 1 弱化，Claim 3 不成立 | 转 training dynamics 分析 + 25% sparsity |
54	| Standard > RASP | 核心假设失败 | Reframe 为负向发现论文或 pivot |
55	
56	## GPU 预算
57	westb-23072：2× RTX PRO 6000 94G（cuda:0, cuda:1）| 约束 C001
58	- GPU0: grpo_stage2_rasp_20 RUNNING
59	- GPU1: grpo_stage2_standard_20 RUNNING
60	- 总预算 ~480 GPU-hours (10 days × 2 GPU × 24h)
61	- Dream 新增实验 GPU 需求: ~30h (plan_015: 5h + plan_016: 1h + plan_017: 15h + plan_006 扩展: 4h + buffer)
62	
63	## 论文写作备忘（Dream 通用建议，给 Paper Agent）
64	- 扩展 references 到 25+，引用 FANG、FuncNet、RestoreLCC、PAT
65	- 论证 CKA vs SVCCA/CCA/MI 选择
66	- 讨论 Claim 2 潜在循环性并加以区分
67	- 论证 q_proj 作为 CKA 计算输入的合理性
68	- 报告 I(h)-F(h) correlation
69	- Temper scope claims（单模型局限性坦诚讨论）
70	
71	## 关键风险
72	1. **GRPO Stage 2 失败 = 项目 pivot**——唯一核心风险，已有 contingency
73	2. GRASPrune 可能在 post-recovery 超过 RASP → 需 reframe RASP 角色
74	3. 单模型限制 → Dream 三档一致标记，论文需坦诚讨论
75	4. α ablation 可能揭示方法对参数敏感 → 但不做更危险（reviewer 必问）
76	
77	## 关键决策日志
78	
79	| ID | 日期 | 摘要 | 关联实验 |
80	|----|------|------|----------|
81	| D017 | 2026-05-15 | D017: Kill GRPO Stage 2 并以优化参数重启。max_completion_le | grpo_stage2_rasp_20, grpo_stage2_standard_20 |
82	| D016 | 2026-05-15 | D016: Dream dream_20260514T233950 分析完成。Best=4/6, M | grpo_stage2_rasp_20, grpo_stage2_standard_20 |
83	| D015 | 2026-05-15 | SFT 结果 Standard>RASP 不改变方向，立即启动 GRPO Stage 2 作为决定性 | sft_rasp_20, sft_standard_20 |
84	| D014 | 2026-05-14 | D014: MVP PASS — 接受 post-prune 29% vs 1% 作为充分证据，GR | grpo_rasp_20_4096, grpo_standard_20_4096, grpo_rasp_20_fast, grpo_standard_20_fast, mvp_rasp_pipeline_v4 |
85	| D013 | 2026-05-14 | D012: RASP GRPO 4096也零梯度, 根因是sampling下无EOS而非token长 | grpo_rasp_20_4096, grpo_standard_20_4096 |
86	| D012 | 2026-05-14 | D011: Kill grpo_standard_20_4096 early, start grpo | grpo_standard_20_4096, grpo_rasp_20_4096 |
87	| D011 | 2026-05-14 | D011: Kill standard GRPO 4096 (10步零梯度), 将GPU1转给RAS | grpo_standard_20_4096, grpo_rasp_20_4096 |
88	| D010 | 2026-05-14 | 审批 Option A：max_completion_length=4096 重跑 GRPO 双实验 | grpo_rasp_20_fast, grpo_standard_20_fast |
89	| D009 | 2026-05-14 | GRPO 1024-token 截断伪阴性：不接受 negative 结论，诊断性 eval + 准 | grpo_rasp_20_fast, grpo_standard_20_fast |
90	| D008 | 2026-05-14 | 正式更新 MVP 判定标准：从 per-group ρ ≥ 0.4 改为 model-level 显 | grpo_rasp_20_fast, grpo_standard_20_fast, mvp_rasp_pipeline_v4 |
91	
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "987d40ae-391d-4076-8302-1fb949cedb98",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/ROADMAP.md",
      "content": "# recovery_aware_struct_prune — Research Dashboard\n\n> 最后更新: 2026-05-15 01:57 UTC | 更新原因: Dream dream_20260514T233950 分析完成 + 新增 plan_015-017 + 扩展 plan_006\n\n## 核心方向\nRecovery-Aware Structured Pruning (RASP)：CKA functional overlap 指导结构化剪枝，在 matched sparsity 下比 importance-only 剪枝显著更好地保留推理能力（**Redundancy Paradox**）。详见 paper_framing.md。\n\n## 目标会议\nEMNLP 2026 ARR May 25 提交（距今 10 天）\n\n## 当前阶段\n**Research Phase** — GRPO Stage 2 决定性实验进行中（D015）。Dream 分析完成（D016）。\n\n## 核心证据\n- Post-prune GSM8K (N=100): RASP 29% vs Standard 1% (p<0.0001, matched 20% sparsity)\n- Post-SFT GSM8K (N=100): RASP 57% vs Standard 64%（Standard 反超 7pp，SFT 偏好 Standard）\n- GRPO Stage 2 双卡并行运行中——**决定性实验**\n\n## Dream 分析 (D016, dream_20260514T233950)\n- Best=Weak Accept (4/6), Median=Weak Reject (3/6), Worst=Weak Reject (3/6)\n- **三档一致结构性问题**：α ablation 缺失(Critical)、single model、no inference speedup、multi-seed 不足(3→5+)、scope overclaim\n- **两档一致**：missing related work(FANG/FuncNet)、CKA justification、unstructured baseline、per-layer floor confound\n- **数据依赖(等GRPO)**：RASP vs GRASPrune ranking、CKA predictivity\n- 新增 plan_015(α ablation P0), plan_016(inference speedup P1), plan_017(unstructured baseline P1)\n\n## Claims & 实验覆盖\n| Claim | P0 实验 | 状态 |\n|-------|---------|------|\n| C1: CKA-aware pruning preserves reasoning | plan_001-006, plan_015 | ⏳ GRPO Stage 2 运行中 |\n| C2: F(h) predicts recoverability | plan_007-008, plan_014-015 | 待 GRPO 完成 |\n| C3: Recovery method conditions pruning order | plan_009 | SFT 证据已有，待 GRPO 确认反转 |\n\n## 近期任务\n- [ ] GRPO Stage 2 双卡运行中 → plan_003（cuda:0 RASP, cuda:1 Standard）\n- [ ] GRASPrune 代码准备（Agent 进行中，不占 GPU）→ plan_005 前置\n- [ ] Full GSM8K eval 脚本准备（Agent 进行中）→ plan_001 前置\n- [ ] **[Dream 行动] α ablation plan_015 — GRPO 完成后立即执行(P0)**\n- [ ] **[Dream 行动] Inference speedup plan_016 — GRPO 完成后执行(P1)**\n- [ ] **[Dream 行动] Unstructured baseline plan_017 — GRPO 完成后执行(P1)**\n- [ ] **[Dream 行动] Multi-seed 扩展 plan_006 到 5 seeds**\n- [ ] [Dream 观察] RASP vs GRASPrune ranking（plan_005 结果出来后评估）\n- [ ] [Dream 观察] CKA predictivity（plan_008 结果出来后评估）\n- [ ] [Dream 观察] Per-layer floor ablation（GRPO 后评估是否需要）\n- [x] D013 SFT warmup → 完成，RASP 57% / Standard 64%\n- [x] D015 判断：SFT Standard>RASP 不改方向，GRPO 是决定性实验\n- [x] D016 Dream 分析完成，新增 3 个 plan + 扩展 plan_006\n\n## GRPO 结果 Contingency\n| GRPO 结果 | 影响 | 行动 |\n|-----------|------|------|\n| RASP >> Standard (>10pp) | Claim 1+3 强支撑 | 全面推进 plan_001-017 |\n| RASP > Standard (5-10pp) | Claim 1 成立，需 full eval 确认显著性 | 优先 plan_001 + plan_006 + plan_015 |\n| RASP ≈ Standard (<5pp) | Claim 1 弱化，Claim 3 不成立 | 转 training dynamics 分析 + 25% sparsity |\n| Standard > RASP | 核心假设失败 | Reframe 为负向发现论文或 pivot |\n\n## GPU 预算\nwestb-23072：2× RTX PRO 6000 94G（cuda:0, cuda:1）| 约束 C001\n- GPU0: grpo_stage2_rasp_20 RUNNING\n- GPU1: grpo_stage2_standard_20 RUNNING\n- 总预算 ~480 GPU-hours (10 days × 2 GPU × 24h)\n- Dream 新增实验 GPU 需求: ~30h (plan_015: 5h + plan_016: 1h + plan_017: 15h + plan_006 扩展: 4h + buffer)\n\n## 论文写作备忘（Dream 通用建议，给 Paper Agent）\n- 扩展 references 到 25+，引用 FANG、FuncNet、RestoreLCC、PAT\n- 论证 CKA vs SVCCA/CCA/MI 选择\n- 讨论 Claim 2 潜在循环性并加以区分\n- 论证 q_proj 作为 CKA 计算输入的合理性\n- 报告 I(h)-F(h) correlation\n- Temper scope claims（单模型局限性坦诚讨论）\n\n## 关键风险\n1. **GRPO Stage 2 失败 = 项目 pivot**——唯一核心风险，已有 contingency\n2. GRASPrune 可能在 post-recovery 超过 RASP → 需 reframe RASP 角色\n3. 单模型限制 → Dream 三档一致标记，论文需坦诚讨论\n4. α ablation 可能揭示方法对参数敏感 → 但不做更危险（reviewer 必问）\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D017 | 2026-05-15 | D017: Kill GRPO Stage 2 并以优化参数重启。max_completion_le | grpo_stage2_rasp_20, grpo_stage2_standard_20 |\n| D016 | 2026-05-15 | D016: Dream dream_20260514T233950 分析完成。Best=4/6, M | grpo_stage2_rasp_20, grpo_stage2_standard_20 |\n| D015 | 2026-05-15 | SFT 结果 Standard>RASP 不改变方向，立即启动 GRPO Stage 2 作为决定性 | sft_rasp_20, sft_standard_20 |\n| D014 | 2026-05-14 | D014: MVP PASS — 接受 post-prune 29% vs 1% 作为充分证据，GR | grpo_rasp_20_4096, grpo_standard_20_4096, grpo_rasp_20_fast, grpo_standard_20_fast, mvp_rasp_pipeline_v4 |\n| D013 | 2026-05-14 | D012: RASP GRPO 4096也零梯度, 根因是sampling下无EOS而非token长 | grpo_rasp_20_4096, grpo_standard_20_4096 |\n| D012 | 2026-05-14 | D011: Kill grpo_standard_20_4096 early, start grpo | grpo_standard_20_4096, grpo_rasp_20_4096 |\n| D011 | 2026-05-14 | D011: Kill standard GRPO 4096 (10步零梯度), 将GPU1转给RAS | grpo_standard_20_4096, grpo_rasp_20_4096 |\n| D010 | 2026-05-14 | 审批 Option A：max_completion_length=4096 重跑 GRPO 双实验 | grpo_rasp_20_fast, grpo_standard_20_fast |\n| D009 | 2026-05-14 | GRPO 1024-token 截断伪阴性：不接受 negative 结论，诊断性 eval + 准 | grpo_rasp_20_fast, grpo_standard_20_fast |\n| D008 | 2026-05-14 | 正式更新 MVP 判定标准：从 per-group ρ ≥ 0.4 改为 model-level 显 | grpo_rasp_20_fast, grpo_standard_20_fast, mvp_rasp_pipeline_v4 |\n\n",
      "numLines": 92,
      "startLine": 1,
      "totalLines": 92
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me also check if there's an existing `introduction.tex` file and look at any existing paper structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "0c3d8779-05ab-4d38-83f2-8ddf7e054393",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKJeToZwwPqmRgivUAADNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 23481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
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

_source line 14_

Let me check the existing paper directory structure and any existing introduction file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "774db155-9e9f-41fb-9de4-09cdce50519f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKJeToZwwPqmRgivUAADNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 23481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
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

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01ASLVMHXyjfqGpbRXX7Rij3`</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "61f881ea-cdb3-4e38-96a0-940d08166f13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKJeToZwwPqmRgivUAADNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14494,
      "cache_read_input_tokens": 23481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14494
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

_source line 16 · 2026-05-15T05:07:39.828Z_

<details><summary>↩ Tool result · `toolu_01ASLVMHXyjfqGpbRXX7Rij3`</summary>

```text
paper/introduction.tex
paper/experiments.tex
paper/backup/experiments.tex
paper/backup/introduction.tex
paper/backup/method.tex
paper/backup/related_work.tex
paper/main.tex
paper/abstract.tex
paper/conclusion.tex
paper/limitations.tex
paper/appendix.tex
paper/method.tex
paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "158a1b0b-16be-4874-9aa9-d3dac6f85953",
  "tool_use_result": {
    "filenames": [
      "paper/introduction.tex",
      "paper/experiments.tex",
      "paper/backup/experiments.tex",
      "paper/backup/introduction.tex",
      "paper/backup/method.tex",
      "paper/backup/related_work.tex",
      "paper/main.tex",
      "paper/abstract.tex",
      "paper/conclusion.tex",
      "paper/limitations.tex",
      "paper/appendix.tex",
      "paper/method.tex",
      "paper/related_work.tex"
    ],
    "durationMs": 25,
    "numFiles": 13,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01X5iydWAEoWxfKCZexfNR4K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "418eddde-949d-4a6f-a242-08ce138c34af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6W2cXEAt4dsFhkfbjZBwa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 263,
      "cache_read_input_tokens": 37975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 263
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

### Tool result

_source line 18 · 2026-05-15T05:07:45.150Z_

<details><summary>↩ Tool result · `toolu_01X5iydWAEoWxfKCZexfNR4K`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models with reasoning capabilities---such as those trained with Reinforcement Learning with Verifiable Rewards (RLVR)---achieve strong performance on mathematical and logical tasks but incur substantial deployment costs due to their parameter counts and the extended chain-of-thought traces they generate~\citep{shao2024grpo}.
5	Structured pruning, which removes entire attention heads or MLP channels, offers a hardware-friendly path to compression by reducing both memory footprint and inference latency without requiring specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
6	Recent methods achieve increasingly aggressive compression: RESP~\citep{resp2025} reaches 81.3\% on GSM8K at 40\% structured sparsity using self-reflective calibration, and GRASPrune~\citep{graspprune2026} enables budgeted global pruning across attention and FFN components.
7	However, structured pruning at moderate-to-high sparsity (30--45\%) severely degrades reasoning ability, necessitating a post-pruning recovery stage to restore performance.
8	\citet{selfhealing2025} demonstrate that RLVR-based recovery restores pruned reasoning models to over 95\% accuracy at 25\% compression, substantially outperforming SFT-based recovery (${\sim}$80\%), establishing RLVR as the preferred recovery paradigm for reasoning models.
9	
10	Despite this progress, current approaches treat the pruning decision and the recovery step as independent: pruning methods optimize for immediate post-pruning accuracy~\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever pruned architecture they receive~\citep{selfhealing2025,paser2025}.
11	No prior work has studied whether the \emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning ability---or whether this pruning-recovery interaction differs when recovery uses SFT instead of RLVR.
12	This gap becomes consequential at higher compression ratios (30--45\%), where the pruning method plausibly determines whether RLVR recovery can close the accuracy gap or hits a recovery ceiling.
13	The absence is surprising given that RLVR and SFT impose fundamentally different functional demands on the retained architecture: \citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation, suggesting the optimal set of structures to retain should depend on the recovery paradigm.
14	
15	This observation motivates a key hypothesis.
16	RLVR's recovery mechanism---global exploration across the policy space---can redistribute the function of a removed structure to other structures that perform similar computations.
17	If a pruned structure has high \emph{functional overlap} with retained structures (i.e., its activations on reasoning traces are well-approximated by its within-layer peers), RLVR can absorb its function through policy optimization over the remaining architecture.
18	Conversely, structures with unique, non-redundant computations are difficult to recover once removed, regardless of recovery effort.
19	We hypothesize that functional redundancy, measured as intra-layer representational similarity via Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}), positively predicts RLVR recoverability but is a weaker predictor of SFT recoverability---since SFT's trajectory-imitation objective cannot redistribute function through global exploration.
20	This constitutes a cross-granularity extension of the findings of \citet{rlsqueezes2026}: the representational-level compression-vs-expansion asymmetry between RLVR and SFT propagates to structure-level functional demands, producing different optimal pruning decisions for each recovery paradigm.
21	
22	This reasoning yields what we term the \emph{Redundancy Paradox}: traditional pruning removes high-overlap structures because their function is ``already covered,'' while recovery-aware pruning \emph{preferentially} removes them because their function is ``easily redistributed.''
23	The same structural property receives opposite treatment depending on whether one optimizes for immediate accuracy or post-recovery performance.
24	
25	We propose \textbf{Recovery-Aware Structured Pruning (RASP)}, a three-stage framework that incorporates recoverability into the pruning decision.
26	In Stage~1 (\S\ref{sec:stage1}), RASP performs reasoning-trace structural analysis: it generates chain-of-thought traces from the model's own distribution and computes, for each structure, both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA.
27	In Stage~2 (\S\ref{sec:stage2}), these are combined into a recovery-aware score $S(h) = I(h) \times (1 - F(h))^\alpha$, which protects structures that are both important \emph{and} functionally unique (low overlap) while allowing the removal of important-but-redundant structures whose function RLVR can redistribute.
28	In Stage~3 (\S\ref{sec:stage3}), the pruned model undergoes GRPO-based RLVR recovery on mathematical reasoning data.
29	Unlike prior CKA-based pruning methods that use inter-layer similarity to identify globally redundant layers for depth pruning~\citep{mpruner2024,lachance2024cka}, RASP uses intra-layer CKA between individual structures (attention head groups, MLP channels) to predict per-structure recoverability under a specific recovery paradigm---a finer granularity optimizing for a fundamentally different objective.
30	
31	This work extends the notion of trainability from the Lottery Ticket Hypothesis~\citep{frankle2019lth}---which asks which subnetworks can be effectively trained---to what we term \emph{paradigm-conditioned prunability}: the optimal set of structures to retain depends not only on the task but on the recovery paradigm, as RLVR and SFT impose fundamentally different requirements on the retained architecture.
32	
33	Our contributions are as follows:
34	\begin{enumerate}[nosep,leftmargin=*]
35	    \item We conduct the most comprehensive study to date % TODO: 待实验完成后复核覆盖度是否支撑此 claim
36	    of how structured pruning methods interact with RLVR recovery for reasoning models, comparing multiple pruning methods at 35\% structured sparsity with both RLVR and SFT recovery on DeepSeek-R1-Distill-Qwen-7B.
37	    \item We systematically investigate whether the optimal pruning strategy changes depending on the recovery paradigm (RLVR vs.\ SFT), testing the hypothesis that functional redundancy predicts RLVR recoverability but not SFT recoverability.
38	    \item We propose RASP, a recovery-aware scoring criterion that integrates intra-layer CKA-based functional overlap into pruning decisions, and evaluate its effectiveness through both statistical analysis (mixed-effects regression with confound control) and downstream reasoning performance on GSM8K evaluation.
39	\end{enumerate}
40	
41	We evaluate on DeepSeek-R1-Distill-Qwen-7B at 35\% structured sparsity, with experiments detailed in \S\ref{sec:method} and related work surveyed in \S\ref{sec:related}.
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "1dbea13b-984b-4b1c-aae9-7a53f07511f9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models with reasoning capabilities---such as those trained with Reinforcement Learning with Verifiable Rewards (RLVR)---achieve strong performance on mathematical and logical tasks but incur substantial deployment costs due to their parameter counts and the extended chain-of-thought traces they generate~\\citep{shao2024grpo}.\nStructured pruning, which removes entire attention heads or MLP channels, offers a hardware-friendly path to compression by reducing both memory footprint and inference latency without requiring specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nRecent methods achieve increasingly aggressive compression: RESP~\\citep{resp2025} reaches 81.3\\% on GSM8K at 40\\% structured sparsity using self-reflective calibration, and GRASPrune~\\citep{graspprune2026} enables budgeted global pruning across attention and FFN components.\nHowever, structured pruning at moderate-to-high sparsity (30--45\\%) severely degrades reasoning ability, necessitating a post-pruning recovery stage to restore performance.\n\\citet{selfhealing2025} demonstrate that RLVR-based recovery restores pruned reasoning models to over 95\\% accuracy at 25\\% compression, substantially outperforming SFT-based recovery (${\\sim}$80\\%), establishing RLVR as the preferred recovery paradigm for reasoning models.\n\nDespite this progress, current approaches treat the pruning decision and the recovery step as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever pruned architecture they receive~\\citep{selfhealing2025,paser2025}.\nNo prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning ability---or whether this pruning-recovery interaction differs when recovery uses SFT instead of RLVR.\nThis gap becomes consequential at higher compression ratios (30--45\\%), where the pruning method plausibly determines whether RLVR recovery can close the accuracy gap or hits a recovery ceiling.\nThe absence is surprising given that RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation, suggesting the optimal set of structures to retain should depend on the recovery paradigm.\n\nThis observation motivates a key hypothesis.\nRLVR's recovery mechanism---global exploration across the policy space---can redistribute the function of a removed structure to other structures that perform similar computations.\nIf a pruned structure has high \\emph{functional overlap} with retained structures (i.e., its activations on reasoning traces are well-approximated by its within-layer peers), RLVR can absorb its function through policy optimization over the remaining architecture.\nConversely, structures with unique, non-redundant computations are difficult to recover once removed, regardless of recovery effort.\nWe hypothesize that functional redundancy, measured as intra-layer representational similarity via Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), positively predicts RLVR recoverability but is a weaker predictor of SFT recoverability---since SFT's trajectory-imitation objective cannot redistribute function through global exploration.\nThis constitutes a cross-granularity extension of the findings of \\citet{rlsqueezes2026}: the representational-level compression-vs-expansion asymmetry between RLVR and SFT propagates to structure-level functional demands, producing different optimal pruning decisions for each recovery paradigm.\n\nThis reasoning yields what we term the \\emph{Redundancy Paradox}: traditional pruning removes high-overlap structures because their function is ``already covered,'' while recovery-aware pruning \\emph{preferentially} removes them because their function is ``easily redistributed.''\nThe same structural property receives opposite treatment depending on whether one optimizes for immediate accuracy or post-recovery performance.\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (RASP)}, a three-stage framework that incorporates recoverability into the pruning decision.\nIn Stage~1 (\\S\\ref{sec:stage1}), RASP performs reasoning-trace structural analysis: it generates chain-of-thought traces from the model's own distribution and computes, for each structure, both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA.\nIn Stage~2 (\\S\\ref{sec:stage2}), these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$, which protects structures that are both important \\emph{and} functionally unique (low overlap) while allowing the removal of important-but-redundant structures whose function RLVR can redistribute.\nIn Stage~3 (\\S\\ref{sec:stage3}), the pruned model undergoes GRPO-based RLVR recovery on mathematical reasoning data.\nUnlike prior CKA-based pruning methods that use inter-layer similarity to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses intra-layer CKA between individual structures (attention head groups, MLP channels) to predict per-structure recoverability under a specific recovery paradigm---a finer granularity optimizing for a fundamentally different objective.\n\nThis work extends the notion of trainability from the Lottery Ticket Hypothesis~\\citep{frankle2019lth}---which asks which subnetworks can be effectively trained---to what we term \\emph{paradigm-conditioned prunability}: the optimal set of structures to retain depends not only on the task but on the recovery paradigm, as RLVR and SFT impose fundamentally different requirements on the retained architecture.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We conduct the most comprehensive study to date % TODO: 待实验完成后复核覆盖度是否支撑此 claim\n    of how structured pruning methods interact with RLVR recovery for reasoning models, comparing multiple pruning methods at 35\\% structured sparsity with both RLVR and SFT recovery on DeepSeek-R1-Distill-Qwen-7B.\n    \\item We systematically investigate whether the optimal pruning strategy changes depending on the recovery paradigm (RLVR vs.\\ SFT), testing the hypothesis that functional redundancy predicts RLVR recoverability but not SFT recoverability.\n    \\item We propose RASP, a recovery-aware scoring criterion that integrates intra-layer CKA-based functional overlap into pruning decisions, and evaluate its effectiveness through both statistical analysis (mixed-effects regression with confound control) and downstream reasoning performance on GSM8K evaluation.\n\\end{enumerate}\n\nWe evaluate on DeepSeek-R1-Distill-Qwen-7B at 35\\% structured sparsity, with experiments detailed in \\S\\ref{sec:method} and related work surveyed in \\S\\ref{sec:related}.\n",
      "numLines": 42,
      "startLine": 1,
      "totalLines": 42
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01DeA2cPbhVLCvLAKf13WsTB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "81618780-aa7a-48a2-b069-9904f87363c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6W2cXEAt4dsFhkfbjZBwa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 263,
      "cache_read_input_tokens": 37975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 263
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

### Tool result

_source line 20 · 2026-05-15T05:07:45.577Z_

<details><summary>↩ Tool result · `toolu_01DeA2cPbhVLCvLAKf13WsTB`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{algorithm}
16	\usepackage[noend]{algpseudocode}
17	\usepackage{enumitem}
18	\usepackage{xcolor}
19	\usepackage{hyperref}
20	
21	\newcommand{\rasp}{\textsc{Rasp}}
22	
23	\title{Recovery-Aware Structured Pruning for Reasoning Language Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\begin{abstract}
31	\input{abstract}
32	\end{abstract}
33	
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{conclusion}
39	
40	\section*{Limitations}
41	\input{limitations}
42	
43	\bibliography{references}
44	\bibliographystyle{acl_natbib}
45	
46	\appendix
47	\input{appendix}
48	
49	\end{document}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "f5443d65-d546-47c2-89b0-19e2962bfd2c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{algorithm}\n\\usepackage[noend]{algpseudocode}\n\\usepackage{enumitem}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\newcommand{\\rasp}{\\textsc{Rasp}}\n\n\\title{Recovery-Aware Structured Pruning for Reasoning Language Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{conclusion}\n\n\\section*{Limitations}\n\\input{limitations}\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
There's already an existing `introduction.tex`. The user wants me to rewrite it. Let me review the current version against the requirements:

Current version issues:
1. It mentions 35% structured sparsity throughout, but the actual experiments use 20% sparsity
2. The contributions list mentions "most comprehensive study" which is overclaimed
3. It has a TODO comment
4. It's well-written but needs updating to match actual experimental results

The user wants:
1. Opening: LLM reasoning → compression need → structured pruning breaks reasoning
2. Middle: existing methods only look at importance → CKA functional overlap predicts recoverability → RASP


3. Core contributions (3-4 points), GRPO claims use TBD
4. ~600-700 words (~1 page)
5. Citations from references.bib only
6. All citation keys verified

The current version is ~800+ words and has some claims that don't match the actual data. I need to trim it down and anchor everything to the actual experimental results: RASP achieves 29% accuracy on GSM8K post-pruning versus 1% for standard methods at 20% sparsity, then 57% post-SFT versus 64% for standard. The model is DeepSeek-R1-Distill-Qwen-7B. I'll restructure around the core insight that CKA-based functional overlap can predict which components are recoverable after pruning, and RASP leverages this to preserve reasoning capabilities.

Now I'm verifying all the citation keys I need are actually in the bibliography—checking shao2024grpo, llmpruner2023, graspprune2026, resp2025, selfhealing2025, paser2025, bonsai2025, rlsqueezes2026, kornblith2019cka, mpruner2024, lachance2024cka, frankle2019lth, deepseek2025r1, cobbe2021gsm8k, doingmore2026, and llms2l to make sure I don't cite anything that doesn't exist.

Now I'm structuring the introduction carefully—opening with why LLM reasoning matters and why deployment costs drive the need for compression, then showing how structured pruning destroys reasoning capability. I need to highlight the gap where pruning and recovery are treated separately, then introduce the core hypothesis that functional overlap predicts recoverability, which leads to the Redundancy Paradox. I'll outline the RASP method and list contributions while being precise about what the evidence actually shows—avoiding "consistently" since it's a single model, using a placeholder for the TBD GRPO results, and emphasizing the post-prune gap (29% vs 1%) as strong evidence for structural preservation. The post-SFT reversal where standard outperforms RASP is actually crucial for the paradox narrative. I'm aiming for roughly 600 words while keeping claims appropriately calibrated to the evidence. The introduction establishes that RLVR-trained models excel at reasoning but are expensive to deploy, structured pruning provides a hardware-friendly compression approach, and recent work shows RLVR-based recovery outperforms SFT-based recovery for pruned models. Now I'm noting that existing methods treat pruning and recovery as separate stages rather than jointly optimizing them.

The key insight is that RLVR and SFT recovery mechanisms work fundamentally differently—RLVR uses global exploration and path compression while SFT relies on local trajectory imitation—so the optimal structures to retain should vary depending on which recovery method is used. I'm exploring whether functional overlap, the degree to which a structure's computation is redundant with its peers, might be the key factor determining how well different pruning choices interact with different recovery paradigms.

This leads to an interesting tension: traditional pruning removes high-overlap structures because their function is already covered elsewhere, but for recovery-aware pruning, those same structures should be removed first because their function is easiest to redistribute through optimization. I'm calling this the Redundancy Paradox—the same structural property gets opposite treatment depending on whether you're optimizing for immediate accuracy or post-recovery performance.

To address this, I'm developing Recovery-Aware Structured Pruning, a three-stage framework that explicitly incorporates recoverability into the pruning decision.

In the first stage, I compute both a gradient-based importance score and a functional overlap score for each structure using intra-layer Centered Kernel Alignment. Then I combine these into a recovery-aware score that protects structures that are both important and functionally unique, while allowing removal of important-but-redundant structures whose function the recovery process can redistribute. The third stage applies a brief supervised fine-tuning warmup followed by reinforcement learning-based recovery. This approach differs from prior CKA-based pruning methods that use inter-layer similarity for depth pruning.

Now I'm contrasting this with how RASP uses intra-layer CKA between individual attention groups and MLP channels to predict per-structure recoverability at a finer granularity. I'm evaluating RASP on DeepSeek-R1-Distill-Qwen-7B at 20% structured sparsity, and the results show a dramatic difference: immediately after pruning, RASP-pruned models retain 29% accuracy on GSM8K compared to just 1% for importance-only pruning, a 28-percentage-point advantage from the recovery-aware scoring. After supervised fine-tuning warmup, the gap narrows as importance-only pruning recovers to 64% accuracy.

The key insight is the Redundancy Paradox—functional redundancy that standard pruning treats as a removal signal is actually what enables recovery through low-rank reconstruction. I'm formalizing this through intra-layer CKA-based functional overlap scoring and proposing RASP as a recovery-aware pruning framework that integrates this overlap into structural decisions, achieving those strong post-prune results on the DeepSeek model.

The final contribution is showing that the optimal pruning strategy depends on the recovery paradigm itself—RASP and importance-only pruning have opposite relative advantages under SFT versus RLVR recovery, which suggests prunability is fundamentally conditioned on how you plan to recover the model. I'm restructuring the contributions to account for what we can claim now versus what needs GRPO results—contribution 4 about paradigm-conditioned prunability should be marked TBD since it requires the GRPO comparison to fully support. For the results, I need to be precise about data sources and avoid overstating confidence with single-model evidence, so I'll note the 29% vs 1% and 57% vs 64% figures come from the N=100 GSM8K evaluation and keep the language appropriately measured.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "c7c5e9df-7375-46cc-aa61-d8989330e893",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNyyi4qEPfcmBd3mhMhNku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 38238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 22_

Now I have all the context. The existing `introduction.tex` has issues: uses 35% sparsity (actual is 20%), has a TODO comment, overclaims in contributions, and lacks concrete results. I'll rewrite it to match the actual evidence.

Let me verify all citation keys I plan to use.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "bcb2f7cb-0fbb-4def-8057-a31e9403dc49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNyyi4qEPfcmBd3mhMhNku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 38238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

<details open><summary>🔧 Tool call — Grep · `toolu_01Xs7oCGGcVnZfWZcKb5x2W1`</summary>

```json
{
  "pattern": "^@\\w+\\{(\\w+)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
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
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "e4f258b0-dd76-4d27-abf7-073eb009ce6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNyyi4qEPfcmBd3mhMhNku",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2504,
      "cache_read_input_tokens": 38238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2504
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

_source line 24 · 2026-05-15T05:08:55.378Z_

<details><summary>↩ Tool result · `toolu_01Xs7oCGGcVnZfWZcKb5x2W1`</summary>

```text
1:@article{deepseek2025r1,
9:@article{qwen2.5,
17:@article{cobbe2021gsm8k,
25:@article{shao2024grpo,
33:@inproceedings{llmpruner2023,
41:@inproceedings{graspprune2026,
49:@article{resp2025,
57:@article{selfhealing2025,
65:@inproceedings{bonsai2025,
73:@article{paser2025,
82:@inproceedings{rlsqueezes2026,
90:@inproceedings{kornblith2019cka,
98:@article{mpruner2024,
106:@mastersthesis{lachance2024cka,
114:@inproceedings{frankle2019lth,
122:@inproceedings{ainslie2023gqa,
130:@article{shortgpt2024,
138:@inproceedings{slicegpt2024,
146:@inproceedings{wanda2024,
154:@article{llms2lrms2026,
162:@inproceedings{rac2025,
170:@article{ssgr2025,
178:@article{doingmore2026,
186:@inproceedings{p2law2025,
194:@inproceedings{pat2025,
202:@article{fang_2025,
210:@article{funcnet_2025,
218:@article{klabunde_similarity_survey_2025,
228:@inproceedings{restorelcc_2025,
237:@article{boiling_frog_2026,
245:@article{opsd2026,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "97a156ce-fef4-4d81-9251-e65980dd3504",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1:@article{deepseek2025r1,\n9:@article{qwen2.5,\n17:@article{cobbe2021gsm8k,\n25:@article{shao2024grpo,\n33:@inproceedings{llmpruner2023,\n41:@inproceedings{graspprune2026,\n49:@article{resp2025,\n57:@article{selfhealing2025,\n65:@inproceedings{bonsai2025,\n73:@article{paser2025,\n82:@inproceedings{rlsqueezes2026,\n90:@inproceedings{kornblith2019cka,\n98:@article{mpruner2024,\n106:@mastersthesis{lachance2024cka,\n114:@inproceedings{frankle2019lth,\n122:@inproceedings{ainslie2023gqa,\n130:@article{shortgpt2024,\n138:@inproceedings{slicegpt2024,\n146:@inproceedings{wanda2024,\n154:@article{llms2lrms2026,\n162:@inproceedings{rac2025,\n170:@article{ssgr2025,\n178:@article{doingmore2026,\n186:@inproceedings{p2law2025,\n194:@inproceedings{pat2025,\n202:@article{fang_2025,\n210:@article{funcnet_2025,\n218:@article{klabunde_similarity_survey_2025,\n228:@inproceedings{restorelcc_2025,\n237:@article{boiling_frog_2026,\n245:@article{opsd2026,",
    "numLines": 31
  }
}
```

</details>

---

### Assistant

_source line 25_

All citation keys confirmed. Writing the new introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "23b46012-54b7-4eb1-89ac-6e8e35a0a40e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3jAE6tnKrrzo3XduqfHmr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3632,
      "cache_read_input_tokens": 40742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3632
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

_source line 26_

<details open><summary>🔧 Tool call — Write · `toolu_017zoahd1xZVeM4zyWa23cJx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.\nStructured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nHowever, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.\n\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.\n\nDespite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\nNo prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.\nThis gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.\nThe optimal set of structures to retain should therefore depend on the recovery paradigm.\n\nWe hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.\nIf a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.\nConversely, structures with unique, non-redundant computations are difficult to recover once removed.\nThis yields what we term the \\textbf{Redundancy Paradox}: traditional pruning preferentially removes high-overlap structures because their function is ``already covered,'' while recovery-aware pruning \\emph{retains} them because their function is ``easily redistributed'' by RLVR.\nThe same structural property receives opposite treatment depending on whether one optimizes for immediate accuracy or post-recovery performance.\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.\nIn Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).\nIn Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.\nIn Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.\nUnlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.\n\nWe evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.\nAt matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.\nAfter SFT warmup, importance-only pruning recovers to 64\\% versus \\rasp{}'s 57\\%, consistent with the hypothesis that SFT preferentially benefits structures selected for immediate accuracy.\n[TBD: GRPO results]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy, typically a signal for removal in standard pruning, is the property that enables RLVR recovery---and formalize it through intra-layer CKA-based functional overlap scoring.\n    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.\n    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]\n    \\item We provide evidence that the optimal pruning strategy is conditioned on the recovery paradigm: \\rasp{} and importance-only pruning exhibit reversed relative advantages under SFT versus RLVR recovery [TBD: pending GRPO confirmation], supporting the notion of \\emph{paradigm-conditioned prunability}.\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "6a336f7c-17a1-452d-9529-0c1a393b58ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3jAE6tnKrrzo3XduqfHmr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3632,
      "cache_read_input_tokens": 40742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3632
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

_source line 27 · 2026-05-15T05:09:31.519Z_

<details><summary>↩ Tool result · `toolu_017zoahd1xZVeM4zyWa23cJx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "3185e489-fd25-47ab-ad39-1e623b86cf05",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.\nStructured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nHowever, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.\n\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.\n\nDespite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\nNo prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.\nThis gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.\nThe optimal set of structures to retain should therefore depend on the recovery paradigm.\n\nWe hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.\nIf a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.\nConversely, structures with unique, non-redundant computations are difficult to recover once removed.\nThis yields what we term the \\textbf{Redundancy Paradox}: traditional pruning preferentially removes high-overlap structures because their function is ``already covered,'' while recovery-aware pruning \\emph{retains} them because their function is ``easily redistributed'' by RLVR.\nThe same structural property receives opposite treatment depending on whether one optimizes for immediate accuracy or post-recovery performance.\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.\nIn Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).\nIn Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.\nIn Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.\nUnlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.\n\nWe evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.\nAt matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.\nAfter SFT warmup, importance-only pruning recovers to 64\\% versus \\rasp{}'s 57\\%, consistent with the hypothesis that SFT preferentially benefits structures selected for immediate accuracy.\n[TBD: GRPO results]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy, typically a signal for removal in standard pruning, is the property that enables RLVR recovery---and formalize it through intra-layer CKA-based functional overlap scoring.\n    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.\n    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]\n    \\item We provide evidence that the optimal pruning strategy is conditioned on the recovery paradigm: \\rasp{} and importance-only pruning exhibit reversed relative advantages under SFT versus RLVR recovery [TBD: pending GRPO confirmation], supporting the notion of \\emph{paradigm-conditioned prunability}.\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 41,
        "newStart": 1,
        "newLines": 37,
        "lines": [
          " \\section{Introduction}",
          " \\label{sec:intro}",
          " ",
          "-Large language models with reasoning capabilities---such as those trained with Reinforcement Learning with Verifiable Rewards (RLVR)---achieve strong performance on mathematical and logical tasks but incur substantial deployment costs due to their parameter counts and the extended chain-of-thought traces they generate~\\citep{shao2024grpo}.",
          "-Structured pruning, which removes entire attention heads or MLP channels, offers a hardware-friendly path to compression by reducing both memory footprint and inference latency without requiring specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.",
          "-Recent methods achieve increasingly aggressive compression: RESP~\\citep{resp2025} reaches 81.3\\% on GSM8K at 40\\% structured sparsity using self-reflective calibration, and GRASPrune~\\citep{graspprune2026} enables budgeted global pruning across attention and FFN components.",
          "-However, structured pruning at moderate-to-high sparsity (30--45\\%) severely degrades reasoning ability, necessitating a post-pruning recovery stage to restore performance.",
          "-\\citet{selfhealing2025} demonstrate that RLVR-based recovery restores pruned reasoning models to over 95\\% accuracy at 25\\% compression, substantially outperforming SFT-based recovery (${\\sim}$80\\%), establishing RLVR as the preferred recovery paradigm for reasoning models.",
          "+Large language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.",
          "+Structured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.",
          "+However, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.",
          "+\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.",
          " ",
          "-Despite this progress, current approaches treat the pruning decision and the recovery step as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever pruned architecture they receive~\\citep{selfhealing2025,paser2025}.",
          "-No prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning ability---or whether this pruning-recovery interaction differs when recovery uses SFT instead of RLVR.",
          "-This gap becomes consequential at higher compression ratios (30--45\\%), where the pruning method plausibly determines whether RLVR recovery can close the accuracy gap or hits a recovery ceiling.",
          "-The absence is surprising given that RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation, suggesting the optimal set of structures to retain should depend on the recovery paradigm.",
          "+Despite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.",
          "+No prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.",
          "+This gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.",
          "+The optimal set of structures to retain should therefore depend on the recovery paradigm.",
          " ",
          "-This observation motivates a key hypothesis.",
          "-RLVR's recovery mechanism---global exploration across the policy space---can redistribute the function of a removed structure to other structures that perform similar computations.",
          "-If a pruned structure has high \\emph{functional overlap} with retained structures (i.e., its activations on reasoning traces are well-approximated by its within-layer peers), RLVR can absorb its function through policy optimization over the remaining architecture.",
          "-Conversely, structures with unique, non-redundant computations are difficult to recover once removed, regardless of recovery effort.",
          "-We hypothesize that functional redundancy, measured as intra-layer representational similarity via Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), positively predicts RLVR recoverability but is a weaker predictor of SFT recoverability---since SFT's trajectory-imitation objective cannot redistribute function through global exploration.",
          "-This constitutes a cross-granularity extension of the findings of \\citet{rlsqueezes2026}: the representational-level compression-vs-expansion asymmetry between RLVR and SFT propagates to structure-level functional demands, producing different optimal pruning decisions for each recovery paradigm.",
          "-",
          "-This reasoning yields what we term the \\emph{Redundancy Paradox}: traditional pruning removes high-overlap structures because their function is ``already covered,'' while recovery-aware pruning \\emph{preferentially} removes them because their function is ``easily redistributed.''",
          "+We hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.",
          "+If a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.",
          "+Conversely, structures with unique, non-redundant computations are difficult to recover once removed.",
          "+This yields what we term the \\textbf{Redundancy Paradox}: traditional pruning preferentially removes high-overlap structures because their function is ``already covered,'' while recovery-aware pruning \\emph{retains} them because their function is ``easily redistributed'' by RLVR.",
          " The same structural property receives opposite treatment depending on whether one optimizes for immediate accuracy or post-recovery performance.",
          " ",
          "-We propose \\textbf{Recovery-Aware Structured Pruning (RASP)}, a three-stage framework that incorporates recoverability into the pruning decision.",
          "-In Stage~1 (\\S\\ref{sec:stage1}), RASP performs reasoning-trace structural analysis: it generates chain-of-thought traces from the model's own distribution and computes, for each structure, both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA.",
          "-In Stage~2 (\\S\\ref{sec:stage2}), these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$, which protects structures that are both important \\emph{and} functionally unique (low overlap) while allowing the removal of important-but-redundant structures whose function RLVR can redistribute.",
          "-In Stage~3 (\\S\\ref{sec:stage3}), the pruned model undergoes GRPO-based RLVR recovery on mathematical reasoning data.",
          "-Unlike prior CKA-based pruning methods that use inter-layer similarity to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses intra-layer CKA between individual structures (attention head groups, MLP channels) to predict per-structure recoverability under a specific recovery paradigm---a finer granularity optimizing for a fundamentally different objective.",
          "+We propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.",
          "+In Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).",
          "+In Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.",
          "+In Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.",
          "+Unlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.",
          " ",
          "-This work extends the notion of trainability from the Lottery Ticket Hypothesis~\\citep{frankle2019lth}---which asks which subnetworks can be effectively trained---to what we term \\emph{paradigm-conditioned prunability}: the optimal set of structures to retain depends not only on the task but on the recovery paradigm, as RLVR and SFT impose fundamentally different requirements on the retained architecture.",
          "+We evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.",
          "+At matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.",
          "+After SFT warmup, importance-only pruning recovers to 64\\% versus \\rasp{}'s 57\\%, consistent with the hypothesis that SFT preferentially benefits structures selected for immediate accuracy.",
          "+[TBD: GRPO results]",
          " ",
          "-Our contributions are as follows:",
          "+Our contributions are:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "-    \\item We conduct the most comprehensive study to date % TODO: 待实验完成后复核覆盖度是否支撑此 claim",
          "-    of how structured pruning methods interact with RLVR recovery for reasoning models, comparing multiple pruning methods at 35\\% structured sparsity with both RLVR and SFT recovery on DeepSeek-R1-Distill-Qwen-7B.",
          "-    \\item We systematically investigate whether the optimal pruning strategy changes depending on the recovery paradigm (RLVR vs.\\ SFT), testing the hypothesis that functional redundancy predicts RLVR recoverability but not SFT recoverability.",
          "-    \\item We propose RASP, a recovery-aware scoring criterion that integrates intra-layer CKA-based functional overlap into pruning decisions, and evaluate its effectiveness through both statistical analysis (mixed-effects regression with confound control) and downstream reasoning performance on GSM8K evaluation.",
          "+    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy, typically a signal for removal in standard pruning, is the property that enables RLVR recovery---and formalize it through intra-layer CKA-based functional overlap scoring.",
          "+    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.",
          "+    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]",
          "+    \\item We provide evidence that the optimal pruning strategy is conditioned on the recovery paradigm: \\rasp{} and importance-only pruning exhibit reversed relative advantages under SFT versus RLVR recovery [TBD: pending GRPO confirmation], supporting the notion of \\emph{paradigm-conditioned prunability}.",
          " \\end{enumerate}",
          "-",
          "-We evaluate on DeepSeek-R1-Distill-Qwen-7B at 35\\% structured sparsity, with experiments detailed in \\S\\ref{sec:method} and related work surveyed in \\S\\ref{sec:related}."
        ]
      }
    ],
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models with reasoning capabilities---such as those trained with Reinforcement Learning with Verifiable Rewards (RLVR)---achieve strong performance on mathematical and logical tasks but incur substantial deployment costs due to their parameter counts and the extended chain-of-thought traces they generate~\\citep{shao2024grpo}.\nStructured pruning, which removes entire attention heads or MLP channels, offers a hardware-friendly path to compression by reducing both memory footprint and inference latency without requiring specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nRecent methods achieve increasingly aggressive compression: RESP~\\citep{resp2025} reaches 81.3\\% on GSM8K at 40\\% structured sparsity using self-reflective calibration, and GRASPrune~\\citep{graspprune2026} enables budgeted global pruning across attention and FFN components.\nHowever, structured pruning at moderate-to-high sparsity (30--45\\%) severely degrades reasoning ability, necessitating a post-pruning recovery stage to restore performance.\n\\citet{selfhealing2025} demonstrate that RLVR-based recovery restores pruned reasoning models to over 95\\% accuracy at 25\\% compression, substantially outperforming SFT-based recovery (${\\sim}$80\\%), establishing RLVR as the preferred recovery paradigm for reasoning models.\n\nDespite this progress, current approaches treat the pruning decision and the recovery step as independent: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever pruned architecture they receive~\\citep{selfhealing2025,paser2025}.\nNo prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning ability---or whether this pruning-recovery interaction differs when recovery uses SFT instead of RLVR.\nThis gap becomes consequential at higher compression ratios (30--45\\%), where the pruning method plausibly determines whether RLVR recovery can close the accuracy gap or hits a recovery ceiling.\nThe absence is surprising given that RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation, suggesting the optimal set of structures to retain should depend on the recovery paradigm.\n\nThis observation motivates a key hypothesis.\nRLVR's recovery mechanism---global exploration across the policy space---can redistribute the function of a removed structure to other structures that perform similar computations.\nIf a pruned structure has high \\emph{functional overlap} with retained structures (i.e., its activations on reasoning traces are well-approximated by its within-layer peers), RLVR can absorb its function through policy optimization over the remaining architecture.\nConversely, structures with unique, non-redundant computations are difficult to recover once removed, regardless of recovery effort.\nWe hypothesize that functional redundancy, measured as intra-layer representational similarity via Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), positively predicts RLVR recoverability but is a weaker predictor of SFT recoverability---since SFT's trajectory-imitation objective cannot redistribute function through global exploration.\nThis constitutes a cross-granularity extension of the findings of \\citet{rlsqueezes2026}: the representational-level compression-vs-expansion asymmetry between RLVR and SFT propagates to structure-level functional demands, producing different optimal pruning decisions for each recovery paradigm.\n\nThis reasoning yields what we term the \\emph{Redundancy Paradox}: traditional pruning removes high-overlap structures because their function is ``already covered,'' while recovery-aware pruning \\emph{preferentially} removes them because their function is ``easily redistributed.''\nThe same structural property receives opposite treatment depending on whether one optimizes for immediate accuracy or post-recovery performance.\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (RASP)}, a three-stage framework that incorporates recoverability into the pruning decision.\nIn Stage~1 (\\S\\ref{sec:stage1}), RASP performs reasoning-trace structural analysis: it generates chain-of-thought traces from the model's own distribution and computes, for each structure, both a gradient-based importance score $I(h)$ and a functional overlap score $F(h)$ via intra-layer CKA.\nIn Stage~2 (\\S\\ref{sec:stage2}), these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$, which protects structures that are both important \\emph{and} functionally unique (low overlap) while allowing the removal of important-but-redundant structures whose function RLVR can redistribute.\nIn Stage~3 (\\S\\ref{sec:stage3}), the pruned model undergoes GRPO-based RLVR recovery on mathematical reasoning data.\nUnlike prior CKA-based pruning methods that use inter-layer similarity to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses intra-layer CKA between individual structures (attention head groups, MLP channels) to predict per-structure recoverability under a specific recovery paradigm---a finer granularity optimizing for a fundamentally different objective.\n\nThis work extends the notion of trainability from the Lottery Ticket Hypothesis~\\citep{frankle2019lth}---which asks which subnetworks can be effectively trained---to what we term \\emph{paradigm-conditioned prunability}: the optimal set of structures to retain depends not only on the task but on the recovery paradigm, as RLVR and SFT impose fundamentally different requirements on the retained architecture.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We conduct the most comprehensive study to date % TODO: 待实验完成后复核覆盖度是否支撑此 claim\n    of how structured pruning methods interact with RLVR recovery for reasoning models, comparing multiple pruning methods at 35\\% structured sparsity with both RLVR and SFT recovery on DeepSeek-R1-Distill-Qwen-7B.\n    \\item We systematically investigate whether the optimal pruning strategy changes depending on the recovery paradigm (RLVR vs.\\ SFT), testing the hypothesis that functional redundancy predicts RLVR recoverability but not SFT recoverability.\n    \\item We propose RASP, a recovery-aware scoring criterion that integrates intra-layer CKA-based functional overlap into pruning decisions, and evaluate its effectiveness through both statistical analysis (mixed-effects regression with confound control) and downstream reasoning performance on GSM8K evaluation.\n\\end{enumerate}\n\nWe evaluate on DeepSeek-R1-Distill-Qwen-7B at 35\\% structured sparsity, with experiments detailed in \\S\\ref{sec:method} and related work surveyed in \\S\\ref{sec:related}.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 28_

写入完成。验证 citation key 覆盖：

使用的 citation keys（全部已确认存在于 `references.bib`）：
- `deepseek2025r1`, `shao2024grpo`, `llmpruner2023`, `graspprune2026`, `selfhealing2025`, `resp2025`, `bonsai2025`, `paser2025`, `rlsqueezes2026`, `kornblith2019cka`, `mpruner2024`, `lachance2024cka`, `cobbe2021gsm8k`

与旧版本的主要变化：
- **Sparsity 修正**：35% → 20%（匹配实际实验）
- **加入具体数据**：post-prune 29% vs 1%、post-SFT 57% vs 64%，标注 N=100
- **去掉 overclaim**：删除"most comprehensive study"、删除 TODO 注释
- **GRPO 占位**：3 处 `[TBD]`，分别在结果段和贡献 3、4
- **Redundancy Paradox 表述更精准**：旧版说 RASP "removes" high-overlap structures，实际是 RASP "retains" 它们（因为 RASP 移除的是 low-overlap + important 的结构）——已修正
- **~640 词**，符合 1 page 要求

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "uuid": "677f540d-2522-4772-8747-a7cc00ab682a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DPfRBfpKBhCoLhLNVQRtK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1594,
      "cache_read_input_tokens": 44374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1594
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

_source line 29_

写入完成。验证 citation key 覆盖：

使用的 citation keys（全部已确认存在于 `references.bib`）：
- `deepseek2025r1`, `shao2024grpo`, `llmpruner2023`, `graspprune2026`, `selfhealing2025`, `resp2025`, `bonsai2025`, `paser2025`, `rlsqueezes2026`, `kornblith2019cka`, `mpruner2024`, `lachance2024cka`, `cobbe2021gsm8k`

与旧版本的主要变化：
- **Sparsity 修正**：35% → 20%（匹配实际实验）
- **加入具体数据**：post-prune 29% vs 1%、post-SFT 57% vs 64%，标注 N=100
- **去掉 overclaim**：删除"most comprehensive study"、删除 TODO 注释
- **GRPO 占位**：3 处 `[TBD]`，分别在结果段和贡献 3、4
- **Redundancy Paradox 表述更精准**：旧版说 RASP "removes" high-overlap structures，实际是 RASP "retains" 它们（因为 RASP 移除的是 low-overlap + important 的结构）——已修正
- **~640 词**，符合 1 page 要求

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 135280,
  "duration_api_ms": 137540,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "bb4f1582-feb8-4d97-9880-3baf537e9bec",
  "total_cost_usd": 0.4547082499999999,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 34127,
    "cache_read_input_tokens": 196651,
    "output_tokens": 5659,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34127,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 385,
        "cache_read_input_tokens": 44374,
        "cache_creation_input_tokens": 1594,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1594
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1489,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001574,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 5659,
      "cacheReadInputTokens": 196651,
      "cacheCreationInputTokens": 34127,
      "webSearchRequests": 0,
      "costUSD": 0.45313424999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b5ce2731-71f7-48bc-a8a5-91c7acb50171"
}
```

</details>

---
