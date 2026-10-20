# Research conversation: Read all the following tex files from the paper and return their FULL content verbatim. Do not summarize - I need the co

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aef8cf76137435b1d.jsonl`
- **Structured JSON:** [`c5e765b062659067cacd.json`](../../sessions/c5/c5e765b062659067cacd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-17T18:08:08.580Z_

Read all the following tex files from the paper and return their FULL content verbatim. Do not summarize - I need the complete text.

Files to read (use the Read tool for each):
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex
8. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex
9. /home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex

Return the complete content of each file, clearly labeled with the filename. This is for a paper review - I need every word.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "78db90e5-b7eb-41b5-9014-1b953f73a6bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T18:08:08.582Z_

```json
{
  "parentUuid": "78db90e5-b7eb-41b5-9014-1b953f73a6bf",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
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
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "aa678762-8d14-4893-8692-c37103d236dd",
  "timestamp": "2026-05-17T18:08:08.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-17T18:08:10.592Z_



I'll read all the files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa678762-8d14-4893-8692-c37103d236dd",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "676b3f19-b340-45a5-9431-1b0cfcf935f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 4 · 2026-05-17T18:08:11.098Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y9a5bxBUVFdTq3rD8Ldw16`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "676b3f19-b340-45a5-9431-1b0cfcf935f4",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f130d92-660a-41a3-b858-1f99acb37a6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 5 · 2026-05-17T18:08:11.117Z_

<details><summary>↩ Tool result · `toolu_01Y9a5bxBUVFdTq3rD8Ldw16`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	% \usepackage{acl}  % uncomment for camera-ready (remove [review])
4	\usepackage{times,latexsym}
5	\usepackage{amsmath,amssymb}
6	\usepackage{graphicx}
7	\graphicspath{{../../figures/paper/}}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Exception Events Are All You Need: \\Component Ablation for Trace-Based Verdict Prediction}
13	\author{Anonymous ACL submission}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	Execution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.
20	We present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models spanning three architecture families and 1.5B to 13B parameters.
21	Exception events alone achieve ${\geq}$99.33\% accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while a code-only baseline shows 9.19pp scale sensitivity (67.3--76.5\%).
22	Adding more trace information actively hurts: a multi-component representation underperforms exception-only, and the full-trace gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%).
23	Tail-truncation experiments reveal that diagnostic signal concentrates near the trace terminus (in a localized window, not the absolute end), recovering 86\% of the gap to exception-only.
24	A format-marker ablation confirms ${\sim}$91\% of the exception signal is semantic (learned by SFT to distinguish caught from uncaught exceptions) rather than format-driven.
25	These results reveal a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99\%, while Tier~2 (loop compression) reaches 85.6\%.
26	Cross-dataset evaluation on DebugBench ($N{=}426$) confirms generalization, with exception-only achieving 100\%.
27	We reframe verdict prediction as fault detection: the minimal sufficient signal is a compact exception event (median 150 tokens) that is scale-invariant, architecture-independent, and deployable in token-constrained settings.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{method}
32	\input{experiments}
33	\input{discussion}
34	\input{related_work}
35	\input{conclusion}
36	
37	\section*{Limitations}
38	
39	Our study has several limitations.
40	First, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\S\ref{sec:debugbench}) confirms that exception dominance generalizes to synthetically injected bugs, generalization to other languages, larger codebases, or real-world fault distributions remains untested.
41	Second, while we evaluate four models spanning 1.5B to 13B parameters across three architecture families, all are code-specialized; generalization to general-purpose models or larger scales remains untested.
42	Third, DeepSeek \texttt{exception\_only} exhibits seed-dependent variance: 2/3 seeds achieve 99.33\% while seed 123 yields 91.09\% ($\sigma{=}4.76$pp, $n{=}3$), which we hypothesize reflects LoRA initialization sensitivity in DeepSeek-Coder, though direct evidence is lacking (fail recall = 70.5\% for the outlier vs.\ 100\% for others).
43	Qwen \texttt{exception\_only} shows perfect seed robustness ($\sigma{=}0$, $n{=}3$), but Qwen \texttt{ae\_only} also exhibits seed variance ($\sigma{=}$0.40pp; seed 123 = 99.08\% vs.\ seeds 42/456 = 99.92\%), though far smaller than DeepSeek's ($\sigma{=}$4.76pp).
44	Whether training stabilization techniques can eliminate DeepSeek's seed sensitivity is unexplored; other conditions use a single seed.
45	Fourth, the initial DeepSeek \texttt{full\_trace} run was invalidated by context overflow; a re-run with extended context yields 79.16\% (CI [76.80\%, 81.30\%]), 2.60pp below Qwen (Table~\ref{tab:cross_model}).
46	Fifth, the candidate solutions were generated by Qwen-2.5-Coder-7B-Instruct, which also serves as one of our evaluation models; this does not affect verdict prediction but may influence the pass/fail distribution.
47	Sixth, self-familiarity bias may inflate absolute accuracy: both Qwen-2.5-Coder and DeepSeek-Coder were likely exposed to HumanEval and MBPP solutions during pretraining, so the models may partially recognize solutions rather than purely reasoning from trace signals; our cross-dataset evaluation on DebugBench mitigates but does not eliminate this concern.
48	Seventh, the error distribution in our test set may not reflect real-world fault distributions: exceptions (especially \texttt{TypeError}, \texttt{ValueError}) dominate LLM-generated failures, but production code may exhibit a broader spectrum of silent logic errors where no exception is raised, potentially reducing the effectiveness of exception-based verdict prediction.
49	Finally, our analysis is limited to verdict prediction; whether exception dominance extends to other classification tasks or generation tasks is an open question.
50	
51	\section*{Ethics Statement}
52	
53	This work uses publicly available benchmarks (HumanEval, MBPP-sanitized, DebugBench) and does not involve human subjects, crowdsourced annotations, or personally identifiable information.
54	All models evaluated are open-source and publicly accessible.
55	Training uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU and total compute under 20 GPU-hours across all experiments, resulting in minimal environmental impact.
56	We do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.
57	
58	\bibliography{references}
59	
60	\appendix
61	\input{appendix}
62	
63	\end{document}
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f130d92-660a-41a3-b858-1f99acb37a6b",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "7f4b51c6-340f-47dd-bb9f-d5629024a60a",
  "sourceToolAssistantUUID": "2f130d92-660a-41a3-b858-1f99acb37a6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T18:08:11.573Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HDM6ZJUxoeGvaNhzhLaZ4P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f4b51c6-340f-47dd-bb9f-d5629024a60a",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cc33d1b-0d80-4ef3-a2fc-f45ce7ed5549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 7 · 2026-05-17T18:08:11.579Z_

<details><summary>↩ Tool result · `toolu_01HDM6ZJUxoeGvaNhzhLaZ4P`</summary>

```text
1	\section{Introduction}
2	
3	Execution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.
4	Yet feeding thousands of trace lines to a model can be no better than feeding none: the diagnostic signal drowns in routine execution steps.
5	\emph{Which trace components actually carry the signal that matters?}
6	
7	Prior work found no single trace representation consistently outperforms others \citep{wang2025dcsh}, but focused on generation-oriented tasks.
8	\emph{Verdict prediction}, classifying whether a test passes or fails, is fundamentally different: it is fault detection, not generation.
9	The model need not simulate execution; it need only determine whether something went wrong.
10	This distinction suggests that a small, fault-specific trace component may suffice.
11	
12	We test this hypothesis through the first systematic component ablation of trace representations for verdict prediction.
13	Using 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program}, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components across four models spanning 1.5B to 13B parameters and three architecture families: Qwen-2.5-Coder-7B/1.5B-Instruct \citep{qwen2025coder}, CodeLlama-13B-Instruct \citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \citep{deepseek2024coder}.
14	
15	\textbf{Exception events alone achieve ${\geq}$99.33\% verdict accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%).}
16	This near-perfect accuracy holds from 1.5B to 13B parameters, while the code-only baseline (\texttt{no\_trace}) varies from 67.3\% to 76.5\% with strong scale dependence.
17	The exception signal eliminates the need for model capacity to compensate for missing information.
18	
19	More surprisingly, adding trace information beyond exceptions actively \emph{hurts}: VOTA (99.41\%) underperforms \texttt{exception\_only} (99.83\%), and the degradation reaches 14.96pp on DeepSeek, compounded by tokenizer-driven truncation.
20	We approximately decompose this gap: ${\sim}$74\% stems from information overload (irrelevant trace content at inference) and ${\sim}$26\% from gradient dilution (dispersed training signal).
21	Tail-truncation experiments confirm the mechanism across three models and two architecture families: retaining only the last 2,048 trace tokens captures 95--98\% of \texttt{exception\_only}'s accuracy, because diagnostic events concentrate at the trace terminus.
22	
23	Our contributions:
24	\begin{enumerate}
25	\item \textbf{Exception events are the minimal sufficient signal}: ${\geq}$99.33\% across four models and three families (1.5B--13B), with ${\sim}$91\% of the signal being semantic rather than format-driven (\S\ref{sec:cross_model}, \S\ref{sec:nomarker}). SFT closes a 6--49pp zero-shot gap across four models and three architecture families, and outperforms both few-shot prompting and the best regex heuristic (\S\ref{sec:ablation}). Cross-dataset evaluation on DebugBench ($N{=}426$) yields 100\% (\S\ref{sec:debugbench}).
26	\item \textbf{Richer traces actively hurt}: We approximately decompose why into gradient dilution (${\sim}$26\%) and information overload (${\sim}$74\%), with cross-model tail-truncation confirming positional concentration across three models (95--98\% of \texttt{exception\_only} recovered; \S\ref{sec:density}, \S\ref{sec:trace_length}).
27	\item \textbf{Two-tier diagnostic hierarchy}: Tier~1 signals (exceptions, assertions) individually achieve ${\geq}$99\%; Tier~2 (loop compression) reaches 85.6\%, still +10.5pp over no trace (\S\ref{sec:ablation}).
28	\end{enumerate}
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cc33d1b-0d80-4ef3-a2fc-f45ce7ed5549",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "6f183344-e135-4d40-bb03-6024b4cfc9ca",
  "sourceToolAssistantUUID": "6cc33d1b-0d80-4ef3-a2fc-f45ce7ed5549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T18:08:12.548Z_

<details open><summary>🔧 Tool call — Read · `toolu_01URThLs5uvY18bvwnYtcwjj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f183344-e135-4d40-bb03-6024b4cfc9ca",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df29663b-63f1-4297-8436-68e31c6e1957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 9 · 2026-05-17T18:08:12.566Z_

<details><summary>↩ Tool result · `toolu_01URThLs5uvY18bvwnYtcwjj`</summary>

```text
1	\section{Method}
2	
3	\subsection{Task Definition}
4	
5	We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
6	The model produces a single token (\texttt{pass} or \texttt{fail}), making this a binary classification task.
7	Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution.
8	
9	\subsection{Dataset}
10	\label{sec:dataset}
11	
12	We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164) and MBPP-sanitized \citep{austin2021program} (427), executed each against canonical tests with \texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\% pass, 33\% fail).
13	The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\%).
14	The \texttt{exception\_only} format collapses passing solutions into identical rows (39.45\% train, 48.99\% test duplicates); train--test input overlap is zero (Appendix~\ref{sec:dedup_stats}).
15	
16	\subsection{Trace Representations}
17	
18	We define seven conditions that vary the trace information available (Figure~\ref{fig:trace_overview}):
19	\begin{itemize}
20	\item \texttt{no\_trace}: Source code and test input only.
21	\item \texttt{full\_trace}: Complete line-by-line trace with variable states.
22	\item \texttt{VOTA}: Exception events + assertion-point comparisons + loop compression.
23	\item \texttt{exception\_only}: Only exception/error events.
24	\item \texttt{ae\_only}: Only assertion-point actual/expected pairs.
25	\item \texttt{loop\_only}: Only loop compression summaries.
26	\item \texttt{VOTA\_no\_ae}: VOTA without assertion-point information.
27	\end{itemize}
28	
29	\begin{figure*}[t]
30	\centering
31	\includegraphics[width=\textwidth]{fig1_trace_overview}
32	\caption{Overview of the verdict prediction pipeline. Source code and a test input are executed to produce a full raw trace. Four conditions vary the trace information: \texttt{no\_trace} (75.13\%), \texttt{full\_trace} (81.76\%), VOTA (99.41\%), and \texttt{exception\_only} (99.83\%). Accuracies for Qwen-2.5-7B (seed=42, $N{=}1{,}190$).}
33	\label{fig:trace_overview}
34	\end{figure*}
35	
36	\subsection{Models and Training}
37	
38	We evaluate four models spanning three architecture families: \textbf{Qwen-2.5-Coder-7B/1.5B-Instruct} \citep{qwen2025coder}, \textbf{CodeLlama-13B-Instruct} \citep{roziere2024code}, and \textbf{DeepSeek-Coder-6.7B-Instruct} \citep{deepseek2024coder}, covering a 1.5B--13B parameter range (8.7$\times$).
39	All conditions use LoRA \citep{hu2022lora} (rank=16, $\alpha$=32, dropout=0.05) on all linear layers, 3 epochs, effective batch size 32, LR $2 \times 10^{-4}$ with linear warmup/decay, max sequence length 2{,}048 tokens.
40	Sequences exceeding this limit are truncated while preserving the verdict label.
41	The primary seed is 42; seeds 123 and 456 test \texttt{exception\_only} robustness (Appendix~\ref{sec:training_details}).
42	
43	\subsection{Loss Ablation}
44	
45	To disentangle training signal from input signal quality, we introduce \texttt{full\_trace\_label\_only}: identical full-trace input but loss computed only on the verdict token (trace positions masked).
46	Improvement over standard \texttt{full\_trace} is attributable to \emph{gradient dilution}; the remaining gap to VOTA reflects \emph{information overload} at inference time.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df29663b-63f1-4297-8436-68e31c6e1957",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "fd0b5099-c341-4434-8144-cd44c14da389",
  "sourceToolAssistantUUID": "df29663b-63f1-4297-8436-68e31c6e1957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T18:08:13.001Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E2hPXJ7j8MKzfHnncxe2rj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd0b5099-c341-4434-8144-cd44c14da389",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80b21907-792f-4efb-83a1-f624ad432440",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 11 · 2026-05-17T18:08:13.008Z_

<details><summary>↩ Tool result · `toolu_01E2hPXJ7j8MKzfHnncxe2rj`</summary>

```text
1	\section{Experiments}
2	
3	We evaluate across two research questions:
4	(1)~Do Tier~1 exception signals generalize across models?
5	(2)~What is the relative contribution of each trace component?
6	All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.
7	Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.
8	
9	\subsection{Cross-Model Comparison}
10	\label{sec:cross_model}
11	
12	Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.
13	
14	\begin{table}[t]
15	\centering
16	\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\pm$std (3 seeds). $^\dag$2/3 seeds; one seed excluded due to LoRA initialization failure (91.09\%, fail recall = 70.5\%; see Appendix~\ref{sec:training_dynamics}). \texttt{ae\_only} and \texttt{loop\_only} ablations tested on Qwen-7B (3 seeds) to isolate component contributions; cross-model validation focused on the primary conditions. Full CIs in Appendix~\ref{sec:full_results}.}
17	\label{tab:cross_model}
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{lcccc}
21	\toprule
22	\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
23	\midrule
24	exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.33}$^\dag$ \\
25	ae\_only & 99.64{\scriptsize$\pm$0.49} & --- & --- & --- \\
26	VOTA & 99.41 & 99.58 & 98.57 & 84.45 \\
27	no\_trace & 75.13 & 67.31 & 76.50 & 73.36 \\
28	\midrule
29	Majority baseline & \multicolumn{4}{c}{71.51} \\
30	\bottomrule
31	\end{tabular}%
32	}
33	\end{table}
34	
35	\paragraph{Exception dominance across families.}
36	Under \texttt{exception\_only}, the Qwen and CodeLlama families achieve ${\geq}$99.83\% (mean): Qwen-7B (99.83\%$\pm$0.00, 3 seeds), Qwen-1.5B (99.83\%), and CodeLlama-13B (99.89\%$\pm$0.10, 3 seeds; seed 123 achieves 100\%).
37	DeepSeek-6.7B reaches 99.33\% on 2/3 seeds with one LoRA-sensitivity outlier at 91.09\% (seed 123; fail recall = 70.5\%); even the outlier outperforms VOTA (84.45\%) by 6.64pp.
38	Excluding the DeepSeek outlier, the cross-model range is 0.56pp (99.33--99.89\%), the tightest of any condition.
39	
40	\paragraph{Scale invariance of exception signals.}
41	Exception-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\%+ on the same representation.
42	CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), confirming that Qwen's two persistent errors (from \texttt{GeneratorExit}; Appendix~\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.
43	In contrast, \texttt{no\_trace} scales monotonically with capacity: 67.31\% (1.5B) $\to$ 75.13\% (7B) $\to$ 76.50\% (13B), a 9.19pp range that exception events completely eliminate (Figure~\ref{fig:cross_scale}).
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{fig3_cross_model_gap}
48	\caption{Verdict accuracy vs.\ model scale. \texttt{exception\_only} maintains ${\geq}$99.33\% regardless of scale (1.5B--13B), while \texttt{no\_trace} shows monotonic scale sensitivity (+9.19pp from 1.5B to 13B). The \texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\sim}$97.7--97.8\%).}
49	\label{fig:cross_scale}
50	\end{figure}
51	
52	\paragraph{VOTA cross-family variation.}
53	VOTA accuracy varies across families: 99.58\% (Qwen-1.5B) $>$ 99.41\% (Qwen-7B) $>$ 98.57\% (CodeLlama-13B; \texttt{codellama13b\_vota\_seed42}, CI [97.9, 99.2]) $\gg$ 84.45\% (DeepSeek-6.7B).
54	The CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\% of DeepSeek training samples were affected; Appendix~\ref{sec:tokenizer_analysis}).
55	In contrast, \texttt{exception\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.
56	
57	\subsection{Component Ablation}
58	\label{sec:ablation}
59	
60	We restrict \texttt{ae\_only} and \texttt{loop\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.
61	Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B (seed=42) and reveals a two-tier hierarchy.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\dag$\texttt{ae\_only}: 3-seed mean 99.64\% ($\pm$0.49; seeds 42: 99.92, 123: 99.08, 456: 99.92). \texttt{exception\_only}: 99.83\% ($\pm$0.00, 3 seeds), more stable ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).}
66	\label{tab:ablation}
67	\small
68	\resizebox{\columnwidth}{!}{%
69	\begin{tabular}{llccc}
70	\toprule
71	\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\
72	\midrule
73	ae\_only & assertion-point & 99.64$^\dag$ & [99.26, 99.87] & 1 \\
74	exception\_only & exception events & \textbf{99.83} & [99.58, 100.00] & 1 \\
75	VOTA & exc+ae+loop & 99.41 & [98.82, 99.83] & --- \\
76	VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
77	loop\_only & loop compression & 85.63 & [83.53, 87.56] & 2 \\
78	full\_trace & complete trace & 81.76 & [79.70, 83.90] & --- \\
79	no\_trace & none & 75.13 & [72.77, 77.48] & --- \\
80	\midrule
81	Regex (best) & exc.\ type regex & 93.61 & --- & --- \\
82	3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\
83	Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\
84	\bottomrule
85	\end{tabular}%
86	}
87	\end{table}
88	
89	Tier~1 signals are individually sufficient: \texttt{ae\_only} (3-seed mean 99.64\% $\pm$ 0.49) and \texttt{exception\_only} (99.83\% $\pm$ 0.00) both exceed VOTA ($p{=}0.01$), implying that combining signals introduces noise; \texttt{exception\_only} is more stable across seeds ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).
90	Removing assertion points has no effect (\texttt{VOTA\_no\_ae} = 99.41\%), confirming exception dominance.
91	Tier~2 \texttt{loop\_only} (85.63\%) improves 10.50pp over \texttt{no\_trace} ($p{<}0.0001$) but falls far short of Tier~1.
92	\paragraph{Rule-based baseline comparison.}
93	The strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\% accuracy (F1=0.876), trailing SFT \texttt{exception\_only} (99.83\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).
94	The gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\ref{sec:regex_baselines}).
95	Across trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\texttt{no\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\ref{sec:regex_baselines}).
96	
97	\paragraph{Zero-shot and few-shot LLM baselines.}
98	Zero-shot prompting spans 51.0--93.5\% across four models (CodeLlama-13B: 51.01\%, Qwen-7B: 89.08\%, DeepSeek-6.7B: 90.59\%, Qwen-1.5B: 93.45\%), a 42.44pp range that SFT compresses to 0.56pp (99.33--99.89\%).
99	Zero-shot performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms both Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%), indicating that pretraining data distribution, not capacity, determines zero-shot verdict ability.
100	CodeLlama-13B drops below the majority baseline (71.51\%), showing extreme fail bias (72.4\% of predictions are \texttt{fail}).
101	Three-shot in-context learning on Qwen-7B (90.84\%, fail recall = 80.53\%) improves only 1.76pp over zero-shot and still trails both the regex heuristic (93.61\%) and SFT by 8.99pp, confirming that a few examples cannot substitute for task-specific fine-tuning.
102	SFT normalizes this cross-architecture variance, closing a 6--49pp gap to ${\geq}$99.33\% across all models with 4,720 training samples (Appendix~\ref{sec:zeroshot_cross_model}).
103	
104	\subsection{Format Marker Ablation}
105	\label{sec:nomarker}
106	
107	The \texttt{exception\_only} format includes a \texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\% accuracy; Appendix~\ref{sec:regex_baselines}).
108	To quantify the marker's contribution, we retrain with all format markers removed (\texttt{nomarker} condition).
109	
110	Qwen-7B 3-seed mean: 97.65\% $\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\%), a drop of 2.18pp from \texttt{exception\_only} (99.83\%).
111	Qwen-1.5B: 97.82\%, drop of 2.01pp.
112	The marker contribution (${\sim}$2pp) accounts for only ${\sim}$9\% of the total exception lift over \texttt{no\_trace} (24.70pp on 7B).
113	Exception events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\sim}$2pp, regex-learnable) and semantic exception content (${\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).
114	
115	\subsection{Information Density Decomposition}
116	\label{sec:density}
117	
118	The 17.65pp gap between \texttt{full\_trace} (81.76\%) and VOTA (99.41\%) decomposes via \texttt{full\_trace\_label\_only}, which retains the full trace but masks all trace tokens from the loss.
119	
120	\begin{table}[t]
121	\centering
122	\caption{Approximate information density decomposition: gradient dilution (${\sim}$26\%) vs.\ information overload (${\sim}$74\%).}
123	\label{tab:density}
124	\small
125	\begin{tabular}{lccc}
126	\toprule
127	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs.\ full\_trace} & \textbf{Gap explained} \\
128	\midrule
129	full\_trace & 81.76 & --- & --- \\
130	label\_only & 86.22 & +4.46pp & 26\% \\
131	VOTA & 99.41 & +17.65pp & 100\% \\
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	Gradient dilution accounts for approximately 26\% of the gap (+4.46pp, $p{<}0.0001$, bootstrap 95\% CI $[{+}2.35, {+}6.55]$): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.
137	The remaining ${\sim}$74\% (+13.19pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.
138	This asymmetry implies that trace compression methods should prioritize \emph{content selection} (removing irrelevant lines) over \emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.
139	The two factors may interact, so this decomposition is approximate.
140	
141	\subsection{Additional Analyses}
142	\label{sec:additional}
143	
144	\paragraph{Trace length ablation.}
145	\label{sec:trace_length}
146	Varying the trace token budget (256--no limit) on Qwen yields accuracy in a narrow 77.2\%--81.8\% band with a non-monotonic pattern, confirming that trace content quality, not quantity, is the bottleneck (Appendix~\ref{sec:trace_length_full}).
147	Notably, 1024-token traces (77.23\%) underperform 512-token traces (80.42\%), revealing that mid-length traces are long enough to introduce execution noise yet too short to reach the diagnostic events concentrated at trace end.
148	This further supports our claim that signal density, not quantity, determines model performance.
149	
150	\paragraph{Truncation direction.}
151	Reversing the truncation direction confirms that diagnostic signal concentrates near the trace terminus: on Qwen-7B, \texttt{tail\_2048} (97.31\%) outperforms \texttt{head\_2048} (81.76\%) by 15.55pp, and \texttt{tail\_256} (77.48\%) drops to the \texttt{no\_trace} baseline, localizing the signal window to 256--512 tokens from the trace end.
152	Cross-model verification confirms the pattern across two architecture families and two scales: Qwen-1.5B \texttt{tail\_2048} = 97.90\% (CI [97.06, 98.74]), DeepSeek-6.7B = 94.96\% (CI [93.70, 96.22]), with residual gaps to \texttt{exception\_only} of only 1.93pp and 4.37pp respectively (Appendix~\ref{sec:trace_length_full}).
153	The positional concentration hypothesis holds across all tested configurations, with \texttt{tail\_2048} capturing 95--98\% of \texttt{exception\_only}'s accuracy.
154	The residual gap confirms that semantic extraction (identifying exception type and message by content) still outperforms positional extraction (retaining a fixed window that includes non-diagnostic lines).
155	
156	\paragraph{Calibration.}
157	\label{sec:calibration}
158	Calibration mirrors the tier hierarchy: \texttt{exception\_only} ECE = 0.0027 vs.\ \texttt{no\_trace} ECE = 0.171, a 63$\times$ gap (Appendix~\ref{sec:calibration_full}).
159	
160	\paragraph{Error orthogonality.}
161	\texttt{exception\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\ref{sec:error_overlap}).
162	
163	\paragraph{Exception type breakdown.}
164	A per-exception-type breakdown (Appendix~\ref{sec:exception_type}) confirms that all standard exception types achieve 100\% accuracy; the only failures arise from \texttt{GeneratorExit}, a benign \texttt{BaseException} subclass.
165	
166	\paragraph{Cross-dataset generalization.}
167	\label{sec:debugbench}
168	On DebugBench \citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \texttt{exception\_only} 100\%, VOTA 99.77\%, \texttt{no\_trace} 96.71\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\ref{sec:debugbench_full}).
169	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80b21907-792f-4efb-83a1-f624ad432440",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "bb06159f-cf04-4d01-9419-9b7fe7cb2c5f",
  "sourceToolAssistantUUID": "80b21907-792f-4efb-83a1-f624ad432440",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T18:08:13.457Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XiC2XsVvsLYVwPjU8SzbJt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb06159f-cf04-4d01-9419-9b7fe7cb2c5f",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0fa453a-44b6-4641-b160-c11bc18005c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 13 · 2026-05-17T18:08:13.464Z_

<details><summary>↩ Tool result · `toolu_01XiC2XsVvsLYVwPjU8SzbJt`</summary>

```text
1	\section{Discussion}
2	
3	Verdict prediction is fundamentally fault detection: the model must determine whether execution deviated from expected behavior.
4	Exception events succeed because they are the runtime's primary fault indicator.
5	When Python raises an unhandled exception, it records exactly what went wrong (the error type), where it happened (the stack frame), and why (the error message).
6	This is precisely the information needed for a pass/fail decision, packaged in a compact, self-contained format.
7	Non-exception trace components (variable states, loop iterations, line-by-line control flow) record \emph{how} the program ran, not \emph{whether} it failed, and dilute the model's attention without providing complementary diagnostic information.
8	
9	This mechanistic account explains three key results.
10	First, adding trace information beyond exceptions actively \emph{hurts} (VOTA $<$ \texttt{exception\_only}, Table~\ref{tab:ablation}), because non-diagnostic content competes for attention.
11	Second, tail-truncation captures 95--98\% of \texttt{exception\_only}'s accuracy across three models and two architecture families (\S\ref{sec:trace_length}), because exceptions are recorded near the trace terminus where Python's error propagation concentrates them (though not at the absolute end: \texttt{tail\_256} ${\approx}$ \texttt{no\_trace}, with the signal localized in a 256--512 token window from the end).
12	Third, the 6.22pp SFT advantage over the best regex baseline concentrates on caught-exception boundary cases (Appendix~\ref{sec:regex_baselines}), confirming the model learns to distinguish \emph{whether an exception terminated execution} rather than merely detecting exception presence.
13	The 0.56pp cross-model exception gap (Appendix~\ref{sec:robustness_analysis}) and the format-collapse nature of the DeepSeek outlier (Appendix~\ref{sec:training_dynamics}) further support that the signal, not the model, is the binding constraint.
14	
15	\paragraph{Why exception\_only outperforms ae\_only.}
16	Although \texttt{ae\_only} achieves 99.92\% on seed 42, it is a strict superset of the exception signal: assertion-point comparisons include the exception event (when present) plus additional information such as fallback local variable states.
17	Multi-seed evaluation reveals that this extra content introduces noise: \texttt{ae\_only} achieves 99.64\% mean accuracy ($\pm$0.49, seeds 42/123/456) while \texttt{exception\_only} achieves 99.83\% ($\pm$0.00).
18	The zero-variance result for \texttt{exception\_only} indicates that it captures a minimal sufficient signal (the compact exception event), while \texttt{ae\_only}'s additional components (fallback locals, assertion formatting) occasionally mislead the model, manifesting as seed-dependent variance ($\sigma{=}$0.49pp).
19	Attention analysis on representative samples confirms this interpretation: within exception events, the error type and location markers receive 5--10$\times$ higher per-token attention than the verbose locals context (module paths, imported objects), suggesting the model learns to focus on diagnostic signals rather than incidental runtime state.
20	Thus \texttt{exception\_only} is both more precise and more stable than its superset.
21	
22	\paragraph{SFT vs.\ regex incremental analysis.}
23	The gap between B5 (format marker, 99.33\%) and SFT \texttt{exception\_only} (99.83\%) isolates the value of learned semantic understanding (McNemar $p{=}0.041$, Table~\ref{tab:regex}).
24	Among 8 test samples where pass-labeled code triggers exceptions (from 2 distinct problems), the SFT model correctly classifies 6 (all from MBPP/113, a try/except ValueError pattern) while B5 misclassifies all 8. The 2 remaining errors (HumanEval/95, GeneratorExit) are misclassified by most training configurations (see Appendix~\ref{sec:irreducible}). At the problem level, SFT handles 1/2 exception-type edge cases vs B5's 0/2.
25	This confirms that SFT learns a genuine semantic boundary (distinguishing caught from uncaught exceptions) rather than merely detecting exception presence or format markers.
26	
27	\paragraph{Why zero-shot and few-shot prompting fall short.}
28	Zero-shot prompting spans 51.0--93.5\% across four models, with cross-architecture variance (42.44pp) dwarfing the SFT range (0.56pp).
29	The failure is not in exception detection but in verdict calibration: the model recognizes that an exception occurred but cannot reliably determine whether it terminated execution or was caught by a \texttt{try/except} block.
30	Performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%, extreme fail bias with 72.4\% of predictions as \texttt{fail}).
31	Within the Qwen family, the 1.5B model's higher zero-shot accuracy likely reflects consistent code training data quality across scales: the smaller model already understands exception format, but both lack the verdict-specific calibration that SFT provides (SFT gap: 6.38pp for 1.5B vs.\ 10.75pp for 7B).
32	Three-shot in-context learning (90.84\% on Qwen-7B, fail recall = 80.53\%) improves fail recall by 13.57pp over zero-shot but still trails SFT by 8.99pp: three examples cannot cover the diversity of caught-exception patterns in the training distribution.
33	SFT normalizes this cross-architecture variance by grounding exception patterns in task-specific verdict labels, compressing a 42.44pp zero-shot range to 0.56pp.
34	
35	\paragraph{Format marker sensitivity.}
36	The B5 baseline (Appendix~\ref{sec:regex_baselines}) achieves 99.33\% by exploiting a deterministic format marker (\texttt{[No exception data in trace]}) present in all pass samples.
37	This near-ceiling performance from a trivial pattern raises a concern: does SFT also learn this shortcut?
38	The answer is partially yes: the format marker correlates perfectly with the pass class. But the SFT model additionally handles the 8 boundary samples where exceptions occur in passing code, achieving 6/8 correct vs.\ B5's 0/8.
39	A \emph{nomarker} ablation (\S\ref{sec:nomarker}) confirms genuine exception semantics: Qwen-7B 3-seed mean 97.65\%$\pm$0.96 and Qwen-1.5B 97.82\%, a drop of only ${\sim}$2pp.
40	The marker contribution (${\sim}$9\% of total lift) is small relative to semantic content (${\sim}$91\%), confirming that SFT learns exception semantics rather than format shortcuts.
41	Both signal layers show comparable accuracy across the two tested scales (1.5B and 7B produce 97.8\% and 97.7\% nomarker accuracy, respectively).
42	
43	\paragraph{Near-perfect floor, not hard ceiling.}
44	Samples 901 and 905 (HumanEval/95, \texttt{check\_dict\_case}) are misclassified by most configurations: Qwen-7B (3 seeds), Qwen-1.5B, and CodeLlama-13B seed 42/456 all produce exactly these 2 errors.
45	The root cause is deterministic: Python's \texttt{all()} raises \texttt{GeneratorExit} (a \texttt{BaseException} subclass) during generator short-circuit, recorded as \texttt{[ERROR]} despite the test passing.
46	However, CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), correctly classifying both samples.
47	This confirms that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most initializations) rather than a hard data limitation: the representation supports perfect accuracy, though most LoRA initializations converge to the same 2-error basin.
48	On this task, exception-only accuracy is \emph{signal-limited} rather than \emph{capacity-limited}: three architecture families spanning 1.5B to 13B converge on the same floor, while \texttt{no\_trace} shows monotonic scale dependence (67.3\% $\to$ 75.1\% $\to$ 76.5\%).
49	
50	\paragraph{Tier hierarchy: practical implications.}
51	The two-tier structure (Tier~1 ${\geq}$99\%; Tier~2 = 85.6\%) has direct engineering implications for trace-augmented systems.
52	First, it implies a \emph{diminishing returns} principle: once a Tier~1 signal is available, adding more trace information provides no benefit and may actively degrade performance through attention dilution.
53	Second, the hierarchy suggests a fallback design: systems should attempt Tier~1 extraction (exception events) and only resort to Tier~2 signals (loop compression) when no exception is raised. Even Tier~2 alone substantially outperforms no-trace baselines (+10.50pp).
54	Third, the minimal token footprint of Tier~1 signals (median 150 tokens vs.\ ${\sim}$1{,}900 for VOTA post-truncation) makes them viable for deployment in token-constrained settings (e.g., real-time CI pipelines, mobile inference).
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0fa453a-44b6-4641-b160-c11bc18005c4",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "4aef5a8c-6d35-408b-9a80-d0647145d845",
  "sourceToolAssistantUUID": "a0fa453a-44b6-4641-b160-c11bc18005c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T18:08:13.929Z_

<details open><summary>🔧 Tool call — Read · `toolu_018D1TEpFMGwPCw4HGLS3dsu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aef5a8c-6d35-408b-9a80-d0647145d845",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09a8805b-7e2f-4039-9d46-7aae3cdbe605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 15 · 2026-05-17T18:08:13.936Z_

<details><summary>↩ Tool result · `toolu_018D1TEpFMGwPCw4HGLS3dsu`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Execution Traces for Code LLMs.}
4	TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \citet{wang2025dcsh} found trace utility to be task- and format-dependent, a finding we extend by identifying exception events as the dominant signal for verdict prediction.
5	NExT \citep{ni2024next} and ET-CoT \citep{eguchi2025etcot} leveraged trace chain-of-thought for repair and execution reasoning.
6	\citet{ferrando2025execute} found compact traces comparable to full traces, supporting our information density finding.
7	CRUXEval \citep{gu2024cruxeval} established execution reasoning benchmarks, extended to 19 languages by \citet{xu2025cruxevalx}.
8	None decompose which trace components contribute to \emph{classification} accuracy.
9	
10	\paragraph{Code Verdict and Patch Classification.}
11	TRACED \citep{ding2024traced} showed execution-aware pretraining improves vulnerability and clone detection.
12	In patch correctness, APPT \citep{appt2024} achieved 79.7\% with BERT+LSTM; LLM4PatchCorrect \citep{zhou2024llm4patch} reached 84.4\% using execution traces.
13	FuseFL \citep{widyasari2024fusefl} demonstrated that structured fault signals improve fault localization.
14	\citet{foster2025mutation} deployed LLM-based equivalence detection at Meta with 0.95 precision.
15	These approaches treat traces as monolithic inputs; none isolate individual components, compare against rule-based baselines to quantify the value of learned representations, or test cross-model generalization.
16	
17	\paragraph{Fault Localization.}
18	Spectrum-based fault localization (SBFL) ranks program elements by statistical suspiciousness computed from passing/failing test spectra.
19	Classic metrics (Ochiai \citep{abreu2007accuracy}, Tarantula \citep{jones2002visualization}, DStar \citep{wong2014dstar}) share a core insight with our work: abnormal execution events (here, coverage patterns correlated with failure) are the most informative diagnostic signal.
20	Recent LLM-based approaches extend this: AutoFL \citep{kang2024autofl} uses function-level call graphs with ChatGPT; AgentFL \citep{qin2024agentfl} introduces multi-agent localization; LLM4FL \citep{widyasari2024llm4fl} combines SBFL spectra with LLM reasoning; and \citet{mukherjee2025llmfl} demonstrate that LLMs can localize faults from test failure information alone.
21	Verdict prediction is a prerequisite to fault localization: one must first determine \emph{whether} a fault exists before localizing \emph{where} it is.
22	Our exception-based approach and SBFL share the principle that anomalous execution events carry the strongest diagnostic signal, but operate at different granularities: we classify at the test level (pass/fail) while FL localizes at the statement or method level.
23	
24	\paragraph{Trace Compression and Selection.}
25	TraceCoder \citep{huang2026tracecoder} and InspectCoder \citep{wang2025inspectcoder} use selective trace extraction for debugging; \citet{haque2025traces} found raw traces provide limited repair benefit, supporting our compression finding.
26	Our approximate information density decomposition (gradient dilution ${\sim}$26\% vs.\ information overload ${\sim}$74\%) provides the first quantitative framework for \emph{why} compression helps, complementing these methods' focus on \emph{how} to compress.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09a8805b-7e2f-4039-9d46-7aae3cdbe605",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "b44e1a1d-9832-4417-9d4e-54e066caea35",
  "sourceToolAssistantUUID": "09a8805b-7e2f-4039-9d46-7aae3cdbe605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T18:08:14.500Z_

<details open><summary>🔧 Tool call — Read · `toolu_0194tHNevCS3E3EqUdQNSwiu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b44e1a1d-9832-4417-9d4e-54e066caea35",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c457fc8-9bfa-46d8-bfe1-7a9b7844b90b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 17 · 2026-05-17T18:08:14.512Z_

<details><summary>↩ Tool result · `toolu_0194tHNevCS3E3EqUdQNSwiu`</summary>

```text
1	\section{Conclusion}
2	
3	We presented the first systematic component ablation of trace representations for verdict prediction across four models (1.5B--13B, three architecture families).
4	Exception events alone achieve ${\geq}$99.33\% across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while \texttt{no\_trace} shows 9.19pp scale sensitivity (67.3--76.5\%).
5	Adding more trace information actively hurts: the gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%), and tail-truncation confirms that diagnostic signal concentrates at the trace terminus.
6	A format-marker ablation shows ${\sim}$91\% of the exception signal is semantic rather than format-driven, and cross-dataset evaluation on DebugBench confirms generalization (\texttt{exception\_only}: 100\%, $N{=}426$).
7	
8	The broader implication is that verdict prediction is not an information-starved task that benefits from richer context.
9	It is a fault detection task where the runtime has already surfaced the critical diagnostic signal; the model's role is to interpret whether that signal indicates a terminal fault (as the SFT advantage over regex on caught-exception cases confirms).
10	This reframing suggests a design principle for trace-augmented systems: extract the highest-specificity diagnostic signal (median 150 tokens) and discard everything else.
11	Future work should test whether this principle extends to additional programming languages, larger real-world codebases, silent logic errors where no exception is raised, and tasks beyond verdict prediction.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c457fc8-9bfa-46d8-bfe1-7a9b7844b90b",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "3298e3fe-0ca0-4b56-a65b-9f61c28b917e",
  "sourceToolAssistantUUID": "0c457fc8-9bfa-46d8-bfe1-7a9b7844b90b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T18:08:14.869Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DSRN2YW7FEggGTQX9HbLv3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3298e3fe-0ca0-4b56-a65b-9f61c28b917e",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b9b68cd-3814-4bc2-b9e7-5b1706474a88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10262,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 19 · 2026-05-17T18:08:15.148Z_

<details><summary>↩ Tool result · `toolu_01DSRN2YW7FEggGTQX9HbLv3`</summary>

```text
1	\section{Per-Class Performance Breakdown}
2	\label{sec:per_class}
3	
4	Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.
5	
6	\begin{table*}[t]
7	\centering
8	\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\% fail precision but only 45.4\% fail recall, indicating systematic bias toward predicting \texttt{pass}. DeepSeek \texttt{exception\_only} seed 42 achieves 100\% fail recall, but seed 123 drops to 70.5\% (see Table~\ref{tab:full_deepseek}).}
9	\label{tab:per_class}
10	\small
11	\begin{tabular}{llccccccc}
12	\toprule
13	\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
14	\midrule
15	No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
16	Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
17	Full Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
18	VOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
19	Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
20	AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
21	Loop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
22	VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
23	\midrule
24	No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
25	Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
26	VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
27	Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
28	\bottomrule
29	\end{tabular}
30	\end{table*}
31	
32	%% ============================================================
33	\section{Training Details}
34	\label{sec:training_details}
35	
36	Table~\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.
37	All experiments use the HuggingFace TRL \texttt{SFTTrainer} with LoRA \citep{hu2022lora} applied to all linear layers.
38	
39	\begin{table}[t]
40	\centering
41	\caption{Training hyperparameters (shared across all conditions).}
42	\label{tab:hyperparams}
43	\small
44	\resizebox{\columnwidth}{!}{%
45	\begin{tabular}{ll}
46	\toprule
47	\textbf{Hyperparameter} & \textbf{Value} \\
48	\midrule
49	LoRA rank ($r$)            & 16 \\
50	LoRA alpha ($\alpha$)      & 32 \\
51	LoRA dropout               & 0.05 \\
52	LoRA target modules        & all linear layers \\
53	\midrule
54	Epochs                     & 3 \\
55	Per-device batch size       & 4 \\
56	Gradient accumulation steps & 8 \\
57	Effective batch size        & 32 \\
58	\midrule
59	Learning rate               & $2 \times 10^{-4}$ \\
60	LR scheduler                & linear decay \\
61	Warmup ratio                & 0.1 \\
62	Weight decay                & 0.01 \\
63	\midrule
64	Max sequence length         & 2048 tokens \\
65	Primary seed                & 42 \\
66	Robustness seeds            & 123, 456 \\
67	\midrule
68	Hardware                    & 1$\times$ RTX PRO 6000 Blackwell (96\,GB VRAM) \\
69	Framework                   & HuggingFace TRL SFTTrainer \\
70	\bottomrule
71	\end{tabular}%
72	}
73	\end{table}
74	
75	Table~\ref{tab:train_time} reports per-condition training wall-clock times.
76	Conditions with longer trace inputs (e.g., \texttt{full\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.
77	
78	\begin{table}[t]
79	\centering
80	\caption{Training wall-clock time per condition on a single RTX PRO 6000 Blackwell GPU. Where multiple seeds were run, individual times are listed.}
81	\label{tab:train_time}
82	\small
83	\begin{tabular}{llr}
84	\toprule
85	\textbf{Condition} & \textbf{Seed(s)} & \textbf{Time (h)} \\
86	\midrule
87	no\_trace       & 42         & ${\sim}$0.5 \\
88	full\_trace     & 42         & ${\sim}$2.2 \\
89	label\_only     & 42         & ${\sim}$2.2 \\
90	VOTA                     & 42         & ${\sim}$2.3 \\
91	exception\_only & 42         & ${\sim}$2.1 \\
92	exception\_only & 123        & ${\sim}$2.1 \\
93	exception\_only & 456        & ${\sim}$1.3 \\
94	ae\_only        & 42         & ${\sim}$1.8 \\
95	loop\_only      & 42         & ${\sim}$2.1 \\
96	VOTA\_no\_ae    & 42         & ${\sim}$1.8 \\
97	\bottomrule
98	\end{tabular}
99	\end{table}
100	
101	%% ============================================================
102	\section{VOTA Trace Examples}
103	\label{sec:vota_examples}
104	
105	We provide two representative VOTA trace examples illustrating the fail and pass cases.
106	In the fail case, the exception event provides an unambiguous fault signal.
107	In the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.
108	
109	\paragraph{Fail example.}
110	A \texttt{ZeroDivisionError} triggers an \texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \texttt{fail}.
111	
112	\begin{small}
113	\begin{verbatim}
114	## Function
115	def divide(a, b):
116	    return a / b
117	
118	## Test Input
119	divide(1, 0)
120	
121	## Expected Output
122	inf
123	
124	## VOTA Trace
125	[ERROR] ZeroDivisionError: division by zero
126	
127	## Verdict
128	fail
129	\end{verbatim}
130	\end{small}
131	
132	\paragraph{Pass example.}
133	No exception is raised, and the assertion point confirms that the actual output matches the expected value.
134	
135	\begin{small}
136	\begin{verbatim}
137	## Function
138	def add(a, b):
139	    return a + b
140	
141	## Test Input
142	add(2, 3)
143	
144	## Expected Output
145	5
146	
147	## VOTA Trace
148	[LOOP] No loops detected.
149	[ASSERT] actual=5, expected=5
150	
151	## Verdict
152	pass
153	\end{verbatim}
154	\end{small}
155	
156	These examples illustrate the core asymmetry exploited by the \texttt{exception\_only} condition: fail cases produce an explicit \texttt{[ERROR]} event, while pass cases are characterized by its absence.
157	This binary signal (presence vs.\ absence of an exception) is sufficient for near-perfect verdict prediction.
158	
159	%% ============================================================
160	\section{Full Experimental Results}
161	\label{sec:full_results}
162	
163	Tables~\ref{tab:full_qwen} and \ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.
164	
165	\begin{table}[t]
166	\centering
167	\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \texttt{exception\_only} achieves 99.83\% across all three seeds ($\sigma{=}$0). \texttt{ae\_only} achieves 99.64\% mean ($\pm$0.49; seed 123 at 99.08\% is the outlier).}
168	\label{tab:full_qwen}
169	\small
170	\resizebox{\columnwidth}{!}{%
171	\begin{tabular}{lcccc}
172	\toprule
173	\textbf{Condition} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean $\pm$ Std} \\
174	\midrule
175	exception\_only & 99.83 & 99.83 & 99.83 & 99.83 $\pm$ 0.00 \\
176	ae\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\pm$ 0.49 \\
177	VOTA                     & 99.41 & ---   & ---   & --- \\
178	VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
179	label\_only     & 86.22 & ---   & ---   & --- \\
180	loop\_only      & 85.63 & ---   & ---   & --- \\
181	full\_trace     & 81.76 & ---   & ---   & --- \\
182	no\_trace       & 75.13 & ---   & ---   & --- \\
183	\bottomrule
184	\end{tabular}%
185	}
186	\end{table}
187	
188	\begin{table}[t]
189	\centering
190	\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \texttt{exception\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\%, while seed 123 yields 91.09\% (LoRA initialization outlier, fail recall = 70.5\%).}
191	\label{tab:full_deepseek}
192	\small
193	\resizebox{\columnwidth}{!}{%
194	\begin{tabular}{llcc}
195	\toprule
196	\textbf{Condition} & \textbf{Seed} & \textbf{Accuracy} & \textbf{Notes} \\
197	\midrule
198	exception\_only & 42  & 99.33 & epoch 1: 99.83 \\
199	exception\_only & 456 & 99.33 & CI [98.82, 99.75] \\
200	exception\_only & 123 & 91.09 & fail recall = 70.5\%; CI [89.40, 92.60] \\
201	\midrule
202	VOTA                     & 42  & 84.45 & \\
203	no\_trace       & 42  & 73.36 & \\
204	full\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\
205	\bottomrule
206	\end{tabular}%
207	}
208	\end{table}
209	
210	%% ============================================================
211	\section{Tokenizer and Truncation Analysis}
212	\label{sec:tokenizer_analysis}
213	
214	The VOTA cross-model gap (14.96pp, Table~\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.
215	The DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.
216	The training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.
217	
218	A post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\%).
219	Per-class analysis (Table~\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 100\% fail recall.
220	
221	Seed robustness diverges across models: Qwen \texttt{exception\_only} produces identical 99.83\% across all three seeds ($\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\% (fail recall = 100\%), seed 123 yields 91.09\% (fail recall = 70.5\%).
222	Because \texttt{exception\_only} test inputs contain 48.99\% duplicates (607 unique of 1,190; \S\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\% (Wilson CI [98.81, 99.91]).
223	
224	%% ============================================================
225	\section{Irreducible Sample Analysis}
226	\label{sec:irreducible}
227	
228	The \texttt{exception\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\% overlap across seeds.
229	Both samples (IDs 901 and 905) share the following characteristics:
230	
231	\begin{itemize}
232	\item \textbf{Function:} \texttt{check\_dict\_case} (HumanEval/95)---a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.
233	\item \textbf{Ground-truth label:} \texttt{pass}.
234	\item \textbf{Predicted label:} \texttt{fail} (false negative).
235	\item \textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.
236	\end{itemize}
237	
238	Manual inspection reveals the root cause: \texttt{check\_dict\_case} uses \texttt{all()} over a generator expression, and Python's \texttt{all()} short-circuits on the first \texttt{True} value, raising \texttt{GeneratorExit} to terminate the generator.
239	Because \texttt{GeneratorExit} is a \texttt{BaseException} subclass, the tracer records it as seven \texttt{[ERROR] GeneratorExit} lines---even though the function executes correctly and the test passes.
240	The model observes these spurious error markers and reasonably but incorrectly predicts \texttt{fail}.
241	This is not a model failure but a representation ambiguity: the \texttt{exception\_only} format cannot distinguish genuine exceptions from benign \texttt{BaseException} subclasses triggered by Python's iterator protocol.
242	
243	Most configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\{901, 905\}$.
244	However, CodeLlama-13B seed 123 achieves 100\% accuracy (0/1190 errors), correctly classifying both samples.
245	This demonstrates that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.
246	The practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.
247	
248	%% ============================================================
249	\section{Exception Type Accuracy Breakdown}
250	\label{sec:exception_type}
251	
252	Table~\ref{tab:exception_type} reports \texttt{exception\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).
253	All standard exception types (\texttt{TypeError}, \texttt{ValueError}, \texttt{IndexError}, etc.) achieve 100\% accuracy.
254	The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}---it is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.
255	
256	\begin{table}[t]
257	\centering
258	\caption{Exception type accuracy breakdown for \texttt{exception\_only} (Qwen-7B, seed=42). All true error types achieve 100\%. The only failures come from \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not an \texttt{Exception}), which appears in 2 passing samples.}
259	\label{tab:exception_type}
260	\small
261	\begin{tabular}{lcc}
262	\toprule
263	\textbf{Exception Type} & \textbf{Samples} & \textbf{Accuracy} \\
264	\midrule
265	TypeError & 96 & 100\% \\
266	ValueError & 62 & 100\% \\
267	IndexError & 41 & 100\% \\
268	KeyError & 28 & 100\% \\
269	AttributeError & 19 & 100\% \\
270	AssertionError & 15 & 100\% \\
271	RecursionError & 12 & 100\% \\
272	Other Exception & 66 & 100\% \\
273	\midrule
274	GeneratorExit (BaseException) & 2 & 0\% \\
275	No exception (pass class) & 849 & 100\% \\
276	\bottomrule
277	\end{tabular}
278	\end{table}
279	
280	This confirms that the model has learned a clean decision boundary: any true \texttt{Exception} subclass in the trace implies failure.
281	The \texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \S\ref{sec:irreducible}.
282	
283	%% ============================================================
284	\section{Trace Length Ablation}
285	\label{sec:trace_length_full}
286	
287	To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.
288	
289	\begin{table}[t]
290	\centering
291	\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\% CIs ($B{=}10{,}000$).}
292	\label{tab:trace_length}
293	\small
294	\begin{tabular}{llcc}
295	\toprule
296	\textbf{Direction} & \textbf{Max Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
297	\midrule
298	Head & 256  & 78.82 & [76.4, 81.0] \\
299	Head & 512  & 80.42 & [78.2, 82.6] \\
300	Head & 1024 & 77.23 & [74.9, 79.6] \\
301	Head & no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
302	\midrule
303	Tail & 256  & 77.48 & --- \\
304	Tail & 512  & 93.61 & --- \\
305	Tail & 1024 & 96.47 & --- \\
306	Tail & 2048 & 97.31 & --- \\
307	\bottomrule
308	\end{tabular}
309	\end{table}
310	
311	\begin{figure}[t]
312	\centering
313	\includegraphics[width=\columnwidth]{budget_curve}
314	\caption{Accuracy as a function of token budget and truncation direction (Qwen-2.5-7B, $N{=}1{,}190$). Tail-truncation (keeping last $k$ tokens) monotonically improves beyond 256 tokens and consistently outperforms head-truncation by 13--19pp at budgets ${\geq}$512. The flat head-truncation curve (77--82\%) contrasts with the steep tail-truncation rise, confirming that diagnostic signal is localized near trace end. Dashed lines show \texttt{exception\_only} (99.83\%) and \texttt{no\_trace} (75.13\%) as upper and lower bounds. Tail-256 (${\approx}$ \texttt{no\_trace}) indicates the signal window begins approximately 256 tokens from the trace terminus.}
315	\label{fig:trace_length}
316	\end{figure}
317	
318	As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
319	To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.
320	
321	\begin{table}[t]
322	\centering
323	\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}
324	\label{tab:trace_length_pairwise}
325	\small
326	\resizebox{\columnwidth}{!}{%
327	\begin{tabular}{llccc}
328	\toprule
329	& \textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
330	\midrule
331	\multirow{4}{*}{\rotatebox{90}{\scriptsize Budget}}
332	& 512 vs.\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\
333	& 1024 vs.\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\
334	& no\_limit vs.\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\
335	& no\_limit vs.\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\
336	\midrule
337	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ no\_trace}}
338	& 256 $-$ no\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\
339	& 512 $-$ no\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\
340	& 1024 $-$ no\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\
341	& no\_limit $-$ no\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\
342	\midrule
343	\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ exc.}}
344	& 256 $-$ exc\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\
345	& 512 $-$ exc\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\
346	& 1024 $-$ exc\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\
347	& no\_limit $-$ exc\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\
348	\bottomrule
349	\end{tabular}%
350	}
351	\end{table}
352	
353	\paragraph{Non-monotonic pattern.}
354	The trend across trace budgets is non-monotonic: 512 tokens (80.42\%) slightly outperforms 256 tokens (78.82\%), but doubling to 1024 tokens \emph{decreases} accuracy to 77.23\%---a statistically significant 3.19pp drop ($p{=}0.002$, 95\% CI [$-$5.29, $-$1.09]).
355	The no-limit condition (81.76\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than the \texttt{no\_trace} baseline (75.13\%; $\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\% CI [$-$0.17, $+$4.37]).
356	This means that truncating traces to an intermediate length can be \emph{worse} than providing no trace at all---the 1024-token budget retains enough irrelevant content to mislead the model while discarding diagnostic events that might appear late in the trace.
357	
358	\paragraph{Comparison to baselines.}
359	All four trace budget conditions significantly exceed \texttt{no\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.
360	The gap to \texttt{exception\_only} (99.83\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.
361	The best full-trace condition (no\_limit, 81.76\%) still lags \texttt{exception\_only} by 18.07pp (95\% CI [$-$20.34, $-$15.88]).
362	
363	\paragraph{Interpretation.}
364	These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
365	The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
366	The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
367	In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).
368	
369	\paragraph{Truncation direction.}
370	Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \texttt{tail\_2048} achieves 97.31\% vs.\ \texttt{head\_2048} (no\_limit) at 81.76\%, a 15.55pp improvement.
371	Even \texttt{tail\_512} (93.61\%) exceeds every head-truncation condition by over 11pp.
372	
373	However, \texttt{tail\_256} (77.48\%) performs at the \texttt{no\_trace} baseline level (75.13\%), indicating that the diagnostic signal does not reside in the very last trace lines.
374	The critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.
375	This is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.
376	
377	The 18.07pp gap from \texttt{full\_trace} to \texttt{exception\_only} decomposes as: 86\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\% residual content noise (the 2.52pp gap from \texttt{tail\_2048} to \texttt{exception\_only} that persists regardless of truncation direction).
378	The fact that \texttt{exception\_only} (99.83\%) still outperforms \texttt{tail\_2048} (97.31\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.
379	
380	\paragraph{Cross-model tail-truncation verification.}
381	Table~\ref{tab:tail_cross_model} extends the tail-2048 analysis to two additional models.
382	The positional concentration pattern generalizes: all three models achieve 94.96--97.90\% with \texttt{tail\_2048}, leaving residual gaps of only 1.93--4.37pp to \texttt{exception\_only}.
383	DeepSeek-6.7B shows the largest residual (4.37pp), consistent with its known sensitivity to long-context formatting (Appendix~\ref{sec:training_dynamics}); the diagnostic signal is present in the tail window but partially degraded by the model's weaker long-context processing.
384	Qwen-1.5B (97.90\%) performs comparably to Qwen-7B (97.31\%), confirming that positional signal extraction, like exception-based extraction, is signal-limited rather than capacity-limited.
385	
386	\begin{table}[t]
387	\centering
388	\caption{Cross-model \texttt{tail\_2048} verification ($N{=}1{,}190$). Positional concentration of diagnostic signal holds across all tested models and architecture families.}
389	\label{tab:tail_cross_model}
390	\small
391	\begin{tabular}{lccc}
392	\toprule
393	\textbf{Model} & \textbf{Tail-2048 (\%)} & \textbf{exc\_only (\%)} & \textbf{Gap (pp)} \\
394	\midrule
395	Qwen-7B & 97.31 & 99.83 & 2.52 \\
396	Qwen-1.5B & 97.90 & 99.83 & 1.93 \\
397	DeepSeek-6.7B & 94.96 & 99.33 & 4.37 \\
398	\bottomrule
399	\end{tabular}
400	\end{table}
401	
402	%% ============================================================
403	\section{Calibration Analysis}
404	\label{sec:calibration_full}
405	
406	Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.
407	
408	\begin{table}[t]
409	\centering
410	\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}
411	\label{tab:calibration}
412	\small
413	\begin{tabular}{lcc}
414	\toprule
415	\textbf{Condition} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} \\
416	\midrule
417	ae\_only & \textbf{0.0004} & \textbf{0.0008} \\
418	exception\_only & 0.0027 & 0.0013 \\
419	VOTA & 0.0054 & 0.005 \\
420	full\_trace & 0.096 & 0.144 \\
421	no\_trace & 0.171 & 0.197 \\
422	\bottomrule
423	\end{tabular}
424	\end{table}
425	
426	Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.
427	Tier~1 conditions (\texttt{ae\_only}: ECE=0.0004; \texttt{exception\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \texttt{full\_trace} (ECE=0.096) and \texttt{no\_trace} (ECE=0.171) exhibit substantial miscalibration.
428	VOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.
429	
430	The Brier scores tell a consistent story: \texttt{ae\_only} (0.0008) and \texttt{exception\_only} (0.0013) achieve near-zero scores, while \texttt{no\_trace} (0.197) indicates substantial miscalibration.
431	
432	\begin{figure}[t]
433	\centering
434	\includegraphics[width=\columnwidth]{fig2_calibration}
435	\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \texttt{exception\_only} (ECE=0.0027) clusters near the diagonal, while \texttt{no\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\times$ gap.}
436	\label{fig:calibration}
437	\end{figure}
438	
439	%% ============================================================
440	\section{Error Overlap Analysis}
441	\label{sec:error_overlap}
442	
443	We analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\ref{fig:error_overlap}).
444	
445	\texttt{exception\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).
446	This orthogonality arises because \texttt{exception\_only} errors are caused by \texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.
447	
448	Among non-exception conditions, error sets exhibit hierarchical containment: \texttt{ae\_only} $\subset$ VOTA $\subset$ \texttt{loop\_only} $\subset$ \texttt{no\_trace}, with pairwise Jaccard indices increasing with signal overlap.
449	\texttt{loop\_only} and \texttt{full\_trace} share the highest overlap (Jaccard ${\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.
450	
451	This analysis confirms that \texttt{exception\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.
452	
453	\begin{figure}[t]
454	\centering
455	\includegraphics[width=\columnwidth]{error_overlap}
456	\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \texttt{exception\_only} (exc\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}
457	\label{fig:error_overlap}
458	\end{figure}
459	
460	%% ============================================================
461	\section{Cross-Dataset Generalization: DebugBench}
462	\label{sec:debugbench_full}
463	
464	To test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \citep{tian2024debugbench}---a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).
465	After filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\%).
466	
467	\begin{table}[t]
468	\centering
469	\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\% CIs. The component ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is preserved, and exception\_only achieves perfect accuracy.}
470	\label{tab:debugbench}
471	\small
472	\begin{tabular}{lcc}
473	\toprule
474	\textbf{Condition} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
475	\midrule
476	exception\_only & \textbf{100.00} & [99.14, 100.00] \\
477	VOTA & 99.77 & [99.30, 100.00] \\
478	no\_trace & 96.71 & [94.80, 98.40] \\
479	\midrule
480	Majority baseline & 51.41 & --- \\
481	\bottomrule
482	\end{tabular}
483	\end{table}
484	
485	Table~\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \texttt{exception\_only} (100.00\%) $\geq$ VOTA (99.77\%) $>$ \texttt{no\_trace} (96.71\%).
486	The \texttt{exception\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.
487	
488	The absolute margins are much narrower than on the main dataset: the \texttt{no\_trace} baseline already achieves 96.71\%---compared to 75.13\% on HumanEval+MBPP---leaving only 3.29pp of headroom for trace-based improvement.
489	This ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.
490	In contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.
491	
492	These results support exception-based verdict prediction as a generalizable approach---the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is consistent across both datasets---but the narrow DebugBench margins are insufficient to independently validate trace importance.
493	The 24.70pp trace lift on the main dataset (no\_trace 75.13\% $\to$ exception\_only 99.83\%) remains the primary evidence for the value of exception-based trace signals.
494	
495	%% ============================================================
496	\section{Cross-Model Robustness Analysis}
497	\label{sec:robustness_analysis}
498	
499	The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
500	Exception events are consistently the most effective component on both models, and their structural simplicity---a fixed-format error message---ensures that the relative advantage over richer representations holds across all seeds.
501	Two of three DeepSeek seeds match Qwen-level accuracy (99.33\%); the outlier (seed 123, 91.09\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\%, though direct evidence is lacking), not a failure of the exception signal itself---even this outlier outperforms VOTA (84.45\%) by 6.64pp.
502	The VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency---the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content---and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \citep{yang2024generalization}.
503	The two factors cannot be disentangled in the current experimental design.
504	Our \texttt{exception\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.
505	The resulting 0.56pp cross-model gap (Table~\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.
506	The practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.
507	
508	%% ============================================================
509	\section{Training Dynamics and Loss Decoupling}
510	\label{sec:training_dynamics}
511	
512	The DeepSeek \texttt{exception\_only} results reveal two instructive training dynamics.
513	First, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\% after epoch~1 but settles at 99.33\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\% to 91.09\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\% at both epoch~1 and epoch~3).
514	Early stopping may yield marginal gains for some seeds, but the epoch effect is small (${\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).
515	
516	Second, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\% vs.\ 99.33\%).
517	The critical difference lies in fail recall: seeds 42 and 456 achieve 100\%, while seed 123 achieves only 70.5\%---the LoRA initialization in seed 123 fails to learn the exception$\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.
518	This demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.
519	The practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.
520	
521	\paragraph{Format collapse, not semantic failure.}
522	The 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.
523	This indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \texttt{exception\_only} inputs.
524	
525	The contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\% to 84.45\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\S\ref{sec:cross_model})---the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.
526	The 84.45\% accuracy reflects a combination of trace information loss and model capability constraints.
527	
528	%% ============================================================
529	\section{Deduplication Statistics}
530	\label{sec:dedup_stats}
531	
532	Table~\ref{tab:dedup} reports the duplication rates across trace formats.
533	Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.
534	Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
535	The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
536	The \texttt{exception\_only} test set contains 48.99\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.
537	
538	\begin{table}[t]
539	\centering
540	\caption{Deduplication statistics. The \texttt{exception\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}
541	\label{tab:dedup}
542	\small
543	\begin{tabular}{lccc}
544	\toprule
545	\textbf{Split} & \textbf{Total} & \textbf{Unique} & \textbf{Dup.\ rate} \\
546	\midrule
547	exception\_only train & 4{,}720 & 2{,}858 & 39.45\% \\
548	exception\_only test  & 1{,}190 &   607 & 48.99\% \\
549	raw\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\% \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	%% ============================================================
555	\section{Regex Baseline Analysis}
556	\label{sec:regex_baselines}
557	
558	To establish a non-learning upper bound, we evaluate six regex-based baselines on the \texttt{exception\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \texttt{full\_trace} inputs.
559	
560	\begin{table}[t]
561	\centering
562	\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \texttt{exception\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\ddag$B5 exploits a data formatting artifact: the \texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}
563	\label{tab:regex}
564	\small
565	\begin{tabular}{llc}
566	\toprule
567	\textbf{Baseline} & \textbf{Method} & \textbf{Acc (\%)} \\
568	\midrule
569	B1: \texttt{[ERROR]} presence & string match & 93.45 \\
570	B2: Traceback presence & string match & 71.51 \\
571	B3: Any keyword & union of B1+B2+Exception & 93.45 \\
572	B4: Exception type regex & regex on exception class names & \textbf{93.61} \\
573	B5: Format marker & \texttt{[No exception data]} $\to$ pass & 99.33$^\ddag$ \\
574	B6: Error count $\geq$2 & count threshold & 92.02 \\
575	\midrule
576	VOTA format regex & best regex on VOTA traces & 75.55 \\
577	full\_trace format regex & best regex on full traces & 77.39 \\
578	\bottomrule
579	\end{tabular}
580	\end{table}
581	
582	The strongest legitimate baseline (B4, 93.61\%) applies regex pattern-matching on Python exception class names (e.g., \texttt{ValueError}, \texttt{TypeError}).
583	Its errors concentrate on 8 boundary samples where a \texttt{ValueError} is raised inside a \texttt{try/except} block and caught---the program passes despite an exception occurring in the trace.
584	SFT \texttt{exception\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.
585	B5 (99.33\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\ SFT yields $p{=}0.041$, confirming a statistically significant difference.
586	
587	\paragraph{Cross-format comparison.}
588	Table~\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.
589	The SFT advantage increases with format complexity: \texttt{no\_trace} (+3.62pp over majority baseline) $<$ \texttt{full\_trace} (+4.37pp) $<$ \texttt{exception\_only} (+6.22pp) $\ll$ VOTA (+23.86pp).
590	The VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \texttt{exception\_only}'s simpler format allows regex to capture most of the signal.
591	
592	\begin{table}[t]
593	\centering
594	\caption{SFT vs.\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \texttt{no\_trace}, keyword matching for \texttt{full\_trace}, pattern matching for VOTA, exception type regex (B4) for \texttt{exception\_only}.}
595	\label{tab:regex_cross_format}
596	\small
597	\begin{tabular}{lccc}
598	\toprule
599	\textbf{Format} & \textbf{SFT (\%)} & \textbf{Regex (\%)} & \textbf{$\Delta$ (pp)} \\
600	\midrule
601	exception\_only & 99.83 & 93.61 & +6.22 \\
602	VOTA & 99.41 & 75.55 & +23.86 \\
603	full\_trace & 81.76 & 77.39 & +4.37 \\
604	no\_trace & 75.13 & 71.51 & +3.62 \\
605	\bottomrule
606	\end{tabular}
607	\end{table}
608	
609	%% ============================================================
610	\section{Cross-Model Zero-Shot Comparison}
611	\label{sec:zeroshot_cross_model}
612	
613	Table~\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \texttt{exception\_only} accuracy across four models.
614	Zero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.
615	SFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.
616	
617	\begin{table}[t]
618	\centering
619	\caption{Zero-shot vs.\ SFT \texttt{exception\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}
620	\label{tab:zeroshot_cross_model}
621	\small
622	\begin{tabular}{llccc}
623	\toprule
624	\textbf{Model} & \textbf{Size} & \textbf{Zero-shot (\%)} & \textbf{SFT (\%)} & \textbf{$\Delta$ (pp)} \\
625	\midrule
626	Qwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\
627	DeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\
628	Qwen-7B & 7B & 89.08 & 99.83 & +10.75 \\
629	CodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\
630	\midrule
631	Range & --- & 42.44pp & 0.56pp & --- \\
632	\bottomrule
633	\end{tabular}
634	\end{table}
635	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b9b68cd-3814-4bc2-b9e7-5b1706474a88",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "f5092552-fc3c-41f8-9174-2987b484e95d",
  "sourceToolAssistantUUID": "7b9b68cd-3814-4bc2-b9e7-5b1706474a88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T18:08:15.207Z_

<details open><summary>🔧 Tool call — Read · `toolu_019quYbvfPgGY14RW1kNjY4S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5092552-fc3c-41f8-9174-2987b484e95d",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3PWNYs8vDgVXXqK6J",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0e2aedb-5998-4db8-9051-ee1cfa3f95bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1QCYw5gcJXWjnsGoXZRzm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10262,
      "cache_read_input_tokens": 8266,
      "output_tokens": 664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10262
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 664,
          "cache_read_input_tokens": 8266,
          "cache_creation_input_tokens": 10262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10262,
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

_source line 21 · 2026-05-17T18:08:15.215Z_

<details><summary>↩ Tool result · `toolu_019quYbvfPgGY14RW1kNjY4S`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[review]{acl}
3	\usepackage{times,latexsym}
4	\usepackage{booktabs}
5	
6	\title{ARR Reproducibility Checklist\\(Supplementary Material)}
7	\author{Anonymous ACL submission}
8	
9	\begin{document}
10	\maketitle
11	
12	\section*{Responsible NLP Research Checklist}
13	
14	\subsection*{A. Limitations and Risks}
15	
16	\begin{enumerate}
17	\item \textbf{Did you discuss the limitations of your work?} \\
18	\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope, single model scale (7B), seed-dependent variance on DeepSeek, the invalidated full\_trace run, generator--evaluator overlap, and task scope limited to verdict prediction.
19	
20	\item \textbf{Did you discuss any potential risks of your work?} \\
21	\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.
22	\end{enumerate}
23	
24	\subsection*{B. Did you use or create scientific artifacts?}
25	
26	\begin{enumerate}
27	\item \textbf{Did you cite the creators of artifacts you used?} \\
28	\textit{Yes.} HumanEval \cite{chen2021evaluating}, MBPP-sanitized \cite{austin2021program}, DebugBench \cite{tian2024debugbench}, Qwen-2.5-Coder-7B/1.5B-Instruct \cite{qwen2025coder}, CodeLlama-13B-Instruct \cite{roziere2024code}, DeepSeek-Coder-6.7B-Instruct \cite{deepseek2024coder}, LoRA \cite{hu2022lora}, and TRL SFTTrainer are all cited.
29	
30	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?} \\
31	\textit{Partial.} All base models and datasets are publicly available. HumanEval is released under MIT license; MBPP under CC-BY-4.0; DebugBench under MIT. Model licenses: Qwen-2.5-Coder under Apache 2.0; DeepSeek-Coder under the DeepSeek License.
32	
33	\item \textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?} \\
34	\textit{Yes.} HumanEval and MBPP are standard code generation benchmarks; we use their canonical test cases for verdict evaluation, consistent with their evaluation purpose. DebugBench is designed for debugging evaluation.
35	
36	\item \textbf{Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?} \\
37	\textit{N/A.} All datasets contain only programming problems and solutions with no personal information.
38	\end{enumerate}
39	
40	\subsection*{C. Computational Experiments}
41	
42	\begin{enumerate}
43	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?} \\
44	\textit{Yes.}
45	\begin{itemize}
46	\item Models: Qwen-2.5-Coder-7B/1.5B-Instruct (7B/1.5B parameters), CodeLlama-13B-Instruct (13B parameters), DeepSeek-Coder-6.7B-Instruct (6.7B parameters). Only LoRA adapters are trained (rank=16, $\alpha$=32, targeting all linear layers).
47	\item Hardware: 2$\times$ RTX PRO 6000 Blackwell (${\sim}$96\,GB VRAM each); each experiment uses a single GPU.
48	\item Total compute: ${\sim}$50 GPU-hours across all conditions, models, and seeds. Per-condition training time ranges from 0.5h (no\_trace) to 4.0h (CodeLlama VOTA). See Appendix~B for per-condition wall-clock times.
49	\end{itemize}
50	
51	\item \textbf{Did you report all hyperparameters?} \\
52	\textit{Yes.} Appendix~B (Table~5) reports: LoRA rank (16), alpha (32), dropout (0.05), target modules (all linear layers), epochs (3), per-device batch size (4), gradient accumulation steps (8), effective batch size (32), learning rate ($2 \times 10^{-4}$), LR scheduler (linear decay), warmup ratio (0.1), weight decay (0.01), max sequence length (2,048 tokens).
53	
54	\item \textbf{Did you report descriptive statistics about your results?} \\
55	\textit{Yes.} All accuracy values include Wilson 95\% confidence intervals. Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42) with reported $p$-values. We report multi-seed results (seeds 42, 123, 456) for the exception\_only condition; other conditions report single-seed results. Standard deviations are provided where multiple seeds are available.
56	
57	\item \textbf{If you used existing packages, did you report the implementation, model, and their versions?} \\
58	\textit{Yes.} HuggingFace TRL SFTTrainer with LoRA via PEFT. Base model identifiers: \texttt{Qwen/Qwen2.5-Coder-7B-Instruct} and \texttt{deepseek-ai/deepseek-coder-6.7b-instruct}.
59	\end{enumerate}
60	
61	\subsection*{D. Human Annotations}
62	
63	\begin{enumerate}
64	\item \textbf{Did you use human annotators?} \\
65	\textit{No.} All labels (pass/fail) are derived from automated test execution. No human annotation was involved.
66	\end{enumerate}
67	
68	\subsection*{E. Data and Code Availability}
69	
70	\begin{itemize}
71	\item \textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.
72	\item \textbf{Data}: Execution traces, VOTA-compressed traces, and train/test splits will be released. Raw traces are generated deterministically from publicly available benchmarks using Python \texttt{sys.settrace}.
73	\item \textbf{Models}: LoRA adapters for all conditions will be released on HuggingFace.
74	\end{itemize}
75	
76	\subsection*{F. Reproducibility Summary}
77	
78	\begin{table}[h]
79	\centering
80	\small
81	\begin{tabular}{lc}
82	\toprule
83	\textbf{Item} & \textbf{Status} \\
84	\midrule
85	All hyperparameters reported & Yes \\
86	Random seeds specified & Yes (42, 123, 456) \\
87	Error bars / CIs reported & Yes (Wilson 95\% CI) \\
88	Statistical tests reported & Yes (bootstrap, McNemar) \\
89	Computing infrastructure reported & Yes \\
90	Training time reported & Yes \\
91	Code release planned & Yes \\
92	Data release planned & Yes \\
93	Model release planned & Yes \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\bibliography{references}
99	
100	\end{document}
101	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0e2aedb-5998-4db8-9051-ee1cfa3f95bd",
  "isSidechain": true,
  "promptId": "ec60f3ff-61a4-4c2f-9b4d-5e80e8a6cf0c",
  "agentId": "aef8cf76137435b1d",
  "type": "user",
  "uuid": "354422f1-c1d0-441a-b040-194136aa45a6",
  "sourceToolAssistantUUID": "a0e2aedb-5998-4db8-9051-ee1cfa3f95bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-17T18:18:10.659Z_

Here are the complete contents of all 9 files:

---

## File 1: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/main.tex`

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[review]{acl}
% \usepackage{acl}  % uncomment for camera-ready (remove [review])
\usepackage{times,latexsym}
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\graphicspath{{../../figures/paper/}}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{xcolor}

\title{Exception Events Are All You Need: \\Component Ablation for Trace-Based Verdict Prediction}
\author{Anonymous ACL submission}

\begin{document}
\maketitle

\begin{abstract}
Execution traces are increasingly used to enhance code language models, but which trace components matter for downstream tasks remains poorly understood.
We present the first systematic component ablation of trace representations for verdict prediction (classifying whether a test passes or fails) across four models spanning three architecture families and 1.5B to 13B parameters.
Exception events alone achieve ${\geq}$99.33\% accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while a code-only baseline shows 9.19pp scale sensitivity (67.3--76.5\%).
Adding more trace information actively hurts: a multi-component representation underperforms exception-only, and the full-trace gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%).
Tail-truncation experiments reveal that diagnostic signal concentrates near the trace terminus (in a localized window, not the absolute end), recovering 86\% of the gap to exception-only.
A format-marker ablation confirms ${\sim}$91\% of the exception signal is semantic (learned by SFT to distinguish caught from uncaught exceptions) rather than format-driven.
These results reveal a two-tier diagnostic hierarchy: Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99\%, while Tier~2 (loop compression) reaches 85.6\%.
Cross-dataset evaluation on DebugBench ($N{=}426$) confirms generalization, with exception-only achieving 100\%.
We reframe verdict prediction as fault detection: the minimal sufficient signal is a compact exception event (median 150 tokens) that is scale-invariant, architecture-independent, and deployable in token-constrained settings.
\end{abstract}

\input{introduction}
\input{method}
\input{experiments}
\input{discussion}
\input{related_work}
\input{conclusion}

\section*{Limitations}

Our study has several limitations.
First, our primary experiments use a single dataset (591 problems from HumanEval and MBPP-sanitized); while a cross-dataset evaluation on DebugBench (\S\ref{sec:debugbench}) confirms that exception dominance generalizes to synthetically injected bugs, generalization to other languages, larger codebases, or real-world fault distributions remains untested.
Second, while we evaluate four models spanning 1.5B to 13B parameters across three architecture families, all are code-specialized; generalization to general-purpose models or larger scales remains untested.
Third, DeepSeek \texttt{exception\_only} exhibits seed-dependent variance: 2/3 seeds achieve 99.33\% while seed 123 yields 91.09\% ($\sigma{=}4.76$pp, $n{=}3$), which we hypothesize reflects LoRA initialization sensitivity in DeepSeek-Coder, though direct evidence is lacking (fail recall = 70.5\% for the outlier vs.\ 100\% for others).
Qwen \texttt{exception\_only} shows perfect seed robustness ($\sigma{=}0$, $n{=}3$), but Qwen \texttt{ae\_only} also exhibits seed variance ($\sigma{=}$0.40pp; seed 123 = 99.08\% vs.\ seeds 42/456 = 99.92\%), though far smaller than DeepSeek's ($\sigma{=}$4.76pp).
Whether training stabilization techniques can eliminate DeepSeek's seed sensitivity is unexplored; other conditions use a single seed.
Fourth, the initial DeepSeek \texttt{full\_trace} run was invalidated by context overflow; a re-run with extended context yields 79.16\% (CI [76.80\%, 81.30\%]), 2.60pp below Qwen (Table~\ref{tab:cross_model}).
Fifth, the candidate solutions were generated by Qwen-2.5-Coder-7B-Instruct, which also serves as one of our evaluation models; this does not affect verdict prediction but may influence the pass/fail distribution.
Sixth, self-familiarity bias may inflate absolute accuracy: both Qwen-2.5-Coder and DeepSeek-Coder were likely exposed to HumanEval and MBPP solutions during pretraining, so the models may partially recognize solutions rather than purely reasoning from trace signals; our cross-dataset evaluation on DebugBench mitigates but does not eliminate this concern.
Seventh, the error distribution in our test set may not reflect real-world fault distributions: exceptions (especially \texttt{TypeError}, \texttt{ValueError}) dominate LLM-generated failures, but production code may exhibit a broader spectrum of silent logic errors where no exception is raised, potentially reducing the effectiveness of exception-based verdict prediction.
Finally, our analysis is limited to verdict prediction; whether exception dominance extends to other classification tasks or generation tasks is an open question.

\section*{Ethics Statement}

This work uses publicly available benchmarks (HumanEval, MBPP-sanitized, DebugBench) and does not involve human subjects, crowdsourced annotations, or personally identifiable information.
All models evaluated are open-source and publicly accessible.
Training uses parameter-efficient LoRA fine-tuning on two RTX PRO 6000 Blackwell GPUs, with each experiment using a single GPU and total compute under 20 GPU-hours across all experiments, resulting in minimal environmental impact.
We do not foresee direct negative societal impacts from this work; verdict prediction is a developer-facing tool for automated testing.

\bibliography{references}

\appendix
\input{appendix}

\end{document}
```

---

## File 2: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/introduction.tex`

```latex
\section{Introduction}

Execution traces (line-by-line records of a program's runtime behavior) have emerged as a promising input modality for code language models \citep{chen2025tracepile,ding2024traced,wang2025dcsh,ni2024next}.
Yet feeding thousands of trace lines to a model can be no better than feeding none: the diagnostic signal drowns in routine execution steps.
\emph{Which trace components actually carry the signal that matters?}

Prior work found no single trace representation consistently outperforms others \citep{wang2025dcsh}, but focused on generation-oriented tasks.
\emph{Verdict prediction}, classifying whether a test passes or fails, is fundamentally different: it is fault detection, not generation.
The model need not simulate execution; it need only determine whether something went wrong.
This distinction suggests that a small, fault-specific trace component may suffice.

We test this hypothesis through the first systematic component ablation of trace representations for verdict prediction.
Using 591 problems from HumanEval \citep{chen2021evaluating} and MBPP-sanitized \citep{austin2021program}, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components across four models spanning 1.5B to 13B parameters and three architecture families: Qwen-2.5-Coder-7B/1.5B-Instruct \citep{qwen2025coder}, CodeLlama-13B-Instruct \citep{roziere2024code}, and DeepSeek-Coder-6.7B-Instruct \citep{deepseek2024coder}.

\textbf{Exception events alone achieve ${\geq}$99.33\% verdict accuracy across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%).}
This near-perfect accuracy holds from 1.5B to 13B parameters, while the code-only baseline (\texttt{no\_trace}) varies from 67.3\% to 76.5\% with strong scale dependence.
The exception signal eliminates the need for model capacity to compensate for missing information.

More surprisingly, adding trace information beyond exceptions actively \emph{hurts}: VOTA (99.41\%) underperforms \texttt{exception\_only} (99.83\%), and the degradation reaches 14.96pp on DeepSeek, compounded by tokenizer-driven truncation.
We approximately decompose this gap: ${\sim}$74\% stems from information overload (irrelevant trace content at inference) and ${\sim}$26\% from gradient dilution (dispersed training signal).
Tail-truncation experiments confirm the mechanism across three models and two architecture families: retaining only the last 2,048 trace tokens captures 95--98\% of \texttt{exception\_only}'s accuracy, because diagnostic events concentrate at the trace terminus.

Our contributions:
\begin{enumerate}
\item \textbf{Exception events are the minimal sufficient signal}: ${\geq}$99.33\% across four models and three families (1.5B--13B), with ${\sim}$91\% of the signal being semantic rather than format-driven (\S\ref{sec:cross_model}, \S\ref{sec:nomarker}). SFT closes a 6--49pp zero-shot gap across four models and three architecture families, and outperforms both few-shot prompting and the best regex heuristic (\S\ref{sec:ablation}). Cross-dataset evaluation on DebugBench ($N{=}426$) yields 100\% (\S\ref{sec:debugbench}).
\item \textbf{Richer traces actively hurt}: We approximately decompose why into gradient dilution (${\sim}$26\%) and information overload (${\sim}$74\%), with cross-model tail-truncation confirming positional concentration across three models (95--98\% of \texttt{exception\_only} recovered; \S\ref{sec:density}, \S\ref{sec:trace_length}).
\item \textbf{Two-tier diagnostic hierarchy}: Tier~1 signals (exceptions, assertions) individually achieve ${\geq}$99\%; Tier~2 (loop compression) reaches 85.6\%, still +10.5pp over no trace (\S\ref{sec:ablation}).
\end{enumerate}
```

---

## File 3: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/method.tex`

```latex
\section{Method}

\subsection{Task Definition}

We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
The model produces a single token (\texttt{pass} or \texttt{fail}), making this a binary classification task.
Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution.

\subsection{Dataset}
\label{sec:dataset}

We sampled 10 candidate solutions per problem from Qwen-2.5-Coder-7B-Instruct (temperature 0.8, top\_p 0.95) for 591 problems from HumanEval \citep{chen2021evaluating} (164) and MBPP-sanitized \citep{austin2021program} (427), executed each against canonical tests with \texttt{sys.settrace} to obtain line-level traces and pass/fail verdicts, yielding 5,910 pairs (67\% pass, 33\% fail).
The dataset is split 80/20 by problem ID into 4,720 training and 1,190 test samples (majority baseline: 71.51\%).
The \texttt{exception\_only} format collapses passing solutions into identical rows (39.45\% train, 48.99\% test duplicates); train--test input overlap is zero (Appendix~\ref{sec:dedup_stats}).

\subsection{Trace Representations}

We define seven conditions that vary the trace information available (Figure~\ref{fig:trace_overview}):
\begin{itemize}
\item \texttt{no\_trace}: Source code and test input only.
\item \texttt{full\_trace}: Complete line-by-line trace with variable states.
\item \texttt{VOTA}: Exception events + assertion-point comparisons + loop compression.
\item \texttt{exception\_only}: Only exception/error events.
\item \texttt{ae\_only}: Only assertion-point actual/expected pairs.
\item \texttt{loop\_only}: Only loop compression summaries.
\item \texttt{VOTA\_no\_ae}: VOTA without assertion-point information.
\end{itemize}

\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{fig1_trace_overview}
\caption{Overview of the verdict prediction pipeline. Source code and a test input are executed to produce a full raw trace. Four conditions vary the trace information: \texttt{no\_trace} (75.13\%), \texttt{full\_trace} (81.76\%), VOTA (99.41\%), and \texttt{exception\_only} (99.83\%). Accuracies for Qwen-2.5-7B (seed=42, $N{=}1{,}190$).}
\label{fig:trace_overview}
\end{figure*}

\subsection{Models and Training}

We evaluate four models spanning three architecture families: \textbf{Qwen-2.5-Coder-7B/1.5B-Instruct} \citep{qwen2025coder}, \textbf{CodeLlama-13B-Instruct} \citep{roziere2024code}, and \textbf{DeepSeek-Coder-6.7B-Instruct} \citep{deepseek2024coder}, covering a 1.5B--13B parameter range (8.7$\times$).
All conditions use LoRA \citep{hu2022lora} (rank=16, $\alpha$=32, dropout=0.05) on all linear layers, 3 epochs, effective batch size 32, LR $2 \times 10^{-4}$ with linear warmup/decay, max sequence length 2{,}048 tokens.
Sequences exceeding this limit are truncated while preserving the verdict label.
The primary seed is 42; seeds 123 and 456 test \texttt{exception\_only} robustness (Appendix~\ref{sec:training_details}).

\subsection{Loss Ablation}

To disentangle training signal from input signal quality, we introduce \texttt{full\_trace\_label\_only}: identical full-trace input but loss computed only on the verdict token (trace positions masked).
Improvement over standard \texttt{full\_trace} is attributable to \emph{gradient dilution}; the remaining gap to VOTA reflects \emph{information overload} at inference time.
```

---

## File 4: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/experiments.tex`

```latex
\section{Experiments}

We evaluate across two research questions:
(1)~Do Tier~1 exception signals generalize across models?
(2)~What is the relative contribution of each trace component?
All experiments use $N{=}1{,}190$ test samples; accuracy is reported with Wilson 95\% CIs.
Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42); all differences are significant at $p{<}0.0001$ unless noted.

\subsection{Cross-Model Comparison}
\label{sec:cross_model}

Table~\ref{tab:cross_model} compares four models spanning an 8.7$\times$ parameter range (1.5B--13B) and three architecture families (Qwen, DeepSeek, CodeLlama) under key conditions.

\begin{table}[t]
\centering
\caption{Cross-model verdict accuracy (\%, $N{=}1{,}190$). Bold: best accuracy per model. Multi-seed entries show mean$\pm$std (3 seeds). $^\dag$2/3 seeds; one seed excluded due to LoRA initialization failure (91.09\%, fail recall = 70.5\%; see Appendix~\ref{sec:training_dynamics}). \texttt{ae\_only} and \texttt{loop\_only} ablations tested on Qwen-7B (3 seeds) to isolate component contributions; cross-model validation focused on the primary conditions. Full CIs in Appendix~\ref{sec:full_results}.}
\label{tab:cross_model}
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lcccc}
\toprule
\textbf{Condition} & \textbf{Qwen-7B} & \textbf{Qwen-1.5B} & \textbf{CL-13B} & \textbf{DS-6.7B} \\
\midrule
exception\_only & \textbf{99.83}{\scriptsize$\pm$0.00} & \textbf{99.83} & \textbf{99.89}{\scriptsize$\pm$0.10} & \textbf{99.33}$^\dag$ \\
ae\_only & 99.64{\scriptsize$\pm$0.49} & --- & --- & --- \\
VOTA & 99.41 & 99.58 & 98.57 & 84.45 \\
no\_trace & 75.13 & 67.31 & 76.50 & 73.36 \\
\midrule
Majority baseline & \multicolumn{4}{c}{71.51} \\
\bottomrule
\end{tabular}%
}
\end{table}

\paragraph{Exception dominance across families.}
Under \texttt{exception\_only}, the Qwen and CodeLlama families achieve ${\geq}$99.83\% (mean): Qwen-7B (99.83\%$\pm$0.00, 3 seeds), Qwen-1.5B (99.83\%), and CodeLlama-13B (99.89\%$\pm$0.10, 3 seeds; seed 123 achieves 100\%).
DeepSeek-6.7B reaches 99.33\% on 2/3 seeds with one LoRA-sensitivity outlier at 91.09\% (seed 123; fail recall = 70.5\%); even the outlier outperforms VOTA (84.45\%) by 6.64pp.
Excluding the DeepSeek outlier, the cross-model range is 0.56pp (99.33--99.89\%), the tightest of any condition.

\paragraph{Scale invariance of exception signals.}
Exception-based accuracy is shared by models spanning 1.5B to 13B parameters (8.7$\times$): both Qwen-1.5B and CodeLlama-13B achieve 99.83\%+ on the same representation.
CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), confirming that Qwen's two persistent errors (from \texttt{GeneratorExit}; Appendix~\ref{sec:irreducible}) are high-probability convergence artifacts rather than hard data limitations.
In contrast, \texttt{no\_trace} scales monotonically with capacity: 67.31\% (1.5B) $\to$ 75.13\% (7B) $\to$ 76.50\% (13B), a 9.19pp range that exception events completely eliminate (Figure~\ref{fig:cross_scale}).

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{fig3_cross_model_gap}
\caption{Verdict accuracy vs.\ model scale. \texttt{exception\_only} maintains ${\geq}$99.33\% regardless of scale (1.5B--13B), while \texttt{no\_trace} shows monotonic scale sensitivity (+9.19pp from 1.5B to 13B). The \texttt{nomarker} condition (format markers removed) shows no degradation at smaller scale (${\sim}$97.7--97.8\%).}
\label{fig:cross_scale}
\end{figure}

\paragraph{VOTA cross-family variation.}
VOTA accuracy varies across families: 99.58\% (Qwen-1.5B) $>$ 99.41\% (Qwen-7B) $>$ 98.57\% (CodeLlama-13B; \texttt{codellama13b\_vota\_seed42}, CI [97.9, 99.2]) $\gg$ 84.45\% (DeepSeek-6.7B).
The CodeLlama result (17 errors) narrows the gap: among models without tokenizer-driven truncation, the VOTA range is only 1.01pp (98.57--99.58\%), suggesting that the 14.96pp DeepSeek deficit is primarily a truncation artifact rather than an inherent model capability limitation (91.7\% of DeepSeek training samples were affected; Appendix~\ref{sec:tokenizer_analysis}).
In contrast, \texttt{exception\_only} inputs are compact (median 150 tokens, mean 398 due to verbose fail-class exceptions), making the cross-model comparison clean.

\subsection{Component Ablation}
\label{sec:ablation}

We restrict \texttt{ae\_only} and \texttt{loop\_only} ablations to Qwen-7B, as these component-level analyses target the trace composition mechanism rather than cross-model generalization.
Table~\ref{tab:ablation} decomposes VOTA on Qwen-2.5-7B (seed=42) and reveals a two-tier hierarchy.

\begin{table}[t]
\centering
\caption{Component ablation on Qwen-2.5-7B ($N{=}1{,}190$). Tier~1 signals achieve near-perfect accuracy; combining them (VOTA) slightly dilutes performance. $^\dag$\texttt{ae\_only}: 3-seed mean 99.64\% ($\pm$0.49; seeds 42: 99.92, 123: 99.08, 456: 99.92). \texttt{exception\_only}: 99.83\% ($\pm$0.00, 3 seeds), more stable ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).}
\label{tab:ablation}
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{llccc}
\toprule
\textbf{Condition} & \textbf{Components} & \textbf{Acc (\%)} & \textbf{95\% CI} & \textbf{Tier} \\
\midrule
ae\_only & assertion-point & 99.64$^\dag$ & [99.26, 99.87] & 1 \\
exception\_only & exception events & \textbf{99.83} & [99.58, 100.00] & 1 \\
VOTA & exc+ae+loop & 99.41 & [98.82, 99.83] & --- \\
VOTA\_no\_ae & exc+loop & 99.41 & [98.90, 99.80] & --- \\
loop\_only & loop compression & 85.63 & [83.53, 87.56] & 2 \\
full\_trace & complete trace & 81.76 & [79.70, 83.90] & --- \\
no\_trace & none & 75.13 & [72.77, 77.48] & --- \\
\midrule
Regex (best) & exc.\ type regex & 93.61 & --- & --- \\
3-shot (Qwen-7B) & in-context learning & 90.84 & --- & --- \\
Zero-shot (4 models) & prompting & 51.0--93.5 & --- & --- \\
\bottomrule
\end{tabular}%
}
\end{table}

Tier~1 signals are individually sufficient: \texttt{ae\_only} (3-seed mean 99.64\% $\pm$ 0.49) and \texttt{exception\_only} (99.83\% $\pm$ 0.00) both exceed VOTA ($p{=}0.01$), implying that combining signals introduces noise; \texttt{exception\_only} is more stable across seeds ($\sigma{=}$0 vs.\ $\sigma{=}$0.49).
Removing assertion points has no effect (\texttt{VOTA\_no\_ae} = 99.41\%), confirming exception dominance.
Tier~2 \texttt{loop\_only} (85.63\%) improves 10.50pp over \texttt{no\_trace} ($p{<}0.0001$) but falls far short of Tier~1.
\paragraph{Rule-based baseline comparison.}
The strongest non-trivial regex heuristic (B4: exception class name matching) achieves 93.61\% accuracy (F1=0.876), trailing SFT \texttt{exception\_only} (99.83\%, F1=0.997) by 6.22pp (McNemar $p{<}0.001$).
The gap concentrates on caught-exception boundary cases: regex flags all exception events as failures, while SFT learns to distinguish caught exceptions (benign, inside \texttt{try/except}) from uncaught faults, correctly resolving 6/8 boundary samples (Appendix~\ref{sec:regex_baselines}).
Across trace formats, SFT consistently outperforms the best applicable regex, from +3.62pp (\texttt{no\_trace} over majority baseline) to +23.86pp (VOTA), with the largest gains on formats requiring semantic interpretation (Appendix~\ref{sec:regex_baselines}).

\paragraph{Zero-shot and few-shot LLM baselines.}
Zero-shot prompting spans 51.0--93.5\% across four models (CodeLlama-13B: 51.01\%, Qwen-7B: 89.08\%, DeepSeek-6.7B: 90.59\%, Qwen-1.5B: 93.45\%), a 42.44pp range that SFT compresses to 0.56pp (99.33--99.89\%).
Zero-shot performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms both Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%), indicating that pretraining data distribution, not capacity, determines zero-shot verdict ability.
CodeLlama-13B drops below the majority baseline (71.51\%), showing extreme fail bias (72.4\% of predictions are \texttt{fail}).
Three-shot in-context learning on Qwen-7B (90.84\%, fail recall = 80.53\%) improves only 1.76pp over zero-shot and still trails both the regex heuristic (93.61\%) and SFT by 8.99pp, confirming that a few examples cannot substitute for task-specific fine-tuning.
SFT normalizes this cross-architecture variance, closing a 6--49pp gap to ${\geq}$99.33\% across all models with 4,720 training samples (Appendix~\ref{sec:zeroshot_cross_model}).

\subsection{Format Marker Ablation}
\label{sec:nomarker}

The \texttt{exception\_only} format includes a \texttt{[No exception data in trace]} marker in all pass-class samples (regex baseline B5 exploits this for 99.33\% accuracy; Appendix~\ref{sec:regex_baselines}).
To quantify the marker's contribution, we retrain with all format markers removed (\texttt{nomarker} condition).

Qwen-7B 3-seed mean: 97.65\% $\pm$ 0.96 (seeds 42/123/456: 96.55/98.32/98.07\%), a drop of 2.18pp from \texttt{exception\_only} (99.83\%).
Qwen-1.5B: 97.82\%, drop of 2.01pp.
The marker contribution (${\sim}$2pp) accounts for only ${\sim}$9\% of the total exception lift over \texttt{no\_trace} (24.70pp on 7B).
Exception events thus provide two signal layers that show no degradation at smaller scale: structural markers (${\sim}$2pp, regex-learnable) and semantic exception content (${\sim}$22pp, requiring SFT to distinguish caught from uncaught exceptions).

\subsection{Information Density Decomposition}
\label{sec:density}

The 17.65pp gap between \texttt{full\_trace} (81.76\%) and VOTA (99.41\%) decomposes via \texttt{full\_trace\_label\_only}, which retains the full trace but masks all trace tokens from the loss.

\begin{table}[t]
\centering
\caption{Approximate information density decomposition: gradient dilution (${\sim}$26\%) vs.\ information overload (${\sim}$74\%).}
\label{tab:density}
\small
\begin{tabular}{lccc}
\toprule
\textbf{Condition} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs.\ full\_trace} & \textbf{Gap explained} \\
\midrule
full\_trace & 81.76 & --- & --- \\
label\_only & 86.22 & +4.46pp & 26\% \\
VOTA & 99.41 & +17.65pp & 100\% \\
\bottomrule
\end{tabular}
\end{table}

Gradient dilution accounts for approximately 26\% of the gap (+4.46pp, $p{<}0.0001$, bootstrap 95\% CI $[{+}2.35, {+}6.55]$): when the model no longer wastes gradient updates on predicting trace tokens, accuracy improves even with identical input.
The remaining ${\sim}$74\% (+13.19pp) reflects information overload at inference: the model receives thousands of irrelevant trace lines that compete for attention with the diagnostic signal, regardless of loss design.
This asymmetry implies that trace compression methods should prioritize \emph{content selection} (removing irrelevant lines) over \emph{loss engineering} (masking non-target tokens), as the larger bottleneck is what the model sees, not how it is trained.
The two factors may interact, so this decomposition is approximate.

\subsection{Additional Analyses}
\label{sec:additional}

\paragraph{Trace length ablation.}
\label{sec:trace_length}
Varying the trace token budget (256--no limit) on Qwen yields accuracy in a narrow 77.2\%--81.8\% band with a non-monotonic pattern, confirming that trace content quality, not quantity, is the bottleneck (Appendix~\ref{sec:trace_length_full}).
Notably, 1024-token traces (77.23\%) underperform 512-token traces (80.42\%), revealing that mid-length traces are long enough to introduce execution noise yet too short to reach the diagnostic events concentrated at trace end.
This further supports our claim that signal density, not quantity, determines model performance.

\paragraph{Truncation direction.}
Reversing the truncation direction confirms that diagnostic signal concentrates near the trace terminus: on Qwen-7B, \texttt{tail\_2048} (97.31\%) outperforms \texttt{head\_2048} (81.76\%) by 15.55pp, and \texttt{tail\_256} (77.48\%) drops to the \texttt{no\_trace} baseline, localizing the signal window to 256--512 tokens from the trace end.
Cross-model verification confirms the pattern across two architecture families and two scales: Qwen-1.5B \texttt{tail\_2048} = 97.90\% (CI [97.06, 98.74]), DeepSeek-6.7B = 94.96\% (CI [93.70, 96.22]), with residual gaps to \texttt{exception\_only} of only 1.93pp and 4.37pp respectively (Appendix~\ref{sec:trace_length_full}).
The positional concentration hypothesis holds across all tested configurations, with \texttt{tail\_2048} capturing 95--98\% of \texttt{exception\_only}'s accuracy.
The residual gap confirms that semantic extraction (identifying exception type and message by content) still outperforms positional extraction (retaining a fixed window that includes non-diagnostic lines).

\paragraph{Calibration.}
\label{sec:calibration}
Calibration mirrors the tier hierarchy: \texttt{exception\_only} ECE = 0.0027 vs.\ \texttt{no\_trace} ECE = 0.171, a 63$\times$ gap (Appendix~\ref{sec:calibration_full}).

\paragraph{Error orthogonality.}
\texttt{exception\_only}'s 2 errors have zero overlap with all other conditions' error sets (Jaccard = 0.000), confirming it operates on an independent signal dimension (Appendix~\ref{sec:error_overlap}).

\paragraph{Exception type breakdown.}
A per-exception-type breakdown (Appendix~\ref{sec:exception_type}) confirms that all standard exception types achieve 100\% accuracy; the only failures arise from \texttt{GeneratorExit}, a benign \texttt{BaseException} subclass.

\paragraph{Cross-dataset generalization.}
\label{sec:debugbench}
On DebugBench \citep{tian2024debugbench} ($N{=}426$), the ranking is preserved: \texttt{exception\_only} 100\%, VOTA 99.77\%, \texttt{no\_trace} 96.71\%; narrow margins reflect a ceiling effect from structurally distinctive mutations (Appendix~\ref{sec:debugbench_full}).
```

---

## File 5: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/discussion.tex`

```latex
\section{Discussion}

Verdict prediction is fundamentally fault detection: the model must determine whether execution deviated from expected behavior.
Exception events succeed because they are the runtime's primary fault indicator.
When Python raises an unhandled exception, it records exactly what went wrong (the error type), where it happened (the stack frame), and why (the error message).
This is precisely the information needed for a pass/fail decision, packaged in a compact, self-contained format.
Non-exception trace components (variable states, loop iterations, line-by-line control flow) record \emph{how} the program ran, not \emph{whether} it failed, and dilute the model's attention without providing complementary diagnostic information.

This mechanistic account explains three key results.
First, adding trace information beyond exceptions actively \emph{hurts} (VOTA $<$ \texttt{exception\_only}, Table~\ref{tab:ablation}), because non-diagnostic content competes for attention.
Second, tail-truncation captures 95--98\% of \texttt{exception\_only}'s accuracy across three models and two architecture families (\S\ref{sec:trace_length}), because exceptions are recorded near the trace terminus where Python's error propagation concentrates them (though not at the absolute end: \texttt{tail\_256} ${\approx}$ \texttt{no\_trace}, with the signal localized in a 256--512 token window from the end).
Third, the 6.22pp SFT advantage over the best regex baseline concentrates on caught-exception boundary cases (Appendix~\ref{sec:regex_baselines}), confirming the model learns to distinguish \emph{whether an exception terminated execution} rather than merely detecting exception presence.
The 0.56pp cross-model exception gap (Appendix~\ref{sec:robustness_analysis}) and the format-collapse nature of the DeepSeek outlier (Appendix~\ref{sec:training_dynamics}) further support that the signal, not the model, is the binding constraint.

\paragraph{Why exception\_only outperforms ae\_only.}
Although \texttt{ae\_only} achieves 99.92\% on seed 42, it is a strict superset of the exception signal: assertion-point comparisons include the exception event (when present) plus additional information such as fallback local variable states.
Multi-seed evaluation reveals that this extra content introduces noise: \texttt{ae\_only} achieves 99.64\% mean accuracy ($\pm$0.49, seeds 42/123/456) while \texttt{exception\_only} achieves 99.83\% ($\pm$0.00).
The zero-variance result for \texttt{exception\_only} indicates that it captures a minimal sufficient signal (the compact exception event), while \texttt{ae\_only}'s additional components (fallback locals, assertion formatting) occasionally mislead the model, manifesting as seed-dependent variance ($\sigma{=}$0.49pp).
Attention analysis on representative samples confirms this interpretation: within exception events, the error type and location markers receive 5--10$\times$ higher per-token attention than the verbose locals context (module paths, imported objects), suggesting the model learns to focus on diagnostic signals rather than incidental runtime state.
Thus \texttt{exception\_only} is both more precise and more stable than its superset.

\paragraph{SFT vs.\ regex incremental analysis.}
The gap between B5 (format marker, 99.33\%) and SFT \texttt{exception\_only} (99.83\%) isolates the value of learned semantic understanding (McNemar $p{=}0.041$, Table~\ref{tab:regex}).
Among 8 test samples where pass-labeled code triggers exceptions (from 2 distinct problems), the SFT model correctly classifies 6 (all from MBPP/113, a try/except ValueError pattern) while B5 misclassifies all 8. The 2 remaining errors (HumanEval/95, GeneratorExit) are misclassified by most training configurations (see Appendix~\ref{sec:irreducible}). At the problem level, SFT handles 1/2 exception-type edge cases vs B5's 0/2.
This confirms that SFT learns a genuine semantic boundary (distinguishing caught from uncaught exceptions) rather than merely detecting exception presence or format markers.

\paragraph{Why zero-shot and few-shot prompting fall short.}
Zero-shot prompting spans 51.0--93.5\% across four models, with cross-architecture variance (42.44pp) dwarfing the SFT range (0.56pp).
The failure is not in exception detection but in verdict calibration: the model recognizes that an exception occurred but cannot reliably determine whether it terminated execution or was caught by a \texttt{try/except} block.
Performance does not correlate with model size: Qwen-1.5B (93.45\%) outperforms Qwen-7B (89.08\%) and CodeLlama-13B (51.01\%, extreme fail bias with 72.4\% of predictions as \texttt{fail}).
Within the Qwen family, the 1.5B model's higher zero-shot accuracy likely reflects consistent code training data quality across scales: the smaller model already understands exception format, but both lack the verdict-specific calibration that SFT provides (SFT gap: 6.38pp for 1.5B vs.\ 10.75pp for 7B).
Three-shot in-context learning (90.84\% on Qwen-7B, fail recall = 80.53\%) improves fail recall by 13.57pp over zero-shot but still trails SFT by 8.99pp: three examples cannot cover the diversity of caught-exception patterns in the training distribution.
SFT normalizes this cross-architecture variance by grounding exception patterns in task-specific verdict labels, compressing a 42.44pp zero-shot range to 0.56pp.

\paragraph{Format marker sensitivity.}
The B5 baseline (Appendix~\ref{sec:regex_baselines}) achieves 99.33\% by exploiting a deterministic format marker (\texttt{[No exception data in trace]}) present in all pass samples.
This near-ceiling performance from a trivial pattern raises a concern: does SFT also learn this shortcut?
The answer is partially yes: the format marker correlates perfectly with the pass class. But the SFT model additionally handles the 8 boundary samples where exceptions occur in passing code, achieving 6/8 correct vs.\ B5's 0/8.
A \emph{nomarker} ablation (\S\ref{sec:nomarker}) confirms genuine exception semantics: Qwen-7B 3-seed mean 97.65\%$\pm$0.96 and Qwen-1.5B 97.82\%, a drop of only ${\sim}$2pp.
The marker contribution (${\sim}$9\% of total lift) is small relative to semantic content (${\sim}$91\%), confirming that SFT learns exception semantics rather than format shortcuts.
Both signal layers show comparable accuracy across the two tested scales (1.5B and 7B produce 97.8\% and 97.7\% nomarker accuracy, respectively).

\paragraph{Near-perfect floor, not hard ceiling.}
Samples 901 and 905 (HumanEval/95, \texttt{check\_dict\_case}) are misclassified by most configurations: Qwen-7B (3 seeds), Qwen-1.5B, and CodeLlama-13B seed 42/456 all produce exactly these 2 errors.
The root cause is deterministic: Python's \texttt{all()} raises \texttt{GeneratorExit} (a \texttt{BaseException} subclass) during generator short-circuit, recorded as \texttt{[ERROR]} despite the test passing.
However, CodeLlama-13B seed 123 achieves 100\% (0/1190 errors), correctly classifying both samples.
This confirms that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most initializations) rather than a hard data limitation: the representation supports perfect accuracy, though most LoRA initializations converge to the same 2-error basin.
On this task, exception-only accuracy is \emph{signal-limited} rather than \emph{capacity-limited}: three architecture families spanning 1.5B to 13B converge on the same floor, while \texttt{no\_trace} shows monotonic scale dependence (67.3\% $\to$ 75.1\% $\to$ 76.5\%).

\paragraph{Tier hierarchy: practical implications.}
The two-tier structure (Tier~1 ${\geq}$99\%; Tier~2 = 85.6\%) has direct engineering implications for trace-augmented systems.
First, it implies a \emph{diminishing returns} principle: once a Tier~1 signal is available, adding more trace information provides no benefit and may actively degrade performance through attention dilution.
Second, the hierarchy suggests a fallback design: systems should attempt Tier~1 extraction (exception events) and only resort to Tier~2 signals (loop compression) when no exception is raised. Even Tier~2 alone substantially outperforms no-trace baselines (+10.50pp).
Third, the minimal token footprint of Tier~1 signals (median 150 tokens vs.\ ${\sim}$1{,}900 for VOTA post-truncation) makes them viable for deployment in token-constrained settings (e.g., real-time CI pipelines, mobile inference).
```

---

## File 6: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/related_work.tex`

```latex
\section{Related Work}

\paragraph{Execution Traces for Code LLMs.}
TracePile \citep{chen2025tracepile} scaled trace-augmented training to 2.6M samples; \citet{wang2025dcsh} found trace utility to be task- and format-dependent, a finding we extend by identifying exception events as the dominant signal for verdict prediction.
NExT \citep{ni2024next} and ET-CoT \citep{eguchi2025etcot} leveraged trace chain-of-thought for repair and execution reasoning.
\citet{ferrando2025execute} found compact traces comparable to full traces, supporting our information density finding.
CRUXEval \citep{gu2024cruxeval} established execution reasoning benchmarks, extended to 19 languages by \citet{xu2025cruxevalx}.
None decompose which trace components contribute to \emph{classification} accuracy.

\paragraph{Code Verdict and Patch Classification.}
TRACED \citep{ding2024traced} showed execution-aware pretraining improves vulnerability and clone detection.
In patch correctness, APPT \citep{appt2024} achieved 79.7\% with BERT+LSTM; LLM4PatchCorrect \citep{zhou2024llm4patch} reached 84.4\% using execution traces.
FuseFL \citep{widyasari2024fusefl} demonstrated that structured fault signals improve fault localization.
\citet{foster2025mutation} deployed LLM-based equivalence detection at Meta with 0.95 precision.
These approaches treat traces as monolithic inputs; none isolate individual components, compare against rule-based baselines to quantify the value of learned representations, or test cross-model generalization.

\paragraph{Fault Localization.}
Spectrum-based fault localization (SBFL) ranks program elements by statistical suspiciousness computed from passing/failing test spectra.
Classic metrics (Ochiai \citep{abreu2007accuracy}, Tarantula \citep{jones2002visualization}, DStar \citep{wong2014dstar}) share a core insight with our work: abnormal execution events (here, coverage patterns correlated with failure) are the most informative diagnostic signal.
Recent LLM-based approaches extend this: AutoFL \citep{kang2024autofl} uses function-level call graphs with ChatGPT; AgentFL \citep{qin2024agentfl} introduces multi-agent localization; LLM4FL \citep{widyasari2024llm4fl} combines SBFL spectra with LLM reasoning; and \citet{mukherjee2025llmfl} demonstrate that LLMs can localize faults from test failure information alone.
Verdict prediction is a prerequisite to fault localization: one must first determine \emph{whether} a fault exists before localizing \emph{where} it is.
Our exception-based approach and SBFL share the principle that anomalous execution events carry the strongest diagnostic signal, but operate at different granularities: we classify at the test level (pass/fail) while FL localizes at the statement or method level.

\paragraph{Trace Compression and Selection.}
TraceCoder \citep{huang2026tracecoder} and InspectCoder \citep{wang2025inspectcoder} use selective trace extraction for debugging; \citet{haque2025traces} found raw traces provide limited repair benefit, supporting our compression finding.
Our approximate information density decomposition (gradient dilution ${\sim}$26\% vs.\ information overload ${\sim}$74\%) provides the first quantitative framework for \emph{why} compression helps, complementing these methods' focus on \emph{how} to compress.
```

---

## File 7: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/conclusion.tex`

```latex
\section{Conclusion}

We presented the first systematic component ablation of trace representations for verdict prediction across four models (1.5B--13B, three architecture families).
Exception events alone achieve ${\geq}$99.33\% across all four models (${\geq}$99.83\% on three of four; one seed reaches 100\%), while \texttt{no\_trace} shows 9.19pp scale sensitivity (67.3--76.5\%).
Adding more trace information actively hurts: the gap approximately decomposes into information overload (${\sim}$74\%) and gradient dilution (${\sim}$26\%), and tail-truncation confirms that diagnostic signal concentrates at the trace terminus.
A format-marker ablation shows ${\sim}$91\% of the exception signal is semantic rather than format-driven, and cross-dataset evaluation on DebugBench confirms generalization (\texttt{exception\_only}: 100\%, $N{=}426$).

The broader implication is that verdict prediction is not an information-starved task that benefits from richer context.
It is a fault detection task where the runtime has already surfaced the critical diagnostic signal; the model's role is to interpret whether that signal indicates a terminal fault (as the SFT advantage over regex on caught-exception cases confirms).
This reframing suggests a design principle for trace-augmented systems: extract the highest-specificity diagnostic signal (median 150 tokens) and discard everything else.
Future work should test whether this principle extends to additional programming languages, larger real-world codebases, silent logic errors where no exception is raised, and tasks beyond verdict prediction.
```

---

## File 8: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/appendix.tex`

```latex
\section{Per-Class Performance Breakdown}
\label{sec:per_class}

Table~\ref{tab:per_class} reports per-class precision, recall, and F1 for all experimental conditions.

\begin{table*}[t]
\centering
\caption{Per-class precision, recall, and F1 for all experimental conditions (seed 42). DeepSeek VOTA achieves 100\% fail precision but only 45.4\% fail recall, indicating systematic bias toward predicting \texttt{pass}. DeepSeek \texttt{exception\_only} seed 42 achieves 100\% fail recall, but seed 123 drops to 70.5\% (see Table~\ref{tab:full_deepseek}).}
\label{tab:per_class}
\small
\begin{tabular}{llccccccc}
\toprule
\textbf{Condition} & \textbf{Model} & \textbf{Acc} & \textbf{Pass P} & \textbf{Pass R} & \textbf{Pass F1} & \textbf{Fail P} & \textbf{Fail R} & \textbf{Fail F1} \\
\midrule
No Trace          & Qwen-2.5-7B & 75.13 & 87.76 & 75.79 & 81.34 & 54.73 & 73.45 & 62.72 \\
Full Trace        & Qwen-2.5-7B & 81.76 & 87.74 & 86.60 & 87.17 & 67.43 & 69.62 & 68.51 \\
Full Trace (LO)   & Qwen-2.5-7B & 86.22 & 88.21 & 93.18 & 90.63 & 80.07 & 68.73 & 73.97 \\
VOTA              & Qwen-2.5-7B & 99.41 & 100.00 & 99.18 & 99.59 & 97.98 & 100.00 & 98.98 \\
Exception Only    & Qwen-2.5-7B & 99.83 & 100.00 & 99.76 & 99.88 & 99.41 & 100.00 & 99.71 \\
AE Only           & Qwen-2.5-7B & 99.92 & 100.00 & 99.88 & 99.94 & 99.71 & 100.00 & 99.85 \\
Loop Only         & Qwen-2.5-7B & 85.63 & 92.39 & 87.07 & 89.66 & 71.65 & 82.01 & 76.48 \\
VOTA\_no\_ae       & Qwen-2.5-7B & 99.41 & 99.88 & 99.29 & 99.59 & 98.26 & 99.71 & 98.98 \\
\midrule
No Trace          & DeepSeek-6.7B & 73.36 & 81.71 & 80.85 & 81.28 & 53.16 & 54.57 & 53.86 \\
Full Trace        & DeepSeek-6.7B & 79.16 & 85.70 & 85.10 & 85.40 & 63.20 & 64.30 & 63.70 \\
VOTA              & DeepSeek-6.7B & 84.45 & 82.14 & 100.00 & 90.20 & 100.00 & 45.40 & 62.50 \\
Exception Only    & DeepSeek-6.7B & 99.33 & 100.00 & 99.06 & 99.53 & 97.69 & 100.00 & 98.83 \\
\bottomrule
\end{tabular}
\end{table*}

%% ============================================================
\section{Training Details}
\label{sec:training_details}

Table~\ref{tab:hyperparams} summarizes the training hyperparameters shared across all conditions.
All experiments use the HuggingFace TRL \texttt{SFTTrainer} with LoRA \citep{hu2022lora} applied to all linear layers.

\begin{table}[t]
\centering
\caption{Training hyperparameters (shared across all conditions).}
\label{tab:hyperparams}
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{ll}
\toprule
\textbf{Hyperparameter} & \textbf{Value} \\
\midrule
LoRA rank ($r$)            & 16 \\
LoRA alpha ($\alpha$)      & 32 \\
LoRA dropout               & 0.05 \\
LoRA target modules        & all linear layers \\
\midrule
Epochs                     & 3 \\
Per-device batch size       & 4 \\
Gradient accumulation steps & 8 \\
Effective batch size        & 32 \\
\midrule
Learning rate               & $2 \times 10^{-4}$ \\
LR scheduler                & linear decay \\
Warmup ratio                & 0.1 \\
Weight decay                & 0.01 \\
\midrule
Max sequence length         & 2048 tokens \\
Primary seed                & 42 \\
Robustness seeds            & 123, 456 \\
\midrule
Hardware                    & 1$\times$ RTX PRO 6000 Blackwell (96\,GB VRAM) \\
Framework                   & HuggingFace TRL SFTTrainer \\
\bottomrule
\end{tabular}%
}
\end{table}

Table~\ref{tab:train_time} reports per-condition training wall-clock times.
Conditions with longer trace inputs (e.g., \texttt{full\_trace}, VOTA) require proportionally more training time due to increased sequence lengths.

\begin{table}[t]
\centering
\caption{Training wall-clock time per condition on a single RTX PRO 6000 Blackwell GPU. Where multiple seeds were run, individual times are listed.}
\label{tab:train_time}
\small
\begin{tabular}{llr}
\toprule
\textbf{Condition} & \textbf{Seed(s)} & \textbf{Time (h)} \\
\midrule
no\_trace       & 42         & ${\sim}$0.5 \\
full\_trace     & 42         & ${\sim}$2.2 \\
label\_only     & 42         & ${\sim}$2.2 \\
VOTA                     & 42         & ${\sim}$2.3 \\
exception\_only & 42         & ${\sim}$2.1 \\
exception\_only & 123        & ${\sim}$2.1 \\
exception\_only & 456        & ${\sim}$1.3 \\
ae\_only        & 42         & ${\sim}$1.8 \\
loop\_only      & 42         & ${\sim}$2.1 \\
VOTA\_no\_ae    & 42         & ${\sim}$1.8 \\
\bottomrule
\end{tabular}
\end{table}

%% ============================================================
\section{VOTA Trace Examples}
\label{sec:vota_examples}

We provide two representative VOTA trace examples illustrating the fail and pass cases.
In the fail case, the exception event provides an unambiguous fault signal.
In the pass case, the absence of an exception event combined with a matching assertion point confirms correct execution.

\paragraph{Fail example.}
A \texttt{ZeroDivisionError} triggers an \texttt{[ERROR]} event, providing a direct fault signal that is sufficient for the model to predict \texttt{fail}.

\begin{small}
\begin{verbatim}
## Function
def divide(a, b):
    return a / b

## Test Input
divide(1, 0)

## Expected Output
inf

## VOTA Trace
[ERROR] ZeroDivisionError: division by zero

## Verdict
fail
\end{verbatim}
\end{small}

\paragraph{Pass example.}
No exception is raised, and the assertion point confirms that the actual output matches the expected value.

\begin{small}
\begin{verbatim}
## Function
def add(a, b):
    return a + b

## Test Input
add(2, 3)

## Expected Output
5

## VOTA Trace
[LOOP] No loops detected.
[ASSERT] actual=5, expected=5

## Verdict
pass
\end{verbatim}
\end{small}

These examples illustrate the core asymmetry exploited by the \texttt{exception\_only} condition: fail cases produce an explicit \texttt{[ERROR]} event, while pass cases are characterized by its absence.
This binary signal (presence vs.\ absence of an exception) is sufficient for near-perfect verdict prediction.

%% ============================================================
\section{Full Experimental Results}
\label{sec:full_results}

Tables~\ref{tab:full_qwen} and \ref{tab:full_deepseek} report the complete experimental results across all conditions, models, and seeds.

\begin{table}[t]
\centering
\caption{Full results for Qwen-2.5-Coder-7B across all conditions and seeds. Conditions with a single seed report no variance. \texttt{exception\_only} achieves 99.83\% across all three seeds ($\sigma{=}$0). \texttt{ae\_only} achieves 99.64\% mean ($\pm$0.49; seed 123 at 99.08\% is the outlier).}
\label{tab:full_qwen}
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{lcccc}
\toprule
\textbf{Condition} & \textbf{S42} & \textbf{S123} & \textbf{S456} & \textbf{Mean $\pm$ Std} \\
\midrule
exception\_only & 99.83 & 99.83 & 99.83 & 99.83 $\pm$ 0.00 \\
ae\_only        & 99.92 & 99.08 & 99.92 & 99.64 $\pm$ 0.49 \\
VOTA                     & 99.41 & ---   & ---   & --- \\
VOTA\_no\_ae    & 99.41 & ---   & ---   & --- \\
label\_only     & 86.22 & ---   & ---   & --- \\
loop\_only      & 85.63 & ---   & ---   & --- \\
full\_trace     & 81.76 & ---   & ---   & --- \\
no\_trace       & 75.13 & ---   & ---   & --- \\
\bottomrule
\end{tabular}%
}
\end{table}

\begin{table}[t]
\centering
\caption{Full results for DeepSeek-Coder-6.7B across all conditions and seeds. \texttt{exception\_only} shows bimodal seed behavior: seeds 42 and 456 achieve 99.33\%, while seed 123 yields 91.09\% (LoRA initialization outlier, fail recall = 70.5\%).}
\label{tab:full_deepseek}
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{llcc}
\toprule
\textbf{Condition} & \textbf{Seed} & \textbf{Accuracy} & \textbf{Notes} \\
\midrule
exception\_only & 42  & 99.33 & epoch 1: 99.83 \\
exception\_only & 456 & 99.33 & CI [98.82, 99.75] \\
exception\_only & 123 & 91.09 & fail recall = 70.5\%; CI [89.40, 92.60] \\
\midrule
VOTA                     & 42  & 84.45 & \\
no\_trace       & 42  & 73.36 & \\
full\_trace     & 42  & 79.16 & CI [76.80, 81.30] \\
\bottomrule
\end{tabular}%
}
\end{table}

%% ============================================================
\section{Tokenizer and Truncation Analysis}
\label{sec:tokenizer_analysis}

The VOTA cross-model gap (14.96pp, Table~\ref{tab:cross_model}; confounded by tokenizer-driven truncation; 91.7\% of DeepSeek training samples were affected) is driven by a training-time truncation asymmetry.
The DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus 1{,}929 for Qwen, causing 91.7\% of DeepSeek VOTA training samples to exceed the 2{,}048-token context window.
The training framework preserves the verdict label but truncates trace content, so the model trains with incomplete diagnostic information for the majority of samples.

A post-hoc group analysis provides directional evidence: partitioning DeepSeek VOTA test samples by whether their training-set counterparts exceeded the context window, intact samples ($N{=}99$) achieve 100\% accuracy while truncated samples ($N{=}1{,}091$) achieve 83.04\% (95\% CI [80.75\%, 85.24\%]; Fisher exact $p{<}0.001$), with all 185 errors concentrated in the fail class (fail recall = 31.23\%).
Per-class analysis (Table~\ref{tab:per_class}) confirms that DeepSeek VOTA achieves 100\% fail precision but only 45.43\% fail recall, systematically defaulting to \texttt{pass}---in contrast to Qwen VOTA, which achieves 100\% fail recall.

Seed robustness diverges across models: Qwen \texttt{exception\_only} produces identical 99.83\% across all three seeds ($\sigma{=}0$), while DeepSeek shows bimodal behavior: seeds 42 and 456 achieve 99.33\% (fail recall = 100\%), seed 123 yields 91.09\% (fail recall = 70.5\%).
Because \texttt{exception\_only} test inputs contain 48.99\% duplicates (607 unique of 1,190; \S\ref{sec:dataset}), CIs assume $n{=}1{,}190$ independent trials; under deduplication ($n{=}607$), Qwen's accuracy is 99.67\% (Wilson CI [98.81, 99.91]).

%% ============================================================
\section{Irreducible Sample Analysis}
\label{sec:irreducible}

The \texttt{exception\_only} condition with Qwen-2.5-Coder-7B misclassifies exactly 2 out of 1,190 test samples across all three seeds (42, 123, 456), with 100\% overlap across seeds.
Both samples (IDs 901 and 905) share the following characteristics:

\begin{itemize}
\item \textbf{Function:} \texttt{check\_dict\_case} (HumanEval/95)---a function that checks whether all dictionary keys are uniformly upper-case or lower-case strings.
\item \textbf{Ground-truth label:} \texttt{pass}.
\item \textbf{Predicted label:} \texttt{fail} (false negative).
\item \textbf{Cross-seed consistency:} Both samples are misclassified identically by all three seeds, indicating a systematic rather than stochastic error.
\end{itemize}

Manual inspection reveals the root cause: \texttt{check\_dict\_case} uses \texttt{all()} over a generator expression, and Python's \texttt{all()} short-circuits on the first \texttt{True} value, raising \texttt{GeneratorExit} to terminate the generator.
Because \texttt{GeneratorExit} is a \texttt{BaseException} subclass, the tracer records it as seven \texttt{[ERROR] GeneratorExit} lines---even though the function executes correctly and the test passes.
The model observes these spurious error markers and reasonably but incorrectly predicts \texttt{fail}.
This is not a model failure but a representation ambiguity: the \texttt{exception\_only} format cannot distinguish genuine exceptions from benign \texttt{BaseException} subclasses triggered by Python's iterator protocol.

Most configurations converge to these same 2 errors: Qwen-1.5B, Qwen-7B (3 seeds), CodeLlama-13B (seeds 42/456), and DeepSeek-6.7B (seeds 42/456) all produce error set $\{901, 905\}$.
However, CodeLlama-13B seed 123 achieves 100\% accuracy (0/1190 errors), correctly classifying both samples.
This demonstrates that 99.83\% is a near-perfect \emph{floor} (the convergence attractor for most LoRA initializations) rather than a hard data ceiling: the representation supports perfect accuracy, but most initializations converge to the same 2-error basin.
The practical implication is that these errors are high-probability convergence artifacts addressable through seed selection or ensemble methods, not fundamental limitations of the exception-based representation.

%% ============================================================
\section{Exception Type Accuracy Breakdown}
\label{sec:exception_type}

Table~\ref{tab:exception_type} reports \texttt{exception\_only} accuracy stratified by exception type on Qwen-2.5-7B (seed=42, $N{=}1{,}190$).
All standard exception types (\texttt{TypeError}, \texttt{ValueError}, \texttt{IndexError}, etc.) achieve 100\% accuracy.
The only misclassifications arise from \texttt{GeneratorExit}, a \texttt{BaseException} subclass that is not an \texttt{Exception}---it is raised by Python's iterator protocol during generator short-circuiting, not by actual program errors.

\begin{table}[t]
\centering
\caption{Exception type accuracy breakdown for \texttt{exception\_only} (Qwen-7B, seed=42). All true error types achieve 100\%. The only failures come from \texttt{GeneratorExit} (a \texttt{BaseException} subclass, not an \texttt{Exception}), which appears in 2 passing samples.}
\label{tab:exception_type}
\small
\begin{tabular}{lcc}
\toprule
\textbf{Exception Type} & \textbf{Samples} & \textbf{Accuracy} \\
\midrule
TypeError & 96 & 100\% \\
ValueError & 62 & 100\% \\
IndexError & 41 & 100\% \\
KeyError & 28 & 100\% \\
AttributeError & 19 & 100\% \\
AssertionError & 15 & 100\% \\
RecursionError & 12 & 100\% \\
Other Exception & 66 & 100\% \\
\midrule
GeneratorExit (BaseException) & 2 & 0\% \\
No exception (pass class) & 849 & 100\% \\
\bottomrule
\end{tabular}
\end{table}

This confirms that the model has learned a clean decision boundary: any true \texttt{Exception} subclass in the trace implies failure.
The \texttt{GeneratorExit} case represents a semantic ambiguity in the trace format rather than a model failure, as discussed in \S\ref{sec:irreducible}.

%% ============================================================
\section{Trace Length Ablation}
\label{sec:trace_length_full}

To test whether the \texttt{full\_trace} performance gap is caused by input truncation at training time, we vary the maximum trace token budget on Qwen-2.5-7B (seed=42) while keeping all other hyperparameters fixed.

\begin{table}[t]
\centering
\caption{Trace length and truncation direction ablation on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). Head = standard left-truncation (retain first $k$ tokens); Tail = retain last $k$ tokens. Per-condition bootstrap 95\% CIs ($B{=}10{,}000$).}
\label{tab:trace_length}
\small
\begin{tabular}{llcc}
\toprule
\textbf{Direction} & \textbf{Max Tokens} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
\midrule
Head & 256  & 78.82 & [76.4, 81.0] \\
Head & 512  & 80.42 & [78.2, 82.6] \\
Head & 1024 & 77.23 & [74.9, 79.6] \\
Head & no\_limit ($\infty$) & 81.76 & [79.7, 83.9] \\
\midrule
Tail & 256  & 77.48 & --- \\
Tail & 512  & 93.61 & --- \\
Tail & 1024 & 96.47 & --- \\
Tail & 2048 & 97.31 & --- \\
\bottomrule
\end{tabular}
\end{table}

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{budget_curve}
\caption{Accuracy as a function of token budget and truncation direction (Qwen-2.5-7B, $N{=}1{,}190$). Tail-truncation (keeping last $k$ tokens) monotonically improves beyond 256 tokens and consistently outperforms head-truncation by 13--19pp at budgets ${\geq}$512. The flat head-truncation curve (77--82\%) contrasts with the steep tail-truncation rise, confirming that diagnostic signal is localized near trace end. Dashed lines show \texttt{exception\_only} (99.83\%) and \texttt{no\_trace} (75.13\%) as upper and lower bounds. Tail-256 (${\approx}$ \texttt{no\_trace}) indicates the signal window begins approximately 256 tokens from the trace terminus.}
\label{fig:trace_length}
\end{figure}

As shown in Table~\ref{tab:trace_length} and Figure~\ref{fig:trace_length}, all four trace length conditions fall within a 5pp range (77.2\%--81.8\%).
To quantify the reliability of the observed differences, Table~\ref{tab:trace_length_pairwise} reports paired bootstrap comparisons ($B{=}10{,}000$, seed=42) across all condition pairs.

\begin{table}[t]
\centering
\caption{Pairwise paired bootstrap comparisons for trace length ablation ($B{=}10{,}000$, seed=42). $\Delta$ = accuracy difference between the two conditions (first $-$ second in the budget group; condition $-$ baseline in the other groups). **$p{<}0.01$; ***$p{<}0.001$.}
\label{tab:trace_length_pairwise}
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{llccc}
\toprule
& \textbf{Comparison} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} & \textbf{$p$-value} \\
\midrule
\multirow{4}{*}{\rotatebox{90}{\scriptsize Budget}}
& 512 vs.\ 256           & $+$1.60  & [$-$0.34, $+$3.53]   & 0.117 \\
& 1024 vs.\ 512          & $-$3.19  & [$-$5.29, $-$1.09]   & 0.002** \\
& no\_limit vs.\ 1024    & $+$4.54  & [$+$2.52, $+$6.55]   & ${<}$0.001*** \\
& no\_limit vs.\ 256     & $+$2.94  & [$+$0.84, $+$5.04]   & 0.006** \\
\midrule
\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ no\_trace}}
& 256 $-$ no\_trace       & $+$3.70  & [$+$1.43, $+$6.05]   & 0.002** \\
& 512 $-$ no\_trace       & $+$5.29  & [$+$3.03, $+$7.56]   & ${<}$0.001*** \\
& 1024 $-$ no\_trace      & $+$2.10  & [$-$0.17, $+$4.37]   & 0.078 \\
& no\_limit $-$ no\_trace & $+$6.64  & [$+$4.37, $+$8.99]   & ${<}$0.001*** \\
\midrule
\multirow{4}{*}{\rotatebox{90}{\scriptsize vs.\ exc.}}
& 256 $-$ exc\_only       & $-$21.01 & [$-$23.45, $-$18.74] & ${<}$0.001*** \\
& 512 $-$ exc\_only       & $-$19.41 & [$-$21.76, $-$17.14] & ${<}$0.001*** \\
& 1024 $-$ exc\_only      & $-$22.61 & [$-$25.04, $-$20.25] & ${<}$0.001*** \\
& no\_limit $-$ exc\_only & $-$18.07 & [$-$20.34, $-$15.88] & ${<}$0.001*** \\
\bottomrule
\end{tabular}%
}
\end{table}

\paragraph{Non-monotonic pattern.}
The trend across trace budgets is non-monotonic: 512 tokens (80.42\%) slightly outperforms 256 tokens (78.82\%), but doubling to 1024 tokens \emph{decreases} accuracy to 77.23\%---a statistically significant 3.19pp drop ($p{=}0.002$, 95\% CI [$-$5.29, $-$1.09]).
The no-limit condition (81.76\%) recovers and significantly exceeds 1024 tokens ($p{<}0.001$), but 1024 tokens is not significantly better than the \texttt{no\_trace} baseline (75.13\%; $\Delta{=}{+}2.10$pp, $p{=}0.078$, 95\% CI [$-$0.17, $+$4.37]).
This means that truncating traces to an intermediate length can be \emph{worse} than providing no trace at all---the 1024-token budget retains enough irrelevant content to mislead the model while discarding diagnostic events that might appear late in the trace.

\paragraph{Comparison to baselines.}
All four trace budget conditions significantly exceed \texttt{no\_trace} except 1024 tokens ($p{=}0.078$), confirming that raw trace content provides some signal but unreliably so.
The gap to \texttt{exception\_only} (99.83\%) is massive for every budget condition (18--23pp, all $p{<}0.001$), underscoring that even unlimited raw traces cannot substitute for targeted signal extraction.
The best full-trace condition (no\_limit, 81.76\%) still lags \texttt{exception\_only} by 18.07pp (95\% CI [$-$20.34, $-$15.88]).

\paragraph{Interpretation.}
These results rule out input truncation as the primary explanation for the full-trace performance gap: even with unlimited tokens, the model cannot extract the diagnostic signal that VOTA's targeted compression provides.
The non-monotonic dip at 1024 tokens is consistent with a ``worst-of-both-worlds'' regime where the model receives enough noisy context to dilute the signal but not enough to compensate through broader coverage.
The result reinforces the information density interpretation (\S\ref{sec:density}): the gap between full traces and VOTA is driven by the \emph{content} of the trace (irrelevant lines diluting the diagnostic signal), not its \emph{length}.
In contrast, VOTA's compressed representation concentrates the diagnostic signal into fewer tokens, making it sensitive to truncation when those tokens are removed (\S\ref{sec:cross_model}).

\paragraph{Truncation direction.}
Tail-truncation (retaining the last $k$ tokens) dramatically outperforms head-truncation: \texttt{tail\_2048} achieves 97.31\% vs.\ \texttt{head\_2048} (no\_limit) at 81.76\%, a 15.55pp improvement.
Even \texttt{tail\_512} (93.61\%) exceeds every head-truncation condition by over 11pp.

However, \texttt{tail\_256} (77.48\%) performs at the \texttt{no\_trace} baseline level (75.13\%), indicating that the diagnostic signal does not reside in the very last trace lines.
The critical jump occurs between 256 and 512 tail tokens (+16.13pp), localizing the signal window to approximately 256--512 tokens from the trace terminus.
This is consistent with Python's execution model: exception tracebacks and assertion comparisons appear near the end of the trace but are preceded by the final function call frames, placing them typically 300--500 tokens from the terminus rather than at the absolute end.

The 18.07pp gap from \texttt{full\_trace} to \texttt{exception\_only} decomposes as: 86\% positional concentration (recovered by tail-truncation at 2048 tokens) and 14\% residual content noise (the 2.52pp gap from \texttt{tail\_2048} to \texttt{exception\_only} that persists regardless of truncation direction).
The fact that \texttt{exception\_only} (99.83\%) still outperforms \texttt{tail\_2048} (97.31\%) confirms that semantic extraction (identifying the exception type and message) is superior to positional extraction (keeping a fixed window), because the model need not filter out non-diagnostic lines that happen to fall within the window.

\paragraph{Cross-model tail-truncation verification.}
Table~\ref{tab:tail_cross_model} extends the tail-2048 analysis to two additional models.
The positional concentration pattern generalizes: all three models achieve 94.96--97.90\% with \texttt{tail\_2048}, leaving residual gaps of only 1.93--4.37pp to \texttt{exception\_only}.
DeepSeek-6.7B shows the largest residual (4.37pp), consistent with its known sensitivity to long-context formatting (Appendix~\ref{sec:training_dynamics}); the diagnostic signal is present in the tail window but partially degraded by the model's weaker long-context processing.
Qwen-1.5B (97.90\%) performs comparably to Qwen-7B (97.31\%), confirming that positional signal extraction, like exception-based extraction, is signal-limited rather than capacity-limited.

\begin{table}[t]
\centering
\caption{Cross-model \texttt{tail\_2048} verification ($N{=}1{,}190$). Positional concentration of diagnostic signal holds across all tested models and architecture families.}
\label{tab:tail_cross_model}
\small
\begin{tabular}{lccc}
\toprule
\textbf{Model} & \textbf{Tail-2048 (\%)} & \textbf{exc\_only (\%)} & \textbf{Gap (pp)} \\
\midrule
Qwen-7B & 97.31 & 99.83 & 2.52 \\
Qwen-1.5B & 97.90 & 99.83 & 1.93 \\
DeepSeek-6.7B & 94.96 & 99.33 & 4.37 \\
\bottomrule
\end{tabular}
\end{table}

%% ============================================================
\section{Calibration Analysis}
\label{sec:calibration_full}

Beyond accuracy, we evaluate whether trace conditions affect prediction calibration, motivated by recent findings that code LLM confidence is often poorly calibrated \citep{spiess2025calibration}.

\begin{table}[t]
\centering
\caption{Calibration metrics on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). ECE = expected calibration error; Brier = Brier score. Lower is better for both.}
\label{tab:calibration}
\small
\begin{tabular}{lcc}
\toprule
\textbf{Condition} & \textbf{ECE $\downarrow$} & \textbf{Brier $\downarrow$} \\
\midrule
ae\_only & \textbf{0.0004} & \textbf{0.0008} \\
exception\_only & 0.0027 & 0.0013 \\
VOTA & 0.0054 & 0.005 \\
full\_trace & 0.096 & 0.144 \\
no\_trace & 0.171 & 0.197 \\
\bottomrule
\end{tabular}
\end{table}

Table~\ref{tab:calibration} shows that calibration quality mirrors the Tier~1/2 hierarchy.
Tier~1 conditions (\texttt{ae\_only}: ECE=0.0004; \texttt{exception\_only}: ECE=0.0027) produce near-perfectly calibrated predictions, while \texttt{full\_trace} (ECE=0.096) and \texttt{no\_trace} (ECE=0.171) exhibit substantial miscalibration.
VOTA (ECE=0.0054) is well-calibrated but slightly worse than either Tier~1 component alone, reinforcing the pattern that combining trace signals dilutes rather than improves the prediction signal.

The Brier scores tell a consistent story: \texttt{ae\_only} (0.0008) and \texttt{exception\_only} (0.0013) achieve near-zero scores, while \texttt{no\_trace} (0.197) indicates substantial miscalibration.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{fig2_calibration}
\caption{Reliability diagrams for four trace conditions on Qwen-2.5-7B ($N{=}1{,}190$, seed=42). \texttt{exception\_only} (ECE=0.0027) clusters near the diagonal, while \texttt{no\_trace} (ECE=0.171) exhibits systematic overconfidence, a 63$\times$ gap.}
\label{fig:calibration}
\end{figure}

%% ============================================================
\section{Error Overlap Analysis}
\label{sec:error_overlap}

We analyze the overlap between error sets of different conditions to determine whether they fail on the same samples (Figure~\ref{fig:error_overlap}).

\texttt{exception\_only}'s 2 errors (samples 901 and 905) have zero intersection with the error sets of all other conditions (Jaccard = 0.000 in all pairwise comparisons).
This orthogonality arises because \texttt{exception\_only} errors are caused by \texttt{GeneratorExit} false positives (pass samples misclassified as fail due to benign \texttt{BaseException} events), while errors from other conditions are predominantly fail samples misclassified as pass due to insufficient signal.

Among non-exception conditions, error sets exhibit hierarchical containment: \texttt{ae\_only} $\subset$ VOTA $\subset$ \texttt{loop\_only} $\subset$ \texttt{no\_trace}, with pairwise Jaccard indices increasing with signal overlap.
\texttt{loop\_only} and \texttt{full\_trace} share the highest overlap (Jaccard ${\sim}$0.65), reflecting their shared reliance on behavioral patterns rather than explicit fault indicators.

This analysis confirms that \texttt{exception\_only} operates on an independent signal dimension: its errors are representation ambiguities (iterator protocol artifacts) rather than information deficits, explaining why combining it with other signals cannot eliminate these specific errors.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{error_overlap}
\caption{Jaccard similarity between error sets of different conditions (Qwen-7B, seed=42, $N{=}1{,}190$). \texttt{exception\_only} (exc\_only) has zero overlap with all other conditions, confirming it operates on an independent signal dimension.}
\label{fig:error_overlap}
\end{figure}

%% ============================================================
\section{Cross-Dataset Generalization: DebugBench}
\label{sec:debugbench_full}

To test whether exception-based verdict prediction generalizes beyond LLM-generated solutions, we evaluate on DebugBench \citep{tian2024debugbench}---a dataset of human-written programs with synthetically injected bugs (single-point mutations such as operator replacement, variable misuse, and missing statements).
After filtering for executable Python samples with valid traces, we retain 426 samples with a near-balanced class distribution (majority baseline: 51.4\%).

\begin{table}[t]
\centering
\caption{Generalization to DebugBench ($N{=}426$, Qwen-2.5-7B, seed=42). Wilson 95\% CIs. The component ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is preserved, and exception\_only achieves perfect accuracy.}
\label{tab:debugbench}
\small
\begin{tabular}{lcc}
\toprule
\textbf{Condition} & \textbf{Acc (\%)} & \textbf{95\% CI} \\
\midrule
exception\_only & \textbf{100.00} & [99.14, 100.00] \\
VOTA & 99.77 & [99.30, 100.00] \\
no\_trace & 96.71 & [94.80, 98.40] \\
\midrule
Majority baseline & 51.41 & --- \\
\bottomrule
\end{tabular}
\end{table}

Table~\ref{tab:debugbench} shows that the component ranking from the main experiments is preserved: \texttt{exception\_only} (100.00\%) $\geq$ VOTA (99.77\%) $>$ \texttt{no\_trace} (96.71\%).
The \texttt{exception\_only} condition achieves perfect accuracy, confirming that the exception-based representation generalizes to a different fault distribution without degradation.

The absolute margins are much narrower than on the main dataset: the \texttt{no\_trace} baseline already achieves 96.71\%---compared to 75.13\% on HumanEval+MBPP---leaving only 3.29pp of headroom for trace-based improvement.
This ceiling effect reflects a fundamental difference in fault characteristics: DebugBench bugs are synthetically injected single-point mutations, which produce code that is structurally dissimilar from the original correct solution; a model can often identify the fault from source code alone.
In contrast, the HumanEval+MBPP solutions are LLM-generated, producing natural errors (logic mistakes, edge-case failures) where the faulty and correct solutions may be structurally similar, making code-only verdict prediction substantially harder.

These results support exception-based verdict prediction as a generalizable approach---the method does not degrade on an out-of-distribution dataset, and the exception dominance ranking (exception\_only $\geq$ VOTA $>$ no\_trace) is consistent across both datasets---but the narrow DebugBench margins are insufficient to independently validate trace importance.
The 24.70pp trace lift on the main dataset (no\_trace 75.13\% $\to$ exception\_only 99.83\%) remains the primary evidence for the value of exception-based trace signals.

%% ============================================================
\section{Cross-Model Robustness Analysis}
\label{sec:robustness_analysis}

The cross-model gap pattern (Table~\ref{tab:cross_model}) suggests a design principle: \emph{trace representations should match the model capability floor, not the ceiling.}
Exception events are consistently the most effective component on both models, and their structural simplicity---a fixed-format error message---ensures that the relative advantage over richer representations holds across all seeds.
Two of three DeepSeek seeds match Qwen-level accuracy (99.33\%); the outlier (seed 123, 91.09\%) we hypothesize reflects LoRA initialization sensitivity landing in a suboptimal basin (fail recall = 70.5\%, though direct evidence is lacking), not a failure of the exception signal itself---even this outlier outperforms VOTA (84.45\%) by 6.64pp.
The VOTA cross-model gap is confounded by two factors: (1)~tokenizer efficiency---the DeepSeek tokenizer averages 2{,}626 tokens per VOTA sample versus Qwen's 1{,}929, causing 91.7\% of training samples to exceed the 2{,}048-token context window; content-aware truncation preferentially removes the terminal structured prompt, preserving the verdict label but truncating trace content---and (2)~base model capability differences, consistent with findings that SFT generalization depends on pretrain quality \citep{yang2024generalization}.
The two factors cannot be disentangled in the current experimental design.
Our \texttt{exception\_only} design sidesteps the truncation confound entirely: inputs have a median of 150 tokens (mean 398), well below the 2{,}048-token context window, so no training samples are truncated on either model.
The resulting 0.56pp cross-model gap (Table~\ref{tab:cross_model}) is therefore a clean measure of model capability differences, making the ``capability floor'' principle directly testable.
The practical implication is that trace-based systems should default to the simplest sufficient signal; for smaller models, training stability (multi-seed selection, warmup schedules) is a secondary but addressable concern.

%% ============================================================
\section{Training Dynamics and Loss Decoupling}
\label{sec:training_dynamics}

The DeepSeek \texttt{exception\_only} results reveal two instructive training dynamics.
First, epoch-level analysis shows mild degradation in 2/3 seeds: seed 42 peaks at 99.83\% after epoch~1 but settles at 99.33\% by epoch~3 ($-$0.50pp), seed 123 degrades from 91.43\% to 91.09\% ($-$0.34pp), while seed 456 shows no epoch degradation (99.33\% at both epoch~1 and epoch~3).
Early stopping may yield marginal gains for some seeds, but the epoch effect is small (${\leq}$0.5pp) compared to the seed effect (8.24pp between seeds 42 and 123).

Second, seeds 123 and 456 converge to nearly identical final training losses (0.122 and 0.123 respectively), yet their accuracies differ by 8.24pp (91.09\% vs.\ 99.33\%).
The critical difference lies in fail recall: seeds 42 and 456 achieve 100\%, while seed 123 achieves only 70.5\%---the LoRA initialization in seed 123 fails to learn the exception$\to$fail mapping for a substantial fraction of failing samples, even though the per-token loss appears converged.
This demonstrates that token-level training loss can mask fundamental differences in sample-level classification ability, suggesting a parallel to the eval-loss/accuracy decoupling observed in DeepSeek VOTA (where eval loss rose 65\% from epoch 1 to 3 while accuracy improved by 6.3pp) at the training phase.
The practical recommendation is twofold: (1)~use task-specific metrics (accuracy, fail recall) for checkpoint and seed selection rather than training or evaluation loss, and (2)~for deployment on smaller models, train multiple seeds and select the best, as a single run may not reliably converge to the correct classification boundary.

\paragraph{Format collapse, not semantic failure.}
The 100 errors of seed 123 are not semantic failures but generation format collapse: on inputs exceeding 4,000 characters (those containing verbose locals dumps), the model echoes trace content instead of emitting a verdict token, while achieving zero errors on shorter inputs.
This indicates that the LoRA initialization of seed 123 specifically compromises long-context format compliance rather than exception signal comprehension, further supporting the robustness advantage of compact \texttt{exception\_only} inputs.

The contrast with VOTA is instructive: DeepSeek VOTA accuracy monotonically increases from 78.15\% to 84.45\% across epochs, but is consistent with a performance limit associated with the high trace truncation rate (\S\ref{sec:cross_model})---the model progressively extracts signal from samples with intact trace content but cannot fully compensate for the information loss in the truncated majority.
The 84.45\% accuracy reflects a combination of trace information loss and model capability constraints.

%% ============================================================
\section{Deduplication Statistics}
\label{sec:dedup_stats}

Table~\ref{tab:dedup} reports the duplication rates across trace formats.
Because multiple passing solutions to the same problem produce identical (input, output) pairs in the \texttt{exception\_only} format---correct executions raise no exceptions, so the trace content is the same regardless of the solution's internal logic---the dataset contains duplicate rows.
Train--test input overlap is zero (split by problem ID), so no information leakage occurs.
The high duplication in \texttt{exception\_only} does not affect our experimental conclusions: after deduplication the training set still contains 2,858 unique samples and the test set 607, providing sufficient coverage for the 591-problem benchmark.
The \texttt{exception\_only} test set contains 48.99\% duplicate inputs due to representation compactness; all confidence intervals treat samples as independent Bernoulli trials.

\begin{table}[t]
\centering
\caption{Deduplication statistics. The \texttt{exception\_only} format collapses multiple passing solutions into identical rows because correct executions produce no exception events. Train--test input overlap is 0 (no leakage).}
\label{tab:dedup}
\small
\begin{tabular}{lccc}
\toprule
\textbf{Split} & \textbf{Total} & \textbf{Unique} & \textbf{Dup.\ rate} \\
\midrule
exception\_only train & 4{,}720 & 2{,}858 & 39.45\% \\
exception\_only test  & 1{,}190 &   607 & 48.99\% \\
raw\_traces (full)    & 5{,}910 & 5{,}803 &  1.81\% \\
\bottomrule
\end{tabular}
\end{table}

%% ============================================================
\section{Regex Baseline Analysis}
\label{sec:regex_baselines}

To establish a non-learning upper bound, we evaluate six regex-based baselines on the \texttt{exception\_only} test set ($N{=}1{,}190$) and two format-specific baselines on VOTA and \texttt{full\_trace} inputs.

\begin{table}[t]
\centering
\caption{Regex baseline accuracy ($N{=}1{,}190$). B4 is the strongest semantic baseline (6.22pp below SFT \texttt{exception\_only}, McNemar $p{<}0.001$). B6 uses an error count threshold. $^\ddag$B5 exploits a data formatting artifact: the \texttt{[No exception data in trace]} marker is deterministically present in all pass samples, making this a format-level shortcut rather than a genuine exception-based heuristic.}
\label{tab:regex}
\small
\begin{tabular}{llc}
\toprule
\textbf{Baseline} & \textbf{Method} & \textbf{Acc (\%)} \\
\midrule
B1: \texttt{[ERROR]} presence & string match & 93.45 \\
B2: Traceback presence & string match & 71.51 \\
B3: Any keyword & union of B1+B2+Exception & 93.45 \\
B4: Exception type regex & regex on exception class names & \textbf{93.61} \\
B5: Format marker & \texttt{[No exception data]} $\to$ pass & 99.33$^\ddag$ \\
B6: Error count $\geq$2 & count threshold & 92.02 \\
\midrule
VOTA format regex & best regex on VOTA traces & 75.55 \\
full\_trace format regex & best regex on full traces & 77.39 \\
\bottomrule
\end{tabular}
\end{table}

The strongest legitimate baseline (B4, 93.61\%) applies regex pattern-matching on Python exception class names (e.g., \texttt{ValueError}, \texttt{TypeError}).
Its errors concentrate on 8 boundary samples where a \texttt{ValueError} is raised inside a \texttt{try/except} block and caught---the program passes despite an exception occurring in the trace.
SFT \texttt{exception\_only} correctly classifies 6 of these 8 samples, indicating that the model learns the semantic distinction between caught (benign) and uncaught (fault-indicating) exceptions.
B5 (99.33\%) achieves near-SFT accuracy but relies on the deterministic presence of a format marker in pass-class traces, which is an artifact of the trace preprocessing pipeline rather than a generalizable signal; McNemar test vs.\ SFT yields $p{=}0.041$, confirming a statistically significant difference.

\paragraph{Cross-format comparison.}
Table~\ref{tab:regex_cross_format} compares SFT and the best applicable regex baseline for each trace format.
The SFT advantage increases with format complexity: \texttt{no\_trace} (+3.62pp over majority baseline) $<$ \texttt{full\_trace} (+4.37pp) $<$ \texttt{exception\_only} (+6.22pp) $\ll$ VOTA (+23.86pp).
The VOTA gap is largest because its structured multi-component format carries semantic content that regex cannot parse, while \texttt{exception\_only}'s simpler format allows regex to capture most of the signal.

\begin{table}[t]
\centering
\caption{SFT vs.\ best regex baseline by trace format ($N{=}1{,}190$). Regex baselines: majority class for \texttt{no\_trace}, keyword matching for \texttt{full\_trace}, pattern matching for VOTA, exception type regex (B4) for \texttt{exception\_only}.}
\label{tab:regex_cross_format}
\small
\begin{tabular}{lccc}
\toprule
\textbf{Format} & \textbf{SFT (\%)} & \textbf{Regex (\%)} & \textbf{$\Delta$ (pp)} \\
\midrule
exception\_only & 99.83 & 93.61 & +6.22 \\
VOTA & 99.41 & 75.55 & +23.86 \\
full\_trace & 81.76 & 77.39 & +4.37 \\
no\_trace & 75.13 & 71.51 & +3.62 \\
\bottomrule
\end{tabular}
\end{table}

%% ============================================================
\section{Cross-Model Zero-Shot Comparison}
\label{sec:zeroshot_cross_model}

Table~\ref{tab:zeroshot_cross_model} compares zero-shot and SFT \texttt{exception\_only} accuracy across four models.
Zero-shot performance does not correlate with model size: the smallest model (Qwen-1.5B, 93.45\%) outperforms all larger models, while the largest (CodeLlama-13B) falls below majority baseline.
SFT compresses the 42.44pp zero-shot range to 0.56pp, eliminating architecture-dependent variance.

\begin{table}[t]
\centering
\caption{Zero-shot vs.\ SFT \texttt{exception\_only} across four models ($N{=}1{,}190$). Zero-shot accuracy is uncorrelated with model size; SFT normalizes cross-architecture variance from 42.44pp to 0.56pp.}
\label{tab:zeroshot_cross_model}
\small
\begin{tabular}{llccc}
\toprule
\textbf{Model} & \textbf{Size} & \textbf{Zero-shot (\%)} & \textbf{SFT (\%)} & \textbf{$\Delta$ (pp)} \\
\midrule
Qwen-1.5B & 1.5B & 93.45 & 99.83 & +6.38 \\
DeepSeek-6.7B & 6.7B & 90.59 & 99.33 & +8.74 \\
Qwen-7B & 7B & 89.08 & 99.83 & +10.75 \\
CodeLlama-13B & 13B & 51.01 & 99.89 & +48.88 \\
\midrule
Range & --- & 42.44pp & 0.56pp & --- \\
\bottomrule
\end{tabular}
\end{table}
```

---

## File 9: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/arr_checklist.tex`

```latex
\documentclass[11pt,a4paper]{article}
\usepackage[review]{acl}
\usepackage{times,latexsym}
\usepackage{booktabs}

\title{ARR Reproducibility Checklist\\(Supplementary Material)}
\author{Anonymous ACL submission}

\begin{document}
\maketitle

\section*{Responsible NLP Research Checklist}

\subsection*{A. Limitations and Risks}

\begin{enumerate}
\item \textbf{Did you discuss the limitations of your work?} \\
\textit{Yes.} A dedicated Limitations section discusses: single-dataset scope, single model scale (7B), seed-dependent variance on DeepSeek, the invalidated full\_trace run, generator--evaluator overlap, and task scope limited to verdict prediction.

\item \textbf{Did you discuss any potential risks of your work?} \\
\textit{Yes.} The Ethics Statement notes that the work uses public benchmarks, involves no human subjects, and has minimal environmental impact. Verdict prediction is a developer-facing tool with no direct end-user impact.
\end{enumerate}

\subsection*{B. Did you use or create scientific artifacts?}

\begin{enumerate}
\item \textbf{Did you cite the creators of artifacts you used?} \\
\textit{Yes.} HumanEval \cite{chen2021evaluating}, MBPP-sanitized \cite{austin2021program}, DebugBench \cite{tian2024debugbench}, Qwen-2.5-Coder-7B/1.5B-Instruct \cite{qwen2025coder}, CodeLlama-13B-Instruct \cite{roziere2024code}, DeepSeek-Coder-6.7B-Instruct \cite{deepseek2024coder}, LoRA \cite{hu2022lora}, and TRL SFTTrainer are all cited.

\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?} \\
\textit{Partial.} All base models and datasets are publicly available. HumanEval is released under MIT license; MBPP under CC-BY-4.0; DebugBench under MIT. Model licenses: Qwen-2.5-Coder under Apache 2.0; DeepSeek-Coder under the DeepSeek License.

\item \textbf{Did you discuss if your use of existing artifacts was consistent with their intended use?} \\
\textit{Yes.} HumanEval and MBPP are standard code generation benchmarks; we use their canonical test cases for verdict evaluation, consistent with their evaluation purpose. DebugBench is designed for debugging evaluation.

\item \textbf{Did you discuss the steps taken to check whether the data contains any information that names or uniquely identifies individual people or offensive content?} \\
\textit{N/A.} All datasets contain only programming problems and solutions with no personal information.
\end{enumerate}

\subsection*{C. Computational Experiments}

\begin{enumerate}
\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?} \\
\textit{Yes.}
\begin{itemize}
\item Models: Qwen-2.5-Coder-7B/1.5B-Instruct (7B/1.5B parameters), CodeLlama-13B-Instruct (13B parameters), DeepSeek-Coder-6.7B-Instruct (6.7B parameters). Only LoRA adapters are trained (rank=16, $\alpha$=32, targeting all linear layers).
\item Hardware: 2$\times$ RTX PRO 6000 Blackwell (${\sim}$96\,GB VRAM each); each experiment uses a single GPU.
\item Total compute: ${\sim}$50 GPU-hours across all conditions, models, and seeds. Per-condition training time ranges from 0.5h (no\_trace) to 4.0h (CodeLlama VOTA). See Appendix~B for per-condition wall-clock times.
\end{itemize}

\item \textbf{Did you report all hyperparameters?} \\
\textit{Yes.} Appendix~B (Table~5) reports: LoRA rank (16), alpha (32), dropout (0.05), target modules (all linear layers), epochs (3), per-device batch size (4), gradient accumulation steps (8), effective batch size (32), learning rate ($2 \times 10^{-4}$), LR scheduler (linear decay), warmup ratio (0.1), weight decay (0.01), max sequence length (2,048 tokens).

\item \textbf{Did you report descriptive statistics about your results?} \\
\textit{Yes.} All accuracy values include Wilson 95\% confidence intervals. Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42) with reported $p$-values. We report multi-seed results (seeds 42, 123, 456) for the exception\_only condition; other conditions report single-seed results. Standard deviations are provided where multiple seeds are available.

\item \textbf{If you used existing packages, did you report the implementation, model, and their versions?} \\
\textit{Yes.} HuggingFace TRL SFTTrainer with LoRA via PEFT. Base model identifiers: \texttt{Qwen/Qwen2.5-Coder-7B-Instruct} and \texttt{deepseek-ai/deepseek-coder-6.7b-instruct}.
\end{enumerate}

\subsection*{D. Human Annotations}

\begin{enumerate}
\item \textbf{Did you use human annotators?} \\
\textit{No.} All labels (pass/fail) are derived from automated test execution. No human annotation was involved.
\end{enumerate}

\subsection*{E. Data and Code Availability}

\begin{itemize}
\item \textbf{Code}: Training, evaluation, and trace preprocessing scripts will be released upon acceptance.
\item \textbf{Data}: Execution traces, VOTA-compressed traces, and train/test splits will be released. Raw traces are generated deterministically from publicly available benchmarks using Python \texttt{sys.settrace}.
\item \textbf{Models}: LoRA adapters for all conditions will be released on HuggingFace.
\end{itemize}

\subsection*{F. Reproducibility Summary}

\begin{table}[h]
\centering
\small
\begin{tabular}{lc}
\toprule
\textbf{Item} & \textbf{Status} \\
\midrule
All hyperparameters reported & Yes \\
Random seeds specified & Yes (42, 123, 456) \\
Error bars / CIs reported & Yes (Wilson 95\% CI) \\
Statistical tests reported & Yes (bootstrap, McNemar) \\
Computing infrastructure reported & Yes \\
Training time reported & Yes \\
Code release planned & Yes \\
Data release planned & Yes \\
Model release planned & Yes \\
\bottomrule
\end{tabular}
\end{table}

\bibliography{references}

\end{document}
```

---

All 9 files have been returned in their entirety. Also note that there is a `references.bib` file referenced but not requested. The paper's figures are sourced from `../../figures/paper/` relative to the tex files. The ARR checklist (`arr_checklist.tex`) is a standalone document (separate `\documentclass`) rather than being included in the main paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "354422f1-c1d0-441a-b040-194136aa45a6",
  "isSidechain": true,
  "agentId": "aef8cf76137435b1d",
  "requestId": "req_011Cb8b3t18PKc3vnuxMCZzp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df4880f3-a5bb-4a56-a2c7-523e2528ad88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/review_reviewer_2_6e2b3343",
  "sessionId": "c480cfc9-2d05-4df2-a2f7-f3f40e1784c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PG1goEZyQkKwxreyZxySTC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31746,
      "cache_read_input_tokens": 18528,
      "output_tokens": 28112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 31746
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 28112,
          "cache_read_input_tokens": 18528,
          "cache_creation_input_tokens": 31746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 31746,
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
