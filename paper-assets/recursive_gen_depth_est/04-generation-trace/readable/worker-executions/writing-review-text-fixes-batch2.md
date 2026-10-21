# writing review text fixes batch2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_writing_review-text-fixes-batch2_20260515T220651.log`
- **Structured JSON:** [`8d47179b7724d583ebda.json`](../../sessions/8d/8d47179b7724d583ebda.json)

## Before a recorded user message

58 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
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
  "uuid": "1de9233f-3c4b-4d6a-ba23-9aa7fdd810e1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/memory/"
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
    "resetsAt": 1778885400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6c1461e2-167b-4da8-9aec-160f6c57ace4",
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a"
}
```

---

### Assistant

_source line 4_

I'll start by reading the paper files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "f26e7951-1adb-4bce-aa2c-08ddc10abfe0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189QTV1Zri3ij42mBJiytYm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11850
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

<details open><summary>🔧 Tool call — Bash · `toolu_01LUjkrSn7ezvcbE3G9JzsSQ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "32dc178b-7bda-4aa0-a429-5f26f3df3e84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189QTV1Zri3ij42mBJiytYm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11850
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

_source line 6 · 2026-05-15T22:07:04.268Z_

<details><summary>↩ Tool result · `toolu_01LUjkrSn7ezvcbE3G9JzsSQ`</summary>

```text
_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
atlas.tex
conclusion.tex
discussion.tex
figures
generalization.tex
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex
section_appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "00e864b1-0434-452b-9549-9d62d11ac2bb",
  "tool_use_result": {
    "stdout": "_pdf_images\nabstract.tex\nacl.sty\nacl_natbib.bst\natlas.tex\nconclusion.tex\ndiscussion.tex\nfigures\ngeneralization.tex\nintroduction.tex\nmain.aux\nmain.bbl\nmain.blg\nmain.fdb_latexmk\nmain.fls\nmain.log\nmain.out\nmain.pdf\nmain.tex\nmethod.tex\nreferences.bib\nrelated_work.tex\nsection_appendix.tex",
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

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01LQ4ykVLWzrY2vCD4TtdUMm`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/ -name \"*.tex\" -o -name \"*.bib\" | sort",
  "description": "Find all tex and bib files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "5e0ebb52-e0e6-45e6-bd52-4fc225218d30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189QTV1Zri3ij42mBJiytYm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11850,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11850
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

_source line 8 · 2026-05-15T22:07:04.994Z_

<details><summary>↩ Tool result · `toolu_01LQ4ykVLWzrY2vCD4TtdUMm`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "aa56a550-ed53-4180-9611-37aaf7be0faf",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
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

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01Xbpe4o2WwULC53Cpefqa9Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "561cd5cf-543b-472d-8f41-876bc575c016",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113XxxRQ9mq9rxHffo1SweX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 23691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 829
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

_source line 10 · 2026-05-15T22:07:08.296Z_

<details><summary>↩ Tool result · `toolu_01Xbpe4o2WwULC53Cpefqa9Y`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
30	For depth extension experiments (\S\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.
31	
32	\paragraph{Generation pipeline.}
33	Starting from a Wikipedia subset as seed text ($\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \cite{hu2022lora} with $r{=}16$, $\alpha{=}32$, lr $2{\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$ (architecture-specific targets); (2)~unconditional generation of 5{,}000 passages (max 512 tokens, starting from BOS) under the specified decoding strategy; (3)~the generated corpus becomes $\mathcal{D}_k$ for the next cycle.
34	There is no per-passage lineage across depths, ensuring cross-validation splits do not introduce information leakage.
35	
36	\paragraph{Reference model.}
37	All statistical features (\S\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.
38	The reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.
39	In cross-model leave-one-out evaluation (\S\ref{sec:generalization}), the reference model remains fixed even when GPT-2~XL is held out; the partial architectural overlap this introduces is discussed in Limitations.
40	
41	\subsection{Statistical Feature Design}
42	\label{sec:method:features}
43	
44	We extract a 19-dimensional feature vector $\mathbf{f}(x)$ from the reference-model perplexity distribution over each passage $x$.
45	The features fall into four categories (Table~\ref{tab:features}).
46	
47	\begin{table}[t]
48	\centering
49	\small
50	\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (GPT-2 base, 124M).}
51	\label{tab:features}
52	\begin{tabular}{@{}llr@{}}
53	\toprule
54	Category & Features & $n$ \\
55	\midrule
56	Perplexity & mean, var, skewness, kurtosis, & 9 \\
57	statistics & p10, p25, p50, p75, p90 & \\
58	\addlinespace
59	Surprisal & mean, var, entropy & 3 \\
60	statistics & & \\
61	\addlinespace
62	Lexical & type--token ratio, hapax ratio, & 4 \\
63	diversity & bigram entropy, trigram entropy & \\
64	\addlinespace
65	Repetition & repeated 2/3/4-gram fractions & 3 \\
66	\bottomrule
67	\end{tabular}
68	\end{table}
69	
70	\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments (mean, variance, skewness, kurtosis) and quantiles (p10--p90); tail quantiles prove especially informative as recursive finetuning erodes the high-perplexity tail (\S\ref{sec:atlas}).
71	\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\log p(\text{token})$; surprisal variance captures second-order structure not redundant with perplexity moments.
72	\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.
73	\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \in \{2, 3, 4\}$.
74	
75	\subsection{Effective Discriminable Depth}
76	\label{sec:method:edd}
77	
78	Aggregate accuracy obscures whether discriminability degrades at specific depths.
79	We introduce the \emph{Effective Discriminable Depth} (EDD): for each adjacent pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute AUC.
80	Given threshold $T$:
81	\begin{equation}
82	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 : \forall\, d' \leq d^*,\; \mathrm{AUC}(d', d'{+}1) \geq T \bigr\}
83	\label{eq:edd}
84	\end{equation}
85	where $d^* \in \{0, \dots, K{-}1\}$; $\mathrm{EDD}_T = 0$ if $\mathrm{AUC}(0,1) < T$.\footnote{Our AUC profiles are monotonically decreasing; for non-monotonic profiles, EDD reports the longest contiguous discriminable prefix (see Limitations).}
86	Default $T{=}0.75$; sensitivity at $T \in \{0.65, 0.70, 0.75, 0.80\}$ in \S\ref{sec:atlas}.
87	Each AUC is from an independent binary classifier, avoiding decision boundary dilution (\S\ref{sec:atlas}).
88	
89	\paragraph{Classifiers.}
90	Our primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).
91	We compare against CORAL ordinal regression \cite{coral2020}, DivEye \cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \S\ref{sec:generalization}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "f4364e32-0843-4733-a447-9779d94d0380",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Definition}\n\\label{sec:method:problem}\n\nLet $f_\\theta$ denote a language model and $\\mathcal{D}_0$ a corpus of human-written seed text.\nWe define a \\emph{recursive generation chain} of depth $K$ as the sequence $\\mathcal{D}_0, \\mathcal{D}_1, \\dots, \\mathcal{D}_K$, where each $\\mathcal{D}_k$ ($k \\geq 1$) is produced by finetuning $f_\\theta$ on $\\mathcal{D}_{k-1}$ and sampling from the resulting model.\nDepth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \\geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.\n\nGiven a text passage $x$, the task is to estimate its recursive generation depth $d \\in \\{0, 1, \\dots, K\\}$.\nThis is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.\n\n\\subsection{Multi-Generational Benchmark Construction}\n\\label{sec:method:benchmark}\n\nWe construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.\n\n\\paragraph{Model families.}\nWe select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).\nRestricting to a narrow parameter range isolates the effect of architecture and training data from scale.\n\n\\paragraph{Decoding strategies.}\nEach model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \\cite{holtzman2020_nucleus}, temperature sampling ($\\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).\nThese span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.\nOur findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.\n\n\\paragraph{Depth and scale.}\nThe primary benchmark covers depths d0--d3 across all $3 \\times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).\nFor depth extension experiments (\\S\\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.\n\n\\paragraph{Generation pipeline.}\nStarting from a Wikipedia subset as seed text ($\\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \\cite{hu2022lora} with $r{=}16$, $\\alpha{=}32$, lr $2{\\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$ (architecture-specific targets); (2)~unconditional generation of 5{,}000 passages (max 512 tokens, starting from BOS) under the specified decoding strategy; (3)~the generated corpus becomes $\\mathcal{D}_k$ for the next cycle.\nThere is no per-passage lineage across depths, ensuring cross-validation splits do not introduce information leakage.\n\n\\paragraph{Reference model.}\nAll statistical features (\\S\\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.\nThe reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.\nIn cross-model leave-one-out evaluation (\\S\\ref{sec:generalization}), the reference model remains fixed even when GPT-2~XL is held out; the partial architectural overlap this introduces is discussed in Limitations.\n\n\\subsection{Statistical Feature Design}\n\\label{sec:method:features}\n\nWe extract a 19-dimensional feature vector $\\mathbf{f}(x)$ from the reference-model perplexity distribution over each passage $x$.\nThe features fall into four categories (Table~\\ref{tab:features}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{The 19 statistical features comprising $\\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (GPT-2 base, 124M).}\n\\label{tab:features}\n\\begin{tabular}{@{}llr@{}}\n\\toprule\nCategory & Features & $n$ \\\\\n\\midrule\nPerplexity & mean, var, skewness, kurtosis, & 9 \\\\\nstatistics & p10, p25, p50, p75, p90 & \\\\\n\\addlinespace\nSurprisal & mean, var, entropy & 3 \\\\\nstatistics & & \\\\\n\\addlinespace\nLexical & type--token ratio, hapax ratio, & 4 \\\\\ndiversity & bigram entropy, trigram entropy & \\\\\n\\addlinespace\nRepetition & repeated 2/3/4-gram fractions & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments (mean, variance, skewness, kurtosis) and quantiles (p10--p90); tail quantiles prove especially informative as recursive finetuning erodes the high-perplexity tail (\\S\\ref{sec:atlas}).\n\\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\\log p(\\text{token})$; surprisal variance captures second-order structure not redundant with perplexity moments.\n\\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.\n\\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \\in \\{2, 3, 4\\}$.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:method:edd}\n\nAggregate accuracy obscures whether discriminability degrades at specific depths.\nWe introduce the \\emph{Effective Discriminable Depth} (EDD): for each adjacent pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute AUC.\nGiven threshold $T$:\n\\begin{equation}\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 : \\forall\\, d' \\leq d^*,\\; \\mathrm{AUC}(d', d'{+}1) \\geq T \\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $d^* \\in \\{0, \\dots, K{-}1\\}$; $\\mathrm{EDD}_T = 0$ if $\\mathrm{AUC}(0,1) < T$.\\footnote{Our AUC profiles are monotonically decreasing; for non-monotonic profiles, EDD reports the longest contiguous discriminable prefix (see Limitations).}\nDefault $T{=}0.75$; sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in \\S\\ref{sec:atlas}.\nEach AUC is from an independent binary classifier, avoiding decision boundary dilution (\\S\\ref{sec:atlas}).\n\n\\paragraph{Classifiers.}\nOur primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).\nWe compare against CORAL ordinal regression \\cite{coral2020}, DivEye \\cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \\S\\ref{sec:generalization}.",
      "numLines": 91,
      "startLine": 1,
      "totalLines": 91
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_016wiSFtkSzxcLTGXaUkpyAT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "1d6708e6-e4d3-4db0-b531-b1e327e990b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113XxxRQ9mq9rxHffo1SweX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 23691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 829
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

_source line 12 · 2026-05-15T22:07:08.764Z_

<details><summary>↩ Tool result · `toolu_016wiSFtkSzxcLTGXaUkpyAT`</summary>

```text
1	% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints
2	% Target: EMNLP 2026 (ARR May cycle)
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{amsmath}
10	\usepackage{amssymb}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage[T1]{fontenc}
15	\usepackage[utf8]{inputenc}
16	\usepackage{microtype}
17	
18	\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\via Statistical Fingerprints}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{atlas}
34	
35	\input{generalization}
36	
37	\input{discussion}
38	
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{section_appendix}
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
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "7c98a49a-c715-4807-b502-d2dd2d827550",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/main.tex",
      "content": "% How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints\n% Target: EMNLP 2026 (ARR May cycle)\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\title{How Deep Is Your Data? Estimating Recursive Generation Depth\\\\via Statistical Fingerprints}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{atlas}\n\n\\input{generalization}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\appendix\n\\input{section_appendix}\n\n\\end{document}\n",
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01FUj1Uzx8gWu7XPzDubyBH2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "c2fecc18-0ae2-40b6-b6e5-9afcfd689ddb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113XxxRQ9mq9rxHffo1SweX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 23691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 829
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

_source line 14 · 2026-05-15T22:07:09.028Z_

<details><summary>↩ Tool result · `toolu_01FUj1Uzx8gWu7XPzDubyBH2`</summary>

```text
1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2024_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2024},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},
46	  year      = {2024},
47	  note      = {arXiv:2307.01850},
48	  url       = {https://arxiv.org/abs/2307.01850},
49	}
50	
51	@misc{gerstgrasser2024_accumulate,
52	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
53	  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
54	  year      = {2024},
55	  howpublished = {arXiv:2404.01413},
56	  url       = {https://arxiv.org/abs/2404.01413},
57	}
58	
59	@inproceedings{marchi2024_heat_death,
60	  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},
61	  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},
62	  booktitle = {Proceedings of ICASSP},
63	  year      = {2024},
64	  note      = {arXiv:2404.02325},
65	  url       = {https://arxiv.org/abs/2404.02325},
66	}
67	
68	@misc{knowledge_collapse2025,
69	  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},
70	  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},
71	  year      = {2025},
72	  howpublished = {arXiv:2509.04796},
73	  url       = {https://arxiv.org/abs/2509.04796},
74	}
75	
76	@misc{sigma2026_spectral,
77	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
78	  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},
79	  year      = {2026},
80	  howpublished = {arXiv:2601.03385},
81	  url       = {https://arxiv.org/abs/2601.03385},
82	}
83	
84	@inproceedings{mohamed2025_broken_telephone,
85	  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
86	  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
87	  booktitle = {Proceedings of ACL},
88	  year      = {2025},
89	  note      = {arXiv:2502.20258},
90	  url       = {https://arxiv.org/abs/2502.20258},
91	}
92	
93	@inproceedings{synthetic_eggs2026,
94	  author    = {Schaffelder, Max and Gatt, Albert},
95	  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},
96	  booktitle = {Findings of ACL},
97	  year      = {2026},
98	  note      = {arXiv:2511.01490},
99	  url       = {https://arxiv.org/abs/2511.01490},
100	}
101	
102	% --- Model collapse: collapse-can-be-avoided / contamination ---
103	
104	@inproceedings{drayson2025_detection_prevents_collapse,
105	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
106	  title     = {{Machine-generated text detection prevents language model collapse}},
107	  booktitle = {Findings of EMNLP},
108	  year      = {2025},
109	  note      = {arXiv:2502.15654},
110	  url       = {https://arxiv.org/abs/2502.15654},
111	}
112	
113	@misc{bakshi2026_collapse_improvement,
114	  author    = {Bakshi, Soham and Chakraborty, Sunrit},
115	  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},
116	  year      = {2026},
117	  howpublished = {arXiv:2602.10531},
118	  url       = {https://arxiv.org/abs/2602.10531},
119	}
120	
121	@misc{wang2026_contamination,
122	  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},
123	  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},
124	  year      = {2026},
125	  howpublished = {arXiv:2602.16065},
126	  url       = {https://arxiv.org/abs/2602.16065},
127	}
128	
129	@misc{falahati2026_curated,
130	  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},
131	  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},
132	  year      = {2026},
133	  howpublished = {arXiv:2605.07724},
134	  url       = {https://arxiv.org/abs/2605.07724},
135	}
136	
137	% ============================================================
138	% AI-Generated Text Detection
139	% ============================================================
140	
141	% --- Statistical / zero-shot detectors ---
142	
143	@inproceedings{gehrmann2019_gltr,
144	  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
145	  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},
146	  booktitle = {Proceedings of ACL: System Demonstrations},
147	  year      = {2019},
148	  note      = {arXiv:1906.04043},
149	  url       = {https://arxiv.org/abs/1906.04043},
150	}
151	
152	@inproceedings{mitchell2023_detectgpt,
153	  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
154	  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
155	  booktitle = {Proceedings of ICML},
156	  year      = {2023},
157	  note      = {arXiv:2301.11305},
158	  url       = {https://arxiv.org/abs/2301.11305},
159	}
160	
161	@inproceedings{fast_detectgpt2024,
162	  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
163	  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
164	  booktitle = {Proceedings of ICLR},
165	  year      = {2024},
166	  note      = {arXiv:2310.05130},
167	  url       = {https://arxiv.org/abs/2310.05130},
168	}
169	
170	@inproceedings{binoculars2024,
171	  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
172	  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
173	  booktitle = {Proceedings of ICML},
174	  year      = {2024},
175	  note      = {arXiv:2401.12070},
176	  url       = {https://arxiv.org/abs/2401.12070},
177	}
178	
179	@article{diveye2026,
180	  author    = {Basani, Advik Raj and Chen, Pin-Yu},
181	  title     = {{Diversity Boosts AI-Generated Text Detection}},
182	  journal   = {Transactions on Machine Learning Research (TMLR)},
183	  year      = {2026},
184	  note      = {arXiv:2509.18880},
185	  url       = {https://arxiv.org/abs/2509.18880},
186	}
187	
188	% --- Robustness / limitations of detectors ---
189	
190	@misc{sadasivan2023_paraphrase,
191	  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
192	  title     = {{Can AI-Generated Text be Reliably Detected?}},
193	  year      = {2023},
194	  howpublished = {arXiv:2303.11156},
195	  url       = {https://arxiv.org/abs/2303.11156},
196	}
197	
198	@misc{pudasaini2026_detection_fails,
199	  author    = {Pudasaini, Shushanta and Miralles-Pech{\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},
200	  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},
201	  year      = {2026},
202	  howpublished = {arXiv:2603.23146},
203	  url       = {https://arxiv.org/abs/2603.23146},
204	}
205	
206	@misc{pu2026_generator_barrier,
207	  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
208	  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
209	  year      = {2026},
210	  howpublished = {arXiv:2604.13692},
211	  url       = {https://arxiv.org/abs/2604.13692},
212	}
213	
214	% --- Beyond binary: attribution, editing extent, benchmarks ---
215	
216	@inproceedings{uchendu2020_attribution,
217	  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
218	  title     = {{Authorship Attribution for Neural Text Generation}},
219	  booktitle = {Proceedings of EMNLP},
220	  year      = {2020},
221	}
222	
223	@inproceedings{editlens2026,
224	  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},
225	  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},
226	  booktitle = {Proceedings of ICLR},
227	  year      = {2026},
228	  note      = {arXiv:2510.03154},
229	  url       = {https://arxiv.org/abs/2510.03154},
230	}
231	
232	@inproceedings{loki2025,
233	  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},
234	  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},
235	  booktitle = {Proceedings of ICLR (Spotlight)},
236	  year      = {2025},
237	  note      = {arXiv:2410.09732},
238	  url       = {https://arxiv.org/abs/2410.09732},
239	}
240	
241	% --- Statistical / feature-based / shared-task detectors ---
242	
243	@inproceedings{verma2024_ghostbuster,
244	  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
245	  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
246	  booktitle = {Proceedings of NAACL},
247	  year      = {2024},
248	  note      = {arXiv:2305.15047},
249	  url       = {https://arxiv.org/abs/2305.15047},
250	}
251	
252	@inproceedings{wang2024_m4_semeval,
253	  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
254	  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
255	  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},
256	  year      = {2024},
257	  note      = {arXiv:2404.14183},
258	  url       = {https://arxiv.org/abs/2404.14183},
259	}
260	
261	@inproceedings{yang2024_dnagpt,
262	  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
263	  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
264	  booktitle = {Proceedings of ICLR},
265	  year      = {2024},
266	  note      = {arXiv:2305.17359},
267	  url       = {https://arxiv.org/abs/2305.17359},
268	}
269	
270	% --- Watermarking ---
271	
272	@inproceedings{kirchenbauer2023_watermark,
273	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
274	  title     = {{A Watermark for Large Language Models}},
275	  booktitle = {Proceedings of ICML},
276	  year      = {2023},
277	  note      = {arXiv:2301.10226},
278	  url       = {https://arxiv.org/abs/2301.10226},
279	}
280	
281	% ============================================================
282	% Decoding Strategies
283	% ============================================================
284	
285	@inproceedings{holtzman2020_nucleus,
286	  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
287	  title     = {{The Curious Case of Neural Text Degeneration}},
288	  booktitle = {Proceedings of ICLR},
289	  year      = {2020},
290	  note      = {arXiv:1904.09751},
291	  url       = {https://arxiv.org/abs/1904.09751},
292	}
293	
294	@inproceedings{finlayson2024_closing,
295	  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},
296	  title     = {{Closing the Curious Case of Neural Text Degeneration}},
297	  booktitle = {Proceedings of ICLR},
298	  year      = {2024},
299	  note      = {arXiv:2310.01693},
300	  url       = {https://arxiv.org/abs/2310.01693},
301	}
302	
303	@inproceedings{garces_arias2025_decoding_decoded,
304	  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},
305	  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},
306	  booktitle = {Proceedings of COLING},
307	  year      = {2025},
308	  note      = {arXiv:2410.06097},
309	  url       = {https://arxiv.org/abs/2410.06097},
310	}
311	
312	@article{wiher2022_decoding,
313	  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},
314	  title     = {{On Decoding Strategies for Neural Text Generators}},
315	  journal   = {Transactions of the Association for Computational Linguistics},
316	  volume    = {10},
317	  pages     = {997--1012},
318	  year      = {2022},
319	}
320	
321	@inproceedings{basu2021_mirostat,
322	  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},
323	  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},
324	  booktitle = {Proceedings of ICLR},
325	  year      = {2021},
326	}
327	
328	% ============================================================
329	% Ordinal Classification / Contrastive Learning
330	% ============================================================
331	
332	@article{coral2020,
333	  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
334	  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
335	  journal   = {Pattern Recognition Letters},
336	  volume    = {140},
337	  pages     = {325--331},
338	  year      = {2020},
339	  note      = {arXiv:1901.07884},
340	  url       = {https://arxiv.org/abs/1901.07884},
341	}
342	
343	@inproceedings{cloc2025,
344	  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},
345	  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},
346	  booktitle = {Proceedings of CVPR},
347	  year      = {2025},
348	  note      = {arXiv:2504.17813},
349	  url       = {https://arxiv.org/abs/2504.17813},
350	}
351	
352	% ============================================================
353	% Foundation Models / Fine-tuning
354	% ============================================================
355	
356	@inproceedings{hu2022lora,
357	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
358	  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},
359	  booktitle = {Proceedings of ICLR},
360	  year      = {2022},
361	  note      = {arXiv:2106.09685},
362	  url       = {https://arxiv.org/abs/2106.09685},
363	}
364	
365	@inproceedings{he2021_deberta_v3,
366	  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
367	  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},
368	  booktitle = {Proceedings of ICLR},
369	  year      = {2023},
370	  note      = {arXiv:2111.09543},
371	  url       = {https://arxiv.org/abs/2111.09543},
372	}
373	
374	@article{liu2019_roberta,
375	  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
376	  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},
377	  journal   = {arXiv preprint arXiv:1907.11692},
378	  year      = {2019},
379	  url       = {https://arxiv.org/abs/1907.11692},
380	}
381	
382	% ============================================================
383	% Data Curation / Selection
384	% ============================================================
385	
386	@inproceedings{dsir2023,
387	  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
388	  title     = {{Data Selection for Language Models via Importance Resampling}},
389	  booktitle = {Proceedings of NeurIPS},
390	  year      = {2023},
391	  note      = {arXiv:2302.03169},
392	  url       = {https://arxiv.org/abs/2302.03169},
393	}
394	
395	@inproceedings{qurating2024,
396	  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
397	  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},
398	  booktitle = {Proceedings of ICML},
399	  year      = {2024},
400	  note      = {arXiv:2402.09739},
401	  url       = {https://arxiv.org/abs/2402.09739},
402	}
403	
404	@article{sugiyama2007_importance_weighting,
405	  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\"u}ller, Klaus-Robert},
406	  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},
407	  journal   = {Journal of Machine Learning Research},
408	  volume    = {8},
409	  pages     = {985--1005},
410	  year      = {2007},
411	}
412	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "3548305c-b807-4df3-b1d2-1a6d2ccbf4c0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
      "content": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2024_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Hossain, Hossein and Romero, Oscar and Ramanarayanan, Sriram and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@article{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  journal   = {arXiv preprint arXiv:1907.11692},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n",
      "numLines": 412,
      "startLine": 1,
      "totalLines": 412
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the remaining .tex files to understand the full picture.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "fc906dd8-01aa-453d-93a1-b751e02ee924",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

Now let me read the remaining tex files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "509270b1-ed8c-4074-99d9-becbb70668d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

<details open><summary>🔧 Tool call — Read · `toolu_01TBi1gGjFj6XqgsuRidTw4E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "25010fbf-2a8e-4090-bbe3-fa3c222c6691",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

_source line 18 · 2026-05-15T22:07:15.012Z_

<details><summary>↩ Tool result · `toolu_01TBi1gGjFj6XqgsuRidTw4E`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are consistent across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surprisal})---emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.
16	
17	We formalize recursive generation depth estimation as an ordinal classification task and introduce a lightweight pipeline to solve it.
18	Given a text passage, we compute a 19-dimensional feature vector from reference-model perplexity statistics---capturing distributional location, spread, tail behavior, and lexical diversity---and classify it with a Random Forest into one of $K{+}1$ depth classes ($d{=}0$ for human text through $d{=}K$ for $K$-th generation text).
19	To systematically characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) and decoding strategies (nucleus $p{=}0.95$, temperature $\tau{=}0.9$, top-$k$ $k{=}50$), each spanning 4 generation depths, totaling 180K samples.
20	The atlas reveals strategy-dependent degradation trajectories---temperature sampling accelerates convergence toward a low-entropy attractor, while top-$k$ attenuates the depth signal---and we introduce the \emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.
21	
22	Our contributions are:
23	
24	\begin{itemize}
25	    \item \textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification and introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.
26	
27	    \item \textbf{Depth Degradation Atlas.} We construct a systematic $3 \times 3$ map across model families and decoding strategies, revealing that \textsc{p90\_ppl} ranks in the top 2 in all 9 cells and \textsc{var\_surprisal} in 8/9, with a mean Spearman rank correlation of $\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.
28	
29	    \item \textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\% and cross-strategy transfer 59.1\% (chance = 25\%). We decompose a temperature-induced d1/d2 AUC inversion into a scale component---partially correctable by per-strategy normalization---and a residual structural component that simple normalization cannot resolve.
30	
31	    \item \textbf{End-to-end learning.} Both DeBERTa-v3-base (58.3\%) and RoBERTa-base (59.5\%) achieve ${\sim}$59\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\%)---with the architecture-invariant gap ruling out model selection bias. Linear probing confirms that PLM representations cannot recover perplexity tail features (negative $R^2$), while SHAP analysis shows these features account for 88.8\% of RF's contribution.
32	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "1ef04c63-4c70-4ab3-86fc-a7cd923eb7fd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nThe text on which large language models are trained increasingly contains their own outputs.\nAs synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \\cite{shumailov2024_nature,alemohammad2024_mad}.\nThis model$\\to$data$\\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \\cite{dohmatob2024_tale_of_tails}.\n\nExisting tools address adjacent but distinct problems.\nBinary detectors such as Binoculars \\cite{binoculars2024}, Fast-DetectGPT \\cite{fast_detectgpt2024}, and DivEye \\cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \\geq 1$ into a single category.\nWatermarking \\cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.\nThe model collapse literature \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \\citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.\nNo existing method estimates the ordinal recursive generation depth of a text passage from its content alone.\n\nOur key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are consistent across the three model families and three decoding strategies studied.\nSpecifically, perplexity tail statistics---the 90th-percentile perplexity (\\textsc{p90\\_ppl}) and surprisal variance (\\textsc{var\\_surprisal})---emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.\n\nWe formalize recursive generation depth estimation as an ordinal classification task and introduce a lightweight pipeline to solve it.\nGiven a text passage, we compute a 19-dimensional feature vector from reference-model perplexity statistics---capturing distributional location, spread, tail behavior, and lexical diversity---and classify it with a Random Forest into one of $K{+}1$ depth classes ($d{=}0$ for human text through $d{=}K$ for $K$-th generation text).\nTo systematically characterize how recursive generation reshapes these features, we construct the \\emph{Depth Degradation Atlas}: a $3 \\times 3$ grid of model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) and decoding strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$, top-$k$ $k{=}50$), each spanning 4 generation depths, totaling 180K samples.\nThe atlas reveals strategy-dependent degradation trajectories---temperature sampling accelerates convergence toward a low-entropy attractor, while top-$k$ attenuates the depth signal---and we introduce the \\emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.\n\nOur contributions are:\n\n\\begin{itemize}\n    \\item \\textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification and introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.\n\n    \\item \\textbf{Depth Degradation Atlas.} We construct a systematic $3 \\times 3$ map across model families and decoding strategies, revealing that \\textsc{p90\\_ppl} ranks in the top 2 in all 9 cells and \\textsc{var\\_surprisal} in 8/9, with a mean Spearman rank correlation of $\\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.\n\n    \\item \\textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\\% and cross-strategy transfer 59.1\\% (chance = 25\\%). We decompose a temperature-induced d1/d2 AUC inversion into a scale component---partially correctable by per-strategy normalization---and a residual structural component that simple normalization cannot resolve.\n\n    \\item \\textbf{End-to-end learning.} Both DeBERTa-v3-base (58.3\\%) and RoBERTa-base (59.5\\%) achieve ${\\sim}$59\\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\\%)---with the architecture-invariant gap ruling out model selection bias. Linear probing confirms that PLM representations cannot recover perplexity tail features (negative $R^2$), while SHAP analysis shows these features account for 88.8\\% of RF's contribution.\n\\end{itemize}",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01EYzSdqbxX5F9t3qdpseBuy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "b6fe8d7a-ec78-41be-bd83-c5084676c09c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

_source line 20 · 2026-05-15T22:07:15.750Z_

<details><summary>↩ Tool result · `toolu_01EYzSdqbxX5F9t3qdpseBuy`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails, collapsing the output distribution.
6	\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \emph{narrowing} from \emph{cutting}; \citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \citet{dohmatob2024_demystified} analyze the regression case.
7	The MAD framework \cite{alemohammad2024_mad} extends this to self-consuming models and quantifies the precision--recall tradeoff.
8	Mitigation strategies include retaining real data \cite{gerstgrasser2024_accumulate} and filtering via detection \cite{drayson2025_detection_prevents_collapse}.
9	Recent work identifies non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, fixed-point convergence \cite{marchi2024_heat_death}, contamination bounds \cite{wang2026_contamination}, curated pipelines \cite{falahati2026_curated}, knowledge collapse \cite{knowledge_collapse2025}, spectral signatures \cite{sigma2026_spectral}, and self-improving loops \cite{synthetic_eggs2026}.
10	These works characterize degradation but assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
11	
12	\paragraph{AI Text Detection.}
13	DetectGPT \cite{mitchell2023_detectgpt} introduced probability curvature as a zero-shot detection signal; Fast-DetectGPT \cite{fast_detectgpt2024} improves efficiency via surrogate-model conditional curvature.
14	Binoculars \cite{binoculars2024} exploits perplexity ratios between related models, DivEye \cite{diveye2026} leverages surprisal diversity, and GLTR \cite{gehrmann2019_gltr} visualizes per-token likelihood ranks.
15	Fundamental limits exist: paraphrasing reduces detection to near chance \cite{sadasivan2023_paraphrase}, detection degrades under distribution shift \cite{pudasaini2026_detection_fails}, and a generator barrier bounds performance when the generator is unknown \cite{pu2026_generator_barrier}.
16	Ghostbuster \cite{verma2024_ghostbuster} trains classifiers on statistical features for binary detection, sharing our feature-engineering philosophy but not addressing depth; M4-SemEval \cite{wang2024_m4_semeval} benchmarks multilingual detection, and DNA-GPT \cite{yang2024_dnagpt} uses divergent $n$-gram analysis.
17	Watermarking \cite{kirchenbauer2023_watermark} embeds detectable signals but requires proactive deployment.
18	All these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.
19	
20	\paragraph{Adjacent Tasks.}
21	EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains.
22	\citet{uchendu2020_attribution} classify \emph{which} model generated text rather than recursion depth.
23	LOKI \cite{loki2025} benchmarks synthetic data detection across modalities but evaluates binary detection only.
24	\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, measuring forward degradation; our task performs the inverse, classifying depth from text alone.
25	
26	\paragraph{Ordinal Classification.}
27	CORAL \cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.
28	We adopt both as baselines (\S\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.
29	
30	\paragraph{Decoding Strategy Effects.}
31	Decoding strategies shape text statistics in ways that interact with depth signals: nucleus sampling maintains diversity \cite{holtzman2020_nucleus}, decoding parameters affect evaluation non-trivially \cite{finlayson2024_closing}, and strategy effects are model-dependent \cite{garces_arias2025_decoding_decoded}.
32	\citet{wiher2022_decoding} systematically compare methods on surface-level properties, and Mirostat \cite{basu2021_mirostat} regulates output entropy via perplexity control.
33	Our Depth Degradation Atlas (\S\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation---temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal---effects beyond single-pass text quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "c5260ea4-3a3a-4b60-a771-406abda8a267",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Model Collapse Theory.}\n\\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails, collapsing the output distribution.\n\\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \\emph{narrowing} from \\emph{cutting}; \\citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \\citet{dohmatob2024_demystified} analyze the regression case.\nThe MAD framework \\cite{alemohammad2024_mad} extends this to self-consuming models and quantifies the precision--recall tradeoff.\nMitigation strategies include retaining real data \\cite{gerstgrasser2024_accumulate} and filtering via detection \\cite{drayson2025_detection_prevents_collapse}.\nRecent work identifies non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, fixed-point convergence \\cite{marchi2024_heat_death}, contamination bounds \\cite{wang2026_contamination}, curated pipelines \\cite{falahati2026_curated}, knowledge collapse \\cite{knowledge_collapse2025}, spectral signatures \\cite{sigma2026_spectral}, and self-improving loops \\cite{synthetic_eggs2026}.\nThese works characterize degradation but assume depth is known a priori; we address the inverse problem of estimating depth from text alone.\n\n\\paragraph{AI Text Detection.}\nDetectGPT \\cite{mitchell2023_detectgpt} introduced probability curvature as a zero-shot detection signal; Fast-DetectGPT \\cite{fast_detectgpt2024} improves efficiency via surrogate-model conditional curvature.\nBinoculars \\cite{binoculars2024} exploits perplexity ratios between related models, DivEye \\cite{diveye2026} leverages surprisal diversity, and GLTR \\cite{gehrmann2019_gltr} visualizes per-token likelihood ranks.\nFundamental limits exist: paraphrasing reduces detection to near chance \\cite{sadasivan2023_paraphrase}, detection degrades under distribution shift \\cite{pudasaini2026_detection_fails}, and a generator barrier bounds performance when the generator is unknown \\cite{pu2026_generator_barrier}.\nGhostbuster \\cite{verma2024_ghostbuster} trains classifiers on statistical features for binary detection, sharing our feature-engineering philosophy but not addressing depth; M4-SemEval \\cite{wang2024_m4_semeval} benchmarks multilingual detection, and DNA-GPT \\cite{yang2024_dnagpt} uses divergent $n$-gram analysis.\nWatermarking \\cite{kirchenbauer2023_watermark} embeds detectable signals but requires proactive deployment.\nAll these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.\n\n\\paragraph{Adjacent Tasks.}\nEditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains.\n\\citet{uchendu2020_attribution} classify \\emph{which} model generated text rather than recursion depth.\nLOKI \\cite{loki2025} benchmarks synthetic data detection across modalities but evaluates binary detection only.\n\\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, measuring forward degradation; our task performs the inverse, classifying depth from text alone.\n\n\\paragraph{Ordinal Classification.}\nCORAL \\cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \\cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.\nWe adopt both as baselines (\\S\\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.\n\n\\paragraph{Decoding Strategy Effects.}\nDecoding strategies shape text statistics in ways that interact with depth signals: nucleus sampling maintains diversity \\cite{holtzman2020_nucleus}, decoding parameters affect evaluation non-trivially \\cite{finlayson2024_closing}, and strategy effects are model-dependent \\cite{garces_arias2025_decoding_decoded}.\n\\citet{wiher2022_decoding} systematically compare methods on surface-level properties, and Mirostat \\cite{basu2021_mirostat} regulates output entropy via perplexity control.\nOur Depth Degradation Atlas (\\S\\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation---temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal---effects beyond single-pass text quality.",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_012sZpk7UhFiKGcDFP2WMrSX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "145a048a-a9ef-43b9-9f33-c06eb9b6e32e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

_source line 22 · 2026-05-15T22:07:16.074Z_

<details><summary>↩ Tool result · `toolu_012sZpk7UhFiKGcDFP2WMrSX`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that 19 statistical features achieve 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	The dominant pair (\texttt{p90\_ppl} top-2 in 9/9 cells, \texttt{var\_surprisal} in 7/9) generalizes across model families without retraining, making depth estimation a measurable early warning for model collapse~\cite{shumailov2024_nature}---though cross-strategy transfer remains the bottleneck (59.1\% vs.\ 66.4\%) and all experiments use 1--1.5B models.
6	Future work should validate on mixed-domain corpora at larger scales and evaluate whether depth-graduated curation improves downstream training outcomes.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "c7c2d48c-23e9-4ba2-b6f7-3dac47a7dc71",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nWe formalized recursive generation depth estimation and showed that 19 statistical features achieve 70--85\\% four-class accuracy ($\\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\\% of full performance and classifier-agnostic convergence within $\\leq$0.4pp.\nThe dominant pair (\\texttt{p90\\_ppl} top-2 in 9/9 cells, \\texttt{var\\_surprisal} in 7/9) generalizes across model families without retraining, making depth estimation a measurable early warning for model collapse~\\cite{shumailov2024_nature}---though cross-strategy transfer remains the bottleneck (59.1\\% vs.\\ 66.4\\%) and all experiments use 1--1.5B models.\nFuture work should validate on mixed-domain corpora at larger scales and evaluate whether depth-graduated curation improves downstream training outcomes.\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01RZxSXAzhPbhFaQp57FwAKN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "d347ffeb-f326-46e3-9f8a-f2ac68b2a571",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

_source line 24 · 2026-05-15T22:07:16.493Z_

<details><summary>↩ Tool result · `toolu_01RZxSXAzhPbhFaQp57FwAKN`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but leaves a residual gap relative to within-strategy performance (${\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.
7	
8	\paragraph{d0 inflation of headline metrics.}
9	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all settings), inflating headline accuracy.
10	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
11	
12	\paragraph{Controlled vs.\ ecological setting.}
13	All experiments use Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models).
14	Depth signal is the dominant classification factor (5-fold CV 59--82\%, up to 2.5$\times$ chance): LOGO accuracy (72.1\%) matches standard CV (72.0\%), and seed-group prediction is at chance (10.2\% vs.\ 10\%; Appendix~\ref{app:domain_bias}).
15	Transfer to mixed-domain corpora, instruction-tuned models, and larger scales (7B+) remains open.
16	Real-world documents may also interleave segments at different recursion depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.
17	
18	\paragraph{Adversarial robustness.}
19	Adversarial paraphrasing \cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.
20	
21	\paragraph{EDD monotonicity assumption.}
22	Our EDD definition (Eq.~\ref{eq:edd}) requires all pairwise AUCs up to depth $d^*$ to exceed $T$, which is well-behaved when AUC decays monotonically---as observed in all our configurations.
23	However, \citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).
24	Our cross-strategy transfer results provide an empirical example: training on nucleus + top-$k$ and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2~XL) and 0.253 (OLMo), violating the monotonicity assumption.
25	In such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work.
26	The choice of threshold $T$ is also application-dependent: at $T{=}0.80$, several cells lose one depth level relative to $T{=}0.75$.
27	
28	\paragraph{Reference model dependency.}
29	Surprisal-based features are computed relative to GPT-2 base (124M), introducing partial overlap when GPT-2~XL is held out, though GPT-2~XL holdout accuracy (67.6\%) does not exceed the unrelated OLMo (69.2\%).
30	The choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.
31	
32	\paragraph{Additional caveats.}
33	Detection features degrade under domain shift \cite{pudasaini2026_detection_fails}; our depth features are likely susceptible.
34	\citet{falahati2026_curated} show that curated synthetic data need not trigger collapse, attenuating the fingerprints we exploit.
35	
36	\section*{Ethics Statement}
37	
38	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
39	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
40	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
41	Code and data will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "0312a150-852c-4d1b-ae44-be0c6689a60f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Cross-strategy deployment constraint.}\nCross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.\nPer-strategy z-score normalization partially corrects the inversion (GPT-2~XL d1v2 AUC $0.24{\\to}0.56$, OLMo $0.19{\\to}0.70$) but leaves a residual gap relative to within-strategy performance (${\\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.\n\n\\paragraph{d0 inflation of headline metrics.}\nDepth~0 (human-written text) is near-perfectly separable (recall $>$98\\% across all settings), inflating headline accuracy.\nCross-model transfer accuracy of 66.4\\% is substantially driven by d0; d2 recall drops to 26.8\\% in the worst case (Pythia holdout).\n\n\\paragraph{Controlled vs.\\ ecological setting.}\nAll experiments use Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models).\nDepth signal is the dominant classification factor (5-fold CV 59--82\\%, up to 2.5$\\times$ chance): LOGO accuracy (72.1\\%) matches standard CV (72.0\\%), and seed-group prediction is at chance (10.2\\% vs.\\ 10\\%; Appendix~\\ref{app:domain_bias}).\nTransfer to mixed-domain corpora, instruction-tuned models, and larger scales (7B+) remains open.\nReal-world documents may also interleave segments at different recursion depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.\n\n\\paragraph{Adversarial robustness.}\nAdversarial paraphrasing \\cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.\n\n\\paragraph{EDD monotonicity assumption.}\nOur EDD definition (Eq.~\\ref{eq:edd}) requires all pairwise AUCs up to depth $d^*$ to exceed $T$, which is well-behaved when AUC decays monotonically---as observed in all our configurations.\nHowever, \\citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \\emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).\nOur cross-strategy transfer results provide an empirical example: training on nucleus + top-$k$ and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2~XL) and 0.253 (OLMo), violating the monotonicity assumption.\nIn such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work.\nThe choice of threshold $T$ is also application-dependent: at $T{=}0.80$, several cells lose one depth level relative to $T{=}0.75$.\n\n\\paragraph{Reference model dependency.}\nSurprisal-based features are computed relative to GPT-2 base (124M), introducing partial overlap when GPT-2~XL is held out, though GPT-2~XL holdout accuracy (67.6\\%) does not exceed the unrelated OLMo (69.2\\%).\nThe choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.\n\n\\paragraph{Additional caveats.}\nDetection features degrade under domain shift \\cite{pudasaini2026_detection_fails}; our depth features are likely susceptible.\n\\citet{falahati2026_curated} show that curated synthetic data need not trigger collapse, attenuating the fingerprints we exploit.\n\n\\section*{Ethics Statement}\n\nThis work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.\nNo human subjects were involved, no private or sensitive data were collected, and no new models were released.\nOur method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.\nCode and data will be released upon acceptance.",
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01Wg45i3N9kwsAxewUYU5KTn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "b2058238-c51c-4e64-80f8-4a76d617528a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

_source line 26 · 2026-05-15T22:07:17.314Z_

<details><summary>↩ Tool result · `toolu_01Wg45i3N9kwsAxewUYU5KTn`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 69.6\% (Pythia, top-$k$) to 85.4\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\%), followed by OLMo (74.2--82.0\%) and Pythia (69.6--78.2\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) across the $3 \times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.2\,(71.2) & 76.3\,(70.6) & 69.6\,(58.8) \\
28	OLMo-1B     & 78.8\,(75.0) & 82.0\,(76.3) & 74.2\,(66.1) \\
29	GPT-2~XL    & 83.3\,(79.0) & 85.4\,(82.6) & 76.6\,(69.5) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	%% ----------------------------------------------------------------
35	\subsection{Feature Universality}
36	\label{sec:atlas:features}
37	
38	Despite the 15.8~pp accuracy spread across cells, a small feature family dominates in every setting.
39	The 90th-percentile perplexity (\texttt{p90\_ppl}) ranks top-2 by Gini importance in all 9 cells; surprisal variance (\texttt{var\_surprisal}) in 7/9 (8/9 under SHAP; Appendix~\ref{app:permutation}).
40	Table~\ref{tab:feature_importance} shows the full per-cell ranking.
41	
42	Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.
43	Among strategies, top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$)---the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\S\ref{sec:atlas:strategy}).
44	
45	Percentile-based features outperform their moment-based counterparts.
46	Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \texttt{p90\_ppl} is robust to such extremes while still capturing the tail erosion that signals recursive depth.
47	
48	Feature ablation confirms this concentration: the top-5 features achieve 97.6\% of full accuracy (76.5\% vs.\ 78.4\%), with perplexity statistics alone reaching 76.6\% (vs.\ surprisal 73.2\%, other categories $<$46\%).
49	Forward selection independently confirms the dominant pair: \texttt{var\_surprisal} is selected first in 6/9 cells, \texttt{p90\_ppl} in 3/9.
50	
51	The feature hierarchy also shifts with depth.
52	At shallow boundaries (d1 vs.\ d2), \texttt{var\_surprisal} dominates importance; at deeper boundaries (d3 vs.\ d4, d4 vs.\ d5), tail perplexity statistics (\texttt{p90\_ppl}, \texttt{kurtosis\_ppl}) take over.
53	This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
54	
55	\begin{table}[t]
56	\centering
57	\small
58	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 7/9 (8/9 under SHAP).}
59	\label{tab:feature_importance}
60	\begin{tabular}{@{}l l@{}}
61	\toprule
62	Cell & Top-5 features (Gini importance, ranked) \\
63	\midrule
64	Pythia, nuc.       & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.15)}, m\_ppl\,(.11), var\_ppl\,(.08), p75\,(.07) \\
65	Pythia, $\tau$     & \textbf{var\_surp\,(.17)}, \textbf{p90\_ppl\,(.14)}, m\_ppl\,(.11), p75\,(.07), m\_surp\,(.07) \\
66	Pythia, top-$k$    & \textbf{var\_surp\,(.16)}, \textbf{p90\_ppl\,(.12)}, m\_ppl\,(.11), var\_ppl\,(.07), m\_surp\,(.06) \\
67	GPT-2\,XL, nuc.    & \textbf{var\_surp\,(.21)}, \textbf{p90\_ppl\,(.21)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.06) \\
68	GPT-2\,XL, $\tau$  & \textbf{p90\_ppl\,(.25)}, \textbf{p75\,(.15)}, m\_surp\,(.13), var\_surp\,(.12), p50\,(.05) \\
69	GPT-2\,XL, top-$k$ & \textbf{p90\_ppl\,(.24)}, \textbf{p75\,(.12)}, var\_surp\,(.10), m\_surp\,(.09), ttr\,(.04) \\
70	OLMo, nuc.         & \textbf{p90\_ppl\,(.18)}, \textbf{var\_surp\,(.15)}, p75\,(.11), m\_surp\,(.07), ttr\,(.06) \\
71	OLMo, $\tau$       & \textbf{p90\_ppl\,(.21)}, \textbf{var\_surp\,(.16)}, p75\,(.12), m\_surp\,(.09), ttr\,(.05) \\
72	OLMo, top-$k$      & \textbf{p90\_ppl\,(.20)}, \textbf{var\_surp\,(.17)}, p75\,(.10), m\_surp\,(.07), m\_ppl\,(.05) \\
73	\bottomrule
74	\end{tabular}
75	\end{table}
76	
77	\begin{figure}[t]
78	\centering
79	\includegraphics[width=\columnwidth]{figures/fig_atlas_heatmap.pdf}
80	\caption{Atlas feature importance heatmap. Rows: 19 features grouped by category (\S\ref{sec:method:features}); columns: 9 model--strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.}
81	\label{fig:atlas_heatmap}
82	\end{figure}
83	
84	%% ----------------------------------------------------------------
85	\subsection{Monotonicity and Inter-Depth Distances}
86	\label{sec:atlas:monotonicity}
87	
88	Depth features exhibit strong monotonic trends: perplexity tail statistics (\texttt{p90\_ppl}, \texttt{mean\_surprisal}) decrease with depth (Spearman $\rho = -1.0$ across cell-level medians) while repetition features increase, reflecting the complementary narrowing and self-repetition of distribution collapse.
89	Inter-depth distances are non-uniform: d0-vs-d1 AUC exceeds 0.99 in all 9 cells, whereas d2-vs-d3 ranges from 0.69 to 0.89---separating adjacent deep generations requires the tail statistics identified in \S\ref{sec:atlas:features}.
90	
91	\begin{figure}[t]
92	\centering
93	\includegraphics[width=\columnwidth]{figures/fig_feature_trajectory.pdf}
94	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \texttt{p90\_ppl} (monotonically decreasing). Middle: \texttt{var\_surprisal} (decreasing). Bottom: \texttt{rep\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
95	\label{fig:feature_trajectory}
96	\end{figure}
97	
98	%% ----------------------------------------------------------------
99	\subsection{EDD Analysis}
100	\label{sec:atlas:edd}
101	
102	We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
103	Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (GPT-2 base, 124M).
104	We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
105	
106	\paragraph{AUC decay profile.}
107	Figure~\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.
108	For Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.
109	The steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.
110	
111	\paragraph{Cross-model convergence at depth 4--5.}
112	The d3-vs-d4 AUC clusters near $T{=}0.75$ (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$; bootstrap CIs in Figure~\ref{fig:auc_decay}), while d4-vs-d5 falls uniformly below 0.70 ($0.681$--$0.684$), confirming model-independent signal saturation at depth~5.
113	This graded decay supports interpreting the d3--d4 region as a \emph{transition zone} rather than a binary boundary.
114	
115	\paragraph{EDD threshold sensitivity.}
116	Table~\ref{tab:edd_sensitivity} reports $\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.
117	At $T{=}0.65$, all 9 cells achieve $\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\mathrm{EDD} \geq 3$; at $T{=}0.80$, the count drops to 5 of 9.
118	The cells losing $\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.
119	
120	\begin{table}[t]
121	\centering
122	\small
123	\caption{Number of atlas cells achieving $\mathrm{EDD} \geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}
124	\label{tab:edd_sensitivity}
125	\begin{tabular}{@{}lcccc@{}}
126	\toprule
127	& $T{=}0.65$ & $T{=}0.70$ & $T{=}0.75$ & $T{=}0.80$ \\
128	\midrule
129	Cells with $\mathrm{EDD} \geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	\begin{figure}[t]
135	\centering
136	\includegraphics[width=\columnwidth]{figures/fig_auc_decay.pdf}
137	\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\% CIs.}
138	\label{fig:auc_decay}
139	\end{figure}
140	
141	\paragraph{Decision boundary dilution.}
142	\label{sec:atlas:edd:dilution}
143	EDD uses binary-pair classifiers to avoid \emph{decision boundary dilution}: in Pythia nucleus, d2\,vs.\,d3 AUC degrades from 0.804 (4-class) to 0.689 (6-class)---a 14.3\% relative decline despite identical data---because shared decision boundaries dilute per-pair capacity.
144	Binary classifiers eliminate this confound, isolating true adjacent-pair discriminability.
145	
146	%% ----------------------------------------------------------------
147	\subsection{Strategy-Dependent Trajectories}
148	\label{sec:atlas:strategy}
149	
150	The three decoding strategies induce qualitatively distinct degradation trajectories.
151	Nucleus ($p{=}0.95$) produces the most consistent accuracy (78.2--83.3\%) and serves as the reference trajectory.
152	Temperature ($\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.4\%, OLMo 82.0\%) because uniform logit scaling accelerates convergence to an attractor distribution~\cite{shumailov2024_nature}, amplifying the statistical fingerprint---but this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\S\ref{sec:generalization}).
153	Top-$k$ ($k{=}50$) produces the lowest accuracy (69.6--76.6\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens, though feature direction is preserved (cross-model $\rho = 0.811$).
154	The strategy effect (8.4~pp range) exceeds the model effect (7.1~pp), indicating deployment-time knowledge of the decoding strategy matters at least as much as the generator model.
155	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "1773ece0-0d9f-40cb-8ce4-ba6d73696908",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
      "content": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.\nThe atlas spans $3 \\times 3 = 9$ model--strategy cells evaluated at depths $d \\in \\{0, 1, 2, 3\\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\\S\\ref{sec:atlas:edd}).\n\n%% ----------------------------------------------------------------\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:id}\n\nTable~\\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.\nAccuracy ranges from 69.6\\% (Pythia, top-$k$) to 85.4\\% (GPT-2~XL, temperature), all exceeding the 25\\% chance baseline by a wide margin.\nTwo axis effects emerge.\nGPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\\%), followed by OLMo (74.2--82.0\\%) and Pythia (69.6--78.2\\%).\nTop-$k$ sampling yields the lowest accuracy in every model.\nThe mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-class RF accuracy (\\%) across the $3 \\times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\\% / 33\\%). Depth-0 recall exceeds 98\\% in all cells.}\n\\label{tab:main_matrix}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n& Nucleus & Temp.\\ $\\tau{=}0.9$ & Top-$k$ \\\\\n\\midrule\nPythia-1.4B  & 78.2\\,(71.2) & 76.3\\,(70.6) & 69.6\\,(58.8) \\\\\nOLMo-1B     & 78.8\\,(75.0) & 82.0\\,(76.3) & 74.2\\,(66.1) \\\\\nGPT-2~XL    & 83.3\\,(79.0) & 85.4\\,(82.6) & 76.6\\,(69.5) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ----------------------------------------------------------------\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nDespite the 15.8~pp accuracy spread across cells, a small feature family dominates in every setting.\nThe 90th-percentile perplexity (\\texttt{p90\\_ppl}) ranks top-2 by Gini importance in all 9 cells; surprisal variance (\\texttt{var\\_surprisal}) in 7/9 (8/9 under SHAP; Appendix~\\ref{app:permutation}).\nTable~\\ref{tab:feature_importance} shows the full per-cell ranking.\n\nCross-model feature-rank Spearman correlation averages $\\bar{\\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.\nAmong strategies, top-$k$ yields the highest cross-model rank correlation ($\\rho = 0.811$)---the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\\S\\ref{sec:atlas:strategy}).\n\nPercentile-based features outperform their moment-based counterparts.\nToken-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \\texttt{p90\\_ppl} is robust to such extremes while still capturing the tail erosion that signals recursive depth.\n\nFeature ablation confirms this concentration: the top-5 features achieve 97.6\\% of full accuracy (76.5\\% vs.\\ 78.4\\%), with perplexity statistics alone reaching 76.6\\% (vs.\\ surprisal 73.2\\%, other categories $<$46\\%).\nForward selection independently confirms the dominant pair: \\texttt{var\\_surprisal} is selected first in 6/9 cells, \\texttt{p90\\_ppl} in 3/9.\n\nThe feature hierarchy also shifts with depth.\nAt shallow boundaries (d1 vs.\\ d2), \\texttt{var\\_surprisal} dominates importance; at deeper boundaries (d3 vs.\\ d4, d4 vs.\\ d5), tail perplexity statistics (\\texttt{p90\\_ppl}, \\texttt{kurtosis\\_ppl}) take over.\nThis transition aligns with model-collapse dynamics~\\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top-5 features by Gini importance. \\textbf{Bold}: top-2. \\texttt{p90\\_ppl} top-2 in 9/9; \\texttt{var\\_surprisal} 7/9 (8/9 under SHAP).}\n\\label{tab:feature_importance}\n\\begin{tabular}{@{}l l@{}}\n\\toprule\nCell & Top-5 features (Gini importance, ranked) \\\\\n\\midrule\nPythia, nuc.       & \\textbf{var\\_surp\\,(.17)}, \\textbf{p90\\_ppl\\,(.15)}, m\\_ppl\\,(.11), var\\_ppl\\,(.08), p75\\,(.07) \\\\\nPythia, $\\tau$     & \\textbf{var\\_surp\\,(.17)}, \\textbf{p90\\_ppl\\,(.14)}, m\\_ppl\\,(.11), p75\\,(.07), m\\_surp\\,(.07) \\\\\nPythia, top-$k$    & \\textbf{var\\_surp\\,(.16)}, \\textbf{p90\\_ppl\\,(.12)}, m\\_ppl\\,(.11), var\\_ppl\\,(.07), m\\_surp\\,(.06) \\\\\nGPT-2\\,XL, nuc.    & \\textbf{var\\_surp\\,(.21)}, \\textbf{p90\\_ppl\\,(.21)}, p75\\,(.10), m\\_surp\\,(.07), m\\_ppl\\,(.06) \\\\\nGPT-2\\,XL, $\\tau$  & \\textbf{p90\\_ppl\\,(.25)}, \\textbf{p75\\,(.15)}, m\\_surp\\,(.13), var\\_surp\\,(.12), p50\\,(.05) \\\\\nGPT-2\\,XL, top-$k$ & \\textbf{p90\\_ppl\\,(.24)}, \\textbf{p75\\,(.12)}, var\\_surp\\,(.10), m\\_surp\\,(.09), ttr\\,(.04) \\\\\nOLMo, nuc.         & \\textbf{p90\\_ppl\\,(.18)}, \\textbf{var\\_surp\\,(.15)}, p75\\,(.11), m\\_surp\\,(.07), ttr\\,(.06) \\\\\nOLMo, $\\tau$       & \\textbf{p90\\_ppl\\,(.21)}, \\textbf{var\\_surp\\,(.16)}, p75\\,(.12), m\\_surp\\,(.09), ttr\\,(.05) \\\\\nOLMo, top-$k$      & \\textbf{p90\\_ppl\\,(.20)}, \\textbf{var\\_surp\\,(.17)}, p75\\,(.10), m\\_surp\\,(.07), m\\_ppl\\,(.05) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_atlas_heatmap.pdf}\n\\caption{Atlas feature importance heatmap. Rows: 19 features grouped by category (\\S\\ref{sec:method:features}); columns: 9 model--strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\n%% ----------------------------------------------------------------\n\\subsection{Monotonicity and Inter-Depth Distances}\n\\label{sec:atlas:monotonicity}\n\nDepth features exhibit strong monotonic trends: perplexity tail statistics (\\texttt{p90\\_ppl}, \\texttt{mean\\_surprisal}) decrease with depth (Spearman $\\rho = -1.0$ across cell-level medians) while repetition features increase, reflecting the complementary narrowing and self-repetition of distribution collapse.\nInter-depth distances are non-uniform: d0-vs-d1 AUC exceeds 0.99 in all 9 cells, whereas d2-vs-d3 ranges from 0.69 to 0.89---separating adjacent deep generations requires the tail statistics identified in \\S\\ref{sec:atlas:features}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_trajectory.pdf}\n\\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \\texttt{p90\\_ppl} (monotonically decreasing). Middle: \\texttt{var\\_surprisal} (decreasing). Bottom: \\texttt{rep\\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \\to d{=}1$ gap exceeds all subsequent inter-depth gaps.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n%% ----------------------------------------------------------------\n\\subsection{EDD Analysis}\n\\label{sec:atlas:edd}\n\nWe extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.\nEach model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (GPT-2 base, 124M).\nWe train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\\ref{eq:edd}.\n\n\\paragraph{AUC decay profile.}\nFigure~\\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.\nFor Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.\nThe steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.\n\n\\paragraph{Cross-model convergence at depth 4--5.}\nThe d3-vs-d4 AUC clusters near $T{=}0.75$ (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$; bootstrap CIs in Figure~\\ref{fig:auc_decay}), while d4-vs-d5 falls uniformly below 0.70 ($0.681$--$0.684$), confirming model-independent signal saturation at depth~5.\nThis graded decay supports interpreting the d3--d4 region as a \\emph{transition zone} rather than a binary boundary.\n\n\\paragraph{EDD threshold sensitivity.}\nTable~\\ref{tab:edd_sensitivity} reports $\\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.\nAt $T{=}0.65$, all 9 cells achieve $\\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\\mathrm{EDD} \\geq 3$; at $T{=}0.80$, the count drops to 5 of 9.\nThe cells losing $\\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Number of atlas cells achieving $\\mathrm{EDD} \\geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n& $T{=}0.65$ & $T{=}0.70$ & $T{=}0.75$ & $T{=}0.80$ \\\\\n\\midrule\nCells with $\\mathrm{EDD} \\geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\\% CIs.}\n\\label{fig:auc_decay}\n\\end{figure}\n\n\\paragraph{Decision boundary dilution.}\n\\label{sec:atlas:edd:dilution}\nEDD uses binary-pair classifiers to avoid \\emph{decision boundary dilution}: in Pythia nucleus, d2\\,vs.\\,d3 AUC degrades from 0.804 (4-class) to 0.689 (6-class)---a 14.3\\% relative decline despite identical data---because shared decision boundaries dilute per-pair capacity.\nBinary classifiers eliminate this confound, isolating true adjacent-pair discriminability.\n\n%% ----------------------------------------------------------------\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:strategy}\n\nThe three decoding strategies induce qualitatively distinct degradation trajectories.\nNucleus ($p{=}0.95$) produces the most consistent accuracy (78.2--83.3\\%) and serves as the reference trajectory.\nTemperature ($\\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.4\\%, OLMo 82.0\\%) because uniform logit scaling accelerates convergence to an attractor distribution~\\cite{shumailov2024_nature}, amplifying the statistical fingerprint---but this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\\S\\ref{sec:generalization}).\nTop-$k$ ($k{=}50$) produces the lowest accuracy (69.6--76.6\\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens, though feature direction is preserved (cross-model $\\rho = 0.811$).\nThe strategy effect (8.4~pp range) exceeds the model effect (7.1~pp), indicating deployment-time knowledge of the decoding strategy matters at least as much as the generator model.\n",
      "numLines": 155,
      "startLine": 1,
      "totalLines": 155
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_016NJtFzYLsZCiCQwPDMjGgN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "1c7c992c-7bcc-43e6-b5ef-9f931dd8e412",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

_source line 28 · 2026-05-15T22:07:17.809Z_

<details><summary>↩ Tool result · `toolu_016NJtFzYLsZCiCQwPDMjGgN`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether the atlas results (69.6--85.4\%) reflect genuine statistical regularities or training artifacts, evaluating four axes: classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and end-to-end learning (\S\ref{sec:gen:e2e}).
5	
6	\subsection{Baseline Comparison}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} evaluates three classifier families---bagging (RF), gradient boosting (XGBoost, LightGBM)---on the same 19 features across three atlas cells spanning the full accuracy range.
10	Per-cell spread is $\leq$0.4pp, establishing a feature-determined ceiling independent of the learning algorithm.
11	On Pythia nucleus, CORAL ordinal regression \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match the within-cell RF of Table~\ref{tab:main_matrix} within 0.1\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\%, $p<0.001$) and logistic regression (75.0\%).
12	Single-feature regression on mean perplexity performs at chance (25.1\%); a zero-shot LLM (DeepSeek V3.2) reaches only 36.2\% (95\% CI $[32.0, 40.4]$\%, 500 samples).
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\caption{Classifier convergence: 4-class accuracy (\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\Delta_{\max}$: largest per-cell spread. Chance = 25\%. RF values differ from Table~\ref{tab:main_matrix} by $\leq$0.7pp due to matched-fold evaluation.}
18	\label{tab:baselines}
19	\begin{tabular}{@{}lcccc@{}}
20	\toprule
21	Cell & RF & XGB & LGBM & $\Delta_{\max}$ \\
22	\midrule
23	Pythia, nuc. & 78.8 & 79.0 & 78.9 & 0.2 \\
24	GPT-2~XL, $\tau$ & 85.8 & 86.2 & 86.2 & 0.4 \\
25	Pythia, top-$k$ & 68.9 & 68.9 & 68.7 & 0.2 \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Convergence across five structurally different classifiers---spanning bagging, gradient boosting, ordinal regression, and ensemble detection---confirms the signal resides in the features, not the learning algorithm.
31	Figure~\ref{fig:confusion_matrix} shows d0 near-perfectly identified; errors concentrate at d2/d3 in-distribution and spread across d1--d3 under transfer.
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
36	\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.4\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
37	\label{fig:confusion_matrix}
38	\end{figure}
39	
40	\subsection{Cross-Model Transfer}
41	\label{sec:gen:crossmodel}
42	
43	We perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\ref{tab:cross_model}).
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 bal.\ acc: Pythia 49.9\%, OLMo 59.2\%, GPT-2~XL 57.2\% (mean 55.4\%).}
49	\label{tab:cross_model}
50	\begin{tabular}{lccccc}
51	\toprule
52	Holdout & Acc & d0 & d1 & d2 & d3 \\
53	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
54	\midrule
55	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
56	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
57	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
58	\midrule
59	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
60	\bottomrule
61	\end{tabular}
62	\end{table}
63	
64	Mean transfer accuracy is 66.4\% (2.7$\times$ chance); d0 recall ($>$98\%) inflates the headline while d2 drops to 26.8\% (Pythia holdout).
65	Excluding d0, d1--d3 balanced accuracy averages 55.4\% (chance = 33\%).
66	
67	\subsection{Cross-Strategy Transfer}
68	\label{sec:gen:crossstrategy}
69	
70	We train on two decoding strategies and test on the held-out third (Table~\ref{tab:cross_strategy}).
71	
72	\begin{table}[t]
73	\centering
74	\small
75	\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89\% inflates headline; d1--d3 mean: 45.9\%.}
76	\label{tab:cross_strategy}
77	\begin{tabular}{lccc}
78	\toprule
79	Holdout & Pythia & OLMo & GPT-2 XL \\
80	 & Acc (\%) & Acc (\%) & Acc (\%) \\
81	\midrule
82	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
83	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
84	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	Mean cross-strategy accuracy (59.1\%) falls 7pp below cross-model transfer (66.4\%); excluding d0, d1--d3 accuracy drops to 45.9\% (chance = 33\%).
90	d2 recall varies sharply: nucleus holdouts retain 30--54\%, top-$k$ holdouts fall to 8--19\%, and temperature holdouts span 3.7--39.5\% (median 8.9\%).
91	Training on nucleus + top-$k$ and testing on temperature inverts the d1/d2 boundary (d1v2 AUC $<$ 0.5); per-strategy z-score normalization partially recovers it but leaves a residual gap (Limitations).
92	
93	\subsection{End-to-End Learning}
94	\label{sec:gen:e2e}
95	
96	DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end both converge to ${\sim}$59\% (19pp below RF 78.2\%).
97	The 1.2pp inter-backbone gap rules out architecture bias; Table~\ref{tab:e2e_detail} shows both backbones share the same failure mode---high d0 F1 ($>$0.94) but collapsed d1/d2 performance (F1 $\leq$ 0.42)---while RF achieves 0.596 d2 recall, a $>$2$\times$ advantage at the hardest depth class.
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Per-class performance for end-to-end PLM classifiers vs.\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}
103	\label{tab:e2e_detail}
104	\begin{tabular}{@{}lccccc@{}}
105	\toprule
106	Method & Acc (\%) & d0 & d1 & d2 & d3 \\
107	\midrule
108	DeBERTa-v3 & 58.3\,$\pm$\,4.7 & .947 & .378 & .247 & .656 \\
109	RoBERTa & 59.5\,$\pm$\,3.2 & .958 & .416 & .261 & .647 \\
110	\midrule
111	RF (19 feat.) & 78.2 & --- & --- & .596$^\dagger$ & --- \\
112	\bottomrule
113	\multicolumn{6}{@{}l}{\footnotesize $^\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}
114	\end{tabular}
115	\end{table}
116	
117	\paragraph{Feature space divergence.}
118	SHAP TreeExplainer shows perplexity and surprisal features account for 88.8\% of RF's contribution (Kendall's $W{=}0.90$ across three importance measures, $p{<}0.005$; Appendix~\ref{app:permutation}).
119	Both PLM backbones correlate \emph{negatively} with RF importance (DeBERTa $\rho{=}{-}0.484$, RoBERTa $\rho{=}{-}0.456$; zero top-5 overlap), with linear probing yielding negative $R^2$ for \texttt{var\_surprisal} and \texttt{p90\_ppl} (Appendix~\ref{app:feature_overlap})---a systematic representational gap, not backbone-specific artifacts.
120	
121	DCOL \cite{cloc2025} reached 64.5\% (Appendix~\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods, suggesting depth estimation benefits from explicit tail statistics absent from PLM representations.
122	
123	\paragraph{Ecological validity.}
124	While cross-validated accuracy on controlled data is 78.8\%, d0 identification is robust to domain shift: the Pythia-nucleus RF classifies all 546 WikiText-103 test passages as d0 (FPR$\,{=}\,$0\%), despite mean perplexity $+$621\% and variance $+$503\% higher than the training d0 distribution (Table~\ref{tab:calibration}).
125	This robustness is partly an easy case---WikiText's higher perplexity places it \emph{farther} from d1--d3 in feature space---and does not imply comparable accuracy on wild text at deeper depths.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "942799fd-5878-4b6d-8b1f-bb3018a55f7f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
      "content": "\\section{Generalization and Robustness}\n\\label{sec:generalization}\n\nWe test whether the atlas results (69.6--85.4\\%) reflect genuine statistical regularities or training artifacts, evaluating four axes: classifier choice (\\S\\ref{sec:gen:baselines}), cross-model transfer (\\S\\ref{sec:gen:crossmodel}), cross-strategy transfer (\\S\\ref{sec:gen:crossstrategy}), and end-to-end learning (\\S\\ref{sec:gen:e2e}).\n\n\\subsection{Baseline Comparison}\n\\label{sec:gen:baselines}\n\nTable~\\ref{tab:baselines} evaluates three classifier families---bagging (RF), gradient boosting (XGBoost, LightGBM)---on the same 19 features across three atlas cells spanning the full accuracy range.\nPer-cell spread is $\\leq$0.4pp, establishing a feature-determined ceiling independent of the learning algorithm.\nOn Pythia nucleus, CORAL ordinal regression \\cite{coral2020} (78.1\\%) and DivEye \\cite{diveye2026} (78.2\\%) match the within-cell RF of Table~\\ref{tab:main_matrix} within 0.1\\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\\%, $p<0.001$) and logistic regression (75.0\\%).\nSingle-feature regression on mean perplexity performs at chance (25.1\\%); a zero-shot LLM (DeepSeek V3.2) reaches only 36.2\\% (95\\% CI $[32.0, 40.4]$\\%, 500 samples).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Classifier convergence: 4-class accuracy (\\%) across three atlas cells. RF (bagging), XGBoost and LightGBM (gradient boosting) operate on the same 19 features; $\\Delta_{\\max}$: largest per-cell spread. Chance = 25\\%. RF values differ from Table~\\ref{tab:main_matrix} by $\\leq$0.7pp due to matched-fold evaluation.}\n\\label{tab:baselines}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nCell & RF & XGB & LGBM & $\\Delta_{\\max}$ \\\\\n\\midrule\nPythia, nuc. & 78.8 & 79.0 & 78.9 & 0.2 \\\\\nGPT-2~XL, $\\tau$ & 85.8 & 86.2 & 86.2 & 0.4 \\\\\nPythia, top-$k$ & 68.9 & 68.9 & 68.7 & 0.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConvergence across five structurally different classifiers---spanning bagging, gradient boosting, ordinal regression, and ensemble detection---confirms the signal resides in the features, not the learning algorithm.\nFigure~\\ref{fig:confusion_matrix} shows d0 near-perfectly identified; errors concentrate at d2/d3 in-distribution and spread across d1--d3 under transfer.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_confusion_matrix.pdf}\n\\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\\tau{=}0.9$, 85.4\\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\\%). d0 recall exceeds 99\\% in both; errors spread across the d1--d3 range under transfer.}\n\\label{fig:confusion_matrix}\n\\end{figure}\n\n\\subsection{Cross-Model Transfer}\n\\label{sec:gen:crossmodel}\n\nWe perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\\ref{tab:cross_model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\\% / 33\\% (d1--d3). d1--d3 bal.\\ acc: Pythia 49.9\\%, OLMo 59.2\\%, GPT-2~XL 57.2\\% (mean 55.4\\%).}\n\\label{tab:cross_model}\n\\begin{tabular}{lccccc}\n\\toprule\nHoldout & Acc & d0 & d1 & d2 & d3 \\\\\n & (\\%) & Rec. & Rec. & Rec. & Rec. \\\\\n\\midrule\nPythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\\\\nOLMo & \\textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\\\\nGPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\\\\n\\midrule\nMean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean transfer accuracy is 66.4\\% (2.7$\\times$ chance); d0 recall ($>$98\\%) inflates the headline while d2 drops to 26.8\\% (Pythia holdout).\nExcluding d0, d1--d3 balanced accuracy averages 55.4\\% (chance = 33\\%).\n\n\\subsection{Cross-Strategy Transfer}\n\\label{sec:gen:crossstrategy}\n\nWe train on two decoding strategies and test on the held-out third (Table~\\ref{tab:cross_strategy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-strategy transfer (leave-one-out). Chance = 25\\% / 33\\% (d1--d3). d0 recall $\\geq$89\\% inflates headline; d1--d3 mean: 45.9\\%.}\n\\label{tab:cross_strategy}\n\\begin{tabular}{lccc}\n\\toprule\nHoldout & Pythia & OLMo & GPT-2 XL \\\\\n & Acc (\\%) & Acc (\\%) & Acc (\\%) \\\\\n\\midrule\nnucleus & \\textbf{69.4} & \\textbf{65.4} & \\textbf{59.9} \\\\\ntemp ($\\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\\\\ntop-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean cross-strategy accuracy (59.1\\%) falls 7pp below cross-model transfer (66.4\\%); excluding d0, d1--d3 accuracy drops to 45.9\\% (chance = 33\\%).\nd2 recall varies sharply: nucleus holdouts retain 30--54\\%, top-$k$ holdouts fall to 8--19\\%, and temperature holdouts span 3.7--39.5\\% (median 8.9\\%).\nTraining on nucleus + top-$k$ and testing on temperature inverts the d1/d2 boundary (d1v2 AUC $<$ 0.5); per-strategy z-score normalization partially recovers it but leaves a residual gap (Limitations).\n\n\\subsection{End-to-End Learning}\n\\label{sec:gen:e2e}\n\nDeBERTa-v3-base \\cite{he2021_deberta_v3} and RoBERTa-base \\cite{liu2019_roberta} finetuned end-to-end both converge to ${\\sim}$59\\% (19pp below RF 78.2\\%).\nThe 1.2pp inter-backbone gap rules out architecture bias; Table~\\ref{tab:e2e_detail} shows both backbones share the same failure mode---high d0 F1 ($>$0.94) but collapsed d1/d2 performance (F1 $\\leq$ 0.42)---while RF achieves 0.596 d2 recall, a $>$2$\\times$ advantage at the hardest depth class.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-class performance for end-to-end PLM classifiers vs.\\ RF baseline (Pythia-1.4B nucleus). PLM columns report F1; RF d2 column reports recall (the class with the largest PLM--RF gap). Both PLM backbones share the same failure pattern: collapsed d1/d2 scores despite adequate d0/d3.}\n\\label{tab:e2e_detail}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nMethod & Acc (\\%) & d0 & d1 & d2 & d3 \\\\\n\\midrule\nDeBERTa-v3 & 58.3\\,$\\pm$\\,4.7 & .947 & .378 & .247 & .656 \\\\\nRoBERTa & 59.5\\,$\\pm$\\,3.2 & .958 & .416 & .261 & .647 \\\\\n\\midrule\nRF (19 feat.) & 78.2 & --- & --- & .596$^\\dagger$ & --- \\\\\n\\bottomrule\n\\multicolumn{6}{@{}l}{\\footnotesize $^\\dagger$Recall; shown for the depth class with the largest PLM--RF gap.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Feature space divergence.}\nSHAP TreeExplainer shows perplexity and surprisal features account for 88.8\\% of RF's contribution (Kendall's $W{=}0.90$ across three importance measures, $p{<}0.005$; Appendix~\\ref{app:permutation}).\nBoth PLM backbones correlate \\emph{negatively} with RF importance (DeBERTa $\\rho{=}{-}0.484$, RoBERTa $\\rho{=}{-}0.456$; zero top-5 overlap), with linear probing yielding negative $R^2$ for \\texttt{var\\_surprisal} and \\texttt{p90\\_ppl} (Appendix~\\ref{app:feature_overlap})---a systematic representational gap, not backbone-specific artifacts.\n\nDCOL \\cite{cloc2025} reached 64.5\\% (Appendix~\\ref{app:dcol_iterations}); all end-to-end approaches (58--65\\%) underperform feature-based methods, suggesting depth estimation benefits from explicit tail statistics absent from PLM representations.\n\n\\paragraph{Ecological validity.}\nWhile cross-validated accuracy on controlled data is 78.8\\%, d0 identification is robust to domain shift: the Pythia-nucleus RF classifies all 546 WikiText-103 test passages as d0 (FPR$\\,{=}\\,$0\\%), despite mean perplexity $+$621\\% and variance $+$503\\% higher than the training d0 distribution (Table~\\ref{tab:calibration}).\nThis robustness is partly an easy case---WikiText's higher perplexity places it \\emph{farther} from d1--d3 in feature space---and does not imply comparable accuracy on wild text at deeper depths.",
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

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01K8JTGG7k8nQMQDL3NaxnWT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "1c77490f-fd5e-47c3-a8c8-e9da2d39391e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

_source line 30 · 2026-05-15T22:07:18.449Z_

<details><summary>↩ Tool result · `toolu_01K8JTGG7k8nQMQDL3NaxnWT`</summary>

```text
1	\begin{abstract}
2	As large language models increasingly train on web text containing their own outputs, a recursive model$\to$data$\to$model loop arises---yet no method estimates how many such iterations a text has undergone.
3	We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
4	From each passage we extract 19 statistical features---perplexity percentiles, surprisal moments, and lexical diversity measures---computed against a fixed reference model (GPT-2 base, 124M).
5	A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; 58.8--82.6\% when excluding the near-perfectly separable d0 class; a zero-shot LLM baseline reaches only 36.2\%), with 90th-percentile perplexity and surprisal variance emerging as consistent depth markers across the studied $3 \times 3$ grid (top-2 importance in 9/9 and 7/9 cells, respectively).
6	Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.
7	Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%; temperature sampling induces a d1/d2 AUC inversion that we decompose into a correctable scale component and a residual structural component.
8	Applied to 546 WikiText-103 passages, the classifier produces zero false positives despite $+$621\% domain shift in mean perplexity.
9	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "05a01dc1-04ee-4415-9c45-e37bdac088a5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nAs large language models increasingly train on web text containing their own outputs, a recursive model$\\to$data$\\to$model loop arises---yet no method estimates how many such iterations a text has undergone.\nWe formalize \\emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.\nFrom each passage we extract 19 statistical features---perplexity percentiles, surprisal moments, and lexical diversity measures---computed against a fixed reference model (GPT-2 base, 124M).\nA Random Forest classifier achieves 70--85\\% four-class accuracy (chance = 25\\%; 58.8--82.6\\% when excluding the near-perfectly separable d0 class; a zero-shot LLM baseline reaches only 36.2\\%), with 90th-percentile perplexity and surprisal variance emerging as consistent depth markers across the studied $3 \\times 3$ grid (top-2 importance in 9/9 and 7/9 cells, respectively).\nOur \\emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \\emph{Effective Discriminable Depth} (EDD) metric, finding $\\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.\nCross-model transfer reaches 66.4\\% and cross-strategy transfer 59.1\\%; temperature sampling induces a d1/d2 AUC inversion that we decompose into a correctable scale component and a residual structural component.\nApplied to 546 WikiText-103 passages, the classifier produces zero false positives despite $+$621\\% domain shift in mean perplexity.\n\\end{abstract}",
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

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_019EzenMJFrnUwfv12KWyDLK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "75e1b0f5-6b85-4ce2-b792-5850bb940552",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rNQdjxFZ7QvCXgRzZFyXX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10249,
      "cache_read_input_tokens": 24520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10249
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

_source line 32 · 2026-05-15T22:07:19.069Z_

<details><summary>↩ Tool result · `toolu_019EzenMJFrnUwfv12KWyDLK`</summary>

```text
1	\section{Additional Results}
2	\label{app:additional}
3	
4	\subsection{Top-$k$ Feature Trajectories}
5	\label{app:topk_trajectories}
6	
7	Figure~\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\tau{=}0.9$) sampling.
8	Top-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \S\ref{sec:atlas:strategy}.
9	Concretely, the d0$\to$d1 drop in \textsc{p90\_ppl} under top-$k$ is 78\% (vs.\ 87\% for nucleus), and the d2$\to$d3 reduction is 31\% (vs.\ 39\% for nucleus).
10	Despite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.
11	
12	\subsection{Permutation Importance}
13	\label{app:permutation}
14	
15	To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
16	The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
17	Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
18	Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
19	Per-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.
20	
21	\subsection{DCOL Iteration Details}
22	\label{app:dcol_iterations}
23	
24	Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
25	DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
26	
27	\begin{table}[h]
28	\centering
29	\small
30	\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\%.}
31	\label{tab:dcol_iterations}
32	\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}
33	\toprule
34	Ver. & Backbone & Config & Outcome \\
35	\midrule
36	v1 & DeBERTa & FT, m\_lr $10^{-3}$ & Embed.\ collapse (31.5\%) \\
37	v2 & DeBERTa & FT, m\_lr $10^{-4}$ & OOM \\
38	v3 & DeBERTa & FT, m\_lr $10^{-4}$ & Forgetting + OOM \\
39	v4 & DeBERTa & LoRA, m\_lr $10^{-3}$ & Embed.\ collapse \\
40	v5 & DeBERTa & LoRA, m\_lr $10^{-4}$ & NaN gradients \\
41	v6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\% ($-$13.7pp) \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	\subsection{Feature Overlap Analysis}
47	\label{app:feature_overlap}
48	
49	We probe whether end-to-end PLM representations capture the same depth signals as our statistical features.
50	DeBERTa attention importance and RF permutation importance exhibit a significant negative correlation (Spearman $\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\,{=}\,0$).
51	PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\textsc{var\_surprisal} and \textsc{p90\_ppl} yield negative $R^2$ under linear probing.
52	This confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\S\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the statistical features capture distributional tail properties that constitute the dominant depth markers.
53	
54	\subsection{Domain Bias Analysis}
55	\label{app:domain_bias}
56	
57	To assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.
58	
59	\paragraph{Methodological note.}
60	An initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\%, seed-group prediction 20.8\%).
61	We discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.
62	The results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.
63	
64	\paragraph{Sub-A: Standard CV.}
65	Five-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\% to 82\% across the 9 atlas cells (up to 2.5$\times$ above the 33.3\% chance level), confirming that depth signal is the dominant classification factor.
66	
67	\paragraph{Sub-B: LOGO evaluation.}
68	We assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.
69	LOGO mean accuracy is 72.1\% (range 59.5--81.6\%), matching standard CV (72.0\%) within noise (before fix: 64.0\%, reflecting the depth--group confound).
70	Per-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.
71	
72	\paragraph{Sub-C: Negative control.}
73	We train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\%).
74	Depth prediction accuracy averages 72.0\%; seed-group prediction averages 10.2\%---indistinguishable from chance (before fix: 20.8\%, inflated by the depth--group confound).
75	The depth-to-seed-group accuracy ratio is 7.1$\times$, confirming that the feature representation encodes depth but not seed-article identity.
76	
77	Taken together, these results show that seed-article grouping has no measurable effect on depth classification after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
78	
79	\subsection{Wild-Data Calibration}
80	\label{app:calibration}
81	
82	Table~\ref{tab:calibration} reports the prediction distribution of the Pythia-1.4B nucleus RF when applied to WikiText-103 test passages (out-of-distribution human text) and to controlled benchmark data.
83	
84	\begin{table}[h]
85	\centering
86	\small
87	\caption{WikiText-103 prediction distribution (Pythia-1.4B nucleus RF). All 546 passages are human-written (true d0); mean d0 posterior probability: 0.996.}
88	\label{tab:calibration}
89	\begin{tabular}{@{}lrcccc@{}}
90	\toprule
91	Source & $n$ & d0\% & d1\% & d2\% & d3\% \\
92	\midrule
93	WikiText-103 & 546 & \textbf{100.0} & 0.0 & 0.0 & 0.0 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\subsection{Extended Discussion}
99	\label{app:extended_discussion}
100	
101	\paragraph{Depth-graduated curation.}
102	Current data curation operates on a binary human-vs-machine distinction \cite{dsir2023,qurating2024}.
103	Recursive depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.
104	The 70--85\% in-distribution accuracy and $\mathrm{EDD}_{0.75}{=}4$ suggest such depth-graduated filtering is feasible across the model--strategy configurations we study, though its downstream effect on training quality remains to be validated empirically.
105	Importance weighting \cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.
106	
107	\paragraph{Toward a provenance toolkit.}
108	Depth estimation complements existing provenance methods along orthogonal axes.
109	Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
110	Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
111	Depth estimation characterizes \emph{iterative reuse} regardless of generator cooperation or identity.
112	A layered provenance system combining these three signals---watermark presence, source model, and recursion depth---could support more nuanced data auditing than any single method.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "d94d0526-2d43-4b71-ba65-ae792e1d9be3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
      "content": "\\section{Additional Results}\n\\label{app:additional}\n\n\\subsection{Top-$k$ Feature Trajectories}\n\\label{app:topk_trajectories}\n\nFigure~\\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\\tau{=}0.9$) sampling.\nTop-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\nConcretely, the d0$\\to$d1 drop in \\textsc{p90\\_ppl} under top-$k$ is 78\\% (vs.\\ 87\\% for nucleus), and the d2$\\to$d3 reduction is 31\\% (vs.\\ 39\\% for nucleus).\nDespite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.\n\n\\subsection{Permutation Importance}\n\\label{app:permutation}\n\nTo verify that the Gini-based importance rankings in \\S\\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.\nThe top-2 features are stable across measures: \\textsc{p90\\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \\textsc{var\\_surprisal} in 8/9 (vs.\\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \\textsc{p75\\_ppl} displaces \\textsc{var\\_surprisal} to rank 3).\nKendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).\nPairwise Spearman correlations are: SHAP--Gini $\\rho{=}0.93$, SHAP--permutation $\\rho{=}0.84$, Gini--permutation $\\rho{=}0.76$.\nPer-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.\n\n\\subsection{DCOL Iteration Details}\n\\label{app:dcol_iterations}\n\nTable~\\ref{tab:dcol_iterations} summarizes all six DCOL iterations.\nDeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\\%.}\n\\label{tab:dcol_iterations}\n\\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}\n\\toprule\nVer. & Backbone & Config & Outcome \\\\\n\\midrule\nv1 & DeBERTa & FT, m\\_lr $10^{-3}$ & Embed.\\ collapse (31.5\\%) \\\\\nv2 & DeBERTa & FT, m\\_lr $10^{-4}$ & OOM \\\\\nv3 & DeBERTa & FT, m\\_lr $10^{-4}$ & Forgetting + OOM \\\\\nv4 & DeBERTa & LoRA, m\\_lr $10^{-3}$ & Embed.\\ collapse \\\\\nv5 & DeBERTa & LoRA, m\\_lr $10^{-4}$ & NaN gradients \\\\\nv6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\\% ($-$13.7pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Overlap Analysis}\n\\label{app:feature_overlap}\n\nWe probe whether end-to-end PLM representations capture the same depth signals as our statistical features.\nDeBERTa attention importance and RF permutation importance exhibit a significant negative correlation (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the statistical features capture distributional tail properties that constitute the dominant depth markers.\n\n\\subsection{Domain Bias Analysis}\n\\label{app:domain_bias}\n\nTo assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.\n\n\\paragraph{Methodological note.}\nAn initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\\%, seed-group prediction 20.8\\%).\nWe discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.\nThe results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.\n\n\\paragraph{Sub-A: Standard CV.}\nFive-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\\% to 82\\% across the 9 atlas cells (up to 2.5$\\times$ above the 33.3\\% chance level), confirming that depth signal is the dominant classification factor.\n\n\\paragraph{Sub-B: LOGO evaluation.}\nWe assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.\nLOGO mean accuracy is 72.1\\% (range 59.5--81.6\\%), matching standard CV (72.0\\%) within noise (before fix: 64.0\\%, reflecting the depth--group confound).\nPer-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.\n\n\\paragraph{Sub-C: Negative control.}\nWe train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\\%).\nDepth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%---indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).\nThe depth-to-seed-group accuracy ratio is 7.1$\\times$, confirming that the feature representation encodes depth but not seed-article identity.\n\nTaken together, these results show that seed-article grouping has no measurable effect on depth classification after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\n\n\\subsection{Wild-Data Calibration}\n\\label{app:calibration}\n\nTable~\\ref{tab:calibration} reports the prediction distribution of the Pythia-1.4B nucleus RF when applied to WikiText-103 test passages (out-of-distribution human text) and to controlled benchmark data.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{WikiText-103 prediction distribution (Pythia-1.4B nucleus RF). All 546 passages are human-written (true d0); mean d0 posterior probability: 0.996.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nSource & $n$ & d0\\% & d1\\% & d2\\% & d3\\% \\\\\n\\midrule\nWikiText-103 & 546 & \\textbf{100.0} & 0.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Depth-graduated curation.}\nCurrent data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.\nRecursive depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest such depth-graduated filtering is feasible across the model--strategy configurations we study, though its downstream effect on training quality remains to be validated empirically.\nImportance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nDepth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining these three signals---watermark presence, source model, and recursion depth---could support more nuanced data auditing than any single method.\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of all the files. Let me work through each modification:

### Modification 1: W3 LoRA 引用定义恢复

In method.tex line 33, I see `LoRA finetuning \cite{hu2022lora}` mentioned but there's no definition of what LoRA actually does. I need to add a brief definition.

### Modification 2: R2-W2 术语一致性

I need to search for inconsistent terminology across all .tex files:
- "depth estimation" vs "depth classification"


- "generation depth" vs "recursion depth" vs "recursive depth"
- "model collapse" - first occurrence should have full citation
- "feature-based" vs "feature-engineered"

### Modification 3: R2-W4 Limitations 位置

Looking at main.tex, I see the structure ends with conclusion.tex before the bibliography and appendix. But conclusion.tex actually contains both the Discussion/Conclusion section and a Limitations section marked with `\section*{Limitations}`. The Limitations section appears to be incomplete, starting with `\section*{Ethics` but cutting off mid-way.

Checking the file order in main.tex: discussion.tex comes first with "Discussion and Conclusion", then conclusion.tex with the Limitations and Ethics Statement sections, followed by the bibliography and appendix. This placement seems to align with EMNLP requirements—Limitations should appear after the main conclusion but before references. Let me verify this matches the conference guidelines exactly.

Now I need to systematically check every bibliography entry to ensure all cited references are actually used in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "2b0ad786-92f1-48be-8556-fdef09e34142",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bx5uWsioCR4F6Y3AbtiMii",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15957,
      "cache_read_input_tokens": 34769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15957
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

_source line 34_

Now let me search for terminology inconsistencies and check bib citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "1d4d82c9-7ca6-4177-b858-d046effd38f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bx5uWsioCR4F6Y3AbtiMii",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15957,
      "cache_read_input_tokens": 34769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15957
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01H4Hy7NJ63qfYCm4gbhk8rn`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper && grep -n \"depth classification\\|depth estimation\\|recursion depth\\|recursive depth\\|generation depth\\|feature-engineered\\|feature-based\\|model collapse\" *.tex",
  "description": "Search for terminology inconsistencies across all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "7380483b-b30c-4a9b-98e0-90145cac9821",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bx5uWsioCR4F6Y3AbtiMii",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15957,
      "cache_read_input_tokens": 34769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15957
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

_source line 36 · 2026-05-15T22:07:39.339Z_

<details><summary>↩ Tool result · `toolu_01H4Hy7NJ63qfYCm4gbhk8rn`</summary>

```text
abstract.tex:3:We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
atlas.tex:4:We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
atlas.tex:46:Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \texttt{p90\_ppl} is robust to such extremes while still capturing the tail erosion that signals recursive depth.
conclusion.tex:16:Real-world documents may also interleave segments at different recursion depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.
conclusion.tex:19:Adversarial paraphrasing \cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.
conclusion.tex:40:Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
discussion.tex:4:We formalized recursive generation depth estimation and showed that 19 statistical features achieve 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
discussion.tex:5:The dominant pair (\texttt{p90\_ppl} top-2 in 9/9 cells, \texttt{var\_surprisal} in 7/9) generalizes across model families without retraining, making depth estimation a measurable early warning for model collapse~\cite{shumailov2024_nature}---though cross-strategy transfer remains the bottleneck (59.1\% vs.\ 66.4\%) and all experiments use 1--1.5B models.
generalization.tex:11:On Pythia nucleus, CORAL ordinal regression \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match the within-cell RF of Table~\ref{tab:main_matrix} within 0.1\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\%, $p<0.001$) and logistic regression (75.0\%).
generalization.tex:121:DCOL \cite{cloc2025} reached 64.5\% (Appendix~\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods, suggesting depth estimation benefits from explicit tail statistics absent from PLM representations.
introduction.tex:11:The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
introduction.tex:12:No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
introduction.tex:17:We formalize recursive generation depth estimation as an ordinal classification task and introduce a lightweight pipeline to solve it.
introduction.tex:19:To systematically characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) and decoding strategies (nucleus $p{=}0.95$, temperature $\tau{=}0.9$, top-$k$ $k{=}50$), each spanning 4 generation depths, totaling 180K samples.
introduction.tex:25:    \item \textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification and introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.
introduction.tex:31:    \item \textbf{End-to-end learning.} Both DeBERTa-v3-base (58.3\%) and RoBERTa-base (59.5\%) achieve ${\sim}$59\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\%)---with the architecture-invariant gap ruling out model selection bias. Linear probing confirms that PLM representations cannot recover perplexity tail features (negative $R^2$), while SHAP analysis shows these features account for 88.8\% of RF's contribution.
method.tex:11:Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
method.tex:17:We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
related_work.tex:22:\citet{uchendu2020_attribution} classify \emph{which} model generated text rather than recursion depth.
section_appendix.tex:25:DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
section_appendix.tex:52:This confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\S\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the statistical features capture distributional tail properties that constitute the dominant depth markers.
section_appendix.tex:77:Taken together, these results show that seed-article grouping has no measurable effect on depth classification after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.
section_appendix.tex:103:Recursive depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.
section_appendix.tex:112:A layered provenance system combining these three signals---watermark presence, source model, and recursion depth---could support more nuanced data auditing than any single method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "0931f393-ac0c-4ba5-9807-821517c46f3b",
  "tool_use_result": {
    "stdout": "abstract.tex:3:We formalize \\emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.\natlas.tex:4:We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.\natlas.tex:46:Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \\texttt{p90\\_ppl} is robust to such extremes while still capturing the tail erosion that signals recursive depth.\nconclusion.tex:16:Real-world documents may also interleave segments at different recursion depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.\nconclusion.tex:19:Adversarial paraphrasing \\cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.\nconclusion.tex:40:Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.\ndiscussion.tex:4:We formalized recursive generation depth estimation and showed that 19 statistical features achieve 70--85\\% four-class accuracy ($\\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\\% of full performance and classifier-agnostic convergence within $\\leq$0.4pp.\ndiscussion.tex:5:The dominant pair (\\texttt{p90\\_ppl} top-2 in 9/9 cells, \\texttt{var\\_surprisal} in 7/9) generalizes across model families without retraining, making depth estimation a measurable early warning for model collapse~\\cite{shumailov2024_nature}---though cross-strategy transfer remains the bottleneck (59.1\\% vs.\\ 66.4\\%) and all experiments use 1--1.5B models.\ngeneralization.tex:11:On Pythia nucleus, CORAL ordinal regression \\cite{coral2020} (78.1\\%) and DivEye \\cite{diveye2026} (78.2\\%) match the within-cell RF of Table~\\ref{tab:main_matrix} within 0.1\\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\\%, $p<0.001$) and logistic regression (75.0\\%).\ngeneralization.tex:121:DCOL \\cite{cloc2025} reached 64.5\\% (Appendix~\\ref{app:dcol_iterations}); all end-to-end approaches (58--65\\%) underperform feature-based methods, suggesting depth estimation benefits from explicit tail statistics absent from PLM representations.\nintroduction.tex:11:The model collapse literature \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \\citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.\nintroduction.tex:12:No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.\nintroduction.tex:17:We formalize recursive generation depth estimation as an ordinal classification task and introduce a lightweight pipeline to solve it.\nintroduction.tex:19:To systematically characterize how recursive generation reshapes these features, we construct the \\emph{Depth Degradation Atlas}: a $3 \\times 3$ grid of model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) and decoding strategies (nucleus $p{=}0.95$, temperature $\\tau{=}0.9$, top-$k$ $k{=}50$), each spanning 4 generation depths, totaling 180K samples.\nintroduction.tex:25:    \\item \\textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification and introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.\nintroduction.tex:31:    \\item \\textbf{End-to-end learning.} Both DeBERTa-v3-base (58.3\\%) and RoBERTa-base (59.5\\%) achieve ${\\sim}$59\\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\\%)---with the architecture-invariant gap ruling out model selection bias. Linear probing confirms that PLM representations cannot recover perplexity tail features (negative $R^2$), while SHAP analysis shows these features account for 88.8\\% of RF's contribution.\nmethod.tex:11:Given a text passage $x$, the task is to estimate its recursive generation depth $d \\in \\{0, 1, \\dots, K\\}$.\nmethod.tex:17:We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.\nrelated_work.tex:22:\\citet{uchendu2020_attribution} classify \\emph{which} model generated text rather than recursion depth.\nsection_appendix.tex:25:DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\nsection_appendix.tex:52:This confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the statistical features capture distributional tail properties that constitute the dominant depth markers.\nsection_appendix.tex:77:Taken together, these results show that seed-article grouping has no measurable effect on depth classification after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\nsection_appendix.tex:103:Recursive depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nsection_appendix.tex:112:A layered provenance system combining these three signals---watermark presence, source model, and recursion depth---could support more nuanced data auditing than any single method.",
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01Le76s5tNFJrYMVfN7VyfRM`</summary>

```json
{
  "command": "grep -oP '(?<=@\\w{1,20}\\{)[^,]+' references.bib | sort",
  "description": "Extract all bib entry keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "99d84c68-ea97-4ea9-8ee3-4252efb3907f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bx5uWsioCR4F6Y3AbtiMii",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15957,
      "cache_read_input_tokens": 34769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15957
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

_source line 38 · 2026-05-15T22:07:40.378Z_

<details><summary>↩ Tool result · `toolu_01Le76s5tNFJrYMVfN7VyfRM`</summary>

```text
alemohammad2024_mad
bakshi2026_collapse_improvement
basu2021_mirostat
binoculars2024
cloc2025
coral2020
diveye2026
dohmatob2024_demystified
dohmatob2024_strong_collapse
dohmatob2024_tale_of_tails
drayson2025_detection_prevents_collapse
dsir2023
editlens2026
falahati2026_curated
fast_detectgpt2024
finlayson2024_closing
garces_arias2025_decoding_decoded
gehrmann2019_gltr
gerstgrasser2024_accumulate
he2021_deberta_v3
holtzman2020_nucleus
hu2022lora
kirchenbauer2023_watermark
knowledge_collapse2025
liu2019_roberta
loki2025
marchi2024_heat_death
mitchell2023_detectgpt
mohamed2025_broken_telephone
pu2026_generator_barrier
pudasaini2026_detection_fails
qurating2024
sadasivan2023_paraphrase
shumailov2024_nature
sigma2026_spectral
sugiyama2007_importance_weighting
synthetic_eggs2026
uchendu2020_attribution
verma2024_ghostbuster
wang2024_m4_semeval
wang2026_contamination
wiher2022_decoding
yang2024_dnagpt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "994cf885-e8ed-4a85-b075-94c9d57a61d7",
  "tool_use_result": {
    "stdout": "alemohammad2024_mad\nbakshi2026_collapse_improvement\nbasu2021_mirostat\nbinoculars2024\ncloc2025\ncoral2020\ndiveye2026\ndohmatob2024_demystified\ndohmatob2024_strong_collapse\ndohmatob2024_tale_of_tails\ndrayson2025_detection_prevents_collapse\ndsir2023\neditlens2026\nfalahati2026_curated\nfast_detectgpt2024\nfinlayson2024_closing\ngarces_arias2025_decoding_decoded\ngehrmann2019_gltr\ngerstgrasser2024_accumulate\nhe2021_deberta_v3\nholtzman2020_nucleus\nhu2022lora\nkirchenbauer2023_watermark\nknowledge_collapse2025\nliu2019_roberta\nloki2025\nmarchi2024_heat_death\nmitchell2023_detectgpt\nmohamed2025_broken_telephone\npu2026_generator_barrier\npudasaini2026_detection_fails\nqurating2024\nsadasivan2023_paraphrase\nshumailov2024_nature\nsigma2026_spectral\nsugiyama2007_importance_weighting\nsynthetic_eggs2026\nuchendu2020_attribution\nverma2024_ghostbuster\nwang2024_m4_semeval\nwang2026_contamination\nwiher2022_decoding\nyang2024_dnagpt",
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01EsPcSjxUsuVgBQcH3FeTd8`</summary>

```json
{
  "command": "for key in $(grep -oP '(?<=@\\w{1,20}\\{)[^,]+' references.bib | sort); do count=$(grep -c \"\\\\\\\\cite.*${key}\\|\\\\\\\\citet.*${key}\\|\\\\\\\\citep.*${key}\" *.tex 2>/dev/null); echo \"$key: $count\"; done",
  "description": "Check each bib entry for citations in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "21620fef-fac6-4db4-a0c4-0c5433c3aba2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Sjtr7b7D4fmweA43YoTia",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2963,
      "cache_read_input_tokens": 50726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2963
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 40 · 2026-05-15T22:07:45.080Z_

<details><summary>↩ Tool result · `toolu_01EsPcSjxUsuVgBQcH3FeTd8`</summary>

```text
alemohammad2024_mad: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:1
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
bakshi2026_collapse_improvement: abstract.tex:0
atlas.tex:0
conclusion.tex:1
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
basu2021_mirostat: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
binoculars2024: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:1
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
cloc2025: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:1
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
coral2020: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:1
introduction.tex:0
main.tex:0
method.tex:1
related_work.tex:1
section_appendix.tex:0
diveye2026: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:1
introduction.tex:1
main.tex:0
method.tex:1
related_work.tex:1
section_appendix.tex:0
dohmatob2024_demystified: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
dohmatob2024_strong_collapse: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
dohmatob2024_tale_of_tails: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:2
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
drayson2025_detection_prevents_collapse: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:1
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
dsir2023: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:0
section_appendix.tex:1
editlens2026: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
falahati2026_curated: abstract.tex:0
atlas.tex:0
conclusion.tex:1
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
fast_detectgpt2024: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:1
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
finlayson2024_closing: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
garces_arias2025_decoding_decoded: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
gehrmann2019_gltr: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
gerstgrasser2024_accumulate: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
he2021_deberta_v3: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:1
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:0
section_appendix.tex:0
holtzman2020_nucleus: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:1
related_work.tex:1
section_appendix.tex:0
hu2022lora: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:1
related_work.tex:0
section_appendix.tex:0
kirchenbauer2023_watermark: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:1
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:1
knowledge_collapse2025: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
liu2019_roberta: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:1
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:0
section_appendix.tex:0
loki2025: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
marchi2024_heat_death: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
mitchell2023_detectgpt: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
mohamed2025_broken_telephone: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
pu2026_generator_barrier: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
pudasaini2026_detection_fails: abstract.tex:0
atlas.tex:0
conclusion.tex:1
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
qurating2024: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:0
section_appendix.tex:1
sadasivan2023_paraphrase: abstract.tex:0
atlas.tex:0
conclusion.tex:1
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
shumailov2024_nature: abstract.tex:0
atlas.tex:2
conclusion.tex:0
discussion.tex:1
generalization.tex:0
introduction.tex:2
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
sigma2026_spectral: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
sugiyama2007_importance_weighting: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:0
section_appendix.tex:1
synthetic_eggs2026: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
uchendu2020_attribution: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:1
verma2024_ghostbuster: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
wang2024_m4_semeval: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
wang2026_contamination: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
wiher2022_decoding: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
yang2024_dnagpt: abstract.tex:0
atlas.tex:0
conclusion.tex:0
discussion.tex:0
generalization.tex:0
introduction.tex:0
main.tex:0
method.tex:0
related_work.tex:1
section_appendix.tex:0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "02abbd07-a5a7-4a68-93b2-f6f3e842c4ab",
  "tool_use_result": {
    "stdout": "alemohammad2024_mad: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:1\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nbakshi2026_collapse_improvement: abstract.tex:0\natlas.tex:0\nconclusion.tex:1\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nbasu2021_mirostat: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nbinoculars2024: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:1\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ncloc2025: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:1\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ncoral2020: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:1\nintroduction.tex:0\nmain.tex:0\nmethod.tex:1\nrelated_work.tex:1\nsection_appendix.tex:0\ndiveye2026: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:1\nintroduction.tex:1\nmain.tex:0\nmethod.tex:1\nrelated_work.tex:1\nsection_appendix.tex:0\ndohmatob2024_demystified: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ndohmatob2024_strong_collapse: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ndohmatob2024_tale_of_tails: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:2\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ndrayson2025_detection_prevents_collapse: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:1\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ndsir2023: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:0\nsection_appendix.tex:1\neditlens2026: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nfalahati2026_curated: abstract.tex:0\natlas.tex:0\nconclusion.tex:1\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nfast_detectgpt2024: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:1\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nfinlayson2024_closing: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ngarces_arias2025_decoding_decoded: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ngehrmann2019_gltr: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\ngerstgrasser2024_accumulate: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nhe2021_deberta_v3: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:1\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:0\nsection_appendix.tex:0\nholtzman2020_nucleus: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:1\nrelated_work.tex:1\nsection_appendix.tex:0\nhu2022lora: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:1\nrelated_work.tex:0\nsection_appendix.tex:0\nkirchenbauer2023_watermark: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:1\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:1\nknowledge_collapse2025: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nliu2019_roberta: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:1\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:0\nsection_appendix.tex:0\nloki2025: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nmarchi2024_heat_death: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nmitchell2023_detectgpt: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nmohamed2025_broken_telephone: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\npu2026_generator_barrier: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\npudasaini2026_detection_fails: abstract.tex:0\natlas.tex:0\nconclusion.tex:1\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nqurating2024: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:0\nsection_appendix.tex:1\nsadasivan2023_paraphrase: abstract.tex:0\natlas.tex:0\nconclusion.tex:1\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nshumailov2024_nature: abstract.tex:0\natlas.tex:2\nconclusion.tex:0\ndiscussion.tex:1\ngeneralization.tex:0\nintroduction.tex:2\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nsigma2026_spectral: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nsugiyama2007_importance_weighting: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:0\nsection_appendix.tex:1\nsynthetic_eggs2026: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nuchendu2020_attribution: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:1\nverma2024_ghostbuster: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nwang2024_m4_semeval: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nwang2026_contamination: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nwiher2022_decoding: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0\nyang2024_dnagpt: abstract.tex:0\natlas.tex:0\nconclusion.tex:0\ndiscussion.tex:0\ngeneralization.tex:0\nintroduction.tex:0\nmain.tex:0\nmethod.tex:0\nrelated_work.tex:1\nsection_appendix.tex:0",
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
All bib entries are cited at least once. Let me verify by summing up each entry's citations across all files:

- alemohammad2024_mad: 2 (intro 1 + related 1)
- bakshi2026_collapse_improvement: 2 (conclusion 1 + related 1)
- basu2021_mirostat: 1 (related 1)
- binoculars2024: 2 (intro 1 + related 1)


- cloc2025: 2 (gen 1 + related 1)
- coral2020: 3 (gen 1 + method 1 + related 1)
- diveye2026: 4 (gen 1 + intro 1 + method 1 + related 1)
- dohmatob2024_demystified: 1 (related 1)
- dohmatob2024_strong_collapse: 1 (related 1)
- dohmatob2024_tale_of_tails: 3 (intro 2 + related 1)

Continuing through the rest of the entries to ensure complete coverage. Continuing through the citations, I'm seeing more papers on detection methods and model collapse across various approaches—LoRA fine-tuning, watermarking techniques, and detection failure scenarios all appear in the related work sections, with a few key papers like Kirchenbauer's watermark study showing up across multiple sections. Now I'm checking for terminology consistency across the paper. I notice "depth classification" appears in the appendix when discussing the effect of seed-article grouping, but since the formal task throughout is "depth estimation," I should standardize on that term. I'm also tracking the various depth-related terms like "recursion depth" and "recursive depth" to ensure they're used consistently. Looking more carefully at the introduction, I see "distributional collapse" appears first on line 6, but that's distinct from "model collapse" which is introduced later on line 11 with proper citations. The first actual use of the term "model collapse" in the paper is in the introduction with references already attached, so that's acceptable. The paper already provides context about model collapse's effects in the preceding sentence, and the citations are in place, so I think that's sufficient. Now let me check for "feature-engineered" — I'm only seeing "feature-based" in the results, which is good. For "depth classification," there's one instance in the appendix that should be changed to "depth estimation" for consistency. So I need to make a few targeted modifications: add a brief definition for W3 LoRA in the methods section, and swap that terminology in the appendix. I'm working through the remaining terminology updates for the paper. The recursion depth references need to be changed to generation depth across several files, and I'm verifying the section structure matches EMNLP requirements—the Limitations section is already correctly positioned after the Conclusion and before References, so that's good. I've also confirmed there are no orphaned bibliography entries to clean up, so I can move forward with implementing these edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "3238cadc-cc24-4d1d-bae3-a5da02057257",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

Analysis complete. Now applying the changes.

**Summary of findings:**
- **Mod 1 (W3):** LoRA is cited on method.tex:33 but lacks definition — needs one.
- **Mod 2 (R2-W2):** 6 terminology inconsistencies found.
- **Mod 3 (R2-W4):** Limitations is already correctly positioned (after Conclusion, before References). No change needed.
- **Mod 4 (R2-W6):** All 43 bib entries are cited at least once. No orphans.

Applying edits now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "47d5aba0-7b73-4e94-9fe6-56d811772843",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

_source line 43_

<details open><summary>🔧 Tool call — Edit · `toolu_016BNJS3CNCioCgwkhu8gytL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
  "old_string": "(1)~LoRA finetuning \\cite{hu2022lora} with $r{=}16$,",
  "new_string": "(1)~Low-Rank Adaptation (LoRA; \\cite{hu2022lora}), which freezes base model weights and trains low-rank update matrices ($<$1\\% additional parameters), with $r{=}16$,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "a37a95a7-1ca1-4f9b-b758-df53de30dcae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

_source line 44 · 2026-05-15T22:08:30.590Z_

<details><summary>↩ Tool result · `toolu_016BNJS3CNCioCgwkhu8gytL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "d21b5547-bd54-49ec-b2f6-2430d4aa5895",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
    "oldString": "(1)~LoRA finetuning \\cite{hu2022lora} with $r{=}16$,",
    "newString": "(1)~Low-Rank Adaptation (LoRA; \\cite{hu2022lora}), which freezes base model weights and trains low-rank update matrices ($<$1\\% additional parameters), with $r{=}16$,",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Definition}\n\\label{sec:method:problem}\n\nLet $f_\\theta$ denote a language model and $\\mathcal{D}_0$ a corpus of human-written seed text.\nWe define a \\emph{recursive generation chain} of depth $K$ as the sequence $\\mathcal{D}_0, \\mathcal{D}_1, \\dots, \\mathcal{D}_K$, where each $\\mathcal{D}_k$ ($k \\geq 1$) is produced by finetuning $f_\\theta$ on $\\mathcal{D}_{k-1}$ and sampling from the resulting model.\nDepth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \\geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.\n\nGiven a text passage $x$, the task is to estimate its recursive generation depth $d \\in \\{0, 1, \\dots, K\\}$.\nThis is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.\n\n\\subsection{Multi-Generational Benchmark Construction}\n\\label{sec:method:benchmark}\n\nWe construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.\n\n\\paragraph{Model families.}\nWe select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).\nRestricting to a narrow parameter range isolates the effect of architecture and training data from scale.\n\n\\paragraph{Decoding strategies.}\nEach model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \\cite{holtzman2020_nucleus}, temperature sampling ($\\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).\nThese span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.\nOur findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.\n\n\\paragraph{Depth and scale.}\nThe primary benchmark covers depths d0--d3 across all $3 \\times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).\nFor depth extension experiments (\\S\\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.\n\n\\paragraph{Generation pipeline.}\nStarting from a Wikipedia subset as seed text ($\\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \\cite{hu2022lora} with $r{=}16$, $\\alpha{=}32$, lr $2{\\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$ (architecture-specific targets); (2)~unconditional generation of 5{,}000 passages (max 512 tokens, starting from BOS) under the specified decoding strategy; (3)~the generated corpus becomes $\\mathcal{D}_k$ for the next cycle.\nThere is no per-passage lineage across depths, ensuring cross-validation splits do not introduce information leakage.\n\n\\paragraph{Reference model.}\nAll statistical features (\\S\\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.\nThe reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.\nIn cross-model leave-one-out evaluation (\\S\\ref{sec:generalization}), the reference model remains fixed even when GPT-2~XL is held out; the partial architectural overlap this introduces is discussed in Limitations.\n\n\\subsection{Statistical Feature Design}\n\\label{sec:method:features}\n\nWe extract a 19-dimensional feature vector $\\mathbf{f}(x)$ from the reference-model perplexity distribution over each passage $x$.\nThe features fall into four categories (Table~\\ref{tab:features}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{The 19 statistical features comprising $\\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (GPT-2 base, 124M).}\n\\label{tab:features}\n\\begin{tabular}{@{}llr@{}}\n\\toprule\nCategory & Features & $n$ \\\\\n\\midrule\nPerplexity & mean, var, skewness, kurtosis, & 9 \\\\\nstatistics & p10, p25, p50, p75, p90 & \\\\\n\\addlinespace\nSurprisal & mean, var, entropy & 3 \\\\\nstatistics & & \\\\\n\\addlinespace\nLexical & type--token ratio, hapax ratio, & 4 \\\\\ndiversity & bigram entropy, trigram entropy & \\\\\n\\addlinespace\nRepetition & repeated 2/3/4-gram fractions & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\emph{Perplexity statistics} (9 features) capture the per-token perplexity distribution via moments (mean, variance, skewness, kurtosis) and quantiles (p10--p90); tail quantiles prove especially informative as recursive finetuning erodes the high-perplexity tail (\\S\\ref{sec:atlas}).\n\\emph{Surprisal statistics} (3 features): mean, variance, and entropy of $-\\log p(\\text{token})$; surprisal variance captures second-order structure not redundant with perplexity moments.\n\\emph{Lexical diversity} (4 features): type--token ratio, hapax ratio, bigram/trigram entropy.\n\\emph{Repetition} (3 features): repeated $n$-gram fractions for $n \\in \\{2, 3, 4\\}$.\n\n\\subsection{Effective Discriminable Depth}\n\\label{sec:method:edd}\n\nAggregate accuracy obscures whether discriminability degrades at specific depths.\nWe introduce the \\emph{Effective Discriminable Depth} (EDD): for each adjacent pair $(d, d{+}1)$, we train a dedicated binary RF (500 trees, 5-fold stratified CV) and compute AUC.\nGiven threshold $T$:\n\\begin{equation}\n\\mathrm{EDD}_T = \\max \\bigl\\{ d^*{+}1 : \\forall\\, d' \\leq d^*,\\; \\mathrm{AUC}(d', d'{+}1) \\geq T \\bigr\\}\n\\label{eq:edd}\n\\end{equation}\nwhere $d^* \\in \\{0, \\dots, K{-}1\\}$; $\\mathrm{EDD}_T = 0$ if $\\mathrm{AUC}(0,1) < T$.\\footnote{Our AUC profiles are monotonically decreasing; for non-monotonic profiles, EDD reports the longest contiguous discriminable prefix (see Limitations).}\nDefault $T{=}0.75$; sensitivity at $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$ in \\S\\ref{sec:atlas}.\nEach AUC is from an independent binary classifier, avoiding decision boundary dilution (\\S\\ref{sec:atlas}).\n\n\\paragraph{Classifiers.}\nOur primary classifier is a Random Forest (200 trees, unconstrained depth, 5-fold stratified cross-validation).\nWe compare against CORAL ordinal regression \\cite{coral2020}, DivEye \\cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \\S\\ref{sec:generalization}.",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 7,
        "newStart": 30,
        "newLines": 7,
        "lines": [
          " For depth extension experiments (\\S\\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.",
          " ",
          " \\paragraph{Generation pipeline.}",
          "-Starting from a Wikipedia subset as seed text ($\\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \\cite{hu2022lora} with $r{=}16$, $\\alpha{=}32$, lr $2{\\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$ (architecture-specific targets); (2)~unconditional generation of 5{,}000 passages (max 512 tokens, starting from BOS) under the specified decoding strategy; (3)~the generated corpus becomes $\\mathcal{D}_k$ for the next cycle.",
          "+Starting from a Wikipedia subset as seed text ($\\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~Low-Rank Adaptation (LoRA; \\cite{hu2022lora}), which freezes base model weights and trains low-rank update matrices ($<$1\\% additional parameters), with $r{=}16$, $\\alpha{=}32$, lr $2{\\times}10^{-4}$, batch size 8, 3 epochs, dropout $0.05$ (architecture-specific targets); (2)~unconditional generation of 5{,}000 passages (max 512 tokens, starting from BOS) under the specified decoding strategy; (3)~the generated corpus becomes $\\mathcal{D}_k$ for the next cycle.",
          " There is no per-passage lineage across depths, ensuring cross-validation splits do not introduce information leakage.",
          " ",
          " \\paragraph{Reference model.}"
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01E4a21BAAsseSeyNkuZBkbV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "old_string": "still capturing the tail erosion that signals recursive depth.",
  "new_string": "still capturing the tail erosion that signals generation depth."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "9e5614b0-ff4a-499e-814f-bdb5789c5684",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

_source line 46 · 2026-05-15T22:08:31.991Z_

<details><summary>↩ Tool result · `toolu_01E4a21BAAsseSeyNkuZBkbV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "e6d9ef62-f76a-492b-abb3-a43c3ea42fc2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
    "oldString": "still capturing the tail erosion that signals recursive depth.",
    "newString": "still capturing the tail erosion that signals generation depth.",
    "originalFile": "\\section{The Depth Degradation Atlas}\n\\label{sec:atlas}\n\nWe present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.\nThe atlas spans $3 \\times 3 = 9$ model--strategy cells evaluated at depths $d \\in \\{0, 1, 2, 3\\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\\S\\ref{sec:atlas:edd}).\n\n%% ----------------------------------------------------------------\n\\subsection{In-Distribution Performance}\n\\label{sec:atlas:id}\n\nTable~\\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.\nAccuracy ranges from 69.6\\% (Pythia, top-$k$) to 85.4\\% (GPT-2~XL, temperature), all exceeding the 25\\% chance baseline by a wide margin.\nTwo axis effects emerge.\nGPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\\%), followed by OLMo (74.2--82.0\\%) and Pythia (69.6--78.2\\%).\nTop-$k$ sampling yields the lowest accuracy in every model.\nThe mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Four-class RF accuracy (\\%) across the $3 \\times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\\% / 33\\%). Depth-0 recall exceeds 98\\% in all cells.}\n\\label{tab:main_matrix}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n& Nucleus & Temp.\\ $\\tau{=}0.9$ & Top-$k$ \\\\\n\\midrule\nPythia-1.4B  & 78.2\\,(71.2) & 76.3\\,(70.6) & 69.6\\,(58.8) \\\\\nOLMo-1B     & 78.8\\,(75.0) & 82.0\\,(76.3) & 74.2\\,(66.1) \\\\\nGPT-2~XL    & 83.3\\,(79.0) & 85.4\\,(82.6) & 76.6\\,(69.5) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ----------------------------------------------------------------\n\\subsection{Feature Universality}\n\\label{sec:atlas:features}\n\nDespite the 15.8~pp accuracy spread across cells, a small feature family dominates in every setting.\nThe 90th-percentile perplexity (\\texttt{p90\\_ppl}) ranks top-2 by Gini importance in all 9 cells; surprisal variance (\\texttt{var\\_surprisal}) in 7/9 (8/9 under SHAP; Appendix~\\ref{app:permutation}).\nTable~\\ref{tab:feature_importance} shows the full per-cell ranking.\n\nCross-model feature-rank Spearman correlation averages $\\bar{\\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.\nAmong strategies, top-$k$ yields the highest cross-model rank correlation ($\\rho = 0.811$)---the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\\S\\ref{sec:atlas:strategy}).\n\nPercentile-based features outperform their moment-based counterparts.\nToken-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \\texttt{p90\\_ppl} is robust to such extremes while still capturing the tail erosion that signals recursive depth.\n\nFeature ablation confirms this concentration: the top-5 features achieve 97.6\\% of full accuracy (76.5\\% vs.\\ 78.4\\%), with perplexity statistics alone reaching 76.6\\% (vs.\\ surprisal 73.2\\%, other categories $<$46\\%).\nForward selection independently confirms the dominant pair: \\texttt{var\\_surprisal} is selected first in 6/9 cells, \\texttt{p90\\_ppl} in 3/9.\n\nThe feature hierarchy also shifts with depth.\nAt shallow boundaries (d1 vs.\\ d2), \\texttt{var\\_surprisal} dominates importance; at deeper boundaries (d3 vs.\\ d4, d4 vs.\\ d5), tail perplexity statistics (\\texttt{p90\\_ppl}, \\texttt{kurtosis\\_ppl}) take over.\nThis transition aligns with model-collapse dynamics~\\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Top-5 features by Gini importance. \\textbf{Bold}: top-2. \\texttt{p90\\_ppl} top-2 in 9/9; \\texttt{var\\_surprisal} 7/9 (8/9 under SHAP).}\n\\label{tab:feature_importance}\n\\begin{tabular}{@{}l l@{}}\n\\toprule\nCell & Top-5 features (Gini importance, ranked) \\\\\n\\midrule\nPythia, nuc.       & \\textbf{var\\_surp\\,(.17)}, \\textbf{p90\\_ppl\\,(.15)}, m\\_ppl\\,(.11), var\\_ppl\\,(.08), p75\\,(.07) \\\\\nPythia, $\\tau$     & \\textbf{var\\_surp\\,(.17)}, \\textbf{p90\\_ppl\\,(.14)}, m\\_ppl\\,(.11), p75\\,(.07), m\\_surp\\,(.07) \\\\\nPythia, top-$k$    & \\textbf{var\\_surp\\,(.16)}, \\textbf{p90\\_ppl\\,(.12)}, m\\_ppl\\,(.11), var\\_ppl\\,(.07), m\\_surp\\,(.06) \\\\\nGPT-2\\,XL, nuc.    & \\textbf{var\\_surp\\,(.21)}, \\textbf{p90\\_ppl\\,(.21)}, p75\\,(.10), m\\_surp\\,(.07), m\\_ppl\\,(.06) \\\\\nGPT-2\\,XL, $\\tau$  & \\textbf{p90\\_ppl\\,(.25)}, \\textbf{p75\\,(.15)}, m\\_surp\\,(.13), var\\_surp\\,(.12), p50\\,(.05) \\\\\nGPT-2\\,XL, top-$k$ & \\textbf{p90\\_ppl\\,(.24)}, \\textbf{p75\\,(.12)}, var\\_surp\\,(.10), m\\_surp\\,(.09), ttr\\,(.04) \\\\\nOLMo, nuc.         & \\textbf{p90\\_ppl\\,(.18)}, \\textbf{var\\_surp\\,(.15)}, p75\\,(.11), m\\_surp\\,(.07), ttr\\,(.06) \\\\\nOLMo, $\\tau$       & \\textbf{p90\\_ppl\\,(.21)}, \\textbf{var\\_surp\\,(.16)}, p75\\,(.12), m\\_surp\\,(.09), ttr\\,(.05) \\\\\nOLMo, top-$k$      & \\textbf{p90\\_ppl\\,(.20)}, \\textbf{var\\_surp\\,(.17)}, p75\\,(.10), m\\_surp\\,(.07), m\\_ppl\\,(.05) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_atlas_heatmap.pdf}\n\\caption{Atlas feature importance heatmap. Rows: 19 features grouped by category (\\S\\ref{sec:method:features}); columns: 9 model--strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.}\n\\label{fig:atlas_heatmap}\n\\end{figure}\n\n%% ----------------------------------------------------------------\n\\subsection{Monotonicity and Inter-Depth Distances}\n\\label{sec:atlas:monotonicity}\n\nDepth features exhibit strong monotonic trends: perplexity tail statistics (\\texttt{p90\\_ppl}, \\texttt{mean\\_surprisal}) decrease with depth (Spearman $\\rho = -1.0$ across cell-level medians) while repetition features increase, reflecting the complementary narrowing and self-repetition of distribution collapse.\nInter-depth distances are non-uniform: d0-vs-d1 AUC exceeds 0.99 in all 9 cells, whereas d2-vs-d3 ranges from 0.69 to 0.89---separating adjacent deep generations requires the tail statistics identified in \\S\\ref{sec:atlas:features}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_trajectory.pdf}\n\\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \\texttt{p90\\_ppl} (monotonically decreasing). Middle: \\texttt{var\\_surprisal} (decreasing). Bottom: \\texttt{rep\\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \\to d{=}1$ gap exceeds all subsequent inter-depth gaps.}\n\\label{fig:feature_trajectory}\n\\end{figure}\n\n%% ----------------------------------------------------------------\n\\subsection{EDD Analysis}\n\\label{sec:atlas:edd}\n\nWe extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.\nEach model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (GPT-2 base, 124M).\nWe train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\\ref{eq:edd}.\n\n\\paragraph{AUC decay profile.}\nFigure~\\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.\nFor Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.\nThe steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.\n\n\\paragraph{Cross-model convergence at depth 4--5.}\nThe d3-vs-d4 AUC clusters near $T{=}0.75$ (Pythia $0.784$, OLMo $0.765$, GPT-2~XL $0.750$; bootstrap CIs in Figure~\\ref{fig:auc_decay}), while d4-vs-d5 falls uniformly below 0.70 ($0.681$--$0.684$), confirming model-independent signal saturation at depth~5.\nThis graded decay supports interpreting the d3--d4 region as a \\emph{transition zone} rather than a binary boundary.\n\n\\paragraph{EDD threshold sensitivity.}\nTable~\\ref{tab:edd_sensitivity} reports $\\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.\nAt $T{=}0.65$, all 9 cells achieve $\\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\\mathrm{EDD} \\geq 3$; at $T{=}0.80$, the count drops to 5 of 9.\nThe cells losing $\\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Number of atlas cells achieving $\\mathrm{EDD} \\geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}\n\\label{tab:edd_sensitivity}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n& $T{=}0.65$ & $T{=}0.70$ & $T{=}0.75$ & $T{=}0.80$ \\\\\n\\midrule\nCells with $\\mathrm{EDD} \\geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_auc_decay.pdf}\n\\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \\in \\{0.65, 0.70, 0.75, 0.80\\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\\% CIs.}\n\\label{fig:auc_decay}\n\\end{figure}\n\n\\paragraph{Decision boundary dilution.}\n\\label{sec:atlas:edd:dilution}\nEDD uses binary-pair classifiers to avoid \\emph{decision boundary dilution}: in Pythia nucleus, d2\\,vs.\\,d3 AUC degrades from 0.804 (4-class) to 0.689 (6-class)---a 14.3\\% relative decline despite identical data---because shared decision boundaries dilute per-pair capacity.\nBinary classifiers eliminate this confound, isolating true adjacent-pair discriminability.\n\n%% ----------------------------------------------------------------\n\\subsection{Strategy-Dependent Trajectories}\n\\label{sec:atlas:strategy}\n\nThe three decoding strategies induce qualitatively distinct degradation trajectories.\nNucleus ($p{=}0.95$) produces the most consistent accuracy (78.2--83.3\\%) and serves as the reference trajectory.\nTemperature ($\\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.4\\%, OLMo 82.0\\%) because uniform logit scaling accelerates convergence to an attractor distribution~\\cite{shumailov2024_nature}, amplifying the statistical fingerprint---but this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\\S\\ref{sec:generalization}).\nTop-$k$ ($k{=}50$) produces the lowest accuracy (69.6--76.6\\%) because hard vocabulary truncation removes depth-discriminative low-probability tokens, though feature direction is preserved (cross-model $\\rho = 0.811$).\nThe strategy effect (8.4~pp range) exceeds the model effect (7.1~pp), indicating deployment-time knowledge of the decoding strategy matters at least as much as the generator model.\n",
    "structuredPatch": [
      {
        "oldStart": 43,
        "oldLines": 7,
        "newStart": 43,
        "newLines": 7,
        "lines": [
          " Among strategies, top-$k$ yields the highest cross-model rank correlation ($\\rho = 0.811$)---the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\\S\\ref{sec:atlas:strategy}).",
          " ",
          " Percentile-based features outperform their moment-based counterparts.",
          "-Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \\texttt{p90\\_ppl} is robust to such extremes while still capturing the tail erosion that signals recursive depth.",
          "+Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \\texttt{p90\\_ppl} is robust to such extremes while still capturing the tail erosion that signals generation depth.",
          " ",
          " Feature ablation confirms this concentration: the top-5 features achieve 97.6\\% of full accuracy (76.5\\% vs.\\ 78.4\\%), with perplexity statistics alone reaching 76.6\\% (vs.\\ surprisal 73.2\\%, other categories $<$46\\%).",
          " Forward selection independently confirms the dominant pair: \\texttt{var\\_surprisal} is selected first in 6/9 cells, \\texttt{p90\\_ppl} in 3/9."
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

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_01KSwVA2pDv4Sc3b7exWN7Ct`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
  "old_string": "segments at different recursion depths",
  "new_string": "segments at different recursive generation depths"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "0f5350bc-162c-4ff3-874c-0c6766df1b1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

_source line 48 · 2026-05-15T22:08:32.932Z_

<details><summary>↩ Tool result · `toolu_01KSwVA2pDv4Sc3b7exWN7Ct`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "31f06056-a37e-4633-9762-f0e7ae20806d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex",
    "oldString": "segments at different recursion depths",
    "newString": "segments at different recursive generation depths",
    "originalFile": "\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Cross-strategy deployment constraint.}\nCross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.\nPer-strategy z-score normalization partially corrects the inversion (GPT-2~XL d1v2 AUC $0.24{\\to}0.56$, OLMo $0.19{\\to}0.70$) but leaves a residual gap relative to within-strategy performance (${\\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.\n\n\\paragraph{d0 inflation of headline metrics.}\nDepth~0 (human-written text) is near-perfectly separable (recall $>$98\\% across all settings), inflating headline accuracy.\nCross-model transfer accuracy of 66.4\\% is substantially driven by d0; d2 recall drops to 26.8\\% in the worst case (Pythia holdout).\n\n\\paragraph{Controlled vs.\\ ecological setting.}\nAll experiments use Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models).\nDepth signal is the dominant classification factor (5-fold CV 59--82\\%, up to 2.5$\\times$ chance): LOGO accuracy (72.1\\%) matches standard CV (72.0\\%), and seed-group prediction is at chance (10.2\\% vs.\\ 10\\%; Appendix~\\ref{app:domain_bias}).\nTransfer to mixed-domain corpora, instruction-tuned models, and larger scales (7B+) remains open.\nReal-world documents may also interleave segments at different recursion depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.\n\n\\paragraph{Adversarial robustness.}\nAdversarial paraphrasing \\cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.\n\n\\paragraph{EDD monotonicity assumption.}\nOur EDD definition (Eq.~\\ref{eq:edd}) requires all pairwise AUCs up to depth $d^*$ to exceed $T$, which is well-behaved when AUC decays monotonically---as observed in all our configurations.\nHowever, \\citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \\emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).\nOur cross-strategy transfer results provide an empirical example: training on nucleus + top-$k$ and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2~XL) and 0.253 (OLMo), violating the monotonicity assumption.\nIn such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work.\nThe choice of threshold $T$ is also application-dependent: at $T{=}0.80$, several cells lose one depth level relative to $T{=}0.75$.\n\n\\paragraph{Reference model dependency.}\nSurprisal-based features are computed relative to GPT-2 base (124M), introducing partial overlap when GPT-2~XL is held out, though GPT-2~XL holdout accuracy (67.6\\%) does not exceed the unrelated OLMo (69.2\\%).\nThe choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.\n\n\\paragraph{Additional caveats.}\nDetection features degrade under domain shift \\cite{pudasaini2026_detection_fails}; our depth features are likely susceptible.\n\\citet{falahati2026_curated} show that curated synthetic data need not trigger collapse, attenuating the fingerprints we exploit.\n\n\\section*{Ethics Statement}\n\nThis work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.\nNo human subjects were involved, no private or sensitive data were collected, and no new models were released.\nOur method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.\nCode and data will be released upon acceptance.",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " All experiments use Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models).",
          " Depth signal is the dominant classification factor (5-fold CV 59--82\\%, up to 2.5$\\times$ chance): LOGO accuracy (72.1\\%) matches standard CV (72.0\\%), and seed-group prediction is at chance (10.2\\% vs.\\ 10\\%; Appendix~\\ref{app:domain_bias}).",
          " Transfer to mixed-domain corpora, instruction-tuned models, and larger scales (7B+) remains open.",
          "-Real-world documents may also interleave segments at different recursion depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.",
          "+Real-world documents may also interleave segments at different recursive generation depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.",
          " ",
          " \\paragraph{Adversarial robustness.}",
          " Adversarial paraphrasing \\cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested."
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

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_01A2x5EuEACK79qyzKS3ULo2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
  "old_string": "rather than recursion depth.",
  "new_string": "rather than generation depth."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "0742cd7c-9b6a-4288-872b-f391401c210e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

_source line 50 · 2026-05-15T22:08:33.875Z_

<details><summary>↩ Tool result · `toolu_01A2x5EuEACK79qyzKS3ULo2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "37b62add-4dd7-4397-8309-e3c4a2b63908",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
    "oldString": "rather than recursion depth.",
    "newString": "rather than generation depth.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Model Collapse Theory.}\n\\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails, collapsing the output distribution.\n\\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws distinguishing tail \\emph{narrowing} from \\emph{cutting}; \\citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \\citet{dohmatob2024_demystified} analyze the regression case.\nThe MAD framework \\cite{alemohammad2024_mad} extends this to self-consuming models and quantifies the precision--recall tradeoff.\nMitigation strategies include retaining real data \\cite{gerstgrasser2024_accumulate} and filtering via detection \\cite{drayson2025_detection_prevents_collapse}.\nRecent work identifies non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, fixed-point convergence \\cite{marchi2024_heat_death}, contamination bounds \\cite{wang2026_contamination}, curated pipelines \\cite{falahati2026_curated}, knowledge collapse \\cite{knowledge_collapse2025}, spectral signatures \\cite{sigma2026_spectral}, and self-improving loops \\cite{synthetic_eggs2026}.\nThese works characterize degradation but assume depth is known a priori; we address the inverse problem of estimating depth from text alone.\n\n\\paragraph{AI Text Detection.}\nDetectGPT \\cite{mitchell2023_detectgpt} introduced probability curvature as a zero-shot detection signal; Fast-DetectGPT \\cite{fast_detectgpt2024} improves efficiency via surrogate-model conditional curvature.\nBinoculars \\cite{binoculars2024} exploits perplexity ratios between related models, DivEye \\cite{diveye2026} leverages surprisal diversity, and GLTR \\cite{gehrmann2019_gltr} visualizes per-token likelihood ranks.\nFundamental limits exist: paraphrasing reduces detection to near chance \\cite{sadasivan2023_paraphrase}, detection degrades under distribution shift \\cite{pudasaini2026_detection_fails}, and a generator barrier bounds performance when the generator is unknown \\cite{pu2026_generator_barrier}.\nGhostbuster \\cite{verma2024_ghostbuster} trains classifiers on statistical features for binary detection, sharing our feature-engineering philosophy but not addressing depth; M4-SemEval \\cite{wang2024_m4_semeval} benchmarks multilingual detection, and DNA-GPT \\cite{yang2024_dnagpt} uses divergent $n$-gram analysis.\nWatermarking \\cite{kirchenbauer2023_watermark} embeds detectable signals but requires proactive deployment.\nAll these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.\n\n\\paragraph{Adjacent Tasks.}\nEditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains.\n\\citet{uchendu2020_attribution} classify \\emph{which} model generated text rather than recursion depth.\nLOKI \\cite{loki2025} benchmarks synthetic data detection across modalities but evaluates binary detection only.\n\\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, measuring forward degradation; our task performs the inverse, classifying depth from text alone.\n\n\\paragraph{Ordinal Classification.}\nCORAL \\cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \\cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.\nWe adopt both as baselines (\\S\\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.\n\n\\paragraph{Decoding Strategy Effects.}\nDecoding strategies shape text statistics in ways that interact with depth signals: nucleus sampling maintains diversity \\cite{holtzman2020_nucleus}, decoding parameters affect evaluation non-trivially \\cite{finlayson2024_closing}, and strategy effects are model-dependent \\cite{garces_arias2025_decoding_decoded}.\n\\citet{wiher2022_decoding} systematically compare methods on surface-level properties, and Mirostat \\cite{basu2021_mirostat} regulates output entropy via perplexity control.\nOur Depth Degradation Atlas (\\S\\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation---temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal---effects beyond single-pass text quality.",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Adjacent Tasks.}",
          " EditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains.",
          "-\\citet{uchendu2020_attribution} classify \\emph{which} model generated text rather than recursion depth.",
          "+\\citet{uchendu2020_attribution} classify \\emph{which} model generated text rather than generation depth.",
          " LOKI \\cite{loki2025} benchmarks synthetic data detection across modalities but evaluates binary detection only.",
          " \\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, measuring forward degradation; our task performs the inverse, classifying depth from text alone.",
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

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Edit · `toolu_01BzYRdHZ7H2WBxfBdSSn8iF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "old_string": "no measurable effect on depth classification after",
  "new_string": "no measurable effect on depth estimation after"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "7e5bcca7-e997-47e0-a979-ca0e5c6e1da9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

_source line 52 · 2026-05-15T22:08:34.823Z_

<details><summary>↩ Tool result · `toolu_01BzYRdHZ7H2WBxfBdSSn8iF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "ece9a100-7350-4949-8fa4-a6187ce7e0c9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "oldString": "no measurable effect on depth classification after",
    "newString": "no measurable effect on depth estimation after",
    "originalFile": "\\section{Additional Results}\n\\label{app:additional}\n\n\\subsection{Top-$k$ Feature Trajectories}\n\\label{app:topk_trajectories}\n\nFigure~\\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\\tau{=}0.9$) sampling.\nTop-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\nConcretely, the d0$\\to$d1 drop in \\textsc{p90\\_ppl} under top-$k$ is 78\\% (vs.\\ 87\\% for nucleus), and the d2$\\to$d3 reduction is 31\\% (vs.\\ 39\\% for nucleus).\nDespite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.\n\n\\subsection{Permutation Importance}\n\\label{app:permutation}\n\nTo verify that the Gini-based importance rankings in \\S\\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.\nThe top-2 features are stable across measures: \\textsc{p90\\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \\textsc{var\\_surprisal} in 8/9 (vs.\\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \\textsc{p75\\_ppl} displaces \\textsc{var\\_surprisal} to rank 3).\nKendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).\nPairwise Spearman correlations are: SHAP--Gini $\\rho{=}0.93$, SHAP--permutation $\\rho{=}0.84$, Gini--permutation $\\rho{=}0.76$.\nPer-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.\n\n\\subsection{DCOL Iteration Details}\n\\label{app:dcol_iterations}\n\nTable~\\ref{tab:dcol_iterations} summarizes all six DCOL iterations.\nDeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\\%.}\n\\label{tab:dcol_iterations}\n\\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}\n\\toprule\nVer. & Backbone & Config & Outcome \\\\\n\\midrule\nv1 & DeBERTa & FT, m\\_lr $10^{-3}$ & Embed.\\ collapse (31.5\\%) \\\\\nv2 & DeBERTa & FT, m\\_lr $10^{-4}$ & OOM \\\\\nv3 & DeBERTa & FT, m\\_lr $10^{-4}$ & Forgetting + OOM \\\\\nv4 & DeBERTa & LoRA, m\\_lr $10^{-3}$ & Embed.\\ collapse \\\\\nv5 & DeBERTa & LoRA, m\\_lr $10^{-4}$ & NaN gradients \\\\\nv6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\\% ($-$13.7pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Overlap Analysis}\n\\label{app:feature_overlap}\n\nWe probe whether end-to-end PLM representations capture the same depth signals as our statistical features.\nDeBERTa attention importance and RF permutation importance exhibit a significant negative correlation (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the statistical features capture distributional tail properties that constitute the dominant depth markers.\n\n\\subsection{Domain Bias Analysis}\n\\label{app:domain_bias}\n\nTo assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.\n\n\\paragraph{Methodological note.}\nAn initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\\%, seed-group prediction 20.8\\%).\nWe discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.\nThe results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.\n\n\\paragraph{Sub-A: Standard CV.}\nFive-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\\% to 82\\% across the 9 atlas cells (up to 2.5$\\times$ above the 33.3\\% chance level), confirming that depth signal is the dominant classification factor.\n\n\\paragraph{Sub-B: LOGO evaluation.}\nWe assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.\nLOGO mean accuracy is 72.1\\% (range 59.5--81.6\\%), matching standard CV (72.0\\%) within noise (before fix: 64.0\\%, reflecting the depth--group confound).\nPer-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.\n\n\\paragraph{Sub-C: Negative control.}\nWe train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\\%).\nDepth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%---indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).\nThe depth-to-seed-group accuracy ratio is 7.1$\\times$, confirming that the feature representation encodes depth but not seed-article identity.\n\nTaken together, these results show that seed-article grouping has no measurable effect on depth classification after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\n\n\\subsection{Wild-Data Calibration}\n\\label{app:calibration}\n\nTable~\\ref{tab:calibration} reports the prediction distribution of the Pythia-1.4B nucleus RF when applied to WikiText-103 test passages (out-of-distribution human text) and to controlled benchmark data.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{WikiText-103 prediction distribution (Pythia-1.4B nucleus RF). All 546 passages are human-written (true d0); mean d0 posterior probability: 0.996.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nSource & $n$ & d0\\% & d1\\% & d2\\% & d3\\% \\\\\n\\midrule\nWikiText-103 & 546 & \\textbf{100.0} & 0.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Depth-graduated curation.}\nCurrent data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.\nRecursive depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest such depth-graduated filtering is feasible across the model--strategy configurations we study, though its downstream effect on training quality remains to be validated empirically.\nImportance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nDepth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining these three signals---watermark presence, source model, and recursion depth---could support more nuanced data auditing than any single method.\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 7,
        "newStart": 74,
        "newLines": 7,
        "lines": [
          " Depth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%---indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).",
          " The depth-to-seed-group accuracy ratio is 7.1$\\times$, confirming that the feature representation encodes depth but not seed-article identity.",
          " ",
          "-Taken together, these results show that seed-article grouping has no measurable effect on depth classification after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.",
          "+Taken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.",
          " ",
          " \\subsection{Wild-Data Calibration}",
          " \\label{app:calibration}"
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

_source line 53_

<details open><summary>🔧 Tool call — Edit · `toolu_019YFU9HnrsVpGgnjUPwasnj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "old_string": "Recursive depth estimation enables",
  "new_string": "Recursive generation depth estimation enables"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "3175c8a5-ce42-4272-877f-2db52a85a0e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

_source line 54 · 2026-05-15T22:08:35.764Z_

<details><summary>↩ Tool result · `toolu_019YFU9HnrsVpGgnjUPwasnj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "bb970dc3-789c-40d2-9429-7968475d10bd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "oldString": "Recursive depth estimation enables",
    "newString": "Recursive generation depth estimation enables",
    "originalFile": "\\section{Additional Results}\n\\label{app:additional}\n\n\\subsection{Top-$k$ Feature Trajectories}\n\\label{app:topk_trajectories}\n\nFigure~\\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\\tau{=}0.9$) sampling.\nTop-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\nConcretely, the d0$\\to$d1 drop in \\textsc{p90\\_ppl} under top-$k$ is 78\\% (vs.\\ 87\\% for nucleus), and the d2$\\to$d3 reduction is 31\\% (vs.\\ 39\\% for nucleus).\nDespite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.\n\n\\subsection{Permutation Importance}\n\\label{app:permutation}\n\nTo verify that the Gini-based importance rankings in \\S\\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.\nThe top-2 features are stable across measures: \\textsc{p90\\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \\textsc{var\\_surprisal} in 8/9 (vs.\\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \\textsc{p75\\_ppl} displaces \\textsc{var\\_surprisal} to rank 3).\nKendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).\nPairwise Spearman correlations are: SHAP--Gini $\\rho{=}0.93$, SHAP--permutation $\\rho{=}0.84$, Gini--permutation $\\rho{=}0.76$.\nPer-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.\n\n\\subsection{DCOL Iteration Details}\n\\label{app:dcol_iterations}\n\nTable~\\ref{tab:dcol_iterations} summarizes all six DCOL iterations.\nDeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\\%.}\n\\label{tab:dcol_iterations}\n\\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}\n\\toprule\nVer. & Backbone & Config & Outcome \\\\\n\\midrule\nv1 & DeBERTa & FT, m\\_lr $10^{-3}$ & Embed.\\ collapse (31.5\\%) \\\\\nv2 & DeBERTa & FT, m\\_lr $10^{-4}$ & OOM \\\\\nv3 & DeBERTa & FT, m\\_lr $10^{-4}$ & Forgetting + OOM \\\\\nv4 & DeBERTa & LoRA, m\\_lr $10^{-3}$ & Embed.\\ collapse \\\\\nv5 & DeBERTa & LoRA, m\\_lr $10^{-4}$ & NaN gradients \\\\\nv6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\\% ($-$13.7pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Overlap Analysis}\n\\label{app:feature_overlap}\n\nWe probe whether end-to-end PLM representations capture the same depth signals as our statistical features.\nDeBERTa attention importance and RF permutation importance exhibit a significant negative correlation (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the statistical features capture distributional tail properties that constitute the dominant depth markers.\n\n\\subsection{Domain Bias Analysis}\n\\label{app:domain_bias}\n\nTo assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.\n\n\\paragraph{Methodological note.}\nAn initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\\%, seed-group prediction 20.8\\%).\nWe discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.\nThe results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.\n\n\\paragraph{Sub-A: Standard CV.}\nFive-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\\% to 82\\% across the 9 atlas cells (up to 2.5$\\times$ above the 33.3\\% chance level), confirming that depth signal is the dominant classification factor.\n\n\\paragraph{Sub-B: LOGO evaluation.}\nWe assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.\nLOGO mean accuracy is 72.1\\% (range 59.5--81.6\\%), matching standard CV (72.0\\%) within noise (before fix: 64.0\\%, reflecting the depth--group confound).\nPer-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.\n\n\\paragraph{Sub-C: Negative control.}\nWe train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\\%).\nDepth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%---indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).\nThe depth-to-seed-group accuracy ratio is 7.1$\\times$, confirming that the feature representation encodes depth but not seed-article identity.\n\nTaken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\n\n\\subsection{Wild-Data Calibration}\n\\label{app:calibration}\n\nTable~\\ref{tab:calibration} reports the prediction distribution of the Pythia-1.4B nucleus RF when applied to WikiText-103 test passages (out-of-distribution human text) and to controlled benchmark data.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{WikiText-103 prediction distribution (Pythia-1.4B nucleus RF). All 546 passages are human-written (true d0); mean d0 posterior probability: 0.996.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nSource & $n$ & d0\\% & d1\\% & d2\\% & d3\\% \\\\\n\\midrule\nWikiText-103 & 546 & \\textbf{100.0} & 0.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Depth-graduated curation.}\nCurrent data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.\nRecursive depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest such depth-graduated filtering is feasible across the model--strategy configurations we study, though its downstream effect on training quality remains to be validated empirically.\nImportance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nDepth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining these three signals---watermark presence, source model, and recursion depth---could support more nuanced data auditing than any single method.\n",
    "structuredPatch": [
      {
        "oldStart": 100,
        "oldLines": 7,
        "newStart": 100,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Depth-graduated curation.}",
          " Current data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.",
          "-Recursive depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.",
          "+Recursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.",
          " The 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest such depth-graduated filtering is feasible across the model--strategy configurations we study, though its downstream effect on training quality remains to be validated empirically.",
          " Importance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.",
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

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Edit · `toolu_01Npv1pa4tkFSExJmEKUSqWi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
  "old_string": "source model, and recursion depth",
  "new_string": "source model, and recursive generation depth"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "9a72b2ad-a0df-42c9-a46a-a22ff81a9a63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183ctx9oa8cMtATCnS8GRG5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 53689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3367
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

_source line 56 · 2026-05-15T22:08:36.665Z_

<details><summary>↩ Tool result · `toolu_01Npv1pa4tkFSExJmEKUSqWi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "efbc4be5-e98e-4d9b-b561-527fa0e18cef",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex",
    "oldString": "source model, and recursion depth",
    "newString": "source model, and recursive generation depth",
    "originalFile": "\\section{Additional Results}\n\\label{app:additional}\n\n\\subsection{Top-$k$ Feature Trajectories}\n\\label{app:topk_trajectories}\n\nFigure~\\ref{fig:feature_trajectory} in the main text shows feature trajectories for nucleus ($p{=}0.95$) and temperature ($\\tau{=}0.9$) sampling.\nTop-$k$ ($k{=}50$) trajectories follow the same monotonically decreasing trend for all features but with compressed inter-depth spacing, consistent with the signal attenuation effect discussed in \\S\\ref{sec:atlas:strategy}.\nConcretely, the d0$\\to$d1 drop in \\textsc{p90\\_ppl} under top-$k$ is 78\\% (vs.\\ 87\\% for nucleus), and the d2$\\to$d3 reduction is 31\\% (vs.\\ 39\\% for nucleus).\nDespite the magnitude reduction, feature rank ordering across depths is preserved, which explains why ordinal classifiers maintain directionality even under top-$k$ conditions.\n\n\\subsection{Permutation Importance}\n\\label{app:permutation}\n\nTo verify that the Gini-based importance rankings in \\S\\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.\nThe top-2 features are stable across measures: \\textsc{p90\\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \\textsc{var\\_surprisal} in 8/9 (vs.\\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \\textsc{p75\\_ppl} displaces \\textsc{var\\_surprisal} to rank 3).\nKendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).\nPairwise Spearman correlations are: SHAP--Gini $\\rho{=}0.93$, SHAP--permutation $\\rho{=}0.84$, Gini--permutation $\\rho{=}0.76$.\nPer-cell top-5 overlap between SHAP and permutation importance is 3--4 out of 5 features; the aggregated (mean-across-cells) top-5 sets are identical, confirming that the top features are robust to the choice of importance measure at the aggregate level while per-cell rankings exhibit model-dependent variation.\n\n\\subsection{DCOL Iteration Details}\n\\label{app:dcol_iterations}\n\nTable~\\ref{tab:dcol_iterations} summarizes all six DCOL iterations.\nDeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\\%.}\n\\label{tab:dcol_iterations}\n\\begin{tabular}{@{}llp{2.2cm}p{2.8cm}@{}}\n\\toprule\nVer. & Backbone & Config & Outcome \\\\\n\\midrule\nv1 & DeBERTa & FT, m\\_lr $10^{-3}$ & Embed.\\ collapse (31.5\\%) \\\\\nv2 & DeBERTa & FT, m\\_lr $10^{-4}$ & OOM \\\\\nv3 & DeBERTa & FT, m\\_lr $10^{-4}$ & Forgetting + OOM \\\\\nv4 & DeBERTa & LoRA, m\\_lr $10^{-3}$ & Embed.\\ collapse \\\\\nv5 & DeBERTa & LoRA, m\\_lr $10^{-4}$ & NaN gradients \\\\\nv6 & RoBERTa & FT, grad clip 1.0 & Stable; 64.5\\% ($-$13.7pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Feature Overlap Analysis}\n\\label{app:feature_overlap}\n\nWe probe whether end-to-end PLM representations capture the same depth signals as our statistical features.\nDeBERTa attention importance and RF permutation importance exhibit a significant negative correlation (Spearman $\\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\\,{=}\\,0$).\nPLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\\textsc{var\\_surprisal} and \\textsc{p90\\_ppl} yield negative $R^2$ under linear probing.\nThis confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\\S\\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the statistical features capture distributional tail properties that constitute the dominant depth markers.\n\n\\subsection{Domain Bias Analysis}\n\\label{app:domain_bias}\n\nTo assess whether the classifier exploits depth-related features or memorizes stylistic cues from individual seed articles, we conduct three sub-experiments.\n\n\\paragraph{Methodological note.}\nAn initial implementation assigned sample IDs with a global counter across depths, inadvertently correlating seed-group identity with depth (LOGO accuracy 64.0\\%, seed-group prediction 20.8\\%).\nWe discovered the issue during internal review, corrected to per-depth seed assignment ensuring each group contains equal samples per depth, and re-ran all sub-experiments.\nThe results below use the corrected pipeline; the initial (buggy) numbers are reported for transparency.\n\n\\paragraph{Sub-A: Standard CV.}\nFive-fold CV accuracy on 3-class (d1/d2/d3) classification ranges from 59\\% to 82\\% across the 9 atlas cells (up to 2.5$\\times$ above the 33.3\\% chance level), confirming that depth signal is the dominant classification factor.\n\n\\paragraph{Sub-B: LOGO evaluation.}\nWe assign each passage to one of 10 seed-article groups (balanced: each group contains equal samples per depth) and perform leave-one-group-out CV.\nLOGO mean accuracy is 72.1\\% (range 59.5--81.6\\%), matching standard CV (72.0\\%) within noise (before fix: 64.0\\%, reflecting the depth--group confound).\nPer-cell fold standard deviations range from 0.4pp to 1.4pp, indicating that cross-group generalization is as reliable as within-group classification.\n\n\\paragraph{Sub-C: Negative control.}\nWe train two classifiers on identical features: one predicting depth, the other predicting seed-group identity (10-class, chance = 10\\%).\nDepth prediction accuracy averages 72.0\\%; seed-group prediction averages 10.2\\%---indistinguishable from chance (before fix: 20.8\\%, inflated by the depth--group confound).\nThe depth-to-seed-group accuracy ratio is 7.1$\\times$, confirming that the feature representation encodes depth but not seed-article identity.\n\nTaken together, these results show that seed-article grouping has no measurable effect on depth estimation after correcting the group assignment: LOGO accuracy equals standard CV, and seed-group prediction is at chance.\n\n\\subsection{Wild-Data Calibration}\n\\label{app:calibration}\n\nTable~\\ref{tab:calibration} reports the prediction distribution of the Pythia-1.4B nucleus RF when applied to WikiText-103 test passages (out-of-distribution human text) and to controlled benchmark data.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{WikiText-103 prediction distribution (Pythia-1.4B nucleus RF). All 546 passages are human-written (true d0); mean d0 posterior probability: 0.996.}\n\\label{tab:calibration}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nSource & $n$ & d0\\% & d1\\% & d2\\% & d3\\% \\\\\n\\midrule\nWikiText-103 & 546 & \\textbf{100.0} & 0.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Depth-graduated curation.}\nCurrent data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.\nRecursive generation depth estimation enables a finer-grained alternative: retain low-depth generations (d1) whose distributional properties remain close to the human source, while down-weighting or filtering high-depth text (d3+) where tail erosion has degraded quality.\nThe 70--85\\% in-distribution accuracy and $\\mathrm{EDD}_{0.75}{=}4$ suggest such depth-graduated filtering is feasible across the model--strategy configurations we study, though its downstream effect on training quality remains to be validated empirically.\nImportance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.\n\n\\paragraph{Toward a provenance toolkit.}\nDepth estimation complements existing provenance methods along orthogonal axes.\nWatermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\nSource attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\nDepth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.\nA layered provenance system combining these three signals---watermark presence, source model, and recursion depth---could support more nuanced data auditing than any single method.\n",
    "structuredPatch": [
      {
        "oldStart": 109,
        "oldLines": 4,
        "newStart": 109,
        "newLines": 4,
        "lines": [
          " Watermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.",
          " Source attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.",
          " Depth estimation characterizes \\emph{iterative reuse} regardless of generator cooperation or identity.",
          "-A layered provenance system combining these three signals---watermark presence, source model, and recursion depth---could support more nuanced data auditing than any single method.",
          "+A layered provenance system combining these three signals---watermark presence, source model, and recursive generation depth---could support more nuanced data auditing than any single method."
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

_source line 57_

全部修改完成。汇总如下：

---

### 修改 1: W3 — LoRA 定义恢复
| 文件 | 行 | 修改 |
|---|---|---|
| `method.tex` | 33 | `LoRA finetuning \cite{hu2022lora}` → `Low-Rank Adaptation (LoRA; \cite{hu2022lora}), which freezes base model weights and trains low-rank update matrices ($<$1\% additional parameters),` |

### 修改 2: R2-W2 — 术语一致性（6 处）
| 文件 | 行 | 原文 → 修正 |
|---|---|---|
| `atlas.tex` | 46 | "recursive depth" → "generation depth" |
| `conclusion.tex` | 16 | "recursion depths" → "recursive generation depths" |
| `related_work.tex` | 22 | "recursion depth" → "generation depth" |
| `section_appendix.tex` | 77 | "depth classification" → "depth estimation" |
| `section_appendix.tex` | 103 | "Recursive depth estimation" → "Recursive generation depth estimation" |
| `section_appendix.tex` | 112 | "recursion depth" → "recursive generation depth" |

"model collapse" 首次出现在 `introduction.tex:11` 已带引用 `\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}`，前文（line 6）已解释其含义（distributional collapse），无需改动。"feature-based" 全文一致，未发现 "feature-engineered"。

### 修改 3: R2-W4 — Limitations 位置
**无需改动。** `main.tex` 中 `\input{conclusion}`（含 `\section*{Limitations}` + `\section*{Ethics Statement}`）在 `\input{discussion}`（含 `\section{Discussion and Conclusion}`）之后、`\bibliography{references}` 之前，符合 EMNLP 要求。

### 修改 4: R2-W6 — Orphan bib 清理
**无 orphan 条目。** 全部 43 个 bib entry 均在至少一个 .tex 文件中被 `\cite` 引用（含 `discussion.tex`, `conclusion.tex`, `section_appendix.tex`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "uuid": "1ffc1776-1eb8-49ad-ac57-b1320a46c891",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dMYbheZRbG2r61PKF27P9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4198,
      "cache_read_input_tokens": 57056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4198
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

_source line 58_

全部修改完成。汇总如下：

---

### 修改 1: W3 — LoRA 定义恢复
| 文件 | 行 | 修改 |
|---|---|---|
| `method.tex` | 33 | `LoRA finetuning \cite{hu2022lora}` → `Low-Rank Adaptation (LoRA; \cite{hu2022lora}), which freezes base model weights and trains low-rank update matrices ($<$1\% additional parameters),` |

### 修改 2: R2-W2 — 术语一致性（6 处）
| 文件 | 行 | 原文 → 修正 |
|---|---|---|
| `atlas.tex` | 46 | "recursive depth" → "generation depth" |
| `conclusion.tex` | 16 | "recursion depths" → "recursive generation depths" |
| `related_work.tex` | 22 | "recursion depth" → "generation depth" |
| `section_appendix.tex` | 77 | "depth classification" → "depth estimation" |
| `section_appendix.tex` | 103 | "Recursive depth estimation" → "Recursive generation depth estimation" |
| `section_appendix.tex` | 112 | "recursion depth" → "recursive generation depth" |

"model collapse" 首次出现在 `introduction.tex:11` 已带引用 `\cite{shumailov2024_nature,dohmatob2024_tale_of_tails}`，前文（line 6）已解释其含义（distributional collapse），无需改动。"feature-based" 全文一致，未发现 "feature-engineered"。

### 修改 3: R2-W4 — Limitations 位置
**无需改动。** `main.tex` 中 `\input{conclusion}`（含 `\section*{Limitations}` + `\section*{Ethics Statement}`）在 `\input{discussion}`（含 `\section{Discussion and Conclusion}`）之后、`\bibliography{references}` 之前，符合 EMNLP 要求。

### 修改 4: R2-W6 — Orphan bib 清理
**无 orphan 条目。** 全部 43 个 bib entry 均在至少一个 .tex 文件中被 `\cite` 引用（含 `discussion.tex`, `conclusion.tex`, `section_appendix.tex`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 107779,
  "duration_api_ms": 108609,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "82dddda2-acaa-4ff4-8ed4-65f99648a31a",
  "total_cost_usd": 0.59918725,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 49413,
    "cache_read_input_tokens": 256292,
    "output_tokens": 6414,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49413,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 642,
        "cache_read_input_tokens": 57056,
        "cache_creation_input_tokens": 4198,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4198
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1715,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001815,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 6414,
      "cacheReadInputTokens": 256292,
      "cacheCreationInputTokens": 49413,
      "webSearchRequests": 0,
      "costUSD": 0.59737225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e10d1a74-55af-4c31-8bfd-0be8824a7387"
}
```

</details>

---
