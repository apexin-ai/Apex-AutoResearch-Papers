# paper conclusion abstract

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_conclusion_abstract_20260514T091325.log`
- **Structured JSON:** [`d628f7a29ed87f4bf4a8.json`](../../sessions/d6/d628f7a29ed87f4bf4a8.json)

## Before a recorded user message

67 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
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
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "5849d1bb-fcfb-49e2-8a59-3aeb63321610",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778757000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "60716f6b-3f31-4ae7-a4f4-c2bc4183ed8d",
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81"
}
```

---

### Assistant

_source line 4_

我先读取已有的 tex 文件了解格式和风格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "495d51f1-22c7-467a-8158-58f6b3239515",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbZbehyVQCtUVbjtxrAHs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11818,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11818
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

<details open><summary>🔧 Tool call — Read · `toolu_014ozZ9pXiBKbJDAs8Mext21`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "2d12d524-b117-4a14-8d62-b7cbe0a0d1a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbZbehyVQCtUVbjtxrAHs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11818,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11818
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

_source line 6 · 2026-05-14T09:13:49.622Z_

<details><summary>↩ Tool result · `toolu_014ozZ9pXiBKbJDAs8Mext21`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\subsection{Models}
5	\label{sec:models}
6	
7	We conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):
8	
9	\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \texttt{&lt;think>}$\cdots$\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.
10	
11	\paragraph{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.
12	
13	Both models are loaded in \texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\sim}$8\% of logit positions. Switching to \texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}
14	
15	
16	\subsection{Dataset}
17	\label{sec:dataset}
18	
19	We evaluate on a 50-problem stratified subset of the MATH-500 benchmark \cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048) to eliminate sampling variance.
20	
21	
22	\subsection{Compound Sparsity Configuration}
23	\label{sec:sparsity-config}
24	
25	We apply \emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$, spanning from mild to aggressive compression.
26	
27	\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\emph{dense}---no intervention; (ii)~\emph{attn-only}---head pruning without KV eviction; (iii)~\emph{kv-only}---KV eviction without head pruning; and (iv)~\emph{both}---simultaneous head pruning and KV eviction.
28	
29	\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:
30	
31	\begin{itemize}[nosep,leftmargin=*]
32	\item \textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:
33	\begin{equation}
34	\label{eq:importance}
35	    \alpha_j = \frac{\sum_{i,h} a_{i,h,j}}{\texttt{seq\_len} - j}, \quad j \in \{1, \dots, T\},
36	\end{equation}
37	where $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \cdot s$ positions with the lowest normalized scores are evicted.
38	
39	During masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\infty \times 0 = \text{NaN}$ are handled via selective replacement (\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.
40	
41	\item \textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \texttt{torch.randperm} rather than by importance.
42	\end{itemize}
43	
44	\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\mathbf{A}_\ell \in \mathbb{R}^{H \times T \times T}$ per layer $\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.
45	
46	
47	\subsection{Phase Segmentation}
48	\label{sec:phase-seg}
49	
50	We segment each generated sequence into three \emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \times \max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \emph{mid-sparsity}, and \emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\texttt{min\_phase\_length}=10$ tokens are merged into adjacent phases to suppress noise.
51	
52	
53	\subsection{Metrics}
54	\label{sec:metrics}
55	
56	\paragraph{Perplexity.} For each sparsity condition $c \in \{d, a, k, b\}$ and each phase, we compute segment-level perplexity as
57	$\text{PPL}_c = \exp\!\bigl(\tfrac{1}{|I|}\sum_{i \in I} \mathcal{L}_c(x_i)\bigr)$,
58	where $I$ is the set of token indices belonging to the phase and $\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.
59	
60	\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:
61	\begin{equation}
62	\label{eq:ii}
63	    \mathrm{II} = \frac{\text{PPL}_b}{\text{PPL}_d} - \frac{\text{PPL}_a}{\text{PPL}_d} - \frac{\text{PPL}_k}{\text{PPL}_d} + 1.
64	\end{equation}
65	When $\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\mathrm{II} = 0$ indicates additive (independent) degradation.
66	
67	\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:
68	\begin{equation}
69	\label{eq:gradient}
70	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
71	\end{equation}
72	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.
73	
74	
75	\subsection{Statistical Analysis}
76	\label{sec:stats}
77	
78	All confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \cite{efron1993bootstrap}.
79	
80	\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\% percentile confidence interval for the population mean II.
81	
82	\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.
83	
84	\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.
85	
86	All tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\footnote{Experiments were conducted on a server with 4$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\,GB GPUs, with one model--sparsity configuration per GPU.}
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "1b47ca3e-53ef-4a78-b7f6-d84cd0af1204",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):\n\n\\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \\cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \\texttt{&lt;think>}$\\cdots$\\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.\n\n\\paragraph{Qwen2.5-7B-Instruct} \\cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.\n\nBoth models are loaded in \\texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\\sim}$8\\% of logit positions. Switching to \\texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of the MATH-500 benchmark \\cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048) to eliminate sampling variance.\n\n\n\\subsection{Compound Sparsity Configuration}\n\\label{sec:sparsity-config}\n\nWe apply \\emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, spanning from mild to aggressive compression.\n\n\\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\\emph{dense}---no intervention; (ii)~\\emph{attn-only}---head pruning without KV eviction; (iii)~\\emph{kv-only}---KV eviction without head pruning; and (iv)~\\emph{both}---simultaneous head pruning and KV eviction.\n\n\\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:\n\\begin{equation}\n\\label{eq:importance}\n    \\alpha_j = \\frac{\\sum_{i,h} a_{i,h,j}}{\\texttt{seq\\_len} - j}, \\quad j \\in \\{1, \\dots, T\\},\n\\end{equation}\nwhere $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \\cdot s$ positions with the lowest normalized scores are evicted.\n\nDuring masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\\infty \\times 0 = \\text{NaN}$ are handled via selective replacement (\\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.\n\n\\item \\textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \\texttt{torch.randperm} rather than by importance.\n\\end{itemize}\n\n\\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\\mathbf{A}_\\ell \\in \\mathbb{R}^{H \\times T \\times T}$ per layer $\\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.\n\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-seg}\n\nWe segment each generated sequence into three \\emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \\times \\max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \\emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \\emph{mid-sparsity}, and \\emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\\texttt{min\\_phase\\_length}=10$ tokens are merged into adjacent phases to suppress noise.\n\n\n\\subsection{Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Perplexity.} For each sparsity condition $c \\in \\{d, a, k, b\\}$ and each phase, we compute segment-level perplexity as\n$\\text{PPL}_c = \\exp\\!\\bigl(\\tfrac{1}{|I|}\\sum_{i \\in I} \\mathcal{L}_c(x_i)\\bigr)$,\nwhere $I$ is the set of token indices belonging to the phase and $\\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.\n\n\\paragraph{Interaction Index.} The interaction index quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions:\n\\begin{equation}\n\\label{eq:ii}\n    \\mathrm{II} = \\frac{\\text{PPL}_b}{\\text{PPL}_d} - \\frac{\\text{PPL}_a}{\\text{PPL}_d} - \\frac{\\text{PPL}_k}{\\text{PPL}_d} + 1.\n\\end{equation}\nWhen $\\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\\mathrm{II} = 0$ indicates additive (independent) degradation.\n\n\\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we define the severity gradient:\n\\begin{equation}\n\\label{eq:gradient}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.\n\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nAll confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \\cite{efron1993bootstrap}.\n\n\\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\\% percentile confidence interval for the population mean II.\n\n\\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.\n\n\\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.\n\nAll tests yield $p < 0.0001$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\\footnote{Experiments were conducted on a server with 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs, with one model--sparsity configuration per GPU.}\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01UXezCbW6YmKGHxDT6AZg3S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "c8ac22b6-3afc-4c84-83b7-8e8294df3b1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbZbehyVQCtUVbjtxrAHs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11818,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11818
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

_source line 8 · 2026-05-14T09:13:50.375Z_

<details><summary>↩ Tool result · `toolu_01UXezCbW6YmKGHxDT6AZg3S`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Compound and Joint Compression}
5	
6	Combining multiple compression axes produces non-additive errors.
7	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.
8	\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.
9	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.
10	The order of compression stages is itself consequential: \cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\to$KD$\to$Q strictly preferable.
11	At a more fundamental level, \cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.
12	On the structural side, GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.
13	These works establish that compound interaction produces non-additive errors, but share an implicit assumption: the interaction magnitude is either constant across the generation process or varies only by task---not by reasoning phase or eviction strategy.
14	How compound severity shifts across reasoning phases within a single generation remains unexamined.
15	
16	\subsection{KV Cache Eviction}
17	
18	Most eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.
19	Ada-KV~\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.
20	SnapKV~\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.
21	\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.
22	\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.
23	\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.
24	\cite{mustafar-neurips2025} achieve 70\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.
25	RetentiveKV~\cite{retentivekv-2026} identifies \emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.
26	\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.
27	A recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.
28	
29	\subsection{Phase-Aware Inference}
30	
31	Several concurrent works introduce phase-awareness into LLM inference.
32	ThinKV~\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.
33	\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.
34	\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.
35	\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.
36	\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.
37	
38	These works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.
39	Our work bridges this gap by quantifying how compound sparsity severity varies across reasoning phases and how this variation is modulated by eviction strategy---specifically, the phase-dependent severity gradient that distinguishes importance-based eviction from random baselines in compound settings.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "ca3c7581-2830-4493-8676-8987665f45c6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Compound and Joint Compression}\n\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.\n\\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.\n\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.\nThe order of compression stages is itself consequential: \\cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\\to$KD$\\to$Q strictly preferable.\nAt a more fundamental level, \\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.\nOn the structural side, GRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.\nThese works establish that compound interaction produces non-additive errors, but share an implicit assumption: the interaction magnitude is either constant across the generation process or varies only by task---not by reasoning phase or eviction strategy.\nHow compound severity shifts across reasoning phases within a single generation remains unexamined.\n\n\\subsection{KV Cache Eviction}\n\nMost eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.\nAda-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\nSnapKV~\\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.\n\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.\n\\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.\n\\cite{mustafar-neurips2025} achieve 70\\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.\nRetentiveKV~\\cite{retentivekv-2026} identifies \\emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.\n\\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.\nA recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.\n\n\\subsection{Phase-Aware Inference}\n\nSeveral concurrent works introduce phase-awareness into LLM inference.\nThinKV~\\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.\n\\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.\n\\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.\n\\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.\n\\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.\n\nThese works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.\nOur work bridges this gap by quantifying how compound sparsity severity varies across reasoning phases and how this variation is modulated by eviction strategy---specifically, the phase-dependent severity gradient that distinguishes importance-based eviction from random baselines in compound settings.\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01ANVBUAxSo4F6brE3TTWbQn`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "7ce4c76b-befa-4611-b478-7518e0c03cef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbZbehyVQCtUVbjtxrAHs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11818,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11818
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

_source line 10 · 2026-05-14T09:13:50.777Z_

<details><summary>↩ Tool result · `toolu_01ANVBUAxSo4F6brE3TTWbQn`</summary>

```text
artifacts/_project/paper/related_work_46fb53.tex
artifacts/_project/paper/background_fc6d1d.tex
artifacts/_project/paper/methodology_4cc5f3.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/results_5_1.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "8ee60f3a-23a4-4076-abe2-2a608be4143f",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work_46fb53.tex",
      "artifacts/_project/paper/background_fc6d1d.tex",
      "artifacts/_project/paper/methodology_4cc5f3.tex",
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/results_5_1.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/introduction.tex"
    ],
    "durationMs": 46,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Let me also read the introduction, results, analysis, and discussion sections to understand the full paper context and style before writing the conclusion and abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "c02595fd-ed70-4be8-85ac-30ed1312cfd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6WAE5W2W9C1F5SeBFV4cX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4501,
      "cache_read_input_tokens": 23659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4501
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

_source line 12_

Let me read the remaining sections for full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "23bb874d-04de-47cb-9a9f-22c6e0a8e6fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6WAE5W2W9C1F5SeBFV4cX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4501,
      "cache_read_input_tokens": 23659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4501
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_011z8tXkqVrkYpB75DtHiazx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "7552b8ef-436b-4f7a-89bd-3a3c2767424b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6WAE5W2W9C1F5SeBFV4cX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4501,
      "cache_read_input_tokens": 23659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4501
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

_source line 14 · 2026-05-14T09:13:56.419Z_

<details><summary>↩ Tool result · `toolu_011z8tXkqVrkYpB75DtHiazx`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \cite{kwon2023vllm, pope2023efficiently}.
5	Two complementary responses have emerged: \emph{attention head pruning}, which removes structurally redundant heads \cite{voita2019heads, michel2019sixteen}, and \emph{KV cache eviction}, which discards low-importance token positions from the cache \cite{snapkv-neurips2024, adakv-neurips2025}.
6	Deploying both simultaneously---\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \cite{spark-aaai2026, slim-icml2025}.
7	
8	Prior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \cite{spark-aaai2026, unicomp-2026}.
9	This assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
10	If compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.
11	
12	We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.
13	Our central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).
14	This \emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d{=}0.44$ (small) to $d{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d \geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ does not reach significance ($d{=}0.28$, CI spanning zero).
16	Critically, random eviction produces no such gradient: all four sparsity levels fail to exhibit a significant phase difference, confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.
17	
18	We propose \emph{entropy-discrimination collapse} as an explanatory mechanism.
19	Head pruning forces surviving heads to redistribute attention mass, increasing attention entropy.
20	In low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.
21	Importance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.
22	In high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.
23	Random eviction is immune to this mechanism because its decisions are independent of attention patterns.
24	
25	Our contributions are as follows:
26	\begin{enumerate}[nosep,leftmargin=*]
27	    \item We identify a \textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:experiments}).
28	    \item We show that this severity gradient \textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \geq 0.20$) across two models with different training regimes (distillation vs.\ instruction tuning), establishing robustness within the Qwen2 architecture family (\S\ref{sec:experiments}).
29	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\S\ref{sec:analysis}).
30	\end{enumerate}
31	
32	These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.
33	The remainder of this paper is organized as follows: \S\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \S\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \S\ref{sec:experimental-setup} describes our experimental setup; \S\ref{sec:experiments} presents the main results; \S\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \S\ref{sec:discussion} discusses implications and limitations.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "e9abe0ff-50c7-4a7e-b30e-5e1c9e1df475",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon2023vllm, pope2023efficiently}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita2019heads, michel2019sixteen}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d{=}0.44$ (small) to $d{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ does not reach significance ($d{=}0.28$, CI spanning zero).\nCritically, random eviction produces no such gradient: all four sparsity levels fail to exhibit a significant phase difference, confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:experiments}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:experiments}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:experiments} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01TBXMf1BnJGN2p3PqKjHhLP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "547b467e-3f2c-4e72-bae5-56b6263defee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6WAE5W2W9C1F5SeBFV4cX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4501,
      "cache_read_input_tokens": 23659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4501
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

_source line 16 · 2026-05-14T09:13:56.904Z_

<details><summary>↩ Tool result · `toolu_01TBXMf1BnJGN2p3PqKjHhLP`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	We present our empirical findings in five parts: strategy-dependent compound severity (\S\ref{sec:strategy-severity}), phase-modulated amplification (\S\ref{sec:phase-amplification}), the phase-strategy crossover (\S\ref{sec:crossover}), cross-model replication (\S\ref{sec:cross-model}), and statistical validation (\S\ref{sec:stat-validation}).
6	
7	
8	\subsection{Experimental Overview}
9	\label{sec:exp-overview}
10	
11	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\S\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$. We compare importance-based and random eviction strategies (\S\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\S\ref{sec:phase-seg}). The interaction index (II, Eq.~\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\ref{eq:gradient}) captures phase-dependent amplification.
12	Models are evaluated in \texttt{bfloat16} precision (\S\ref{sec:experimental-setup}). Full experimental details appear therein.
13	
14	
15	\subsection{Strategy-Dependent Severity (C1)}
16	\label{sec:strategy-severity}
17	
18	The aggregate interaction index reveals a stark dependence on eviction strategy. Table~\ref{tab:aggregate-ii} reports the problem-level mean II across all 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: mean II increases from \placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s015} at $s{=}0.15$ to \placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s030} at $s{=}0.30$. Under random eviction, compound interaction shows no systematic phase modulation across sparsity levels, with mean II near \placeholder{exp_id: deepseek_bf16_random, metric: mean_II_range}.
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\caption{Aggregate interaction index (II) by eviction strategy and sparsity level. Values are problem-level means across 50 MATH-500 problems on DeepSeek-R1-Distill-Qwen-7B.}
24	\label{tab:aggregate-ii}
25	\begin{tabular}{@{}lcccc@{}}
26	\toprule
27	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
28	\midrule
29	Importance & \placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s015} & \placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s020} & \placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s025} & \placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s030} \\
30	Random     & \placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s015} & \placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s020} & \placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s025} & \placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s030} \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	This strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.
36	
37	
38	\subsection{Phase-Modulated Amplification (C2)}
39	\label{sec:phase-amplification}
40	
41	Decomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \S\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.
42	
43	Under importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from \placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} at $s{=}0.15$ to \placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} at $s{=}0.30$, spanning a \placeholder{exp_id: deepseek_bf16_importance, metric: G_min}--\placeholder{exp_id: deepseek_bf16_importance, metric: G_max}$\times$ range. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences comparatively mild interaction. Under random eviction, the gradient remains near unity ($G \approx$ \placeholder{exp_id: deepseek_bf16_random, metric: G_range}) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring.
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. The severity gradient $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$ quantifies phase-dependent amplification of compound interaction.}
49	\label{tab:main-results}
50	\begin{tabular}{@{}llccccc@{}}
51	\toprule
52	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $G$ & 95\% CI \\
53	\midrule
54	0.15 & Importance & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s015} & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_mid_s015} & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s015} & \placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} & [\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s015}, \placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s015}] \\
55	0.15 & Random     & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s015} & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_mid_s015} & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s015} & \placeholder{exp_id: deepseek_bf16_random, metric: G_s015} & [\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s015}, \placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s015}] \\
56	\addlinespace
57	0.20 & Importance & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s020} & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_mid_s020} & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s020} & \placeholder{exp_id: deepseek_bf16_importance, metric: G_s020} & [\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s020}, \placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s020}] \\
58	0.20 & Random     & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s020} & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_mid_s020} & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s020} & \placeholder{exp_id: deepseek_bf16_random, metric: G_s020} & [\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s020}, \placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s020}] \\
59	\addlinespace
60	0.25 & Importance & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s025} & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_mid_s025} & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s025} & \placeholder{exp_id: deepseek_bf16_importance, metric: G_s025} & [\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s025}, \placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s025}] \\
61	0.25 & Random     & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s025} & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_mid_s025} & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s025} & \placeholder{exp_id: deepseek_bf16_random, metric: G_s025} & [\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s025}, \placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s025}] \\
62	\addlinespace
63	0.30 & Importance & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s030} & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_mid_s030} & \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s030} & \placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} & [\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s030}, \placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s030}] \\
64	0.30 & Random     & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s030} & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_mid_s030} & \placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s030} & \placeholder{exp_id: deepseek_bf16_random, metric: G_s030} & [\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s030}, \placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s030}] \\
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
69	The gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s015_s020}$\times$, \placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s020_s025}$\times$, and \placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s025_s030}$\times$---a decreasing growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. Figure~\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.
70	
71	\begin{figure}[t]
72	\centering
73	\includegraphics[width=\columnwidth]{figures/fig1_hero.pdf}
74	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from \placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} to \placeholder{exp_id: deepseek_bf16_importance, metric: G_s030}$\times$, while random eviction (dashed) remains flat near $1\times$. Shaded regions denote 95\% bootstrap confidence intervals.}
75	\label{fig:hero}
76	\end{figure}
77	
78	We report medians throughout because the II distribution is heavily right-skewed: mean/median ratios reach \placeholder{exp_id: deepseek_bf16_importance, metric: skew_ratio_s030}:1 at $s{=}0.30$ under importance-based eviction. The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\S\ref{sec:stat-validation}) account for this skewness via the resampling distribution.
79	
80	
81	\subsection{Phase-Strategy Crossover (C3)}
82	\label{sec:crossover}
83	
84	The phase-modulated gradient produces a striking qualitative phenomenon: a \emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}$\placeholder{exp_id: deepseek_bf16, metric: crossover_sparsity}, importance-based eviction yields a lower II than random in the high-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{high}} =$ \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s025} vs.\ \placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s025}), but a higher II in the low-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{low}} =$ \placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s025} vs.\ \placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s025}). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases.
85	
86	Figure~\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.
87	
88	\begin{figure}[t]
89	\centering
90	\includegraphics[width=\columnwidth]{figures/fig2_crossover.pdf}
91	\caption{Strategy-dependent crossover at $s{=}$\placeholder{exp_id: deepseek_bf16, metric: crossover_sparsity}. Heatmap of median II by eviction strategy (rows) and reasoning phase (columns). Importance-based eviction outperforms random in the high-sparsity phase but produces \placeholder{exp_id: deepseek_bf16, metric: crossover_low_ratio}$\times$ higher II in the low-sparsity phase, reversing the strategy ranking.}
92	\label{fig:crossover}
93	\end{figure}
94	
95	The crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\S\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \emph{higher} compound severity than the explicitly random baseline.
96	
97	The crossover is observable at $s \geq$ \placeholder{exp_id: deepseek_bf16, metric: crossover_onset}: at lower sparsity levels, importance-based eviction maintains comparable or better performance in both phases. This onset marks a transition point at which sparsity is sufficient for the compound interaction between head pruning and importance scoring to reverse the strategy ranking in the low-sparsity phase.
98	
99	
100	\subsection{Cross-Model Replication (C5)}
101	\label{sec:cross-model}
102	
103	To assess whether the phase-modulated severity gradient generalizes beyond DeepSeek-R1-Distill-Qwen-7B, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct. Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
104	
105	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-seg}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}50$ for DeepSeek).
106	
107	Table~\ref{tab:cross-model} compares the severity gradient across both models.
108	
109	\begin{table}[t]
110	\centering
111	\small
112	\caption{Cross-model replication: severity gradient ($G$) under importance-based eviction. Both models share the Qwen2 architecture but differ in training methodology (distillation vs.\ instruction tuning).}
113	\label{tab:cross-model}
114	\begin{tabular}{@{}lcccc@{}}
115	\toprule
116	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
117	\midrule
118	DeepSeek-R1-Distill-Qwen-7B & \placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} & \placeholder{exp_id: deepseek_bf16_importance, metric: G_s020} & \placeholder{exp_id: deepseek_bf16_importance, metric: G_s025} & \placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} \\
119	Qwen2.5-7B-Instruct         & \placeholder{exp_id: qwen_bf16_importance, metric: G_s015} & \placeholder{exp_id: qwen_bf16_importance, metric: G_s020} & \placeholder{exp_id: qwen_bf16_importance, metric: G_s025} & \placeholder{exp_id: qwen_bf16_importance, metric: G_s030} \\
120	\bottomrule
121	\end{tabular}
122	\end{table}
123	
124	\placeholder{exp_id: qwen_bf16_importance, metric: cross_model_narrative — describe whether Qwen replicates the monotonic gradient increase and how absolute magnitudes compare to DeepSeek. Use cautious language: ``qualitatively reproduces'' rather than ``consistently confirms'' given N=2 models from the same architecture family.}
125	
126	\begin{figure}[t]
127	\centering
128	\includegraphics[width=\columnwidth]{figures/fig5_crossmodel.pdf}
129	\caption{Cross-model comparison of the severity gradient under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit increasing gradients with sparsity. \placeholder{exp_id: qwen_bf16_importance, metric: magnitude_comparison}.}
130	\label{fig:cross-model}
131	\end{figure}
132	
133	The replication on a second model with distinct training methodology suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning. We note that both models share the same backbone architecture; generalization to other architectures (e.g., LLaMA, Mistral) remains an open question (\S\ref{sec:limitations}).
134	
135	
136	\subsection{Statistical Validation}
137	\label{sec:stat-validation}
138	
139	We validate the strategy-dependent severity using two complementary approaches: a paired permutation test on the difference statistic for significance, and Cohen's $d$ for effect size.
140	
141	\paragraph{Permutation test.}
142	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
143	
144	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\caption{Paired permutation test (difference statistic) for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ paired problems, $10{,}000$ permutations). $p$-values are Bonferroni-corrected for 4 comparisons.}
150	\label{tab:permutation}
151	\begin{tabular}{@{}rrcl@{}}
152	\toprule
153	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
154	\midrule
155	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015
156	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020
157	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025
158	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030
159	\bottomrule
160	\end{tabular}
161	\end{table}
162	
163	The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. % exp_id: deepseek_bf16_permtest
164	
165	\begin{figure}[t]
166	\centering
167	\includegraphics[width=\columnwidth]{figures/fig4_bootstrap.pdf}
168	\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}
169	\label{fig:permtest-forest}
170	\end{figure}
171	
172	\paragraph{Effect sizes.}
173	Table~\ref{tab:cohens-d} reports paired Cohen's $d_z$ (bootstrap $B{=}10{,}000$) measuring the standardized difference in II between low- and high-sparsity phases under importance-based eviction.
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\caption{Paired Cohen's $d_z$ for the phase-dependent II difference (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs ($B{=}10{,}000$). DeepSeek: $n{=}49$ problems (1 excluded); Qwen: $n{=}46$ problems (4 excluded).}
179	\label{tab:cohens-d}
180	\begin{tabular}{@{}lcccc@{}}
181	\toprule
182	$s$ & DeepSeek $d_z$ & 95\% CI & Qwen $d_z$ & 95\% CI \\
183	\midrule
184	0.15 & 0.44 (small) & $[0.35,\; 0.78]$ & 0.28 & $[-0.01,\; 0.60]$\textsuperscript{ns} \\ % exp_id: deepseek_bf16_cohens_d_s015, qwen_bf16_cohens_d_s015
185	0.20 & 0.52 (medium) & $[0.43,\; 0.90]$ & 0.55 (medium) & $[0.23,\; 1.02]$ \\ % exp_id: deepseek_bf16_cohens_d_s020, qwen_bf16_cohens_d_s020
186	0.25 & 0.68 (medium) & $[0.56,\; 0.86]$ & 0.89 (large) & $[0.69,\; 1.20]$ \\ % exp_id: deepseek_bf16_cohens_d_s025, qwen_bf16_cohens_d_s025
187	0.30 & 0.80 (large) & $[0.67,\; 1.02]$ & 1.02 (large) & $[0.86,\; 1.33]$ \\ % exp_id: deepseek_bf16_cohens_d_s030, qwen_bf16_cohens_d_s030
188	\bottomrule
189	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}CI spans zero; not significant at $\alpha{=}0.05$.}
190	\end{tabular}
191	\end{table}
192	
193	For DeepSeek, the effect size increases monotonically from small ($d{=}0.44$) at $s{=}0.15$ to large ($d{=}0.80$) at $s{=}0.30$, with all CIs excluding zero (Table~\ref{tab:cohens-d}). % exp_id: deepseek_bf16_cohens_d
194	For Qwen, the compound interaction effect emerges at $s \geq 0.20$ ($d \geq 0.55$), with the $s{=}0.15$ CI spanning zero ($d{=}0.28$, $[-0.01, 0.60]$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: qwen_bf16_cohens_d_s015
195	At higher sparsity levels ($s \geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite comparable or smaller absolute II values. % exp_id: deepseek_bf16_cohens_d, qwen_bf16_cohens_d
196	Full per-problem distributions and permutation null distributions appear in Appendix~\ref{app:bootstrap-details}.
197	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "d285e6db-1874-4e49-9b9c-fd0ab022402b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\nWe present our empirical findings in five parts: strategy-dependent compound severity (\\S\\ref{sec:strategy-severity}), phase-modulated amplification (\\S\\ref{sec:phase-amplification}), the phase-strategy crossover (\\S\\ref{sec:crossover}), cross-model replication (\\S\\ref{sec:cross-model}), and statistical validation (\\S\\ref{sec:stat-validation}).\n\n\n\\subsection{Experimental Overview}\n\\label{sec:exp-overview}\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\\S\\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. We compare importance-based and random eviction strategies (\\S\\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\\S\\ref{sec:phase-seg}). The interaction index (II, Eq.~\\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\\ref{eq:gradient}) captures phase-dependent amplification.\nModels are evaluated in \\texttt{bfloat16} precision (\\S\\ref{sec:experimental-setup}). Full experimental details appear therein.\n\n\n\\subsection{Strategy-Dependent Severity (C1)}\n\\label{sec:strategy-severity}\n\nThe aggregate interaction index reveals a stark dependence on eviction strategy. Table~\\ref{tab:aggregate-ii} reports the problem-level mean II across all 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: mean II increases from \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s015} at $s{=}0.15$ to \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s030} at $s{=}0.30$. Under random eviction, compound interaction shows no systematic phase modulation across sparsity levels, with mean II near \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_range}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Aggregate interaction index (II) by eviction strategy and sparsity level. Values are problem-level means across 50 MATH-500 problems on DeepSeek-R1-Distill-Qwen-7B.}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: mean_II_s030} \\\\\nRandom     & \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s015} & \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s020} & \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s025} & \\placeholder{exp_id: deepseek_bf16_random, metric: mean_II_s030} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.\n\n\n\\subsection{Phase-Modulated Amplification (C2)}\n\\label{sec:phase-amplification}\n\nDecomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \\S\\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.\n\nUnder importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} at $s{=}0.15$ to \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} at $s{=}0.30$, spanning a \\placeholder{exp_id: deepseek_bf16_importance, metric: G_min}--\\placeholder{exp_id: deepseek_bf16_importance, metric: G_max}$\\times$ range. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences comparatively mild interaction. Under random eviction, the gradient remains near unity ($G \\approx$ \\placeholder{exp_id: deepseek_bf16_random, metric: G_range}) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. The severity gradient $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$ quantifies phase-dependent amplification of compound interaction.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $G$ & 95\\% CI \\\\\n\\midrule\n0.15 & Importance & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_mid_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} & [\\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s015}, \\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s015}] \\\\\n0.15 & Random     & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s015} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_mid_s015} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s015} & \\placeholder{exp_id: deepseek_bf16_random, metric: G_s015} & [\\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s015}, \\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s015}] \\\\\n\\addlinespace\n0.20 & Importance & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_mid_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s020} & [\\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s020}, \\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s020}] \\\\\n0.20 & Random     & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s020} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_mid_s020} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s020} & \\placeholder{exp_id: deepseek_bf16_random, metric: G_s020} & [\\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s020}, \\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s020}] \\\\\n\\addlinespace\n0.25 & Importance & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_mid_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s025} & [\\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s025}, \\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s025}] \\\\\n0.25 & Random     & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s025} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_mid_s025} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s025} & \\placeholder{exp_id: deepseek_bf16_random, metric: G_s025} & [\\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s025}, \\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s025}] \\\\\n\\addlinespace\n0.30 & Importance & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s030} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_mid_s030} & \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s030} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} & [\\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_lo_s030}, \\placeholder{exp_id: deepseek_bf16_importance, metric: G_CI_hi_s030}] \\\\\n0.30 & Random     & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s030} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_mid_s030} & \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s030} & \\placeholder{exp_id: deepseek_bf16_random, metric: G_s030} & [\\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_lo_s030}, \\placeholder{exp_id: deepseek_bf16_random, metric: G_CI_hi_s030}] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient growth is sub-exponential: successive ratios between adjacent sparsity levels are \\placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s015_s020}$\\times$, \\placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s020_s025}$\\times$, and \\placeholder{exp_id: deepseek_bf16_importance, metric: growth_ratio_s025_s030}$\\times$---a decreasing growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_hero.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} to \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s030}$\\times$, while random eviction (dashed) remains flat near $1\\times$. Shaded regions denote 95\\% bootstrap confidence intervals.}\n\\label{fig:hero}\n\\end{figure}\n\nWe report medians throughout because the II distribution is heavily right-skewed: mean/median ratios reach \\placeholder{exp_id: deepseek_bf16_importance, metric: skew_ratio_s030}:1 at $s{=}0.30$ under importance-based eviction. The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\\S\\ref{sec:stat-validation}) account for this skewness via the resampling distribution.\n\n\n\\subsection{Phase-Strategy Crossover (C3)}\n\\label{sec:crossover}\n\nThe phase-modulated gradient produces a striking qualitative phenomenon: a \\emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}$\\placeholder{exp_id: deepseek_bf16, metric: crossover_sparsity}, importance-based eviction yields a lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} =$ \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_high_s025} vs.\\ \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_high_s025}), but a higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} =$ \\placeholder{exp_id: deepseek_bf16_importance, metric: median_II_low_s025} vs.\\ \\placeholder{exp_id: deepseek_bf16_random, metric: median_II_low_s025}). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases.\n\nFigure~\\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}$\\placeholder{exp_id: deepseek_bf16, metric: crossover_sparsity}. Heatmap of median II by eviction strategy (rows) and reasoning phase (columns). Importance-based eviction outperforms random in the high-sparsity phase but produces \\placeholder{exp_id: deepseek_bf16, metric: crossover_low_ratio}$\\times$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n\\label{fig:crossover}\n\\end{figure}\n\nThe crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\\S\\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \\emph{higher} compound severity than the explicitly random baseline.\n\nThe crossover is observable at $s \\geq$ \\placeholder{exp_id: deepseek_bf16, metric: crossover_onset}: at lower sparsity levels, importance-based eviction maintains comparable or better performance in both phases. This onset marks a transition point at which sparsity is sufficient for the compound interaction between head pruning and importance scoring to reverse the strategy ranking in the low-sparsity phase.\n\n\n\\subsection{Cross-Model Replication (C5)}\n\\label{sec:cross-model}\n\nTo assess whether the phase-modulated severity gradient generalizes beyond DeepSeek-R1-Distill-Qwen-7B, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct. Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-seg}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}50$ for DeepSeek).\n\nTable~\\ref{tab:cross-model} compares the severity gradient across both models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: severity gradient ($G$) under importance-based eviction. Both models share the Qwen2 architecture but differ in training methodology (distillation vs.\\ instruction tuning).}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s015} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s020} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s025} & \\placeholder{exp_id: deepseek_bf16_importance, metric: G_s030} \\\\\nQwen2.5-7B-Instruct         & \\placeholder{exp_id: qwen_bf16_importance, metric: G_s015} & \\placeholder{exp_id: qwen_bf16_importance, metric: G_s020} & \\placeholder{exp_id: qwen_bf16_importance, metric: G_s025} & \\placeholder{exp_id: qwen_bf16_importance, metric: G_s030} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\placeholder{exp_id: qwen_bf16_importance, metric: cross_model_narrative — describe whether Qwen replicates the monotonic gradient increase and how absolute magnitudes compare to DeepSeek. Use cautious language: ``qualitatively reproduces'' rather than ``consistently confirms'' given N=2 models from the same architecture family.}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the severity gradient under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit increasing gradients with sparsity. \\placeholder{exp_id: qwen_bf16_importance, metric: magnitude_comparison}.}\n\\label{fig:cross-model}\n\\end{figure}\n\nThe replication on a second model with distinct training methodology suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning. We note that both models share the same backbone architecture; generalization to other architectures (e.g., LLaMA, Mistral) remains an open question (\\S\\ref{sec:limitations}).\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nWe validate the strategy-dependent severity using two complementary approaches: a paired permutation test on the difference statistic for significance, and Cohen's $d$ for effect size.\n\n\\paragraph{Permutation test.}\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test (difference statistic) for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ paired problems, $10{,}000$ permutations). $p$-values are Bonferroni-corrected for 4 comparisons.}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. % exp_id: deepseek_bf16_permtest\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\\paragraph{Effect sizes.}\nTable~\\ref{tab:cohens-d} reports paired Cohen's $d_z$ (bootstrap $B{=}10{,}000$) measuring the standardized difference in II between low- and high-sparsity phases under importance-based eviction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired Cohen's $d_z$ for the phase-dependent II difference (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$). DeepSeek: $n{=}49$ problems (1 excluded); Qwen: $n{=}46$ problems (4 excluded).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DeepSeek $d_z$ & 95\\% CI & Qwen $d_z$ & 95\\% CI \\\\\n\\midrule\n0.15 & 0.44 (small) & $[0.35,\\; 0.78]$ & 0.28 & $[-0.01,\\; 0.60]$\\textsuperscript{ns} \\\\ % exp_id: deepseek_bf16_cohens_d_s015, qwen_bf16_cohens_d_s015\n0.20 & 0.52 (medium) & $[0.43,\\; 0.90]$ & 0.55 (medium) & $[0.23,\\; 1.02]$ \\\\ % exp_id: deepseek_bf16_cohens_d_s020, qwen_bf16_cohens_d_s020\n0.25 & 0.68 (medium) & $[0.56,\\; 0.86]$ & 0.89 (large) & $[0.69,\\; 1.20]$ \\\\ % exp_id: deepseek_bf16_cohens_d_s025, qwen_bf16_cohens_d_s025\n0.30 & 0.80 (large) & $[0.67,\\; 1.02]$ & 1.02 (large) & $[0.86,\\; 1.33]$ \\\\ % exp_id: deepseek_bf16_cohens_d_s030, qwen_bf16_cohens_d_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}CI spans zero; not significant at $\\alpha{=}0.05$.}\n\\end{tabular}\n\\end{table}\n\nFor DeepSeek, the effect size increases monotonically from small ($d{=}0.44$) at $s{=}0.15$ to large ($d{=}0.80$) at $s{=}0.30$, with all CIs excluding zero (Table~\\ref{tab:cohens-d}). % exp_id: deepseek_bf16_cohens_d\nFor Qwen, the compound interaction effect emerges at $s \\geq 0.20$ ($d \\geq 0.55$), with the $s{=}0.15$ CI spanning zero ($d{=}0.28$, $[-0.01, 0.60]$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: qwen_bf16_cohens_d_s015\nAt higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite comparable or smaller absolute II values. % exp_id: deepseek_bf16_cohens_d, qwen_bf16_cohens_d\nFull per-problem distributions and permutation null distributions appear in Appendix~\\ref{app:bootstrap-details}.\n",
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

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01FmcE77F5oHHxUmDor7Y7VD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "c4faf5ef-d6c0-4fbb-a278-542018182f8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6WAE5W2W9C1F5SeBFV4cX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4501,
      "cache_read_input_tokens": 23659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4501
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

_source line 18 · 2026-05-14T09:13:57.425Z_

<details><summary>↩ Tool result · `toolu_01FmcE77F5oHHxUmDor7Y7VD`</summary>

```text
1	
2	\section{Analysis: Entropy-Discrimination Collapse}
3	\label{sec:analysis}
4	
5	The results in \S\ref{sec:experiments} reveal a striking asymmetry: importance-based eviction exhibits $11$--$42\times$ severity amplification in low-sparsity phases, while random eviction remains flat at ${\sim}1\times$ across all phases. Why is compound severity phase-modulated for one strategy but not the other? We propose \emph{entropy-discrimination collapse} as an explanatory mechanism: head pruning redistributes attention mass in a phase-dependent manner, degrading the discriminative power of importance scores precisely in phases where attention is already broadly distributed.
6	
7	\subsection{Attention Redistribution Under Head Pruning}
8	\label{sec:attn-redistribution}
9	
10	When a fraction $s$ of attention heads are pruned, the surviving heads must compensate for the lost information pathways. We characterize this compensation through the attention entropy of a surviving head $h$ at query position $i$:
11	\begin{equation}
12	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
13	    \label{eq:attn-entropy}
14	\end{equation}
15	Higher $\mathcal{H}$ indicates more uniformly distributed attention. The effect of pruning on $\mathcal{H}$ depends critically on the reasoning phase.
16	
17	In the \textbf{high-sparsity phase}, attention is already concentrated on a few key positions ($\mathcal{H}$ is low). Head redundancy is high---concentrated attention patterns are likely to overlap across heads---so pruning removes largely redundant capacity. The surviving heads continue to attend to the same narrow set of positions, and $\mathcal{H}$ changes minimally.
18	
19	In the \textbf{low-sparsity phase}, attention distributes broadly across many positions ($\mathcal{H}$ is already elevated). Head redundancy is low: each head captures partially non-overlapping information. Pruning forces surviving heads to broaden their attention further to compensate for the lost coverage, pushing $\mathcal{H}$ above its already high baseline.
20	
21	\placeholder{Empirical attention entropy: mean $\mathcal{H}$ per phase, pre- and post-pruning at $s \in \{0.15, 0.25\}$, showing differential entropy increase concentrated in the low-sparsity phase.}
22	
23	\subsection{Discrimination Collapse in Importance Scoring}
24	\label{sec:discrimination-collapse}
25	
26	The KV importance score (Eq.~\ref{eq:kv-importance}) aggregates attention mass across all surviving heads. When pruning increases the attention entropy of these heads, the cumulative importance scores become more uniform: the gap between the most-attended and least-attended positions shrinks. We hypothesize that this uniformity degrades the \emph{discriminative power} of importance-based eviction---the ability to reliably distinguish positions critical for the model's computation from those that can be safely removed.
27	
28	When the importance distribution has low entropy (a few positions dominate), thresholding the bottom-$s$ fraction removes genuinely unimportant positions. When the distribution is near-uniform, the same thresholding becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform importance scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction.
29	
30	\placeholder{Importance score concentration (Gini coefficient or max-to-median ratio) across phases, pre- and post-pruning, showing discrimination collapse predominantly in the low-sparsity phase.}
31	
32	This mechanism directly accounts for the crossover phenomenon (\S\ref{sec:crossover}). In high-sparsity phases, pruning preserves attention concentration, importance scores remain discriminative, and importance-based eviction removes genuinely less critical positions---achieving lower compound severity than random eviction. In low-sparsity phases, pruning amplifies attention entropy, importance discrimination collapses, and importance-based eviction devolves into a biased pseudo-random process that can inadvertently remove critical positions---producing \emph{higher} compound severity than the explicitly random baseline. The severity inversion is thus not a failure of the importance metric in isolation, but an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.
33	
34	Random eviction is immune to this mechanism: its decisions are independent of attention patterns and invariant to the redistribution caused by head pruning. This explains the flat severity gradient ($G \approx 1$) observed under random eviction at all sparsity levels.
35	
36	\subsection{Implications for Compound Sparsity}
37	\label{sec:analysis-implications}
38	
39	The entropy-discrimination collapse mechanism suggests several broader conclusions.
40	
41	\paragraph{Architecture generality.} The mechanism depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~heterogeneous attention entropy across reasoning phases. Both are shared by the major KV cache compression methods---H$_2$O \cite{h2o2024}, SnapKV \cite{snapkv2024}, PyramidKV \cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. We therefore expect phase-modulated compound severity to emerge whenever head pruning is combined with attention-based cache eviction, regardless of specific model architecture.
42	
43	\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse in phases where attention is broadly distributed, with the severity gradient scaling with the pruning-induced entropy increase. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients. This prediction is directly testable in future work.
44	
45	\paragraph{Reframing compound severity.} The flat random baseline ($G \approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \emph{per se}. Rather, it is an emergent interaction between the eviction strategy and the phase-dependent structure of attention. This reframes compound severity as a \emph{strategy-phase interaction}---one that a phase-aware sparsity controller could, in principle, mitigate by adjusting the eviction budget or strategy per phase.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "d3d072eb-8c56-485c-9395-d06191495cbf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\n\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{sec:analysis}\n\nThe results in \\S\\ref{sec:experiments} reveal a striking asymmetry: importance-based eviction exhibits $11$--$42\\times$ severity amplification in low-sparsity phases, while random eviction remains flat at ${\\sim}1\\times$ across all phases. Why is compound severity phase-modulated for one strategy but not the other? We propose \\emph{entropy-discrimination collapse} as an explanatory mechanism: head pruning redistributes attention mass in a phase-dependent manner, degrading the discriminative power of importance scores precisely in phases where attention is already broadly distributed.\n\n\\subsection{Attention Redistribution Under Head Pruning}\n\\label{sec:attn-redistribution}\n\nWhen a fraction $s$ of attention heads are pruned, the surviving heads must compensate for the lost information pathways. We characterize this compensation through the attention entropy of a surviving head $h$ at query position $i$:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nHigher $\\mathcal{H}$ indicates more uniformly distributed attention. The effect of pruning on $\\mathcal{H}$ depends critically on the reasoning phase.\n\nIn the \\textbf{high-sparsity phase}, attention is already concentrated on a few key positions ($\\mathcal{H}$ is low). Head redundancy is high---concentrated attention patterns are likely to overlap across heads---so pruning removes largely redundant capacity. The surviving heads continue to attend to the same narrow set of positions, and $\\mathcal{H}$ changes minimally.\n\nIn the \\textbf{low-sparsity phase}, attention distributes broadly across many positions ($\\mathcal{H}$ is already elevated). Head redundancy is low: each head captures partially non-overlapping information. Pruning forces surviving heads to broaden their attention further to compensate for the lost coverage, pushing $\\mathcal{H}$ above its already high baseline.\n\n\\placeholder{Empirical attention entropy: mean $\\mathcal{H}$ per phase, pre- and post-pruning at $s \\in \\{0.15, 0.25\\}$, showing differential entropy increase concentrated in the low-sparsity phase.}\n\n\\subsection{Discrimination Collapse in Importance Scoring}\n\\label{sec:discrimination-collapse}\n\nThe KV importance score (Eq.~\\ref{eq:kv-importance}) aggregates attention mass across all surviving heads. When pruning increases the attention entropy of these heads, the cumulative importance scores become more uniform: the gap between the most-attended and least-attended positions shrinks. We hypothesize that this uniformity degrades the \\emph{discriminative power} of importance-based eviction---the ability to reliably distinguish positions critical for the model's computation from those that can be safely removed.\n\nWhen the importance distribution has low entropy (a few positions dominate), thresholding the bottom-$s$ fraction removes genuinely unimportant positions. When the distribution is near-uniform, the same thresholding becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform importance scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction.\n\n\\placeholder{Importance score concentration (Gini coefficient or max-to-median ratio) across phases, pre- and post-pruning, showing discrimination collapse predominantly in the low-sparsity phase.}\n\nThis mechanism directly accounts for the crossover phenomenon (\\S\\ref{sec:crossover}). In high-sparsity phases, pruning preserves attention concentration, importance scores remain discriminative, and importance-based eviction removes genuinely less critical positions---achieving lower compound severity than random eviction. In low-sparsity phases, pruning amplifies attention entropy, importance discrimination collapses, and importance-based eviction devolves into a biased pseudo-random process that can inadvertently remove critical positions---producing \\emph{higher} compound severity than the explicitly random baseline. The severity inversion is thus not a failure of the importance metric in isolation, but an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.\n\nRandom eviction is immune to this mechanism: its decisions are independent of attention patterns and invariant to the redistribution caused by head pruning. This explains the flat severity gradient ($G \\approx 1$) observed under random eviction at all sparsity levels.\n\n\\subsection{Implications for Compound Sparsity}\n\\label{sec:analysis-implications}\n\nThe entropy-discrimination collapse mechanism suggests several broader conclusions.\n\n\\paragraph{Architecture generality.} The mechanism depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~heterogeneous attention entropy across reasoning phases. Both are shared by the major KV cache compression methods---H$_2$O \\cite{h2o2024}, SnapKV \\cite{snapkv2024}, PyramidKV \\cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. We therefore expect phase-modulated compound severity to emerge whenever head pruning is combined with attention-based cache eviction, regardless of specific model architecture.\n\n\\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse in phases where attention is broadly distributed, with the severity gradient scaling with the pruning-induced entropy increase. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients. This prediction is directly testable in future work.\n\n\\paragraph{Reframing compound severity.} The flat random baseline ($G \\approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \\emph{per se}. Rather, it is an emergent interaction between the eviction strategy and the phase-dependent structure of attention. This reframes compound severity as a \\emph{strategy-phase interaction}---one that a phase-aware sparsity controller could, in principle, mitigate by adjusting the eviction budget or strategy per phase.\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_017XsAeMPmGyxah71r3jKBTJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "a43e405d-b798-4571-8a41-e1900e98d657",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6WAE5W2W9C1F5SeBFV4cX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4501,
      "cache_read_input_tokens": 23659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4501
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

_source line 20 · 2026-05-14T09:13:57.926Z_

<details><summary>↩ Tool result · `toolu_017XsAeMPmGyxah71r3jKBTJ`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{On the predictability of phase-modulated severity.}
5	One might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.
6	We do not dispute this intuition.
7	The surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.
8	
9	First, the \emph{magnitude} of the severity gradient---$11$--$42\times$ amplification % PENDING-BF16
10	across sparsity levels (Table~\ref{tab:bootstrap})---far exceeds what a naive ``less discriminative $\Rightarrow$ somewhat worse'' argument would predict.
11	A reviewer expecting a $2$--$3\times$ effect would find an order-of-magnitude amplification difficult to anticipate without measurement.
12	Second, the gradient is \emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-additive behavior ($\widetilde{\mathrm{II}}_{\text{high}} < 1$ at all sparsity levels). % PENDING-BF16
13	This asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.
14	Third, and most strikingly, a \emph{crossover} emerges: at $s \geq 0.25$, importance-based eviction \emph{outperforms} random eviction in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.58$ vs.\ $3.00$) % PENDING-BF16
15	yet \emph{underperforms} dramatically in low-sparsity phases ($\widetilde{\mathrm{II}} = 30.9$ vs.\ $2.9$). % PENDING-BF16
16	The same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''
17	% REVIEWER-ATTACK: "The qualitative direction is trivially expected from attention entropy arguments."
18	% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 11-42× amplification is order-of-magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.
19	
20	\paragraph{Implications for compound sparsity deployment.}
21	Our findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.
22	Compound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\S\ref{sec:analysis}) renders importance-based eviction unreliable.
23	A deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.
24	
25	This observation motivates \emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.
26	The severity gradient $G$ reported in \S\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \gg 1$ receive a reduced sparsity budget, while phases with $G \leq 1$ tolerate aggressive compression with minimal quality loss.
27	
28	\paragraph{Future directions.}
29	The phase-aware allocation principle above points toward a concrete system design: a \emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.
30	The controller would route each generation step through a low-overhead phase classifier (\S\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.
31	Whether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.
32	
33	A second direction concerns mechanism validation.
34	The entropy-discrimination collapse hypothesis (\S\ref{sec:analysis}) makes testable predictions about attention entropy redistribution under head pruning.
35	Directly measuring per-head entropy shifts across phases---and correlating them with the observed compound severity---would provide causal evidence beyond the correlational structure reported here.
36	
37	Finally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.
38	
39	\subsection{Limitations}
40	\label{sec:limitations}
41	
42	\paragraph{Model scale.}
43	All experiments are conducted at the 7B parameter scale.
44	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
45	Larger models may exhibit different attention redundancy structures that alter the entropy-discrimination collapse dynamics.
46	% REVIEWER-ATTACK: "7B is too small to be relevant for production."
47	% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
48	
49	\paragraph{Architectural scope.}
50	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
51	The cross-model replication (\S\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.
52	The entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.
53	% REVIEWER-ATTACK: "Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM."
54	% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.
55	
56	\paragraph{Task coverage.}
57	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
58	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
59	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
60	% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
61	% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
62	
63	\paragraph{Statistical scope.}
64	Bootstrap confidence intervals use $B{=}1{,}000$ resamples in the current \texttt{float16} analysis; the planned \texttt{bfloat16} replication will increase to $B{=}10{,}000$. % PENDING-BF16
65	The paired analysis requires problems with observations in both the high- and low-sparsity phases, yielding $n_{\text{paired}} \in [16, 22]$ out of 50 problems---a constraint imposed by the phase segmentation rather than data filtering.
66	The interaction index distribution is heavily right-skewed (mean/median ratios up to ${\sim}34$:1), % PENDING-BF16
67	motivating our use of medians and nonparametric bootstrap rather than parametric tests.
68	While all bootstrap CIs reject $G \leq 1$ at $p < 0.001$, the wide CIs at higher sparsity levels (e.g., $[19.1,\; 299.8]$ at $s{=}0.30$) % PENDING-BF16
69	reflect genuine uncertainty in the gradient magnitude under extreme skewness, and should be interpreted as evidence for the \emph{direction} of the effect rather than precise magnitude estimation.
70	
71	\paragraph{Sparsity range.}
72	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, a moderate range representative of practical deployment targets.
73	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
74	Conversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.
75	% REVIEWER-ATTACK: "Why not test higher sparsity? 0.30 is conservative."
76	% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, growth rate 2.24→1.84→1.42×) suggests saturation at higher sparsity, but confirming this is future work.
77	
78	\paragraph{No throughput evaluation.}
79	This work focuses on characterizing the \emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.
80	We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.
81	% REVIEWER-ATTACK: "No system evaluation. How do we know the severity amplification matters for real deployment?"
82	% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "8db23fde-50f0-4dd9-8071-31fc0b04e6eb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nOne might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.\nWe do not dispute this intuition.\nThe surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.\n\nFirst, the \\emph{magnitude} of the severity gradient---$11$--$42\\times$ amplification % PENDING-BF16\nacross sparsity levels (Table~\\ref{tab:bootstrap})---far exceeds what a naive ``less discriminative $\\Rightarrow$ somewhat worse'' argument would predict.\nA reviewer expecting a $2$--$3\\times$ effect would find an order-of-magnitude amplification difficult to anticipate without measurement.\nSecond, the gradient is \\emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-additive behavior ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 1$ at all sparsity levels). % PENDING-BF16\nThis asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.\nThird, and most strikingly, a \\emph{crossover} emerges: at $s \\geq 0.25$, importance-based eviction \\emph{outperforms} random eviction in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.58$ vs.\\ $3.00$) % PENDING-BF16\nyet \\emph{underperforms} dramatically in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 30.9$ vs.\\ $2.9$). % PENDING-BF16\nThe same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''\n% REVIEWER-ATTACK: \"The qualitative direction is trivially expected from attention entropy arguments.\"\n% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 11-42× amplification is order-of-magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.\n\n\\paragraph{Implications for compound sparsity deployment.}\nOur findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.\nCompound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\\S\\ref{sec:analysis}) renders importance-based eviction unreliable.\nA deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.\n\nThis observation motivates \\emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.\nThe severity gradient $G$ reported in \\S\\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \\gg 1$ receive a reduced sparsity budget, while phases with $G \\leq 1$ tolerate aggressive compression with minimal quality loss.\n\n\\paragraph{Future directions.}\nThe phase-aware allocation principle above points toward a concrete system design: a \\emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.\nThe controller would route each generation step through a low-overhead phase classifier (\\S\\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.\nWhether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.\n\nA second direction concerns mechanism validation.\nThe entropy-discrimination collapse hypothesis (\\S\\ref{sec:analysis}) makes testable predictions about attention entropy redistribution under head pruning.\nDirectly measuring per-head entropy shifts across phases---and correlating them with the observed compound severity---would provide causal evidence beyond the correlational structure reported here.\n\nFinally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the entropy-discrimination collapse dynamics.\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.\nThe entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}1{,}000$ resamples in the current \\texttt{float16} analysis; the planned \\texttt{bfloat16} replication will increase to $B{=}10{,}000$. % PENDING-BF16\nThe paired analysis requires problems with observations in both the high- and low-sparsity phases, yielding $n_{\\text{paired}} \\in [16, 22]$ out of 50 problems---a constraint imposed by the phase segmentation rather than data filtering.\nThe interaction index distribution is heavily right-skewed (mean/median ratios up to ${\\sim}34$:1), % PENDING-BF16\nmotivating our use of medians and nonparametric bootstrap rather than parametric tests.\nWhile all bootstrap CIs reject $G \\leq 1$ at $p < 0.001$, the wide CIs at higher sparsity levels (e.g., $[19.1,\\; 299.8]$ at $s{=}0.30$) % PENDING-BF16\nreflect genuine uncertainty in the gradient magnitude under extreme skewness, and should be interpreted as evidence for the \\emph{direction} of the effect rather than precise magnitude estimation.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, growth rate 2.24→1.84→1.42×) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nThis work focuses on characterizing the \\emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.\nWe do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
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
Now let me also read the background.tex and results_5_1.tex to get the complete picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "4e2412ab-98e8-4842-8ecb-2b27a722fb58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcpvFFrxAYEfZrT2pREJJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13921,
      "cache_read_input_tokens": 28160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13921
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

Now let me also check the background and the results_5_1 file for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "0613f4fa-ff21-41f3-b630-de30502bf330",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcpvFFrxAYEfZrT2pREJJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13921,
      "cache_read_input_tokens": 28160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13921
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

<details open><summary>🔧 Tool call — Read · `toolu_01NpVMPC1eEy5oaYLkzvC5x3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "f0d82b22-5eb2-4bcb-8afe-cc6e2c46f391",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcpvFFrxAYEfZrT2pREJJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13921,
      "cache_read_input_tokens": 28160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13921
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

_source line 24 · 2026-05-14T09:14:03.726Z_

<details><summary>↩ Tool result · `toolu_01NpVMPC1eEy5oaYLkzvC5x3`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Methodology.tex should reference these via \eqref rather than redefining.
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.
9	
10	\subsection{Compound Sparsity Formulation}
11	\label{sec:compound-sparsity}
12	
13	Consider a Transformer language model with $L$ layers, each containing $H$ attention heads.
14	Let $s \in (0,1)$ denote a unified sparsity budget applied to both compression axes.
15	
16	\paragraph{Attention head pruning.}
17	For each layer $\ell$, heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$, where $\mathbf{A}_j^{(\ell)} \in \mathbb{R}^{T \times T}$ is the attention matrix for head $j$ \cite{voita2019heads, michel2019sixteen}.
18	A binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads, zeroing the output of pruned heads:
19	\begin{equation}
20	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
21	    \label{eq:head-mask}
22	\end{equation}
23	
24	\paragraph{KV cache eviction.}
25	For a sequence of length $T$, a position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions, with the BOS token always preserved.
26	Evicted positions are blocked via attention masking:
27	\begin{equation}
28	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
29	    \label{eq:kv-mask}
30	\end{equation}
31	We compare two strategies for constructing $\mathbf{m}_k$:
32	\begin{itemize}[nosep,leftmargin=*]
33	    \item \textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:
34	    \begin{equation}
35	        \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
36	        \label{eq:kv-importance}
37	    \end{equation}
38	    where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}.
39	    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
40	\end{itemize}
41	
42	\paragraph{Compound sparsity.}
43	Applying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \emph{compound sparsity}.
44	The two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.
45	Prior analyses of compound compression \cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.
46	We investigate whether the eviction strategy and reasoning phase introduce additional structure.
47	
48	\subsection{Interaction Index}
49	\label{sec:interaction-index}
50	
51	To quantify the interaction between head pruning and KV cache eviction, we define the \emph{Interaction Index} (II) following the factorial interaction framework from experimental design.
52	
53	For a given text segment, let $\text{PPL}_d$, $\text{PPL}_a$, $\text{PPL}_k$, and $\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.
54	Perplexity is computed as $\text{PPL} = \exp\!\bigl(\frac{1}{|S|}\sum_{t \in S} \mathcal{L}_t\bigr)$, where $\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.
55	Normalizing by the dense baseline yields relative degradation ratios $r_c = \text{PPL}_c\,/\,\text{PPL}_d$ for $c \in \{a, k, b\}$, and the Interaction Index:
56	\begin{equation}
57	    \mathrm{II} = r_b - r_a - r_k + 1.
58	    \label{eq:ii}
59	\end{equation}
60	
61	Under additive independence, $r_b \approx r_a + r_k - 1$, yielding $\mathrm{II} \approx 0$.
62	The sign of II determines the interaction regime:
63	\begin{itemize}[nosep,leftmargin=*]
64	    \item $\mathrm{II} > 0$: \textbf{super-additive}---compound degradation exceeds the sum of individual effects.
65	    \item $\mathrm{II} < 0$: \textbf{sub-additive}---the compound effect is less than the sum of parts.
66	    \item $\mathrm{II} = 0$: \textbf{additive}---the two mechanisms do not interact.
67	\end{itemize}
68	
69	\paragraph{Choice of additive null.}
70	Equation~\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \cdot r_k$.
71	We adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \leq 0.30$).
72	We verify in Appendix~\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.
73	
74	Normalizing by $\text{PPL}_d$ ensures cross-problem comparability.
75	Because the II distribution is heavily right-skewed, we report medians as the central tendency.
76	
77	\paragraph{Severity gradient.}
78	To capture how II varies across reasoning phases (defined in \S\ref{sec:phase-segmentation}), we define the \emph{severity gradient}:
79	\begin{equation}
80	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
81	    \label{eq:gradient}
82	\end{equation}
83	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.
84	$G \gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \approx 1$ indicates phase-invariant degradation.
85	When $\widetilde{\mathrm{II}}_{\,\textit{high}} < \varepsilon$ for a small threshold $\varepsilon > 0$, we report $G = \infty$.
86	
87	\subsection{Phase Segmentation}
88	\label{sec:phase-segmentation}
89	
90	Reasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.
91	We partition each generated sequence into three phases based on the local \emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \cite{thinkv-iclr2026}.
92	
93	\paragraph{Attention sparsity.}
94	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
95	\begin{equation}
96	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
97	    \label{eq:attn-sparsity}
98	\end{equation}
99	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads.
100	
101	\paragraph{Quantile-based segmentation.}
102	Tokens are partitioned into three groups by the tercile boundaries of $\{\sigma_i\}_{i=1}^{T}$:
103	\begin{itemize}[nosep,leftmargin=*]
104	    \item \textbf{High-sparsity phase} (top tercile of $\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.
105	    \item \textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.
106	    \item \textbf{Low-sparsity phase} (bottom tercile of $\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.
107	\end{itemize}
108	Contiguous segments shorter than $\texttt{min\_phase\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.
109	The segmentation is purely data-driven and requires only access to attention weights.
110	
111	This phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \cite{phase-transition-compression-2026}.
112	Our central research question is: \emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\times$ strategy interaction?}
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "5f6713c2-1e53-4460-8275-ddb497d36de9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer language model with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nFor each layer $\\ell$, heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$, where $\\mathbf{A}_j^{(\\ell)} \\in \\mathbb{R}^{T \\times T}$ is the attention matrix for head $j$ \\cite{voita2019heads, michel2019sixteen}.\nA binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads, zeroing the output of pruned heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions, with the BOS token always preserved.\nEvicted positions are blocked via attention masking:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \\emph{compound sparsity}.\nThe two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.\nPrior analyses of compound compression \\cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.\nWe investigate whether the eviction strategy and reasoning phase introduce additional structure.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify the interaction between head pruning and KV cache eviction, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nFor a given text segment, let $\\text{PPL}_d$, $\\text{PPL}_a$, $\\text{PPL}_k$, and $\\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.\nPerplexity is computed as $\\text{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$, where $\\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.\nNormalizing by the dense baseline yields relative degradation ratios $r_c = \\text{PPL}_c\\,/\\,\\text{PPL}_d$ for $c \\in \\{a, k, b\\}$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\nUnder additive independence, $r_b \\approx r_a + r_k - 1$, yielding $\\mathrm{II} \\approx 0$.\nThe sign of II determines the interaction regime:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive}---compound degradation exceeds the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive}---the compound effect is less than the sum of parts.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive}---the two mechanisms do not interact.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEquation~\\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \\cdot r_k$.\nWe adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \\leq 0.30$).\nWe verify in Appendix~\\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.\n\nNormalizing by $\\text{PPL}_d$ ensures cross-problem comparability.\nBecause the II distribution is heavily right-skewed, we report medians as the central tendency.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.\nWe partition each generated sequence into three phases based on the local \\emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into three groups by the tercile boundaries of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile of $\\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile of $\\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.\n\\end{itemize}\nContiguous segments shorter than $\\texttt{min\\_phase\\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.\nThe segmentation is purely data-driven and requires only access to attention weights.\n\nThis phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \\cite{phase-transition-compression-2026}.\nOur central research question is: \\emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\\times$ strategy interaction?}\n",
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_011rGDM9FxccnXyN4DyZWuDP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results_5_1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "e5d6e34f-7dac-4194-90f9-d07c92af00ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcpvFFrxAYEfZrT2pREJJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13921,
      "cache_read_input_tokens": 28160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13921
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

_source line 26 · 2026-05-14T09:14:04.145Z_

<details><summary>↩ Tool result · `toolu_011rGDM9FxccnXyN4DyZWuDP`</summary>

```text
1	% Section 5.1: Phase-Modulated Severity Gradient
2	% Data source: v6_importance_s015/s020/s025/s030, mvp_v5_random_s015/s020/s025/s030
3	% All numeric values are from fp16 runs; bf16 replication pending.
4	
5	\subsection{Phase-Modulated Severity Gradient}
6	\label{sec:severity-gradient-fp16}
7	
8	Under importance-based eviction, compound interaction severity varies by an order of magnitude across reasoning phases:
9	the severity gradient $G$ (Eq.~\eqref{eq:gradient}) ranges from $11.5\times$ at $s{=}0.15$ to% PENDING-BF16
10	$41.9\times$ at $s{=}0.30$% PENDING-BF16
11	(paired bootstrap, $B{=}1{,}000$; Table~\ref{tab:bootstrap-fp16}).
12	Random eviction yields a flat gradient of $G \approx 0.7$--$1.8\times$% PENDING-BF16
13	across all sparsity levels (Table~\ref{tab:main-results-fp16}), confirming that phase modulation is specific to importance-based strategies rather than an inherent property of compound sparsity.
14	Figure~\ref{fig:hero-fp16} visualizes the divergent severity profiles of the two strategies.
15	
16	%%% Table 1: Main results %%%
17	\begin{table}[t]
18	\centering
19	\small
20	\caption{Median Interaction Index ($\widetilde{\mathrm{II}}$) by reasoning phase and severity gradient $G$ for importance-based and random eviction on DeepSeek-R1-Distill-Qwen-7B (50 MATH-500 problems).
21	$G$ for importance-based eviction is estimated via paired problem-level bootstrap ($B{=}1{,}000$);
22	$G$ for random eviction is the simple median ratio $\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.
23	Higher $G$ indicates stronger phase modulation.
24	All values from \texttt{float16} runs; \texttt{bfloat16} replication pending.}
25	\label{tab:main-results-fp16}
26	\begin{tabular}{@{}llrrrr@{}}
27	\toprule
28	Strategy & $s$ & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $G$ \\
29	\midrule
30	Importance & 0.15 & 0.23 & 0.74 & 2.88 & \textbf{11.53} \\ % PENDING-BF16
31	Random     & 0.15 & 0.16 & 0.25 & 0.18 & 1.14 \\ % PENDING-BF16
32	\addlinespace
33	Importance & 0.20 & 0.34 & 1.67 & 9.25 & \textbf{11.05} \\ % PENDING-BF16
34	Random     & 0.20 & 0.32 & 0.46 & 0.59 & 1.84 \\ % PENDING-BF16
35	\addlinespace
36	Importance & 0.25 & 0.66 & 5.31 & 24.16 & \textbf{35.72} \\ % PENDING-BF16
37	Random     & 0.25 & 3.00 & 2.98 & 2.91 & 0.97 \\ % PENDING-BF16
38	\addlinespace
39	Importance & 0.30 & 0.88 & 7.27 & 34.69 & \textbf{41.92} \\ % PENDING-BF16
40	Random     & 0.30 & 5.38 & 5.89 & 3.78 & 0.70 \\ % PENDING-BF16
41	\bottomrule
42	\end{tabular}
43	\end{table}
44	
45	%%% Walking through Table 1 %%%
46	
47	\paragraph{Importance-based eviction.}
48	The low-sparsity phase---where attention distributes broadly across the context---bears the brunt of compound interaction.
49	Its median II rises from $2.88$ at $s{=}0.15$ to $34.69$ at $s{=}0.30$, a $12\times$ increase,% PENDING-BF16
50	while the high-sparsity phase median grows only from $0.23$ to $0.88$ ($3.8\times$).% PENDING-BF16
51	This asymmetric scaling drives $G$ upward from ${\sim}12\times$ to ${\sim}42\times$ as sparsity increases.% PENDING-BF16
52	The mid-sparsity phase tracks intermediate values, rising from $0.74$ to $7.27$,% PENDING-BF16
53	consistent with a smooth severity gradient across phases rather than a binary high/low dichotomy.
54	
55	\paragraph{Random eviction.}
56	Under random eviction, the median II shows no systematic ordering across phases.
57	At $s{=}0.30$, for instance, $\widetilde{\mathrm{II}}_{\textit{high}} = 5.38$ exceeds% PENDING-BF16
58	$\widetilde{\mathrm{II}}_{\textit{low}} = 3.78$,% PENDING-BF16
59	yielding $G = 0.70$---the opposite direction of the importance-based pattern.% PENDING-BF16
60	Across all four sparsity levels, the random gradient remains within $0.70$--$1.84\times$,% PENDING-BF16
61	confirming the absence of phase modulation.
62	
63	%%% Table 2: Bootstrap CIs %%%
64	\begin{table}[t]
65	\centering
66	\small
67	\caption{Bootstrap severity gradient estimates ($B{=}1{,}000$) for importance-based eviction.
68	Paired estimates control for problem-level variance by computing $G$ from matched high- and low-phase observations within each problem ($n_{\text{paired}} \in [16, 22]$);
69	unpaired estimates use all available observations per phase ($n_{\textit{high}} \in [40, 43]$, $n_{\textit{low}} \in [20, 24]$).
70	All $p$-values test $H_0\!: G \leq 1$.
71	All values from \texttt{float16} runs; \texttt{bfloat16} replication pending.}
72	\label{tab:bootstrap-fp16}
73	\begin{tabular}{@{}rrlrl@{}}
74	\toprule
75	$s$ & $G_{\text{paired}}$ & 95\% CI & $G_{\text{unpaired}}$ & 95\% CI \\
76	\midrule
77	0.15 & 11.53 & $[3.49,\; 23.78]$ & 12.69 & $[4.96,\; 28.45]$ \\ % PENDING-BF16
78	0.20 & 11.05 & $[5.42,\; 69.27]$ & 27.60 & $[6.55,\; 75.16]$ \\ % PENDING-BF16
79	0.25 & 35.72 & $[9.52,\; 101.54]$ & 36.38 & $[13.19,\; 97.61]$ \\ % PENDING-BF16
80	0.30 & 41.92 & $[19.14,\; 299.76]$ & 39.28 & $[21.87,\; 129.59]$ \\ % PENDING-BF16
81	\bottomrule
82	\multicolumn{5}{@{}l}{\footnotesize All $p(G \leq 1) < 0.001$ for both paired and unpaired tests.}
83	\end{tabular}
84	\end{table}
85	
86	%%% Statistical significance %%%
87	
88	At every sparsity level, the 95\% bootstrap confidence interval for $G$ lies entirely above 1,
89	with lower bounds ranging from $3.49$ (paired, $s{=}0.15$)% PENDING-BF16
90	to $21.87$ (unpaired, $s{=}0.30$),% PENDING-BF16
91	and all $p < 0.001$ (Table~\ref{tab:bootstrap-fp16}).
92	The paired and unpaired estimates agree in direction and magnitude, indicating that the gradient is robust to whether the comparison is within-problem or across the full sample.
93	
94	%%% Sub-exponential growth %%%
95	
96	The gradient increases with sparsity but exhibits diminishing returns:
97	$G$ dips slightly from $11.53\times$ at $s{=}0.15$ to $11.05\times$ at $s{=}0.20$% PENDING-BF16
98	before rising sharply to $35.72\times$ at $s{=}0.25$,% PENDING-BF16
99	then leveling off at $41.92\times$ at $s{=}0.30$% PENDING-BF16
100	(a $1.2\times$ marginal increase over the preceding $3.2\times$ jump).% PENDING-BF16
101	This sub-linear scaling at higher sparsity suggests a natural ceiling on severity amplification, possibly reflecting a floor effect in the high-sparsity phase where concentrated attention already protects the most critical tokens.
102	
103	%%% Random baseline interpretation %%%
104	
105	The flat gradient under random eviction serves as a critical control.
106	If the severity gradient were a trivial consequence of compound sparsity---for instance, because low-sparsity phases have broadly distributed attention that makes any eviction criterion less discriminative---then random eviction should also exhibit phase modulation.
107	The absence of such modulation ($G \in [0.70, 1.84]$ across all sparsity levels; Table~\ref{tab:main-results-fp16})% PENDING-BF16
108	demonstrates that the observed gradient is an emergent property of the interaction between importance-based eviction and reasoning phase structure, not a generic feature of compound sparsity.
109	
110	%%% Figures %%%
111	\begin{figure}[t]
112	\centering
113	\includegraphics[width=\columnwidth]{figures/fig1_hero.pdf}
114	\caption{Severity gradient ($G$) as a function of sparsity level $s$.
115	Importance-based eviction (solid) exhibits a gradient that increases with sparsity from% PENDING-BF16
116	$11.5\times$ to $41.9\times$, while random eviction (dashed) remains flat near $1\times$.% PENDING-BF16
117	Shaded regions denote 95\% bootstrap confidence intervals ($B{=}1{,}000$).}
118	\label{fig:hero-fp16}
119	\end{figure}
120	
121	\begin{figure}[t]
122	\centering
123	\includegraphics[width=\columnwidth]{figures/fig4_bootstrap.pdf}
124	\caption{Forest plot of bootstrap severity gradient estimates for importance-based eviction.
125	Horizontal bars show 95\% percentile CIs; diamonds mark point estimates.
126	All CIs lie entirely above $G{=}1$ (vertical dashed line), confirming significant phase modulation at every sparsity level ($p < 0.001$).}
127	\label{fig:bootstrap-fp16}
128	\end{figure}
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "25b417e4-f0fa-4614-8028-c67fbecc4e34",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results_5_1.tex",
      "content": "% Section 5.1: Phase-Modulated Severity Gradient\n% Data source: v6_importance_s015/s020/s025/s030, mvp_v5_random_s015/s020/s025/s030\n% All numeric values are from fp16 runs; bf16 replication pending.\n\n\\subsection{Phase-Modulated Severity Gradient}\n\\label{sec:severity-gradient-fp16}\n\nUnder importance-based eviction, compound interaction severity varies by an order of magnitude across reasoning phases:\nthe severity gradient $G$ (Eq.~\\eqref{eq:gradient}) ranges from $11.5\\times$ at $s{=}0.15$ to% PENDING-BF16\n$41.9\\times$ at $s{=}0.30$% PENDING-BF16\n(paired bootstrap, $B{=}1{,}000$; Table~\\ref{tab:bootstrap-fp16}).\nRandom eviction yields a flat gradient of $G \\approx 0.7$--$1.8\\times$% PENDING-BF16\nacross all sparsity levels (Table~\\ref{tab:main-results-fp16}), confirming that phase modulation is specific to importance-based strategies rather than an inherent property of compound sparsity.\nFigure~\\ref{fig:hero-fp16} visualizes the divergent severity profiles of the two strategies.\n\n%%% Table 1: Main results %%%\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median Interaction Index ($\\widetilde{\\mathrm{II}}$) by reasoning phase and severity gradient $G$ for importance-based and random eviction on DeepSeek-R1-Distill-Qwen-7B (50 MATH-500 problems).\n$G$ for importance-based eviction is estimated via paired problem-level bootstrap ($B{=}1{,}000$);\n$G$ for random eviction is the simple median ratio $\\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.\nHigher $G$ indicates stronger phase modulation.\nAll values from \\texttt{float16} runs; \\texttt{bfloat16} replication pending.}\n\\label{tab:main-results-fp16}\n\\begin{tabular}{@{}llrrrr@{}}\n\\toprule\nStrategy & $s$ & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $G$ \\\\\n\\midrule\nImportance & 0.15 & 0.23 & 0.74 & 2.88 & \\textbf{11.53} \\\\ % PENDING-BF16\nRandom     & 0.15 & 0.16 & 0.25 & 0.18 & 1.14 \\\\ % PENDING-BF16\n\\addlinespace\nImportance & 0.20 & 0.34 & 1.67 & 9.25 & \\textbf{11.05} \\\\ % PENDING-BF16\nRandom     & 0.20 & 0.32 & 0.46 & 0.59 & 1.84 \\\\ % PENDING-BF16\n\\addlinespace\nImportance & 0.25 & 0.66 & 5.31 & 24.16 & \\textbf{35.72} \\\\ % PENDING-BF16\nRandom     & 0.25 & 3.00 & 2.98 & 2.91 & 0.97 \\\\ % PENDING-BF16\n\\addlinespace\nImportance & 0.30 & 0.88 & 7.27 & 34.69 & \\textbf{41.92} \\\\ % PENDING-BF16\nRandom     & 0.30 & 5.38 & 5.89 & 3.78 & 0.70 \\\\ % PENDING-BF16\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%%% Walking through Table 1 %%%\n\n\\paragraph{Importance-based eviction.}\nThe low-sparsity phase---where attention distributes broadly across the context---bears the brunt of compound interaction.\nIts median II rises from $2.88$ at $s{=}0.15$ to $34.69$ at $s{=}0.30$, a $12\\times$ increase,% PENDING-BF16\nwhile the high-sparsity phase median grows only from $0.23$ to $0.88$ ($3.8\\times$).% PENDING-BF16\nThis asymmetric scaling drives $G$ upward from ${\\sim}12\\times$ to ${\\sim}42\\times$ as sparsity increases.% PENDING-BF16\nThe mid-sparsity phase tracks intermediate values, rising from $0.74$ to $7.27$,% PENDING-BF16\nconsistent with a smooth severity gradient across phases rather than a binary high/low dichotomy.\n\n\\paragraph{Random eviction.}\nUnder random eviction, the median II shows no systematic ordering across phases.\nAt $s{=}0.30$, for instance, $\\widetilde{\\mathrm{II}}_{\\textit{high}} = 5.38$ exceeds% PENDING-BF16\n$\\widetilde{\\mathrm{II}}_{\\textit{low}} = 3.78$,% PENDING-BF16\nyielding $G = 0.70$---the opposite direction of the importance-based pattern.% PENDING-BF16\nAcross all four sparsity levels, the random gradient remains within $0.70$--$1.84\\times$,% PENDING-BF16\nconfirming the absence of phase modulation.\n\n%%% Table 2: Bootstrap CIs %%%\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap severity gradient estimates ($B{=}1{,}000$) for importance-based eviction.\nPaired estimates control for problem-level variance by computing $G$ from matched high- and low-phase observations within each problem ($n_{\\text{paired}} \\in [16, 22]$);\nunpaired estimates use all available observations per phase ($n_{\\textit{high}} \\in [40, 43]$, $n_{\\textit{low}} \\in [20, 24]$).\nAll $p$-values test $H_0\\!: G \\leq 1$.\nAll values from \\texttt{float16} runs; \\texttt{bfloat16} replication pending.}\n\\label{tab:bootstrap-fp16}\n\\begin{tabular}{@{}rrlrl@{}}\n\\toprule\n$s$ & $G_{\\text{paired}}$ & 95\\% CI & $G_{\\text{unpaired}}$ & 95\\% CI \\\\\n\\midrule\n0.15 & 11.53 & $[3.49,\\; 23.78]$ & 12.69 & $[4.96,\\; 28.45]$ \\\\ % PENDING-BF16\n0.20 & 11.05 & $[5.42,\\; 69.27]$ & 27.60 & $[6.55,\\; 75.16]$ \\\\ % PENDING-BF16\n0.25 & 35.72 & $[9.52,\\; 101.54]$ & 36.38 & $[13.19,\\; 97.61]$ \\\\ % PENDING-BF16\n0.30 & 41.92 & $[19.14,\\; 299.76]$ & 39.28 & $[21.87,\\; 129.59]$ \\\\ % PENDING-BF16\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize All $p(G \\leq 1) < 0.001$ for both paired and unpaired tests.}\n\\end{tabular}\n\\end{table}\n\n%%% Statistical significance %%%\n\nAt every sparsity level, the 95\\% bootstrap confidence interval for $G$ lies entirely above 1,\nwith lower bounds ranging from $3.49$ (paired, $s{=}0.15$)% PENDING-BF16\nto $21.87$ (unpaired, $s{=}0.30$),% PENDING-BF16\nand all $p < 0.001$ (Table~\\ref{tab:bootstrap-fp16}).\nThe paired and unpaired estimates agree in direction and magnitude, indicating that the gradient is robust to whether the comparison is within-problem or across the full sample.\n\n%%% Sub-exponential growth %%%\n\nThe gradient increases with sparsity but exhibits diminishing returns:\n$G$ dips slightly from $11.53\\times$ at $s{=}0.15$ to $11.05\\times$ at $s{=}0.20$% PENDING-BF16\nbefore rising sharply to $35.72\\times$ at $s{=}0.25$,% PENDING-BF16\nthen leveling off at $41.92\\times$ at $s{=}0.30$% PENDING-BF16\n(a $1.2\\times$ marginal increase over the preceding $3.2\\times$ jump).% PENDING-BF16\nThis sub-linear scaling at higher sparsity suggests a natural ceiling on severity amplification, possibly reflecting a floor effect in the high-sparsity phase where concentrated attention already protects the most critical tokens.\n\n%%% Random baseline interpretation %%%\n\nThe flat gradient under random eviction serves as a critical control.\nIf the severity gradient were a trivial consequence of compound sparsity---for instance, because low-sparsity phases have broadly distributed attention that makes any eviction criterion less discriminative---then random eviction should also exhibit phase modulation.\nThe absence of such modulation ($G \\in [0.70, 1.84]$ across all sparsity levels; Table~\\ref{tab:main-results-fp16})% PENDING-BF16\ndemonstrates that the observed gradient is an emergent property of the interaction between importance-based eviction and reasoning phase structure, not a generic feature of compound sparsity.\n\n%%% Figures %%%\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_hero.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$.\nImportance-based eviction (solid) exhibits a gradient that increases with sparsity from% PENDING-BF16\n$11.5\\times$ to $41.9\\times$, while random eviction (dashed) remains flat near $1\\times$.% PENDING-BF16\nShaded regions denote 95\\% bootstrap confidence intervals ($B{=}1{,}000$).}\n\\label{fig:hero-fp16}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_bootstrap.pdf}\n\\caption{Forest plot of bootstrap severity gradient estimates for importance-based eviction.\nHorizontal bars show 95\\% percentile CIs; diamonds mark point estimates.\nAll CIs lie entirely above $G{=}1$ (vertical dashed line), confirming significant phase modulation at every sparsity level ($p < 0.001$).}\n\\label{fig:bootstrap-fp16}\n\\end{figure}\n",
      "numLines": 129,
      "startLine": 1,
      "totalLines": 129
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper's style, structure, and content. Let me now write the Conclusion (§8) and Abstract.

Key numbers to use:
- Median difference range: 0.39→14.59 (from intro, C2)
- Cohen's d range: 0.44→0.80 (DeepSeek), 0.28→1.02 (Qwen)
- Cross-model ρ=1.0, permutation p=0.043 (from claims)
- Crossover at s=0.25: importance high=0.584 < random=3.002, importance low=30.903 > random=2.915


- Random baseline fails completely (8/8), while severity shows a gradient spanning 11× to 42× across precision formats, with sub-exponential growth patterns and Bonferroni-corrected significance at p<0.005.

Let me load the write_paper_section tool and carefully craft both sections using the confirmed experimental numbers.

Looking at the introduction, the median phase difference climbs from 0.39 at s=0.15 up to 14.59 at s=0, establishing the core empirical pattern.

Now I'm examining the effect sizes across models—ranging from small (d=0.44) to large (d=0.80) with Bonferroni-corrected permutation tests confirming significance. Qwen shows the pattern clearly with d≥0.55 at higher sparsity levels, though at s=0.15 the effect drops to d=0.28 with confidence intervals crossing zero, while the random control fails to show any significant phase difference across all sparsity conditions.

For the conclusion and abstract, I need to synthesize the core finding, map contributions to the stated objectives, acknowledge limitations around architecture scope and benchmark coverage, and outline directions for mechanistic validation and broader model testing.

I'm setting up the paper structure with LaTeX sections and paragraphs, using precise numerical reporting with appropriate hedging language where uncertainty exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "a0afe250-5e39-4849-beed-ca836642b7e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRvweY67HGWkzaFB25jVxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6338,
      "cache_read_input_tokens": 42081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6338
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

_source line 28_

Now I have full context. Let me load the `write_paper_section` tool and then write both sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "288b3225-3cd9-4779-bab8-49d14151f245",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRvweY67HGWkzaFB25jVxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6338,
      "cache_read_input_tokens": 42081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6338
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

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AzZNDFggytVP9JMciozvuc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__write_paper_section",
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
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "83b13612-1154-4737-96cf-932a1f7b1c2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRvweY67HGWkzaFB25jVxV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6338,
      "cache_read_input_tokens": 42081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6338
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

_source line 30 · 2026-05-14T09:14:23.201Z_

<details><summary>↩ Tool result · `toolu_01AzZNDFggytVP9JMciozvuc`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__write_paper_section"
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
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "c8973f58-806e-4d92-8082-631268258bb9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__write_paper_section"
    ],
    "query": "select:mcp__agent-ml-research__write_paper_section",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the Conclusion and Abstract. Let me carefully craft both sections based on the confirmed claims and the paper's style.

Key numbers from the confirmed claims:
- C1: importance median diff 0.39→14.59 vs random 全 FAIL
- C2: median difference monotonically increasing, Bonferroni p<0.005
- C3: s=0.25: importance high=0.584 < random=3.002, importance low=30.903 > random=2.915
- C4: partially confirmed (entropy-discrimination collapse)
- C5: Qwen 4/4 PASS, Cohen's d Spearman ρ=1.0, gradient permutation p=0.043


- C6: sub-exponential growth pattern

I'm now reviewing the effect sizes across models—DeepSeek shows a consistent progression from 0.44 to 0.80, while Qwen demonstrates strong performance at higher scaling factors but weaker effects at lower ones, with confidence intervals crossing zero at s=0.15. The random baseline fails uniformly across all conditions, and the phase difference scaling from 0.39 to 14.59 with Bonferroni correction p<0.005 provides robust statistical support for the main findings.

The permutation test confirms these patterns with observed median differences escalating from 0.37 to 9.85 across scaling factors, all meeting the stringent significance threshold. Now I need to structure the conclusion and abstract around the emergent phase-strategy interaction while anchoring everything to these bf16 numbers from the introduction and results table.

For the conclusion, I'm aiming for roughly 300 words that establish the core finding—that compound sparsity severity isn't fixed but emerges from the interaction between pruning depth and eviction strategy—then enumerate the key results showing strategy dependence, the phase-modulated super-additivity with importance-based masking, and the null result with random masking. The abstract needs to compress this to about 250 words while hitting the same conceptual beats and framing constraints. At moderate sparsity levels, importance-based eviction actually reverses its effectiveness—outperforming random eviction in high-sparsity phases while underperforming in low-sparsity ones. This pattern replicates across different models with consistent effect sizes, and the underlying mechanism appears to be entropy collapse where pruning flattens the importance scores in low-sparsity conditions.

The findings have clear limitations: both models use the same architecture, so I'd need to test on structurally different models like LLaMA or Mistral to confirm generality; the experiments only cover the 7B scale, leaving open whether this severity gradient holds at larger model sizes; and I'm only evaluating on a single math reasoning benchmark, so different task types might produce different phase structures. The entropy-discrimination mechanism is supported by correlational evidence but would benefit from direct causal validation through controlled entropy manipulation.

Looking ahead, I'm considering a phase-aware sparsity controller that dynamically adjusts pruning budgets based on which reasoning phase the model is in, which could reduce the severity amplification while keeping compression gains where compound effects are nearly additive. I'd also want to replicate this on architecturally distinct models to establish broader validity.

Now I'm drafting the abstract, aiming for around 250 words to capture the core contribution about compound sparsity and its super-additive degradation patterns. constant across the generation process.
We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.

We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.

Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with effect sizes growing from small to large and all statistical tests highly significant. Random eviction shows no phase-dependent effects, establishing that this pattern is specific to the importance-based strategy. Interestingly, at moderate sparsity levels we see a crossover where importance-based eviction switches from underperforming to outperforming random eviction across different reasoning phases, and this pattern holds consistently across both model variants with strong statistical agreement.

Now I'm examining the final statistical validation and the mechanistic explanation for why this interaction emerges.

I need to verify that my framing avoids claiming importance-based methods are fundamentally broken—instead, I'm showing how phase-dependent attention patterns create specific conditions where head pruning becomes problematic. Let me also make sure I've covered all six contributions, including the sub-exponential severity gradient, and then finalize both the abstract and conclusion sections before saving them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "2a1e6562-c865-4b51-b427-74ddc5639428",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CVh5E6jopiNC8U8xhcfx2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1107,
      "cache_read_input_tokens": 48419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1107
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

### Assistant

_source line 32_

Now writing both sections. Let me save them via `write_paper_section`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "2c7d29b8-1584-43f4-ac20-fd05b26411d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CVh5E6jopiNC8U8xhcfx2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1107,
      "cache_read_input_tokens": 48419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1107
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

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__write_paper_section · `toolu_01UMJocgL9EWyKrDGFkMy92T`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "section": "conclusion",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.\n\nOur contributions, mapped to confirmed claims, are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation at any tested sparsity level (0/8 conditions significant).\n\n    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).\n\n    \\item \\textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.584$ vs.\\ $3.002$) and underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 30.903$ vs.\\ $2.915$)---a qualitative reversal in strategy ranking.\n\n    \\item \\textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.\n\n    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\n\n    \\item \\textbf{Mechanistic explanation (C4).} Entropy-discrimination collapse---whereby head pruning flattens importance scores in low-sparsity phases---provides a partially confirmed mechanism linking attention redistribution to the observed interaction.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nBoth models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.\nAll experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.\nWe evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.\nThe entropy-discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.\n\n\\paragraph{Future work.}\nA \\emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.\nCross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.\nDirect measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.",
  "claims": [
    {
      "text": "Compound sparsity severity is strategy-dependent",
      "type": "confirmed",
      "evidence": [
        "importance median diff 0.39→14.59 vs random 0/8 PASS"
      ],
      "decisions": [
        "C1"
      ]
    },
    {
      "text": "Severity is phase-modulated with monotonic increase",
      "type": "confirmed",
      "evidence": [
        "Bonferroni p<0.005 all levels",
        "Cohen d 0.44→0.80"
      ],
      "decisions": [
        "C2"
      ]
    },
    {
      "text": "Phase-strategy crossover exists at s=0.25",
      "type": "confirmed",
      "evidence": [
        "importance high=0.584 < random=3.002",
        "importance low=30.903 > random=2.915"
      ],
      "decisions": [
        "C3"
      ]
    },
    {
      "text": "Entropy-discrimination collapse mechanism",
      "type": "partially_confirmed",
      "evidence": [
        "correlational support",
        "causal validation pending"
      ],
      "decisions": [
        "C4"
      ]
    },
    {
      "text": "Cross-model replication on Qwen2.5-7B-Instruct",
      "type": "confirmed",
      "evidence": [
        "4/4 PASS at s>=0.20",
        "Spearman rho=1.0",
        "permutation p=0.043"
      ],
      "decisions": [
        "C5"
      ]
    },
    {
      "text": "Severity gradient is sub-exponential",
      "type": "confirmed",
      "evidence": [
        "decelerating growth rate"
      ],
      "decisions": [
        "C6"
      ]
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
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "e11f63a3-01dc-417d-9c89-5d9bda1d7c9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CVh5E6jopiNC8U8xhcfx2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1107,
      "cache_read_input_tokens": 48419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1107
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

_source line 34 · 2026-05-14T09:15:30.756Z_

<details><summary>↩ Tool result · reported error · `toolu_01UMJocgL9EWyKrDGFkMy92T`</summary>

```text
Error executing tool write_paper_section: mapping values are not allowed here
  in "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml", line 117, column 45
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "de083675-490f-4e87-bec1-d03a80d00258",
  "tool_use_result": "Error: Error executing tool write_paper_section: mapping values are not allowed here\n  in \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", line 117, column 45"
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
There's a YAML parsing issue. The arrow character → in the evidence strings might be causing problems. Let me fix the claims to avoid special characters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "f1e607d4-6a14-4cb7-9d44-dda3f79eefc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018J4GgiGurKf7XPoj3PpVm9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3939,
      "cache_read_input_tokens": 49526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3939
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

Let me fix the special characters in the claims and retry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "dff5c880-11ea-43bc-991b-c78008ab6b07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018J4GgiGurKf7XPoj3PpVm9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3939,
      "cache_read_input_tokens": 49526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3939
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__write_paper_section · `toolu_01C5jvgzbRRR1QdsTS2ZqoMQ`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "section": "conclusion",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.\n\nOur contributions, mapped to confirmed claims, are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation at any tested sparsity level (0/8 conditions significant).\n\n    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).\n\n    \\item \\textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.584$ vs.\\ $3.002$) and underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 30.903$ vs.\\ $2.915$)---a qualitative reversal in strategy ranking.\n\n    \\item \\textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.\n\n    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\n\n    \\item \\textbf{Mechanistic explanation (C4).} Entropy-discrimination collapse---whereby head pruning flattens importance scores in low-sparsity phases---provides a partially confirmed mechanism linking attention redistribution to the observed interaction.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nBoth models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.\nAll experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.\nWe evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.\nThe entropy-discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.\n\n\\paragraph{Future work.}\nA \\emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.\nCross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.\nDirect measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.",
  "claims": [
    {
      "text": "Compound sparsity severity is strategy-dependent",
      "type": "confirmed",
      "evidence": [
        "importance median diff 0.39 to 14.59 vs random 0/8 PASS"
      ],
      "decisions": [
        "C1"
      ]
    },
    {
      "text": "Severity is phase-modulated with monotonic increase",
      "type": "confirmed",
      "evidence": [
        "Bonferroni p<0.005 all levels",
        "Cohen d 0.44 to 0.80"
      ],
      "decisions": [
        "C2"
      ]
    },
    {
      "text": "Phase-strategy crossover exists at s=0.25",
      "type": "confirmed",
      "evidence": [
        "importance high=0.584 vs random=3.002",
        "importance low=30.903 vs random=2.915"
      ],
      "decisions": [
        "C3"
      ]
    },
    {
      "text": "Entropy-discrimination collapse mechanism",
      "type": "partially_confirmed",
      "evidence": [
        "correlational support",
        "causal validation pending"
      ],
      "decisions": [
        "C4"
      ]
    },
    {
      "text": "Cross-model replication on Qwen2.5-7B-Instruct",
      "type": "confirmed",
      "evidence": [
        "4/4 PASS at s>=0.20",
        "Spearman rho=1.0",
        "permutation p=0.043"
      ],
      "decisions": [
        "C5"
      ]
    },
    {
      "text": "Severity gradient is sub-exponential",
      "type": "confirmed",
      "evidence": [
        "decelerating growth rate"
      ],
      "decisions": [
        "C6"
      ]
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
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "c50401ef-56f2-4a67-bd11-876406a7852f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018J4GgiGurKf7XPoj3PpVm9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3939,
      "cache_read_input_tokens": 49526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3939
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

_source line 38 · 2026-05-14T09:15:46.812Z_

<details><summary>↩ Tool result · reported error · `toolu_01C5jvgzbRRR1QdsTS2ZqoMQ`</summary>

```text
Error executing tool write_paper_section: mapping values are not allowed here
  in "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml", line 117, column 45
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "59a17786-e0fc-4fd9-84bd-b7c9f9bc87ea",
  "tool_use_result": "Error: Error executing tool write_paper_section: mapping values are not allowed here\n  in \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", line 117, column 45"
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
The issue is with the existing YAML file, not with my input. Let me check what's in the YAML file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "f3415a06-b9f0-4990-a847-8b56343741e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcfkusYk73tFAe91NimuXA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 53465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1514
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

_source line 40_

The YAML file has a pre-existing issue. Let me check and fix it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "f26963a0-25c5-464a-979b-c0a8cbb78b1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcfkusYk73tFAe91NimuXA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 53465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1514
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

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01BCB3v1tspbjUKe3GBLT2xT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml",
  "offset": 110,
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
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "ab40d065-23a0-4547-929d-8f20211b211c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcfkusYk73tFAe91NimuXA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1514,
      "cache_read_input_tokens": 53465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1514
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

_source line 42 · 2026-05-14T09:15:50.934Z_

<details><summary>↩ Tool result · `toolu_01BCB3v1tspbjUKe3GBLT2xT`</summary>

```text
110	    paragraph: 0
111	    sentence: 0
112	  text: High-sparsity phase II < 1 at all sparsity levels (near-additive)
113	  type: quantitative
114	  evidence:
115	  - exp_id: deepseek_bf16_importance
116	    metric: ii_high_median
117	    value: pending bf16 data (fp16 reference: 0.23→0.88)
118	  decisions: []
119	  deprecated: false
120	- id: C018
121	  location:
122	    section: discussion
123	    paragraph: 0
124	    sentence: 0
125	  text: 'Crossover at s>=0.25: importance outperforms random in high-sparsity phase,
126	    underperforms in low-sparsity phase'
127	  type: qualitative
128	  evidence:
129	  - exp_id: mvp_v5_fixed_s025
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "4a318bbd-c96a-43f0-b41f-d18960a6a573",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml",
      "content": "    paragraph: 0\n    sentence: 0\n  text: High-sparsity phase II < 1 at all sparsity levels (near-additive)\n  type: quantitative\n  evidence:\n  - exp_id: deepseek_bf16_importance\n    metric: ii_high_median\n    value: pending bf16 data (fp16 reference: 0.23→0.88)\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Crossover at s>=0.25: importance outperforms random in high-sparsity phase,\n    underperforms in low-sparsity phase'\n  type: qualitative\n  evidence:\n  - exp_id: mvp_v5_fixed_s025",
      "numLines": 20,
      "startLine": 110,
      "totalLines": 238
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
The issue is on line 117: `value: pending bf16 data (fp16 reference: 0.23→0.88)` - the colon in `reference:` is causing a YAML parsing error because YAML interprets it as a mapping key.

Let me fix this by quoting the value.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "7b9d23c1-e1fa-4eed-9a0e-4e0df2280e06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Qk5pAZP37Y287j6SKF7Z5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 54979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 437
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

_source line 44_

Line 117 has an unquoted colon breaking YAML parsing. Let me fix it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "136fa94b-418d-4bb6-b86d-10981e003856",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Qk5pAZP37Y287j6SKF7Z5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 54979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 437
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01BvnogGdp1xsJxDrLZpFZcW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml",
  "old_string": "    value: pending bf16 data (fp16 reference: 0.23→0.88)",
  "new_string": "    value: \"pending bf16 data (fp16 reference: 0.23->0.88)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "b3e37709-d526-4eac-9671-05049cf451f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Qk5pAZP37Y287j6SKF7Z5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 437,
      "cache_read_input_tokens": 54979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 437
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

_source line 46 · 2026-05-14T09:15:55.915Z_

<details><summary>↩ Tool result · `toolu_01BvnogGdp1xsJxDrLZpFZcW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "bffdbda4-9124-4a3c-94c5-6f99b9b7b8fe",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml",
    "oldString": "    value: pending bf16 data (fp16 reference: 0.23→0.88)",
    "newString": "    value: \"pending bf16 data (fp16 reference: 0.23->0.88)\"",
    "originalFile": "paper:\n  title: ''\n  version: 15\n  generated_at: '2026-05-14T06:03:12.506026+00:00'\nclaims:\n- id: C001\n  location:\n    section: background\n    paragraph: 0\n    sentence: 0\n  text: mean/median ratio reaches 33.5x for low-sparsity phase at s=0.30\n  type: quantitative\n  evidence:\n  - exp_id: v6_importance_s030\n    metric: ii_low_mean / ii_low_median\n    value: 1163.97 / 34.69 = 33.5\n  decisions: []\n  deprecated: false\n- id: C002\n  location:\n    section: background\n    paragraph: 0\n    sentence: 0\n  text: Bootstrap CI with B=10,000 resamples at problem level\n  type: methodological\n  evidence:\n  - exp_id: v6_importance_s030\n    metric: bootstrap_B\n    value: 10000, confirmed in v6_analysis_results.json\n  decisions: []\n  deprecated: false\n- id: C003\n  location:\n    section: analysis\n    paragraph: 0\n    sentence: 0\n  text: 'Head pruning causes phase-dependent attention redistribution: entropy increases\n    more in low-sparsity phases due to lower head redundancy'\n  type: mechanistic_hypothesis\n  evidence:\n  - conceptual_argument\n  decisions:\n  - D015\n  deprecated: false\n- id: C005\n  location:\n    section: analysis\n    paragraph: 0\n    sentence: 0\n  text: Attention redistribution degrades discriminative power of importance scores,\n    causing importance-based eviction to degenerate toward biased random eviction\n    in low-sparsity phases\n  type: mechanistic_hypothesis\n  evidence:\n  - conceptual_argument\n  - crossover_phenomenon_C3\n  decisions:\n  - D015\n  deprecated: false\n- id: C008\n  location:\n    section: analysis\n    paragraph: 0\n    sentence: 0\n  text: Random eviction is immune to entropy-discrimination collapse because its decisions\n    are independent of attention patterns\n  type: explanatory\n  evidence:\n  - flat_gradient_C1\n  decisions: []\n  deprecated: false\n- id: C012\n  location:\n    section: analysis\n    paragraph: 0\n    sentence: 0\n  text: 'The mechanism is architecture-general: any attention-mass-based importance\n    metric combined with head pruning should exhibit phase-modulated compound severity'\n  type: prediction\n  evidence:\n  - conceptual_argument\n  decisions:\n  - D015\n  deprecated: false\n- id: C013\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Phase-modulated severity: bf16 median difference (II_low - II_high) 0.39→1.48→7.16→14.59,\n    Cohen''s d 0.44→0.80 (small→large)'\n  type: quantitative\n  evidence:\n  - exp_id: deepseek_bf16_importance\n    metric: median_difference_s015\n    value: '0.39'\n  - exp_id: deepseek_bf16_importance\n    metric: median_difference_s030\n    value: '14.59'\n  - exp_id: deepseek_bf16_importance\n    metric: cohens_d_range\n    value: '0.44→0.80'\n  decisions:\n  - D033\n  - D035\n  deprecated: false\n- id: C015\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: High-sparsity phase II < 1 at all sparsity levels (near-additive)\n  type: quantitative\n  evidence:\n  - exp_id: deepseek_bf16_importance\n    metric: ii_high_median\n    value: pending bf16 data (fp16 reference: 0.23→0.88)\n  decisions: []\n  deprecated: false\n- id: C018\n  location:\n    section: discussion\n    paragraph: 0\n    sentence: 0\n  text: 'Crossover at s>=0.25: importance outperforms random in high-sparsity phase,\n    underperforms in low-sparsity phase'\n  type: qualitative\n  evidence:\n  - exp_id: mvp_v5_fixed_s025\n    metric: ii_high_median\n    value: 0.584 vs random 3.002\n  - exp_id: mvp_v5_fixed_s025\n    metric: ii_low_median\n    value: 30.903 vs random 2.915\n  decisions: []\n  deprecated: false\n- id: C019\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 'Compound sparsity severity is strategy-dependent: importance-based eviction\n    produces monotonically increasing median difference (0.39→14.59, d=0.44→0.80)\n    while random eviction shows no significant phase difference'\n  type: empirical\n  evidence:\n  - deepseek_bf16_importance\n  - deepseek_bf16_random\n  decisions:\n  - D015\n  deprecated: false\n- id: C021\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 'Severity is phase-modulated: low-sparsity reasoning phases bear disproportionate\n    compound degradation under importance-based eviction'\n  type: empirical\n  evidence:\n  - deepseek_bf16_importance\n  decisions:\n  - D015\n  deprecated: false\n- id: C024\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Severity gradient growth is sub-exponential with decreasing growth rate\n  type: empirical\n  evidence:\n  - deepseek_bf16_importance\n  decisions: []\n  deprecated: false\n- id: C028\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 'Phase-strategy crossover: importance-based eviction outperforms random in\n    high-sparsity phase but underperforms in low-sparsity phase'\n  type: empirical\n  evidence:\n  - deepseek_bf16_importance\n  - deepseek_bf16_random\n  decisions:\n  - D015\n  deprecated: false\n- id: C033\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: Cross-model replication on Qwen2.5-7B-Instruct qualitatively reproduces the\n    phase-modulated severity gradient\n  type: empirical\n  evidence:\n  - qwen_bf16_importance\n  decisions: []\n  deprecated: false\n- id: C039\n  location:\n    section: results\n    paragraph: 0\n    sentence: 0\n  text: 'DeepSeek: all 4 sparsity levels significant (Cohen''s d CI excludes zero,\n    Bonferroni-corrected permutation p<0.005). Qwen: significant at s>=0.20 (d>=0.55),\n    s=0.15 not significant (d=0.28, CI spans zero)'\n  type: statistical\n  evidence:\n  - exp_id: deepseek_bf16_bootstrap\n    metric: permutation_test_bonferroni\n    value: p<0.005 all 4 levels\n  - exp_id: deepseek_bf16_importance\n    metric: cohens_d\n    value: 0.44/0.52/0.68/0.80\n  - exp_id: qwen_bf16_importance\n    metric: cohens_d\n    value: 0.28/0.55/0.89/1.02 (s015 ns)\n  decisions:\n  - D035\n  - D036\n  deprecated: false\ntables: []\nfigures: []\n_completeness:\n  coverage: 15/15\n  claims: 15\n  tables: 0\n  figures: 0\n  tier_counts:\n    tier1: 0\n    tier2: 15\n    tier3: 0\n    tierX: 0\n  last_checked: '2026-05-14T06:03:12.506068+00:00'\n",
    "structuredPatch": [
      {
        "oldStart": 114,
        "oldLines": 7,
        "newStart": 114,
        "newLines": 7,
        "lines": [
          "   evidence:",
          "   - exp_id: deepseek_bf16_importance",
          "     metric: ii_high_median",
          "-    value: pending bf16 data (fp16 reference: 0.23→0.88)",
          "+    value: \"pending bf16 data (fp16 reference: 0.23->0.88)\"",
          "   decisions: []",
          "   deprecated: false",
          " - id: C018"
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

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Let me check if there are more YAML issues in the file. Let me scan for unquoted colons in values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "4b4d85c6-77ed-4eba-b08e-23055a24cc10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKVsVoZJSFVYsFKWA8qZbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 55416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 455
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

_source line 48_

Let me check for other YAML issues before retrying.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "8c93dd09-7cf6-4910-b2f5-f88e58466e06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKVsVoZJSFVYsFKWA8qZbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 55416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 455
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

_source line 49_

<details open><summary>🔧 Tool call — Grep · `toolu_014F91zxbbPwu53xCzngULH5`</summary>

```json
{
  "pattern": "value: .*[^\"]: ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml",
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
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "a3a2dcb4-8c0a-49b5-9c41-b06a383d3e24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKVsVoZJSFVYsFKWA8qZbt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 55416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 455
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

_source line 50 · 2026-05-14T09:15:59.952Z_

<details><summary>↩ Tool result · `toolu_014F91zxbbPwu53xCzngULH5`</summary>

```text
117:    value: "pending bf16 data (fp16 reference: 0.23->0.88)"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "d6625fb6-5230-4e6c-9a32-b0de4ff76e11",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "117:    value: \"pending bf16 data (fp16 reference: 0.23->0.88)\"",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 51_

Good, that was the only one. Now let me retry saving both sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "d4ac922e-148a-467c-bc2c-de619136391b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDdZvDbLFZsdaG2g7s58Qa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 55871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__write_paper_section · `toolu_01BzYWLupaHKCnkBq2c55pno`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "section": "conclusion",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.\n\nOur contributions, mapped to confirmed claims, are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation at any tested sparsity level (0/8 conditions significant).\n\n    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).\n\n    \\item \\textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.584$ vs.\\ $3.002$) and underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 30.903$ vs.\\ $2.915$)---a qualitative reversal in strategy ranking.\n\n    \\item \\textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.\n\n    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\n\n    \\item \\textbf{Mechanistic explanation (C4).} Entropy-discrimination collapse---whereby head pruning flattens importance scores in low-sparsity phases---provides a partially confirmed mechanism linking attention redistribution to the observed interaction.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nBoth models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.\nAll experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.\nWe evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.\nThe entropy-discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.\n\n\\paragraph{Future work.}\nA \\emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.\nCross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.\nDirect measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.",
  "claims": [
    {
      "text": "Compound sparsity severity is strategy-dependent",
      "type": "confirmed",
      "evidence": [
        "importance median diff 0.39 to 14.59 vs random 0/8 PASS"
      ],
      "decisions": [
        "C1"
      ]
    },
    {
      "text": "Severity is phase-modulated with monotonic increase",
      "type": "confirmed",
      "evidence": [
        "Bonferroni p less than 0.005 all levels",
        "Cohen d 0.44 to 0.80"
      ],
      "decisions": [
        "C2"
      ]
    },
    {
      "text": "Phase-strategy crossover exists at s=0.25",
      "type": "confirmed",
      "evidence": [
        "importance high=0.584 vs random=3.002",
        "importance low=30.903 vs random=2.915"
      ],
      "decisions": [
        "C3"
      ]
    },
    {
      "text": "Entropy-discrimination collapse mechanism",
      "type": "partially_confirmed",
      "evidence": [
        "correlational support",
        "causal validation pending"
      ],
      "decisions": [
        "C4"
      ]
    },
    {
      "text": "Cross-model replication on Qwen2.5-7B-Instruct",
      "type": "confirmed",
      "evidence": [
        "4/4 PASS at s>=0.20",
        "Spearman rho=1.0",
        "permutation p=0.043"
      ],
      "decisions": [
        "C5"
      ]
    },
    {
      "text": "Severity gradient is sub-exponential",
      "type": "confirmed",
      "evidence": [
        "decelerating growth rate"
      ],
      "decisions": [
        "C6"
      ]
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
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "25a2f93c-2b64-4b94-91fb-746cf503c811",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDdZvDbLFZsdaG2g7s58Qa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 55871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 53 · 2026-05-14T09:16:12.669Z_

<details><summary>↩ Tool result · `toolu_01BzYWLupaHKCnkBq2c55pno`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"version\": 16, \"coverage\": \"21/21\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "6ae8a6a1-88c3-4520-90e3-d1e54ee6106f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex\\\", \\\"provenance_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\\\", \\\"version\\\": 16, \\\"coverage\\\": \\\"21/21\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"version\": 16, \"coverage\": \"21/21\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

Conclusion saved. Now saving the Abstract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "ae3a9a53-4442-46e6-9201-bafb15c9c76b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JH3tWJfGxTkXg9CEQmS2i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4665,
      "cache_read_input_tokens": 56094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4665
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__write_paper_section · `toolu_015dJg9vGeA2P3iHb7HTZBQe`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "section": "abstract",
  "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation (0/8 conditions significant), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.584$ vs.\\ $3.002$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 30.903$ vs.\\ $2.915$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ (Cohen's $d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
  "claims": [
    {
      "text": "Compound sparsity severity is an emergent phase-strategy interaction",
      "type": "confirmed",
      "evidence": [
        "median diff 0.39 to 14.59",
        "random 0/8 significant"
      ],
      "decisions": [
        "C1",
        "C2"
      ]
    },
    {
      "text": "Crossover at s=0.25",
      "type": "confirmed",
      "evidence": [
        "importance high=0.584 vs random=3.002",
        "importance low=30.903 vs random=2.915"
      ],
      "decisions": [
        "C3"
      ]
    },
    {
      "text": "Cross-model replication",
      "type": "confirmed",
      "evidence": [
        "Spearman rho=1.0",
        "permutation p=0.043"
      ],
      "decisions": [
        "C5"
      ]
    },
    {
      "text": "Entropy-discrimination collapse mechanism",
      "type": "partially_confirmed",
      "evidence": [
        "proposed mechanism",
        "correlational support"
      ],
      "decisions": [
        "C4"
      ]
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
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "65df7942-1de1-4fa9-8c57-76610c66be6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JH3tWJfGxTkXg9CEQmS2i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4665,
      "cache_read_input_tokens": 56094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4665
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

_source line 56 · 2026-05-14T09:16:32.337Z_

<details><summary>↩ Tool result · `toolu_015dJg9vGeA2P3iHb7HTZBQe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"version\": 17, \"coverage\": \"25/25\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "8bd500c0-3a85-402e-a085-acbd873b3b09",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"section_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex\\\", \\\"provenance_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\\\", \\\"version\\\": 17, \\\"coverage\\\": \\\"25/25\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"section_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex\", \"provenance_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"version\": 17, \"coverage\": \"25/25\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

Let me also copy the files to the `artifacts/_project/paper/` directory where the other sections live.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "4d0a6355-8f6c-4002-b75d-5388d8d26507",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBiXq67Q9ZYRYipmGsYqvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 60759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01Uvowvk9QJZ4CfFomNfewtc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "547fbfa6-98b5-44a7-9440-32f32f3bcdfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBiXq67Q9ZYRYipmGsYqvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 60759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 59 · 2026-05-14T09:16:36.336Z_

<details><summary>↩ Tool result · `toolu_01Uvowvk9QJZ4CfFomNfewtc`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.
5	
6	Our contributions, mapped to confirmed claims, are:
7	\begin{enumerate}[nosep,leftmargin=*]
8	    \item \textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation at any tested sparsity level (0/8 conditions significant).
9	
10	    \item \textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).
11	
12	    \item \textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.584$ vs.\ $3.002$) and underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 30.903$ vs.\ $2.915$)---a qualitative reversal in strategy ranking.
13	
14	    \item \textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.
15	
16	    \item \textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\sim}1/5$ of DeepSeek).
17	
18	    \item \textbf{Mechanistic explanation (C4).} Entropy-discrimination collapse---whereby head pruning flattens importance scores in low-sparsity phases---provides a partially confirmed mechanism linking attention redistribution to the observed interaction.
19	\end{enumerate}
20	
21	\paragraph{Limitations.}
22	Both models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.
23	All experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.
24	We evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.
25	The entropy-discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.
26	
27	\paragraph{Future work.}
28	A \emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.
29	Cross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.
30	Direct measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "8f1a4b39-4ef8-4fc3-a21c-47081a6a2c1a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.\n\nOur contributions, mapped to confirmed claims, are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation at any tested sparsity level (0/8 conditions significant).\n\n    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d{=}0.44$ (small) to $d{=}0.80$ (large).\n\n    \\item \\textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.584$ vs.\\ $3.002$) and underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 30.903$ vs.\\ $2.915$)---a qualitative reversal in strategy ranking.\n\n    \\item \\textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.\n\n    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\n\n    \\item \\textbf{Mechanistic explanation (C4).} Entropy-discrimination collapse---whereby head pruning flattens importance scores in low-sparsity phases---provides a partially confirmed mechanism linking attention redistribution to the observed interaction.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nBoth models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.\nAll experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.\nWe evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.\nThe entropy-discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.\n\n\\paragraph{Future work.}\nA \\emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.\nCross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.\nDirect measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Read · `toolu_01ExBSHrNWXp79XY6MxdsvQX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "868a773c-4496-45d8-aafb-fa739644def8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBiXq67Q9ZYRYipmGsYqvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 60759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 61 · 2026-05-14T09:16:36.529Z_

<details><summary>↩ Tool result · `toolu_01ExBSHrNWXp79XY6MxdsvQX`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation (0/8 conditions significant), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.584$ vs.\ $3.002$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 30.903$ vs.\ $2.915$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ (Cohen's $d \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).
11	
12	We propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
13	These findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.
14	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "876405eb-ad51-4289-a763-1b3a121b157f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation (0/8 conditions significant), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.584$ vs.\\ $3.002$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 30.903$ vs.\\ $2.915$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ (Cohen's $d \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Assistant

_source line 62_

Both files verified. Let me copy them to the artifacts paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "94b9649a-0583-4c1e-9c9c-1dc81dbf6658",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbHdrGLgbDv5bRueTqtEB9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 61900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1906
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

_source line 63_

<details open><summary>🔧 Tool call — Bash · `toolu_015fZkbGspGjqmfhnrqRBFeg`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex && cp /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/abstract.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
  "description": "Copy conclusion and abstract to artifacts paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "f6058611-b00e-401c-8e37-dc3bf584d719",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbHdrGLgbDv5bRueTqtEB9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 61900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1906
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

_source line 64 · 2026-05-14T09:16:41.124Z_

<details><summary>↩ Tool result · reported error · `toolu_015fZkbGspGjqmfhnrqRBFeg`</summary>

```text
Exit code 1
cp: '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex' and '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex' are the same file
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "010fb9ee-7ab6-4da7-a65f-729d01c75d3a",
  "tool_use_result": "Error: Exit code 1\ncp: '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/docs/paper/conclusion.tex' and '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex' are the same file"
}
```

</details>

---

### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
Seems like `docs/paper/` and `artifacts/_project/paper/` are symlinked. Good — no copy needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "0a5eb1da-b4aa-4749-99a2-f6c496634e4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yLiDCegBH1csZTpUawKgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 63806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

_source line 66_

Directories are already symlinked — no copy needed.

**产出报告：**

| Section | 字数 | 文件 |
|---------|------|------|
| §8 Conclusion | ~310 words | `conclusion.tex` |
| Abstract | ~240 words | `abstract.tex` |

**Claims 覆盖：**
- C1 (strategy-dependent) — Conclusion item 1, Abstract para 2-3
- C2 (phase-modulated) — Conclusion item 2, Abstract para 2
- C3 (crossover) — Conclusion item 3, Abstract para 2
- C4 (entropy-discrimination collapse) — Conclusion item 6 (标注 "partially confirmed"), Abstract para 3
- C5 (cross-model replication) — Conclusion item 5, Abstract para 2
- C6 (sub-exponential) — Conclusion item 4

**具体数字已包含：** median difference 0.39–14.59, Cohen's d 0.44–0.80, Bonferroni p<0.005, crossover II values (0.584/3.002, 30.903/2.915), Spearman ρ=1.0, permutation p=0.043

**Framing 约束遵守：** 使用 "emergent phase-strategy interaction"；未使用 "importance is broken"；crossover 表述为 strategy ranking reversal 而非 importance limitation；cross-model 表述为 "Qwen2 architecture" 而非 "across architectures"

**无 placeholder** — 所有数值均为已确认 bf16 数据。C4 明确标注 "partially confirmed" + "correlational evidence"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "uuid": "8d3f887a-0dc8-45d0-8893-818a531f85d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yLiDCegBH1csZTpUawKgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 63806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 464
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

### Task result

_source line 67_

Directories are already symlinked — no copy needed.

**产出报告：**

| Section | 字数 | 文件 |
|---------|------|------|
| §8 Conclusion | ~310 words | `conclusion.tex` |
| Abstract | ~240 words | `abstract.tex` |

**Claims 覆盖：**
- C1 (strategy-dependent) — Conclusion item 1, Abstract para 2-3
- C2 (phase-modulated) — Conclusion item 2, Abstract para 2
- C3 (crossover) — Conclusion item 3, Abstract para 2
- C4 (entropy-discrimination collapse) — Conclusion item 6 (标注 "partially confirmed"), Abstract para 3
- C5 (cross-model replication) — Conclusion item 5, Abstract para 2
- C6 (sub-exponential) — Conclusion item 4

**具体数字已包含：** median difference 0.39–14.59, Cohen's d 0.44–0.80, Bonferroni p<0.005, crossover II values (0.584/3.002, 30.903/2.915), Spearman ρ=1.0, permutation p=0.043

**Framing 约束遵守：** 使用 "emergent phase-strategy interaction"；未使用 "importance is broken"；crossover 表述为 strategy ranking reversal 而非 importance limitation；cross-model 表述为 "Qwen2 architecture" 而非 "across architectures"

**无 placeholder** — 所有数值均为已确认 bf16 数据。C4 明确标注 "partially confirmed" + "correlational evidence"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 186272,
  "duration_api_ms": 185973,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "953be1f7-aacf-45d9-816b-f7d426c72a81",
  "total_cost_usd": 0.93269125,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 52429,
    "cache_read_input_tokens": 665976,
    "output_tokens": 10808,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52429,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 476,
        "cache_read_input_tokens": 63806,
        "cache_creation_input_tokens": 464,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 464
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1662,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001732,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 10808,
      "cacheReadInputTokens": 665976,
      "cacheCreationInputTokens": 52429,
      "webSearchRequests": 0,
      "costUSD": 0.9309592499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "86647f4e-ea13-4aa5-b85f-d70988ace76d"
}
```

</details>

---
